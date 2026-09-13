# AMGT_RESAPP -- ROUND 2 ANALYSIS (L10, 1.0.0_SA_CTO~Z)

**archetype:** SCRIBE (ledger) · **written by** `1.0.0_SA_CTO~Z` · **2026-09-11**

| | |
|---|---|
| **Answers** | the L10 slug `surprise-channel/remediations/REMEDIATION_v2.md` @`b3acbcf3dd` from `3.0.0_SA_CVO~Z` (msg this tick); ADJUDICATION_v2 + CVO evidence JSON ride the same pin; drain `56c755b86a`; artifacts pinned `9a2e542c0b` |
| **Graded against** | each round-1-routed DEFECT's fix, not an FWD realization (surfaces remain DESIGN_SPEC-gated) |
| **Routes to** | `2.0.0_SA_COO~ZZZ` (round-2b recut of the 3 failed fixes + 2 new source findings) · `0.0.0_AB_MSTR~Z` (the repo-ignore hygiene item) · Andrew (round 3, unchanged) |

---

## 1. THE VERDICT: a DEFECT-FIX round -- 2 of 5 fixes LANDED, 3 FAILED, and the CVO's control found 2 MORE

Round 2 was the defect-fix round for the five defects round 1's analysis routed. It is NOT an FWD-realization
round -- every FWD still needs an EXERCISED surface and no `.tsx` exists, so **0 of 14 FWDs newly REALIZED**,
unchanged from round 1. The grade is the FIXES' correctness. 21 of 21 orders terminal, 21 of 21 proof
instances VALID, 15 existing tests pass, both-root rollup 28 investigations / 0 undispositioned / 0 defects.

| round-1 defect | cell | AC | CVO grade | disposition |
|---|---|---|---|---|
| fiscal-year join (W1-S2) | r-1 | AC4 | **PASS** on the 30-row sample | LANDED, but carries C-S8 (text) + C-S15 (source defect) + C-S16 (not integrated) |
| SA re-run (s-4) | r-4 | AC5 | **PASS** | LANDED, with C-S9 (population naming) |
| check-face salience (s-10) | r-10 | AC4 | **FAIL** (C-S12) | re-cut |
| identity coverage (s-12) | r-12 | AC4 | **FAIL** (C-S13) | re-cut (doc) + Andrew fallback decision |
| impostor AND-clause (s-15) | r-15 | AC4 | **FAIL** (C-S14) | re-cut |

⭐ The measured workbook gain is REAL and correctly bounded: **34 distinct MEASURED identifiers, up from 32**
(IMB LN/IMPERIAL BRANDS, SAP GY/SAP SE named in the original workbooks). The CVO's discipline holds the line
that the failed r-12 document must NOT turn 15 hypothetical INFERRED candidates into 15 measured gains.

## 2. THE THREE FAILED FIXES (routed to a round-2b recut; NONE is DESIGN_SPEC-gated -- all are pre-surface correctness)

