# comp-tools segment-scope reference card

**Last updated:** 2026-05-08 (ADHC_COMPIL_V4.020 — comp-trace/blast moved A; INF gold + platinum nodes baked into comp-build)
**Companion:** `org/modules/graph/comp-tools.yaml` (full catalog) + `docs/architecture/ADHC_COMPIL_V4_017_TEST_MATRIX.md` (empirical evidence)

This is the 1-page "which tool, when?" reference for agents working across BD, INF, and multi-firm surfaces. Use it before reaching for the full `comp-tools.yaml` catalog.

## Three-tier scope

| Tier | What it means | Tools |
|---|---|---|
| **A — cross-segment** | Single invocation covers all surfaces. No flag, no auto-detect, no per-pipeline scoping needed. | `comp-build`, `comp-trace`, `comp-blast`, `comp-diff`, `comp-xref`, `comp-cache`, `comp-pii`, `comp-tooltip`, `comp-shell`, `loop-quiescence` |
| **B — segment-aware** | Auto-detects scope from input (script-id prefix, component name, URL) OR requires an explicit flag (`--pipeline`, `--config`, `--feature`, `--function`). | `comp-pipescript`, `comp-routes`, `comp-platinum`, `comp-transform`, `comp-iam`, `comp-validate`, `comp-constants`, `comp-freshness`, `check-lambda-layer-deps` |
| **C — segment-locked** | Currently only works on one pipeline. Broadening would need config/extension. | `comp-incrparity` (BD-only) |

## "If you're working on X, use these tools"

