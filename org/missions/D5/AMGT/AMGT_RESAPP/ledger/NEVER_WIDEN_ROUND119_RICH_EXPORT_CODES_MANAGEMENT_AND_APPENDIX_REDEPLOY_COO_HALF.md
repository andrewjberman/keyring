# NEVER-WIDEN CO-SIGN -- COO HALF. Round 119, `AMGT-bz-5`: the redeploy of `opal-amgt-scoped-api` from the release pin `2771164d0d`, carrying `AMGT-bz-1` (the rich export's measured money rows carry the figure's own currency code), `AMGT-bz-2` (the rich export reads the CEO profile and the management lines as the PDF does: C-S195) and `AMGT-bz-3` (the PDF appendix's served source and basis definition go through the plain-reason mapper; `steer clear`)

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-18 ~12:5xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND119_RICH_EXPORT_CODES_MANAGEMENT_AND_APPENDIX_REDEPLOY_CTO_HALF.md`. Model: `NEVER_WIDEN_ROUND118_PACK_REASON_MAPPER_AND_RICH_EXPORT_REDEPLOY_COO_HALF.md` (signed, applied).
**Applier:** the one AMGT CloudOps lane on dell1 (CLAUDE.md rule 34). **Source:** the CTO's round-118 analysis (`ledger/ROUND_ANALYSIS.round118.R1.md`, msg 8020, `@9e9f8454d5`); orders `AMGT_RESAPP.TO-AMGT-bz-1.*`, `bz-2.*`, `bz-3.*` (complete; merged `8d0849a3e1`, `a93a333e18`, `96c2c0f910`, the `bz-2` receipt `b6f5989705`) and `AMGT-bz-5` (cut when both halves are signed).
**Status:** DRAFT, not yet signed: it binds on the bytes the CTO half names. Nothing is deployed by this document. Push state of every commit named: LOCAL on box/dell1, unread.
**Measured from** the live function (read 2026-10-18 ~12:5xZ), the live packs and rich exports of eight names, the live packs of all 101 covered names, and this checkout's own handler over the same live pool with the `ai_fill` reader run as the live function runs it (`AMGT_AIFILL_ROOT` absent); instruments in `deliverables/2.0.0_SA_COO~R1/round116_prep/checks/` (`r116_pack_money_vs_page.py`, `r116_pack_form_check.py`), `round114_prep/checks/` (`r114_pack_capture_compare.py`, `r115_local_candidate_capture.py` with `R117_AIFILL_LIVE=1`), `round118_prep/checks/` (`r118_leak_scan.py`) and `round119_prep/checks/r119_cross_surface.py`; the BEFORE captures are on this box at `C:/dev/ui-walk-evidence/r119-packs-before/` and `r119-rich-before/` and the candidate at `r119-cand-packs/` and `r119-cand-rich/` (client data stays local).

## THE ACT

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from the RELEASE PIN **`2771164d0d`** (branch `rel-amgt-bz5`, LOCAL on dell1): its parent is the live pin `d4c6f1c533` (the build input of the live package since `by-5`) and its only change against it is ONE member taken byte for byte from this branch's `b6f5989705`:

| member | git blob live to new | file sha256 (12) live to new |
|---|---|---|
| `lib/research/print/render_pack.py` | `3ddc696def09` to `a281246c18c0` | `5f4cffc172ba` to `ce54affc8f87` |

`scoped_amgt.py` does NOT change (`bz-2` found both routes already read one management object and changed only the rich export's wording in `render_pack.py`). The member adds no import. **The pin is NOT the box branch head on purpose**, as in `by-5`.
Live pre-act, read 2026-10-18 ~12:5xZ: CodeSha256 `H3dCSGLEs4abPk0alOWclPZX1U6lYrxEXkhGZOAJ434=`, LastModified 2026-10-18T11:14:20.000+0000 (the `by-5` act), RevisionId `caab3655-4909-4c3d-ba32-76446effe97d`, memory 1769, timeout 29, environment `{HARVEST_ARTICLES_TABLE, HARVEST_METRICS_TABLE}` (no `AMGT_AIFILL_ROOT`).

What changes at request time (read in the pin): (1) every measured money row of the rich export (the Header table and the fiscal and forecast rows the export prints from figure objects) prints the figure's own currency code, read by the same `_own_currency` the PDF uses (RIO LN `PX_LAST` `GBp`; ICT PM `PHP` and `USD`; GOOGL US `USD`); a measured figure with no code prints `currency not stated`; the five UNMEASURED header figures of the eight names stay withheld with the page's words; every other row is unchanged; (2) the export's management section prints the PDF's own CEO-profile sentence (`CEO public profile (EDWARD P. DECKER): The CEO web search returned ...` for HD US, `CEO public profile: no public profile is on file yet.` where none is on file) and the management passages the pack prints, with their labels, instead of the reading word (`the object could not be read`); (3) the PDF appendix's served `source` and basis definition go through `_plain_reason` at six sites (a plain `Bloomberg` source and a plain definition print as before; a path-bearing or id-bearing text prints the site's fixed sentence), and the unknown-verdict sentence reads `steer clear`.

## THE MEASUREMENT (the expected outcome is its reading)

This checkout's own handler over the LIVE pool, eight names, status 200 on all sixteen requests (pdf and rich), against the LIVE function's captures taken ~12:4xZ before the act:

| reading | value |
|---|---|
| the PDF text of the eight names, candidate against live | **IDENTICAL on 8 of 8** (the run day masked): this act moves no PDF line of these names; the PDF is the reference the export is read against |
| cross-surface read (`r119_cross_surface.py`: the PDF's Management section against the export's: the CEO line exact, roster names, labels inside Management, no `could not be read` or `UNREADABLE_OBJECT`, RIO LN's withheld rows), candidate | **`CROSS SURFACE: YES (8 of 8 names)`**; the same instrument on the LIVE captures taken before the act reads **NO (0 of 8)**: the base control |
| the export's money rows, candidate | RIO LN `PX_LAST` `GBp 6816.0`, market cap, net debt and enterprise value read `Bloomberg does not confirm this figure's currency` and carry no amount; ICT PM `PX_LAST` `PHP 860.0`, `CUR_MKT_CAP` `PHP`, `CURR_ENTP_VAL` `USD`, `NET_DEBT` withheld; GOOGL US `USD` on every money row; the same three live exports before the act carry **no currency code on any money row** (0 rows) and each says `could not be read` once |
| form and money, candidate | `PACK FORM: YES (8 of 8 names)` and `MONEY VS PAGE: YES (16 of 16 money lines)` (unchanged: the pack's figures and sections do not move) |
| leak scan of the candidate pack of every covered name | `r118_leak_scan.py local`: 101 distinct names, **0 leaking lines**, 100 clean, 1 error: `WALMEX*_MM_Equity`, status 500 from this checkout's handler on WINDOWS (`OSError` on a temp file name carrying `*`; the Lambda runs on Linux; the live function answers 200 for that name and the live scan reads it clean): a property of the local run, as in round 118 |
| latency | candidate over the live pool, local handler, two runs each: pdf worst 9.5 s; **rich** KMB US 3.1 s, RIO LN 2.7 s, GOOGL US 2.8 s; the live function after `by-5`: pdf worst 7.8 s, rich worst 2.0 s; the bar is the CTO's 20 s on both routes |
| tests | the merged tree, `lib/research/print/tests` plus `lib/research/api/tests`: `9 failed, 1382 passed`, the SAME nine failures as before the round; 83 new tests |

Stated limits: the candidate is the checkout's handler, not the built package (the applier's content diff is the authority); the export still lacks the thesis-pillars passage the PDF prints for ICT PM, GOOGL US and ICICIBC IN (outside this round's list: reported for the CTO); the `bz-2` unit control M6 (both routes hand the builder the same management object) is true by construction of its stub (the re-seated worker's own correction in the receipt); the two armed rows `W518-S2` (the reader labels a null profile `UNREADABLE_OBJECT`) and the appendix's absent-source `?` (`bz-3` row S5) are not changed here.

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package, admitted by BLOB at the GO

