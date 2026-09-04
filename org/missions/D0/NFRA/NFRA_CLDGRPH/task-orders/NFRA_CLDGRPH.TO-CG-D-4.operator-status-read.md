# TO NFRA_CLDGRPH.TO-CG-D-4 -- the OPERATOR STATUS READ: `comp-graph status` REPOINTED at the projection pointer's manifest -- a PULL read that answers "did it refresh last night" with yes/no + a time from the served artifact's own record, and a NIGHT THAT DID NOT RUN reads differently (planted, the control); NO alarm, SNS, checker or monitor (R4; CLAUDE.md s.5)

<to_id>NFRA_CLDGRPH.TO-CG-D-4</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~3</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- 0.9.0_WK_NFRA_CLDGRPH~3, all 7 criteria (D4-AC1..D4-AC7) PASS-by-output; proof-of-spec instance at org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/NFRA_CLDGRPH.TO-CG-D-4.operator-status-read.proof_of_spec.json, VALID rc 0. ROUND 4 of NFRA_CLDGRPH (the ONE issuance covering every open cell, Andrew's word via CRO record @aff3bfb7bf), slot ~3's FIRST order; STAGE 3's first cell, released by CG-s-3 DONE (@93c26badf8: a manifest exists to read). Push state LOCAL on wk-NFRA_CLDGRPH-3; not pushed by this seat.</status>

**Directive:** D0 · **Fabric:** laptop · **PRD:** `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md` v0.4 @`25c66d3358` (FWD-8; s.7 row S7; R4) · **Decomp cell:** `CG-s-7` (v0.2 @`70918d5d2b`) · **Lane:** `org/modules/graph/graph_status_cli.py` (comp-graph's engine), `.tools/comp-graph`, `.tools/tests/` · **Rule 27 seating:** `0.9.0_WK_NFRA_CLDGRPH~3`, a spine-v3 worker subagent of `2.0.0_SA_COO~A`.

---

## STANDING LAW (inlined; the worker face is your whole context)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~3;`. Commit only on your worktree branch via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~3 <0.9.0_WK_NFRA_CLDGRPH~3@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state is LOCAL and you say so.
- **Your write surface is exactly the PATHS block below plus `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/`.** A path you need that the block lacks is a BLOCKING row on that criterion, never an override.
- **Surprise = ONE ROW, never a message.** Append to `org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md` a new `## <id> -- <title>` section with a fenced json array holding one object (the S28 row's field set); id `NFRA_CLDGRPH-W3-S<k>`, `<k>` the next unused within W3 (start at 1); restate the header denominator line; never edit an existing row; keep working.
- **Every criterion invocation runs under `timeout 120`**; rc 124 IS the recorded output, retried once at most.
- **NEVER:** an alarm, SNS topic/subscription, EventBridge rule, Lambda, checker, monitor or scheduled anything (R4 + the standing moratorium: this is a PULL READ, run by a human or a seat when asked); a write to S3 (the read is `GetObject` only); a rebuild or a call into any engine; non-ASCII in code/logs; `2>/dev/null` a read whose emptiness is a verdict; bare `git commit`.
- **Search rail:** `python .tools/comp-read <file> --for "..."` / `--enumerate '<regex>'`; `python .tools/comp-find '<pattern>' <pathspec>`; raw recursive grep/find in Bash is refused; a `cmd | grep` receiver is free. AWS CLI = `.tools/aws`.

## THE CELL (verbatim, decomposition v0.2 s.1a)

> **CG-s-7** | S7 operator status read: repoint `comp-graph status` at the pointer's manifest | FWD-8 (acc 8) | claim: absent | status: OPEN | evidence: `graph_status_cli.py:214-232` (360 @`ee49b14381`) reports "kuzu_db 81d / stitch_graph 38d" -- the wrong artifacts (brief F6, attributed) | lane `0.8.0_AE_CloudComp` | placement laptop | depends_on: CG-s-3 -> a manifest exists to read | **closes on:** R4: a PULL read; "did it refresh last night" prints yes/no + a time; a NIGHT THAT DID NOT RUN reads differently -- planted by pointing at a stale manifest (the control). NO alarm, SNS, checker or monitor (CLAUDE.md s.5)

**PRD R4 (binding):** *"FWD-8's mechanism is a PULL-style status READ of the projection pointer's own manifest (the repoint of the mis-aimed `comp-graph status`, brief F6). No alarm, SNS, checker or monitor. FRESHGUARD's alarm legs remain torn down."* **The binding handoff** (`PROJECTION_CONTRACT.md` s.8, `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~T/PROJECTION_CONTRACT.md`): *"CG-s-7 operator status: begin at `projection/current.json`, apply the same straddle rule, and report `vintage`, `age_line`, `built_at`, `nessie_commit_hash`, both snapshot ids, source `writer_id`, `producer.mode`, `producer.source_commit`, `node_count`, `edge_count`, `edges_skipped_missing_endpoint`, exact artifact bytes, and expected size-band status. A pre-pointer crash reports the previous healthy vintage, not a half-publish."*

## MEASURED BY THE ISSUER AT THE CUT (2026-09-04 06:1xZ)

- **Today's engine:** `org/modules/graph/graph_status_cli.py` (360 lines; `.tools/comp-graph` is a 9-line shim onto it). Its cloud group (`:214-232`, re-locate by content: `kuzu = _GLOBGRPH_DIR / "kuzu_db"` and `stitch = _GLOBGRPH_DIR / "stitch_graph.json"`) stats two LOCAL files that are the wrong artifacts; the local trace-layer group (`.comp-graph/` caches, `_ttl_verdict`, `cli.trace_freshness`) is correct and stays.
- **The record to read:** pointer `s3://opal-313476888478-globgrph/projection/current.json` -> `{"schema_version":1,"vintage":"...","artifact_prefix":"projection/<vintage>/","manifest_key":"projection/<vintage>/_build_manifest.json","manifest_sha256":"..."}`; the manifest's fields per `PROJECTION_CONTRACT.md` s.3 (`vintage`, `committed_at`, `age_line`, `writer_id` = `derive_runner` for the nightly full or `incremental_updater` for an intraday stamp, `built_at`, `producer.mode` = `full|incremental`, `node_count`, `edge_count`, `edges_skipped_missing_endpoint`, `artifact.files[0].size_bytes`, `artifact.expected_publish_set_size_band_bytes`). The straddle rule (s.6): GET pointer P1, GET its manifest and verify `manifest_sha256`, GET the pointer again as P2; if P1 != P2 repeat from P2.
- **Live at the cut:** the pointer read `vintage 2026-09-04T05:53:37.689093+00:00` (writer `incremental_updater`, mode `incremental`, built_at 05:54:06Z, 27,244 nodes / 58,622 edges); the last NIGHTLY full: `2026-09-04T02:09:19.993324+00:00` (writer `derive_runner`, mode `full`, built_at `2026-09-04T02:22:43Z`, 27,246 / 58,646). Seventeen versioned prefixes under `projection/` from 2026-09-03T13:23:54 to 2026-09-04T05:53:37 (`list-objects-v2 --prefix projection/ --delimiter /`). The nightly schedule is `cron(0 2 * * ? *)` (`infra/aws/terraform/globgrph/item2a.tf:439`).
- **"Last night" is a DEFINITION you write down, not a feeling:** the most recent 02:00Z boundary before now; the night RAN if a `producer.mode == "full"` manifest with `writer_id == "derive_runner"` exists whose `vintage` falls inside [boundary, boundary + 6 h]; the time printed is that manifest's `built_at`. Finding it means listing the `projection/` prefixes (bounded: `--delimiter /`, one call) and reading the manifests of the vintages inside that window (bounded: at most 12 GETs). A NIGHT THAT DID NOT RUN: no such manifest in the window -> `NO (last full: <built_at of the newest full manifest before the boundary>)`.
- **The R4 control that can fail:** env `COMP_GRAPH_POINTER_URI` (default `s3://opal-313476888478-globgrph/projection/current.json`; a `file://` or plain path admitted) so a planted pointer+manifest pair in a temp dir whose newest full vintage is older than the last boundary makes the same read print `NO`. The plant is a local file; the live bucket is never written.

## DELIVERABLE -- in this order

1. **MEASURE FIRST (read-only):** `bash .tools/comp-graph status` today, quoted whole -- the two wrong rows with their ages (the "before"). Read the pointer and the two manifests above with `.tools/aws s3 cp ... -` and quote them.
2. **THE REPOINT** in `graph_status_cli.py`: the cloud group's two local-file rows are REPLACED by projection rows read from the pointer (straddle rule applied; `boto3` if importable else `.tools/aws s3 cp` via subprocess -- state which): a `projection.current` row (verdict PRESENT/UNVERIFIABLE; `vintage`, `age_line` verbatim, `built_at`, `writer_id`, `producer.mode`, `producer.source_commit`, `node_count`, `edge_count`, `edges_skipped_missing_endpoint`, artifact bytes, band status IN-BAND/OUT-OF-BAND/NO-BAND); a `projection.last_night` row: `REFRESHED LAST NIGHT: YES at <built_at>` or `NO (last full: <time>)` with the boundary printed; the `query` column reads `comp-kuzu` and the `rebuild` column reads `none -- the estate refreshes itself (FWD-2)`. `--json` carries the same fields under `graphs[]`. A pointer/manifest that cannot be read prints `UNVERIFIABLE (reason)` -- never a pass, never a default. Nothing else in the file changes (the local group, the contract text, `cmd_clear`).
3. **THE PLANT + THE BATTERY** `.tools/tests/test_cg7_status_read_battery.py` (NEW; direct AND pytest, FILE grain): arms: (i) live-shaped fixture (a pointer+manifest pair with a full vintage 2 h after the boundary) -> `YES at`; (ii) the plant (newest full 30 h before the boundary) -> `NO (last full:`; (iii) an unreadable pointer -> `UNVERIFIABLE`; (iv) `--json` carries `refreshed_last_night` and `vintage`; (v) the source carries no `sns`, `cloudwatch`, `put_metric`, `events`, `schedule` call (the R4 census, denominator printed); a RED mutant per arm where expressible (a reader that prints YES when the window is empty). The plant fixtures are written under the test's temp dir, never under `infra/`.
4. **THE EXERCISE (the closes-on):** `bash .tools/comp-graph status` post-commit, quoted whole; `COMP_GRAPH_POINTER_URI=<the plant> bash .tools/comp-graph status` quoted whole; both differ on the `last_night` line. Then the deliverable `CG-s-7.operator-status-read.result.md` (before/after, the definition of "last night", both readings, the battery numbers), the proof instance, validate, flip, commit.

## ACCEPTANCE (v3 grammar: one clause per criterion; every mechanical invocation bounded)

<criterion id="D4-AC1" cell_refs="CG-s-7"><invocation>bash .tools/comp-graph status</invocation><expect>REFRESHED LAST NIGHT: (YES at 20[0-9]{2}-[0-9]{2}-[0-9]{2}T[0-9:.]+|NO \(last full: )</expect></criterion>
`D4-AC1` -- THE READ ANSWERS yes/no + a time from the served artifact's own manifest (FWD-8).

<criterion id="D4-AC2" cell_refs="CG-s-7"><invocation>COMP_GRAPH_POINTER_URI=org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/plant/current.json bash .tools/comp-graph status</invocation><expect>REFRESHED LAST NIGHT: NO \(last full: </expect></criterion>
`D4-AC2` -- A NIGHT THAT DID NOT RUN READS DIFFERENTLY: the planted stale pointer+manifest pair (yours, committed under `plant/` in your deliverables folder, newest full vintage older than the last boundary) prints `NO`. The control that can fail.

<criterion id="D4-AC3" cell_refs="CG-s-7"><invocation>bash .tools/comp-graph status | grep -c -E 'kuzu_db .*(81d|MISSING|present)|stitch_graph'</invocation><expect>^0$</expect></criterion>
`D4-AC3` -- THE WRONG ARTIFACTS ARE GONE from the cloud group (brief F6).

<criterion id="D4-AC4" cell_refs="CG-s-7"><invocation>bash .tools/comp-graph status --json | python -c "import sys,json; d=json.load(sys.stdin); r=[g for g in d['graphs'] if g['name']=='projection.current'][0]; print('FIELDS', all(k in r for k in ('vintage','age_line','built_at','writer_id','producer_mode','node_count','edge_count','edges_skipped_missing_endpoint','artifact_bytes','band_status')))"</invocation><expect>FIELDS True</expect></criterion>
`D4-AC4` -- THE CONTRACT'S FIELD SET is reported (`PROJECTION_CONTRACT.md` s.8, CG-s-7 handoff) in `--json`.

<criterion id="D4-AC5" cell_refs="CG-s-7"><invocation>python .tools/comp-read org/modules/graph/graph_status_cli.py --enumerate 'sns|put_metric|cloudwatch|events\.put|schedule|create_alarm' --limit 5</invocation><expect>ENUMERATE: 0 hit\(s\)</expect></criterion>
`D4-AC5` -- R4 HOLDS: no alarm, SNS, metric, event or schedule call in the engine (the census, denominator printed by the tool).

<criterion id="D4-AC6" cell_refs="CG-s-7"><invocation>python .tools/tests/test_cg7_status_read_battery.py</invocation><expect>PASS</expect></criterion>
`D4-AC6` -- THE BATTERY passes at the direct grain, each arm with its denominator.

<criterion id="D4-AC7" cell_refs="CG-s-7"><invocation>bash .tools/commit-gate.sh org/modules/graph/graph_status_cli.py .tools/tests/test_cg7_status_read_battery.py</invocation><expect>pre-commit gate clean</expect></criterion>
`D4-AC7` -- COMMIT GATE clean on every `.py` this order touches.

<expected_criteria>D4-AC1, D4-AC2, D4-AC3, D4-AC4, D4-AC5, D4-AC6, D4-AC7</expected_criteria>

## SURFACES

`org/modules/graph/graph_status_cli.py` · `.tools/comp-graph` (READ; unchanged unless the shim needs the env passed through -- it does not, env inherits) · `.tools/tests/test_cg7_status_read_battery.py` (NEW) · `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~T/PROJECTION_CONTRACT.md` s.3, s.6, s.8 (READ) · `infra/aws/terraform/globgrph/item2a.tf:439` (READ: the schedule) · the live pointer + manifests (READ).

## BOUNDS

- **PULL READ ONLY.** Nothing created in AWS; no S3 write; no engine call; no rebuild; no cache file.
- **No edit outside `graph_status_cli.py`, the battery, and your deliverables** (the local trace-layer rows and the contract text stay as they are).
- **The plant is a local fixture**, never a live object.
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
org/modules/graph/graph_status_cli.py
.tools/comp-graph
.tools/tests/test_cg7_status_read_battery.py
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-D-4.operator-status-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> @70918d5d2b (v0.2), cell CG-s-7 (s.1a; STAGE 3).
<owned_cells>CG-s-7</owned_cells>
Read-dependencies, NOT claimed: CG-s-3 (DONE @93c26badf8, the manifest + pointer contract). Downstream, NOT yours: CG-x-8 (the read taken on a real morning, cut as TO-CG-D-11 to this slot).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-04 06:2xZ at the cut: GATES ARMED 21 across 5 carriers (C1 21 -> 5, C2 4, C3 12, C4 20, C5 337); NEEDS-READ 138 prose fields (a reading list, never counted); the C3 moratoria (no alarm/monitor) bind this face's BOUNDS and R4.
comp-iam: DECLARED-NOT-APPLICABLE -- a read of two S3 objects with the seat's existing credentials; no principal, policy or grant is read or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 on the decomposition (rc 0 @07288006e5, 22/22 cited commits VERIFIED); the deliverable's validator context is the L9 seat's compose.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `D4-AC1`..`D4-AC7`. The ASSIGNEE fills a `org/standards/PROOF_OF_SPEC.schema.json` instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/NFRA_CLDGRPH.TO-CG-D-4.operator-status-read.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> D4-AC1,D4-AC2,D4-AC3,D4-AC4,D4-AC5,D4-AC6,D4-AC7` BEFORE the complete flip, which the WORKER commits itself with the instance and the deliverable. `D4-AC2` (the plant reads NO), `D4-AC3` and `D4-AC5` are the controls that must be able to FAIL. No judgment criterion on this face.
</proof_of_spec>

<compiler_tools_mandate>
BEFORE WRITE: `python .tools/comp-read org/modules/graph/graph_status_cli.py --for "the cloud group rows, how records are collected and rendered, the --json shape, and every place the local trace-layer group is computed so it is left alone"`; `python .tools/comp-read org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~T/PROJECTION_CONTRACT.md --for "the pointer body, the manifest field set, the straddle rule and the CG-s-7 handoff"`. BEFORE COMMIT: `bash .tools/commit-gate.sh` on every `.py` touched (D4-AC7); the battery direct AND `python -m pytest .tools/tests/test_cg7_status_read_battery.py -q`.
</compiler_tools_mandate>

**THE REPORT IS YOUR FINAL MESSAGE, ONCE, IN THE `WORKER REPORT` SHAPE.** You cannot send a message and nobody can send you one.

**GO = the spawn itself.**
