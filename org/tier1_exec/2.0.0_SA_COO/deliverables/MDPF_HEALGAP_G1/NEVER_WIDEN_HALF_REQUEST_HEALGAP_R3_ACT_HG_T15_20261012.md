# Never-widen half (COO half SIGNED, CTO half owed): MDPF_HEALGAP round 3, drain act HG-t-15 -- retire the 07:00Z registry rule

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-12 ~14:0xZ. **For:** `1.0.0_SA_CTO~DELL1`, who owes the CTO half.
**Ruling this applies:** CTO ADDENDUM 5 `0c9f67d92d` (msg 3898): "The 07:00Z retirement is its own pair, cut the day the first 12:45Z fire is read
(13:15Z-only path serves a correct registry.json with no 07:00Z write) and applied within one trading day."
**Status:** order `MDPF_HEALGAP.TO-HG-t15` issued (`0d488da900`, workstream `RULERETIRE`); worker `0.9.0_WK_MDPF_HEALGAP~12` running. Nothing applied.
The CTO half is asked once the worker's proof and the merge are in; the bytes read are named then.

## 1. The act

`terraform` in `infra/aws/terraform/cot-pipeline`, via `.tools/safe-apply.sh`, saved plan, `-target` on exactly:
`aws_cloudwatch_event_rule.cot_satellites_registry_producer_daily`, `aws_cloudwatch_event_target.cot_satellites_registry_producer_daily`,
`aws_lambda_permission.events_cot_satellites_registry_producer`.
**Condition:** the plan reads `0 to add, 0 to change, 3 to destroy` and those three addresses only. Any other line refuses the act.

## 2. The measured case for retiring it (first exercised day, 2026-10-12)

- 07:00Z invocations of the rule: 07:00:15Z, 07:01:11Z, 07:03:16Z (the original and the two async retries), each `RegistryProducerError: BLOCKED: no
  roster partition at .../rebalancer_models/2026-10-12/page_000.json (S3 said AccessDenied)`, durations 1594 / 190 / 205 ms, no write.
- `registry.json` LastModified 2026-10-11T13:15:48Z and `holdings.json` 13:15:49Z were unchanged until the 13:15Z stamp-gated fire (13:15:47-48Z,
  3300 ms, `as_of` 2026-10-12, rc 0). The sentinel invocation pulled at 11:32:07Z (stamp 11:32:28Z), so a 07:00Z fire can never find today's roster.
- Writers of `registry.json` / `holdings.json`: N = 1 by grant (role `cot-satellites-registry-producer-role`, statements `WriteSatellitesRegistry`,
  `WriteSatellitesHoldings`, read live 2026-10-11 05:1xZ); triggers 2 before, 1 after (the stamp-gated rule). Same function, same code, same two keys.

## 3. What changes, and what does not

- **Changes:** three EventBridge objects are destroyed; the daily failed invocation (3 attempts) stops; the log group stops accumulating
  `BLOCKED` lines at 07:00Z.
- **Does not change:** the function, its code, its role and policy, the stamp-gated rule `etfs-cot-satellites-registry-producer-stamp-gated-daily`
  (`cron(15 13 * * ? *)`, input `{"require_stamp":true}`), its permission, any served key. Served delta: 0 (the 07:00Z fire wrote nothing).
- **Loss, named:** if HG-t-5 is ever rolled back to the 06:00Z runner, the 07:00Z rule is the one that would serve the same-day registry again;
  the rollback of HG-t-5 must restore this rule in the same act (the order's comment and this half say so).

## 4. Every reference to the rule's name (comp-find, corpus all, 183-193 hits across 85916 files; HEAD/DEF/SURFACED/CONFIG bands)

| where | what it is | effect of the retirement |
|---|---|---|
| `satellites-registry-producer.tf` | the resources (this act's write set) | removed by the order |
| `satellites-characteristics-producer.tf` (comment, line 35) | a derivation note naming the 07:00Z rule as the margin's anchor | stale text, no behaviour (already superseded by HG-t-14's 13:25Z derivation; row `D1-W11-S1`) |
| `org/tier1_exec/2.0.0_SA_COO/.../R3_CHECKS/hg_r3_rules.py --t9` | HG-t-9's acceptance asserts the 07:00Z rule exists | reads `T9-BAD` after the act; HG-t-9 is complete and is not re-graded (named in the order) |
| `infra/logic/registry/root_map.json` | LGIC registry row `cot-satellites-registry-producer-daily`, `EVENT_RULE`, system `posn` | a registry row for a resource that no longer exists. **Not edited here (not this lane).** |
| `workflows/legacy_transform/mdpf/20261011T181700Z-98fc86e/{plan,contract}.json` | an in-flight LGIC legacy-transform plan: row R-0118, tension T-0073 "current spelling vs `{system}-cot-satellites-registry-producer-daily`", step MAP | that tension and any later rename step become moot; the migration project's owner must disposition R-0118 / T-0073 |
| change-management records, POSN_ASTTAX and ETFS_SATELLITES orders and proofs, TO-6-AE records, CVO certification | history | none |
| `org/missions/D14/LGIC/**` deliverables and census JSON | LGIC census outputs naming the rule | none |

**Open for the CTO (not for this act):** the LGIC registry row and the in-flight plan name a resource this act destroys. The half does not
edit them. Who dispositions R-0118 / T-0073 is the LGIC migration project's owner; the CTO routes it.

## 5. Rollback

Restore the three resource blocks from `f3afa83d59` (the file at the base of the order) and apply the same three targets; read back
`list-rule-names-by-target` (two rules) and the lambda policy (two statements). A run already made by either rule is inert: both write the
same two keys from the same code, one writer.

## 6. Acceptance

1. `list-rule-names-by-target` on `cot-satellites-registry-producer` reads exactly one rule, the stamp-gated one; `describe-rule` of
   `cot-satellites-registry-producer-daily` reads `ResourceNotFoundException`; the lambda policy carries only
   `EventBridgeCotSatellitesRegistryProducerStampGated`.
2. The first 07:00Z after the act: zero invocations in the log group (the three `BLOCKED` attempts are gone).
3. The 13:15Z fire the same day: unchanged (`require_stamp`, `as_of` that date, both keys rewritten, rc 0).
