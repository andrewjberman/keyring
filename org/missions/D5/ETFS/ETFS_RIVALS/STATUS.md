# ETFS_RIVALS (rivalfunds) -- FAST status

Seat `2.0.0_SA_COO~RV` (CLAUDE). Lease: FAST to 2026-10-02T17:08:53Z, surface `data/etfs/scripts/rivalfunds`
(`org/mcp/drive-mode.log` line 56). Goal (Andrew ~04:59Z): "i want mcp.opalinvest.dev/rivalfunds demoable Today".
Team: reviewer `3.0.0_SA_CVO~RV` (grades pins after the fact: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_FAST_GRADES_20261002.md`),
open calls `4.0.0_SA_CRO~RV` (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_RULINGS_20261002.md`: CALLs 1-9 ruled).
As of 2026-10-02T13:0xZ.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `rv-fast` at `/c/tmp/rv-fast` (drained to CLOUD at 93227704b7); apply tree removed 10:23Z (MSTR disk ask) -- re-add detached at CLOUD HEAD for the next apply |
| Deployed artifact pin | CLOUD **f122e4476b** in the five etfs-rivalfunds Lambdas (ledgers fast-a1, -r2 .. -r11 all CLOSED; latest @7af008a129) |
| Served page | `platinum/page/date=2026-10-02/index.html` (newest; the gateway serves it), batch fast-a1-publish-1002e 12:24Z: 13 of 13, 213 trades, AI 22/2 (re-graded, CALL 11), money-market trades counted not shown; the last served change before Andrew's 13:00Z read |
| AI run objects | `research_hypotheses` date=2026-10-01 run 20261002T062229Z-ai; date=2026-10-02 run 20261002T110438Z-ai (20/4, unchanged) + its re-grade -rg4 (grounding_check/4, 22/2) |
| Push state | LOCAL @04fb5c283c: origin CLOUD 1f2346734b (ls-remote 10:24Z); MSTR~Z asked to carry it (msg 07:43Z) |

## Live thread

State: LIVE END TO END on the A1 page. The served 2026-10-01 page is the Lambda's own publish: 12 of 13 funds current
(GQGU lagging by freshness), 39 ranking panels (12 read "Sectors not shown"), 13 buying trends (ETFT, GQGU, IDVZ, PCLG sector tables read "Sectors not shown": one rule with the ranking panels), 12 AI accounts (none for the benchmark SCHY; TSEL's
30-day account shown as grounding FAIL), the input census, the closed audit block with all 198 trades; 1.60 MB.

## Acceptance

| Cell | State | Evidence |
|---|---|---|
| pt-1, pg-1, rk-1, tb-1, ic-1, ai-1, ai-2 | LIVE; grades 8-11 PASS (G8-1, G8-2, G8-3, G10-1 closed; no P0/P1 open for 13:00Z @5488015d8f); residual P2s: CGIC's stored text narrates CMQXX and F5 ids remain in today's stored prose (both fixed for the next run); grade 2 FAIL (F1 P0) -> fixed; grade 3 PASS F1-F4; grade 4 PASS CALL 6 + futures; grade 5 PASS CALL 8; grade 6 PASS; grade 7 PASS @3e93998f8e (G6-1 closed; sector_source own/other_fund/mixed + null ratified by CRO~RV @87fb953c86) | `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_FAST_GRADES_20261002.md` |

## Write claims

None open. No served change before Andrew's 13:00Z read (CTO~Z msg 28450).

## Next proof

1. Andrew's read of the 10-02 page (1002e, grade 11 PASS); any finding is the next item.
2. The next rivalfunds Lambda deploy carries, beside the bronze-read grant (a policy change) and F5: round 5's universe.py,
   collector and G4 changes (drained 13:0xZ). Its pair measures them through the handlers.
3. F5 (P2): prompt a1-chain/4 (readings named by label, no source/name keys) BUILT @0839079a9c, 397 passed, drained @7dbe861883;
   proven only by the next AI run; its Lambda copy rides the next pair.
4. The publish-page Lambda's missing bronze read: grant BUILT on rv-fast @fd0d285da3 (publish-page GET on the issuer-site and
   Bloomberg bronze holdings; policy JSON regenerated); its own pair (a plan with a policy change) after the demo.

## Round 5 drains (DONE 13:0xZ)

Morning read 2026-10-02, all three legs OK: (1) issuer fetch marker `fetch_holdings/date=2026-10-02/096abf8e..` OK (2026-10-01 +
GQGU); (2) vehicle log `bbg_tplus1_20261002_070002.log`: Bloomberg leg 90 (whole), enrichment 94 (landed G3 160 / G4 32 rows);
(3) the 13:00Z sweep (RequestId de6abfaa.., 8.5 s): its graph for 2026-10-02 read with stub runners over an overlay sink is
complete -- ran [], waiting [], unresolved {} -- and the served page stayed fast-a1-publish-1002e.
Drained: `wk-rivals5-2` (m-2 collector dedup, l-1 v0.8 Bloomberg leg inert) @e4e9eedfa9; `wk-rivals5-5` (s-6 G4 as-of guard)
@213540f408, the surprise-channel conflict resolved as the union of disjoint appended rows (133 = 129 + 126 - 122; JSON parses).
rivalfunds suite on combined CLOUD 213540f408: 410 passed, 2 skipped. The vehicle runs this code from the CLOUD tree at the
next trading morning (07:00 ET 2026-10-05). The two worktrees stay: each holds an untracked `.scratch/`, so removal needs
`--force` (a recursive delete, human-confirmed).

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
