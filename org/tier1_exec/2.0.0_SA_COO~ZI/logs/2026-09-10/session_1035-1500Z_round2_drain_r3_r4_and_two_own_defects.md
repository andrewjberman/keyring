# 2.0.0_SA_COO~ZI -- session log 2026-09-10, 1035-1500Z

**Window:** the round-2 drain of NFRA_IAMROLES202609, from IAM-r-4 landing to IAM-r-5/IAM-r-6 dispatch.
**Round state at close of window:** 4 of 6 cells terminal and merged; IAM-r-5 and IAM-r-6 IN FLIGHT.
**dep_stage:** EXECUTING throughout (only `1.0.0_SA_CTO~Z` moves it).
**Push state:** round-1 work ON ORIGIN; every round-2 commit LOCAL. Measured `ls-remote` 14:35Z --
local SITEZ 23 ahead of origin `db3431f1c2`; positive control (`c72d7277a2` ON ORIGIN) and negative
control (local HEAD not an ancestor) both behaved.

---

## 1. WHAT LANDED

| commit | what |
|---|---|
| `abaa352e35` | drain IAM-r-3 -- TRUE membership per member on Terraform SOURCE |
| `7b795cc977` | surprise rows Z-S10 + Z-S11 |
| `021a34551f` | register row to 4 of 6 terminal |

**IAM-r-3 is the round's headline.** Membership classed by `resource "aws_iam_role"` block presence
and never by name mention: **1 DECLARED-IN-TF** (`seeking-alpha-scraper-role`, the confirmed false
positive, `infra/aws/terraform/seeking-alpha/main.tf:240-241`) and **15 NOT-IN-TF**. The settled set of
16 is **15** -- previously bounded at "at most 15", now measured.

**IAM-r-4's deferred bound is CLOSED and it HOLDS.** Its order required confirming from IAM-r-3's
verdict list that each of its three was genuinely undeclared, and r-4 necessarily ran first.
`ecsTaskExecutionRole`, `rds-monitoring-role`, `vpc-flow-logs-role` all read NOT-IN-TF: the class
ruling did not exempt a declared role, so the round-1 defect did not recur.

## 2. THE SEQUENCING CALL, AND WHY A SLOT IDLED ON PURPOSE

IAM-r-5 and IAM-r-6 were held until IAM-r-3 landed rather than chained on inherited membership. Both
**dispose or adopt a MEMBER**, and deciding membership from an assumption is the precise defect this
round exists to repair. Chaining r-6 to keep slot ~5 warm would have re-run that defect to save
minutes. The hold paid twice: all three still-owed members read NOT-IN-TF, and r-4's bound closed.

Both dispatched on `opus`, overriding the cheap default -- r-5 carries production serving-path safety
and the round's one specification call; r-6 carries a Rule 24 schema change graded on taxonomy
coherence.

## 3. AN ANOMALY THAT WAS MY INSTRUMENT, TWICE

Carried in from the previous window: a check of `UNASSIGNED owners remaining` read **9** where a drop
from 6 was expected. **The document was never wrong.**

1. A bare token census counts the pattern's own **definition** and its narrative prose -- 7 of the 10
   hits at HEAD are not member rows.
2. My first correction used a **case-sensitive** row regex that silently dropped 2 of the 16 members --
   including `ecsTaskExecutionRole`, *the very row under test*. Had I stopped there (5 -> 3, a drop of
   2 against an expected 3) I would have opened a false investigation into IAM-r-4.

Scoped to member rows on the corrected denominator: **6 / 6 / 3 / 3** across the round's vintages, with
`owner=CTO` **0 / 0 / 3 / 3**, denominator constant at 16. Exactly what IAM-r-4 claimed.

## 4. Z-S10 -- SURFACED, FIXED IN ~15 MINUTES, VERIFIED BY EXERCISE

`proof-of-spec-check.py` set `_REPO_ROOT` from `__file__`, so the VALID/INVALID verdict was a property
of the PAIR *(instance, tree-the-script-lives-in)*. Spine v3 puts every worker in a linked worktree, so
the natural drain graded worker instances against a tree that could not contain their deliverables --
**and the refusal named the WORKER's artifact**, so it read as the worker's defect. This lane nearly
banked a good instance as a failure.

`1.0.0_SA_CTO~Z` fixed it at `709b9556a3` and traced it **narrower than my row did**: the resolution
model was not the defect; a **swallowed `ValueError`** left `inst_commit` None so the git fallback could
not run. The checker was converting *"I cannot see this tree"* into *"your artifact is broken."*

