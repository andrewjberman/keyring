# COMP_HEALTH -- does each comp-tool actually work? (2026-10-08 ~21:4xZ-22:2xZ, laptop, read-only)

Fork of 4.0.0_SA_CRO for Andrew-direct ~21:3xZ (record org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_213xZ_COMP_TOOLS_AUDIT_DELETE_UNUSED_REVIEW_COMP_WHICH_ROUTER.md): "1.) Actually works." Usage is the other slice; this file is health only.

**Method.** Population: every `.tools/comp-*` on disk = **105** files (99 distinct tools + 6 `.py` twins of a bash wrapper), plus TOOL_MASTER's 100 entries (3 of them name a bare command that is not a file: comp-ledger-agreement, comp-which-routing-test, comp-v5-composite-test). Before running anything, each engine's source was read for a read-only path: an AST scan of every engine's top level for side-effect calls (none found that write; the hits are `git rev-parse`, `shutil.which`, interpreter guards), and argparse/help handling. Then each tool ran ONE safe exercise (stdin empty, 90 s cap; reruns at 300 s for slow self-tests): its self-test where one exists (51 tools), else `--help`, plus offline self-tests found on a second read (comp-iam census-self-test, comp-denytest --offline-self-test), plus a cheap real read-only call for 13 key help-only tools (comp-find, comp-read, comp-kuzu, comp-graph status, comp-keys prefix, comp-xref --check, comp-system --check, comp-routes behaviors, comp-describe <name>, comp-learns-status, comp-fedobs, ...). Repo state was diffed before/after: no file created or changed by these runs.

**Verdicts:** WORKS = a self-test passed, or `--help` plus a real read-only call succeeded. PARTIAL = loads and parses (`--help` rc 0) but behaviour not exercised here (no self-test; the real call would write, hit AWS heavily, or rebuild a cache). BROKEN = crash/import error/missing dependency/stale path. NOT-EXERCISED = no safe path.

## Counts (denominator 105 files)

- WORKS: 57
- PARTIAL: 45
- BROKEN: 0
- NOT-EXERCISED: 3

## BROKEN

None. Every tool that was run loaded and exited 0 on its safe path (or 2 where 2 is its documented 'stale' answer).

## Defects found that are not crashes

1. **`.tools/comp-stitch-refresh` is a live stitch PUBLISHER (HAZARD).** Lines 82-83 `aws s3 cp` the artifact and marker to `s3://opal-313476888478-globgrph/stitch/`. NFRA_CLDGRPH S29 (@a46abe413a, R16) retired `.tools/stitch-refresh` as a publisher because the key must have ONE writer (the cloud producer opal-stitch-produce); this comp-* copy (last commit d31bfb5977, 2026-07-07, 0.7.0_AE_CloudOps) was never retired and TOOL_MASTER lists it `active`. Anyone who runs it overwrites the served stitch. Not run here.
2. **Three registry names that do not resolve.** TOOL_MASTER lists `comp-ledger-agreement`, `comp-which-routing-test`, `comp-v5-composite-test`; on disk they are `.py` / `.sh` files and the bare names are not on PATH (`command -v` empty), so a routed call by the registered name fails.
3. **`comp-describe --self-test` is unreachable** through its wrapper (it always prepends `--describe`; rc 2). The engine's self-test exists; a real describe call works (30 s).
4. **`comp-depth` exits 0 on an unknown subcommand** (prints the error, rc 0) -- an rc-only caller reads success.
5. **`comp-v5-composite-test.sh` is not a comp-tool**: a June one-off live Lambda composite test with boto3 clients at module top, no registry status, named into the comp-* namespace.
6. **Slow self-tests:** comp-schedule 127 s, comp-estate 62-90 s, comp-adversary 47 s, comp-tool-health(-gate) 26-28 s; comp-gitdrill timed out at 90 s cold, 18 s warm.

## Duplicates and overlaps

