# Naming-Centralization Residual Chase-Down (all four) -- 1.0.0_SA_CTO~X

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, IMPLEMENT, DEPLOY

**Date:** 2026-08-18 (~1900-1945Z)
**Task Order:** ad-hoc, Andrew-direct: "We need to chase these down" (the four brief residuals)
**Status:** COMPLETE (residual 4 pending only the MSTR push landing; remote-verify armed)

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | content x3 (FE sector-label tolerance) | PASS | measured-zero hits proved no hardcoded sector keys in Positioning FE |
| comp-pulse (via safe-commit) | diff, per commit | PASS | clean on all commits |

**What worked:** importing both the lambda and _shared as MODULES for the dict census (no regex
transcription risk). **What failed:** my earlier tickerRegistry census regex under-counted entries
(54 vs true ~124, nested-brace blindness) -- caught by this window's strip count, correction recorded
in 8cbb2f86's message; conclusions unaffected (both strips ran file-wide). **Gap found:** none new.

---

## Work Completed

### R1 -- ICSH name RULED and applied everywhere
WebSearch against SEC/BlackRock ETF Trust filings: official name since 2020-12 is
'iShares Ultra Short Duration Bond Active ETF' -- BOTH estate variants were stale (pre-2020 name vs
issuer-brand confusion). Applied: DDB update-item; CANONICAL_SECURITIES; _shared comment + override.

### R2 -- classification through the registry (yang-pipeline-v1.5.8)
Census first (module-import, not regex): asset_class 100 inline entries, 0 disagreements vs registry;
management_style 71 entries, 0 disagreements; sector 20 + sub_asset 25 disagreements, all
inline-vocab drift off canon. Data prerequisites: 55 rows restored (mgmt/sector/sub stripped by the
old put_item; 114/116 now carry management_style, the 2 without have no _shared value and defaults
handle them); _shared 'other'->'hedge' x7 (reseed-regression path; registry + both lambdas operate on
'hedge'); 50-name protection sync + DIVZ/IDVZ Opal alignment -> registry<->_shared name parity TOTAL
(0 mismatches / 116). Code: registry_field() helper; 12 sites swapped incl. both membership-test
sites; four dicts deleted (259 lines); ETF_GEOGRAPHY_MAPPING deliberately kept (no registry field --
schema widening is a Rule-24 taxonomy act, surfaced not chased). Exercised: full local CLI run on the
real 20260817 PKLs + live registry, field-diffed vs served (CLI-vs-handler shape gap noted, not a
deploy delta). Deployed v1.5.8 (plan 1-change, 0-diff, recorded, tagged), regenerated via the
production event, served diff verified: 11 ICSH-name sites + 157 sector/sub-asset canonicalizations
(PFDE/PFOE 'Other'->'US Large Cap' -- genuine improvement) + ZERO active-flag changes + ZERO
weight/returns/characteristics touches. FE tolerance pre-verified (sector keys rendered generically;
PositioningSummary sub-categories already read canonical attribution data).

### R3 -- tickerRegistry description strip (portal DEV 8cbb2f86)
Same dead-and-wrong class as displayName; 124 entries stripped + interface field; tsc clean;
submodule bumped; rides the next promote (non-visual). Denominator correction recorded (see above).

### R4 -- integration requested from [0.0.0_AB_MSTR]
17 workspace CLOUD commits + tags yang-pipeline-v1.5.4..v1.5.8 (--follow-tags) + 1 portal DEV
commit; measured-ahead counts in the message; remote-verification is mine when the push lands.

### Brief updated
docs/briefs/security-naming-centralization-brief-20260818.md section 6 rewritten to CLOSED state.
The original artifact URL became unreachable because Andrew signed into a NEW account (his word,
mid-turn) -- republished under the current account:
https://claude.ai/code/artifact/cc82fc85-ee3b-4bdb-9170-bf8a66981e12 ; the repo copy stays canonical.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| ICSH = the official prospectus name | both estate variants provably stale; web-grounded |
| Repair registry DATA before the code swap | swapping onto rows with stripped attrs would regress behavior |
| Keep ETF_GEOGRAPHY_MAPPING inline | registry has no geography field; schema widening needs its own ruling |
| Ship the segment re-keying | inherent to Andrew's GO; FE key-generic (measured); rollback = prior artifact |
| Republish artifact under the new account | Andrew clarified mid-turn: account switch, not deletion |

## Current State (zero-context)
- Registry `etf-classifications`: 116 rows, 0 placeholder names, 114 with management_style, ICSH
  ruled; total name parity with `_shared` ETF_NAME_OVERRIDES (116 protected).
- `yang-generate-positioning` @ v1.5.8: names + all four classification axes registry-backed; only
  geography + beta-overrides + BENCHMARK_ETFS tickers remain inline (each with a reason).
- Served `positioning_data.json` regenerated 2026-08-18 ~1935Z on the production 20260817 input.
- Awaiting: MSTR pushes (workspace CLOUD + tags; portal DEV 8cbb2f86). Verify-from-remote armed.

## Next Steps
- [1.0.0_SA_CTO~X] verify MSTR pushes from the remote when they land (background watch armed).
- [ANDREW] one open taxonomy question, NOT executed: widen the registry schema with a geography
  field so ETF_GEOGRAPHY_MAPPING can follow the same path (Rule-24 act, needs your word).
