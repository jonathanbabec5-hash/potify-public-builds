"""Chronologically stratified sample of finalized signatures for the program."""
from random import Random

from .rpc import ReadError


def select_window(client, hours, size, seed):
    before, cutoff, end = None, None, None
    eligible, seen = [], set()
    # Limit a scan to 100k signatures to bound an operator's RPC usage.
    for _ in range(100):
        page = client.page(1000, before)
        if not page:
            raise ReadError("RPC history ended before the requested window was covered")
        times = [row.get("blockTime") for row in page]
        if None in times:
            raise ReadError("Missing block time prevents a complete window count")
        if end is None:
            end = times[0]
            cutoff = end - hours * 3600
        for row in page:
            sig = row["signature"]
            if sig in seen:
                raise ReadError("Overlapping RPC pages; retry on a stable endpoint")
            seen.add(sig)
            if cutoff < row["blockTime"] <= end:
                eligible.append(sig)
        before = page[-1]["signature"]
        # A cushion accommodates small clock reversals at nearby slots.
        if times[-1] < cutoff - 60:
            break
    else:
        raise ReadError("Window exceeds 100 RPC pages; use fewer hours")
    count = min(size, len(eligible))
    rng = Random(seed)
    chosen = [eligible[rng.randrange(i * len(eligible) // count, (i + 1) * len(eligible) // count)]
              for i in range(count)]
    plan = dict(method="one seeded draw per equal-count chronological stratum",
                start_exclusive=cutoff, end_inclusive=end, program_signatures=len(eligible),
                newest_signature=eligible[0], oldest_signature=eligible[-1],
                seed=seed, sample_size=count)
    return chosen, plan
