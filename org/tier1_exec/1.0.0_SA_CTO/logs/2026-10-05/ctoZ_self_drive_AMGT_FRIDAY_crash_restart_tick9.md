# /self-drive AMGT_FRIDAY -- tick 9 after the SentinelOne crash (1.0.0_SA_CTO~Z, 2026-10-05 ~02:2xZ -> ~03:2xZ)

**archetype:** COORDINATE

state: ARMED. Cadence 60m, cron `29c8b141`. Arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_194xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RESTART_AFTER_SENTINELONE_CRASH.md`
@2b18064b99. Previous log: tick 8 @bcdb188483.

## Andrew's words in the window (each recorded by the seat he typed at)

| word | where | what this seat did |
|---|---|---|
| "/rivalfunds drops MTD" (~02:4xZ, @575e7d7250) | COO~RV | **ETFS_RIVALS PRD v0.15** @e99a733d4c: last 30 trading days (default), a divider, then QTD and YTD; FWD-14 ranks three periods |
| `/open-calls` before sleep (~02:5xZ) | this terminal | 5 cards: (1) overnight standing DEV-push permission; (2) overnight seat-relaunch permission; (3) Bloomberg rotation; (4) the portal PROD promote, tomorrow; (5) HARVST FWD-7 guidance, admit a publisher at 95% or more with uncovered names shown as not searched. **No answer was received before he went AFK**, so each stays carried and nothing assumes a yes. |
| "Dont attempt FT until I return ..." (~02:5xZ) | COO~H | matches the running state; ft stays stopped |
| "CTO~Z must adjudicate [ETFS_RIVALS open calls] for you" (~03:0xZ) | COO~RV | accepted. Card 29452 (WCMG history before 2026-04-23) RULED: accept and label it, with no issuer contact |
| benchmarks ACWI/IWM; every ticker clickable; ETFClassifier backfill (~03:3xZ) | COO~RV | item 1 = COO~RV r8 lg-1; item 2 = **PRD v0.16 NEW FWD-21** @646ce7f4b8; items 3-4 = MDPF_SECCLASS (laptop) placement, relayed via MSTR~Z |
| "cap on all lookback of 3 years" (@357e681ddf) | COO~RV | carried to the laptop relay. The ACWI/IWM backfill is ruled at a 1M-row cap, per date, stop on first failure, within the Bloomberg budget and the 3-year cap |

CVO~Z re-signed ETFS_RIVALS v0.16 @57c61f75ed: ADMITTED.

## Calls, rulings, analyses (since tick 8)

| item | act | commit |
|---|---|---|
| DSGN grading venue (COO~D msg 29399) | Grade rounds 34-36 on DEV `c66d08f3` now; the PROD promote is a separate act on Andrew's word (card 4) | -- |
| comp-surprise rows stuck ARMED (CVO msg 29407) | Ruled: they close by a CITING row and the reader changes (`adjudicates` moves ADJUDICATION-doc rows; remediation `disarms: [ids]`). The build is in flight (subagent, worktree `C:/tmp/ctoz-tools-fix`). | -- |
| RESAPP r68 slug (msg 29454) | **Round 68 CLOSED; FWD-39 and FWD-36 REALIZED.** Round 69 = the `/ledger` dedupe plus a redeploy. Z-S348 (the seating lint counts `withdrawn` as open, and reads the FIRST status tag) is in the same tool build. | f54b52325e |
| HARVST collection run | Running: sa, barrons (queued behind sa), bbg and wsj. ft is stopped on Andrew's word. | -- |

No design forks went to CRO~Z and no governance forks went to CVO~Z.

## Scope state (register read 03:18Z, denominator 5)

| project | status | dep_stage | in flight |
|---|---|---|---|
| AMGT_CORPUS | active | EXECUTING | r37: am-2 and am-5 wait on the 2026-10-05 13:00Z fire |
| AMGT_HARVST | active | EXECUTING | r46: the collection run in progress |
| AMGT_RESAPP | active | EXECUTING | r69 owed by COO~Z |
| DSGN_AMGTV1 | active | EXECUTING | grading r34-36 on DEV |
| ETFS_RIVALS | active | EXECUTING | r8 (A 5 + B 4), drain ~07:41 ET; v0.16 ADMITTED |

Open TOs, directive-wide: D5 138, D13 1. Sequence: 5 UNPLACED. Open deploys in scope: 0.

**Completion test: NOT DONE.** 0 of 5 complete; all 5 REACHABLE.

## Acts only Andrew can do (each cited)

1. The 5 carried cards above. Cards 1 and 2 only need answers if the overnight work hits them; card 3 is his account; card 4 is
   PROD; card 5 is guidance.
2. The DSGN and ETFS_RIVALS FWD-1 signed-in reads (his login).
3. The FT collection route, "until I return" (his hold, quoted).

## Compiler Tools

`directives-check.py --json`, `sequence-check.py --project` x5, `active-commitments.py`, `prd-signoff.py status`, a sparse
worktree plus a background subagent for the two tool fixes. Two shared-tree hazards were avoided by waiting: PRD edits were held
through MSTR~Z's merge window (02:56-03:04Z) rather than editing the tree mid-merge.
