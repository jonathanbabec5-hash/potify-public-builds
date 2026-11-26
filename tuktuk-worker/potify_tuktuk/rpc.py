"""Read finalized Solana RPC data. Only read methods are exposed."""
import json
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .decode import PROGRAM, decode

MAINNET = "5eykt4UsFv8P8NJdTREpY1vzqKqZKvdpKuc147dw2N9d"


class ReadError(RuntimeError):
    pass


class Client:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def call(self, method, params):
        body = json.dumps(dict(jsonrpc="2.0", id=1, method=method, params=params)).encode()
        request = Request(self.endpoint, data=body, headers={"Content-Type": "application/json"})
        for attempt in range(3):
            wait = 2 ** attempt
            try:
                with urlopen(request, timeout=20) as response:
                    data = json.load(response)
                if "error" in data:
                    code = data["error"].get("code")
                    if code not in (429, -32005):
                        raise ReadError(f"{method}: RPC error {code}")
                else:
                    return data["result"]
            except HTTPError as exc:
                if exc.code != 429 and exc.code < 500:
                    raise ReadError(f"{method}: HTTP {exc.code}") from None
                retry = exc.headers.get("Retry-After", "")
                if retry.isdigit():
                    wait = min(30, max(wait, int(retry)))
            except (URLError, TimeoutError, OSError):
                pass
            if attempt < 2:
                time.sleep(wait)
        raise ReadError(f"{method} unavailable after 3 tries")

    def mainnet(self):
        if self.call("getGenesisHash", []) != MAINNET:
            raise ReadError("The endpoint did not report Solana mainnet-beta")

    def page(self, limit, before=None):
        options = dict(limit=limit, commitment="finalized")
        if before:
            options["before"] = before
        return self.call("getSignaturesForAddress", [PROGRAM, options])

    def transaction(self, signature):
        return self.call("getTransaction", [signature, dict(commitment="finalized",
                         encoding="json", maxSupportedTransactionVersion=0)])


def collect(client, signatures, pause):
    rows = []
    for index, signature in enumerate(dict.fromkeys(signatures)):
        if index and pause:
            time.sleep(pause)
        try:
            rows.append(decode(signature, client.transaction(signature)))
        except (ReadError, IndexError, KeyError, ValueError, TypeError) as exc:
            print(f"{signature}: {type(exc).__name__}", file=sys.stderr)
            rows.append(dict(signature=signature, status="unavailable"))
    return rows
