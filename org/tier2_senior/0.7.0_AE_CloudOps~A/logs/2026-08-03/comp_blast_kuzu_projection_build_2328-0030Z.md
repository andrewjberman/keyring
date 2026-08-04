# comp-blast kuzu-projection build -- universe re-base + 4 dial defects

**archetype:** IMPLEMENT

**Agent:** `0.7.0_AE_CloudOps~A` · **Window:** 2026-08-03 ~2328Z - ~0030Z
**Authority:** Andrew-direct ruling 2026-08-03 (projections default to the kuzu full resource graph);
CVO spec `SPEC_comp-blast_kuzu_projection_20260803.md` @03ff36daee. Andrew instantiated this seat for
the build and assigned it at the CVO terminal.
**Commits:** `72753ea4f2` (build) · `7dcebf0c6c` (comp-system discharge)
**Baseline vintage:** `a1cab01483` (all four defects measured live there, before any edit)

---

## Current State

DELIVERED, awaiting CVO's 7-gate acceptance battery + CLOSE verdict.

comp-blast's universe is now the canonical kuzu graph. The private trace graph is retired as a
universe; its one defensible property (invocation-time head-pinning) survives as a subject-scoped
worktree overlay. All four 07-31 dial defects are fixed, each with a failing-direction regression,
and all five mutants are caught.

| | before (`a1cab01483`) | after (`72753ea4f2`) |
|---|---|---|
| universe | 2,255 nodes / 2,950 edges | 20,480 / 40,924 |
| S3 buckets | 4 | 33 |
| cold path | ~35,000 ms | ~4,461 ms |
| `comp-blast opal-data-mdpf` | rc=3 NOT-FOUND | rc=0 full answer |

## What I did

1. **Cut baselines BEFORE touching anything** (spec s4): exit-code suite 7/7 green at
   `a1cab01483`, universe census, and a live reproduction of each defect.
2. **Built `org/modules/graph/comp_blast_universe.py`** -- kuzu projection, ASCII emission boundary,
   subject resolution, worktree overlay, dual provenance.
3. **Re-wired `cmd_blast`**; fixed (a)/(b)/(c)/(d); added rc=5 AMBIGUOUS-SUBJECT.
4. **Gates:** 26 passed / 1 skipped across both suites; 5/5 mutants caught; manifest-check PASS.

## Defects -- measured, not inherited

**(a) cp1252 crash. ROOT FOUND, and my first measurement was wrong.**
I scanned `nerves-risk-edges.json` as raw text, got **0 non-ASCII**, and nearly recorded (a) as
non-reproducing. It stores non-ASCII **JSON-escaped** (`→`), so the FILE is pure ASCII while
`json.load` decodes real arrows into the claim prose `_render_risk` prints. A full-denominator sweep
through a real cp1252 stream found **28 of 2,255** nodes crashing (07-31 measured 20 of 2,252 --
same class, count tracks the cache). *I was checking the wrong layer; only exercising it caught that.*
**The crashing nodes are the RISK-BEARING ones** -- the crash silenced HOLD warnings on the most
dangerous files in the estate. Fixed at the **emission boundary**, not in the data: the corpus is
harvested from commit prose, so non-ASCII is a permanent inflow and a data edit re-breaks on the
next harvest.

**(b) `--direction up` inverted the consumer verdict into a false phantom.**
`gold:A_00.accounts_dimension`, 143 real consumers: default `rc=0 CONSUMER-OK`, with `--direction up`
`rc=4 PHANTOM-CONSUMER`. `grounding_lib` maps rc=4 to deletion evidence. Verdict now evaluated over
dependents in **both** directions; direction governs display only, so no flag can manufacture a phantom.

**(c) substring + `matches[0]` answered about a different node at rc=0.**
`comp-blast load_accounts_dim` returned a full answer about
`gold:B_01.holdings_lots:load_accounts_dimension` -- different function, different script -- while the
exact node existed among 17 matches, with nothing saying a choice had been made. Now: exact-id ->
colon-suffix -> exact-segment -> substring; any ambiguous tier refuses at **rc=5**.

