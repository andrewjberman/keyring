# L4-R REVIEW -- AMGT_RESAPP PRD v0.31 @18c3f9c496, ratified-text half -- REFUSE

**Reviewer:** `3.0.0_SA_CVO~Z`. **Delivery:** `1.0.0_SA_CTO~Z` msg 27507 (half_hash 9da280f6c458). **Prior signed:** v0.30
@5d3052d8d7. **Pins read:** Andrew 03:4xZ verbatim (CRO~Z record); placement R3, R11, R12 @e18d3a4e6a; shared CONTRACT
`AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` @b8c93f6342; counterpart DSGN_AMGTV1 v0.6 (signed this session @0a41d21713).
Quotes verified by printing the bytes at `git show 18c3f9c496:<prd>` and the CONTRACT at HEAD.

## Refusal ground (P0, one edit)

**The empty-month shape contradicts the CONTRACT on the bubble chart's only dependency.**
- PRD `:865-866` (FWD-32 DONE WHEN): "a name with nothing collected in a month reads a measured zero, not a missing row".
  `:2613-2614` (C-MONTHLY-CHATTER-NO-COVERAGE-GATE): "a zero is a measured zero and is served as one".
- CONTRACT section 1 (`:40-41`): "A month with nothing is absent from `by_month`; it is never written as a zero row."
- DSGN builds FWD-21's fixtures to the CONTRACT's exact shape (CONTRACT section 6, `:78`). A route that passes FWD-32 breaks
  that shape, and a route that keeps it fails FWD-32. One of the two texts must move. Which one is the CTO's call, not this
  seat's.

## Fix with the same edit (P1)

1. **Unit carrier.** C-MOVEMENT-IN-PERCENT (`:2623`) requires "an explicit unit field". The CONTRACT carries the unit in
   the field name (`return_30d_pct`, `*_pct`, `:48-50`). FWD-34 inherits the ambiguity. State which.
2. **Date fallback scope.** FWD-33 (`:881`) and C-SERVED-T1-FALLBACK (`:2617`) promise the fallback for a per-name lookup
   only. CONTRACT section 3 (`:56`) promises it for "a per-name or ranking read". The price bars read a ranking.
3. **FWD-35 is an unqualified wait.** It requires "the scheduled producer, not an ad-hoc run" (`:921`). Placement section
   5 item 1 says the 07:00 ET price pull fails without Andrew's Bloomberg Terminal sign-in. The L2 rule (CLAUDE.md
   rule 27) requires an essential wait to be qualified on the outcome with its reason and Andrew's word, as CORPUS
   FWD-22 does.

## Recorded, not blocking (P2)

- The label exists in three wordings: RESAPP "collected" (`:2615`), DSGN FWD-21 "collected", CONTRACT "articles
  collected" (`:43`). The caption is presentation, so DSGN owns it.
- ENDPOINT holds an addendum header with version and date (`:854`) and "row COO~Z" in SOURCE lines.

## What holds

FWD-32..35 are pure data feeding, as Andrew said of RESAPP ("its just data feeding"), and none is wider or narrower than
his words. R3, R11 and R12 are present. C-FRIDAY-NEVER-WIDEN (`:2642`) names both halves, the blast radius and a per-key
rollback. FWD-32 carries a positive control, FWD-33 a negative arm, and FWD-34 grades against the producer's stored
fraction.

## Verdict

**REFUSE** the ratified-text half at 18c3f9c496. A re-delivery that reconciles FWD-32 with CONTRACT section 1 and
carries the three P1 edits is a fast re-sign; nothing else in the half needs to move.

## What you should have asked but did not

Whether the CONTRACT is itself a ratified carrier. It is cited by both PRDs' CONTRACTS and binds the fixtures, but it has
no L4-R half. A CONTRACT edit made to settle this refusal moves DSGN's agreement without re-opening DSGN's half. If
the fix lands in the CONTRACT rather than in RESAPP, the DSGN half (signed @0a41d21713) should be re-read against it.

-- 3.0.0_SA_CVO~Z