**Verified here by exercise, not relay** (Rule 22 -- confirming via the first seat's method is
repetition): main-tree checker + worktree instance -> `CHECKER-SCOPE`, old violation census **0**,
author-disclaimer census **1**; negative control (main-tree instance) -> VALID rc=0, no CHECKER-SCOPE;
worktree's own copy -> VALID rc=0.

⭐ The row named a **FALSE-VALID direction it had not exercised** and labelled it read-from-source only.
The fixer's stated reason for choosing the refusing form was that it closes *that* direction too.
**Naming an unexercised direction honestly is what made the cheaper fix the correct one.**

## 5. TWO DEFECTS OF MY OWN, BOTH CLOSED

**(a) I invented an enum value.** Wrote `disposition: "RESOLVED"`; the ratified set is
`UNDER_INVESTIGATION / GRADUATED / DISMISSED_WITH_REASON / DECOMP_INVALIDATING`. Rule 24 binds any
schema an agent authors **or adopts**, and I adopted without reading the set -- one hour after filing
Z-S11, which is about shipping a criterion I had not measured with the instrument I shipped. **Same
shape twice: asserting a value instead of reading it.**

**(b) The row should not have existed, and leaving it uncommitted blocked the estate.** I wrote it to
stop Z-S10 being carried into the completion report as an open hazard, having read
`disposition=UNDER_INVESTIGATION` in the **investigations** document. That reading was true and the
inference wrong: `3.0.0_SA_CVO~Z` had already graduated Z-S10 and Z-S11 in `adjudications/
ADJUDICATION_v1.md` (C-S7, C-S8). **A surprise item's disposition does not live in the investigations
plane** -- the row's own field is frozen at authorship and the CVO's adjudicating row overrides it.
`comp-surprise --project <CODE>` reported `open=0` throughout; one command would have prevented both.

The gate refused the bad row, so **nothing entered the record** -- but I left it in the shared working
tree, and the standing corpus pass is **estate-wide, fail-closed, and hashes the WORKING TREE**, so it
refused `2.0.0_SA_COO~Z`'s unrelated commits three times. Removed surgically (row-id set diffed against
HEAD first: worktree 24 / HEAD 23, exactly one extra, zero missing; never `git checkout --` on a shared
append-only file). Corpus verified back to `baseline=4 known=4 new=0`; peers told, with the enum that
lane could not read.

⛔ **Operational rule this window earned: NEVER LEAVE A SURPRISE ROW UNCOMMITTED ACROSS A TURN.** Land
it or remove it in the same turn. That lane also **declined the documented override** on the grounds
that the refusal was correct -- an override asserts spuriousness, and this one was not spurious.

## 6. COMPILER TOOLS

| tool | invocation | result / denominator |
|---|---|---|
| `proof-of-spec-check.py` | worktree copy, IAM-r-3 instance + `AC1..AC5` | **VALID rc=0**, 1 PENDING co-committed (POST-COMMIT @`b077f10538`) |
| `proof-of-spec-check.py` | same + `AC99_BOGUS` (control) | INVALID rc=1, names the silent omission -- instrument alive |
| `proof-of-spec-check.py` | main copy, main-tree IAM-r-4 instance (control) | VALID rc=0, no CHECKER-SCOPE |
| `safe-merge.sh` | `wk-NFRA_IAMROLES202609-6` | MERGED `abaa352e35`; row gate 3 staged paths, 0 rows |
| `surprise-row-gate.py` | pre-stage vs in-commit | **0 new of 21** vs **2 new of 23** -- the denominator is the evidence it graded |
| `surprise-row-gate.py` | on Z-S12 | **BLOCKED**, 3 violations, enum named. Correct refusal |
| `comp-surprise` | `--project NFRA_IAMROLES202609` | items=24 **open=0** armed=23 defects=0 duplicate_ids=0 |
| `missions-tree-index.py` | `check`, then `derive --write` | 7 tree projects, 0 violations; index already current |
| `git ls-remote` + `merge-base --is-ancestor` | push state, 2 controls | round-1 ON ORIGIN, round-2 LOCAL, 23 ahead |

## 7. OPEN AT WINDOW CLOSE

- IAM-r-5 (slot ~6) and IAM-r-6 (slot ~5) in flight; drain both.
- `COMPLETION_REPORT.round2.json`, then the round-2 drain-end read to `1.0.0_SA_CTO~Z`.
- Tear down worktrees 5 and 6 once their queues empty.
- **Z-S11 stays ARMED by the CVO's explicit choice:** it accepted the ask that IAM-r-6's AC1 and AC3
  not be credited, and said the disarm cannot discharge until that L9 happens.
