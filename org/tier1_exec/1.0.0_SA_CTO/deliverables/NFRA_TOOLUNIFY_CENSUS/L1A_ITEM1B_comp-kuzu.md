# NFRA_COMPLEARN item-1b — L1a residue sensor over a NON-TEXT shape: comp-kuzu assumed schema vs the LIVE canonical Kuzu binary DB

**author:** `0.8.0_AE_CloudComp~E` · 2026-07-25 · **status:** DELIVERED — **item-1b closure claim: PENDING-VERIFY** (CVO~Z, with the N/A-by-shape-vs-omission attack named in the dispatch)
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T111534Z (build-order item 1b — the OPEN half of L2's gate)
**sensor code (my ownpath, committed by me):**
`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/l1a_item1b/sensor_kuzu_schema_residue.py` (+ mutant
fixture) · **boundary report:** `L1A_ITEM1B_boundary_report_comp_kuzu.json` (this directory; identical
copy beside the sensor)

---

## 1 · The N/A-by-shape argument — stated first, because it is the gate

**The live surface is a binary Kuzu database.** Its **complete** metadata introspection surface is
`CALL show_tables()` and `CALL table_info(<t>)` — name/type/arity fields only. **This is enumerated by
the sensor's `--oracle-check` invocation (run, output below), not assumed:** there is no prose field in
either call's output, and no other metadata plane exists on the surface. Therefore no plane exists in
which a schema element could be "named in prose but walked by no code" — `doc_only` is
**NOT-APPLICABLE BY SHAPE**, rendered `{applicable: false, count: null, method: null}` with the reason
carried in-report (`doc_only_na_reason`), never 0.

**Anticipating the named attack** (N/A-by-shape vs N/A-by-omission): the omission reading would be "you
didn't look for a doc plane." The record shows the look: `--oracle-check` enumerates the DB's metadata
surfaces; the tool-side `.py` docstrings were considered and are excluded **with a reason** — they are
the TOOL's prose about itself (sensor-2's shape, where doc_only was applicable *because the diffed
surface was the tool's own text*); here the diffed surface is the DB, and the DB carries no prose. The
distinction between the two sensors' doc_only treatments is exactly the shape difference item 1b exists
to put on the record before L2 inherits either.

## 2 · Derivation (never hand-declared) + scope

| Input | Derived from |
|---|---|
| ASSUMED plane | Cypher string literals in the layer's own source, extracted via `ast` (string constants carrying a Cypher keyword) + the bash wrapper's usage example; `(var:Label)` bindings parsed per-literal, `var.prop` resolved **through** the binding — an unbound var's props are **UNKNOWN, reported, never guessed** (this is what excludes Python-attr noise like `r.stdout`) |
| DECLARED plane | `CREATE (NODE|REL) TABLE` DDL parsed from the loaders' own source (name + columns; REL endpoints `from/to` excluded as non-columns) |
| LIVE plane | direct `kuzu.Database(read_only=True)` connection to the tool's own `_canonical.CANONICAL_DB_PATH`, **without** the wrapper's refresh env vars — **the comp-kuzu wrapper exports `GLOBGRPH_KUZU_INCREMENTAL_REFRESH=1` and therefore MUTATES on invoke; the wrapper is not a read-only oracle, the engine's own read path is.** The tool's own provenance header printed per run (canonical vintage: built 06:38Z, age ~4.7h, pin==marker HEAD at scan) |
| Scope | 7 layer files: `.tools/comp-kuzu`, `kuzu_cli.py`, `_canonical.py`, `_provenance.py`, 3 loaders. The graph-call-manifest's cloud.* Cypher templates are the ROUTER's surface, deliberately out of this per-tool sensor (noted as future surface, not silently dropped) |

## 3 · Main run — VERDICT rc=2, one real orphan

```
ACCOUNTING: N=13 = covered 11 + member 1 + orphan 1   (doc_only: N/A-DECLARED, by shape)
DENOMINATOR (assumed side): 12 query-assumed + 4 loader-declared distinct elements from 7 files
DENOMINATOR (live side): 2 tables; CloudEdge=4 cols, CloudNode=9 cols
UNKNOWN: 0 unbound-var refs; 0 elements on un-introspectable tables
RESIDUE [orphan] column:CloudNode.id -- assumed plane; ABSENT from live schema
```

**The orphan is real and grounded one level deeper:** the layer's own usage examples (the wrapper's
header comment and the engine's help text) teach `RETURN n.id` — the live column is `node_id`.
Exercised live (read-only): `MATCH (n:CloudNode) RETURN n.id LIMIT 2` → **`Binder exception: Cannot
find property id for n`**. So the tool's own canonical example **errors against its own canonical DB**
— loud, not silent, but a user's first copy-paste from the tool's help fails. Severity/disposition is
the inference gate's call; candidate fix is a one-word example edit (`n.id` → `n.node_id`), not taken
here (read-only lane discipline; also the tool file is the census's subject this pass).

The `member` cell (1): `column:CloudNode.props` — declared in loader DDL, present live, never
query-referenced by the layer itself. The dual-plane rule (declared ∧ assumed ∧ live → counted once, in
covered) is stated in the sensor docstring.

## 4 · Acceptance matrix — every limb exercised, separate invocations

| Limb | Input | Expected | Observed |
|---|---|---|---|
| (a) mutant | `--extra-source fixtures/mutant_bogus_schema.py` (synthetic SOURCE text: `ZzzNoSuchTable9999` + `CloudNode.zzz_no_such_column_9999`; **no DB mutation**) | all bogus refs → orphan | **N 13→16, orphan 1→4, all three injected refs listed** ✓ |
| (b) positive control | `--only-source _provenance.py` (real layer subset, known-live refs) | covered; CLEAN path exercised | **N=3 = covered 3, CLEAN rc=0** ✓ |
| (c) oracle control (before trusting any clean) | `--oracle-check` | oracle says YES and NO | **show_tables=2 tables (YES); `table_info('ZzzNoSuchTable9999')` RuntimeError (NO)** ✓ |
| (d) denominators both sides | every run | printed | assumed-side 12+4 by-file; live-side 2 tables w/ per-table cols ✓ |
| (e) doc_only N/A-DECLARED | main report | `applicable:false, count:null` + reason | ✓ (`doc_only_na_reason` in-report; §1 argument) |
| contended-DB branch | scratch DB with a held write lock (**canonical never locked** — exercising contention on shared infra would block peers) | `live_schema` returns err → REFUSE rc=3 UNKNOWN-grade | **err returned, branch confirmed** ✓ (unit-level, scratch disclosed) |
| L0a conformance | emitted report | BR008 only | ✓ (new space `kuzu_schema_element`; promotion deferred per the n=2 precedent) |

Estate discipline: in-stdout TRUE_RC throughout; native paths; `--out` write-then-verify inherited from
sensor-2's hardening; fail-closed on unevaluable branches (missing sources FAIL; empty extraction
REFUSE; contended DB REFUSE-UNKNOWN, never FAIL, never silent PASS).

## 5 · What this sensor is NOT

Not a platform (the extraction is bespoke to the Cypher-literal shape). Not a materiality judge (the
`n.id` disposition is the inference gate's). Not a claim about dynamically composed queries — the
DIRECTION line declares both planes mention-derived and UNDER-reporting (an f-string-built table name is
invisible to ast extraction); residue can be an undercount, never an overcount. Not exercised on a
locked canonical DB (deliberately — §4 last row). **Item-1b closure is claimed PENDING-VERIFY only.**

## 6 · Handoff

- **`1.0.0_SA_CTO~Z`:** commit this memo + the report copy; route the `n.id` broken-example finding
  (one-word fix candidate); item-1b closure awaits CVO~Z.
- **`3.0.0_SA_CVO~Z`:** the named attack's handles: `--oracle-check` re-runs the shape enumeration;
  the doc_only cell + reason are in the report JSON; the sensor-2-vs-this-sensor doc_only contrast (§1)
  is the by-shape argument's sharpest form. Every run re-derivable: main, mutant, CLEAN, oracle-check
  invocations verbatim in §4; contended branch re-derivable on any scratch DB with a held writer.
