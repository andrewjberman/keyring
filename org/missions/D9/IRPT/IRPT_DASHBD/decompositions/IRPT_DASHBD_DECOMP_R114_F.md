# IRPT_DASHBD round 114 -- workstream ~F2 decomposition (F-SHIP: the default performance report reaches the Performance tab and the export)

Issuer `2.0.0_SA_COO~F2`, 2026-10-15 ~01:3xZ. Seated by `1.0.0_SA_CTO~DELL2`'s ruling
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` @a6d9baacaf (Andrew, "Go on").
Gate key: `<round>114</round><workstream>~F2</workstream>` (GATE (x), per-workstream rounds). Workstream B (`~D2`) is still in round 113; the
two issue disjointly. Worker slots for this workstream are numbered from 501 so they cannot collide with `~D2`'s sequential slots.

**No CTO analysis answers this workstream yet** (the CTO's first analysis here follows this workstream's first slug). The cells below are cut
on the ruling's write surface and the CRO's assessment (`org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_DASHBD_PARALLELIZATION_ASSESSMENT_20261014.md`
section 4, row F-SHIP), and on what this seat measured at the cut.

## What was measured (the cut's ground)

- The default performance report is built and graded: 20 commits (18 new files, 4,291 lines) on the local branch `wk-IRPT_DASHBD-180-portal`
  @c81d54ff31b0c44b45dabdd217b531a183723c8b, a chain on `origin/PROD` @5d646418 (`git rev-list origin/PROD..` reads 20). The CVO passed the 49 Financial
  report in round 107 (6 of 6) except the disclosure page, which waits on call a252.
- **Nothing mounts it.** On that branch no file outside `__tests__` imports `PerformanceReport` or `PerformanceReportDocument`: the tab and the export
  still render the older body. Every render so far came from a private sample built by a script (`build_sample.py`), never from a served file.
- **No route serves a filled report.** `comp-find` for `reporting/.../manifest` over `lib/research/api` reads 0 hits in 132 files, and the only
  `filled_report` sources are the sample builders and the contract. The served read route that exists (`irpt-reporting-read`, IRPT_BCKEND `~P2`)
  serves a per-account `manifest` and `series` and a per-client `summary`.
- Both existing IRPT candidates (`cand/dell2/asof-date-only-no-invented-clock`, `cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal`) are
  APPROVED by Andrew (open-calls approval-status, read 01:2xZ). This workstream's branch is a third, separate feature.

## Cells

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. The REPORT READER and the TAB MOUNT: `dashboard/report/reportRead.ts` (the one fetch of a client's filled report through a route that mirrors the summary route, `GET /api/scoped/investor-reporting/reporting/client/{client_id}/report`, read as `served` or `absent`, never partial; a body that does not conform to `FilledReport` is `absent`), and the Performance tab shows `PerformanceReport` in place of its body when the report is served for the selected client; every other state (absent, a fixture adapter, a different client) keeps the tab exactly as it is | `DB-f-501` | FWD-21 | LOCAL (portal branch only, never pushed; the route does not exist yet, so the live tab changes for no one) | none | R114-F-A |
| 2. The SERVE-PATH READ: what serves a filled report from gold to the browser today (the read route, the platinum publisher, any report object, the export render path), the hops still missing with an owner and a risk class each, and the proposed route | `DB-f-502` | FWD-21 | LOCAL (a read; nothing written) | none | R114-F-B |

**Decisions inside this decomposition (the issuer's, stated):**
(a) The route is a PROPOSAL, named in the reader only; the reader is one function, so a different route is a one-line change. The contract writer
(`~D2`) and the route owner (`~P2`) are told by the read's record (cell 2), not by a message, and the route is theirs to accept or rename.
(b) The mount lands INERT: with no served report the tab is byte-for-byte as it is, so the branch is safe to approve and merge before the route
exists; the CTO and Andrew see a real page only when a route serves a report (a later round).
(c) The EXPORT mount is not cut this round: the export is rendered by a server host from a frozen series version (`performance_source`, IB-pr-301),
so how it can render a filled report is cell 2's question; cutting it before the read would be a guess.
(d) The cand branch itself (`cand/dell2/irpt-default-performance-report`, cut from `origin/PROD`, carrying the 20 commits plus this round's
commits, registered as a client-facing approval row) is the issuer's own act after the round drains (the decomposition of round 94 placed it
there), and waits on Andrew's approval after that; nothing is registered this round.
(e) Filled-report ownership stays as the ruling says: the reader reads the filled document and never builds one; the builder and the contract stay
with `~D2`.

**Four-postulate record.** (i) Domain: the portal write surface of the ruling (`dashboard/report/`, `tabs/reporting/`, and the tests of
`__tests__/irpt-dashbd/`), nothing else. (ii) Same grain: one client's report. (iii) One intent: a served report reaches the tab. (iv) What this
round does not move: the export, the contract, the builder, every route, every served file, `dashboard/*.ts` outside `dashboard/report/`.

**Chain read.** M = 2 (the cells share no file and no data edge). N = 2.

fanout: 2 of 2 chains, cap 8, portal_ref: `wk-IRPT_DASHBD-180-portal` (c81d54ff31b0c44b45dabdd217b531a183723c8b) for slot ~501, none for ~502, reason: the reader and the read are independent with disjoint write sets (the portal files of cell 1; the read record of cell 2). Workers `0.9.0_WK_IRPT_DASHBD~501` (`DB-f-501`) and `~502` (`DB-f-502`).

| criterion | invocation | base reading |
|---|---|---|
| DBF114-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r114/p114_ship.py . DBF114-1-AC1` | FAIL (no file) |
| DBF114-1-AC2 | `... p114_ship.py . DBF114-1-AC2` | FAIL (tab lacks the mount) |
| DBF114-2-AC1 | `... p114_ship.py . DBF114-2-AC1` | FAIL (no record) |
