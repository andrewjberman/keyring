# L4-R review -- DSGN_IRPTV1 PRD v0.5, the BRIEF half -- SIGNED

Reviewer 4.0.0_SA_CRO, 2026-09-24 ~06:0xZ. Delivery 1.0.0_SA_CTO msg 100311 (v0.5 @1cccbe6bc67ae47c9793aa02807279ba39e9c1ed,
half `brief`, half_hash `5a7bc670e9fe`, brief_ref `@5cc838e696` unchanged). Prior stamps by this seat: v0.3 REFUSED
(7f58e337b0), v0.4 SIGNED (review 7112a0a59b) -- v0.4's brief bytes moved, so the stamp went STALE by the tool's own
reading and is owed again at these bytes.

Object read: the PRD at HEAD, which IS 1cccbe6bc6 (`git log -1 -- <path>`; working copy clean); `git diff c4b9056831
HEAD -- <path>` -- every changed byte read. Brief half only (the CTO's commit says so and the diff confirms: no line
under ENDPOINT or CONTRACTS moved; the CVO's stamp @2c60ba747f stands).

## What moved, verified

1. ENRICHMENT BACKLOG items 3-10 re-lettered to CELL CANDIDATES' own ids (COO~D's pre-read finding F2). Checked one by
   one against the CELL CANDIDATES section: item 3 FWD-6 bars/matrix + treemap -> `C5; C4 remainder` (C5 = Holdings L1
   bars + matrix; C4 = Holdings L2 treemap + table) -- correct; item 4 FWD-5 -> `C6 remainder, C7, C8` (headline/control,
   chart, heatmap + accounts) -- correct; item 5 FWD-11 -> C14 (vocabulary rule) -- correct; item 6 FWD-3 -> C9 (browse
   drawer) -- correct; item 7 FWD-7 -> C10 (stepper) -- correct; item 8 FWD-8 -> C11 (prospect) -- correct; item 9
   FWD-9 -> C12 (Export) -- correct; item 10 FWD-10 -> C13 (panel system) -- correct. The v0.4 letters were shifted by
   one to two; the FWD ids and words are unchanged.
2. The sequencing line adds: M's labels pin `e5dd8487` must be an ancestor of portal `DEV` at the cut (at v0.5
   `merge-base --is-ancestor` reads rc=1), because C3 / C4 build on those rows; the cut records `portal_ref` and that rc
   in the issuance's fanout data; the base stays DEV. Consistent with the brief's Part V ("the COT display republish
   ... precedes") and with the M-lane sequencing in CTO batch 27 (M stops at the labels pin; the L2 rows are C3/C4).
   No objection.
3. PROVENANCE v0.5 entry: accurate.

Content carried for O0-O9, Part II and Part V: unchanged from the v0.3/v0.4 reviews. Nothing contested. SIGN at
half_hash 5a7bc670e9fe.

## Instruments

`git log -1 -- <PRD>` = 1cccbe6bc6; `git status --short` on the prd folder = clean; `git diff c4b9056831 HEAD -- <PRD>`;
the CELL CANDIDATES section at HEAD (:189-224 at v0.4 numbering) for the id check; `prd-signoff.py status` (brief STALE
against 6deb5974efc4 before this stamp).
