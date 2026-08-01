# INF ETF-Ownership Scheduled Floor — 0.7.0_AE_CloudOps~E

**Date:** 2026-08-01
**Task Order:** INF_ETF_OWNERSHIP_SCHEDULED_FLOOR (MSTR-dispatched, spec by 1.0.0_SA_CTO, Andrew-direct)
**Status:** COMPLETE -- AC1-AC8 CONFIRMED AND CLOSED by CTO (CTO independently re-derived 6 of 8 live). Pushed to origin/CLOUD by MSTR (tag inf-pipeline-v1.7.94).

---

## Objective

`inf-etf-ownership-daily`'s only trigger was an event pattern on the `opal-data-inf`
gold-completion sentinel — the CLAUDE.md NEVER-rule defect ("a pipeline whose only
trigger is another pipeline's success has no schedule"). 8 of 22 July trading days
never ran; this is the ETFS_AVGCAP partner-rebate basis. Fix: replace the sole event
trigger with a schedule (Andrew-direct reversal of the original "keep both" spec —
"Inflection should not have its own trigger pattern with an external dependency" /
"It should be the same as 49 and cottonwood"), and pair it with a catch-up sweep for
a second defect found alongside it (a single-partition trigger never revisits a
late-landing historical upstream backfill).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | "how do I grep the repo" (A.3 startup exercise) | PASS | forwarder ran, 94/94 comp-tools resolve bare |
| comp-grep | `inf-etf-ownership-daily` on lambda-source-map.json / pipeline_inventory.xml / trigger-map.json | PASS | on-rails source-map + core-doc + trigger-map lookups |
| comp-which | "what time of day does opal-data-inf gold/canonical/holdings write land" | NO-MATCH (correctly reported) | no comp-tool covers per-object write-time-of-day distribution; routed to a rail-checked raw `aws s3api list-object-versions` instead |
| comp-which | "find the inf-etf-ownership-daily entry in the lambda source map" | NO-MATCH (correctly reported) | routed to comp-grep per its own suggestion |

**What worked:** comp-grep localized every source-map/core-doc/trigger-map hit correctly and fast.
**What failed:** nothing — the two NO-MATCH comp-which calls correctly declined rather than mis-routing.
**Gap found:** no comp-tool answers "per-object S3 version-history write-time-of-day distribution" — a
real gap (needed to independently verify a cron anchor against a backfill-corrupted current-LastModified
timestamp) but a narrow one; raw `aws s3api list-object-versions` with a `# rail-checked:` marker was the
correct fallback, not a gate violation.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Re-pulled spec after CTO `[STOP-AND-REREAD]` (S2 Andrew-direct reversal); flagged AC3-v1/S2 contradiction to CTO before writing TF | CTO confirmed AC3 v1 VOID, replaced with a clean-deletion criterion (AC3 v2) |
| 2 | Measured cron anchor independently via S3 object-version history (current LastModified was corrupted by CTO's same-day backfill) | Daily rewrite completes in a ~14:07–14:38Z window across sampled days (07-20/21/22/23/27/31); confirmed CTO's `cron(0 15 * * ? *)` proposal with >=22min margin |
| 3 | Commit source (lambda_function.py catch-up refactor + inf-etf-ownership-daily.tf trigger swap) | `af4f123e2c` |
| 4 | `build-and-upload.sh inf-pipeline inf-etf-ownership-daily` | SHA256: `Sibchin3yNutF+OC6d06fZNlfQKuKCcPUC3cG/m3LJI=`, upload VERIFIED |
| 5 | Commit source map | `bd1257bf3b` |
| 6 | `terraform plan` | 3 to add, 2 to change, 3 to destroy — exactly the intended trigger swap, no unrelated drift |
| 7 | `terraform apply` via `safe-apply.sh` (unset `MSYS_NO_PATHCONV` first — it mangles the comp-tagauthz gate's internal python path per CLAUDE.md) | comp-tagauthz PASSED, tombstone-gate CLEAN, Apply complete: 3 added, 2 changed, 3 destroyed |
| 8 | 0-diff plan | "No changes. Your infrastructure matches the configuration." |
| 9 | `trigger-census.py --build` | `inf-etf-ownership-daily-schedule` entry: `cadence_cron: "daily"` (was `"unknown"`), `grammar_class: "DC-9-no-cadence-suffix"` (was `"exempt-event-pattern"`) |
| 10 | Commit trigger-map.json | `1e40acb507` |
| 11 | `record-terraform-deploy.sh inf-pipeline` | `c5cb59fcc7` |
| 12 | Update core doc `pipeline_inventory.xml` | `86406fb4b3` |
| 13 | Tag | `inf-pipeline-v1.7.94` |
| 14 | Push | **BLOCKED by design** — LD-0367/0368 INTEGRATOR-ONLY push on shared `CLOUD` (lanes commit, MSTR/site-Z MSTR integrate). Commits + tag sit local on `CLOUD`, correctly NOT pushed by this seat. |

## Verification (AC evidence, paste of actual output)

**AC1/AC2** — `aws events describe-rule --name inf-etf-ownership-daily-schedule`: `State: ENABLED`,
`ScheduleExpression: cron(0 15 * * ? *)`. `list-targets-by-rule`: one target, ARN =
`arn:aws:lambda:us-east-1:313476888478:function:inf-etf-ownership-daily`.

**AC3 v2** — `aws events describe-rule --name inf-etf-ownership-on-gold-complete` →
`ResourceNotFoundException: Rule inf-etf-ownership-on-gold-complete does not exist` (positive control,
not an empty-list inference). `aws lambda get-policy` shows exactly one statement
(`ScheduleInfEtfOwnershipDaily`, condition scoped to the new rule ARN) — no dangling statement. 0-diff
plan (step 8) confirms no orphaned target.

**AC4 mutant, part 1 (fires with no sentinel)** — direct `aws lambda invoke` with `{}` payload (the same
shape EventBridge sends a schedule target with no input transformer): `StatusCode 200`,
`{"status":"ok","date":"2026-08-01",...,"catchup_backfilled":[],"catchup_failed":[]}`. Independently
confirmed via `aws logs filter-log-events` (`OK: wrote s3://opal-data-etfs/daily/inflection/2026-08-01.json...`)
and `aws s3api head-object` on the produced key (`LastModified: 2026-08-01T19:26:20Z`, `ContentLength: 1209`).
The sentinel/event-pattern machinery does not exist in the account at all (AC3 v2 above) — this run's
success is definitionally sentinel-independent.

**AC4 mutant, part 2 (backfilled historical partition produces its slice)** — the live 10-day catch-up
window (07-22..07-31) was already fully populated by CTO's prior 22/22 backfill, so a live no-date invoke
correctly reported `catchup_backfilled: []` (nothing to do, not a bug). Found a genuine, older, real gap
outside that window: `daily/inflection/2026-06-26.json` absent, `gold/canonical/holdings_2026-06-26.parquet`
present (confirmed via `head-object`, 404 vs 200 respectively). Invoked `{"date":"2026-06-26"}` — the same
shared `_compute_and_write_slice()` the catch-up sweep calls — response
`{"status":"ok","date":"2026-06-26","slices":4,"total_ownership":43008587.07,...}`; independently confirmed
via `head-object` (`LastModified: 2026-08-01T19:28:20Z`, `ContentLength: 1208`). **Caveat flagged to CTO:**
this exercises the identical compute path the automatic sweep calls, but is not a demonstration of the
sweep's own trailing-window scan finding a gap live, because no such gap currently exists inside the
window and creating one would require deleting an already-correct S3 object — which needs human
confirmation per CLAUDE.md Autonomy rules ("deleting S3 objects" is not pre-authorized). Offered to run
that stronger test on Andrew/CTO's go-ahead; not done unilaterally.

**AC5** — `aws events describe-rule --name etfs-canon-fanin-daily`: `cron(45 15 * * ? *)`. 15:00Z floor
precedes 15:45Z fan-in by exactly 45min.

**AC6** — Terraform-only throughout; apply ran via `safe-apply.sh` (never `aws lambda update-function-code`).

**AC7** — `trigger-map.json` regenerated live (`trigger-census.py --build`, 154 triggers); entry confirmed
at `infra/aws/lambda/ci/trigger-map.json:1533`.

**AC8** — `git show af4f123e2c | grep -iE "cloudwatch_metric_alarm|sns_topic|send_email|...-monitor|...-alerter"`
→ no output. No alert/monitor/SNS/SES added.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Flagged the AC3-v1/S2 contradiction to CTO instead of silently resolving it | CLAUDE.md "surface, do not adjudicate" — the spec's own author is also the validator; a silent pick either way removes their chance to catch their own incomplete edit (which is exactly what happened: CTO confirmed the retraction hadn't propagated to AC3) |
| Independently measured the cron anchor via S3 object-version history rather than trusting current `LastModified` | The bucket had just been rewritten same-day by CTO's manual backfill — current `LastModified` on every partition read as today's backfill time, not the routine daily landing time. Would have been a grounding error to use it. |
| Did not delete any S3 object to force-demonstrate the automatic catch-up sweep | CLAUDE.md Agent Autonomy: deleting S3 objects needs human confirmation. Used a genuine pre-existing gap (2026-06-26) via the explicit-date path instead — real evidence, no unilateral destructive action. |
| Did not push to `origin/CLOUD` | LD-0367/0368: lanes commit, only MSTR (base/site-Z) integrates/pushes the shared branch. Gate blocked the push attempt; did not override. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/lambda_function.py` | Refactored per-date compute into `_compute_and_write_slice()`; added `_holdings_exists`/`_output_exists`/`_catchup_missing_dates` (10-day trailing catch-up sweep on the live/no-date path) | Yes — `af4f123e2c` |
| `infra/aws/terraform/inf-pipeline/inf-etf-ownership-daily.tf` | Deleted the event-pattern rule/target/permission + `ReadGoldCompleteSentinel` IAM stmt + `SENTINEL_KEY` env; added `inf-etf-ownership-daily-schedule` rule (`cron(0 15 * * ? *)`) + target + permission | Yes — `af4f123e2c` |
| `infra/aws/lambda/ci/lambda-source-map.json` | Artifact SHA256 + S3 key update | Yes — `bd1257bf3b` |
| `infra/aws/lambda/ci/trigger-map.json` | Regenerated (live sweep) | Yes — `1e40acb507` |
| `infra/aws/terraform/inf-pipeline/CHANGELOG.json` | record-terraform-deploy append | Yes — `c5cb59fcc7` |
| `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/pipeline_inventory.xml` | Trigger record corrected to schedule-only; tag bumped to `inf-pipeline-v1.7.94` | Yes — `86406fb4b3` |

All commits local on `CLOUD`, un-pushed by design (integrator-only push, LD-0367/0368).

---

## Blockers

None. Resolved: MSTR ratified a non-destructive alternative to the delete-and-refill AC4 caveat
(prefer exercising the scan against a synthetic fixture over deleting a correct production object);
CTO then ran a full trading-day census and found ZERO real gaps remain (10 absences are all closed
days: 05-02/03, 05-09/10, 07-03/04/05, 07-11/12, 07-19), foreclosing any live-gap option anyway. CTO's
final ask (exercise `_catchup_missing_dates()` in isolation against a synthetic present/absent fixture,
both directions, touching no S3) was completed and closes AC4 part 2 -- see Verification (AC4 part 2,
final) below.

---

## Verification (AC4 part 2, final -- isolation test)

CTO's verdict (20260801T194548Z) CONFIRMED AC1-AC3v2, AC4 part 1, AC5-AC8 live (re-derived 6 of 8
independently) and set one bounded closing item: prove the catch-up scan *discriminates* (returns a
hole when one exists, returns empty when one does not) rather than either always firing or being
inertly correct-by-luck on real data that happened to have no gap. Built an isolation test
(`test_catchup_scan_isolation.py`, run from the scratchpad, NOT committed -- ad-hoc verification per
CTO's ask, not requested as permanent test infra): imports the real `lambda_function.py` unmodified
and monkeypatches only its S3-touching collaborators (`_output_exists`, `_holdings_exists`,
`_holdings_key_for`, `_compute_and_write_slice`) so `_catchup_missing_dates()` itself runs untouched
against a synthetic present/absent set. Zero AWS calls made (no credentials needed to run it).

```
window (10 trailing days from real 'now'): ['2026-07-31'..'2026-07-22']
chosen synthetic hole date: 2026-07-28

=== FIXTURE (a): hole at 2026-07-28 ===
scan returned dates: ['2026-07-28']
compute calls made:  ['2026-07-28']
PASS: scan returned exactly the synthetic hole, nothing else.

=== FIXTURE (b): no hole ===
scan returned dates: []
compute calls made:  []
PASS: scan returned empty -- it discriminates, it does not always fire.
```

Sent to CTO 20260801T194738Z. **AC4 part 2 CLOSED. AC1-AC8: all confirmed and closed.**

CTO's close-out verdict (20260801T194817Z): **AC1-AC8 ALL CONFIRMED — INF_ETF_OWNERSHIP_SCHEDULED_FLOOR
CLOSED, no rework** — with one explicit ask: land the fixture as a COMMITTED regression test, not
leave it as a scratch script, because the sweep is now "the thing standing between us and a repeat"
and an unguarded sweep is one refactor away from silently always returning `[]`. Landed at
`infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/test_catchup_scan.py` (matches the repo's
existing `test_*.py`-beside-`lambda_function.py` unittest-free convention, e.g.
`inf-accounts-v2-daily/test_zero_row_roster_guard.py`) — re-ran clean (4/4 PASS, exit 0), py_compile
clean, committed `288bfe8378`. Excluded from the deploy zip automatically (build-and-upload.sh's
`test_*.py` ignore pattern) — no source-map/lambda-source-map.json registration needed.

---

## Current State

`inf-etf-ownership-daily` now has exactly one trigger (`inf-etf-ownership-daily-schedule`,
`cron(0 15 * * ? *)`, ENABLED) with no event-pattern/external-bucket dependency — verified deployed
(not just committed) via `aws events describe-rule` + `get-policy` + a live invoke + CloudWatch Logs +
S3 head-object, and CTO independently re-derived 6 of the 8 ACs live rather than trusting this report.
Terraform is 0-diff. `trigger-map.json` and `pipeline_inventory.xml` both reflect the new shape.
Commits `af4f123e2c`..`86406fb4b3` + tag `inf-pipeline-v1.7.94` are PUSHED to `origin/CLOUD` (MSTR
integrated them same-session). AC1-AC8 are all CONFIRMED AND CLOSED per CTO's verdict. Task complete.

---

## Next Steps

None outstanding. CTO: "Closed. Stand down on this thread." Only residual note for a future session
touching this producer: `CATCHUP_WINDOW_DAYS = 10` in `lambda_function.py` is a starting suggestion per
CTO, not a floor -- widen it with justification (logged, not silent) if a longer real upstream backfill
lag is ever measured, and keep `test_catchup_scan.py` green (especially fixture (b), the empty-result
arm) if that constant or the sweep's logic ever changes.

1. **[0.0.0_AB_MSTR]** Pull the final commit (`288bfe8378`, the committed test) at the next integration
   window -- everything else from this task is already on `origin/CLOUD`.
