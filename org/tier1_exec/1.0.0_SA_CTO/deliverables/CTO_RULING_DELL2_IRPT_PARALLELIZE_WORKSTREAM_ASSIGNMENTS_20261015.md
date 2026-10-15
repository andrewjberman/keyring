# CTO RULING -- IRPT suite parallelization: the workstream assignments (2026-10-15 ~23:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**On:** Andrew's go (`ANDREW_DIRECT_20261015_231xZ_PARALLELIZE_IRPT_SUITE_GO.md` @efdb6554ef) on the plan @41ba81c63a.
**No PRD addendum is needed:** every outcome below is already an ENDPOINT outcome of its admitted PRD. Each lane decomposes (L5) and
issues (L6) as usual, as its own workstream with a disjoint write surface (CLAUDE.md rule 27: one issuer per round, a workstream is a
scope).

## Move 1 -- IRPT_BCKEND splits into three issuers (seats by MSTR)
| seat | workstreams | write surface |
|---|---|---|
| `2.0.0_SA_COO~P2` | holdings producer (~P); refused publishes and the exemption (~PJ/PQ); split returns (~PM); row S206 | holdings bundles, `holdings_snapshot.py`, `publication.py`, the holdings-performance function |
| `2.0.0_SA_COO~N2` (new) | the Inflection Scope feed (~PN); the Orion re-cut (~PO) | `data/inf/manual_api/`, `infra/aws/terraform/inf-pipeline`, the feed's `opal-data-assets/orion/inflection/` prefixes |
| `2.0.0_SA_COO~S2` (new) | the filled-report export (~PS); the report route IB-pr-551; the analysis-route items (~PI) | the export and route code under `infra/aws/lambda/investor-reporting/` (not `holdings-performance`), the serve path |

**Hand-over, by record:**
- `~P2` writes ONE hand-over file per new seat. Each lists that seat's non-terminal orders, its open rows (with owners re-pointed by an
  appended row, never an edit), its signed pairs and their ledger state.
- An order in flight finishes under its current issuer. Only NEW cells cut under the new seat.
- A disputed boundary (one file touched by two seats) is a ruling back to me, never two issuers on one file.

## Move 2 -- the waiting lanes take outcomes nobody has started (no new seats)
| lane | outcome (PRD) | start with | write surface |
|---|---|---|---|
| `2.0.0_SA_COO~F2` | IRPT_DASHBD **FWD-3** (asset-class performance and mix) and **FWD-5** (transactions browse, filter, sort, export) | FWD-3 per the PRD's surface row S09 (gold `account_class_daily`, classes sum to the account), then FWD-5 | new portal tab sections plus their gold readers; not the default-report files it already holds |
| `2.0.0_SA_COO~C2` | IRPT_DASHBD **FWD-10** (where the data starts, which days are missing) | Cottonwood first: the 07-10 floor, the 3 absent days, the 12-day gap, all measured. Then 49F and Inflection | the coverage readers and `MethodAndSources` (surface row S07), the coverage vocabulary |
| `2.0.0_SA_COO~T2` | IRPT_ANLREQ **FWD-4** (a broken step is never silent) and **FWD-5** (another firm never sees the request) | FWD-5's cross-firm tests on the paths that run today; then FWD-4's per-step failure surfacing, as gates and owned rows, never a new alarm (the standing moratorium) | tests and the pipeline's own refusal paths in the commentary and request lanes |
| `2.0.0_SA_COO~V2` | its own TCKT_VNEXT (P2, due Oct 24) | MSTR reads why it stopped first | unchanged |

Each lane's first round is ONE issuance with its decomposition cells. Fan-out stays at the default cap of 8.

## Move 3 -- the other queues
- **Deploy agents:** one per artifact family (`IB3` for `inf-pipeline`, `YC3` for `irpt-ycharts-generate` and the portal promotes).
  This needs the CVO's reading that the rule binds an artifact, not a seat (pitched as a governance fork).
- **CTO halves:** a pair matching a signed template is signed within the hour. The templates are a handler-only code update (the
  chain-cap half's Q3), a release whose member diff equals the intended members, and a spelling addendum.
- **A second IRPT CVO lane:** only if the slug rate climbs past the CVO's measured pace (MSTR's measure).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (~23:2xZ): seated, and the CPU budget (MSTR msg on 8738/8753)
- **Seated 23:10-23:13Z:** COO `~N2` and `~S2`; AE `IB3` and `YC3`. `~V2` was never stopped: it is live and waiting on the laptop bucket
  apply (target Oct 20).
- **Headroom, as MSTR measured it:**
  - 8 cores and 16 threads; CPU 74% before and 75% after;
  - RAM 32.3 of 63.7 GB free;
  - 44 claude.exe processes.
- **CPU is the limit, RAM is not.** So the per-issuance fan-out on dell2 is **4, not the default 8**, for every IRPT lane, until MSTR reads
  CPU below 60% sustained.
  - The parallelism comes from more issuers (now 11 lanes), not from more workers per issuer.
  - MSTR re-reads CPU at its hourly cadence. A sustained read above 90% is a call back to me, which may ask dell1 to host a lane, MSTR to
    MSTR.
