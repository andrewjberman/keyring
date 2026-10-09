# NFRA_GATSCP decomposition -- ROUND 1, the thread: a worker's drain and a box sync land beside two other projects' standing defects (issuer 2.0.0_SA_COO~N1; cut 2026-10-09)

**Status: CUT for one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** PRD v0.2 @7cb6183997, ADMITTED (`python .tools/prd-signoff.py status NFRA_GATSCP`: ratified-text SIGNED by
`3.0.0_SA_CVO`, current; brief half admitted because `4.0.0_SA_CRO~A` wrote the brief). Brief
`docs/briefs/gitops-gates-scoped-to-the-act-brief-20261009.md` @4c795d29a4. Placement: `dell1` (project row).

**The rectangle is FWD-1's hops.** The PRD carries no THREAD section; the hops below are read from FWD-1's ACCEPT and the
brief's candidate thread (Part I). FWD-2 to FWD-7 are not cut this round (spine L6: on round 1 of a threaded project only
FWD-1 is in scope); the commit-path halves of FWD-2, FWD-3 and FWD-6 ride along because the same gates serve both.

## Measured at the base (box/dell1 d707ef7c27, 2026-10-09 ~07:3xZ; contains CLOUD 3848a4e89b)

1. **The corpus pass grades the whole corpus and has no scope input.** `.tools/surprise-corpus-validate.py` `main(argv)` (:338)
   takes `--write-baseline`, `--json`, `--index`, `--index-rows`; it refuses on any NEW or RESOLVED tuple anywhere (:396-399).
   Documents are read from the index blob (:178-227, 086b594d5e); the SCHEMAS (:61-67) and the BASELINE (:271-276) are read from
   the working tree with `open()`. Base run: 331 documents, 9,940 rows, 4 known, 0 new, 0 resolved, rc 0.
2. **The row gate calls the corpus pass with no paths.** `.tools/surprise-row-gate.py` :3979-3992, `_scv.main([])`; a refusal is
   one more string in `all_v` with no owner. Dispatched paths come from argv or `STAGED` (`_dispatched_from_argv_or_env`,
   :1884-1911). The owning project of a channel path is already derivable: `_folder_identity(rel)` (:69-98).
3. **The tree check is whole-estate and reads the working tree.** `.tools/git-hooks/missions-tree-check.sh` :63 runs
   `missions-tree-index.py check` over every project; its header (:24-27) names the worktree read as a known hole.
   `missions-tree-index.py` reads the filesystem (:143, :184) except `_index_only_projects` (:194-237); it already takes
   `--contract --root --projects --directives --macros` overrides (:46-53, :813-828). A violation is `(rule_id, path, detail)`;
   its project is the last segment of the tree home or the flat file's stem. Base run: 0 violations.
4. **box-sync grades a merge with the row gate only.** `.tools/box-sync.sh` `grade_merge` (:100-119) grades on a private GIT_DIR
   with `STAGED=<paths the merge changes against both parents, plus paths both sides changed>`; the tree check is never run
   (`--verify-merge` at :163 is the tree-carry check). Modes are `box|integrate|status` only (:32).
5. **safe-merge's two paths.** The in-tree path commits with `git commit`, so the pre-commit hook (and so missions-tree-check.sh)
   fires on the merged index. The fast lane (`_sm_fast_lane`, :517-) lands by `commit-tree`: no hook fires and no tree check runs.
6. **No carrier for a standing defect exists** (`open-calls.py` has no such kind). FWD-1 asks only that each error is printed and
   named to its owner; delivery onto a carrier is FWD-5, not this round.

## Rule 24 record

**The cell set.** Domain: FWD-1's hops. Subtraction from the printed hop list:

| hop | what | cell |
|---|---|---|
| 1 | a fresh channel error in another project is printed `STANDING <CODE>` and does not refuse; the act's own documents refuse as today | `GS-t-1` |
| 2 | a register mismatch in another project is printed `STANDING <CODE>` and does not refuse; a project the act touches refuses as today; read from the staged bytes | `GS-t-2` |
| 3 | a worker's drain lands through `safe-merge.sh`: in-tree path = hops 1+2 via the hooks; fast lane = the tree check wired | `GS-t-1` (row gate wire), `GS-t-2` (hook), `GS-t-3` (fast lane) |
| 4 | the box sync lands through `box-sync.sh`: row gate (hop 1) plus the tree check on the merged bytes | `GS-t-3` |
| 5 | nobody repairs by hand | no cell: an absence, proven by the history read at the issuer's one real run |

