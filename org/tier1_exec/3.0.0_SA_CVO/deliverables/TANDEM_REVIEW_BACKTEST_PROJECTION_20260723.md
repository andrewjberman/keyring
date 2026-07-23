# TANDEM REVIEW -- backtest_projection (third provenance class)

**Verifier:** `3.0.0_SA_CVO` · **2026-07-23** · **archetype:** VALIDATE · **Read-only; no PRD/code/spec edited.**
**Andrew-ordered** (CRO 050559Z; chain CRO spec -> CVO tandem -> COO decomposition).
**Reviewed:** CRO backtest spec `@88a0204ad`. **Companion:** CTO's Global-aggregation half (CTO owns the
aggregator -- several findings bind THAT half, flagged).
**Same pinned-delta discipline** as the interpolated sign; CRO holds; changes re-enter as a delta.

---

## VERDICT: the per-firm honesty machinery is SOUND and correctly reuses the pin. **DO NOT DECOMPOSE
YET** -- two gaps bind first, both at the GLOBAL aggregation (CTO's half), and one is the exact crux CRO
asked me: **the per-cohort label does NOT prevent a hypothetical from reading as actual once it enters
the Global sum.** Plus a hard external dependency (price source) that gates the whole deep-history region.

**What is genuinely sound and I am not re-opening:** the additive enum extension
(`measured | interpolated_estimate | backtest_projection | absent`) is TRULY additive -- it adds one
value + one point_class, does not touch the signed ones, so the "extend-not-invent" problem does NOT
recur; this is a real extension of the channel I signed. The compute-quarantine (one filter predicate),
the one-class-per-date-per-MODEL boundary keyed on real bronze `createdAt`, and the vintage-in-
`backfill_method` label are the machinery I already signed, correctly applied. CRO named the categorical
difference ("no accounts, no assignment, hypothetical not AUM") precisely.

---

## >> F1 (BINDS CTO's AGGREGATOR, P0-equivalent) -- ONE-CLASS-PER-DATE IS PER-MODEL; THE GLOBAL
CROSS-FIRM SUM IS WHERE THE HYPOTHETICAL LEAKS. <<
The boundary rule (§6) is per **model**: `d < createdAt(M) -> backtest`. But the **Global** timeseries
sums across FIRMS. On a pre-cottonwood-creation date (say 2026-04-01), 49F and inflection have
**measured** history while cottonwood is **backtest**. So a Global date mixes `{measured, measured,
backtest_projection}` -- and the spec does **not** define (a) whether the cottonwood backtest VALUE
enters the Global AUM sum, nor (b) how the Global `point_class` derives in that mixed case (CRO §3 only
says "backtest-class where ALL cohorts are backtest" -- the MIXED cell is undefined).

**This is the crux you asked me, answered:** the composition-vintage label is sufficient at the
**per-firm cottonwood band**; it is **NOT** sufficient at the **Global sum**. A labelled hypothetical
cohort summed into a real-AUM total produces a Global dollar figure that is part-real, part-hypothetical
-- and no per-cohort label stops the SUM from being read as actual AUM. **This is categorically
different from the interpolated band, which I could sign into the Global sum precisely because
interpolated is estimated-*actual* AUM (summable). Backtest is *not* AUM at all -- it cannot enter the
AUM sum, and a label is not a structural barrier to summation.**

**Required before build (CTO's aggregator):** backtest is a **per-firm display band ONLY, structurally
excluded from the Global AUM sum**. If it renders on Global at all, the Global point must be
**backtest-tainted AND the backtest dollars excluded from any "actual AUM" figure** -- enforced by the
aggregator, not by the cohort label. Define the three-class point_class LATTICE explicitly:
least-certain-present wins (`measured < interpolated_estimate < backtest_projection`), and a
backtest-tainted Global point never contributes to a measured-AUM consumer.

## F2 (HONESTY, P1) -- THE ANCHOR PUTS THE HYPOTHETICAL ON THE DOLLAR AXIS; "STYLE" BECOMES THE ONLY GUARD
§4 anchors `backtest_value = first_real_value x CompIndex(d)/CompIndex(createdAt)` -- so the backtest
renders **in dollars, at real-AUM scale**, meeting the real line. Then grey-dotted style is the ONLY
thing telling a viewer it is not ~$X of assets in April. **"Visual style is the only guard" is the
care-is-not-a-control pattern.** CRO flags this honestly (continuity-vs-purity) and leans anchored; I
weigh the other way and say why: the **rebased-performance basis (growth-of-$1)** is **structurally**
safer because it is a **different axis** -- you cannot misread an index as dollars, whereas a dollar-axis
line relies on the label doing work an axis would do for free. **Andrew/CTO's product call**, but the
distinction to put in front of them is structural-guard (different axis) vs visual-guard (style) --
and for something that must "never read as actual," a structural guard beats a visual one.

## F3 (HONESTY, P1) -- THE VINTAGE LABEL IS CONSTANT; THE ASSUMPTION IT LABELS DEGRADES WITH DEPTH
§5 holds **current composition constant backward**, justified by B6 structural-blend stability (0.6.2).
B6 established stability over the **observed** window (weeks). The backtest may reach **months or years**
pre-creation -- and "today's composition is what it would have been 3 years ago" is a far stronger claim
than "stable over the observed weeks." **But the honesty statement here is a CONSTANT label
(`backtest_current_composition_held_constant_YYYYMMDD`) -- it is identical for a 2-month and a 5-year
backtest, and there is no confidence scalar (§3 sets it null) to carry the degradation.** This is the
backtest analogue of the interpolated band's confidence-must-degrade condition: the honesty signal does
not weaken as the extrapolation gets less defensible. **Recommend** either a bounded **max-lookback**, or
a **depth/distance-from-createdAt indicator** carried per point, so a deep extrapolation is
distinguishable from a shallow one. Do not let one constant label cover a 2-month and a 5-year claim.

## F4 (GROUNDED GATE -- CONFIRMED + SHARPENED, DECISION for Andrew) -- the price source is a HARD
EXTERNAL DEPENDENCY, not a build detail
**I verified CRO's absence claim** (not taken on report): `opal-market-data-v2` top level is
`fred/ indices/ corpus/ causal_claims/ lambda/`; `indices/` = one `bullets.index` (a corpus index, not
prices); a sweep of 7 liquid ETF tickers (IWM/SPY/VTI/AGG/IJR/VEA/VWO) returned **none** anywhere in the
bucket. **ETF price history is genuinely not in-estate** (minor: the prefix is `fred/`, not the
`update/` CRO named -- substance holds). **Sharpening CRO's ranking with the egress law:**
- **Option 1 (holdings-derived, egress-free)** reaches only ~06-08+ -- structurally it **cannot** price
  the deep pre-creation region (holdings start 06-09; the backtest region is pre-`createdAt`, i.e.
  pre-05-28 for the earliest models). So it covers a sliver, not the point.
- **Options 2 (public closes) and 3 (ycharts)** are BOTH **egress off Opal infra** -- pre-authorization
  **excludes** every such egress. **ycharts is explicitly HELD** (standing vendor prohibition; per-use
  Andrew word). **Public closes is ALSO not pre-authorized** (a new egress, different category than the
  vendor-client-data ban, but still Andrew's word). **So the deep-history backtest is HARD-BLOCKED on an
  Andrew egress decision** -- it is a gating external dependency, and no build can proceed past ~06-08
  without it. CRO named the gate; I confirm it is a hard block, not a detail.

---

## MUTANT SET (CRO's four + two the findings force)
| # | mutant | must produce | proves |
|---|---|---|---|
| a | backtest point -> any measured-only consumer | REJECTED (as interpolated is) | §8.2 |
| b | backtest point with NULL/absent vintage | **fail LOUD** (the vintage IS the honesty) | §8.3 |
| c | two classes on one date per model | impossible (backtest ends exactly at createdAt) | §8.1 |
| d | anchor continuity at createdAt | backtest(createdAt) == first_real_value exactly | §8.4 |
| **e** | **Global date mixing backtest + measured cohorts** | **the backtest $ NEVER enters the Global AUM sum; the Global point is backtest-tainted and excluded from measured-AUM consumers** | **F1 -- the crux at the level it fails** |
| **f** | **a backtest date with no available ETF price** (pre price-source floor) | **`absent`, not a fabricated or forward-filled value** | **F4 -- the price gate as a machine check** |

---

## ROUTING
- **CTO (aggregator half):** F1 -- define the three-class point_class lattice + structurally exclude
  backtest dollars from the Global AUM sum (mutant e). This is the load-bearing one.
- **CRO (method):** F3 -- max-lookback or a depth indicator so the constant vintage label does not cover
  arbitrarily deep extrapolations; mutant f (price-floor -> absent).
- **Andrew / CTO (decisions, not build):** F4 -- the price source (holdings-only-and-accept-the-floor vs
  a public-pull egress vs ycharts-egress); F2 -- anchored-dollars vs rebased-performance visual.
- **NOT signed:** I sign the schema when F1 is resolved in CTO's aggregator (the lattice + the sum
  exclusion), F3 is dispositioned, and there is a pinned pair (CRO delta + CTO Global half) as with the
  interpolated band. The per-firm method is sound; the Global aggregation and the price gate are what
  remain.

## RESIDUAL / not verified
- CTO's Global-aggregation half for the third class was not in hand as a written spec at review time; F1
  is stated against the aggregation PRINCIPLE, and binds whatever CTO writes. If CTO has already
  specified the lattice + sum-exclusion, F1 is satisfied on sight of it.
- The CompIndex method's numerical accuracy is CRO's METHOD (out of scope); I reviewed the SCHEMA, the
  honesty boundary, and the grounded gate.

-- `3.0.0_SA_CVO`
