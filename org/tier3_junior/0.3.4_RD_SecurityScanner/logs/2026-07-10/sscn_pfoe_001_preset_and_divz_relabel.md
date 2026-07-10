# SSCN_PFOE.001 -- Add PFOE preset + relabel DIVZ
**archetype:** IMPLEMENT

**Agent:** 0.3.4_RD_SecurityScanner
**Date:** 2026-07-10
**TO:** org/tier3_junior/0.3.4_RD_SecurityScanner/task_orders/SSCN_PFOE.001.add-pfoe-preset-relabel-divz.md
**Issued by:** 2.0.0_SA_COO~C | **Arch-gate:** 1.0.0_SA_CTO~C | **RAVC:** COO~C
**PRD:** docs/architecture/SSCN_PFOE.md (v0.1, CTO~C @ e010d37b3)

## What

Pure-frontend config change to `portal/src/pages/SecurityScanner/constants.ts` (single file):

1. **Added `PFOE_PRESET`** -- a readonly `PresetEntry[]` of 16 factors (Appendix A verbatim),
   Sum weight = 100 (Growth 42 / Quality 30 / Sentiment 10 / Valuation 8 / Momentum 10).
2. **Registered `PRESETS['pfoe']`** -- `{ id:'pfoe', label:'PFOE', universe:'r1000', entries: PFOE_PRESET }`.
3. **Extended `PresetGroup` union + `PRESET_GROUP_ORDER`** with `'Growth' | 'Sentiment' | 'Valuation'`
   (required so tsc accepts the new group tags).
4. **Relabeled DIVZ** -- `PRESETS['divz'].label` `'DIVZ -- Dividend'` -> `'DIVZ'`. id / entries / universe
   untouched, so `activePresetId` matching and the DIVZ default-on-load seed are unaffected.

No edits to ScannerHeaderPanel.tsx / useScannerState.ts / SecurityScanner.tsx -- the registry entry
auto-adds the dropdown option; scoring is 100% client-side. FE-only, no backend/DS/Lambda/S3.

Diff: `src/pages/SecurityScanner/constants.ts | 57 insertions(+), 8 deletions(-)`. Portal branch: DEV.

## Hazards handled (PRD sec.4.1)

- **applyPreset silent-skip:** `useScannerState.applyPreset` (line 134) drops any preset code absent
  from `allFactors`. Traced the source: `allFactors` = `factorData.factors` from `useFactorMetadata()`
  (SecurityScanner.tsx:47/53/78), which fetches the served `factor_metadata.json`. Verified all 16 PFOE
  codes present in that exact served array (289 factors, asOf 20260521, MISSING = NONE) -> no code is
  dropped -> applied `totalWeight` will be 100. This is the decisive check, done against the artifact
  the page actually loads, not just the S3 file in the abstract.
- **Group-union compile:** extended `PresetGroup` in the same edit; tsc passes (below).

## Compiler Tools

| Phase | Tool + command | Result | Disposition |
|---|---|---|---|
| 1 (before write) | `Grep "PRESET_GROUP_ORDER\|PresetGroup" portal/src` | Only constants.ts:27/30/41 -- no external render consumer | Union extension safe; PRESET_GROUP_ORDER has no render consumer |
| 1 (before write) | `aws s3 cp .../security_scanner/latest/factor_metadata.json` + code-membership audit | 289 factors, asOf 20260521; 16/16 PFOE codes PRESENT, MISSING = NONE | AC2 data side confirmed; applyPreset drops none |
| 2 (before commit) | `bun run typecheck` (tsc -b --noEmit) | exit 0 (transcript below) | AC3 union coverage confirmed |
| 2 (before commit) | `bun run lint` (eslint .) | exit 0 (transcript below) | AC5 clean |
| 2 (before commit) | `comp-cache collisions` | 104/104 captured; 14 shared keys; **0 TYPE MISMATCH**; no SecurityScanner key | No new scanner query key; reuses DIVZ r1000 endpoint |
| 2 (before commit) | `comp-transform schema-check SecurityScanner` | "All rendered fields match their response types." | Clean; preset adds no rendered field |

Rail note: raw `Grep` used for the union-consumer scan (HUD nudged comp-dispatch, which is a gold-dispatch
DAG tool -- not a fit for a portal TS symbol grep); code-membership `aws s3 cp` is an operational served-artifact
read (not nudged). comp-cache + comp-transform are the mandated frontend rails and both ran clean.

### typecheck transcript
```
$ tsc -b --noEmit
TYPECHECK_EXIT=0
```

### lint transcript
```
$ eslint .
[baseline-browser-mapping] The data in this module is over two months old.  ... (benign data-freshness notice, not a lint error)
LINT_EXIT=0
```

## Acceptance criteria

- **AC1** PRESETS has exactly 2 entries, ids ['divz','pfoe']; divz.label === 'DIVZ'; pfoe.label === 'PFOE'. -- **PASS** (mechanically verified)
- **AC2** PFOE_PRESET 16 entries; Sum weight === 100; every code in served factor_metadata.json. -- **PASS** (sum=100.0; 16/16 present)
- **AC3** Each PFOE group in extended PresetGroup union; tsc passes. -- **PASS** (groups subset of union; tsc exit 0)
- **AC4** DEV smoke (select PFOE -> 16 factors, badge 100 green, grid re-ranks; DIVZ -> 13 factors, badge 100; default-on-load DIVZ). -- **DEFERRED to DE** (Phase-3 after-commit; /frontend-dev smoke is DE's per TO handback)
- **AC5** typecheck + lint exit 0; /frontend-dev smoke green (DE runs it). -- **typecheck/lint PASS**; smoke DE-owned

## Handoff + commit (DE review WAIVED by Andrew)

Update: DE review WAIVED by Andrew-direct (via CTO~C, relayed by COO~C 2026-07-10T211717Z):
*"it looks good to me, just bring on DT and get it deployed."* Per the revised GO I committed my
own green build instead of handing to DE.

**COMMIT: portal DEV `7db8f6b5`** (full `7db8f6b54a2784b0ed6fce27e315f08c324c9d05`), my author line,
1 file / 57 insertions / 8 deletions. LOCAL commit, NOT pushed (RD has no push permission) -- visible
in the shared portal repo on this host; DT's DEV->PROD promote handles the push.
- Committed via `.tools/safe-commit.sh` run from `cwd=portal` (so `show-toplevel` resolves to the portal
  submodule), scoped to `-- src/pages/SecurityScanner/constants.ts` ONLY. safe-commit surface-check OK
  (no critical surface). Verified via `git show --stat`: only constants.ts committed; the 3 POSN_CUSTOM
  Positioning files also dirty in the tree were NOT swept.
- Commit message authored via `-F <file>` (no shell-parsed body), ASCII-only.

Routed the DEV hash to 1.0.0_SA_CTO~C (fast arch-gate glance -- single-file spec-match confirm) AND
2.0.0_SA_COO~C (RAVC). Next stage: 0.3.0_DT_TradingOperations DEV->PROD promote (CTO~C spawning DT).
COO~C pre-cleared the weight-check gate (16/16 exact, sum 100%).

AC4 DEV smoke + /frontend-dev remain the post-commit verification stage (DT/CTO~C during promote glance).
TO stays `pending` -- not self-closed (arch-gate + DT promote + COO~C RAVC still open per the TO's do-not-self-close rule).
Non-blocking Yang-flag on `eps_stability` (vs analyst-name `eps_stable_est`) carried forward -- built per
Andrew's coverage rule, does not gate.