**ONE member:** `lib/research/print/render_pack.py` (live sha256 `5f4cffc172ba`, new `ce54affc8f87`). **The BUILT package's content diff against the live package is the authority.** Any other differing member, or this member at another hash, is a STOP BEFORE UPLOAD and returns to me for an addendum to both halves. NO IAM, route, memory, timeout, schedule, layer, environment variable, store write or S3 delete. The act writes NO data object. The Terraform plan must show the CODE only (the artifact hash and key).

## WRITER CENSUS of the moved served property (N printed, each rule read in the pin)

- A rich-export money row's currency: ONE reader, `_own_currency` (1 definition, called by the pack's `_format_figure_value` and `_converted` and now by the export's `_export_money_cell`); the withheld test is the ONE function `_currency_unmeasured` (1 definition). The export's CEO-profile line: ONE builder, `_ceo_profile_sentence` (1 definition, called by the pack's `_print_management` and now by the export's management section). The appendix's served source and definition: 6 sites in `_withheld_line`, `_plain_figure_line` (header and fiscal) and `_plain_label` (definition and forecast branches), each through `_plain_reason`.
- READERS of the rich export: the CVO's L9 read and the partner export; a machine consumer of the markdown was not searched for.

## SEQUENCE CONDITION

None on the page. Independent of any portal promote.

