# DSGN_IRPTV1 -- status (FAST lease)

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` v0.5
@1cccbe6bc6. Reviewer `3.0.0_SA_CVO` (grades each landed pin after the fact). Mode: FAST under
`org/mcp/drive-mode.log` line 1 (Andrew-direct ~17:4xZ blast mode), lease to 2026-09-24T20:41:52Z.
As of 2026-09-24T17:58Z.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | portal `dsgn-irptv1-fast` at `C:/tmp/dsgn-irptv1-fast` (node_modules junction to the shared portal) |
| Workspace candidate pin | CLOUD (this file's commit) |
| Portal candidate pin | `5e339ffd` = origin/DEV (ls-remote read 17:52Z); no FAST item landed yet |
| Deployed artifact pin | DEV CI deploys opalinvest.dev from DEV; PROD `a0690a03` untouched (gated) |
| Push state | portal: nothing pushed by this seat this session. CLOUD: LOCAL |
| Screen | `localhost:5174` served from `C:/tmp/dsgn-irptv1-fast` (`bun run dev --port 5174`), log `C:/tmp/dsgn-irptv1-fast.vite5174.log` |

## Live thread

State: NOT LIVE END TO END. Rounds 1-2 (IV-t-1..4, IV-e-1..6, IV-e-8) are on DEV since a3f4c860. The signed-in
FWD-1 trace on Anna Thiessen's Cottonwood account has not been walked; hop 6's `spread` is not served (backlog 11).

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| Round 1 (IV-t-1..4) | CVO graded, round CLOSED | `ledger/ROUND_ANALYSIS.round1.md` @c06e435786 |
| Round 2 (IV-e-1..6, 8) | ON DEV, L8/L9 not run; graded after the fact in FAST | portal a3f4c860 |
| IV-e-7 (FWD-11 sweep) | SUPERSEDED by the FAST lease, never spawned | its task order, drive-mode.log line 1 |

## Write claims

- `portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTreemap.tsx` (S6: black tiles)
- the display-name resolver used by the Holdings components (S6: CUSIP printed as a name)

## Next proof

S6: on the smoke fixture `fixtures/smoke/dsgn-irptv1-cottonwood.json`, the Securities map draws coloured tiles
when no model/sleeve ancestor exists, and `037833100` prints nowhere as a name. Proved by one real run on 5174
(screenshot read) and the item's own test.

## Next-list (in order)

1. S6 -- black treemap tiles; CUSIP rendered as a security name (row DSGN_IRPTV1-S6).
2. S7 -- the 8 legacy fe-s failures new on DEV since a3f4c860: each a regression to fix or a legacy assertion
   retired by ruling, never edited to pass (row DSGN_IRPTV1-S7).
3. `2.0.0_SA_COO~P`'s IRPT portal candidates as they arrive, candidate 8 first; this seat lands each on DEV.
4. FWD-11 sweep (the superseded IV-e-7's cell): states, reason codes and the classification gap off the
   Performance and Holdings bodies into footer disclosures; Analysis measured only.
5. PRD backlog 7-10 in order: FWD-7 Analysis stepper, FWD-8 prospect as subject (waits on upload composition),
   FWD-9 one page-level Export, FWD-10 panel system + tab order.
6. PRD backlog 11: the `spread` member when P serves it.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| IRPT portal candidates | `2.0.0_SA_COO~P`, `~M`, `~Y` | one message: branch, tip, suites run | AWAITED |
| `spread` served | `2.0.0_SA_COO~P` | performance contract | AWAITED |
| A signed-in session for the FWD-1 trace | Andrew | 5174 or opalinvest.dev | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| DEV CI does not run `bun test` (S7's cause of invisibility) | `1.0.0_SA_CTO` | a ruling to add the unit suite to ci.yml |
| Round-2 drain packet to the CVO (crash brief row 6) | `2.0.0_SA_COO~D` | superseded by FAST grading; revisit at FAST -> FULL |

## Limits

Nothing in round 2 is CVO-graded. No live signed-in trace has run. PROD promotion, deploys and vendor egress stay
under their normal gates. A FAST lease never lowers a `<risk>` class.
