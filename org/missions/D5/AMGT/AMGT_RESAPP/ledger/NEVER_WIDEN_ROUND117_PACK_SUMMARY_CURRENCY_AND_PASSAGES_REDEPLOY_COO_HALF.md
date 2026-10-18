# NEVER-WIDEN CO-SIGN -- COO HALF. Round 117, `AMGT-bx-5`: the redeploy of `opal-amgt-scoped-api` from the release pin `9ab6d36305`, carrying `AMGT-bx-1` (the Summary reads the served recommendation; no state sentence names a path, a key or an order id), `AMGT-bx-2` (a money figure's currency by the page's rule, withheld where the page withholds) and `AMGT-bx-3` (the cleared machine-written passages the page shows, each labelled)

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-18 ~07:5xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND117_PACK_SUMMARY_CURRENCY_AND_PASSAGES_REDEPLOY_CTO_HALF.md`. Model: `NEVER_WIDEN_ROUND116_PACK_FORM_AND_CURRENCY_REDEPLOY_COO_HALF.md` (signed, applied).
**Applier:** the one AMGT CloudOps lane on dell1 (CLAUDE.md rule 34). **Source:** the CTO's round-116 analysis (`ledger/ROUND_ANALYSIS.round116.R1.md`, msg 7933, `@90802c3fe0`) and its item-3 correction (msg 7937); orders `AMGT_RESAPP.TO-AMGT-bx-1.*`, `bx-2.*`, `bx-3.*` (complete; merged `74e37dade8`, `543dc225ef`, `3dd98e9a9d` and the amendments `4613d6c0cb`, `64907494e1`) and `AMGT-bx-5` (cut when both halves are signed).
**Status:** DRAFT, not yet signed: it binds on the bytes the CTO half names. Nothing is deployed by this document. Push state of every commit named: LOCAL on box/dell1, unread.
**Measured from** the live function (read 2026-10-18 ~07:5xZ), the live packs of eight names, and this checkout's own handler over the same live pool with the `ai_fill` reader run as the live function runs it (the variable `AMGT_AIFILL_ROOT` absent); instruments in `deliverables/2.0.0_SA_COO~R1/round116_prep/checks/` (`r116_pack_money_vs_page.py`, `r116_pack_form_check.py`) and `round114_prep/checks/` (`r114_pack_capture_compare.py`, `r115_local_candidate_capture.py` with `R117_AIFILL_LIVE=1`); the BEFORE captures are on this box at `C:/dev/ui-walk-evidence/r116-packs-issuer-after/` and the candidate at `r117-cand2-packs/` (client data stays local).

## THE ACT

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from the RELEASE PIN **`9ab6d36305`** (branch `rel-amgt-bx5`, LOCAL on dell1): its parent is the live pin `fe04d740bf` (the build input of the live package since `bw-5`) and its only change against it is ONE member taken byte for byte from this branch's `0367a39372`:

| member | git blob live to new | file sha256 (12) live to new |
|---|---|---|
| `lib/research/print/render_pack.py` | `7f0f0d70a3ca` to `329f8b4e9304` | `7f5c5bb94a18` to `004bafd2338f` |

`scoped_amgt.py` does NOT change (the thesis bundle the route already hands `build_pack` carries `ai_fill` and `dossier_fields`). The member adds one stdlib import (`urllib.parse.urlsplit`, a local import) and no module. **The pin is NOT the box branch head on purpose**, as in `bw-5`.
Live pre-act, read 2026-10-18 ~07:5xZ: CodeSha256 `lNWo6Cm6AjLrkBeu2rB25cpbcaVTXLgVH7RQ+dQGmtg=`, LastModified 2026-10-18T05:52:41Z (the `bw-5` act), RevisionId `2eecd7e1-03b4-4f34-bec7-767bbd437a6e`, memory 1769, timeout 29, environment `{HARVEST_ARTICLES_TABLE, HARVEST_METRICS_TABLE}` (no `AMGT_AIFILL_ROOT`).

What changes at request time (read in the pin): (1) the `Summary` leads with the served recommendation (`dossier_fields.last_stated_position`: its text, the fund and weight, and one `Source: research report "<title>", passage <n>` line; never a key or a path), then the drafted sentences; the no-recommendation sentence prints only when both are absent; (2) no state sentence of the pack names a storage path, a key, an order id or a vendor error: an absent posture reads `No positioning view is on file for this name.`, an absent peer set `No peer set is on file for this company yet.`, an absent positioning call `No positioning call was made for this name.`; (3) a header money figure whose served `currency_basis` begins `UNMEASURED` is printed as `<label>: Bloomberg does not confirm this figure's currency - <source>` with NO amount (the page withholds it); a measured figure prints its own code, or `currency not stated` where it has none; (4) a machine-written passage of `ai_fill` (`mgmt_team_view`, `mgmt_bio`, `mgmt_recent` inside `Management`, above the roster, in the page's order; `thesis_pillars` as its own `Thesis pillars` section between `Summary` and `Risks and considerations`; `identity_description` only under an empty company description) prints ONLY when `ai_fill.status` is `SERVED`, the block has text and `validation.state` is `CLEARED` with verdict `PASS`, each followed by the line `machine-drafted, cleared <date>` (the `validation.checked_at` day in the house long form) with the page's source words and caption; an uncleared or withheld block prints nothing; the line `CEO public profile: no public profile is on file yet.` prints only when no management passage prints.