**(d) PROVEN not assumed -- it did NOT dissolve under kuzu.**
The spec said "likely dissolves into edge_type mapping -- prove it with the regression, don't assume
it." It does not. `endpoint:getPlatinumPartnerAnalytics` has **8 upstream FETCHES callers and 0
downstream**; the old default computed upstream only for function-grain `GOLD_SCRIPT`, a node_type
that existed only in the retired universe, so under kuzu the default hid **every caller in the
estate** -- and combined with (b) would have called that live endpoint an orphan. Root: the graph
**mixes edge conventions** -- `WRITES` points producer->artifact (consumers downstream) while
`CALLS`/`FETCHES`/`READS` point consumer->producer (consumers upstream). Default is now bidirectional.

## Judgment calls surfaced (not silently taken)

1. **ID-shape migration.** Kuzu says `pipeline:bd:gold:A_00.x`; every existing call site says
   `gold:A_00.x`, and kuzu carries **zero** `gold:`-prefixed ids. Without the colon-boundary suffix
   tier the legacy id is a substring of the script AND all ~40 of its function nodes -> AMBIGUOUS:
   a fix that breaks the fleet. Gated by a regression.
2. **Declared exception (ruling clause 2).** `--compare` / `--overlap-sweep` / `--all-producers`
   still read the private trace graph and now say so at runtime, named + vintaged + scoped. They are
   corpus statistics whose idf is defined over a producer population; silently swapping it would
   change what every score MEANS while the numbers kept printing. **Routed to CVO as residue.**
3. **Freshness contract preserved exactly.** `--check` still delegates to the same `_freshness_probe`
   the status surface uses (spec s4 "must survive unchanged"); kuzu's vintage is a separate axis
   reported in the dual-provenance block, never folded into that predicate.
4. **Test candidate derivation re-pointed to the live universe.** On the first post-rewire run the
   phantom regression -- the test that file exists for -- **SKIPPED**, because kuzu gives those nodes
   dependents. A skipped test is not a gate (that file's own words). Assertions unchanged.
5. **Module named `comp_blast_universe.py`.** The owned-paths gate blocked `blast_universe.py`
   (fell through to exec-locked `org/modules/graph/**`). `comp_*.py` is `ANY_EXEC_OR_AE` --
   *"Compiler tool implementations. AE owns build"* -- and matches the repo convention
   (`comp_debt`, `comp_pydeps`, `comp_ladder`). The gate was right; my filename didn't express
   the ownership the gate encodes.

## Compiler Tools

| Tool | Result | Notes |
|---|---|---|
| `comp-kuzu` | PASS | Confirmed `opal-data-mdpf` present as S3_BUCKET + S3Key grain; read the provenance header (build 2.2h old, `graph_nodes` flagged STALE>6h cadence) |
| `comp-blast` | PASS | The subject of the build; exercised before/after on all four defects |
| `comp-manifest-check completeness` | PASS | registration + output-contract + stage-2 vocab + retired-alias invariants all PASS over 69 registered tools |
| `comp-system` | PASS | Regenerated 06_current_state to discharge the two-phase override |
| `comp-surface-check` (via safe-commit) | OK | 5 files screened against 6 surfaces, no critical surface touched |
| `comp-pulse diff` (risk reflex) | CLEAN | measured: 5 files vs 1,662 danger nodes |
| `comp-grep`/`comp-which` | n/a | Targets were known from the spec (`cli.py`, `trace_graph.py`); used native Read/Grep on named files, which is the on-rails exception |

## Blockers

**None.** Nothing is waiting on me.

## Next Steps

1. **[3.0.0_SA_CVO]** Run the s6 acceptance battery + issue the CLOSE verdict (also closes the
   07-31 comp-blast DIAL record).
2. **[3.0.0_SA_CVO / 1.0.0_SA_CTO]** Rule on the declared exception: re-base the three statistical
   modes onto kuzu, or ratify the exception permanently.
3. **[Andrew, non-blocking]** comp-blast's formal purpose line (P1) and the `chain` reserved-term
   collision -- both explicitly do not block this build.
