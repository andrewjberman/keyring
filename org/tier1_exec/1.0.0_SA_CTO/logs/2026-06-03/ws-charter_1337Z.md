# ws-charter cycle — 2026-06-03 1337Z

**CLASS:** FIX (promote-orchestration / bundle-tracking)
**Trigger:** DRIVE_ESCALATION from 2.0.0_SA_COO (20260603T133630Z) — new portal DEV change to fold into next promote + status update.

## Inbox

- **[DRIVE] ws COO** — portal DEV change `548c9d7d` (Model Portfolios source-attribution firm-scoping, Andrew-direct 2026-06-03). Asks: (1) fold into next DEV->PROD promote; (2) add visual-smoke scope. Plus status update: Andrew smoke-passed INFPRM -> COO flipped `ADVI_INFPRM status=complete` (bbb9f4355); edge-untier Distribution cross-advisor drill carved out as CTO/AE fast-follow (graceful-placeholder by-design, preserved). INFOTD/INFNNA still awaiting Andrew smoke on live v2.1.112.

## Verification (verify-channel discipline)

- `548c9d7d` confirmed on `origin/DEV`; it is the **sole** commit `origin/PROD..origin/DEV` (i.e. the entire DEV-ahead-of-PROD delta).
- Subject: `fix(ModelPortfolios): firm-scope source attribution — Inflection -> Orion, 49F -> SmartX (Andrew-direct 2026-06-03)`. FE-only (`src/pages/ModelPortfolios.tsx`, two footnote sites ~1174 + ~1646), derived off `effectiveFirmId` (firm-scoped via MDPF_SCOPED.S5). Reported tsc-clean + VALGATE D-1 PASS (no adapter files).
- Portal main tree on `DEV` (Rule 19 compliant).

## Next-promote bundle manifest (CTO-tracked)

Current PROD = portal-v2.1.112 (6549038c). Next DEV->PROD promote bundle:

| Commit | Change | Class | Smoke-scope add |
|---|---|---|---|
| 548c9d7d | Model Portfolios source attribution firm-scoping | FE-only, Andrew-direct | Inflection Model Portfolios footnote == "Source: Orion Portfolio Solutions." AND 49F/default footnote == "Source: SMArtX Advisory Solutions." (unchanged) |

**Promote trigger (HELD):** promote is gated on Andrew GO (HARD-BLOCK #6 — tag create+push via `.tools/portal-promote.sh` under Andrew direction). It naturally rides the next promote, which is itself pending Andrew's INFOTD/INFNNA smoke confirm on the already-live v2.1.112. Held; not auto-fired.

## Frontier state

- **ADVI_INFPRM:** COMPLETE (Andrew smoke-pass, bbb9f4355). Edge-untier Distribution cross-advisor drill = CTO/AE fast-follow, preserved (graceful-placeholder by-design).
- **ADVI_INFOTD / ADVI_INFNNA:** PROD-live in v2.1.112, awaiting Andrew smoke confirm.
- **SERVED-PROD e2e CVO convene:** CVO-GO-confirmed; INFPRM leg now Andrew-confirmed. Remaining gate = Andrew INFOTD/INFNNA smoke.
- **Next promote:** 548c9d7d staged, smoke-scope captured, HELD for Andrew GO.

## Follow-on

- ACK to COO: 548c9d7d verified + tracked for next promote bundle, smoke-scope recorded.
- Surface to Andrew: 548c9d7d promote-ready; will bundle with next promote (pending his INFOTD/INFNNA smoke).
- Next cron tick: re-check for Andrew INFOTD/INFNNA smoke confirm or promote GO.
