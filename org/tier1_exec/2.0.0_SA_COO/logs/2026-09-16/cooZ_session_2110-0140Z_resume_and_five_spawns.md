# 2.0.0_SA_COO~Z -- resume after model reset, rk-7 co-sign, and five parallel spawns

**Opened** 2026-09-16 ~21:10Z on Andrew's "wind down your workers immediately", **closed** 2026-09-17 ~01:4xZ after
five workers spawned. Model reset to Sonnet mid-window per Andrew-direct ("we need to make workers use sonnet
moving forward ... make sure they are sonnet agents with high effort"); this seat's own model is now Sonnet 5.

## 1. A gap in this seat's own liveness, measured and closed

`3.0.0_SA_CVO~Z`'s L9 working record s.6 measured this seat DEAF from before the 22:2xZ hold until 01:15Z (4 of 4
messages OFFER-EXHAUSTED, no watcher, no commit since 21:16Z; reported to `1.0.0_SA_CTO~Z` as msg 23497). The
gap spans the model-reset restart of this session. Resolved by re-arming `/watcher` and resuming from the
committed restart handoff (`cooZ_session_1645-2110Z_round12_restart_handoff.md` @`3708871504`) -- no world state
was lost, because everything load-bearing had already been committed or preserved as a patch before the gap.

## 2. State re-measured at resume, matching the handoff

HEAD had advanced past the handoff via a `CLOUD -> SITEZ` integrate leg (`c0aa291a17`) and several other seats'
own commits during the hold. Re-verified before touching anything: no merge open; `worker.md` still
`sonnet`/`effort: high`; all four never-widen ledger halves for rk-6 present; all three residue patches present;
the three residue worktrees (`wk-amgt-12-23/24/25`) fast-forwarded clean to each new HEAD in turn, with the one
expected `M portal` gitlink diff on `wk-12-23` resolving itself once `0.0.0_AB_MSTR~Z`'s Card-3 push landed
(the superproject gitlink now equals that worktree's own portal branch tip exactly). Adapter unchanged throughout.

## 3. rk-7's COO half, written and signed -- both never-widen pairs now complete

`1.0.0_SA_CTO~Z` landed rk-7's CTO half at `7e84705c7a` during the hold. This seat's COO half landed at
`09b20e5546`: instrument-separated (APPLIED/EXERCISED vs the CTO half's DESIRED/source), confirming the enqueue
route, the empty queue, zero event-source mappings, zero SQS grant, and the pre-rk-6 11-route census. **This
seat's call, stated in the half: rk-6 and rk-7 ship as ONE combined deploy** (same worker slot, same function,
zero marginal safety from splitting). `4.0.0_SA_CRO~Z`'s fresh 01:19Z read confirms the Lead Panel is currently
serving ABSENT on both axes because the page's own call carries no date -- rk-7's AC4 is not latent, it is live.

## 4. ISSUER AMENDMENT 16, applied to rk-15 -- `ed8d4fe3de`

Written and dry-run before the restart, applied now after re-verifying the pre-state was unchanged (`/thesis`
for `BA_US_Equity` still `points 0`, `chart_status ABSENT`). AC2 keeps its one real bar (a control that cannot
act says why) and demotes two bars that already passed pre-work to printed context; a new AC4 grades
`point_count` on the served `/thesis` body; the `BA_US_Equity` pilot re-run (row S127) is placed on this order,
not on rk-18.

## 5. Five workers spawned, none with an explicit `model` argument -- all run Sonnet at effort high

| slot | chain | order(s) | worktree | note |
|---|---|---|---|---|
| `~24` | B | rk-6 + rk-7 (combined) | `wk-amgt-12-24` (resumed, 10 files uncommitted) | told explicitly to ship as one deploy per the COO half |
| `~29` | D | rk-17 (close-out) | `wk-amgt-12-29` (fresh) | told the two runs already happened; verify + write proof only, no re-pull |
| `~30` | E | rk-18 (fresh run) | `wk-amgt-12-30` (fresh) | egress-as-needed written into its face verbatim |
| `~23` | A | rk-12 (resume) | `wk-amgt-12-23` (resumed, 9 files uncommitted in portal) | told rk-15/rk-16 follow in a later turn, not now |
| `~25` | C | rk-14 (resume) | `wk-amgt-12-25` (resumed, 5 files uncommitted) | continues past the CSC horizon-label work it was mid-way through |

**rk-16 is the one order with no worker yet** -- it is chain A's, after rk-12, and the portal has one writer. Its
two criteria were dry-run this session and need no amendment: AC1's key-split carries the same slash cosmetic
as rk-17's did (`BP`, `NG` fragment in the printed list) but the bar itself (`keys_with_2plus_stamps`) is
unaffected, since BA/BABA/SAP/NVDA all have no slash; AC3 (the compare-surface page work) reads 0/0/0 at the cut,
a real gap to build, not a criterion defect. **Spawn it the moment `~23` reports rk-12 terminal.**

## 6. Owed next

- Drain each worker as it reports (union the channel per the established script).
- Spawn chain A on rk-16 once rk-12 lands.
- The round-12 L10/L8 packet items from the restart handoff s.5 are unchanged and still owed at drain-end.

Push state: LOCAL on SITEZ.
