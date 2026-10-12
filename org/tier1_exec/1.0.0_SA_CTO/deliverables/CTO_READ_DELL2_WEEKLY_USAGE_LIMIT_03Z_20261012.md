# CTO read -- dell2 hit its WEEKLY Claude usage limit at 03:08Z 2026-10-12 (resets Oct 17, 5 pm ET); 16 seats stopped; the call is Andrew's

From 1.0.0_SA_CTO (laptop, cluster lead), 2026-10-12 ~12:3xZ. Source: `0.0.0_AB_MSTR` msg 108541 relaying `0.0.0_AB_MSTR~DELL2`
(bus d427e8b2), which peeked `1.0.0_SA_CTO~DELL2`'s tab: "You've hit your weekly limit - resets Oct 17, 5pm (America/New_York)" at
11:08 PM ET (03:08Z). All 16 dell2 seats went silent within minutes (this seat's commit census: lanes last at 01:32-03:03Z). Each
sits at a three-way prompt (stop / wait until Oct 17 / switch to usage credits). Only the dell2 manager runs, on the fresh
account Andrew signed in at ~12:25Z; it has keyed nothing. Crossbox mail for dell2 seats is delivered to inboxes they cannot
read yet. No dell2 work moved 03:08Z-12:25Z, and none moves until the seats are re-keyed or the week resets.

## What stalls on dell2 until then (placement DELL2, status active)

IRPT_BCKEND (the Investor Reporting backend; Monday 14:15Z fire read owed), IRPT_ANLREQ (release 6 fallback cell, AR-y-101..103),
IRPT_YCDGEN (FWD-1 not yet run), IRPT_DASHBD (Monday 13:00Z fire writes one more manifest; R45 packet), DSGN_IRPTV1 (PROD
candidate), ADVI_COTBKF (round 71 corrections), TCKT_VNEXT (fifth run on st32), NFRA_TRNSPT (round 23 cells; Monday 13:00Z fire
read), NFRA_OPSWKF (the trade-handler fence FWD, no lane anyway), ADVI_BILLING (parked). Cross-box asks TO dell2 from site Z
(ad8b, 7884) and the laptop's returns to it wait with them.

## The call (Andrew's; money and seating)

(a) Move dell2's seats onto the fresh account (each seat re-launched by the dell2 manager under `ajb` on that account; the
model policy unchanged: dell2 is the Sonnet-worker control arm) -- fastest; the cost is the fresh account's own weekly budget.
(b) Buy usage credits on the exhausted account and let the 16 seats take the "switch to credits" branch -- metered spend.
(c) Re-place the time-bound projects (IRPT_BCKEND, IRPT_DASHBD, NFRA_TRNSPT for Monday's fires) on dell1 or the laptop for the
week -- a placement change per project, workers and worktrees re-cut, the most disruption.
(d) Wait until Oct 17 -- five days of no Investor Reporting, Ticket Center or Cottonwood-backfill progress.

REC: (a) for the three time-bound projects' lanes first (IRPT_BCKEND ~P2, IRPT_DASHBD ~D2, NFRA_TRNSPT ~T2 with their CloudOps
lanes), the rest as (a) or (d) by his word; (c) only if the fresh account is not the same subscription tier. One line decides.

## Why this is also a measurement for the model-policy question (Andrew 2026-10-11 ~18:1xZ, q.4)

dell2 (Sonnet 5.5 workers, the control arm) exhausted a weekly budget first; dell1 (haiku workers, the treatment arm) carried a
comparable commit load (1,045 vs 1,229 commits since the policy) and has not. The other boxes' headroom is being read now (MSTR
asked 12:3xZ) so the comparison has a denominator; it is recorded here so the next model-policy read has it.
