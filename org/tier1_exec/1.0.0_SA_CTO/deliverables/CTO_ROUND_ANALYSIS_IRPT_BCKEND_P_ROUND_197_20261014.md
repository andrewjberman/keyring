# CTO ROUND-197 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- ship the cash rule without the CUSIP port; the port gets its own release (2026-10-14 ~21:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** the CVO slug for round 196 (msg 7863, `ADJUDICATION_v97.md` @a25a244747). **No PRD addendum.**

## 1. What round 196 established

- **The new pin `b1d354cfc9`** is the old pin plus `opal_unidentified.py` in the closure: 2 lines, nothing else. Cottonwood no longer
  crashes (W384-S1 closed).
- **The built-bundle differential reproduces 32 / 485 / 841.**
- **Cottonwood's 236 extra changes:** 232 trace to the CUSIP fallback port `01e843ce2e` (SC-e-56). 4 are overdetermined, produced by the
  fallback AND by the signed cash rule (W387-S6, the STOP, held).
- **45 Cottonwood sub-class values become ABSENT under the pin.** That is client-visible loss of detail.

## 2. Rulings

1. **Joint attribution (the issuer's recommendation) is ACCEPTED as a method.** One combined toggle that reverts both commits and removes
   the 4 attributes them jointly to the cash rule and the CUSIP port. They are not UNATTRIBUTED.
2. **The 45 absent sub-class values do NOT ship in this release, and neither does the CUSIP port.** This release exists to fix S1
   (`account_lost`: Cottonwood and 49 Financial stale since 10-08 and 10-12), and that is P1's critical path. The CUSIP port is a different
   change, with a client-visible regression this round found and nobody has explained. Bundling it delays S1 and ships an unexplained
   loss.
   - **This release's pin** = `b1d354cfc9` plus ONE commit that reverts `01e843ce2e` only (the closure fix stays). It is a real commit, so
     the bundle is a commit's bytes (CLAUDE.md 22a).
   - **Re-run the built-bundle differential at that pin.** Expect 49 Financial 32, Inflection 841 unchanged, and Cottonwood 485 less the
     232. Every remaining Cottonwood change must attribute to the cash rule alone, the 4 included. Any UNATTRIBUTED change is a STOP.
   - **Packet v3** is written on that pin. Both halves sign, then the apply under round 193's per-firm business-date rule and the
     manifest-anchor rule.
3. **The CUSIP fallback port follows as its OWN release, under its own pair, after a READ:** why the 45 sub-class values become absent
   (which securities, which rule path). Either the port keeps the sub-class where the prior path held it, or the absence is a documented
   correction that Andrew is told of before it ships. Its 232 changes are its release scope, named per class.

-- 1.0.0_SA_CTO~DELL2
