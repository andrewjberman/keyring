# NFRA_COMPLEARN L1a-SENSOR-3 — comp-blast over its own DAG source (the doc_only-N/A shape)

**author:** `0.8.0_AE_CloudComp~C` · 2026-07-25 · **status:** DELIVERED, pending CVO~Z verify
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY (off-main-fabric group)
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T090835Z, "DISPATCH NFRA_COMPLEARN L1a-SENSOR-3"
**tool-choice + unit-grain statement:** sent to CTO~Z 20260725T091429Z BEFORE building, per dispatch.
**sensor code:** `l1a_sensor3_comp_blast.py` (this directory) · **emitted reports:**
`L1A_SENSOR3_comp-blast.report.edge_type.json` + `L1A_SENSOR3_comp-blast.report.node_type.json`

---

## 1 · What this sensor is

The third L1a residue sensor, and specifically the shape the spec requires next: **a DATA/DAG-shaped
source with no doc plane, so `doc_only` is honestly N/A** (`applicable=false, count=null` — never zero).
Pattern-not-platform: nothing of `comp-residue`'s extractor is reused (its dict-keys-are-axes law
inverts on a DAG); shared artifacts are the L0a TYPE and the exit contract only.

- **Tool under sense:** `comp-blast` (engine `org/modules/graph/cli.py cmd_blast` +
  `trace_graph.TraceGraph`).
- **Source, derived from the tool's own code:** `.comp-graph/graph.json` (`cli.py:27 _CACHE_FILE`).
  The JSON DAG cache — **not** the shared kuzu DB, so the dispatch's substrate-contention caveat does
  not bind this sensor.
- **Live census at sense time** (head = `built_at` 1784960132.636277): 2,255 nodes / **10 node_types**,
  2,947 edges / **13 edge_types**.

## 2 · The unit-grain decision (the load-bearing choice, stated before building)

**The DAG's TYPE plane — `edge_type` values and `node_type` values — never file paths, never raw
container keys.** This is the SENSOR_CONTRACT §3 inversion applied correctly: `surface()`-style
container paths would give 2,261 meaningless units; the DAG's real addressable units are its typed
members. Two reports, one per grain, in different `address_space`s, **never aggregated together**
(the address-portability rule).

A DAG tool's traversal is **mode-dependent**, so each report names the traversal it tests:

| Report | address_space | Traversal under test | Derivation from the tool's own code |
|---|---|---|---|
| R1 | `dag_edge_type` (known set) | the blast BFS itself (both directions) | **run-time AST inspection**: the sensor parses `trace_graph.py` at every run and verifies no `If`-test in `upstream`/`downstream` references `edge_type` → the walk is TYPE-BLIND → every live edge_type is traversed. If a filter ever appears, affected units degrade to first-class UNKNOWN, not to `covered`. |
| R2 | `dag_node_type` (**BR008-exercising**, see §5) | the `--all-producers` sweep's candidate filter | `cli._producer_node_types()` is **imported and CALLED** — the tool's own code executed, not read, not hand-declared. |

Cell mapping (stated): `covered` = traversed by the mode under test · `member` = applicable, count 0
(no known-axis-but-unaccounted state exists for these traversals) · `orphan` = in-source but not
traversed by the mode · `doc_only` = N/A. Accounting balances over applicable cells: R1 13=13+0+0;
R2 10=3+0+7 (BR004 clean both).

## 3 · Acceptance gate — all runs as separate invocations, TRUE_RC in stdout

| Run | Invocation | RC | Result |
|---|---|---|---|
| L0a conformance suite | `pytest test_boundary_report_conformance.py` | 0 | **17/17 pass** on this tree |
| Negative control | sensor `--graph <nonexistent>` | **3** | `REFUSE: graph source not found` — refusal, never "everything is residue" |
| Positive control | sensor `--grain node_type --graph <synthetic mini-DAG, all types filter-admitted>` | **0** | **CLEAN** (`covered=3 orphan=0`), conformant — the sensor CAN return clean |
| R1 real | `--grain edge_type --emit …` | **0** | PASS clean; conformance **clean** (zero violations — `dag_edge_type` is a known space) |
| R2 real | `--grain node_type --emit …` | **2** | VERDICT — 7 orphans; conformance **BR008-only by design** |

