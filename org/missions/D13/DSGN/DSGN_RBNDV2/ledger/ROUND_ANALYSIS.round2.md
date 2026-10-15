# DSGN_RBNDV2 -- ROUND-2 ANALYSIS (1.0.0_SA_CTO, 2026-10-15 ~11:1xZ)

**On:** the CVO's L10 slug: `ADJUDICATION_v2.md` @c6f62af60b and `ADJUDICATION_v3.md` @428d5413c0, with its addendum @692b534f6a.
2 of 3 MET; 22 of 22 branch tests OK. **Branch:** `feature/dsgn-rbndv2-light`, unpushed.

## 1. What round 2 moved

- **Round 1's two defects are cured.** The sidebar accent now renders violet. The box-in-box is replaced by hairline sections
  (RB2I1-AC3 MET).
- **One shared modal frame exists, and every listed modal adopts it** (RB2M1-AC2 MET).
- **Andrew's FWD-1 look is carded** (laptop call `3c44`). His YES or NO grades FWD-1.

## 2. RB2M4-AC3 NOT MET: one defect, cut now

The FearGreed and MarketRegime modals paint chart ticks `rgba(255,255,255,0.6)` (white) on the new silver body
(`FearGreedModal.tsx`:406, :424, :890; `MarketRegimeModal.tsx`:611, :626), so the axes cannot be read. The Market Regime signal
row is also clipped by the footer.

- Fix: chart ticks read one ink token, navy-grey, never a literal white. The footer does not overlap the content.
- It is a defect inside round 2's own scope, so it does not wait on Andrew's look.

## 3. Rulings on the graduated rows

1. **W8-S1 (ARMED, this seat's): the commit hooks grade 0 portal `.tsx` files**, because the risk reflex's danger map is stale
   and commit-gate reads only `.py/.sh/.tf`. On this branch nothing is pushed, so the portal's push-time VALGATE never runs
   either. Two parts:
   - **Inside this project, now:** every merge onto the branch runs the portal's own checks (typecheck, lint and the
     relevant tests, as VALGATE would) and prints the counts in the merge record. That is the real grading for an unpushed
     branch.
   - **The hooks:** routed to NFRA_CTLPLN's next batch. The risk reflex refreshes its map, and both hooks print
     `not graded: N .tsx` rather than passing silently.
   - Disarmed when both hold.
2. **W8-S6, W8-S9 and W8-S11 (ARMED, the issuer's):** the autoFocus loss, RSIModal's dark ground and the session-warning X.
   They are read in the round-3 walk, as their remedies say, and each fixed if the read fails.
3. **W2-S3** stays ARMED as the CVO holds it, owned by the issuer.

## 4. ENRICHMENT LIST for round 3 (one issuance; C-BRANCH binds)

1. The modal chart-tick and footer-clip fix (section 2), proved by a computed-style read of a tick's fill in both modals.
2. The merge-time portal checks (ruling 1, first part).
3. **The walk (FWD-5)** starts on Andrew's YES to `3c44`. It folds in the reads for W8-S6, W8-S9 and W8-S11, and the 288
   faint signal-colour elements. If he says NO, round 3 fixes what he names first.

FWD-4 (heat maps) still waits on `be0b`.
