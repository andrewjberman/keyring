# THE ARCHIVE-TIER CENSUS -- every comp-tool entrypoint on disk, joined against usage, registries and invokers (2026-09-04T14:37Z)

**Authority:** Andrew-direct at the 3.0.0_SA_CVO terminal 2026-09-04 ~13:3xZ, VERBATIM "approve all recs" on /open-calls card 2 ("The archive-tier census: authorize it, yes or no?" REC yes). Record `org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260904_133xZ_APPROVE_ALL_RECS_ESTATE_SITTING_ARCHIVE_CENSUS_COMPWHICH_F2.md@16a1f47ec1`; the draft v2 @c9785fb9e2 section 4 defined the act. **This census decides nothing and retires nothing:** it names the set an archive tier would hold, for his word.

## Denominators (every number beside its frame)

- Universe: **96 extensionless `.tools/comp-*` entrypoints** on disk at HEAD's worktree (8 `.py` siblings not counted as entrypoints). The registries' own universe is `comp-coverage-map.yaml`; disk is used here because an unregistered tool is one of the findings.
- Instrument 1, `org/mcp/comp-tool-runs.jsonl`: 29,945 rows total, 0 unparseable, **15,599 in the trailing 30 days** (ts_epoch); a run counts for the `tool` field it names.
- Instrument 2, `org/mcp/comp-which-rail.log`: 51,397 rows total, **22,021 in the trailing 30 days** (the leading timestamp); a mention counts for every `tool=` token on the row (routing intent as well as invocation, so it OVER-counts use and under-counts nothing).
- Invokers scanned, word-boundary match on the tool name: 74 skill files, 12 hooks, 49 gate/check/safe-* tools, `.tools/comp-which` (the curated rules), 1 agent types, CLAUDE.md, and the estate-report runner (NOT FOUND at either known path).
- Registries: `comp-coverage-map.yaml`, `graph-call-manifest.yaml`, `comp-tools.yaml` (the last is a curated subset by its own header and is not a census).

## The verdict (three classes, MECE over the universe)

| class | count | meaning |
|---|---|---|
| ACTIVE | 48 | at least one run in 30 days on either instrument |
| ZERO-RUN, INVOKED | 37 | no run in 30 days, but a skill, hook, gate, the router, an agent type, CLAUDE.md or the runner names it -- retiring it breaks a caller |
| **ARCHIVE-CANDIDATE** | **11** | no run in 30 days AND no invoker found -- the set an archive tier would hold |

Unregistered in every registry: 0 of 96 -- none.

## ARCHIVE-CANDIDATE, by name (kept, not deleted; off the route table; no battery obligation -- if he says so)

| tool | registered in | note |
|---|---|---|
| `comp-arity` | coverage-map, call-manifest | 0 runs / 0 rail mentions in 30d; no invoker |
| `comp-canon-motif` | coverage-map, call-manifest | 0 runs / 0 rail mentions in 30d; no invoker |
| `comp-claimlink` | coverage-map, call-manifest | 0 runs / 0 rail mentions in 30d; no invoker |
| `comp-coverage` | coverage-map, call-manifest | 0 runs / 0 rail mentions in 30d; no invoker |
| `comp-imgread` | coverage-map, call-manifest | 0 runs / 0 rail mentions in 30d; no invoker |
| `comp-missions` | coverage-map, call-manifest, comp-tools.yaml | 0 runs / 0 rail mentions in 30d; no invoker |
| `comp-passcraft` | coverage-map, call-manifest | 0 runs / 0 rail mentions in 30d; no invoker |
| `comp-perf` | coverage-map, call-manifest | 0 runs / 0 rail mentions in 30d; no invoker |
| `comp-residue` | coverage-map, call-manifest | 0 runs / 0 rail mentions in 30d; no invoker |
| `comp-stitch-refresh` | coverage-map, call-manifest | 0 runs / 0 rail mentions in 30d; no invoker |
| `comp-v5-composite-test.sh` | call-manifest | 0 runs / 0 rail mentions in 30d; no invoker |

## ZERO-RUN, INVOKED, by name (do not archive on usage alone -- a caller exists)

