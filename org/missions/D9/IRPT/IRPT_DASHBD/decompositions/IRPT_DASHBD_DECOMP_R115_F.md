# IRPT_DASHBD round 115 -- workstream ~F2 decomposition (F-SHIP: the export mount of the filled report)

Issuer `2.0.0_SA_COO~F2`, 2026-10-15 ~04:1xZ. Gate key: `<round>115</round><workstream>~F2</workstream>`.

**Answers:** the CTO's analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_114_20261015.md` @adf3e0d808
(msg 8022), which answers `3.0.0_SA_CVO~IRPT`'s slug `ADJUDICATION_v74.md` @71e6255e69 (3 of 3 PASS, MAY-CLOSE). Its one cell: the export mount in F-SHIP's
`export/` folder, against the export source kind of the signed IB-pr-551 packet (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~395/SERVE_PATH_PAIR_PACKET_V1.md`,
hop 4), tests on an injected answer, on the tab's portal branch, not pushed, inert until the route serves.

## What was measured at the cut

- The tab's branch is `cand/dell2/irpt-default-performance-report` @d3c379663faceca7f4907366e0943d2b19022b6e (the 20 report commits plus round 114's 3).
- The packet says the filled-report source kind "pins the filled object by its VersionId and sha256 and is frozen by the submit the way the PATH B platinum series is frozen"
  and names no wire field. PATH B today: the page sends `performance_source: {path: 'PLATINUM', account_id, start, end}` and never a version, sha256 or as_of; the server pins them
  at submit (`export/submit.ts` `PerformanceSource`; `export/ExportButton.tsx` line 236). The print query carries `account` and the frozen `version`
  (`render/PrintEntry.tsx` lines 214-217, 292). The bundle resolver (`export/resolveBundle.ts`) reads PATH B and puts it on the bundle (`dashboardPerformance`).
- **Decision (a): the wire names are a PROPOSAL that mirrors PATH B**: `performance_source: {path: 'FILLED_REPORT', client_id}` at submit, and a print query naming
  `client` and `version`. They live in ONE small file (`export/filledReportSource.ts`) so that packet v2 or slice IB-pr-551c changes them in one place; the CTO's analysis says a
  changed ENDPOINT-visible byte follows by an issuer amendment, not a new round.
- The print route and the render host are hop 5, windowed and not released by the pair; this cell builds the portal half of the print (the entry reads the report by client and
  version and renders `PerformanceReportDocument`), and nothing prints until hop 5 is up.

## Cell

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| The EXPORT MOUNT: `export/filledReportSource.ts` (the source named at submit, one place); `submit.ts` carries it beside PATH B's; `ExportButton` takes `clientId` and submits the filled-report source when it is set; `Preview` and `resolveBundle` read the report through round 114's `readReportAnswer` (the live object for the preview, the frozen `version` for a print) and put it on the bundle as `filledReport`, never a retained report; `ReportingTab` emits an export target carrying the client for a served report (`buildFilledReportExportTarget`); `PrintEntry` reads `client` and `version` and the render renders the report through `PerformanceReportDocument`; `reportRead.ts` takes a version (`version_id`). Not served or fixture adapter: every existing path exactly as before | `DB-f-503` | FWD-21 | LOCAL (portal branch only, never pushed; no route serves a report, so nothing changes for anyone) | none | R115-F-A |

**Decisions inside this decomposition (the issuer's, stated):**
(a) the wire names above are a proposal, in one file; (b) `index.tsx` is not in this workstream's write surface: the one hookup it needs (passing the target's `clientId` to `ExportButton`) is the issuer's,
added at the merge in one commit with the order's report naming it (dispatch Step 5), never by the worker; (c) `ExportBundle.ts` (the wire type of the server's authorized revisions) is not edited: the server's
echo of the new source kind is slice IB-pr-551c's; (d) a client's report is the same object for the tab, the preview and the print; the preview reads the live object and a print reads the version the submit
froze, as the series does; (e) the cell is one order because the five edit sites share one bundle type; it carries three mechanical criteria (the export side, the print side, the bounds).

**Four-postulate record.** (i) Domain: `export/`, `render/`, `tabs/reporting/ReportingTab.tsx`, `dashboard/report/reportRead.ts` and two new test files, under `InvestorReporting/`. (ii) Same grain: one client's report.
(iii) One intent: an export of a served report carries and prints that report. (iv) Not moved: every PATH A and PATH B read and request when no report is served; the contract; the tab's body; `index.tsx`; `ExportBundle.ts`;
every route and every served file.

**Chain read.** M = 1. N = 1.

fanout: 1 of 1 chains, cap 8, portal_ref: `cand/dell2/irpt-default-performance-report` (d3c379663faceca7f4907366e0943d2b19022b6e), reason: one cell with a single write set (the shared bundle type makes the five sites one chain). Worker `0.9.0_WK_IRPT_DASHBD~503` (`DB-f-503`).

| criterion | invocation | base reading |
|---|---|---|
| DBF115-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r115/p115_export.py . DBF115-1-AC1` | FAIL (no file) |
| DBF115-1-AC2 | `... p115_export.py . DBF115-1-AC2` | FAIL (no reader file at the base tree) |
| DBF115-1-AC3 | `... p115_export.py . DBF115-1-AC3` | FAIL (no change from the round-114 head) |
