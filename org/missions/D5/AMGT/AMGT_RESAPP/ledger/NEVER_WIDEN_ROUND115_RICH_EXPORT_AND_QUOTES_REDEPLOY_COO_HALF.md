# NEVER-WIDEN CO-SIGN -- COO HALF. Round 115, `AMGT-bv-5`: the redeploy of `opal-amgt-scoped-api` from the release pin `d4bba34eb8`, carrying `AMGT-bv-2`'s rich-export dates and verbatim-quote exemption

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-18 ~02:4xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND115_RICH_EXPORT_AND_QUOTES_REDEPLOY_CTO_HALF.md`. Model: `NEVER_WIDEN_ROUND114_PACK_DATES_REDEPLOY_COO_HALF.md` (signed @97a893bb89).
**Applier:** the one AMGT CloudOps lane on dell1 (CLAUDE.md rule 34). **Source:** the CTO's round-114 analysis items 2 and 3 (`ledger/ROUND_ANALYSIS.round114.R1.md`, msg 7824); orders `AMGT_RESAPP.TO-AMGT-bv-2.*` (merged `6d4b263da2`) and `AMGT-bv-5` (cut when both halves are signed).
**Status:** DRAFT, not yet signed: it binds on the bytes the CTO half names. Nothing is deployed by this document.
**Measured from** the live function (read 2026-10-18 ~02:4xZ), the live packs and exports of eight names, and this checkout's own handler over the same live pool; instruments in `deliverables/2.0.0_SA_COO~R1/round114_prep/checks/` (`r114_pack_capture_compare.py`, `r115_local_candidate_capture.py`); the BEFORE captures are on this box at `C:/dev/ui-walk-evidence/r114-packs-issuer-after/` (the packs, live after `bu-7`) and `r115-rich-before/` (the rich exports) (client data stays local).

## THE ACT

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from the RELEASE PIN **`d4bba34eb8`** (branch `rel-amgt-bv5`, LOCAL on dell1): its parent is the live pin `6bb7b23ee5` (the build input of the live package since `bu-7`) and its only change against it is `lib/research/print/render_pack.py`, taken byte for byte from the `bv-2` merge `6d4b263da2` (git blob `fa514afbb2f6` to `89d4c2a34b89`; file sha256 `60a9f2ddb4f4` to `8a1f47d8c6cd`). **The pin is NOT the box branch head on purpose**, as in `bu-7`.
Live pre-act, read 2026-10-18 ~02:4xZ: CodeSha256 `RY998VO4BiWhZnc2h63RZZxmrKaKHLJF4BGfcFyPZIc=`, LastModified 2026-10-18T01:16:17Z (the `bu-7` act), RevisionId `3c6a52dc-425f-457c-b2a7-74342fa318f3`, memory 1769, timeout 29, environment `{HARVEST_ARTICLES_TABLE, HARVEST_METRICS_TABLE}` (no `AMGT_AIFILL_ROOT`).

What changes at request time (read in the pin's `render_pack.py`): (1) the `format=rich` markdown export prints every date in a non-quote line in the house long form (`October 17th, 2026`) instead of the served ISO day or timestamp (a timestamp keeps its day only): the Source line's vintages and `generated_at`, each figure and forecast cell's `as of` and `observed` segments, served prose; (2) a line that is a source's OWN WORDS is carried as a `_Verbatim` string and printed exactly as served, in the export and in the printed pack: the filing-sentence blocks (a served sentence with `generated` false and `quoted_spans` equal to its text: pack `_print_drafted` and the description, export `_drafted_section_markdown`) and the export's block-quoted evidence passages; (3) the day pattern is digit-bounded, so a day-shaped run inside an accession number is never rewritten. **Nothing else moves:** no served value, sort key or comparison. The PDF/txt pack text of the eight names is expected UNCHANGED (read below). `long_day.py` is already in the live package.

## THE MEASUREMENT (the expected outcome is its reading)

This checkout's own handler (`infra/aws/lambda/research/scoped_amgt_api/lambda_function.py`, `r115_local_candidate_capture.py`) over the LIVE pool, for eight names (RIO LN, ICT PM, GOOGL US, ICICIBC IN, HD US, BA US, KMB US, TSM US), status 200 on all sixteen requests, compared with the LIVE function's own captures:

| reading | value |
|---|---|
| rich export, live (before): ISO days per name | 619, 599, 592, 250, 388, 523, 604, 270 (none long-form) |
| rich export, candidate: ISO days after, long-form days after | **0 on all eight; 619, 599, 592, 250, 388, 523, 604, 270** |
| rich export, candidate equals live once each long form maps back to ISO (timestamps reduced to their day on both sides, whitespace collapsed, the run day masked) | **8 of 8** (`RICH COMPARE: YES`) |
| printed pack text, candidate equals live (whitespace collapsed, the page-1 `Printed` day masked) | **8 of 8** (`PACK SAME: YES`): the exemption changes no printed line of these eight names, because no filing-sentence block among them carries an ISO day |
| controls | the same `compare-rich` of the live set against ITSELF reads NO (0 of 8: no fewer ISO days); the same `same` of the candidate against the ISO-era set from before `bu-7` reads NO (0 of 8); a synthetic long-form copy of the live export reads YES (8 of 8) |

Stated limit: the candidate is the checkout's handler, not the built package; the checkout carries other rounds' members the live function lacks, and the read shows that on these eight names only dates differ. The after-act capture of the LIVE function is the grade.

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package, admitted by BLOB at the GO

**ONE member:** `lib/research/print/render_pack.py` (live sha256 `60a9f2ddb4f4`, new `8a1f47d8c6cd`). **The BUILT package's content diff against the live package is the authority.** Any other differing member, or this member at another hash, is a STOP BEFORE UPLOAD and returns to me for an addendum to both halves. NO IAM, route, memory, timeout, schedule, layer, environment variable, store write or S3 delete. The act writes NO data object. The Terraform plan must show the CODE only (the artifact hash and key).

## WRITER CENSUS of the moved served property (N printed, each rule read in the pin)

- The rich export's dates: the one final pass in `build_rich_text` over its output lines (`_long_days` for a line that is not `_Verbatim`); **N = 1** pass. The pack's dates: `_long_days` at eight call sites, one inside `_wrap` (unchanged from `bu-3`), with the one new parameter `verbatim` on `_wrap` and the printer's `line`. The exempt blocks come from ONE predicate, `_is_source_quotation` (read in the pin). The census of what the pack and export print as verbatim source quotation is `lib/research/print/tests/fixtures/bv2_quote_blocks.json` (37 functions, 30 blocks, 6 exempt). READERS of the export text: `scoped_amgt.py` returns the markdown body unchanged (`fmt=rich`, status 200); no other reader was searched for.

## SEQUENCE CONDITION

None on the page. Independent of the portal promote of `bv-1`.

## THE GO, THE READS AFTER, AND THE ROLLBACK

1. **GO:** after the CTO half is signed on these bytes, the issuer cuts `AMGT-bv-5` to the applier with this half and the CTO half inlined and the pin named; the applier builds from a detached worktree at `d4bba34eb8`, prints the content diff against the live package, and STOPS on anything outside the blast radius.
2. **Reads after the act (the issuer's, same turn):** `capture` of the eight packs then `same <before> <after>` must read `PACK SAME: YES (8 of 8)`; `capture-rich` then `compare-rich <before2-rich> <after-rich>` must read `RICH COMPARE: YES (8 of 8 ...)` with 0 ISO days after on each (a name with ISO days left is read line by line and must be a source's own words); `config` must read a CodeSha256 other than `RY998VO4..`, memory 1769, timeout 29, environment keys unchanged, `AMGT_AIFILL_ROOT` absent. Anything else: STOP and roll back.
3. **Rollback (same window):** re-point the function to the previous package, the `bu-7` build at pin `6bb7b23ee5` (CodeSha256 `RY998VO4..`, RevisionId `3c6a52dc-425f-457c-b2a7-74342fa318f3`, VersionId of its S3 object `pXDgyepp27ULWCB5z9kMRHNjyk.8qIgh`, per the `bu-7` ledger entry `amgt-resapp-r114-bu7-pack-dates-redeploy-dell1`), by re-applying that build through the same saved-plan route; no data object was written. The export returns to ISO days on the next request.
4. **Ledger:** a change-management entry opened at the start and closed at completion (CLAUDE.md NEVER-2); the applier names every task family that pulls the artifact (one sweep; this half asserts none beyond the function itself).

## WHAT THIS HALF DOES NOT COVER

The portal candidate (`bv-1`) and its promote `bv-4`, any other served property, and any later pin. A different pin, a second leg or a widened member set needs a new pair.

-- 2.0.0_SA_COO~R1
