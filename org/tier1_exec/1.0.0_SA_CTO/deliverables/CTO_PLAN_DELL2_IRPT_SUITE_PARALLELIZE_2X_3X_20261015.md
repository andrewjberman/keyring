# CTO PLAN -- parallelize the Investor Reporting Suite 2x to 3x (2026-10-15 ~23:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Asked by:** Andrew at the dell2 terminal: "We need to figure out how to parallelize this 2x or 3x:
org/tier1_exec/4.0.0_SA_CRO/briefs/IRPT_SUITE_STATUS_BY_WORKSTREAM_BRIEF_20261015.md, how can we scale workers across these streams?"
**Basis:** the CRO's brief (@d56567f5ed) and three reads measured at ~23:0xZ:
- the live roster (`org/mcp/liveness.json`);
- today's commits by author (`git log --since 2026-10-15`);
- the sequence reader's capacity line.

**Status:** a PLAN for Andrew's word. Nothing in it is acted on until he says go. Seating is MSTR's act; issuing is each COO's.

## 1. Where the time goes (measured, not guessed)

The suite is 3 of 41 outcomes and 20 of 62 checkpoints done (brief section 1). The limit is not workers, which are cheap and capped at 8
per issuance. The limits are **five serial queues** that every lane passes through:

| queue | who | load today (commits 10-15) | why it serializes |
|---|---|---|---|
| **Q1: IRPT_BCKEND issuance** | `2.0.0_SA_COO~P2`, ONE seat running six or more lanes (~P, ~PJ/PQ, ~PM, ~PN, ~PO, ~PS, ~PI, ~PB, ~PL) | **242**, the most of any seat | "one issuer per round"; each lane waits its turn for ~P2's attention |
| Q2: applies | 3 deploy agents: IB2 (all IRPT_BCKEND), DB2 (IRPT_DASHBD), AQ2 (resident and portal runs) | -- | "one executor never runs two applies at once" is currently enforced per AGENT, not per artifact |
| Q3: CTO halves and analyses | `1.0.0_SA_CTO~DELL2` | 161 | every pair, ruling and round analysis |
| Q4: L9 grading | `3.0.0_SA_CVO~IRPT` | 81 | every IRPT round's slug |
| Q5: Andrew | -- | -- | 2 items on the P1 path (the disclosure page is now a placeholder; the client-facing approval) |

**Idle or waiting capacity** (brief section 4):
- `~C2`, `~F2` and `~T2` are WAITING, and `~V2` has had no commit for about 25 h. That is 4 of 9 COO lanes not building.
- **13 of 21 IRPT_DASHBD outcomes and 4 of 13 IRPT_BCKEND outcomes are NOT STARTED.** Most do not depend on the critical path at all.

## 2. The plan: three moves, in order of leverage

### Move 1 -- split ~P2 into three seats (Q1). Leverage: the largest. The critical path for holdings and Inflection runs through it.

Rule 27 allows several workstreams with disjoint boundaries and write surfaces under different `~lane` instances; seating is one
project per Tier-2 instance. IRPT_BCKEND's lanes already fall into three disjoint write surfaces:

| new seat | lanes it takes | write surface (disjoint) |
|---|---|---|
| `~P2` (keeps) | holdings producer (~P), refused publishes / exemption (~PJ/PQ), split (~PM), CUSIP S206 | holdings bundles, `holdings_snapshot.py`, `publication.py`, the holdings-performance function |
| `~N2` (new) | Inflection Scope feed (~PN), Orion re-cut (~PO) | `data/inf/manual_api/`, `infra/aws/terraform/inf-pipeline`, `opal-data-assets/orion/inflection/` |
| `~S2` (new) | filled-report export (~PS), the report route IB-pr-551 (the item gating ~F2 and ~D2), analysis-commentary route items (~PI) | `infra/aws/lambda/investor-reporting/` export and route code, the serve path |

Each seat issues its own rounds. The CVO~IRPT slugs stay per workstream as today. Expected effect: three IRPT_BCKEND rounds in flight
instead of one. **IB-pr-551 gets a dedicated owner**, which unblocks ~F2's default report and ~D2's 49F household.

### Move 2 -- open the NOT-STARTED outcomes on the idle lanes (capacity already seated, 0 new seats)

Point each WAITING lane at independent outcomes the critical path does not touch. Each is a new workstream with its own write surface.

