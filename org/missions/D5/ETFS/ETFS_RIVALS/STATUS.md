# ETFS_RIVALS (rivalfunds) -- FAST status

Seat `2.0.0_SA_COO~RV` (CLAUDE). Lease: FAST to 2026-10-02T17:08:53Z, surface `data/etfs/scripts/rivalfunds`
(`org/mcp/drive-mode.log` line 56). Goal (Andrew ~04:59Z): "i want mcp.opalinvest.dev/rivalfunds demoable Today".
Team: reviewer `3.0.0_SA_CVO~RV` (grades pins after the fact: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_FAST_GRADES_20261002.md`),
open calls `4.0.0_SA_CRO~RV` (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_RULINGS_20261002.md`: CALLs 1-9 ruled).
As of 2026-10-02T12:1xZ.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `rv-fast` at `/c/tmp/rv-fast` (drained to CLOUD at 93227704b7); apply tree removed 10:23Z (MSTR disk ask) -- re-add detached at CLOUD HEAD for the next apply |
| Deployed artifact pin | CLOUD **2d511b9058** in the five etfs-rivalfunds Lambdas (ledgers fast-a1, -r2 .. -r10 all CLOSED; latest @897b17b83b) |
| Served page | `platinum/page/date=2026-10-02/index.html` (newest; the gateway serves it), batch fast-a1-publish-1002d 12:09Z: 13 of 13, 236 trades, AI 22/2 (re-graded, CALL 11); grade 10 PASS |
| AI run objects | `research_hypotheses` date=2026-10-01 run 20261002T062229Z-ai; date=2026-10-02 run 20261002T110438Z-ai (20/4, unchanged) + its re-grade -rg4 (grounding_check/4, 22/2) |
| Push state | LOCAL @04fb5c283c: origin CLOUD 1f2346734b (ls-remote 10:24Z); MSTR~Z asked to carry it (msg 07:43Z) |

## Live thread

State: LIVE END TO END on the A1 page. The served 2026-10-01 page is the Lambda's own publish: 12 of 13 funds current
(GQGU lagging by freshness), 39 ranking panels (12 read "Sectors not shown"), 13 buying trends (ETFT, GQGU, IDVZ, PCLG sector tables read "Sectors not shown": one rule with the ranking panels), 12 AI accounts (none for the benchmark SCHY; TSEL's
30-day account shown as grounding FAIL), the input census, the closed audit block with all 198 trades; 1.60 MB.

## Acceptance

| Cell | State | Evidence |
|---|---|---|
| pt-1, pg-1, rk-1, tb-1, ic-1, ai-1, ai-2 | LIVE; grades 8-10 PASS (G8-1 closed @33f6db4880, G8-2 closed @c3050c9b94; G8-3 + G10-1 = addendum 10; F5 source ids P2 open); grade 2 FAIL (F1 P0) -> fixed; grade 3 PASS F1-F4; grade 4 PASS CALL 6 + futures; grade 5 PASS CALL 8; grade 6 PASS; grade 7 PASS @3e93998f8e (G6-1 closed; sector_source own/other_fund/mixed + null ratified by CRO~RV @87fb953c86) | `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_FAST_GRADES_20261002.md` |

## Write claims

- Addendum 10 (G8-3 money-market trades off the trade log + AI facts; CALL 12 notional condition, G10-1): code @3a937fbbe3,
  drained f122e4476b; plan 0/5/0 `/c/tmp/rv_apply11.tfplan` from `/c/tmp/rv-fast` (HEAD = f122e4476b; do not commit there until
  applied); COO half @39b59393a8; CTO~Z half asked 12:17Z. Then ledger r11 && apply outside 12:50-13:15Z, republish 1002e.

## Next proof

1. Addendum 10 applied and republished (1002e); CVO grade 11.
2. Drain the held round-5 vehicle chains after the 13:00Z sweep (below).
3. F5 (P2): 106 `fear_greed/...` source ids in AI prose -- prompt a1-chain/4 naming readings by label; proven only by the next AI run.
4. The publish-page Lambda's missing bronze read (parked below) as its own addendum with a policy change.

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
| The publish-page Lambda has no GetObject on `issuer-site/etfs/bronze/holdings/*` and `bloomberg/etfs/bronze/holdings/*` (the daily Lambda has it): marker-driven pages show "source URL unavailable (bronze sidecar unreadable)" x108 until the 09:00 ET sweep republishes through the daily Lambda | `2.0.0_SA_COO~RV` | its own addendum (a plan with a policy change), after the demo |
| The census lists every missing G4 price and GICS line (766 each): honest, long | `2.0.0_SA_COO~RV` | after the demo |
| The concentration cell (ACWI top-10 share) | `2.0.0_SA_COO~RV` | ACWI lands daily (v0.8 leg) |
| CTO~Z msg 28395 items 1-2 BUILT on rv-fast @688c4a7c59 (one `_sectors_hidden` function; `_e` prints NaN empty); overlay render of 10-01 byte-identical to served 1001g; drained to CLOUD @2bf0e85772; not deployed | `2.0.0_SA_COO~RV` | deploy rides the next pair after the demo |

## Limits

No product ID is PASS until `3.0.0_SA_CVO~RV` grades the served artifact. The AI accounts are a seat ad-hoc QA-class
read (CALL 5 rule 4); FWD-16/17 grade EXERCISED only on the scheduled round-6 run.
