# Iterative publication harvest loop — working strategy

Author: 4.0.0_SA_CRO~W
Date: 2026-09-14 US Eastern
Authority: ANDREW_DIRECT_20260914_HARVEST_ITERATIVE_LOOP_W.md
Status: ACTIVE LOCAL TESTING; target not yet measured.

## Required result

Fixed publisher order: SA → FT → WSJ → Bloomberg. One ticker across all four in a round; a different ticker in the following round. Continue with evidence-based strategy changes until each publisher delivers five distinct substantive complete articles for three consecutive different tickers. The implemented final gate conservatively requires the same final three rounds to pass across all four publishers.

## Local runner

`org/tier1_exec/4.0.0_SA_CRO/scripts/harvest_iterative_loop.py`

The Codex driver executes one round at a time, reviews results, writes notes, adjusts the next strategy and resumes the runner. A round is not counted merely because it was attempted. There is no cloud data write or scheduler. Chromium runs visibly through the installed Chrome channel. Existing Secrets Manager reads and, when selected, established proxy/Unlocker services remain remote dependencies.

```powershell
python org/tier1_exec/4.0.0_SA_CRO/scripts/harvest_iterative_loop.py --rounds 1 --candidates 14 --proxy --discovery-fallback
python org/tier1_exec/4.0.0_SA_CRO/scripts/harvest_iterative_loop.py --review-only
```

Default ticker sequence: BA, COST, HD, INTU, VLO, HAL, KMB; all selected from the checked-in 89-name universe. A candidate budget bounds each strategy attempt, not the overall research objective. A failed publisher still yields to the next publisher in the required order. The next round begins with SA again.

## Evidence and acceptance

Local root: `.runtime/codex-seats/4.0.0_SA_CRO~W/harvest-iteration/`.

Each round retains per-publisher HTML/screenshots or browser API responses, extracted article JSON, metadata, issues, and notes. Browser storage state stays in local `sessions/`; it is never committed. `state.json` records rounds and measured streaks; `review.json` binds a review to an exact body hash. Raw content stays local.

Structural screening requires a scoped article body, at least 120 words and three content blocks, title, publication time, a company mention, and no detected code/markup or access barrier. This is a conservative candidate filter, not a completeness oracle. The agent then reviews body boundaries, relevance, and page-shell/promotion contamination. Explicit complete/relevant reviews tied to the exact body hash are required before acceptance. Each publisher needs five unique canonical URLs and five distinct body hashes. An unreviewed body, changed hash, repeated body, or failed publisher cannot advance the corresponding success streak. The final window must contain three different tickers.

Brief SA news can be skipped by the conservative size filter even when complete. Generated reports do not count as articles. SA news and analysis remain distinguishable. Broad company mentions are not automatically primary-subject relevance; the first five accepted FT/HD articles all have Home Depot in the headline.

## Round log so far

| Round | Ticker | Strategy and learning |
|---|---|---|
| 1 | BA | Native browser with parked sessions. SA challenge; FT substantial bodies but outer promotions; WSJ naive links included navigation; Bloomberg article pages challenged. No accepted set. |
| 2 | COST | Corrected mouse release, narrower FT body, ticker-state WSJ discovery. SA article navigation still challenged; FT four candidates from five links; WSJ state absent; Bloomberg challenged. No five-article set. |
| 3 | HD | SA in-browser news API returned 403; FT search supplementation produced five reviewed directly relevant articles; WSJ hydration retries still absent; Bloomberg challenged. FT streak 1. |
| 4 | INTU | Active: existing residential proxy in SA/Bloomberg headful contexts; WSJ legacy client may supply discovery URLs, with article pages still fetched in the local browser. |

## Shared challenge-handler defect and live observation

The checkmark branch in `press_and_hold_lib.py` set `is_pressed=False` before exiting without actually releasing the mouse. Added the missing `page.mouse.up()`; an offline regression test verifies exactly one release. This fixes an input-state defect, not the challenge oracle: live central-pixel spikes still occurred without access resolving.

Andrew's live observation, verbatim:

> im seeing the trick on this seeking alpha case where you have to let it go when it starts draining and then re press, keep that in your notes

Operational rule retained: release briefly when fill starts draining, then re-press. The final release follows the real checkmark. The existing handler's drain threshold and false-positive center-pixel signal require further validation; its own signal log never counts as successful access.

## Validation and remaining work

Six offline regression tests pass: mouse release, three distinct passing tickers, missing review, stale body hash, duplicate body, and repeated ticker. Live rounds are the acceptance evidence; unit tests cannot establish publisher access or complete content.

Still working toward SA/WSJ/Bloomberg clean five-article sets, FT's next two consecutive tickers, robust interruption/resume behavior, and stronger challenge discrimination. The WSJ brief has no subscriber login; an optional question about an existing authorized account/session remains pending while independent work continues.
