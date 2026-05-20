# Parity-Class Catalog

**Status:** ACTIVE — 2026-05-20
**Owner:** ADHC_VALGATE (acceptance-gate discipline framework) — catalog maintained by the AE lane
**TO of record:** ADHC_VALGATE.008
**PRD:** docs/architecture/ADHC_VALGATE.md §4.P (parity-class catalog, N8), §2 (parity row), §3.4 (DRIFTD owns the source-map check; VALGATE catalogs, does not duplicate)

---

## What this catalogs

The **parity gate** is not a single check — it is a recurring gate **shape**: a
*declared inventory* (a manifest, a `files[]` array, a graph node-set, a source map,
a Terraform config) compared against the *empirical inventory* it claims to describe
(an on-disk / on-S3 / on-runtime / on-AWS scan). When the two drift, something that
was supposed to ship did not — silently.

This file is the single registry of every declared-vs-empirical parity pair known in
the system, each pair's **gate status** (built / scoped / un-built) and its **owner**.
It is a catalog, not a build: building a missing parity check is a follow-on TO routed
to the relevant infra owner (see §Routing). DRIFTD-owned checks are **referenced here,
not duplicated** — DRIFTD owns the check, this catalog points at it.

Gate-status legend:
- **BUILT** — an automated or process-enforced check exists and runs.
- **SCOPED** — a build TO is authored but not yet shipped.
- **UN-BUILT** — no check exists; the drift is currently undetectable except by manual audit.

---

## Summary table

| ID | Parity pair | Declared source | Empirical source | Status | Owner |
|----|-------------|-----------------|------------------|--------|-------|
| P1 | Lambda source-map `files[]` vs `source_dir` | source-map `files[]` array | files on disk in the Lambda `source_dir` | BUILT | ADHC_DRIFTD |
| P2 | EC2 service: local source vs deployed code | manifest `deployed_commit` / local `source_path` | code running on the EC2 instance | BUILT | AE / EC2-deploy |
| P3 | Terraform config vs live AWS resources | `.tf` config + tfstate | actual AWS resources | BUILT (process) | per-pipeline AE/DT |
| P4 | EventBridge cron resource-maps vs declared | cron resource-map | EventBridge rules in AWS | SCOPED | ADHC_DRIFTD v0.2 (TO-4) |
| P5 | Portal deployment manifest vs deployed bundle | portal deployment manifest | deployed frontend bundle | SCOPED | ADHC_DRIFTD v0.2 (TO-5) |
| P6 | `EC2_MANIFEST.json` service set vs running EC2 fleet | `EC2_MANIFEST.json` (18 services) | `aws ec2 describe-instances` | BUILT (ADHC_VALGATE.009 -- `.tools/parity-gates.sh ec2-manifest`, WARN-mode v1) | AE infra (CloudOps) |
| P7 | comp-graph node-set vs source files on disk | `.comp-graph/graph.json` (~1940 nodes) | `.py` / `.tsx` files on disk | DOCUMENTED-OUT -- NOT a VALGATE TO (CTO~B ruling 2026-05-20); overlaps ADHC_COMPIL_V4.012, reconcile there first | comp-tooling lane / ADHC_COMPIL_V4 (base) |
| P8 | repo-HEAD vs S3-deployed code, swept across INF chain | `origin/CLOUD` HEAD of each chain script | object in `s3://{pipeline}/code/scripts/` | BUILT (ADHC_VALGATE.009 -- `.tools/parity-gates.sh inf-deploy`, gold+silver tiers; bronze/pull-tier sweep = follow-on candidate) | AE pipeline (INF/ETL) |
| P9 | source-map entry set vs deployed AWS Lambda set | `lambda-source-map.json` (~163 fn entries, .functions{}+top-level union) | `aws lambda list-functions` | BUILT (ADHC_VALGATE.009 -- `.tools/parity-gates.sh lambda-sourcemap`, WARN-mode v1) | AE infra (CloudOps) |
| P10 | `gold_validate_config.yaml` coverage vs gold scripts | validate-config script entries | `data/*/scripts/gold/*.py` on disk | DOCUMENTED-OUT -- NOT a VALGATE TO (CTO~B ruling 2026-05-20); comp-tooling / gold-validate scope | DS / comp-tooling |

---

## Built instances

