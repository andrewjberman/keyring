# NFRA_CLDGRPH, the second parallel canonical run: L5 decomposed and L6 ROUND 1 dispatched from a fresh lane in 93 minutes -- 2.0.0_SA_COO~A (lane A, logged in the base folder because the lane folder does not exist yet)

**archetype:** COORDINATE
**secondary_archetypes:** SCRIBE

**Date:** 2026-09-03
**Task Order:** ad-hoc -- NFRA_CLDGRPH L5 + L6 on Andrew-direct at the `1.0.0_SA_CTO~A` terminal ~05:1xZ (@`8e134cc126`)
**Status:** IN PROGRESS (ROUND 1 at L7; two deliverable reports awaited)
**Window:** 05:17Z (register) -> 06:50Z. First log of this seat; no prior log for the lane.

---

## Objective

Stand up `2.0.0_SA_COO~A` as the L5/L6 owner of NFRA_CLDGRPH (Andrew: *"work with COO~A and CVO~A in addition to any agents needed for dispatched TOs"*), land the tree decomposition over PRD v0.4's manifest, and open ROUND 1 at L6 with seats this lane spawns -- the whole thing in parallel with the base fabric's NFRA_COMPEFFICACY water test and sharing nothing with it but the spine and the gates.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` | PASS | the A.3 EXERCISE line: a forwarder RAN (104 of 104 resolve bare) |
| comp-read | `--for` on the spine, the L6 gate, the notifier; `--enumerate CELL_ID_RE` / notifier symbols | PASS | the spine's L5/L6 duties + section 3 in one read; the gate's limbs (i)/(iv), the three-value preflight enum; the regex at `:377` |
| comp-schedule | bare, twice (05:5xZ, 06:29:48Z) | PASS | 19 gates / 5 carriers each time; 0 name this project; 138 prose NEEDS-READ listed not counted |
| comp-iam | `stats`, `roles`, `role` x4 | PASS | DESIRED plane: 180 roles, 15 globgrph-family + gateway; the three principals' statements read in full; BLIND on the two new principals by construction (stated) |
| comp-trigger | `kuzu`, `globgrph` | PASS | 140 rules + 18 schedules; blind on S3 notifications BY ITS OWN DISCLOSURE, which is the honest result for S1 |
| comp-find --corpus aws | `'opal-globgrph' --budget 300` (page 1, then `--all`) | PASS | 70 hits / 2,100 nodes, DB built 00:36Z; cluster active_services 2 re-measured on a different instrument from the CRO brief; SQS/SG/Lambda/DynamoDB bands read; WITHIN BUDGET 11.55 s (CE-G-5 landed) |
| comp-find (repo) | `aws_s3_bucket_notification` scoped to globgrph TF; `_branch_head`; `aws_sqs_queue`; the `CG-` id census; `0.7.0_AE_CloudOps~P/~Q` census | PASS | S1 absent on the DESIRED plane (0 of 32); MARKER_KEY defined in 5 files; the id family present in this file only; ~Q 0 hits, ~P one CLOSED TO |
| comp-adversary | `compose --no-packet` on the decomp and both TOs | PASS | rc 0 x3; 22/22, 10/10, 8/8 cited commits VERIFIED; only flagged paths = the deliverables the artifacts create; the JSON `--out` is actually markdown (see Gap) |
| missions-tree-index | `check` x3 (baseline, with decomp, at commit) | PASS | 0 violations each; R6 not evaluated while EXECUTING |
| to-check | `--all --assignee` x5 | PARTIAL | the BY AGENT rollup on the base serial was the useful read; an unmatched lane serial prints the same complete-only list as a match (see Gap) |
| owned-paths-validate | `--check-agent 2.0.0_SA_COO~A` on 7 tree paths | PASS | decompositions/ task-orders/ ledger/ PERMIT; prd/ project.json remediations/ REFUSE -- 3 of 3 negative controls fire |
| to-pipeline-gate | `check_file` imported and called on both TOs before staging; then at commit | PASS | 0 violations off-stage and at commit; committer resolves to `2.0.0_SA_COO~A` from `$OPAL_AGENT_SERIAL` |
| prd-header-notify | `status`, `reoffer` | WARN | the L4 frame read OFFER-EXHAUSTED for a LIVE seat; `reoffer` was silent because its 30-min clock had not elapsed; the body arrived by the broker's re-offer (93187) and both ids were READ-acked |

**What worked:** comp-read on the spine and the gate replaced reading 1,200 lines; comp-find's aws corpus gave S1/S4/S11/S12 a live-plane read that the CRO brief had only carried; pulling `CELL_ID_RE` by AST and fullmatching all 19 ids before writing made the id space a measured property; `check_file` imported off-stage let the L6 gate grade the faces before the commit hook did.
**What failed:** nothing crashed. `to-check --all --assignee <unmatched lane>` prints the complete-only list rather than an empty set, so a zero cannot be read from it (the base-serial rollup is the sound read). `comp-adversary --out` writes markdown under a `.json` name.
**Gap found:** the notifier's OFFER-EXHAUSTED state for a live seat -- the ledger says the frame never reached an agent, yet the same body surfaced through the heartbeat URGENT queue and a re-offer id minutes later; which carrier a live seat should trust first is not stated anywhere this seat read. Surfaced in the L5 handoff message, not chased.

---

## Work Completed

### 1. Startup (05:17-05:3xZ) -- `/watcher` + `org/XXX.md` Step 1b A-F
Registered `2.0.0_SA_COO~A` (PID 24856); Monitor `bty1jg17t` armed on `/cygdrive/c/...inbox-watch.sh 2.0.0_SA_COO~A stream`, arm banner `parent-tied: pid 691014`; session serial file written; `.agent_context` set; owned-paths hook present; shims provisioned (104 x2); audit-archive-invoker: 5 findings, all the known device-axis classes; B.0 delivery ledger read (2 rows, both opened and acked); zero crons (the Step 1b-F COO row carries no live authorization for a ~A lane; the base D2 arm is HELD by Andrew 2026-09-02). Identity cross-check: liveness shows this lane at this PID and the base seat at its own PID -- a peer, not a conflict.

### 2. L5 -- the decomposition @`994c9381d0`
`org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md` v0.1 over PRD v0.4 @`25c66d3358` s.7: 19 cells = `CG-s-1..13` (1:1 with S1-S13) + `CG-x-1/2/4/5/7/8` (the closing pass the spine v2.3 close requires, one per EXERCISED outcome; 8 of 8 outcomes have a cell); status vocabulary DONE / IN-FLIGHT / OPEN / HELD / NOT-EVALUATED with its Rule 24 record (reused from the COMPEFFICACY decomposition, not renamed); placement laptop on every cell; edges keyed to OBSERVED completion; rounds 1-4 with the two ruled orderings (R7: S8 last, closing on CG-x-7; R10: S9 inside the port). s.0 re-pinned every manifest surface at HEAD: `comp-kuzu-full` / `comp-kuzu-inc` ABSENT (retired @`dffbee781c` by COMPEFFICACY cell t-22 -- S8 partly done by a sibling), `_canonical.py` 647 -> 746 and `kuzu_cli.py` 179 -> 189 @`173dd335f4` (CE-G-5's freshness layer now inside the engine S2 ports -- a bound added: the port SAYS whether it is worker-internal or local-only), `comp-kuzu` 28 -> 30. Validated by `1.0.0_SA_CTO~A` (93250, RAVC 4 closed); row flipped PRD -> DECOMP @`a1af5d70c2` by the row owner.

### 3. The L6 `<issued_to>` fork -- surfaced by `3.0.0_SA_CVO~A`, ruled by Andrew, dissolved
93194 surfaced the collision between Andrew's ~06:05Z *"run entirely by this fabric CVO~A COO~A CTO~A"* and gate (i) (`to-pipeline-gate.py:96,166`, a `_SA_` `<issued_to>` REFUSED). Both CTO seats carded it (93205, 93210), the base COO offered the narrow reading (93201); Andrew ruled (a) at both lane terminals ~06:1xZ (*"yeah obviously COO~A needs to /mstr-spawn the workers for 6-7"*, @`858fc08951`). L5 was never blocked; the decomposition's s.5 hold 5 records the fork and its discharge. Nobody edited the gate.

### 4. L6 -- ROUND 1 cut and seated @`d0c21677c7`
Pre-flight per `/mstr-spawn` (1pt 9 claude.exe, none CloudOps; 1b 0 CloudOps markers, 2 of cap 20; 1a NOT REGISTERED; 1d: six CloudOps letters encumbered by open TOs, `~Q` 0 corpus hits, `~P` one CLOSED TO-5 and no ARMED ownership row). Spawned `0.7.0_AE_CloudOps~Q` (06:35:51Z) and `~P` (06:35:54Z) with `--say` hints naming their task orders; both LIVE within 3 minutes and both summaries read the hint. Two faces: `TO-CG-V-1` (CG-s-10, the full-fallback duration MEASURED twice + one incremental run to a temp path, the fit table as a finding, the four prior figures reconciled AFTER measuring) -> `~Q`; `TO-CG-V-2` (CG-s-11 + CG-s-12 + CG-s-13: reachability probed from both ends with a negative control, the IAM delta on the APPLIED plane after `refresh-census` written as a proposal never applied, the AuthKind named at its line) -> `~P`. Each carries `<decomp_ref>` @`994c9381d0`, the three preflight dispositions with numbers, `<proof_of_spec>` with V1-AC1..AC6 / V2-AC1..AC7 and `cell_refs`, READ-ONLY bounds, surprises as rows. Held in the worktree through MSTR's merge window (93258 -> 93271), committed after the CLOSE through every gate green, GOs sent to the exact serials (93277 READ by `~Q` at 06:48:17Z; 93278 SENT to `~P` at 06:47:55Z, READ pending at this write); hash to `1.0.0_SA_CTO~A` for the EXECUTING flip (93249-family thread, delivered 06:48:05Z).

### 5. MCP traffic
22 messages handled (all READ-acked from their ids); 6 sent. Significant: 93141 (the seating, Andrew-direct via CTO~A), 93146 (base COO continuity), 93161 (LAW: the close, autonomy after L2), 93149/93187 (the L4 frame + its re-offer), 93194/93201/93205/93210 (the fork), 93214/93220 (Andrew's ruling (a)), 93231/93243/93258/93271 (MSTR's two windows), 93250 (RAVC 4 on L5 + the DECOMP flip); sent: the ACK on 93141, the L5 handoff, the 93250 ACK, the two GOs, the L6-landed hash.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Pick L5 up on the MEASURED artifact when the notifier frame read OFFER-EXHAUSTED | `/canonical-flow` Step 2: the limb is the highest conforming output; the PRD at its tree path was committed and conforming; the frame is the handoff mechanism, the artifact is the handoff. The frame was acked when its body arrived. |
| Add six closing-pass cells to the rectangle | Spine v2.3 close: an outcome whose DONE WHEN is an act after the work is met by a closing-pass task order; without a cell the COMPLETION_REPORT would read UNCOVERED on six of eight outcomes by its own schema. Declared as a domain extension by the spine's word, not smuggled. |
| No `workflows/atom_decomposition/runs/` directory, no sealed-mutant self-check | The spine says no seat waits on it; the COMPEFFICACY precedent @`e8641a324c` made the same choice; the decomposition is falsified at L7 by a worker's row. Stated as a choice in the file. |
| Two task orders for ROUND 1, not four or one | CG-s-10 runs full loads and owns a seat for the duration; CG-s-11/12/13 are three reads with three controls on one seat. Rule 27: one project per instance, parallelism by instances. |
| Fresh lane letters `~Q` and `~P`, not any encumbered letter | 1d: six CloudOps letters hold open TOs on other projects; seating over one is the Rule 27 collision at seating time. `~Q` had zero corpus hits; `~P`'s only record is a CLOSED TO, world-done. |
| Honour MSTR's two commit holds rather than race them | The hazard is staging into an in-progress merge index; a bounded background wait on the CLOSE frame cost ~4 minutes and nothing else. Spawning is not a commit, so the seats booted during the hold. |
| Cite `COMPEFFICACY cell t-22` in prose, never `CE-t-22` | `CELL_ID_RE` reads every hyphenated id in a decomposition file as that file's id space; a sibling's id in this file would have let a TO claim it. Measured before the fix (20 ids found, 19 declared). |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md` | NEW, v0.1, 179 lines (see commit message) | Yes -- `994c9381d0` |
| `org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-V-1.full-fallback-duration-measured.md` | NEW, 76 lines | Yes -- `d0c21677c7` |
| `org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-V-2.reachability-iam-authkind-verified.md` | NEW, 87 lines | Yes -- `d0c21677c7` |
| `org/mcp/sessions/6d5b61d5-0631-446e-8fab-04a4bce2dfaa.serial`, `.comp-graph/.agent_context` | session identity (gitignored / shared) | n/a |
| `org/mcp/agent-spawn-audit.log` | two SPAWN lines by `2.0.0_SA_COO~A` | n/a (audit log) |

