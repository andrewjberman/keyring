# /self-drive dell2-box -- tick 59 (2026-10-16 ~18:28Z-18:58Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** since tick 58 (@5d87243d34). Substantive delta.

## Andrew this tick (his smoke of the Performance tab on 5174)

His words: *"I have not seen a change on this page in days."* Four screenshots; then *"beginning value should come prior to ending value,
they should also have dollar amounts and commas"*; then *"ping me when it is on 5174 ready to smoke"*.
**Measured root cause:** at Global the page sends no `selected_tenant`, so every firm-bound served read is refused
(`ReportingTab.tsx:450-452`, `_authz/served.py:535`). Cottonwood and 49 Financial show nothing, Inflection shows PATH A under the firm
banner, and the template view renders nothing. `~C2`'s trace confirms it for BEYER ****9943: published (6,954 accounts; 257 days, history
FULL), refused only at Global. Ruled @d22e05dd68: Global resolves per client, the banner removed, an advisor's Firm control locked, no silent
template, proof on three named clients, a visuals panel list first. His formatting ask and the template carried into the print window are
added to DB-b-309.

## Acts taken

| act | carrier |
|---|---|
| Ruling: the Performance tab from Andrew's smoke | @d22e05dd68; msgs 9747/9748, 9754/9755 |
| DB-b-309 proof: the cell's tests plus IB2 read-only direct invokes for the three clients; the browser walk is Andrew's 5174 smoke | msg to `~D2` |
| DB-b-307 pushed @1779d676 (AC1-AC3 PASS); the 5174 smoke copy moved to it. Andrew is pinged only when DB-b-309 lands | smoke worktree |
| YCharts budget (6 calls, 390 s) as a floor, counted per securities_info CALL (the CRO's read); an unknown-symbol paced read after window 4 | msgs to `~G2` |
| TCKT_VNEXT R18_RUN AMENDMENT 2 SIGNED (FWD-11 meeting run now). FWD-10 = (c), a never-pushed local scratch build; Andrew's hide intact on DEV and PROD | @510daa4f60 |

## Open calls (dell2 list: 1 open, Andrew's act)

## ACTS ONLY ANDREW CAN DO

- **c02c:** POSTPONED on his word (the Inflection operations ask about Orion accountStartDate), condition met.
- **The Performance tab's approval** as client-facing, after he smokes DB-b-309 on 5174 (portal law: client-facing waits on Andrew).

Completion test: NOT DONE. state: ARMED

## Compiler Tools

Grep (portal src), Read, git worktree, curl, safe-commit.sh.
