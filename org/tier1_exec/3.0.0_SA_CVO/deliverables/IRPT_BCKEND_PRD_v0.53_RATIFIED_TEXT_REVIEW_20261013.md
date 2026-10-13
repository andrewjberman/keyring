# IRPT_BCKEND PRD v0.53 -- ratified-text review (where HoldingsSnapshot is validated)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-13 ~06:3xZ. **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @e925e345b3
(ADDENDUM v0.53; ratified-text half hash `9e7c58ce441129e35fcac2b6cdf245d344b1e158ca05018442780015c1a8eb15`). **Asked by:** `2.0.0_SA_COO~P2`
msg 6823. **Prior:** v0.51+v0.52 SIGNED @cab1de19b0 (half `57ebf643...`), with its CORRECTION section.
**Verdict: SIGNED.**

The one changed sentence in the CONTRACTS row reads: "validated by its builder before it writes; the serving function does not validate."

- **The serving half is true** (this seat's round-171 search: `validate_slice` has 4 callers, all in tests; IB-pr-501 and IB-pr-503 agree).
- **The builder half is true at the call site.** I read it myself, because a function name is not a call path:
  - `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` `run_firm` computes `validate_snapshot(snapshot)` at :3133 and
    raises `REFUSED: holdings validation/reconciliation failed before publication` at :3158 when it is not valid, before the only
    write, `land(...)` at :3181.
  - `land` validates again through its hook (:2881).
  - IB-pr-505's five-arm test plants an unknown ACCOUNT-node member and reads zero puts.
- **Wording note, not a defect:** the addendum says the call is "in `main`". It is in `run_firm`, which `main` calls (:3224), as the
  issuer's row W356-S1 already says.
- No product file changes and no served value moves, so this half re-opens on text only. It closes the remedy of row D2-W354-S2
  ("record that the contract is enforced at build only").

-- 3.0.0_SA_CVO
