# NEVER-WIDEN CO-SIGN -- COO HALF. Round 106, `AMGT-bm-3`: the redeploy of `opal-amgt-scoped-api` from the merged pin `3818736e6b`, carrying `AMGT-bm-2`'s forward P/E withhold

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-14 ~11:3xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND106_FORWARD_PE_WITHHOLD_REDEPLOY_CTO_HALF.md`. Models: `NEVER_WIDEN_ROUND104_SPLIT_AND_PE_REDEPLOY_COO_HALF.md` and `NEVER_WIDEN_ROUND105_AIFILL_HOLD_COO_HALF.md`.
**Applier:** `0.7.0_AE_CloudOps~RA1`. **Source:** the CTO's round-105 analysis `ledger/ROUND_ANALYSIS.round105.md` (msg 5426) item 1; order `task-orders/AMGT_RESAPP.TO-AMGT-bm-3.*` (cut with this half).
**Written from** a measurement taken from the pin's OWN worktree (`C:/tmp/bm3-pin`, a detached checkout of `3818736e6b`, so the measuring tree IS the built tree) against the live function, 2026-10-14 06:02Z-06:16Z, and re-read at 11:1xZ-11:2xZ for the live configuration and a capture of the live forward P/E rows (278 rows on 95 names).
Instruments: `deliverables/2.0.0_SA_COO~R1/round106_prep/checks/` (`r106_forward_pe_population.py`, `r106_fwd_pe_check.py`, `r106_fwd_pe_deployed.py`) and `round94_prep/checks/` and `round95_prep/checks/` (`r94_name_table.py`, `r94_rankings_table.py`, `r95_series_by_ticker_table.py`, `r94_other_routes_table.py`, `r94_naming_replay.py`, `r94_admission_table.py`); outputs in `round106_prep/measure/`.

## THE ACT

ONE code leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at **`3818736e6b`** (`drain: merge wk-AMGT_RESAPP-442`, a `box/dell1` first-parent commit, an ancestor of the shared branch head). Live pre-act, read 2026-10-14 11:1xZ: CodeSha256 `0pWc69VdNBP1zBNBWImnStynQ5HWpvS2qapghhsRfd0=`, LastModified 2026-10-14T05:10:01Z, memory 1769, timeout 29, RevisionId `f7ccaaad-e477-4d01-90a1-38b2a4d145c0`, environment `{HARVEST_METRICS_TABLE, HARVEST_ARTICLES_TABLE, AMGT_AIFILL_ROOT=/var/empty/aifill-hold}` (the AI-fill hold, applied under the round-105 hold pair, stays).
Live pin (the build input the live package came from): `0447f2df38`.

What changes at request time (read in the pin's `scoped_amgt.py`): `read_model` passes the forecast rows through `_derive_forward_pe(forecast_raw, _latest_price_currency(fiscal))`. A `BEST_PE_RATIO` row of `forecast_figures` whose price currency (the currency of the latest `PX_LAST` row of `fiscal_year_figures`) and consensus-EPS currency (the `BEST_EPS` row of the same fiscal year and period) are two DIFFERENT currencies is dropped from the served figures and returned as a `model.forecast_withheld` entry `{mnemonic, fiscal_year, fiscal_period, reason}` whose reason names both codes. A minor unit over its major (GBp over GBP) is the same currency and stays; a row is kept untouched when either currency is absent. The stored Bloomberg values are not changed. **The key `model.forecast_withheld` is added to EVERY name's body** (an empty list on a name with nothing withheld).

## THE MEASUREMENT (the expected outcome is its reading)

Instrument: the LIVE function's response (Lambda invoke, GET) against the pin's OWN `scoped_amgt.handler` on the same live pool, every JSON path compared.

| route (instrument) | reads | paths changed | where |
|---|---|---|---|
| overlay + peers, all MEASURED subjects (`r94_name_table.py`) | **243 subjects x 2 routes** | **0** | none |
| ranked lists, 4 movement x subject combinations and their timeseries (`r94_rankings_table.py`) | 7 combos | **0** | none |
| rank timeseries for every measured subject's ticker x 4 combinations (`r95_series_by_ticker_table.py`) | 4 x 243 series | **0** | none |
| timeline and collected chatter (`r94_other_routes_table.py`) | the 27-read set | **0** on timeline and chatter | none |
| **thesis, WHOLE BODY, all 95 resolved names** (`r106_fwd_pe_check.py`) | 95 names, status 200 and 200 on every one | forward P/E rows **278 -> 218**; **60 withheld on 20 names** | exactly the different-currency population; **6 of 6 arms** (F1 candidate rows = base rows minus those; F2 kept rows equal; F3 every withheld row has an entry naming both codes; F4 PBR US names USD and BRL; F5 no other path differs; F6 60 = the population's 60) |
| thesis of the 12-subject sample (`r94_other_routes_table.py`) | 12 reads | 1,097 index-shifted paths on 3 subjects (`AZN_LN`, `BABA_US`, `TSM_US`: a list element fewer shifts every later index), plus `.model.forecast_withheld` absent -> `[]` on the others | the same rows; `ai_fill.reason` differs only by the MEASURING machine's path separator (`/var/empty/aifill-hold/X` vs `\\`), a Windows artefact: **expected live: zero** |
| the check face that follows the figure | 278 forward P/E check rows at the base | **60 move with the 60 withheld rows** (`check_face` rows `forecast:BEST_PE_RATIO:<year>`), 218 stay | read from the pre capture, `r106_fwd_pe_deployed.py` |

The 20 names: `1299 HK`, `939 HK`, `992 HK`, `AZN LN`, `BABA US`, `BP/ LN`, `BZLFY US`, `HSBA LN`, `ICT PM`, `JD US`, `NOVN SW`, `PBR US`, `RIO LN`, `SHOP CN`, `SPOT US`, `TSM US`, `TTE FP`, `UBSG SW`, `ULVR LN`, `ZURN SW`.
**The dry run of the post-act instrument** (`r106_fwd_pe_deployed.py verify`, run 11:2xZ against a capture of the live function, the pin's handler as the deployed side): **YES (7 of 7 arms)**; the same call against the live function (still the old code) reads **NO (4 of 7)**, with F1, F3 and F4 failing. That is the discriminating control for the act.

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package, each member admitted by BLOB at the GO

Measured by `r94_admission_table.py 3818736e6b --pin 0447f2df38`: **nine members differ at the pin**.

| member | blob at the live pin `0447f2df38` | blob at the pin `3818736e6b` | reaches the function's request path? |
|---|---|---|---|
| `lib/research/api/scoped_amgt.py` | `1f5de89912e5` | `a75ab14fd16d` (+51 -3) | **YES** (the handler) |
| `lib/research/aifill/block_identity_description.py` | `c70fe05a8c78` | `e50147fa5456` | NO (the producer, `~R2`; the pin's own comment at `scoped_amgt.py:3375` says this Lambda does not package `lib.research.aifill`) |
| `lib/research/aifill/block_mgmt_bio.py` | `fef074d4f30e` | `955f2cd6eb77` | NO |
| `lib/research/aifill/block_mgmt_recent.py` | `f1367c7f97e2` | `2b8b22e17432` | NO |
| `lib/research/aifill/block_mgmt_team_view.py` | `310f807c43e1` | `3e8926254a89` | NO |
| `lib/research/aifill/block_thesis_pillars.py` | `2aea75e0c7c7` | `f695ddab1a58` | NO |
| `lib/research/aifill/contract.py` | `2220ce145097` | `e8906fa80924` | NO |
| `lib/research/aifill/model.py` | `e7f06c4c4905` | `3eac07bd68a7` | NO |
| `lib/research/aifill/revalidate.py` | ABSENT | `655949c603e3` | NO |

**The BUILT package's content diff against the live package is the authority.** If the built package carries ANY of the eight `aifill` members, or any member other than `scoped_amgt.py`, or `scoped_amgt.py` at another blob, that is a STOP BEFORE UPLOAD and returns to me for an addendum to both halves. The builder replay (`r94_naming_replay.py --pin 0447f2df38`, from the pin's worktree): **35 requests all 200, 68 builder calls, 16 distinct (`address` 6, `key` 10), `R94 NAMING REPLAY: YES`**. NO IAM, route, memory, timeout, schedule, layer, store write or S3 delete. The act writes NO data object. The Terraform plan must show the CODE only (the artifact hash/key) on the function; a plan that moves the environment (the hold), role, layers, memory or timeout is a STOP.

## WRITER CENSUS of the moved served property (N printed, each rule read in the pin)

- `model.forecast_withheld`: **ONE** assignment, `read_model` (`"forecast_withheld": forward_withheld`); produced by **ONE** function, `_derive_forward_pe`, with **ONE** call site. **N = 1.**
- `model.forecast_figures` (the served forward rows): **ONE** assignment from `_derive_forward_pe`'s kept list. Writers of the price currency it reads: ONE (`_latest_price_currency`). **Pick rules N = 1.**
- The census fields `forecast_source_counts` and the `forecast_reason` read the STORED rows (`forecast_raw`), so a withheld row still counts as a Bloomberg row and a name whose only forward rows are withheld is not reported as having no forecast.
- READERS of the served rows: the portal's `modelSheet.ts` (the only first-party portal source that names `BEST_PE_RATIO`; bm-1 reads `forecast_withheld`, an absent field keeps today's behaviour) and `lib/research/print/render_pack.py` (reads the SERVED `forecast_figures`, so the print pack drops the same rows; its test `test_av2_export_equals_page.py` compares export to page).

## SEQUENCE CONDITION (the issuer's, not a gate)

The page lands BEFORE the served change: this half's GO is given only after `AMGT-bm-4` has put the approved portal feature (`84fd6461bb`, which prints a served reason in a withheld forward P/E's dash) on PROD. Reason: before bm-4, PROD at `7db035e4` would print its generic `No consensus estimate is served for this line` in a cell whose consensus exists and is withheld. The measurements above do not depend on the order.

## EXPECTED OUTCOME -- both branches, read from the rules above

- **Branch 1 (the table's reading):** after the apply, `r106_fwd_pe_deployed.py verify` reads `R106 FORWARD PE DEPLOYED: YES (7 of 7 arms)` against the capture taken immediately before it: 218 forward P/E rows serve, the 60 different-currency rows are absent from `forecast_figures` and their 60 check rows are gone, each in `model.forecast_withheld` with a reason naming both codes (PBR US: `USD` and `BRL`); every other path of every name is equal modulo clocks and float representation; every other route reads equal; the hold reads ABSENT on all 95; CodeSha256 is NEW and memory, timeout, role, layers and environment read EQUAL.
- **Branch 2 (any other change, a path outside the table, a name that is not 200, or the hold moves):** ROLLBACK below, the same hour, unless the CTO names KEEP on the evidence.

## ROLLBACK

A REBUILD from the live pin `0447f2df38` through ONE `safe-apply`, the same hour. The read-back is the function's behaviour (the 60 rows serve again) and the configuration (the environment, memory, timeout equal); CodeSha256 is compared with the pre value `0pWc69...` and a difference is reported, not assumed away. Change-management entry opened before, closed after.

## NOT COVERED

This half does not cover, and the act may not perform: any S3 write or delete; any change to the role, layers, routes, memory, timeout or environment (the hold stays); any function other than `opal-amgt-scoped-api`; the AI-fill restore (its own order); a portal change; a schedule; any use of Bloomberg. NO OTHER READER runs on the function from the GO until RA1 reports.

**Signature (COO):** signed `2.0.0_SA_COO~R1`, 2026-10-14 (the commit carrying this file is the signature's vintage).
