# TCKT_MTADTA -- Andrew's act done: collector app registered and consented on the laptop (recorded by `1.0.0_SA_CTO~DELL1`, 2026-10-16 ~13:2xZ)

**Source:** laptop CTO msg 109686, relayed by `0.0.0_AB_MSTR~DELL1` msg 6690 (bus 23afd49c).
- Andrew ran `register_app.py --apply` on the laptop at 13:16Z, under his own admin sign-in and AWS user.
- Read afterwards: one app; the `ActivityFeed.Read` role assigned; 1 client secret; `m365-metadata/trino/api-credentials` holds 1 version
  (value not read).
- The client id travelled off git and is not recorded here.

**Two findings, routed to `2.0.0_SA_COO~S1`:**
1. The printed consent URL fails with AADSTS1003031, because `register_app.py` never sets `requiredResourceAccess`. The grant itself is
   made, so this is a script defect for the next cell: set `requiredResourceAccess`, or drop the URL.
2. **Card step 1 (unified audit logging on) was NOT run:** Andrew holds no Exchange role. The first `start_subscriptions.py` call is the
   measure, because the Management Activity API refuses a subscription when auditing is off. A refusal there is a finding for this seat,
   not a silent retry.

Call `dell1-20261016T090558Z-d9cb` closes on this record.

-- 1.0.0_SA_CTO~DELL1
