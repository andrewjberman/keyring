# ws-charter tick — 1.0.0_SA_CTO — 2026-06-01 1651Z

**CLASS:** FIX/investigation (Andrew-direct; Macro page data anomaly)

## Trigger
Andrew-direct: portal Macroeconomics page shows MAY-2026 BLANK for most sections
(Consumer, Housing, Labor [except Continuing/Initial Jobless Claims], Inflation,
Lagging, Leading, Financial Condition [except Bloomberg FCI / Chicago Fed FCI /
Fed Balance Sheet]) — but JUNE-2026 FULLY filled, despite Yang's latest data being
May 29. "Team put on this; look into YALP_MACRO work."

## CTO scoping + hypothesis
Diagnostic pattern: blank-May sections = MONTHLY-lagged indicators; present-in-May
= WEEKLY/DAILY high-freq. Future-month-filled + current-month-blank + source-to-
May-29 => likely PERIOD-LABELING / off-by-one-month (monthly release stamped a
month forward) OR forward-fill/projection into June, OR source-vs-serving period
mismatch.
Data flow mapped: FE portal/src/pages/Macroeconomics + api/endpoints/macro.ts ->
S3 <- producers: yang-generate-macro(-timeseries) [prime suspect: serving period
bucketing] + fred-data-ingestion + fred-macro-ingestion + data/yang_macros_re
adapters (YALP_MACROS Phase-2 RE harness) + 07_macroeconomics lambdas.

## Action / staffing
- AE OpalETL (0.5.0, owns FRED/macro pipeline, live+warm) = immediate investigation
  lead; tasked to trace end-to-end + root-cause the date/period bug (165112Z).
- MSTR spawn-request (165121Z) for a dedicated macro-investigation DS lane — the
  YALP_MACROS-native 0.1.0_DS pod is NOT in the live roster. MSTR STALE 345s
  (liveness flagged to Andrew); AE proceeds solo meanwhile.

## Next-cycle expected state
AE returns the trace + root-cause + proposed in-pattern fix (surface before change).
MSTR spawns the dedicated lane on wake. Data-honesty: any forecast/estimate/forward-
fill must be labeled, not presented as actual (same bar as the benchmark fix).

ws-charter-cycle:0006 class:FIX
