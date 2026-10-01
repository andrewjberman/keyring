# /self-drive AMGT_FRIDAY -- tick 16, `1.0.0_SA_CTO~Z`, 2026-10-01 17:47Z-18:46Z

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_040xZ_SELF_DRIVE_60M_AMGT_FOUR_PLUS_ETFS_RIVALS_ARM_ON_CRO_BRIEF.md`. **state: ARMED.**

## Scope state (measured at 18:45Z)

- **Projects:** 5 of 5 `active`, 0 `complete`.
  - **DSGN_AMGTV1:** the freeze candidate is portal DEV `3c37a01c`.
  - **AMGT_HARVST:** in round 35, ah-3's fixes are drained (a78b06d3e6). Gold rebuild #3 starts at 20:00Z.
  - **ETFS_RIVALS:** in round 4, v-2 amendment 3 is complete (Z-S10 resolved), and d-5 is in flight.
  - **CORPUS and RESAPP:** idle; the Friday face and feed are complete.
- **Inbox:** 0 unread. Acked: 28011, 28014, 28016, 28027.
- **Push state (ls-remote):** origin CLOUD `0abf99fcd4`; origin portal DEV `2bb367ef10`; local DEV `3c37a01c`. Nothing has been pushed from site Z.
- **Completion test:** NOT DONE. 0 of 5 are complete, and all 5 are REACHABLE.

## Calls closed and acts taken (ETFS_RIVALS, on Andrew's live CRO~RV session)

| item | ruling or act | hash |
|---|---|---|
| CRO~RV 28011: the hop-9 method defects | **(a)** an ID-CHANGE needs an identifier relation (CUSIP zero-pad at silver). **(b)** a window with an implausible flow factor is REFUSED, not inferred (band 0.5-1.5, zero-quantity share 0.20, PROVISIONAL). **(d)** `key_resolution` becomes its own G5 column. All three are round-5 cells, and d-5 finishes as cut. | `4baf852611` |
| Hazard on call 1 (the PFOE history from BD/COT) | Raised as a cross-firm data hazard. CRO~RV corrected the source: the funds' own issuer files (28014, @381bec5549). | -- |
| Andrew's three answers (28016, record @19c5277a57) | **PRD v0.8:** IDVZ and PFOE join the rivalfunds Bloomberg leg, daily and backfill, as the one in-pipeline producer. The Positioning pull is untouched. The controls are ACWI (IDVZ) and IWM (PFOE, the Russell 2000), with SCHY still a member. FWD-10 and G9 follow. | `951a2b6a35` |
| Andrew-direct ~18:3xZ at this terminal, confirming v0.8 ("two different data shapes ... separate for separate use case") | Recorded verbatim, and the C-HOME-PRODUCER basis is reworded. | `8d937833ae` |
| CVO~Z 28027: v0.8 SIGNED, with one scope fix | The second Bloomberg request is bound to IDVZ and PFOE ONLY. CVO~Z closed P1 by diff (de9f7664b1). The round-5 cut condition (the G9 style-read preview on ACWI and IWM first) went to COO~RV. | `fe946c1366` |

**Round-5 inputs held for the round-4 analysis:**
- hop-9 a, b and d;
- the v0.8 home-fund Bloomberg leg, with a budget measurement before the first fire;
- the ACWI and IWM controls, previewed first;
- the per-fund issuer floor.

## Acts only Andrew can do

1. **Push portal DEV and CLOUD, then promote to PROD** (CLAUDE.md Git: `0.0.0_AB_MSTR` pushes trunks on Andrew's word).
   - The freeze candidate is `3c37a01c`.
   - The leg is a pull-merge of origin DEV `2bb367ef`; it is never a rebase.
2. All other items are unchanged from tick 10.

## Compiler Tools

`git log`, `git ls-remote`, PRD edits, broker `send_message`/`ack_messages`.
