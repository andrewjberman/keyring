# NEVER-WIDEN -- CTO HALF -- ETFS_RIVALS round 1, `RIV-d-2` (apply, gateway deploy, BASG backfill, fire) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~10:0xZ

**Against:** `deliverables/2.0.0_SA_COO~RV/round1/NEVER_WIDEN_HALF_COO_D2.md` @`462db51701` (msg 27063, READ-acked; read to EOF,
6,297 B).
**Vendor authority:** R-21 @`b390c36444`, Andrew's word *"you have all the egress you want for vendors"*, on its mechanism: a
scheduled, scripted fetch Lambda, never an agent turn. The issuer site is fetched by `etfs-rivalfunds-fetch-holdings-lambda` only.

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT (client-side counts; the paginated `--query length()` trap caught and discarded)

- **Keys 1-10:** the bucket `opal-data-etfs` top-level prefixes read `bbg-testpull/ bbg/ config/ daily/ gold/ platinum/ silver/
  snapshots/`. That listing is the positive control: the bucket is visible. `issuer-site/` and `rivalfunds/` are absent, so there
  are 0 objects.
- **Key 11:** `get-bucket-notification-configuration` returns 0 bytes, which is empty and equals the half.
  - **Enabling EventBridge on the bucket was checked against every rule:** 144 rules, 18 with an EventPattern, **1 read error**.
  - 12 are `aws.s3`-sourced. Every `Object Created` rule filters on `opal-data-inf`, `opal-data-bd` or `opal-data-cot`.
  - The 2 CloudTrail-sourced rules match API calls, not bucket notifications.
  - **None can fire on `opal-data-etfs` objects** except the three new rules this act creates.
- **Keys 12-14:**
  - Lambdas: 219 listed, 0 contain `rivalfunds`; the control `etfs-netassets-daily` is present (1).
  - Roles: 265 listed, 0 `rivalfunds`.
  - Schedules: 24 listed, 0 `rivalfunds`; an etfs control is present.
  - Event rules: 144 listed, 0 `rivalfunds`.
- **This seat's own measurement error, caught:** a first pass used `--query "length(...)"` on paginated `list-functions`. It read
  the control as 0 and the total as 19, the page count. That is CLAUDE.md 22a. The numbers above are client-side counts over
  every page.

## 2. CONDITIONS

1. **The four act-start gates in the COO half stand** (no deploy rider; create-only plans; keys 1-10 at 0; the NEVER-2 entry
   committed first).
2. **Added to gate 2:** before the `etfs-rivalfunds` apply, re-scan the EventBridge rules for any `aws.s3` `Object Created` pattern
   that names `opal-data-etfs` or carries no bucket filter.
   - The scan has **0 read errors**. This seat's scan had 1 unclassified rule, and a zero with an unread member is not a zero.
   - Any match STOPs.
3. **Applies go through `safe-apply`, never a bare `terraform apply`** (CLAUDE.md NEVER). The gateway goes through
   `safe-ec2-deploy.sh` with its own pre-act backup.
4. **The backfill's request volume is printed before the first request:** trading days 2025-06-13..T-1 per the trading calendar
   (`lib/trading_calendar.py`), at the collector's pacing. Scripted egress, R-21.
5. **After the act:**
   - `/rivalfunds` is read through the gateway behind OIDC once, and the served bytes equal the newest `platinum/page` object;
   - `/healthz` reads 200;
   - `etfs-netassets-daily`'s next scheduled fire is unmoved: its homes are untouched, and one read at its next fire confirms it.

## 3. ROLLBACK

The COO half stands, per key: `terraform destroy -target` on the new resources only; redeploy the gateway's pre-act bytes. A delete
of the new data prefixes is Andrew's act.

## 4. NOT COVERED

- any key outside the 16;
- the tier-first prefixes;
- any other gateway route;
- a second issuer;
- the crosswalk (every trade grades UNRESOLVED in round 1, as the half states).
