# NEVER-WIDEN CO-SIGN -- COO HALF. Round 114, `AMGT-bu-7`: the redeploy of `opal-amgt-scoped-api` from the release pin `6bb7b23ee5`, carrying `AMGT-bu-3`'s long-form dates in the printed pack

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-17 ~23:5xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND114_PACK_DATES_REDEPLOY_CTO_HALF.md`. Model: `NEVER_WIDEN_ROUND110_SEGMENT_LABEL_REDEPLOY_COO_HALF.md`.
**Applier:** the one AMGT CloudOps lane on dell1 (CLAUDE.md rule 34). **Source:** the CTO's round-113 R1-track analysis item 2, pack half (`ledger/ROUND_ANALYSIS.round113.R1.md`, msg 7763); orders `AMGT_RESAPP.TO-AMGT-bu-3.*` (merged `0100aab018`) and `AMGT-bu-7` (cut when both halves are signed).
**Status:** DRAFT, not yet signed: it binds on the bytes the CTO half names. Nothing is deployed by this document.
**Measured from** the live function (read 2026-10-17 ~23:5xZ), the live package (downloaded, 408 members), and the live printed packs of eight names; instrument `deliverables/2.0.0_SA_COO~R1/round114_prep/checks/r114_pack_capture_compare.py`; the BEFORE captures are on this box at `C:/dev/ui-walk-evidence/r114-packs-before/` (client data stays local).

## THE ACT

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from the RELEASE PIN **`6bb7b23ee5`** (branch `rel-amgt-bu7`, LOCAL on dell1): its parent is the live pin `7a8f2bb8e6` (the build input of the live package, round 110 `bp-6`) and its only change against it is `lib/research/print/render_pack.py`, taken byte for byte from the `bu-3` merge `0100aab018` (git blob `fa514afbb2f6`; file sha256 `60a9f2ddb4f4`; the live package carries sha256 `8e8266859b7b`, git blob `729693a65f7f`). **The pin is NOT the box branch head on purpose**, exactly as `bp-6`'s was: the box head carries other rounds' members the live function has not deployed.
Live pre-act, read 2026-10-17 ~23:5xZ (`get-function-configuration`): CodeSha256 `hLW4fD/aGMs/7V/mmp5eERQcaStjiq6s08DmSlAxn2I=`, LastModified 2026-10-17T16:34:05Z (the `bp-6` act), RevisionId `cf9191fc-e3d2-4c9a-8a3e-2672858446e7`, memory 1769, timeout 29, environment `{HARVEST_ARTICLES_TABLE, HARVEST_METRICS_TABLE}` (no `AMGT_AIFILL_ROOT`).

What changes at request time (read in the pin's `render_pack.py`): every date or day a reader sees on the printed PDF and the plain-text pack is the house long form (`September 22nd, 2026`) instead of the served ISO day: the page-1 `Printed` line, each `period ending` and `as of` source line, the earnings-dates line, the `observed` segment, and any ISO day inside a printed sentence (the `_wrap` guard runs the helper on every printed line before it is cut, so a wrapped line is measured on the printed text). **Nothing else moves:** no served value, no sort, no comparison. The `format=rich` export is NOT changed and still prints ISO days (a stated limit, row W506-S4). **`long_day.py` is already in the live package** (`lib/research/freshness/long_day.py`, sha256 `2395e368235d`, read from the downloaded live zip), so no member is newly packaged.

## THE MEASUREMENT (the expected outcome is its reading)

The LIVE `/print?format=pdf` route for eight names (RIO LN, ICT PM, GOOGL US, ICICIBC IN, HD US, BA US, KMB US, TSM US), PDF text read with PyMuPDF, captured BEFORE the act: status 200 on all eight; ISO days per pack 51, 51, 51, 30, 51, 50, 51, 33 (none carries a long-form day). The act's expected outcome is read from the producer's rule (`_long_days` over every printed line, tested by `AMGT-bu-3`'s seven tests on hand-built fixtures, because no committed RIO LN or ICT PM block exists): the AFTER capture, with whitespace collapsed (a longer date moves the wrap) and each long-form date mapped back to ISO by the hand-written inverse in the instrument, must EQUAL the BEFORE capture on every name, and no ISO day may remain. That is the T6 control of `bu-3` run on live data.

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package, admitted by BLOB at the GO

**ONE member:** `lib/research/print/render_pack.py` (live sha256 `8e8266859b7b`, new `60a9f2ddb4f4`). **The BUILT package's content diff against the live package is the authority.** Any other differing member, or this member at another hash, is a STOP BEFORE UPLOAD and returns to me for an addendum to both halves. NO IAM, route, memory, timeout, schedule, layer, environment variable, store write or S3 delete. The act writes NO data object. The Terraform plan must show the CODE only (the artifact hash and key).

## WRITER CENSUS of the moved served property (N printed, each rule read in the pin)

- The printed date text: `render_pack.py`'s `_long_days` is called at eight sites (`build_pack` page 1; `_figure_date_text` twice; `_format_figure_value` twice; `_plain_figure_line`; and inside `_wrap`, the one place every printed title, heading and body line passes, which also covers the census's served-prose sites S07 to S09). **N = 8 call sites of one helper (read by `grep -c` as 9 lines including its definition; `bu-3`'s receipt `## Date census`: 58 functions read, 26 that touch a date, 9 pack-path sites fixed).** The pack is built by ONE function, `build_pack`, reached from `lib/research/api/scoped_amgt.py`'s `_print_pack`; `format=rich` goes through `build_rich_text`, which is not changed.
- READERS of the printed text: the portal's print button and a person; no machine reader of the PDF text was found in `lib/research` (not searched in the portal).

