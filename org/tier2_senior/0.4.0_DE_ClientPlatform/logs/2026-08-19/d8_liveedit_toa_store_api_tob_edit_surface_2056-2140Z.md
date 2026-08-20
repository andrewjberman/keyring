# D8_LIVEEDIT TO-A (store+API, author leg) + TO-B (edit surface, both families) — sitez build
**archetype:** IMPLEMENT
**serial:** 0.4.0_DE_ClientPlatform~Z (lane ~Z, base-folder log per convention)
**window:** 2026-08-19 2056Z–2140Z
**TO:** D8_LIVEEDIT.TO-AB-SITEZ @ org/tier0_exec/0.0.0_AB_MSTR/task_orders/ (status flipped staged->pending in-tree, UNSTAGED — MSTR~Z commits per owned-paths)
**Vintage:** PRD docs/architecture/D8_LIVE_EDIT_MODALS_PRD.md @7416fb46d0; auth ruling D8_AUTH_SURFACE_RULING_20260819.md @e697f1450e

## What landed

**Dev-build proof (D8-1, kickoff first-act): PASS, MEASURED.** bun 1.3.14, `bun install` rc=0,
Vite v7.3.5 ready 401ms on :5175, HTTP 200 root, live TSX transform served. The estate's one
unmeasured envelope cell is priced: portal dev-builds RUN on site Z. Reported to MSTR~Z 2102Z.

**Portal submodule reconcile (pre-work, kickoff-mandated):** local DEV had DIVERGED from the
recorded gitlink (5 local-only commits vs 13 gitlink-only incl. the OPAL_INVPHL components D8
targets). ff-only refused; reconciled by MERGE of origin/DEV (never rebase) -> 46f127eb, clean,
zero conflicts, both sides preserved. Surfaced to MSTR~Z (5 unpushed local portal commits await
integration).

**TO-A author package (workspace CLOUD-lane commits, applies are laptop's per envelope law):**
- `4c8fe9d006` — infra/aws/lambda/portal_content/lambda_function.py (GET all / PUT one /
  DELETE one = explicit reset leg; server-side `_is_internal` chokepoint firmId=='opal-capital';
  updated_by from token subject; prev_bodies last-5 audit; 8KB cap; surface_id regex makes a
  display name structurally unkeyable) + infra/aws/terraform/portal-content/main.tf (table
  PITR/no-GSI, table-scoped role, yang-lambda 256/30, routes pure-add on 7k3ed8px20 authorizer
  naqxlm) + build-and-upload.sh + portal-auth CF behaviors 4c/4d (auth-validator-edge,
  tickets-idiom). Committed under audited GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL (lane
  refusal on role-authorized work; MSTR seat assignment carries the AE-class row).
- `13fd07d510` — lambda-source-map.json entry (Rule 4), separate commit under
  GIT_COMMIT_AUTHOR_OVERRIDE=YANG_PIPELINE_DEPLOY (Rule 14a: one lane per commit).
- Route-spelling refinement SURFACED: /api/scoped/portal-content (PRD §3 wrote /api/portal-content
  pre-ruling; the ruled "existing scoped-route auth chain" lives on the scoped prefix).
- Existence checks (D8-2) RE-VERIFIED live, not inherited: dynamodb list-tables materialized,
  DENOMINATOR 35 tables, no content-store table under any name; per-module route survey
  (bd-pipeline/partners-api/ticket-center/trade-pipeline) grounded the new-Lambda decision per
  PRD §6 escape clause — both precedent Lambdas are single-domain with table-scoped roles;
  extending either widens a foreign role grant and couples deploys.

**TO-B build (portal DEV commit `ccda8711`):** LiveEditableProse (ONE component, both families)
+ usePortalContent hook (['portal-content'] net-new key) + portal-proxy GET/PUT/DELETE +
PhilosophyPillars wiring (incl. the ruled §1 header-comment SUPERSESSION of the 08-12 ceiling)
+ ModelPortfolioModal Key Notes wiring (figures untouched). All three rulings bound: STORE-WINS
with the losing path VISIBLE (override shows who/when/what it masks), ALL-INTERNAL affordance
gate (advisory; API 403 is the control), PK stable identifiers.

**Verification run here:** tsc -b PASS; eslint PASS (5 files); commit-gate PASS (lambda .py);
terraform validate PASS both modules (backendless init; portal-auth warnings pre-existing);
ui-smoke screenshots BOTH identity directions — internal shows pencil, partner
(firmId=49financial) shows NO affordance; colour law holds on the light dialog panel.

## Gated remainder (rides the laptop apply, WDAC-bounded 08-20 07:00)
D8-3 second-session persistence, D8-4 API-level 403, D8-5 live both-call-sites, D8-6 live DEV
exercise, D8-7 IAM simulate battery (one --resource-arns per call, separate positive control).
I can run the HTTPS exercises from here post-apply; applies themselves never run on site Z.

## Compiler Tools

| Tool + invocation | Result | Note |
|---|---|---|
| comp-routes trace /api/portal-content | catch-all /* only — net-new path | MSYS leading-/ mangle noted by tool; read correctly |
| comp-routes behaviors | full behavior census; scoped-route auth chain identified (auth-validator-edge + APIGateway-portal) | grounded the route design |
| comp-iam service opal-ticket-api | 9 DDB ops [UNKNOWN], role unmapped — fail-closed floor | precedent Lambda survey |
| comp-transform schema-check PhilosophyPillars | PASS (pre + post edit) | Phase 1 + 2 |
| comp-transform schema-check ModelPortfolioModal | "Component not found" — components/ dir not indexed | PRD run B4 tool limit REPRODUCED; contract via direct source read |
| comp-cache collisions | no defect rows; ['portal-content'] net-new, no collision | Phase 1 + 2 |
| comp-find (7k3ed8px20 survey; PROOF_OF_SPEC locate) | per-module wiring survey; schema found | |
| comp-which (A.3 exercise) | forwarder RAN | startup |
| comp-to D8_LIVEEDIT.TO-AB-SITEZ.content-store-and-edit-surface | session TO context set | race-free per-session |
| rail-checked raw aws: dynamodb list-tables | 35 tables materialized, absence RE-VERIFIED | comp-aws is TF-DESIRED; absence claim needs live census |

## Surprises (surprise channel, no action beyond sanctioned reconcile)
1. Portal DEV divergence (5 local-only commits) — reconciled by merge, surfaced to MSTR~Z.
2. audit-archive-invoker 18 findings at startup — known site-Z cross-device baseline class,
   already in FINDINGS.md; surfaced in ack, not chased.
3. .tools/terraform.exe does not exist on site Z (device-axis; laptop layout hardcoded in law
   Quick-reference) — winget terraform used for read-only validate only. Surfaced here.
4. ui-smoke's stubbed default identity IS internal (opal-capital Dev) — a "default" capture
   cannot serve as the non-employee negative; explicit --claim firmId=49financial required.
