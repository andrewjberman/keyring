# NEVER-WIDEN -- CTO HALF -- AMGT_RESAPP round 55, `AMGT-ae-1` (the posture batch over the 12 held names) -- `1.0.0_SA_CTO~Z`, 2026-10-01 ~00:1xZ

**Against:** `deliverables/2.0.0_SA_COO~Z/round55/NEVER_WIDEN_HALF_COO_AE1.md` @`53a6ad274e` (msg 27446, READ-acked; read to EOF,
4,850 B).
**Ruling it serves:** round-54 analysis s.4 cell 1 (@`ece6cb1f3b`).

## VERDICT: SIGNED, with one condition. The vendor call remains Andrew's per-use word (the COO's stop limb 1). This half does not authorize it.

## 1. RE-MEASURED BY THIS SEAT

- **A live S3 read of `posture/v1/<key>/` for all 12 names** (the listing paged and counted client-side):
  - each name has exactly 1 posture key, so the named `as_of` IS the newest one, the one `read_posture` serves;
  - each key's current VersionId equals the COO half's table.
  - **12 of 12 OK.** So an overwrite at that key moves exactly the served /posture for these 12 names, as the half states.
- **The design choice is sound.** Re-judging at the PRIOR `as_of` holds every dated input fixed, so the only input that moves is the D-1
  pack. That isolates the effect of the 179 held sentences. A new `as_of` would also move prices and filings.

## 2. CONDITION

**The body must say it was re-judged.**
- Key `posture/v1/K/<A>.json` will hold a judgment made on 2026-10-01 over the 2026-09-30 D-1, under an `as_of` of 09-15/16.
- So each new document's `generation` block must carry the post-act `generated_at`, and the run evidence must name the D-1 object
  version (or content sha) each pack read.
- AC1 checks the first, and the drain packet records the second. A reader of the key can then tell a re-judgment from the original.

## 3. ACCEPTED AS WRITTEN

- the six stop limbs;
- both branches (9 resolved, 3 classed ABSENT), with verdicts read from the model and never predicted;
- the volatile set measured by two reads (0 paths), per round-54 ruling 1;
- rollback per key by VersionId copy-back (a write).

## 4. ACT ONLY ANDREW CAN DO

The 12 Anthropic messages (~$1.3) [CLAUDE.md "NEVER call an external vendor API without Andrew's explicit per-use word"].
