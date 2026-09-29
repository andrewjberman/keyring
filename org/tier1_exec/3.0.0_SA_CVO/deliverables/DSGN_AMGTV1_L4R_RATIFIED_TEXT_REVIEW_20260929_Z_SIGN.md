# DSGN_AMGTV1 -- L4-R RATIFIED-TEXT HALF (ENDPOINT + CONTRACTS) -- REVIEW, VERDICT SIGN

**Seat:** `3.0.0_SA_CVO~Z` (the project's CVO, `project.json` leads.cvo) - **Written:** 2026-09-29 ~03:1xZ
**Reviewed:** `org/missions/D13/DSGN/DSGN_AMGTV1/prd/DSGN_AMGTV1_PRD.md` v0.1 @`4df8bc2cd3`, ratified-text half_hash
`c3c47a67ff56383cd03daa712e1df1029770f10e07a686100c99a7a7de63b363` (computed by `prd_signoff_lib.half_hashes` on the HEAD
bytes). Asked by `1.0.0_SA_CTO~Z`, msg 26407. PROPORTIONATE: a new project, so this half is signed once, and only an ENDPOINT
change re-opens it.

## VERDICT: SIGN, with two conditions for v0.2 that do not block L5

Neither condition changes an outcome. Both are wording the CTO lands at its next header bump.

## WHAT WAS CHECKED, AND WHAT IT READ

1. **The ENDPOINT landed from its source, with ONE difference.** The PRD's block was diffed line-by-line against
   `DSGN_AMGTV1_ENDPOINT_FORWARD_20260928.md` @`3d7fc6695e`: 96 of 96 lines, and **1 differs**. FWD-3's ACCEPT dropped its
   closing sentence *"The form is Andrew's call (fork F1)."* The drop is justified, because F1 is ruled in C-FORKS @`ac5433b35b`.
   But the header says "Landed verbatim". **CONDITION 1:** say "verbatim except FWD-3's fork-F1 sentence, removed because F1
   is ruled", so a later verbatim check does not read an unexplained edit.
2. **Every outcome is an act a seat can take on demand (Rule 27 L2, NO FWD IS A WAIT).**
   - FWD-1 names Valero in *today's* Trending x Price list, which is a daily population. Measured now through
     `scoped_amgt.read_rankings('trending', 'price')`: state COMPLETE, 32 rows, **`VLO_US_Equity` present**. The walk is
     available today. The brief (:62) says why Valero is the name: its tabs carry content. ⚠ Membership moves daily. If Valero
     leaves the list on the day of the walk, the outcome cannot be exercised as worded. That is a named risk, not a refusal.
   - FWD-1's "signed in with a real account" is not a wait on Andrew: the brief itself came from a seat's signed-in `/ui-walk`
     (CRO~Z record, PRD :17), and Andrew's 02:2xZ word is that nothing waits on him.
   - FWD-7's officer fallback reaches a roster without vendor egress at the dossier leg (F3 order: filing -> dossier ->
     vendors), so it does not depend on a per-use word.
3. **The contracts agree with the outcomes.** C-PRESENTATION-ONLY ("the page does not convert a currency, rank, classify") agrees
   with FWD-4 ("every money figure in the company's own currency") through the C-ASKS row "every money figure carries its
   currency". F2 (classification from `etf-classifications` only) agrees with FWD-2. F5 (presentation here, payloads at
   AMGT_RESAPP) is the same line C-PRESENTATION-ONLY draws.
4. ⚠ **ONE CONTRACT-OUTCOME TENSION -- CONDITION 2.** C-PRESENTATION-ONLY says a missing field "renders as a designed empty
   state naming what is missing **and whose it is to fill**". FWD-11 says "no raw code, id or storage path shows anywhere on the
   page". Rendered literally, "whose it is to fill" is a project code or a seat serial (`AMGT_RESAPP`, `2.0.0_SA_COO~Z`), which
   is exactly what FWD-11 forbids a reviewer to see. **CONDITION 2:** the empty state names the owner **in words a PM reads**
   (for example "the research data team"), never a project code or serial. Otherwise the page can meet C-PRESENTATION-ONLY
   only by failing FWD-11.
5. **Cross-fabric dependency is stated honestly.** The C-ASKS row for DSGN_REBRND's white-ground header/footer variants is marked
   "WAITED ON, never driven here", which respects the fabric boundary the per-member exception creates.

## BOUNDS

- The ENDPOINT's SOURCE line references (brief :54-124, memo M-numbers) were spot-read at O1 only (brief :54-62), not all eleven.
- This review is of the ENDPOINT and CONTRACTS text. It does not grade THE THREAD, PATHS or SURFACE MANIFEST, which sit outside
  this half.
