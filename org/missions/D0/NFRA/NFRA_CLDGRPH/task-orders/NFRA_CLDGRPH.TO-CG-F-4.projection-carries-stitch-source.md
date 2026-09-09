# TO NFRA_CLDGRPH.TO-CG-F-4 -- CG-s-24 (ADDED at decomposition v0.6 on the CTO's round-5 analysis @30027295be, PRD addendum v0.6 row S24): THE PROJECTION CARRIES THE STITCH SOURCE -- the nightly derive folds the cloud-produced `stitch/stitch_graph.json` into the one graph (an ADDITIVE fold beside the folds it already runs), the marker and the served manifest declare a STITCH source vintage beside the Nessie one, the shared image is REBUILT and every family re-pinned by DIGEST under a NEVER-2 entry naming all seven (R13), and a thin-client query for the stitch node types returns non-zero from the SERVED graph with the stitch vintage on the VINTAGE line. The JOIN's cell 2 of 4

<to_id>NFRA_CLDGRPH.TO-CG-F-4</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~2</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-09</issued_date>
<status>pending -- GO = the COO handing this order to slot ~2 by CONTINUING the same subagent after TO-CG-F-3 (CG-s-23) is terminal and merged, with CLOUD merged into your branch (spine v3 L7 drain). ROUND 6 of NFRA_CLDGRPH. Slot ~2's SECOND order; TO-CG-F-5 (CG-s-25) then TO-CG-F-6 (CG-s-26, LAST) follow. PREMISE RE-GROUND at hand-off: F-3's instance VALID at your HEAD; `stitch/stitch_marker.json` reads `producer: stitch-codebuild` with a `git_sha` in this repository (F3-AC4); `.tools/terraform.exe` PRESENT in your worktree (the issuer copies the gitignored binary at hand-off -- a fresh worktree has none and the PATH substitute re-pins remote state; if absent, BLOCKING row + report, never the PATH `terraform`); if any fails, BLOCKING row + report. The assignee commits its own status flip after a VALID proof-of-spec instance whose mechanical rows ALL read PASS; the L8 seat reads the record.</status>

**Directive:** D0 · **Fabric:** laptop · **PRD:** `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md` v0.6 @`30027295be` (FWD-7 by the arc; s.7 row S24; s.6 R13) · **Decomp cell:** `CG-s-24` (decomposition v0.6, this recut) · **Lane:** `0.8.0_AE_CloudComp` (the engine) with the `0.7.0_AE_CloudOps` pins the image act requires · **Rule 27 seating:** `0.9.0_WK_NFRA_CLDGRPH~2`.

---