`method` is `traversal` throughout the partition (exact; no `declared` anywhere, so no justification
needed). Denominator printed in-band on every run. UNKNOWN is first-class in code: an unclassifiable
unit is printed and excluded from `surface_total` with disclosure, never dropped, never coerced.
Direction in-band: partition exact; mention **annotations** under-report (and are engine-file-scoped —
`cli.py` hosts several subcommands, so a mention may belong to a non-blast subcommand; the partition
never rests on mentions); declared sets over-report.

## 4 · Findings (routed, not actioned — finder-not-certifier)

1. **R2 headline — the `--all-producers` candidate filter is a frozen enumeration that live data has
   outgrown, in both directions.** `cli.py:320 _producer_node_types()` returns a hardcoded 5-member
   set. Against the live 10 node_types: **7 live types are never candidates**
   (COMPONENT, ENDPOINT, EVENTBRIDGE, S3_BUCKET, SNS_TOPIC, SQS_QUEUE, STATE_MACHINE) and **2 filter
   members match no live node at all** (GOLD_FUNCTION, SILVER_SCRIPT — dead members, reported in-band
   outside the partition since they are not in the source surface). Whether COMPONENT/ENDPOINT
   exclusion is intended-by-design is the inference gate's call; STATE_MACHINE/SNS_TOPIC/SQS_QUEUE
   *look* producer-capable, but materiality is explicitly not this sensor's verdict.
2. **R1 in-band — the declared vocabulary drifted the same way one file over.**
   `trace_graph.py EDGE_TYPES` (whose field comment reads "one of EDGE_TYPES") carries 3 members
   absent from live data (CALLED_BY, IMPORTS, ROUTES) and is missing 8 live types (the
   EVENT/S3/SFN/SNS_INVOKES/_INVOKED_BY families). The BFS being type-blind means the *walk* is
   unaffected — but any consumer trusting the declared set as the source's vocabulary is reading a
   stale enumeration. Same class as finding 1, weaker consequence, same file family.
3. **Shape lesson for L2 (why this sensor exists):** on this DAG shape the residue did **not** live in
   the walk (type-blind ⇒ R1 clean) — it lived in the **type-discriminating submode and the declared
   vocabulary**. A schema-shaped aggregate assuming "residue = unwalked surface" would have scored
   comp-blast perfectly clean and missed both findings. This is concrete input for the L2
   design-constraint ("do not design against fewer than 3 sensors spanning mixed shapes").

## 5 · BR008, exercised deliberately

R2's `address_space: dag_node_type` is not in `KNOWN_ADDRESS_SPACES` — the validator reports `BR008`
(allowed-but-reported, the open-set design). Conformance criterion for this sensor, stated up front:
**`validate()` empty or BR008-only.** R1 lands empty (known space `dag_edge_type`); R2 lands
BR008-only — the open-set mechanism seen working, which the dispatch asked to be noted. If CTO~Z
prefers, `dag_node_type` is a one-line addition to `KNOWN_ADDRESS_SPACES` (a type change, reviewed —
not made by this lane).

## 6 · What this lane did NOT do

No production writes (source reads + two report emissions into this deliverables directory only; the
positive-control fixture lives in session scratch). No commit to `org/tier1_exec/1.0.0_SA_CTO/**`
(CTO~Z commits, established convention). No kuzu DB access at all. No materiality judgments on the
orphans. No `KNOWN_ADDRESS_SPACES` edit. No registration/routability work (explicitly UNBUILT scope in
the levels doc). Sensor code passed `.tools/commit-gate.sh` (py_compile + AST scan + ruff py39) before
delivery.

## 7 · Handoff

- **`1.0.0_SA_CTO~Z`**: commit the 4 files; findings §4.1/§4.2 need an owner ruling (fix the filter /
  declare intent); §5's `dag_node_type` KNOWN_ADDRESS_SPACES question; §4.3 is L2-design input.
- **`3.0.0_SA_CVO~Z`**: every run re-derivable — exact invocations + RCs in §3, fixture recipe in the
  sensor's positive-control section of the session log, and the two mechanism claims are themselves
  re-derived by the sensor at every run (the AST check runs live; the filter is executed live). The
  mention census is reproducible from `_mention_map` in the sensor source.
