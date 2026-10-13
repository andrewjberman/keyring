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

## FB-k-4 findings (Cottonwood serving layer and crosswalk; merged 3ffb7c95a0; record `deliverables/0.9.0_WK_ADVI_FIRMBKTS~79/PLANINV_COTTONWOOD_SERVING_CROSSWALK.json`)

56 rows (16 touch the legacy home); 20 crosswalk rows: the crosswalk INPUT lives outside every legacy home, at `opal-data-assets` key prefix `commonwealth/cottonwood/silver/crosswalk/`
(the issuer listed it: present), with its builder, 7 consumers and 11 module importers. Three rows for the plan:
- `D1-W79-S1`: the Cottonwood Black Diamond scope is in `opal-data-assets/blackdiamond/cottonwood/`, not in `opal-data-bd` (the order's premise did not match).
- `D1-W79-S2`: **Cottonwood holdings have TWO live homes** -- the edge router resolves `cottonwood` to `opal-data-cot`, while the IRPT holdings reader reads `opal-data-cottonwood` (the issuer's
  head-bucket read: that bucket exists). The plan must name which is canonical and move the other.
- `D1-W79-S3`: `bd-cot-freshness-probe` exists in the repository and reads `opal-data-cot`; none of the 237 live functions has that name.
Not read (unknowns for the plan): environment values of 226 live functions, IRPT invocation triggers, SNS subscribers, the default-band crosswalk enumeration (timed out).

## FB-k-1 findings (Inflection pipeline layer; merged 5a848b3fc0; record `deliverables/0.9.0_WK_ADVI_FIRMBKTS~76/PLANINV_INFLECTION_PIPELINE.json`)

54 functions, 34 touch the legacy home (50 measured, 2 held, 2 absent). Kinds: 33 Lambdas, 9 EventBridge rules, 7 scripts, 2 edge, 1 service, 2 other. Denominators: 156 EventBridge rules listed
(targets read for 52), 34 Scheduler schedules (targets read 34), 51 Lambda configurations, 3 bucket notification configs (2 Lambda notifications on `opal-data-inf`, 2 on `opal-data-bd`), 9 ECS task
definitions, 1 CloudFront distribution (7 origins, 30 behaviours), 169 repo files under `data/` naming `opal-data-inf`. Not read: targets of 104 of 156 rules, 31 of 34 schedule sources, the in-instance
runner content, the live Lambda@Edge version, IAM and SNS, object-level listings.
- `D1-W76-S1`: the order's premise (an Inflection scope inside `opal-data-bd`) does not hold: the census holds 0 such tokens and 0 of 247 `opal-data-bd` mapping rows are Inflection. Inflection's legacy
  home is `opal-data-inf` alone (3,127 of 3,451 mapping rows). The plan treats `opal-data-bd` as the shared lake, not an Inflection home.

## FB-k-2 findings (Inflection serving layer; merged ff86b62216; record `deliverables/0.9.0_WK_ADVI_FIRMBKTS~77/PLANINV_INFLECTION_SERVING.json`)

97 rows, 80 touch the legacy home. 237 live Lambdas (238 graph nodes: `D1-W77-S5`, the difference unidentified); 303 IAM roles scanned, 40 with an Allow on `opal-data-inf` and 20 deny-only;
CloudFront distribution with 30 behaviours (0 on the Inflection origin); 17 SNS topics (3 matched); 26 SES identities (2 Inflection, addresses withheld). Rows for the plan:
- `D1-W77-S1`: a second live watcher on the prohibited key (the S3 notification to `inf-portal-publisher`); the PRD names only the `mdpf-feeder-accelerator` rule (see the CTO's ruling above).
- `D1-W77-S2`: **`exec-summary-trigger` is ENABLED live** (the issuer read it: pattern `chain-complete` from `bd-pipeline.gold-chain`), but Terraform declares only a DISABLED placeholder and no Terraform
  declares the live rule: the plan must bring it under Terraform (a drift to name, not a move to start).
- `D1-W77-S3`: the served graph cannot answer IAM-grant or Lambda-environment questions for the bucket; the live read found the 40 roles above.
- `D1-W77-S4`: no Inflection scope in `opal-data-bd` (0 mapping rows, 0 IAM statements), agreeing with `D1-W76-S1`.
Not read (16 items in the record): the orion JWT contents (by rule), line-level code of the pull Lambdas and IRPT source, the edge router rewrite template beyond its firm map, the auth-validator and
public-data-router packages, subscription endpoints and SES addresses, EC2 instance-profile consumers, the second CloudFront distribution.

## FB-k-3 findings (Cottonwood pipeline layer; merged df59f3fb58; record `deliverables/0.9.0_WK_ADVI_FIRMBKTS~78/PLANINV_COTTONWOOD_PIPELINE.json`)

42 rows, 23 touch the legacy home (13 rules, 2 schedules, 13 Lambdas, 4 SSM tasks, 9 repository scripts, 1 bucket configuration). 156 rules with all targets read, 34 schedules, 237 Lambdas (environment
read for 27), 1,741 repository files naming `opal-data-cot`. Rows: `D1-W78-S1` (the Cottonwood scope inside `opal-data-bd` is empty; the legacy home is `opal-data-cot`; see `D1-W79-S1` for where the
Black Diamond Cottonwood scope really is), `S2` (`characteristics.json` header says zero writers but the object was modified 2026-10-13T15:56:02Z: a writer exists), `S3` (a graph Lambda,
`cot-satellites-registry-producer-daily`, absent live), `S4` (`cot-etf-ownership-daily` names `opal-data-cot` in `SRC_BUCKET` but its code does not read it). Not read (14 entries): ECS and Step Functions
contents, 210 Lambdas, the `mdpf-gold-lambda` source and trigger, live code bytes, EC2 state and crontabs, object bodies, the other 32 schedules.

## PLANINV status at 22:4xZ

FB-k-1 to FB-k-5 all merged and complete (5 of 5). Three questions the plan must close, from the unknowns above: the Cottonwood canonical home (two live homes, `D1-W79-S2`), the Door 6 successor
(CTO msg 5260), and the `exec-summary-trigger` rule under Terraform (`D1-W77-S2`).
