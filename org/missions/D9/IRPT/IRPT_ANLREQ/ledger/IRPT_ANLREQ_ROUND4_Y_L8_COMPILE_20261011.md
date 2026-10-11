# IRPT_ANLREQ round 4, workstream Y -- L8 COMPILE: release 5 was applied, exercised, and ROLLED BACK after 61 minutes; one cell built

Compiled by the issuer `2.0.0_SA_COO~Y2` on dell2, 2026-10-11. Decomposition: `org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R4_Y.md`.
Analysis cut from: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_ROUND_4_Y_20261011.md` @9da283e89f.
`python .tools/round-close-check.py --project IRPT_ANLREQ --round 4` after the last merge: 8 orders in scope, 7 complete, proof_ok 7,
proof_bad 0, verdict MAY-CLOSE. (Its first run read REFUSED, proof_ok 3 of 7; section 6 says why. Which order is the eighth was not read.)

Claim words: MEASURED = this seat ran or read it; RELAYED = the laptop reader's read, carried by `0.0.0_AB_MSTR~DELL2`; INFERRED = said so.

## 1. State at this compile

- **Live:** irpt-status runs revision 6, `6idtFvAmYk73wJdr5DPRIyEPrLeWgzjlqbdNr5f1wxc=` (MEASURED ~11:5xZ). NOTHING built in rounds 3 or 4
  is live on the service. The Ticket Center change of round 3 is on portal DEV.
- **The source map builds the live bytes** (MEASURED at 1f37df97ed: check `y33-digest` prints `Y33-DIGEST-OK`).
- **Thread:** `n`.

## 2. Release 5: applied 10:25:40Z, rolled back 11:26:53Z

Pair: `deliverables/2.0.0_SA_COO~Y2/release5/NEVER_WIDEN_PAIR_ANLREQ_RELEASE5_IRPT_STATUS.md` (blob 1b310f3c2a) and the CTO half @2c3d9e91af.
Orders: `org/tier2_senior/0.7.0_AE_CloudOps~DELL2/task_orders/IRPT_ANLREQ.TO-APPLY-Y5.irpt-status-release5-dell2.md` (complete, ROLLED BACK)
and `org/tier2_senior/0.7.0_AE_CloudOps~ANL/task_orders/IRPT_ANLREQ.TO-READS-Y5.release5-after-reads-laptop.md` (complete).

**While live (build `Iw3FADFr`):**
- R0, R1, plan 1 change, re-plan 0, reach read count 0: the applier's record, re-checked by this seat (`APPLY5-RECORD-OK`).
- R8: both tenants 200 with the same keys, but it reached a `NOT_AUTHORIZED` refusal only. Recorded "refusal envelope only".
- R2 true: `retained_ref` present after and absent before, on 14 readable of 50 accepted requests; 0 receipt refusals.
- R3 true: 40 rows before and after; every row carries `client_id` and `client_claim` (UPLOAD 40); the page carries `unreadable_rows` 0.
- R5 true (50 compared, 0 changed). R6 and R7 true (S3 object versions 3 and 3; DynamoDB not counted).
- R4 ABSENT, NOT EXERCISED: 0 OPAL_ENGINE among the 14 readable; `REQ-5e4149d2` refuses `FIRM_BINDING` on owner replay.
- Unit read (analysis item 3, row `IRPT_YCDGEN-D2-S38`): 988 served sections; 513 with unit `pct`, of which 425 carry an absolute value
  of 1 or more and 88 below 1 (zeros included). This seat's run of the reads check on the laptop's file: `APPLY5-READS-OK`.

**Why it was rolled back.** The portal's history reader admits EXACT key sets: `readOwnedHistory` exactly `items` and `next_cursor`,
`readOwnedRequest` an exact row key set (READ by this seat at portal PROD `37aa1247ee` and DEV `11f25102dd`,
`src/pages/InvestorReporting/contracts/owned-requests.ts`). Release 5 added one page member and two row members. So every Investor Reporting
history read through the portal was refused for 61 minutes (INFERRED from the reader's code and R3; nobody looked at the page). Found by
`2.0.0_SA_COO~D2` (msg 4804); rollback ruled by the CTO (msg 4805); ordered 11:20Z; rows `IRPT_ANLREQ-D2-S43` (armed) and `-S44` (disarms it).

**The rollback:** the recorded revision-6 object version copied onto the key, no S3 delete; plan 1 change, re-plan 0; ledger closed;
the map entry restored (the applier's record `R5_rollback_record.json` @0581ad2a46). MEASURED: live `6idtFvAm`, 0 release-5 sentinels open.
RELAYED: owner history after the rollback reads page keys `items`, `next_cursor` and row keys `accepted_at`, `identity`, 40 rows.

**What the pair missed, and it is this seat's:** the blast radius named the function and 19 backend readers, never the portal reader
that consumes the changed answer; all nine after-reads read the SERVICE's new fields and none read the page. The CTO says the same of
its half (msg 4805).

**Order of return (CTO msgs 4805, 4819):** the portal reader that admits both answers on PROD first (DSGN_IRPTV1 cell IV-e-99; on DEV
at `8ed372cb72` by the integrator's receipt; PROD is a client-facing push and waits on Andrew's word), then the service, with the page
among the after-reads. A later named cell makes the reader contract-exact.

## 3. The map hazard after the rollback (rows S45, S46)

After the restore, the map recorded `6idtFvAm` and BUILT `UNn2/KeP` (MEASURED): two members came from the tree, which holds the breaking
history change. Any rebuild-and-apply would have re-broken the page. CTO ruling msg 4838: pin `owned_requests.py` and `prospect_dates.py`
at `361c44fa9d`. Done under TO-AR-y-33 AMENDMENT 2, merged @1f37df97ed; `Y33-DIGEST-OK` by this seat. Limit: true only of a tree that
contains that commit. The un-pin condition is written in the entry: the reader on PROD.

## 4. The one build cell (TO-AR-y-41)

- `AR-y-41` DONE, merged @35c17fdd07: `persist_inputs.report_index` members typed from the producer -- `report_id` `^RPT-[0-9a-f]{32}$`,
  `revision` 64 hex, `retention_ref` a closed two-member object. The analysis counted two empty members; three were measured and typed.
  Four fixtures held values the producer never writes and were corrected. `Y41-TYPES-OK`, `Y41-KEEP-OK` (2 failed, 203 passed) by this seat.
- `AR-y-42` CLOSED AS A RESULT, not passed (CTO msg 4797): fresh generator output drops hand-added exports and, by the worker's report
  (not re-run here), breaks 13 types in 8 consumers. The wire folder's regeneration with its consumers is DSGN_IRPTV1's; branch
  `wk-IRPT_ANLREQ-51-portal-r4` @890f1d0f3d is its input, not merged. Rows `IRPT_ANLREQ-D2-W51-S6` (BLOCKING), `-S7`, moved with it.

## 5. Rows of this round

| row | class | disposition |
|---|---|---|
| IRPT_ANLREQ-D2-S43 | BLOCKING, was ARMED | disarmed by S44 (rollback; the relayed two-key read) |
| IRPT_ANLREQ-D2-S45 | BLOCKING, was ARMED | disarmed by S46 on a tree containing 1f37df97ed |
| IRPT_ANLREQ-D2-S39 | OBSERVATION | `irpt-ycharts-generate`'s five digests: `2.0.0_SA_COO~P2`'s read-only cell (CTO msg 4622) |
| IRPT_ANLREQ-D2-S41 | OBSERVATION | REL4-READ5 now rides TCKT_VNEXT's fourth run (inherited from `2.0.0_SA_COO~G2` msg 4700) |
| IRPT_ANLREQ-D2-W51-S6, -S7 | BLOCKING, OBSERVATION | moved to `2.0.0_SA_COO~D2` with the wire folder (CTO msg 4797) |
| IRPT_ANLREQ-D2-S36 | OBSERVATION | the pinned-member finding; the one-tree re-pin it led to is withdrawn with the rollback and returns with the re-release |
| IRPT_ANLREQ-D2-S26 | ARMED | unchanged: one test message on the commentary-ready queue until about 2026-10-15T06:10Z |

## 6. This seat's defects in the round

- The blast radius of section 2.
- A complete flip of TO-AR-y-41 beside a FAIL row (@ce4c252845), reversed; the criterion was then retired by amendment on the CTO's ruling.
- `apply5_checks.py` resolved its default root one folder too high; both appliers hit it on the verbatim invocation. Fixed @e678c59c59.
- The CTO was not told when the hold was lifted and the apply landed; it asked (msg 4744).
- The round-3 packet's section 5 claim, corrected in that round's addendum.

## 7. For L9

Judgment criteria on these orders: none cut by this seat. What a reviewer may grade on its own reading: whether section 2's "exercised"
can stand for a release whose consumer refused it; and the two INFERRED statements (the page was refused for 61 minutes; it answers
again), neither of which anyone observed on a page.
