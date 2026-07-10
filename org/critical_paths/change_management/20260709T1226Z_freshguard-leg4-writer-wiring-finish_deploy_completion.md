# Deploy Completion Record
**Date opened:** 2026-07-09T12:26:09.108694+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / L4 -- CRITERION v3. Gate on the STAMP; classify by the VERDICT TOKEN, not the exit code. (0.7.0_AE_CloudOps 041930Z.)
Supersedes ed5b2479a (invocation-gated, FALSE-PASSED live) and 3b2c817a5's command block (crash reads as FAIL).

=== CORRECTIONS THIS LEDGER HAS ALREADY EATEN. Do not re-derive them; do not carry the old prose. ===
(C1) derive = cron(0 2 * * ? *) = 02:00Z, not "~02:10Z".
(C2) incremental_updater is NOT hourly and has NO schedule: SQS event-source-mapping on
     opal-globgrph-incremental-events (Enabled); `aws events list-rule-names-by-target` on its ARN -> EMPTY.
     "Hourly" was an OBSERVED CADENCE that four artifacts promoted to a SCHEDULE. THERE IS NO 03:00Z READ.
(C3) AN INVOCATION IS NOT A STAMP. lambda_function.py:718 calls stamp_branch_head_marker() (:722) only inside
     `if all_nodes or all_deletes:` -- a no-op batch invokes and never stamps. _provenance.py:227 skips a
     not-newer stamp. Observed: invocation 02:12:00Z after T_d, zero stamps, queue drained -> the old criterion
     read PASS on a merge that does not exist. CloudWatch Invocations can NEVER establish this gate.
(C4) THE PREDICATE'S FAILURE MODE MUST NOT BE A VERDICT. Python exits 1 on any uncaught exception, and the old
     block defined 1 = FAIL -- so a SyntaxError, an unreadable marker, or a bad extraction returned exactly the
     answer everyone expected tonight. Proven: extracting the old body to a file -> SyntaxError -> exit 1 ->
     "FAIL (expected)". v3 below exits 2 on every anticipated failure and carries ZERO double-quote characters,
     so it parses both inside `python -c "..."` and standalone in a file.

=== EVIDENCE BANKED (limb A of the criterion, and it is unrecoverable if lost) ===
T_d = 2026-07-10T02:09:13Z -- tonight's derive stamp, caught live by a marker-transition poller:
    writer_id=derive_runner  tables=[cse,graph_contracts,graph_edges,graph_nodes]  cse=PRESENT
    ETag 94ab4adc17ca85fc0d8681c5c8bfd09a   size 1502
