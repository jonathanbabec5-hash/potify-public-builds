# The POTIFY project field guide

**Seed → Soil → Solana.** Start anywhere. Each chapter tells you why a project exists, opens the actual source behind one detail and offers a first contribution. The links point to public revisions inspected on November 25 and 26, 2026. A published source file proves that file exists. Tests, reader responses and live services each need their own evidence.

1. [Keep a field note](#keep-a-field-note)
2. [Build a neighborhood](#build-a-neighborhood)
3. [Read, listen and watch](#read-listen-and-watch)
4. [Check a Solana claim](#check-a-solana-claim)
5. [Study a fictional checkout](#study-a-fictional-checkout)
6. [Find the right doorway](#find-the-right-doorway)
7. [Make editorial work checkable](#make-editorial-work-checkable)
8. [Inspect work on Solana](#inspect-work-on-solana)

## Keep a field note

### Plant Doctor

**What does a yellow leaf leave out?**

A yellow leaf is a good reason to look closer. On its own it tells a grower remarkably little. Plant Doctor gives the question back to the person standing beside the pot: what else can you actually observe? That small pause is the point of the tool.

Start with the [ranking rules](https://github.com/jonathanbabec5-hash/potify-plant-doctor/blob/63488a0679ccf250bb6dc1ed6ed9f209e3ba8e28/src/diagnosis.ts) and the [regression fixtures](https://github.com/jonathanbabec5-hash/potify-plant-doctor/blob/63488a0679ccf250bb6dc1ed6ed9f209e3ba8e28/tests/plant-doctor.test.mjs). The standalone app has 37 authored care profiles. The separate website library has 313 condition records; adding the two numbers together would tell you nothing about diagnostic accuracy.

Keep a fictional plant, its stage and its symptoms fixed. Change only the moisture observation from unknown to stays-wet. Record the top suggestion and its next check before and after, even if they stay the same. A small fixture with an explanation is more useful than a photo of someone’s grow.

The [Original Replit application](https://github.com/jonathanbabec5-hash/potify-plant-doctor/tree/ed16e3d730bc6f91935e8e8d0756c864d28c589e/replit-source/plant-doctor/) now builds outside Replit with its restored original hero artwork. The key-free status route reports 46 causes and 9 interactions. These belong to a separate implementation from the 37 authored standalone profiles and the 313 website condition records.

[Repository](https://github.com/jonathanbabec5-hash/potify-plant-doctor/tree/ed16e3d730bc6f91935e8e8d0756c864d28c589e) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-plant-doctor/archive/ed16e3d730bc6f91935e8e8d0756c864d28c589e.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-plant-doctor/blob/ed16e3d730bc6f91935e8e8d0756c864d28c589e/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-plant-doctor/blob/ed16e3d730bc6f91935e8e8d0756c864d28c589e/docs/BUILD-LOG.md)

### Plant Health Journal

**Can tomorrow’s grower find yesterday’s note?**

A timeline earns its place when someone can come back to a note and remember exactly what they saw before they changed anything. Plant Health Journal keeps observations, feeding and forecasts in different views so a prediction does not quietly become part of the plant’s history.

Look at the [device storage layer](https://github.com/jonathanbabec5-hash/potify-plant-health/blob/de6a583235833c3ba4dd9d50117d2888e46ffcda/app/storage.js) beside the [workspace model](https://github.com/jonathanbabec5-hash/potify-plant-health/blob/de6a583235833c3ba4dd9d50117d2888e46ffcda/app/model.js). IndexedDB keeps the local workspace in the browser. Reloading the same profile and recovering a record on a new phone are two different promises; only the first belongs in this small check.

Create a fictional plant, add one dated observation and reload. Record whether the exact note returns under the right plant. Keep personal grow histories off GitHub. If portability matters, describe the export-and-restore check that would convince you before relying on it.

[Repository](https://github.com/jonathanbabec5-hash/potify-plant-health/tree/de6a583235833c3ba4dd9d50117d2888e46ffcda) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-plant-health/archive/de6a583235833c3ba4dd9d50117d2888e46ffcda.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-plant-health/blob/de6a583235833c3ba4dd9d50117d2888e46ffcda/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-plant-health/blob/de6a583235833c3ba4dd9d50117d2888e46ffcda/docs/BUILD-LOG.md)

### Soil Biology Weekly

**A Friday note worth revisiting next Friday**

The best soil question is often small enough to come back to. A keeper can record how a bed looked after watering, then discover a week later that their first explanation was too simple. Good field writing leaves room for that second observation.

The [issue worksheet](https://github.com/jonathanbabec5-hash/potify-soil-biology-weekly/blob/7841736c1a74cb8db78f820d3abd84a4723494b4/examples/issue.json) separates the question, dated observation and source. The [renderer](https://github.com/jonathanbabec5-hash/potify-soil-biology-weekly/blob/7841736c1a74cb8db78f820d3abd84a4723494b4/src/render.py) turns that structure into a readable brief. This is the editorial kit; a filled-in template is not evidence of a published issue or a measured change in the soil.

Take a fictional field note and underline the part another person could actually see. Put the interpretation on a separate line and name the next observation that could change it. A useful edit fixes one sentence and explains why.

[Repository](https://github.com/jonathanbabec5-hash/potify-soil-biology-weekly/tree/7841736c1a74cb8db78f820d3abd84a4723494b4) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-soil-biology-weekly/archive/7841736c1a74cb8db78f820d3abd84a4723494b4.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-soil-biology-weekly/blob/7841736c1a74cb8db78f820d3abd84a4723494b4/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-soil-biology-weekly/blob/7841736c1a74cb8db78f820d3abd84a4723494b4/docs/BUILD-LOG.md)

### Field Card 01

**The crease is part of the interface**

Field Card 01 has to work away from the screen, where a fold can hide a label and the back of the page matters as much as the front. Its best usability test is a sheet of paper, not another screenshot of the download button.

The [printable card](https://github.com/jonathanbabec5-hash/potify-field-card/blob/26e4e3a7cd5b7bc28babc026d202fbb4040ed57f/public/field/01/assets/Field_Card_01.pdf) and its [reading companion](https://github.com/jonathanbabec5-hash/potify-field-card/blob/26e4e3a7cd5b7bc28babc026d202fbb4040ed57f/public/field/01/card.html) carry the same small publication into two settings. An HTTP delivery tells us a file arrived. It cannot tell us whether the type survived the fold.

If you already have a print, note the paper size, side orientation and first line that becomes hard to read when folded. If you only have the PDF, identify your feedback as a screen check. Both kinds of observation are useful when they stay distinct.

[Repository](https://github.com/jonathanbabec5-hash/potify-field-card/tree/26e4e3a7cd5b7bc28babc026d202fbb4040ed57f) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-field-card/archive/26e4e3a7cd5b7bc28babc026d202fbb4040ed57f.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-field-card/blob/26e4e3a7cd5b7bc28babc026d202fbb4040ed57f/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-field-card/blob/26e4e3a7cd5b7bc28babc026d202fbb4040ed57f/docs/BUILD-LOG.md)

### Field Card Delivery and Measurement

**Did a reader receive a field card?**

A button can be pressed without a PDF arriving. A PDF can arrive without the reader ever seeing the button. For a publisher making a useful thing on paper, that difference is the whole measurement question.

Follow the [test request](https://github.com/jonathanbabec5-hash/potify-field-measurement/blob/9e16809b0f9ead2ad87bfc162b3653fa0e24af87/tests/field-tracking.test.mjs) from the landing page to the file, then inspect the [Worker](https://github.com/jonathanbabec5-hash/potify-field-measurement/blob/9e16809b0f9ead2ad87bfc162b3653fa0e24af87/src/field-worker.mjs). The SQLite fixture separates anonymous delivery counts, consent-based attribution and excluded traffic. Seven local cases are documented; no real visitor records are included.

Run a direct-file request and a page-only visit in the fixture. Explain which counter should change in each case and why. A good correction uses synthetic requests and protects the reader’s choice. It does not turn delivery into a claim that the card was read.

[Repository](https://github.com/jonathanbabec5-hash/potify-field-measurement/tree/9e16809b0f9ead2ad87bfc162b3653fa0e24af87) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-field-measurement/archive/9e16809b0f9ead2ad87bfc162b3653fa0e24af87.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-field-measurement/blob/9e16809b0f9ead2ad87bfc162b3653fa0e24af87/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-field-measurement/blob/9e16809b0f9ead2ad87bfc162b3653fa0e24af87/docs/BUILD-LOG.md)

## Build a neighborhood

### POTIFY City · Roof 7B

**Who gets to stay on Roof 7B?**

A first crop gives you something to sell. The lease gives you a reason to care what that sale makes possible. Roof 7B belongs as much to the neighbors downstairs as it does to the person watering the roof. A player who remembers Moss and a broken latch has found a different game from one who only remembers the balance.

Follow a harvest in the [game store](https://github.com/jonathanbabec5-hash/Potify/blob/1cfb7051dd15b886a25062e6b6831466cbaf3c9b/artifacts/potify-high-life/src/game/store.ts), then a resident’s task in the [story model](https://github.com/jonathanbabec5-hash/Potify/blob/1cfb7051dd15b886a25062e6b6831466cbaf3c9b/artifacts/potify-high-life/src/game/story.ts). The ledger, latch and signal belong to different residents. Growth, inventory and the local save have to agree with the story even after you close the tab.

Start a fresh local game, harvest once, speak to a resident and reload. Tell us the first moment you understood why the lease mattered—or where that connection was lost. Give the device and the last action. The currency is fictional; this is a playtest.

The November 4 teaser, vertical story, and public Master Key show the rooftop premise before the lease story. The November 8 draft asks the player to choose a first upgrade. Its posting kit records a planned time on X. Publication is unverified. [Browse the original files](https://github.com/jonathanbabec5-hash/Potify/blob/37f99867c04c8d13197def4dd964e23a661ef606/docs/marketing/ORIGINALS.md) · [Read the campaign draft](https://github.com/jonathanbabec5-hash/Potify/blob/37f99867c04c8d13197def4dd964e23a661ef606/docs/marketing/2026-11-08-original-campaign.md) · [Open the public Master Key PDF](https://github.com/jonathanbabec5-hash/Potify/blob/37f99867c04c8d13197def4dd964e23a661ef606/docs/canon/originals/POTIFY_Master_Key_PUBLIC.pdf)

[Repository](https://github.com/jonathanbabec5-hash/Potify/tree/1cfb7051dd15b886a25062e6b6831466cbaf3c9b) · [Source ZIP](https://github.com/jonathanbabec5-hash/Potify/archive/1cfb7051dd15b886a25062e6b6831466cbaf3c9b.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/Potify/blob/1cfb7051dd15b886a25062e6b6831466cbaf3c9b/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/Potify/blob/1cfb7051dd15b886a25062e6b6831466cbaf3c9b/docs/BUILD-LOG.md)

### POTIFY City Public World Bible

**A city can have 469 ideas and one playable roof**

A world bible lets an illustrator and a game developer talk about the same corner of town without spoiling what lives there. A feature ID is useful precisely because a sketch, a line of dialogue and a playable scene can all refer to it without pretending to be the same milestone.

The [public registry](https://github.com/jonathanbabec5-hash/potify-city-canon/blob/5628e8b1e12d19ec1f8e80a2f3c0a7a00b02ea8b/public/POTIFY_CITY_REGISTRY_PUBLIC.json) divides 469 distinct IDs into 18 sections. The [count check](https://github.com/jonathanbabec5-hash/potify-city-canon/blob/5628e8b1e12d19ec1f8e80a2f3c0a7a00b02ea8b/tests/project.test.mjs) verifies the IDs. The playable neighborhood has its own game repository; an entry in this book does not make a mechanic playable.

Pick one public ID and describe what its stated status lets a reader expect. If you can reproduce it in the game, cite the game revision and the action; otherwise leave the design status as written. Keep story discoveries out of the issue title.

[Repository](https://github.com/jonathanbabec5-hash/potify-city-canon/tree/5628e8b1e12d19ec1f8e80a2f3c0a7a00b02ea8b) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-city-canon/archive/5628e8b1e12d19ec1f8e80a2f3c0a7a00b02ea8b.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-city-canon/blob/5628e8b1e12d19ec1f8e80a2f3c0a7a00b02ea8b/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-city-canon/blob/5628e8b1e12d19ec1f8e80a2f3c0a7a00b02ea8b/docs/BUILD-LOG.md)

### Vape God

**Can a player tell why the round ended?**

Two minutes is a short time to learn a game. It is a long time to spend wondering what a button meant. Vape God’s most interesting design question comes at the end of a round: did the player understand what happened well enough to want a second try?

The [editable game client](https://github.com/jonathanbabec5-hash/potify-vape-god/blob/438c0b9a05a3f5161016bd5a82e93b665bd4b7f3/src/VapeGod.tsx) keeps the clock and input state; the [website reward route](https://github.com/jonathanbabec5-hash/potify-vape-god/blob/438c0b9a05a3f5161016bd5a82e93b665bd4b7f3/reference/reward-route.ts) in this revision disables game rewards. The score starts with a session-dependent value. A screenshot alone cannot establish who played best.

For an adult practice playtest, start one local round without coaching. Write down the control you discovered first, what ended the round and what you expected next. An unclear ending is useful feedback. This build does not announce a contest or offer token prizes.

[Repository](https://github.com/jonathanbabec5-hash/potify-vape-god/tree/438c0b9a05a3f5161016bd5a82e93b665bd4b7f3) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-vape-god/archive/438c0b9a05a3f5161016bd5a82e93b665bd4b7f3.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-vape-god/blob/438c0b9a05a3f5161016bd5a82e93b665bd4b7f3/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-vape-god/blob/438c0b9a05a3f5161016bd5a82e93b665bd4b7f3/docs/BUILD-LOG.md)

### POTIFY Greenhouse and Holder Hub

**Giving credit for the same good deed exactly once**

A quest is a small promise between a contributor and an organizer: do the work, show what happened, receive a fair review. In the Greenhouse the most revealing case is the second review of the same quest. A community should be able to recognize a contribution without counting it twice.

Read the [local beta server](https://github.com/jonathanbabec5-hash/potify-holder-hub/blob/9817ba64d002eefa1ae85b522231c69d47307e17/server.mjs) with the [hub tests](https://github.com/jonathanbabec5-hash/potify-holder-hub/blob/9817ba64d002eefa1ae85b522231c69d47307e17/tests/hub.test.mjs). SQLite ties the review decision to the award. These Seeds are non-transferable community points; the older wallet-keyed beta and the later multi-wallet identity pilot have different data models.

Use the synthetic tests to trace one submission, one authorized review and an attempted repeat. Report the visible state after both attempts. Actual membership records and production migrations belong outside a public fixture.

[Repository](https://github.com/jonathanbabec5-hash/potify-holder-hub/tree/9817ba64d002eefa1ae85b522231c69d47307e17) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-holder-hub/archive/9817ba64d002eefa1ae85b522231c69d47307e17.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-holder-hub/blob/9817ba64d002eefa1ae85b522231c69d47307e17/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-holder-hub/blob/9817ba64d002eefa1ae85b522231c69d47307e17/docs/BUILD-LOG.md)

### Potify ID

**Credit that can travel without carrying a whole identity**

Someone tends a community project and later turns up at a screening. The organizer might need to know they earned a badge. They do not need every address the person has used. Potify ID makes that distinction concrete in two small fixture apps.

In the [two-app pilot](https://github.com/jonathanbabec5-hash/potify-id/blob/99bab8dc408655abe294d7d8d0f411fcee8c155d/src/pilot.mjs), a member can have different identifiers in different apps. The [local demonstration](https://github.com/jonathanbabec5-hash/potify-id/blob/99bab8dc408655abe294d7d8d0f411fcee8c155d/src/run.mjs) generates disposable keys, grants a particular disclosure and exercises an attendance pass. That lets a developer follow what the organizer actually sees without recruiting a real attendee.

Trace a pass from issue to redemption and then look at a second redemption attempt. Write down what each app learned and which permission made that possible. Eight local scenarios were recorded; a deployed issuer, physical-device recovery and independent adoption still need their own evidence.

[Repository](https://github.com/jonathanbabec5-hash/potify-id/tree/99bab8dc408655abe294d7d8d0f411fcee8c155d) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-id/archive/99bab8dc408655abe294d7d8d0f411fcee8c155d.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-id/blob/99bab8dc408655abe294d7d8d0f411fcee8c155d/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-id/blob/99bab8dc408655abe294d7d8d0f411fcee8c155d/docs/BUILD-LOG.md)

## Read, listen and watch

### The First Cycle Edition

**A book you can enter through a song**

Book I of The POTIFY Chronicle, *The Soil Remembers (Grow Room Version)* and the *From Seed to Smoke* premiere NFT belong to one First Cycle. Start with the Cultivator’s Note. Read a paragraph at your own pace, then put on the recording. The difference between the rhythm you imagined and the one you hear is a good reason to give both a little time.

The [edition page](https://github.com/jonathanbabec5-hash/potify-first-cycle-public-edition/blob/5d7a7364627054adbda03607096d51048dd97ec2/public/index.html) keeps the opening pages, Book I handoff and listening controls close together. The [song file](https://github.com/jonathanbabec5-hash/potify-first-cycle-public-edition/blob/5d7a7364627054adbda03607096d51048dd97ec2/public/assets/the-soil-remembers-grow-room.mp3) identifies the Grow Room recording precisely. Reading and listening stand on their own. The 25 artworks are individual NFT designs; the last verified claim state was paused.

[Open the free edition](https://potify-first-cycle.wile-e-coyot.chatgpt.site/#edition). On a phone, try moving from one paragraph to the track and back. Tell us which step lost your place, if any. For eligibility and recipient-signed claim status, use the [premiere page](https://potify-first-cycle.wile-e-coyot.chatgpt.site/premiere/).

[Repository](https://github.com/jonathanbabec5-hash/potify-first-cycle-public-edition/tree/5d7a7364627054adbda03607096d51048dd97ec2) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-first-cycle-public-edition/archive/5d7a7364627054adbda03607096d51048dd97ec2.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-first-cycle-public-edition/blob/5d7a7364627054adbda03607096d51048dd97ec2/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-first-cycle-public-edition/blob/5d7a7364627054adbda03607096d51048dd97ec2/docs/BUILD-LOG.md)

### The POTIFY Chronicles

**A bookmark that still points to the same paragraph**

The Cultivator’s Note is a deliberate threshold into Book I of The POTIFY Chronicle. A reader who leaves a thought there and follows the song ought to be able to find their way back. For the developer, that quiet promise lives in a section identifier.

The [Book I source](https://github.com/jonathanbabec5-hash/potify-chronicles/blob/ac44d60975c26378c50752324ed798b63b45c929/src/chronicle.ts) retains the paragraph sequence. The [reader check](https://github.com/jonathanbabec5-hash/potify-chronicles/blob/ac44d60975c26378c50752324ed798b63b45c929/tests/book.test.mjs) verifies that each canonical section has an anchor in the offline book. Chapters I–V are in this public edition. Later manuscripts and private branches are outside it.

[Open the free edition](https://potify-first-cycle.wile-e-coyot.chatgpt.site/#edition), return to a passage, and note the section name if the link loses your place. A precise bookmark report protects the writing without asking readers to reproduce the manuscript.

[Repository](https://github.com/jonathanbabec5-hash/potify-chronicles/tree/ac44d60975c26378c50752324ed798b63b45c929) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-chronicles/archive/ac44d60975c26378c50752324ed798b63b45c929.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-chronicles/blob/ac44d60975c26378c50752324ed798b63b45c929/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-chronicles/blob/ac44d60975c26378c50752324ed798b63b45c929/docs/BUILD-LOG.md)

### From Seed to Smoke

**The detail a caption can save**

At the beginning of the public field film, the caption marks two pencil taps. That is a small sound to keep, but it gives the scene a pulse even for a viewer watching silently. The attention paid to that cue is a good way into From Seed to Smoke.

The [timed captions](https://github.com/jonathanbabec5-hash/potify-seed-to-smoke/blob/563ba0e2bc6e96ce6ecd52210f70008366fde9ab/public/film/field-note.vtt) sit alongside the [public field film](https://github.com/jonathanbabec5-hash/potify-seed-to-smoke/blob/563ba0e2bc6e96ce6ecd52210f70008366fde9ab/public/film/field-note.mp4). They are a versioned preview, distinct from a finished episode. Read one cue and look at the same moment in the picture before deciding how to edit it.

Check the opening cue and one transition on a phone. If a line disappears too early or lands late, include the timestamp, device and a proposed change. A preview view is not a premiere attendance record.

[Repository](https://github.com/jonathanbabec5-hash/potify-seed-to-smoke/tree/563ba0e2bc6e96ce6ecd52210f70008366fde9ab) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-seed-to-smoke/archive/563ba0e2bc6e96ce6ecd52210f70008366fde9ab.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-seed-to-smoke/blob/563ba0e2bc6e96ce6ecd52210f70008366fde9ab/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-seed-to-smoke/blob/563ba0e2bc6e96ce6ecd52210f70008366fde9ab/docs/BUILD-LOG.md)

### Grow Room Sessions

**The recording that belongs with these pages**

‘Grow Room Version’ matters. A link can say the right song title and still point at a different edit. When a reader moves from Book I to the music, the file behind the play button is an editorial decision, just as surely as a paragraph break.

The [listening page](https://github.com/jonathanbabec5-hash/potify-grow-room-sessions/blob/b69c60ebe2b4d0c715e58909389f8d875fb8ba5d/public/index.html) points to [The Soil Remembers (Grow Room Version)](https://github.com/jonathanbabec5-hash/potify-grow-room-sessions/blob/b69c60ebe2b4d0c715e58909389f8d875fb8ba5d/public/audio/the-soil-remembers-grow-room.mp3). A filename and digest let an editor identify the bytes. The listener can answer a different question: does the intended recording start, sound right and remain usable on their device?

Try the beginning from a cold visit. If something is wrong, note the player, device and timestamp. Public listening is not a sync or remix license. The track’s companion is Book I of The POTIFY Chronicle in the [free edition](https://potify-first-cycle.wile-e-coyot.chatgpt.site/#edition).

[Repository](https://github.com/jonathanbabec5-hash/potify-grow-room-sessions/tree/b69c60ebe2b4d0c715e58909389f8d875fb8ba5d) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-grow-room-sessions/archive/b69c60ebe2b4d0c715e58909389f8d875fb8ba5d.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-grow-room-sessions/blob/b69c60ebe2b4d0c715e58909389f8d875fb8ba5d/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-grow-room-sessions/blob/b69c60ebe2b4d0c715e58909389f8d875fb8ba5d/docs/BUILD-LOG.md)

### First Cycle premiere NFT design source

**A numbered design and an on-chain record tell different stories**

Book I of The POTIFY Chronicle, *The Soil Remembers (Grow Room Version)* and the *From Seed to Smoke* premiere NFT are the First Cycle invitation. The 25 artworks are individual NFT designs. A record describing one design preserves creative intent; it does not prove an NFT was issued to a recipient.

The [collection metadata](https://github.com/jonathanbabec5-hash/potify-premiere-herbarium/blob/7e1e291dc2714850e0ab4e7b7e062631a8b740d4/metadata/collection.json) and [project checks](https://github.com/jonathanbabec5-hash/potify-premiere-herbarium/blob/7e1e291dc2714850e0ab4e7b7e062631a8b740d4/tests/project.test.mjs) describe the source package. A metadata URL, local render or transaction simulation is not a confirmed recipient-signed claim. The last verified public claim state was paused.

[Open the free edition](https://potify-first-cycle.wile-e-coyot.chatgpt.site/#edition) for the book and recording. The [premiere page](https://potify-first-cycle.wile-e-coyot.chatgpt.site/premiere/) is the place to check eligibility and current claim information. Do not infer mint availability from this repository.

[Repository](https://github.com/jonathanbabec5-hash/potify-premiere-herbarium/tree/7e1e291dc2714850e0ab4e7b7e062631a8b740d4) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-premiere-herbarium/archive/7e1e291dc2714850e0ab4e7b7e062631a8b740d4.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-premiere-herbarium/blob/7e1e291dc2714850e0ab4e7b7e062631a8b740d4/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-premiere-herbarium/blob/7e1e291dc2714850e0ab4e7b7e062631a8b740d4/docs/BUILD-LOG.md)

### The Living Archive · technical reference

**How to describe twelve stages without making up a grow**

The name of a stage helps a keeper file a note. A dated observation tells us what happened to a particular plant. An illustration can do the first job beautifully and still say nothing about the second. That distinction is the editorial heart of the Living Archive.

This repository is a technical source reference. The [stage model](https://github.com/jonathanbabec5-hash/potify-living-archive/blob/bce3c6acddd59662809f0d286dbc04860ef98a95/public/app.js) and [technical paper](https://github.com/jonathanbabec5-hash/potify-living-archive/blob/bce3c6acddd59662809f0d286dbc04860ef98a95/docs/WHITEPAPER.md) show how labels and illustrations correspond. **The Living Archive remains private.** Its presence in the public source directory is not an invitation to access private grow logs or reader records.

For a maintainer review, compare stage terminology between the model and the paper. Flag a label that could be read as a documented result instead of an illustration. The public reading destination is the [free First Cycle edition](https://potify-first-cycle.wile-e-coyot.chatgpt.site/#edition).

[Repository](https://github.com/jonathanbabec5-hash/potify-living-archive/tree/bce3c6acddd59662809f0d286dbc04860ef98a95) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-living-archive/archive/bce3c6acddd59662809f0d286dbc04860ef98a95.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-living-archive/blob/bce3c6acddd59662809f0d286dbc04860ef98a95/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-living-archive/blob/bce3c6acddd59662809f0d286dbc04860ef98a95/docs/BUILD-LOG.md)

### Signal Drop 001

**A printed link cannot receive a hotfix**

Once a signal card leaves the printer, the quiet border around its code matters just as much as the URL inside it. Signal Drop 001 makes those tiny black and white decisions inspectable long after somebody has put the paper in a pocket.

Compare the [QR component](https://github.com/jonathanbabec5-hash/potify-signal-drop/blob/60def113922c3933b29f3cb543dcc160e39e3f1b/app/SignalDropQr.tsx) with the [independent matrix decoder](https://github.com/jonathanbabec5-hash/potify-signal-drop/blob/60def113922c3933b29f3cb543dcc160e39e3f1b/tests/qr-matrix.test.mjs). The regression checks the encoded destination. It cannot tell us whether a phone camera reads a worn print or where the server sends that visitor today.

If you have an existing print, record its size, the camera used and the actual final destination after a scan. If you only ran the decoder, report the decoded string as a software result. No event attendance or sale can be inferred from either one.

[Repository](https://github.com/jonathanbabec5-hash/potify-signal-drop/tree/60def113922c3933b29f3cb543dcc160e39e3f1b) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-signal-drop/archive/60def113922c3933b29f3cb543dcc160e39e3f1b.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-signal-drop/blob/60def113922c3933b29f3cb543dcc160e39e3f1b/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-signal-drop/blob/60def113922c3933b29f3cb543dcc160e39e3f1b/docs/BUILD-LOG.md)

## Check a Solana claim

### Project Reclaim

**The most useful number is what remains**

‘Recoverable’ can sound like money already in your pocket. The useful work in Project Reclaim happens before a signature: what could be recovered, what comes out of it and what would actually remain? A reader should be able to check that arithmetic on paper.

The [integer illustration](https://github.com/jonathanbabec5-hash/potify-reclaim-developer/blob/1de4db4fe232a2e7c6074c1c079509c33fb95fa3/src/quote.mjs) gives a small example: 2,000,000 lamports gross, 360,000 for the 18% service fee, and 5,000 assumed network cost leave 1,635,000. The [offline tests](https://github.com/jonathanbabec5-hash/potify-reclaim-developer/blob/1de4db4fe232a2e7c6074c1c079509c33fb95fa3/tests/project.test.mjs) and the recovered engine are separate evidence. The recorded 58 engine tests are not a completed live-wallet claim.

Read a fictional quote and identify the gross, service fee, network cost and estimated net. Flag the first label that could be mistaken for the amount received. Reclaim is POTIFY-developed, in Phantom early access. Review the net before signing; optional burns are irreversible. Stop on wallet warnings.

[Repository](https://github.com/jonathanbabec5-hash/potify-reclaim-developer/tree/1de4db4fe232a2e7c6074c1c079509c33fb95fa3) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-reclaim-developer/archive/1de4db4fe232a2e7c6074c1c079509c33fb95fa3.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-reclaim-developer/blob/1de4db4fe232a2e7c6074c1c079509c33fb95fa3/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-reclaim-developer/blob/1de4db4fe232a2e7c6074c1c079509c33fb95fa3/docs/BUILD-LOG.md)

### POTIFY Public Treasury Record

**What ‘pending’ ought to look like**

A public record is sometimes most useful before it contains a number. The sample treasury statement leaves its slot and reference empty. That tells the reader exactly which evidence is missing and gives the next reviewer something concrete to check.

The [synthetic record](https://github.com/jonathanbabec5-hash/potify-treasury-record/blob/a137d5d5bc2f3d324bab1bd83417e50caae509e4/examples/record.json) and the [validator](https://github.com/jonathanbabec5-hash/potify-treasury-record/blob/a137d5d5bc2f3d324bab1bd83417e50caae509e4/src/record.py) distinguish the shape of a report from the truth of a financial claim. Valid JSON cannot establish ownership, custody, a current balance or vesting. This repository supplies a reporting specification.

Review the sample as written. Is ‘pending’ still unmistakable after rendering? Suggest a clearer label or a fixture that keeps an unsupported claim pending. Public contributions need no real balances, private addresses, signer details or treasury records.

[Repository](https://github.com/jonathanbabec5-hash/potify-treasury-record/tree/a137d5d5bc2f3d324bab1bd83417e50caae509e4) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-treasury-record/archive/a137d5d5bc2f3d324bab1bd83417e50caae509e4.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-treasury-record/blob/a137d5d5bc2f3d324bab1bd83417e50caae509e4/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-treasury-record/blob/a137d5d5bc2f3d324bab1bd83417e50caae509e4/docs/BUILD-LOG.md)

## Study a fictional checkout

### Green Light Pay Consumer

**Which balance did the receipt change?**

A shopper should be able to put a finger on the confirmation screen and say what moved. Green Light Pay Consumer gives a product team a fictional basket and a keypad so that question can be asked before anyone brings real money to the counter.

Follow a simulated purchase in the [consumer demo](https://github.com/jonathanbabec5-hash/potify-green-light-pay/blob/d6f68699bb80e9e2a17a70a5304fb9248b3abae7/GreenLight_Pay_Consumer_Demo.html) beside the [journal checks](https://github.com/jonathanbabec5-hash/potify-green-light-pay/blob/d6f68699bb80e9e2a17a70a5304fb9248b3abae7/tests/demo.test.cjs). Separate what the keypad displays from the asset debited and the journal entries that must balance. A wallet balance read is another operation again.

Try the same fictional confirmation twice and account for the resulting entries. Quote the label that made this clear or propose one better label. Provider clearance, settlement and custody remain unverified. Green Light Pay has separate finances, contracts and governance from POTIFY.

[Repository](https://github.com/jonathanbabec5-hash/potify-green-light-pay/tree/d6f68699bb80e9e2a17a70a5304fb9248b3abae7) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-green-light-pay/archive/d6f68699bb80e9e2a17a70a5304fb9248b3abae7.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-green-light-pay/blob/d6f68699bb80e9e2a17a70a5304fb9248b3abae7/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-green-light-pay/blob/d6f68699bb80e9e2a17a70a5304fb9248b3abae7/docs/BUILD-LOG.md)

### Green Light Pay Initiative

**What would a cashier say the demo missed?**

A checkout can look convincing from three feet away while asking the wrong person to make the next decision. Green Light Pay Initiative uses a shared fictional receipt so a cashier, a customer and an operator can describe the same moment in their own words.

Step through the [demo controls](https://github.com/jonathanbabec5-hash/potify-glp-initiative/blob/753b779a19e70d8e55247c2c57c08e4553ea50e6/public/demo.js) and the [research microsite source](https://github.com/jonathanbabec5-hash/potify-glp-initiative/blob/753b779a19e70d8e55247c2c57c08e4553ea50e6/public/index.html). The receipt views give the interviewer a concrete screen to discuss. The dated overview is research context; it does not establish current provider approval or a live payment service.

Name one moment in the fictional checkout and the role that would need clearer information. No customer records or payment details are needed. Green Light Pay keeps its own finances, contracts and governance; a research response is not an endorsement.

[Repository](https://github.com/jonathanbabec5-hash/potify-glp-initiative/tree/753b779a19e70d8e55247c2c57c08e4553ea50e6) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-glp-initiative/archive/753b779a19e70d8e55247c2c57c08e4553ea50e6.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-glp-initiative/blob/753b779a19e70d8e55247c2c57c08e4553ea50e6/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-glp-initiative/blob/753b779a19e70d8e55247c2c57c08e4553ea50e6/docs/BUILD-LOG.md)

### Green Light Pay Merchant Sandbox

**Can the cashier trace one receipt back to the basket?**

Start a fictional sale at the counter, hand it to a customer, and follow it through partner screening and reconciliation. The [Original merchant engine](https://github.com/jonathanbabec5-hash/potify-glp-merchant-sandbox/blob/aaf3e77e990942f36a4cc61004074dad179a806f/sandbox/src/core.mjs) and HTTP routes are now in the merchant repository. The 12 published frontend assets matched the Replit export after applying its base path to the HTML.

One useful first contribution is to change the expected total in a synthetic fixture and record which transition catches the difference. A clean install passed 99 offline tests. Browser checks covered direct terminal navigation, command entry and transaction-filter focus at desktop and mobile viewport sizes. The authorized demonstration uses fictional records. [Run the recovered release](https://github.com/jonathanbabec5-hash/potify-glp-merchant-sandbox/blob/aaf3e77e990942f36a4cc61004074dad179a806f/README.md)

[Repository](https://github.com/jonathanbabec5-hash/potify-glp-merchant-sandbox/tree/aaf3e77e990942f36a4cc61004074dad179a806f) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-glp-merchant-sandbox/archive/aaf3e77e990942f36a4cc61004074dad179a806f.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-glp-merchant-sandbox/blob/aaf3e77e990942f36a4cc61004074dad179a806f/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-glp-merchant-sandbox/blob/aaf3e77e990942f36a4cc61004074dad179a806f/docs/BUILD-LOG.md)

### Green Light Pay Wallet Connection

**Which account is the screen showing now?**

A balance can be correct and still be misleading if it belongs to the account the user just left. The wallet component is small enough to follow this question end to end without authorizing a payment.

Read the [mock-provider tests](https://github.com/jonathanbabec5-hash/potify-glp-wallet-connect/blob/754b24425ffb331ea55d37791b882874287f5053/tests/wallet.test.cjs) beside the [adapter](https://github.com/jonathanbabec5-hash/potify-glp-wallet-connect/blob/754b24425ffb331ea55d37791b882874287f5053/wallet-connection.js). Look for the moments an account changes and a connection ends. Connection, balance display, identity and spending permission are distinct; a locally simulated balance is not a native-phone compatibility result.

Use only the disposable fixture to compare the display before a switch and after disconnect. Tell us which old value should disappear. Nothing needs to be signed, and no real address or balance needs to be published. Green Light Pay remains independently governed and financed.

[Repository](https://github.com/jonathanbabec5-hash/potify-glp-wallet-connect/tree/754b24425ffb331ea55d37791b882874287f5053) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-glp-wallet-connect/archive/754b24425ffb331ea55d37791b882874287f5053.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-glp-wallet-connect/blob/754b24425ffb331ea55d37791b882874287f5053/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-glp-wallet-connect/blob/754b24425ffb331ea55d37791b882874287f5053/docs/BUILD-LOG.md)

### Green Light Pay · July Reference Sandbox

**A July checkout you can still put under a microscope**

Keeping an old experiment intact lets a new maintainer ask a better question than ‘does this look current?’ They can ask exactly what the July team meant by an intent, a register and a receipt, then decide which assumptions still hold.

In the [core test](https://github.com/jonathanbabec5-hash/potify-glp-reference-sandbox/blob/84dec801bee1b32ef0f0e8ee47a588b924fcba86/test/core.test.mjs), a synthetic checkout starts with 4,250 US cents and an idempotency key. The [sandbox core](https://github.com/jonathanbabec5-hash/potify-glp-reference-sandbox/blob/84dec801bee1b32ef0f0e8ee47a588b924fcba86/src/core.mjs) handles the fixture locally. The July 22 handoff labels this historical reference; it is not the canonical merchant backend.

Trace that $42.50 fictional intent and record what a repeat request should do. Name one assumption you would recheck before reusing the design. No commercial provider, real funds or settlement is implied; Green Light Pay’s finances, contracts and governance are separate.

[Repository](https://github.com/jonathanbabec5-hash/potify-glp-reference-sandbox/tree/84dec801bee1b32ef0f0e8ee47a588b924fcba86) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-glp-reference-sandbox/archive/84dec801bee1b32ef0f0e8ee47a588b924fcba86.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-glp-reference-sandbox/blob/84dec801bee1b32ef0f0e8ee47a588b924fcba86/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-glp-reference-sandbox/blob/84dec801bee1b32ef0f0e8ee47a588b924fcba86/docs/BUILD-LOG.md)

## Find the right doorway

### POTIFY Website

**What did the visitor come here to do?**

One person arrives for a book; another for a plant question. A homepage that sends both through the same unexplained doorway makes the project harder to love. The website directory is where those different intentions ought to become obvious.

Compare the [observed route list](https://github.com/jonathanbabec5-hash/potify-website-developer-guide/blob/eee89271fc005a1eaae74faaa5e1db93fd67a7b8/src/observed-routes.json) with the [public directory](https://github.com/jonathanbabec5-hash/potify-website-developer-guide/blob/eee89271fc005a1eaae74faaa5e1db93fd67a7b8/src/directory.json). A path in the source tells you how the application is arranged. A completed task requires a person to arrive at the right screen and be able to use it.

Choose one free destination. Record the entry label, the final page and the task you could actually complete without signing in. If a route comes back to the homepage, give that route and a description of what you expected to see.

[Repository](https://github.com/jonathanbabec5-hash/potify-website-developer-guide/tree/eee89271fc005a1eaae74faaa5e1db93fd67a7b8) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-website-developer-guide/archive/eee89271fc005a1eaae74faaa5e1db93fd67a7b8.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-website-developer-guide/blob/eee89271fc005a1eaae74faaa5e1db93fd67a7b8/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-website-developer-guide/blob/eee89271fc005a1eaae74faaa5e1db93fd67a7b8/docs/BUILD-LOG.md)

### Beneath the Surface · Launch Room

**A doorway is only as good as where it leaves you**

A newcomer taps ‘Plant Doctor’ because they have a plant question. If the next page quietly drops them on a general homepage, the link may technically work while the visit fails. That last step is why the Launch Room deserves its own project.

Compare the [navigation component](https://github.com/jonathanbabec5-hash/potify-launch-room-developer/blob/6c4aabc97ff86533ca560d47289237e9e9008aab/src/EcosystemTabs.tsx) with the [destination records](https://github.com/jonathanbabec5-hash/potify-launch-room-developer/blob/6c4aabc97ff86533ca560d47289237e9e9008aab/src/directory.json). The component tells you what the button promises; the destination tells you where the reader is sent. Neither on its own proves that the promised task can be finished.

Choose a public destination and write down its label, final page and the first action a newcomer can complete. Report a misleading label with a clearer alternative. Leave account-specific routes and internal allocations out of the report.

[Repository](https://github.com/jonathanbabec5-hash/potify-launch-room-developer/tree/6c4aabc97ff86533ca560d47289237e9e9008aab) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-launch-room-developer/archive/6c4aabc97ff86533ca560d47289237e9e9008aab.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-launch-room-developer/blob/6c4aabc97ff86533ca560d47289237e9e9008aab/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-launch-room-developer/blob/6c4aabc97ff86533ca560d47289237e9e9008aab/docs/BUILD-LOG.md)

### POTIFY Merch Directory

**From a line in a book to something you can carry**

A book tote is a modest idea and a good test of this directory. Someone who comes from the First Cycle should reach that particular object without guessing among unrelated products. The link is the part this project owns.

The [two catalogue records](https://github.com/jonathanbabec5-hash/potify-merch/blob/85e7fb86ba48250b06c270decdf1f1c570f7d68c/src/directory.json) distinguish the storefront from product 32713018. The [entry page](https://github.com/jonathanbabec5-hash/potify-merch/blob/85e7fb86ba48250b06c270decdf1f1c570f7d68c/public/index.html) makes the handoff; the merchant platform owns the product details and checkout. Source can establish which item was selected, not its stock, price, delivery date or any sale.

Trace the tote link and compare the destination’s product identity with the record. If it lands at a storefront, a missing page or a different item, report the destination and date. No purchase is needed to make that correction.

[Repository](https://github.com/jonathanbabec5-hash/potify-merch/tree/85e7fb86ba48250b06c270decdf1f1c570f7d68c) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-merch/archive/85e7fb86ba48250b06c270decdf1f1c570f7d68c.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-merch/blob/85e7fb86ba48250b06c270decdf1f1c570f7d68c/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-merch/blob/85e7fb86ba48250b06c270decdf1f1c570f7d68c/docs/BUILD-LOG.md)

### Spin to Win and Prize Verification

**The wheel stops. What can a participant verify?**

A spinning wheel is the easy part to recognize. The hard part comes afterward, when someone has a code and wants to know what it means. This project keeps the participant’s view, the verification route and the organizer’s responsibilities distinct.

The [public route manifest](https://github.com/jonathanbabec5-hash/potify-spin-to-win-guide/blob/648d56e3be4f58a72c4a7c67854042ae407c688b/src/routes.json) lists the wheel, verification entry and code-specific route. The [participant verification component](https://github.com/jonathanbabec5-hash/potify-spin-to-win-guide/blob/648d56e3be4f58a72c4a7c67854042ae407c688b/reference/pages/spin-verify.tsx) shows the other side of the handoff. A route string cannot establish available prizes, an active event or a completed redemption.

Trace a fictional code through the source and point out the first place a participant could confuse ‘code recognized’ with ‘prize delivered.’ A wording correction is useful here without launching a draw or exposing anyone’s claim.

[Repository](https://github.com/jonathanbabec5-hash/potify-spin-to-win-guide/tree/648d56e3be4f58a72c4a7c67854042ae407c688b) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-spin-to-win-guide/archive/648d56e3be4f58a72c4a7c67854042ae407c688b.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-spin-to-win-guide/blob/648d56e3be4f58a72c4a7c67854042ae407c688b/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-spin-to-win-guide/blob/648d56e3be4f58a72c4a7c67854042ae407c688b/docs/BUILD-LOG.md)

## Make editorial work checkable

### POTIFY Dispatch Console

**One slot, two people, one preventable duplicate**

An editor sees a blank receipt at the end of a long day. Is that a reason to send again? The Dispatch Console gives a team a safe place to rehearse the much less dramatic, and much more useful, answer: find out who owns the slot first.

The [local console](https://github.com/jonathanbabec5-hash/potify-dispatch-console-reference/blob/e571c2ccb089f36ad47962b50fec9e018c2cecf2/public/index.html) stores fictional records in the browser. Read its [checks](https://github.com/jonathanbabec5-hash/potify-dispatch-console-reference/blob/e571c2ccb089f36ad47962b50fec9e018c2cecf2/tests/project.test.mjs) alongside a manual rehearsal: reserve a slot, let a second editor find it, then add a receipt to the first record. A local state change is visible without sending a real message.

Describe the exact screen or word that would tempt an editor to replay an uncertain post. Include the steps using made-up copy. The private dispatch console, connected accounts and actual publishing records are outside this example.

[Repository](https://github.com/jonathanbabec5-hash/potify-dispatch-console-reference/tree/e571c2ccb089f36ad47962b50fec9e018c2cecf2) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-dispatch-console-reference/archive/e571c2ccb089f36ad47962b50fec9e018c2cecf2.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-dispatch-console-reference/blob/e571c2ccb089f36ad47962b50fec9e018c2cecf2/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-dispatch-console-reference/blob/e571c2ccb089f36ad47962b50fec9e018c2cecf2/docs/BUILD-LOG.md)

### POTIFY Operations Workflow

**What exactly did the editor approve?**

Change a single word after a post is approved and a different piece of writing may go out under somebody’s name. This little workflow takes that ordinary editorial concern seriously enough to put it in code.

Read the [state transitions](https://github.com/jonathanbabec5-hash/potify-operations-workflow/blob/6ae977c5b6ffaaa8922cf48cfd2d0e98285a5ba0/lib/workflow.ts) beside the [seven workflow tests](https://github.com/jonathanbabec5-hash/potify-operations-workflow/blob/6ae977c5b6ffaaa8922cf48cfd2d0e98285a5ba0/tests/workflow.test.mjs). Watch for three different decisions: accepting a particular version, recording an actual schedule and recording publication evidence. A time typed into a form satisfies none of them by itself.

Take one approved fixture and change material copy while keeping its time. Follow its review state and explain which evidence would let it advance again. A useful contribution is a small example an editor can read aloud and an engineer can reproduce.

[Repository](https://github.com/jonathanbabec5-hash/potify-operations-workflow/tree/6ae977c5b6ffaaa8922cf48cfd2d0e98285a5ba0) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-operations-workflow/archive/6ae977c5b6ffaaa8922cf48cfd2d0e98285a5ba0.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-operations-workflow/blob/6ae977c5b6ffaaa8922cf48cfd2d0e98285a5ba0/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-operations-workflow/blob/6ae977c5b6ffaaa8922cf48cfd2d0e98285a5ba0/docs/BUILD-LOG.md)

### POTIFY Telegram Editorial Kit

**Two spaces or a different promise?**

A line break added on a phone shouldn’t trick an editor into posting the same message twice. Changing ‘Soil’ to ‘Roots’ really does change the copy. The Telegram Editorial Kit puts those two cases next to one another so the distinction is visible.

The [fingerprint tests](https://github.com/jonathanbabec5-hash/potify-telegram-editorial/blob/6a5525e616377e71cf605c29210357552ea474fd/tests/test_review.py) compare those exact examples. The [review utility](https://github.com/jonathanbabec5-hash/potify-telegram-editorial/blob/6a5525e616377e71cf605c29210357552ea474fd/src/review.py) runs offline; the historical bot is retained as source reference. A matching fingerprint says something about text, not who authorized it or whether Telegram received it.

Try a line-break-only edit, then change the meaning of one word. Report what matched and what changed using fictional copy. No access token, real conversation, bot deployment or message send is needed.

[Repository](https://github.com/jonathanbabec5-hash/potify-telegram-editorial/tree/6a5525e616377e71cf605c29210357552ea474fd) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-telegram-editorial/archive/6a5525e616377e71cf605c29210357552ea474fd.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-telegram-editorial/blob/6a5525e616377e71cf605c29210357552ea474fd/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-telegram-editorial/blob/6a5525e616377e71cf605c29210357552ea474fd/docs/BUILD-LOG.md)

### Potify Command Center

**A handoff that leaves room for ‘we don’t know’**

Three tools can all look like a dashboard and still solve completely different problems. Command Center matters because the person inheriting it should not have to guess whether they are looking at the founder’s workspace, the dispatch console or a diagram of either.

This release contains the [source handoff specification](https://github.com/jonathanbabec5-hash/potify-command-center-handoff/blob/c30afd1480ee4477b6a90ef9bbba99b74ea999fc/docs/HANDOFF.md) and a [scope paper](https://github.com/jonathanbabec5-hash/potify-command-center-handoff/blob/c30afd1480ee4477b6a90ef9bbba99b74ea999fc/docs/WHITEPAPER.md). A workspace listing was located. The original implementation and its distribution rights have not been established here; there is no Command Center executable to try in this repository.

A maintainer can review the handoff privately: identify the owner, name one input and output, and define one acceptance check. The useful public correction is a more precise interface description. Do not put access credentials, an internal export or operating records in an issue.

[Repository](https://github.com/jonathanbabec5-hash/potify-command-center-handoff/tree/c30afd1480ee4477b6a90ef9bbba99b74ea999fc) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-command-center-handoff/archive/c30afd1480ee4477b6a90ef9bbba99b74ea999fc.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-command-center-handoff/blob/c30afd1480ee4477b6a90ef9bbba99b74ea999fc/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-command-center-handoff/blob/c30afd1480ee4477b6a90ef9bbba99b74ea999fc/docs/BUILD-LOG.md)

### Wake and Bake POTIFY Price Update

**A chart needs a clock**

There is an honest sentence a market show should be willing to say on a quiet evening: the last trade is old. A fresh screenshot does not make it new. Wake and Bake POTIFY Price Update starts by giving each observation its own time, interval and source.

The [episode worksheet](https://github.com/jonathanbabec5-hash/potify-wake-and-bake/blob/a544bf4e6897dab412451753a3d67fd1eb7928e4/examples/issue.json) opens with the observation time and verified mint. The [renderer](https://github.com/jonathanbabec5-hash/potify-wake-and-bake/blob/a544bf4e6897dab412451753a3d67fd1eb7928e4/src/render.py) holds the editorial structure together; it does not fetch a fresh market price. Archived chart frames stay attached to their original dates.

Use the example to trace a single price statement back to its chart and time. If it cannot be traced, leave it unknown and suggest the missing source field. This review concerns editorial evidence; it makes no trading call or promise.

[Repository](https://github.com/jonathanbabec5-hash/potify-wake-and-bake/tree/a544bf4e6897dab412451753a3d67fd1eb7928e4) · [Source ZIP](https://github.com/jonathanbabec5-hash/potify-wake-and-bake/archive/a544bf4e6897dab412451753a3d67fd1eb7928e4.zip) · [Engineering or editorial paper](https://github.com/jonathanbabec5-hash/potify-wake-and-bake/blob/a544bf4e6897dab412451753a3d67fd1eb7928e4/docs/WHITEPAPER.md) · [Recorded checks](https://github.com/jonathanbabec5-hash/potify-wake-and-bake/blob/a544bf4e6897dab412451753a3d67fd1eb7928e4/docs/BUILD-LOG.md)

## Inspect work on Solana

### POTIFY Roots Agent Gateway

**What does an agent learn from a public address?**

Keep an address fixed in a synthetic fixture and change the account’s close authority. Does that account still qualify? Compare the result from the scanner with the summary the HTTP or MCP client receives. The gateway reports gross lamports. Its devnet challenge and five-call target are separate from a paid customer result.

[Source example](https://github.com/jonathanbabec5-hash/potify-roots-agent-gateway/blob/bd58b74a4d3778964a824555349609f85def79a0/src/reclaim-scanner.ts) · [Download this revision](https://github.com/jonathanbabec5-hash/potify-roots-agent-gateway/archive/bd58b74a4d3778964a824555349609f85def79a0.zip) · [Whitepaper](https://github.com/jonathanbabec5-hash/potify-roots-agent-gateway/blob/bd58b74a4d3778964a824555349609f85def79a0/docs/WHITEPAPER.md) · [Marketing and sales plan](https://github.com/jonathanbabec5-hash/potify-roots-agent-gateway/blob/bd58b74a4d3778964a824555349609f85def79a0/docs/MARKETING.md)

### POTIFY TukTuk Worker

**Who kept the reward after the transaction fee?**

Pick a saved transaction and trace a single job from its instruction through the payout log to the fee payer. A transaction can contain multiple jobs. If the evidence is ambiguous, record the unknown. This is how a queue maintainer can test a proposed reporting service against the public record.

[Source example](https://github.com/jonathanbabec5-hash/potify-tuktuk-worker/blob/30c986d5625b3b38f76eea63a212983987b3b587/potify_tuktuk/decode.py) · [Download this revision](https://github.com/jonathanbabec5-hash/potify-tuktuk-worker/archive/30c986d5625b3b38f76eea63a212983987b3b587.zip) · [Whitepaper](https://github.com/jonathanbabec5-hash/potify-tuktuk-worker/blob/30c986d5625b3b38f76eea63a212983987b3b587/docs/WHITEPAPER.md) · [Marketing and sales plan](https://github.com/jonathanbabec5-hash/potify-tuktuk-worker/blob/30c986d5625b3b38f76eea63a212983987b3b587/docs/MARKETING.md)


[Follow the builder on GitHub](https://github.com/jonathanbabec5-hash). A report that names a revision and one reproducible observation gives the next reader something useful to come back for.
