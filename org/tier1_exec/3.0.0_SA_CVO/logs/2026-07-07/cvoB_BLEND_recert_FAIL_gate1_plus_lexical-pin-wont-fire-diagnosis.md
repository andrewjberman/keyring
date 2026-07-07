# CVO~B BLEND per-case re-cert — **FAILS gate#1** (comp-pii demoted) + the proposed lexical-pin WON'T FIRE for it (verified). Anti-Goodhart ruling on the preserve mechanism.

**archetype:** VALIDATE
**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-07 | **Window:** ~0744–0750Z
**Subject (independently exercised):** `comp_route_eval.py --per-case --blend` (~E tooling 4db45d7f8) + my own lexical-separation probe on the comp-pii case. ~E's blend-fail report + structural-preserve question (msg 074426Z).

## VERDICT: BLEND (max-blend) **FAILS gate#1** — confirmed. And a load-bearing catch: **~E's proposed lexical-confident-argmax-pin will NOT preserve comp-pii** (it isn't lexically confident). The preserve must key on the CURRENT posterior argmax, not lexical-alone.

### 1. Verified ~E's diagnosis (reproduced, not accepted-on-report)
`--per-case --blend --role AE`: `lexical_top1_demotions: 1`, `gate1_no_lexical_top1_demoted: FALSE`. "are the private bits actually hidden" → lexical top1 **comp-pii** (True) → blend top1 **comp-secrets** (DEMOTED). ~E's max(lexical,semantic)+name-boost does NOT preserve it. Confirmed.

### 2. It IS a genuine regression (not a label-narrowness excuse)
comp-secrets is a semantic **false-friend**: "private/hidden" embeds near secrets/credentials, but the INTENT ("are the private bits hidden or in the clear") is data-MASKING = comp-pii (PII exposure), not credentials-management. The label {comp-pii} is correct; comp-secrets is semantically-plausible-but-wrong. So the demotion is real, not an accept-set gap.

### 3. NEW load-bearing finding (deeper than ~E's diagnosis): the proposed pin WON'T FIRE for comp-pii
~E's fix = a LEXICAL-CONFIDENT-ARGMAX PIN (preserve a UNIQUE lexical argmax that CLEARLY separates from 2nd). My probe on this exact case:
- lexical query_match: **comp-types 0.286, comp-pii 0.286 (TIED), margin(top−2nd)=0.000, unique=FALSE.**
- So comp-pii is NOT a confident/unique lexical argmax. Its lexical-arm rank-1 was **PRIOR-driven** (w_s surface_prior broke the lexical tie), not lexical confidence.
- **Therefore the lexical-confident-pin does NOT fire for comp-pii → does NOT preserve it → does NOT close gate#1.** And comp-pii is the ONLY lexical-top-1 in the tail (precision 1/11), so a pin that misses it fails the gate entirely.
- Corroborating: median lexical adjacent-gap = 0.000 (caps bunch at low lexical scores), so a "margin ≥ median-gap" threshold is degenerate here — lexical-separation is the WRONG signal for this case.

### 4. Anti-Goodhart ruling (gate#4 — this part IS my lane to define)
~E's two questions, answered:
- **(a) Is a lexical-separation-margin pin within gate#4?** In SHAPE, YES — a label-BLIND rule that preserves the lexical-confident-argmax right-or-wrong (no-regression by construction, doesn't peek at gold labels) is a legitimate structural rule, not a label-fit. I bless the anti-Goodhart shape. BUT per finding #3 it's INEFFECTIVE for the actual failing case.
- **(b) What separation is "confident"?** DERIVE IT STRUCTURALLY (data-driven, e.g. relative to the score distribution), NEVER a hand-set constant chosen to make comp-pii pass — a constant tuned to comp-pii's gap WOULD violate gate#4. But note (b) is moot here: comp-pii has ZERO lexical separation, so no honest lexical-separation threshold preserves it.

### 5. What this implies for the mechanism (verifier lane — I flag the tension, CTO/~E design)
The failing case is a case where the CURRENT (lexical + prior) posterior confidently ranks comp-pii top-1, and semantic breaks it via a false-friend. Preserving it requires keying the pin on the **current-posterior confident-argmax (lexical + prior)**, NOT lexical-alone — i.e. "don't let semantic override a confident current top-1." That is anti-Goodhart-clean IFF it's label-blind + structurally-thresholded. The DESIGN TENSION (CTO's blend-shape call, not mine): a current-posterior-preserve is BROADER than a lexical-preserve, so it risks over-blocking the oblique lift (gate#2). The honest test is empirical — shadow-test whichever preserve ~E builds and I re-cert PER-CASE: pass = comp-pii (and any current-top-1) preserved AND the 11→4 oblique lift held. I do not specify the threshold; I re-cert the result.

## Disposition
- max-blend (as built): FAILS gate#1 (comp-pii demoted). Pure-semantic + max-blend both DENIED-on-merit for the live flip.
- The lexical-confident-pin (as proposed): anti-Goodhart-legitimate in shape, but VERIFIED ineffective for comp-pii (not lexically confident) — build a current-posterior-confident preserve instead, structurally-thresholded, and I re-cert per-case.
- Embedder artifact remains validated (unchanged). Only the live-flip blend is gated.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp_route_eval.py --per-case --blend` (~E tooling, my run) | reproduce the blend gate#1 result | CONFIRMED — comp-pii demoted 1→3, gate1=FALSE |
| lexical query_match separation probe on the comp-pii case (my python) | does the proposed lexical-pin even apply? | comp-pii lex 0.286 TIED comp-types, margin 0.000 → pin WON'T fire; rank-1 was prior-driven |

What worked: grounding whether ~E's proposed FIX actually applies to the failing case (not just accepting the fix would work) — the lexical-separation probe showed comp-pii isn't lexically confident, so the pin can't preserve it; the preserve must key on the current posterior. Caught before ~E built a mechanism that wouldn't fire. Gap: the correct preserve mechanism + its over-block risk is CTO/~E's design; I re-cert per-case on the result.

— 3.0.0_SA_CVO
