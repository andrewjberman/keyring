# Naming Centralization -- 4-Step Execution ("Execute") -- 1.0.0_SA_CTO~X

**Date:** 2026-08-18 (~1840-2000Z)
**Task Order:** ad-hoc, Andrew-direct "Execute" on the 4-step centralization plan delivered with the
/draw layers assessment (same terminal, same day as the VUG fix + 59-placeholder sweep)
**Status:** COMPLETE -- all four steps landed, deployed where applicable, verified at the consumed end

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | --name, x3 | PASS | located vendor-manifest.sh, BUILD_MANIFEST precedents, portal files |
| comp-pulse (via safe-commit) | diff, per commit | PASS | clean on all workspace commits |
| /frontend-dev | ui-smoke.mjs attribution + fixtures | PASS | rendered PNG READ; VUG = "Vanguard Growth ETF" server-sourced |

**What worked:** the BUILD_MANIFEST/vendor-manifest.sh precedent (mirror_conversion pattern) meant
step 2 needed ZERO new machinery. **Gap found:** none.

---

## Step 1 -- yang-generate-positioning through the registry (v1.5.5 + v1.5.6)

Inline 29-entry `ETF_NAME_OVERRIDES` DELETED; names resolve registry-first via
`resolve_display_name` (same pattern/role/grant as holdings-attribution). ALSO decommissioned:
`etf_classification.py` inside the lambda dir -- packaged in every deploy yet imported ZERO times and
492 diff-lines stale vs `_shared` (asset-class vocabulary even differed). Pre-deploy prediction
computed against the live registry: 32/32 served tickers resolve, exactly 5 name changes.
**Post-deploy L7 caught a real gap:** only 3 of 5 landed -- AGG/BIL flow through a THIRD path, the
hardcoded `BENCHMARK_ETFS` dict. Patched (names resolve at use time via `benchmark_etf_info`),
redeployed v1.5.6, regenerated: served == the full prediction EXACTLY
(AGG -> 'iShares Core U.S. Aggregate Bond ETF', BIL -> 'State Street SPDR Bloomberg 1-3 Month T-Bill
ETF', DIVZ/IDVZ -> the Opal-branded names the FE mask already displayed, ICSH -> registry form),
non-name payload byte-identical. Commits 1b5493ea23, d6a0e4d36d; ledger
`20260818T1845Z_naming-centralization-phase1-positioning_deploy_completion.md` CLOSED.

## Step 2 -- classifier client single-homed (v1.5.7)

`etf_classifications_dynamodb.py` canonical home now `infra/aws/lambda/v2_portal/_shared/`; the two
per-lambda copies are DECLARED VENDORED ARTIFACTS via `BUILD_MANIFEST.json` + `ci/vendor-manifest.sh`
(the estate's existing mechanism -- mirror_conversion precedent), parity `--check` green both dirs.
The universal py-gate required `from __future__ import annotations` on the new canonical; propagated
by RE-RUNNING the vendor flow (exercising it end-to-end), both lambdas rebuilt + applied (plan 2
in-place / 0-diff), deployed bytes re-hashed. Commits 80-series through e87f3f4576.

## Step 3 -- Attribution frontend overlay retired (portal DEV 8dbaf56b)

Precondition verified on the served vintage first: all 56 tickers real names; classes all
Equity/Fixed Income incl. the fallback's special cases (PFDE/PFOE/UVXY/VXX = Equity).
`ETF_NAME_FALLBACKS` (53 entries) DELETED from holdings-shared; SelectionTab reads
`h.name`/`h.asset_class` directly (5x2 sites) -- repeating the Positioning page's identical
2026-06-01 retirement. The never-read `name` fields stripped from both `etf-categories.ts`
(56 + 36 entries; call-site census shows only `.segment` is consumed). `tsc -b --noEmit` clean;
/frontend-dev headless render with the real served JSON as fixture READ: VUG renders
"Vanguard Growth ETF", all rows named, color law clean. Submodule pointer bumped on CLOUD.

## Step 4 -- tickerRegistry ratified NON-NAMING (portal DEV, second commit)

Measurement first: `displayName` is read by NOTHING (sole importer `dataLoader.ts` consumes
`.ticker` only), and **26 of 51 overlapping values disagreed with the SSOT -- many naming the WRONG
SECURITY outright** (UTWO the 2Y-Treasury ETF as 'ProShares Ultra Russell 2000'; CLIP the T-Bill ETF
as a preferred-stock ETF; XLU as Energy; QBER duplicated into BOTH Equities and Fixed Income with two
fabricated names). Chose Andrew's option B: field STRIPPED from interface + all 54 entries (a
dead-but-wrong naming surface has no offsetting reader), QBER dupe deleted + description corrected,
header marks the file a grouping/typing projection with the SSOT named. Typecheck clean.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Registry-first at every producer name site | one canon, the pattern already proven on holdings-attribution |
| Vendoring over a new Lambda layer | estate mechanism exists (Build Ladder rung 2); zero new infra |
| Verify-then-retire for the FE overlay | the mask's one remaining job (classification) proven served before deletion |
| Strip displayName rather than align it | dead field + 26 wrong values = liability with no reader; option B ratified |
| L7 verify against a PRE-COMMITTED prediction | the AGG/BIL miss was caught BY the prediction, found the third name path |

## Residuals (surfaced, not chased)

- ICSH canon-content question: registry says 'iShares Ultra Short-Term Bond ETF'; two estate comments
  say 'BlackRock ...' (issuer rebrand vintage). One-row canon fix once ruled -- that being a ONE-row
  fix in ONE place is the centralization working.
- `yang-generate-positioning` still inlines ETF_CLASSIFICATIONS / management-style / sector dicts
  (classification, not naming -- same disease, different organ; a follow-up ruling can route them
  through the registry the same way).
- `tickerRegistry.ts` `description` fields share displayName's fabrication problem (also unread);
  left in place as non-naming scope.
- Workspace CLOUD commits + tags v1.5.5-7 and portal DEV commits ride the integration window
  (lanes commit, integrators push).
