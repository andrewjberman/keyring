# Deploy Completion Record
**Date opened:** 2026-07-09T12:26:09.108694+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / L4 -- CRITERION v4. A VERDICT REQUIRES AN OBSERVATION. (0.7.0_AE_CloudOps 043200Z; COO 042243Z caught v3.)
Supersedes ed5b2479a (invocation-gated: FALSE-PASSED live) and 3b2c817a5/f7a74aaf6 (crash and aws-failure both
printed a VERDICT). Do not carry any earlier command block forward.

=== WHY v4 EXISTS: v3 RELOCATED THE COLLISION ONTO THE VERDICT THIS LEDGER RESTS ON ===
v3 fixed `1 = FAIL` colliding with Python's uncaught-exception code. But its `except` printed
`CANNOT-EVALUATE` whenever the marker could not be READ. EXERCISED, not argued:
    aws s3 cp <nonexistent key> | python <v3>   -> stdout 'CANNOT-EVALUATE: ...'   rc=2
    aws s3 cp --badflag         | python <v3>   -> stdout 'CANNOT-EVALUATE: ...'   rc=2
A typo'd key, expired creds, no network, or a bad flag was BYTE-IDENTICAL to the verdict this ledger is
currently resting on. v3 collapsed NO OBSERVATION into a NEGATIVE OBSERVATION -- CVO's law (a denied call looks
exactly like a call nobody made), committed inside the repair of the previous instance of it.

  CANNOT-EVALUATE means: I READ the marker, and there is no stamp after T_d.   <- a real, negative observation
  It NEVER means:        I never read the marker.                              <- that is INVOCATION-ERROR

=== THE FOUR TOKENS. THE TOKEN IS THE ORACLE; THE EXIT CODE IS A CONVENIENCE. ===
  PASS:              stamp after T_d AND marker lists all 4 (cse PRESENT)   rc 0   -> the merge landed
  FAIL               stamp after T_d AND cse ABSENT                         rc 1   -> clobber. EXPECTED, BY DESIGN.
  CANNOT-EVALUATE:   marker READ + well-formed; no stamp after T_d          rc 2   -> ledger stays OPEN
  INVOCATION-ERROR:  no marker was read, or it is not a marker              rc 3   -> NOT A VERDICT. Re-run.
                                                                                      Do not record. Do not close.
stdout MUST begin with one of those four. ANY OTHER OUTPUT, OR NONE, IS AN INVOCATION-ERROR -- e.g. a `python`
usage error (rc 2, empty stdout) or a SyntaxError (rc 1, empty stdout). rc alone can never tell you which:
  rc 0 = success default   rc 1 = ANY uncaught exception   rc 2 = python/argparse usage error   rc 3 = ours alone
PUT THE CONTROL ON THE RETRIEVAL, NOT THE PATTERN.

=== CORRECTIONS ALREADY EATEN. Do not re-derive; do not carry the old prose. ===
(C1) derive = cron(0 2 * * ? *) = 02:00Z, not "~02:10Z".
(C2) incremental_updater is NOT hourly and has NO schedule: SQS event-source-mapping on
     opal-globgrph-incremental-events; `aws events list-rule-names-by-target` on its ARN -> EMPTY. NO 03:00Z READ.
(C3) AN INVOCATION IS NOT A STAMP. lambda_function.py:718 calls the stamp (:722) only inside
     `if all_nodes or all_deletes:` -- a no-op batch invokes and never stamps; _provenance.py:227 skips a
     not-newer stamp. Observed: invocation 02:12:00Z after T_d, zero stamps, queue drained. CloudWatch
     Invocations can NEVER establish this gate.
(C4) A CRASH IS NOT A VERDICT.  (C5) A FAILED READ IS NOT A VERDICT EITHER.

