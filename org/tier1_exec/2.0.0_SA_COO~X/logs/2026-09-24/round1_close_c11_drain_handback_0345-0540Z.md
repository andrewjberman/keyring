# 2.0.0_SA_COO~X -- AMGT_CORPUS: hand-back to canonical flow, c-11 closed, round 1 drained and handed to L8 (2026-09-24 03:45-05:40Z)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, IMPLEMENT

Seat `2.0.0_SA_COO~X`, Claude, site Z, shared tree `CLOUD`. Window: after `startup_claude_seat_takeover_and_corpus_state_0311-0345Z.md`
(commit e35dd62097) to 05:40Z. Watcher re-armed at every expiry (bt73d8s90 -> b65xxyimz -> bjqky4kgw -> bvm4el63v -> bbk9y8mz2).

## Summary

1. **Andrew handed AMGT back to canonical flow** (~04:3xZ, relayed by `1.0.0_SA_CTO~Z` as R-26 @`ad5c7a75c6` and msg 25252):
   `AMGT_CORPUS` -> this lane, two outcomes (the dossier fold + the full backfill). The closer gate this lane was waiting on
   (R-22) was dissolved by the hand-back itself. Read R-26/R-26a/R-26b and `HANDBACK_TO_CANONICAL_20260924.md` s.3 while
   they were still uncommitted working-tree edits, acted only once the commit and the message landed.
2. **Round 1's one open order, `CRPS-c-11` (read-only proof), closed on the issuer's own execution** (G00 @`8d33ad1cc5` had
   transferred it; the worker slot was never spawned). Criteria re-run on the carried-forward branch: AC1 91 PASS, AC3 census
   files_scanned 30 / write_like_calls 27 / library_write_calls 0 / plant flagged 1, AC4 212 PASS, AC6 hygiene 51 of 51 in
   grant; AC2 is the retained root-bound negative control (write_denied_probe PermissionError x2, ingest 123 stored / 0 puts /
   0 read failures) that C01 graded PASS (CTO msg 24841). AC5 (judgment) recorded with no verdict for `3.0.0_SA_CVO~Z`.
3. **Two things the literal order could not do as written, each filed rather than papered over:** (a) AC3's `tail -30`
   window drops the census header now that the output is 32 lines -- row `AMGT_CORPUS-Z-S10` @`4359367fee` (first minted as
   `W1-S3`; the row gate refused a seat row carrying a W coordinate, correctly), window amended to `tail -40`, expect
   unchanged; (b) the owned-paths hook refused this seat a write under `deliverables/0.9.0_WK_AMGT_CORPUS~1/`
   (TREE_DELIVERABLES, owner in the path) -- rather than an audited author override into another serial's folder, AC2's
   path and the section-6 instance home were amended to this lane's folder, which `check_complete_flip` searches.
4. Instance VALID (rc=0) bound to the order: 6 of 6 criteria, 5 of 5 invocations aligned, surprises 1 of 1 resolve. Flip
   committed @`4c50cbc076` on the lane branch; **drained through `safe-merge.sh` as `b4a8638eeb`** (51 paths: c-11, the B08
   adapter + evidence, the typed.py period fix, closer channel C with rows Z-S5..S9; merge-commit exemptions printed by
   the gates). Round 1: 11 of 11 terminal.
5. **L8 handed to `3.0.0_SA_CVO~Z`** (05:24Z, delivered filesystem + broker + push): new rows and c-11's AC5 at L9. Tree row
   phase + STATUS.md re-cut as the canonical carrier @`a4daac6ce2`.
6. Read PRD v0.5 ADDENDUM A @`1ffb156ecd` (msg 25261): FWD-10..FWD-18 = the fold, FWD-19 = 93 of 93 DISPOSITIONED;
   `C-NO-VENDOR-CALL` amended narrowly (one `reference_data` call per name, once, via `add_security`, scripted; V3 not
   authorized); R12-R14; the L5 question of which seat RUNS the induction is named for the two seats.

## Rulings and messages

