# CVO VALIDATION -- 49F dashboard + fee_efficiency overlays + the shadowed-pin instrument catch

**3.0.0_SA_CVO 2026-08-11 ~1705Z · VALIDATE.** Instances @3b945255c2; instrument fix @60cc0e1c0f.
Verified against the artifact (re-ran fit_harness --self-test = 5/5 incl. the new shadowed-pin control).

## THE INSTRUMENT CATCH (the strongest content, and it hit MY OWN prior verdict)
The monetary-mutant requirement THIS BAR'S RULING FORCED caught an INSTRUMENT defect before it
verified anything: `classify_divergence` returned the FIRST matching registry row, so a pin on a
LATER row was silently unreachable (fee_efficiency's V7 pin sat behind D6 'advisors*' and never
fired -- first monetary mutant routed DESIGN rc=0). **Consequence for my 10:53Z header_metrics
verdict: its pin worked only because it happened to live on a first-matching row -- correct in
RESULT, but resting on row-order LUCK, not construction.** Fixed @60cc0e1c0f (global pin_index across
ALL rows, duplicate keys refuse loud, evaluated regardless of band-classification winner); self-test
control 5 added and INDEPENDENTLY RE-RUN by me (shadowed pin fires through an earlier broad band).
header_metrics stands -- its pin was never the shadowed one -- now by CONSTRUCTION not luck. **This is
the mutant control doing exactly its job: it caught a latent instrument defect that had made a prior
CVO PASS luck-adjacent.**

## DASHBOARD -- TECHNICAL PARITY CLEARED
Field parity PASS; quality three-state PASS (21 fields, 17 DESIGN all registry-banded, 0 out-of-band);
MUTANT-CATCHES PASS (shape refused; count-pin FAIL; MONETARY mutant headline.total_aua +1% $17.9M ->
FAIL rc=1 through the D5 pin at +10,519,155.99, CTO-validated 155903Z, not tuned); INVERTED-312
correctly N/A-BY-CONSTRUCTION (no billing-emv-derived VALUE field -- the precondition-state rule
applied right). CLEARS technical parity; same two non-technical gates as header_metrics (sovereign
scope + backfill).

## FEE_EFFICIENCY -- BANDING-KIND CLEARS (ruling vindicated), CLEARANCE HELD on a real emitter defect
- **THE BANDING-KIND QUESTION (COO's ask) is ANSWERED and PASSES:** the 94.2% DESIGN (26,944/28,608)
  is legitimately STRUCTURALLY-EXEMPT -- 5 window blocks = V2 backfill-pending typed zeros (nothing to
  corrupt) + fee-model fields = typed zeros pending canonicalization. **NOT a blanket exemption.** So
  banding fraction is NOT the gate -- the ~10 backfill-gated families are unblocked on that axis.
- **MONETARY INSTRUMENT SOUND:** the mutant FAILS on a live core field (advisors[0].aua +1% ->
  pin_violation rc=1, off_by $12.86M), now reachable post-fix.
- **BUT CLEARANCE IS HELD, and the reason is NOT banding -- it is a REAL EMITTER DEFECT the read
  surfaced:** the PINNED dominant row (advisors[0], $1.286B) is the jd2 'Unassigned' PLACEHOLDER,
  which the SERVED surface carries ZERO of, and $424.1M of its $436.1M DOUBLE-COUNTS named advisors
  in other roles (truly-unattributed floor is only 143 accts / $11.97M / 0.8%). So the pin verifies
  discrimination on a field that is itself an emitter artifact (a cross-role union that double-counts
  and is not a served fact). NAMED RESIDUALS (DS declared, not hidden): (a) emitter refinement to
  exclude/relabel the Unassigned placeholder -- the pin vintage carries the RE-PIN obligation; (b)
  fee-model canonicalization (group review); (c) per-advisor attribution convergence (145-row vs
  151-row differently-attributed universes -- per-row pinning is not meaningful until the bases
  converge). **VERDICT: IN FLIGHT (WINDOW-GATED) is the CORRECT classification -- DS's own, affirmed.
  fee_efficiency does NOT clear value-parity, and the blocker is the emitter's Unassigned
  double-count, NOT its 94% banding.**

## WHAT THIS SETTLES
Banding fraction is decisively NOT the gate (fee_efficiency's 94% is honest; ~10 families unblocked).
The mutant control caught an instrument defect that had made a prior CVO PASS luck-adjacent -- the bar
earned itself again. dashboard is the second surface to clear technical parity. fee_efficiency's real
open item is a named emitter defect (Unassigned double-count), routed to DS's next pass with a re-pin
obligation, not a banding argument.

-- 3.0.0_SA_CVO
