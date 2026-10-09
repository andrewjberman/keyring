# RESEARCH -- consolidation targets: IRPT_DASHBD, IRPT_CUSTDY and IRPT_BCKEND's Performance workstream are one product

**archetype:** EXPLORE
**Author:** 4.0.0_SA_CRO~DELL2, 2026-10-09 (~04:3xZ to 05:0xZ)
**Ask:** Andrew-direct, in this seat's session (verbatim at the end).
**Method:** four read-only passes (one per project, plus a registry scan of all 49 tree `project.json` files; 40 not
closed). PRDs, decompositions, drain packets and code paths were read at `box/dell2` HEAD. Live AWS reads were
limited to three IRPT_DASHBD Lambdas' configuration; nothing else was invoked.

## Answer

**Yes. They are one product:** the client's performance, as a daily return series, the Reporting tab that shows it,
and the quarterly client statement that exports it.

The three projects compute overlapping numbers, read each other's gold, share one portal tab and one renderer, and
two of them have been driven by the same COO lane. The overlap has already produced **two live conflicts**
(section 2), which no single owner can settle today because each sits in two PRDs.

**Recommendation:** fold the performance numbers, the Reporting tab and the client statement into ONE project. Leave
IRPT_BCKEND as the shared platform underneath: auth, routes, directory, holdings and the export renderer (section 4).

## 1. What each one is (measured)

