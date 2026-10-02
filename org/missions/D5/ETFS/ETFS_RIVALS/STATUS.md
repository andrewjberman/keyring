# ETFS_RIVALS (rivalfunds) -- FAST status

Seat `2.0.0_SA_COO~RV` (CLAUDE). Lease: FAST to 2026-10-02T17:08:53Z, surface `data/etfs/scripts/rivalfunds`
(`org/mcp/drive-mode.log` line 56). Goal (Andrew ~04:59Z): "i want mcp.opalinvest.dev/rivalfunds demoable Today".
Team: reviewer `3.0.0_SA_CVO~RV` (grades pins after the fact), open calls `4.0.0_SA_CRO~RV`
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_RULINGS_20261002.md`: CALLs 1-5 ruled).
As of 2026-10-02T06:5xZ.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `rv-fast` at `/c/tmp/rv-fast` (full checkout) |
| Workspace candidate pin | CLOUD **7aa0186d45** (drain of rv-fast: all seven A1 cells + wiring) |
| Deployed artifact pin | d-5 addendum 1 (CLOUD 25f4ac5418); the A1 deploy is PLANNED (0 add / 7 in place / 0 destroy) |
| AI run objects | `research_hypotheses` date=2026-10-01 run 20261002T062229Z-ai (seat-adhoc, 23 PASS / 1 FAIL) -- in S3 |
| Push state | LOCAL (pushing is the integrator's act) |

## Live thread

State: LIVE END TO END on the round-4 page (2026-10-01, `publish_page/2`). The A1 page is proven over served inputs
in an overlay (S3 reads, local writes): `C:/tmp/rfpage/live_1001.html`, 1.61 MB, 13 fund statuses and 198 trades equal
to served, + 39 ranking panels, 13 buying trends, 12 AI accounts.

## Acceptance (CVO grades after the fact; AC checks in round5/checks/)

| Cell | State | Evidence |
|---|---|---|
| pt-1 theme | CANDIDATE @fe5c417d52 | pt-1.AC1 PASS |
| pg-1 page | CANDIDATE @6f3c3066bb | pg-1.AC1, AC2 PASS |
| rk-1 contribution | CANDIDATE @24363c9fe8 | rk-1.AC1 PASS (fixture day amended per CALL 3) |
| tb-1 trend | CANDIDATE @5d9d7bf96e | tb-1.AC1 PASS (bet vs gross per CALL 4) |
| ic-1 census | CANDIDATE @5d9d7bf96e | ic-1.AC1, AC2 PASS (AC2 clause amended per row Z-S14) |
| ai-1 readings | CANDIDATE @adc2097557 | ai-1.AC1, AC2 PASS (live, read-only) |
| ai-2 accounts | CANDIDATE @20525cac7c + b60e1eba81 | ai-2.AC1, AC2, AC3 PASS; live run 23/24 grounded |

## Write claims

None open in the package. Next act: the deploy (below).

## Next proof

1. **Deploy** (never-widen pair): COO half `round5/NEVER_WIDEN_HALF_COO_FAST_A1.md` @6bd16e078e SIGNED; CTO~Z signs
   on the filled G1/G5/G6 table (msg 28260). Then NEVER-2 ledger `etfs-rivalfunds-fast-a1`, `safe-apply` (plan
   0/7/0), CodeSha256 + policy read-back, republish 2026-10-01 via `daily-lambda {"only": ["publish-page"]}`, served
   page read and screenshot. Window: before 10:45Z (the 07:00 ET fetch), else after the 09:00 ET sweep.
2. **Page day 2026-10-02**: after the 07:00 ET fetch lands the 10-01 reports, the seat AI run for 10-02 (CALL 5),
   then after the 09:00 ET sweep one republish (`only: publish-page`) so the accounts show.

## Held from round 5 (vehicle-run drains, SERVED; unchanged by FAST)

`wk-rivals5-2` (m-2, l-1 @86ddb6cec0) and `wk-rivals5-5` (s-6 @ca98d691f8) drain after the morning read, in order: the
07:00 ET issuer fetch markers, the 08:03 vehicle exit lines, then the 09:00 sweep.

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| Lambda wiring of the AI chain + a dedicated OpenAI secret (round 6, CALL 5 rule 3) | `2.0.0_SA_COO~RV` | the FAST lease ends (cut round 6 from this list) |
| Per-fund issuer floors with the 2-line tolerance (CALL 2) | `2.0.0_SA_COO~RV` + `1.0.0_SA_CTO~Z` pair | first round after FAST |
| G4 carries no price field (row Z-S14); rankings run on holding-implied prices | round-6 G4 history cell | px_close lands |
| AI prompt polish: names over ids, percent formatting in observed lists | `2.0.0_SA_COO~RV` | after the demo |
| The concentration cell (ACWI top-10 share) | `2.0.0_SA_COO~RV` | ACWI lands daily (v0.8 leg) |

## Limits

Nothing here is graded until `3.0.0_SA_CVO~RV` grades the pinned candidate on the real run's artifact. The AI accounts
are a seat ad-hoc QA-class read (CALL 5 rule 4); FWD-16/17 grade EXERCISED only on the scheduled round-6 run.
