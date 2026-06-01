# comp-lambdamap — design spec (DRAFT for CTO charter-confirm)

**Author:** 0.7.0_AE_CloudOps · **Origin:** CVO recommendation (359375d87) + BMKAUD source-map audit + the yang-v2.4.10 functions_updated over-list · **Status:** SCOPE for CTO charter (do NOT build until charter-confirmed)

## Problem (the write-and-age failure class)
`infra/aws/lambda/ci/lambda-source-map.json` is HAND-MAINTAINED. Today's BMKAUD-adjacent audit found this manifests as recurring drift:
- **Wrong source_dir** (item 2: seeking-alpha-analysis-dedup → news-dedup dir; item 3: analysis-scraper → absent article-scraper dir) — a build would zip the WRONG code.
- **Mislocated + incomplete entries** (item 1: 7 entries OUTSIDE `functions{}` with partial schemas, e.g. inf-gold-trigger lacks source_dir) — get NO sha-refresh / NO deploy-provenance.
- **Stale provenance over-list** (yang-v2.4.10: `record-terraform-deploy.sh` enumerates source-map-delta functions in the commit window → co-listed a peer's not-yet-applied function + a sha-unchanged benchmark lambda).
Root cause: the map is hand-authored + hand-aged, so it drifts from the two real sources of truth — the **TF** (`function_name` + `source_dir` + `tf_resource`/`tf_file`) and the **lambda dirs** (`files`).

## Proposal: DERIVE the map, don't hand-age it
`comp-lambdamap` — a comp-* tool that derives the lambda→source mapping from ground truth + checks drift, so the JSON becomes a generated artifact (or a verified-against-truth one), not a hand-edit.

### Inputs (ground truth)
1. **TF parse:** every `module "..." { source = "../modules/yang-lambda" | ... }` + `resource "aws_lambda_function"` across `infra/aws/terraform/**` → extract `function_name`, `source_dir`, `tf_file`, `tf_resource`, `pipeline` (workspace dir).
2. **Lambda dirs:** `infra/aws/lambda/**` → the source dirs + their files.
3. **Artifact bucket:** `s3://opal-313476888478-lambda-artifacts/{pipeline}/{fn}.zip` content-sha256 (the deployed-artifact truth) + live `get-function-configuration` CodeSha256 (the running truth).

### Outputs / modes
- `comp-lambdamap check` — diff the live JSON vs derived truth; report: WRONG_SOURCE_DIR, MISLOCATED (outside functions{}), INCOMPLETE_SCHEMA, MISSING_ENTRY (TF-backed fn w/ no entry), ORPHAN_ENTRY (entry w/ no TF/dir), SHA_DRIFT (source-map sha ≠ live CodeSha256). (Supersedes the manual BMKAUD audit + the lambda-deploy.yml drift check — always-on.)
- `comp-lambdamap derive [--write]` — regenerate the canonical functions{} from TF+dirs (source_dir/files/tf_file/tf_resource/pipeline), normalizing the 7 mislocated entries (item 1) in one pass.
- `comp-lambdamap provenance {fn}` — the per-function commit→zip→deploy chain from CodeSha256↔artifact-sha↔source-map, derived not recorded (fixes the v2.4.10 over-list class: provenance is read from truth, not written-and-aged).

### Fixes it structurally resolves
- BMKAUD audit item-1 (normalize the 7 mislocated/incomplete entries — the deferred item folds here).
- items 2/3 (wrong source_dir) — `check` catches them; `derive` prevents them.
- yang-v2.4.10 functions_updated over-list — `provenance` derives per-function from CodeSha256, so a peer's not-yet-applied fn or a sha-unchanged co-list can't appear.
- The "every change to the minute / commit→zip→deploy provable" rigor Andrew set for BMKAUD becomes a tool guarantee, not manual discipline.

### Build estimate / placement
- New tool under `.tools/` (comp-* family); registry entry in `org/modules/graph/comp-tools.yaml`; pytest fixtures per `feedback_comp_tool_pytest_suite`. Reuses the existing TF-parse approach from comp-iam (which already parses iam.tf for roles/grants) — extend to lambda modules.
- Rough: 1 focused build cycle for `check` (highest value — always-on drift), +1 for `derive`/`provenance`.

## Charter ask (CTO)
1. Confirm comp-lambdamap is GO to build (vs deferring / a lighter check-only extension of lambda-deploy.yml).
2. Scope: `check` first (drift-detection, immediate value), then `derive`/`provenance`? Or full tool in one?
3. Sequencing vs the manual item-1 normalization: build comp-lambdamap `derive` and let IT normalize item-1 (preferred — no throwaway), OR do the manual item-1 stopgap now if comp-lambdamap is >2 cycles out (CVO's framing).
HOLD build until charter-confirmed. This spec is the scoping artifact COO's "stay on comp-lambdamap" capacity-fill resolves to while BMKAUD durability-TF is Andrew-gated.