### P1 — Lambda source-map `files[]` vs `source_dir`
- **Declared:** the `files[]` array in `infra/aws/lambda/ci/lambda-source-map.json` for a Lambda.
- **Empirical:** the actual files in that Lambda's `source_dir`, walked recursively.
- **Comparison:** bidirectional set diff. Files in `source_dir` but absent from `files[]` → ERROR + halt (forces registration). Files in `files[]` but absent from `source_dir` → ERROR + halt (stale manifest). Ignore list: `__pycache__`, `*.pyc`, `.pytest_cache`, `.git`, `tests/`, `README.md`, `*.md`.
- **Check:** `check_source_map_parity()` in `.tools/build-and-upload.sh`, pre-zip hook. Halts the build on mismatch.
- **Owner:** ADHC_DRIFTD (shipped under ADHC_DRIFTD.002). **Referenced, not duplicated** here.
- **Anchor:** DS-base commit `144493642` added `append_non_model_today.py` to a Lambda `source_dir` without source-map registration; would have ImportError'd at runtime; caught manually pre-build, then closed structurally by DRIFTD.002.

### P2 — EC2 service: local source vs deployed code
- **Declared:** each `EC2_MANIFEST.json` service's `deployed_commit` + `source_path`.
- **Empirical:** the code actually present on the EC2 instance.
- **Comparison:** `infra/aws/ec2/verify-ec2.sh` — quick mode (git: commits to `source_path` since `deployed_commit`) and `--ssm` mode (SHA256 checksum of remote files vs local). Exit 1 on any drift.
- **Owner:** AE / EC2-deploy. CLAUDE.md Rule 11 mandates running it before EC2 work.
- **Coverage limit:** verifies code parity only for services **already in the manifest**. An EC2 instance missing from the manifest entirely is invisible to it — that gap is P6.

### P3 — Terraform config vs live AWS resources
- **Declared:** the `.tf` configuration + the pipeline's tfstate in `opal-313476888478-terraform-state`.
- **Empirical:** the actual AWS resources.
- **Comparison:** `terraform plan` — a non-empty plan IS the parity diff. CLAUDE.md Rule 2/6 mandate a post-apply 0-diff plan ("No changes. Infrastructure is up-to-date.") as the deploy gate.
- **Owner:** per-pipeline AE/DT.
- **Status nuance:** BUILT but **process-enforced per apply**, not a swept/scheduled gate. Between applies, console/CLI drift is undetected until the next `terraform plan`. A scheduled drift sweep is a candidate hardening but is out of this catalog's scope.

---

## Scoped instances (build TO authored, not yet shipped)

### P4 — EventBridge cron resource-maps vs declared
- **Declared:** the cron resource-map for a pipeline.
- **Empirical:** the EventBridge rules actually in AWS.
- **Status:** SCOPED — ADHC_DRIFTD v0.2 **TO-4** (EventBridge cron resource-maps for the 5 active pipelines: inf / bd / news / market-overview / smartx). Authored 2026-05-15; per `org/projects/ADHC_DRIFTD.json` pending COO co-sign + dispatch.
- **Owner:** ADHC_DRIFTD. Catalog references it; does not duplicate.

### P5 — Portal frontend deployment manifest vs deployed bundle
- **Declared:** the portal frontend deployment manifest.
- **Empirical:** the deployed frontend bundle.
- **Status:** SCOPED — ADHC_DRIFTD v0.2 **TO-5**. Authored 2026-05-15; pending COO co-sign + dispatch.
- **Owner:** ADHC_DRIFTD. Catalog references it; does not duplicate.

---

## Un-built instances (routed — see §Routing)

### P6 — `EC2_MANIFEST.json` service set vs running EC2 fleet
- **Declared:** the 18 services in `infra/aws/ec2/EC2_MANIFEST.json`.
- **Empirical:** the set of EC2 instances actually running in the account (`aws ec2 describe-instances`).
- **Comparison:** does every running instance have a manifest row, and does every manifest row map to a real instance / a `source_path` that exists on disk?
- **Why un-built:** `verify-ec2.sh` (P2) checks **code parity for services in the manifest** — it cannot catch an instance that was never registered, nor a manifest row whose `source_path` no longer resolves. CLAUDE.md Rule 8 ("EC2_MANIFEST.json is the source of truth — every EC2 service must be registered") is currently a cultural rule with no structural check.
- **Note for the build TO:** the seed framing "EC2_MANIFEST vs `infra/aws/ec2/`" is imprecise — manifest entries carry a `source_path` field and several services (`bd-allocations`, `bd-assets`, `bd-fees`, `bd-price-runner`, `bd-transactions`) have no `infra/aws/ec2/<name>/` directory because their code lives elsewhere. The empirical side is the **running fleet + `source_path` resolution**, not folder-name matching.
- **Owner:** AE infra (CloudOps lane).

