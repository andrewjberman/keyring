# ETFS_RIVALS (rivalfunds) -- FAST status

Seat `2.0.0_SA_COO~RV` (CLAUDE). Lease: FAST to 2026-10-02T17:08:53Z, surface `data/etfs/scripts/rivalfunds`
(`org/mcp/drive-mode.log` line 56). Goal (Andrew ~04:59Z): "i want mcp.opalinvest.dev/rivalfunds demoable Today".
Team: reviewer `3.0.0_SA_CVO~RV` (grades pins after the fact: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_FAST_GRADES_20261002.md`),
open calls `4.0.0_SA_CRO~RV` (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_RULINGS_20261002.md`: CALLs 1-9 ruled).
As of 2026-10-02T09:4xZ.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `rv-fast` at `/c/tmp/rv-fast` (drained to CLOUD at c2b9023fc6); apply tree `/c/tmp/rv-apply` (detached) |
| Deployed artifact pin | CLOUD **c2b9023fc6** in the five etfs-rivalfunds Lambdas (ledgers fast-a1, -r2 .. -r6 all CLOSED; latest @0905b21b49) |
| Served page | `platinum/page/date=2026-10-01/index.html`, publish_page/3, batch fast-a1-publish-1001f (rebuilt with refresh_a1) |
| AI run objects | `research_hypotheses` date=2026-10-01 run 20261002T062229Z-ai (seat-adhoc, 23 PASS / 1 FAIL) |
| Push state | LOCAL: origin CLOUD 1f2346734b (ls-remote 08:47Z); MSTR~Z asked to carry it (msg 07:43Z) |

## Live thread

State: LIVE END TO END on the A1 page. The served 2026-10-01 page is the Lambda's own publish: 12 of 13 funds current
(GQGU lagging by freshness), 39 ranking panels, 13 buying trends, 12 AI accounts (none for the benchmark SCHY; TSEL's
30-day account shown as grounding FAIL), the input census, the closed audit block with all 198 trades; 1.60 MB.

## Acceptance

| Cell | State | Evidence |
|---|---|---|
| pt-1, pg-1, rk-1, tb-1, ic-1, ai-1, ai-2 | LIVE; grade 2 FAIL (F1 P0) -> fixed; grade 3 PASS F1-F4; grade 4 PASS CALL 6 + futures; grade 5 PASS CALL 8; trend futures out + cross-fund GICS + missing_reason live at c2b9023fc6, graded next | `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_FAST_GRADES_20261002.md` |

## Write claims

None open.

## Next proof

1. **Page day 2026-10-02.** The 07:00 ET (11:00Z) fetch lands the 2026-10-01 reports; the chain publishes the 10-02 page
   with the three producer tables. Then the seat AI run for 10-02 (CALL 5; prompt a1-chain/2 from rv-fast) and ONE
   republish via `daily-lambda {"only": ["publish-page"]}` (never-widen key K7), read back on the moved fields (CTO
   condition 3: the 10-02 headline count, the three A1 components, the reason on any REFUSED new window).
2. Drain the held round-5 vehicle chains after the morning read (below).
3. Drain rv-fast (prompt a1-chain/2) in a gap of the shared index.

## Held from round 5 (vehicle-run drains, SERVED; unchanged by FAST)

`wk-rivals5-2` (m-2, l-1 @86ddb6cec0) and `wk-rivals5-5` (s-6 @ca98d691f8) drain after the morning read, in order: the
07:00 ET issuer fetch markers, the 08:03 vehicle exit lines, then the 09:00 sweep.

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| Lambda wiring of the AI chain + a dedicated OpenAI secret (round 6, CALL 5 rule 3) | `2.0.0_SA_COO~RV` | the FAST lease ends (cut round 6 from this list) |
| Per-fund issuer floors with the 2-line tolerance (CALL 2) | `2.0.0_SA_COO~RV` + `1.0.0_SA_CTO~Z` pair | first round after FAST |
| G4 carries no price field (row Z-S14); rankings run on holding-implied prices | round-6 G4 history cell | px_close lands |
| PCLG / WCMG +1 historical windows stay INFERRED (round-4 t-5) until a control replay reads them | `2.0.0_SA_COO~RV` | a G5/G6 history replay is cut |
| buying_trend rows carry `sector_source` own / other_fund (CRO~RV CALL 9 condition) | `2.0.0_SA_COO~RV` | after the demo (a column + a deploy) |
| A served-delta instrument that runs each A1 stage's handler_entry on an overlay (the r5 miss) | `2.0.0_SA_COO~RV` | before the next A1 deploy |
| The census lists every missing G4 price and GICS line (766 each): honest, long | `2.0.0_SA_COO~RV` | after the demo |
| The concentration cell (ACWI top-10 share) | `2.0.0_SA_COO~RV` | ACWI lands daily (v0.8 leg) |

## Limits

No product ID is PASS until `3.0.0_SA_CVO~RV` grades the served artifact. The AI accounts are a seat ad-hoc QA-class
read (CALL 5 rule 4); FWD-16/17 grade EXERCISED only on the scheduled round-6 run.
