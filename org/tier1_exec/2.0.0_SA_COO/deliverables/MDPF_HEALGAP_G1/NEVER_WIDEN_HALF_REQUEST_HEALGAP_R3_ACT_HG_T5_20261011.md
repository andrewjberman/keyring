# Never-widen half (DRAFT): MDPF_HEALGAP round 3, drain act HG-t-5 -- the cottonwood runner's daily fire moves 06:00Z -> 12:45Z

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-11 ~08:5xZ. **For:** `1.0.0_SA_CTO~DELL1`, who owes the CTO half.
**Status:** DRAFT; waits on HG-t-14's apply (the CTO's order of acts, ADDENDUM 3). COO half NOT yet signed. **Precondition (mine, not yet met):** ACT 1 (HG-t-9 v2) is applied (read live 05:2xZ,
ledger `healgap-r3-act1-satellites-stamp-gated-v2-20261011`) AND one 13:15Z fire is read back (L5). Nothing is applied by this
document. One OPEN DECISION below (section 3) is the CTO's before this half is worth signing.

## 1. The act

`terraform` in `infra/aws/terraform/opal-assets`, via `.tools/safe-apply.sh`, `-target aws_cloudwatch_event_rule.cot_rebalancer_runner_daily`
only. The merged change (`98d6e00ba5`, order `MDPF_HEALGAP.TO-HG-t5`, proof VALID): `schedule_expression` `cron(0 6 * * ? *)` ->
`cron(45 12 * * ? *)`, and the PLACEHOLDER comment replaced by the derivation.
- **Condition:** the targeted plan reads exactly ONE resource changed in place, that attribute, and nothing else.
- The retry settings (`maximum_event_age_in_seconds` 900) were applied under R2 act 1; they are not in this act.

## 2. What it changes (read live and from the runner's own rule)

- **Live now:** rule `cot-rebalancer-runner-daily` `cron(0 6 * * ? *)` ENABLED (read 2026-10-11 08:3xZ). Today's fire: Lambda REPORT
  06:00:59Z (17.9 s), stamp `meta/2026-10-11-complete.json` LastModified 06:01:00Z, silver `opal-assets-silver-blackdiamond` REPORT
  06:01:07Z (4.3 s). Runner to silver complete: about 70 s (N = 1 day read; 10-10's 06:00:59 / 06:02:19 / 06:04:21 attempts were the
  PARTIAL day, spread about 4 min).
- **After the act:** bronze, the stamp and the event-driven silver run land at about 12:45-12:47Z. The 13:30Z gold floor then has
  about 43 min over the chain (the check `hg_t5_schedule.py` grades the session and floor margins, not the chain length).
- **Writers of the runner's same-day outputs:** N = 1 (the runner role), unchanged. The rule has one target; the `cot-bronze-complete`
  re-attempt rule (HG-t-2) hangs off the sentinel, not the clock.

## 3. EVERY reader of the runner's same-day bronze (D1-S7's lesson), and the one that moves served bytes

Census: `comp-find 'cottonwood/bronze/rebalancer_model|rebalancer_model_detail|rebalancer_models'` -- 888 hit(s) across 81150 files
(corpus=all); first-party source readers after removing audit logs and docs: 21 files (below). No pagination: `--all`, three bands.

| reader | clock today | reads | after the move |
|---|---|---|---|
| `cot-rebalancer-runner` (writer) | 06:00Z | -- | 12:45Z |
| silver `opal-assets-silver-blackdiamond` | event, `cot-bronze-complete` | same-day bronze | follows the runner, ~70 s |
| silver-etf `mirror_conversion.py` (census hit) | NOT READ: its trigger was not read here | unread | UNREAD -- named, not graded |
| gold floor / MDPF daily runner | 13:30Z | silver | unchanged clock; margin ~43 min |
| `cot-satellites-registry-producer` | 07:00Z + 13:15Z (HG-t-9, applied) | `rebalancer_model_detail` | 07:00Z reads YESTERDAY's bronze; the 13:15Z stamp-gated fire serves today's |
| **`cot-satellites-characteristics-producer`** | **12:30Z; 13:25Z once HG-t-14 is applied (read before this act)** | `holdings.json` (the registry producer's output) + positioning + BBG T-1 | **reads the 07:00Z holdings, built on yesterday's bronze; `holdings.json` is rewritten at 13:15Z, after it. `characteristics.json` then carries holdings one day behind on every day** |

**The finding, measured from the producer's own text:** `satellites-characteristics-producer.tf:316-353` sets 12:30Z as "AFTER the
Bloomberg pull ... margin over the registry producer's 07:00Z fire", and records `holdings_as_of` in the artifact
(`build_satellites_characteristics.py:688`). Today that is the same day (bronze 06:00Z, holdings 07:00Z, characteristics 12:30Z).
After the move the order inverts: runner 12:45Z, holdings (final) 13:15Z, characteristics 12:30Z. Its input is not wrong or missing,
so it does not raise; it is one calendar day stale by construction. This is a served-output change not named in the HG-t-5 order.

**RULED (B) by the CTO, msg 3655, ADDENDUM 3 @c3cc34f2d0: the characteristics rule is re-timed FIRST, as its own pair (cell `HG-t-14`, order @60ee1f8f3d,
half `NEVER_WIDEN_HALF_REQUEST_HEALGAP_R3_ACT_HG_T14_20261011.md`), to `cron(25 13 * * ? *)`; HG-t-5 is applied only after it.** The options as asked:
- (A) Apply HG-t-5 alone and accept `characteristics.json` one day behind `holdings.json` from the first post-move day.
- (B) **Recommended:** re-time `cot-satellites-characteristics-producer-daily` to after the 13:15Z fire (it must stay after the
  07:00 ET Bloomberg pull, which it does at any time past 12:30Z) FIRST, as its own pair; HG-t-5 second. The re-time is harmless
  while the runner is still at 06:00Z (same inputs), so the order of the two acts removes the stale window instead of creating one.
- Not measured here: the portal readers of `characteristics.json` and whether a one-day-old holdings basis there is acceptable.

## 4. Rollback

`terraform apply -target aws_cloudwatch_event_rule.cot_rebalancer_runner_daily` with the prior `schedule_expression` (`cron(0 6 * * ? *)`,
`98d6e00ba5~1`), then read the rule back. A day's run already made at 12:45Z is inert (same keys, same single writer).

## 5. Acceptance

1. `describe-rule cot-rebalancer-runner-daily` reads `cron(45 12 * * ? *)` ENABLED; the targeted plan before it read 1 change.
2. The first 12:45Z fire: runner REPORT, stamp for the date, silver REPORT within 5 min, `meta/<date>-result.json` COMPLETE.
3. The 13:15Z fire after it serves `registry.json` `as_of` = that date (the stamp-gated path from HG-t-9).
4. If (B) was ruled: `characteristics.json` `holdings_as_of` equals its own `as_of` on that day.
