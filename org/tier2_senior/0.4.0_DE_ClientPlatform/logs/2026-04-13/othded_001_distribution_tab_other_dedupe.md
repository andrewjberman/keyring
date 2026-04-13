# ADVI_OTHDED.001 — Distribution tab `other_{state}` dedupe

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-04-13 (ET)
**Commit:** portal DEV `801349d`
**Status:** code landed on DEV; `/frontend-dev` visual pass pending (see Outstanding).

## Summary

Extended `enforceTop9Other` in `portal/src/pages/AdvisorIntelligence/tabs/DistributionTab.tsx` to treat D_01-emitted `other_{state}` keys (e.g. `other_tx`, `other_ca`) as Other sentinels. Previously only plain `other` (case-insensitive) was recognized, so D_01's pre-rolled state tails entered the Top-9 AUA sort as regular cities while the genuine frontend tail got merged into a *second* "Other" slice — producing two Other entries on any state drill with >=10 cities (TX, CA, FL, and 25 others).

## Fix

Two edits to `DistributionTab.tsx`:

1. Sentinel regex extension on the normalization pass:
   ```ts
   const lower = s.key.toLowerCase()
   const isOther = lower === 'other' || /^other_[a-z0-9_]+$/.test(lower)
   ```
   Canonicalizes `other_{slug}` to `key='Other'` / `label='Other'` so every downstream equality check and color lookup collapses to a single row.

2. Multi-Other merge-reduce in place of the single `find(s => s.key === 'Other')`. After normalization multiple entries can legitimately map to `Other` (foldUnknownKeys already produced one AND D_01 emitted `other_{state}`). All numeric fields (excluding `rank`) are summed into a single `existingOther` before Top-9 enforcement.

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| 1 | `comp-transform schema-check DistributionTab` | pass — rendered field set unchanged; see compiler-tools-log entry |
| 1 | raw S3 inspect `s3://opal-data-bd/platinum/firm/partner_analytics_monthly.json` | confirmed 28 states emit `other_{state}`; TX = 10 cities, `other_tx` AUA $416,516,783.03 / 1,795 acct — matches TO |
| 1 | ADV `other_{architect}` probe | **not emitted** — jq `[.. | objects | select(.key? | tostring | test("^other_")) | .key] | unique` returned only state codes (al, ar, az, ca, co, fl, ga, ia, il, ks, la, md, mi, mn, mo, ms, nc, nj, ny, oh, ok, or, pa, sc, tn, tx, va, wa). ADV path unchanged by this fix. |
| 2 | `comp-blast DistributionTab.tsx` | pass — no new downstream impact |
| 2 | `tsc --noEmit` | clean |
| 2 | `eslint DistributionTab.tsx` | 0 errors, 10 warnings (all pre-existing `react-hooks/set-state-in-effect`, not from this change) |
| 3 | `/frontend-dev` visual-test | **outstanding** — see below |

## Acceptance criteria status

| # | Criterion | Status |
|---|-----------|--------|
| 1 | TX drill: 10 entries, single final `Other` with combined AUA | code-complete; visual pending |
| 2 | any other >=10-city state: same guarantee | code-complete; visual pending |
| 3 | ADV architect drill with `other_{architect}` | **N/A** — D_01 does not currently emit that pattern. Verified via S3 inspect. Fix is forward-compatible: if D_01 ever adds `other_{slug}` on ADV, the same sentinel catches it. |
| 4 | <=9-city state: at most 1 Other entry | covered by merge-reduce path |
| 5 | City percentages sum to 100% | no math changed; still derives from existing pct field |
| 6 | `/frontend-dev` pass recorded | **outstanding** |

## Outstanding

- `/frontend-dev` Playwright visual pass against the Distribution tab: drill TX, FL, CA (each >=10 cities); WCAG check. Will run when DT 0.4.0 bumps parent submodule pointer to include `801349d` (currently portal DEV is ahead of the parent's recorded submodule SHA). Separately: the parallel `ADVI_PROFIL.008` TO is the umbrella frontend-dev visual pass and can absorb this site.

## Do-not adherence

- No D_01 or gold-script edits. Frontend-only.
- Regex scoped to `^other_[a-z0-9_]+$` — no collateral matches.
- No types.ts or Lambda changes.