Bucket versioning is OFF (Andrew-locked #5) -> the next incremental stamp DESTROYS that object. Snapshot held
off-bucket. Without it the criterion degrades from FAIL to UN-EVALUABLE with nothing to distinguish them, which
is why CTO elevated _branch_head.history/{ts}.json to a PRECONDITION of the merge fix. That ETag is also the
exact value put_object(IfMatch=) needs: the CAS fix and the history archive are ONE READ.

=== THE CRITERION ===
An incremental STAMP after T_d is EXACTLY:  writer_id == 'incremental_updater'  AND  committed_at_iso > T_d
(_provenance.py:201,220,221 set both on every successful stamp.)
  PASS             stamp-after-T_d AND marker lists all 4 (cse PRESENT)  -> the merge landed
  FAIL             stamp-after-T_d AND cse ABSENT                        -> clobber. EXPECTED, BY DESIGN.
  CANNOT-EVALUATE  no stamp after T_d, REGARDLESS of invocation count    -> ledger stays OPEN
A quiet SQS queue is not evidence the merge works. Neither is a busy one. Only a STAMP is evidence.

=== RUN IT. CLASSIFY BY THE TOKEN ON STDOUT, NOT BY THE EXIT CODE. ===
aws s3 cp s3://opal-313476888478-globgrph/warehouse/_branch_head.main.json - | python -c "
import sys, json, datetime as dt
T_d = dt.datetime.fromisoformat('2026-07-10T02:09:13+00:00')
try:
    d = json.load(sys.stdin)
    tm = d.get('table_metadata', {}) or {}
    w = d.get('writer_id')
    c = d.get('committed_at_iso')
    stamped = (w == 'incremental_updater') and bool(c) and dt.datetime.fromisoformat(c) > T_d
except Exception as e:
    print('CANNOT-EVALUATE: predicate could not read the marker (%s: %s)' % (type(e).__name__, e))
    raise SystemExit(2)
if not stamped:
    print('CANNOT-EVALUATE: no incremental stamp after T_d (writer=%s committed_at=%s). Ledger stays OPEN.' % (w, c))
    raise SystemExit(2)
if 'cse' in tm:
    print('PASS: merge landed -- n=%d %s' % (len(tm), sorted(tm)))
    raise SystemExit(0)
print('FAIL (expected): cse clobbered -- n=%d %s' % (len(tm), sorted(tm)))
raise SystemExit(1)
"

STDOUT MUST BEGIN WITH ONE OF: 'PASS:' | 'FAIL' | 'CANNOT-EVALUATE:'.
ANY OTHER OUTPUT (or none) = INVOCATION-ERROR. It is NOT a verdict. Re-run; do not record; do not close.
Exit codes 0/1/2 mirror the tokens, but 1 is ALSO Python's uncaught-exception code -- so the TOKEN is the oracle
and the exit code is the convenience. Put the control on the RETRIEVAL, not the pattern.

=== EXERCISED ACROSS ITS FULL RANGE (a criterion that has only ever returned one value is not a criterion) ===
    live marker                          -> exit 2  token CANNOT-EVALUATE   <- state at 04:19Z
    synthetic incremental stamp, no cse  -> exit 1  token FAIL
    synthetic incremental stamp, w/ cse  -> exit 0  token PASS
    stale stamp (committed before T_d)   -> exit 2  token CANNOT-EVALUATE   (an old stamp is not a stamp)
    non-JSON on stdin                    -> exit 2  token CANNOT-EVALUATE   (NOT FAIL)
    committed_at_iso = 'NOT-A-TIMESTAMP' -> exit 2  token CANNOT-EVALUATE   (NOT FAIL)

=== STATE AT 2026-07-10T04:19Z: CANNOT-EVALUATE ===
One invocation after T_d (02:12:00Z), ZERO stamps, SQS drained 0/0. Everyone -- CTO, COO, me -- expected FAIL
tonight. FAIL requires a stamp we have not had. It is not yet evaluable, and that is the honest verdict.

=== THE MERGE FIX REMAINS HELD (unchanged) ===
stamp_marker must MERGE over existing table_metadata, but a bare merge is STRICTLY WORSE than the clobber: a
read-modify-write against an event-driven writer with no conditional put trades a VISIBLE erasure for an
INVISIBLE one. Conditions: IfMatch CAS confirmed in BOTH DEPLOYED runtimes (Lambda bundled botocore + derive
image pinned boto3 -- the dev box is not the runtime), bounded 412 retry, LOUD raise on exhaustion AND on
ParamValidationError (stamp_marker is best-effort/never-raises, so an unsupported IfMatch is swallowed into a
WARN and SILENTLY STOPS STAMPING). Probe 8c0b67afd UNRUN, hard-gated to first light. Verdict IGNORED (param
accepted, silently dropped) is the one that kills us. Fold _branch_head.history/{committed_at_iso}.json into the
same CAS write. Do NOT enable bucket versioning (Andrew-locked #5).

L4 STAYS OPEN. This is a REFUSAL, not a failure to finish. (held since 2026-07-09T13:11:12.866381+00:00)
**Deploy:** FRESHGUARD leg-4 finish: wire all 3 writers (derive_runner/incremental_updater/cse_store) to the centralized _provenance.stamp_marker so per-table last_write_iso lands live. GROUNDED: leg-4 is SOURCE-INCOMPLETE (unwired), not merely undeployed -- the centralized stamp has ZERO call sites; all 3 writers stamp their own local marker with no last_write_iso field. HELD on CTO approach-gate (A centralize-import vs B 3-copy).
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: wire 3 writers -> _provenance.stamp_marker + Dockerfile COPY _provenance.py + Lambda zip vendors _provenance.py | hash pushed | committed 86ab291f8 (6 files, +61/-133), pushed origin/CLOUD edc6790c4..86ab291f8. All 3 writers delegate to _provenance.stamp_marker; Dockerfile COPY _provenance.py; zip vendors _provenance.py (sha256 9dC0bal9...); source map updated. commit-gate clean; grep-proven zero residual local marker-write (only _provenance.py:227). | CLOSED 20260709T125750Z |
| L2 | activation | derive image CodeBuild rebuild+push (derive_runner+cse_store call shared stamp; image carries _provenance.py) | CodeBuild build-id + image digest | CodeBuild globgrph-derive-build:fb7b48b9 SUCCEEDED/COMPLETED. APPLIED-truth: ECR opal-globgrph-derive-runner:latest pushed 2026-07-09T13:06Z, tag 20260709-130548, digest sha256:2b7f5ec0bfdb329d25cef5adeaad9ba1abc23904ada56aefd68d87a4990e821a. Image carries _provenance.py + derive_runner/cse_store delegation (P3-FREE: motif reverted to fad55a83c^, signature-free per CTO sequencing). Task-def globgrph-derive-runner references :latest -> nightly auto-picks up (no revision needed). | CLOSED 20260709T130943Z |
| L3 | activation | incremental_updater Lambda: rebuild zip(+_provenance.py) + safe-apply TF (source_code_hash tracks) | get-function CodeSha256 + 0-diff plan | safe-apply complete 0-add/1-change/0-destroy (HALT-gate clean). APPLIED-truth (Rule22a): get-function-configuration opal-globgrph-incremental-updater CodeSha256=9dC0bal9JcpQ9D0CuBaeXOT1E9LY80btOGR6lsHmzTA= (== rebuilt zip w/ _provenance.py vendored), State=Active, LastUpdateStatus=Successful, LastModified 2026-07-09T13:07:33Z; targeted 0-diff plan = No changes. Lambda now delegates to _provenance.stamp_marker. | CLOSED 20260709T130834Z |
| L4 | verify | live marker last_write_iso POPULATED all 3 tables, EXERCISED (real incremental write + nightly derive), APPLIED-truth Rule22a | marker read per-table non-null + writer_id |  | OPEN |

## Log

- 20260709T122609Z OPENED by 0.7.0_AE_CloudOps with 4 leg(s)
- 20260709T125750Z LEG L1 closed: committed 86ab291f8 (6 files, +61/-133), pushed origin/CLOUD edc6790c4..86ab291f8. All 3 writers delegate to _provenance
- 20260709T130834Z LEG L3 closed: safe-apply complete 0-add/1-change/0-destroy (HALT-gate clean). APPLIED-truth (Rule22a): get-function-configuration opal
- 20260709T130943Z LEG L2 closed: CodeBuild globgrph-derive-build:fb7b48b9 SUCCEEDED/COMPLETED. APPLIED-truth: ECR opal-globgrph-derive-runner:latest push
- 20260709T131112Z HELD-SOVEREIGN-GATED gate=external/next nightly derive_runner ECS run ~02:10Z (last_write_iso all 4 tables) + next 
- 20260709T232036Z HELD-SOVEREIGN-GATED gate=external/GATE RESTATED 2026-07-09T23:20Z (0.7.0 finding 231918Z, source+applied+exercised
- 20260709T232058Z HELD-SOVEREIGN-GATED gate=external/GATE RESTATED 2026-07-09T23:20Z (0.7.0 finding 231918Z; source + applied + exerc
- 20260709T232435Z HELD-SOVEREIGN-GATED gate=external/L4 RE-SPECCED (CTO 232022Z) -- the old criterion ('last_write_iso populated on a
- 20260710T021104Z HELD-SOVEREIGN-GATED gate=external/L4 RE-SPECCED (CTO 232022Z) + TRIGGER-MODEL CORRECTED (0.7.0_AE_CloudOps 020930Z
- 20260710T021840Z HELD-SOVEREIGN-GATED gate=external/L4 -- CRITERION CORRECTED TWICE. GATE ON THE **STAMP**, NOT THE INVOCATION. (0.7
- 20260710T041752Z HELD-SOVEREIGN-GATED gate=external/L4 -- CRITERION v3. Gate on the STAMP; classify by the VERDICT TOKEN, not the ex
