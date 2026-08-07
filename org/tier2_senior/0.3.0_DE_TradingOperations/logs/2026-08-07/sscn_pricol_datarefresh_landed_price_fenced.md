# SSCN_PRICOL — DataRefresh half landed; price half fenced to the producer and rerouted

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE

Session 1945Z–2115Z, 2026-08-07. Serial `0.3.0_DE_TradingOperations`.
Spawned for SSCN_PRICOL under a hard external clock — Andrew promised Yang Liu in
Teams at 19:18:39Z, "Yes ok will have it within the hour or so" (outer edge ~2018Z).

## Summary

Two-part display-layer job. **Half (b) landed inside the window. Half (a) was NOT a
display-layer job at all** — it was blocked at the producer, which I surfaced at 20:08Z
rather than absorbing. Andrew then rerouted the producer fix to `0.3.0_DT` directly.

## The finding (the substantive part)

The project premise was "the price data ALREADY EXISTS, point at it." That premise is
**TRUE OF THE EXCEL AND FALSE OF THE SERVED JSON**, and the portal only ever sees the
served JSON.

Grounded on the SERVED ARTIFACT, not source alone:
`s3://opal-data-portal-v2/json/security_scanner/latest/universes/sp500/universe_data.json`
(written 2026-08-07 15:00:33Z, asOf 2026-08-06 — Yang's own upload). 502 securities,
row keys exactly `ticker,name,mktVal,country,sector,industryGroup,universeWeight,divzWeight`,
284 factor codes in `values{}`, **price-like codes = ZERO**. Re-checked on `acwx`:
identical schema, same absence.

Mechanism, source-confirmed at `infra/aws/lambda/opal_security_scanner_processor/lambda_function.py`
@`5fd7d60495`:
- `:78` — `NON_SCORING_COLS` explicitly contains `"price"` (with `price_split`, `price_unadj`)
- `:328` — `scoring_cols = [c for c in df.columns if c not in NON_SCORING_COLS]` → price dropped
- `:232-242` / `:272-283` — both row builders emit a FIXED 8-key row; no price

**The detail worth keeping (MSTR asked it be carried): `"price"` sitting IN the exclusion
list is POSITIVE evidence the Excel carries the column.** `NON_SCORING_COLS` is derived
from `source_headers_20251028.json`, so an exclusion list became confirmation of Yang's
claim. Andrew independently confirmed the column letter ("its in column AB").

Later verified directly on the live workbook (339 cols, 2,864 rows, `header=4` as the
producer reads it): **column AB (idx 27) header is literally `'price'`**, lowercase, no
whitespace — so the producer's `row.get("price")` resolves and will not silently emit
nulls. AAPL 312.41, MSFT 499.86. Andrew's motivating ticker **AU: price 87.59,
mkt_val 44,233.6 ($M = 44.2b, matching his "~44.2b"), member of `wt_iwb` (r1000) ONLY** —
not sp500, which is why earlier sp500/acwx probes showed AU absent.

### Second finding — currency (display-layer, mine)
`price` is in **LOCAL TRADING CURRENCY**, not USD.
- sp500 / r1000 / r1000v (`US_ONLY_UNIVERSES`): only UNITED STATES; max 6,304.81 (NVR) → USD
- acwx / eafe / eafev: 47 / 23 / 23 countries; 126 / 27 / 8 names priced >10,000; acwx max
  2,708,000 (South Korea) → local currency

My first draft formatted `$${value}`, which would have rendered a Korean listing as
"$2,708,000.00". Staged patch corrected to prefix `$` only for `US_ONLY_UNIVERSES` and to
label the rest local-currency in the header tooltip. Flagged to DT with an explicit
**do NOT convert at the Lambda** — an FX normalization would be a derivation, outside the fence.

## What landed

**portal DEV `7877d7e1`** (local, unpushed — option (b), DT pushes):
`fix(DataRefresh): advertise the file types the upload ACTUALLY accepts — the path worked, the UI just never said so`
2 files, 30 insertions(+), 4 deletions(-).

The gap was NOT where the brief pointed. `FILE_TYPE_LABELS:14` already had
`screening_excel`, and `CurrentStatePanel`'s "Data Sources" list is DATA-DRIVEN off the
served manifest — which already carries `screening_excel` (`updated_at` 19:00:59Z, i.e.
Yang's own upload put it there). **That list had self-healed before I arrived.**

The real defect was one panel over: the HARDCODED "Supported File Types" reference in
`UploadTab.tsx`, whose `*.xlsx` card enumerated only "CMA, peer performance, or
attribution". The upload classifier (`infra/aws/lambda/data_refresh/lambda_function.py:242-252`)
branches on FIVE xlsx keywords — `screening`, `cma`, `peer`, `attribution`, `saa`. The UI
advertised three of five and both omissions were real accepted types, one of them Yang's.
That is exactly Andrew's "I must not have adjusted the sample data examples." Panel now
mirrors the classifier one-to-one.

Also added `saa_excel: 'SAA Analysis'` to `FILE_TYPE_LABELS` — a real backend type
(`:252`) with no label, and `CurrentStatePanel.tsx:137` falls back to the raw key, so an
SAA upload would have rendered "saa_excel" at the user. Same defect class, same list, one
line. Judged in-scope as display-layer and flagged explicitly rather than buried.

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| `comp-which` | "which lambda/script produces universe_data.json" | PASS | near-tie, surfaced comp-estate / comp-pipescript; routed me to comp-find |
| `comp-find` | `'universe_data.json'` | PASS | DENOMINATOR 83 hits / 24,878 files, banded HEAD/SURFACED/CONFIG/DOC — the SURFACED band isolated both Lambdas immediately; band separation did the work a raw grep could not |
| `Grep` (native) | `market_?[Cc]ap` over portal/src | PASS | confirmed CTO's warning: zero hits under SecurityScanner/**; the column is `mktVal` |

**What worked:** `comp-find`'s band + denominator output put the producer in hand in one
call — the DOC band (71 of 83 hits) would have buried the 2 source files in a raw grep.
**What failed:** the `.tools/aws` shim silently reported `rc=0` on `aws s3 cp` while
writing no file, twice, under an `ANDREW~1` 8.3 path — the documented silent-shim class.
Worked around via PowerShell. **Gap found:** none new; the shim failure is already
CLAUDE.md-recorded, but it cost ~3 minutes against a live external clock.

## Files Modified

see commit message: `7877d7e1` (portal). Workspace-side: this log only.

## Blockers

**None on me.** Half (a) is not blocked-on-DE — it is OWNED ELSEWHERE by Andrew's word.
Producer edit exists at `:245`/`:288` (AE-authored, correct, `price` properly left in
`NON_SCORING_COLS`) but is **UNCOMMITTED, UNDEPLOYED, NOT RE-TRIGGERED** — the served
artifact is byte-unchanged. That is the silent-no-op I flagged at 20:08Z: a source edit
every config-level check calls GREEN while the user still sees nothing.

## Current State

- `portal` main tree on **DEV** throughout (Rule 19), never moved. Commit `7877d7e1` is
  LOCAL and UNPUSHED; `0.3.0_DT` owns push + promote (option (b), lanes commit / integrators push).
- Local DEV sits 2 commits ahead of origin/DEV independent of me (`e293ec5e` CTO~C
  comment-only; `e6bca5ce` Andrew's surface-check retirement). DT is carrying them knowingly.
- typecheck `tsc -b --noEmit`: **exit 0**. lint: 1 error, **pre-existing and not mine** —
  `ModelPortfolios.tsx:15:149` unused `ReferenceLine`; neither changed file appears in lint
  output. Deliberately not fixed (unrelated page; tidying it into a time-boxed promote
  breaks a clean rollback).
- Rendered `/data-refresh` headless and READ the PNG per portal CLAUDE.md ("a grep cannot
  see contrast"): all 8 cards inside `Panel variant="chart"` (navy) so the amber/emerald
  idiom is legal; nothing light on the silver canvas. Artifact
  `portal/.frontend-dev/screenshots/sscn_pricol_datarefresh.png`.
- **Price column: PREPARED, NOT APPLIED**, per MSTR ruling 20:12Z (a dormant column renders
  502 em-dashes and reads as BROKEN, not pending). Full patch with currency handling +
  verify steps staged OUTSIDE the portal tree so it cannot pollute DT's promote:
  `C:\Users\AndrewBerman\AppData\Local\Temp\claude\sscn\READY_price_column_patch.md`.
  Target: immediately before the `field: 'mktVal'` block in
  `portal/src/pages/SecurityScanner/tabs/UniverseDataTab.tsx` (:90) and
  `UniverseScannerTab.tsx` (:261), plus `price: number | null` on both row interfaces in
  `types.ts`.

## MCP traffic

7 messages. Significant: MSTR `[GO]` inbound; my `[FENCE HIT]` to MSTR + CTO at 20:08/20:10Z;
MSTR ACK endorsing the hold-the-dormant-column call and setting acceptance at the SERVED
artifact; DT's staging question (answered (b)); my Andrew-direct reroute to DT + hand-off
request to AE.

**ANDREW-DIRECT this session, verbatim, 3 messages ~2050Z:**
1. "I see you all saying you cant find the price column or its not in the data set. Yes it is, its in column AB."
2. "oh nevermind looks like AE already did it"
3. "have 0.3.0_DT do it, they should have cloud permissions for lambdas."

Relayed to DT and AE; scope NOT widened. Note on (1): my finding was never "price is not in
the dataset" — it was that price is absent from the SERVED JSON, citing the exclusion list
as evidence the Excel column exists. The finding appears to have been FLATTENED in relay
into "the data isn't there." The layer distinction WAS the finding; worth knowing which hop
lost it.

## Next Steps

1. **[0.3.0_DT_TradingOperations]** Push DEV + promote `7877d7e1`. Independently: commit the
   producer edit, Terraform deploy (`safe-apply`, never bare apply, never
   `update-function-code`), **RE-TRIGGER** against
   `s3://.../security_scanner/uploads/2026-08-06/Screening_DIVZ_IDVZ_20260806.xlsx`, and
   verify on the SERVED artifact (write time must move off 15:00:33Z AND a row must carry a
   price value). Spot-check AU in **r1000**, not sp500.
2. **[0.3.0_DE_TradingOperations]** On DT's green: apply the staged patch, typecheck, render +
   READ the screenshot, confirm REAL values (not em-dashes) in one US and one international
   universe, commit.
3. **[0.7.0_AE_CloudOps]** Hand off / do not double-deploy; escalate loudly if already mid-deploy.
