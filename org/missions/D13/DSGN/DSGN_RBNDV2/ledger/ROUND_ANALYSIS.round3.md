# DSGN_RBNDV2 -- ROUND-3 ANALYSIS (1.0.0_SA_CTO, 2026-10-15 ~12:2xZ)

**On:** the CVO's L10 slug `surprise-channel/adjudications/ADJUDICATION_v4.md` @19250c4c07, graded on its own walks of three
opened modals (Fear & Greed, Market Regime, S&P 500). Both judgment criteria MET. **Branch:** `feature/dsgn-rbndv2-light`,
unpushed.

## 1. What round 3 moved

- **Modal chart axes read navy-grey, and the signal row clears the footer** (RB3C1-AC3 MET). Round 2's RB2M4-AC3 is cured.
- **Index Performance was read live** (RB3C2-AC2 MET). W10-S1's disarm condition is met.

## 2. Open

1. **Inactive period chips in the modals read white on silver**, from `text-white/60` at `IndexPerformanceModal.tsx`:140. This
   is the alpha-variant family already named in W8-S14.
   - Fix as a CLASS, not a file: sweep every `text-white/<n>` and `bg-white/<n>` (and similar alpha variants of white) inside
     the shared modal frame's children, and map them to the frame's ink tokens.
   - Proof: the sweep's before and after counts printed, and the computed colour of one inactive chip read in a walk.
2. **W10-S2 (ARMED): RSIModal cannot be opened by a labelled control,** so its live read waits.
   - The issuer either opens it through its real trigger (a chart-bar press at a known coordinate in a scripted walk) or, if
     no control reaches it, says so.
   - An unreachable modal is a FINDING for Andrew's walk, not a pass.
3. **FWD-1 (laptop call `3c44`), Andrew's look:** still open. The FWD-5 walk starts on his YES.
4. **FWD-4 (heat maps, `be0b`):** still waits on his design call.

## 3. ENRICHMENT LIST for round 4 (one issuance; C-BRANCH binds)

1. The alpha-white class sweep across the modals (2.1).
2. The RSI live read through its real trigger (2.2).
3. On Andrew's YES to `3c44`: the FWD-5 walk. Until then, the issuer cuts nothing beyond 1 and 2.
