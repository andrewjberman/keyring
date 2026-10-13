# NFRA_DEVPLN decomposition -- round 2, ENRICHMENT: the live run on row 9e8a, the per-commit read, one repair batch (issuer 2.0.0_SA_COO~DV; cut 2026-10-13 ~21:0xZ)

**Status: ISSUED in one issuance.** The issuance commit carries the `fanout:` line. The decomposition is FROZEN at the cut.

**Input.** The L10 round analysis `org/missions/D0/NFRA/NFRA_DEVPLN/ledger/ROUND_ANALYSIS.round1.md` @14a0501ee5 (1.0.0_SA_CTO msg 108885: "cut round 2 in one issuance"), ENRICHMENT LIST items 1-6.
**Cut on.** PRD v0.3 @14a0501ee5. `python .tools/prd-signoff.py status NFRA_DEVPLN` at the cut: ADMITTED; ratified-text SIGNED by 3.0.0_SA_CVO~L (current by ENDPOINT hash), brief SIGNED (auto). Lease read FULL.

## Measured at the base (issuer, ~21:0xZ, box/laptop, portal origin fetched)

1. Row `laptop-20261013T200117Z-9e8a` (`cand/laptop/contributing-boxes`): `APPROVED valid=yes by=1.0.0_SA_CTO head_sha=07f065e69f54 commits=1 class=opal-internal`. The branch tip is still `07f065e6`.
2. Portal `origin/PROD` = `63c4f9e3` (the settlement commit). `origin/DEV` = `a577cba5`: 7 commits PROD lacks, all from three IRPT_ANLREQ merges landed by `0.0.0_AB_MSTR~DELL2` at 16:04-16:05 -0400, none carrying an `Approved-By:` trailer (0 of 7). This is the organic unapproved case FWD-4 and FWD-5 are about.
3. `.tools/tests/test_open_calls.py` prints `OPEN-CALLS-TEST cases=0/2 ok=False` (FileNotFoundError on the scratch state file) at the base.
4. `approval-lease --help` lists `--project` with a default.

## Cells and issuer acts

| item | cell / act | what | risk | served by |
|---|---|---|---|---|
| E1 | `DP-x-1` | FWD-1 hops 4-7 on row 9e8a: after the integrator pushes the merge to DEV, the DT promotes the chosen set naming only `cand/laptop/contributing-boxes`; the file is read on PROD; both trunks are measured after | SERVED | `0.4.0_DT_ClientPlatform` (task order) |
| E1 | act A1 | the integrator `0.0.0_AB_MSTR` runs `bash .tools/portal-merge-forward.sh cand/laptop/contributing-boxes --push` (admission (i), until S03) | -- | ask, one message |
| E2 | `DP-g-1` | S03 gate edit; the round-1 cell file stands (`org/tier1_exec/2.0.0_SA_COO~DV/deliverables/DP-g-1_gate_edit_cell.md`); `1.0.0_SA_CTO` lands it at its bytes | -- | CTO (not a task order, GATE (i)) |
| E2 | act A7 | the FWD-3 refusal arm: one direct DEV push from a box seat refused, and the same work through the route, read after S03 lands; the gate bytes read on all four box branches | -- | issuer, after S03 |
| E3 | act A10 | a dell2 Investor Reporting feature through the route (client-facing, Andrew approves): needs a dell2 builder seat; the pivot parks IRPT work, so the CTO places it. Asked in the drain-end read, not cut | -- | CTO / dell2 manager |
| E4 | act A9 | the nine branches as ruled: 5 contained refs retired (a tag first where the tip is not an ancestor of DEV), 4 unique-patch branches to their owners by name; settlement list re-run | -- | issuer |
| E5 | `DP-c-1` | FWD-4's per-commit read: `.tools/portal-dev-approval-read.py` prints, for every first-parent commit on DEV since the settlement commit, approved with its feature and approver, or UNAPPROVED | LOCAL | `0.9.0_WK_NFRA_DEVPLN~1` |
| E5 | act A8 | FWD-2 declined arm and FWD-5 negative arm: one deliberately tiny second candidate registered, declined by the box CTO, then refused by the merge-forward (`declined`) and by the release builder; read back by `approval-status` | -- | issuer + box CTO |
| E5 | (no cell) | FWD-7 in `CONTRIBUTING-BOXES.md`: the page already states the three classes (DP-b-4 item 5); the gate half is `DP-g-1`. No cell is cut for coverage alone | -- | -- |
| E6 | `DP-r-1` | the batch repair: `test_open_calls.py` red at base (W1-S8); merge-forward fetches by default, `--no-fetch` skips (W2-S2); the result line carries `merge=<sha>` (no merge sha without `--push`); `approval-lease` requires `--project` (W1-S7) | LOCAL | `0.9.0_WK_NFRA_DEVPLN~2` (worker-light) |
| E6 | (resolved) | W3-S3: DP-b-3 already added the `PROMOTE-LIST` rows to the Step 8 receipt table (`.claude/skills/prod-deploy/SKILL.md` line 282). Nothing to repair | -- | -- |

Carried and not cut (Andrew's act): the CLAUDE.md FAST-lease line edit.

## Rule 24 (four postulates)

**Domain:** the six items of the analysis's ENRICHMENT LIST. **Subtraction:** E1 -> DP-x-1 + A1; E2 -> DP-g-1 + A7; E3 -> A10 (carried); E4 -> A9; E5 -> DP-c-1 + A8 (+ DP-g-1 for the gate's FWD-7 line); E6 -> DP-r-1 (+ W3-S3 resolved). No item is unowned.
**Same grain:** one tool, one repair batch or one live run per cell. **Intent coherence:** each cell serves one outcome of the list. **State coherence:** the two worker cells push nothing and touch no shared branch; `DP-x-1` is the only cell that moves a served trunk (PROD), under the push law and a change-management entry.

## Dependency chains and fan-out

Edges: none between cells. `DP-x-1` waits on act A1 (a precondition its face checks with a git command, not an edge). `DP-r-1` edits `.tools/portal-merge-forward.sh`, which A1 runs: the live run uses the script as merged at HEAD when A1 fires, and the repair merges at its own drain. Write sets: `DP-c-1` writes a new tool, its test and one ledger read; `DP-r-1` writes four existing files; `DP-x-1` writes the change-management ledger and its deliverable. Disjoint.
M = 3 chains; workers N = 2 (the third chain is a seat's order); cap 8.

## Battery (L5)

Enrichment round: every lens `DECLARED-NOT-APPLICABLE` with reason "thread round; the lens runs on the enrichment round that touches its surface" is NOT used here; the surfaces touched are the portal DEV/PROD trunks and one PROD promotion. `comp-iam`: not applicable, no IAM. `comp-adversary`: RUN as a BLIND-stated read: the denominator is the issuer's own read of the three cells' invocations (below); blind to the filesystem around the cited paths. Findings inlined where they touch a cell: (1) a promote makes DEV and PROD diverge again by one merge commit each (the merge-forward's on DEV, the release's on PROD), though content is equal; `DP-x-1` MEASURES both directions after the push and reports it (a row if non-zero), it does not resolve it; (2) the 7 unapproved DEV commits stay behind on DEV by construction (the release is cut from PROD), which is the FWD-5 evidence; `DP-x-1` prints them.