| tool | invoked by | registered in |
|---|---|---|
| `comp-axes` | skill:comp-adversary, comp-which | coverage-map, call-manifest, comp-tools.yaml |
| `comp-chainrun` | comp-which | coverage-map, call-manifest, comp-tools.yaml |
| `comp-clobber` | comp-which | coverage-map, call-manifest |
| `comp-coverage-check` | gate/tool, comp-which | coverage-map, call-manifest |
| `comp-deadgrant` | comp-which | coverage-map, call-manifest |
| `comp-depth` | comp-which | coverage-map, call-manifest |
| `comp-dispatch` | comp-which | coverage-map, call-manifest |
| `comp-dups` | comp-which | coverage-map, call-manifest, comp-tools.yaml |
| `comp-fedobs` | gate/tool, comp-which | coverage-map, call-manifest |
| `comp-firmsep-sweep` | comp-which | coverage-map, call-manifest |
| `comp-freshness` | skill:prd-delta, hook, comp-which, CLAUDE.md | coverage-map, call-manifest, comp-tools.yaml |
| `comp-genesis` | comp-which | coverage-map, call-manifest |
| `comp-gitdrill` | comp-which | coverage-map, call-manifest |
| `comp-heat` | hook, comp-which | coverage-map, call-manifest, comp-tools.yaml |
| `comp-honesty` | gate/tool | coverage-map, call-manifest |
| `comp-iam-usage` | comp-which | coverage-map, call-manifest |
| `comp-incrparity` | comp-which | coverage-map, call-manifest |
| `comp-kit-striplist-gate` | gate/tool | coverage-map, call-manifest |
| `comp-learns-score` | comp-which | coverage-map, call-manifest |
| `comp-learns-status` | comp-which | coverage-map, call-manifest |
| `comp-parity` | comp-which | coverage-map, call-manifest, comp-tools.yaml |
| `comp-pii` | skill:cloud-ops, gate/tool, comp-which | coverage-map, call-manifest, comp-tools.yaml |
| `comp-routable-check` | gate/tool | coverage-map, call-manifest |
| `comp-schedule` | skill:comp-schedule, hook, gate/tool | coverage-map, call-manifest |
| `comp-secrets` | gate/tool, comp-which | coverage-map, call-manifest |
| `comp-shell` | gate/tool | coverage-map, call-manifest, comp-tools.yaml |
| `comp-state` | skill:daily-sprint, comp-which | coverage-map, call-manifest |
| `comp-symbols` | comp-which | coverage-map, call-manifest |
| `comp-tagauthz` | gate/tool, comp-which | coverage-map, call-manifest |
| `comp-to` | hook, comp-which | coverage-map, call-manifest |
| `comp-tool-health` | gate/tool, comp-which | coverage-map, call-manifest |
| `comp-tool-health-gate` | gate/tool | coverage-map, call-manifest |
| `comp-toolgraph` | comp-which | coverage-map, call-manifest |
| `comp-tooltip` | comp-which | coverage-map, call-manifest, comp-tools.yaml |
| `comp-types` | comp-which | coverage-map, call-manifest, comp-tools.yaml |
| `comp-whoread` | comp-which | coverage-map, call-manifest |
| `comp-xref` | gate/tool, comp-which | coverage-map, call-manifest, comp-tools.yaml |

## ACTIVE, by traffic (30d runs / rail mentions)

