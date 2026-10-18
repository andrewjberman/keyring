# NEVER-WIDEN CO-SIGN -- COO HALF. Round 116, `AMGT-bw-5`: the redeploy of `opal-amgt-scoped-api` from the release pin `fe04d740bf`, carrying `AMGT-bw-1` (each money figure prints its own currency) and `AMGT-bw-2` (the pack reads as a note, narrative first, figures in an appendix; the print route's three new reads guarded)

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-18 ~05:5xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND116_PACK_FORM_AND_CURRENCY_REDEPLOY_CTO_HALF.md`. Model: `NEVER_WIDEN_ROUND115_RICH_EXPORT_AND_QUOTES_REDEPLOY_COO_HALF.md` (signed).
**Applier:** the one AMGT CloudOps lane on dell1 (CLAUDE.md rule 34). **Source:** the CTO's round-115 analysis items 1 to 3 (`ledger/ROUND_ANALYSIS.round115.R1.md`, addendum 1 `@942cdf7357`, msg 7894); orders `AMGT_RESAPP.TO-AMGT-bw-1.*` and `AMGT_RESAPP.TO-AMGT-bw-2.*` (complete; merged `3a3dcec0b8`, `e50900d1b1`, `b1628a34ef`; flips `84520a17d1`) and `AMGT-bw-5` (cut when both halves are signed).
**Status:** DRAFT, not yet signed: it binds on the bytes the CTO half names. Nothing is deployed by this document. Push state of every commit named: LOCAL on box/dell1, unread.
**Measured from** the live function (read 2026-10-18 ~05:3xZ), the live packs of eight names, and this checkout's own handler over the same live pool; instruments in `deliverables/2.0.0_SA_COO~R1/round116_prep/checks/` (`r116_pack_money_vs_page.py`, `r116_pack_form_check.py`) and `round114_prep/checks/` (`r114_pack_capture_compare.py`, `r115_local_candidate_capture.py`); the BEFORE capture is on this box at `C:/dev/ui-walk-evidence/r116-packs-before/` and the candidate at `r116-cand-packs/` (client data stays local).

## THE ACT

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from the RELEASE PIN **`fe04d740bf`** (branch `rel-amgt-bw5`, LOCAL on dell1): its parent is the live pin `d4bba34eb8` (the build input of the live package since `bv-5`) and its only changes against it are TWO members taken byte for byte from this branch's `b1628a34ef`:

| member | git blob live to new | file sha256 (12) live to new |
|---|---|---|
| `lib/research/print/render_pack.py` | `89d4c2a34b89` to `7f0f0d70a3ca` | `8a1f47d8c6cd` to `7f5c5bb94a18` |
| `lib/research/api/scoped_amgt.py` | `a75ab14fd16d` to `43c8139d2d2d` | `73f53b54747d` to `472df817702c` |

**The pin is NOT the box branch head on purpose**, as in `bu-7` and `bv-5` (other workstreams' members sit at the head).
Live pre-act, read 2026-10-18 ~05:3xZ: CodeSha256 `lp+7X1VkDi7sFz3v5W3yZSlWFZaMQSKo7knlvp1GxBQ=`, LastModified 2026-10-18T03:07:37Z (the `bv-5` act), RevisionId `e4e64b80-28bf-4e1a-8f68-f85e312db781`, memory 1769, timeout 29, environment `{HARVEST_ARTICLES_TABLE, HARVEST_METRICS_TABLE}` (no `AMGT_AIFILL_ROOT`).

What changes at request time (read in the pin): (1) every money amount in the printed pack prints the currency of the figure's OWN served `currency` (never `CRNCY` or `EQY_FUND_CRNCY`), and an amount whose figure carries none reads `<amount> currency not stated` (the page's words), never `local currency` and never a borrowed code; the second market-value line `Market value, currency-adjusted` is kept only when its value differs from the market cap AND both carry a code and the codes differ (then it reads `(converted, rate not carried)`); (2) the PDF reads as a note: `Summary`, `Risks and considerations`, `Company description`, `Management` (the roster and the CEO profile line, or one sentence saying why not), `Positioning`, `Peers`, `What changed` (one sentence saying it is not an input), then `Appendix: model figures`; (3) the print route hands `build_pack` the thesis bundle, the peer set and the posture it already reads for the rich export, each read guarded: a raising reader is an absent input, one warning line is logged, and the section prints its absence sentence.

## THE MEASUREMENT (the expected outcome is its reading)

This checkout's own handler over the LIVE pool, eight names (RIO LN, ICT PM, GOOGL US, ICICIBC IN, HD US, BA US, KMB US, TSM US), status 200 on all sixteen requests, against the LIVE function's captures taken 05:3xZ:

| reading | value |
|---|---|
| money lines, candidate, against the page's served figure (own currency and amount), three names | **`MONEY VS PAGE: YES (15 of 15 money lines)`** (`r116_pack_money_vs_page.py` with `R116_LOCAL=1`); the same instrument on the LIVE packs (the base control) reads **NO (11 of 17)** with six wrong labels |
| the two CVO findings | ICT PM `Market value, currency-adjusted` USD against its PHP: no longer printed (the dedup drops the same-value line); RIO LN market cap `GBp 115,578.9 million`: now `115,578.9 million currency not stated` (the figure carries no currency) |
| pack form, candidate against live, eight names | **`PACK FORM: YES (8 of 8 names)`** (`r116_pack_form_check.py`): the eight headings in note order, a body under each, figures start after the appendix heading; figure lines equal live as a multiset on 5 of 8 names, and on the three that differ (RIO LN, ICT PM, TSM US) ONLY money lines differ (4 and 3, 2 and 1, 2 and 1 lines), each a currency label |
| controls | the form check run live-against-live reads NO (no appendix heading, wrong order); the money check on the live packs reads NO; GOOGL US prints no `currency not stated` and no changed figure line |
| latency | the candidate print route, local handler over the live pool: KMB US 9.7 s, RIO LN 7.1 s, GOOGL US 6.0 s; the live function over the same names 6.3 s, 5.9 s, 6.2 s (different hosts; the timeout is 29 s) |
| tests | the merged tree, `lib/research/print/tests` plus `lib/research/api/tests`: `9 failed, 1187 passed`, the nine failures the known set; 27 new tests passing |

Stated limits: the candidate is the checkout's handler, not the built package (the checkout carries other workstreams' members the live function lacks; the applier's content diff is the authority); the live latency of the three extra reads is measured only after the act; the `format=rich` branch still reads the three readers unguarded (surprise row `AMGT_RESAPP-D1-W511-S9`, pre-existing, not changed here and not covered by this half); the `Positioning` section prints the posture state sentence as served (`ABSENT -- no O-1 posture object under s3://...`), which names an internal key prefix: an OBSERVATION for the CVO's read, not an act of this half.

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package, admitted by BLOB at the GO

