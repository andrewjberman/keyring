# NFRA_GRAPHUNI.P0-A — STORAGE-STRATUM read-only AUDIT + the STORAGE DENOMINATOR SLICE

**TO:** NFRA_GRAPHUNI.P0-A (org/projects/NFRA_GRAPHUNI/task_orders/NFRA_GRAPHUNI.P0-A.storage-stratum-audit.md)
**Author:** 0.8.0_AE_CloudComp~A (STORAGE-stratum populator, GRAPHDEPTH by-stratum fleet — CTO-concurred 212036Z)
**Date:** 2026-06-30
**Status:** DELIVERED — read-only audit complete, ZERO graph mutation. RAVC2 -> COO~B, cc CTO + ~C + ~D.
**Scope guard honored:** AUDIT + denominator slice ONLY. No derive, no node/edge creation, no cache mutation. Population (P1) rides ~D's CVO-fixture-gated build.
**Conformed to:** ~C's `grain_contract` (org/modules/graph/comp-coverage-map.yaml) — granularity = declared `level`, no re-type-by-depth; ~C governs, I populate to it.

---

## 0. Grounding (the two sides of the storage diff — independently ground-truthed, not relayed)

| Side | Artifact | Vintage / head | Storage census |
|---|---|---|---|
| **Unified graph (target)** | Kuzu `kuzu_nessie_db` (Nessie-backed, marker-headed) | HEAD **current** (pin == marker HEAD); built 2026-06-30T19:34:59Z (age ~1.9h); nodes snapshot 1832939377093282234 | **S3_BUCKET 35** (bucket-granular only); **0 S3Key / 0 object** nodes; **0 READS_S3 / 0 WRITES_S3** edges |
| **comp-blast/trace cache** | `.comp-graph/graph.json` (`TraceGraph`) | built 2026-06-30T16:44Z | **S3_ARTIFACT 288** (key-level, bucketLESS); READS_S3 496 / WRITES_S3 407 (the cross-stratum coupling) |
| **comp-platinum DAG cache** | `.comp-graph/platinum.dag.{bd,inf,cot}.cache` (pickle PipelineDAG) | bd/routing 2026-06-30T14:08; **inf STALE 2026-06-12T16:37**; cot 2026-06-12 | **bd S3Key 103** (21 prefix / 82 object); **inf S3Key 0 (STALE/empty — F2)**; **cot S3Key 96** (21 prefix / 75 object) |

Provenance header read on every comp-kuzu call (Rule 20): **current**, pin == marker HEAD — authoritative baseline, not a stale/scratch vintage. **Zero-mutation evidence:** every comp-kuzu call was `MATCH … RETURN` (no CREATE/MERGE/SET/DELETE); graph.json read via `json.load` (read-mode); platinum caches via `pickle.load` (read-mode); the served-key check via `aws s3api list-object-versions` (read). No graph or cache byte changed.

---

## 1. Baseline — what the unified Kuzu graph HOLDS for STORAGE at the marker head

```
node_type         count          edge_type   count
----------------  -----          ---------   -----
S3_BUCKET           35           CONTAINS    5411   <- ms-folder/portal containment, NOT storage (0 S3Key to contain)
S3_BUCKET_POLICY     9           OWNED_BY    5410   <- ms-file/portal, NOT storage (0 S3Key to own)
KMS_KEY              8           READS        646   <- portal-field + bucket grain, NOT gold key-IO
                                 WRITES       543   <- portal-field + bucket grain
(NO S3Key / NO S3_ARTIFACT / NO S3_OBJECT node_type)   (NO READS_S3 / NO WRITES_S3 edge_type)
```

**Decisive storage observations (the gap mechanism):**
- S3 is **bucket-granular only** — the 35 `S3_BUCKET` nodes carry the bucket name; there is **no key-level and no object-level storage node** (`S3Key` / `S3_ARTIFACT` queries return 0). The storage ladder is **depth-flat at the bucket** today.
- The 5410 `OWNED_BY` + 5411 `CONTAINS` edges are **NOT storage** — they are MS_FILE→MS_FOLDER + portal containment. There are **zero storage `OWNED_BY` (S3Key→S3_BUCKET)** edges because there are no S3Key nodes to own.
- **Zero `READS_S3` / `WRITES_S3` edges** at head — the gold key-level IO (the compute→storage coupling) is entirely absent from the unified graph (it lives only in the TraceGraph cache). The chain dead-ends at the bucket.

