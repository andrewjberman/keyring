# Andrew-direct 2026-10-13 ~14:3xZ (laptop, 4.0.0_SA_CRO terminal) -- NFRA_DEVPLN recs approved; COMM_ASSIST to be run mostly through "muse"

## VERBATIM

> "yes agreed for all of this. I also think that we should ultimately aim to set up COMMS_ASSIST in a manner that I can handle most
> of it through "muse" on tailnet. Muse does not have AWS CLI, which means that information needs to be placed somewhere it can read,
> I think this can be hosted on DELL2 somewhere local on the device, maybe DELL2 has some kind of script that pulls open-calls and
> other summary info from AWS that muse would need on some local schedule to DELL2 local for muse to access through SSH. The issue is
> that Muse is a lot more user friendly/intelligence than Kimi, because the Quo-phone line approach is a little rigid and
> unintelligent compared to coming up with a muse-focused solution, so I also want to figure out how to wrap COMMS_ASSIST into a
> muse-friendly solution based on the work we're doing with the tailnet already and so on"

## Applied

1. **"yes agreed for all of this"** answers the CRO's summary of ~14:2xZ. It approves the five NFRA_DEVPLN open decisions as
   recommended, in `docs/briefs/nfra-devpln-per-box-portal-dev-approval-brief-20261013.md` @5386676d4f:
   - (a) one approval covers one feature;
   - (b) Andrew approves client-facing features, the box CTO approves Opal-internal ones, and test-only changes need none;
   - (c) approvals go through the open-calls list first, then COMM_ASSIST;
   - (d) DEV is accepted as the baseline after a review by feature group;
   - (e) PROD is merged back into DEV once.

   Routed to `1.0.0_SA_CTO` for NFRA_DEVPLN's L2.
2. **COMM_ASSIST through muse.** `muse` is Andrew's VM on the tailnet (100.113.31.20, per
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/LD0644_ROLLOUT_PLAN_CLUSTER_REMOTE_ACCESS_TAILNET_20261011.md` line 16). The direction:
   - muse becomes the main way Andrew works COMM_ASSIST, ahead of the Kimi + phone-line (Quo) text path, which he calls "a little
     rigid and unintelligent";
   - muse has no AWS CLI, so a script on dell2 pulls open calls and the other summary information from AWS on a local schedule into
     a folder on dell2;
   - muse reads that folder over tailnet SSH.

   The CRO writes a midstream brief on COMM_ASSIST for this. COMM_ASSIST is site Z's project: its owner reads the brief through
   `0.0.0_AB_MSTR`, and the laptop CTO rules any cross-box part.
