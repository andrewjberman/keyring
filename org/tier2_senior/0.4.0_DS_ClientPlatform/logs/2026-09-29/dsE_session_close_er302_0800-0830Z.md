# Round-3 close — the ~E queue is done — 0.4.0_DS_ClientPlatform~E

**archetype:** VALIDATE

**Date:** 2026-09-29, 08:00–08:30Z
**Task Order:** `IRPT_BCKEND.TO-IB-er-302` (complete). Delta on the preceding log
`dsE_v020_reemit_inflection_and_comparison_0500-0800Z.md` @`6851215833`, which was written while
er-302 was still in flight and left it open under Next Steps.
**Status:** BOTH ORDERS COMPLETE. `E3-AC1`, `E3-AC2`, `E3-AC3`, `E3-AC4` all PASS.

## Objective

Land the FWD-13 comparison partitions, grade E3-AC3, plant its mutants, write the proof, close the
ledger, and drain.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| naming-gate.py | on the new-file diff, then in `safe-commit.sh` | REFUSE 4, then **PASS 0 graded** | The refusal changed the design — see Decisions. |
| commit-gate.sh | on both new `.py` files | clean | py_compile + ds-precommit + ruff py39. |
| proof-of-spec-check.py | on the er-302 instance | INVALID once, then **VALID rc=0** | `findings` is not a permitted top-level key. |
| deploy_ledger.py | `close-leg` x3, `close` | all 3 legs proven, CLOSED | Opened before the first write. |
| safe-merge.sh | `ds-e-irpt-r3-holdings` | MERGED `727315d096` | The earlier REFUSE (another seat's staged index) cleared on retry. |

**What worked:** grading the new file against the gate with `git diff --no-index -- /dev/null <file>`
BEFORE attempting the commit. An untracked file is invisible to a plain `git diff`, so the first
commit attempt was the first time the gate saw it; the synthetic diff makes that a cheap dry run.

**What failed:** nothing this segment.

**Gap found:** none new.

## Work Completed

### 1. The comparison table landed and graded

`E3-AC3 PASS`. 5,318 rows over 5,318 bronze files in two partitions: as-of 2026-06-30 (1 file,
1 row) and as-of 2026-08-28 (5,317 files, 5,317 rows, 5,277 compared, 40 named not-comparable).
5,318 distinct `source_key`, 0 duplicated, 0 rows carrying neither figures nor a reason. Row
counts read back from the parquet footers, not the producer's tally. Reason census:
`PERIOD-OUTSIDE-GOLD` 35, `NO-VENDOR-FIGURE` 4, `ACCOUNT-UNRESOLVED` 1.

### 2. What the comparison measured

- **Where both methods have something to measure, they agree.** Of 4,256 fully-covered rows,
  4,098 are on accounts still holding priced positions at period end; 3,994 of those (97.5%)
  agree within 5 percentage points over a 251-trading-day year. Median absolute difference
  1.64pp; median signed difference −1.62pp, Opal below the vendor — the shape of a basis carrying
  no income and no flow term against one that does.
- **The tail is near-empty accounts, not a producer defect.** 20 fully-covered rows differ by
  more than 50pp; 16 are accounts whose gold row holds ZERO priced positions at period end
  (`account_value` median $112.00, minimum $1.09), where the holdings basis correctly reads 0.00%
  per day while the vendor's time-weighted figure runs −74.1% to +150.0% on flows through a shell.
  The comparison table carries no `account_value`, so this is invisible from the row alone.
- **1,022 of 5,278 compared rows (19.4%) are PARTIAL** and their differences are not usable:
  maximum absolute difference 13.98 against 1.50 among fully-covered rows. `opal_partial` and
  `partial_days` are on every row for exactly this reason.

### 3. Mutants

Two, both on the 1-file partition so the restore reads one bronze file rather than 5,317, and both
restored by re-running the producer. M1 duplicated the row → `dup 1` → FAIL → PASS. M2 dropped the
figure and left no reason → `neither 1` → FAIL → PASS.

## Decisions Made

1. **The naming limb refused `bd_account_ids` and `bd_account_id`, and the fix is better than the
   original.** The emitted column became `vendor_account_ids`, and both cross-reference join
   columns are now found by MEASUREMENT — the column whose values contain the ids read from a
   32-file bronze probe, and the column whose values match the declared `account_id_zero_pad`
   form — refusing if either matches anything other than exactly one column. Typing a join key
   assumes it; measuring it checks it, and an ambiguous join key does not fail loudly, it produces
   a plausible wrong answer. The resolved pair is printed on every run.
2. **No surprise row was filed.** The three findings above are the deliverable's own output, not
   something found off-task, and they are carried in the proof where a reader of that table will
   meet them. Minting a channel row for the thing the order asked me to produce would be process
   without a consumer.

## Files Modified

| File | Commit |
|---|---|
| `.../deliverables/0.4.0_DS_ClientPlatform~E/...TO-IB-er-302...proof_of_spec.json` | `8798bc4c4a` |
| `.../task-orders/IRPT_BCKEND.TO-IB-er-302...md` (status → complete) | `8798bc4c4a` |
| `org/critical_paths/change_management/20260929T0735Z_...deploy_completion.md` (CLOSED) | `8798bc4c4a` |

**Workspace CLOUD commit:** `727315d096` (`safe-merge.sh`). Worktree `ajb_irpt_e_r3` removed and
branch `ds-e-irpt-r3-holdings` deleted. All five round-3 commits verified as ancestors of local
`CLOUD` with a positive control. Push state: LOCAL — `git ls-remote origin CLOUD` read
`15655f4a25` at 08:20Z; `CLOUD` is pushed by `0.0.0_AB_MSTR` only.

## Blockers

**None.** No open task order, no open deploy ledger, no unread mail.

## Current State

Workstream ~E's round 3 is complete. The 49F holdings gold is re-emitted under PRD v0.20 with no
served implausible day; the Inflection slice covers every computable trading day from 2020-04-27;
FWD-13's comparison points exist for every landed Black Diamond pull. Nothing reads any of these
prefixes — `comp-estate` places the subject in 0 of 135 estate chains — so no served output moved.
Both reports are with `2.0.0_SA_COO~P`.

## Next Steps

1. **[`2.0.0_SA_COO~P`]** The adapter switch re-cut; its precondition now reads true. Two things
   to carry into the never-widen half: a manifest is the producer's SELF-REPORT (mutant M2 in
   er-301 dropped a row from a landed parquet and `complete` still read true), and the comparison
   table carries no `account_value`, so its large differences cannot be triaged from the row.
2. **[`2.0.0_SA_COO~P` / `1.0.0_SA_CTO`]** Cottonwood is next under ruling 11 and cannot be
   declared by monolith — `blackdiamond` carries 2 registry scopes, so `firm_scope()` will refuse
   and ask for a `registry_key`. There is no Cottonwood custody master in `infra/logic/registry/`
   today; that is a registry row to add before the cell is cut.
3. **[`0.4.0_DS_ClientPlatform~E`]** IDLE, available. The Inflection comparison points (the weekly
   Orion household factors, ruling 8) are the obvious next cell on this lane, unissued.
