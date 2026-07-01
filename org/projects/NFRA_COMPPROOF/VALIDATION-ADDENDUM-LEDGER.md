# Graph + Tooling e2e Validation -- ADDENDUM LEDGER (fix -> retest -> revalidate)

**Owner:** 2.0.0_SA_COO~B (NFRA_COMP* program coordination)
**Source:** ~B's Andrew-direct 52-agent e2e validation, `org/tier2_senior/0.8.0_AE_CloudComp/GRAPH_TOOLING_VALIDATION_REPORT_20260701.md` (commit 4e9f0258d), Nessie HEAD 5cca1bdd.
**Verdict:** VALIDATED_WITH_GAPS -- graph categorically complete + current (52 node/52 edge cats, 19844n/34834e, provenance CURRENT); 27/32 tools PASS with spot-checks matched to LIVE AWS/TF/source; 0 hard failures; 3/5 cross-layer walks connect. Trustworthy for load-bearing cases.
**This is the COMPPROOF-B SEED** (the first honest, source-grounded e2e proof-of-tooling) -- routed to CTO 132020Z-adjacent for the COMPPROOF PRD baseline + gap-list.
**Andrew-direct addendum:** Step 1 re-verify -> Step 2 fix (per error, to owner) -> Step 3 revalidate (re-run affected checks / full workflow -> 0 open gaps).

## DISCIPLINE GATE (Rule-22 / NEVER#5)
E3 + M1-M4 are self-disclosed with file:line but NOT adversarially re-verified; comp-grep/comp-glob/comp-validate were UNTESTED (transient rate-limit hit 8 agents). A self-disclosed error is a HYPOTHESIS until adversarially confirmed -- **no fix dispatches for the unverified set until ~B's Step-1 re-verify greens them.** E1 + E2 are grounded structural HIGHs (root-caused file:line) -> proceed now.

## ERROR REGISTER

| ID | Sev | Class | Finding (file:line) | Owner | Status |
|---|---|---|---|---|---|
| E1 | HIGH | naturalness | comp-which routes read Qs ("what lambdas read bucket X") to comp-aws DERIVE (8-min rebuild); comp_route.py ignores the manifest mode:query\|rebuild tag | ~E (comp_route) + ~B assist + CTO | **FOLDED INTO COMPROUTE default-router re-scope** (Andrew-direct). E1 = the mode-GATE hard prior. Design converging CTO/~E/~C; dispatch on CTO ruling. |
| E2 | HIGH | connectivity | portal serving->prod provenance dead-ends: SERVED_FROM lands on coarse opal-data-portal-v2 BUCKET not key-level S3Keys (derive_runner.py:1300); Endpoint->Lambda = 0 edges | ~D/DE (globgrph/TSGRAPH derive) | BANKED into the (a) GRAPHUNI derive-fidelity follow-on (~D ACK 131948Z) -- one derive pass, dispatched with (a). |
| E3 | HIGH | tool | comp-drift reports a CLEAN lambda as a deploy break: drift_cli.py:217 passes target positionally to `comp-lambdamap parity` (no positional -> rc=2) | ~B (comp-drift, its domain) | RE-VERIFY (~B Step-1) then fix. ~B took it on the confirm. |
| M1 | MED | tool | comp-trace S3 direction inverted | TBD on re-verify | RE-VERIFY (~B Step-1) |
| M2 | MED | tool (SEV1-adjacent) | comp-types fabricates + PERSISTS a consumer graph for 0-importer nested types (MP/benchmark surface) | TBD on re-verify | RE-VERIFY (~B Step-1) -- MP/benchmark = critical-surface, verify carefully |
| M3 | MED | tool | comp-parity headline is a hardcoded frozen string | TBD on re-verify | RE-VERIFY (~B Step-1) |
| M4 | MED | tool | comp-heat federated mode crashes on its own default query | TBD on re-verify | RE-VERIFY (~B Step-1) |

## UNTESTED (rate-limited) -- Step-1 must exercise
comp-grep, comp-glob, comp-validate -> PASS-or-error. (comp-grep/glob are the router's own fallback surface -> important they PASS.)

## SEQUENCE
1. **Step 1 (~B, GO'd 131831Z):** re-verify the 3 untested + adversarially confirm E3 + M1-M4 (live repro + file:line). RAVC COO~B -> the CONFIRMED set.
2. **Step 2 (on confirm):** dispatch fixes to owners. E1 rides the COMPROUTE increment; E2 rides (a); E3 = ~B; M1-M4 = owners TBD (M2 critical-surface care).
3. **Step 3:** revalidate -- re-run the affected checks / the workflow -> 0 open gaps. CVO~B verify-gate (COMPPROOF-adjacent honesty).

## NOTES
- E1's convergence with the Andrew-direct COMPROUTE default-router re-scope is the headline: ~B's independent validation root-caused the exact problem Andrew directed (read intent -> rebuild tool). The fix is ONE increment, not two.
- ~B stays OFF COMPPROOF tasking (Andrew hard constraint) -- but the validation + this fix->retest->revalidate addendum IS ~B's Andrew-direct lane (not COMPPROOF), so ~B on E3 + E1-assist is in-scope.
