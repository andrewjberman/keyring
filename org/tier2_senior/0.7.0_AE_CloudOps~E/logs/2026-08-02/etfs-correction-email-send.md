# ETFS_ORION_LABEL_CORRECTION email send -- 0.7.0_AE_CloudOps~E

**Date:** 2026-08-02
**Task Order:** Andrew-direct via CTO GO (moratorium-exempt), verbatim: "Ok let's makes sure that we
have these final numbers memorialized somewhere. Have the lambda send me an email with the updated
figures including CSVs to andrew@opalinvest.com"
**Status:** COMPLETE -- email sent, delivered, verified via CloudWatch.

---

## Objective

One-time SES send from `etfs-reports-orchestrator` to Andrew, attaching the already-committed
ETFS_ORION_LABEL_CORRECTION figures (inflection July 2026, Orion date-label defect). Explicitly
moratorium-exempt (Andrew asked directly); no alarm/monitor/schedule/SNS topic added.

---

## Compiler Tools

Not applicable -- this task is a single Lambda code addition + one manual invoke, no gold/silver/bronze
script touched, no IAM change (reused an existing grant). `# rail-checked:` markers used for the small
number of raw `aws` calls needed for send-verification evidence (CloudTrail lookup, SES statistics,
CloudWatch metrics/logs) -- no comp-tool covers post-send SES delivery verification.

---

## Work Completed

### 1. Uploaded the committed correction artifacts to S3

Mirrored `org/tier1_exec/1.0.0_SA_CTO/deliverables/ETFS_ORION_LABEL_CORRECTION/*` to
`s3://opal-data-etfs/platinum/reports/corrections/ETFS_ORION_LABEL_CORRECTION/` -- deliberately under
the orchestrator's EXISTING `platinum/reports/*` IAM read grant, so no new IAM statement was needed.
Verified all 3 uploads by size match (287B / 1895B / 4113B).

### 2. Added two new manual-invoke-only modes to `etfs-reports-orchestrator`

`send_correction_qa` (send-free rehearsal, mirrors the existing `email_qa` pattern -- no `ses` call is
reachable on this path) and `send_correction` (the one real send). Neither touches EC2/SSM/the normal
month-end render path -- re-firing that would have recomputed and re-sent the UNCORRECTED July numbers.

Body carries the three things CTO required, not just the number: "measurement, not a restatement"
(nothing restated, no partner notified), "basis, not payment" (simple mean, ETFS_AVGCAP aggregation
unconfirmed), and the cross-partner T-1-vs-T date-basis defect stated as the bigger finding before the
dollar delta.

Commit carries the required `andrew-asked:` marker (moratorium-exemption gate form).

### 3. Verified locally, then on the deployed function, before sending

Ran `send_correction_qa` against a local import of the lambda module reading the real S3 attachments --
subject, all 3 attachment filenames, and the full body rendered exactly as intended. Re-ran the same
mode against the DEPLOYED function post-apply -- identical output, confirming the deploy carried the
same code.

### 4. Sent

Invoked `{"mode": "send_correction"}` against the deployed function. Response: `{"ok": true,
"recipient": "andrew@opalinvest.com"}`.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Upload 3 correction artifacts to S3 (new prefix under existing IAM grant) | 3/3 verified by size |
| 2 | Commit source (`lambda_function.py`, andrew-asked marker) | `dfb30cba79` |
| 3 | `terraform plan` (etfs-reports; this lambda zips directly via `archive_file`, no build-and-upload step) | 0 add / 1 change / 0 destroy -- only the code hash, no IAM/env drift |
| 4 | `terraform apply` via `safe-apply.sh` | comp-tagauthz PASSED, tombstone-gate CLEAN, Apply complete: 0 added, 1 changed |
| 5 | 0-diff plan | "No changes. Your infrastructure matches the configuration." |
| 6 | Invoke `send_correction_qa` on the deployed function (send-free pre-flight) | Subject/attachments/body all correct |
| 7 | Invoke `send_correction` (the real send) | `{"ok": true, "recipient": "andrew@opalinvest.com"}` |

## Verification (evidence, paste of actual output)

**Lambda execution** -- CloudWatch Logs, log stream `2026/08/02/[$LATEST]3d61b298c9f04a62b4cd88a8f0f91b93`:
both invocations recorded cleanly, no errors. QA rehearsal RequestId `02f769dd-...` (233.48ms, no SES
call). Real send RequestId `60b5840c-...` (427.93ms -- the ~200ms delta over the QA rehearsal is
consistent with the added outbound SES API round-trip that only this path makes).

