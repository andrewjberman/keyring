# NFRA_TOOLUNIFY — CONSOLIDATED ESTATE MAP (audit complete, all 5 lanes CVO~Z-verified)

**author:** `1.0.0_SA_CTO~Z` · 2026-07-25 · **status:** AUDIT COMPLETE — decision input for "how we handle it"
**verification:** `3.0.0_SA_CVO~Z` re-derived every load-bearing claim at source; all 5 lanes PASS.
**lane deliverables (committed):** base @d4f80d742e · A @7df3559a26 · B @488d580 · C @163ec2ce5 · D @7490d459f7
**plan of record:** `docs/briefs/NFRA_TOOLUNIFY_ESTATE_CENSUS_PLAN_20260724.md` @6fd377d78

---

## 0 · The two findings that outrank the rest

**(1) THE STORE IS 93% OUTSIDE THE ONTOLOGY IT NOMINALLY HAS.** Of the federated cloud truth's 20,403
nodes, only **6.7% carry a type name matching its own governing vocabulary** (the GLOBGRPH PRD's 41 declared
classes). CVO~Z-verified decomposition:

| Bucket | Types | Nodes | Share | Remedy |
|---|---|---|---|---|
| Exact-name match to declared vocabulary | 14 | 1,372 | 6.7% | — |
| Declared concept, different name (vocab drift) | 13 | 1,384 | 6.8% | **alias table — hours** |
| Genuinely undeclared | 31 | 17,647 | 86.5% | **ontology must be authored** |

**It is a GRAIN gap, not neglect.** The PRD describes *resource-grain* topology (Lambda, S3 key, EventBridge).
The store has since grown a *symbol-grain* code-semantic plane it was never written for (`Field` 4969,
`JSXElement` 2205, `PipelineFunction` 1201, `TypeDecl` 807…) plus M365 (`MS_FILE` 4618, `MS_FOLDER` 1034).
Counter-control (CVO~Z, against its own framing): `LOG_GROUP` 233 is a plain *resource* type and is also
undeclared — so bucket C is not purely the semantic plane.

**(2) THE THROUGH-LINE — "a control that works and is inaudible reads exactly like health."** SIX instances of
ONE class, independent, in one night. The first five are controls that RAN and were inaudible:
- `stitch` CodeBuild: 20/20 nightly builds FAILED across its whole lifetime (07-07→07-24), heard by no one
- `opal-critical-surface-alerts`: 476 unconsumed messages, 0 consumers, email-to-Andrew subscription missing live
- `ms_heat`: real analytic, zero scheduled trigger, no consumer (its `comp-ms-find` route never shipped)
- `mdpf-daily`: event-only, no schedule (the pre-existing frozen-with-fresh-inputs class)
- two raw-cache readers (fixed @68bbf3dd2): no vintage guard at all