Five hops, three cells, none uncovered. Same grain: each cell is one gate and its caller. One intent each (who a gate refuses).
State: a cell's status is one of `NOT_EVALUATED`, `PASS`, `FAIL`, `REFUSED`; every cell is `NOT_EVALUATED` at the cut.

**The STANDING line** (a schema this cut authors). Domain: every finding a gate in scope produces when it is given an act set.

| class | condition | refuses |
|---|---|---|
| in-act | the finding's project is a project the act touches | yes, exactly as today |
| `STANDING` | the finding's project is not touched by the act | no; printed `STANDING <CODE> <gate> <path> <detail>` |
| always | a RESOLVED baseline tuple; a baseline that cannot be read; a gate that cannot evaluate itself | yes (C-SCOPE; fail-closed) |

Tested in the order `always`, `in-act`, `STANDING`, so the classes are disjoint and `STANDING` is the remainder. Without an act set
a gate behaves exactly as today (the whole estate is in-act). Cut decision, stated: for the tree check, an act that stages a
shared register file (`org/missions/DIRECTIVES.yaml`, `org/missions/MACROS.yaml`, `org/standards/PROJECT_TREE.contract.json`)
puts every project in-act, because such an edit can introduce a violation in any project. State: a STANDING line never moves
the gate's exit code; only the act's own findings and the `always` class do.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE -- thread round; no schedule is created or changed.
- `comp-iam`: DECLARED-NOT-APPLICABLE -- the thread touches no IAM.
- `comp-adversary`: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches its surface. The
  cut's own adversarial arms: every criterion carries a difference control (the same plant, the act's own path: refused), so
  a gate that stops refusing passes no criterion. BLIND: the checks plant in a private index; a defect that exists only in a
  working tree is not exercised (by design: C-BYTES says the working tree is never graded).

## The cells

| cell | what | serves | hop | placement | risk | status |
|---|---|---|---|---|---|---|
| `GS-t-1` | the corpus pass takes the act's documents (`--act PATH`, repeatable); a NEW failure or malformed block outside them prints `STANDING <CODE>` and does not refuse; inside them it refuses as today; a RESOLVED tuple always refuses; the schemas and the baseline are read from the graded index; the row gate passes its dispatched paths | FWD-1 hops 1, 3 | 1, 3 | dell1 | LOCAL | NOT_EVALUATED |
| `GS-t-2` | the tree check reads every input from the git index (`check --staged`, honouring `GIT_INDEX_FILE` and `GIT_DIR`) and takes the act's paths (`--act PATH`, repeatable; `--act-from-env VAR`); a violation in a project the act does not touch prints `STANDING <CODE>` and does not refuse; `missions-tree-check.sh` passes the staged list and `--staged` | FWD-1 hops 2, 3 | 2, 3 | dell1 | LOCAL | NOT_EVALUATED |
| `GS-t-3` | box-sync's `grade_merge` and safe-merge's fast lane run the `GS-t-2` tree check on the merged bytes with the merge's graded path set as the act; box-sync gains a read-only `grade P1 P2` mode that computes the merge and grades it, landing nothing | FWD-1 hops 3, 4 | 3, 4 | dell1 | LOCAL | NOT_EVALUATED |

Risk is `LOCAL`: repository tooling and tests; nothing served moves and nothing deploys.

## Interfaces fixed at the cut

- `surprise-corpus-validate.py`: `--act PATH` (repeatable). With at least one `--act`, a tuple whose document is not an act
  path, and a malformed block in such a document, prints `STANDING <CODE> surprise-corpus <doc_rel> <row_id> <json_pointer>`
  and does not count toward the exit code. `<CODE>` is the tree project folder, or the flat `org/surprise_channel/<CODE>/`
  folder. Without `--act`: unchanged. `main(argv)` keeps its signature.
