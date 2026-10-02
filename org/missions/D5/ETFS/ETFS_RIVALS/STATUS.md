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
   collector and G4 changes (drained 13:0xZ). Its pair measures them through the handlers. Pre-measured 13:1xZ: an overlay
   publish of 2026-10-02 at CLOUD 213540f408 differs from the served 1002e in ONE line, the G0 map date (10-01 -> 10-02: a
   newer map object, data any republish reads); page code delta 0. Still to measure: the A1 tables (served_delta_a1.py).
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

## Round-6 cut list (FAST -> FULL at 17:08:53Z; cut straight from here, thread-first, repairs batched)

| # | Cell | Risk | Grounding | Gate |
|---|---|---|---|---|
| 1 | The next Lambda pair if FAST does not land it: publish-page bronze-read grant (policy) + F5 prompt a1-chain/4 + round 5's universe/collector/G4 code | WORLD | grant @fd0d285da3, F5 @0839079a9c, drains e4e9eedfa9 / 213540f408; overlay page delta = G0 map date only | Andrew's word that served changes resume (next-calls CALL 1) |
| 2 | The 2026-10-05 seat AI run (one run, CALL 5 terms), then one republish: the only proof of F5 and of G8-3's fact-pack change | WORLD | CTO~Z msg 28437 (next AI run free); `org/ref/VENDOR_EGRESS_WHITELIST.yaml` @213102cff1 lists no OpenAI word | Andrew's per-use word (next-calls CALL 2) |
| 3 | AI chain wired into the Lambda + a dedicated OpenAI secret (CALL 5 rule 3): the scheduled run replaces the seat run | WORLD | parked since 2026-10-02 06:xxZ | a standing OpenAI word on the whitelist |
| 4 | Per-fund issuer floors with the 2-line tolerance (CALL 2) | SERVED | CRO~RV rulings CALL 2 | the CTO~Z pair |
| 5 | G4 carries a price field (row Z-S14), so rankings stop leaning on holding-implied prices (1849 implied / 1498 missing on 10-02) | SERVED | a1_produced detail, 2026-10-02 manifest | px_close lands in G4 |
| 6 | Repairs, ONE cell: PFOE home-producer "source URL unavailable" x26; the census's 766-line length; the AI placeholder "No AI account. the ..." capital; trending-topic headline digits read as figures; the AI prose's Bloomberg ticker forms (CALL 10: style for the next prompt) | LOCAL/SERVED | 2026-10-02 audit reads in this file | none |
| 7 | PCLG / WCMG +1 historical windows read by a control replay (round-4 t-5) | SERVED | INFERRED since round 4 | a G5/G6 history replay is cut |
| 8 | The concentration cell (ACWI top-10 share) | SERVED | v0.8 leg built inert (l-1) | ACWI lands daily |

## Limits

No product ID is PASS until `3.0.0_SA_CVO~RV` grades the served artifact. The AI accounts are a seat ad-hoc QA-class
read (CALL 5 rule 4); FWD-16/17 grade EXERCISED only on the scheduled round-6 run.
