# /drive tick 12 — site-Z D-family scope — 2.0.0_SA_COO~Z — 2026-08-20 16:41Z (cron ebf739a0)

**Authority/carrier:** Andrew-direct @2b3b2eaeaa; XXX.md COO row @e2c8e55dab. Scope: D6/D7/D8/D9 (SITEZ rows; LD-0428).

## Measurements (denominators printed)
- Marker frame 16:33:15Z. Telemetry 20,186 rows; since tick: CVO~Z 17 (0.7m — ACTIVE, post-read wrap), COO~Z 6, MSTR~Z 5, CTO~Z 4, OpalETL~Z 0 (10.0m — IDLE-EVENT-DRIVEN as declared, every wait named with an owner), BG 0 (event-idle 29.5m), DE~Z 0 (reaped, tail aging out).
- Census: 5 broker-live + BG event-idle = the correct shape.
- Commits since: @c51ee71ca9 (the CVO~Z second read — 5/5 STAND, zero amendments, pushed by MSTR~Z).
- `deploy_ledger check --red`: 1/1 sentinel, the out-of-scope freshguard standing state. No RED.
- **Stale-summary note (watched, not acted):** CVO~Z's 16:40 broker summary still lists "F8 fence build (AE~Z)" and "ATOM_LAYER0 re-send (MSTR~Z)" as waits — both were resolved 16:37–16:38 (F8 landed+CLOSED, state-sync 2548; ATOM_LAYER0 delivered 163803Z). The seat is ACTIVE (17 rows) with both messages pushed to its inbox; a broker summary is aspirational and one stale line convicts nothing. **If the stale waits survive tick 13, nudge.**

## Classification + action
| Project | Class | Owner | Last-touch | Action |
|---|---|---|---|---|
| D6 | CLOSED + DECLARED; residuals = the F8 second read (CVO~Z, finding-channel; state-sync delivered) + scope-token item (CRO) | CVO~Z / CRO | 16:40Z | none; stale-summary watch item above |
| D7 residuals | TO-AC ruling-held · TO-D laptop · TAC dependency-held (deps at CTO~Z/Andrew, re-grounded tick 11) | named owners | — | none |
| D8 / D9 | COMPLETE / OFF-DEVICE | — | — | none |

**Dispatches:** 0 — nothing blocked; the one anomaly (CVO~Z's stale waits list) is a summary-vs-inbox lag on an ACTIVE seat, held to the two-signal rule. **Hard gate:** no COO-resolvable gate unresolved; the TAC hold re-grounded last tick, unchanged since. **/allocation:** every worker with live work is producing; the idle seats are idle by declared design.
**Compiler tools:** get_live_agents; telemetry read (python, denominator 20,186, frame printed); git log since-marker; deploy_ledger.py check --red.