## THE GO, THE READS AFTER, AND THE ROLLBACK

1. **GO:** after the CTO half is signed on these bytes, the issuer cuts `AMGT-bz-5` to the applier with this half and the CTO half inlined and the pin named; the applier builds from a detached worktree at `2771164d0d`, prints the content diff against the live package, and STOPS on anything outside the blast radius. Immediately before upload it re-reads CodeSha256, RevisionId and LastModified and STOPS on any change from the pre-act print above.
2. **Reads after the act (the issuer's, `r118_post_act_reads.sh` plus `r119_cross_surface.py`):** `config` must read a CodeSha256 other than `H3dCSGL..`, memory 1769, timeout 29, environment keys unchanged, `AMGT_AIFILL_ROOT` absent; `PACK FORM: YES (8 of 8 names)`; `MONEY VS PAGE: YES (16 of 16 money lines)`; the live all-names leak scan `NO LEAK` (101 of 101 clean); the eight live rich exports with 0 `s3://`, `AMGT-` or vendor-error lines; `CROSS SURFACE: YES (8 of 8 names)` between the live PDFs and the live exports, and the live PDF text of the eight names identical to before the act; the three exports' money rows carrying their code; the print route (pdf and rich) timed for KMB US, RIO LN and GOOGL US against the 20 s bar (over it: rollback). Anything else: STOP and roll back.
3. **Rollback (same window):** re-point the function to the previous package, the `by-5` build at pin `d4c6f1c533` (CodeSha256 `H3dCSGLEs4abPk0alOWclPZX1U6lYrxEXkhGZOAJ434=`, RevisionId `caab3655-4909-4c3d-ba32-76446effe97d`, VersionId of its S3 object `xr.zAPt5G9_Tjw8D60wN54ZgecD0x9P4` in `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`, per the `by-5` ledger entry `amgt-resapp-r118-by5-plain-reasons-rich-export-redeploy-dell1`), by re-applying that build through the same saved-plan route; no data object was written. The export returns to its previous form on the next request.
4. **Ledger:** a change-management entry opened at the start and closed at completion (CLAUDE.md NEVER-2); the applier names every task family that pulls the artifact (one sweep; this half asserts none beyond the function itself).

## WHAT THIS HALF DOES NOT COVER

The thesis-pillars passage in the export, a currency carried from the fund currency onto the figures, the producer's `UNREADABLE_OBJECT` label for a null profile (row `W518-S2`), the appendix's absent-source `?`, the portal, any other served property, and any later pin. A different pin, a second member or a second leg needs a new pair.

-- 2.0.0_SA_COO~R1
