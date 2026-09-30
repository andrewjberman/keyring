# AMGT_CORPUS -- ROUND 15 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~22:1xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, subject *"L10 slug AMGT_CORPUS round 15 @166f02e312"*, citing
`surprise-channel/adjudications/ADJUDICATION_v18.md`. Issuer packet: `ROUND15_DRAIN_END_PACKET.md` @`bb54b9a183`.

**Round 15 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **Hitachi 6501 JP is registered and served** (`q-2`, pair COO `ca6e2ef4f2` / CTO `411236c2b7`).
  - `crosswalk/v1/2026-09-29.json`: 236 -> 237 records. Added `6501_JP_Equity` only; removed 0, changed 0 (the CVO's own
    record diff).
  - **The live library resolves 96 of 96.** This closes AMGT_RESAPP's one read failure (`Z-S303`) and FWD-4's organic arm
    (`Z-S58` GRADUATED).
- **`q-1` needed no build.** `read_dossier` reads both `/` names from their encoded partitions (`BP-SLASH-_LN_Equity`,
  `NG-SLASH-_LN_Equity`). `Z-W4-S5`'s 93 of 95 was the sweep passing partition names as keys. GRADUATED.
- The CVO AGREED both of the issuer's calls.

## 2. RULING -- the standing mechanism for new library folders (CVO section 5.1)

**RULED: schedule the producer that already exists. Build nothing new.**
- **Measured by this seat:** `lib/research/corpus/induction_run.py` is the estate's registration producer for new
  folders. It is FWD-4's WILL-ADD path, driven on planted folders in round 14.
  - `comp-find 'induction_run'` over `lib infra data .tools org/ref` finds 83 hits in 2 files: the module and its own
    test. **Nothing triggers it.**
  - The two related site-Z Scheduled Tasks, `OpalResearch-ExecManagement` and `OpalResearch-FilingsAnalyzer`, both read
    **Disabled**.
  - So a folder waits for a manual act, and the crosswalk went 4 days without a vintage while Hitachi waited.
- **Why a schedule and not a watcher:** CLAUDE.md forbids a monitor and requires production producers to be scheduled.
  Andrew's R-21 names the model for a vendor-calling producer: a deterministic, scripted, re-runnable pull on a trigger,
  like the existing pull. By the build ladder, the estate already has the producer, so only the trigger is new.
- **The one cell's contract:**
  - A daily trigger runs `induction_run` over the live library: every folder with no crosswalk row is registered through
    `add_security`'s scripted path (R-21), and ambiguous names are REFUSED, not picked (CVO~Z's calls-not-picks ruling
    stands).
  - The trigger runs from a pinned commit, never the shared working tree. Site-Z Scheduled Tasks run the working tree,
    which a peer's uncommitted edit can change under it.
  - Its name is builder output (Rule 30).
  - The FIRST scheduled fire is the acceptance, under a NEVER-2 entry and a never-widen pair. The expected outcome is read
    from the producer's rule at signing: today's population is 0 of 96, so the first fire's expected write is a no-op
    (the digest-equal branch of `write_pool`), and a planted folder is the positive arm on a scratch library.

## 3. FWD GRADES

- **13 of 19 REALIZED, 6 NOT REALIZED, 0 unmeasurable.** Unchanged in count.
- FWD-4's organic arm now reads its real limb: population 0 of 96, and Hitachi resolves.
- **The six NOT REALIZED (FWD-10, 11, 12, 15, 16, 18)** remain AMGT_RESAPP's served reader (`/thesis` passing the
  dossier's fields), carried to its round 50. This project re-grades them on the deployed function once that lands.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` cuts for round 16 in ONE issuance

| # | cell | risk | note |
|---|---|---|---|
| 1 | **Schedule `induction_run`** (ruling above) | WORLD (a scheduled producer with a vendor leg), under a never-widen pair and a NEVER-2 entry for the first fire | Adds the daily trigger only: pinned commit, builder-named, no new producer code unless the pin demands a CLI entry. AC: (a) a planted folder on a scratch library is registered by one scheduled-path run, and an ambiguous planted name is REFUSED; (b) the first real scheduled fire reads population 0 and writes nothing (`write_pool` digest-equal no-op); (c) the task's `Actions` resolve to the pinned commit, not the shared tree. |

**Fan-out:** 1.

**NOT cells:**
- the six render outcomes (AMGT_RESAPP round 50);
- `Z-S59` (the tool's owner);
- the two Disabled `OpalResearch-*` tasks. Recorded as an observation: whether they should run is their own producers'
  owners' call, and FWD-7's officer path is AMGT_RESAPP `xx-3`'s.

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- None. R-21 @`b390c36444` is the vendor word for the scheduled registration path, whose mechanism (scripted, scheduled)
  is exactly the one it names.

## Compiler Tools

- The CVO's v18: its pool listing, its own record diff (236 -> 237), its 96-of-96 resolution census and its
  `read_dossier` reads.
- This seat:
  - `comp-find 'write_pool|write-pool'`: 196 hits in 9,371 files, 13 DEF.
  - `comp-find 'induction_run'`: 83 hits in 2 files; no trigger found.
  - `Get-ScheduledTask` filtered on research/crosswalk/filings/management: 2 `OpalResearch-*` tasks, both Disabled.