- **r-10 check-face (C-S12, BLOCKING).** The fix added a second trailing text tag (`12345 [PROVISIONAL]` ->
  `12345 [PROVISIONAL] [WARN]`) -- another plain suffix on the same number-first presentation round 1 already
  rejected; no color, glyph, leading status or visual-prominence change. And the test compares DIFFERENT
  values (500 vs 12345), so string-inequality never proved the marker made the difference. **Re-cut: a visibly
  salient warning in the permitted print fixture (no .tsx needed -- S5's render_print.py), comparing the SAME
  number under PASS vs PROVISIONAL; regrade AC4 before FWD-10 is treated realized.** The token contract
  (green/OK, amber/WARN, red/BLOCKED) passed and carries forward into the eventual approved design.
- **r-12 identity note (C-S13, BLOCKING).** The measured-source limb PASSED (34 distinct MEASURED). The
  DECISION NOTE failed: `DESIGN_QUESTION_identity_fallback.md` promises "MEASURED-or-better 34->49" while
  limiting all fallback values to INFERRED -- categories that cannot share one denominator -- and treats
  hypothetical renaming as a measured failure. **Re-cut (doc): correct to 34 MEASURED + up to 15 INFERRED
  candidates, separate observed ambiguity from hypothetical renaming, name which downstream gates still refuse
  INFERRED. Keep the fallback UNIMPLEMENTED pending Andrew's decision.**
- **r-15 impostor predicate (C-S14, BLOCKING).** The advertised impostor AND-clause executes as `check1 OR
  check2` and returns official immediately; the 8-case enumeration admits check2-alone and check1-alone, and a
  non-identity-bound verification mark plus a copied bio still passes. **Re-cut: clarify the intended truth
  table and the identity meaning of "verification"; require the co-occurrence where intended; add negative
  controls for verification-without-further-evidence and for a mark that does not attest company identity. Keep
  all real handles UNRESOLVED; no social/vendor call authorized** (that is an Andrew per-use word, round 3).

## 3. TWO NEW SOURCE FINDINGS ON r-1 (the CVO's independent control -- L8/L9 working), + one repo-hygiene item

- **C-S15 (BLOCKING) -- the fiscal join can select a FUTURE price.** `fye_join._nearest_price` falls back to
  the nearest point in EITHER direction and `gap_days` uses `abs`, so a period_end 2025-12-31 with only a
  2026-01-02 price returns that future price at gap_days 2 and passes the under-45-day check. ⭐ ALL 30 live
  served rows have ZERO such violations at this vintage -- a BOUNDED SOURCE defect, not a fourth live failure.
  **Re-cut with r-1's integration: return UNRESOLVED when no on-or-before price exists; add a future-only
  negative control and a direction assertion.**
- **C-S16 (OBSERVATION) -- r-1's corrected block is not wired to consumers.** `derive_fye_fixed.py` writes
  `derived/model_block_fye/`; the provenance/print consumers still read the original `model_block` lane (r-1
  explicitly excluded replacing them). **Re-cut as integration: name and test the consumer path + its derived
  vintage before claiming the served pack uses the corrected join.** So r-1's fix is CORRECT on the sample but
  NOT YET the served figure -- do not report the fiscal alignment as live until C-S15 + C-S16 close.
- **C-S8 / C-S9 (OBSERVATION, INERT) -- correction-notes, no re-cut.** C-S8: the r-1 order text implies a mapped
  `FISCAL_YEAR_END` field, but that field is BAD_FLD; the join correctly uses the fundamentals row-date --
  correct the order/analysis text, do not imply a mapped reference field. C-S9: the SA population is
  BABA/BA/COST (18 raw keys), not the order's BABA/RTX/+1 -- correct future cuts to the actual denominator. Both
  are "correct the words" items; the WORK is sound.

## 4. THE ONE ITEM ROUTED TO ME, AND MY ACT

- **C-S10 (ARMED, disarm_owner me) -- the root `.gitignore:47:lib/` still hides FUTURE untracked lib source.**
  All five new modules ARE tracked (`git add -f` via safe-commit; `ls-files --error-unmatch` confirms), and the
  issuer disarmed this round's omission exposure -- so nothing is lost NOW. The residual DISCOVERY defect (a
  future untracked lib file is invisible to ordinary `status`) is repo-tree hygiene, **not** AMGT_RESAPP's to
  fix and NOT a second independent defect (it is the same class as round-1 W1-S3, kept linked). **My act
  (driver's own lane): routed to `0.0.0_AB_MSTR~Z` as the repository owner** -- a scoped source-tree ignore
  correction or an explicit tracked-plus-ignored enumeration; a bare `!lib/research/` under an ignored parent
  must not be assumed sufficient. The disarm rides that routing.

## 5. FWD STATE + ROUTING

**No FWD grade changes** -- all 14 remain NOT_REALIZED because every one needs an EXERCISED served surface and
none is built (round-1's finding, unchanged). Round 2 improved the pre-surface CORRECTNESS the surfaces will
rest on; it built no surface.

**Round-2b recut (`2.0.0_SA_COO~ZZZ`, ONE issuance):** the three failed fixes (r-10 salience, r-12 doc, r-15
predicate) + the two new r-1 source findings (C-S15 direction, C-S16 integration). ⛔ **None is
DESIGN_SPEC-gated** -- they are print-fixture / doc / logic / source correctness, doable now without a `.tsx`
and without Andrew's design approval; only the surface EXERCISE (round 3) waits on him. C-S8/C-S9 fold in as
text corrections. The recut is NOT a reset: round-1 OPEN obligations remain historical and open.

**Round 3 (surface build) stays gated on ANDREW, unchanged:** DESIGN_SPEC approval (the pivot, folded in my
synthesis @`79b48a9298`), the social/model per-use word (r-15's handles, S13), the drafting-model word, the
peer quota (S8), and the list owners (S15). FWD-15 (the Lead Panel) is minted at that boundary.

**Push state:** LOCAL at write time. `0.0.0_AB_MSTR~Z` pushes.
