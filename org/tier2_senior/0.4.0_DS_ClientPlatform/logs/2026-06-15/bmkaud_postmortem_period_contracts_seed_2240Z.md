# BMKAUD postmortem + period_contract seed (lane ~A, Andrew-direct)

**archetype:** DIAGNOSE
**secondary_archetypes:** SCRIBE, IMPLEMENT

Agent: 0.4.0_DS_ClientPlatform~A. Window 2108Z->2240Z, after NFRA_PIPESCRIPT close. Andrew-direct
(post-close): reconstruct the benchmark 1M-column break as a postmortem, then evaluate whether the
enhanced pipescript + Nessie/Kuzu surfaces would catch it -> seed the fix.

## Summary

Two pieces of Andrew-direct work: (1) a context postmortem of the BMKAUD incident (Model Portfolios
/performance tab, 1M column, 2026-06-01); (2) the architectural follow-on Andrew greenlit -- a
`period_contract` / `graph_contracts` seed that closes the SEMANTIC-flip gap the postmortem exposed.

## The incident (reconstructed from logs/commits, not re-run)

BMKAUD (Benchmark Yang-Truth Audit, 2026-06-01, directive `docs/briefs/benchmark-yang-truth-audit-20260601.md`):
- ROOT: a SmartX override replaced the canonical Yang-PKL benchmark numbers as the INPUT; SmartX
  `1M=last-complete-calendar-month` != Yang trailing-1M -> wrong 1M (CTO WS-3 msg; revert `80224d674`).
- CONTRIBUTING: `json/benchmarks/*` has 1 canonical writer (yang-pipeline-role) but 4 non-canonical
  principals CAN write it (smartx-monthly-pull, EC2 exporter `generate_benchmark_performance.py`
  = `opal-generate-benchmark-returns` dormant dual-writer, smartx-ingestion, news) -- writer census
  `b7fb71fa0`; v2.4.10 deploy-record drift (benchmark co-listed but not redeployed, `d78fd32ca`).
- COMPOUNDING (separate FE bug): UST-1M Peers chart "No data available" = a JS `!p95` falsy guard
  dropping `p95=-0.0`; data present+faithful (`c868bd41`, CVO `8d3252f15`).
- DETECTION: manual (Andrew eyeballed a wrong 1M; no alarm -- artifact was fresh + present + a valid float).
- FIX (durable): reverts to pure-yang; IAM `DenyNonYangWriteBenchmarks` (`b1a3543c9`); smartx
  canonical<->bundle drift guard; dual-writer retirement.

## The analysis (would the new surfaces catch it?)

- pipescript: YES for STRUCTURE -- `pipescript model-portfolios` shows yang as canonical producer +
  consumer in one view; `pipescript --resource benchmark` surfaces the 4-writer reality (incl
  smartx) the audit hand-censused. PREVENTS wiring the wrong source; collapses WS-1 to two queries.
- Nessie/Kuzu: YES for the STRUCTURAL change -- a new WRITES edge into json/benchmarks is a snapshot
  diff (comp-kuzu live, showed BEHIND->auto-refresh to current HEAD; queries the benchmark lambdas).
- BOTH MISS the SEMANTIC value-contract (SmartX-1M != Yang-1M). Graph charter = code/infra changes
  only, excludes data-plane values; pipescript maps structure not period-definitions. That residual
  is what the seed addresses.

## The seed (Andrew greenlit "go ahead do it")

`period_contract` = both the reference frame the Iceberg/Nessie snapshot history is diffed against
AND the allow-list the diff is judged by -> "what flipped + which crossed a line nobody re-drew."
The never-widen doctrine encoded on the value layer (ratified contract edit = the sign-off, recorded
as a Nessie commit). Brief contains: `graph_contracts` Iceberg DDL (globgrph Nessie main, beside
graph_nodes/edges) + the benchmark contract fully worked (binds SEV1 `model_portfolios.benchmark` =
the literal performance tab + pipescript `yang-benchmarks-etf-returns`; canonical_writer=
yang-pipeline-lambda-role; period_defs incl 1M=trailing; forbidden_writers incl the smartx override)
+ Q1 what-flipped / Q2 which-shouldn't-have (SANCTIONED-vs-UNSANCTIONED = intended-vs-regression) +
BMKAUD replay + pipescript --contract/--flipped surface + SEV1 rollout.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| pipescript | `model-portfolios`, `--resource benchmark/smartx-model-monthly` | PASS | grounded the postmortem: showed yang canonical + the 4-writer surface |
| comp-pipescript | `io finbert-batch-processor` (OOS-guard demo) | PASS | OUT-OF-SCOPE -> globgrph exit 2 (P1b.1 working, used as analysis example) |
| comp-kuzu | `MATCH ... WHERE n.name CONTAINS 'benchmark'` | PASS | live; BEHIND-Nessie-HEAD -> auto-refreshed to current; returned yang + opal-generate-benchmark-returns |
| safe-commit (surface-check) | seed brief commit | PASS | OK: touches no critical surface |

**What worked:** the live tools made the postmortem CONCRETE -- `pipescript --resource benchmark`
reproduced the audit's hand-census in one line; comp-kuzu confirmed the dual-writer in the live graph.
**What failed:** nothing this window. **Gap found:** the SEMANTIC value-contract is a real blind spot
in BOTH pipescript and the graph charter -- the seed (period_contract) is the proposed third limb.

## Briefs Written (DS)

| Brief | Path | For |
|---|---|---|
| Period-contracts seed | docs/briefs/period-contracts-seed-benchmark-20260615.md (48635a865) | CTO schema-ratify / AE Iceberg stand-up / CVO contract-author / DS pipescript-surface |

## Blockers

None.

## Current State

NFRA_PIPESCRIPT CLOSED (prior). This window = Andrew-direct postmortem + seed, both context/doc work
(no code/infra change). Seed committed+pushed: docs/briefs/period-contracts-seed-benchmark-20260615.md
(48635a865). Routed to COO (CC CTO) for cross-lane decomposition. Tree clean. The seed proposes a
NEW capability (graph_contracts Iceberg table + period_contract surface) -- not yet a registered
project; COO to decide project placement (NFRA_CONTRACTS vs fold under globgrph/DEBTSCAN).

## Next Steps

1. [2.0.0_SA_COO] - decompose the period_contract seed (project placement + the 4-lane ownership
   split in the brief); or hold for Andrew's project-shape call.
2. [1.0.0_SA_CTO] - ratify the graph_contracts schema + the ratified-commit-as-sign-off semantics.
3. [0.7.0_AE_CloudOps] - (on CTO ratify) stand up the Iceberg table + Q1/Q2 (comp-aws diff) + wire
   Q2 into comp-surface-check for SEV1 contracted surfaces.
4. [3.0.0_SA_CVO] - author SEV1 contract rows (benchmark seeded -> AUM -> NNA).
5. [0.4.0_DS_ClientPlatform~A] - IDLE/available; ready to take the `pipescript --contract/--flipped`
   surface leg or iterate the schema on CTO's read. Otherwise event-driven for MSTR/Andrew direction.
