# IRPT_CUSTDY decomposition -- ROUND 7, ADDENDUM 1 (issuer 2.0.0_SA_COO~K2; 2026-10-07 ~17:4xZ, dell2)

**Status: ISSUED** (the issuance commit carries the `fanout:` line). Workstream `~K2-B3`.

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-6 ADDENDUM 1
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_CUSTDY_ROUND_6_ADDENDUM_1_HOP5_BREAKS_20261007.md` @c3addc6f25
(msg 914), Ruling 1: "`~K2` cuts break 3 as a one-key adapter on its side. The custody document carries `as_of_date` as the export
contract names it. Its first producer is this project, so the contract's name wins; no consumer is asked to read two names." Row S14.

The round-7 decomposition @0b672a8d47 is unchanged: E1 done, E2 re-scoped by the addendum (waits on IRPT_BCKEND P-c1..c3 + PROD),
E3 gated on the Black Diamond report. This addendum adds one cell.

## Measured constraints (dell2, ~17:4xZ)

1. **The contract:** `infra/aws/lambda/investor-reporting/export/narrative_submit.py` `custody_report_as_of(report)` reads
   `report["as_of_date"]` (YYYY-MM-DD) and refuses by name without it. Hop 3's household documents carry `as_of` today
   (`client_report_figures.py`, `hop3_real_run.py`).
2. **Two consumers of the document key, both ours:** `client_report_figures.validate_document` and the portal template on
   `wk-IRPT_CUSTDY-14-portal` @4c10b488 (`types.ts` 4, `ClientReportDocument.tsx` 7, fixture 1 references to `as_of`). "No consumer
   reads two names" means both move to `as_of_date` together; function arguments and partition dates named `as_of` stay as they are.
3. **4c10b488 is being merged to portal DEV now** (Andrew's word, msg 900). The portal half of this cell is a NEW commit on a NEW branch
   cut from 4c10b488; it lands on DEV later, after CTO review and on Andrew's word, like 4c10b488.

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `CU-g-4` (break 3) | the custody household document carries `as_of_date` (the export contract's name), never `as_of`; validator, producer and template read that one name; the export's own `custody_report_as_of` accepts a produced document | FWD-1 | NOT-EVALUATED | dell2 | LOCAL | A, `0.9.0_WK_IRPT_CUSTDY~16` |

**Fan-out:** `fanout: 1 of 1 chain, cap 8`.

## The issuer's acts after the drain

1. The real run: `hop3_real_run.py --advisor matthew_gooch --as-of 2026-09-30`, then every household document through the export's
   `custody_report_as_of` (all must return `2026-09-30`), and through `validate_document`.
2. The portal candidate to `1.0.0_SA_CTO~DELL2`; DEV on Andrew's word. Tell `2.0.0_SA_COO~P2` (P-c3 mounts the template from that tree).
