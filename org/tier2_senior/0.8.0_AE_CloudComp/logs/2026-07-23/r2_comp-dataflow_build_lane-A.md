# NFRA_MSBEFF.R2 — comp-dataflow BUILT + acceptance + bounded sweep (lane ~A)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, TRACE
**serial:** 0.8.0_AE_CloudComp~A · **date:** 2026-07-23 · **window:** session start (~18:30Z) -> ~20:05Z

## Summary

Built `comp-dataflow` (NFRA_MSBEFF.R2) — the tool for Andrew's own named state-and-dependency gap:
"does this value come from the CANONICAL source, or from somewhere else?" Value-origin trace +
canonical-source assertion; flags a producer that reads a SERVED (platinum/served/portal-json)
artifact as a value source — the layer grammar running BACKWARDS (RF-7 / PSTMRT item-9 class). One
traversal, two entry points (`origin` QUERY form + `gate` = item-9's GATE form, subsumed here per
CTO~Z). Accepted by CTO~Z @194300Z; RAVC-closed by base 0.8.0 (re-ran, not self-report) @194401Z.

## Work done

- **Startup:** /watcher (Monitor task b8z42aa8x), session serial file (LD-0290), register, cloud-ops,
  XXX.md protocol, audit-archive-invoker (rc0), comp-graph context, comp-to.
- **Phase-1 decision = BUILD** (item-9's layer-grammar gate had NOT landed — bundle 7/8/9, owner
  0.8.0_AE; I build the shared traversal + item-9 rides it). Grounded RF-7 target at
  `build_legacy_compat_emit.py:277` (platinum read -> served write) + isolated negative control
  (`build_mdpf_wse_49f_non_model_aua.py:277`, gold reads silver).
- **Grounded reversal (banked by CTO~Z):** EXERCISED `scan_lambda_io` on the RF-7 file before relying
  on it — it collapses `f"{PLATINUM_PREFIX}/{iso}.json"` to `{*}/{*}.json` (layer-bearing constant
  LOST), structurally blind to the exact read. Reversed to a focused AST reader resolving module-const
  AND function-local vars inside f-strings. Not a fork — item-9's traversal did not exist.
- **Built** `org/modules/graph/comp_dataflow.py` (engine) + `.tools/comp-dataflow` (wrapper). Layer
  grammar: bronze<silver<gold<platinum<served; served-layer reads (platinum/served/portal-json/
  legacy-served-basename) flag; inline `# dataflow-exempt:` first-class per TRIGGER_LAYER.
- **Registered additively** (base 0.8.0's 4 rules, tail-appends, self-landed): tools_index +
  entries `lineage.dataflow.canonical_source` + comp-output-contracts.yaml verdict contract
  (rc1=verdict, rc3=refuse) + comp-coverage-map.yaml not_homed ledger (read-source sibling of
  comp-clobber). comp-manifest-check completeness PASS; coverage-view --verify 65/65 in sync.
- **comp-system regen** folded in (base rule 3); attributed the gensdk scaffold.py rule-bank
  v1.1->v1.2 ride-along as mechanical generator output of the already-committed ~C ONTOLOGY2 P1 v1.2.

## Acceptance (all on the record)

- **RF-7 mutant** (`build_legacy_compat_emit.py`) — exit 1, 5 blocking findings incl. L277 platinum
  read. FLAGGED.
- **Isolated negative control** (separate invocation) — exit 0, gold-reads-silver clean, 2 dynamic
  reads named+counted.
- **Same-file 4-read discrimination** (CTO~Z refinement) — platinum (module-const) FLAG + silver/gold
  (local-var) PASS: reads GRAMMAR not filename, both constant scopes. self-test 7/7.
- **Bounded sweep** (Phase-3): `comp-dataflow gate data/mdpf/scripts/` — **16 served-origin findings /
  8 producer files** (platinum=11, portal-json=5). Denominator: 27 files swept, 71 reads scanned,
  30 unresolved-dynamic (BLIND floor), 0 exempt. TRUE exit=1. Routed to CTO~Z first (MDPF hard
  constraint); artifact `deliverables/NFRA_MSBEFF.R2_comp-dataflow_mdpf_sweep_20260723.json`.
  **RF-7 is a PATTERN across the mdpf tree, not a one-off** — 8 producers read platinum/served as
  value sources. Framed as the CLASS for CTO~Z triage (defect vs exempt-worthy), not pre-judged bugs.

## Self-caught measurement artifact

First sweep read `exit=0` through a `| tail` pipe (the piped-exit trap — `$?` captured tail's exit,
not the tool's). Re-measured with PIPESTATUS: real gate exit = 1. Tool correct; measurement masked.
Same "put the control on the RETRIEVAL, not the pattern" class as the CLAUDE.md `grep -c` example.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-to | set TO_ID NFRA_MSBEFF.R2 | OK | race-free session TO |
| comp-manifest-check | completeness | PASS (bar existence, resolved at commit) | output-contract invariant clean; only block = untracked wrapper, fixed by safe-commit git add -f |
| comp_coverage_view.py | --verify | PASS | 65/65 tools_index in ledger union; projection current |
| comp-dataflow | --self-test / origin / gate | PASS 7/7; exit 1 on RF-7, exit 0 on control | my own tool, exercised as acceptance |
| comp_output_contract.py | --self-test | PASS | comp-dataflow declared (19), not stray |
| comp-blast/comp-pipescript | (Phase-1 reuse survey via source read) | — | evaluated scan_lambda_io for reuse; exercised + rejected (blind to RF-7) |

**What worked:** the R1R3 output-contract helper (`comp_output_contract.header_block`) — clean
downstream consumption, LOUD UNKNOWN before registration then resolved after. The coverage-map/
tools_index projection guard caught nothing (in sync) because I edited both.
**What failed:** nothing blocking. `--self-test` as an argparse subparser name (starts with `--`)
didn't dispatch — fixed by intercepting it before the parser.
**Gap found:** `scan_lambda_io` loses layer-bearing constants inside f-strings — a real reuse blind
spot (documented in comp_dataflow docstring + the coverage-map not_homed_reason).

## Current State

- `comp-dataflow` LIVE + pushed @6327b0006; sweep artifact @b81ec4bda; both on origin/CLOUD.
- 16 mdpf served-origin findings routed to `1.0.0_SA_CTO~Z` (disposition owner; MDPF-first constraint).
- Future seam (base flagged): when ~B's `retired_aliases` lands, wire a retired-producer-name check
  into `comp-dataflow origin`. Not this wave.
- Watcher b8z42aa8x live. 17 remaining pending TOs in my lane queue (R2 was the dispatched one).

## Next Steps

- [1.0.0_SA_CTO~Z] triage the 16 served-origin findings (defect vs exempt); owns whether/when any
  reaches main-fabric after their MDPF serve closes.
- [3.0.0_SA_CVO~Z] verify the RF-7 flag + isolated + same-file 4-read controls (family charter).
- [0.8.0_AE_CloudComp~A] event-driven; await next dispatch / CVO~Z rework if any.

## Blockers

None.
