# CVO Cert — 49F Lever A Belt CLOSE (both limbs independently grounded)

**Date:** 2026-07-07T00:24Z
**Agent:** 3.0.0_SA_CVO
**Subject:** 49 Financial (bd) Lever A — cookie-first daily-OTP skip — belt landed on the NATURAL 00:00Z daily
**Verdict:** PASS — belt CLOSED (closes the earlier PASS-with-belt verdict 4b4e802d3)
**Grounding standard:** exercise + live-primitive (Rule 22a: BEHAVIOR -> exercise the path; STATE -> live head-object UTC). NOT a producer self-report — I pulled the log + head-object'd myself.

## Andrew's thesis (BD-auth investigation)
"Assess if there are long-lived cookies and employ those to just call the REST API. Only if those are stale do we need the full sign-in with OTP." Lever A = cookie-first skip on the daily; OTP only on cookie-stale. This belt proves it in production.

## LIMB 1 — SKIP-NOT-MINT (zero OTP on the natural daily)
Source: bd-49f-session-trigger CloudWatch, 2026-07-07 00:00-00:15Z window (pulled via PowerShell to avoid MSYS leading-`/` path-mangling on the log-group name).
```
bd-49f-session-trigger invoked 2026-07-07T00:00:18Z mode=session-refresh
Mode marker written: s3://opal-data-bd/blackdiamond/49f/session-trigger-mode.json  mode=skip-live-direct-invoke runner=main
Lever A: cookie POSITIVE-live (captured_at=2026-07-06T00:02:36.184Z) -> SKIP mint, direct-invoke bd-49f-runner (target=main)
Invoked bd-49f-runner (async, target=main) status=202
```
- The `cron(0 0)` fired -> mode=session-refresh.
- Cookie captured_at 2026-07-06T00:02:36Z, used 2026-07-07T00:00:18Z = **~24h-old cookie still POSITIVE-live** (keepalive working).
- ZERO OTP-mint / box-start / session-fetch in the window (the only 'mint' token is inside "SKIP mint"). => the daily-OTP breakage surface is DEAD on the scheduled run.

## LIMB 2 — ALL-4-FRESH via the SKIP path (not an idempotent no-op)
Source: independent `head-object` LastModified (UTC, not `s3 ls` local).
| table | forwardfill_v2 07-07 LastModified (UTC) |
|---|---|
| transactions | Tue, 07 Jul 2026 00:01:13 GMT |
| allocations | Tue, 07 Jul 2026 00:09:37 GMT |
| realized | Tue, 07 Jul 2026 00:09:44 GMT |
| unrealized | Tue, 07 Jul 2026 00:09:55 GMT |

Sentinel `s3://opal-data-bd/bronze/2026-07-07/_BRONZE_COMPLETE.json` @00:09:55Z:
```json
{"stage":"bronze","run_date":"2026-07-07","completed_at":"2026-07-07T00:09:54Z","overall":"success","artifacts":{"tables":["transactions","allocations","realized","unrealized"],"count":4},"producer":"cot_bronze_ingest.py"}
```
All 4 in the 00:00Z window (00:01-00:09Z); sentinel overall=success, tables=4. The SKIP-path runner did a REAL fresh all-4 pull — the load-bearing proof the earlier storm-confounded force-pull couldn't give.

## VERDICT
49F Lever A is PROVEN in production on the natural daily: cookie-first SKIP (zero OTP) + the skip path yields a COMPLETE fresh bronze. Belt CLOSED.

## P2 naming-hygiene finding (non-blocking, routed to COO/AE)
The 49F bronze sentinel stamps `producer="cot_bronze_ingest.py"` — a cot-prefixed name in a bd-firm artifact. **GROUNDED benign, no firm-separation issue:** it is a SHARED ingest module firm-bound to bd via env, pulled from opal-data-bd's OWN `code/bronze/` prefix (bd-49f-runner l.6-20,59), `BD_S3_BUCKET=opal-data-bd` only, a bucket-unset/==opal-data-cot run ABORTS (l.15), explicit IAM Deny on opal-data-cot (l.16). Data lands only in opal-data-bd. **But** the cot-prefixed name stamped in a bd sentinel is an audit-readability trap (any auditor must re-derive it's not a cross-firm leak). Rec: firm-neutral rename (e.g. `blackdiamond_bronze_ingest.py`) on next touch. P2, follow-on, owner's call.

## Open (my last Lever A item)
cot 02:00Z 07-07 belt — AE~A certs; I hold for the same independent both-limbs grounding, then CLOSE.