## STANDING LAW (inlined; the worker face is your whole context)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~2; export PATH="/c/Users/AndrewBerman/AppData/Local/Programs/Python/Python312:$PATH";`. Commit only on your worktree branch via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~2 <0.9.0_WK_NFRA_CLDGRPH~2@opal.agent>" -F <msgfile> -- <files>`. Never push, merge, rebase, `checkout --` or `clean`. Push state is LOCAL and you say so.
- **Your write surface is exactly the PATHS block below plus `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/`.** Every script and capture carries `f4_` in its name. Scratch: `<your worktree>/.scratch/`.
- **Surprise = ONE ROW, never a message** (`NFRA_CLDGRPH-W2-S<k>`, continuing your numbering; restate the header denominator; never edit a row; keep working).
- **Every criterion invocation runs under `timeout 120`**; a derive or a projection wait is a polled loop (`describe-tasks` / head-object every 30 s under `timeout 3600`), never a bare sleep.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** Non-ASCII in code is refused.
- **NEVER:** bare `terraform apply` (the apply is `bash .tools/safe-apply ...` from the worktree with `.tools/terraform.exe` present -- read the E-2 record for the exact call and the TEN-address set); `aws lambda update-function-code`; a `:latest` tag left on ANY family (R13); an image act without its NEVER-2 entry naming ALL SEVEN families that pull the tag (`globgrph-derive-runner`, `globgrph-projection-worker`, `globgrph-serving`, `comp-learns-producer`, `cse-producer`, `fedobs-producer`, `resource-summaries-producer`); a local Kuzu store built or opened (the projection is built IN THE CLOUD by the worker task; you read it through the thin client); the stitch STORE touched (S26's); a monitor; `2>/dev/null` on a verdict read; bare `git commit`.
- **Search rail:** `python .tools/comp-read` / `python .tools/comp-find`; raw recursive grep/find refused; a `cmd | grep` receiver is free. AWS CLI = `.tools/aws` (v1).

## THE CELL (decomposition v0.6, this recut, s.1a; PRD v0.6 s.7 row S24 verbatim in its accept)

> **CG-s-24** | S24 THE PROJECTION CARRIES THE STITCH SOURCE: the derive includes the stitch tables; the served manifest declares a stitch source vintage beside its Nessie one (E-4's JOIN_PROJECTION, C-S33) | FWD-7 (cell 2) | claim: absent (E-4's record names it as the second cell with its accept) | status: OPEN -- ROUND 6 (recut) | lane `0.8.0_AE_CloudComp` | placement laptop | verb build (an IMAGE act under R13) | depends_on: CG-s-23 -> DONE (a join to a producer that produces nothing is a join to a fiction) | **closes on (the PRD's accept, verbatim):** a thin-client query for the stitch node types returns non-zero from the served graph with the stitch vintage on the VINTAGE line; the NEVER-2 entry names all seven families

## MEASURED BY THE ISSUER AT THE CUT -- and the route the issuer expects (say which if you take another)

- **The projection's shape today:** `projection_worker.py:44` `ARTIFACT_NAME = "kuzu_nessie_db"`; the worker reads the marker (`_provenance.MARKER_KEY`), runs `kuzu_incremental_refresh.py` (manifest at `:254`, `source_vintage=pin` from the Nessie/Iceberg metadata) or falls back to `kuzu_nessie_load.py` (`:252`), publishes artifact-first / manifest / pointer-last. The served header prints `source_vintage`'s keys (`_provenance.format_provenance_header`, `:560+`). **The stitch types are NOT in the served graph today** (E-4 s.1c: *not today; and the consumer would need no change if it did*): `GOLD_SCRIPT`, `S3_DATA_KEY`, `API_ROUTE`, `PORTAL_COMPONENT`, `REACT_QUERY_KEY` and the STITCH edge types `ROUTES_TO`, `WRITES`, `READS`, `DERIVES_FROM`, `STORED_IN` (`derive_stitch.py:10-17`).
- **The derive already FOLDS additive producers** (`derive_runner.py:2285-2326`: `ingest_cluster_producer`, `ingest_graphuni_producers`, `stitch_served_from` -- each best-effort, each `WARN: ..._FAIL` and continue). **The expected route:** ONE more fold, `ingest_stitch_artifact(graph)`, reading `s3://opal-313476888478-globgrph/stitch/stitch_marker.json` then `stitch/stitch_graph.json` (the marker's `artifact_sha256` verified against the bytes BEFORE the fold -- a mismatch is a LOUD skip with the reason), unioning the stitch nodes/edges into the same `classes_data` (ARN-keyed AWS nodes already present are NOT duplicated: co-key by node id, count the duplicates skipped), and carrying the marker's `built_at`, `git_sha`, `producer`, `artifact_sha256` into the derive's own marker stamp (`derive_runner.py:389` region, `MARKER_KEY`) under a `stitch` key -- so the projection worker's `pin` (read from that marker/metadata; trace how `pin` is built in `kuzu_incremental_refresh.py`) carries `stitch_built_at` + `stitch_artifact_sha256` into `source_vintage`, and the header prints them. **A fold that FAILS must print `WARN: STITCH_INGEST_FAIL` and continue** (the derive's contract); a fold that succeeds prints `INFO: STITCH_INGEST nodes=<n> edges=<m> skipped_dup=<k> vintage=<built_at>`.
- **The IMAGE act (R13, NEVER-2):** the Dockerfile `infra/aws/globgrph/Dockerfile` (COPY `:56`, CMD `:206`); `build-derive-image.sh`; the D-1 record `deliverables/0.9.0_WK_NFRA_CLDGRPH~1/CG-s-15.shared-image-digest-pins.result.md` and the E-2 record `deliverables/0.9.0_WK_NFRA_CLDGRPH~1/CG-s-18.four-producers-pinned.result.md` carry the exact build/push/pin procedure and the TEN-address apply set (seven task definitions + three launcher roles' revision-scoped RunTask grants); the digest local `serving.tf:22 local.globgrph_image_digest`. Read them; do not re-derive the procedure. The ECR `:latest` tag may move with the push (the families are pinned by digest, so nothing pulls it; say so in the entry).
- **Then ONE ad-hoc derive** on the new digest (the D-1/E-2 records' `run-task` shape; the log `/ecs/globgrph/derive-runner` must show `INFO: STITCH_INGEST nodes=...`), a real marker stamp -> the projection worker builds and publishes -> the pointer advances -> `bash .tools/comp-kuzu --json "MATCH (n:CloudNode) WHERE n.node_type IN ['GOLD_SCRIPT','S3_DATA_KEY','API_ROUTE'] RETURN n.node_type AS t, count(*) AS c ORDER BY t"` answers non-zero with the VINTAGE line carrying the stitch vintage. Budget the wait: the projection worker's deadline is 3600 s.

## ISSUER RULING 2026-09-09 18:5xZ on row NFRA_CLDGRPH-S71 (the CVO, 18:44Z)

The marker at `stitch/stitch_marker.json` may be rewritten by a post-commit hook at either clone (`producer=stitch-local`) within ~60 s of a commit; see F-3's ruling. For this order: the fold CARRIES the marker's `producer`, `git_sha`, `built_at` and `artifact_sha256` into the derive's marker and the served `source_vintage` (`stitch_producer` beside `stitch_built_at`) and does NOT refuse on `producer` -- the served graph DECLARES who produced its stitch; whether a hook-made stitch is admissible is `1.0.0_SA_CTO`'s reconciliation (pitched this tick), and the vintage line makes the answer readable either way. F4-AC4's expectation gains nothing; the record prints `STITCH_PRODUCER_AT_FOLD=<value>` beside the vintage.

## DELIVERABLE -- in this order

1. The fold in `derive_runner.py` (+ the marker stamp) and the `pin` carrier in `kuzu_incremental_refresh.py` / `kuzu_nessie_load.py` / `projection_worker.py` as the trace requires; unit test `f4_test_stitch_ingest.py` in the deliverables folder exercising the fold on a fixture (a 3-node stitch graph + a marker; the sha256 mismatch arm; the duplicate-skip arm). Commit-gate each file.
2. The NEVER-2 entry OPENED naming all seven families and the ten addresses; image built + pushed; the ten-address `safe-apply` from the worktree; `describe-task-definition` x7 reading the NEW digest; the entry CLOSED.
3. The ad-hoc derive; the projection; the thin-client read; the header.
4. The record `CG-s-24.projection-carries-stitch-source.result.md` (one fenced JSON block: the fold's counts, the digest before/after, the seven families' revisions, the derive task id, the pointer before/after, the query answer, the VINTAGE line) then prose; the instance; the flip.

## ACCEPTANCE (v3 grammar)

<criterion id="F4-AC1" cell_refs="CG-s-24"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/f4_test_stitch_ingest.py</invocation><expect>FOLD_OK nodes=3 edges=[0-9]+ skipped_dup=1[\s\S]*SHA_MISMATCH_ARM=SKIPPED_LOUD[\s\S]*F4_TESTS=([0-9]+) passed of \1</expect></criterion>
`F4-AC1` -- THE FOLD, EXERCISED ON A FIXTURE: three stitch nodes folded, one duplicate (an ARN already in the graph) skipped and counted, the sha256-mismatch arm skipping LOUD, every test passing with its denominator.

<criterion id="F4-AC2" cell_refs="CG-s-24"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/f4_families_pinned.sh</invocation><expect>FAMILIES_ON_NEW_DIGEST=7 of 7[\s\S]*LATEST_TAG_REFERENCED_BY=0 of 7[\s\S]*LEDGER_FAMILIES_NAMED=7[\s\S]*LEDGER_ENTRY_STATUS=CLOSED</expect></criterion>
`F4-AC2` -- R13 AND NEVER-2: all seven ACTIVE globgrph task definitions reference the NEW digest by `describe-task-definition` (live), none references `:latest`, the ledger entry names seven and is CLOSED.

<criterion id="F4-AC3" cell_refs="CG-s-24"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/f4_derive_folded.sh</invocation><expect>DERIVE_TASK=arn:aws:ecs:[^\s]+[\s\S]*STITCH_INGEST nodes=[1-9][0-9]* edges=[1-9][0-9]*[\s\S]*STITCH_INGEST_FAIL_LINES=0</expect></criterion>
`F4-AC3` -- ONE REAL DERIVE ON THE NEW DIGEST FOLDED THE STITCH: the task's log carries the INFO line with non-zero counts and no FAIL line (the pre-fix image's log, with no STITCH_INGEST line at all, is the control).

<criterion id="F4-AC4" cell_refs="CG-s-24"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/f4_served_stitch.sh</invocation><expect>SERVED_STITCH_TYPES=([1-9][0-9]*) of 3 non-zero[\s\S]*GOLD_SCRIPT=[1-9][0-9]*[\s\S]*VINTAGE_HAS_STITCH=true stitch_built_at=2026-09-(09|10)T[\s\S]*POINTER_ADVANCED=true</expect></criterion>
`F4-AC4` -- THE SERVED GRAPH ANSWERS FOR THE STITCH TYPES with the stitch vintage on the VINTAGE line and the pointer advanced past the pre-fold vintage (the pre-fold answer, 0 of 3, is the control; a positive control on a type the projection already carried).

<criterion id="F4-AC5" cell_refs="CG-s-24" judgment="true"/> `F4-AC5` -- THE JOIN, READ: what the served graph now IS (one graph with two sources under one vintage line), what the fold does NOT guarantee (the stitch's own freshness is the producer's, F-3's nightly), where a second compile business could re-enter (a local Kuzu of the stitch -- S26 retires it), and what a reader should expect of the two vintages on a night the stitch nightly fails but the derive runs. A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9.

<expected_criteria>F4-AC1, F4-AC2, F4-AC3, F4-AC4, F4-AC5</expected_criteria>

## SURFACES

`infra/aws/globgrph/derive_runner.py` (the fold + marker stamp) · `kuzu_incremental_refresh.py`, `kuzu_nessie_load.py`, `projection_worker.py` (the vintage carrier, MINIMUM) · `_provenance.py` (READ; S27 is editing it in slot ~3 -- do NOT edit it here; if the header needs a change to print the stitch keys, it already prints every `source_vintage` key: verify, and a row if not) · `Dockerfile`, `build-derive-image.sh` (READ/run) · `infra/aws/terraform/globgrph/serving.tf:22` + the four producers' `.tf` (the digest local; the pins) · the D-1 and E-2 records (READ: the procedure).

## BOUNDS

- **The fold is ADDITIVE and best-effort by the derive's own contract; the image act is ledgered; the apply is the ten-address set from the worktree with `.tools/terraform.exe` present.** No local store. No monitor.
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
infra/aws/globgrph/derive_runner.py
infra/aws/globgrph/kuzu_incremental_refresh.py
infra/aws/globgrph/kuzu_nessie_load.py
infra/aws/globgrph/projection_worker.py
infra/aws/globgrph/Dockerfile
infra/aws/terraform/globgrph/serving.tf
infra/aws/terraform/globgrph/comp_learns_producer.tf
infra/aws/terraform/globgrph/cse_producer.tf
infra/aws/terraform/globgrph/fedobs_producer.tf
infra/aws/terraform/globgrph/resource_summaries_producer.tf
infra/aws/terraform/globgrph/item2a.tf
infra/aws/terraform/globgrph/projection.tf
org/critical_paths/change_management/
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-F-4.projection-carries-stitch-source.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> v0.6 (this recut), cell CG-s-24 (s.1a; ADDED on the CTO's round-5 analysis @30027295be, PRD addendum v0.6 row S24, on E-4's JOIN_PROJECTION record and C-S33).
<owned_cells>CG-s-24</owned_cells>
Read-dependencies, NOT claimed: CG-s-23 (TO-CG-F-3, terminal and merged before this order is handed), CG-s-15/16/18 (DONE; the image and pin procedure). Downstream, yours next: CG-s-25 (TO-CG-F-5), then CG-s-26 (TO-CG-F-6, LAST). Sibling editing `_provenance.py`: CG-s-27 (slot ~3) -- not yours.
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-09 15:3xZ at the round-5 recut (GATES ARMED 25); C2's open deploy-ledger entries are the NEVER-2 discipline this order adds one to; the C3 moratoria bind BOUNDS.
comp-iam: DECLARED-NOT-APPLICABLE for the derive's read of `stitch/*` IF the derive task role already reads the globgrph bucket (verify with ONE `simulate-principal-policy` call on the `stitch/stitch_graph.json` ARN before the derive; a deny is a BLOCKING row -- the grant is `0.7.0_AE_CloudOps`'s Terraform, out of this order); the pins change no principal.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 on the decomposition (rc 0 @07288006e5); the L9 seat's compose is the deliverable's context.
comp-find: RUN at the cut -- `stitch` on the projection path 7 hits / 5 files, all `derive_runner.py` (the TSGRAPH P4 `stitch_served_from`, a DIFFERENT join); `write_manifest(` 9 hits / 961 files.
</preflight>

<proof_of_spec>
Criterion ids minted at the recut by the issuer: `F4-AC1`..`F4-AC5`. Instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-F-4.projection-carries-stitch-source.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> F4-AC1,F4-AC2,F4-AC3,F4-AC4,F4-AC5` BEFORE the flip; rc 0 AND every mechanical row PASS. `F4-AC2` (0 of 7 on `:latest`) and `F4-AC4` (the pre-fold 0 of 3) are the controls that must be able to FAIL. `F4-AC5` is `judgment="true"`: `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; **`PASS` or `FAIL` on it is INVALID.** Two commits at the flip.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE ANY ACT: `python .tools/comp-read infra/aws/globgrph/derive_runner.py --for "how the additive folds are structured (ingest_graphuni_producers, stitch_served_from), how and where the marker is stamped, and the graph dict's classes_data shape"`; `python .tools/comp-read infra/aws/globgrph/kuzu_incremental_refresh.py --for "how pin is built and what source_vintage carries"`; the D-1 and E-2 records with `--for "the exact build, push, pin and ten-address apply commands"`. Every `.py`: `bash .tools/commit-gate.sh <file>`.
</compiler_tools_mandate>

**THE REPORT IS YOUR FINAL MESSAGE, ONCE, IN THE `WORKER REPORT` SHAPE.**

**GO = the hand-off (the COO continues this subagent after TO-CG-F-3's drain).**
