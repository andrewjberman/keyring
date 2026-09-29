# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 17, `CRPS-s-1` act (Hitachi 6501 JP model-block pull) -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~23:3xZ

**Against:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND17_HITACHI_MODEL_BLOCK.md` @`6e7bdec3bd` (msg 26778, READ-acked).

## VERDICT: SIGNED

## 1. READ BY THIS SEAT

- **`integrations/bloomberg/READ_HERE.md`, read first as CLAUDE.md requires.**
  - A signed-out terminal is section 2's two-phase sign-in, whose submit is budgeted and needs Andrew's MFA.
  - The COO half's stop limb 1 routes exactly that, so this pair never signs in.
- **The gap is real.** The census at `01682baecd` reads 95 of 96 with a model block, and `6501_JP_Equity` is absent. The
  producer admits no newly registered name without a named ticker.
- **Before-state:**
  - `git show HEAD:integrations/bloomberg/research/field_map.json` holds 0 `6501` keys.
  - The shared tree's copy carries a peer's UNCOMMITTED edit, +1,187/-134 lines. It is not this pair's.
  - That confirms why the act must run from a clean detached worktree.
- **Vendor authority:** R-21 @`b390c36444`, all vendors, scripted. Every call is inside `model_block_pull.py` and its
  `sa_forecast_fallback.py`.

## 2. CONDITIONS

1. **The Seeking Alpha fallback currently answers HTTP 402** (`AMGT_HARVST-Z-W37-S4`; Andrew renews). A 402 on a fallback
   cell must leave that cell `unresolved` and never `SA_FALLBACK`.
   - If `derive` instead aborts on the 402, that is stop limb 2: nothing is committed, and a row is filed.
   - A partial block must never carry a cell marked `SA_FALLBACK` that the vendor did not answer.
2. **The `field_map.json` merge into CLOUD must not touch the peer's uncommitted edit** in the shared tree.
   - If the merge would overwrite it (git refuses, or `safe-merge` flags it), HOLD the merge.
   - Name the edit's owner from the tree's evidence (mtime, the active seats on `integrations/bloomberg/research/`) and ask
     that seat to commit or stash first.
   - The Hitachi keys are never carried by overwriting another seat's work.
3. **The after-state census re-run reads `present 96 absent 0`,** and the `field_map.json` diff against CLOUD HEAD adds only
   `6501` keys (0 changed, 0 removed), as the COO half states.

## 2a. RULING ON CONDITION 3's FAILURE (~23:3xZ, 2.0.0_SA_COO~X msg 26784, row `Z-S65`, `evidence/r17_after.txt` @70da93e7ee)

- **The pull and derive are done, and Hitachi's block is SERVED:** census 96 of 96, and the SA fallback was not called.
- **The `field_map.json` merge fails condition 3, as the condition exists to catch.** It flips **4 shared fields from
  MEASURED to UNRESOLVED-ON-6501** and changes **1 field's unit from a scalar to a dict**. That moves what every other
  name's derive reads.
- The producer's "additive merge that never overwrites a MEASURED entry" is not additive at the field level when one
  security disagrees.

**RULED: (b) commit Hitachi's per-security entries ONLY.**
- The committed diff adds only `6501`-scoped keys: 0 shared fields changed, 0 removed, and no type change. The executor
  prints that diff as leg F's proof.
- **(a) is refused:** it regresses 95 names' unit map to fit one.
- **(c) is refused:** it would leave Hitachi's block un-reproducible from the committed map.
- **The shared-field disagreement is not lost.** It is `Z-S65`, cut into AMGT_CORPUS round 18: `build_unit_map` records a
  per-security exception when one name disagrees with a MEASURED shared field, and never downgrades the shared field or
  changes its type.
- Leg F closes inside the entry's window (ends 01:26Z) on (b).

## 3. NOTED, NOT IN THIS PAIR

- `Z-S64`: the model-block writer bypasses `slash_safe_key`, so `BP/` is stored under a literal `/`. This act writes only
  `6501_JP_Equity`, which has no `/`. The defect is carried to this project's round-18 list.

## 4. ROLLBACK

The COO half stands: revert the `field_map.json` commit. The derived object is write-once, with newest-stamp pick. An
un-serve needs a delete, which is Andrew's act. The exposure is one name gaining the block it lacked.
