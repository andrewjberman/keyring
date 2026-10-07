# IRPT_YCDGEN PRD v0.9 -- ratified-text half review (L4-R)

**archetype:** VALIDATE

Reviewer: `3.0.0_SA_CVO` (seated on dell2; NFRA_CTLPLN ADDENDUM v0.12: the CVO on a Dell signs the PRDs that Dell's CTO lane writes),
2026-10-07 ~08:5xZ. Subject: `org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md` v0.9 @8499df49ce (`1.0.0_SA_CTO~DELL2`), read as
the diff against v0.8 @4bc1b9aff1. Asked by msgs 168 and 169.

**Verdict: SIGN.** One coverage finding, which does not block (P2).

## What changed in the ratified text

- ENDPOINT: FWD-17 to FWD-23 appended; FWD-1 to FWD-16 byte-unchanged in the diff. `endpoint_outcomes` lists 22.
- CONTRACTS: none changed. The traceability table gains S33-S39, one per new outcome; the MECE line now reads 22 of 22.

## Checks

1. **Each new outcome traces to the brief.** Brief `docs/briefs/irpt-check-swap-ai-autosuggest-ux-brief-20261007.md` @c16f0f8ddd,
   table at :169-179. FWD-17 = O1/R1; FWD-18 = O2, O4/R2; FWD-19 = O3/R5; FWD-20 = O5/R6, R9; FWD-21 = O6/R4; FWD-22 = O7/R3;
   FWD-23 = Part VIII/R12. O1 to O7 are all carried.
2. **No outcome is a wait.** Each DONE WHEN is an act a seat can take on demand. FWD-22 drives the failure deliberately ("the check is
   made to fail"). FWD-23 is APPLIED, provable by a read that no screen offers a free-text bypass.
3. **ACCEPT lines are observable and keep the guard.** FWD-18 "nothing is accepted unless the advisor chose it"; FWD-17 asks for a
   reason in words, and S33 holds back a numeric confidence until it is calibrated (brief R1); FWD-20 forbids calling a typo fix a
   stand-in.
4. **The Andrew-direct citation reads true at its bytes.** Record @1ea0796be2,
   `ANDREW_DIRECT_20261007_080xZ_CRO_RESEARCH_ARM_AI_SWAP_AUTOSUGGEST_CHECK_SWAP_UX.md:10` reads "I am more intrigued in AI
   functionalities for autosuggesting swaps of unrecognized securities and associated frontend ops for that process."
5. **No vendor act is introduced.** R11 (the web-search swap) is left out, as the brief recommends; packet 2 is superseded by S32.

## Finding (P2, not blocking)

**R7 and R8 have no carrier, although section 8's new coverage row says "O1-O7 and R1-R12" are carried.** R7 is one row-centric list,
removing the duplicate findings bullets and leading with "fix below". R8 is saying once, not twice, what the resolve is doing. Both are
TODAY-sized in the brief (brief :175-176). Neither has an FWD or an S row. Either FWD-18's cell takes them (they serve "clears every
flagged row quickly"), or the coverage row names them as left out. This is a wording fix under the ENDPOINT hash only if it lands in
section 8 or the traceability table.

## Not checked

The brief's measured claims (file and line citations in S33-S39) were not re-read; they are the brief's and the cells will meet them.

-- 3.0.0_SA_CVO
