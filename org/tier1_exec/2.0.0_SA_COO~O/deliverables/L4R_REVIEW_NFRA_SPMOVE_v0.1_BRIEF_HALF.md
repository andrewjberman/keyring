# L4-R review -- NFRA_SPMOVE PRD v0.1, BRIEF half -- REFUSE

Reviewer: `2.0.0_SA_COO~O`, in `4.0.0_SA_CRO~G`'s stead (no live CRO session; this seat holds neither this
project's round nor `NFRA_MCPINDEX`'s brief half, so the spine's disqualification does not apply).
Delivered by `1.0.0_SA_CTO` msg 97664. PRD `org/missions/D9/NFRA/NFRA_SPMOVE/prd/NFRA_SPMOVE_PRD.md` v0.1
@`aad379d84b` (128 lines). Brief `docs/briefs/schwab-trn-sharepoint-export-brief-20260916.md` @`d5e870fed2`
(232 lines). Reviewed 2026-09-17 ~21:3xZ.

## VERDICT: REFUSE -- two items, both cheap

This is not a disagreement with the design. The CONTRACTS section is strong and carries most of the brief's
substance as content rather than pointers (verified below). The half is refused because the ONE INSTRUMENT the
brief half is reviewed with does not exist in the PRD, and because the brief's only quantitative substrate is
missing at the exact contract that needs it.

### ITEM 1 -- there is no BRIEF COVERAGE section, so carriage cannot be reviewed at all

The review question for this half is: does every brief entry carry its section's CONTENT into a consuming
decision or cell, or carry `NOT CONSUMED` with its reason, against a heading denominator measured at the
brief's pin. The PRD's sections are `Authority and project arc`, `Scope and evidence boundary`, `ENDPOINT`,
`CONTRACTS`, `SURFACE MANIFEST`, `Acceptance matrix`, `Canonical handoff` -- there is no coverage section and
no denominator anywhere in the file (`grep -n "^## "` over the PRD, 7 sections, 0 named coverage).

Measured at the pin for whoever writes it: `git cat-file -p d5e870fed2:docs/briefs/schwab-trn-sharepoint-export-brief-20260916.md`,
fence-aware, gives **22 headings** -- the title (`:1`), `ANDREW'S WORDS` (`:11`), Parts I-VII (`:42`, `:71`,
`:91`, `:102`, `:163`, `:184`, `:192`), outcomes O1-O6 (`:44`, `:48`, `:52`, `:56`, `:60`, `:64`), substrate
4.1-4.5 (`:104`, `:117`, `:127`, `:142`, `:153`), `s.8` (`:205`) and `REFS` (`:217`). Absent the table I cannot
certify the entries I did not sample, and a reviewer's sample is not a denominator.

### ITEM 2 -- PART IV.5's measured sizes are not carried into C4, the contract that needs them

The brief's 4.5 (`:153-159`) is its only built measurement: at 140 columns and 134,387 rows, the xlsx is
**45.4 MB written in 158 s** (44-column CSV 47.3 MB / 1.4 s; 44-column xlsx 19.6 MB / 63 s), and the largest
month so far, 2025-12 at ~213k rows, is **~72 MB INFERRED, not built**. C4 carries only "a binary workbook of
tens of MB replaced daily". That phrase does not decide a chunk size, a timeout or a host: 158 s of write time
and a ~72 MB ceiling are the numbers the bounded upload capability is designed against, and the inferred one
must arrive labelled inferred. Carry them into C4 (or into C1 and cite them from C4), with 4.5's own
provenance -- built vs scaled.

## WHAT I VERIFIED AS SOUND, so the re-review is short

Sampled the brief's substantive findings against the PRD, reading both sides:
- **4.1 the data -> C1.** All 140 source columns, per-master files, nothing de-duplicated, rebuilt from silver:
  carried, and the 99.98% overlap is named in Scope as expected rather than a defect.
- **4.2 the trigger -> C2.** The marker path `schwab/{master}/meta/complete/date=YYYY-MM-DD.json`, the
  ~15-minute lag, and BOTH measured irregularities (the 2026-09-11 second-fire marker, the 2026-09-15 rewritten
  zero-table marker) are carried as design input, with A7 grading the whole-month-or-no-change rule. This is the
  strongest carriage in the document.
- **4.3 the address -> C3.** Builder output, the `AWS/` + builder's key mirror rule, the measured fact that
  `NAMING_SCHEMA.json` carries no SharePoint grammar, the LGIC_NAMING route rather than a rider on
  LGIC_ENFORCE, and the tier question left to L5: all carried.
- **4.4 the destination -> C4 + Scope.** The existing `upload_text_to_site` writing small text and never
  overwriting, the new bounded replace-under-`AWS/`-only capability, version history as rollback, and the site
  choice `sites/OpalCapital` flagged as this seat's reading CONFIRMED AT L5: all carried. The
  not-vendor-egress point is carried in Scope.
- **Marker vintage.** "Markers exist only from 2026-08-31, so earlier behaviour is UNMEASURED" is carried
  verbatim in the evidence boundary.
- **O1-O6 -> FWD-1..FWD-6 and A1-A8.** Each outcome has an acceptance row, and A7 and A8 cover C2's
  irregularities and C4's path bound.

## NOT COVERED BY THIS REVIEW

The RATIFIED-TEXT half (ENDPOINT and CONTRACTS) is `3.0.0_SA_CVO`'s; nothing here signs for it. Nor does this
review judge the site choice, the tier question or the SharePoint grammar's shape -- all three are correctly
deferred to L5 by the PRD itself.

## RE-REVIEW

Add the coverage table against the 22-heading denominator above, and carry 4.5's numbers into C4. I will
re-review on the bump; only the brief half's bytes need change.
