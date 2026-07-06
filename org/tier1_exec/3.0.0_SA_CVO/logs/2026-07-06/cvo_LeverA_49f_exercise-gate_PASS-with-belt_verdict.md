# CVO exercise-gate verdict: ADVI_BDAPIMIG Lever A (49F/bd) -- PASS (with a tomorrow-daily all-4 belt)

**archetype:** VALIDATE
**serial:** 3.0.0_SA_CVO | **date:** 2026-07-06 ~1917Z | **subject:** Lever A cookie-first daily-OTP skip (bd-v2.48.0, 0.7.0~A) | **ledger owner:** 2.0.0_SA_COO (L4=this gate)
**method:** exercise-the-path + independent live grounding (CloudWatch/S3/SM/code) -- NOT certed off AE self-report. This is the finding Andrew's 07-06 BD-OTP observation kicked off, verified end-to-end.

## VERDICT: PASS (49F/bd) -- with one non-blocking belt (tomorrow's natural daily all-4-fresh).

Deploy independently verified: bd-v2.48.0 tag @ 804f66020; live Lambda CodeSha256 = EOOuJMrkSk...N4= == tagged artifact (LastModified 18:53:18Z).

### Condition-by-condition (COO's 4 + CTO's exercise-gate)
1. **SKIP DECISION + ZERO OTP -- PROVEN LIVE.** session-trigger @19:00:06Z: session-check positive-live -> "Lever A: cookie POSITIVE-live -> SKIP mint, direct-invoke bd-49f-runner", mode-marker `skip-live-direct-invoke`. Independently counted **StartInstances/RunCommand/session-fetch = 0** (PowerShell, real query -- NOTE: my first Bash query returned a false "0" because MSYS mangled the leading-`/` log-group name into an InvalidParameterException; caught it, re-ran in PowerShell). No box start, no SSM, no OTP.
2. **BRONZE LANDS (the load-bearing one) -- PROVEN.** The 19:00 skip invoke drove the runner to auth-OK on the live cookie + emit `bronze/2026-07-06/_BRONZE_COMPLETE.json` (19:00:10Z, tables=4). Plus FRESH-WRITE proven: `forwardfill_v2/transactions/TRANSACTIONS_DAILY_2026-07-06.xlsx` LastModified ADVANCED to 19:10:48Z on the skip-path cookie (pulled=['transactions']). So the skip path produces real bronze -- not a bare 200. (Size 4387B = low-activity-day file; the LastModified-advance + pulled= is the mechanism proof, which is what Lever A governs.)
3. **SINGLE-FIRE -- PROVEN + CODE-GROUNDED.** Skip branch returns BEFORE any SSM dispatch (lambda_function.py:252-262) -> bd-49f-session-complete never fires -> exactly one `_fire_runner` direct invoke. Log-confirmed: one "Invoked bd-49f-runner status=202", zero SSM.
4. **SKIP-vs-MINT PARITY -- CODE-GROUNDED.** Both legs share the ONE `_fire_runner` (l.205-213): same FunctionName / InvocationType=Event / empty payload -> structurally indistinguishable.
5. **FAIL-SAFE -- CODE-GROUNDED (honest-limit: not live-fired, correctly).** `_session_is_positive_live` (l.216-235) is fail-safe-absolute: SM-read-error / empty-cookie / probe-raise / probe-negative ALL `return False -> MINT`; returns True ONLY on positive-live. Belt: skip-path invoke raise -> falls through to the UNCHANGED mint path (l.263-266). I did NOT live-fire a dead cookie (would fire a real OTP on the shared 49f/cot mailbox mid-un-freeze -- not worth it; the fall-through target is unchanged, pre-existing, already-proven code). Honest-limit recorded per the discipline.

### The force-pull incident (resolved -- NOT a Lever A defect)
My requested force=true fresh-pull triggered a retry storm (5 overlapping runner execs 19:05-19:09, 401s on 3/4 tables). ROOT CAUSE (AE-owned, honest): AE invoked force=true as **RequestResponse (sync)**; the ~3min runner exceeded the AWS-CLI 60s socket read-timeout, and **botocore default-retry re-sent the invoke 5x** -> concurrent runners hammered BD -> bearer-401 on the later templates (mislabeled "cookie dead"). INDEPENDENTLY CONFIRMED it was storm-induced, NOT a real cookie/pull gap:
- Cookie LIVE after the storm: session-check @19:12:01Z -> `live=True`.
- Non-destructive: allocations/realized/unrealized 07-06 files unchanged at 00:13Z (storm's failed-table gate blocked overwrite + blocked the sentinel -> no spurious silver trigger).
- Storm settled: 0 runner STARTs since 19:09:30Z.
- No alarm paged Andrew.
This is downstream of the skip decision (Lever A fires the runner ONCE, proven), not a Lever A behavior. The clean all-4-fresh via skip was CONFOUNDED by this client-invoke error -- hence the belt below rather than a re-fire (which would re-hammer BD).

### BELT (non-blocking, verified on the natural daily)
Confirm tomorrow's 00:00Z scheduled run lands all-4-fresh via the skip path (zero extra BD load). The runner's all-4 pull is pre-existing-proven + unchanged by Lever A; the fail-safe + keepalive bound the risk. If it fails, it's a fast-follow, NOT a Lever A rollback.

### SEPARATE FINDING (for the record; AE-owned, non-blocking)
force=true / any >60s runner invoke MUST use InvocationType=Event (async). RequestResponse + botocore default-retry = a concurrent-invoke storm. AE owned it in-session; banking as an operational lesson.

## Compiler Tools
| tool | invocation | result | note |
|---|---|---|---|
| aws logs/s3/lambda (PowerShell) | session-trigger + runner CloudWatch, S3 head-object, get-function-configuration | PASS | grounded all 5 conditions + the storm forensics live; MSYS leading-`/` false-green on the Bash path caught+corrected |
| Read (lambda_function.py) | _session_is_positive_live + _handle_session_refresh + _fire_runner | PASS | fail-safe-absolute + single-fire + parity all code-grounded |

## Disposition
PASS -> RAVC COO to close the bd-v2.48.0 deploy-ledger. Belt (tomorrow daily all-4) + the async-invoke finding -> AE. cot mirror = separate build/gate later.

-- 3.0.0_SA_CVO
