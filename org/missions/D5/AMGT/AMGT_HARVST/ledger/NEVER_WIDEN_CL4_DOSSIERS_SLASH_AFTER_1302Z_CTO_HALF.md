# NEVER-WIDEN -- CTO HALF: `HVST-cl-4`, the BP/ and NG/ dossiers rebuilt after the 13:02Z model blocks (round 97)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~15:0xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round97/NEVER_WIDEN_HALF_COO_CL4_DOSSIERS_SLASH_AFTER_1302Z.md` as committed
at 5fc9ab77eb, sha256 `512874fb6489162b6fd720921080c73ced3bf80d803e5ca8d64412a7f8220164`. Any edit to that file voids this half.

## What I read at signing

- **The shape:** the act has the cj-5 shape (my half @93f7352b2e): add-only, at the encoded partitions. The census reads `model_rows`
  moving on both names, caused by `model_block`.
- **The guard read** (W1's question, row D1-W175-S2). The guard is read through `dossier._model_block_read`, the same function `build()`
  calls at `dossier.py:1511`, because `build()` does not return the record. **Confirmed as the right reader, with one race to close:** a
  model block can land between the guard read and the build's own read. Condition 1 closes it.
- **The code pin:** the worktree is AT `4c7a60cabe` exactly, since `lib/research` has changed at HEAD from another project. That is the
  same discipline as ch-7.

## Blast radius

- 2 gold keys are added under `amgt/harvest/gold/research_dossier/`, at the encoded partitions of `BP/_LN_Equity` and
  `NG/_LN_Equity`.
- Served moves: `model_rows` to the newer block, plus `as_of`, `dossier_key`, `content_sha256` and the dossier entry of `source_keys`.
- All else stays equal. No overwrite or delete. ADD-ONLY: removing the keys is an S3 delete, Andrew's act, not pre-approved.

## Conditions of this signature

1. **The guard and the build read the same block:**
   - the model-block key the guard prints must equal the model-block key in the written object's `inputs`;
   - if it differs (a block landed in between), STOP for that name and re-run the census.
2. **C-1 to C-10 of cj-5 bind,** with this act's names and counts: dossiers +2, continuations unchanged, BP read in all four spellings
   before NG, and site Z told first.
3. **The NEVER-2 close is COMMITTED.**

## Not covered, and ruled as a round-98 cell (W1's fact)

**Model blocks land daily at ~13:0xZ, so a hand-rebuilt dossier is a day behind again within hours. Hand rebuilds are not the fix.**
- The round-98 cell is a SCHEDULED dossier refresh, triggered on the daily cycle after the model-block landing, by its own clock and not
  by success-of-upstream alone (CLAUDE.md: production pipelines are scheduled).
- The census-and-guard of cj-4 is built into the job, so a name whose moves fall outside `{fund_form_ref, model_rows}`, or whose block
  read is not SERVED and newer, is skipped and reported, never written.
- It goes under its own pair, with its schedule and writer census named. Until it lands, the dossiers' `as_of` lag is stated, not
  hidden.

## VERDICT: SIGNED (CTO).
