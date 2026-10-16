# MDPF_SECCLASS TO-SC-e107b: seed22.py apply wrote 13 new keys into etf-classifications (lane 0.7.0_AE_CloudOps~SC1)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Seat:** `0.7.0_AE_CloudOps~SC1` on dell1 | **Order:** `MDPF_SECCLASS.TO-SC-e107b.seed22-apply` (round 27, cell SC-e-107, `<risk>WORLD</risk>`) | **Issuer:** `2.0.0_SA_COO~M1` (GO msg 6548) | **Window:** 2026-10-16 06:19Z -> 06:40Z.

## Current State

**The 13 keys are in the table and leg B is green.** `SEED22-APPLY written=13 refused=0` at 06:27:08Z; `E107-SEEDED ok=True present=13/13 absent_ok=9/9 problems=[]`; scan 11362 -> 11375; the 9 held-out keys absent; 200 pre-act census keys re-read by `get_item`: 0 missing, 0 `last_updated` moved. Ledger `secclass-e107b-seed22-apply-20261016` CLOSED. Leg G is the issuer's, on the first scheduled fire.

## What happened, in order

| step | what | result |
|---|---|---|
| 0 | three documents read; sha256 of plan, script, request equal; runner stopped; trigger-pending 404; PutItem simulation; 25 worktrees read for open ledgers | `E107_STEP0_20261016.out` |
| P | 22 `get_item` all absent, ItemCount 11362, PITR ENABLED, 200-key census, VersionIds of the two served mix summaries | `E107_LEGP_20261016.json` |
| A | in one shell: window re-read, hashes, leg P, ledger open, apply | `E107_ACT_20261016.out` |
| B | seeded check, post census | `E107_LEGP_POST_20261016.json`, `E107_ACT_20261016.out` |

## Decisions Made

- Ran this order while the cb-15 window (`HVST-cb-15`) was open: the runner work is event-driven and idle between events; the two orders touch different systems.
- Named, and did not touch, the two old open ledgers that mention the table (`secclass-e57e61-fwd10-apply-s-20261007`, `secclass-multi-asset-remap-b-m-20261007`).

## Blockers

**None.** Issuer: leg G; the held-out 9 stay Unclassified by design.

## Corrections and gaps, mine

1. **The PutItem simulation proves nothing here:** its typo control (`dynamodb:ZzzNoSuch`) also read allowed, so the principal's grant is a wildcard. The conditional put's `written=13 refused=0` is the evidence.
2. **My first post-act census comparison printed `moved=1 AMT`:** an artifact of the 13 new keys sorting into the first 200 and pushing the 200th pre-act key out. Re-read by `get_item` of each of the 200 keys: 0 moved. Recorded in the act file.
3. **The act shell's `list-objects-v2 --max-items 1 --query length(...)` printed an `aws` error line beside the correct count of 1** (a pagination-token quirk of the control read); the window verdicts do not depend on it.
4. **The order file flip to `complete` was refused once by the pipeline gate** until the proof-of-spec instance existed; instance added.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `seed22.py` | `apply --plan ... --pair ...` | `written=13 refused=0` | the act |
| `e107_seeded_check.py` | no args | `ok=True present=13/13 absent_ok=9/9` | AC1 |
| `deploy_ledger.py` | `open` (2 legs), `close-leg` x2, `close` | PASS | |
| `commit-gate.sh` | `e107_legp.py` | clean | py_compile, ds-precommit, ruff |
| `comp-iam` (simulate) | PutItem, DescribeTable, a typo action | all allowed | wildcard; not relied on |
| `comp-find` | `trigger-pending\.json` | 253 hits | too broad; the lane's earlier orders named the bucket |