## THE MEASUREMENT (the expected outcome is its reading)

This checkout's own handler over the LIVE pool, eight names (RIO LN, ICT PM, GOOGL US, ICICIBC IN, HD US, BA US, KMB US, TSM US), status 200 on all sixteen requests, against the LIVE function's captures taken ~06:0xZ after `bw-5`:

| reading | value |
|---|---|
| form, candidate against live | **`PACK FORM: YES (8 of 8 names)`** (`r116_pack_form_check.py`): the headings in note order (with `Thesis pillars` where a pillars passage prints), a body under each, figures after the appendix, **no line naming a path, an order id or a vendor error**; the same instrument on the live packs reads **NO (3 of 8)** (the posture sentence's `s3://` path and `AMGT-rj-11` on five names, one comparable line): that is the base control |
| money lines, candidate, against the page's served figure | **`MONEY VS PAGE: YES (16 of 16 money lines)`**: four lines withheld (RIO LN market cap, net debt, enterprise value; ICT PM net debt: the page's words, no amount), one second market-value line deduped; the same instrument (taught the page's withheld rule) on the live packs reads **NO (12 of 16)**: the base control |
| Summary | RIO LN and ICT PM lead with `MAINTAIN 2.75% POSITION IN IDVZ` and `MAINTAIN 1.75% POSITION IN IDVZ`, fund, weight and the report title; GOOGL US prints its line-only position `Maintain positions in PFOE and DIVZ`; none prints `No recommendation has been written` |
| labelled passages, candidate | RIO LN 1 (the Simon Trott profile), ICT PM 3, GOOGL US 4, ICICIBC IN 3, BA US 1, KMB US 1; HD US and TSM US 0 (every `ai_fill` block of those two has no text, so nothing prints) |
| controls | form check live-against-live NO; the withheld branch of the money check was proven to fire only after a stray backspace byte in its regex was fixed (the base control read the old verdicts before the fix); GOOGL US prints no withheld words |
| latency | the candidate print route, local handler over the live pool: KMB US 10.0 and 6.9 s, RIO LN 6.6 and 5.8 s, GOOGL US 5.8 and 7.0 s; the live function after `bw-5` 7.4 to 8.8 s (different hosts; the timeout is 29 s, the CTO's bar 20 s) |
| tests | the merged tree, `lib/research/print/tests` plus `lib/research/api/tests`: `9 failed, 1230 passed`, the nine failures the known set; 40 new tests passing |

Stated limits: the candidate is the checkout's handler, not the built package (the applier's content diff is the authority); the `ai_fill` object is read from S3 by this box's credentials, as the live function reads it by its role: the same read was exercised by the live `/thesis` (SERVED) after `bw-5`; the post-act latency is read after; the `format=rich` export is NOT covered (it still prints raw amounts for the withheld figures and served reasons verbatim: rows `AMGT_RESAPP-D1-W513-S1` and `W512-S4`); `EQY_FUND_CRNCY` is served USD for RIO LN though no per-figure currency is (row `W513-S2`): the pack prints the page's withhold.

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package, admitted by BLOB at the GO

**ONE member:** `lib/research/print/render_pack.py` (live sha256 `7f5c5bb94a18`, new `004bafd2338f`). **The BUILT package's content diff against the live package is the authority.** Any other differing member, or this member at another hash, is a STOP BEFORE UPLOAD and returns to me for an addendum to both halves. NO IAM, route, memory, timeout, schedule, layer, environment variable, store write or S3 delete. The act writes NO data object. The Terraform plan must show the CODE only (the artifact hash and key).

## WRITER CENSUS of the moved served property (N printed, each rule read in the pin)

- The pack's Summary lines: ONE builder, `_print_summary`; the served recommendation is read from ONE field (`dossier_fields.last_stated_position`), the one the page's Posture tab reads. The pack's state sentences: the 8 sites the order's census changed (of 23 print sites; the other 15 read in the order's receipt, each stating why it carries no path, key or id).
- A money figure's printed currency: ONE reader, `_own_currency(fig)` (1 definition, 2 call sites), and ONE withheld test (a `currency_basis` that begins `UNMEASURED`: 1 definition, read at render_pack.py:627), in the figure-line functions; the figure's `currency_basis` is read as the page reads it (`figureBasis`, `isUnmeasuredBasis`). Fiscal-year lines carry their own currency on every served row and are unchanged.
- The machine-written passages: ONE reader, `_cleared_passage(thesis_bundle, block_id)` (`ai_fill.status SERVED`, text present, `validation.state CLEARED`, `verdict PASS`), 1 definition and 4 call sites (the pillars section, the team view, a loop over `mgmt_bio` and `mgmt_recent`, the identity fallback); ONE label helper. READERS of the printed pack: the CVO's L9 read and the partner export (a machine consumer of the PDF text was not searched for).

## SEQUENCE CONDITION

None on the page. Independent of any portal promote.

## THE GO, THE READS AFTER, AND THE ROLLBACK

1. **GO:** after the CTO half is signed on these bytes, the issuer cuts `AMGT-bx-5` to the applier with this half and the CTO half inlined and the pin named; the applier builds from a detached worktree at `9ab6d36305`, prints the content diff against the live package, and STOPS on anything outside the blast radius. Immediately before upload it re-reads CodeSha256, RevisionId and LastModified and STOPS on any change from the pre-act print above.
2. **Reads after the act (the issuer's, same turn):** `config` must read a CodeSha256 other than `lNWo6Cm6..`, memory 1769, timeout 29, environment keys unchanged, `AMGT_AIFILL_ROOT` absent; `capture` of the eight packs then `r116_pack_form_check.py <before> <after>` must read `PACK FORM: YES (8 of 8 names)`; `r116_pack_money_vs_page.py` (live) must read `MONEY VS PAGE: YES (16 of 16 money lines)`; the three live PDFs for the CVO are rebuilt; the print route is timed for KMB US, RIO LN and GOOGL US against the 20 s bar (over it: rollback). Anything else: STOP and roll back.
3. **Rollback (same window):** re-point the function to the previous package, the `bw-5` build at pin `fe04d740bf` (CodeSha256 `lNWo6Cm6AjLrkBeu2rB25cpbcaVTXLgVH7RQ+dQGmtg=`, RevisionId `2eecd7e1-03b4-4f34-bec7-767bbd437a6e`, VersionId of its S3 object `EVD2sGd8Bb.DGRU1XjvuhPJ6cOJo.otg` in `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`, per the `bw-5` ledger entry `amgt-resapp-r116-bw5-pack-note-currency-redeploy-dell1`), by re-applying that build through the same saved-plan route; no data object was written. The pack returns to its previous form on the next request.
4. **Ledger:** a change-management entry opened at the start and closed at completion (CLAUDE.md NEVER-2); the applier names every task family that pulls the artifact (one sweep; this half asserts none beyond the function itself).

## WHAT THIS HALF DOES NOT COVER

The `format=rich` export, the posture reader's own landing, the portal, any other served property, and any later pin. A different pin, a second member or a second leg needs a new pair.

-- 2.0.0_SA_COO~R1
