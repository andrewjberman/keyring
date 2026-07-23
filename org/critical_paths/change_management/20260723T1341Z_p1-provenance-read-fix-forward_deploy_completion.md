# Deploy Completion — P1 Fix-Forward: pairedProvenanceRead pre-contract hardening (portal v2.1.144)

**Status:** CLOSED — completed in-session (condition-3 live-verify residual named below; DE's live verify PASSED @931f6b11c)
**Closed:** 2026-07-23T13:47Z
**Owner:** 0.2.0_DT_PortfolioAnalytics (Andrew-direct report -> DT diagnosis -> CTO ratification 133702Z -> DE fix -> DT promote)
**Window:** 2026-07-23 ~13:32Z (Andrew report) -> 13:47Z (CI SUCCESS + DE verify triggered)

## Incident
Andrew-direct at DT terminal: Inflection + 49 Financial firm dropdown views crash on PROD
("TypeError: Cannot read properties of null (reading 'date')", page not loading). Introduced by
v2.1.143 (live 13:01Z): pairedProvenanceRead.ts:100 iterated cohort_provenance reading e.date with
a length-only guard. The 07-18 per-firm artifacts carry the channel PRE-CONTRACT: inflection
429/429 null entries; 49financial 347 null + 82 date-less old-schema (basis/custody/model_1a keys).
Cottonwood (same-day re-emit, new contract) was clean — which is why v2.1.143's acceptance could
not see it (control-that-cannot-fail class; named by CTO).

## Decision
CTO ratified FIX-FORWARD 133702Z; rollback rejected on the record (would strand the served band
artifact without its honest renderer — trading a loud crash for a silent honesty defect). Four
conditions gated the promote (degrade-honestly / exercise-both-failure-shapes pre-push /
three-firm post-verify / standing per-firm-acceptance checklist amendment).

## Evidence
| Gate | Result |
|---|---|
| Fix commit | 5bb54ecf (DE): malformed channel (any null or date-less entry) -> whole-channel predates-contract degrade, loud warnOnce, never guess |
| Condition-2 at gate | DE mutant control on REAL served bytes: pre-fix logic THROWS the exact PROD TypeError on both firms' artifacts; post-fix degrades both; renders P1_inflection_fixed.png ($202M/713) + P1_49f_fixed.png ($1.64B/7,041) + P1_cottonwood_unregressed.png (band intact, 446-entry index) |
| Delta promoted | 5bb54ecf + 4d812d9a (fee-basis caption) + 0a261c74 (Global read-path prep, inert) |
| Typecheck / parity / push gates | tsc clean; parity EMPTY; provenance guard + VALGATE + push-time tsc PASS |
| PROD commit | ffc022ed (d270acc9..ffc022ed); rollback SHA d270acc9 encoded |
| CI | run 30012584835 conclusion: success (gh run view --json) |
| Tag | portal-v2.1.144, peeled ^{commit} == head |
| Workspace pointer | CLOUD ff1254d9b — gitlink VERIFIED == 5bb54ecf pre-commit (v2.1.143 pointer-message lesson applied) |
| Main tree | DEV, workspace root; worktree pruned (FTL residue inert) |
| Timeline | report ~1332Z -> root-cause+dispatch 1336Z -> ratify 1337Z -> gated fix 1341Z -> push 1344Z -> CI SUCCESS 1347Z (~15 min report-to-live) |

## Residual — DISCHARGED 135046Z
- CTO condition-3 PASSED (DE 135046Z, evidence @931f6b11c, three-way grounded): (1) BUNDLE —
  served chunk ModelPortfolios-BVoIZL20.js carries the fix's distinctive warn literal;
  (2) CRASH-FREE — inflection + 49financial render on the LIVE origin with real served
  artifacts, ZERO pageerror (exercised negative: pre-fix state emitted the exact TypeError);
  (3) NON-REGRESSION — cottonwood live band + confidence label + trading-day axis intact.
  **P1 CLOSED end-to-end: report 1332Z -> live-verified fix 1350Z (~18 min).**
- Condition-4 standing amendment adopted: per-firm acceptance covers EVERY firm the renderer
  serves, not the firm that motivated the release.
