# AMGT_RESAPP -- ROUND 52 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~12:5xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 27141, *"L10 slug AMGT_RESAPP round 52 @108fb01895"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v62.md` (read to EOF, 8,230 B). Issuer packet: `round52/DRAIN_END_PACKET.md` @`54f5805c8d`.

**Round 52 is CLOSED:** 6 of 6 terminal; `Z-S312`/`Z-S311` GRADUATED; `Z-S314` CARRIED ARMED to its owner's cell; 1 of 1 judgment
criterion graded. **The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **ab-6, the one build + the ASML splice.** Live CodeSha256 `nKWCfQRQ...` (11:43:22Z).
  - **ASML's `thesis_driver_chart` is SERVED from `filing`.** The round-51 unmet (zz-8 AC2) is now met, and `Z-S312`/`Z-S311`
    graduate.
  - This seat's ab-6 half traced that branch before the act (the exact join matched none of 419 figures).
- **6501:** `/thesis` serves the full `dossier_fields` block ABSENT with reasons (ab-2).
- **ab-3, the page-FWD map (L9): PARTIAL, 8 of 9.** FWD-27's relation does not follow from its two quotes (controls vs footers).
- **FWD-30 is NOT gradeable at close.**
  - All 131 `val_differ` lines are header cells read as displayed figure + tooltip text, a parsing gap DSGN round 12's hover
    figures opened; `val_unscaled` is 0.
  - It is not a value move.

## 2. RULINGS

1. **Addendum C's FWD-27 placement line is amended in place, per the addendum's own condition** (PRD v0.30, this commit).
   - It now reads "FWD-27 -> DSGN FWD-18 (no DSGN owner before v0.4)", as the CVO's L9 requires.
   - The obligation is unchanged: FWD-27 was carried whole to DSGN FWD-18.
   - This is a wording change under an unchanged ENDPOINT obligation. Under PROPORTIONATE sign-off the re-sign is a formality and
     withholds no delivery.
2. **FWD-30's grader reads the DISPLAYED figure, never the cell's whole text.** The fix is paired with a planted tooltip cell that
   must not change the read. FWD-30 is graded again only on that grader.
3. **`Z-S314` (a live `--rebuild-pool` regresses served `/thesis` sentences) stays ARMED with `2.0.0_SA_COO~Z` as disarm owner.**
   - Its cell: the regeneration keeps every served sentence, and its AC counts served sentences before and after on the names where
     round 52 measured the drop.
   - No scheduled task invokes the producer (the CVO scanned 208), so only a manual run reaches it. It is still disarmed by fixing
     it, not by that absence.
4. **THE NEXT SCOPED-API BUILD IS THE SLASH-KEY WINDOW, and nothing else may deploy from HEAD before it.**
   - Since the deployed pin `a1a70e00eb`, `scoped_amgt.py` carries CORPUS z-4's slash-safe READERS (it builds pool paths with
     `crosswalk.slash_safe_key`). `timeline_api.py` carries `q-5`'s found-codes reader (`91b74a9047`).
   - A HEAD build deployed before the 30 raw-slash objects move would make BP/_LN and NG/_LN read at encoded keys that do not exist
     yet.
   - **So the build that carries `91b74a9047` is the SAME act as CORPUS's 30-object copy:**
     - ONE never-widen pair, whose legs are (a) copy the 30 objects to their encoded keys, then (b) deploy the build;
     - cut by `2.0.0_SA_COO~Z`, with `2.0.0_SA_COO~X` supplying the object list and its before-state;
     - the raw objects are kept.
   - This is CORPUS round-23 ruling 2's single window, placed here because the deploy is this project's.

## 3. FWD GRADES

- **FWD-21..FWD-29: RE-HOMED** to DSGN_AMGTV1 FWD-12..FWD-20 (PRD v0.29 s.C.1). They are graded there, never here.
- **REALIZED: FWD-9, 13, 24, 25, 26** hold (24-26 as of their pre-re-home grades; their properties now live at DSGN).
- **FWD-30: met on its served instrument at round 51.** It is ungradeable after DSGN round 12 until the grader fix (ruling 2). Its
  person-act clause (Adam's forward) stays unmeasured.
- **FWD-18 (the driver chart): the ASML chart is SERVED** from the filing branch. It is graded REALIZED at the next FWD sweep, once
  read on the page.
- The remaining unmet and unmeasurable outcomes are as round 51.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~Z` cuts for round 53 in ONE issuance

| # | cell | risk | note |
|---|---|---|---|
| 1 | **FWD-30's grader reads the displayed figure** (ruling 2) | LOCAL | The AC re-runs the sweep: `val_differ` 0 on the 131, and a planted tooltip cell leaves the read unchanged. |
| 2 | **`Z-S314`: regeneration keeps served sentences** (ruling 3) | LOCAL | The AC counts served sentences before and after on the round-52 drop names. It disarms `Z-S314`. |
| 3 | **The slash-key window:** copy the 30 objects to encoded keys + deploy the scoped-API build at a pinned HEAD carrying z-4's readers and `91b74a9047` | WORLD, ONE pair (ruling 4) | Expected: BP/_LN and NG/_LN read at encoded keys with byte-equal bodies, `/timeline` serves `publishers_found_codes`, and every other route is unchanged against a pre-capture. It waits for CORPUS round 24 cell 4 to drain, so every reader is routed. |
| 4 | **`Z-S315`: the `harvest.store` docstring** | LOCAL, text | |

**Fan-out:** 1, 2 and 4 are independent. 3 follows CORPUS's cell 4.

## 5. ACTS ONLY ANDREW CAN DO (cited)

- The portal DEV push and promotion [CLAUDE.md Portal].
- Adam's forward of the export: FWD-30's ACCEPT is a person's act [PRD FWD-30].

## Compiler Tools

- The CVO's v62: the live CodeSha256, the ASML `/thesis` read, and its reading of all 9 map rows.
- This seat read `git diff a1a70e00eb HEAD` on `scoped_amgt.py` (4 `slash_safe_key` reader sites) and `timeline_api.py` for ruling 4.
