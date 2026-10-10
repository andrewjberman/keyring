# ANDREW-DIRECT 2026-10-10 ~20:0xZ -- delete the retired Terraform roots' leftovers

**Channel:** Andrew at the 4.0.0_SA_CRO terminal, laptop, 2026-10-10 ~20:0xZ (16:0x ET).
**Answering:** this seat's open question since 2026-10-09 ~10:0xZ: may the untracked leftovers in the two retired Terraform roots
(`infra/aws/terraform/canonical-schwab-si2-schedule/`, `infra/aws/terraform/opal-assets-absence/`) be deleted on each box?
It is a recursive delete, which CLAUDE.md reserves for his word.

## Verbatim

> yes delete the retired tf leftovers

## What it covers (scope as asked, nothing wider)

- The two folders' remaining contents on each box. Their tracked files were already removed by `0.7.0_AE_CloudOps~DELL1`
  (26eb2403f8, LGIC_BLANKFIX.TO-BF-aa-1); both Terraform states hold 0 resources (ruling R10-4,
  `ROOT_MAP_ROUND10_RULINGS_20261009.md`).
- Laptop contents measured before the delete: two stray agent-telemetry files (`org/mcp/agent_telemetry/0.6.2_AE_PartnerETL.jsonl`,
  838 B, 2026-06-30; `0.7.0_AE_CloudOps~Z.jsonl`, 208 B, 2026-07-15), `.build/opal-assets-absence-check.zip`, `.terraform.lock.hcl`,
  `frontier-token.tfplan`. No Terraform code, no state.
- NOT covered: the two empty state objects in `opal-313476888478-terraform-state` (an S3 delete; not asked).

## Carriers

- Laptop: deleted by this seat, same turn.
- dell1, dell2, site Z: one line to `0.0.0_AB_MSTR` to relay to each box's MSTR, naming this record.
