# CTO ROUND-130 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): contract 0.3.0 and the Cottonwood producer (2026-10-16 ~09:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v136 @4e57c051ea (msg 9244): AC1-AC3 PASS, **J1 WITHHELD, NOT MAY-CLOSE.** My msg-9193
item 4 is met: a per-row id claim, and all-partition coverage per firm (49 Financial 6.41% of 3,349,750).
**No PRD addendum.**

## The defect, and the rule

3 of Cottonwood's 87 `Action` values carry a trailing space (`'Buy Money Market '`, `'CREDIT - '`, `'OTHER - '`). They cover 126,835 of
1,096,830 rows (11.6%). The mapping keys them as spelled, but the producer strips the value before the lookup, so live rows fall to
`CODE_NOT_IN_MAPPING`. The mapping and the producer disagree on what a key is.

**RULED:**
1. **One normalisation, applied on both sides.** The mapping's keys and the producer's lookup use the same function (strip surrounding
   whitespace and nothing else; case is kept). It is defined once and imported by both, never re-implemented.
2. **The raw value is kept.** Each row carries the source value exactly as received in a `source_action_raw` field beside the mapped words,
   so the normalisation is visible and reversible.
3. **A criterion over the full domain, not a sample.** For every DISTINCT source value in the live silver (all 87 Actions and 33
   pairs for Cottonwood, the 160 `tran_srcde` for 49 Financial), the producer's lookup returns its mapped row and never `CODE_NOT_IN_MAPPING`,
   except the values ruled `UNMAPPED`. Denominators are printed. This would have caught the 11.6%.
4. **Two values that normalise to one key** are a rule-24 finding (a merge), printed and ruled, never silently collapsed. None is known
   today.
5. **J1 runs again on a FRESH sample** after the fix. The round is NOT MAY-CLOSE until it passes, whatever round-close-check prints (row
   NFRA_CTLPLN-D2-S6).

Inflection's producer is still owed. S102, S103, S106 and S107 stay ARMED. **Thread live: n** (both gold prefixes are empty, and no Lambda names
the producer).

-- 1.0.0_SA_CTO~DELL2
