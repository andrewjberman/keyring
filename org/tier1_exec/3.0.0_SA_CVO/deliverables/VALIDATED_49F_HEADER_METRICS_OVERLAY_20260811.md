# CVO VALIDATION -- 49F header_metrics platinum overlay (FIRST surface to clear the parity bar)

**3.0.0_SA_CVO 2026-08-11 ~1051Z · VALIDATE.** Instance @8993fcd090, bar @bcf9e14802 (+amendments).
Independently verified against the artifact (re-ran fit_harness --self-test myself), not the summary.

## VERDICT: TECHNICAL PARITY CLEARED. Kill-clear on this surface PENDING two non-technical gates.

> **AMENDMENT 2026-08-11 ~1857Z (GATE 1 DISCHARGED -- this verdict was written ~1051Z, BEFORE the ruling):**
> **Gate 1 (the $122.5M DIVERGE-SOVEREIGN scope call) is CLOSED.** Andrew ruled it ~1742Z (/open-calls
> "Recs approved"): Schwab-08335338-canonical is AUTHORITATIVE over the BD-legacy serve, the $122.5M
> DIVERGE-SOVEREIGN RULED-ACCEPTED, record @745ca6d78f (parity bar SS 3a carries it + the cutover re-pin
> obligation). So of the two gates below, ONLY GATE 2 remains: the V2 window backfill (nna_qtd/ytd/12m),
> which is RUNNING NOW (fill-2, PID 1399266). **header_metrics is therefore ONE LANDED COMPUTE from being
> the FIRST BAR-CLEARED 49F surface** -- when fill-2 lands I re-grade the window monetary discrimination
> (it re-arms on the live V2 windows) and, clean, this surface flips SCOPE-VALIDATED -> BAR-CLEARED.
> Neither remaining step needs a human. The per-account composition enumeration (the "one thing to watch"
> below) stays a live control regardless.

| Axis | State | Evidence (verified) |
|---|---|---|
| Field parity | **CLEAR** | 35/35 both denominators, spelling-aware; mutant A (unbanded field) FAILs rc=1 -- field discrimination proven |
| Structural quality | **CLEAR** | three-state 53 MATCH-CLEAN / 31 pre-banded DIVERGE / 0 out-of-band; ordering VERIFIED at source (bands @28cdbed0e1 06:35:58 BEFORE evidence @8993fcd090) |
| Monetary value-parity | **CLEAR -- DEMONSTRATED** | the blanket-exemption hole (mutant B routed DESIGN) is CLOSED by a pinned-delta band: D5 pins total.aua at expected=-122,520,423.05 tol=191,157.89 (1bp-of-served, the RULED band transposed -- no new number). Baseline PASSES at pin; mutant B +1% now FAILS rc=1 with pin_violation. **I re-ran the self-test independently: 4/4 incl. the pin control (on-pin PINNED-OK / off-pin pin_violation).** UNVERIFIABLE-BY-INSTRUMENT re-grade SUPERSEDED -- it is now verified. |

## THE LOOP THAT GOT HERE (the bar working as designed)
Blanket band masked a regression (I caught it: mutant B DETECTED-but-DESIGN) -> DS built the RIGHT
fix in the INSTRUMENT not the evidence (pinned-delta, evaluated BEFORE a band excuses a value diff;
a STALE pin FAILs loud, forcing re-enumeration -- no silent drift) -> I verified it on the artifact.
Monetary discrimination went from asserted to demonstrated.

## TWO GATES (as of ~1051Z) -- GATE 1 NOW DISCHARGED (see amendment above); GATE 2 remains
1. **[DISCHARGED ~1742Z @745ca6d78f] DIVERGE-SOVEREIGN, Andrew's scope call:** total.aua serves the Schwab-canonical book, $122.5M
   SMALLER than the current BD-tree served book. The delta is now enumerated EXACTLY (identity
   residual -$0.00; mechanism source-confirmed BD=49F's arrival path). But whether to ACCEPT serving
   a $122.5M-smaller book is a BUSINESS decision, not a technical pass -- ANDREW's, via COO. The pin
   makes it technically discriminating; the scope stays sovereign.
2. **Residual (b), backfill:** the V2 window fields (nna_qtd/ytd/12m) are legitimately zero on the
   single day; monetary discrimination on THEM re-arms at the backfill. Data-pending, nothing to
   discriminate today.

## ONE THING TO WATCH (routed, not a blocker)
The net delta ($40.6M securities) HIDES +/-$435M of OFFSETTING universe misalignment. A
net-preserving COMPOSITION shift would be invisible to the net pin -- the per-account enumeration
(COO-commissioned, going to Andrew) is the control for that class, and it must stay CURRENT at each
vintage or a composition drift hides behind an unchanged net. The pin catches net regressions; the
enumeration catches composition drift. Both layers must live.

## GENERALIZATION
header_metrics is the ARCHETYPE emitter; the pinned-delta instrument it just proved is reused by the
other 15 families and by INF/COT. The bar + this instrument now carry monetary discrimination for
every family that has a live non-sovereign monetary field; band-covered families split to
UNVERIFIABLE-BY-INSTRUMENT with the named re-arm.

-- 3.0.0_SA_CVO
