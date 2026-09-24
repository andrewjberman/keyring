# DSGN_IRPTV1 -- status (FAST lease)

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` v0.5
@1cccbe6bc6. Reviewer `3.0.0_SA_CVO` (grades each landed pin after the fact). Mode: FAST under
`org/mcp/drive-mode.log` line 1 (Andrew-direct ~17:4xZ blast mode), lease to 2026-09-24T20:41:52Z. Build place:
Andrew-direct ~18:3xZ, `org/tier1_exec/2.0.0_SA_COO~D/deliverables/ANDREW_DIRECT_20260924_183xZ_5174_FROM_MAIN_PORTAL_CHECKOUT_WORK_ON_DEV.md`.
As of 2026-09-24T19:1xZ.

## Pins

| What | Value |
|---|---|
| Working tree | the main portal checkout `C:/Users/AndrewBerman/Desktop/ajb_workspace/portal`, branch DEV (no side worktree) |
| Portal pin | `a65a8db5` = origin DEV (ls-remote read after the push). Carries P's candidate 8 (`237bdfda`), S6 (`92d16efc`), the two Andrew-direct ~18:4xZ fixes (`a65a8db5`) |
| CI | DEV run on 92d16efc: success; the run on a65a8db5 started at push |
| Deployed | DEV CI deploys opalinvest.dev from DEV; PROD `a0690a03` untouched (gated) |
| Screen | `localhost:5174` served from the main checkout (`bun run dev --port 5174`, its `.env.local`), log `C:/tmp/portal-main.vite5174.log` |
| Workspace push state | CLOUD LOCAL |

## Live thread

State: NOT LIVE END TO END. Rounds 1-2 and the S6 fix are on DEV. The signed-in FWD-1 trace on Anna Thiessen's
Cottonwood account has not been walked; hop 6's `spread` is not served (backlog 11).

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| Round 1 (IV-t-1..4) | CVO graded, round CLOSED | `ledger/ROUND_ANALYSIS.round1.md` @c06e435786 |
| Round 2 (IV-e-1..6, 8) | ON DEV since a3f4c860; graded after the fact in FAST | portal a3f4c860 |
| IV-e-7 (FWD-11 sweep) | SUPERSEDED by the FAST lease, never spawned | its task order |
| S6 (black tiles, CUSIP as a name) | CANDIDATE @92d16efc, awaiting the CVO | row DSGN_IRPTV1-S8; `deliverables/2.0.0_SA_COO~D/s6.fast-run.png` |
| P candidate 8 (DirectoryPage wire type + fixtures) | LANDED on DEV @237bdfda (fast-forward) | P msg 100816 |
| Andrew ~18:4xZ: firm tab FIRM_BINDING; Holdings $10K rounding | CANDIDATE @a65a8db5, awaiting the CVO. Firm filter, directory rows: Global 4 -> 49financial 2 (NARROWS); before the fix Global 4 -> 0 (search disabled, re-POST `fir_c9fc...`) | `deliverables/2.0.0_SA_COO~D/ad184x.fast-run.{png,txt}`, `firm-filter.run.txt`, `firm-filter.{before,after}.png`, `firm-filter-driver.mjs` |

## Write claims

- S7: the legacy fe-s suites named in row DSGN_IRPTV1-S7 and the product files behind them (read-only until each is
  dispositioned; a legacy assertion is retired by ruling, never edited to pass).

## Next proof

S7: the 8 failures new since a3f4c860, each named as a regression (fixed, with the suite re-run) or a legacy assertion
that asks for the retired behaviour (routed for a ruling). Measured with `bun test src/pages/InvestorReporting` in the
main checkout, before and after.

## Next-list (in order)

1. S7 -- the 8 legacy fe-s failures new on DEV since a3f4c860 (row DSGN_IRPTV1-S7).
2. The drill breadcrumb prints the root node id (`N-CW-ROOT`); same class as S6 (row S8 notes).
3. IRPT portal candidates from `2.0.0_SA_COO~P` / `~M` / `~Y` as they arrive; this seat lands each on DEV.
4. FWD-11 sweep (the superseded IV-e-7's cell): states, reason codes ("OK [code not defined by the v1 contract]")
   and the classification gap off the Performance and Holdings bodies into footer disclosures.
5. PRD backlog 7-10: FWD-7 the Analysis stepper (consumes Y's upload-poll interface below), FWD-8 prospect as subject
   (waits on upload composition), FWD-9 one page-level Export, FWD-10 panel system + tab order.
6. PRD backlog 11: the `spread` member when P serves it.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| IRPT portal candidates | `2.0.0_SA_COO~P`, `~M`, `~Y` | one message: branch, tip, suites run | P 8 CONSUMED; rest AWAITED |
| Template upload POST answers RESOLVING; poll by re-POST (2-5 s) | `2.0.0_SA_COO~Y` | msg 100825, Y @bb1eb7f92b | PUBLISHED, live once P composes it |
| `spread` served | `2.0.0_SA_COO~P` | performance contract | AWAITED |
| A signed-in session for the FWD-1 trace | Andrew | 5174 | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| DEV CI does not run `bun test` (why S7 was invisible) | `1.0.0_SA_CTO` | a ruling to add the unit suite to ci.yml |
| `.owned-paths.yaml` has no row for `org/missions/*/*/*/STATUS.md` (commits use the audited override) | `1.0.0_SA_CTO` | the row lands |
| Model Portfolios' own $10K grain (the 09-15 word vs today's "mistake") | Andrew | his word; `CategoryViewTree exactAmounts` is the switch |
| Leftover folders `C:/tmp/dsgn-irptv1-fast`, `C:/tmp/dsgn-irptv1-base` (deregistered worktrees, node_modules junctions inside) | Andrew | his OK for a recursive delete |

## Limits

Nothing in round 2 or S6 is CVO-graded. No live signed-in trace has run. The S6 real run used the stubbed-auth smoke
fixture, not served data. PROD promotion, deploys and vendor egress stay under their normal gates.
