# inf orchestrator semantics ruling — INFRA-copy canonical; (e) = quorum RE-KEY, not date-default flip
**archetype:** VALIDATE

Trigger: COO [ARCH-RULING] 213954Z — AE 0.6 (BRONZE-FIX #1, ad1f03b7f) found the 06-11 cutover deployed the
un-hardened data/orion-lineage orchestrator, silently dropping a month of May hardening that lives in the
divergent twin at infra/aws/ec2/inf-bronze-runner/orchestrator.py (JWT pre-flight JWTRES.001b; S3-output
sentinel gate INFETL.CHAININC; assets expected_fail removal INFREL.010; transactions-decommission
INFINGE.005b). L5 of the incident.

## RULING 1 — The INFRA copy's semantics are canonical, in full.
1. **Transactions: DECOMMISSIONED from the orchestrator; inf-api-txn is the single producer.** Grounds:
   (a) INFINGE.005b was a deliberate, project-recorded decision; (b) inf-api-txn is the proven live
   producer (tonight's recovery ran through it); (c) single-writer doctrine — the orchestrator csv leg
   running alongside inf-api-txn recreates the dual-writer class ADVI_DWSPLT existed to kill; (d) the
   bronze csv is UNCONSUMED by the served chain (DS-established: silver parquet has never come from the
   csv path) — it is dead weight + double Orion API load. The transactions DimSpec is REMOVED in the #2
   port. (Tonight's R-leg csv re-fire was harmless R1 hygiene; no served effect.)
2. **Assets: expected_fail REMOVED (INFREL.010 semantics).** Empirically confirmed TODAY: the assets dim
   ran ok (328s, manifest ok) — the deployed copy's expected_fail=True is stale pessimism.
3. **Port direction:** BRONZE-FIX #2 ports the May hardening ONTO the canonical data/inf copy (JWT
   pre-flight + sentinel gate + the semantics above); the infra/ twin then RETIRES (single source). The
   sentinel gate IS partial completion-contract work — AE 0.6's fold-into-#2 disposition affirmed.

## RULING 2 — (e) completes as QUORUM RE-KEYING, NOT a date-default flip. The trap, explicitly:
inf-api-txn's D-1 default is NOT a bug to flip — it is transaction-data semantics. Transactions for day D
are complete only after D ends; a same-day pull at 13:00Z captures a PARTIAL day (and Orion's morning
update itself serves data through D-1 close — the same-day dim pulls are D-1-VINTAGE data too). Flipping
the default to now() would serve partial transaction days. The actual defect is the KEYING MISMATCH:
the D 13:00Z run pulls D-1-complete transactions but writes its sentinel under D-1's quorum, while the
8 dims key under D — so day-D gold fires at D+1 13:00Z, serving ~20h late data that was available D
13:05Z.
**Fix:** the D 13:00Z inf-api-txn run (pulling D-1-complete transactions, unchanged) writes its sentinel
under SERVING-DAY D's quorum. Gold then fires D ~13:05Z with a vintage-consistent build: dims = Orion's
D-morning state (data through D-1 close) + transactions complete through D-1. Same data, served the same
morning — which is exactly Andrew's stated expectation ("Orion updates prior-day data before market
open"). Document the vintage semantics in the sentinel (source-vintage stamping, #4 pattern).

## Cross-checks for the #2/(e) TO bodies
- Quorum contract (#2) defines transactions as a REQUIRED member keyed to serving-day D per Ruling 2.
- The re-key changes WHEN served output updates (a day earlier) — by construction toward already-available
  truth. Treat the first re-keyed morning as a verified vintage-shift with before/after captured (never-
  widen drift-acceptance lite: CTO+COO note, evidence = the first morning's artifact pair), not silent.
- The 9 manual_api DRIFT rows (TOOL-03 finding) triage under #1 with these semantics as the tiebreak:
  repo data/inf copies + the hardened semantics win; stale S3 twins retire.

## Compiler Tools
| Tool | Run? | Why |
|---|---|---|
| comp-* | NO | Semantics adjudication over AE 0.6's diff evidence + tonight's live recovery facts; no change by me. #1/#2/(e) TOs carry the mandates (TOOL-03 deployed-checks now cover bronze first-class). |