### P7 — comp-graph node-set vs source files on disk
- **Declared:** the ~1940 nodes in `.comp-graph/graph.json`.
- **Empirical:** the actual `.py` / `.tsx` source files on disk.
- **Comparison:** graph nodes referencing files that no longer exist (orphan nodes); source files with no graph node (un-modeled — comp-* tools silently miss them).
- **Why un-built:** `comp-build` **refreshes** the graph but emits no orphan/missing-node parity report. ADHC_COMPIL_V4.012 (`comp-build-stale-node-warn`) is adjacent and may already cover part of this — the build TO should reconcile against it before implementing.
- **Owner:** comp-tooling lane.

### P8 — repo-HEAD vs S3-deployed code, swept across the INF chain
- **Declared:** the `origin/CLOUD` HEAD content of each INF chain script (~46 gold + silver/bronze, ~56 total per the TO).
- **Empirical:** the script object actually in `s3://{pipeline}/code/scripts/`.
- **Comparison:** per-script content/SHA match across the **full chain in one sweep**.
- **Why un-built:** `comp-pipescript deployed <script>` returns MATCH / STALE / MISSING for **one script, ad-hoc**. There is no swept all-scripts gate. A single-homed deploy-miss on a script nobody happens to check stays invisible.
- **Anchor:** AE 0.6.1, 2026-05-18 — `pull_inflection_performance_rest.py` shipped commit `f39550d99` that never reached any S3 `code/` prefix. A deploy-miss can hit single-homed scripts, not just collision-prone multi-homed ones; a collision census cannot catch it, a full repo-HEAD-vs-S3 sweep can.
- **Owner:** AE pipeline lane (INF / OpalETL).

### P9 — source-map entry set vs deployed AWS Lambda set
- **Declared:** the ~8 function entries in `infra/aws/lambda/ci/lambda-source-map.json`.
- **Empirical:** the actual deployed Lambda functions (`aws lambda list-functions`).
- **Comparison:** a Lambda in AWS with no source-map row (CLAUDE.md Rule 4 violation — CI drift detection blind to it); a source-map row for a deleted/renamed function (stale manifest).
- **Why un-built:** distinct from P1 — P1 checks files **within** a registered Lambda; P9 checks the **set of Lambdas itself**. No check compares the source-map's function set to the AWS function set.
- **Owner:** AE infra (CloudOps lane).

### P10 — `gold_validate_config.yaml` coverage vs gold scripts on disk
- **Declared:** the gold-script entries in `data/black_diamond/scripts/gold/gold_validate_config.yaml`.
- **Empirical:** the `data/*/scripts/gold/*.py` files on disk.
- **Comparison:** a gold script on disk with no validate-config entry has no `comp-validate` gate — a silent post-run-validation coverage hole.
- **Why un-built:** `comp-validate` consumes the config; nothing checks the config covers every gold script. Coverage gaps are invisible.
- **Owner:** DS / comp-tooling lane.

---

## Routing — un-built sites for COO follow-on build-TO authoring

Per ADHC_VALGATE.008 Phase 3, the un-built sites are surfaced to COO; COO authors the
follow-on build TOs (each defaults WARN-not-BLOCK per ADHC_VALGATE PRD §7 Q1). DRIFTD-
owned checks (P1, P4, P5) are **not** routed here — DRIFTD owns them.

| ID | Build-TO recommendation | Recommended owning lane |
|----|-------------------------|-------------------------|
| P6 | EC2_MANIFEST completeness check vs the running fleet (extend or sit alongside `verify-ec2.sh`) | AE infra (CloudOps) |
| P7 | comp-graph orphan/missing-node parity report (reconcile with ADHC_COMPIL_V4.012 first) | comp-tooling lane |
| P8 | swept repo-HEAD-vs-S3 deploy-parity audit across the full INF chain (~56 scripts) | AE pipeline (INF / OpalETL) |
| P9 | source-map function-set vs `aws lambda list-functions` parity check | AE infra (CloudOps) |
| P10 | `gold_validate_config.yaml` coverage check vs gold scripts on disk | DS / comp-tooling |

**Recommended sequencing note for COO:** P6 + P9 are both AE-infra (CloudOps) and both
small `aws` CLI vs JSON-manifest comparisons — they can be bundled into one build TO.
P8 should be checked against whether `comp-pipescript deployed` can simply gain a
`--all` sweep mode rather than a new tool.
