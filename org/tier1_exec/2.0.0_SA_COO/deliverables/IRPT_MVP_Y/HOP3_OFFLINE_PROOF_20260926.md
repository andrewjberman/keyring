# Hop 3 proved offline -- the whole /analysis composition, then the resident's replay to the vendor boundary

Author `2.0.0_SA_COO~Y`, 2026-09-26 ~18:5xZ. **Order:** CTO 101355 ("prove the WHOLE /analysis composition WITHOUT a
principal ... 0 refusals, every resolver producing, a printed list of each stage reached") before any window 4.

## Result

With the fix patch `P_HOP3_SUBMISSION_FIXES_20260926.patch` (this folder), the deployed generate code handles one
Opal POST /analysis on window 3's real input with report_title null:
- 0 refusals and 26 stages, through the queue send;
- the resident's own admission code then admits the captured composition and reaches the vendor boundary.

Without the patch, the same runs reproduce window 3's live refusal. The runs also found **two more defects the live
path would have hit next**. Each would have cost a window.

## Instruments (committed beside this file, in `live_walk/`)

- `offline_submit_proof.py`:
  - the served zip `85TXFzzv` is extracted fresh and FIRST on sys.path (`--overlay` copies fixed files over it);
  - the real `generate_installed.compose_ports` + `build_boundary` + served Entry handle one API-Gateway-shaped event
    (verified-edge Opal headers, `selected_tenant=cottonwood`);
  - every READ goes to the live table and bucket; every WRITE is captured in memory and never leaves the process;
  - a call tracer records the stages;
  - a module census proves every first-party module came from the extract (31/31 in every run below).
- `resident_admission_replay.py`: the captured composition is replayed through the resident package `f624e8a72f`'s OWN
  `CompositionAdmission.validate` and `recipe_snapshot.consume_configuration`, which is everything the resident does
  before its vendor session.

Input: window 3's `portfolio_d188498ed12466f72431cb45199997ee457d7efc94f70bd8d35e0e64bcdae512` (cottonwood, template
lane, AAPL 10.01 / VNQ 2.02). The seeded fact is the deleted walk principal's profile row.

## The runs, in order

| # | Code | Result | What it showed |
|---|---|---|---|
| 1 | served zip, no overlay (negative control) | REFUSED `MaintainedSourceRefused: maintained recipe title descriptor required`, public UNEXPECTED, 0 writes | reproduces window 3's live K5 exactly (corr-85a852bf59dd) |
| 2 | + title producer (templates.json default_report_title, recipe_snapshot.capture_title_source, prospect/custody wiring; CTO 101367) | REFUSED `FileNotFoundError ...\intake\settings.json` | **NEW DEFECT 1:** `recipe.py:61` resolves `settings.json` at `../../intake/` (the tree layout). In the flat Lambda that is `/intake/settings.json`, which does not exist; the zip stages it beside recipe.py. Every null-title submission would have failed here. |
| 3 | + recipe.py packaged-settings path | REFUSED `SubmissionRefused: EXACT_PROSPECT_OWNER_REQUIRED` | **NEW DEFECT 2:** `submission.py:97,132` bound and admitted only `CSV_UPLOAD` inputs. An Opal submission on a `TEMPLATE_UPLOAD` input is refused. The live ARTIFACT# rows (6/6) show both lanes store under the same upload-scoped owner. |
| 4 | + submission.py PROSPECT_UPLOAD_LANES, a DIFFERENT viewer than the uploader | REFUSED `CompositionRefused: SOURCE_OWNER_BINDING` | the title descriptor binds the ACTOR (maintained_sources:487), while request_composition:88-92 binds every non-configuration source to the INPUT OWNER. They agree only when uploader = submitter. Parked for M below; the live flow is the same principal. |
| 5 | same fixes, viewer = the window-3 uploader (the live flow) | **ACCEPTED**, 26 stages, stopped at the queue send | see below |
| 6 | resident f624e8a72f as deployed, replaying run 5's composition | REFUSED `EXACT_PROSPECT_OWNER_REQUIRED` | the resident carries the same submission.py (5460fcdccd): **it must be redeployed with the lane fix too** |
| 7 | resident + the submission.py fix | **ADMITTED** | reaches the vendor boundary |

### Run 5: stages reached (26)

validate_public_request, generate_installed.submit, uploads.read_input, **recipe_snapshot.capture_title_source**,
**maintained_sources.resolve_profile_fields**, **maintained_sources.resolve_comparison_fields**,
**recipe_snapshot.capture_configuration**, **request_composition.validate_bindings**, repository.put (REQUEST_COMPOSITION),
retention.reserve/publish, repository.publish, **acceptance.accept**, request_composition.validate_bindings (replay),
**acceptance.dispatch**, **generate_installed.send**.

Captured writes, 9, none sent:
- RETENTION# and ARTIFACT# rows;
- the REQUEST_COMPOSITION object at `opal-data-irpt/irpt/cottonwood/state/request_compositions/ART-.../...json`;
- the `analysis#REQ-...#1` request row and the `REQ-...` job row, in one transaction;
- outbox SENDING, then ONE `analysis_generate` message, then outbox SENT.

The frozen composition carries `report_title='Portfolio Overview'` from source `maintained-recipe-title`
(RECIPE_CONFIGURATION), and `organization='Opal Capital'`, read from the live table.

### Run 7: resident stages reached

1. admission.validate: schema, compose_frozen_request, validate_bindings, verify_frozen_portfolio.
2. consume_configuration: template 14141822, OVERVIEW.
3. The profile is ready (title 'Portfolio Overview').
4. The frozen holdings for the vendor upload: AAPL 10.01, VNQ 2.02, total 12.03.

The next act is the vendor session.

## Regression (P's tip f35dfe003c + the patch, a scratch copy)

- 11 new tests pass (`test_recipe_title_source.py` 7, `test_template_lane_submission.py` 4).
- ycharts/generate + _scope show 6 failed / 458 passed, against 6 failed / 447 passed unpatched. The 6 failure ids are
  IDENTICAL, all pre-existing: test_custody_binding M-publication replay x5 and test_resolve header x1.

## What must ship, and what this does not prove

- **Both** functions: `irpt-ycharts-generate` (all 6 source files) and the resident (`submission.py`; its tree-layout
  settings path already resolves, and it needs no title producer).
- This proves the composition offline on live-read data. After the deploy, the same `offline_submit_proof.py`, run on
  the NEW served zip with no overlay, is the deployed-code proof to pin in window 4's packet.
- Not proved: the vendor session and PDF (hops 6-7). The resident's replay stops before them.
- **Parked for 2.0.0_SA_COO~M:** `request_composition.py:88` exempts only recipe_source_id and settings_source_id from
  the input-owner binding. A null-title submission by a DIFFERENT Opal viewer than the uploader (a supported case) is
  refused SOURCE_OWNER_BINDING. Un-parks when cross-viewer submission is in scope; the REC is to add the recipe title
  source id to that exempt set.
- Parked for 2.0.0_SA_COO~P: the zip's staged `settings.json` (pin dc5d119b84) differs from the tree's current one in
  non-value fields. All 7 setting values are equal.
