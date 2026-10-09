# NFRA_GATSCP decomposition -- ROUND 2, the enrichment list of the round-1 analysis (issuer 2.0.0_SA_COO~N1; cut 2026-10-09)

**Status: CUT for one issuance.** FROZEN at the cut.

**Cut on:** `ledger/ROUND_ANALYSIS.round1.md` @5c65160327 (1.0.0_SA_CTO~DELL1; FWD-1 REALIZED; rulings R1-R3; section 3, six items),
PRD v0.2 @7cb6183997. Placement: dell1, except GS-e-2 (site Z, a Codex lane).

## Measured at the base (box/dell1 7611122124, 2026-10-09 ~10:0xZ; read-only agent at HEAD 32c925520c plus the issuer's dry runs)

1. **FWD-5 (R1).** `box-sync.sh` `grade_merge` (:104-131) returns at :112 ("grade SKIP") when the graded set is empty, before the
   row gate or the tree check runs, so a sync prints nothing about standing defects. Both tools already show standing defects when
   given an act that belongs to no project: `missions-tree-index.py check --staged --act <non-project path>` puts every violation
   STANDING, rc 0, and prints `ACT SCOPE: in-act=0 STANDING=m`; `surprise-corpus-validate.py --act <non-channel path>` puts every
   NEW tuple STANDING, still refuses a RESOLVED tuple, and prints its `SCOPE:` line.
2. **FWD-2.** A commit staging only `org/surprise_channel/.corpus-baseline.json` runs no corpus pass: `CHANNEL_RE`
   (`surprise-row-gate.py:61-66`) does not match it, so `main` returns early (:3961-3965). Its lane is `CVO_WORKSPACE`
   (`.owned-paths.yaml:1892`), which also admits the CTO and COO. With `--act <the baseline>`, a reset (a dropped tuple) would
   surface as a NEW failure in another project's document and print STANDING, not refuse. So "resetting the known-errors list
   stays a refusal" is false today. The own-rows half of FWD-2 is met by GS-t-1 (r2_baseline_reset arm 2 passes at the base).
