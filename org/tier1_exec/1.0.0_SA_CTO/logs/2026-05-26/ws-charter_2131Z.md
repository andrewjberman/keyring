# /ws-charter cycle 0040 — NOVEL — MDPF_OWNTS PRD v0.1 ship

**Tick:** 2026-05-26T21:31Z (cycle 0040)
**Class:** NOVEL
**Author:** 1.0.0_SA_CTO
**Trigger:** [BRIEF-FOR-PRD] inbox delivery from 0.4.0_DS_ClientPlatform (broker channel push ~21:21Z) carrying Andrew sovereign direct 2026-05-26 (3 sequential asks + 2 methodology refinements during /work-cycle interrupt)

---

## Inbox-summary

1 message, `[BRIEF-FOR-PRD] MDPF ETF Ownership Tracking` from 0.4.0_DS_ClientPlatform — relaying Andrew direct sovereign ask chain for PRD authoring absorption. Brief substrate at `docs/briefs/mdpf-etf-ownership-inflection-tracking-20260526.md` (commits `12f01b4e1` initial + `d0aa4073b` methodology amendment). DS findings inline: snapshot + MTD answers delivered to Andrew; 9 open questions surfaced for CTO PRD scoping; Option A (lean chain extension) recommended by DS; 2 binding refinements (trading-day basis + prorated methodology).

Classification: ANDREW_DIRECTION (relayed via DS [BRIEF-FOR-PRD] pattern with explicit "Andrew instructed me to ... relay to you for absorption into an official PRD") → NOVEL per /ws-charter Step 4b ladder.

## Action-taken

PRD v0.1 authored + shipped. 9-question disposition:

| Q | Type | Disposition | v1 default |
|---|---|---|---|
| Q1 Option A vs B | [A] Andrew-ratification | CTO judgment defaults A; flagged for Andrew | A lean chain extension |
| Q2 Headline methodology | [A] Andrew-ratification | CTO judgment defaults (b) per DS read of "prorated"; flagged | (b) full-window-with-pre-onboard-zeros |
| Q3 Trading-day calendar | [C] CTO default | NYSE/pandas_market_calendars | Same |
| Q4 Partner scope | [C] CTO default | All current+future MDPF partners (partner-list-keyed shape) | Same |
| Q5 ETF scope | [C] CTO default | Opal 4 only | Same |
| Q6 Anomaly sentinel | [C] CTO default | Audit-only DoD flag at 1.5pp threshold | Same |
| Q7 Portal consumer | [C] CTO default | No portal v1; documented shape absorbs later binding | Same |
| Q8 Missing-day handling | [C] CTO default | Explicit null + escalate-after-2 | Same |
| Q9 Project code | [C] confirmed | MDPF_OWNTS | Same |

3-TO decomposition (preliminary; ws COO authoritative):
- MDPF_OWNTS.001 — DS author Pod 0.4 (~1d). Substrate-rich (0.4.0_DS_ClientPlatform = brief author).
- MDPF_OWNTS.002 — AE chain wire Pod 0.7 (~1d). Gates on .001 RAVC.
- MDPF_OWNTS.003 — DS RAVC live-run (~30min). Gates on .002 ship + first chain fire.

Wall ~2d sequential if both lanes have capacity. Project closes on 3-TO RAVC-accept + first live emit + reconcile-PASS.

## Commits

- `<this commit>` — PRD v0.1 (`docs/architecture/MDPF_OWNTS.md`) + project JSON (`org/projects/MDPF_OWNTS.json`) + REGISTRY row + this log

## Follow-on dependencies

1. ws COO TO authoring + dispatch for MDPF_OWNTS.001 (MCP routing this commit).
2. Q1 + Q2 Andrew ratification — MCP to Andrew via ws COO at TO dispatch; ws CVO consult-candidate per LD-0026 joint-decide if Andrew silent >1 cycle.
3. ws CVO /verify-channel coverage on first live emit (Stage 4 chain wire) — coordinate at .002 RAVC.

## Next-cycle expected state

- ws COO TO files authored + DS Pod 0.4 GO'd within next 1-2 /drive cycles (~20m cadence).
- Q1 + Q2 Andrew MCP fired from ws COO; default-proceed armed on ALWAYS-PROCEED LD-0084 backstop if Andrew silent 1 cycle.
- Next /ws-charter tick (cycle 0041, ~22:07Z per cron 7,37 schedule) likely CLEAN-SWEEP unless ws CVO surfaces a /verify-channel finding citing this PRD or Andrew direct response to Q1/Q2 arrives.

## Cycle-log file location

`org/tier1_exec/1.0.0_SA_CTO/logs/2026-05-26/ws-charter_2131Z.md` (this file).

## Commit-tag trailer

`ws-charter-cycle:0040 class:NOVEL`
