# ETFS_RIVALS (rivalfunds) -- status (FULL since 14:40:14Z; was FAST)

Seat `2.0.0_SA_COO~RV` (CLAUDE). Lease: ENDED 14:40:14Z on Andrew's word ("yes you can move to /canonical-drive for the remainder";
relayed ~14:1xZ: "max parallelization on subagents"; record @ next commit); was FAST, surface `data/etfs/scripts/rivalfunds`
(`org/mcp/drive-mode.log` line 56). Goal (Andrew ~04:59Z): "i want mcp.opalinvest.dev/rivalfunds demoable Today".
Team: reviewer `3.0.0_SA_CVO~RV` (grades pins after the fact: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_FAST_GRADES_20261002.md`),
open calls `4.0.0_SA_CRO~RV` (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_RULINGS_20261002.md`: CALLs 1-9 ruled).
As of 2026-10-02T14:4xZ.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `rv-fast` at `/c/tmp/rv-fast` (drained to CLOUD at 93227704b7); apply tree removed 10:23Z (MSTR disk ask) -- re-add detached at CLOUD HEAD for the next apply |
| Deployed artifact pin | CLOUD **722f0db291** in the five etfs-rivalfunds Lambdas + the publish-page bronze-read grant (ledgers fast-a1, -r2 .. -r13 all CLOSED; latest @747a314b2d) |
| Served page | `platinum/page/date=2026-10-02/index.html` (newest; the gateway serves it), batch fast-a1-publish-1002f 14:17Z: 13 of 13, 213 trades, AI 22/2, PFOE's 26 trace cells name the home producer's file; 1,575,052 B |
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

None open. Andrew-direct 13:33Z "RECS APPROVED GO AHEAD" (@74e6e01a5b, CALL 2 corrected @a555e1301b): addendum 11 APPLIED (r12),
the round-5 worktrees removed, FAST lapses at 17:08:53Z (not extended).

## Next proof

1. **Round 6 ONE issuance NOW** (FULL, /dispatch): ap-1, rk-2, e-2 spawned at once (3 of 3 chains, cap 8); r-6 joins after
   ap-1 + rk-2; issuer acts I-1..I-3. Decomposition from the DRAFT + battery (14 checks, every one FAIL at base).
2. **RFW-D01/D02 on the demo page** (issuer act, parallel): `refresh_a1` republish of 2026-10-02 under a never-widen pair; the
   A1 tables predate the 11:11Z G1 refresh (header 13 of 13 vs census 2 of 13).
3. **The 33-finding walk register** (`docs/briefs/rivalfunds-ui-data-findings-20261002.json`) joins as cells when 1.0.0_SA_CTO~Z's
   PRD carries every id (Andrew); an amendment issuance adds them.
4. **2026-10-05:** the 07:00 ET marker page read ("source URL unavailable" 0 -- PFOE's now name their file); the 10-05 AI accounts.

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

## Round 6 rectangle (ONE issuance at FAST -> FULL)

DRAFT decomposition: `deliverables/2.0.0_SA_COO~RV/round6/ETFS_RIVALS_DECOMP.round6.DRAFT.md` (5 cells: ap-1, rk-2, e-2 on
three chains; px-1 and r-6 joins; issuer acts I-1..I-3). Cell 7's premise measured 14:2xZ: G4 carries px_close now (09-29
newer object 430/434, 10-01 32/32); the gap is HISTORY (rk-1 read one G4 date). Battery still to write and dry-run.

Cells 1-7 = `ledger/ROUND_ANALYSIS.round5.md` section 4 @56c99763bb, authoritative:
1. the AI chain as a production act (scheduled Lambda path + its dedicated secret; VEW-2);
2. the A1 plausibility guard on CRO~RV CALL 13's amended terms (@6e3c94774a: per fund x period; total < -100% hard, the
   planted -188% refuses; one holding |c| > 0.25 PROVISIONAL; NAV reconciliation where on file);
3. W4-S9's disarm by one deliberate run above 45 dates;
4. the backfills (IDVZ, PFOE, ACWI, IWM) and the G5/G6 replay under its own pair;
5. W3-S11 and W3-S12 (a probe first);
6. ~~PFOE's 26 home-producer lines without a source URL~~ -- DONE under FAST: addendum 12, r13 CLOSED @747a314b2d (CTO~Z: round 6 drops
   cell 6);
7. the S14 G4 price cell.
L5 rule for the round: CALL 13 C2 (every judgment criterion names its positive control).
Remediations, batched into ONE repair cell: the AI placeholder "No AI account. the ..." capital; trending-topic headline digits
read as figures; the census's 766-line length; the AI prose's Bloomberg ticker forms (CALL 10: style for the next prompt).
Carried, not cells: CALL 2 issuer floors (deferred post-FAST, CTO~Z pair); the ACWI concentration cell (ACWI lands daily);
CGIC's stored 10-02 CMQXX narration and F5's stored ids (fixed for future runs; never re-rolled).

## Limits

No product ID is PASS until `3.0.0_SA_CVO~RV` grades the served artifact. The AI accounts are a seat ad-hoc QA-class
read (CALL 5 rule 4); FWD-16/17 grade EXERCISED only on the scheduled round-6 run.