3. **FWD-3.** Met by GS-t-2 at the gate and through the commit hook: a commit to one project lands beside another project's
   register drift with `STANDING`, and a project the act touches refuses. No build. It is exercised at this round's close by a
   real commit (the issuer's ROUND_CLOSE flip), so no cell is cut for coverage alone.
4. **FWD-4.** `derive --write` is whole-estate and reads the working tree only (`--staged applies to check only`, :1145-1147);
   `compose_index(self, t)` (:383) composes one row. safe-commit has no call to the tool. The insertion point is after the merge
   re-check (:754) and before `IN_SCOPE` (:757). Precedent for adding a path inside the act: the naming-log block (:1109-1118).
5. **FWD-6.** Inside this project's two gates, one working-tree reader remains. The tree hook's `close_gate` falls back to the
   working tree for dep_stage (`missions-tree-check.sh`, the `< "$ROOT/$p"` line), and `round-close-check.py` (500 lines) reads
   orders, proofs and rows from the working tree. Other gates on the commit path read the working tree or grade beyond the act
   (commit-gate, to-pipeline-gate, to-decomp-ref-lint, owned-paths YAML, mstr-ledger, pipescript-suite, rcg-manifest). They are
   outside C-SCOPE and are filed as row NFRA_GATSCP-D1-S5 for the CTO.
6. **FWD-7 (R3).** `crossbox-call.py` checks that the body and the crossbox file are committed LOCALLY only (`tracked_clean`
   :229-236; `line` :304-311); nothing checks origin. A manager sends the bus line by hand (`agentbus-sqs.sh send`, then `sent`);
   no automated send path exists, and nothing links issuance to `open`. Serial to box: only site Z has `lane_letters` (["Z"],
   DEVICES.json), so a `~Z*` lane is sitez. Site Z's Codex lanes: `0.7.0_AE_CloudOps~ZV`, `~ZQ`, `~ZC`, `~ZW`. Site Z's
   AGENTS.md @a55888e3a2 admits a 2.0.0_SA_COO-issued mission-tree order to a full suffixed serial with no seat-home copy.

## Rule 24 record

**The cell set.** Domain: the analysis's six items. Subtraction:

| item | cell |
|---|---|
| 1 FWD-5 / R1 | `GS-e-1` |
| 2 FWD-7 / R3, the live read | `GS-e-2` (site Z) |
| 2 FWD-7, the remaining delivery half | `GS-e-3` |
| 3 FWD-2 | `GS-e-4` (the reset half; the own-rows half is met) |
| 4 FWD-3 | none: met (measurement 3); exercised at the close |
| 5 FWD-4 | `GS-e-5` |
| 6 FWD-6 | `GS-e-6` (inside C-SCOPE); the rest is row D1-S5 |

Six items, six cells, none uncovered. Same grain: one gate or tool and its caller per cell. One intent each. State: a cell's status
is one of `NOT_EVALUATED`, `PASS`, `FAIL`, `REFUSED`; every cell is `NOT_EVALUATED` at the cut.

**The sync's standing line** (R1, a schema this cut authors). One line per sync: `box-sync: <N> standing`, where N counts the
`STANDING ` lines the sync printed, 0 included. A sync with an empty graded set still runs both tools with an act that belongs to no
project (information only: their exit codes never refuse that pass). A sync with a non-empty graded set grades exactly as round 1
did (refusal power unchanged) and adds the same count line.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE -- no schedule is created or changed (box-sync's scheduled task keeps its trigger).
- `comp-iam`: DECLARED-NOT-APPLICABLE -- no IAM is touched; the agent-bus send in GS-e-3 is an existing path, driven by a fake
  command in its test.
- `comp-adversary`: RUN, in the cut's own arms. Every build criterion carries a difference control: the same plant in the act's own
  file is refused (P1), or the working-tree read is the control (GS-e-6). BLIND: GS-e-5 AC2 and GS-e-6 AC2 are structural; their
  seams are the issuer's real ROUND_CLOSE commit at the close.

## The cells

| cell | what | serves | placement | risk | status |
|---|---|---|---|---|---|
| `GS-e-1` | box-sync's `grade_merge` shows standing defects on every sync, as information, plus `box-sync: N standing` | FWD-5 | dell1 | LOCAL | NOT_EVALUATED |
| `GS-e-2` | the live read on site Z: a Codex lane runs this order from the mission tree with no seat-home copy and reports round 1's tools present on its box | FWD-7 | sitez | LOCAL | NOT_EVALUATED |
| `GS-e-3` | crossbox delivery: `line` refuses until the order's and the crossbox file's commits are on origin; `issue --order` opens the crossbox file for an addressee on another box; `send-pending` (a manager only) sends what is admitted, all times UTC | FWD-7 | dell1 | LOCAL | NOT_EVALUATED |
| `GS-e-4` | a commit that stages the corpus baseline runs the corpus pass with every finding in-act, so a reset refuses | FWD-2 | dell1 | LOCAL | NOT_EVALUATED |
| `GS-e-5` | `derive --staged --only CODE --stdout` composes one entry from the staged row; safe-commit regenerates and stages it inside the act, or refuses with the reason | FWD-4 | dell1 | LOCAL | NOT_EVALUATED |
| `GS-e-6` | `round-close-check.py --staged` reads the project's orders, proofs and rows from the index; the tree hook's close gate passes it and drops its working-tree fallback | FWD-6 | dell1 | LOCAL | NOT_EVALUATED |

## Interfaces fixed at the cut

- `box-sync.sh`: after grading (or instead of the empty-set SKIP's silence), one `box-sync: <N> standing` line per merge graded,
  `grade` mode included.
- `surprise-row-gate.py`: a dispatched `org/surprise_channel/.corpus-baseline.json` triggers the corpus pass;
  `surprise-corpus-validate.py`: when the baseline path is among the `--act` paths, every finding is in-act.
- `missions-tree-index.py derive --staged --only CODE --stdout`: prints the entry's JSON; rc 1 with a reason when it cannot be
  composed; writes no file. safe-commit writes that JSON to `org/projects/<CODE>.json`, stages it and appends it to PATHSPEC.
- `round-close-check.py --staged`: the same verdict line, every input from the index git resolves.
- `crossbox-call.py`: `line` (origin check added), `issue --order <path>`, `send-pending [--dry-run]`; the send command is
  overridable by `CROSSBOX_SEND_CMD` for tests.

## Dependency edges

None. GS-e-2 reads round 1's tools only. GS-e-3's issuance and send hookups belong to no cell: the issuer adds the /dispatch line at
the merge, and /govern's line is 0.0.0_AB_MSTR's skill (routed at the merge). M = 6 chains.

## Write sets (disjoint)

- **GS-e-1:** `.tools/box-sync.sh`.
- **GS-e-2:** `org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.7.0_AE_CloudOps~ZQ/` only.
- **GS-e-3:** `.tools/crossbox-call.py`, `.tools/tests/test_crossbox_deliver.py`.
- **GS-e-4:** `.tools/surprise-corpus-validate.py`, `.tools/surprise-row-gate.py`.
- **GS-e-5:** `.tools/missions-tree-index.py`, `.tools/safe-commit.sh`.
- **GS-e-6:** `.tools/round-close-check.py`, `.tools/git-hooks/missions-tree-check.sh`.
- Each: the project's `surprise-channel/investigations/INVESTIGATION_v1.md` (append-only; the merge unions it).

## The checks (files, dry-run at the base box/dell1 7611122124)

`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round2_prep/checks/`.

| check | cell | base |
|---|---|---|
| `r2_sync_standing.py` | GS-e-1 AC1 | FAIL as expected (no count line; SKIP silent); own-defect arm PASS |
| `r2_sitez_read.py` | GS-e-2 AC1 | PASS as expected on dell1 (a control; the lane runs it on site Z) |
| `.tools/tests/test_crossbox_deliver.py` (built by the cell) | GS-e-3 AC1 | FAIL as expected (absent) |
| `crossbox-call.py --selftest` | GS-e-3 AC2 | PASS as expected (a control) |
| `r2_baseline_reset.py` | GS-e-4 AC1 | FAIL as expected (reset arm rc 0: early return) |
| `r2_derive_one.py` | GS-e-5 AC1 | FAIL as expected (unrecognized arguments) |
| `r2_safecommit_regen.py` | GS-e-5 AC2 | FAIL as expected (no call) |
| `r2_close_staged.py` | GS-e-6 AC1 | FAIL as expected (no --staged); worktree control arm PASS |
| `r2_closegate_staged.py` | GS-e-6 AC2 | FAIL as expected (no --staged; fallback present) |

## The close (the issuer's real runs, not cells)

The ROUND_CLOSE flip of round 2 is one real commit of a project's stage made through safe-commit with no manual derive (FWD-4's
DONE WHEN, and the hook's staged close gate, FWD-6), landing beside whatever standing defects the box carries (FWD-3). FWD-2 and
FWD-3's "one refused on its own" arms are run on a never-pushed QA branch, as ruling J did for FWD-1. FWD-5 is read on the next real
box-sync pass (its `N standing` line). FWD-7 is graded on GS-e-2's ACK and receipt.
