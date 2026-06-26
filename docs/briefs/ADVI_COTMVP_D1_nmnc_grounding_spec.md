# ADVI_COTMVP D1 -- COT NMNC stock/flow: GROUNDED SPEC (producer-fix premise does NOT hold)

**Author:** 0.4.0_DS_ClientPlatform, 2026-06-26. **Gate:** spec -> CTO arch-gate BEFORE implement (per PRD sequencing). **Status:** CLOSED -- CTO arch-gate ruled **Option A (GO)** 2026-06-26 (CTO 183427Z; committed to PRD 05f72c2f6). D1 producer leg STOOD DOWN (premise falsified, no producer change). The young-firm NMNC display concern folds into D3 (pod4 DE lane: relabel/suppress year-quarter NMNC when NMEC=0 / history<N). Options B/C rejected (B=fabric-wide redefinition = Andrew's separate call; C=invents a semantic). DS gold lane freed. CVO loops in for D3 served-verify.

## TL;DR
The PRD frames D1 as "COT producer NMNC mis-aggregated to a STOCK vs the 49F exemplar's convention -> fix the producer." **Grounded against source + the served 49F artifact, that premise does NOT hold:** COT's NMNC already uses the IDENTICAL convention as 49F (same shared code). COT's $401M year=quarter / NMEC=0 is the FAITHFUL output of that convention for a firm where 100% of clients onboarded in one quarter -- not a producer bug. There is no "49F exemplar convention" to align to that differs from what COT already does.

## What the NMNC metric actually IS (source-grounded)
- Served `platinum/firm/timeseries_overview.json` -> `aua.{gran}.data[].NMNC/NMEC`.
- D_04.client_portal_summary.py:1807 `build_timeseries_overview` passes `aua` THROUGH VERBATIM from `timeseries_chart.json` (D_00b).
- D_00b.portal_timeseries.py:539 `_build_static_aua_periods`: for each period, snapshot total_aua at period-end; **NMNC = sum(total_aua) of relationships whose first_seen_date is within the period** (i.e. the AUA *balance* of new-in-period clients -- a STOCK); NMEC = balance of all other (pre-existing) clients.
- This is "New Money / New Clients" = AUA contributed by clients first onboarded in the window. It is a STOCK by design, uniformly across all three grans (NOT monthly=flow as the PRD states -- monthly is the same stock, sliced to that month's new clients).

## Why COT "reads broken" but 49F doesn't -- SAME CODE, firm-age artifact (GROUNDED)
- The `_build_static_aua_periods` + D_04 pass-through code is **identical** between cot and bd/49F (data/cot vs data/black_diamond, same functions/lines).
- **49F served (s3://opal-data-bd/platinum/firm/timeseries_overview.json, data_as_of 2026-06-24):** annually-2026 NMNC=$159.26M / NMEC=$1,586.17M; quarterly-Q2 NMNC=$57.59M / NMEC=$1,687.84M; monthly-06 NMNC=$7.75M / NMEC=$1,737.68M. NMNC is a small, sensibly-nested fraction of ~$1.7B AUA -> reads fine.
- **COT served:** annually=quarterly NMNC=$401,437,408.55, NMEC=0; monthly-04 NMNC=$168,717.70. Because COT onboarded over 2026-Q2, EVERY client is "new" -> year and quarter both capture the WHOLE firm ($401M) as new-client AUA, NMEC=0 (no pre-2026 clients). Internally consistent + TRUE, just degenerate-for-a-young-firm.

## Decision (CTO/COO/Andrew -- I am NOT inventing a semantic)
- **Option A (recommended) -- no producer change; route to display:** D1-as-producer-fix is grounded-out. The "$401M new money" is factually correct for a 3-month-old firm. The "reads broken" is a young-tenant DISPLAY/labeling concern -> fold into D3 (young-tenant UX): e.g. a label/treatment for "newly-onboarded firm: all AUA is new-client" or suppress year/quarter NMNC when NMEC=0 / history < N periods. Zero risk to 49F.
- **Option B -- redefine NMNC as a period NET FLOW** (consistent with `nna` net=inflow-outflow, which the overview ALREADY carries separately): this is a real producer change BUT it changes the metric for 49F TOO (shared code) -> cross-tenant regression + 49F re-cert; contradicts the PRD's "no cross-tenant regression" principle. Only if CTO/Andrew want NMNC redefined fabric-wide.
- **Option C -- COT-only young-firm producer guard** (e.g. when NMEC=0 / history < N, relabel or null the stock-NMNC): cot-only, but it INVENTS a new semantic the PRD explicitly warns against.

## Recommendation
Option A. The producer is not mis-aggregating; the 49F "exemplar" is the same convention COT already uses. Pushing a producer fix would either change nothing meaningful or silently alter 49F's working metric. The genuine question -- "what should NMNC show for a firm where every client is new?" -- is a display + product-semantic call for CTO/Andrew, best handled in the D3 young-tenant lane, not a D1 gold re-aggregation. Requesting CTO arch-gate ruling on which option before any code.

## Compiler tools run
comp-pipescript io D_00b (consumers/column-gaps); source reads on D_00b._build_static_aua_periods + D_04.build_timeseries_overview (cot + bd); served-artifact ground on both cot + 49F timeseries_overview.json. firm-sep intact (CODE comparison only; no cross-firm bucket reference in any producer).
