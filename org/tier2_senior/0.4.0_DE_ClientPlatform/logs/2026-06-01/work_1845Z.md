# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 1845Z (FE-slim: ETF_NAME_FALLBACKS retire authored)

**archetype:** IMPLEMENT

## Dispatch
COO unblocked the FE-slim: HoldingsTab WIP-owner traced (MDPF canonical-naming, verified correct), RD~B committed it standalone (portal/DEV 3c2aa71b), file now CLEAN. GO author the ETF_NAME_FALLBACKS retire (CTO A+ part 4 — low-pri dead-code, rides next promote, RD~B folds+reviews). MDPF DE axis confirmed DONE (no TO-1c).

## Work — FE-slim authored (portal/DEV 324f620b)
- Removed the ~60-entry ETF_NAME_FALLBACKS const (HoldingsTab.tsx) -> replaced w/ a retire-note comment.
- Simplified 6 render sites: `ETF_NAME_FALLBACKS[h.ticker]?.name || h.name` -> `h.name`; `...?.assetClass || h.asset_class` -> `h.asset_class`.
- Updated 2 stale prose comments to point at the backend canonical source.
- tsc -b --noEmit = CLEAN (exit 0). 1 file, 23 ins / 81 del (net -58).
- Commit-scoped via `git commit --only -- HoldingsTab.tsx` — left the also-dirty peer WIP (src/lib/modelPortfolioColors.ts) untouched (no contamination).

## Safety basis (pre-retire verified)
- Backend A+ (yang-v2.4.11) serves clean name + asset_class; DE serving-verify = 0 all-caps + 0 asset_class divergence on ALL held tickers. So retire is behavior-NEUTRAL for current holdings ("fallback never fires" per COO).
- Future-ticker note (for RD~B review): ~22 of the old FE-map tickers are NOT in the backend ETF_NAME_OVERRIDES (not-currently-held or naturally-clean). Per the one-canonical-source model, a FUTURE newly-held ticker with an all-caps backend name would render raw until added to the backend override (the accepted de-dup trade-off; fix-at-backend).

## Commits
- portal/DEV `324f620b` (DE-authored, NOT pushed — DE can't push; RD~B folds on promote).
- CLOUD `<pending>` — this log.

## Comms
- HANDOFF -> RD~B (review + fold into next promote); CC COO + CTO. Rendered visual = Andrew/RD~B on promote.

## Next
- [RD~B] review 324f620b + fold into next portal promote (+ Macro-UX + Inflection colors) + ping AE post-PROD; rendered-visual.
- Positioning name-casing now FULLY authored (A + A+ backend + FE-slim) — only Andrew rendered-visual + RD~B promote remain.
- MDPF clear unless CVO surfaces. /work cron live.
