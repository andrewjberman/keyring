# IRPT_YCDGEN round 7 -- decomposition: one research role per allowed firm, then FWD-1 re-run

Issuer `2.0.0_SA_COO~G2`, 2026-10-09 ~09:5xZ.

**Input:** CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_IRPT_YCDGEN_ROUND7_RESEARCH_ROLES_20261009.md`
@f29d0d8ca1 (msg 3019), on row IRPT_YCDGEN-D2-S19 @31b9816847.

## Finding

Round 6's real run on 49financial chose OPAL, then failed on `sts:AssumeRole` of `irpt-49f-ycharts-research-role` (`NoSuchEntity`).

In `infra/aws/terraform/investor-reporting/ycharts/resident.tf`, the research roles, their policies and the runner's
`AssumeTheFirmResearchPrincipal` list are ALL `for_each` over `local.ycdgen_firms`. That local is `toset(...firms)` of policy row
`irpt-ycdgen-research-v1` in `infra/logic/registry/reporting_policies.json`.

The row names `["cottonwood"]` only. Each role's name is `module.opal_name` output (rule 30), and its resource list is that firm's
own bucket and scope from `scopes.json`. All three firms hold an enabled client FIRM scope with their own bucket.

## Cell

| cell | lane | what EXISTS at the end |
|---|---|---|
| `YCD-a-7` | ~G2 | The policy row names cottonwood, 49financial and inflection. Each firm's research prefixes name only its own bucket and scope (checked from the registry, as resident.tf derives them). Every code reader of the row's firm list behaves for three firms, with the generate and research suites not newly red. |

**Not cells; the apply pair's legs (applier `0.7.0_AE_CloudOps~DELL2`, never-widen pair):**
- the plan shows +2 roles, +2 policies and the runner policy's assume list at exactly the 3 ARNs;
- `simulate-principal-policy` shows each research role DENIED on the other firms' buckets;
- the apply;
- then F1 re-runs on 49financial: OPAL, zero YCharts markers, a served report. It uses the st28 discipline (st28 is reinstalled
  for the run, with the DLQ and rollback legs).

## Four-postulate record

(i) Domain: the firms of the generate path's allow list, which the policy row now names in full. (ii) One cell, one row edit
plus its readers. (iii) One intent: the Opal path reaches every allowed firm. (iv) The cross-firm fence does not move: each
role reads its own firm only.

fanout: 1 of 1 chains, cap 8.
