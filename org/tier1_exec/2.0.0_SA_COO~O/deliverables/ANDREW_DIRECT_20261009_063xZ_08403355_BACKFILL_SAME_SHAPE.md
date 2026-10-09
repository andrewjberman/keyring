# ANDREW-DIRECT 2026-10-09 ~06:3xZ -- 08403355: ad-hoc history backfill, same schedule, EXACT SAME layout as 08242234 / 08335338

Received at the 2.0.0_SA_COO~O terminal during the site Z reboot wind-down.

## Verbatim

"We have never pulled from it before, but I want to backfill the same shape from the same rest API just ad hoc, and put
it on the same schedule, giving it the same exact layout and related lambdas/processes/etc, EXACT SAME, as is done for
0824 and 0833 schwab accounts"

Earlier in the same exchange: "there is a schwab master we never knew existed but its definitely available via our rest
api, alyssa had sent the acct number" / "08403355 is the number".

## What already satisfies it (NFRA_OPLGTW round 32)

- **Same schedule and layout.** OG-tm-1, applied by OG-ap-1 (rule live 04:29:02Z), put 08403355 on:
  - the daily pull (rule `schwab-canonical-si2-08403355-pull-daily`, 10:45Z and 22:45Z);
  - the box's write grants;
  - the opal-assets silver conversion;
  - the gateway reader roles.
  Each mirrors 08335338. The first scheduled pull is 10:45Z today.

## What it adds (cut by 2.0.0_SA_COO~O after the reboot, under the NFRA_OPLGTW decomposition)

- **Ad-hoc history backfill for 08403355,** through the same SSM pull document, then silver conversion, then completion
  records. It covers the same 13-month window 08242234 and 08335338 now hold, in the same shape. Steps:
  1. A census of which past dates the source still serves.
  2. A never-widen ask: COO half plus CTO half before any write, as for OG-bf-1.
  3. The pulls.
  4. Read back each date: QUALIFIED.
- It does not wait for the 10:45Z day to qualify; that day is the parallel QA arm.

## To confirm with Andrew, not assumed

- **The 49F accelerator.** It is an S3 notification on `schwab/08335338/meta/complete/` that feeds the 49F gold dispatch.
  It is 08335338's alone, and 08242234 has none. OG-tm-1 deliberately left 08403355 without one. "EXACT SAME" as
  08242234 means none. If Andrew wants 08403355 fed into a gold build, the order needs his word naming which one.
- **Source retention.** OG-en-1 enumerated 2026-09-08..2026-10-08. Whether the source serves 13 months back for a
  never-pulled master is measured by the census, not assumed. A shortfall is reported with its dates.

-- 2.0.0_SA_COO~O
