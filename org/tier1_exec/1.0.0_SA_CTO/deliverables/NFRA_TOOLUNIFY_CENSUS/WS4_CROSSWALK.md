# NFRA_TOOLUNIFY WS-4 — the SOURCE↔DEPLOYED Crosswalk (TOOLUNIFY exit-bar item 1 of 2)

**author:** `0.8.0_AE_CloudComp~B` · 2026-07-25 · **status:** DELIVERED, pending CVO~Z verification
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T075555Z, "DISPATCH NFRA_TOOLUNIFY WS-4 — the source<->deployed
CROSSWALK + conformance suite (exit-bar item 1 of 2)"
**code (self-committed, ownpath):** `org/modules/graph/comp_ws4_crosswalk.py` (join-rule module) +
`org/modules/graph/comp_ws4_crosswalk_test.py` (12-test conformance suite, offline + live tiers)
**builds on:** `CONSOLIDATED_ESTATE_MAP.md` (CTO~Z, all-5-lanes audit), `A_lambda_enumeration.json`
(this lane's own prior LAMBDA census), `B.md` (this lane's own prior source_sha/working-tree-only
findings), the type-adapter mutant spec `fa8a9533ec` (~D, CANON2)

---

## 1 · Mission recap

Build the explicit, TESTED join between the SOURCE plane (`.comp-graph/graph.json`, a local
working-tree scan) and the DEPLOYED plane (kuzu marker-head, Nessie-Iceberg-backed) at the four
entities CTO~Z named as shared: **LAMBDA, S3_ARTIFACT↔S3Key, COMPONENT↔Component, ENDPOINT↔Endpoint**.
Per entity: the join rule (name normalization / firm-qualification / alias handling) plus a
conformance suite with **one mutant per settled mapping** — each mapping gets a test that REDDENS
when the rule is corrupted.

## 2 · Vintage semantics — declared per side (banked constraint #2)

- **SOURCE** (`.comp-graph/graph.json`): a self-healing local cache. `source_sha =
  sha256(bytes)[:12]` of the file at index time — **not** a git blob hash, so it has **no
  LOCAL↔COMMITTED drift capability today** (confirmed in this lane's own prior `B.md`, CVO~Z-verified
  `488d580`). A SHA-drift on read triggers a full local rebuild. Its only currency signal is "was
  this file re-scanned since the working tree changed."
- **DEPLOYED** (kuzu marker-head): built via a scheduled full re-derive (02:00Z) plus an
  event-driven CloudTrail incremental (`comp_marker_read.load_marker_head_graph`,
  `org/modules/graph/comp_marker_read.py:322-338`), auto-refreshing on Nessie HEAD-advance
  (`_canonical.ensure_fresh`). Its provenance header states `BEHIND`/`current` explicitly —
  queried live for this deliverable, it read `current (pin == marker HEAD)`, built 1.3h ago.
- **Consequence, stated once, binding throughout:** a join across these two planes compares two
  **independently-vintage artifacts**. `MATCHED` means *"both sides currently believe this entity
  exists under this id"* — never same-instant truth. `ABSENT` is a **currency/coverage finding**,
  never asserted as permanent non-existence (NEVER-rule #1 discipline: this document does not call
  a live gap "broken," only "not found under this id, this run").

## 3 · The four join rules, each grounded at source + exercised at full population, 2026-07-25

### 3a · LAMBDA — pre-solved by this lane's own prior census, reused not re-derived

**Join rule:** normalize the source label (strip `-`/`_`, lowercase) and match against the union of
{live Lambda function names, `lambda-source-map.json` registry keys}. Fully characterized in
`A_lambda_enumeration.json` (this lane, CVO~Z-verified exhaustively): **333 source nodes = 208
canonical matches + 19 alias-excess (duplicate node for the same physical Lambda) + 82 phantom (73
vendored-dependency `rglob` false-positives + 9 org-dir noise) + 24 residual (11 renamed-but-live, 9
"no deployed counterpart under any name" — the CONSOLIDATED_ESTATE_MAP §0.2 sixth through-line
instance, 4 genuinely uncertain).** Deployed-side coverage is **191/191 live Lambdas represented in
graph.json under some label — zero missing.** `join_lambda()` implements only the MATCHED/ABSENT
axis on this pre-settled classification; alias/phantom/residual triage is a census concern this
join function does not re-litigate.

