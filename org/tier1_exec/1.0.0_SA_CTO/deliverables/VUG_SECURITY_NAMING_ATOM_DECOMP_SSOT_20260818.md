# VUG SECURITY-NAMING DEFECT -- ATOM_DECOMP SSOT RECTANGLE (focused run)

**Author:** 1.0.0_SA_CTO~X
**Date:** 2026-08-18, measurements ~1600-1700Z this session (each cell's evidence gathered live this session unless noted)
**Authorization:** Andrew-direct at this terminal, 2026-08-18 (screenshot + instruction): investigate the
security filtering/naming system behind the Positioning-page Attribution Breakdown, identify why ticker
VUG renders `1.61931034482759` in the NAME column, rectify end-to-end incl. redeploy, log step-by-step,
and "Begin with atom_decomp workflow to establish ground truth ... rigorous SSOT before beginning work."
**Method:** `projects/ATOM_DECOMP/skill/atomic-decomposition/SKILL.md` Rule 14, FOCUSED single-seat run.

## Boundaries (SKILL.md: "A focused run may omit a phase only when the omission cannot affect the conclusion and is recorded as a boundary")

- OMITTED: multi-agent status-missioned fan-out (14c), sealed-mutant certification + standing certifier
  seat (14e), phases P5-P12 (migration/cutover machinery). Why safe: this is a display-name defect with a
  two-file code fix + one data row, not a migration; every load-bearing cell below is MEASURED on a live
  primary read performed this session by this seat -- there is no INFERRED cell for a fan-out to kill.
- SCOPE: the Yang positioning/attribution naming chain. NOT decomposed: news/advi/market naming, the
  bd-securities classifier consumers (noted as edges, below).
- This run doubles as evidence toward ATOM_DECOMP M1 ("the ETF/Positioning fold-in" -- the registration
  brief's own Andrew-suggested proving subject), but it is a FOCUSED run, not the certified M1 execution.

## The symptom (MEASURED)

Portal Positioning page, Attribution Breakdown table: row `VUG` renders NAME = `1.61931034482759`.
Served JSON (`s3://opal-data-portal-v2/json/positioning/holdings_attribution_data.json`, generated_at
2026-08-04T22:32:55Z, as_of 2026-07-31) carries for VUG four distinct numeric `name` values -- one per
period sheet: {1.61931034482759, 0.416312056737589, 4.1, 0.935458167330677}.

## SSOT RECTANGLE -- entity x {value, status, evidence}

Statuses per SKILL.md: PROVEN (measured on the primary this session). No CONTRADICTED cells remain;
one UNKNOWN is recorded at the bottom.

| # | Entity (surface) | Finding (value) | Status | Evidence (locator @ this session) |
|---|---|---|---|---|
| 1 | Served artifact `json/positioning/holdings_attribution_data.json` | `name` field is NEVER a real security name in the current vintage: 56 held tickers; names are numeric junk or `--`. VUG = 4 numeric values (one per period sheet) | PROVEN | downloaded bytes, full-file census (DENOMINATOR 56 tickers) |
| 2 | Producer `yang-generate-holdings-attribution` `lambda_function.py:574` | `name` read from hardcoded Excel col idx 4 ("Column E"), a vestige of the pre-2026-06 format | PROVEN | source read; repo == deployed (below) |
| 3 | Deployed bytes vs repo (Rule 22a CODE layer) | sha256 MATCH on both members (`lambda_function.py` 69a45613..., `etf_classifications_dynamodb.py` 9b29d0e8...) -- no drift, repo is the executing code | PROVEN | deployed zip downloaded via `lambda get-function`, member-hashed vs source-map dir |
| 4 | Source workbook `uploads/Model Portfolio Attribution 20260731.xlsx` | Sheets `_QTD/_YTD/_1Y/_SI`; header row 8: col0=Ticker, col1=hierarchy label, col2+=portfolio numeric blocks. **There is NO name column.** Col 4 = first portfolio's (ULT) Style Bench Average Weight -- the numeric that lands in `name`, per sheet, hence 4 distinct values | PROVEN | workbook downloaded + parsed; layout printed |
| 5 | History of the shift | June-2026 export shifted portfolio blocks left by 3 cols; portfolio DETECTION was made scan-based (`lambda_function.py:226-247` comment records it) but the shared name-column read at `:574` was left hardcoded | PROVEN | in-file comment + measured current layout |
| 6 | DynamoDB `etf-classifications` (declared SSOT: module docstring "single source of truth"; TF-managed `infra/aws/terraform/yang-pipeline/etf-classifications.tf`) | 116 rows (scan, no LastEvaluatedKey). VUG row EXISTS but `name='VUG'` -- placeholder (`updated_by: seed-script`, 2026-02-19). 60/116 rows carry ticker-as-name placeholders, all `seed-script` | PROVEN | full table scan this session |
| 7 | Intersection: held x defective | **VUG is the ONLY held ticker (of 56) whose DDB name is a placeholder; the ONLY one absent from `CANONICAL_SECURITIES`; absent from `_shared` `ETF_NAME_OVERRIDES`; absent from all 4 portal maps** (`tickerRegistry.ts`, 2x `etf-categories.ts`, `holdings-shared.tsx` -- 0 occurrences each) | PROVEN | programmatic intersections + per-file membership counts |
| 8 | Producer's classifier use | Lambda queries DDB per ticker (`:577`) for asset_class/sub_asset_class but NEVER uses `classification['name']` | PROVEN | source read |
| 9 | Frontend mask `portal/src/pages/Attribution/tabs/SelectionTab.tsx` (:162,:193,:262,:310) | `ETF_NAME_FALLBACKS[h.ticker]?.name \|\| h.name` -- a hardcoded map masks the junk for every held ticker EXCEPT VUG, which falls through to the served junk. This is why only VUG shows the defect | PROVEN | source read + map membership (VUG=0) |
| 10 | Canonical display name for VUG | **"Vanguard Growth ETF"** -- already served in-estate by the sibling producer: `positioning_data.json` carries `{"ticker":"VUG","name":"Vanguard Growth ETF",...}` (PKL metadata via `yang-generate-positioning`) | PROVEN | served artifact read |
| 11 | Sibling artifacts | `positioning_data.json`: VUG name correct. `allocation_summary.json`: no per-ticker names (VUG absent) -- both unaffected | PROVEN | served artifact reads |
| 12 | Name-data supply chain | `_shared/etf_classification.py` `ETF_NAME_OVERRIDES` -> `seed-etf-classifications.py` writes `name = OVERRIDES.get(ticker, ticker)` (the placeholder mechanism, incl. VUG's) -> DDB. Separately `data/black_diamond/scripts/classification/seed_canonical_securities.py` `CANONICAL_SECURITIES` (last verified 2026-03-25) upserts bd-securities + (--yang) etf-classifications with real names (`canonical_si_seed` -- the path that fixed VTV). VUG joined the models AFTER that sweep and was registered NOWHERE | PROVEN | seeder sources read; DDB `updated_by` fields |
| 13 | Seeder blast radius (guards the data fix) | `seed_canonical_securities.py --yang` `put_item` omits `management_style`/`sector` -- a full-item replace DROPS those attrs from rows that have them (VTV row measurably lost both). A wholesale re-run is therefore NOT the remediation vehicle for one row | PROVEN | seeder write-path read + VTV row attrs |
| 14 | Trigger/production path | Step Functions `yang-pipeline` state `GenerateHoldingsAttribution` (choice on `$.manifest.files.attribution_excel`, monthly upload, pattern `Model Portfolio Attribution.*?(\d{8})\.xlsx`); handler consumes only `manifest` (bucket+files) and `data_as_of_date`. Last production input: the 2026-08-04 upload of `Model Portfolio Attribution 20260731.xlsx` | PROVEN | SFN definition + handler source + uploads listing |
| 15 | Deploy mechanism | TF-only via `modules/yang-lambda` reading `s3://opal-313476888478-lambda-artifacts/yang-pipeline/yang-generate-holdings-attribution.zip` (version + content-sha256 metadata); build+stage via `infra/aws/lambda/ci/build-and-upload.sh yang-pipeline <fn>` (commit-first gate in the script header); then plan -> safe-apply -> 0-diff -> record-terraform-deploy -> tag+push | PROVEN | module + script sources |
| 16 | Commit lanes | `infra/aws/lambda/v2_portal/yang_pipeline/**` = lane YANG_PIPELINE_DEPLOY; `data/black_diamond/**` = lane POD4; neither admits 1.0.0_SA_CTO~X -> Rule 14a audited `GIT_COMMIT_AUTHOR_OVERRIDE=<LANE>`, one lane per commit | PROVEN | `.owned-paths.yaml` read |

**UNKNOWN (owned, non-blocking):** which consumers (if any) read `management_style`/`sector` off
`etf-classifications` -- matters only to a future wholesale reseed, not to this fix (cell 13's guard
means we touch only VUG's `name` via attribute-preserving update). Owner: noted for the log.

## Root cause, stated once

Two stacked defects, one exposure:
(1) **Producer**: the current workbook format carries no name column, and `lambda_function.py:574` still
reads col 4 as the name -- so every emitted `name` is a benchmark-weight numeric (or `--`).
(2) **Registry**: VUG's row in the declared SSOT (`etf-classifications`) still carries the seed
placeholder `name='VUG'`, because VUG entered the models after the 2026-03-25 canonical sweep and was
never added to any naming surface.
The frontend's hardcoded `ETF_NAME_FALLBACKS` masks (1) for every held ticker except VUG -- which is why
exactly one row leaks the junk, and why the defect survived since at least the 2026-08-04 generation.

## Fix design (each element cites its cells)

- **F1 code** (cells 2,4,5,8,10): in the horizontal parser, resolve the display name
  DDB-registry-name -> Excel-value-only-if-it-is-a-plausible-name -> ticker; a numeric or `--` or
  ticker-equal value is never accepted as a name. The classifier lookup already sits in the loop -- zero
  added I/O. Vertical (pre-2026) parser untouched: its format carried real names in its name column.
- **F2 data** (cells 6,7,13): targeted attribute-preserving `update-item` on VUG only:
  `name = 'Vanguard Growth ETF'`. NOT a wholesale seeder run (cell 13).
- **F3 repo registry parity** (cells 7,12): add VUG to `CANONICAL_SECURITIES` (equity / US Large Cap)
  and to `_shared` `ETF_NAME_OVERRIDES` -- otherwise the next `seed-etf-classifications.py` run would
  REGRESS the DDB name back to the placeholder.
- **F4 deploy** (cells 3,15,16): commit (lane-per-commit) -> build-and-upload -> plan -> safe-apply ->
  0-diff -> record -> tag+push; deploy-completion ledger opened at start.
- **F5 regenerate + verify** (cells 1,14): re-fire the production input (the 20260731 manifest event)
  against the redeployed function; verify the served JSON carries real names (VUG = "Vanguard Growth
  ETF", zero numeric names across all 56 tickers); frontend needs NO change -- VUG is not in
  `ETF_NAME_FALLBACKS`, so the fixed `h.name` flows straight to the render.
- **Deliberately NOT done**: no new monitor/alert (standing moratorium); no 5th hardcoded frontend map
  entry (Build Ladder rung 1 -- the JSON now carries the truth); no wholesale DDB reseed (cell 13); no
  consolidation of the 4 portal maps or the 2 classifier-module copies (surfaced below, not chased --
  remediation is not authorized by a finding).

## Surfaced-not-chased (for the record)

- The `etf_classifications_dynamodb.py` module exists as TWO byte-copies (holdings-attribution +
  generate-positioning dirs) -- the two-homes class of Rule 22a.
- 59 non-held DDB rows still carry ticker-as-name placeholders (harmless today; they become live the day
  such a ticker enters a model -- exactly how VUG happened).
- The portal carries 4 overlapping hardcoded ticker->name maps; the DDB table's own docstring says it
  exists to replace exactly these.
- `seed_canonical_securities.py --yang` strips `management_style`/`sector` on rows it touches (cell 13).
