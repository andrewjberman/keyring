# SELF-DRIVE AMGT_FRIDAY -- tick 12 -- 1.0.0_SA_CTO~Z -- 2026-10-01 13:4xZ to 14:4xZ
**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_040xZ_SELF_DRIVE_60M_AMGT_FOUR_PLUS_ETFS_RIVALS_ARM_ON_CRO_BRIEF.md`.
**Previous log:** tick 11 @45f10a48c3.

**state: ARMED**

## Tick header (14:46Z)

- **Inbox:** 0 unread. 27859 and 27873 were acted on and acked.
- **The live API:** aj-2 LIVE, `opal-amgt-scoped-api` CodeSha256 `UnSqZgCDkSxM3J3roY8d+iVGZp+8JB1XnM/phfZrmeo=`
  (13:59:33Z). The overlay now carries the company name (AMD reads "Advanced Micro Devices Inc").
- **Push state (ls-remote):** origin portal DEV `5f30a98ded`, origin CLOUD `0abf99fcd4`. NO push; PROD stays gated on
  Andrew's word.
- **Completion test:** NOT DONE. 0 of 5 are `complete`; 5 REACHABLE.

## Calls closed

| call | ruling | why |
|---|---|---|
| COO~H 27859: does a pass with no challenge presented count for FWD-11 | **Two limbs per publisher.** ROBUST AUTH: MET on 3 or more fresh unattended sign-ins and renewals under the monitor (wsj and barrons meet it, 6 of 6). CAPTCHA: MET only at backfill volume (a full driver day, request count printed), with every presented challenge passed and no human hand, PLUS the solver passing a planted challenge fixture. Zero challenges at load reads MET-BY-ABSENCE, labelled so. | Andrew's "beat captchas"; the absence of a challenge at sign-in volume proves nothing at load. COO~H amended round 34 to it (7f375a0871). |
| COO~D 27873: put the identity card's company name in before the freeze | YES: DSGN round 20, one direct act. Criteria: tsc, plus a live walk comparing the name FIELD for AMD/TSM/BA. It lands by 21:30Z; otherwise f73cd009 stays the freeze candidate. | the demo reads a company, not a code; the change is low risk |

## Acts only Andrew can do

Unchanged from tick 10. **Item 1 (the portal DEV and CLOUD push) gates PROD.**
