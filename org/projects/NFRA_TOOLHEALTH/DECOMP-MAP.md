# NFRA_TOOLHEALTH -- DECOMP-MAP (COO~B, 2026-07-02)

**Charter:** MSTR DECOMP-GO (Andrew-greenlit 2026-07-02, LD-0239). PRD `docs/architecture/NFRA_TOOLHEALTH_PRD.md`.
**Shape (locked, do NOT re-litigate):** FOLLOW-ON project depending on the COMPLETED NFRA_COMPLEARN + the in-flight NFRA_COMPPROOF. **REUSE the shipped substrate UN-FORKED** (tool_activity catalog P0-LIVE + `comp_learns_score.py` value-anchored scorer + the worklist stay COMPLEARN-owned); do NOT reopen COMPLEARN's clean 2026-07-01 closure. Read/observability -> decompose FREELY, no governance gate.
**Lane:** COO~B (NFRA_COMP* program coordination).

## The 3 genuinely-new deliverables (per MSTR + PRD SS0)
- (a) The **EFFECTIVE axis** -- fold COMPPROOF's blind-run REACH x USABILITY in as a RECURRING per-tool/per-class effectiveness probe (log-mining alone can't tell you a tool actually *reaches* the answer).
- (b) The **single per-tool 3-axis HEALTH QUERY** -- one query returns, per tool, USED x RAIL-CONSISTENT x EFFECTIVE -> a verdict + action.
- (c) **Close-the-inert-loop as an ACCEPTANCE gate** -- make the fused view DRIVE fix/promote/retire (not merely display), cross-checked by COMPPROOF-D1's autonomy audit.

## The action taxonomy (PRD SS3 -- the FIX row is load-bearing)
| USED | RAIL-CONSISTENT | EFFECTIVE | -> Action |
|---|---|---|---|
| yes | yes | yes | KEEP |
| yes | yes | **no** | **FIX** (used + reached-for but doesn't reach the answer -- only the EFFECTIVE probe surfaces it) |
| no | -- | yes | PROMOTE / surface (effective but ignored -> feeds COMPROUTE) |
| no | -- | no/unknown | RETIRE (dead) |

## TO legs (all -> 0.8.0_AE_CloudComp fleet, except TH-V -> CVO)

| TO | Title | Owner | Gate (blockedBy) | Cross-domain nodes |
|---|---|---|---|---|
| **TH-A** | EFFECTIVE-axis recurring per-tool probe (extends COMPPROOF-B1 blind-run from per-incident to per-tool) | 0.8.0_AE_CloudComp | **COMPPROOF-B1 harness** (`NFRA_COMPPROOF.B1`, blind-run REACHxUSABILITY, same fleet) + isolation gate | COMPPROOF-B1 harness; tool_activity substrate (write a new probe stream) |
| **TH-B** | Fused per-tool 3-axis HEALTH QUERY + action taxonomy | 0.8.0_AE_CloudComp | 2 live axes (USED/RAIL) runnable NOW on COMPLEARN substrate; full 4-verdict needs **TH-A** EFFECTIVE feed | tool_activity (read); comp-which-rail.log; comproute-routing.jsonl; comp_learns_score.py (read, un-forked) |
| **TH-C** | Close-the-loop acceptance gate (verdict DRIVES fix/promote/retire) | 0.8.0_AE_CloudComp | **TH-A + TH-B** + **COMPPROOF-D1** autonomy cross-check | COMPLEARN worklist (consume side); CTO commission path; COMPROUTE (PROMOTE verdicts); COMPPROOF-D1 |
| **TH-V** | Independent CVO honesty verification | 3.0.0_SA_CVO | **TH-A + TH-B + TH-C** | scorer honesty; EFFECTIVE-verdict isolation; FIX/RETIRE reproduction on LIVE |

## Cross-domain resource flags (wave protocol)
- **tool_activity substrate** appears in TH-A (writes a probe stream), TH-B (reads), AND cross-PROJECT in NFRA_AGENTBUS (app-layer meter writes cross-employee rows). This is the shared query surface -- **any schema change to tool_activity is a 2-project coordination event** (TOOLHEALTH + AGENTBUS) and stays COMPLEARN-owned (do not fork). Flagged in TH-A + AGENTBUS-S3 `<cross_domain_coordination>`.
- **COMPPROOF-B1 harness** is shared: it is B1's deliverable AND TH-A's input. Same fleet (0.8.0_AE_CloudComp) -> coordinate the per-incident-vs-per-tool generalization inside the fleet; do NOT fork the harness (one home `org/modules/graph/compproof/`).
- **comp_learns_score.py** is read-only-reused by TH-B; the value-anchored honesty gate (COMPLEARN SS5) is inherited un-modified.

## Arch-gates carried in EVERY TO (PRD SS5)
1. Value-anchored honesty (score on VALUE not usage-count -- no Goodhart).
2. EFFECTIVE-probe honesty (REACH x USABILITY + blind-solver isolation author!=solver!=judge; CVO-verified).
3. Advisory, not auto-mutating (CTO ratifies retire/fix/promote).
4. Ground on LIVE logs/Trino + actual probe results (Rule 22).

## Sequencing summary
- **Runnable near-term (2 live axes):** TH-B skeleton over USED (tool_activity, COMPLEARN P0-LIVE) + RAIL-CONSISTENT (comp-which-rail.log) -- KEEP/RETIRE-partial verdicts possible NOW.
- **Gated on COMPPROOF-B1:** TH-A (the EFFECTIVE feed) -> completes the 4-verdict taxonomy (FIX/PROMOTE become distinguishable).
- **Gated on TH-A+B + COMPPROOF-D1:** TH-C (close-loop) -> TH-V (CVO accept).
- **Dispatch:** all staged. GO fires per-leg when (i) the 0.8.0_AE_CloudComp fleet is live (currently OFFLINE -- fabric is on the ETL P0; spawn-request to MSTR when the wave is greenlit to run), and (ii) the named gate clears.