Received 3 (all acked): CTO~Z 25252 (hand-back record), 25261 (ADDENDUM A). Sent 1: the L8 hand-off to `3.0.0_SA_CVO~Z`.
Rulings read: R-26/R-26a (a field written to a GENERATED row is erased by the next derive; the tree row is the carrier),
R-26b (residue routed to `0.0.0_AB_MSTR~Z`; a branch census cannot see whether a worker was spawned).

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `pytest lib/research/corpus/tests/test_readonly_proof.py` | AC1 | PASS | 91 passed, twice |
| `readonly_proof --code-census` | AC3 | PASS | 30 / 27 / 0 / plant 1, three runs |
| `pytest lib/research/corpus/tests` | AC4 | PASS | 212 passed, twice |
| `.scratch/c11/hyg.py` | AC6 | PASS | outside_allowed [], bad 0, three runs (50, 50, 51 changed) |
| `.tools/proof-of-spec-check.py --governing-order` | c-11 instance | PASS | first run INVALID with 5 schema/resolution violations, all fixed; then VALID rc=0 twice |
| `.tools/surprise-row-gate.py` (via safe-commit) | row Z-S10 | PASS | first attempt refused (W coordinate on a seat row), re-minted |
| `.tools/safe-commit.sh` | 4 commits | PASS | one refusal (owned-paths, worker folder) resolved by re-homing, not override |
| `.tools/safe-merge.sh` | drain | PASS | b4a8638eeb, row gate on the merged index, 0 conflicts |
| `.tools/missions-tree-index.py derive --write` | tree row | PASS | no index change for this project (compared fields unchanged) |

What worked: reading the gate's own resolution rule (`deliverables/*/`) turned a lane refusal into a path amendment
instead of an override. What failed: two first attempts (W coordinate; worker folder), both refused by the right gate.
Gap: `git worktree remove` refuses a merged worktree that carries only gitignored scratch, and `--force` is a recursive
delete -- left for the integrator.

## Blockers

None BLOCKED. Gated: the round-1 slug (`3.0.0_SA_CVO~Z`, with c-11 AC5), then the round-1 analysis (`1.0.0_SA_CTO~Z`);
this lane cuts round 2 only after both (Rule 27 order, LD-0521).

## Current State (for a reader with zero context)

CLOUD @`a4daac6ce2` LOCAL; origin/CLOUD `be10e5c34d` (ls-remote 05:38Z); this lane does not push. AMGT_CORPUS round 1
terminal at `b4a8638eeb`; L8 with the CVO. Lane worktree `C:/tmp/closer-amgt-corpus-x-20260923` is MERGED and idle
(branch `closer-amgt-corpus-x-20260923` fully merged; only `.scratch/c11/hyg.py` left; removal is a recursive delete,
routed with R-26b's residue). Round 2 inputs: PRD v0.5 ADDENDUM A, CRO~Y brief @`328e17d5e5`, PDF_EXTRACTABILITY package,
round-1 decomposition v1.0 (bijection cells<->rows, 5 chains, fan-out as data). STATUS.md is the current-state carrier.

## Next Steps

1. [3.0.0_SA_CVO~Z] L8 compile + L9 on c-11 AC5; the round-1 slug to the CTO.
2. [1.0.0_SA_CTO~Z] round-1 analysis (the HANDBACK s.3 is its draft); the L5 question of which seat runs the scripted
   induction, with this lane's recommendation: a corpus-owned runner that imports `add_security` read-only, pinned and
   reviewed by `2.0.0_SA_COO~Z` before it fires.
3. [2.0.0_SA_COO~X] on the analysis: L5 decomposition v2.0 over R12-R14 + the reader cells (FWD-16 first: extract.py
   inline-lead rule + PFOE name set; continuation.py PDF pillar branch, docx as control), battery, ONE issuance, fresh
   worker worktrees from CLOUD.
4. [0.0.0_AB_MSTR~Z] residue: the four read-only library copies, the census plant dirs, the merged worktree.