- `surprise-row-gate.py`: calls `_scv.main(["--act", p, ...])` with every dispatched channel path.
- `missions-tree-index.py check [--staged] [--act PATH ...] [--act-from-env VAR]`: `--staged` reads the contract, the tree rows,
  the flat index, `DIRECTIVES.yaml`, `MACROS.yaml` and the close artifacts from the index git resolves (`GIT_INDEX_FILE`,
  `GIT_DIR`), never the working tree. A violation outside the act's projects prints `STANDING <CODE> <rule_id> <path> <detail>`.
  rc 0 when no in-act violation remains, 1 otherwise, as today. `derive` is unchanged.
- `missions-tree-check.sh`: runs `check --staged --act-from-env OWNED_PATHS_STAGED_FILES` (the staged list it already holds).
- `box-sync.sh grade P1 P2`: any seat, read-only (no fetch, no ref moved, no lock taken, no audit row): `git merge-tree`, then
  `grade_merge`, which now also runs `missions-tree-index.py check --staged --act ...` under the same private GIT_DIR with the
  same path set. Exit 0 pass, 1 refused, 4 conflict.
- `safe-merge.sh` `_sm_fast_lane`: the same tree-check call on its private GIT_DIR and its graded path set.

## Dependency edges

- `GS-t-2 -> GS-t-3`: box-sync and the fast lane call `check --staged --act`.

Chains: `t-1`; `t-2 > t-3`. M = 2. `fanout: 2 of 2 chains, cap 8`: slot `~1` takes `GS-t-1`; slot `~2` takes `GS-t-2`, then
`GS-t-3` after `GS-t-2` is merged.

## Write sets (disjoint)

- **GS-t-1:** `.tools/surprise-corpus-validate.py`, `.tools/surprise-row-gate.py`.
- **GS-t-2:** `.tools/missions-tree-index.py`, `.tools/git-hooks/missions-tree-check.sh`, `.tools/tests/test_missions_tree_index_selftest.py`.
- **GS-t-3:** `.tools/box-sync.sh`, `.tools/safe-merge.sh`.
- Each: the project's `surprise-channel/investigations/INVESTIGATION_v1.md` (append-only; the merge unions it).

## The checks (files, dry-run at the base)

`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round1_prep/checks/`. Each plants its defect in a private copy
of the index, never in the working tree or a ref. Bystander: `LGIC_BLANKFIX`. Act: `NFRA_GATSCP` or `NFRA_CTLPLN`'s channel.

| check | cell | base |
|---|---|---|
| `r1_corpus_scope.py` | GS-t-1 AC1 | FAIL as expected (bystander arm rc 1, no STANDING) |
| `r1_rowgate_seam.py` | GS-t-1 AC2 | FAIL as expected (bystander arm rc 1) |
| `r1_corpus_bytes.py` | GS-t-1 AC3 | FAIL as expected (baseline read from the working tree: rc 0) |
| `r1_tree_scope.py` | GS-t-2 AC1 | FAIL as expected (no `--staged`: usage rc 2) |
| `r1_treehook_seam.py` | GS-t-2 AC2 | FAIL as expected (own arm rc 0: the hook reads the working tree) |
| `r1_tree_selftest.py` | GS-t-2 AC3 | FAIL as expected (green half PASS 38/38; no `--staged`/`--act` arm) |
| `r1_boxsync_grade.py` | GS-t-3 AC1 | FAIL as expected (no `grade` mode: usage rc 2) |
| `r1_fastlane.py` | GS-t-3 AC2 | FAIL as expected (fast lane not wired; self-test arm PASS) |

## The close (the issuer's one real run, not a cell)

FWD-1 is graded on one real drain and one real box sync, both landed, while a fresh channel error and a register mismatch of two
other projects stand on the box. This round's own worker drains are the real project work. The arrangement of the two standing
errors at the close (placed on purpose, as FWD-1's ACCEPT permits) is the issuer's, recorded with the trace under
`deliverables/2.0.0_SA_COO~N1/`.
