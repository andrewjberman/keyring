# Drive-queue window — overlay validated, $122.5M enumerated, billing fix deployed, 50%-external characterized

**archetype:** MIXED (IMPLEMENT / DIAGNOSE / VALIDATE)
**Window:** 2026-08-11 1025Z -> 1058Z · **Serial:** 0.4.0_DS_ClientPlatform
**Context:** Andrew's 10-min drive loop (kill = code compiles + platinum overlay field/quality
parity, CVO-validated). COO re-sequence 103002Z + 103756Z.

## Landed, in order

| commit | content |
|---|---|
| @327e877e32 | A_03 backfill: B-1 re-VALID 13 rows; accrual-predicate row an HONEST FAIL (next_pay_date 1/112 DEGENERATE -> DERIVE computes it; maturity_date 132/2,313 refutes the spec prose) |
| @28cdbed0e1 | V1-V4 overlay bands PRE-committed (10:35:58Z, before the evidence run) |
| @eb431e9ac0 | overlay instance VALID: field parity 35/35, fit_harness evidence run, mutant A FAIL rc=1 |
| @8993fcd090 | pinned-delta extension: D5/V3 pinned to the ENUMERATED composition; mutant B re-armed FAILS rc=1; self-test 4/4 (new control 4). CVO VALIDATED 105319Z — FIRST surface to clear the bar |
| @38b5921727 | billing fix: periods restored (791/907, ISO), absence stays null, ending_mv_reported verbatim, three-way enum (495/353/59). DEPLOYED BOTH LEGS via safe_deploy_core, comp-pipescript VERIFY OK x2 (the lib leg nearly rode the atomic-commit≠atomic-deploy class — caught) |
| (uncommitted evidence) | $122.5M enumeration + 50%-external characterization in p1_evidence/ |

## The two big measured findings

1. **$122.5M decomposition (identity residual -$0.00):** $108.0M bd cash/other basis gap +
   $40.6M securities net that HIDES ±$435M offsetting universe misalignment (962 unmapped bd
   accounts $242.6M vs 1,687 Schwab-only $193.0M; map coverage 83.88%). Held-away story
   demoted to one unverified candidate. At Andrew via COO for the port decision.
2. **50%-external distribution (at CTO for ruling):** 40/68 rows = SAME-ACCOUNT type
   round-trips netting $0.00 exactly (structurally unmatchable by the different-accounts
   matcher); one $50.5K journal = 74% of gross with an 8-digit counterpart in its own text;
   swb columns exist, 2/76 populated; adjacent-day timing REFUTED 0/45.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| fit_harness | self-test + 4 surface runs | 4/4 controls; PASS/FAIL per design |
| proof-of-spec-check | 3 instances re-validated | VALID x3 (one artifact-coverage catch fixed) |
| comp-find / comp-pipescript | vocabulary sweeps + deploy verify | VERIFY OK x2 on the deploy |
| safe_deploy_core | 2 legs | DEPLOYED + verified |

## Current State (zero-context reader)

Queue EMPTY; all remaining work clock-gated: 13:28Z wake (bp4knmpw6) -> serve-release #2
post-bar by 13:40Z (both halves in hand) -> 13:47Z CPR-4 step-4 served read -> CPR-6 own
window (both halves in hand) -> 15:06Z cot+CPR-5 deploy (bvz9hq02u). Billing silver
producer deployed; next scheduled pull emits the corrected artifact; served figures move
only on Andrew's null-consumption ruling. header_metrics kill-clear pends Andrew's $122.5M
call + the backfill (V2 windows).

## Next Steps

- [0.4.0_DS_ClientPlatform] execute the three deploy windows on their timers.
- [1.0.0_SA_CTO] 50%-external ruling on the characterization; [2.0.0_SA_COO/Andrew] the
  $122.5M port call; [3.0.0_SA_CVO] remaining families validate per-family as emitters build.

## SUPERSEDE NOTE (14:36Z, CTO adjudication 143625Z)

The "one $50.5K journal = 74% of gross with an 8-digit counterpart in its own text" line
above is KNOWN-WRONG on the attribution: the counterpart detail belongs to a $4,300 pair;
the $50.5K journal is a 12-digit SCHWAB BANK transfer the in-book guard correctly refuses
(it stays external-by-default). The ruling stands on the form (mechanism-based); only the
value characterization moved. Corrected record: CTO report 143346Z + @288f5eda4a.
