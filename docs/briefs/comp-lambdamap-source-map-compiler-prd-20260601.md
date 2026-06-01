# PRD — comp-lambdamap: categorical Lambda source-map compiler

**Author:** 1.0.0_SA_CTO · **Trigger:** Andrew-direct ("we should have a script that does that categorically") relayed via CVO parity audit (359375d87, lambda_source_map_parity_audit_20260601.md) · **Design:** ws CTO (this) · **Mechanism:** AE CloudOps · **Verify:** CVO · **Decompose:** COO → TOs.
**Status:** DRAFT for review.

## 1. Problem (CVO audit, empirical)
`infra/aws/lambda/ci/lambda-source-map.json` is the source of truth for CI drift-detection (CLAUDE.md Rule 4), but it is **hand-maintained ("written-and-aging"), not compiled** — so it silently decays and CI drift-detection has blind spots:
- **7 entries mislocated** as TOP-LEVEL JSON keys OUTSIDE `functions{}` (bd-incrparity-trigger + 6 inf-* incl the TF-backed inf-client-detail) → invisible to every tool that iterates `m['functions']` (build-and-upload, record-terraform-deploy, comp-iam): no sha-refresh, no provenance, no IAM-gap-check.
- **Rule-4 gaps:** TF-backed lambdas with ZERO map entry (seeking-alpha-dedup-coordinator) = CI-drift-blind on a deployed function; + absent likely-dormant ones.
- **Broken source_dir** (seeking-alpha entry pointed at an absent dir — already hot-fixed e70ddcfda, but the class persists).
- **Decay metrics:** 14/126 stale; 49/169 no tf_resource; 40/169 no tf_file; 42/169 no last_deployed_at; ~30% no TF-linkage.

Net: the map's integrity depends on agents remembering to hand-edit it correctly — exactly the cultural-not-structural failure class this fabric repeatedly converts to tooling.

## 2. Solution — a categorical compiler (`comp-lambdamap`)
A `comp-*`-family tool that COMPILES the source-map from ground truth rather than trusting hand edits. Core passes:
1. **ENUMERATE** every Lambda source dir under the lambda roots (infra/aws/lambda/** + v2_portal/** + any external roots) across handler variants: Python (.py), Node (.mjs/.js), container/Image (Dockerfile), and multi-handler dirs. Output: the authoritative function set.
2. **PARSE Terraform** (`aws_lambda_function` resources across infra/aws/terraform/**) to derive, per function: `tf_file`, `tf_resource`/module address, artifact S3 key, IAM role. This is what closes the Rule-4 gaps (a TF-backed function with no source dir, or a source dir with no TF, is flagged — not silently absent).
3. **RECOMPUTE sha** of each function's source vs (a) the recorded `last_deployed` sha and (b) the LIVE `CodeSha256` (extends lambda-deploy.yml's partial drift check to an always-on batch). Classify per function: MATCH / STALE-SOURCE / DRIFT (live≠recorded) / MISSING-ENTRY (TF-backed, no map row) / NO-TF-LINKAGE / NO-PROVENANCE / ORPHAN-DIR (source, no TF).
4. **NORMALIZE schema by construction** — everything lives under `functions{}` with a fixed shape; the top-level-key misplacement class becomes impossible (the compiler writes the canonical structure).
5. **BATCH-run** as a CI gate (fail on TF-backed-no-entry / unresolved drift) AND on-demand `comp-lambdamap` CLI (report-by-default, `--apply` to write the normalized map under an audited author line — same pattern as `comp-registry sync`).

## 3. Fit + ownership
- Fits the `comp-*` categorical-compiler family (`.tools/`, PATH); reference in `org/modules/graph/comp-tools.yaml` + the CLAUDE.md comp-tools table.
- **ws CTO:** this design/PRD. **AE CloudOps:** the mechanism (it touches CI + the source-map + TF parsing = AE infra lane). **CVO:** verify the compiler's output vs current state (CVO already did the manual audit — it becomes the compiler's first regression fixture). **COO:** TO-decompose.

## 4. Acceptance criteria
- AC1: enumerates ALL lambda source dirs (py + mjs + Image + multi-handler) — count reconciles to a hand-spot-check; 0 mislocated/top-level entries post-normalize.
- AC2: every TF-backed `aws_lambda_function` has a map entry (Rule-4 gap = 0); every source dir maps to a TF resource or is explicitly flagged ORPHAN-DIR.
- AC3: per-function drift verdict (recorded sha vs source sha vs live CodeSha256) for the full set, batch.
- AC4: `--apply` writes the normalized canonical-schema map via safe-commit under an audited author line; report-only default.
- AC5: CI integration (gate on TF-backed-no-entry + unresolved DRIFT); CVO verifies output reproduces + supersedes the manual audit findings (the 7 mislocated, the seeking-alpha gap, etc.).

## 5. Notes
- The seeking-alpha source_dir hot-fix (e70ddcfda) + the 7 mislocated entries are the compiler's day-1 fixtures — it must surface exactly those.
- This is the same "convert a cultural/hand-maintained invariant into a structural compiler" move as the rest of the comp-* suite; the source-map is overdue for it given it gates Rule-4 CI drift-detection fabric-wide.
- Open: whether to fold this as a standalone ADHC_* project (COO/registry call) or a comp-tools enhancement TO.
