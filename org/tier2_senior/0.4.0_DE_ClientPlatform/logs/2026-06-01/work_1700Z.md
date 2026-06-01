# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 1700Z (Positioning VUG — CTO GO'd, verified, handed AE)

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, COORDINATE

## Dispatch
CTO RULING (165454Z): GO Option A NOW (add 'VUG':'Vanguard Growth ETF' to backend ETF_NAME_OVERRIDES, yang-generate-positioning) — DE authors diff -> 0.7.0_AE_CloudOps deploys. A+ (sweep 28 + retire FE map) follow-on, gated on a canonical name source.

## Pre-handoff verification (caught + resolved a would-be-wrong-fix risk)
Before handing AE, found the serving artifact has TWO holdings sections + the override is path-specific — had to confirm the FE-read path actually applies the override:
- `portfolios/{model}/holdings` = NO override (all all-caps). `current_holdings/{model}/holdings` = override APPLIED (PFDE/DIVZ clean).
- FE Holdings tab (Current) reads `current_holdings` (HoldingsTab.tsx:592) -> applies override -> **adding VUG to dict FIXES the FE Current view.** (VUG carries attribution cols matching CTO ref row.)
- QTD/YTD/1Y/SI view reads a SEPARATE Lambda (yang-generate-holdings-attribution -> holdings_attribution_data.json) which ALREADY shows VUG = "Vanguard Growth ETF". So defect is ISOLATED to Current view, and the proper name is CONFIRMED by a live artifact (not guessed). That attribution source = the canonical clean-name source A+ needs.

## Action
- Authored exact Option A diff (1 line in ETF_NAME_OVERRIDES). Brief updated w/ verified resolution + diff + A+ source: docs/briefs/positioning-security-name-casing-trace-20260601.md.
- Handed AE (0.7.0_AE_CloudOps) the diff + deploy steps (terraform via safe-apply, re-run positioning rollup, CF-invalidate, post-deploy verify); CC CTO + COO.
- DE cannot edit/deploy infra/aws/ -> AE applies. Visual smoke = Andrew post-deploy.

## Commits
- CLOUD `<pending>` — brief update + this log

## Comms
- HANDOFF -> 0.7.0_AE_CloudOps (CC 1.0.0_SA_CTO + 2.0.0_SA_COO): Option A diff + deploy + verify.

## Next
- [AE] apply Option A diff in yang-generate-positioning + deploy + rollup + CF-invalidate; ping me + I confirm serving current_holdings VUG = clean.
- [me] verify post-deploy serving; flag Andrew for visual. A+ scope w/ AE (canonical source = attribution Lambda).
- Held: DS~B Schwab continuity re-verify; RD~B SMA-fold (103f623a DEV) rendered-math verify. /work cron live.
