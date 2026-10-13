# ADVI_FIRMBKTS -- inputs held for the round-8 move plan (FWD-9) -- 2.0.0_SA_COO~B1, 2026-10-13

Round 7 stays scoped to closing 49 Financial (spec and decomposition frozen). These are the rulings that arrived mid-round and belong to the plan
document, the next enrichment item at the round-7 L10 (CTO msg 5028; PRD v1.5 @c7a122d445). Nothing here starts a move.

## Andrew-direct ~20:0xZ (CTO msg 5128; record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_200xZ_NINE_OPEN_CALLS_ANSWERED_FIRMBKTS_DEMQUE_BRIEF_HARVEST.md`)

| call | ruling | plan consequence |
|---|---|---|
| DEC-12 | YES | its trail is a CloudTrail write (a Dell deny), routed by the CTO to the laptop; the plan cites its outcome, no Dell act |
| DEC-13 Door 6 | RETIRE, no successor marker | retire Door 6 and the `mdpf-feeder-accelerator` rule INSIDE the Inflection move, after a no-other-consumer read; rollback per step |
| DEC-13 B2 | KEEP, untouched | the bucket stays open for it; the plan names it as out of the decommission list |
| DEC-14 mockadv | RETIRE | a census first, then ONE change with its rollback (the packet's census: 255 files carry the token, most under `org/`; live use unread) |

The opal-data-inf sequence hold is LIFTED (both DEC-13 rulings recorded). Do not start an act on `opal-data-inf` from this record: the plan is
written first, and writing it starts no Inflection or Cottonwood move.

## Also carried into the plan (pivot packet O10, `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL1_20261013.md`)

- per firm (Inflection, Cottonwood): every Advisor Intelligence operating function (gold chain, exec-summary generator, IRPT Lambdas, edge functions,
  schedules, notifications); the order of moves with a rollback per move; each legacy bucket's decommission (45-day quiet window, FWD-6); each legacy
  OPERATION to retire (`FIRMSEP-s3-direct-access-bypass`; `inf-canonical-prices-daily` stays disabled and held).
- the Cottonwood crosswalk input (CTO msg 5028).
- the exec-summary pricing defect (B_01 silver-noncash cap, row W75-S2) is the CRO's pricing brief, not a move.

## FB-k-5 finding and the CTO's ruling (msg 5260, ~22:1xZ)

Door 6 is not consumer-free: `opal-data-inf` has an ObjectCreated S3 notification on prefix `gold/meta/`, suffix `pipeline-complete.json`, invoking the Lambda `inf-portal-publisher`
(read live by the issuer; row `D1-W80-S1`, ARMED, disarm owner `1.0.0_SA_CTO~DELL1`). The CTO's ruling: Andrew did not order the publish to stop; he ordered Inflection to run as
49 Financial does ("the same flow for inflection as the comparable 49 Financial/Cottonwood job"). So:
- the plan READS 49 Financial's live trigger for its portal publish and gives `inf-portal-publisher` that same shape in the new home;
- only AFTER that is proven live do the marker, its S3 notification, `mdpf-feeder-accelerator` and the `router_iam` Door 6 deny retire, in ONE change with a rollback;
- `D1-W80-S1` disarms when the plan names the successor and its proof;
- the 13 CTO candidates among FB-k-5's 16 are ruled at the round-7 L10 on the plan's REC per row (record `deliverables/0.9.0_WK_ADVI_FIRMBKTS~80/PLANINV_LEGACY_OPERATIONS.json`).
