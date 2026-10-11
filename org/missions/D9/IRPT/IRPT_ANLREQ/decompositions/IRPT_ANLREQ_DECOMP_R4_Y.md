# IRPT_ANLREQ -- decomposition, round 4, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO round-4 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_ROUND_4_Y_20261011.md`
@9da283e89f, section 4, the ENRICHMENT LIST (four items). No PRD addendum; the endpoint is unchanged. Workstream G is
`2.0.0_SA_COO~G2`'s; its write surface is disjoint.

**Thread:** FWD-1 is not live. This round closes release 5's reads and one contract defect. It does not make the thread live.

## The four items and where each lands

| item | analysis text | lands as |
|---|---|---|
| 1 | Release 5's apply and its nine after-reads | ALREADY CUT before this decomposition, on the two signed halves: `org/tier2_senior/0.7.0_AE_CloudOps~DELL2/task_orders/IRPT_ANLREQ.TO-APPLY-Y5.irpt-status-release5-dell2.md` (complete @e678c59c59: R0, R1, R8) and `org/tier2_senior/0.7.0_AE_CloudOps~ANL/task_orders/IRPT_ANLREQ.TO-READS-Y5.release5-after-reads-laptop.md` (pending: R2 to R7). No cell here. |
| 2 | The typed members of `persist_inputs.report_index` (row D2-S35), with the portal's wire regeneration closing DSGN_IRPTV1's id `iv-e-26` | cells `AR-y-41` and `AR-y-42` |
| 3 | The served section's unit (row D2-S38), read at R2 | an amendment to TO-READS-Y5 (one more recorded member on R2). No cell. |
| 4 | The census line for `acceptance.py` (AR-y-37) to `2.0.0_SA_COO~P2` | DONE: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release5/GENERATE_MEMBER_CENSUS_AR-y-37_FOR_IRPT_BCKEND.md` @ffa08e68f9, sent. No cell. |

## Cells

| cell | analysis item | what is built | write set | risk |
|---|---|---|---|---|
| `AR-y-41` | item 2, rows D2-S35 and IRPT_YCDGEN-D2-W10-S7 | In `OwnedAnalysisRequest.schema.json`, the members of `persist_inputs.report_index` that are empty schemas get the type the producer actually writes. The analysis says two; the schema at this base holds THREE empty members (`report_id`, `revision`, `retention_ref`), measured by the issuer, and the cell types all three. One refusal test for a wrong-typed value. No served byte changes: the schema is not packaged by any function for validation at runtime | `docs/contracts/investor-reporting/v1/OwnedAnalysisRequest.schema.json`, `infra/aws/lambda/investor-reporting/_contracts/` (the persist_inputs test file and fixtures) | WORLD by the gate's floor (an `infra/` path; tests and a contract document only) |
| `AR-y-42` | item 2, DSGN_IRPTV1 id `iv-e-26` | The portal's generated wire folder is regenerated from the typed contract so `iv-e-26.wire-regen.test.ts` passes: the committed folder equals fresh generator output | portal `src/pages/InvestorReporting/contracts/wire/` (generated files only) | LOCAL (portal, DEV only; generated type files, no page changes) |

## Interfaces

- I11: `persist_inputs.report_index` is `null` or an object with exactly `report_id`, `revision`, `retention_ref`, `sha256`, each typed.
  The types are READ from the producer (`ops/owned_report.py`, `_custody_report_index` and the index row it returns), never chosen to
  fit a fixture. The required list and `additionalProperties: false` do not change.

## Edges and chains

- `AR-y-42` consumes `AR-y-41`'s output (the generator reads the contract): one chain, one worker's queue, `AR-y-41` first.
- M = 1 chain.

fanout: 1 of 1 chains, cap 8, reason: one chain of two cells, issued as ONE order to one slot.

## Not cut, and why

- Row D2-S34 (two functions that do not build without the skip flag): ruled to `2.0.0_SA_COO~P2` by the analysis, section 3.
- Row D2-S39 (`irpt-ycharts-generate`'s five digests): `2.0.0_SA_COO~P2`'s read-only cell, by CTO msg 4622.
- Row D2-W66-S1 (BLOCKING, the packager cannot read the ticket): workstream G's cell AR-g-32, after TCKT_VNEXT's R2-pk-2.
