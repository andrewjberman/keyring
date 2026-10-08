# E8 -- irpt-custody-x10-v1 (PENDING_ENFORCEMENT): the row and its equality proof (2.0.0_SA_COO~M2, 2026-10-08 ~19:0xZ)

Ruling: `1.0.0_SA_CTO~DELL2` analysis ADDENDUM 6 @90d0b7fb71 (msg 1414), item (a). Row IRPT_BCKEND-D2-W175-S1. Lane
IRPT_COMPLETION_REGISTRY (`.owned-paths.yaml:66-74`, this seat).

## The row

`infra/logic/registry/reporting_policies.json` gains ONE row, appended last:
- `policy_id irpt-custody-reporting`, `policy_revision irpt-custody-x10-v1`, register X10 (same register_path and register_commit as
  the other three rows), `ruling_commit` 90d0b7fb719b190bade17dc9cdaf09c812de4ed3;
- `firms` 49financial, cottonwood, inflection (= irpt-x10-v1's);
- `state PENDING_ENFORCEMENT`, `enforcement_ref null`, `physical_disposal OPEN`;
- one family `CUSTODY_REPORT`: `tier platinum`, `table custody_reports`, `extension json`, `unreferenced_days null`,
  `accepted_ceiling_days 2555`. **Source of the terms: mirrors PERFORMANCE in irpt-x10-v1** (every term but the table equal; the
  custody PRD states no retention terms).

Appended last because `lib/tests/test_irpt_destination.py:202` edits `policies[1]` by position (inserting before the dashbd row
failed 6 tests; appending passes all).

## Equality proof (read through the builder, `lib/opal_naming.reporting_policy`)

| check | result |
|---|---|
| rows 1-3 (irpt-x10-v1, irpt-dashbd-x10-v1, irpt-ycdgen-research-v1) vs HEAD | byte-equal as parsed JSON; rows 3 -> 4 |
| top-level keys other than `policies` | equal |
| irpt-x10-v1 `policy_sha256` | `e0046398e23951451498c0fcfec29154db5b26d4c70d80c4121f50fd3dfc8c85` = the test pin `ACTIVE_ROW_SHA` (unchanged: every live retained row under it still binds) |
| new row `reporting_policy('irpt-custody-x10-v1')` | loads; state PENDING_ENFORCEMENT; policy_sha256 `0550a37a722c8fc1...` |
| `reporting_destination(..., 'CUSTODY_REPORT', policy_revision='irpt-custody-x10-v1')` | refused: "reporting policy is not writable: enforcement is pending or disabled" (PENDING grants no address) |
| `preview_reporting_destination` (builder output, the address the row will grant once ACTIVE) | `s3://opal-data-irpt/irpt/<firm>/platinum/custody_reports/<RPT-id>/<sha256>.json`, per firm; PERFORMANCE control `.../platinum/performance_reports/...` |
| `pytest lib/tests/test_irpt_destination.py` | 73 passed (baseline at HEAD: 73 passed) |
| `pytest infra/aws/lambda/investor-reporting/reports/tests` | 120 passed |

## What this does NOT do

- Deploys nothing. The registry reaches a host only inside a later resident package.
- Retains nothing: `ReportRepository.persist` still reserves under irpt-x10-v1 until E9 (`~P2`) lands; with E9 and this row PENDING,
  a CUSTODY_REPORT is still refused (not writable).
- Flips nothing ACTIVE. The ACTIVE flip (40-hex enforcement_ref) is a later act, after E9 is installed (ADDENDUM 6 order).
