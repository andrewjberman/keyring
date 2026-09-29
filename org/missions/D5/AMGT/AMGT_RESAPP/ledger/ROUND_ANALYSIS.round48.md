# AMGT_RESAPP -- ROUND 48 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~21:1xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26706, READ-acked, subject *"L10 slug AMGT_RESAPP round 48 @33ed750433"*,
citing `surprise-channel/adjudications/ADJUDICATION_v58.md`. Issuer packet: `round48/DRAIN_END_PACKET.md` @`da5e2356ac`.

**Round 48 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **Round 47's merged work is SERVED.** `ww-1` landed and closed on the canonical `research_dossier/` prefix, with ONE
  `dynamodb:GetItem`.
  - CodeSha256 `lg6NJ2JL...B3s=`, LastModified 19:18:58Z (the CVO re-read it).
  - The basis-true formula and "Historical-multiple reference" label (`vv-1`), the team's cases (`vv-2`), the served company
    name and classification on list rows (`ww-2`), and the export's words from one served definition (`ww-4`) are live.
  - `ww-3` wrote 59 rows to `etf-classifications` (285 -> 344).
- **The API suite is green on the full tree:** 323 passed (the CVO's run).
- **The 33 FWD-30 NOT_OK are PROVEN page-side by a controlled run (`Z-S305` GRADUATED).**
  - With the page set back to round 45, 95 of 95 absences and figures are equal. The only difference is the one served
    case line per name, which round 45's page predates.
  - `ww-1` is exonerated by measurement.
- **`Z-S303` GRADUATED.** Hitachi 6501 JP has no identity in `crosswalk/v1`, whose newest vintage is 2026-09-25; the
  folder was created 09-29. The deployed route is never invoked for it.

## 2. RULINGS

1. **FWD-30 has ONE grader, and it keys on the page's data attributes, never its wording (`Z-S297` / `Z-S305`).**
   - Round 47 named one writer per artifact (the page harness is DSGN_AMGTV1's, `render_pack.py` is AMGT_RESAPP's). But
     this round's grade came from a third instrument, RESAPP's `round45/checks/sweep.py`, which still matches the page's
     WORDS. The CVO measured that no portal vintage reads 96 of 96.
   - **Ruling:** `sweep.py` stays AMGT_RESAPP's and is FWD-30's one grader. It re-keys every page read on the page's
     stable data attributes, never on visible text. The page already carries them on DEV: `data-model-row`,
     `data-model-cell`, `data-model-refused`, `data-model-case-status`, `data-model-case-reason`, `data-cite-resolved`,
     `data-posture-*`, `data-exec-officer`.
   - DSGN_AMGTV1 then owns wording freely, and the grade stops moving each time DSGN rewrites a sentence for a PM. Where an
     absence has no attribute, RESAPP ASKS DSGN_AMGTV1 through DSGN's round for one, never by a direct page edit.
   - `exportCompare.harness.cjs` stays DSGN's own page-side check. It is not FWD-30's grade.
2. **The sweep's `reason` field names CASES** (CVO observation 2). A cases-only NOT_OK must say so. Folded into cell 1.
3. **Hitachi 6501 JP: routed to AMGT_CORPUS round 15** as a crosswalk row for any library folder newer than the crosswalk's
   newest vintage. The identity store is CORPUS's. Until then FWD-30's denominator is 95 identified names, printed beside
   the 96 folders.
4. **Record hygiene (packet item 4):** an amendment commit that says "no gate limb graded it" must be checked against GATE
   (viii), which grades a MODIFIED order that declares `<placeholders>`. Noted to 2.0.0_SA_COO~Z. No cell.
5. **DSGN_AMGTV1's two producer asks** (its round-4 analysis @177c576c80 s.2 ruling 5) are cut here as cells 2 and 3.

## 3. FWD GRADES

- **`FWD-30`: NOT REALIZED.** No vintage passes until cell 1 re-keys the grader. The export side is correct by the
  controlled run.
- **`FWD-12` (render half) and the team's cases on the page:** SERVED since 19:18Z. Graded on the next walk, which is
  DSGN_AMGTV1 round 5's.
- The others stand as `ROUND_ANALYSIS.round46.md` left them.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~Z` cuts for round 49 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **FWD-30's grader keys on data attributes and names CASES** | LOCAL plus a live read. `sweep.py --served --live --require-cases` matches absences, figures, cites and cases by the attributes above. At HEAD page `09bd04b1`, or later, against the served export, it reads **95 of 95 identified names equal** (Hitachi printed as unidentified, not failed). The `reason` column names the failing class, cases included. A planted wording change on one page line must NOT move the grade (the positive control that the key is the attribute). At most 3 mechanical criteria. |
| 2 | **The served company name on the rank-history series** (DSGN FWD-3 labels) | SERVED under a never-widen pair. The name is joined server-side the same way `ww-2` joins it on list rows. The expected outcome is read from the join rule at signing. |
| 3 | **Officers from a second filing when the 10-K's officer section is absent** (DSGN FWD-7) | LOCAL first cut. When the 10-K's Item 10 lists no officers (or incorporates them by reference), the officer list is read from the company's latest proxy statement (DEF 14A) through the SAME filings path already in use, with no new vendor. It is proven on the walked no-officer name (filing 0000896878-26-000037). A census over the 95 names prints how many gain officers, with the denominator. Serving it is round 50's, under a pair. |

**Fan-out:** 3, independent.

**NOT cells:**
- the Hitachi crosswalk row (AMGT_CORPUS);
- the page's wording (DSGN_AMGTV1);
- `Z-S302`'s seed-script guard (INERT, and the BD script owner's).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- None new. The CLOUD push's remaining 4 conflicts sit with him through 0.0.0_AB_MSTR~Z (record @d0e74747a9). None of
  those files is this project's.

## Compiler Tools

- The CVO's v58: its controlled two-arm FWD-30 run, its crosswalk census, and its full-tree api-suite run (323 passed),
  taken as measurements.
- This seat: `git -C portal grep` over `src/pages/SecurityAnalysis` on DEV for `data-*` attributes (top 30 by count).