---

## 2. Cache side — what the finer storage grain HOLDS (the derive source)

- **TraceGraph (`graph.json`)**: `S3_ARTIFACT` **288** (key-level). Tier breakdown (top key segment): **gold 139, platinum 37, silver 23, bronze 11**, json/served 39, + raw/ingestion tail (security-reports 7, seeking-alpha 5, orion 3, schwab 3, smartx/macro/sentiment/benchmarks …). The artifacts span the **whole tier ladder**, confirming Amendment-8 (storage mirrors ingestion→bronze→silver→gold→platinum, not gold-only).
  - Node shape: `{id:"s3:gold/dimensions/accounts_dimension_latest.parquet", label:"<key path>", file_path:"", …}` — **id/label carry the KEY PATH ONLY, no bucket** (see F1).
  - Coupling edges: **READS_S3 496 + WRITES_S3 407 = 903** gold-fn→artifact edges (these point AT the S3Key nodes ~A will land — the cross-stratum seam).
- **comp-platinum PipelineDAG**: per-firm `S3Key{constant_name, s3_path, is_prefix, is_function}` — **bd 103 (21 prefix / 82 object)**, **cot 96 (21 prefix / 75 object)**, **inf 0 (STALE cache, F2)**. The per-firm DAG gives the `is_prefix` flag (the object-vs-prefix `level`) and per-firm bucket attribution.

