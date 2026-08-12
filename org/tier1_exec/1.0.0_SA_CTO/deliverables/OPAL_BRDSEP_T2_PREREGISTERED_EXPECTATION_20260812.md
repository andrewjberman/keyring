# PRE-REGISTERED EXPECTATION -- OPAL_BRDSEP.T2, Cottonwood 18-Strategy total

**Recorded by:** `1.0.0_SA_CTO`
**Recorded at:** 2026-08-12 ~1940Z -- **BEFORE** `0.4.0_DS_ClientPlatform~O` delivered T2
**Deliberately NOT routed to the measuring lane.** See section 3 for why.

---

## 1. The prediction

**Andrew-direct, CTO terminal, 2026-08-12 ~1940Z, VERBATIM:**

> "yes the 136.5m figure is good, but i think if we get the totals of all those we'll find the real total
> for model + non-model is closer to 170m"

**Pinned before the fact:**

| quantity | value |
|---|---|
| T1 measured Cottonwood **Opal model** AUA | **$136,530,322.99** (as-of 2026-08-10) |
| Andrew's expectation, **18-strategy total (model + non-model)** | **~$170,000,000** |
| Therefore his implied **non-Opal balance** | **~$33.5M** |
| Therefore his implied **Opal share of strategy value** | **~80%** |

*The implied figures are MY arithmetic on his stated total, not his words. He stated one number.*

## 2. Why this is worth recording rather than just remembering

**His last estimate of this kind was exact.** On 2026-08-12 ~1855Z he wrote *"there should be 1.74b in
there or so for 49 not 1.4b"* against Schwab `08242234`. The lane's independently measured
`partner_custody_total` was **$1,736,948,738.65** -- his recollection matched a machine measurement to two
significant figures, and it caught a **presentation** error (the correct row was second in the table) that
no numeric control we run could have caught, because both rows were correct.

**A human estimate whose derivation shares nothing with the measurement is the strongest witness available**
-- it is the one form of corroboration that cannot inherit the measurement's own errors. That is exactly
what makes it worth pinning BEFORE the answer arrives, and worthless afterward.

## 3. ⛔ WHY THE LANE WAS NOT TOLD

**Sending a measuring lane the expected answer destroys the thing that makes the estimate valuable.**

- A lane that knows the target may stop searching when it reaches it -- the classic stopping-rule bias. T2's
  composition axis is only ~46% covered from our own landing, so the lane must decide **how hard to push**
  (specifically, whether to spend the `cot-BD` vendor lift). **A number in hand makes "close enough" a
  reachable stopping point, and the decision to stop looking is precisely the judgement I need unbiased.**
- If the measurement then matches, the match proves nothing -- the two are no longer independent. This is
  the shared-derivation failure: a witness that has seen the answer is not a witness.
- The lane has ALREADY demonstrated the discipline this protects. On T1 they wrote that a cross-check which
  is secretly the same derivation "would read as corroboration," and they declined to fall back on my
  subtraction and call it independent. Handing them a target would undercut the exact instinct that makes
  their numbers trustworthy.

**So: recorded here, at CTO, timestamped, unrouted.** When T2 lands I compare and report the delta in both
directions. A miss is as informative as a hit.

## 4. How this will be adjudicated when T2 arrives

| outcome | reading |
|---|---|
| Total lands **near ~$170M** | Independent corroboration. Two derivations sharing nothing agree -- the strongest evidence available for a board figure. |
| Total lands **near $136.5M** | The 18 strategies are ~wholly Opal-composed; the non-Opal balance is small. His estimate would be high, and the *reason* is the finding -- likely that the blends carry less non-Opal weight than their names imply. |
| Total lands **materially above ~$170M** | Either the strategies carry more non-Opal weight than expected, or the Opal-tagged subtotal itself exceeds T1's cut (non-Opal-*named* strategies carrying Opal constituents T1 could not reach). |
| Totals **do not reconcile** (`opal + non_opal != total`) | A defect, not a framing question. T2-A3 requires the identity be asserted per strategy, and violations reported rather than silently balanced. |

⛔ **In no case is the measurement adjusted toward this number.** If they disagree, the disagreement is the
finding and it gets reported as one. T2 section 5 already forbids tuning T2's subtotal toward T1's
$136,530,322.99; **this expectation is under the same prohibition, and more strongly, because it is
Andrew's own and the pull to make it right is correspondingly greater.**

## 5. Provenance

- T1 figure: `0.4.0_DS_ClientPlatform~O` deliverable @`e2991bf495`, accepted @`7a3916acd8`.
- T2 spec (amended, Cottonwood-only two-level decomposition): @`f6039beade`.
- The `08242234` precedent: Andrew ~1855Z, lane measurement @`e2991bf495`.
