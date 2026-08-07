# V-1 — Route & event-architecture validation (rows V1–V5), read-only

**Run:** 2026-08-07 01:21–01:25Z by `3.0.0_SA_CVO~Z` · TO `MDPF_CANPLAT.V1` · V-PRD @2dedd8f6a §2 V-1
**Instruments:** `comp-trigger mdpf` (denominator: 139 events-rules + 16 schedules, us-east-1) + live
primitives (`scheduler get-schedule`, `events describe-rule`/`list-targets-by-rule`,
`lambda get-policy` [rail-checked: TO-legalized, live=APPLIED layer per Rule 22a], `sqs
get-queue-attributes`, `lambda list-functions`/`list-function-event-invoke-configs`,
`s3api get-bucket-notification-configuration`). MEASURE ONLY — nothing changed.

## V1 — the four entries, targets RESOLVED

| entry | type | state | expression | tz | target | target resolves |
|---|---|---|---|---|---|---|
| `mdpf-scheduled-floor` | Scheduler | ENABLED | `cron(0 9 * * ? *)` | America/New_York | `mdpf-daily-trigger` | **EXISTS, Active** (get-function-configuration 01:01Z) |
| `mdpf-accrual-bridge-daily` | Scheduler | ENABLED | `cron(40 9 * * ? *)` | America/New_York | `mdpf-accrual-trigger` | **EXISTS, Active** |
| `opal-assets-mdpf-portal-publisher-daily` | Scheduler | ENABLED | `cron(50 9 * * ? *)` | America/New_York | `opal-assets-mdpf-portal-publisher` | **EXISTS, Active** |
| `mdpf-daily-refresh-trigger` | classic rule | ENABLED | event-pattern: `opal-data-inf` / `gold/meta/pipeline-complete.json` ObjectCreated | — | `mdpf-daily-trigger` (sole target) | **EXISTS, Active** |

Floor carries DLQ `mdpf-daily-trigger-dlq`; **accrual + publisher schedules have NO DLQ configured
(measured `DeadLetterConfig: null`)** — recorded as a datum, not chased.

## V2 — live resource policies (APPLIED layer)

| function | grants |
|---|---|
| `mdpf-daily-trigger` | `scheduler.amazonaws.com` ← `schedule/default/mdpf-scheduled-floor` **AND** `events.amazonaws.com` ← `rule/mdpf-daily-refresh-trigger` — both live paths correctly authorized |
| `mdpf-accrual-trigger` | `scheduler.amazonaws.com` ← `schedule/default/mdpf-accrual-bridge-daily` |
| `opal-assets-mdpf-portal-publisher` | `scheduler.amazonaws.com` ← `schedule/default/opal-assets-mdpf-portal-publisher-daily` |

**Every target permits exactly its own schedule's principal + source ARN. PASS.**

## V3 — floor DLQ

Depth: **0** (`ApproximateNumberOfMessages`, 01:23Z). Policy: **the KNOWN MIS-SCOPE, confirmed as
recorded** — sole statement `AllowEventBridgeSend`, principal `events.amazonaws.com`, source
`rule/mdpf-daily-refresh-trigger`. It does NOT name `scheduler.amazonaws.com` or the current
`mdpf-scheduled-floor` ARN, so a floor-delivery failure today would be refused by its own DLQ.
**Per the TO: recorded, corrected at cutover, NOT chased.**

## V4 — the dead event edge

`mdpf-daily-refresh-trigger` is **accelerator-only**: sole target `mdpf-daily-trigger`, which the
ENABLED 09:00 floor schedule independently covers (A2 — the rule is never the only trigger). Live
fired-evidence (comp-trigger): **last fired 2026-07-30** — a dead event edge is not a defect under
schedule-first; its re-point rides the cutover.

## V5 — the negatives, WITH DENOMINATORS

1. **Event-invoke destinations: 0, on every mdpf function.** Denominator: **3 mdpf-named functions of
   196 total** (full list materialized, auto-paginated): `mdpf-daily-trigger`,
   `mdpf-accrual-trigger`, `opal-assets-mdpf-portal-publisher` — `list-function-event-invoke-configs
   = []` for all 3. ⚠ Frame delta, recorded not chased: the V-PRD says "all four MDPF functions";
   exactly THREE mdpf-named functions exist at 01:24Z (`mdpf-gold-lambda` not yet deployed, V-PRD
   §1b's own measurement).
2. **S3 notifications on gold/portal-gold/platinum: 0, of 10 total configs** on the two chain
   buckets: `opal-data-assets` 8 (all `{vendor}/{firm}/bronze/` → silver converters) +
   `opal-data-portal-v2` 2 (`uploads/` → yang, `security_scanner/uploads/` → scanner). **Not one
   names `gold/`, `portal/gold`, or `platinum/`** — matches the V-PRD's measured 10/10 bronze-ingest
   census exactly.

**⇒ There is no event-driven architecture between gold and the publisher; the hop is purely
scheduled — confirmed live, with denominators, matching V-PRD §1a.**

— 3.0.0_SA_CVO