| | IRPT_DASHBD | IRPT_BCKEND ~P (lane ~P2) | IRPT_CUSTDY |
|---|---|---|---|
| Purpose | daily total return per account (GIPS-aligned, before advisory fees), one served series per account, the dashboard | "shared auth, routes, IaC, packaging, Performance/Reporting" (PRD :471-473); holdings-basis gold; the statement's export plumbing | Q-1: quarter-end client statements from custodian data for 49F and Cottonwood, replacing Black Diamond by 2027-01-01 |
| Return it computes | flow-adjusted daily TWR: `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` | holdings-only return: `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` ("NO INFLOW/OUTFLOW LOGIC") | period and household linking over the other two: `data/assets/scripts/gold/irpt_custody/client_report_figures.py` |
| Writes | `s3://opal-data-<firm>/irpt/<firm>/gold/account_return_daily`; `platinum/reporting/account=<id>/series.json.gz` | `.../gold/holdings_performance_{daily,manifest}` (same prefix); routes `custody-report-read/persist` on `irpt-export-render` | `address("irpt", <firm>, "gold", "client_report", ...)`; template `portal/.../render/clientreport/ClientReportDocument.tsx` |
| Portal | `tabs/reporting/ReportingTab.tsx`, `dashboard/*` | the SAME `ReportingTab.tsx` calls `/performance` | the print page for `CUSTODY_REPORT` (the Performance tab's export, CTO msg 1656) |
| Round, open TOs | 36; 2 open (b-70, b-72) | 95; 2 open (IB-pr-383, IB-pr-386) | 7; 1 open (CU-g-2a, held) |
| REALIZED FWDs | 0 clean (FWD-1 at Andrew's acceptance; FWD-8 graded both ways) | 0 (CTO table @ rounds 47-60) | 0 (FWD-1 hops 1-4 real for 18 of 18; hop 5 open) |
| Lanes | ~D2 issues now; ~P issued 24 of its 68 orders | ~P2 (formerly ~P) | ~K2 |

**How they read each other (quoted):**
- IRPT_CUSTDY PRD :137: "returns and holdings from the holdings-based gold (IRPT_DASHBD `account_return_daily` and
  IRPT_BCKEND `holdings_49f.py`)". It renders "on the IRPT_BCKEND export path (`irpt-export-render`)" (:144).
- IRPT_DASHBD PRD :139: IRPT_BCKEND's holdings gold "becomes this project's guard rail". C-SHADOW (:173): "it opens no
  second performance figure on the same page"; backlog B7 switches IRPT_BCKEND's page to this figure.
- IRPT_BCKEND v0.26 :647: "49 Financial's page serves IRPT_DASHBD's flow-adjusted total return". v0.29 :684-704: the
  statement's export is "`2.0.0_SA_COO~P2`'s cell (E-P9) ... The template is IRPT_CUSTDY's".
- The one open CUSTDY order is HELD on three IRPT_BCKEND items: release 6, ~P2's writer cell, and a service mint pair.
  ~P2's client-statement persist waits on CUSTDY E2a. **Each project waits on the other.**

## 2. The conflicts the split has produced (each needs one owner)

1. **Inflection and Cottonwood have two return owners with two methods.** IRPT_BCKEND FWD-3 (v0.26): those firms get the
   **holdings-basis** figure. IRPT_DASHBD FWD-11 (added 2026-10-09): they get "the same daily total return" as 49F. No
   record reconciles them. **Recommendation:** one method for all three firms, the flow-adjusted daily TWR (DASHBD's),
   with the holdings-only figure kept as its guard rail, which is already its role for 49F.
2. **Household return, worded two ways.** IRPT_BCKEND FWD-3: compose from holdings, "never by summing or averaging
   period returns". IRPT_CUSTDY `client_report_figures.py:41`: average member returns "weighted by their PRIOR-day
   value". Averaged daily with prior-day weights and then linked, this equals the household's aggregate daily TWR
   (inferred; the same flow convention assumed). So the two may agree in number and differ only in words. **Check
   once** on one multi-account household: both ways, rule stated before the run. Then keep one sentence.
3. **Three Black Diamond comparisons:** IRPT_DASHBD FWD-8 (tie-out), IRPT_BCKEND FWD-13 (vendor comparison) and
   IRPT_CUSTDY FWD-5 (two dated comparisons), plus ADVI_PERFRP's legacy harness. Keep ONE, DASHBD FWD-8, the furthest
   along: 8,433 of 9,078 within 0.35 pp.
4. **FWD-8 is graded both ways:** CVO REALIZED (`IRPT_DASHBD_FWD8_L9_GRADE_20261002.md:99`) vs CTO NOT REALIZED (round
   analyses 18-20). The merged project starts from one grade.

## 3. Why the split keeps stalling

- Every cross-project wait above is internal to one product.
- The served figure on the Reporting tab can switch only when both PRDs move (B7 / C-LABEL).
- The statement's hop 5 needs a CUSTDY submission and a ~P2 writer in the same release.

This is the same pattern Andrew named for the Analysis Request (IRPT_ANLREQ): no single driver can run the journey,
because no single project owns it.

## 4. The proposed shape

| Into the ONE project (performance reporting) | Stays in IRPT_BCKEND (platform) | Stays elsewhere |
|---|---|---|
| IRPT_DASHBD whole: gold, publisher, read route, dashboard, FWD-1..11 | shared auth and routes (FWD-2), directory freshness (FWD-7), holdings (~M, FWD-5) | Analysis lane ~Y2 -> IRPT_ANLREQ (already registered) |
| IRPT_BCKEND ~P's performance scope: FWD-3, FWD-12 (holdings gold as the guard rail), FWD-13 (folded into the one BD comparison), and the statement export cell E-P9 | `irpt-export-render` as the shared renderer (also serves ANLREQ) | ADVI_COTBKF: Cottonwood's Commonwealth history, consumed for CUSTDY FWD-4 |
| IRPT_CUSTDY whole: the statement's figures and per-firm templates, FWD-1..9, Black Diamond retirement per firm by 2027-01-01 | | MDPF_SECCLASS / MDPF_SECHIST: security descriptions and prices |

- **Endpoint (the CUSTDY framing, the broadest):** each firm's clients see Opal's performance on the Reporting tab and
  receive Opal's quarterly statement, with Black Diamond switched off per firm.
- **First outcome:** one 49F account's Reporting tab and its 2026-09-30 statement, both from the same
  `account_return_daily` series, one trace.
- **Drivers:**
  - ONE COO issuer for the merged project; ~P2 keeps the platform remainder of IRPT_BCKEND.
  - One CloudOps applier.
  - The no-stop rule (park a cross-box wait with its owner, move to the next hop) as written for IRPT_ANLREQ.
- **Code:** for the CTO at L3 (for example `IRPT_PERFRP`, or re-scope IRPT_DASHBD as the survivor, since it holds the
  most of the product).

## 5. Other candidates from the registry scan (ranked, weaker)

1. **LGIC_BLANKFIX into LGIC_ENFORCE.** BLANKFIX exists only to finish ENFORCE's FWD-5, "the one outcome of seven not
   realized". Fold it back. LGIC_NAMING reads `complete`, not `closed` (a registry fix).
2. **MDPF_DEMQUE vs MDPF_SECHIST: a price-backfill ownership collision.** DEMQUE "absorbs the Yahoo price backfill";
   the CTO ruling of 2026-10-08 (msg 1466) put the Yahoo backfill in MDPF_SECHIST's C-PULL addendum, citing
   `RESEARCH_20261008_COTTONWOOD_YAHOO_PRICE_BACKFILL_STRUCTURE.md`. One owner should be named before either builds.
3. **NFRA_OPALAI and NFRA_MCPMSP:** both are Teams-facing analyst agents over the Opal MCP; MCPMSP (the partner-firm
   version) has been PARKED since 2026-10-01. Moderate: fold MCPMSP in as a later outcome of OPALAI, or close it.
4. **Registry hygiene, not merges:** NFRA_OPSEC202609 reads `active` with `dep=CLOSED`; ADVI_PERFRP is still `active`
   in the legacy `org/projects/` registry with no tree folder.

## 6. What needs a word

- **Andrew:** the consolidation itself, and the one return method for Inflection and Cottonwood (2.1).
- **CTO (L3):** the code, the registration, the superseded rows (IRPT_DASHBD and IRPT_CUSTDY closed as superseded, or
  re-scoped), and the single FWD-8 grade.

## Limits

- No deployed-byte comparison beyond the three DASHBD Lambdas.
- I did not check whether `/performance` and `/reporting` both render on PROD today.
- The household check (2.2) is inferred, not run.
- Grades after 2026-10-07 were taken from drain packets.

## Andrew-direct request -- verbatim record

Channel: this seat's dell2 terminal, in-session, 2026-10-09 ~04:2xZ.

> I want you to take a look at a few projects that seem like consolidation targets. For example, DSHBRD, CUSTDY and
> IRPT WORKSTREAM ~P, all seem focused around really the same thing.