| You're touching ... | Reach for | Notes |
|---|---|---|
| **A BD gold script** (D_04, C_07, B_00) | `comp-pipescript io/feeds/consumers/postdeps`, then `comp-blast` for the function-level fanout | comp-trace + comp-blast cover BD gold (graph nodes); INF gold absent from graph |
| **An INF gold script** (INF_D_04, INF_C_01) | `comp-pipescript io/feeds/consumers/overlap` for full I/O manifests. `comp-trace INF_D_04 --all` + `comp-blast _build_aua_view` for cross-layer + function-level questions. | ADHC_COMPIL_V4.020: INF gold now graph-resident (script + function-level). Multi-match disambiguation via `--all` per usual. |
| **An INF manual-API script** (`pull_inflection_*`, `orion_*`) | `comp-pipescript dag --pipeline inf-manual-api`, `comp-pipescript io <script>` | V4.008 ship; auto-detect via name patterns |
| **A Lambda function** (any pipeline) | `comp-iam service <name>` (auto-falls-through to IAM-role; V4.013), `check-lambda-layer-deps --function <name>`, `comp-trace <name> --direction up` | All three work cross-pipeline. comp-trace finds what fetches the Lambda. |
| **An EC2 role** (bd-exporter, inf-bronze-runner) | `comp-iam service <name>` (V4.013 fallback finds `*-ec2-role`), `comp-iam role <name>` | |
| **A React component** (PartnerAnalytics, ClientsTab) | `comp-platinum page <name>` (full stack), `comp-transform schema-check <name>` | comp-platinum chains transform + routes + pipescript |
| **A frontend endpoint** (getFirmLeaderboard) | `comp-routes trace <name>`, `comp-trace <name> --direction up` | |
| **A CloudFront URL** (`/api/scoped/...`) | `comp-routes trace <url>`, `comp-routes behaviors`, `comp-routes auth-map` | URL-based; pipeline-agnostic |
| **An S3 artifact** (gold/artifacts/X.json) | `comp-trace s3:<key>`, `comp-platinum reverse <key>` (full reverse), `comp-pipescript consumers <producer>` | **Always prefix `s3:`** — without it comp-trace/comp-blast won't match |
| **A platinum/* artifact** | `comp-trace s3:<key>` for BD-side hardcoded writes (post-V4.020) OR `comp-platinum reverse <key>` for full producer/serving/consumer chain | V4.020: BD platinum keys (`s3:platinum/firm/*`, `s3:platinum/clients/{*}/*`, `s3:platinum/advisors/{*}/*`) baked into graph as nodes via D_04 hardcoded-write detection. Reverse still preferred for full reverse audit. |
| **A marker constant** (FIRM_ID, INFLECTION_REP_IDS) | `comp-constants check` (drift), `comp-constants new` (discovery) | Lane-aware via config; auto-detects bd/inf/multifirm |
| **A gold-artifact validate config** | `comp-validate <script_id> --artifact <path>` (auto-detect by script_id prefix), `--config <path>` to override | V4.009 |
| **A schema/types question on a component** | `comp-transform schema-check <comp> [--feature <token>]`, `comp-transform ternary-audit <comp>` | --feature escalates feature-named UNUSED to WARN |
| **A pipeline freshness gate** | `comp-freshness chain {bd|inf}`, `comp-freshness --list` | Live AWS calls; returns PASS/WARN/FAIL/SKIP |
| **A shell script in .tools/** | `comp-shell scan <file>` | Detects bare pgrep/pkill/flock/pidof/setsid/wget |
| **A REACT cache key** | `comp-cache collisions`, `comp-cache key <substring>` | Portal-wide |
| **A PII exposure question** | `comp-pii audit`, `comp-pii routes`, `comp-pii sweep` | Full registry + per-route audit |
| **A tooltip migration** | `comp-tooltip summary`, `comp-tooltip drift` | One-off audit |
| **A graph state question** | `comp-build`, `comp-xref` (diff mode = no arg, symbol mode = arg) | dual-purpose |
| **Macro quiescence before `/loop {MACRO}`** | `loop-quiescence <PROJECT_CODE> --summary` | **Pass project code (`ADHC_COMPIL_V4`), NOT macro prefix (`ADHC`)** — bare prefix returns false-positive QUIESCENT_CLEAN |

## Cross-cutting axes

Beyond pipeline (BD/INF), tools may also vary by:

- **Firm** — `49financial`, `inflection`, `cottonwood` (post-FIRMSEP.10). Affects comp-platinum, comp-routes (firm-scoped paths), comp-iam (firm-segregated buckets).
- **Layer** — `gold` / `silver` / `bronze` / `platinum` / `portal`. comp-pipescript distinguishes via `--pipeline {bd-gold,bd-silver,inf-gold,inf-silver,inf-manual-api}`.
- **Surface type** — Lambda / EC2 / CF / API GW / S3 prefix / DDB table. comp-iam, comp-routes, comp-events (post-V4.005) split here.
- **Mode** — default / `--strict` / `--verbose` / `--json`. Varies per tool; not all tools support all modes (see test matrix Triage #13 — `--json` not implemented on comp-trace despite catalog claim).

## Common gotchas (from V4.OPS empirical run, post-V4.019/.020 fixes)

1. **`comp-trace D_04`** returns "Multiple matches" — the canonical script-level node ID is `gold:D_04.client_portal_summary` or use `comp-trace D_04 --all`. Catalog example does not work as written.
2. **`comp-trace platinum/firm/leaderboard.json`** still needs `s3:` prefix; post-V4.020 the `s3:platinum/*` nodes DO exist in the graph (BD D_04 platinum writes baked in). Use `comp-trace s3:platinum/firm/leaderboard.json --direction up`.
3. ~~`comp-pipescript chain --pipeline inf-gold` silently returns BD chain~~ — **FIXED V4.019**: now explicit "Unknown chain X for pipeline Y" + lists valid chains. INF chains exist (`full`/`incremental`/`label`/`silver_prep`).
4. ~~`comp-pipescript deployed --pipeline inf-gold INF_D_04` crashes with UnboundLocalError~~ — **FIXED V4.019**: returns clean MATCH/STALE per script.
5. **`check-lambda-layer-deps`** uses `--function <name>` / `--pipeline <name>` flags, NOT positional args (catalog says positional). Run `--help` if confused. (Doc-fix candidate in V4.021.)
6. **`comp-constants --lane bd`** doesn't work — lane is auto-detected from config metadata, not flag-controlled.
7. **`loop-quiescence <MACRO_PREFIX>`** (e.g., `ADHC` vs `ADHC_COMPIL_V4`) returns `QUIESCENT_CLEAN total=0` — false-positive when no project file exists. Pass full project code. (V4.022 candidate.)
8. **`comp-iam service bd-gold-trigger`** shows role `(not mapped)` — Lambda-source-map IAM mapping incomplete for ~100 BD Lambdas. INF Lambdas mapped via V4.013 fallback (works). (V4.022 backfill candidate.)

For full empirical evidence + all test cases + recommended fixes, see `docs/architecture/ADHC_COMPIL_V4_017_TEST_MATRIX.md`.
