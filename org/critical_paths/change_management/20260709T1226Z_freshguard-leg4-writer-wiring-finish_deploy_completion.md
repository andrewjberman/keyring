# Deploy Completion Record
**Date opened:** 2026-07-09T12:26:09.108694+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / L4 -- CRITERION CORRECTED TWICE. GATE ON THE **STAMP**, NOT THE INVOCATION. (0.7.0_AE_CloudOps 021930Z.)

!! THE PRIOR GATE TEXT OF THIS LEDGER (ed5b2479a, ~15 min old, which CTO 021626Z ratified as "the authority
   over my memo") CONTAINED A FALSE-PASS AND IT FIRED LIVE TONIGHT. Do not execute it. Superseded below. !!

=== WHAT WENT WRONG (mine; the third correction to this same criterion) ===
v1 clock:      "read 4 tables at ~02:20Z, close"          -> certifies a transient.        (CTO re-spec killed it)
v2 clock:      "after the next HOURLY incremental, ~03:00Z" -> a clock on an SQS trigger.  (I killed it, ed5b2479a)
v3 invocation: ">=1 incremental_updater INVOCATION completed at t > T_d AND marker still lists 4" -> FALSE-PASS.

**AN INVOCATION IS NOT A STAMP.** Two source-confirmed paths where incremental_updater runs and never touches
the marker:
  (a) `incremental_updater/lambda_function.py:718` -- `stamp_branch_head_marker()` (:722) is called ONLY inside
      `if all_nodes or all_deletes:`. A NO-OP BATCH INVOKES AND NEVER STAMPS.
  (b) `_provenance.py:227` -- monotonicity guard: `if existing.committed_at_iso >= mine: MARKER_SKIP not-newer`.
      A not-newer stamp is SKIPPED.

OBSERVED LIVE, TONIGHT, WITHIN 3 MINUTES OF THE CRITERION BEING WRITTEN:
    T_d                = 2026-07-10T02:09:13Z  (derive_runner, 4 tables, cse PRESENT, ETag 94ab4adc17ca85fc0d8681c5c8bfd09a)
    invocation         = 2026-07-10T02:12:00Z  (CloudWatch Invocations Sum=1, AFTER T_d)
    marker at 02:19Z   = writer_id=derive_runner, committed_at_iso=2026-07-10T02:09:12.714167+00:00, n=4, cse PRESENT
    SQS at 02:19Z      = ApproximateNumberOfMessages=0, NotVisible=0  (fully drained)
=> v3 reads: ">=1 invocation" TRUE, "marker lists 4" TRUE  =>  **PASS**, on a merge that DOES NOT EXIST.
The 02:12Z invocation was a no-op batch. It never stamped. The 4 tables are still the DERIVE's.

=== THE CORRECTED CRITERION -- gate on an incremental STAMP, observed on the marker itself ===
An "incremental stamp after T_d" is EXACTLY:
    marker.writer_id == "incremental_updater"  AND  marker.committed_at_iso > T_d
(`_provenance.py:201,220,221` set both on every successful stamp -- they are the stamp's own record, written by
the code path under test, and they are the only observable that distinguishes a stamp from a run.)

  PASS            incremental stamp after T_d  AND  marker lists all 4 (cse PRESENT)   -> the merge landed
  FAIL            incremental stamp after T_d  AND  cse ABSENT                          -> clobber; EXPECTED today
  CANNOT-EVALUATE no incremental stamp after T_d, REGARDLESS OF INVOCATION COUNT        -> exit 2, ledger OPEN
                  ^ this is the state as of 2026-07-10T02:19Z. One invocation, zero stamps, queue drained.

  A quiet SQS queue is not evidence the merge works. Neither is a busy one. Only a STAMP is evidence.
  Silence from an untriggered instrument and silence from a passing one are byte-identical.

=== EXACT READ COMMANDS (any lane; T_d = 2026-07-10T02:09:13Z) ===
aws s3 cp s3://opal-313476888478-globgrph/warehouse/_branch_head.main.json - | python -c "
import sys,json,datetime as dt
T_d = dt.datetime.fromisoformat('2026-07-10T02:09:13+00:00')
d = json.load(sys.stdin); tm = d.get('table_metadata',{}) or {}
w  = d.get('writer_id'); c = d.get('committed_at_iso')
stamped = (w=='incremental_updater') and c and dt.datetime.fromisoformat(c) > T_d
if not stamped:
    print(f'CANNOT-EVALUATE: no incremental stamp after T_d (writer={w} committed_at={c}). Ledger stays OPEN.'); raise SystemExit(2)
print(('PASS: merge landed' if 'cse' in tm else 'FAIL (expected): cse clobbered') + f\" -- n={len(tm)} {sorted(tm)}\")
raise SystemExit(0 if 'cse' in tm else 1)
"
# exit 0 = PASS   exit 1 = FAIL (expected today)   exit 2 = CANNOT-EVALUATE (never a pass)
# CloudWatch Invocations is a SUPPORTING signal ONLY -- it can NEVER establish the gate. Do not use it as one.

=== EVIDENCE PRESERVED ===
Versioning is OFF (Andrew-locked #5). The derive's 4-table object is destroyed by the next incremental stamp, so
limb (A) survives only in the off-bucket snapshot: scratchpad/leg4_derive_4table_marker_20260710T0209Z.json
(ETag 94ab4adc17ca85fc0d8681c5c8bfd09a). CTO 021626Z has elevated `_branch_head.history/{ts}.json` from
"nice-to-have" to a PRECONDITION of the merge fix landing: you cannot ship a CAS whose success condition is
unobservable after one subsequent write. The same ETag is the value `put_object(IfMatch=)` needs.

=== THE MERGE FIX REMAINS HELD (unchanged) ===
IfMatch CAS + bounded 412 retry + LOUD raise on exhaustion AND on ParamValidationError (stamp_marker is
best-effort/never-raises, so an unsupported IfMatch is swallowed into a WARN and SILENTLY STOPS STAMPING).
Probe 8c0b67afd UNRUN, hard-gated to first light, must exercise BOTH deployed runtimes. Verdict IGNORED (param
accepted, silently dropped) is the one that kills us. Fold the history archive into the same CAS write.

L4 STAYS OPEN. Today's honest verdict is CANNOT-EVALUATE, not FAIL, and not PASS. (held since 2026-07-09T13:11:12.866381+00:00)
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
