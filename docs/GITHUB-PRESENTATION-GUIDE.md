# Making POTIFY repositories easier to explore

Seed → Soil → Solana. A visitor should understand what a project is, where to start, and how to take part without knowing the whole ecosystem first.

## Patterns studied

These are documentation references, not endorsements or claims that POTIFY implements their features.

| Repository | What its presentation does well | POTIFY application |
| --- | --- | --- |
| [Anza Wallet Adapter](https://github.com/anza-xyz/wallet-adapter) | A one-sentence purpose and separate routes for app developers, wallet developers, packages and FAQs. | Put a concise project purpose and audience-specific paths near the top. |
| [Solana Tools](https://github.com/solana-developers/solana-tools) | A compact catalog pairs each tool with its function, tags and repository; separates available work from work in development. | Group the ecosystem by visitor interest and describe each destination's scope. |
| [Solana Payments App](https://github.com/solana-labs/solana-payments-app) | Prominent documentation and walkthrough links lead into prerequisites, quick start and local simulation. This reference repository is archived. | Make simulation, source and verification separate destinations; state prerequisites without implying production settlement. |
| [OpenAcre](https://github.com/OpenAcre-Project/OpenAcre) | An agricultural life sim uses a clear concept, features, setup, architecture links and distinct licensing information. | Connect the game to its design record, explain what is playable and preserve artwork rights. |
| [2D Farming Game](https://github.com/wkoziel/2D-Farming-Game) | A farming-game README puts its gameplay, setup, visual examples and project status in separate sections. | Help players find how to try the baseline while separating it from concepts and review branches. |

## README structure

1. Give the project a plain-language purpose and identify its present scope.
2. Show an **interest → starting point → useful action** table with links to existing files or sections.
3. Preserve the project's story, setup, tests, source history and rights.
4. Point to related public repositories, naming relationships carefully. A related idea is not necessarily an integration.
5. Date or qualify evidence. Local tests are not a production release, wallet certification or payment settlement.
6. Use compact diagrams when they clarify a relationship; give all key information in text for mobile and accessibility.

## Practical maintenance

- Link to the default branch for a general entry point; pin a commit when a statement depends on that exact revision.
- Verify linked paths exist and check whether the repository is public before adding it to a public README.
- Describe original assets and third-party material with their actual terms; do not add a license or claim permission without evidence.
- Keep public examples synthetic and free of personal data, credentials and private source.
- Add screenshots only when they are genuine, current and have appropriate rights. Give images useful alt text.
- Prefer one meaningful first task to a long list of generic “contribute” invitations.

## Current priorities

The catalog routes visitors across the ecosystem. Project-level entry points should next cover the game and world bible, growing tools, reading and film, identity and the Greenhouse, wallet and payment examples, and editorial workflows. Later passes should check every public repository for an accurate status, runnable entry point and contribution path.