**Bucket-attribution feasibility (the OWNED_BY derivation, ground-truthed via producer edges):**
- 146/288 artifacts have ≥1 in-graph WRITER (gold-fn whose `file_path` encodes the firm→bucket): **black_diamond 90, inf 32, black_diamond+inf 23, mdpf 1**.
- **23 artifacts are written by BOTH bd and inf** → bucket-ambiguous even WITH a producer (same key path is a distinct object in each firm's bucket — they must split into per-bucket S3Key instances).
- **142/288 are read-only inputs** (no in-graph producer) — produced by silver/bronze/ingestion scripts absent from the ~99%-gold-only TraceGraph (Amendment-8) or landed by EC2/external; bucket recovered from reader-firm / key-prefix (F5).

---

## 3. THE STORAGE DENOMINATOR SLICE (= ~A's slice of the enumerated denominator; no-silent-caps covered-vs-expected)

Conformed to `grain_contract`: **strata** `[resource, compute, object]`; **node_grain_ladder** ONE `CONTAINS` relation, levels `[estate, surface, container, file, object, function, field]`.

### 3a. STORAGE NODES (the bucket→key→object ladder)
| Node | Stratum | Level (ladder) | In Kuzu | EXPECTED (denominator) | Derive source |
|---|---|---|---|---|---|
| **S3_BUCKET** | resource | `container` | **35** | 35 (exists; the storage root) | Kuzu (already populated) |
| **S3Key** | object | `object` (= `s3key`†) | **0** | **≥288 bucket-qualified** (288 bucketless TraceGraph artifacts; HIGHER once the 23 bd+inf-ambiguous split per-bucket). Per-firm DAG cross-check: bd 103 + cot 96 + **inf (rebuild — cache stale, F2)** | TraceGraph `S3_ARTIFACT` ∪ platinum `S3Key` — **derive ONCE** (CTO ruling 2: same underlying object) |
| **S3 object/version** | object | `object` (finer) | 0 | **BOUNDED-MATERIALIZATION — lazy / on-demand, NOT eager** (CTO ruling 3 / boundary 4b: object-version fan-out is combinatorial). The eager ladder bottoms at KEY. | n/a (lazy) |

† **F4 level-token mismatch:** `node_grain_ladder` uses `object` for the key level, but the `OWNED_BY` edge_type declares `levels:[s3key, ddb-item]`. Storage conceptually wants bucket ⊃ key ⊃ object-version (3 levels); the ladder supplies container + object (2). Coordination point for ~C (below).

### 3b. STORAGE EDGE-TYPES × LEVEL (intra-storage + the cross-stratum coupling)
| edge_type | relation | level(s) | from → to | stratum span | producer (per contract) | In Kuzu | EXPECTED | /seams parties |
|---|---|---|---|---|---|---|---|---|
| **OWNED_BY** | owned_by | `s3key` | S3Key → S3_BUCKET | object → resource (**storage drilldown seam**) | `graphuni-infra` ⚠ **F3** | 0 | **≥288** (1 per bucket-qualified key) | **~A + ~C** (single-stratum, 2-party) |
| **CONTAINS** | contains | `container`→`object` | S3_BUCKET → S3Key | resource → object (inverse drilldown) | `graphuni-gold`/infra | 0 (storage) | **≥288** (inverse of OWNED_BY) | **~A + ~C** (2-party) |
| **READS_S3** | reads_s3 | `object`, `prefix` | gold-fn → S3Key | **compute → object (CROSS-STRATUM)** | `graphuni-gold` (**~D**) | 0 | **496** | **~A + ~D + ~C** (TRI-party, bucket↔key) |
| **WRITES_S3** | writes_s3 | `object`, `prefix` | gold-fn → S3Key | **compute → object (CROSS-STRATUM)** | `graphuni-gold` (**~D**) | 0 | **407** | **~A + ~D + ~C** (TRI-party) |

`prefix` vs `object` `level` split (from platinum `is_prefix`): ~21 prefix-keys per firm, the remainder object-keys. The `level` attribute on each S3Key + its READS_S3/WRITES_S3 edge carries object-vs-prefix (Amendment-2: SAME type, depth on `level`).

### 3c. CROSS-STRATUM ROLLUP (storage participates in the existential rollup — 4-party)
The coarse `EC2/LAMBDA READS/WRITES S3_BUCKET` (resource→resource, exists at head) **⟸ existential-rolls-up-from** the fine `PipelineFunction -READS_S3-> S3Key -OWNED_BY-> S3_BUCKET`. Per `grain_contract.rollup` (existential-aggregation, `rollup_via:[RUNS, CONTAINS, OWNED_BY]`, defects UNSUPPORTED + COARSE-INCOMPLETE). **My `OWNED_BY` (S3Key→S3_BUCKET) is the storage leg of this rollup chain** → the rollup `EC2 READS S3_BUCKET ⟸ fn READS_S3 S3Key OWNED_BY bucket` is a **~B + ~D + ~A + ~C FOUR-party** seam (DECOMP-MAP N-party rule). The check is single-sourced via canonical `rollup_defects()` (28fac26f2); only the sign-off is N-party.

**Categorical coverage attestation (no-silent-caps):** EVERY storage level (container/object [+bounded object-version]), EVERY storage edge_type (OWNED_BY, CONTAINS), the compute→storage coupling (READS_S3, WRITES_S3), and the storage rollup leg are enumerated above. Covered-vs-expected: storage currently **1/3 levels** populated (bucket only), **0/2 storage edge_types** + **0/2 coupling edge_types** populated.

---

## 4. THE bucket↔key COUPLING (the cross-stratum seam I co-sign with ~D + ~C) — AC3

**F1 (load-bearing).** ~D's gold `READS_S3`/`WRITES_S3` (903 edges) and the TraceGraph `S3_ARTIFACT` (288) are keyed by a **bucketless key path** → the same path (e.g. `gold/dimensions/accounts_dimension_latest.parquet`) **collapses across firm buckets** (23 artifacts written by both bd AND inf — i.e. distinct objects in opal-data-bd vs opal-data-inf, one bucketless node). Therefore:
- ~A's **S3Key nodes MUST be (bucket, key)-qualified** — the bucket is the disambiguator. ~A cannot bucket-qualify a key without **~D's producer-script firm** (the gold-fn `file_path` → firm → `opal-data-{firm}` bucket); ~D's `READS_S3`/`WRITES_S3` cannot resolve to a UNIQUE S3Key endpoint without **~A's bucket-qualified node**. **Co-derived, co-signed** (the seam is the bucket-qualification handshake).
- For the **142 read-only inputs** (no producer in graph, F5), bucket comes from the reader's firm / key-prefix — a Phase-B enrichment as silver/bronze/ingestion producers land (Amendment-8); for gold-tier-first Phase A, attribute via reader-firm.
- **OWNED_BY is the materialization of this seam:** `S3Key(bucket,key) -OWNED_BY-> S3_BUCKET(bucket)`. The 23 ambiguous collapses become **N distinct (bucket,key) S3Key nodes**, each OWNED_BY its own bucket — so the true expected S3Key count is **> 288** once bucket-qualified.

---

## 5. AUDIT FINDINGS / coordination points (smell pass)

- **F1 — bucketless-collapse (above):** the bucket↔key qualification is the gating coupling; resolved only by the ~A+~D co-derive. *Primary seam.*
- **F2 — inf platinum DAG cache STALE/empty:** `platinum.dag.inf.cache` is Jun-12 with **0 s3_keys**. The inf storage-key denominator must come from the **06-30 rebuilt TraceGraph** (which DOES hold inf artifacts among the 288) or a fresh inf DAG build — **NOT** the stale cache. *Route to ~D (cache rebuild) + COO~B; do not let a stale-cache 0 understate the inf storage denominator.*
- **F3 — `producer` label drift in grain_contract:** `OWNED_BY` declares `producer: graphuni-infra`, but the fleet partition (DECOMP-MAP) assigns storage `OWNED_BY/CONTAINS` to **~A (storage)**, distinct from ~B's infra `RUNS`. Per ~D's seam pre-flight finding 3, `producer` scopes the seam's registry-orphan check → a wrong producer falsely demands the wrong lane populate it. *~C to split: storage `OWNED_BY`/`CONTAINS` producer = `graphuni-storage` (~A) vs infra `RUNS` producer = `graphuni-infra` (~B).*
- **F4 — node-ladder vs edge level-token mismatch:** ladder key-level = `object`; `OWNED_BY` level = `s3key`. Storage wants bucket⊃key⊃object-version. *~C to reconcile: canonicalize key as `object` (bucket=`container`, object-version=bounded beneath), or mint a distinct `key` ladder level. The `level` token must be ONE name across node ladder + edge_type.*
- **F5 — 142/288 read-only inputs lack an in-graph producer:** these are silver/bronze/ingestion/EC2-landed inputs (the ~99%-gold-only TraceGraph, Amendment-8). Their WRITER edges + bucket are net-new Phase-B lineage; gold-tier-first Phase A attributes bucket via reader-firm. *Flag for ~D Phase-B compute-enrich; not a Phase-A blocker.*

---

## 6. Acceptance-criteria attestation
- **AC1 — STORAGE denominator slice:** §3 — every storage stratum/edge_type/level enumerated (nodes §3a, edges §3b, rollup §3c), no-silent-caps covered-vs-expected (1/3 levels, 0/4 storage+coupling edge_types populated). Composes into COO~B's full enumerated denominator for the /seams.
- **AC2 — ZERO graph mutation, evidenced:** §0 — all comp-kuzu calls `MATCH…RETURN`; caches `json.load`/`pickle.load` (read-mode); `s3api list-object-versions` (read). graph.json + platinum caches byte-unchanged.
- **AC3 — bucket↔key coupling identified:** §4 — the ~A+~D+~C cross-stratum seam (bucket-qualification handshake; OWNED_BY is its materialization) + the ~B+~D+~A+~C 4-party rollup leg (§3c).
- **AC4 — RAVC2:** to COO~B, cc CTO + ~C + ~D. Self-committed to org/projects/NFRA_GRAPHUNI/ (grant live; pathspec EXCLUDES task_orders/). Compiler-tools reproduction in the session log.

## 7. Residual unknowns / for the /seams + governance
1. **True bucket-qualified S3Key count** — > 288 (the 23 bd+inf ambiguous split per-bucket; inf rebuild pending F2). Exact count lands when ~D's producer-firm attribution + the inf cache rebuild resolve. *The denominator is the EXPECTED SET (every (bucket,key) the pipeline IO references); the exact cardinality firms up at co-derive.*
2. **F3/F4 grain_contract reconciliations** — producer-label split + level-token unification — are ~C governor calls; flagged, not assumed.
3. **object-version level** — confirmed bounded-materialization (lazy); no eager denominator. The /seams asserts coverage of bucket+key levels; object-version is out of eager scope by ruling 3.