**SES delivery** -- `aws cloudwatch get-metric-statistics` (namespace `AWS/SES`, the authoritative
record, not `SendQuota` which CTO flagged as eventually-consistent and misleading): in the 5-minute
window containing the send (`2026-08-02T03:17:00Z`-`03:22:00Z`):
```
Send:      Sum=1.0
Delivery:  Sum=1.0
Bounce:    (no datapoints -- zero)
Complaint: (no datapoints -- zero)
Reject:    (no datapoints -- zero)
```
Cross-checked against `aws ses get-send-statistics`: most recent 15-min bucket
(`2026-08-02T03:06:00Z`) shows `DeliveryAttempts=1, Bounces=0, Complaints=0, Rejects=0` -- consistent.

**MessageId** -- NOT captured. The `_send_correction_email()` call does not log the `send_raw_email`
response object (matching the pre-existing `_email_report`'s style, which also doesn't). `aws
cloudtrail lookup-events` for `SendRawEmail` in the relevant window returned zero events (SES send
calls are not captured as CloudTrail management events by default in this account). Using the
CloudWatch Send/Delivery metrics as the authoritative cross-check instead -- same class of evidence
accepted for the prior ETFS month-end send verification. Flagging the gap rather than implying I have
a MessageId I don't.

**Attachments** -- confirmed via both the local test and the deployed `send_correction_qa` rehearsal:
`opaletfs_inflection_202607_published_vs_corrected.csv`, `opaletfs_inflection_202607_CORRECTED_true_settled.csv`,
`FINDINGS.md` -- 3 attachments, matching the 3 uploaded S3 objects exactly.

**Rendered body** -- confirmed identical between the local test, the deployed pre-send rehearsal, and
the committed source: all three required statements present (measurement-not-restatement, basis-not-
payment, cross-partner T-1-vs-T finding), headline figure exact ($424,062.91 / 0.891% total, per-ticker
breakdown matching `FINDINGS.md` §3 to the cent).

**IAM** -- no new grant. Correction artifacts placed under the orchestrator's pre-existing
`platinum/reports/*` read scope; `terraform plan` confirmed zero IAM diff.

**Moratorium compliance** -- `andrew-asked:` marker present on the commit; no
`aws_cloudwatch_metric_alarm` / `aws_sns_topic` / new `ses.send_email` identity / `-monitor`/`-alerter`
naming added (grepped the commit diff, zero hits beyond the pre-existing `_alert`/SNS calls this file
already had before tonight, untouched).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Mirrored the committed CSVs/FINDINGS.md to S3 under the existing `platinum/reports/*` prefix, rather than requesting new IAM | The orchestrator already has read access there; placing the new content inside an already-permitted prefix avoids a Terraform IAM change entirely for a one-time send. |
| Added a send-free `send_correction_qa` rehearsal mode before the real send | Mirrors the codebase's own established pattern (`email_qa`) for anything email-shaped; given this send carries real financial figures to Andrew, verifying the exact rendered body and attachment set on the DEPLOYED function before firing felt like the appropriate bar, not optional polish. |
| Included `FINDINGS.md` as a third attachment alongside the two CSVs Andrew explicitly named | Andrew asked to "memorialize" the final numbers; the full written record (defect mechanism, oracle test, one still-open item) seemed like the more complete answer to "memorialized somewhere" than the bare CSVs alone. Disclosing this as an addition, not silently expanding scope. |
| Used CloudWatch Send/Delivery metrics as the delivery-evidence anchor instead of a captured MessageId | The existing code path never logged the SES response object and CloudTrail did not capture the API call; rather than fabricate or omit evidence, used the same authoritative CloudWatch-metrics method already validated for the prior ETFS month-end send, and disclosed the MessageId gap explicitly. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py` | Added `send_correction_qa` + `send_correction` modes, `_build_correction_email`/`_send_correction_email` | Yes -- `dfb30cba79` |
| `s3://opal-data-etfs/platinum/reports/corrections/ETFS_ORION_LABEL_CORRECTION/*` | New artifacts (data, not code) -- 3 files mirrored from the committed org/ deliverable | N/A (S3, not git) |

All commits local on `CLOUD`, un-pushed by design (integrator-only push, LD-0367/0368).

---

## Current State

Email sent and delivered (CloudWatch-confirmed) to andrew@opalinvest.com from noreply@opalinvest.dev,
carrying the corrected inflection July 2026 figures, both CSVs, and the full FINDINGS.md record. No
alarm/monitor/schedule/SNS topic added -- moratorium-compliant, marker present. Terraform 0-diff.
Nothing further owed on this task unless CTO or Andrew has follow-up.

---

## Next Steps

None outstanding on this task. Evidence report going to CTO for validation.