| lane | stop waiting on | take now (P1-relevant, independent) |
|---|---|---|
| `~F2` | the served 49F sample | FWD-3 (asset-class performance and mix) and FWD-5 (transactions browse and export): new tab sections on gold that already exists |
| `~C2` | the first scheduled report run | FWD-10 (where data starts and which days are missing): Cottonwood's 3 absent days, its 07-10 floor and the 12-day gap are already measured |
| `~T2` | run 3 | IRPT_ANLREQ FWD-4 (a broken step is never silent) and FWD-5 (another firm never sees the request): tests and alarms-as-gates on paths that already run |
| `~V2` | (idle 25 h) | its own TCKT_VNEXT P2 (due Oct 24); MSTR reads why it stopped |

Each one is cut by its own COO from a decomposition cell, as usual (the CTO adds the cells by PRD addendum where none exists).

### Move 3 -- widen the four other queues, so Moves 1 and 2 do not just pile up behind them

1. **Applies (Q2): one deploy agent per artifact family, not per project.**
   - IB2 keeps the holdings bundles.
   - A new `IB3` takes `inf-pipeline` (Scope feed, Orion pairs, the runner).
   - AQ2 keeps the resident.
   - A new `YC3` takes `irpt-ycharts-generate` (r33) and the portal promotes.

   The rule stays "never two applies on one artifact at once"; two DIFFERENT artifacts may apply at once. This is a CVO ruling on the
   rule's reading, pitched with that REC.
2. **CTO halves (Q3): a standing template class.**
   - A pair matching an already-signed template is signed within the hour, on its checklist alone. The templates are a handler-only code
     update, a member-diff-equals-intended release, and a spelling addendum.
   - Everything else gets a full read.
   - No new seat. The batching is mine to do.
3. **L9 (Q4):** the IRPT CVO lane grades about 10 slugs an hour today. If Move 1 triples IRPT_BCKEND's rounds, seat a second IRPT CVO lane
   `3.0.0_SA_CVO~IRPT2` with a disjoint project split (CVO~IRPT keeps IRPT_DASHBD; ~IRPT2 takes IRPT_BCKEND and IRPT_ANLREQ).
4. **Workers:** keep fan-out at the cap of 8 per issuance. The gain comes from more issuers (Moves 1 and 2), not more workers per
   issuer, because each round's cells are already cut along its dependency chains.

## 3. What it costs, and the one constraint

- **New seats:** 2 COO (~N2, ~S2), 2 AE (IB3, YC3), 1 CVO (~IRPT2). That makes 11 COO lanes on dell2, against 9 today.
- **The constraint is Andrew's own word of 2026-09-14 ~07:0xZ:** "We can only have 3 COOs running their respective projects/subagents at
  any one time". The box already runs 9, and the sequence reader prints "no cap ruled for this box". Moves 1 and 2 need his word that
  the cap does not bind dell2, or a cap number. That is the one decision in this plan that is his.
- **Box resources are not measured here.** CPU and memory headroom for 2 to 4 more Claude sessions plus their workers on dell2 should be
  read by MSTR before seating. If the box is full, ~N2 or ~S2 can seat on dell1 only if their write surfaces stay disjoint, which is a
  cross-box placement and MSTR to MSTR.

## 4. Expected effect (an estimate, not a measurement)

- **Move 1:** IRPT_BCKEND throughput about 2x to 3x; three issuers instead of one.
- **Move 2:** 4 idle lanes produce. That starts 6 not-started outcomes now instead of after the critical path.
- **Move 3:** keeps the added rounds from queuing at apply, sign and grade.

Together this is the 2x to 3x asked for, on the outcome count, not only the commit count. The next status brief (the CRO's, same shape)
is the measurement: count checkpoints done per day before and after.

## 5. Order of acts on Andrew's go
1. MSTR reads box headroom, then seats ~N2 and ~S2 (Move 1). ~P2 hands each lane's open orders and rows over by record.
2. The CTO writes the PRD addenda that cut the Move 2 cells, and the lanes issue.
3. The CTO pitches the per-artifact applier reading to the CVO. MSTR seats IB3 and YC3.
4. If the slug rate climbs past the CVO's measured pace, MSTR seats CVO~IRPT2.

-- 1.0.0_SA_CTO~DELL2
