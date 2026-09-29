# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 14, `CRPS-p-5` (continuation /3 rewrite + dossier re-derive) -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~19:4xZ

**Against:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND14_CONTINUATION_V3.md` @`69e88e71ad` (msg 26675, READ-acked).
**Worker tip:** `a53f4c4bfc`, equal to the tip of branch `wk-crps14-5r` at signing. **Ruling it implements:** round-13
analysis s.4 item 5 @`f1c482d24f`; amendment 1 @`af9e934ae2`.

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT

- **Before-state (S3, ~19:32Z, `opal-data-harvest`):**
  - `research-continuation/` holds 225 objects in 95 partitions.
  - `research_dossier/` holds 95 objects in 95 partitions.
  - Both equal the COO half.
- **The key rule, read at `a53f4c4bfc`.**
  - `_inputs_sha16` hashes `{"method_version": METHOD_VERSION, "inputs": ...}` (`continuation.py:161-163`).
  - `METHOD_VERSION` is `/3` on the branch and `/2` on CLOUD, so every name gets a new key and `gold_put` never
    overwrites.
  - The branch diff against CLOUD is 6 files; the only non-test code change is `continuation.py` (+57/-3).
- **Writers, N=2.** A `comp-find` census for `research-continuation|research_dossier` over `lib infra data` found
  19 hits in 5 files.
  - The writers are `continuation.py` and `dossier.py`.
  - `scoped-amgt-api.tf` is the reader's grant; the rest are tests.
- **This seat's own content census, independent of the worker's.**
  - Method: `continuation.build()` under `/3` for all 95 resolved names, read-only, compared field by field with each
    name's stored input-matching `/2` object. The script is kept in this seat's scratchpad.
  - Result: **95 of 95 compared, 0 errors; 1 name changed, `ML_FP_Equity`, `thesis_pillars` only.** The other four fields
    are equal on all 95 names. This equals the COO half's "94 unchanged".

## 2. CORRECTION TO THE COO HALF (it does not change the verdict)

"Merge -> step 2: trunk code reading continuation picks the `/2` object" is **not what the rule does.**
- With no `/3` object stored, `_select_stored` falls back to the lowest sorted key among the input-matching objects.
- Measured across the 95 names, the fallback picks **`/1` for 49 names and `/2` for 46.**
- No served reader reads continuation directly: the deployed scoped API reads dossier objects. So the window moves
  nothing served, provided no dossier build runs inside it. Condition 2 below binds that.

## 3. CONDITIONS

1. **Sequence after ww-1.** Step 1 (the merge) starts only after the `amgt-resapp-ww1-redeploy-research-dossier-restart-20260929`
   entry closes its V1 leg. The new scoped-API function reads `research_dossier/`, and nothing this seat has read
   confounds V1's `/timeline` or `/print` captures with a dossier move. Sequencing removes the question at no cost.
2. **No continuation or dossier consumer runs between the merge and step 2 completing 95 of 95.** Step 3 is the only
   dossier build, and it follows step 2. If step 2 stops short (stop limb 2), revert the merge before anything else runs.
3. **After-state verify, as in the COO half's items 1-5,** plus one check this seat adds: `dossier --pick-census` reads
   `current_method_available 95`. That shows every name's pick moved from the `/1`-or-`/2` fallback to `/3`.
4. **Same-UTC-day rollback is named as unavailable by write.** The exposure is one field on one name (ML_FP gaining 5
   real pillars), and the direction is the ratified fix. A same-day un-serve would need a delete of the 95 step-3
   objects, which is an act only Andrew can do (CLAUDE.md Agent Autonomy). The next-day rollback stands as the COO half
   states it.

## 4. NOT COVERED

- Any delete or overwrite.
- Any deploy or IAM act.
- Any write from code other than `a53f4c4bfc` merged. If the branch moves, this half does not travel with it.
- Any served move on a name other than ML_FP.