## SEQUENCE CONDITION

None on the page: the pack is built server-side. The act is independent of the portal promote `AMGT-bu-5` and of its fold-back.

## THE GO, THE READS AFTER, AND THE ROLLBACK

1. **GO:** after the CTO half is signed on these bytes, the issuer cuts `AMGT-bu-7` to the applier with this half and the CTO half inlined and the pin named; the applier builds from a detached worktree at `6bb7b23ee5`, prints the content diff against the live package, and STOPS on anything outside the blast radius.
2. **Reads after the act (the issuer's, same turn):** `r114_pack_capture_compare.py capture` into an AFTER folder, then `compare <before> <after>` must read `PACK COMPARE: YES (8 of 8 names ...)`; `config` must read a CodeSha256 other than `hLW4fD..`, memory 1769, timeout 29, environment keys unchanged, `AMGT_AIFILL_ROOT` absent. A name that still prints ISO days, or whose text differs beyond dates, means the package did not take or moved something else: STOP and roll back.
3. **Rollback (same window):** re-point the function to the previous package, the `bp-6` build at pin `7a8f2bb8e6` (CodeSha256 as printed above, RevisionId `cf9191fc-e3d2-4c9a-8a3e-2672858446e7`; its S3 object and VersionId are in the `bp-6` ledger entry `20261017T1620Z_amgt-resapp-r110-bp6-segment-label-redeploy-dell1_deploy_completion.md`, L6), by re-applying that build through the same saved-plan route; no data object was written. The pack returns to ISO days on the next request.
4. **Ledger:** a change-management entry opened at the start and closed at completion (CLAUDE.md NEVER-2); the applier names every task family that pulls the artifact (one sweep; this half asserts none beyond the function itself).

## WHAT THIS HALF DOES NOT COVER

The portal candidates (`bu-1`, `bu-2`, `bu-4`) and their promote `bu-5`, the `format=rich` export's ISO days (`W506-S4`), any other served property, and any later pin. A different pin, a second leg or a widened member set needs a new pair.

-- 2.0.0_SA_COO~R1