- **Six `.py` twins on disk** beside their bash wrapper (same engine twice in PATH): comp-deadgrant / comp-deadgrant.py, comp-denytest / comp-denytest.py, comp-firmsep-sweep / comp-firmsep-sweep.py, comp-surprise / comp-surprise.py, comp-tagauthz / comp-tagauthz.py, comp-whoread / comp-whoread.py. Harmless, but they double the namespace count.
- **Aliases by design:** comp-grep and comp-glob forward to comp-find (the rail's search primitives, `_comprail`).
- **One engine, five entry points:** comp-blast / comp-build / comp-diff / comp-trace / comp-xref all run `org/modules/graph/cli.py` (declared intentional_shared_infra).
- **Declared overlaps (coverage map redundancy_census, 9 groups, all 'finding: none'):** IAM (comp-iam, comp-aws, comp-lambdamap); parity (comp-lambdamap, comp-parity, comp-incrparity); freshness (comp-freshness, comp-heat, comp-graph, comp-xray); trace-graph (trace, blast, diff, xref); portal-component (transform, pii); estate-structure (dups, aws); dispatch-dag (pipescript, dispatch); panel-coupling (cache, cluster); symbol-defn (blast, symbols).
- **Meta-tools about tools (candidates to consolidate):** comp-tool-health, comp-tool-health-gate, comp-toolgraph, comp-learns-score, comp-learns-status, comp-routable-check, comp-coverage-check, comp-manifest-check, comp-which-routing-test -- 9 tools that grade the other tools.
- **Deprecated still on disk:** comp-aws (agent use retired 2026-09-09; the engine still runs estate-side, so the file stays). No `retired` tool is on disk.

## Per-tool table

| tool | status | engine | lines | last commit | test? | exercise cmd | rc | secs | verdict | note |
|---|---|---|---|---|---|---|---|---|---|---|
| comp-activity | active | .tools/fabric-activity.py | 564 | 2026-10-08 4.0.0_SA_CRO | yes | `comp-activity surface infra/aws/terraform/shared-infra/s3.tf` | 0 | 1.9 | WORKS |  |
| comp-adversary | active | .tools\comp-adversary | 935 | 2026-10-01 0.0.0_AB_MSTR | - | `comp-adversary --self-test` | 0 | 47.4 | WORKS | self-test 47 s; the one FAIL-word line is report content, rc 0 |
| comp-arity | active | .tools\comp-arity | 439 | 2026-07-25 0.8.0_AE_CloudComp~D | yes | `comp-arity --self-test` | 0 | 1.1 | WORKS |  |
| comp-assets | active | org/modules/graph/comp_assets.py | 554 | 2026-07-14 2.0.0_SA_COO | yes | `comp-assets --self-test` | 0 | 1.7 | WORKS |  |
| comp-atomcheck | active | org/modules/graph/atomcheck_cli.py | 490 | 2026-08-25 0.8.0_AE_CloudComp | - | `comp-atomcheck --help` | 0 | 2.0 | PARTIAL |  |
| comp-aws | deprecated | org/modules/graph/comp_aws_cli.py | 3379 | 2026-09-09 0.9.0_WK_NFRA_CLDGRPH~6 | yes | `comp-aws --help` | 0 | 2.0 | PARTIAL | DEPRECATED (agent use retired 2026-09-09; engine runs estate-side); still on disk |
| comp-axes | active | .tools\comp-axes | 525 | 2026-07-15 0.8.0_AE_CloudComp~Z | yes | `comp-axes --self-test` | 0 | 0.2 | WORKS |  |
| comp-blast | active | org/modules/graph/cli.py | 1915 | 2026-09-05 0.9.0_WK_NFRA_CLDGRPH~2 | yes | `comp-blast --self-test` | 0 | 1.9 | WORKS |  |
| comp-build | active | org/modules/graph/cli.py | 1915 | 2026-09-05 0.9.0_WK_NFRA_CLDGRPH~2 | yes | `comp-build --help` | 0 | 2.1 | PARTIAL | help only: build rebuilds the trace cache (a write); engine cli.py's self-test passed via comp-blast |
| comp-cache | active | org/modules/graph/cache_cli.py | 569 | 2026-09-03 0.8.0_AE_CloudComp~J | yes | `comp-cache --help` | 0 | 1.9 | PARTIAL |  |
| comp-canon-motif | active | infra/aws/globgrph/canon_motif_scorer.py | 381 | 2026-09-05 0.9.0_WK_NFRA_CLDGRPH~2 | - | `comp-canon-motif --self-test` | 0 | 1.9 | WORKS |  |
| comp-chainrun | active | org/modules/graph/chainrun_cli.py | 739 | 2026-07-10 3.0.0_SA_CVO~B | - | `comp-chainrun --help` | 0 | 1.7 | PARTIAL |  |
| comp-claimlink | active | .tools\comp-claimlink | 223 | 2026-08-06 3.0.0_SA_CVO | - | `comp-claimlink --self-test` | 0 | 0.8 | WORKS |  |
| comp-clobber | active | org/modules/graph/clobber_scan.py | 30 | 2026-07-21 3.0.0_SA_CVO | - | `comp-clobber --help` | 0 | 0.2 | PARTIAL |  |
| comp-closure | active | org/modules/graph/comp_closure.py | 954 | 2026-10-01 0.0.0_AB_MSTR | yes | `comp-closure --self-test` | 0 | 2.6 | WORKS |  |
| comp-cluster | active | infra/aws/globgrph/comp_cluster_cli.py | 293 | 2026-09-05 0.9.0_WK_NFRA_CLDGRPH~2 | yes | `comp-cluster --help` | 0 | 1.8 | PARTIAL |  |
| comp-cochange | active | org/modules/graph/comp_cochange.py | 381 | 2026-08-05 3.0.0_SA_CVO | - | `comp-cochange --self-test` | 0 | 1.9 | WORKS |  |
| comp-constants | active | org/modules/graph/comp_constants_cli.py | 682 | 2026-07-25 0.8.0_AE_CloudComp~E | yes | `comp-constants --help` | 0 | 1.8 | PARTIAL |  |
| comp-coverage | active | org/modules/graph/coverage_cli.py | 306 | 2026-07-10 3.0.0_SA_CVO~B | yes | `comp-coverage --help` | 0 | 1.9 | PARTIAL |  |
| comp-coverage-check | active | org/modules/graph/comp_coverage_check.py | 51 | 2026-06-30 0.8.0_AE_CloudComp~C | yes | `comp-coverage-check` | 0 | 0.7 | WORKS |  |
| comp-dataflow | active | org/modules/graph/comp_dataflow.py | 690 | 2026-09-03 0.8.0_AE_CloudComp~A | - | `comp-dataflow --self-test` | 0 | 2.3 | WORKS |  |
| comp-deadgrant | active | .tools/comp-deadgrant.py | 551 | 2026-08-20 0.8.0_AE_CloudComp | - | `comp-deadgrant --self-test` | 0 | 2.2 | WORKS |  |
| comp-deadgrant.py | active | .tools\comp-deadgrant.py | 551 | 2026-08-20 0.8.0_AE_CloudComp | - | `comp-deadgrant.py --self-test` | 0 | 0.2 | WORKS |  |
| comp-debris | active | org/modules/graph/comp_debris.py | 325 | 2026-07-17 0.8.0_AE_CloudComp~B | - | `comp-debris --self-test` | 0 | 3.1 | WORKS |  |
| comp-denytest | active | .tools/comp-denytest.py | 673 | 2026-09-03 0.8.0_AE_CloudComp~E | - | `comp-denytest --offline-self-test` | 0 | 0 | WORKS | offline answer-state self-test 4/4 PASS, zero live IAM calls |
| comp-denytest.py | active | .tools\comp-denytest.py | 673 | 2026-09-03 0.8.0_AE_CloudComp~E | - | `comp-denytest.py --offline-self-test` | 0 | 0 | WORKS | same engine as comp-denytest |
| comp-depth | active | org/modules/graph/comp_depth_cli.py | 255 | 2026-08-04 0.7.0_AE_CloudOps~F | yes | `comp-depth --help` | 0 | 1.8 | PARTIAL | help works; a bare ARN is not a subcommand and the tool prints 'unknown subcommand' yet exits 0 |
| comp-describe | active | org/modules/graph/debtscan/summary_corpus.py | 1619 | 2026-09-09 0.9.0_WK_NFRA_CLDGRPH~2 | - | `comp-describe --self-test` | 2 | 2.2 | WORKS | wrapper always prepends --describe, so `comp-describe --self-test` is unreachable (rc 2); a real describe works |
| comp-diff | active | org/modules/graph/cli.py | 1915 | 2026-09-05 0.9.0_WK_NFRA_CLDGRPH~2 | yes | `comp-diff --help` | 0 | 2.2 | PARTIAL | help only; same engine (cli.py) whose self-test passed via comp-blast |
| comp-directives | active | org/modules/graph/comp_directives.py | 514 | 2026-08-26 0.0.0_AB_MSTR | - | `comp-directives --self-test` | 0 | 2.0 | WORKS |  |
| comp-dispatch | active | org/modules/graph/comp_dispatch.py | 295 | 2026-07-10 3.0.0_SA_CVO~B | yes | `comp-dispatch --help` | 0 | 2.5 | PARTIAL |  |
| comp-drift | active | org/modules/graph/drift_cli.py | 1012 | 2026-09-03 0.8.0_AE_CloudComp~G | yes | `comp-drift --help` | 0 | 2.4 | PARTIAL |  |
| comp-dups | active | org/modules/graph/debtscan/dup_scan.py | 27 | 2026-06-26 3.0.0_SA_CVO | - | `comp-dups --help` | 0 | 0.3 | PARTIAL |  |
| comp-estate | active | .tools\comp-estate | 62 | 2026-07-30 3.0.0_SA_CVO | yes | `comp-estate --self-test` | 0 | 61.7 | WORKS | self-test 62 s (over a 90 s cap on first run? no: first run TIMEOUT at 90 s was the cap; passes in 62-90 s) |
| comp-fedobs | active | .tools\comp-fedobs | 131 | 2026-07-10 0.7.0_AE_CloudOps~C | yes | `comp-fedobs --help; comp-fedobs ` | 0;0 | 0.4 | WORKS |  |
| comp-find | active | .tools\comp-find | 753 | 2026-09-28 1.0.0_SA_CTO~Z | yes | `comp-find --help; comp-find def overlay infra/aws/globgrph --limit 3` | 0;0 | 0.7 | WORKS |  |
| comp-firmsep-sweep | active | .tools/comp-firmsep-sweep.py | 190 | 2026-08-20 0.8.0_AE_CloudComp | - | `comp-firmsep-sweep --help` | 0 | 2.2 | PARTIAL |  |
| comp-firmsep-sweep.py | active | .tools\comp-firmsep-sweep.py | 190 | 2026-08-20 0.8.0_AE_CloudComp | - | `comp-firmsep-sweep.py --help` | 0 | 0.3 | PARTIAL |  |
| comp-freshness | active | .tools\comp-freshness | 1704 | 2026-10-01 0.9.0_WK_NFRA_MCPINDEX~25 | yes | `comp-freshness self-test` | 0 | 1.8 | WORKS |  |
| comp-genesis | active | infra/system/sdk/genesis_cli.py | 437 | 2026-09-03 1.0.0_SA_CTO | - | `comp-genesis --help` | 0 | 2.8 | PARTIAL |  |
| comp-gitdrill | active | org/modules/graph/comp_gitdrill.py | 242 | 2026-07-24 3.0.0_SA_CVO~Z | - | `comp-gitdrill --self-test` | 0 | 17.9 | WORKS | self-test TIMEOUT at 90 s first run, 18 s on rerun (cold git cache) |
| comp-glob | active | .tools\comp-glob | 67 | 2026-08-28 1.0.0_SA_CTO~D | yes | `comp-glob --help` | 0 | 0.2 | PARTIAL | help only; forwards to comp-find (WORKS) |
| comp-graph | active | org/modules/graph/graph_status_cli.py | 707 | 2026-09-04 0.9.0_WK_NFRA_CLDGRPH~3 | yes | `comp-graph --help; comp-graph status` | 0;0 | 1.7 | WORKS |  |
| comp-grep | active | .tools\comp-grep | 50 | 2026-08-28 1.0.0_SA_CTO~D | - | `comp-grep --help` | 0 | 0.1 | PARTIAL | help only; forwards to comp-find (WORKS) |
| comp-heat | active | .tools\comp-heat | 1107 | 2026-10-01 0.0.0_AB_MSTR | yes | `comp-heat --help` | 0 | 0.2 | PARTIAL | help only: its live mode launches an ECS task (not exercised by design) |
| comp-honesty | active | .tools\comp-honesty | 15 | 2026-07-09 0.8.0_AE_CloudComp | - | `comp-honesty --self-test` | 0 | 0.1 | WORKS |  |
| comp-iam | active | org/modules/graph/iam_cli.py | 1785 | 2026-09-10 1.0.0_SA_CTO~Z | yes | `comp-iam census-self-test` | 0 | 1 | WORKS | offline census self-test: all cases pass |
| comp-iam-usage | active | org/modules/graph/comp_iam_usage.py | 591 | 2026-09-10 0.9.0_WK_NFRA_IAMROLES202609~1 | - | `comp-iam-usage self-test` | 0 | 1.9 | WORKS |  |
| comp-icedrill | active | org/modules/graph/comp_icedrill.py | 370 | 2026-07-14 1.0.0_SA_CTO~Z | - | `comp-icedrill --self-test` | 0 | 2.2 | WORKS |  |
| comp-imgread | active | .tools\comp-imgread | 197 | 2026-07-15 0.7.0_AE_CloudOps~A | - | `comp-imgread --help` | 0 | 0.3 | PARTIAL |  |
| comp-incrparity | active | org/modules/graph/incrparity_cli.py | 169 | 2026-07-25 0.8.0_AE_CloudComp~E | yes | `comp-incrparity --help` | 0 | 1.6 | PARTIAL |  |
| comp-keys | active | org/modules/graph/comp_keys.py | 274 | 2026-07-23 0.8.0_AE_CloudComp | yes | `comp-keys --help; comp-keys prefix s3://opal-313476888478-globgrph/fab` | 0;0 | 1.7 | WORKS |  |
| comp-kit-striplist-gate | active | .tools\comp-kit-striplist-gate | 276 | 2026-07-10 0.7.0_AE_CloudOps~C | - | `comp-kit-striplist-gate --selftest` | 0 | 0.2 | WORKS |  |
| comp-kuzu | active | infra/aws/globgrph/kuzu_cli.py | 169 | 2026-09-04 0.9.0_WK_NFRA_CLDGRPH~2 | yes | `comp-kuzu --schema; comp-kuzu MATCH (n:CloudNode) RETURN count(*)` | 0;0 | 1.9 | WORKS |  |
| comp-lambdamap | active | org/modules/graph/lambdamap_cli.py | 685 | 2026-08-04 3.0.0_SA_CVO | yes | `comp-lambdamap --help` | 0 | 1.6 | PARTIAL |  |
| comp-learns-score | active | org/modules/graph/comp_learns_score.py | 689 | 2026-08-21 0.8.0_AE_CloudComp | yes | `comp-learns-score --self-test` | 0 | 11.8 | WORKS |  |
| comp-learns-status | active | infra/aws/globgrph/comp_learns_status.py | 163 | 2026-07-10 0.8.0_AE_CloudComp~E | - | `comp-learns-status --help; comp-learns-status ` | 0;0 | 1.8 | WORKS |  |
| comp-lease | active | org/modules/graph/comp_lease.py | 572 | 2026-08-20 0.8.0_AE_CloudComp | yes | `comp-lease --self-test` | 0 | 4.0 | WORKS |  |
| comp-ledger-agreement.py | active | .tools\comp-ledger-agreement.py | 257 | 2026-08-20 1.0.0_SA_CTO~Z | - | `comp-ledger-agreement.py --help` | 0 | 0.2 | PARTIAL | TOOL_MASTER lists bare comp-ledger-agreement; only the .py exists; bare name not on PATH |
| comp-legacywriter | active | .tools\comp-legacywriter | 56 | 2026-07-29 1.0.0_SA_CTO~C | - | `comp-legacywriter --self-test` | 0 | 0.8 | WORKS |  |
| comp-manifest-check | active | org/modules/graph/manifest_check_cli.py | 1746 | 2026-09-09 0.9.0_WK_NFRA_CLDGRPH~4 | yes | `(inside .tools/commit-gate.sh today)` | 0 | 0 | WORKS | ran in-process in today's commit gates: registration-invariant PASS |
| comp-missions | active | .tools/comp_missions.py | 2 | 2026-07-28 0.0.0_AB_MSTR | - | `comp-missions --help` | 0 | 1.4 | PARTIAL |  |
| comp-ontolint | active | org/modules/graph/comp_ontolint.py | 268 | 2026-07-20 0.8.0_AE_CloudComp~C | - | `comp-ontolint self-test` | 0 | 1.8 | WORKS |  |
| comp-parity | active | org/modules/graph/comp_parity_cli.py | 314 | 2026-07-01 0.8.0_AE_CloudComp~A | yes | `comp-parity --help` | 0 | 2.3 | PARTIAL |  |
| comp-passcraft | active | org/modules/graph/comp_passcraft.py | 802 | 2026-07-12 3.0.0_SA_CVO~A | yes | `comp-passcraft --self-test` | 0 | 2.5 | WORKS |  |
| comp-perf | active | org/modules/graph/vectorize_audit_cli.py | 291 | 2026-08-20 0.8.0_AE_CloudComp | yes | `comp-perf --help` | 0 | 1.9 | PARTIAL |  |
| comp-pii | active | org/modules/graph/pii_cli.py | 833 | 2026-07-11 1.0.0_SA_CTO | yes | `comp-pii --help` | 0 | 2.1 | PARTIAL |  |
| comp-pipescript | active | org/modules/graph/pipeline_cli.py | 4193 | 2026-09-03 0.8.0_AE_CloudComp~L | yes | `comp-pipescript --help` | 0 | 2.4 | PARTIAL | help only: deployed/postdeps call AWS |
| comp-platinum | active | org/modules/graph/platinum_cli.py | 1095 | 2026-09-03 0.8.0_AE_CloudComp~L | yes | `comp-platinum --help` | 0 | 1.9 | PARTIAL | help only: may rebuild local caches |
| comp-pulse | active | org/modules/graph/comp_pulse.py | 802 | 2026-09-10 1.0.0_SA_CTO~Z | yes | `comp-pulse --self-test` | 0 | 4.6 | WORKS |  |
| comp-pydeps | active | org/modules/graph/comp_pydeps.py | 366 | 2026-07-14 1.0.0_SA_CTO~Z | - | `comp-pydeps --self-test` | 0 | 14.5 | WORKS |  |
| comp-read | active | .tools\comp-read | 1252 | 2026-09-10 1.0.0_SA_CTO~Z | yes | `comp-read --help; comp-read .tools/comp-kuzu --for what does this wrap` | 0;0 | 0.4 | WORKS |  |
| comp-registry | active | org/modules/graph/registry_cli.py | 637 | 2026-07-10 3.0.0_SA_CVO | yes | `comp-registry --help; comp-registry --help` | 0;0 | 3.6 | WORKS |  |
| comp-residue | active | org/modules/graph/residue_cli.py | 490 | 2026-07-24 1.0.0_SA_CTO~Z | yes | `comp-residue --help` | 0 | 1.8 | PARTIAL |  |
| comp-routable-check | active | .tools\comp-routable-check | 185 | 2026-07-28 0.8.0_AE_CloudComp | yes | `comp-routable-check` | 0 | 0 | WORKS | run by the parent today ~19:0xZ: RESULT PASS |
| comp-routes | active | org/modules/graph/routes_cli.py | 701 | 2026-07-24 0.8.0_AE_CloudComp~A | yes | `comp-routes --help; comp-routes behaviors` | 0;0 | 1.7 | WORKS |  |
| comp-schedule | active | .tools\comp-schedule | 1070 | 2026-10-02 1.0.0_SA_CTO~Z | yes | `comp-schedule --self-test` | 0 | 127.2 | WORKS | self-test 127 s (8/8 PASS) -- slow |
| comp-secrets | active | .tools\comp-secrets | 395 | 2026-09-21 0.9.0_WK_AMGT_RESAPP~67 | yes | `comp-secrets --help` | 0 | 0.2 | PARTIAL |  |
| comp-shell | active | org/modules/graph/shell_cli.py | 375 | 2026-04-30 1.0.0_SA_CTO | yes | `comp-shell --help` | 0 | 1.2 | PARTIAL |  |
| comp-similar | active | org/modules/graph/debtscan/comp_similar.py | 1049 | 2026-09-09 0.9.0_WK_NFRA_CLDGRPH~2 | - | `comp-similar --self-test` | 0 | 1.9 | WORKS |  |
| comp-state | active | .tools\comp-state | 29 | 2026-07-14 2.0.0_SA_COO | yes | `comp-state --self-test` | 0 | 0.7 | WORKS |  |
| comp-stitch-refresh | active | (bash publisher; derive_stitch.py + aws s3 cp) | 794 | 2026-09-10 0.9.0_WK_NFRA_CLDGRPH~2 | - | `-` | NOT-RUN | 0 | NOT-EXERCISED | HAZARD: un-retired copy of the stitch PUBLISHER (aws s3 cp to s3://opal-313476888478-globgrph/stitch/ :82-83); NFRA_CLDGRPH S29 retired .tools/stitch-refresh as a publisher (one writer: the cloud producer) but this copy still publishes. Registry says active. |
| comp-surprise | active | .tools/comp-surprise.py | 337 | 2026-10-04 1.0.0_SA_CTO~Z | - | `comp-surprise --help` | 0 | 2.0 | PARTIAL |  |
| comp-surprise.py | active | .tools\comp-surprise.py | 337 | 2026-10-04 1.0.0_SA_CTO~Z | - | `comp-surprise.py --help` | 0 | 0.2 | PARTIAL |  |
| comp-symbols | active | org/modules/graph/comp_symbols.py | 187 | 2026-06-30 0.8.0_AE_CloudComp~E | yes | `comp-symbols --help` | 0 | 1.6 | PARTIAL |  |
| comp-system | active | org/modules/graph/comp_system.py | 2164 | 2026-09-03 0.8.0_AE_CloudComp~N | yes | `comp-system --help; comp-system --check` | 0;2 | 1.6 | WORKS | --check rc 2 = STALE (a valid result: infra/system 06 drifted again after today's commits) |
| comp-tagauthz | active | .tools/comp-tagauthz.py | 425 | 2026-10-08 0.9.0_WK_IRPT_BCKEND~173 | yes | `comp-tagauthz --help` | 0 | 1.6 | PARTIAL |  |
| comp-tagauthz.py | active | .tools\comp-tagauthz.py | 425 | 2026-10-08 0.9.0_WK_IRPT_BCKEND~173 | yes | `comp-tagauthz.py --help` | 0 | 0.2 | PARTIAL |  |
| comp-to | active | (bash only) | 33 | 2026-09-03 1.0.0_SA_CTO | yes | `-` | NOT-RUN | 0 | NOT-EXERCISED | setter: writes org/mcp/sessions/<sid>.to_id; no read-only path |
| comp-tool-health | active | org/modules/graph/comp_tool_health.py | 856 | 2026-07-12 0.8.0_AE_CloudComp | yes | `comp-tool-health --self-test` | 0 | 26.4 | WORKS |  |
| comp-tool-health-gate | active | org/modules/graph/comp_tool_health_gate.py | 358 | 2026-07-12 0.8.0_AE_CloudComp | - | `comp-tool-health-gate --self-test` | 0 | 28.0 | WORKS |  |
| comp-toolgraph | active | org/modules/graph/comp_toolgraph.py | 806 | 2026-07-12 0.8.0_AE_CloudComp | - | `comp-toolgraph --self-test` | 0 | 1.5 | WORKS |  |
| comp-tooltip | active | org/modules/graph/tooltip_cli.py | 263 | 2026-07-10 3.0.0_SA_CVO | yes | `comp-tooltip summary` | 0 | 2.5 | WORKS |  |
| comp-trace | active | org/modules/graph/cli.py | 1915 | 2026-09-05 0.9.0_WK_NFRA_CLDGRPH~2 | yes | `comp-trace --help` | 0 | 2.2 | PARTIAL | help only; same engine (cli.py) whose self-test passed via comp-blast |
| comp-transform | active | org/modules/graph/transform_cli.py | 981 | 2026-07-10 3.0.0_SA_CVO~A | yes | `comp-transform --help` | 0 | 1.9 | PARTIAL |  |
| comp-trigger | active | org/modules/graph/comp_trigger.py | 714 | 2026-09-09 1.0.0_SA_CTO~Z | yes | `comp-trigger --self-test` | 0 | 1.8 | WORKS |  |
| comp-types | active | org/modules/graph/types_cli.py | 556 | 2026-07-25 0.8.0_AE_CloudComp~A | yes | `comp-types --help` | 0 | 1.5 | PARTIAL |  |
| comp-v5-composite-test.sh | - | infra/aws/lambda/v2_portal/01_market_overview/lambdas/market-overview-tiered-generator/lambda_function.py | 586 | 2026-06-16 0.7.0_AE_CloudOps | yes | `-` | NOT-RUN | 0 | NOT-EXERCISED | a one-off live Lambda composite test (boto3 at module top), not a comp-tool; no registry status; bare name not on PATH |
| comp-validate | active | org/modules/graph/validate_cli.py | 952 | 2026-07-23 0.8.0_AE_CloudComp | yes | `comp-validate --help` | 0 | 1.7 | PARTIAL |  |
| comp-which | active | .tools\comp-which | 2764 | 2026-10-08 4.0.0_SA_CRO | yes | `comp-which who else is working on this terraform folder` | 0 | 1.3 | WORKS |  |
| comp-which-routing-test.py | active | .tools\comp-which-routing-test.py | 1739 | 2026-09-10 0.9.0_WK_NFRA_COMPEFFICACY~2 | - | `-` | NOT-RUN | 0 | WORKS | not re-run (>10 min); the parent ran it today ~19:0xZ: VERDICT PASS; bare name in TOOL_MASTER not on PATH |
| comp-whoread | active | .tools/comp-whoread.py | 179 | 2026-07-11 3.0.0_SA_CVO~A | - | `comp-whoread --help` | 0 | 1.4 | PARTIAL |  |
| comp-whoread.py | active | .tools\comp-whoread.py | 179 | 2026-07-11 3.0.0_SA_CVO~A | - | `comp-whoread.py --help` | 0 | 0.1 | PARTIAL |  |
| comp-xray | active | infra/aws/compdiff/cli.py | 302 | 2026-07-10 0.7.0_AE_CloudOps~C | yes | `comp-xray --help` | 0 | 2.1 | PARTIAL |  |
| comp-xref | active | org/modules/graph/cli.py | 1915 | 2026-09-05 0.9.0_WK_NFRA_CLDGRPH~2 | yes | `comp-xref --help; comp-xref --check` | 0;0 | 2.7 | WORKS |  |

## Not read / not done

- PARTIAL tools were not exercised beyond `--help`: their real paths call AWS, rebuild caches, scan the whole repo, or need arguments whose safety was not established. PARTIAL means 'loads', not 'works'.
- comp-which-routing-test.py was not re-run (taken from the parent's run today).
- Test files are matched by file-name stem only (`test?` column); a test elsewhere under another name is missed.
- Usage (who runs each tool, how often) is the other slice; nothing here says a WORKS tool is used.
- Other boxes (dell1, dell2, site Z) were not checked; results are the laptop's.
