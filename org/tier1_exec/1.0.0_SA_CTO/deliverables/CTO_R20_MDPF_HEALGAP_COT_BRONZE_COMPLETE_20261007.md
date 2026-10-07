# R20 DECLARED EXCEPTION -- MDPF_HEALGAP, the literal `cot-bronze-complete` in `cot_rebalancer_reattempt.tf` (entry MDPF-HEALGAP-R20-01, register X16)

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~14:0xZ. This is the authority record the naming-gate entry `MDPF-HEALGAP-R20-01` pins.

## Andrew's acknowledgement (R20: "Every exception is sovereign-acknowledged")

Andrew-direct ~13:58Z 2026-10-07 at the `2.0.0_SA_COO~G1` terminal (dell1), VERBATIM: "1.) Yes, rec approved. 2.) Yes this is fine.
Calls 3 and 4 both approved." Recorded by G1 at
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/ANDREW_DIRECT_20261007_135xZ_HEALGAP_ACT1_YES_R20_YES_ACT2_NO_WORKTREE_DELETE_YES.md`
@e5fb41862f. Call 2, as printed and answered "Yes this is fine": *"R20 naming exception: may the existing rule name
`cot-bronze-complete` be written in two places in `cot_rebalancer_reattempt.tf`?"*

## The exception

| field | value |
|---|---|
| entry id | MDPF-HEALGAP-R20-01 |
| register row | X16 (`infra/logic/06_CONFORMANCE_LEDGER.md` section 6) |
| file | `infra/aws/terraform/opal-assets/cot_rebalancer_reattempt.tf` (MDPF_HEALGAP HG-t-2, branch `wk-healgap-1-2`) |
| literal | `cot-bronze-complete` |
| occurrences | 2: the event target's `rule =` and the Lambda permission's `source_arn` suffix |
| axis | A3 naming |
| why | the file attaches a second target to an EXISTING rule (`infra/aws/terraform/cot-pipeline/eventbridge.tf:173`, registered legacy-shaped `EVENT_RULE`, `infra/logic/registry/resources.json`); `opal_naming` cannot build that name, and renaming a live rule is its own R19 migration, never a rider |
| kind | CONDITIONAL: it holds until the rule's own R19 migration renames it, then this file takes the builder's name in that migration's act |
| owner | `1.0.0_SA_CTO~DELL1` |

What it does not cover: any new resource name (the target and permission resources take builder names where they have them), any third
occurrence, and any other file.
