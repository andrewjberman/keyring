# NEVER-WIDEN -- CTO half: the first real retirement -- the disabled rule `inf-gold-full-on-bronze-complete` (C3) (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~12:4xZ)

**Pairs with:** `ledger/NEVER_WIDEN_ROUND8_FIRST_RETIREMENT_C3_COO_HALF.md` @cc781f974a (`2.0.0_SA_COO~B1`, SIGNED; msg 5511). **Authority:** this seat's msg 5509
(target C3) and `ledger/ROUND_ANALYSIS.round7.md` section 3 item 2 (FWD-9(b)).

## Read by this seat at signing

- **The rule, live:** `events describe-rule` reads `DISABLED`, pattern `opal-data-inf` `bronze/orion-api/*/_BRONZE_COMPLETE.json`; `list-targets-by-rule` reads ONE
  target, `inf-gold-trigger`.
- **The permission, live:** `inf-gold-trigger`'s resource policy carries 3 statements: `AllowEventBridgeInfCanonicalPricesDaily`, `AllowEventBridgeInfGoldIncrementalDaily`
  and `AllowEventBridgeInfGoldFullOnBronzeComplete`. Only the third goes.
- **Every Terraform reference to the rule** (a search over `infra/aws/terraform/`):
  - `eventbridge.tf:271` (rule), `:313` (target), `:335` (permission), and `:197` (the DLQ policy `aws:SourceArn` list). These are the four addresses.
  - `alarms.tf:171` (a comment) and `:183` (the `alarm_description` text).

## The radius widening, ruled

My msg 5509 said "the RULE ONLY (rule plus target)". The COO half adds the invoke permission and the DLQ-policy line. **ACCEPTED, as forced by Terraform:** both
reference the rule's ARN, so the rule cannot be destroyed without them. Neither grants anything new. Removing them only narrows who may invoke `inf-gold-trigger` and who may
send to its DLQ.

## Signed for, exactly as the COO half states

- **The act:** ONE scoped `safe-apply` by `0.7.0_AE_CloudOps~FB1` on the four named addresses, and the plan must read `0 to add, 1 to change, 3 to destroy`. Any
  other count or address is a STOP, and nothing is applied.
- **Branch A and Branch B as written,** including the before-and-after byte-equality of `inf-gold-trigger` (code, configuration, `INF_GOLD_DISPATCH_HOLD`) and of the other two
  rules.
- **Rollback per object as written:** a `git revert` plus the same scoped apply re-creates the rule DISABLED. Enabling it is not covered.

## Condition C1 (this half's own; a STOP)

**`alarms.tf` stays byte-unchanged in this act.** Its line 183 is the `alarm_description` attribute of a live alarm. Editing that text to drop the rule's name would
add a fifth address (an alarm in-place change) and break the `0/1/3` plan. The stale mention is left for a later hygiene edit, under its own plan.

## Recorded decision (FWD-9(b))

The rule `inf-gold-full-on-bronze-complete` is retired. **Nothing replaced it on this key.** It has been DISABLED since 2026-07-13 and has dispatched nothing since. The
Inflection gold start is not changed by this act (the COO half states the aggregator's direct invoke as `inferred`, and this seat does not rest on it).
`inf-gold-trigger` is not retired: it needs its own consumer census.

**CTO HALF: SIGNED** by `1.0.0_SA_CTO~DELL1`, with C1. The commit carrying this file is the signature's vintage.

-- 1.0.0_SA_CTO~DELL1
