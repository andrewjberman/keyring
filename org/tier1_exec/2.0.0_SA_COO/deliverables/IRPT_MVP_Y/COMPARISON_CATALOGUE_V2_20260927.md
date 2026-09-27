# The maintained comparison catalogue, v2: 4/4 identities verified on current reads; permission is Andrew's word

Author `2.0.0_SA_COO~Y`, 2026-09-27 ~21:1xZ. Scope: FWD-4's Comparison and Multi-Comp arms. Rulings:
- CTO 102028 (1): the reads;
- Andrew-direct "call 1 yes" (CTO 102046, record @fce766f6ed): the permission.

## The evidence and its grade

- P's window 18 read the 4 identities: `IRPT_MVP_P/COMPARISON_IDENTITY_READS_W18_20260927.json` (sha256 `424eb3bf..`,
  retrieved 20:52:56Z, @c3e77cb937). All 4 answered HTTP 200 with JSON, and no read stopped.
- The grade is `COMPARISON_IDENTITY_GRADE_W18_20260927.json`, from `live_walk/comparison_identity.py`: **IDENTITY
  4/4**, with no reads outside the catalogue.

| Key | Id | Returned name (verbatim) | Type |
|---|---|---|---|
| opal_long_term | P:1728413 | "Opal Long-Term " (trailing space) | model_portfolio |
| opal_short_term | P:1728415 | "Opal Short-Term" | model_portfolio |
| opal_intermediate_term | P:1728315 | "Opal Intermediate-Term" | model_portfolio |
| opal_ultra_long_term | P:1728420 | "Opal Ultra Long-Term " (trailing space) | model_portfolio |

Names are compared stripped, as the research worker compared them. The returned names are recorded verbatim.

## The catalogue (Y @c5aa93d60e; `P_COMPARISON_CATALOGUE_V2_20260927.patch`, apply-check rc=0 on P `12a67ed5ee`)

`ycharts/generate/templates.json` `comparison_catalog` changes only:
- `candidate_version` is `irpt-ycharts-comparison-candidate.20260927.v2`.
- `admission` is `IDENTITY_VERIFIED_PERMISSION_WORD_GRANTED_M_VALIDATION_PENDING`.
- per entry, `identity_status` is `VERIFIED`, and `entitlement_status` is `WORD_GRANTED_FIRMS_PENDING_M`.
- `verification_ref` holds the evidence path and sha, `retrieved_at`, reader, grader, returned name, type and
  instance id, `permission_ref` and `permission_scope` (firms that already see these models in Model Portfolios,
  FWD-11).
- `permitted_firm_ids` stays `[]`: **M resolves the firms**.

## What this does and does not enable

- **Nothing new is served by this file alone.** The served generate's `maintained_sources.resolve_comparison_fields`
  requires candidate v1, then refuses every selection.
- With v2 it refuses "catalogue unavailable" instead of "unverified"; a comparison is refused either way.
- A selection is admitted only when M's reviewed policy consumer accepts v2 and the viewer's firm is in
  `permitted_firm_ids`.
- The Overview thread is unaffected. The served generate zip with this file overlaid ACCEPTS window 15's input
  (31/31 modules from the extract). The resident runs from the frozen composition and never re-reads the catalogue.

Checks:
- The grader re-run on the new file: 4/4.
- generate suite: 281 passed, 30 skipped. `test_recipe_title_source` fails at HEAD without this change:
  `maintained_sources._owner_binding` is absent from the Y worktree's `_scope` copy.
- `_scope` `test_maintained_sources`: 26 passed.

## Next, by owner

- **2.0.0_SA_COO~M:** validate, resolve `permitted_firm_ids` under FWD-11, and review the consumer that admits v2.
- **2.0.0_SA_COO~P:** package this `templates.json` into generate AND the resident in one release. Their
  `configuration_sha256` differs from the current file's, but only new compositions record it.
- **2.0.0_SA_COO~Y:** once M's consumer admits a selection, the Comparison variant goes live in a window (Y4/Y7's next
  case).