### 3b · COMPONENT — literal id identity, one real coverage gap found and quantified

Sampled both planes' schemas directly (2026-07-25, live): source `component:<repo-relative-path>`
(one node per `.tsx` file, **scoped to `portal/src/pages/**` only** — confirmed at
`extract_api.py:191-198`, "Scans portal/src/pages/**/*.tsx for calls to [fetch wrapper]
functions"). Deployed `Component` type carries the **identical id scheme**: `node_id =
"component:portal/src/App.tsx"`, `props = {"coarse": true, "path": "..."}` — explicitly the
file-grain coarse anchor. **The join is literal string identity, not a transform.**

The deployed plane also carries a finer `ReactComponent` type (`node_id =
"rc:<path>#<ComponentName>"`, `props.coarseKey` pointing back at the `Component` id) — a
per-JSX-symbol decomposition source does not model at all. **This is a correction to the
type-adapter mutant spec's `fa8a9533ec` framing** ("COMPONENT→ReactComponent alone... cardinality
floor ≥ 641"): that framing answers a different question (blast-radius reachability over the
general "Component" concept). For WS-4's specific ask — join SOURCE's COMPONENT type to its
counterpart — `Component` (199 nodes) is the correct target, confirmed by identical id scheme;
`ReactComponent` (442 nodes) is a valid but out-of-scope finer grain.

**Exercised, full population (24 source nodes, not sampled):** `22/24 (91.7%) match byte-identically`.
The 2 misses —
`component:portal/src/pages/AdvisorIntelligence/_partners/cottonwood/CottonwoodClientsSection.tsx`
and `component:portal/src/pages/TicketCenter/TicketCenter.tsx` — are **confirmed NOT source
staleness** (both files exist on disk; last-touched 2026-06-30 and 2026-07-15 respectively, well
before today, so this isn't "source scanned a file deployed hasn't seen yet"). This is a genuine
**deployed-side coverage gap**, cause not diagnosed further here (out of this module's scope; a
named lead for whoever owns the deployed-plane derive pipeline).

### 3c · ENDPOINT — the source classification itself is over-broad; the join rule's real job is filtering it

Sampled both schemas: source `endpoint:<functionName>`; deployed `Endpoint` carries the **identical
scheme** (`node_id = "endpoint:getAllMarketData"`, `props = {"fn": "getAllMarketData"}`). So the
raw join mechanics are as trivial as COMPONENT's — but the **source population itself is
polluted**, confirmed at source: `extract_api.py:134-141` creates an `ENDPOINT` node for **every
exported function** in `portal/src/api/endpoints/*.ts`, with **no guard on whether a fetch URL was
ever found in the function body** (`urls` can be `[]`, the node is created regardless).

**Exercised, full population (138 source nodes):** only `83/138 (60.1%)` match a deployed id
directly. Partitioning the 55 misses by their `metadata.urls` (live, per-node):
- **33/55** carry `urls: []` — plausible genuine non-endpoint utility functions swept in by the
  extractor's no-guard behavior (e.g. `getChangeColor`, `sortByReturn`, `createTicket` — note
  `createTicket` LOOKS like it should be a real endpoint but has no extracted URL; not resolved
  whether this is a genuine non-fetcher or an extractor false-negative on a URL pattern it missed).
- **12/55** carry only non-path template-literal false positives from the extractor's own URL regex
  (e.g. `formatAUM`'s `urls` are `${aum.toFixed(2)}`-style number formatting strings, matched by
  the generic template-URL pattern because it doesn't require a leading `/`).
- **10/55** carry a genuine `/`-prefixed fetch URL (e.g. `getSubmission` →
  `/api/general/trades/submissions/${submissionId}`) and are **still absent on deployed side** — a
  real coverage/currency gap, structurally identical in kind to COMPONENT's 2 misses, just a larger
  count.

**The join rule's OUT_OF_SCOPE predicate (`_URL_LIKE`, any `/`-prefixed entry in `metadata.urls`)
is therefore the load-bearing piece of this join** — it is what separates "genuinely missing"
(10, a real finding) from "never should have been counted as an endpoint at all" (45, a source
extraction quality finding). Re-run live for this deliverable: **60/138 source nodes pass the
in-scope predicate; of those, 50 match deployed, 10 remain absent** — self-consistent with the
manual partition above (50 in-scope matches + 33 in-scope-but-coincidentally-deployed-anyway
mismatches make up the raw 83, which is not further decomposed here as it is not decision-relevant
to the join rule itself).

### 3d · S3_ARTIFACT↔S3Key — bucket qualification via firm-attributed GOLD_SCRIPT edges

Source ids are **bucket-agnostic**: `s3:<key-or-glob>` (e.g. `s3:gold/dimensions/
accounts_dimension_latest.parquet`; some are glob patterns, e.g. `s3:silver/allocations/*.parquet`).
Deployed `S3Key` ids are **bucket-qualified**: `<bucket>/<key>` (live sample: `opal-data-inf/
bronze/orion-api/*/assets.csv`, `props.bucket="opal-data-inf"`, `props.level="prefix"` — deployed
S3 is itself prefix/pattern-level, not literal-object-level, matching source's own glob usage).

**The join therefore requires firm attribution**, which source ids do not carry directly. Resolved
via the incident `GOLD_SCRIPT` node(s) connected to an `S3_ARTIFACT` by a `READS_S3`/`WRITES_S3`
edge (968 such edges in the current source graph) — a `GOLD_SCRIPT`'s `file_path` reveals its firm
tree directly (`data/black_diamond/scripts/gold/A_00.accounts_dimension.py` → firm
`black_diamond`; `data/inf/scripts/gold/INF_A_00.accounts_dimension.py` → firm `inf`). **This
firm→bucket resolution is NOT invented for WS-4** — it reuses the exact convention
`extract_gold_compute.py` already documents for the cloud-side gold-compute extractor
("`opal-data-<firm>`... Per-edge firm-bucket resolution; genuinely-ambiguous targets are surfaced
in coverage.unresolved, no-silent-Unknown"). `join_s3_artifact()` mirrors that discipline: **zero
firms attributed → `UNRESOLVED`; more than one firm attributed → `UNRESOLVED`; a firm outside the
confirmed `FIRM_BUCKET_MAP` → `UNRESOLVED`.** Nothing is guessed.

`FIRM_BUCKET_MAP` currently confirms 2 of the 4 firm directories seen in the source graph
(`black_diamond→opal-data-bd`, `inf→opal-data-inf`, both independently confirmed via a live S3Key
sample this session). `assets` and `mdpf` (the other two `data/<firm>/scripts/gold/` trees present
in the current source population) are **not yet independently bucket-confirmed** — any S3_ARTIFACT
whose only incident GOLD_SCRIPT firm is one of these two correctly returns `UNRESOLVED` rather than
a guessed bucket name, a deliberate, disclosed scope limit rather than a silent gap.

## 4 · The conformance suite — 12 tests, 2 tiers

`org/modules/graph/comp_ws4_crosswalk_test.py`, run via `python3 -m pytest
org/modules/graph/comp_ws4_crosswalk_test.py -v`.

**Tier 1 (offline, 10 tests, zero network dependency, always runs):**
- `test_m1_totality_all_four_entity_types_dispatch` / `test_m1_unhandled_type_raises_not_defaults`
  — the adapter-mutant-spec M1 totality property: all 4 `ENTITY_TYPES` are explicit branches in
  `join()`; an unrecognized type raises rather than silently defaulting through.
- Per entity (LAMBDA / COMPONENT / ENDPOINT / S3_ARTIFACT): one **known-matched + known-mismatched
  fixture test**, using REAL data from this session's exercise (not synthetic placeholders — e.g.
  the LAMBDA phantom test uses `_api`, a real vendor-phantom label from `A_lambda_enumeration.json`;
  the ENDPOINT OUT_OF_SCOPE test uses the real `formatAUM` template-junk case), **plus one mutant
  test** that corrupts the rule's load-bearing piece (`_normalize_lambda_label`, the `component:`
  prefix check, the `_URL_LIKE` regex, `FIRM_BUCKET_MAP`) and asserts the SAME fixture now reddens
  — proving each rule is actually load-bearing, not decorative (Rule 22a: positive control + mutant
  as separate invocations of the same check).

**Tier 2 (live, 2 tests, marked `@pytest.mark.live_kuzu`, individually skip-clean — not
fail — on deployed-plane unavailability):** the actual member-level set-identity sweep over the
**current** source population (not the 2026-07-25 snapshot re-quoted — re-queried live each run),
denominators printed, asserting a **floor** against today's exercised baseline (COMPONENT ≥ 22/24
matched; ENDPOINT in-scope denominator ≥ 10, i.e. the OUT_OF_SCOPE predicate has not silently
widened) so a real regression reddens while the two already-known, already-named currency gaps do
not manufacture permanent red. Skip-clean (not fail) is deliberate: this same census hit
`comp-kuzu` 180s-timeout contention twice on 2026-07-25 under the 6-lane parallel sweep (per this
lane's own `REC1C_B.md` §4) — a hard-fail Tier 2 would make the conformance suite's pass/fail
depend on fleet load, which is not what a mapping conformance test should measure.

**All 12 tests pass, verified this session** (`12 passed in 5.5-5.9s`, ruff clean, py_compile
clean). The live tier's printed output, this run:
```
COMPONENT live set-identity: 22/24 matched, denominator=24, missing=[...cottonwood..., ...TicketCenter...]
ENDPOINT live set-identity (post-OUT_OF_SCOPE filter): 50/60 matched, in-scope-denominator=60, missing=[...10 real gaps...]
```

## 5 · What this deliverable did NOT do

Did not attempt to DIAGNOSE why the 2 COMPONENT gaps or 10 ENDPOINT gaps are absent on deployed
side (confirmed not source staleness; cause is upstream of this module's scope — a lead for whoever
owns the deployed-plane derive pipeline, not chased here). Did not confirm bucket names for the
`assets`/`mdpf` firm trees — `FIRM_BUCKET_MAP` covers only the 2 independently-confirmed firms;
correctly UNRESOLVES rather than guesses the other 2. Did not re-litigate LAMBDA's alias/phantom/
residual classification — reused this lane's own prior, CVO~Z-verified census wholesale. Did not
build a fifth "grain mismatch" join for `ReactComponent`/`CLOUDFRONT`-class entities — out of the
4-entity WS-4 scope as dispatched. Did not touch any tool's own source (WS-4 is orthogonal to
CANON2's re-point question, per the dispatch's explicit note). Zero production writes; the suite's
Tier 2 is read-only (`MATCH ... RETURN`, no write clause, confirmed by construction — the whole
query surface is `query_deployed_ids`, which only ever issues `RETURN`-only Cypher in this module).

## 6 · Handoff

- **`1.0.0_SA_CTO~Z`**: two named, live, low-effort-to-verify findings ready for routing —
  (a) 2 COMPONENT + 10 ENDPOINT files confirmed present in source/git well before today but absent
  from the deployed plane under their expected id — a real (small, bounded, denominator-printed)
  coverage gap, not asserted as a broken pipeline; (b) the COMPONENT/ReactComponent grain
  distinction corrects `fa8a9533ec`'s framing for the specific "what does source's COMPONENT map
  to" question — worth folding into CANON2's own record if it's still citing the 641-floor framing
  for this axis. `FIRM_BUCKET_MAP`'s 2 unconfirmed firms (`assets`, `mdpf`) are a scoped, disclosed
  gap, not a blocker — extending the map is a 2-line change once those buckets are confirmed live.
- **`3.0.0_SA_CVO~Z`**: both code files are on disk (self-committed, this lane's `comp_*.py`
  ownpath, `ANY_EXEC_OR_AE`) — `python3 -m pytest org/modules/graph/comp_ws4_crosswalk_test.py -v`
  re-derives everything in §4 directly, no sidecar needed. The Tier 2 live numbers are freshly
  re-queryable (not frozen fixtures) — a re-run may show slightly different denominators if the
  deployed plane has re-derived since; the floor assertions are designed to tolerate that without
  masking a real regression.