| tool | runs | rail | invoked by |
|---|---|---|---|
| `comp-which` | 736 | 8,177 | skill:atom-decomp, hook, gate/tool, comp-which, CLAUDE.md |
| `comp-pulse` | 8,405 | 0 | skill:comp-adversary, gate/tool, comp-which |
| `comp-read` | 1,560 | 3,488 | skill:comp-adversary, hook, gate/tool, comp-which, agent-type, CLAUDE.md |
| `comp-find` | 599 | 4,360 | skill:mstr-spawn, hook, gate/tool, comp-which, agent-type, CLAUDE.md |
| `comp-kuzu` | 1,529 | 0 | skill:molecule, gate/tool, comp-which |
| `comp-system` | 619 | 0 | gate/tool, comp-which |
| `comp-pipescript` | 475 | 0 | skill:cloud-ops, hook, gate/tool, comp-which |
| `comp-estate` | 316 | 0 | skill:gold-runner-code-review, hook, comp-which, CLAUDE.md |
| `comp-grep` | 0 | 271 | gate/tool, comp-which, CLAUDE.md |
| `comp-blast` | 201 | 0 | skill:cloud-ops, gate/tool, comp-which |
| `comp-iam` | 158 | 0 | skill:cloud-ops, hook, gate/tool, comp-which |
| `comp-adversary` | 107 | 0 | skill:comp-adversary, gate/tool |
| `comp-manifest-check` | 88 | 0 | skill:prod-deploy, gate/tool, comp-which |
| `comp-trigger` | 78 | 0 | comp-which |
| `comp-keys` | 54 | 0 | - |
| `comp-glob` | 0 | 44 | gate/tool, comp-which |
| `comp-directives` | 42 | 0 | skill:directives-check, gate/tool |
| `comp-routes` | 42 | 0 | skill:cloud-ops, hook, gate/tool, comp-which |
| `comp-cache` | 37 | 0 | skill:cloud-ops, hook, gate/tool, comp-which |
| `comp-similar` | 36 | 0 | comp-which |
| `comp-surprise` | 35 | 0 | skill:canonical-flow, hook |
| `comp-transform` | 35 | 0 | skill:cloud-ops, hook, gate/tool, comp-which |
| `comp-validate` | 30 | 0 | skill:cloud-ops, gate/tool, comp-which |
| `comp-closure` | 28 | 0 | skill:agentbus, comp-which |
| `comp-cochange` | 25 | 0 | skill:comp-adversary |
| `comp-dataflow` | 21 | 0 | gate/tool |
| `comp-lease` | 17 | 0 | skill:comp-schedule, comp-which |
| `comp-trace` | 14 | 0 | skill:cloud-ops, gate/tool, comp-which |
| `comp-lambdamap` | 12 | 0 | comp-which |
| `comp-platinum` | 11 | 0 | skill:cloud-ops, gate/tool, comp-which |
| `comp-xray` | 11 | 0 | comp-which |
| `comp-pydeps` | 9 | 0 | comp-which |
| `comp-aws` | 8 | 0 | hook, gate/tool, comp-which |
| `comp-atomcheck` | 7 | 0 | gate/tool |
| `comp-constants` | 7 | 0 | gate/tool, comp-which |
| `comp-debris` | 7 | 0 | comp-which |
| `comp-denytest` | 7 | 0 | comp-which |
| `comp-diff` | 3 | 0 | gate/tool, comp-which |
| `comp-assets` | 2 | 0 | comp-which |
| `comp-drift` | 2 | 0 | comp-which |
| `comp-icedrill` | 2 | 0 | comp-which |
| `comp-legacywriter` | 2 | 0 | comp-which |
| `comp-build` | 1 | 0 | skill:cloud-ops, gate/tool, comp-which |
| `comp-cluster` | 1 | 0 | comp-which |
| `comp-describe` | 1 | 0 | comp-which |
| `comp-graph` | 1 | 0 | skill:cloud-ops, hook, gate/tool, comp-which |
| `comp-ontolint` | 1 | 0 | comp-which |
| `comp-registry` | 1 | 0 | skill:cloud-ops, comp-which |

## The phantom invoker of a retired tool (v1's finding, closed or not)

`comp-surface-check` was RETIRED 2026-08-06 by Andrew-direct. This census: **202 runs in the trailing 30 days**; on disk: no; callers found by word-boundary scan: .claude/skills\prod-deploy\SKILL.md, .tools\commit_gate_runner.py, .tools\safe-commit.legacy-golden.sh, .tools\safe-commit.sh, .tools/comp-which, CLAUDE.md.

## What this census cannot see (stated, not hidden)

- A caller outside the scanned set: a script under `data/`, `infra/` or a seat's lane that shells a comp-tool by name. The scan covers the estate's LAW carriers and routers, not every file; a name-list from usage alone is exactly the error the draft named, so an archive act would run one `comp-find` per candidate over the whole corpus first.
- runs.jsonl counts only tools that emit to it (the unit-1 class); the rail log counts routing intent. Both are printed so neither stands alone.
- Codex-runtime invocations since the 21:0xZ reap are zero by construction; the window still reaches back into their era.

-- 3.0.0_SA_CVO
