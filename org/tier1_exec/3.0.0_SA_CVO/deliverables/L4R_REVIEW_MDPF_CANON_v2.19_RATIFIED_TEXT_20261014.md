# L4-R review -- MDPF_CANON PRD v2.19, ratified-text half (ENDPOINT + CONTRACTS)

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (dell1), 2026-10-14 ~20:5xZ. Delivered by 1.0.0_SA_CTO~DELL1 msgs 5869 and 5870.
**Graded:** `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` @02852d9d16 (v2.19) against v2.18 @0736ed5c23, which this seat
signed (`L4R_REVIEW_MDPF_CANON_v2.18_RATIFIED_TEXT_20261014.md` @9838caee57).

## Verdict: REFUSE

## The change

FWD-9's head gains the v2.19 OVERRIDES (a)-(d) for the GLOBAL Trend:
- (a) full history from 2024-11-01: the five models before 2026-05-15 from 49 Financial's series alone, and Custom by difference;
- (b) Client Supervised by difference on every date, with "Other AUA" retired;
- (c) roll-forward of `carried` points;
- (d) v2.18's exception (ii) retired at Global.

The foot addendum narrows FWD-3 for the Global Trend history only: "The Global Trend's history may show single-firm model lines: 49
Financial before 2026-05-15, and Inflection's Custom from 05-15 to 07-19. That rests on Andrew's stated fact that only Opal staff can
open Global. **If a partner login can ever open Global, this exception lapses.**" Andrew's words (verbatim in the addendum): "Call 3,
only opal staff see global, that is correct."

## Why refused: the premise of (a) is contradicted by served PROD code

Read by this seat on portal `origin/PROD` (5ab67a651a):
- `src/pages/ModelPortfolios.tsx:271`: `const MDPF_GLOBAL_VIEW_FIRMS: ReadonlySet<string> = new Set(['demo'])`.
- `:375-379`: `effectiveFirmId = internal ? selectedFirmId : MDPF_GLOBAL_VIEW_FIRMS.has(claims?.firmId ?? '') ? 'global' : (claims?.firmId ?? 'global')`.
  An EXTERNAL login of the demo tenant is routed to Global. The code comment calls 'demo' "a real external firmId", and Andrew-direct
  2026-09-09 says the demo tenant "should get the 'Global' api for model portfolios, so it shows Opal Aggregate". An external claim
  with no firmId also falls back to `'global'`.
- `src/lib/firmAccess.ts:115-117`: the `'demo'` tenant's route set includes `/portfolios` (ADVI_DEMOV1.008: "demo tenant gets the
  full canonical Opal experience").

So a non-staff login can open the Global Trend today. Under v2.19 (a), that login would see 49 Financial's single-firm model lines
before 2026-05-15, and Inflection's Custom line from 05-15 to 07-19. The fact the exception rests on, "only opal staff see global", is
not true of the served portal. By the PRD's own sentence, the exception lapses.

This is a sovereign call, not a seat's. Whether external demo users may see one partner firm's model history is Andrew's to rule, with
the demo tenant named. His recorded word does not show that he had it in view.

## What would let this half be signed (any one)

1. Andrew rules, with the demo tenant named, that demo logins may see the single-firm history. The addendum records that word, and the
   exception's condition names "staff and the demo tenant".
2. The demo tenant is routed off the Global Trend history: it sees Global with FWD-3's fold kept, or its own scope. The ENDPOINT
   override then names the audience it holds for.
3. (a) is narrowed so the pre-2026-05-15 per-model lines draw only for internal sessions. That is a rendering condition the PRD would
   state.

## Secondary (not by itself a reason to refuse)

- The FWD-9 head now carries history and citations inside ENDPOINT: "v2.19 OVERRIDES ... (Andrew-direct 2026-10-14 ~20:1xZ and
  ~20:4xZ; L10 ADDENDUM v2.19 below)", and a deliverables path containing a seat name (`4.0.0_SA_CRO/deliverables/...`). The review bar
  keeps annotation, history and seat names out of the section. On the re-cut, state the rule in ENDPOINT and leave the provenance in
  the addendum.
- (d) retires the exception (ii) text this seat signed at v2.18 two hours earlier. That is coherent only if (a) holds. If (a) is
  narrowed by option 2 or 3, exception (ii) still governs the demo tenant's view.
- CONTRACTS: no line changed between the two pins.

-- 3.0.0_SA_CVO
