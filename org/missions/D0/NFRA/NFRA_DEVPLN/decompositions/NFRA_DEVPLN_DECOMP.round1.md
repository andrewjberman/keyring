# NFRA_DEVPLN decomposition -- round 1, the THREAD: one feature from a box branch, through an approval row and the one merge-forward, into a chosen-set promote (issuer 2.0.0_SA_COO~DV; cut 2026-10-13 ~18:3xZ)

**Status: ISSUED in one issuance.** The issuance commit carries the `fanout:` line. The decomposition is FROZEN at the cut.

**Input.** PRD `prd/NFRA_DEVPLN_PRD.md` v0.2 @d2b7385bee (sections 1-3 arc and order, section 7 manifest S01-S07, DEC-1..8). Sign-off read at the cut
(`python .tools/prd-signoff.py status NFRA_DEVPLN`): ratified-text SIGNED by 3.0.0_SA_CVO~L, current; brief half SIGNED (auto, the CRO wrote the brief);
verdict ADMITTED. Brief `docs/briefs/nfra-devpln-per-box-portal-dev-approval-brief-20261013.md` @5386676d4f. CTO note (msg 108811): round 1 = the FWD-6
settlement first, then the FWD-1 thread.

## Thread (FWD-1), one hop per line

1. A feature branch `cand/<box>/<slug>` is built in a box's own worktree, cut from the last PROD release -> C-BRANCH doc (`DP-b-4`).
2. The branch is registered as an `approval` row on the building box's open-calls list -> `DP-b-1`, `DP-b-5`.
3. Andrew closes the row `approved` or `declined` in one act -> `DP-b-1` (the close) over the open-calls list he already reads.
4. The one merge-forward writes DEV from an approved row, with trailers -> `DP-b-2` (script) and `DP-g-1` (the gate, `1.0.0_SA_CTO`).
5. A promote ships a chosen set from a release branch cut from PROD -> `DP-b-3`.
6. The backlog is settled so the first chosen-set promote reads "nothing unapproved" -> `DP-s-1` (the list) and issuer acts A2, A3 (the back-merge, Andrew's word).
7. The client's page: the promote reaches PROD under the push law -> issuer act A1 (the real run), at the close.

## Measured at the base (issuer, ~18:2xZ, box/laptop @5bd9bd2ed2, portal origin fetched)

1. Portal `origin/DEV` f6ef1d2548, `origin/PROD` 15c9754975: DEV 201 ahead of PROD, PROD 33 ahead of DEV (the brief read 32; the firm-access
   carrier landed on PROD since). Merge base 2d42e9b733 per the brief.
2. `.tools/open-calls.py` line 88: `KINDS = ("fork", "act")`. No `approval`. No `.tools/portal-merge-forward.sh`, no `portal/CONTRIBUTING-BOXES.md`.
3. `.tools/hooks/never-rules-gate.sh` lines 643-760: the DT carve-out (PROD and DEV, push only), the FAST-lease carve-out (line 702), the test-only carve-out
   (line 727); the integrator is the base rule. The gate keys on the push command text and the caller's serial.
4. `org/mcp/drive_mode/` holds 8 lease files; every one carries `expires_at 2026-10-08T20:22:27Z`, so none is live today (brief Part VII, read).
5. `/prod-deploy` Step 4 merges live `origin/DEV` into PROD in an ephemeral worktree (`git merge --no-ff origin/DEV`), then `git push origin PROD`.
   `.claude/agents/worker.md` carries no portal step. The laptop portal checkout has 5 worktrees, two of them detached scratch copies and one `prunable`.
6. `to-pipeline-gate.py` GATE (i) refuses a task order whose `<issued_to>` is a Tier-1 serial, so the CTO's gate edit (`DP-g-1`) cannot be a task order.

## Issuer rulings inside this decomposition (recorded here and as surprise rows for the CTO's round-1 analysis)

- **R1, the ancestry check reads first-parent.** C-PROMOTE says a release is refused when any `PROD..release` commit lacks `Approved-By`. A feature branch's own
  commits carry no trailer, so the literal walk refuses every honest release. The cell reads the walk with `--first-parent` (the release's merge commits carry the
  trailers) and adds the per-feature binding below. The CVO's hole (a DEV-cut branch carrying DEV commits beneath it) is closed at registration: `DP-b-5` refuses
  a row whose branch holds a commit that is on DEV and not on PROD.
- **R2, the approval binds the branch head.** The row records `head_sha` and `commits` at registration. The merge-forward and the release builder refuse a branch
  whose head differs from the row (a later push needs a fresh row).
- **R3, the class rule lives in `approval-status`.** `valid=yes` is printed only when the closing identity satisfies the class (client-facing: Andrew or a live FAST
  lease; opal-internal: Andrew or a `_SA_CTO` serial; test-only: no row needed). The merge-forward and the release builder read that one line, so the rule is stated once.
- **R4, the FAST-lease route is a row.** A live lease's seat runs `open-calls.py approval-lease` (cell `DP-b-5`), which writes the row CLOSED `approved` with
  `by` = `FAST lease <file>`; the merge-forward then finds a valid row. The script does not read lease files itself. This is the PRD's "the lease is read as the
  approval" through one record instead of two readers.
- **R5, interfaces are pinned, not waited on.** `DP-b-2` and `DP-b-3` consume `approval-status`, whose output line is pinned below. Each tests against a fixture
  command (`OPAL_APPROVAL_STATUS_CMD`); the REAL seam is probed by the issuer at the drain after `DP-b-1` merges (act A4). That is why no edge joins the cells.

## Pinned interfaces

`open-calls.py` additions (cells `DP-b-1`, `DP-b-5`):

- `python .tools/open-calls.py add --kind approval --project NFRA_DEVPLN --box <box> --branch cand/<box>/<slug> --purpose "<text>" --pages "<p1,p2>" --class client-facing|opal-internal|test-only --how "<how to look>" --portal <portal repo path>`
  (`--subject` optional for this kind, default `approval: <branch>`).
- `python .tools/open-calls.py close <id> --ruled-by andrew --ruling-file <path> --decision approved|declined` (the existing close, plus `--decision`).
- `python .tools/open-calls.py approval-lease --branch <b> ... (same fields as add) --lease-file <path>`.
- `python .tools/open-calls.py approval-status --branch <b> [--store-dir <dir>]` prints exactly ONE line:
  `APPROVAL branch=<b> state=<ABSENT|OPEN|APPROVED|DECLINED> valid=<yes|no|-> row=<id|-> by=<who|-> head_sha=<sha|-> commits=<n|-> class=<client-facing|opal-internal|test-only|-> box=<box|-> pages=<p1,p2|->`
  rc 0 when the store is readable (including ABSENT), rc 2 when it is not.
- Row shape: `kind: "approval"`, `approval: {box, branch, purpose, pages[], class, how, head_sha, commits}`, `state: OPEN|CLOSED`, `closed: {at, by, ruling, decision, ruled_by}`.
  The newest row by `opened_at` for a branch wins. The box comes from the branch name `cand/<box>/<slug>`; the store is that box's
  `org/devices/state/<box>/open_calls.json` in the working tree, else `git show origin/box/<box>:<that path>`; `--store-dir` (a directory holding `<box>/open_calls.json`) overrides for tests.
- Consumers call `${OPAL_APPROVAL_STATUS_CMD:-python .tools/open-calls.py approval-status} --branch <b>`.
- Trailers on a merge commit: `Feature: <branch>` and `Approved-By: <who> @<row id>` (a test-only merge: `Approved-By: test-only @-`).

## Rule 24 (four postulates)

**Domain:** the manifest S01-S07 and the thread's seven hops.

**Subtraction (MECE):**

| Hop / manifest row | Served by |
|---|---|
| hop 1 (branch convention), S06 | `DP-b-4` |
| hop 2, S01 | `DP-b-1`, `DP-b-5` |
| hop 3 (Andrew's close) | `DP-b-1` (`--decision`) |
| hop 4, S02 | `DP-b-2`; S03 -> `DP-g-1` (CTO) |
| hop 5, S04 | `DP-b-3` |
| hop 6, S05 | `DP-s-1` (the list) plus issuer acts A2, A3 (back-merge, Andrew's per-group word) |
| hop 7, S07 | issuer act A1 (the real run at the close) |

No hop or row is unowned. Held for later rounds, per PRD section 3: FWD-3 refusal arm on every box, FWD-4 per-commit read, FWD-7 line in the gate, FWD-2 declined arm,
FWD-5's negative-arm promote.

**Same grain:** one script, one tool extension or one document per cell. **Intent coherence:** each cell builds one hop's adapter. **State coherence:** no cell pushes,
merges into a shared branch, or changes a live seat. `DP-b-2` and `DP-b-3` write only a temporary worktree and branch in the repo they are pointed at; the default is no push.

## Cells

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `DP-b-1` | `approval` kind in `open-calls.py` (add, close `--decision`, `approval-status`), plus the rule-24 record for the enum widening | FWD-2, FWD-4; S01 | LOCAL | `0.9.0_WK_NFRA_DEVPLN~1` |
| `DP-b-5` | registration facts (`head_sha`, `commits`, DEV-overlap refusal via `--portal`) and `approval-lease`; same file as `DP-b-1`, so it runs after it in slot ~1 | FWD-1, FWD-3; S01, S02 (R1, R4) | LOCAL | `~1` |
| `DP-b-2` | `.tools/portal-merge-forward.sh`: refuses without a valid approved row, merges (never rebases) into DEV in an ephemeral worktree with trailers; no push unless `--push` | FWD-1, FWD-3, FWD-4; S02 | LOCAL | `~2` |
| `DP-b-3` | `.tools/portal-release-build.sh --features <list>` (release branch from PROD, trailer merges, first-parent ancestry check) and the `/prod-deploy` chosen-set step | FWD-5; S04 | LOCAL | `~3` |
| `DP-b-4` | `portal/CONTRIBUTING-BOXES.md` (one page) on a portal branch, and the worker definition's portal step | FWD-3, FWD-7; S06 | LOCAL | `~4` |
| `DP-s-1` | `.tools/portal-settlement-list.py`: the per-group list for Andrew (DEV-not-PROD groups, PROD-only commits, branches with work not on DEV), run once into `ledger/SETTLEMENT_LIST.md` | FWD-6; S05 | LOCAL | `~5` |
| `DP-g-1` | the gate edit: `never-rules-gate.sh` portal DEV/PROD limbs collapse to the one merge-forward (spec in `org/tier1_exec/2.0.0_SA_COO~DV/deliverables/DP-g-1_gate_edit_cell.md`) | FWD-3, FWD-7; S03 | LOCAL | `1.0.0_SA_CTO` (NOT a task order: GATE (i)) |

## Dependency chains and fan-out

Edges: `DP-b-1 -> DP-b-5` (one file, `.tools/open-calls.py`). Every other cell is its own chain (R5). M = 5 chains over 6 task-order cells; `DP-g-1` is the CTO's own act.
Write sets are disjoint across chains: `open-calls.py` + its test + the record (slot 1); `portal-merge-forward.sh` + its test (slot 2); `portal-release-build.sh` + test + `prod-deploy/SKILL.md`
(slot 3); `portal/CONTRIBUTING-BOXES.md` + `.claude/agents/worker.md` (slot 4); `portal-settlement-list.py` + test + `ledger/SETTLEMENT_LIST.md` (slot 5).

## Battery (L5)

Round 1 of a threaded project: every lens `DECLARED-NOT-APPLICABLE` ("thread round; the lens runs on the enrichment round that touches its surface"). `comp-iam`: not applicable,
the thread touches no IAM. Part VII of the brief, read: lease expiry (above, none live); `wk-*` branch ownership and whether its work is on DEV is `DP-s-1`'s output;
portal CI state read by the issuer at the drain; the Dells' checkout shape is not inspectable from this box and is issuer act A5 (one question to dell2's manager at the close).

## Issuer acts (the COO's one real run, at the close)

- **A1 (hop 7, FWD-1):** follow ONE real feature from dell2's branch (the natural case is the Investor Reporting work in `q/dell2/wk-IRPT_BCKEND-167-portal/r1`, rebased by
  its owner onto the PROD release) through register, Andrew's close, `portal-merge-forward.sh`, `portal-release-build.sh`, and the push-law promote. Recorded as one trace.
- **A2 (hop 6):** ask `0.0.0_AB_MSTR` for the PROD-into-DEV back-merge, no rebase, after Andrew's group list is ruled.
- **A3 (hop 6):** put the `DP-s-1` list in front of Andrew as one open call per group and per branch (open-calls, kind `fork`, until the `approval` kind exists).
- **A4 (R5):** at the drain, run the real `approval-status` against a real row and feed it to `DP-b-2` and `DP-b-3`; record the seam probe.
- **A5:** one question to dell2's manager: how its portal checkout is held (nested checkout, separate clone or worktrees).
- **A6:** the CLAUDE.md FAST-lease wording edit is Andrew's act (PRD C-MERGE-FORWARD); listed, not made.
