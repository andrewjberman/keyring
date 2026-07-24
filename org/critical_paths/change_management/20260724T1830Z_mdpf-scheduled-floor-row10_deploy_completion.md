# Deploy Completion Ledger — MDPF SCHEDULED FLOOR (closure row 10)

**Change:** `MDPF_CHANNEL_INDEPENDENCE.CI-R3R10` — scheduled floor + retries-or-records
**Owner:** 0.7.0_AE_CloudOps · **Opened:** 2026-07-24T18:30Z
**Status:** **OPEN — BUILT AND VERIFIED, DELIBERATELY NOT APPLIED**

## Why this is open and NOT a stranded leg

NEVER#6 forbids leaving a *confirmed deploy* half-landed. **No deploy was begun.** This ledger is opened at
build-completion to record a verified-but-ungated change, per CI-R3R10 AC-5 (*"ledger open-at-start,
closed-on-proof **or explicitly left open with the billing block named** — a legitimate close-out state
today"*).

**The apply is gated on COO/CTO, not on me, and not on CI.** Correcting a thing I was initially told and
which COO then corrected: `lambda-deploy.yml` is a **drift check, not a deploy path**, and `safe-apply.sh`
runs **locally** — so the org-wide GitHub Actions billing block does **not** technically prevent this apply.
**What we lost is the drift DETECTOR**, which makes post-apply landed-artifact verification *more*
load-bearing, not less. I am not applying because the change is not mine to take unilaterally under a P0 with
an active push-freeze, not because I am blocked.

## What is built

| Resource | Action | File |
|---|---|---|
| `aws_cloudwatch_event_rule.mdpf_scheduled_floor` | **create** — `cron(0 20 * * ? *)`, ENABLED | `scheduled-floor.tf` |
| `aws_cloudwatch_event_target.mdpf_scheduled_floor` | **create** — static input `source=mdpf.scheduled-floor` | `scheduled-floor.tf` |
| `aws_lambda_permission.eventbridge_mdpf_scheduled_floor` | **create** | `scheduled-floor.tf` |
| `aws_sqs_queue_policy.mdpf_trigger_dlq` | **update in-place** — widen ArnEquals to BOTH rules | `eventbridge.tf` |
| `mdpf-daily-trigger/lambda_function.py` | floor branch + `_record_deferral` | lambda |

## Verification performed (build-and-verify, pre-apply)

- `python3 -m py_compile` — **OK**
- `.tools/commit-gate.sh` — **All checks passed**
- `terraform validate` — **Success**
- `terraform plan` — **`Plan: 3 to add, 1 to change, 0 to destroy`**
- **Accelerator untouched, confirmed at plan level:** `aws_cloudwatch_event_rule.mdpf_daily_refresh` appears
  ONLY as `Refreshing state...` — no modify, no destroy. *PRD §2.3: "NEVER REMOVE THE GUARD THAT WORKED."*

## NOT YET TRUE — the acceptance that has not been run

**Row 10's own verification is "disable the event → the floor still publishes." THAT HAS NOT BEEN RUN.**
Nothing here may be read as row 10 passing. Verdict is **`not-yet-true`** pending apply + that exercise.
A schedule that exists is not a floor that works; adding the rule and declaring the row true is the exact
shortcut the TO names.

**AND A BLOCKING FINDING ABOVE MY LANE (see the deliverable):** the driver is **two-layer**. Removing the
Lambda's spine-halt is necessary and NOT sufficient — `mdpf-daily-dispatch.sh` hard-requires WS-C
(Inflection) and `exit 1`s the chain if it fails, with no `is_stale_partner inflection` branch anywhere.
**So a floor firing while INF is genuinely down would dispatch and then hard-fail at Stage 1.** That is
dispatch-layer work, it is adjacent to row 4 (CVO's), and it goes to CTO's gate rather than being absorbed.

## Close-out condition

Closes when: apply lands 0-diff → the deployed rule is confirmed by **invoking it and reading `is_floor` in
the decision** (never by comparing the TF and Python strings by eye — that contract has no compiler) → the
disable-the-event exercise runs → a deferral is CONSTRUCTED and shown to record.

**Unclosed at session end is expected here and is not a COO alarm condition** — it is a build awaiting a gate,
recorded so it cannot become invisible.
