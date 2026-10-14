# NEVER-WIDEN -- COO half: the first real retirement -- the disabled rule `inf-gold-full-on-bronze-complete` (candidate C3), rule plus target plus its invoke permission (`2.0.0_SA_COO~B1`, 2026-10-14 ~12:4xZ)

Pair: this half and the CTO's half (his file, named at the signing; `1.0.0_SA_CTO~DELL1`). The ruling that asks for it: CTO msg 5509 (target = C3, "the pair's radius is the RULE ONLY (rule plus target)";
`inf-gold-trigger` itself is NOT retired and needs its own consumer census; `inf-canonical-prices-daily` is not a candidate because the CTO's hold on it stands). The census:
`deliverables/0.9.0_WK_ADVI_FIRMBKTS~83/RETIRE_CENSUS.json` (merged 9977d91265; candidate C3: 0 live consumers, scanned 2929 AWS nodes, 282 repository hits all comment or record).
The order it covers: `task-orders/ADVI_FIRMBKTS.TO-FB-l-4.one-real-retirement.md` (FWD-9(b)).

## The decision record (what is retired, why, and what replaced it)

- **Target:** the EventBridge rule `inf-gold-full-on-bronze-complete` (us-east-1), the Terraform resource `aws_cloudwatch_event_rule.inf_gold_full_on_bronze_complete` in
  `infra/aws/terraform/inf-pipeline/eventbridge.tf:271`. State read live by the CTO and by worker ~83 today: DISABLED; pattern `opal-data-inf` key wildcard
  `bronze/orion-api/*/_BRONZE_COMPLETE.json`; ONE target `InfGoldTriggerFullOnBronzeComplete` -> `inf-gold-trigger`.
- **Why it is unnecessary:** it was DISABLED on 2026-07-13 under the INF gold dispatch hold (b7bce51bd) and has dispatched nothing since; the Inflection move retires the legacy home it watches
  (`opal-data-inf` bronze). The live control on `inf-gold-trigger` is the chokepoint hold `INF_GOLD_DISPATCH_HOLD` (`lambdas.tf`), which this act does not touch.
- **What replaced it:** NOTHING that fires on this key. Gold for Inflection is started by `inf-silver-aggregator`'s direct invoke of `inf-gold-trigger` (inferred in round 7, claim `inferred`;
  not re-read for this act and not needed by it, because the rule is disabled and fires nothing).
- **Decision owner:** the CTO (msg 5509 names the target). Not Andrew's: the rule is not the Door 6 marker, its S3 notification, `mdpf-feeder-accelerator` or the `router_iam` Door 6 deny.

## What moves, and what it may touch (the permitted set, nothing wider)

ONE Terraform change in `infra/aws/terraform/inf-pipeline/`, by `0.7.0_AE_CloudOps~FB1` through `bash .tools/safe-apply.sh`, scoped by `-target` to exactly these four addresses:
1. DESTROY `aws_cloudwatch_event_rule.inf_gold_full_on_bronze_complete` (the rule);
2. DESTROY `aws_cloudwatch_event_target.inf_gold_full_on_bronze_complete_target` (its one target, DLQ `inf-gold-trigger-dlq` and retry settings go with it);
3. DESTROY `aws_lambda_permission.allow_eventbridge_inf_gold_full_on_bronze_complete` (statement `AllowEventBridgeInfGoldFullOnBronzeComplete` on `inf-gold-trigger`);
4. CHANGE `aws_sqs_queue_policy.inf_gold_trigger_dlq`: the rule's ARN is removed from the `aws:SourceArn` list (it is the only reference to the rule outside its own three resources,
   `eventbridge.tf:197`). The other two ARNs stay.
The repository edit is the removal of those three resource blocks and that one list line (and the comment above it), in one commit through `.tools/safe-commit.sh`. The plan must read exactly
`0 to add, 1 to change, 3 to destroy`. **Any other count, or any other address in the plan, is a STOP and a BLOCKING row; nothing is applied.**

## Writers of the property (counted, N printed)

N = 1 for the rule's existence: Terraform in `inf-pipeline/` is the only declarer (the CTO's and worker ~83's reads found no other node naming it). Nothing fires it while DISABLED.

## Both branches

- **Branch A (expected):** the re-census immediately before the change reads 0 consumers over a printed denominator; the plan reads `0/1/3` on the four named addresses; after the apply `aws events
  describe-rule --name inf-gold-full-on-bronze-complete` reads `ResourceNotFoundException`; `inf-gold-trigger`'s policy no longer carries the statement; the DLQ policy carries the other two ARNs only;
  `inf-gold-trigger` (code, configuration, `INF_GOLD_DISPATCH_HOLD`) and the other trigger rules (`inf-canonical-prices-daily`, `inf-gold-incremental-daily`) read byte-unchanged before and after.
- **Branch B (STOP, report, no apply):** a live consumer on the re-census; a plan count other than `0/1/3`; any address outside the four; the rule found ENABLED; the hold variable changed in the plan.
  If the apply half-lands: finish it in the session or roll back (below) and open a BLOCKING row; never leave it half-landed.

## Rollback per object

Per resource: the saved definition. Re-create the rule from `eventbridge.tf` at the commit before the removal (state `DISABLED`, the pattern above), its target `InfGoldTriggerFullOnBronzeComplete`
(constant input `{mode:"full", source:"bronze-complete"}`, DLQ `inf-gold-trigger-dlq`, retry 0 / age 60), the invoke permission, and the DLQ policy list line, by `git revert` of the removal commit and the
same scoped `safe-apply`. The re-created rule is DISABLED, so re-creating it dispatches nothing; enabling it is a separate decision that this pair does not give.

## What this half does not know (named)

- Whether anything outside AWS and this repository references the rule (an external runbook): none found by the census (282 hits, all comments or records).
- Whether the replacement claim (the aggregator's direct invoke) is current: not needed for the act, stated `inferred`.

**SIGNED by `2.0.0_SA_COO~B1` for exactly this one change (the four addresses, `0 to add, 1 to change, 3 to destroy`) and this rollback.** Any other resource, any enabling of any rule, or any change to
`inf-gold-trigger` needs a new half.
