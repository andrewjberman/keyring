# A second Opal viewer's null-title submission -- the request_composition binding, fixed and proved offline

Author `2.0.0_SA_COO~Y`, 2026-09-26 ~20:0xZ. Routed to `2.0.0_SA_COO~P`: `.owned-paths.yaml:1125` gives
`infra/aws/lambda/investor-reporting/reports/**` to lane IRPT_COMPLETION_P. `2.0.0_SA_COO~M` reviewed it (101479).

**Order:** Andrew at the ~Y terminal, option 4 of ~Y's /next-steps. The seam was parked in `STATUS~Y.md` from proof run 4
(`HOP3_OFFLINE_PROOF_20260926.md`).

## The seam

- `maintained_sources.py:487` mints the maintained recipe TITLE descriptor (CTO 101367) for the ACTUAL SUBMITTER: "Recipe
  configuration belongs to its actual submitter."
- `request_composition.py:88-92` binds only `recipe_source_id` and `settings_source_id` to the request owner, and every
  other source to the INPUT's creator.
- When the submitter differs from the uploader, which is a supported case for an Opal viewer, a null title is refused
  `SOURCE_OWNER_BINDING`, in generate AND in the resident's replay.

## The fix: `M_CROSS_VIEWER_TITLE_BINDING_20260926.patch` (this folder)

When the `report_title` provenance source is `RECIPE_CONFIGURATION`, its id joins `configuration_ids`, so it binds the
request owner exactly as the recipe and settings do. apply-check rc=0 on CLOUD and on P's tree; blob `b82c1ad7d7`
before.

## Proof

Served zip `85TXFzzv` plus P's six deployed files (`a219094b1a`, LF) = the served `/iFhTAvT` content, on window 3's real
input with report_title null:

| Run | Viewer | Result |
|---|---|---|
| deployed six, no fix (negative control) | a SECOND Opal viewer | REFUSED `SOURCE_OWNER_BINDING` |
| + this fix | a SECOND Opal viewer | **ACCEPTED**, `analysis_generate` queued, title 'Portfolio Overview', 31/31 modules from the extract |
| + this fix | the uploader (the live flow, regression) | **ACCEPTED** |
| resident f624e8a72f + deployed six, no fix, on the second-viewer composition | -- | REFUSED `SOURCE_OWNER_BINDING` |
| resident + deployed six + this fix | -- | **ADMITTED** to the vendor boundary (template 14141822, AAPL 10.01 / VNQ 2.02) |

Regression at P's tip, with the fix applied in a scratch copy:
- `_contracts/test_request_composition.py`: 50/50 before and after.
- `_contracts`: 35 failed / 145 passed before and after, with identical failure ids (pre-existing).
- `reports/tests`: 81 passed, 7 errors, before and after.

## What ships

`reports/request_composition.py` in BOTH `irpt-ycharts-generate` and the resident package. Not on the next window's
path: the same principal uploads and submits, and that case already passes.

## Review (2.0.0_SA_COO~M, 101479)

M found the binding change correct and scoped to RECIPE_CONFIGURATION, and proposed a guard, `title_id in sources and ...`,
for a title source absent from `sources`. The patch is unchanged, because the guard would not change the outcome:
- Without the guard, the absent id raises KeyError at the new line.
- With the guard, the same absent id raises KeyError at the profile loop (`sources[fact["source_id"]]`, :115).
- In both cases, `except (KeyError, TypeError, ValueError)` at :250-253 converts it to a `COMPOSITION_BINDING` refusal,
  not a crash.
