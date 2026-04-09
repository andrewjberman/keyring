# MKOV_TRENDS.005 — Bullet Summaries + Article Lead Images
**Date:** 2026-04-08
**Agent:** 0.1.1_RD_MarketPerformance
**Task Order:** MKOV_TRENDS.005.rd-portal-rendering.md

## Changes

### 1. Bullet List Rendering (ContextBullets component)
- Added `ContextBullets` function component in ExecutiveSummary.tsx
- Splits `context` on newlines, strips `- ` or `* ` prefix from each line
- Renders as `<ul>` with `list-disc` when 2+ bullets detected
- Falls back to `<p>` with `line-clamp-2` for single-line contexts
- Applied in HeroTrendCard (hero topic #1) and DrilldownModal header

### 2. Article Lead Image (TopicLeadImage component)
- Added `TopicLeadImage` function component replacing `TrendingTopicImage` SVG icons
- Uses `topic.image_url` (populated by DS .003 via og:image extraction)
- Renders `<img>` with `object-cover` and `onError` fallback
- Fallback: colored initial avatar with green/red gradient (PALETTE.green700 / PALETTE.red600)
- Removed `TrendingTopicImage` import (no longer used in ExecutiveSummary)

### 3. Hero Headline Truncation (verified)
- `truncate` class already on `<h3>` at line 875 — confirmed working

## Files Changed
- `portal/src/components/market-performance/ExecutiveSummary.tsx` (+75/-13)

## Commits
- `8a354a1` feat(MarketOverview): bullet summaries + article lead images in trending
- `adf00e8` fix(MarketOverview): use native list-disc bullets, keep white text

## Scope Note
Changes are in shared component `ExecutiveSummary.tsx` (outside normal page directory boundary).
COO task order MKOV_TRENDS.005 directly assigned this work to 0.1.1_RD.
