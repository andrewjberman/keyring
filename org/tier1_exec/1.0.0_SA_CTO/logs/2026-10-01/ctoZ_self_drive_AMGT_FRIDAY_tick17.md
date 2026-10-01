# /self-drive AMGT_FRIDAY -- tick 17, `1.0.0_SA_CTO~Z`, 2026-10-01 18:46Z-19:46Z

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_040xZ_SELF_DRIVE_60M_AMGT_FOUR_PLUS_ETFS_RIVALS_ARM_ON_CRO_BRIEF.md`. **state: ARMED.**

## Scope state (measured at 19:45Z)

- **Projects:** 5 of 5 `active`, 0 `complete`.
  - **AMGT_HARVST:** round 35 is CLOSED (analysis @89539ccbc2), and round 36 goes to COO~H.
  - **DSGN_AMGTV1:** the freeze candidate is portal DEV `3c37a01c`.
  - **ETFS_RIVALS:** round 4, d-5, is in flight. The v0.8 inputs are held for round 5.
  - **CORPUS and RESAPP:** idle; the Friday face and feed are complete.
- **Inbox:** 0 unread. Acked: 28046.
- **Push state (ls-remote):** origin CLOUD `0abf99fcd4`; origin portal DEV `2bb367ef10`. Nothing has been pushed from site Z.
- **Completion test:** NOT DONE. 0 of 5 are complete, and all 5 are REACHABLE.

## Calls closed

| call | ruling | hash |
|---|---|---|
| CVO~Z 28046: limb 2a is unreachable under hourly grading while people use the Terminal box | **Per-minute grading with a +/-1 minute guard band.** The limb needs 1,440 clean minutes, and every clean-minute challenge must pass. Drivers run unattended 03:00-11:00Z tonight. The ruling was reported to Andrew at this terminal, and his word overrides it. | `89539ccbc2` |
| Limb 2b for the four publishers that presented no challenge | **OPEN (NO SAMPLE).** Capture-at-load stays armed, and a real DOM from the same challenge vendor may stand in. | `89539ccbc2` |
| Andrew's "this pace is fine" was glossed as "no residential arm" | COO~H commits his verbatim words with no gloss, and the residential arm stays on the act list. | `89539ccbc2` |

## Acts only Andrew can do

1. **Push portal DEV and CLOUD, then promote to PROD** (CLAUDE.md Git: `0.0.0_AB_MSTR` pushes trunks on Andrew's word).
   - The freeze candidate is `3c37a01c`.
   - The leg is a pull-merge of origin DEV `2bb367ef`, never a rebase.
2. **A HARVST residential arm, if wanted** (the vendor per-use word; R7).
3. All other items are unchanged from tick 10.

## Compiler Tools

`git log`, `git ls-remote`, `ADJUDICATION_v45.md` read, broker `send_message`/`ack_messages`.
