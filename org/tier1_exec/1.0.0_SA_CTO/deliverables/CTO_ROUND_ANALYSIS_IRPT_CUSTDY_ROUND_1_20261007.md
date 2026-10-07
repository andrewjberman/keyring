# IRPT_CUSTDY -- ROUND ANALYSIS, round 1 (the FWD-1 thread over six hops)

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~09:0xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES. This answers `3.0.0_SA_CVO`'s slug (msg 211):
REMEDIATION_v1 @648dd308a6. 6 rows: 3 dismissed, 3 OPEN (S3, W1-S1, W4-S1), 0 ARMED. Order census: 4 of 4 terminal
(CU-a-1..a-4), each drained (`737839f762`, `06a44e56bd`, `9dd85cec00`, `36c37ef88d`) with its proof VALID. PRD v0.3 @1aa8fb7a0c.

## 1. Outcome state -- 0 of 9 REALIZED

FWD-1 is NOT LIVE. Round 1 built every hop, but two hops do not run end to end on real data:
- hop 1: the real advisor pick crashes (S3);
- hop 5: the export render cannot take a client report (W4-S1).

FWD-2 to FWD-9 are enrichment and were not attempted. The since-inception windows of hop 3 wait under the laptop CTO's HOLD A
(nothing dated before 2024 through `lib/trading_calendar.py` on dell2 until the kit carries the calendar package; NFRA_CTLPLN v0.14
C-KIT-PYTHON).

## 2. Rulings on the open rows

| row | ruling | carrier |
|---|---|---|
| W1-S1 (BLOCKING) | **DONE in the PRD.** Hop 1 and S01 now name the firm advisor-ownership map (v0.3 @1aa8fb7a0c). The map's naming-registry row is added only for a builder refusal (laptop decision 106087). `~K2` sends the `address()` refusal line and the key spec through `0.0.0_AB_MSTR~DELL2`; laptop `3.0.0_SA_CVO` reads the fresh map and delivers it as a FILE | msgs 192, 213 |
| W4-S1 | **RULED (a)**, on `4.0.0_SA_CRO~DELL2`'s research `org/tier1_exec/4.0.0_SA_CRO/deliverables/CRO_RESEARCH_IRPT_CUSTDY_RENDER_FORK_20261007.md` @14fe71e545. IRPT_BCKEND's export lane (`2.0.0_SA_COO~P2`) adds a client-report kind to the export contract (a1 resolve and freeze, a2 read grant, a3 host dispatch, a4 portal print kind), following the three-cell ANALYSIS precedent (IB-pr-281, 291, 296). IRPT_CUSTDY writes only the template (a5, C-TEMPLATE). (b) is refused: it would need a new Andrew word to start the host for another purpose, it duplicates the render authorization, and it sits near the duplicate-output-path veto | this file; msg to `~P2` |
| S3 (BLOCKING) | Round 2's first item, as the issuer proposed. The CVO's compile narrows the cause: the refused raw key is the literal string `'None'`, so part of the 482 may be a null stringified upstream rather than a missing key. The fix finds where the string is made; it does not just count it | E1 |

**Hazards carried from the research (section 4):**
1. `render_export.cjs:240` renders any template name not starting with "analysis" as PERFORMANCE. A client-report name sent
   before a3 lands would be mis-rendered silently. It must refuse an unknown name. This is IRPT_BCKEND's (`~P2`), and it lands
   with or before a3.
2. The render host is the YCharts runner, and IRPT_YCDGEN FWD-11 / S28 removes the "YCharts producer". **RULED:** S28 removes
   the YCharts producer code and its session, not the host, its browser or its node modules, because every export render
   depends on them. This is recorded in IRPT_YCDGEN's manifest at the next PRD edit and sent to `~G2` now.

## 3. The ENRICHMENT LIST -- round 2, ONE issuance by `2.0.0_SA_COO~K2` (each item at most three mechanical criteria)

| # | item (FWD / rows) | criteria | risk |
|---|---|---|---|
| E1 | **The advisor pick runs on live data** (S3; FWD-1 hop 1) | (1) the source of the literal `'None'` key is named with a file:line and fixed there; (2) on the delivered ownership map, the pick for the chosen advisor completes, and each account it cannot project is counted as uncovered with its reason, never raised; (3) the count of uncovered accounts is printed beside the 7,022 denominator | LOCAL |
| E2 | **The chosen advisor, by census** (FWD-1) | (1) the census of 49 Financial advisors by household count is printed (advisors scanned, households each); (2) the pick is the fewest households among advisors with 10 or more, every account with Schwab rows at 2026-09-30 (ruling of 08:02Z); (3) the pick and its census are recorded in the decomposition | LOCAL |
| E3 | **The 49 Financial client-report template** (FWD-1 hop 5, FWD-3; a5) | (1) a `ClientReportDocument` for 49 Financial renders hop 3 and hop 4's figures for one client from a fixture of the real shape; (2) it is built from the custodian-shaped model, with no field named after a Black Diamond field (C-SHAPE); (3) the page lane's typecheck and the template's test pass | LOCAL |
| E4 | **Hop 3 on 2024 onward** (FWD-1) | (1) QTD, YTD and 1Y for the chosen advisor's accounts are computed for the 2026-09-30 quarter; (2) SI is reported as "held: calendar fix pending" for any account whose inception is before 2024, never computed on dell2 under HOLD A; (3) each figure names its source rows | LOCAL |

Chains: E1 then E2; E3 and E4 are independent. Fan-out 3.

**Not this round (named so they are not lost):**
- The served render of hop 5 waits on IRPT_BCKEND a1 to a4 (`~P2`).
- The advisor read (hop 6) waits on hop 5 and is Andrew's act (egress off Opal infrastructure: the reports go to an outside
  person).
- The pre-2024 SI windows wait on the calendar fix.

## 4. Acts only Andrew can do (this project)

- Putting the round's reports in front of the chosen advisor (hop 6). Citation: CLAUDE.md Agent Autonomy, "Excluded: all egress
  off Opal infrastructure", and C-TEMPLATE, "nothing reaches a client without his word". Listed when hop 5 serves.

-- 1.0.0_SA_CTO~DELL2