**TWO members:** the two above. **The BUILT package's content diff against the live package is the authority.** Any other differing member, or either member at another hash, is a STOP BEFORE UPLOAD and returns to me for an addendum to both halves. NO IAM, route, memory, timeout, schedule, layer, environment variable, store write or S3 delete. The act writes NO data object. The Terraform plan must show the CODE only (the artifact hash and key).

## WRITER CENSUS of the moved served property (N printed, each rule read in the pin)

- The currency a pack money line prints: ONE reader, `_own_currency(fig)` (one definition, 2 call sites: `_format_figure_value` and `_converted`); the amount is formatted by `_money`, **N = 5** textual uses in the file (1 definition, 4 call sites in `_format_figure_value`). `build_pack` passes `CRNCY` and `EQY_FUND_CRNCY` to no money label (the text lines `Currency:` and `Reporting currency:` print the served text field as written, unchanged). The rich export's figure lines name no currency code (`render_figure_line`, unchanged, read-only).
- The note's section order and bodies: ONE builder, `build_pack`; the print route's call sites: `_print_pack`'s PDF branch (3 guarded reads) and the rich branch (unchanged). READERS of the printed pack: the CVO's L9 read and the partner export (a machine consumer of the PDF text was not searched for).

## SEQUENCE CONDITION

None on the page. Independent of any portal promote.

## THE GO, THE READS AFTER, AND THE ROLLBACK

1. **GO:** after the CTO half is signed on these bytes, the issuer cuts `AMGT-bw-5` to the applier with this half and the CTO half inlined and the pin named; the applier builds from a detached worktree at `fe04d740bf`, prints the content diff against the live package, and STOPS on anything outside the blast radius. Immediately before upload it re-reads CodeSha256, RevisionId and LastModified and STOPS on any change from the pre-act print above.
2. **Reads after the act (the issuer's, same turn):** `config` must read a CodeSha256 other than `lp+7X1V..`, memory 1769, timeout 29, environment keys unchanged, `AMGT_AIFILL_ROOT` absent; `capture` of the eight packs then `r116_pack_form_check.py <before> <after>` must read `PACK FORM: YES (8 of 8 names)`; `r116_pack_money_vs_page.py` (live) must read `MONEY VS PAGE: YES`; the three live PDFs for the CVO are rebuilt; the print route's timing for the three names is read against the 29 s timeout. Anything else: STOP and roll back.
3. **Rollback (same window):** re-point the function to the previous package, the `bv-5` build at pin `d4bba34eb8` (CodeSha256 `lp+7X1V..`, RevisionId `e4e64b80-28bf-4e1a-8f68-f85e312db781`, VersionId of its S3 object `kF6PjYv9I.PZF9kNMUGxBM98ZYpE922E` in `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`, per the `bv-5` ledger entry `amgt-resapp-r115-bv5-rich-export-quotes-redeploy-dell1`), by re-applying that build through the same saved-plan route; no data object was written. The pack returns to its previous form on the next request.
4. **Ledger:** a change-management entry opened at the start and closed at completion (CLAUDE.md NEVER-2); the applier names every task family that pulls the artifact (one sweep; this half asserts none beyond the function itself).

## WHAT THIS HALF DOES NOT COVER

The `format=rich` export's reader guards, the posture sentence's wording, the portal, any other served property, and any later pin. A different pin, a third member or a second leg needs a new pair.

-- 2.0.0_SA_COO~R1
