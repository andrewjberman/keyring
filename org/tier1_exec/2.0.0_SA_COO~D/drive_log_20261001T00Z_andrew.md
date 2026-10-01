# Drive log -- 2.0.0_SA_COO~D, 2026-09-30 23:xxZ - 2026-10-01 00:2xZ (DSGN_IRPTV1: FAST item 49, two Andrew-direct reports)

Substantive ticks only; NO-OP ticks sit in the gitignored runtime file `org/mcp/drive_ticks/2.0.0_SA_COO~D.md`.
Host `andrew` (laptop). Loop: cron d49f1666 (LIVE_ARMS DIRECTED row, `/canonical-drive 10m`).

| Tick (UTC) | Limb | Act |
|---|---|---|
| 23:xxZ | Andrew-direct | Two reports at this terminal: (1) localhost:5174 "Failed to fetch dynamically imported module .../src/pages/MarketPerformance/index.ts"; (2) Investor Reporting: "the predictive text search isnt working. Is something rolling back this function somehow?" |
| 23:xxZ-00:0xZ | FAST item 49 | Search: no rollback (22cccf87 in DEV, header/search.ts unchanged since). Cause: the tiers ran only when an answer landed, against that answer's query; rows held while the next answer is in flight kept their old order. `ClientSearch.tsx` ranks the held rows in a memo keyed on the live query. iv-e-122 + iv-e-47 wiring re-goldened; tsc -b 0, eslint 0 errors, both from the portal root after the last edit; real run on 5174 with the typed answer held 20 s: fixed component lists the typed name first, HEAD component (negative control) lists it last; screenshot read. Portal `970d5c75`; lease read in its own call (FAST until 00:28Z), then pushed; ls-remote DEV = 970d5c75. Not verified: Andrew's exact spelling against the live directory |
| 00:0xZ-00:1xZ | 5174 | Market Performance: all 76 /src modules 200; a fresh headless load reproduced the error -- 504 on /.vite/deps/@visx_text.js and @visx_wordcloud.js; portal/.vite/deps absent under the running server (pid 27592, up since 09:33 local), 34 deps_temp_* directories beside it. Restarted 5174 (pid 18500); cache rebuilt; two fresh loads render "Market Overview", 0 module failures. Row DSGN_IRPTV1-S42 (cause of the removal not identified; temp directories left in place) |