=== EVIDENCE BANKED (limb A; unrecoverable if lost) ===
T_d = 2026-07-10T02:09:13Z -- derive stamp caught live: writer_id=derive_runner, 4 tables, cse PRESENT,
ETag 94ab4adc17ca85fc0d8681c5c8bfd09a, size 1502. Versioning OFF (Andrew-locked #5) -> the next incremental
stamp DESTROYS it; snapshot held off-bucket. Without it the criterion degrades from FAIL to un-evaluable with
nothing to distinguish them -- why CTO made _branch_head.history/{ts}.json a PRECONDITION of the merge fix.
That ETag is also exactly what put_object(IfMatch=) needs: the CAS fix and the history archive are ONE READ.

=== THE CRITERION ===
An incremental STAMP after T_d is EXACTLY: writer_id == 'incremental_updater' AND committed_at_iso > T_d
(_provenance.py:201,220,221 set both on every successful stamp).
A quiet SQS queue is not evidence the merge works. Neither is a busy one. Only a STAMP is evidence.

=== RUN IT (any lane). The aws read is checked BEFORE python ever sees the stream. ===
MARKER=$(aws s3 cp s3://opal-313476888478-globgrph/warehouse/_branch_head.main.json - 2>/dev/null); RC=$?
if [ $RC -ne 0 ]; then echo "INVOCATION-ERROR: aws read failed (rc=$RC). The marker was never read. NOT a verdict."; exit 3; fi
printf '%s' "$MARKER" | python -c "
import sys, json, datetime as dt
T_d = dt.datetime.fromisoformat('2026-07-10T02:09:13+00:00')
raw = sys.stdin.read()
if not raw.strip():
    print('INVOCATION-ERROR: empty stdin -- the marker was never read. NOT a verdict.')
    raise SystemExit(3)
try:
    d = json.loads(raw)
except Exception as e:
    print('INVOCATION-ERROR: stdin is not JSON (%s). The marker was never read. NOT a verdict.' % type(e).__name__)
    raise SystemExit(3)
if not isinstance(d, dict) or 'writer_id' not in d or 'table_metadata' not in d:
    print('INVOCATION-ERROR: payload is not a branch-head marker. NOT a verdict.')
    raise SystemExit(3)
w = d.get('writer_id')
c = d.get('committed_at_iso')
tm = d.get('table_metadata') or {}
if not c:
    print('INVOCATION-ERROR: marker has no committed_at_iso -- cannot order it against T_d. NOT a verdict.')
    raise SystemExit(3)
try:
    c_dt = dt.datetime.fromisoformat(c)
except Exception:
    print('INVOCATION-ERROR: committed_at_iso is unparseable. NOT a verdict.')
    raise SystemExit(3)
if not (w == 'incremental_updater' and c_dt > T_d):
    print('CANNOT-EVALUATE: marker READ, no incremental stamp after T_d (writer=%s committed_at=%s). Ledger stays OPEN.' % (w, c))
    raise SystemExit(2)
if 'cse' in tm:
    print('PASS: merge landed -- n=%d %s' % (len(tm), sorted(tm)))
    raise SystemExit(0)
print('FAIL (expected): cse clobbered -- n=%d %s' % (len(tm), sorted(tm)))
raise SystemExit(1)
"

=== EXERCISED. Full range + the R6 rail on the token itself. ===
VERDICT PATHS (marker read + well-formed):
    live marker                     rc 2  CANNOT-EVALUATE     <- state at 04:32Z
    synthetic clobber (no cse)      rc 1  FAIL
    synthetic merge (cse)           rc 0  PASS
    stale stamp (pre-T_d)           rc 2  CANNOT-EVALUATE
R6 RAIL -- CANNOT-EVALUATE must NEVER appear when the marker was not read. LEAKED INTO 0 of 5:
    empty stdin / non-JSON / JSON-not-a-marker / no committed_at_iso / unparseable timestamp   -> rc 3 INVOCATION-ERROR
    aws nonexistent key -> rc 3 INVOCATION-ERROR      aws --badflag -> rc 3 INVOCATION-ERROR
POSITIVE CONTROL on that rail (else it is vacuous): the live marker STILL yields CANNOT-EVALUATE.
The body carries ZERO double-quote characters: it parses inside `python -c "..."` AND standalone in a file.

=== VERDICT RECORDED 2026-07-10T05:00:19Z: FAIL, EXACTLY AS DESIGNED. L4 DOES NOT CLOSE. ===
The first incremental STAMP after T_d landed, and the criterion fired on its first real evaluation:
    stored v4 command, run verbatim  ->  rc 1  token FAIL   ("cse clobbered -- n=3")
The stamp is real and ordered:
    writer_id=incremental_updater   committed_at_iso=2026-07-10T05:00:19.084753+00:00   (> T_d)
    ETag 0d05ce2e0c343ac82ace970ef1ee733c   LastModified 2026-07-10T05:00:20Z
    transitions: 02:07:59Z n=3 -> 02:09:15Z derive_runner n=4 cse PRESENT -> 05:00:36Z n=3 cse ABSENT

STATE vs MECHANISM (Rule 22; these are not the same claim):
  STATE      the predicate reads FAIL from the CURRENT marker alone: a stamp after T_d, and cse absent.
  MECHANISM  that the incremental ERASED what the derive wrote -- rather than the derive never writing cse --
             rests on the banked transient (ETag 94ab4adc17ca85fc0d8681c5c8bfd09a, 4 tables, 02:09:13Z), now
             DESTROYED on the bucket. Versioning is OFF. Without that off-bucket snapshot the two are
             indistinguishable and this verdict would be UN-EVALUABLE, not FAIL. That is the empirical case for
             _branch_head.history/{ts}.json as a PRECONDITION of the merge fix (CTO 021626Z).

b9f991994 (read-path honesty) EXERCISED for the first time -- observable ONLY while cse is absent:
    LIVE        cse: ABSENT FROM MARKER -- vintage unverifiable (26h cadence declared; last writer
                'incremental_updater' did not stamp it)
    R2 VARIANCE synthetic 4-table marker (cse PRESENT) -> does NOT print it (the line is not unconditional)
    R-NULL      no marker -> 'per-table vintage: UNKNOWN (no branch-head marker)'
The silent omission it replaced would have printed NOTHING for cse at this exact moment. That visible failure IS
the deliverable of b9f991994.

=== THE CRITERION IS NOW SPENT FOR THIS T_d. A RE-TEST NEEDS A NEW ONE. ===
FAIL is the CORRECT and EXPECTED result and it DOES NOT CLOSE L4: the stamp_marker merge + CAS has not landed.
After the merge fix deploys, this criterion CANNOT be re-run against T_d=2026-07-10T02:09:13Z -- that window is
closed and its verdict is recorded. A fresh evaluation requires:
    (1) a NEW derive 4-table stamp -> that becomes T_d'
    (2) a subsequent incremental STAMP (writer_id=incremental_updater AND committed_at_iso > T_d')
    (3) the marker STILL listing all 4 -> only then PASS.
Snapshot T_d' off-bucket BEFORE step (2), or the same evidence problem recurs.

L4 STAYS OPEN. proof=None. A REFUSAL, not a failure to finish -- and now a MEASURED one.

=== THE MERGE FIX REMAINS HELD ===
IfMatch CAS confirmed in BOTH DEPLOYED runtimes (the dev box is not the runtime), bounded 412 retry, LOUD raise
on exhaustion AND on ParamValidationError (stamp_marker never raises, so an unsupported IfMatch is swallowed into
a WARN and SILENTLY STOPS STAMPING). Probe 8c0b67afd UNRUN, first-light. Verdict IGNORED (param accepted, silently
dropped) is the one that kills us. Fold _branch_head.history/{committed_at_iso}.json into the same CAS write.
Do NOT enable bucket versioning (Andrew-locked #5).

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
- 20260710T042550Z HELD-SOVEREIGN-GATED gate=external/L4 -- CRITERION v4. A VERDICT REQUIRES AN OBSERVATION. (0.7.0_AE_CloudOps 043200
- 20260710T050407Z HELD-SOVEREIGN-GATED gate=external/L4 -- CRITERION v4. A VERDICT REQUIRES AN OBSERVATION. (0.7.0_AE_CloudOps 043200
