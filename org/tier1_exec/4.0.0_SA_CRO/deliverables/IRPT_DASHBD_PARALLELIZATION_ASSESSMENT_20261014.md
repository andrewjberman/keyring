# IRPT_DASHBD -- how to put dell2's idle capacity on it without duplicated work (assessment, 2026-10-14 ~19:2xZ)

**Author:** 4.0.0_SA_CRO~DELL2A. **Ordered by:** Andrew, record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_191xZ_IRPT_DASHBD_PARALLELIZE_ON_UNUSED_DELL2_COMPUTE.md`.
**Status:** an assessment. The split is the CTO's ruling (workflow) and the COO lanes' issuance, on Andrew's pick. Nothing here is
issued.

## 1. What IRPT_DASHBD is doing now (measured)

- **One lane, one workstream.** Every order since round 88 is workstream B, issued by `2.0.0_SA_COO~D2`. Workstream F (the frontend
  lane `2.0.0_SA_COO~D`, a laptop seat) has no seat on dell2. Workstream B now carries the data, the render and all three firms'
  adapters.
- **Round 110 issued 19:05Z with 6 orders.** Four are pending, held by workers ~175 to ~178:
  - DB-b-217: contract 0.5.0, with the equivalence map and the Inflection household return;
  - DB-b-219: the as-of helper;
  - DB-b-220: the BD date read;
  - DB-b-221: the Cottonwood producer read.

  Two are staged behind DB-b-217: DB-b-222 (the Inflection sample) and DB-b-223 (the render). Round 111 cell 1 (the 49F household
  return) is ruled (@6c67ce88b6).
- **Cadence.** Rounds 94 to 110 took about 23.5 h, about 1.5 h per round, at about 2-3 orders per round. The fan-out cap is 8. Each
  round passes through all of these, one after another: CTO analysis, COO issuance, workers, drain, CVO compile and grade, slug,
  CTO analysis.
- **The rate limit is the serial round loop, not compute.**
  - dell2 has 16 logical CPUs, 64 GB RAM (38 GB free) and 1.5 TB free disk, and the CPU reads 53% busy.
  - 15 seats are live. 7 are idle: `2.0.0_SA_COO~C2` holds no project; `~B2` is waiting to hand off ADVI_BILLING; `0.7.0_AE_CloudOps~AQ2`
    and `~CA2`, `3.0.0_SA_CVO~DELL2`, `1.0.0_SA_CTO~DELL2` and `0.0.0_AB_MSTR~DELL2` are idle.
- **FWD coverage by order count** (211 orders):
  - FWD-8: 66; FWD-21: 37; FWD-11: 32; FWD-4: 31; FWD-12: 26; FWD-2: 15; FWD-1: 8; FWD-3: 2; FWD-9: 2.
  - FWD-5, 6, 7, 10 and 13-20 have 0.
- **Nothing for FWD-21 is on portal DEV.** Every render is private and local, and every portal commit stays on a worker branch
  ("never pushed"). FWD-21's DONE WHEN needs the report on DEV, on the tab and as the export, for one household at each of 3 firms.

## 2. The seams: where the work divides without overlap

The report has one contract, one sample builder, one renderer and one whole-document checker. The **sections** share all four, and
the same figure prints in several tables (the reason for round 110's equivalence map). Splitting by section (one agent per page)
therefore puts several writers on the same four files. **That is the overlap Andrew wants avoided, so a section split is not
recommended.**

The **firm data paths** do not overlap. Each firm has its own vendor feed, adapter, gold partition and blocker:

| path | what remains | blocker | WORLD acts (need an AE) |
|---|---|---|---|
| **49 Financial** | household TWR series (round 111 cell 1); cover name and account list (2 ABSENT, from the household directory); MTD window | none | a scheduled producer for the household series, once built |
| **Cottonwood** | account_dim adapter into gold; return gold resumed onto a schedule (S37: ends 2026-09-25, channel `blackdiamond_z09` unscheduled); household TWR (same cell as 49F) | silver stops 2026-06-23; the input is ADVI_COTBKF, now on **dell1** | the producer schedule under a never-widen pair |
| **Inflection** | adapter (account_dim, household key) done in rounds 108-109; household return from Orion's client grain (DB-b-217); account TWR derivation and tie-out (DB-b-216); render J1 re-grade | none | none yet (dry-run tables are private) |

The **ship path** (render and export onto portal DEV, the tab mount, the as-of helper, cand/dell2 approval rows) is a fourth seam.
Its write surface is the portal (`render/`, `export/`, `tabs/reporting/`, `dashboard/`), and it only READS the contract and the
filled documents.

## 3. Angles assessed

| angle | gain | overlap risk | feasibility |
|---|---|---|---|
| **A. Fill the fan-out** (same lane `~D2`, cut every round to 6-8 cells across all three firms) | about 2x per round; no new seats | low | Immediate. Still one CTO analysis and one CVO grade per round, and data-then-render pairs still take 2 rounds. |
| **B. Firm-and-ship split** (4 workstreams, 4 COO lanes, disjoint write surfaces) **-- RECOMMENDED** | about 3-4x; rounds run concurrently, not one after another | low, IF the contract has ONE writer (below) | Rule 27 permits several workstreams with disjoint surfaces under different `~lane` issuers. IRPT_DASHBD already carried B and F. Seats exist today. |
| **C. Section split** (one agent per report page) | apparent only | **high** (4 shared files, cross-table figures) | Not recommended. |
| **D. CloudOps squad "shotgun"** | small | medium (never-widen pairs, one applier per resource) | Most remaining cells are LOCAL (contract, builder, reads, render). AE work is real only for Cottonwood's producer schedule and the household-series schedule. One or two AE seats are enough; `~AQ2` and `~CA2` are idle. IAM edits are the laptop AE's (CTO correction, 2026-10-09). |
| **E. Open the untouched FWDs** (FWD-3, 7, 10 feed P1; FWD-5 and 6 do not) | new scope, not speed | low | Second. Each needs the ship lane landed first, or it renders nowhere. |

## 4. The recommended shape (B, at the next round boundary (round 114, per ADDENDUM 1))

| workstream | issuer | write surface (disjoint) | first cells |
|---|---|---|---|
| **B-49F + contract** | `2.0.0_SA_COO~D2` (continues) | `org/standards/IRPT_DASHBD_*_CONTRACT.json` (**sole writer**), the sample builder, the 49F gold | round 111 cell 1 (household TWR); cover fields from the directory; MTD |
| **B-CW** (Cottonwood) | `2.0.0_SA_COO~C2` (idle, no project) + `0.7.0_AE_CloudOps~AQ2` for WORLD | the Cottonwood adapter and gold partition, its producer schedule | DB-b-221's read becomes the schedule packet; account_dim into gold; ask dell1 for the ADVI_COTBKF silver frontier date |
| **B-IN** (Inflection) | a new COO lane (e.g. `2.0.0_SA_COO~I2`), or `~B2` once billing is handed off | the Inflection adapter and gold partition, the TWR derivation | DB-b-216 tie-out ruling; DB-b-222 sample moved here |
| **F-SHIP** (render, tab, export to DEV) | a COO lane on the portal surface (e.g. `2.0.0_SA_COO~F2`) | portal `render/`, `export/`, `tabs/reporting/`, `dashboard/`; cand/dell2 branches | land the 49F render on DEV as a cand row (internal page: CTO approves; the as-of helper is client-facing: Andrew); mount the report on the Performance tab; export PDF |

**The rules that keep it overlap-free:**

1. **One contract writer.** The other lanes PROPOSE a member's source by a surprise row or an ask to `~D2`; they never edit the
   contract.
2. **The firm lanes write only their own partition and adapter.** The shared checker scripts stay per-issuer, under each lane's
   `deliverables/2.0.0_SA_COO~<lane>/checks/`, as today.
3. **F-SHIP reads the filled document; it never builds one.** The builder stays with the contract writer.
4. **IRPT_BCKEND (`~P2`) keeps its surface** (holdings, security nodes). The household TWR is IRPT_DASHBD's (CTO msg 7829).

## 5. Feasibility limits (where the extra capacity does NOT help)

- **Grading.** One CVO on dell2 grades every J1. Four lanes roughly quadruple the L8/L9 load. `3.0.0_SA_CVO~DELL2` is idle now; a
  second CVO lane is the remedy if its queue grows.
- **The CTO.** Four workstreams mean four round analyses. `1.0.0_SA_CTO~DELL2` is idle now, but it also holds TCKT_VNEXT and
  IRPT_ANLREQ (P2, Oct 24).
- **Cottonwood.** Cottonwood's lane can do its producer read and packet, but its full history waits on dell1 (ADVI_COTBKF). A lane
  does not remove that wait.
- **Andrew's words.** The FWD-21 organic arm is Andrew's own read. The disclosure page waits on call a252. A client-facing page
  on PROD waits on him.
- **Mid-round freeze.** Round 110 is frozen; the split lands at round 111 by the CTO's ruling. It needs no PRD change, because
  FWDs do not change, only the workstreams.

## 6. What it takes to start

Andrew picks an angle. The CTO rules the workstream split as a round-111 addendum, naming the four lanes and surfaces, and seats
the new COO lanes (MSTR spawns them). Each lane then cuts its first issuance from the cells above.

-- 4.0.0_SA_CRO~DELL2A

## ADDENDUM 1 -- Andrew's go (2026-10-15 ~01:0xZ)

**Andrew, verbatim, in this terminal, answering "Say go and I'll send this to the CTO":**

> "Go on"

**Re-measured at the go (01:05Z):** IRPT_DASHBD has reached round 113. That round is ONE order (DB-b-229), issued by `~D2`,
still workstream B. Rounds 111 to 113 confirm that the round loop is the limit. The split lands at the next round boundary, round
114, by the CTO's ruling. The relay to `1.0.0_SA_CTO~DELL2` is this file's path.
