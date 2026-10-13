# NFRA_DEVPLN act A13 -- RETIRED: DO NOT RUN (superseded 2026-10-13 ~23:35Z)

Issuer: `2.0.0_SA_COO~DV`. This file originally gave a command to withdraw dell2's duplicate approval row `dell2-20261013T221411Z-3635`. **It is void. Do not run any command from it.**

Why: dell2's cluster copy (read ~23:33Z, last modified 23:22:29Z) shows the duplicate pair already settled:

| row | state | note |
|---|---|---|
| `dell2-20261013T221352Z-cffa` | CLOSED `declined` at 23:02:26Z by `1.0.0_SA_CTO~DELL2`, ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_DELL2_APPROVAL_ROW_CFFA_DUPLICATE_OF_3635_20261013.md` | closed before `withdrawn` existed, on the CTO's earlier relay; same head `03073765`, 4 commits |
| `dell2-20261013T221411Z-3635` | OPEN | the NEWEST row, so `approval-status` reads it, and it carries the feature for Andrew |

Withdrawing `3635` would leave `cffa` (declined) as the only row the route could read for a feature Andrew has not ruled on. The CTO ruled the same (`1.0.0_SA_CTO` msg 108992, after his round-4 analysis `ROUND_ANALYSIS.round4.md` section 2, which named `cffa` before he read that it was already closed): `3635` stays open and Andrew rules only `3635`. `cffa`'s `declined` is harmless because `approval-status` reads the newest row. `withdrawn` cannot be applied to `cffa` (a withdraw ends only an OPEN row).

Read-back, from any box: `python .tools/open-calls.py approval-status --branch cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal` reads `state=OPEN row=dell2-20261013T221411Z-3635`.
