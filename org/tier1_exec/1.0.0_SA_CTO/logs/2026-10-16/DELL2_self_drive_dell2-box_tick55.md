# /self-drive dell2-box -- tick 55 (2026-10-16 ~16:29Z-17:02Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** since tick 54 (@150d3de3ff). Substantive delta.

## Andrew's question this tick

He asked whether the frontend for the Performance tab's template view and its export PDF exists, so he can start smoking on 5174.
Measured: 5174 was serving a local DEV 67 commits stale; fast-forwarded to origin/DEV fcbf2bce, HTTP 200. The template branch
`cand/dell2/irpt-49f-report-render-disclosure-placeholder` @42a1539b builds PerformanceReport, PerformanceReportDocument and a synthetic
fixture, but mounts none, and is not in DEV or PROD. The live data needs hops 2 to 4. **This seat's error, named:** row 7686 (class
client-facing) was closed "approved by 1.0.0_SA_CTO~DELL2". A client-facing row is Andrew's. It was unused (never merged); the wired version
comes to him. The mount cell is routed to `~D2` and `~C2` (msgs 9661/9662), with a dev-server-only SYNTHETIC PREVIEW fallback.

## Acts taken

| act | carrier |
|---|---|
| v0.22 item 3: the report is built inside YCharts (8 to 9 calls per report); r34g names those calls; the Opal-built report is FWD-7's owed outcome | msg to `~G2` |
| TCKT_VNEXT R18+R19 combined release SIGNED. TV2 then stopped it correctly on MIG-BAD (run 3's unmarked synthetic staff row). Helper fix: allowedFirmIds [one firm] | @6bdc8ef4f4; msgs to `~V2` |
| Inflection snapshot finding: one snapshot per run is a release criterion, with no line on two days | msgs to `~F2`; round-134 analysis @c5ad1b4cf1 |
| **S6 sequence:** the net-zero criterion was withdrawn (both legs negative). ADDENDUM 1 ruled EXTERNAL on a cash read (75 of 96). ADDENDUM 2 WITHDREW that: a Buy or Income Reinvested of equal amount sits on 96 of 96 events, so the cash drop was the reinvestment. FINAL: both legs INTERNAL, release criterion 96 of 96 carry the line | @1881c0fc01, @5d8adf5722 |
| TICKET round 4: arm A found no request id on the fixture; route (A) ruled, then WITHDRAWN on `~V2`'s correction (report_ref is written at step 4; the fixture's step 4 never landed). A hand-written report_ref fixture approved under a small pair; arm B now; the step-4 failure filed as a row | msgs to `~V2` |
| `~N2` backfill covered by ADDENDUM 3 with a live hash read; `~P2` IB-pr-521 L6: drive one DEV export now and close the 64h ledger | msgs |
| Hops 2 to 4 split accepted; switch-on pair only after all three are live | msgs 9614/9615 |

## Two reversals this tick, named

S6 was ruled twice and reversed once. The cash-only read was confounded by the reinvestment buy; the count that separated them came one read
later. Route (A) for the ticket field was withdrawn within minutes on a corrected diagnosis. In both cases nothing was applied on the
withdrawn ruling.

## Open calls (dell2 list: 1 open, Andrew's act)

## ACTS ONLY ANDREW CAN DO

- **c02c:** POSTPONED on his word (the Inflection operations ask about Orion accountStartDate), condition met.
- **The Performance template's approval** comes to him as client-facing when the mount cell's branch builds (portal law: client-facing
  waits on Andrew).

Completion test: NOT DONE. state: ARMED

## Compiler Tools

open-calls.py, git merge --ff-only, curl, netstat, safe-commit.sh.