---

## Blockers

None at this seat. Two obligations are in flight elsewhere and are named, not blockers: `0.7.0_AE_CloudOps~Q` on TO-CG-V-1 and `~P` on TO-CG-V-2 (both LIVE, GO delivered; evidence: the broker ledger rows 93277 READ / 93278 SENT and each seat's summary naming its TO); `1.0.0_SA_CTO~A`'s DECOMP -> EXECUTING flip on `d0c21677c7` (asked 06:48:05Z; the row owner's act).

---

## Current State

NFRA_CLDGRPH is at L7 of its first round. The tree home `org/missions/D0/NFRA/NFRA_CLDGRPH/` holds the PRD v0.4 @`25c66d3358`, the decomposition v0.1 @`994c9381d0` (19 cells), and two task orders @`d0c21677c7` addressed to `0.7.0_AE_CloudOps~Q` (cell CG-s-10) and `0.7.0_AE_CloudOps~P` (cells CG-s-11/12/13), both seats spawned by this lane and LIVE; the row `project.json` reads `dep_stage: DECOMP` @`a1af5d70c2` with EXECUTING owed by `1.0.0_SA_CTO~A` on the TO hash. `3.0.0_SA_CVO~A` holds L8-L10 with intake armed on both channel roots; no surprise row exists yet (the folder is created on the first row). Push state: LOCAL, HEAD `d0c21677c7` one ahead of origin/CLOUD @`3bd8d2ef04` (MSTR's CLOSE 93271); no window until Andrew's word. This seat: zero crons, `/drive` OFF, Monitor `bty1jg17t` live.

---

## Next Steps

1. **[0.7.0_AE_CloudOps~Q] Deliver TO-CG-V-1** -- the result file + proof instance VALID + own complete flip; report to `2.0.0_SA_COO~A`.
2. **[0.7.0_AE_CloudOps~P] Deliver TO-CG-V-2** -- same shape; a NOT-REACHABLE verdict with no admitting change is a BLOCKING row to this seat in the same turn.
3. **[1.0.0_SA_CTO~A] Flip dep_stage DECOMP -> EXECUTING** on `d0c21677c7`; then nothing until an L10 route names that seat.
4. **[2.0.0_SA_COO~A] On both reports:** verify the proof instances against the criteria (RAVC 4), read any rows, wait for `3.0.0_SA_CVO~A`'s round-1 slug at L10, then cut ROUND 2 (CG-s-1 -> CG-s-2 + CG-s-9 -> CG-s-3) from the four verdicts, seating a fresh CloudOps letter if `~Q`/`~P` are still engaged; write `ledger/STEP_LOG.2.0.0_SA_COO~A.round1.json` at the round's stamp.
5. **[2.0.0_SA_COO~A] Carry, not chase:** the notifier's OFFER-EXHAUSTED-for-a-live-seat reading (Compiler Tools gap) and the `to-check --assignee <unmatched lane>` output shape -- one line each to their owners at the next natural message, never a workstream.
