# L4-R re-review -- ADVI_COTBOOKS PRD v0.4 @7402cd0e3e, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO~DELL1 (dell1), 2026-10-21 ~16:4xZ. Delivered by the L4 notifier (msg 9142) on the v0.4 bump. The CTO's msg 9143
says the delivery for signature follows Andrew's ea86 word. Half hash `d0786cc5b7cb`. Answers
`L4R_REVIEW_ADVI_COTBOOKS_v0.3_RATIFIED_TEXT_20261021.md` @1d11ff88d8.

## Verdict: REFUSE (two grounds; the v0.3 superseded-endpoint ground is closed)

- **Closed: the superseded endpoint.** A script compared the fenced blocks at 7402cd0e3e: the PRD's ENDPOINT is IDENTICAL to
  `ENDPOINT_FORWARD_ADVI_COTBOOKS_20261020.md` (v2, FWD-1 to FWD-8), and the status line points at ea86.
- **Ground 1 -- v2 is unconfirmed.** Call `dell1-20261020T135705Z-ea86` reads `[OPEN]` (spine :120-121, :191; accepted by the CTO for
  NFRA_FIDSLVR in msg 9134).
- **Ground 2 -- the contracts contradict the no-Black-Diamond rule on the REC 2 seed.**
  - v2's binding rule says: "a Black Diamond read is allowed only in a column labelled as the comparison. A Black Diamond read anywhere
    else on an outcome's path fails that outcome."
  - C-NOBD says: "No book figure, assignment, client key ... is computed from a Black Diamond table."
  - Against these, C-ASSIGN seeds the `account -> advisor_id` table "once from Black Diamond's Portfolio Group", and C-CLIENT builds the
    client key "from the C-ASSIGN seed otherwise". So FWD-5 (the books) and FWD-6 (the household key) carry a Black Diamond read on their
    path, outside a comparison column. By v2's own words they fail.
  - Decision 2 calls the seed "the only Black Diamond" read, but no contract names it as an exception.
  - **Remedy:** REC 2 is Andrew's, and it is already carried with ea86. Make it an explicit exception, not a silent one:
    - C-NOBD names the REC 2 seed as its single exception, conditional on Andrew's yes to REC 2;
    - the ea86 ask tells him that a yes to REC 2 is an exception to his "no BD" rule for FWD-5 and FWD-6;
    - if he says no, C-ASSIGN and C-CLIENT need a non-Black-Diamond seed (for example the C-ROSTER login-to-advisor map) before FWD-5 can
      pass.

## Checks that pass

- **C-FIDELITY and C-ROSTER-G:** they follow the NFRA_FIDUPL landing and the per-G roster, consistent with the verdicts @bc07810172 and
  @6e5e420536. C-ROSTER-G's wait is qualified, with its reason and Andrew's act named.
- **C-HISTORY:** it re-makes the stitch against Fidelity's own positions, never Black Diamond's holdings.
- **C-COVERAGE:** it labels both Strata sizes and adopts neither.
- **C-COMPARE:** it is the only Black Diamond reader.
- **C-SCOPE:** the supervised book only.
- **C-NAMES:** the non-application for the existing opal-data-cot pipeline is stated.

## Re-delivery

Re-deliver after Andrew answers ea86, with ground 2 settled by his REC 2 answer in the text. Only the changed lines are then re-read.

-- 3.0.0_SA_CVO~DELL1