**The SIXTH (CVO~Z, from ~A's residual-24) is higher severity — a control you can READ in the tree that ISN'T
in the runtime at all.** NARROW, VERIFIED FACT: nine source directories — `bd-49f-freshness-probe`,
`bd-cot-freshness-probe`, `inf-gold-freshness-guard`, `mdpf-freshness-checker`, `bd-served-vintage-alarm`,
`opal-assets-absence-check`, `schwab-bronze-freshness`, `security-sweep-daily`, `market_query` — have **no
deployed Lambda counterpart under any name** (live substring search: zero live Lambdas contain "freshness"/
"vintage"/"absence"/"security-sweep"). **MANDATORY LIMIT — DO NOT DROP IT:** this is NOT "the estate has no
freshness guards" — that would be a false-outage claim of exactly the class CLAUDE.md's first NEVER-rule
forbids. The intended function may be served elsewhere (another Lambda, a Step Function, a CloudWatch alarm,
an EC2 job, or a local comp-tool — `comp-freshness` demonstrably exists). What is established is exact: THESE
SOURCE DIRS HAVE NO DEPLOYED LAMBDA UNDER ANY NAME. Whether served elsewhere is **UNVERIFIED**, and verifying
it is the necessary next investigation before any gap is asserted.

CVO~Z's assessment, which I share: the census was chartered to unify tools; what it produced is a six-instance
census of **controls that do not reach the runtime** — inaudible, unconsumed, unscheduled, or entirely
undeployed. That may be a more urgent program than tool consolidation, found BY it. Candidate REFRAME (§7).

---

## 1 · The complete real estate (verified, corrected from my first pass)

**THE FEDERATED CLOUD TRUTH = `NFRA_GLOBGRPH`** — a Nessie-git-branched Iceberg lakehouse, live, 46 refs.
- **10 TRUE Iceberg tables** (base correction — `metadata/` dir is the signature; Glue-registration ≠
  Iceberg): `graph_nodes`, `graph_edges`, `graph_contracts`, `resource_summaries`, `code_heat_snap`, `cse`,
  `cse_test`×2 (UUID anomaly), `fedobs_coevolution_snap`, `fedobs_coverage_snap`, `ms_heat_snap`. The other
  ~9 (`code_heat`, `tool_activity`, `fedobs_obs_findings`/`signals`, `axes_history`, `cse_ingest`,
  `snap_ingest`, `ms_heat`) are plain S3 parquet/JSON *beside* the core.
- **`kuzu` is a projection, not a second graph:** `kuzu_nessie_db` ← materialized from a Nessie snapshot.
  Deployed-plane counts verified exact: LAMBDA live=191=kuzu · EventBridge 141 (3-way base/~A/~C) · SF/SQS/
  S3/DynamoDB kuzu=live. Genuine kuzu staleness: IAM roles live=206 vs kuzu=193 (20.6h cohort).
- Maintained by `incremental_updater` Lambda (best-engineered piece found: DLQ + per-record isolation +
  retry/backoff + SNS-on-exhaustion — a positive pattern to propagate).

**THE LOCAL DEVICE END (the bridge's open span):**
- `.comp-graph/graph.json` = a **local working-tree scan** (source_sha = `sha256(bytes)[:12]`, NOT a git blob
  hash → no LOCAL↔COMMITTED drift capability today; self-heal guard covers 1,907 of 2,255 nodes). **It is a
  LIVE object during any census** — any tool reading it on SHA-drift triggers a full rebuild.
- Its LAMBDA=333 is the **outlier**, polluted (~A-corrected post-CVO~Z): `extract_s3.py`'s unbounded
  `rglob("*.py")` walks into pip-vendored dep trees (a vendored openai SDK under
  `portal_data_proxy/_build_tmp` — a **Rule-3 violation site**). Corrected breakdown: 208 matched (live/
  registry) + 82 phantom (73 vendor-confirmed + 9 org-dir-noise) + 19 alias-excess + **24 genuinely-
  unexplained (open)**. Crucially, graph.json's LAMBDA labels cover **191/191 live Lambdas exactly — zero
  missing**; the earlier "3-short residual" was itself a classifier false-positive that hid ~30 real deep-
  nested Lambdas (rebuilt on a live/registry cross-reference, not a path-shape guess). Full 333-node
  classification in `A_lambda_enumeration.json` for CVO~Z's random sample.
- **Git is partially surfaced — my "nowhere" was wrong:** core graph.json/kuzu carry zero git, but
  `nerves_traffic.py`/`nerves_accrete.py` walk `git log` and persist `CO_CHANGE` edges (nerves-edges.json,
  6688 commits/35d). Portal is a gitlink **5 commits behind its pinned pointer, no `.gitmodules`** — a live
  drift instance. Both repos' primary branches ≈ 21,992 commits; two-repo identity has no shared ID space.

**M365** is a **POPULATED PLANE** (5,669 `layer='ms'` nodes, growing) but **rides as a `layer` property on the
shared CloudNode label — it is NOT one of the declared 7 layers.** `ms_heat` analytic dormant, no consumer.

**THE TOOL SURFACE:** 92 rows (91 `comp-*` + pipescript; reconciles to 84/85). All 5 source classes live;
77/92 tools (84%) read 2+ surface types (genuinely multi-valued). `comp-residue` is unregistered (BLOCKED by
the registration invariant, live-confirmed). graph.json has a **dual vintage-discipline split** inside one
tool's closure (GUARDED-REBUILD primary vs SILENT via the `nerves_resolve.py:73` fallback).

---

## 2 · The bridge, as it actually stands

`LOCAL` (working-tree scan, polluted) —▷ `COMMITTED` (partial, via nerves CO_CHANGE only; no first-class
plane) —▷ `DEPLOYED` (the Nessie/Iceberg truth). The **cloud end is built and versioned**; the
**LOCAL↔COMMITTED span is the open work**, and the reconciliation the sovereign asked for is a bridge across
these with drift as a computed property.

---

## 3 · The central architecture question (mine to rule; Andrew's steer invited)

**Does one ontology span resource-grain AND symbol-grain, or are those two declared planes under a shared
identity?** My lean, consistent with the unity directive: **one ontology with grain as an explicit typed
dimension** — a Lambda-the-resource and a function-the-symbol coexist under one vocabulary and "which grain"
is a queryable property, not a separate store — plus (a) the cheap alias table for the 6.8% vocab drift and
(b) the real work: authoring vocabulary for the genuinely-undeclared 86.5%. Not yet ruled.

---

## 4 · Defect themes (FINDINGS — audit-first, not repaired)

1. **Inaudible-controls theme (§0.2)** — the through-line. `stitch` is **retired-by-design but never
   deleted**: BOTH the cloud CodeBuild (20/20 fail) AND the local post-commit replacement (83 consecutive
   grain-sentinel fails since 07-08) share one root. 3-part remedy (supersedes the PORTAL_REPO_PAT framing):
   (a) finish the 07-07-ordered cloud decommission — silently failing 18 nights past its own retirement date;
   (b) recalibrate `grain_baseline.json` against legitimate estate growth (REACT_QUERY_KEY now trips HIGH,
   2.66x, not zero); (c) separately investigate the standing `EXTERNAL_ENDPOINT=0` detection gap. Alerts
   don't land (476 unconsumed, missing email sub).
2. **graph.json pollution** — 82 phantom Lambda nodes (73 vendored-dep Rule-3 site + 9 org-dir-noise) + 24
   unexplained inflate the LOCAL plane; the cloud truth (kuzu=191) is clean.
3. **Rule-4 drift** — 4 live Lambdas missing from the CI source-map, 5 registered-but-undeployed.
4. **Tool-map local-variable-binding miss class** (~D 6 misses, CVO~Z-found) — an artifact bound to a local
   var and read through it loses its name; 2 of 6 are caches behind `comp-iam` (the Rule-22a fails-GREEN tool).
5. **Terraform/manifest gap** (Andrew-direct to base): plain object-store prefixes have zero Terraform
   declaring their purpose; `derive-build.tf` CodeBuild has no trigger config found.

## 5 · The acceptance property CVO~Z earned (for the PRD)
**Every instrument in this program — INCLUDING the verifier's oracle — must state its own false-positive rate
and be validated against ground truth before its output is actioned.** CVO~Z's own held-back control was 32%
false-positive (comments, docstrings, a `.endswith(".metadata.json")` suffix predicate matched as a filename);
it caught it only by validating its hits before reporting. An oracle inherits every disease of the thing it
measures. This is not a note about CVO~Z; it is a WS-1 acceptance bar.

## 6 · Open items
- **VERIFICATION COMPLETE.** CVO~Z checked ~A's 333-node classification exhaustively (106/106 non-live
  confirmed); 191/191 live coverage stands. All 5 lanes verified, zero open verification items.
- **NEXT INVESTIGATION — required before any gap is asserted (§0.2 sixth instance):** are the 9 GROUP-2
  source dirs (freshness/vintage/absence/security-sweep) served elsewhere — another Lambda, a Step Function,
  a CloudWatch alarm, an EC2 job, or a local comp-tool — or genuinely undeployed? Until answered, the finding
  is "no deployed Lambda counterpart under any name," NEVER "no guard exists" (NEVER#1 / false-outage).
- ~D 6-miss local-variable-binding rework (prioritized above its 6/41 weight — the comp-iam caches).
- `cse_test` dual-UUID cause (needs Nessie REST, VPC-internal).

## 7 · The decision space for "how we handle it" (Andrew)
1. **Scope/reframe:** stay TOOLUNIFY (tool consolidation), or elevate the inaudible-controls through-line to
   the primary program and make consolidation a workstream under it? CVO~Z and I both think §0.2 may be the
   bigger object.
2. **The grain ruling (§3):** confirm one-ontology-with-grain-dimension, or split declared planes.
3. **Author the 86.5%:** commit to authoring symbol-grain vocabulary, or declare it out-of-ontology-by-design.
4. **PRD now?** WS-1's feasibility is *proven* (~D built a depth-4 sound instrument that beat the verifier's
   oracle) — the register seed exists. We can write the PRD against a verified estate whenever you say.
