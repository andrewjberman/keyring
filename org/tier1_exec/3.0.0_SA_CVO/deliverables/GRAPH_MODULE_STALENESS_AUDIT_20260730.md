# GRAPH MODULE STALENESS AUDIT -- org/modules/graph/ (2026-07-30, Andrew-commissioned)

**Method:** 9-agent Sonnet fan-out (workflow wf_26453974-5ea), 4 top-level file batches +
5 subtree units; every verdict evidence-cited (git last-touch, bounded consumer sweep,
file:line staleness). 187 units over 685 files. Read-only; NOTHING deleted -- deletions
await Andrew sign-off. Consumer claims are BOUNDED-SWEEP statements, not proofs of absence.

**Verdict counts:** {'NECESSARY': 140, 'GENERATED': 8, 'HISTORICAL-KEEP': 19, 'TRASH-CANDIDATE': 15, 'AT-RISK': 5}

## AT-RISK -- live-consumed AND silently decaying (the dangerous quadrant)

### org/modules/graph/shadow-detect/
- purpose: On-demand output of `comp-pipescript shadow-detect` (pipeline_cli.py:2797-2930, .tools/comp-pipescript wrapper): walks a named function's body and enumerates its post-condition lock-in chain (dropna/astype/merge/sort_values/groupby) into a per-function YAML manifest.
- last_touch: d0e2226b88 2026-06-11 0.7.0_AE_CloudOps
- consumers: only the writer (pipeline_cli.py:cmd_shadow_detect) references the dirname in the bounded sweep; no gate reads the manifests back
- STALE: shadow-detect/D_04.client_portal_summary.compute_hh_lifecycle.yaml:1-3 names path `data/inf/scripts/gold/D_04.client_portal_summary.py` -- that file DOES NOT EXIST on disk; the script was renamed to `INF_D_04.client_portal_summary.py` (confirmed via ls, and the sibling function is now found there)
- STALE: same file's func_lines: 339-420 no longer matches: `_compute_hh_lifecycle` is now defined at INF_D_04.client_portal_summary.py:999 in a file that has grown to 4378 lines (last touched 2026-07-13, after this 2026-06-11 manifest) -- both the path AND the line range are dead pointers
- note: flagged AT-RISK rather than plain GENERATED because this specific manifest is the exact dangerous shape the audit is hunting for: a dated snapshot naming a since-renamed, since-massively-grown file with no refresh mechanism -- an agent or human trusting this YAML as a live pointer into the lock-in chain would look at the wrong file and the wrong lines. No code gate depends on it (bounded sweep found none), so the blast radius is confined to manual/agent misdirection, not a runtime break; the other 2 files in this dir (INF_D_00c.portal_leaderboard.*, INF_D_02.advisor_client_detail.*) DO still resolve to live paths -- only the D_04 one is stale.

### org/modules/graph/comp_route_affinity_ic.py
- purpose: Intent-conditioned affinity provider (charter-2): extends learned affinity from per-(cap,role) to per-(cap,role,intent-class), explicitly SHADOW pending a CTO flip-gate.
- last_touch: 3bbe4e7ba3 2026-07-07 0.8.0_AE_CloudComp~E
- consumers: none found anywhere in org/.tools/docs bounded sweep except its own file and 07-07-dated inbox mail -- specifically NOT imported by comp_route.py, so its class IntentConditionedAffinityProvider never reaches the live router
- STALE: self-declared 'SHADOW until that cert + CTO's flip-gate' (line 18) with zero evidence in this sweep that the cert/flip ever happened or was ever revisited after 07-07 -- a built, never-wired charter-2 deliverable that could be silently forgotten rather than deliberately shelved
- note: AT-RISK in the sense that it's presented as a live design decision awaiting a gate that may have simply been dropped; worth a one-line CTO check on whether charter-2 intent-conditioning is still wanted.

### org/modules/graph/comp_route_outcome.py
- purpose: Charter-2 route->run OUTCOME capture: joins a route decision to the agent's subsequent tool runs, classifying TOOK-AND-SUFFICED vs REJECTED (anti-compliance-confound signal).
- last_touch: ac678ed89d 2026-07-13 1.0.0_SA_CTO~Z
- consumers: its ONLY consumer is comp_route_affinity_ic.py (line 38, 'from comp_route_outcome import capture_outcomes'), which is itself the unwired SHADOW module above -- so this file's real-world effect is currently zero
- STALE: built as a live signal-capture pipeline but the only thing that reads its output is a module nothing else imports; a silently-orphaned charter-2 pair
- note: Same charter-2 flip-gate question as comp_route_affinity_ic.py applies here -- these two files rise or fall together.

### org/modules/graph/critical-surfaces.yaml
- purpose: The production guardrail registry (NFRA_GRAPHS D8) naming client-facing surfaces (Model Portfolios, Advisor Intelligence, etc.) whose backend subgraph is carved, signed, and commit-gated by comp-surface-check.
- last_touch: 95e8df1dd0 2026-07-08 2.0.0_SA_COO~B
- consumers: surface_check_cli.py (portal-enforced blocking gate per CLAUDE.md rule 20), resign_surface_baseline.py, comp_promote_materializer.py, estate_infrastructure_cli.py, .tools/drift_producer.py
- STALE: File self-declares 'STATUS: v0.3 (CTO carve-review 2026-06-12; v0.2 paths VERIFIED against the live portal submodule 2026-06-11)' -- a hand-dated verification ~7 weeks stale relative to today, with no visible auto-refresh beyond the manual resign_surface_baseline.py path.
- note: Live-enforced blocking gate (SEV1, must-always-be-right per CLAUDE.md) whose frontend-carve paths were last human-verified 2026-06-11/12 -- exactly the dangerous quadrant (dated baseline + live consumer); worth a fresh carve-review given ~7 weeks of portal changes since.

### org/modules/graph/adapter_audit_cli.py
- purpose: comp-adapter-audit backend: portal adapter field-threading audit vs the live S3 envelope, scoped to 19 of 122 exported adapters (one bucket/firm/layer).
- last_touch: 4822bf63d0 2026-07-10 3.0.0_SA_CVO
- consumers: .tools/comp-adapter-audit wrapper (live)
- STALE: Lines 11-14: the tool's own coverage denominator ('Of 122 exported adapters... this tool can audit 19... 96 adapters are Lambda-backed... 7 more serve static .json from a path shape this tool does not model') is a hand-frozen census dated 2026-07-10 with no stated re-census trigger -- if portal endpoints grew or shifted since, the coverage fraction silently under- or over-states what is actually checked
- note: Live-consumed AND the coverage claim decays silently as the portal evolves -- exactly the dangerous AT-RISK quadrant: nothing forces a re-census when adapter count changes.

## TRASH-CANDIDATE -- deletion manifest (await sign-off)

### org/modules/graph/tsgraph_spike/node_modules/
- purpose: bun/ts-morph (^28.0.0) dependency install supporting local runs of the spike's *.ts extractor/measurement scripts.
- last_touch: UNTRACKED (gitignored via org/modules/graph/tsgraph_spike/.gitignore:2 'node_modules/'; not in git ls-files)
- consumers: bun resolves it for extractor.ts/extractor_full.ts/smoke.ts/measure_full.ts/field_parity_check.ts only if someone re-runs the spike locally; no deployed pipeline touches it.
- note: 15MB, local-device-only build output; safe to delete -- regenerable via `bun install` from the tracked package.json + bun.lock (bun.lock itself is also gitignored/untracked, .gitignore:3).

### org/modules/graph/tsgraph_spike/out/scratch_kuzu_db/ + out/scratch_clusters_db/
- purpose: Local scratch Kuzu graph databases used to validate P0/P2-1 Cypher query shapes before AE materialized the real layer into the canonical Nessie->Kuzu graph.
- last_touch: UNTRACKED (scratch_kuzu_db gitignored explicitly at .gitignore:3; scratch_clusters_db caught by a broader root-level `out/` gitignore rule, confirmed via git check-ignore)
- consumers: none found beyond the two loader scripts (load_scratch_kuzu.py, load_clusters_scratch.py) that build them for local testing.
- STALE: load_clusters_scratch.py:6-8 self-documents as 'SCRATCH / frozen vintage (Rule 20): local-load only; the real Nessie write is AE-owned' -- exactly the class of frozen-vintage DB CLAUDE.md Rule 20 warns never to quote as 'the estate'.
- note: 20M + 17M = 37MB local-only; safe to delete, regenerable by re-running the loader scripts against the tracked out/*.graph.json producer files if the spike is ever revisited.

### org/modules/graph/tsgraph_spike/org/mcp/agent_telemetry/0.4.0_DE_ClientPlatform.jsonl
- purpose: Misrouted PostToolUse agent-telemetry JSONL for 0.4.0_DE_ClientPlatform, written here because the telemetry hook resolved its output path relative to cwd instead of the workspace root while an agent worked inside this subdir.
- last_touch: UNTRACKED, filesystem mtime 2026-06-30 18:46 (not a git artifact)
- consumers: none -- it is a stray duplicate/shadow of the real org/mcp/agent_telemetry/0.4.0_DE_ClientPlatform.jsonl at the workspace root; nothing reads telemetry from inside a tool subdirectory.
- STALE: the dir's own .gitignore:8-9 carries a rule specifically to keep this bug-class out of git ('misrouted PostToolUse telemetry (hook writes relative to cwd; real root is workspace root)') -- a named, self-acknowledged recurring artifact, not a one-off.
- note: 26KB, device-local, safe to delete. If the underlying hook cwd-resolution bug is still live, this class will recur in other subdirs too -- worth a note to whoever owns the telemetry hook, out of scope for this file-level audit.

### org/modules/graph/nerves_traffic.py
- purpose: NFRA_NERVES L2 'universal traffic record': reads rail/runs/git/telemetry streams, addresses each event via nerves_resolve, and would append to org/mcp/nerves-traffic.jsonl.
- last_touch: 14c5abf917 2026-07-14 1.0.0_SA_CTO~Z
- consumers: none found in bounded sweep -- not imported by nerves_accrete.py, nerves_lexical.py, or comp_pulse.py (all of which read git/rail directly instead); no .tools wrapper; its own sink file org/mcp/nerves-traffic.jsonl does not exist on disk (never run to completion); 0 hits for its name in comp-tool-runs.jsonl or comp-which-rail.log.
- STALE: docstring frames itself as the module 'every other NERVES layer is a function of' (line 7-10), but nerves_accrete.py and nerves_lexical.py both bypass it and derive from git/nerves_resolve directly -- a declarative mismatch between the claimed architecture and the real import graph, confirmed by CTO~Z's own 2026-07-14/24 inbox trail describing it as verified but not wired into L3.
- note: Built + self-tested at NFRA_NERVES L2 commissioning (2026-07-14, CVO~Z verified 'SOUND') but zero downstream consumer ever materialized and its own output artifact has never been produced -- safe to delete or fold away pending an explicit decision to actually wire it into comp-pulse/nerves_accrete, since nothing currently depends on it.

### org/modules/graph/coverage-report/
- purpose: Tool-output snapshot (REPORT.md + 61 per-agent yamls) from `comp-coverage report --write`: a TO-compliance audit (which completed Task Orders got logged to org/compiler-tools-log.md), classified FRONTEND/GOLD/API/DOC.
- last_touch: 702fe31c55 2026-05-14 1.0.0_SA_CTO
- consumers: none found in bounded sweep (grep for 'coverage-report' outside the dir hits only inbox-message mentions and its own generator coverage_cli.py, which only WRITES to it, never reads it back)
- STALE: (b)/(e) REPORT.md self-labels 'Generated: 2026-05-15' and shows 'Raw coverage: 8.4%' -- but commit 33146f0297 (2026-07-10, CVO~B) proved that headline was a match ARTIFACT and the true number is 17.1% (itself flagged a lower bound pending a TO-ID convention fix); the committed file was never regenerated to reflect this, so it reads as current when it is a known-superseded number.
- STALE: (c)/(e) that same commit made `comp-coverage report` STDOUT-ONLY by default specifically to stop this directory's git churn (file writes now opt-in via --write) -- i.e. the tool was redesigned around NOT maintaining this tracked snapshot, and per a 2026-07-10 CVO/COO thread the fix-then-write+commit was deliberately deferred pending the TO-ID fix. 20 days later (today 2026-07-30) it is still unregenerated and the recommended gitignore-pending-consumer-blast-check was never actioned.
- STALE: consumer blast-check (asked for by CVO 20260710T201332Z, routed to CTO, apparently never completed): I ran it -- zero readers found besides the generator itself.
- note: Safe to delete/gitignore: fully regenerable via `.tools/comp-coverage report --write` (or read live via stdout, no --write) whenever anyone actually needs this metric, and the frozen committed copy is presently a stale, known-wrong number sitting in git looking authoritative. If kept, at minimum re-run --write once the TO-ID fix lands, or add a 'STALE SNAPSHOT, see 33146f0297' banner.

### org/modules/graph/corpus.py
- purpose: Two-tier (JSON+DuckDB/parquet) query engine for federal-contractor entity data against s3://corporeal-agg -- ported verbatim from the separate 'corporeal' codebase, unrelated to Opal's own estate.
- last_touch: 98dd7b1f1e 2026-04-07 1.0.0_SA_CTO (commit msg: 'Port 14 deterministic compiler modules from corporeal-dev into org/modules/')
- consumers: none found in bounded sweep -- the only `import corpus` hits (compproof/blind_run.py, compproof/harness.py) resolve to the sibling compproof/corpus.py via an explicit sys.path.insert, not this file
- STALE: Domain mismatch: docstring is about UEI/contractor S3 lookups, has nothing to do with org/modules/graph's estate-ontology purpose -- confusing to a reader auditing this directory.
- note: Zero real consumers ~4 months after landing; safe to delete or relocate out of org/modules/graph (was an intentional cross-project port per the commit message, not an accident, but never got wired into anything here).

### org/modules/graph/execution_graph.py
- purpose: A LangGraph StateGraph wiring architect->coordinator->workers->reviewer for Tier-1 project execution -- ported from the separate 'corporeal' codebase's compiler-module set, unrelated to Opal's dependency graph.
- last_touch: 98dd7b1f1e 2026-04-07 1.0.0_SA_CTO (commit msg: 'Port 14 deterministic compiler modules from corporeal-dev')
- consumers: none found in bounded sweep (only hits are __pycache__, old message-archive/inbox mentions, and a missions commit-log entry)
- STALE: Domain mismatch: this is a LangGraph agent-orchestration graph, not the org/modules/graph estate-dependency graph the rest of this directory implements.
- note: 48.9KB of unreferenced code sitting in the estate-graph directory since April; no wrapper, no importer -- safe to delete or relocate.

### org/modules/graph/graph_compiler.py
- purpose: Three-tier (per-entity/cross-entity/temporal-diff) corpus semantic graph compiler for federal-contractor entities -- ported from the separate 'corporeal' codebase, mirrors a different project's compile.py.
- last_touch: 98dd7b1f1e 2026-04-07 1.0.0_SA_CTO (commit msg: 'Port 14 deterministic compiler modules from corporeal-dev')
- consumers: none found in bounded sweep (only __pycache__, an old inbox message, a missions commit-log entry, and one unrelated doc mention)
- STALE: Domain mismatch, same as corpus.py/execution_graph.py: contractor/entity graph compiler, not Opal's estate-dependency graph.
- note: 59.3KB unreferenced since April, same dead-port batch as corpus.py and execution_graph.py (all 3 landed in one commit, none ever wired in); safe to delete or relocate together.

### org/modules/graph/comp-constants-seed-bd.yaml
- purpose: One-time bootstrap seed file (BD-lane canonical constants + hardcode sites) folded into the live comp-constants.config.yaml at authoring time (2026-05-08).
- last_touch: 290476bbf3 2026-05-08 0.4.0_DS_ClientPlatform~B
- consumers: none at runtime -- comp_constants_cli.py's DEFAULT_CONFIG_PATH resolves to <workspace-root>/comp-constants.config.yaml, never to this file (confirmed by reading the CLI's lane-resolution code, which never opens an org/modules/graph path); the root config's own header says 'bootstrap from SEED-{BD,INF,MULTIFIRM} YAMLs' (past tense) plus 'Re-derive from current AST scan'
- note: Deletion is safe -- content was already merged into comp-constants.config.yaml, which self-regenerates via `comp-constants index`; no unique information would be lost.

### org/modules/graph/comp-constants-seed-cot.yaml
- purpose: Bootstrap seed adding the Cottonwood ('cot') lane to comp-constants, filed as a WSE_COTMDL WS-4 unblock; the header itself narrates a real architecture finding (FIRM_ID cannot represent a 4th firm without a tool change).
- last_touch: ac099e4be3 2026-07-22 2.0.0_SA_COO
- consumers: none at runtime -- same DEFAULT_CONFIG_PATH finding as the BD/INF/multifirm siblings applies; commit ac099e4be3's message duplicates the narrative in full
- STALE: File's own line 2 claims 'Consumed by comp-constants (`comp-constants check --lane cot`)' -- traced and found FALSE for the live code path; the tool reads comp-constants.config.yaml at workspace root, never this file, by the time --lane cot resolves
- note: Deletion is safe: the unique architectural finding in this file's header is fully preserved verbatim in git commit ac099e4be3's message, so no information loss.

### org/modules/graph/comp-constants-seed-inf.yaml
- purpose: One-time bootstrap seed file (INF-lane canonical constants + hardcode sites) folded into comp-constants.config.yaml at authoring time.
- last_touch: d0e2226b88 2026-06-11 0.7.0_AE_CloudOps
- consumers: none at runtime -- same DEFAULT_CONFIG_PATH finding as comp-constants-seed-bd.yaml applies
- note: Deletion is safe; content already merged into comp-constants.config.yaml, which self-regenerates.

### org/modules/graph/comp-constants-seed-multifirm.yaml
- purpose: One-time bootstrap seed file (shared/multi-firm-tree constant lane) folded into comp-constants.config.yaml at authoring time.
- last_touch: d1be501859 2026-05-08 0.4.0_DS_ClientPlatform~D
- consumers: none at runtime -- same DEFAULT_CONFIG_PATH finding applies
- note: Deletion is safe; content already merged into comp-constants.config.yaml, which self-regenerates.

### org/modules/graph/debtscan/org/
- purpose: Accidental nested directory: org/mcp/agent_telemetry/0.8.0_AE_CloudComp.jsonl, created when some tool/hook ran with cwd=org/modules/graph/debtscan instead of the workspace root and wrote its relative 'org/mcp/agent_telemetry/<serial>.jsonl' path here instead of the real org/mcp/agent_telemetry/ at repo root.
- last_touch: UNTRACKED (gitignored by .gitignore:415 `**/org/`, never committed)
- consumers: none found in bounded sweep -- gitignored, invisible to any tool that reads the real org/mcp/agent_telemetry/*.jsonl stream (e.g. comp_debt/signals/usage.py)
- STALE: Instance of a systemic cwd-bug: this exact shape recurs at org/modules/graph/aws-shapes/org/ and org/modules/graph/org/ (see those entries) -- 11 telemetry files total across 3 locations, all silently shadowed off the real telemetry stream.
- note: Safe to delete (1KB, gitignored, no consumer); the higher-value fix is finding and correcting whatever hook/script writes agent_telemetry with a relative path instead of an absolute workspace-root path, since it is quietly under-counting invocations for the usage signal that comp_debt/signals/usage.py relies on.

### org/modules/graph/aws-shapes/org/
- purpose: Same accidental-nested-org-dir bug as debtscan/org/ -- org/mcp/agent_telemetry/ with 2 files (0.7.0_AE_CloudOps~B.jsonl, 3.0.0_SA_CVO~A.jsonl), created by a hook running with cwd inside aws-shapes/.
- last_touch: UNTRACKED (gitignored by .gitignore:415 `**/org/`)
- consumers: none found in bounded sweep
- STALE: Same systemic cwd-relative-path defect as debtscan/org/ and org/modules/graph/org/ -- see debtscan/org/ entry for the cross-cutting risk note.
- note: Safe to delete; ~5KB, gitignored, no consumer.

### org/modules/graph/org/
- purpose: The largest instance of the same accidental nested-org-dir bug: org/mcp/agent_telemetry/ holding 8 separate agent-serial .jsonl telemetry files (0.4.0_DE, 0.4.0_DS~B, 0.7.0_AE_CloudOps, 0.8.0_AE_CloudComp x2, 1.0.0_SA_CTO~Z, 3.0.0_SA_CVO x2) -- all written because some tool/hook resolved 'org/mcp/agent_telemetry/<serial>.jsonl' relative to a cwd of org/modules/graph/ instead of the workspace root.
- last_touch: UNTRACKED (gitignored by .gitignore:415 `**/org/` -- not committed, not visible on a fresh clone)
- consumers: none found in bounded sweep; explicitly invisible to org/modules/graph/comp_debt/signals/usage.py, which reads the REAL org/mcp/agent_telemetry/*.jsonl at the repo root as its live-invocation evidence source
- STALE: This is the clearest evidence of a live, ongoing defect (8 distinct agent serials hit it, spanning at least June-July): every one of these agents' tool invocations while their cwd was under org/modules/graph/ is silently missing from the real telemetry stream, which directly undermines the USAGE signal that org/modules/graph/comp_debt/signals/usage.py is designed to reason from ('a tool/artifact un-invoked in N days' -- false-cold risk if the missing invocations happened to be the only recent ones).
- note: Recommend: (1) delete this directory (28KB, gitignored, dead weight), (2) find and fix the root cause -- whichever script/hook writes agent_telemetry via a relative path instead of an absolute workspace-root path -- since it directly poisons the comp_debt USAGE signal's denominator. This is a mechanism bug, not a documentation one; naming it here so it reaches an owner rather than getting silently deleted and recurring.

## GENERATED -- derived surfaces (audit their sources, not them)

### org/modules/graph/tests/__pycache__/
- purpose: Compiled bytecode cache (172 .pyc files, 3.4MB) auto-generated by the Python interpreter on test collection/run.
- last_touch: UNTRACKED (git check-ignore confirms it is gitignored; not a git object)
- consumers: Python interpreter only, at import time; no source file or gate references it by name.
- note: Deletion-candidate, zero risk: 3.4MB / 172 files, regenerates automatically on next pytest run, already excluded from version control via .gitignore.

### org/modules/graph/gold-nan/
- purpose: On-demand output directory for `comp-validate gold-nan` (validate_cli.py:707-864, .tools/comp-validate wrapper): audits every top-level data/inf/scripts/gold/*.py for NaN-safe JSON-emit compliance (PASS/INLINE/NEITHER/N/A) and writes one YAML manifest per script plus a chain-wide REPORT.md.
- last_touch: d17d45be07 2026-06-15 0.4.0_DT_ClientPlatform
- consumers: only the writer (validate_cli.py:cmd_gold_nan) references the path in a bounded sweep of .tools + org/modules/graph; no gate or downstream script reads gold-nan/*.yaml or REPORT.md back
- STALE: REPORT.md:3 self-dates 'Generated: 2026-05-14' and REPORT.md:14 freezes 'Total 79' scripts with no runtime derivation -- current data/inf/scripts/gold/*.py top-level count is 53 (verified via find), and REPORT.md:27+38 list BOTH a bare-named ('09.generate_partner_analytics') and INF_-prefixed ('INF_09.generate_partner_analytics') entry as separate NEITHER rows -- a since-completed bare->INF_ rename artifact never re-run to collapse
- STALE: gold-nan/INF_09.generate_partner_analytics.yaml:5-7 records emit_sites lines 102,252,258, but the live source (touched 2026-07-12, after this manifest) has json.dumps calls at lines 117 and 267 -- the manifest's line pointers no longer resolve to the cited code
- note: self-healing on next `comp-validate gold-nan` run (the tool re-walks source fresh each invocation) and nothing gates on the frozen artifact, so this is a stale historical snapshot rather than a live silent-decay risk -- but an agent reading REPORT.md today would get a wrong script-count and wrong line citations without re-running the tool.

### org/modules/graph/postmerge-cols/
- purpose: On-demand output of `comp-pipescript postmerge-cols` (pipeline_cli.py:2583-2680, registered subcommand at graph-call-manifest.yaml:1473, .tools/comp-pipescript wrapper): per-script merge()-call-site manifests flagging suffix-collision risk (e.g. INF_B_00.canonical_holdings.yaml:1-20 records a `pos x accounts` merge at line 288 with flagged _x/_y-suffix columns).
- last_touch: d0e2226b88 2026-06-11 0.7.0_AE_CloudOps
- consumers: only the writer (pipeline_cli.py:cmd_postmerge_cols) and its own registration in graph-call-manifest.yaml/.tools/tool_index.py reference the dirname in the bounded sweep; no gate reads the manifests back
- STALE: only 4 of the current 53 top-level gold scripts have a manifest here (INF_B_00, INF_C_00, INF_C_01, INF_D_00c) -- these are one-off per-script CLI invocations from 2026-06-11, not a corpus sweep, so the directory is a partial/dated sample rather than coverage of the live gold estate
- note: low risk: purely informational, on-demand, self-regenerating per invocation, no gate or script consumes the stored output as ground truth.

### org/modules/graph/vectorize-audit/
- purpose: On-demand output of `comp-perf vectorize-audit` (vectorize_audit_cli.py:13 sets _VECTORIZE_DIR here; .tools/comp-perf wrapper): pandas-vectorization-opportunity findings per gold script, plus a per-pipeline rollup (_chain_inf.yaml).
- last_touch: d0e2226b88 2026-06-11 0.7.0_AE_CloudOps
- consumers: vectorize_audit_cli.py (writer), .tools/comp-perf (wrapper), org/modules/graph/tests/test_vectorize_audit_ascii.py (test coverage); no gate reads the stored YAMLs back
- STALE: only 4 of 53 current top-level gold scripts have a per-script file (INF_B_00, INF_B_03, INF_C_00, INF_D_06.cash_drag) plus one rollup (_chain_inf.yaml) -- a partial one-off sample from 2026-06-11, not a corpus sweep; all report 0 findings/0 warn, so it cannot be distinguished from 'never re-run since' vs 'genuinely clean'
- note: low risk: informational, self-regenerating per invocation, no gate consumes the stored output; the 0-findings rows are not evidence the estate is vectorization-clean today, only that these 4 scripts were clean as of 06-11.

### org/modules/graph/comp_toolgraph_census.json
- purpose: Committed 'C0 node table' snapshot produced by `comp-toolgraph census --write` (LEAD-1 versioned rendering of the comp-tool universe, 63 IN).
- last_touch: 7ada688374 2026-07-10 0.8.0_AE_CloudComp
- consumers: comp_toolgraph.py (self-write path) and comp_passcraft.py
- STALE: comp_toolgraph_census.json:~924-937: node 'pipescript' has on_disk:true, substrate 'org/modules/graph/pipescript_cli.py' -- that file was RENAMED to estate_infrastructure_cli.py today (2026-07-30) and bare 'pipescript' is now a prohibited rc=2 tombstone, so this frozen (07-10) node entry misdescribes both the file path and the tool's live status.
- STALE: universe_count:63 (frozen at generation time) predates today's deletion of comp-semantic-estates + comp-opalbizsem from the tool universe, so the denominator is stale by at least 2.
- note: Source is comp_toolgraph.py (`census --write`); re-run it to refresh -- the committed copy is a ~3-week-stale vintage that now misdescribes the renamed pipescript_cli.py path and an outdated universe count.

### org/modules/graph/estate-coverage-resolver.json
- purpose: Generated resolver (by gen-estate-resolver.py) joining CVO's authoritative thread-routing manifest with per-thread census detail (producers/served/frontend); the read-source comp-estate uses for NAMES.
- last_touch: 97dc3e07b6 2026-07-30 3.0.0_SA_CVO
- consumers: estate_infrastructure_cli.py / opal_estate_infrastructure.py (comp-estate)
- note: Freshly regenerated today (last_review: 2026-07-30); the CLAUDE.md-flagged '14-day staleness' risk does not currently apply.

### org/modules/graph/.manifest_check_advisory_tally.jsonl
- purpose: Local advisory-tally log appended by the comp-manifest-check gate, recording advisory-mode findings (e.g. B_rebuild_when_query, C_adhoc_reimplementation) by file/line/category.
- last_touch: UNTRACKED (deliberately gitignored: .gitignore:402, confirmed via `git check-ignore -v`)
- consumers: org/modules/graph/manifest_check_cli.py and manifest_check_config.yaml (writer/reader)
- note: Correctly gitignored device-local runtime log, not meant to be tracked -- not the silent-deprecation risk class the prompt warns about.

### org/modules/graph/TOOL_MASTER.yaml
- purpose: GENERATED heavy tool-attribute master (concern/canonical_call/state/refresh_mechanism per tool), composing with comp-coverage-map.yaml.
- last_touch: b38d005b08 2026-07-30 3.0.0_SA_CVO
- consumers: .tools/tool_index.py; the comp_coverage_view.py projection ecosystem
- note: Header explicitly says 'DO NOT HAND-EDIT' and fails loud on population divergence from comp-coverage-map.yaml -- audit that source file, not this one.

## HISTORICAL-KEEP -- records, harmless if stale

### org/modules/graph/tsgraph_spike/
- purpose: NFRA_TSGRAPH.P0/P1/P2-1 ts-morph TS-Compiler-API spike (extractor.ts/extractor_full.ts/cluster_extract.py/emit_producer.py/parity_sweep.py/field_parity_check.ts/measure_full.ts/smoke.ts + 2 LEGC + 1 SEAMS validation .md) that proved the compiler-grade portal semantic-graph substrate and field-grain stitch before production build-out.
- last_touch: b47839cff7 2026-06-26 0.4.0_DE_ClientPlatform
- consumers: none found in bounded sweep as a live import/CLI target -- the LIVE comp-cluster tool (.tools/comp-cluster) execs infra/aws/globgrph/comp_cluster_cli.py, not anything in this dir; org/projects/NFRA_TSGRAPH.json status='complete' for P1+P4, and graph-call-manifest.yaml's comp-cluster entry (status: canonical) points to the P2-3 materialization, not this spike. .owned-paths.yaml:1108-1110 still carries an active grant note for the path (lane NFRA_TSGRAPH_SPIKE), which is governance bookkeeping, not a functional consumer.
- STALE: self-marked as a spike, not current infra: own .gitignore:1 'NFRA_TSGRAPH.P0 spike -- transient/large artifacts (not source of truth)'; package.json:2,5 name='tsgraph-spike', description opens 'NFRA_TSGRAPH.P0 spike'.
- STALE: no forward pointer inside the dir to the successor: a reader landing on cluster_extract.py or the LEGC/SEAMS docs has no in-dir link to infra/aws/globgrph/comp_cluster_cli.py, which is where the real, still-evolving logic now lives (comp_cluster_cli.py/derive_runner.py/kuzu_nessie_load.py etc., all touched far more recently than 2026-06-26).
- STALE: the LEGC/SEAMS .md files are point-in-time validation results (all dated 2026-06-17, 'F5 STATUS: LIVE-VALIDATED (closed)') -- accurate as history, but a reader could mistake their live-graph node/edge counts (e.g. '12,397 nodes', '961 FLOWS_TO') for current estate size; those numbers are 6+ weeks stale against the now-canonical graph and carry no refresh mechanism.
- note: Low risk in isolation (self-labeled spike, gitignored heavy artifacts do not ship to a fresh clone, tracked source is inert once superseded) -- the residual risk is purely navigational: nothing in the dir redirects a future reader to the canonical infra/aws/globgrph/ implementation, so this is a plausible source of 'which version is real' confusion, not of runtime breakage.

### org/modules/graph/promote_lifecycle_cse.jsonl
- purpose: Append-only compressed-semantic-event log of promotion lifecycle transitions (OPEN->CANDIDATE etc.) for the MOTIF/promote pipeline.
- last_touch: bedc1bfd04 2026-07-14 0.8.0_AE_CloudComp~Z
- consumers: comp_promote_lifecycle.py.
- STALE: last write 2026-07-14 (16 days stale as an event log); no evidence of an active producer still appending -- could be intentionally quiet (no new promotions) or a dead pipeline; sweep cannot distinguish the two.
- note: A quiet event log is not itself evidence of breakage (CLAUDE.md staleness-reasoning default applies to any 'stale' read); flag for the pipeline owner to confirm whether MOTIF promotion activity is genuinely dormant or the sink stopped firing.

### org/modules/graph/promote_lifecycle_manifest.json
- purpose: Current-state manifest of promotion candidates (motif:*, recognizer:* etc.) with decompression_chain evidence, keyed by candidate_id.
- last_touch: bedc1bfd04 2026-07-14 0.8.0_AE_CloudComp~Z
- consumers: comp_promote_lifecycle.py.
- STALE: same 2026-07-14 vintage as its sibling jsonl logs -- one coherent write-set, not independently stale.
- note: Companion file to promote_lifecycle_cse.jsonl; same quiet-vs-dead ambiguity applies.

### org/modules/graph/promote_materialize_cse.jsonl
- purpose: Append-only event log of recognizer materialize/demote actions (hot-register/deregister against the live dispatch set).
- last_touch: bedc1bfd04 2026-07-14 0.8.0_AE_CloudComp~Z
- consumers: comp_promote_lifecycle.py, comp_promote_materializer.py.
- STALE: 2026-07-14 vintage, same write-set as the other promote_* files.
- note: Part of the same coherent promote-pipeline write batch; two live consumers found so not orphaned code, just a quiet stream.

### org/modules/graph/promote_surface_events.jsonl
- purpose: Small append-only log (1.2KB) of surface/seam identifiers touched by promote actions (e.g. compilerkit.recognizer.hot_register).
- last_touch: bedc1bfd04 2026-07-14 0.8.0_AE_CloudComp~Z
- consumers: comp_promote_materializer.py.
- STALE: same 2026-07-14 vintage.
- note: Smallest of the promote_* set; genuinely consumed, just quiet since the same date as its siblings.

### org/modules/graph/resign_surface_baseline.py
- purpose: DEV-BOX signer that re-signs the D8 critical-surface scan baseline from critical-surfaces.yaml aws_backend membership.
- last_touch: d79abd1e63 2026-06-17 1.0.0_SA_CTO
- consumers: none found in bounded sweep beyond its own historical inbox trail and one change-management ledger entry -- no active .py/.yaml/.sh caller.
- STALE: self-marked 'DEPRECATED -- DO NOT USE' at line 2, superseded by derive_runner.py --sign-baseline (same-code-same-data signer); the file still exists on disk and is intentionally kept ('Kept as the historical record + membership-parse reference only') behind a hard ALLOW_DEPRECATED_RESIGN=1 gate -- this is a documented, deliberate, gated deprecation, not a silent one.
- note: Textbook case (c) self-marker on a file that still exists, but explicitly justified and hard-gated against accidental re-use -- low risk as written; genuinely safe to delete if anyone wants to shed the reference copy, but no urgency.

### org/modules/graph/compproof/{report.json, JUDGE_REPORT_TO-B2_CVO-B.md, JUDGE_REPORT_TO-B2_CVO-B_tranche2_B09-B20.md, JUDGE_DIAGNOSTIC_B01_B08_CVO-B.md, judge_axes.json, judge_methodology_caveats.json, solver_results_full.json, comproute_c1_report.json, comproute_c1_tail_report.json, solver_view_B-01.txt}
- purpose: The frozen final output of the ORIGINAL one-time B1 blind-run (18 incidents scored: 10 SOLVED / 1 PARTIAL / 7 MISS, 55.6% solved) plus the CVO~B judge's per-case rubric scoring and diagnostic writeups -- an archival record of that specific completed experiment, not a live-refreshed metric.
- last_touch: 733ea98fef 2026-07-02 0.8.0_AE_CloudComp~D (report.json); 3bca7637bf 2026-07-02 3.0.0_SA_CVO~B (judge files); b98a061970 2026-07-01 3.0.0_SA_CVO~B (JUDGE_REPORT); 1d95043d5c/bb0eb2ca26 2026-07-07 0.8.0_AE_CloudComp~E (comproute_c1_*)
- consumers: none found reading these back programmatically (blind_run.py WRITES report.json from solver_results.json+judge_axes.json; nothing downstream re-reads report.json) -- they are the record of the run, cited by RUN_PROTOCOL.md/AFFORDANCE_SPEC.md and referenced in commit messages/inbox threads as evidence for the TRUE-SANDBOX design decisions.
- STALE: (e) dated snapshot with no refresh mechanism, but harmless: these are self-evidently a one-time run's results (n_scored: 18, fixed case IDs B-01..B-20), not a metric anyone expects to track current state, and no live gate reads them.
- note: Keep as the evidentiary record the sandbox-design rulings (CTO 154055Z TRUE-SANDBOX, etc.) cite; no action needed.

### org/modules/graph/comp_learns_leg4_exercise.py
- purpose: One-time AC-L4 acceptance exercise proving a repeated routing outcome shifts the next route (COMPLEARN leg-4 activation falsifier).
- last_touch: ec64edd9b3 2026-07-10 0.8.0_AE_CloudComp~E
- consumers: none found in bounded sweep beyond its own imports (comp_route_shadow, comp_route_affinity); no .tools wrapper
- STALE: self-described as a one-shot ACCEPTANCE EXERCISE ('THE SHIFT IS THE ACCEPTANCE') -- inbox mail from 07-10 shows it was BUILT and RAVC2-accepted that day, so its job is done; harmless as a record
- note: Safe to keep as the acceptance proof-of-record; not a recurring gate.

### org/modules/graph/comp_promote_lifecycle.py
- purpose: NFRA_PROMOTE-P1 state machine (CANDIDATE->MEASURED->PROPOSED->RATIFIED->MATERIALIZED->MONITORED->SUSTAINED) + 5-invariant gate for promoting a motif candidate.
- last_touch: 53b0794f92 2026-07-14 0.8.0_AE_CloudComp~Z
- consumers: none found in bounded sweep -- no .tools wrapper, and comp_promote_materializer.py (the module it claims to gate) contains ZERO import of it despite the docstring's claim ('materialize_live REFUSES without one'); coupling if any is file-based (a commission artifact on disk), not code-level
- STALE: docstring asserts an enforcement relationship to comp_promote_materializer.py that the bounded import-grep could not confirm -- either file-interface coupling (benign) or a claim that decayed after the 07-14 NFRA_PROMOTE convergence ruling (org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_PROMOTE_P1_CONVERGENCE_20260714.md)
- note: If the gate is meant to be actively enforcing, this is dormant machinery -- worth a follow-up grep for the commission JSON path it reads/writes to confirm the file-interface actually fires; not verified in this pass.

### org/modules/graph/comp_promote_materializer.py
- purpose: NFRA_PROMOTE-P2/GOV-B: the LIVE hot-registration producer that reads a ratified manifest and registers a Recognizer into a running registry without redeploy.
- last_touch: a0528032d6 2026-07-08 0.8.0_AE_CloudComp~D
- consumers: imports comp_recognizer_sdk.py (a live, actively-consumed SDK) -- but no .tools wrapper and no importer of this file found in bounded sweep
- STALE: referenced heavily in 07-14 inbox CERT/DELIVERY traffic suggesting the NFRA_PROMOTE arc reached a closeout state around then; no evidence of ongoing invocation since
- note: Code paths are not dead (SDK import is live) but the materializer entry point itself appears unwrapped/uninvoked in current flow.

### org/modules/graph/comp_rail_audit.py
- purpose: COMPRAIL TO-5 closeout audit: post-enforce telemetry (route/deny/override distribution) + broad-grep-tier FP/TP classification, recommending GO/HOLD/NO-GO.
- last_touch: 3b87a05a12 2026-07-01 0.8.0_AE_CloudComp~E
- consumers: none found in bounded sweep -- no .tools wrapper, no importer
- STALE: own docstring frames it as 'the close TO' for COMPRAIL TO-5; COMPRAIL is now described elsewhere (CLAUDE.md Rule 21) as LIVE + enforcing, i.e. the GO decision this tool fed has already been acted on
- note: Harmless as a record of the enablement decision; not a recurring instrument.

### org/modules/graph/D8-findings.md
- purpose: Day-0 baseline findings (NFRA_GRAPHS D8) for 5 critical portal surfaces (model_portfolios.*, advisor_intelligence), a June-12 comp-platinum scan snapshot.
- last_touch: 74ec2cadf3 2026-06-12 2.0.0_SA_COO
- consumers: Named as `baseline_findings` pointer in critical-surfaces.yaml:139 (the comp-surface-check SEV1 gate config) and cited in docs/architecture/NFRA_DEBTSCAN_PRD.md; NOT programmatically parsed -- grep for the field name found no read in surface_check_cli.py, only a prose mention at line 25
- STALE: Alarm-eligible language ('First alarm should fire only when a FUTURE scan detects deviation') pre-dates the 2026-07-28 standing moratorium on building alerts/alarms (CLAUDE.md)
- STALE: All 5 signed-baseline rows read 'true (pending YAML update)' -- unclear whether ever resolved
- STALE: Vintage pinned to a single nessie commit (b879522196e3/59b0a6a9...) with no refresh mechanism
- note: Dated snapshot with a live-but-descriptive pointer-consumer -- drift here is a human-readability risk, not a gate-correctness risk, since the pointer is never machine-parsed.

### org/modules/graph/DESIGN.md
- purpose: Original April-2026 design spec for the full-stack trace compiler (comp-trace/comp-blast): node/edge types, phasing plan.
- last_touch: 0848bd7093 2026-04-09 1.0.0_SA_CTO
- consumers: none found in bounded sweep (only auto-generated org/missions/*/commits.jsonl entries mention the path, not a functional reader)
- STALE: 'Phasing' section lists Phase 2 (EventBridge/Lambda routing) and Phase 3 (auth schema/pre-commit hook) as future; comp-tools.yaml/comp-routes now describe those areas as already built, so this reads as an unrevised founding spec
- note: Harmless -- superseded in practice by the live comp-tools.yaml catalog; kept as the founding-design record for comp-trace/comp-blast.

### org/modules/graph/comp-aws-agent-usage.yaml
- purpose: Agent-facing usage guide (commands + when-to-use) for comp-aws (comp_aws_cli.py), the AWS cloud compiler.
- last_touch: 9df98e50b6 2026-06-08 1.0.0_SA_CTO
- consumers: none found in bounded sweep (only org/audit/archive/*/org_git-author-override-audit.log mentions, which are commit-bypass logs, not functional readers); comp-tools.yaml's own comp-aws entry appears to be the operative agent-facing doc today
- STALE: Dated 2026-06-08, ~7 weeks stale relative to comp-tools.yaml (touched today) and comp_aws_cli.py (last touched 2026-07-10); no linkage mechanism ties this guide to the engine's command surface so drift would go unnoticed here
- note: Low risk since comp-tools.yaml appears to have absorbed the agent-facing catalog role; this file reads as a superseded parallel doc.

### org/modules/graph/comp-shell-dup-source-baseline.json
- purpose: One-time duplicate-source-file scan baseline (post-FIRMSEP.05 cleanup) over Lambda/inf/bd script trees, recording resolved and one open needs_investigation entry.
- last_touch: d0e2226b88 2026-06-11 0.7.0_AE_CloudOps
- consumers: none found in bounded sweep -- its name suggests pairing with a dup-source scanner, but comp-shell (shell_cli.py) is a DIFFERENT tool (Rule-16 forbidden-utility detection, unrelated to duplicate-source scanning); no producer/consumer for this specific baseline path was identified
- STALE: The needs_investigation entry (public-data-router) noted in the file's own summary was never confirmed resolved in this sweep
- note: Name collision with the live comp-shell tool could mislead a future cleanup pass into thinking it's that tool's baseline; otherwise an inert historical snapshot.

### org/modules/graph/comp-tool-universe.md
- purpose: AC-0 methodology ruling ('a tool universe is a predicate, not an integer') plus the multi-agent retraction log from a 2026-07-09 tool-count reconciliation session where 60/63/77 were all withdrawn.
- last_touch: 9501d9dbce 2026-07-09 0.8.0_AE_CloudComp
- consumers: none found in bounded sweep; appears to be the philosophical precedent behind COMPTOOL_REGISTRATION_FLOW.md's completeness-gate design, but no file cites it by name
- STALE: Line 39 cites bare 'pipescript' as 'invokable, in tools_index, in CLAUDE.md's trigger table' -- true as of the July 9 measurement, but bare pipescript is now a prohibited rc=2 tombstone as of the 2026-07-30 rename; a reader skimming past the dateline could misread this as a current fact
- STALE: Lines 159-180 carry several other now-obsolete frozen counts (42/60/63/24/23/31/28) from the same superseded session
- note: Low risk -- the doc is explicitly framed as a dated ruling/retraction record ('Measured, this session'), not a living count; risk is only to a reader who skips the historical framing.

### org/modules/graph/comp-tools-segment-scope.md
- purpose: One-page 'which comp-tool, when' reference card for BD/INF/multi-firm segment scoping, meant as a distilled front-end to comp-tools.yaml.
- last_touch: 4fd343b452 2026-05-08 0.7.0_AE_CloudOps
- consumers: none found in bounded sweep; no code/gate parses it, purely an agent-facing reference card
- STALE: Line 3: 'Last updated: 2026-05-08' hand-maintained date field, ~12 weeks stale relative to comp-tools.yaml (touched today), the companion catalog it tells readers to consult
- note: Low functional risk -- the comp-pipescript command surface it documents still matches today's comp-tools.yaml -- but the card is unmaintained relative to its stated companion and could drift further unnoticed.

### org/modules/graph/comp_aggregate_honesty.py
- purpose: PROPOSAL-ONLY module (explicitly self-labeled) rendering current-vs-proposed system_parity.py roll-up wording side by side, under CTO~Z's falsifiability constraint; lands nothing and is not wired into any gate.
- last_touch: 4a49eacb21 2026-07-25 0.8.0_AE_CloudComp~B
- consumers: none found in bounded sweep; it imports comp_desc_sensitivity.py but nothing imports comp_aggregate_honesty itself
- note: Harmless by the file's own design ("THIS MODULE LANDS NOTHING"); keep until the CTO~Z proposal it renders is formally ruled on or superseded.

### org/modules/graph/comp_desc_sensitivity.py
- purpose: NFRA_TOOLUNIFY Phase-1 LEAF measurement -- lexically checks whether a check's `desc` over-claims relative to its actual measured sensitivity, per infra/system/scope_contract.json.
- last_touch: 3272197a93 2026-07-25 0.8.0_AE_CloudComp~B
- consumers: comp_aggregate_honesty.py (itself proposal-only/unlanded, see that entry) and comp_desc_sensitivity_test.py; no .tools/comp-* wrapper found
- note: Not gate-wired; a real, tested measurement instrument sitting at the end of an unlanded proposal chain -- keep pending a ruling on comp_aggregate_honesty's proposal.

## NECESSARY -- live inputs to tools/gates (consumer named per item)

### org/modules/graph/tests/
- purpose: Live pytest mutant-kill/negative-control suite (85 test files, ~695 test functions) for the comp-* tool estate under org/modules/graph -- e.g. IAM verdicts, comp-freshness, comp-route, comp-which/routing, sovereign firm-separation (bd-hold), and the active NFRA_VELOCITY_ESTATE WS-E4/E5/E6 telemetry-verdict acceptance bar (test_e41/e42/e413/e5/e6r8, all authored 2026-07-30).
- last_touch: 3d9ad164b2 2026-07-30 0.7.0_AE_CloudOps (whole-dir HEAD; individual files range 2026-06-11 to 2026-07-30, continuous activity)
- consumers: .owned-paths.yaml:733 names 'org/modules/graph/tests/**' explicitly as the P4 build surface/deliverable (per-tool negative-control fixtures) with an active grant to 0.7.0_AE_CloudOps + DS~B + CVO-verifies + CTO~C arch-gates; TOOL_MASTER.yaml:80 lists test_comp_system_metrics.py as a comp-system engine; .tools/comp-arity:385 references the same file directly; multiple 0.7.0/0.8.0_AE session logs (org/tier2_senior/.../logs/2026-07-*) record dispatches that authored/exercised files in this dir same-day.
- STALE: (c-adjacent, benign) test_e42_fail_kind_separation.py:22 quotes a PAST measured incident ('comp-opalbizsem --list exits 2') inside a dated docstring describing a causal investigation -- clearly historical/narrative framing, not asserted as a currently-callable tool, so this is the acceptable 'clearly-labeled historical mention' case, not live staleness.
- STALE: (b, low-risk) several newer files (test_e42_fail_kind_separation.py:15-25, test_e413..., test_e5...) carry hand-written point-in-time counts in docstrings ('54 of 87 FAIL rows at build time -- 62%', 'rc=120 across 6 tools') -- these are prose evidence-of-derivation for a mutant test, not runtime-derived and not assertion inputs (spot-checked: the numbers live in the module docstring, not in an assert), so they will silently read stale as the estate's tool count/fail count drifts but do not affect test correctness.
- STALE: no per-file staleness of type (a)/(d)/(e) found in the sampled set -- no references to comp-semantic-estates/comp_opalbizsem/opal_business_estates/pipescript_cli.py used as CURRENT, and no dated snapshot-with-live-consumer-and-no-refresh pattern observed in the sample.
- note: None material -- this is the opposite of the dangerous quadrant: it is a live, actively-authored, gate-owned acceptance-test tree with same-day commits; the only 'staleness' found is cosmetic (a historical incident quote, and prose point-in-time counts inside docstrings).

### org/modules/graph/incrparity_core.py
- purpose: Importable diff-logic core for comp-incrparity (S3-client-injectable dual-run parity checker, BD gold incremental-vs-full comparison).
- last_touch: 847ba967c6 2026-06-03 0.4.0_DS_ClientPlatform
- consumers: incrparity_cli.py imports it directly; comp-constants-seed-bd.yaml references it; two test files (test_failure_class_hardening.py, test_incrparity_cli_bd_hold.py).
- STALE: none found -- pure logic module, no hand-maintained counts/dates, no self-deprecation marker.
- note: Live input to .tools/comp-incrparity via incrparity_cli.py; core diff logic for INCREMENTAL_RUNS_DESIGN.md.

### org/modules/graph/keep-dormant.yaml
- purpose: Canonical keep-dormant registry (CTO arch-gated): per-resource reason/rearm_condition/annotation_cite/revalidate_by entries the dormant-vs-dead debt guard looks up instead of parsing comments.
- last_touch: 142d396b5d 2026-07-02 1.0.0_SA_CTO
- consumers: org/modules/graph/comp_debt/dormant_guard.py loads it live (REGISTRY_PATH at dormant_guard.py:50, cited at :16/:59/:131/:218); NFRA_ONTOLOGY_C2C3_CANONICAL.yaml also references it.
- STALE: entries carry revalidate_by decay dates -- checked 2026-08-16 (lever:mdpf-custody-flip-LEVER-2) and 2026-12-29 (others): none past-due as of 2026-07-30, so the decay mechanism is currently honest, not yet exercised.
- note: Gate-enforced governance registry with a working decay/revalidation mechanism; nearest revalidate_by (2026-08-16) is 17 days out -- worth a calendar note but not currently stale.

### org/modules/graph/lambdamap_cli.py
- purpose: comp-lambdamap backend: read-only drift check of infra/aws/lambda/ci/lambda-source-map.json against Terraform + on-disk dirs (Phase1) and live CodeSha256 (Phase2).
- last_touch: 1a4fd82be1 2026-06-29 0.7.0_AE_CloudOps~B
- consumers: .tools/comp-lambdamap wrapper invokes it; referenced in comp-tools.yaml, extract_lambda_routes.py, TOOL_MASTER.yaml, tests/test_lambdamap.py.
- STALE: docstring says 'Phase 2 remaining (next increments, CVO-gated): derive --write ... multi-region/multi-runtime' -- an open-ended forward-looking TODO, not a false current-state claim, so not flagged as stale.
- note: Live CI-gate-friendly drift tool with a working .tools wrapper.

### org/modules/graph/manifest_check_cli.py
- purpose: comp-manifest-check: commit-time enforcement of graph-call-manifest.yaml (flags deprecated-entry calls, rebuild-vs-query, ad-hoc re-implementation of the graph).
- last_touch: 29c3fedeb8 2026-07-30 3.0.0_SA_CVO (touched TODAY)
- consumers: .tools wrapper comp-manifest-check; comp-output-contracts.yaml, compproof/tool_probe.py, debtscan/summary_corpus.py, and 3 tests (mutants/completeness/direction).
- STALE: none -- edited same-day; mirrors the manifest_check_config.yaml ramp (advisory mode) which is itself current.
- note: Gate-enforced (NFRA_GRAPHS D6), folded into ds-commit-gate; freshest file in the whole batch.

### org/modules/graph/manifest_check_config.yaml
- purpose: Single-knob (advisory/blocking) ramp control + severity routing + exempt-path list + tally_log path for the comp-manifest-check gate.
- last_touch: 98d3c4fe97 2026-06-11 0.4.0_DS_ClientPlatform
- consumers: manifest_check_cli.py (_CONFIG path) reads it directly; the only consumer found.
- STALE: prose says ramp stays advisory 'until DS + CTO agree ... should accrue real-commit evidence in advisory mode first' -- open-ended, not a frozen claim, current `mode: advisory` matches CLAUDE.md Rule text which still describes it as gated/announce-then-enforce, so consistent.
- note: Single live knob for a gate-enforced tool; low risk since it's a config, not logic.

### org/modules/graph/nerves-edges.json
- purpose: L3a CO_CHANGE edge file (NFRA_NERVES): decayed traffic-weighted git co-change edges (half-life 21d), machine-generated by nerves_accrete.py build.
- last_touch: 907620c800 2026-07-14 1.0.0_SA_CTO~Z
- consumers: comp_pulse.py (comp-pulse, EDGES constant) reads it live and prints its 'stale'/vintage flag in every report; also referenced from cli.py, comp-coverage-map.yaml, graph-call-manifest.yaml, .tools/tool_index.py.
- STALE: dated snapshot (2026-07-14, 16 days old at review time) with a declared 21-day half-life and NO auto-heal path in comp_pulse (comp_pulse.py:499-501 just tells the operator to 'run nerves_accrete build', it does not self-regenerate the way it does for the risk map) -- consumer discloses staleness via a printed 'stale' field rather than silently trusting it, so this is disclosed-stale, not silent-stale.
- note: Live-consumed (comp-pulse) generated artifact whose regen is manual-only; the consumer's own honesty gate (vintage/stale field) is the mitigation -- would become a true AT-RISK item only if comp_pulse's disclosure were ever removed.

### org/modules/graph/nerves-risk-edges.json
- purpose: L3b danger map (NFRA_NERVES): entity-linked HOLD/RISK/DOCTRINE edges from the corpus onto graph nodes, machine-generated by nerves_lexical.py build; largest file in batch (1.85MB).
- last_touch: 2d8609a9eb 2026-07-22 1.0.0_SA_CTO
- consumers: comp_pulse.py (RISK constant) -- reads it AND auto-regenerates it on staleness via _ensure_fresh_danger_map()/subprocess nerves_lexical.py build (comp_pulse.py:152-183); also wired into safe-commit.sh's [risk-reflex] advisory block per graph-call-manifest.yaml:1089.
- STALE: self-heals via comp_pulse's heal-on-read mechanism, so a stale on-disk copy is not a silent-decay risk the way a manually-regenerated artifact would be.
- note: Live-consumed, gate-wired (safe-commit risk-reflex) with an active auto-refresh mechanism -- the dangerous-quadrant risk is specifically mitigated here, unlike nerves-edges.json.

### org/modules/graph/nerves_accrete.py
- purpose: NFRA_NERVES L3a engine: computes decayed CO_CHANGE edges from git log and emits nerves-edges.json.
- last_touch: 907620c800 2026-07-14 1.0.0_SA_CTO~Z
- consumers: imports nerves_resolve (resolve()); invoked by comp_pulse.py's regen instruction; no dedicated .tools/comp-nerves* wrapper found -- run directly as a script.
- STALE: none in the code itself; its emitted output (nerves-edges.json) is the thing that ages, tracked separately above.
- note: Producer of a live-consumed artifact (nerves-edges.json); no CLI wrapper in .tools, so regeneration is an operator-invoked `python nerves_accrete.py build`, not gated/scheduled.

### org/modules/graph/nerves_lexical.py
- purpose: NFRA_NERVES L3b engine: entity-links CLAUDE.md/memory/ledger/critical-path danger-zone prose onto graph nodes, emits nerves-risk-edges.json.
- last_touch: 1055b5d630 2026-07-22 1.0.0_SA_CTO~Z
- consumers: imports nerves_resolve (resolve()); invoked directly (subprocess) by comp_pulse.py's _ensure_fresh_danger_map(); registered in TOOL_MASTER.yaml and graph-call-manifest.yaml.
- STALE: none -- actively invoked/regenerated by comp_pulse, unlike its L3a sibling.
- note: Producer half of the gate-wired danger map; the one L3 engine with a real auto-refresh caller.

### org/modules/graph/nerves_resolve.py
- purpose: NFRA_NERVES L2 keystone: the ONE shared ref->node resolver (trace_graph -> comp-pydeps -> repo-path -> cloud-ref precedence), used by every other NERVES layer.
- last_touch: 6acff60264 2026-07-14 1.0.0_SA_CTO~Z
- consumers: imported by nerves_accrete.py, nerves_lexical.py, nerves_traffic.py, and cli.py.
- STALE: none -- lives up to its 'keystone' claim; genuinely imported by all three sibling modules.
- note: True shared dependency; no drift between its docstring claim and actual import graph.

### org/modules/graph/opal_estate_infrastructure.py
- purpose: comp-estate engine (C4 estate-infrastructure): live-from-source Opal estate traversal that diffs the frozen snapshot's key names against source-derived keys, replacing the pre-2026-07-30 opal_business_estates.py.
- last_touch: 7ef6215359 2026-07-30 3.0.0_SA_CVO (touched TODAY, the renamed file itself)
- consumers: comp_api.py, .tools/comp-estate wrapper, comp-coverage-map.yaml, comp-output-contracts.yaml, graph-call-manifest.yaml, .tools/tool_index.py; delegates to estate_infrastructure_cli.py (legacy engine, confirmed present on disk).
- STALE: file IS the freshly-landed rename target of today's consolidation -- its own docstring correctly documents the naming history (opal_business_estates -> opal_estate_infrastructure, pipescript_cli.py -> estate_infrastructure_cli.py) as HISTORY, not as a current claim, so it self-documents correctly rather than going stale.
- note: This is the correct, current, freshly-renamed live tool -- confirms the 2026-07-30 consolidation landed cleanly on disk (old comp-semantic-estates/comp-opalbizsem wrappers confirmed absent from .tools).

### org/modules/graph/pii_cli.py
- purpose: comp-pii backend: PII field detection/pseudonymization audit cross-referencing pseudonymizer.py, auth-validator-edge, comp-transform and comp-routes.
- last_touch: c9949dd3b6 2026-07-11 1.0.0_SA_CTO
- consumers: .tools/comp-pii wrapper; comp-coverage-map.yaml, graph-call-manifest.yaml; 4 tests (failure-class hardening, masking reachability, sweep denominator, routes-unresolved).
- STALE: none found.
- note: Standard live comp-tool backend, no drift.

### org/modules/graph/pipeline_cli.py
- purpose: comp-pipescript backend (largest file, 159KB): authoritative pipeline dependency tool -- DAG/io/chain/feeds/consumers/overlap/inject/stats over gold scripts.
- last_touch: 64a17a77b9 2026-07-30 3.0.0_SA_CVO (touched TODAY)
- consumers: .tools/comp-pipescript wrapper; comp_api.py, extract_s3.py, comp-output-contracts.yaml; multiple tests (column-gaps bd-hold, pipescript_deployed bd-hold, io discrimination).
- STALE: docstring self-labels as 'comp-pipescript' -- per session context this is the DISTINCT, still-valid tool (MEMORY.md: 'comp-pipescript is a DIFFERENT tool', not the retired bare-`pipescript` tombstone), so no rename staleness here; imports sovereign_held's is_held_bucket/include_held correctly (post-split, live half).
- note: Edited same-day as the naming consolidation and correctly untouched by it (different tool, same name family) -- no cross-contamination with the opal_estate_infrastructure rename.

### org/modules/graph/platinum_cli.py
- purpose: comp-platinum: full-stack trace chaining comp-transform + comp-routes + comp-pipescript from portal page to gold script.
- last_touch: 611b627ddc 2026-07-10 3.0.0_SA_CVO~A
- consumers: comp_marker_read.py, trace_graph.py, TOOL_MASTER.yaml; tests (platinum_held_path_guard, platinum_nested_keys, sovereign_held_no_drift).
- STALE: none -- uses the shared graph_cache (NFRA_GRAPHS D2 query-vs-rebuild cache), no frozen counts.
- note: Standard live comp-tool; the file's own comment flags it as historically 'the lone rebuild-every-call trace tool' before the cache fix -- documented history, not current staleness.

### org/modules/graph/prod_write_guard.py
- purpose: LOAD-BEARING SECURITY LEAF: pure-string predicates blocking an automated probe from targeting a production bd/Schwab resource; split out of sovereign_held.py 2026-07-25 to survive the governance-half deletion.
- last_touch: afa4dcdee8 2026-07-25 1.0.0_SA_CTO
- consumers: compproof/tool_corpus.py, compproof/tool_probe.py; tests test_prod_write_guard.py and test_sovereign_held_no_drift.py assert stdlib-only import via AST check.
- STALE: none -- explicitly documents its own split history and the trap it survives (byte-identical retracted tuples); this is a self-aware historical note, not drift.
- note: Security-critical leaf; docstring explicitly warns future editors never to delete by path-literal grep -- worth flagging to any future estate sweep that greps 'opal-data-bd'.

### org/modules/graph/registry_cli.py
- purpose: comp-registry: REGISTRY.md-vs-project-JSON-vs-PRD narrative drift detector + optional write-back under CVO author line.
- last_touch: ead15a2d4f 2026-07-10 3.0.0_SA_CVO
- consumers: tests/test_registry_held_rows.py; TOOL_MASTER.yaml.
- STALE: none found; default mode is read-only diff (apply-flag-required) which is inherently safe against drift.
- note: Live governance-drift tool named directly in CLAUDE.md/registry workflows.

### org/modules/graph/residue_cli.py
- purpose: comp-residue: detects structural axes (mapping keys) present in a source that no downstream consumer traverses -- the 'orthogonal-shape' blind-spot detector.
- last_touch: 705a19ef66 2026-07-24 1.0.0_SA_CTO~Z
- consumers: tests/test_residue_detector.py; TOOL_MASTER.yaml.
- STALE: none -- self-declares its own under-report bias explicitly (a design honesty note, not staleness).
- note: Contracted-exit tool (comp-output-contracts) with an explicit stated blind spot -- correctly documented, not stale.

### org/modules/graph/routes_cli.py
- purpose: comp-routes: traces the full serving path from S3 artifact to frontend component via CloudFront/API-GW/portal fetch/component sources.
- last_touch: b9f80e6dae 2026-07-24 0.8.0_AE_CloudComp~A
- consumers: .tools/comp-routes wrapper; comp_api.py, comp-output-contracts.yaml; tests (routes_trace_discriminates, routes_unresolved_not_none); TOOL_MASTER.yaml.
- STALE: none found.
- note: Standard live comp-tool backend.

### org/modules/graph/ses_sender_lint_cli.py
- purpose: Enforces CLAUDE.md Rule 23: flags any ses.send_email/send_raw_email Source= or EMAIL_FROM/SES_SENDER default not on opalinvest.dev, in both Python and Terraform.
- last_touch: 16c6915669 2026-07-07 0.7.0_AE_CloudOps~B
- consumers: .tools/commit_gate_runner.py imports it directly as `ses_sender_lint` (line 100) -- folded into the universal commit gate rather than a standalone .tools/comp-* wrapper.
- STALE: none -- Rule 23 (opalinvest.dev-only sender) is unchanged and still current per CLAUDE.md.
- note: Gate-enforced at every commit via commit_gate_runner.py; the only file in the batch with no standalone .tools wrapper by design (folded, not orphaned).

### org/modules/graph/shell_cli.py
- purpose: comp-shell: detects bare (unguarded) references to forbidden Git Bash 3.6.7 utilities (pgrep/pkill/flock/pidof/setsid/wget) per CLAUDE.md Rule 16.
- last_touch: 74a1ade334 2026-04-30 1.0.0_SA_CTO
- consumers: tests/test_shell_guard_discrimination.py; TOOL_MASTER.yaml; .tools/commit_gate_runner.py.
- STALE: oldest last-touch in the batch (2026-04-30, 3 months) but the forbidden-utility list matches CLAUDE.md Rule 16 verbatim (still current), and the rule itself hasn't changed -- age alone is not staleness when the enforced contract is unchanged.
- note: Gate-enforced, stable rule surface -- old age is expected for a settled detector, not a red flag.

### org/modules/graph/sovereign_held.py
- purpose: LOAD-BEARING SECURITY LEAF: canonical held-path/held-bucket predicates for the (now-retracted) 2026-07-09 bd/Schwab governance hold, split from prod-target-safety per CTO ruling.
- last_touch: 7a07814b94 2026-07-22 1.0.0_SA_CTO
- consumers: clobber_scan.py, comp-coverage-map.yaml, compproof/tool_probe.py, comp_constants_cli.py, comp_dispatch.py, comp_recognizers_code.py; also trace_graph.py, pipeline_cli.py, platinum_cli.py, validate_cli.py, tests/test_sovereign_held_no_drift.py.
- STALE: GOVERNANCE tuples correctly EMPTY (SOVEREIGN_HELD_PATHS/BUCKETS = ()) reflecting the 2026-07-14 retraction (matches MEMORY.md '49F/Schwab/RPS/bd SOVEREIGN BLOCK: LIFTED COMPLETELY'); RETRACTED_20260709_* tuples deliberately retained byte-identical for fast re-arm, self-documented as intentional, not drift.
- note: Widely-imported security leaf, current and consistent with the live retraction state; correctly distinguishes the retracted governance predicate from the still-live prod-write-guard half (now split into prod_write_guard.py).

### org/modules/graph/state_scan.py
- purpose: comp-state engine: BM25 registry/TO/PRD drift linter over recent git commits (REUSES debtscan's dup_scan.py BM25).
- last_touch: aaa9364dc6 2026-07-17 2.0.0_SA_COO
- consumers: graph-call-manifest.yaml, TOOL_MASTER.yaml, .tools/tool_index.py; also the /comp-state skill invokes it.
- STALE: none -- explicitly a self-test-gated, advisory-only, read-only instrument per its own docstring; matches the /comp-state skill description exactly.
- note: Live engine behind a documented skill; self-test-gated (--self-test must PASS 3/3) so its own honesty is enforced.

### org/modules/graph/surface_check_cli.py
- purpose: comp-surface-check: commit-time guard mapping changed portal files to critical-surface SEV1/SEV2 verdicts (NFRA_GRAPHS D8), published to S3 for portal CI to consume.
- last_touch: 81d37b0574 2026-07-29 3.0.0_SA_CVO
- consumers: compproof/tool_probe.py, TOOL_MASTER.yaml; distributed via .github/workflows/surface-check-publish.yml to portal CI.
- STALE: docstring's distribution note (LD-0273 Stage-1 Half-2) matches CLAUDE.md Rule 20's corrected text (portal-side enforced, workspace-side advisory) -- consistent, not stale.
- note: One of the two must-always-be-right gates named in CLAUDE.md Rule 20; touched yesterday, actively maintained.

### org/modules/graph/test_grain_sentinel.py
- purpose: Regression test (4 asserts) for the AC-GRAIN grain sentinel (S3-object-as-bucket phantom detector, NFRA_GRAPHS D5).
- last_touch: d57900ab76 2026-06-11 3.0.0_SA_CVO
- consumers: imports grain_sentinel from the same directory (sys.path insert); referenced in org/tier1_exec/3.0.0_SA_CVO/CMPAWS_F1_CERT_METHODOLOGY.md and a 2026-06-11 cert log.
- STALE: none -- straightforward regression test, no frozen counts beyond the '23,664-phantom class' historical citation which is clearly labeled as the incident it guards against, not a live count.
- note: Standard regression test guarding a certified fix (CMPAWS_F1); no .tools wrapper needed since it's a pytest-style unit test, not a CLI.

### org/modules/graph/test_iam_v4_024_fp_elimination.py
- purpose: Regression fixture for comp-iam gap-detector V4.024 false-positive elimination (EC2-shipped-script exclusion + AWS-managed-policy attachment resolution).
- last_touch: 4fd343b452 2026-05-08 0.7.0_AE_CloudOps
- consumers: imports extract_iam.py directly; no other .py/.yaml/.sh reference found in bounded sweep beyond audit-archive logs (unrelated hits on 'author-override' text, not this file).
- STALE: none in content -- but per CLAUDE.md Rule 22a, comp-iam has since grown MORE known-insufficiency axes (resource-style two-hop invisibility etc.) that this older V4.024-scoped fixture does not cover; that is a coverage gap, not a defect in the test itself.
- note: Oldest-content regression test for a still-live tool (extract_iam.py backs comp-iam); worth confirming it's still run in CI/commit-gate rather than a one-time fixture that nobody re-executes.

### org/modules/graph/tooltip_cli.py
- purpose: comp-tooltip: scans portal/src for tooltip rendering patterns, classifies against the canonical dark-navy/white-text spec, reports migration status.
- last_touch: c91aaa8040 2026-07-10 3.0.0_SA_CVO
- consumers: tests/test_tooltip_canonical_exclusion.py; TOOL_MASTER.yaml.
- STALE: none found -- pattern-detection logic, no frozen migration counts in the head.
- note: Standard live comp-tool backend for portal design-system conformance.

### org/modules/graph/trace_graph.py
- purpose: Core full-stack trace-graph node/edge model (COMPONENT/ENDPOINT/LAMBDA/S3_ARTIFACT/GOLD_SCRIPT/EVENTBRIDGE/CLOUDFRONT) backing opal-trace and opal-blast.
- last_touch: fe19d46ff4 2026-07-22 0.8.0_AE_CloudComp
- consumers: cli.py, comp_marker_read.py, comp_pydeps.py, comp_recognizers_config.py, comp_ws4_crosswalk.py, extract_api.py -- widely imported across the graph module.
- STALE: none -- correctly re-exports the sovereign_held predicate post-consolidation (dual try/except import pattern documented as deliberate).
- note: Foundational, widely-imported module -- 'the estate's structural spine' per nerves_resolve.py's own description, and the import fan-out here confirms that claim is true (unlike nerves_traffic.py's unfulfilled claim).

### org/modules/graph/transform_cli.py
- purpose: comp-transform: traces client-side data flow inside React components (fetch -> response type -> useMemo/useCallback chains -> rendered JSX fields).
- last_touch: 6b69b126c3 2026-07-10 3.0.0_SA_CVO~A
- consumers: TOOL_MASTER.yaml; imported by pii_cli.py and platinum_cli.py (build_component_dataflow / build_all_dataflows).
- STALE: none found.
- note: Widely depended-on by other comp-tools (pii, platinum), not just a leaf CLI.

### org/modules/graph/ts_source.py
- purpose: Comment-aware JS/TS source stripper (character state machine) shared by the graph extractors, built to fix the aum.ts false-presence bug (dead commented-out code matched before live code).
- last_touch: d34e1ed4d7 2026-07-24 1.0.0_SA_CTO~Z
- consumers: comp_constants_complete.py, extract_api.py, extract_routes.py, extract_ts_source.py; tests/test_routes_comment_blindness.py.
- STALE: none -- small, single-purpose, well-tested shared utility; no frozen counts.
- note: Load-bearing shared fix across multiple extractors; regression-tested against the exact incident it closes.

### org/modules/graph/types_cli.py
- purpose: comp-types backend: TypeScript type consumer index, blast-radius, and field-usage audit over portal/src, using the shared msys_argv_guard for safe grep invocation.
- last_touch: cb71ae2e94 2026-07-25 0.8.0_AE_CloudComp~A
- consumers: tests/test_comp_types_index_idempotent_and_fallback.py; TOOL_MASTER.yaml.
- STALE: none -- correctly uses .tools/msys_argv_guard per the CLAUDE.md Git-section mandate (5-member MSYS class), citing it as the interface's first production consumer.
- note: Model citizen for the msys_safe_run mandate -- worth using as the reference pattern for other CLIs that still shell out to grep raw.

### org/modules/graph/validate_cli.py
- purpose: comp-validate: checks gold artifact output invariants pre-S3-upload against per-pipeline (BD/INF) YAML config, with pass-through to standalone validators.
- last_touch: 3258419105 2026-07-23 0.8.0_AE_CloudComp
- consumers: .tools/comp-validate wrapper; comp-output-contracts.yaml, extract_validate.py, sovereign_held.py (imports it); tests (comp_validate_bd_hold, sovereign_held_no_drift); TOOL_MASTER.yaml.
- STALE: none found.
- note: Directly named in CLAUDE.md's compiler-tools table (comp-validate row) as the gold-run signaling step to AE -- high operational relevance.

### org/modules/graph/variance_dimensions.yaml
- purpose: Governed declared-variance-dimension catalog (firm axis: bd/cot/inf + aliases) realizing the ontology rule-bank's VARIANCE section for cross-firm variance verdicts (Canonical/Twin/Fork-Shadow/Variant/Superseded/Orphan).
- last_touch: 5d1161d70c 2026-07-23 1.0.0_SA_CTO~Z
- consumers: debtscan/summary_corpus.py (variance_verdict), NFRA_ONTOLOGY_RULE_BANK.yaml (canonical_source cross-reference).
- STALE: allowed_facets: [] is deliberately empty ('NOT YET GROUNDED' -- strictly advisory per the CTO gate criterion), self-documented as v1/incomplete-by-design rather than drifted; no frozen counts that could go stale.
- note: Correctly self-labeled as advisory-only until firm facets are populated with grounded evidence -- the gate criterion (empty allowed_facets = advisory) prevents a premature-enforcement failure mode.

### org/modules/graph/vectorize_audit_cli.py
- purpose: comp-perf vectorize-audit backend: AST-based pandas-vectorization-opportunity detector over INF gold scripts.
- last_touch: 59ecbec3ee 2026-07-10 3.0.0_SA_CVO~B
- consumers: tests/test_vectorize_audit_ascii.py; TOOL_MASTER.yaml; .tools/comp-perf wrapper.
- STALE: none found.
- note: Standard live comp-tool backend, scoped to data/inf/scripts/gold only (by design, per _GOLD_ROOT constant).

### org/modules/graph/types-index/
- purpose: Live read/write store for `comp-types` (types_cli.py:14 sets _TYPES_INDEX_DIR here; .tools/comp-types wrapper; registered comp-tools.yaml:582-587): per-TypeScript-type consumer/blast-radius index used before editing a portal interface/type/const.
- last_touch: 211ee3bdb8 2026-07-30 1.0.0_SA_CTO~C
- consumers: types_cli.py (engine, reads+writes this dir), .tools/comp-types (wrapper), org/modules/graph/tests/test_comp_types_index_idempotent_and_fallback.py (test coverage), comp-tools.yaml (registry entry)
- STALE: no stale-name/frozen-count issues found: MdpfAggregateAUATimeSeries.yaml was regenerated TODAY (2026-07-30) by 1.0.0_SA_CTO~C, i.e. actively in use, not a dormant snapshot
- STALE: types_cli.py:412-417 documents a since-FIXED bug (2026-07-25) where an unknown type used to silently write a garbage <type>.blast.yaml into this dir with rc=0 -- now fail-closed via _enumerate_known_types() before any write, so the historical debris class this dir was once vulnerable to is closed
- note: each YAML is a point-in-time consumer index (line numbers into portal/src) that will drift as the portal changes, but that is inherent to the tool's contract (re-run comp-types before trusting a stale index) rather than an unmonitored decay -- the directory itself is actively regenerated and tested.

### org/modules/graph/compproof/
- purpose: NFRA_COMPPROOF B: a clean-room TRUE-SANDBOX blind-solver test harness (corpus.py/corpus_loader.py/harness.py/blind_run.py + build_sandbox.sh/spawn_solver.sh) that spawns a fresh, narrative-stripped agent against a filtered-repo copy to test whether comp-tools alone let it reach a real incident's root cause; the harness is UN-FORKED and reused live by NFRA_TOOLHEALTH TH-A (tool_corpus.py/tool_probe.py), the recurring per-tool EFFECTIVE-axis probe that feeds comp-tool-health (TH-B).
- last_touch: e8325cb52a 2026-07-29 0.0.0_AB_MSTR~Z (build_sandbox.sh/spawn_solver.sh -- fixed a hardcoded site path); tool_corpus.py/tool_probe.py touched 2026-07-25 by 1.0.0_SA_CTO
- consumers: org/modules/graph/comp_tool_health.py + comp_tool_health_gate.py (backing .tools/comp-tool-health, the TH-B fused KEEP/FIX/PROMOTE/RETIRE verdict tool) directly import/consume tool_probe.py's effective_feed.json; harness.py is imported by tool_probe.py ('import harness # reuse score_run'); 8 files under org/modules/graph/tests/ (test_tool_probe_discrimination.py, test_effective_feed_unknown_never_false.py, test_cycle_a_ensure_fresh_wire.py, test_cycle_a1_gate_feed_readonly.py, etc.) exercise this module directly.
- STALE: No RENAMED/DELETED-name staleness found -- files predate today's comp-semantic-estates/pipescript rename by weeks and don't reference those names.
- STALE: Untracked, device-local debris nested at org/modules/graph/compproof/org/mcp/{agent_telemetry/*.jsonl,hook_errors.log} -- looks like a spawned solver wrote its own telemetry/hook-error log relative to a wrong cwd into this tree instead of the real org/mcp/; pure junk (~5KB), zero purpose, safe to delete.
- STALE: __pycache__/ (192K, untracked) -- build junk, safe to delete.
- STALE: Inconsistent generated-artifact tracking: solver_view_B-01.txt is TRACKED but solver_view_B-02.txt..B-20.txt (19 files) plus solver_results.json (4.9KB, dated Jul 1, superseded-looking vs. tracked solver_results_full.json) are UNTRACKED -- device-local, invisible to a fresh clone, no obvious reason B-01 alone was committed.
- STALE: effective_probe_log.jsonl (untracked) is described in tool_probe.py's own docstring as 'the canonical APPEND-only per-probe stream' that the live TH-A mechanism writes -- currently only device-local; the derived rollup (effective_feed.json) IS tracked/committed (last 2026-07-12), so the accrued raw history would be lost (not the rollup) if this device were lost.
- note: The core mechanism is live and actively maintained (edited yesterday); do not touch corpus.py/harness.py/corpus_loader.py/tool_probe.py/tool_corpus.py/build_sandbox.sh/spawn_solver.sh. Separately: delete the __pycache__ dir and the stray nested org/mcp/ debris (pure junk); consider git-adding effective_probe_log.jsonl if its accrual history matters, or explicitly documenting it as intentionally-ephemeral scratch.

### org/modules/graph/comp_desc_sensitivity_test.py
- purpose: Conformance/mutant-test suite for comp_desc_sensitivity.py (NFRA_TOOLUNIFY Phase 1) -- one mutant per settled rule, exercised to actually flip.
- last_touch: 3272197a93 2026-07-25 0.8.0_AE_CloudComp~B
- consumers: tests comp_desc_sensitivity.py (exists on disk, org/modules/graph/comp_desc_sensitivity.py); run standalone/pytest-style, no .tools wrapper (test files don't get one)
- STALE: none found; 'LIVE tier prints its own denominators' explicitly avoids frozen-number staleness
- note: Regression guard for a module not in this batch; low risk.

### org/modules/graph/comp_dispatch.py
- purpose: Parses gold_dispatch.sh's declared CATALOG/CHAIN/GROUP blocks read-only to answer which scripts run in what order/gate (orchestration-DAG grain, sibling to comp-pipescript's per-script grain).
- last_touch: f095620b82 2026-07-10 3.0.0_SA_CVO~B
- consumers: .tools/comp-dispatch wrapper (confirmed) calls this file directly
- STALE: comp-pipescript mentions (lines 6-9) are CURRENT-correct: comp-pipescript is the still-live io/deployed tool per CLAUDE.md table, not the renamed estate-traversal tool -- not stale
- note: none

### org/modules/graph/comp_gitdrill.py
- purpose: Drills a graph node to its producer's git TIME axis (commit history / --at vintage / --diff) -- the code-time complement to comp_icedrill's data-time drill.
- last_touch: 68bbf3dd29 2026-07-24 3.0.0_SA_CVO~Z
- consumers: .tools/comp-gitdrill wrapper; registered in .tools/tool_index.py (GENERATED)
- STALE: none found
- note: none

### org/modules/graph/comp_honesty.py
- purpose: Runnable gate for the I1/I2/I3 honesty invariants (honest-missing, per-case measurement, control-must-fire) over a CLAIM+EVIDENCE pair, static AST + evidence modes.
- last_touch: 20858f3dcf 2026-07-07 0.8.0_AE_CloudComp~D
- consumers: .tools/comp-honesty wrapper; imports comp_ladder.py internally
- STALE: none found
- note: none

### org/modules/graph/comp_iam_census.py
- purpose: comp-iam APPLIED-plane census generator with explicit vintage-honesty (fresh-vs-stale coverage banner), implementing CVO's applied-plane design brief.
- last_touch: 72fda2aa56 2026-07-22 0.8.0_AE_CloudComp
- consumers: org/modules/graph/iam_cli.py imports it directly (iam_cli.py is wrapped by .tools/comp-iam); also org/modules/graph/tests/test_iam_census_vintage.py
- STALE: none found
- note: none

### org/modules/graph/comp_iam_investigate.py
- purpose: RoleLastUsed TRIAGE-ONLY signal (deliberately refuses to license 'UNUSED' verdicts -- role-grain evidence cannot license an action-grain deletion).
- last_touch: 1ecfe671fb 2026-07-25 0.8.0_AE_CloudComp~A
- consumers: org/modules/graph/iam_cli.py imports it (wrapped by .tools/comp-iam)
- STALE: none found
- note: none

### org/modules/graph/comp_iam_live.py
- purpose: IAM LIVE-PRIMARY plane -- keys IAM state off real AWS state (via kuzu) rather than Terraform templates, per Andrew's 2026-07-22 flip.
- last_touch: 4a09baa496 2026-07-22 0.8.0_AE_CloudComp
- consumers: org/modules/graph/iam_cli.py imports it (wrapped by .tools/comp-iam)
- STALE: none found
- note: none

### org/modules/graph/comp_iam_usage.py
- purpose: IAM access-plane lifecycle sibling to comp-iam: role-cold classification, who-can-reach, and reach-check (rule-22a-disciplined simulate-principal-policy).
- last_touch: 57d9c8fd20 2026-07-17 1.0.0_SA_CTO
- consumers: .tools/comp-iam-usage wrapper
- STALE: none found
- note: none

### org/modules/graph/comp_icedrill.py
- purpose: Drills a served artifact to its VERSION/PARTITION history across S3/DDB/Iceberg substrates, always naming which substrate answered.
- last_touch: b7b9293533 2026-07-14 1.0.0_SA_CTO~Z
- consumers: .tools/comp-icedrill wrapper; also referenced by .tools/comp-which-routing-test.py
- STALE: none found
- note: none

### org/modules/graph/comp_keys.py
- purpose: Key/partition enumeration primitive (prefix/partitions/exists) answering 'what exists' distinct from freshness -- closes 268 measured raw-aws-ls rail overrides.
- last_touch: b78d41fb07 2026-07-23 0.8.0_AE_CloudComp
- consumers: .tools/comp-keys wrapper; imports comp_output_contract.py
- STALE: none found
- note: none

### org/modules/graph/comp_ladder.py
- purpose: C0->C3 semantic-compression fidelity gate: proves every compressed node decompresses to lexical C0 evidence (LOSSY-up/LOSSLESS-down).
- last_touch: d4a38e902a 2026-07-07 1.0.0_SA_CTO
- consumers: imported by cse_schema.py (S3.6 fidelity binding), comp_recognizer_sdk.py, comp_honesty.py -- no dedicated .tools wrapper (a .tools/comp-glob comment merely uses its filename as an unrelated example, verified false-positive)
- STALE: none found
- note: none

### org/modules/graph/comp_learns_score.py
- purpose: COMPLEARN value-anchored scorer -- ranks build-next/retire candidates on BAD-OUTCOMES-AVERTED, never raw usage count (the Goodhart-avoidance instrument).
- last_touch: ac678ed89d 2026-07-13 1.0.0_SA_CTO~Z
- consumers: .tools/comp-learns-score wrapper AND .tools/comp-tool-health (imports it for the USED axis)
- STALE: none found
- note: none

### org/modules/graph/comp_legacywriter.py
- purpose: WRITER-CONTEST lens joining comp_dataflow's AST resolver with clobber/trigger/aws live axes to flag legacy writers clobbering pipeline artifacts.
- last_touch: d51f6b38a0 2026-07-29 1.0.0_SA_CTO~C
- consumers: .tools/comp-legacywriter wrapper
- STALE: lines 106-110, 186-188 mention bare 'pipescript' -- these are CLEARLY-LABELED HISTORICAL narrative (a 170946Z finding, a snapshot 'frozen 2026-06-15') describing a past incident that motivated the current header-contract design, not an instruction to invoke pipescript today -- fine per the historical-mention carve-out
- STALE: estate-coverage-resolver.json (line 192) verified present on disk -- reference is live, not dangling
- note: none

### org/modules/graph/comp_log_auto.py
- purpose: Auto-appends every compiler-tool run to compiler-tools-log.md, called by every comp-* wrapper post-run; loud-not-silent on dropped emissions.
- last_touch: 470b9b316a 2026-07-30 0.7.0_AE_CloudOps
- consumers: 60+ .tools/comp-* wrappers call it directly (confirmed by broad grep -- comp-aws, comp-blast, comp-estate, comp-which, comp-iam, comp-pipescript, etc.)
- STALE: none found; touched today alongside comp_output_contract.py
- note: Core cross-cutting infra; highest blast-radius file in this batch.

### org/modules/graph/comp_marker_read.py
- purpose: The ONE shared marker-headed graph read-API (NFRA_GRAPHUNI P2/D2) so structure tools never read a private stale local cache again.
- last_touch: 08dc06ebe9 2026-07-01 0.8.0_AE_CloudComp~C
- consumers: .tools/comp-depth wrapper (bounded sweep); own docstring names blast/trace/xref/platinum as callers
- STALE: none found
- note: none

### org/modules/graph/comp_msbeff_rebaseline.py
- purpose: Re-verdicts historical comp-tool telemetry rows under the CURRENT derived output contracts (non-destructive, sidecar jsonl only) so MSBEFF's own counts aren't a frozen-vs-derived mix.
- last_touch: c9cc2ea22a 2026-07-30 0.7.0_AE_CloudOps
- consumers: imports comp_output_contract.py; consumed by org/modules/graph/tests/test_e413_dual_basis_preservation.py; no .tools wrapper (ad hoc re-baseline utility by design)
- STALE: none found; touched today, coordinated with comp_output_contract.py/comp_log_auto.py landing
- note: none

### org/modules/graph/comp_ontolint.py
- purpose: Lints the NFRA_ONTOLOGY Relation-vs-Role dual-axis composite exception as a machine-checked invariant read from the rule-bank YAML, replacing prose enforcement.
- last_touch: 2799f8c49c 2026-07-20 0.8.0_AE_CloudComp~C
- consumers: .tools/comp-ontolint wrapper
- STALE: none found; reads the rule-bank live, not a frozen exception list
- note: none

### org/modules/graph/comp_output_contract.py
- purpose: THE output-contract helper (coverage_line/plane_header/verdict_exit_map/classify_exit) -- one implementation, N tool consumers, derived from graph-call-manifest.yaml + comp-output-contracts.yaml at run time.
- last_touch: 470b9b316a 2026-07-30 0.7.0_AE_CloudOps
- consumers: imported by comp_dataflow.py, comp_keys.py, comp_log_auto.py, comp_msbeff_rebaseline.py, manifest_check_cli.py, routes_cli.py, plus 4 test files
- STALE: line 219: 'comp-opalbizsem --list exits 2 both piped and unpiped' is a DATED (2026-07-30) historical measurement note explaining a REFUTED causal hypothesis about rc=120 -- it is explicitly framed as a measured-then-not-the-cause finding, not an instruction that comp-opalbizsem is a current tool (which was deleted/renamed the same day per session context); worth a future cleanup pass since the named tool no longer exists under that name, but it doesn't mislead a reader about current state
- note: Core cross-cutting infra; the stale tool-name mention is cosmetic, not functional (it's inert prose in a comment, not a runtime reference).

### org/modules/graph/comp_parity_cli.py
- purpose: comp-parity: the daily tolerance-aware DATA-parity gate (4 tolerance classes A-D) proving a canonical pipeline can replace BD-served surfaces before the Schwab-SSOT cutover flip.
- last_touch: 0f30067630 2026-07-01 0.8.0_AE_CloudComp~A
- consumers: .tools/comp-parity wrapper
- STALE: none found
- note: Live cutover-gating instrument (49F/Schwab-SSOT is an active workstream per MEMORY) -- if this ever silently degraded it would be the AT-RISK quadrant, but no evidence of decay found.

### org/modules/graph/comp_passcraft.py
- purpose: Recon-scaffolding SDK: templates the mechanical opening moves of a tool front-pass (denominator print, cache/oracle find, archetype lead-probes) and stops at the verdict door -- no verdict engine.
- last_touch: 32141b332b 2026-07-12 3.0.0_SA_CVO~A
- consumers: .tools/comp-passcraft wrapper
- STALE: none found
- note: none

### org/modules/graph/comp_potion_relevance.py
- purpose: POTION SemanticRelevanceProvider swapped into comp_route.route() in place of lexical token-overlap; fail-safe to lexical on any embedder load failure.
- last_touch: 162eb94231 2026-07-28 0.8.0_AE_CloudComp
- consumers: .tools/comp-which wrapper path; imports comp_route_shadow.py
- STALE: none found; recently landed (07-28), part of live route-engine evolution
- note: none

### org/modules/graph/comp_pulse.py
- purpose: comp-pulse: the estate's vital-signs dashboard -- composes NERVES L2 traffic + L3 co-change + L3b risk edges into a DANGER x TRAFFIC intersection view, every number vintage+denominator stamped.
- last_touch: bdc4512a84 2026-07-22 0.8.0_AE_CloudComp
- consumers: .tools/comp-pulse wrapper
- STALE: none found; explicitly designed to invent nothing and carry live vintage/denominator on every number
- note: none

### org/modules/graph/comp_pydeps.py
- purpose: Repo-wide Python REFERENCE graph over .tools/ + org/modules/ (IMPORT/LOADER/etc edges) -- closes the compiler-tools blind spot the DATA/PORTAL trace_graph structurally cannot see.
- last_touch: cf22d5a75a 2026-07-14 1.0.0_SA_CTO~Z
- consumers: .tools/comp-pydeps wrapper
- STALE: none found
- note: none

### org/modules/graph/comp_recognizer_sdk.py
- purpose: Shared Recognizer SDK (COMPILERKIT-P1): the framework the 2 production compilers reconcile onto -- IR=CSE, fidelity gate=comp_ladder, validator=cse_schema.validate.
- last_touch: 4e83065973 2026-07-07 0.8.0_AE_CloudComp~D
- consumers: imported by comp_promote_materializer.py, comp_recognizers_code.py, comp_recognizers_config.py, comp_recognizers_ticket.py, comp_recognizers_tsx.py
- STALE: none found
- note: none

### org/modules/graph/comp_recognizers_code.py
- purpose: COMPILERKIT-P1 compiler #1 (code/infra) recognizer set: dispatch-catalog + S3-key recognizers, pure-lexical, file:line provenance.
- last_touch: 5a74ba345e 2026-07-10 3.0.0_SA_CVO~B
- consumers: imported by comp_recognizers_config.py, comp_recognizers_tsx.py, and 2 test files (test_comp_recognizers_bd_hold.py, test_sovereign_held_no_drift.py)
- STALE: none found
- note: none

### org/modules/graph/comp_recognizers_config.py
- purpose: COMPILERKIT-P2 config-artifact compiler (first non-code class): emits config:{scope}:{artifact} REFERENCES edges into infra entities (S3 buckets, secret refs).
- last_touch: 5a74ba345e 2026-07-10 3.0.0_SA_CVO~B
- consumers: exercised by test_comp_recognizers_bd_hold.py and test_sovereign_held_no_drift.py in bounded sweep
- STALE: none found
- note: Only test-file consumers found for the entry point itself (no .tools wrapper) -- tests are a real regression guard, not treated as orphaned.

### org/modules/graph/comp_recognizers_ticket.py
- purpose: COMPILERKIT-P3 ticket compiler bridging org-intent (TO XML requirement blocks) to code, pure-lexical Requirement->IMPLEMENTS->Component edges.
- last_touch: 4e83065973 2026-07-07 0.8.0_AE_CloudComp~D
- consumers: imported by comp_recognizers_config.py
- STALE: none found
- note: none

### org/modules/graph/comp_recognizers_tsx.py
- purpose: COMPILERKIT-P1 compiler #2: migrates the TSGRAPH frontend-TSX FLOWS_TO extractor onto the shared Recognizer SDK, the symmetric counterpart to comp_recognizers_code.py.
- last_touch: 4e83065973 2026-07-07 0.8.0_AE_CloudComp~D
- consumers: imported by comp_recognizers_config.py
- STALE: none found
- note: none

### org/modules/graph/comp_route.py
- purpose: COMPROUTE core posterior decision engine (score = query_match + surface_prior + history_affinity) -- the intent->capability router comp-which fronts.
- last_touch: 7215ee75cf 2026-07-13 1.0.0_SA_CTO~Z
- consumers: .tools/comp-routable-check and .tools/comp-which wrappers -- the fabric's default-search router
- STALE: line 304 mentions 'comp-iam / comp-freshness / comp-pipescript' -- comp-pipescript is CURRENT-correct (still the live io/deployed tool), not stale
- note: Highest-authority routing file in the batch; correctly current.

### org/modules/graph/comp_route_affinity.py
- purpose: CachedAffinityProvider + affinity-cache emitter -- bridges COMPLEARN tool_activity outcomes into comp_route's LEARNED (w_h) term, deliberately SHADOW (computed+logged, not yet weighting live decisions) pending real-telemetry justification.
- last_touch: 5434b66aa1 2026-07-01 0.8.0_AE_CloudComp~E
- consumers: .tools/comp-which wrapper path
- STALE: own docstring's SHADOW-mode claim ('comp-which keeps affinity_provider=None') is unverified against comp_route.py's CURRENT default arm in this bounded pass -- if the affinity has since flipped live elsewhere, this file's self-description would be stale; not confirmed either way here
- note: Flagging for a follow-up check of comp_route.py's live default affinity_provider wiring, not asserting staleness.

### org/modules/graph/comp_route_eval.py
- purpose: NFRA_COMPPROOF C1 efficacy eval: precision@1/recall for the default router, Goodhart-tier-split, affinity OFF/ON A/B, aligned-by-construction with the DR2 shadow fixture.
- last_touch: 9d7ac49feb 2026-07-07 0.8.0_AE_CloudComp~E
- consumers: imported by comp_route_outcome.py and org/modules/graph/potion/potion_shadow_rank.py (the live POTION relevance work)
- STALE: lines with {'comp-pipescript'} as expected-cap fixtures are CURRENT-correct (comp-pipescript still exists)
- note: none

### org/modules/graph/comp_route_shadow.py
- purpose: DR2 SEV1 safety-gate harness: runs the primary router in parallel with today's comp-which backstop over the full fixture, proving zero regression before any flip.
- last_touch: 2033b8d70e 2026-07-01 0.8.0_AE_CloudComp~C
- consumers: imported by comp_learns_leg4_exercise.py, comp_potion_relevance.py (recent 07-28 live work), comp_route_eval.py, and potion/potion_shadow_rank.py
- STALE: regex on line 84 (r'\\b(comp-[a-z0-9-]+|pipescript)\\b') matches bare 'pipescript' as a tool-name token -- tolerant of historical fixture/log text carrying the old bare name, not an assertion that bare pipescript is currently valid; low-risk, worth a comment update but functionally harmless since bare pipescript is now rc=2 and would never appear in fresh routing output
- note: none material

### org/modules/graph/comp_symbols.py
- purpose: Intra-file symbol-inventory tool (forward enumeration of functions/classes/constants by file, ast.parse, Python now / other languages pluggable later).
- last_touch: e5ae5dd7a2 2026-06-30 0.8.0_AE_CloudComp~E
- consumers: .tools/comp-symbols wrapper
- STALE: none found
- note: none

### org/modules/graph/comp_system.py
- purpose: comp-system compiler: reads live compiled-system state across LOCALROOT knowledge-classes via existing comp-tools and emits infra/system/06_current_state.{md,json}, auto-refreshing on HEAD-advance.
- last_touch: 4d2588f35e 2026-07-25 0.8.0_AE_CloudComp~D
- consumers: .tools/comp-system and .tools/comp-arity wrappers
- STALE: none found; the file's own design explicitly forbids hand-fabricated numbers (grounds every number or marks UNKNOWN-VINTAGE), which is the correct anti-staleness posture the audit is looking for
- note: none

### org/modules/graph/comp_tool_health.py
- purpose: Fused 3-axis (USED/RAIL_CONSISTENT/EFFECTIVE) per-tool health query producing a KEEP/FIX/PROMOTE/RETIRE verdict, read-only fusion over existing telemetry (not a new stack).
- last_touch: 305d88e5b8 2026-07-12 0.8.0_AE_CloudComp
- consumers: .tools/comp-tool-health and .tools/comp-tool-health-gate wrappers; imports comp_learns_score.load_corpus un-forked
- STALE: 3 regex sites (lines 82,102,117) match bare 'pipescript' alongside comp-* tokens for parsing historical corpus rows -- same tolerant-of-old-data pattern as comp_route_shadow.py, not a live-current claim
- note: none material

### org/modules/graph/comp_tool_health_gate.py
- purpose: TH-C close-the-loop acceptance gate: converts each ACTIONABLE (non-KEEP) TH-B verdict into a typed advisory commission (fix/deprecation-cand/route-proposal) the CTO ratifies -- never auto-mutates.
- last_touch: e0bac4db9a 2026-07-12 0.8.0_AE_CloudComp
- consumers: .tools/comp-tool-health-gate wrapper; imports comp_tool_health.health() un-forked
- STALE: none found
- note: none

### org/modules/graph/comp_toolgraph.py
- purpose: Backend for `comp-toolgraph`: computes the comp-tool suite as a quality-annotated graph (nodes/edges/coupling-diff/denominator) and writes the committed census JSON.
- last_touch: 16fbe735c9 2026-07-12 0.8.0_AE_CloudComp
- consumers: .tools/comp-toolgraph wrapper; imported by comp_passcraft.py; referenced in comp-coverage-map.yaml, graph-call-manifest.yaml, TOOL_MASTER.yaml, .tools/tool_index.py
- note: none

### org/modules/graph/comp_trigger.py
- purpose: Read-only EventBridge/Scheduler trigger-dispatch forensics backend for `comp-trigger` (what fires X, DESIRED-vs-LIVE schedule state, CloudWatch TriggeredRules with denominator).
- last_touch: ac678ed89d 2026-07-13 1.0.0_SA_CTO~Z
- consumers: .tools/comp-trigger wrapper
- note: none

### org/modules/graph/comp_which_signals.py
- purpose: NFRA_COMPROUTE DR2 SignalExtractors + 2-tier intent classifier feeding comp-which's route() as priors; shadow-runs alongside the live comp-which cascade pre-flip.
- last_touch: a27628d386 2026-07-25 0.8.0_AE_CloudComp~C
- consumers: comp_pydeps.py, comp_route_outcome.py, comp_route_shadow.py, .tools/hooks/comp-tool-hud.sh
- note: Its `_cap_from_call` docstring example cites 'comp-pipescript' (the live hyphenated medallion tool, distinct from deleted bare pipescript) -- not stale.

### org/modules/graph/comp_ws4_crosswalk.py
- purpose: NFRA_TOOLUNIFY WS-4 SOURCE<->DEPLOYED crosswalk joining local trace_graph.json entities against the kuzu marker-head canonical for LAMBDA/S3_ARTIFACT/COMPONENT/ENDPOINT.
- last_touch: 03c1855a28 2026-07-25 0.8.0_AE_CloudComp~B
- consumers: comp_ws4_crosswalk_test.py; types_cli.py (wrapped by .tools/comp-types)
- note: none

### org/modules/graph/comp_ws4_crosswalk_test.py
- purpose: Conformance suite for comp_ws4_crosswalk.py: offline mutant-per-join-rule tier + a live member-level set-identity sweep against a pinned 2026-07-25 baseline.
- last_touch: 03c1855a28 2026-07-25 0.8.0_AE_CloudComp~B
- consumers: pytest entry point (`python3 -m pytest org/modules/graph/comp_ws4_crosswalk_test.py`); exercises comp_ws4_crosswalk.py
- STALE: Tier-2 baseline is pinned to a 2026-07-25 exercised floor (5 days old at audit time) -- self-declared as tolerant of 2 known currency gaps, not yet re-verified since.
- note: Test suite, low risk if stale (worst case: a masked regression, not a false alarm).

### org/modules/graph/contract_engine.py
- purpose: NFRA_GCONTR period-contracts engine (Q1 structural WRITES-edge diff + Q2 policy JOIN against graph_contracts) shared by `comp-aws contract-diff` and `comp-surface-check check`.
- last_touch: 92733a2e53 2026-06-18 1.0.0_SA_CTO
- consumers: comp_aws_cli.py, surface_check_cli.py, estate_infrastructure_cli.py; referenced in comp-coverage-map.yaml, .tools/tool_index.py
- STALE: contract_engine.py:537 comment describes a 'critical-surfaces:<id> | pipescript:...' blob format -- worth confirming no live contract data still keys on a literal 'pipescript:' prefix post-rename (not verified either way in this pass).
- note: none

### org/modules/graph/coverage_cli.py
- purpose: Backend for `comp-coverage`: audits compiler-tools TO compliance by classifying TOs (FRONTEND/GOLD/API/DOC) against org/compiler-tools-log.md completion status.
- last_touch: 33146f0297 2026-07-10 3.0.0_SA_CVO~B
- consumers: .tools/comp-coverage wrapper; referenced in TOOL_MASTER.yaml
- note: none

### org/modules/graph/critical-alarm-egress.yaml
- purpose: Registry of SNS topics that must have a CONFIRMED-deliverable subscriber (not merely present) for critical-surface CloudWatch alarms; consumed by the egress-check leg of comp-surface-check.
- last_touch: ae63b4d24a 2026-06-25 1.0.0_SA_CTO
- consumers: surface_check_cli.py (`comp-surface-check egress-check`)
- STALE: opal-bd-49f-cookie-alerts entry's `alarms: []` is marked as a seed/placeholder ('confirm/extend at first egress-check run') -- unclear if that reconciliation has ever actually run.
- note: Predates the 2026-07-28 alarm/SNS moratorium (built for a real 2026-06-25 SEV1 with COO/CTO sign-off) -- not a moratorium violation, just old enough to flag for a live egress-check re-run.

### org/modules/graph/cse_schema.py
- purpose: NFRA_CSE.P1 Canonical Semantic Event contract + versioned semantic algebra validator (enums-as-code, fail-closed validator, CloudNode/CloudEdge mapping table) -- DS's executable form of CTO's algebra design.
- last_touch: c903904094 2026-07-18 2.0.0_SA_COO
- consumers: comp_passcraft.py, comp_promote_lifecycle.py, comp_promote_materializer.py, comp_recognizers_code/config/ticket/tsx.py, comp_recognizer_sdk.py, comp_system.py, NFRA_ONTOLOGY_RULE_BANK.yaml, tests/test_passcraft_anti_harness.py
- STALE: Docstring says 'DRAFT for CTO arch-gate... staged here in the DS lane (org/modules/graph is EXEC-lane); CTO/exec places it canonically on the gate' -- yet it has 9+ live importers and has clearly become de facto canonical without that formal re-homing ever being recorded.
- note: Self-description (DRAFT/staged, awaiting arch-gate placement) no longer matches reality (it IS the canonical, heavily-imported implementation) -- a declarative/map-vs-territory drift, not a functional risk.

### org/modules/graph/debris_adapters.py
- purpose: Per-resource-type (S3/DDB/EC2/EventBridge) activity-signal adapters for comp-debris, applying trading-calendar dormancy and cadence-aware windowing so a T-1 weekend isn't misread as debris.
- last_touch: 97f6a8b704 2026-07-17 0.8.0_AE_CloudComp~B
- consumers: comp_debris.py (.tools/comp-debris wrapper); comp-coverage-map.yaml, graph-call-manifest.yaml
- note: none

### org/modules/graph/drift-topology.yaml
- purpose: Declares the estate's cross-seam propagation topology (local->git->cloud->nessie->kuzu->iceberg->trino->served) that comp-drift walks, calling out to each seam's own engine rather than re-implementing checks.
- last_touch: 37f9165400 2026-07-01 0.8.0_AE_CloudComp~D
- consumers: drift_cli.py (.tools/comp-drift wrapper)
- note: none

### org/modules/graph/drift_cli.py
- purpose: Backend for `comp-drift`: the estate propagation-drift orchestrator that fans out across seam engines (comp-pipescript deployed, comp-lambdamap parity, comp-iam reconcile, comp-kuzu, iceberg/trino parity) per drift-topology.yaml, tri-state exit.
- last_touch: eeccc217ad 2026-07-14 1.0.0_SA_CTO~Z
- consumers: .tools/comp-drift wrapper; comp_debt/grounding_lib.py; comp-tools.yaml, TOOL_MASTER.yaml
- note: References to 'comp-pipescript deployed' throughout are the live hyphenated medallion tool (distinct from deleted bare pipescript) -- not stale.

### org/modules/graph/estate-coverage-manifest.yaml
- purpose: Single source of truth for which tool owns which estate thread (owning_tool: comp-pipescript | globgrph | stitch | portal-consumer-tools | none), the input gen-estate-resolver.py joins against the CVO census.
- last_touch: 29c3fedeb8 2026-07-30 3.0.0_SA_CVO
- consumers: gen-estate-resolver.py, estate_infrastructure_cli.py
- STALE: schema field `last_full_review: 2026-06-15` is a hand-typed date, ~6.5 weeks stale relative to the file's own 2026-07-30 last-touch -- a frozen field that does not auto-track the file's real edit history.
- note: owning_tool: comp-pipescript entries throughout are the live hyphenated medallion tool, correct usage, not the deleted bare pipescript.

### org/modules/graph/estate_infrastructure_cli.py
- purpose: The legacy thread-model CLI engine that comp-estate delegates to for named-thread traversal (--list/--resource/--debt/etc); parses the original bare-pipescript argv forms, now reached only via comp-estate.
- last_touch: 7ef6215359 2026-07-30 3.0.0_SA_CVO
- consumers: opal_estate_infrastructure.py, comp_api.py; referenced in comp-coverage-map.yaml, comp-output-contracts.yaml, comp-tools.yaml, graph-call-manifest.yaml
- note: Correctly and explicitly self-labels its rename ('RENAMED from pipescript_cli.py 2026-07-30... do not invoke it standalone') -- a clean example of a properly-flagged historical mention, not stale.

### org/modules/graph/extract_api.py
- purpose: Pass 1 of trace_graph: regex-extracts COMPONENT->ENDPOINT edges from portal/src/api/endpoints + pages fetch-call sites.
- last_touch: b6e4a784cf 2026-07-22 0.8.0_AE_CloudComp
- consumers: extract_lambda_routes.py, comp_recognizers_tsx.py, comp_recognizer_sdk.py, comp_ws4_crosswalk.py, trace_graph.py
- note: none

### org/modules/graph/extract_assets.py
- purpose: Extraction pass for the opal-data-assets monolith's dynamic-key silver artifacts, closing a comp-blast NOT-FOUND blind spot the hardcoded-path extractors missed.
- last_touch: c628e7b54e 2026-07-22 0.8.0_AE_CloudComp
- consumers: pipeline_cli.py, trace_graph.py; own test tests/test_extract_assets.py
- note: none

### org/modules/graph/extract_event_invoke.py
- purpose: Pass 8: bridges SQS/DynamoDB-stream/Kinesis event-source-mappings, SNS-subscription, and S3 bucket-notification Lambda invokers into trace_graph for blast-radius completeness.
- last_touch: 7ad3334aaf 2026-07-06 0.8.0_AE_CloudComp
- consumers: comp_recognizer_sdk.py, trace_graph.py
- note: none

### org/modules/graph/extract_eventbridge.py
- purpose: Pass 4: extracts EventBridge TRIGGERS edges (schedule rules + rule->Lambda targets) from Terraform eventbridge.tf files.
- last_touch: 75d93eaf70 2026-07-07 0.8.0_AE_CloudComp
- consumers: extract_sfn.py, trace_graph.py
- note: none

### org/modules/graph/extract_iam.py
- purpose: IAM permission cross-reference: scans Lambda/gold-EC2 source for AWS operations and cross-references against Terraform IAM policy documents to flag under-permissioned calls.
- last_touch: dec85522d7 2026-07-25 0.8.0_AE_CloudComp~A
- consumers: iam_cli.py (.tools/comp-iam wrapper), prod_write_guard.py, sovereign_held.py; 10+ dedicated tests under tests/
- note: This is the module CLAUDE.md rule 22a documents as necessary-but-insufficient (models (action) not (action,resource), several known blind axes) -- that caveat is about its INHERENT scope, not staleness; the module itself is actively maintained (2812 lines, heavily tested).

### org/modules/graph/extract_lambda_routes.py
- purpose: Pass 5: connects ENDPOINT nodes to LAMBDA nodes via lambda-source-map.json directory mapping + handler-source route-pattern scanning.
- last_touch: 19e4177db0 2026-07-10 3.0.0_SA_CVO~B
- consumers: trace_graph.py
- note: none

### org/modules/graph/extract_pipeline.py
- purpose: Authoritative gold-script I/O DAG extractor using lib/s3_layout.py constants + gold_dispatch.sh (vs. extract_s3.py's regex heuristics) for pipescript/comp-pipescript io/deployed.
- last_touch: e8fa952ad1 2026-07-11 3.0.0_SA_CVO~B
- consumers: pipeline_cli.py, platinum_cli.py, trace_graph.py; 5 dedicated tests
- note: Comments reference 'comp-pipescript io' output (live hyphenated tool) correctly, not the deleted bare pipescript.

### org/modules/graph/extract_routes.py
- purpose: Maps the full S3-artifact-to-frontend-component serving path via cloudfront-distribution.tf, the shared-advisor-router rewrite rules, api-gateway.tf, and endpoint files.
- last_touch: b9f80e6dae 2026-07-24 0.8.0_AE_CloudComp~A
- consumers: pii_cli.py, pipeline_cli.py, platinum_cli.py, routes_cli.py (comp-routes); 3 dedicated tests
- note: none

### org/modules/graph/extract_s3.py
- purpose: Pass 2: extracts WRITES_S3/READS_S3 edges from gold-script write patterns and Lambda read patterns, plus gold-script run_order from filename prefix.
- last_touch: bd61228a49 2026-07-10 3.0.0_SA_CVO~B
- consumers: extract_pipeline.py, pipeline_cli.py, trace_graph.py
- note: none

### org/modules/graph/extract_sfn.py
- purpose: Pass 7: projects Step-Functions state-machine -> Lambda INVOKE edges into trace_graph for blast-radius completeness on SFN-orchestrated Lambdas.
- last_touch: 3a7a6cce22 2026-07-06 0.8.0_AE_CloudComp
- consumers: extract_event_invoke.py, trace_graph.py
- note: none

### org/modules/graph/extract_transforms.py
- purpose: Traces client-side React data flow (fetch->response var->useMemo/useCallback chains->rendered fields) to answer what fields a component actually uses.
- last_touch: 6b69b126c3 2026-07-10 3.0.0_SA_CVO~A
- consumers: pii_cli.py, platinum_cli.py, transform_cli.py (comp-transform); 2 dedicated tests
- note: none

### org/modules/graph/extract_ts_source.py
- purpose: Comment-aware JS/TS source-handling utility for the graph extractors, built to stop dead/commented-out code from first-match-winning over live calls (the aum.ts false-presence incident).
- last_touch: b6e4a784cf 2026-07-22 0.8.0_AE_CloudComp
- consumers: extract_api.py, extract_routes.py, comp_constants_complete.py; tests/test_routes_comment_blindness.py
- note: none

### org/modules/graph/extract_validate.py
- purpose: Gold-artifact invariant validator: checks declared invariants (gold_validate_config.yaml) against a local JSON/parquet artifact before S3 upload.
- last_touch: d0e2226b88 2026-06-11 0.7.0_AE_CloudOps
- consumers: validate_cli.py (comp-validate); tests/test_failure_class_hardening.py
- note: Its own comment correctly defers source-level checks to 'comp-pipescript io' (live hyphenated tool), not stale.

### org/modules/graph/gen-estate-resolver.py
- purpose: Generates estate-coverage-resolver.json by joining CVO's authoritative estate-coverage-manifest.yaml routing with per-thread census detail; corrected an earlier heuristic that over-assigned comp-pipescript (79 vs correct 13).
- last_touch: d4e70fd056 2026-06-23 2.0.0_SA_COO
- consumers: estate_infrastructure_cli.py, opal_estate_infrastructure.py
- STALE: gen-estate-resolver.py:2 docstring calls the resolver 'the pipescript CLI read-source' -- bare 'pipescript' is the prohibited/tombstoned name as of today; should read comp-estate.
- STALE: gen-estate-resolver.py:82 comment: 'the resource enumeration `pipescript <name>` surfaces' -- same bare-name staleness.
- note: Cosmetic/comment-only staleness (predates today's rename by 5 weeks); does not affect the script's actual behavior, which still correctly regenerates the live comp-estate read-source.

### org/modules/graph/grain_baseline.json
- purpose: Certified per-node-class magnitude baseline (2026-06-11, kuzu_stitch_db) used by grain_sentinel's AC-GRAIN.2 band check to catch wrong-grain graph explosions/collapses.
- last_touch: fc8b81ec09 2026-07-25 1.0.0_SA_CTO~Z
- consumers: infra/aws/globgrph/derive_stitch.py (_load_grain_baseline, passed into run_grain_sentinel) -- outside the org/modules/graph + .tools bounded sweep, found via a wider check
- STALE: 'certified' field is dated 2026-06-11, ~7 weeks old at audit time, with no automatic refresh mechanism -- purely hand-updated.
- note: Fail-open by design (derive_stitch.py's _load_grain_baseline returns {} on any read error, degrading to AC-GRAIN.1-only) and the magnitude band is wide (0.4x-2.5x), so staleness risk is low despite the frozen date. Note separately: comp_aws_cli.py's two run_grain_sentinel() call sites omit the baseline argument entirely, so AC-GRAIN.2 never fires via `comp-aws` -- only via derive_stitch.py.

### org/modules/graph/grain_sentinel.py
- purpose: Structural identity/grain invariant library (AC-GRAIN.1 id-format + AC-GRAIN.2 magnitude-band checks) built after AC4's untyped==0 bar missed 23,664 phantom S3_BUCKET nodes that were mis-typed object keys.
- last_touch: ba8d9908b5 2026-07-25 1.0.0_SA_CTO~Z
- consumers: comp_aws_cli.py (comp-aws derive/AC-GRAIN.1-only), infra/aws/globgrph/derive_stitch.py (full AC-GRAIN.1+2 with grain_baseline.json)
- note: none

### org/modules/graph/graph-call-manifest.yaml
- purpose: Authoritative catalog of every graph use-case -> canonical call, mandated by CLAUDE.md rule 20 and gated by comp-manifest-check.
- last_touch: 7ef6215359 2026-07-30 3.0.0_SA_CVO
- consumers: gate-enforced registry (comp-manifest-check); cited throughout CLAUDE.md and every comp-* tool docstring
- note: Actively and correctly self-maintained through today's rename -- contains explicit correction notes (e.g. line ~1030, ~446, ~1500) documenting the pipescript->comp-semantic-estates->comp-estate lineage and marking old names deleted/do-not-resolve. A good example of a live registry kept current.

### org/modules/graph/graph_cache.py
- purpose: Shared query-vs-rebuild freshness contract (NFRA_GRAPHS D2/D3) so every rebuild-capable graph tool answers 'query vs rebuild' the same way.
- last_touch: 44d93e9a12 2026-07-09 0.8.0_AE_CloudComp
- consumers: comp_system.py, graph_compiler.py (dead consumer, see below), graph_status_cli.py (comp-graph wrapper), platinum_cli.py; tests/test_graphuni_headpin_d4.py
- note: One of its listed importers (graph_compiler.py) is itself dead code (see that entry) -- does not affect this file's status since graph_status_cli.py/platinum_cli.py are live consumers.

### org/modules/graph/graph_status_cli.py
- purpose: Backend for `comp-graph status`: one place reporting which dependency graphs exist, how fresh each is, and when last derived (local .comp-graph/ trace caches + cloud/kuzu).
- last_touch: ee49b14381 2026-07-09 0.8.0_AE_CloudComp
- consumers: .tools/comp-graph wrapper; cli.py, TOOL_MASTER.yaml
- note: none

### org/modules/graph/iam_cli.py
- purpose: Backend for `comp-iam`: IAM permission cross-reference for Lambda/EC2 scripts against Terraform policy documents (service/gaps/reconcile/investigate-candidates subcommands).
- last_touch: 1ecfe671fb 2026-07-25 0.8.0_AE_CloudComp~A
- consumers: .tools/comp-iam wrapper; comp_api.py, comp_iam_census.py, comp_iam_investigate.py, comp_iam_live.py, drift_cli.py; multiple tests
- note: This is the tool CLAUDE.md rule 22a extensively caveats (necessary-but-insufficient for new-ARN grants, (action)-only modeling) -- an inherent-scope caveat, not evidence of staleness in the file itself.

### org/modules/graph/iam_dr_exempt_roles.json
- purpose: DR/break-glass role exemption declaration for `comp-iam investigate-candidates` -- roles listed here still render their real verdict, marked exempt alongside it, never silently hidden.
- last_touch: e0b0fed0a8 2026-07-25 1.0.0_SA_CTO~Z
- consumers: comp_iam_investigate.py
- note: Content is intentionally empty (exempt_roles: [], reason: "") with a self-explaining comment that no DR role has been identified yet -- not stale, a legitimate not-yet-populated state.

### org/modules/graph/incrparity_cli.py
- purpose: Backend for `comp-incrparity`: validates parity between incremental and full gold-script runs for a given script/date, diffing to stderr + S3 on mismatch.
- last_touch: f9ddda52f7 2026-07-25 0.8.0_AE_CloudComp~E
- consumers: .tools/comp-incrparity wrapper; tests/test_incrparity_cli_bd_hold.py, tests/test_sovereign_held_no_drift.py
- note: Comment notes a smoke-path fixture 'derived from pipescript IO' -- referring to the live comp-pipescript io output format, not the deleted bare command; not stale.

### org/modules/graph/COMPTOOL_REGISTRATION_FLOW.md
- purpose: Canonical, CTO-arch-gated process doc for creating/revising/registering/excluding a comp-tool, backing the comp-manifest-check five-member completeness gate.
- last_touch: 47c84ecdbe 2026-07-21 3.0.0_SA_CVO
- consumers: Referenced from 0.8.0_AE_CloudComp/prompt.md; documents the live comp-manifest-check gate (org/modules/graph/manifest_check_cli.py) that runs inside safe-commit
- STALE: Line 15: "77 tracked comp-* launchers today, up from 62 on 2026-07-14" is a hand-frozen count now superseded -- TOOL_MASTER.yaml (generated today) reports counts.tools=91
- note: Low risk: the file's own thesis is 'the gate is the check, not this prose', so the stale digit doesn't undermine the enforced mechanism.

### org/modules/graph/ESTATE_WORLD_MODEL_PROCESS.md
- purpose: Today's canonical process-of-record for the comp-estate world model's 4-layer granularity ladder (named_thread/family/resource/served-key), commissioned by Andrew 2026-07-30.
- last_touch: 222b0c27ce 2026-07-30 3.0.0_SA_CVO
- consumers: comp-tools.yaml's comp-estate entry and gen-estate-resolver.py's `generated_from` both point here (stated in the file's own line 7)
- note: Freshly authored same day as this audit; its own counts table explicitly labels each number's derivation mode (HAND-legislated vs DERIVED), a model example of not hiding a frozen digit.

### org/modules/graph/NFRA_ONTOLOGY_C2C3_CANONICAL.yaml
- purpose: Canonical C2 motif-family / C3 system catalog plus C4 verticals layer, authored today under Andrew's sovereign ontology ruling.
- last_touch: 29c3fedeb8 2026-07-30 3.0.0_SA_CVO
- consumers: Extends NFRA_ONTOLOGY_RULE_BANK.yaml; canon-patterns.yaml defers to the rule-bank pair for the archetype vocab
- note: None -- same-day authoritative ruling.

### org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml
- purpose: Machine-readable ontology rule bank (14 Roles / 10 Relations / 6 Variance verdicts) consumed by classifiers (COMPSIMILAR, the canon-deviation adapter, canon-patterns.yaml).
- last_touch: 222b0c27ce 2026-07-30 3.0.0_SA_CVO
- consumers: canon-patterns.yaml (declares this file its canonical_source at line ~25 there); NFRA_ONTOLOGY_C2C3_CANONICAL.yaml (extends it)
- STALE: Header carries two different grounding vintages for comp-kuzu ('2026-07-18T02:18Z' at line 8 vs '2026-07-23T14:52Z' at line 17) without reconciling which is current
- note: Minor: dual vintage stamps in one header could confuse a reader about which comp-kuzu snapshot the bindings are actually grounded on; not a functional defect.

### org/modules/graph/__init__.py
- purpose: One-line package docstring making org/modules/graph importable as a Python package.
- last_touch: 0848bd7093 2026-04-09 1.0.0_SA_CTO
- consumers: implicit -- required for every `import` of a sibling module in this directory
- note: Trivial, no risk.

### org/modules/graph/axes_history.jsonl
- purpose: Append-only run-log of comp-axes drill executions (heat/pulse/freshness/learns-gaps/fedobs-signals...), one JSON line per axis per run with elapsed_s/status/summary/vintage.
- last_touch: c442002730 2026-07-15 0.8.0_AE_CloudComp~Z
- consumers: .tools/comp-axes (writer), .tools/tool_index.py, comp-coverage-map.yaml, comp-tools.yaml (registry entries)
- STALE: Only 16 lines total; last entry 2026-07-15T20:22:55Z -- comp-axes appears not to have been run in 15 days; the last captured 'learns-gaps' entry itself self-reports DEGRADED/stale data ('BEHIND flag... stale catalog', lag_h 153.3)
- note: Not a defect in the file itself, but its idleness means anyone reading it today gets a 15-day-old cross-section rather than current axis health.

### org/modules/graph/boundary_report.py
- purpose: Shared BoundaryReport type/contract every NFRA_TOOLSTACK sensor emits (address-space tagging + vocabulary-denominator reporting) so sensor outputs are commensurable.
- last_touch: 48f5ab1037 2026-07-25 1.0.0_SA_CTO~Z
- consumers: org/modules/graph/tests/test_boundary_report_conformance.py, test_e5_recall_standard_arity_limits.py; real sensors org/tier2_senior/0.8.0_AE_CloudComp/deliverables/l1a_item1b/sensor_kuzu_schema_residue.py, sensor_lambda_env_residue.py, l1a_sensor2/sensor_cache_residue.py, l2_aggregate/l2_aggregate.py
- note: Well-tested, genuinely imported shared library type -- none found.

### org/modules/graph/cache_cli.py
- purpose: comp-cache: React Query cache-key collision and type-mismatch detector across portal components.
- last_touch: 17cfd531b1 2026-07-25 0.8.0_AE_CloudComp~E
- consumers: .tools/comp-cache wrapper
- note: None found.

### org/modules/graph/canon-patterns.yaml
- purpose: CTO-authored canonical path-motif library (e.g. PIPELINE_CANON bronze->silver->gold->platinum) the DE/AE debt scorer diffs live paths against; adapter binding down to NFRA_ONTOLOGY_RULE_BANK.yaml's archetype vocab.
- last_touch: f7eef81f19 2026-07-19 1.0.0_SA_CTO
- consumers: TO-D3 scorer/DE-AE build; pairs_with graph-call-manifest.yaml and debtscan/suppression_v1.yaml
- STALE: Lines 30,34,39,51,53,63-64 use bare 'pipescript' as shorthand for the comp-pipescript flow graph -- this is the still-live, DIFFERENT tool from the deleted comp-semantic-estates, so NOT stale under today's rename, but the naming overlap is a readability trap for a fast reader given the tombstone context
- note: No functional staleness; flagged only for the name-collision-with-deleted-tool readability risk.

### org/modules/graph/chainrun_cli.py
- purpose: comp-chainrun: VALGATE Class-B pre/post chain-run sentinel-diff gate, catching partial-refactor leaks across an atomic-bundle ship.
- last_touch: 1fc318f31b 2026-07-10 3.0.0_SA_CVO~B
- consumers: .tools/comp-chainrun wrapper
- note: None found.

### org/modules/graph/cli.py
- purpose: CLI entry point for the original full-stack trace / blast-radius engine (comp-trace and comp-blast).
- last_touch: 1ca9b375dd 2026-07-29 3.0.0_SA_CVO
- consumers: .tools/comp-trace and .tools/comp-blast wrappers (both confirmed to call `cli.py trace/blast`); named throughout comp-tools-segment-scope.md and DESIGN.md
- STALE: Module docstring lines 6-9 say 'Or via bash wrappers: opal-trace ... / opal-blast ...' -- neither .tools/opal-trace nor .tools/opal-blast exists on disk (confirmed); the live wrappers are named .tools/comp-trace and .tools/comp-blast
- note: Pure in-file documentation drift (category d, referenced-but-nonexistent tool names); runtime is unaffected because the real wrappers correctly invoke `cli.py trace/blast`.

### org/modules/graph/clobber_scan.py
- purpose: comp-clobber: output-key collision scanner -- finds two distinct producers writing the same S3/DynamoDB sink (static code scan + live etag-lineage oracle).
- last_touch: 7a07814b94 2026-07-22 1.0.0_SA_CTO
- consumers: .tools/comp-clobber wrapper
- note: None found.

### org/modules/graph/comp-coverage-map.yaml
- purpose: The source-of-truth ledger for every comp-tool's (surface|seam) x granularity x concern home; drives the comp-manifest-check/coverage-check gates and the tools_index projection.
- last_touch: 29c3fedeb8 2026-07-30 3.0.0_SA_CVO
- consumers: comp_coverage_check.py (the gate), comp_coverage_view.py (the projector), comp_capability_provider.py, TOOL_MASTER.yaml's population_authority
- STALE: Line 564 / comment near line 1066: 'union(tools,meta_tools)=49 as of 2026-07-01' is a hand-frozen count now 4 weeks stale -- TOOL_MASTER.yaml (generated today from this same file) reports counts.tools=91. This is precisely the frozen-count anti-pattern CLAUDE.md itself names ('the prior frozen 62/49 drifted to 78->79 within one session')
- note: The stale digit lives in a YAML comment, not in code the gate evaluates (the gate enumerates the live tools[]/meta_tools[] arrays), so gate correctness is unaffected -- but a human/agent reading the comment for orientation gets a materially wrong number, and this is the exact file CLAUDE.md's own text was warning about.

### org/modules/graph/comp-learns-backlog.md
- purpose: Append-only, deduped backlog bridging comp-learns-status gap detection to build/decline dispositions (the gap->build bridge, NFRA_COMPCLOSE).
- last_touch: b4fca85eae 2026-07-23 2.0.0_SA_COO
- consumers: COO /drive reads the OPEN head each cycle (per the file's own header); CTO ratifies BUILD/DECLINE entries in place
- note: Self-describing anti-drift discipline (entries never silently re-ranked, closures require citation) mitigates staleness risk by design.

### org/modules/graph/comp-output-contracts.yaml
- purpose: Gate-enforced registry of each comp-tool's declared exit-code/output contract (verdict classes, blind spots), exercised and validated at commit/CI time.
- last_touch: 6e3f24676d 2026-07-30 3.0.0_SA_CVO
- consumers: comp-coverage-check family; CVO's declare-by-exercise discipline
- note: Already correctly documents today's comp-semantic-estates deletion (line 465) and lists bare 'pipescript' in pending_declaration (line 521) as a tombstone awaiting a formal contract -- reconciled, not stale.

### org/modules/graph/comp-tools.yaml
- purpose: The full agent-facing comp-tool catalog (commands, use-cases, distinct-from notes) -- the main reference table CLAUDE.md points every agent to.
- last_touch: 29c3fedeb8 2026-07-30 3.0.0_SA_CVO
- consumers: CLAUDE.md ('reference: org/modules/graph/comp-tools.yaml'), comp_capability_provider.py, comp-which routing
- note: Already fully reconciled with today's rename (line 291: 'comp-estate: RENAMED from pipescript 2026-07-30').

### org/modules/graph/comp_api.py
- purpose: In-process Python facade composing multiple comp-tool CLI modules without subprocessing, working around the Windows python-subprocess-bash-launcher limitation.
- last_touch: 29c3fedeb8 2026-07-30 3.0.0_SA_CVO
- consumers: org/modules/graph/estate_infrastructure_cli.py (the renamed pipescript_cli.py)
- note: Already correctly names 'comp-estate->opal_estate_infrastructure' (post-rename accurate) in its own docstring -- touched the same day as the consolidation and consistent with it.

### org/modules/graph/comp_assets.py
- purpose: Read-only backfill census over the OPAL_ASSETS s3://opal-data-assets monolith -- reconciles what is LISTED (S3 truth) vs what is CLAIMED (each channel's own backfill-status.json) per channel folder.
- last_touch: 4c8f2803cb 2026-07-14 2.0.0_SA_COO
- consumers: .tools/comp-assets wrapper
- note: None found.

### org/modules/graph/comp_aws_cli.py
- purpose: comp-aws: comprehensive AWS cloud compiler reconciling Terraform (declared), live boto3 (applied), and source provenance into a typed drift-classed graph (largest file in batch, 156KB).
- last_touch: 37b76f7ecc 2026-07-10 3.0.0_SA_CVO~A
- consumers: .tools/comp-aws wrapper; documented (staleley) by comp-aws-agent-usage.yaml
- note: Sampled head only per size guidance (156KB) -- deep-body staleness not exhaustively verified beyond the header/purpose.

### org/modules/graph/comp_capability_provider.py
- purpose: NFRA_COMPROUTE L2 capability-map provider -- exposes comp-coverage-map.yaml as typed Capability records behind a provider-agnostic interface for comp-which's routing engine.
- last_touch: b917f2fafd 2026-07-28 0.8.0_AE_CloudComp
- consumers: .tools/comp-routable-check, .tools/comp-which wrappers
- note: None found.

### org/modules/graph/comp_constants_cli.py
- purpose: comp-constants: AST-based constant-drift indexer, drift gate, and discovery surface across lane-scoped search surfaces.
- last_touch: 2bc837ee41 2026-07-25 0.8.0_AE_CloudComp~E
- consumers: .tools/comp-constants wrapper; .tools/commit-gate.sh
- note: This is the tool whose live config (comp-constants.config.yaml at workspace root) the org/modules/graph seed files no longer feed -- see the four comp-constants-seed-*.yaml TRASH-CANDIDATE findings above.

### org/modules/graph/comp_constants_complete.py
- purpose: The enumeration-completeness axis for comp-constants -- asserts a lane's constant set is COMPLETE over its declared scope against firm_registry.json, not merely drift-free between sites.
- last_touch: d9b665de33 2026-07-22 0.8.0_AE_CloudComp
- consumers: comp_constants_cli.py (imports it); org/modules/graph/tests/test_comp_constants_complete.py
- note: None found.

### org/modules/graph/comp_coverage_check.py
- purpose: THE gate enforcing comp-coverage-map.yaml's schema.gate_contract.rules (one_home, seam_reference_integrity, declared_non_redundancy, coverage_single_home, no_trino_phantom_seam, inventory_completeness, plus projection-currency).
- last_touch: 0d08fbb386 2026-07-10 3.0.0_SA_CVO~A
- consumers: .tools/comp-coverage-check wrapper
- note: The gate reads live tools[]/meta_tools[] arrays, not the stale '49 as of 2026-07-01' comment flagged in comp-coverage-map.yaml, so gate correctness is unaffected by that specific comment.

### org/modules/graph/comp_coverage_view.py
- purpose: Projects comp-coverage-map.yaml's ledger into the tools_index generated view (graph-call-manifest.yaml's projection); provides the projection-currency check comp_coverage_check.py uses.
- last_touch: 6560cc103c 2026-06-30 0.8.0_AE_CloudComp~C
- consumers: comp_coverage_check.py (`import comp_coverage_view` at its line 42), comp_system.py, TOOL_MASTER.yaml/.tools/tool_index.py ecosystem, comp-coverage-map.yaml
- note: No standalone .tools/comp-* wrapper -- used in-process only, which is by design per its own docstring ('Run --verify in CI / at S2 gate time').

### org/modules/graph/comp_dataflow.py
- purpose: comp-dataflow: answers 'does this value come from the CANONICAL source, or somewhere else?' -- catches served-artifact-used-as-source violations (the layer-grammar-backwards defect class).
- last_touch: 6327b00060 2026-07-23 0.8.0_AE_CloudComp~A
- consumers: .tools/comp-dataflow wrapper
- note: None found.

### org/modules/graph/comp_debris.py
- purpose: comp-debris: coldest-first cloud-resource invocation-coldness ledger (advisory, never deletes) -- ranks dormant AWS resources for human review.
- last_touch: 97f6a8b704 2026-07-17 0.8.0_AE_CloudComp~B
- consumers: .tools/comp-debris, .tools/comp-iam-usage wrappers
- note: None found.

### org/modules/graph/comp_depth_cli.py
- purpose: comp-depth: depth-scoped querying (grain coordinate) on the marker-head graph, complementing breadth tools (blast/trace/xref) with a size-invariant grain argument.
- last_touch: 3e8d457a92 2026-07-01 0.8.0_AE_CloudComp~C
- consumers: .tools/comp-depth wrapper (name also co-occurs in comp-dispatch/comp-learns-status/comp-symbols/comp-tool-health strings, likely incidental cross-reference rather than each wrapping it)
- note: None found.

### org/modules/graph/debtscan/
- purpose: NFRA_DEBTSCAN estate tree: home of comp-dups (dup_scan.py) and comp-similar (comp_similar.py + summary_corpus.py) live engines, plus the D1-D5/TOOL01/TOOLDEFECT dated census-wave ledgers, canon-motif design docs, suppression registry, and gitignored generated outputs (canon_motif/, dups_latest.json).
- last_touch: 984d0be0c7 2026-07-19 0.7.0_AE_CloudOps~B (summary_corpus.py, most-recent live-code touch)
- consumers: dup_scan.py <- .tools/comp-dups wrapper; comp_similar.py <- .tools/comp-similar wrapper; summary_corpus.py <- .tools/comp-describe, comp-similar, AND infra/aws/globgrph/resource_summaries_store.py (imports build_corpus directly); suppression_v1.yaml read by comp_debt signal adapters.
- STALE: AT-RISK-adjacent, unenforced directive: 2026-07-09_LIVE_DO-NOT-DELETE_bd-allocation-processor.md declares an ACTIVE SUPPRESSION on a production Lambda ('do not reap, do not disable') but the resource name 'bd-allocation-processor' appears in NEITHER suppression_v1.yaml NOR keep-dormant.yaml -- the do-not-delete is prose-only, not wired into any mechanical gate a decommission sweep would consult. Its own text sets a review-gate condition ('may be reconsidered ONLY after the bd-49f-runner sentinel/as_of seam fix lands') that is now 3 weeks old and unverified as met/unmet from this file alone.
- STALE: (a) minor: comp_debt_standing_scan_spec.md line ~18 and 2026-06-12_TOOL01_completion_ae06.md reference 'pipescript' as a live tool name (pre-rename spec/report text) -- both are explicitly dated (2026-07-07 / 2026-06-12), so this is the labeled-historical case the audit brief says is fine, not live drift.
- STALE: (b) DUPS_summary.md carries a frozen '523 pairs' suppression count from 2026-06-26 with no runtime re-derivation in the file itself, but the file's own header discloses this ('Auto-emitted... tracked audit trail'; full JSON is gitignored/regenerable) -- self-disclosed snapshot, not a misleading current-state claim.
- STALE: (e) canon_motif/ and the top-level canon_motif JSON/DUPS JSONs are dated snapshots with a real refresh mechanism (comp-canon-motif --ledger, comp-dups --nightly) and real consumers -- not the dangerous quadrant since they ARE refreshed, just gitignored (device-local, not shipped in a fresh clone, which is by design per .gitignore lines 85-86).
- note: The DO-NOT-DELETE file's protection is entirely social/documentary -- nothing in the suppression/keep-dormant machinery would stop an automated reap of bd-allocation-processor; recommend either registering it in suppression_v1.yaml/keep-dormant.yaml or re-verifying and closing this note now that 3 weeks have passed.

### org/modules/graph/aws-shapes/
- purpose: NFRA_COMPAWS hand-audit oracle tree: CVO-certified ground-truth fixtures (s3/iam-ec2/stepfunctions hand-audit YAMLs) that comp_aws_cli.py loads at runtime to score its derived-edge cert, plus g2_edge_oracle.py (independent boto3 edge census generator) and archived aws-shape_*.tar.gz snapshot baselines.
- last_touch: a801d64eb4 2026-07-01 0.8.0_AE_CloudComp~A (stepfunctions-live-census-20260701.json, most recent)
- consumers: s3-hand-audit-fixture-v1.1.yaml, iam-ec2-hand-audit-fixture-v0.1.yaml, stepfunctions-hand-audit-fixture-v0.1.yaml <- org/modules/graph/comp_aws_cli.py:_load_fixture (lines 2340/2367/2428), also org/modules/graph/tests/test_comp_aws_cert_mutants.py; g2-edge-census-cut1.yaml/g2_edge_oracle.py referenced from org/modules/graph/comp_aws_cli.py and extract_iam.py as the independent PASS-2 cert oracle.
- STALE: (c)-adjacent superseded-but-present: s3-hand-audit-fixture-v1.0.yaml (2026-06-08) is superseded by v1.1 (2026-06-24) -- comp_aws_cli.py's _load_fixture only ever loads 'v1.1', so v1.0 has zero runtime consumers found in the bounded sweep; kept as a version-history artifact, harmless.
- STALE: eventing-hand-audit-fixture-v0.1.yaml has NO consumer found anywhere in org/modules/graph, .tools, or infra (unlike its s3/iam-ec2/stepfunctions siblings which are all actively _load_fixture'd) -- looks like a hand-audit fixture whose cert leg was never wired into comp_aws_cli.py, or was superseded silently.
- STALE: stepfunctions-live-census-20260701.json is a one-time 'no-drift anchor' cert artifact (self-described as evidence for a specific 2026-07-01 re-cert) with no ongoing consumer -- correctly a point-in-time record, not a live input.
- STALE: the three aws-shape_*.tar.gz snapshots (Jun 8) are GENERATED output of comp_aws_cli.py's own snapshot-write path (line 2888) with no found read-back consumer; one is explicitly named '-cert13of13-baseline', suggesting deliberate retention as a milestone record rather than routine snapshot litter.
- note: eventing-hand-audit-fixture-v0.1.yaml is the one item here worth a follow-up question to its owner (0.7.0_AE_CloudOps lineage): either comp_aws_cli.py's eventing cert leg was never built (coverage gap, not a stale-file problem) or the fixture is genuinely orphaned.

### org/modules/graph/comp_debt/
- purpose: In-progress NFRA_COMPDEBT_PRD build: grounding_lib.py (shared dual-evidence dead-confirm lifted from dup_scan) + dormant_guard.py (the keep-dormant-vs-dead KEYSTONE discriminator) + signals/{duplicates,graph,usage}.py (thin adapters onto comp-dups/comp-blast/telemetry) -- Milestones 1-3 of a 5-step PRD; fuse.py (Milestone 5, the final per-resource verdict + wiring) has not been built yet.
- last_touch: 984d0be0c7 2026-07-19 0.7.0_AE_CloudOps~B (grounding_lib.py, most recent)
- consumers: Internal package cohesion only right now (signals/*.py import grounding_lib and dormant_guard.py); keep-dormant.yaml sibling registry exists at org/modules/graph/keep-dormant.yaml confirming Milestone 2 is genuinely landed. No .tools/comp-debt wrapper exists yet -- distinct from the SEPARATELY-NAMED infra/aws/globgrph/comp_debt.py (the standing-scan orchestrator, a different file that only reuses this package's SIBLING debtscan/ engines, not this package itself).
- STALE: Not yet externally wired: fuse.py (PRD step 5, 'per-resource 3-way verdict + --firm scope') is absent, so this package has no live comp-* entrypoint today -- it is legitimate in-progress PRD code (docs/architecture/NFRA_COMPDEBT_PRD.md, CTO arch-gated 2026-07-02), not dead code, but a future auditor should re-check whether fuse.py landed and this classification should flip to a wrapped-and-consumed status.
- STALE: Naming collision risk (not a staleness defect per se): infra/aws/globgrph/comp_debt.py ('comp-debt' orchestrator, LEDGER_DIR=org/modules/graph/debtscan/comp_debt/) is easily confused with this org/modules/graph/comp_debt/ package -- two same-named-but-different things in the estate; worth a rename or a disambiguating comment if not already done.
- note: No live-consumed risk today (nothing invokes it externally yet); flag for re-check once fuse.py lands and a .tools wrapper appears.

### org/modules/graph/adapter-audit/
- purpose: GENERATED output directory for comp-adapter-audit (org/modules/graph/adapter_audit_cli.py): one field-threading manifest YAML per portal adapter function (getPlatinumAdvisorSummary, getPlatinumFirmDashboard, etc.), each regenerated fresh on every audit run.
- last_touch: 573aa429f0 2026-06-12 2.0.0_SA_COO (getPlatinumAdvisorSummary.yaml/getPlatinumAdvisorSummaryStaticInflection.yaml/getPlatinumAdvisorDrilldownSummary.yaml) -- committed content unchanged since; getPlatinumAdvisorSummaryStaticInflection.yaml mtime is Jul 13 but git diff is clean (filesystem-touch noise, not a real edit)
- consumers: org/modules/graph/adapter_audit_cli.py (the generator, writes here by default per its own --help text); .tools/portal-hooks/d1_adapter_threading_gate.py (the portal D1 pre-commit BLOCKING gate, invokes comp-adapter-audit fresh each run rather than reading a stale copy); also referenced from comp-coverage-map.yaml, comp-output-contracts.yaml, TOOL_MASTER.yaml, tests/test_adapter_audit.py.
- STALE: GENERATED / self-refreshing quadrant, not the dangerous one: the D1 gate re-invokes the audit CLI live at commit time rather than trusting these committed files as ground truth, so a stale committed YAML cannot silently pass a bad schema-drift state through the gate.
- STALE: getPlatinumAdvisorSummary.yaml reports 84/84 findings as WARN-severity SCHEMA-DRIFT ('In S3 actual envelope but NOT in typed interface... type is stale') -- this is the audit correctly flagging a DIFFERENT file (the portal TypeScript adapter type) as stale, not itself; out of scope for this batch but worth flagging upstream to whoever owns portal/src/api/endpoints/advisor-intelligence.ts.
- note: None specific to this directory; it behaves as designed (regenerate-on-gate).

### org/modules/graph/potion/
- purpose: NFRA_COMPROUTE Charter-1 vendored POTION semantic embedder: potion_embed.py (runtime loader, safetensors+tokenizer, no model2vec/pickle at route-time), potion_shadow_rank.py (offline residual-rank measurement harness), MANIFEST.json (SHA256-pinned vendored-file manifest), model/{model.safetensors,tokenizer.json} (the actual 7.4MB embedding table + 668KB tokenizer, vendored from minishlab/potion-base-2M).
- last_touch: 14d6812b53 2026-07-07 0.8.0_AE_CloudComp~E
- consumers: potion_embed.PotionEmbedder <- org/modules/graph/comp_potion_relevance.py <- org/modules/graph/comp_route_eval.py; confirmed genuinely LIVE-wired into the real router org/modules/graph/comp_route.py (lines ~143/268-271: 'POTION semantic cosine' relevance_provider blend, with fail-safe fallback to lexical on load failure) -- i.e. this backs the live comp-which tool, not just an eval harness.
- STALE: None found -- SHA256-pinned manifest, fail-closed load, fail-safe caller; this is a well-controlled vendored-artifact pattern with no hand-maintained count/date drift risk.
- note: None. model.safetensors (7.4MB) and tokenizer.json (668KB) are large binaries but are the deliberate deliverable of a CTO-gated design (NFRA_COMPROUTE_POTION_DESIGN.md), not build junk -- do not flag for deletion.

## Batch summaries

- **?**: Audited org/modules/graph/tests/ as a single subtree unit (85 test files, ~695 pytest functions, 3.4MB __pycache__). This is an unambiguously live, actively-growing test suite -- HEAD commit is same-day (2026-07-30, 0.7.0_AE_CloudOps), .owned-paths.yaml:733 explicitly names 'org/modules/graph/tests/**' as the NFRA_TOOLCHECK.P4 build-surface deliverable under an active do-er/verifier/arch-gate grant, and several files (test_e41/e42/e413/e5/e6r8) are the literal acceptance bar for today's NFRA_VELOCITY_ESTATE workstream dispatched by COO with CTO gate approval. Classified NECESSARY. The only staleness signal found in a bounded sample was benign: one docstring (test_e42_fail_kind_separation.py:22) quotes a past incident mentioning the now-deleted 'comp-opalbizsem' tool, but it is clearly historical/narrative (describing a dated causal investigation), not asserted as current -- exactly the labeled-historical case the task says is fine. A handful of newer docstrings carry hand-written point-in-time counts ('54 of 87 FAIL rows -- 62%') that are prose evidence-of-derivation, not runtime-derived and not used in assertions, so they carry low-grade future-staleness risk but no live defect today. Split out __pycache__/ (172 .pyc, 3.4MB, gitignored/untracked) as a zero-risk GENERATED deletion-candidate.
- **?**: org/modules/graph/tsgraph_spike/ is the NFRA_TSGRAPH.P0/P1/P2-1 ts-morph proving-ground (22 tracked files: 8 source scripts, 3 dated validation .md, package.json, .gitignore, plus tracked out/*.json snapshots) that established the compiler-grade portal semantic-graph substrate. It is functionally superseded -- the live comp-cluster tool now execs infra/aws/globgrph/comp_cluster_cli.py, not anything here -- but is a legitimate, self-labeled ('spike') historical record with no live consumer in a bounded sweep, so it classifies HISTORICAL-KEEP as a unit; the only defect is the dir carries no forward pointer to its production successor. Local (untracked/gitignored) disk litter inside the same tree is real cleanup opportunity: node_modules (15M, bun-regenerable), two scratch Kuzu DBs (20M+17M, explicitly self-labeled 'frozen vintage/SCRATCH' by their own loader scripts -- exactly the CLAUDE.md Rule-20 quoting-a-scratch-DB-as-the-estate hazard), and a 26KB misrouted-telemetry JSONL that is a known hook cwd-resolution bug leaving shadow copies wherever an agent works. All four are safe, low-risk deletions; last touch to the tracked content is 2026-06-26 (b47839cff7).
- **?**: Audited 37 org/modules/graph/ files (36 tracked files + all confirmed non-UNTRACKED). 30 are NECESSARY live comp-tool backends/engines/tests/registries with named consumers (mostly .tools/comp-* wrappers plus internal imports) and no staleness evidence -- the 2026-07-30 pipescript->comp-estate naming consolidation landed cleanly (opal_estate_infrastructure.py and estate_infrastructure_cli.py both present and correctly self-documenting their own rename history; old comp-semantic-estates/comp-opalbizsem wrappers confirmed absent). 4 promote_*.jsonl/.json files (2026-07-14 vintage, one coherent write-set) are HISTORICAL-KEEP: genuinely consumed by comp_promote_lifecycle.py/comp_promote_materializer.py but quiet since 07-14 -- plausibly a dormant-not-dead pipeline per the workspace's own staleness-reasoning discipline, not independently verified either way. resign_surface_baseline.py is HISTORICAL-KEEP: a textbook self-marked DEPRECATED file that still exists, but deliberately and safely so (hard ALLOW_DEPRECATED_RESIGN=1 gate, explicit historical-reference rationale). The one real finding: nerves_traffic.py (NFRA_NERVES L2, part of a CVO~Z-verified 'SOUND' 2026-07-14 commissioning) is TRASH-CANDIDATE -- its docstring claims every other NERVES layer is 'a function of' it, but nerves_accrete.py and nerves_lexical.py both bypass it entirely (verified via import grep), it has no .tools wrapper, and its own declared output sink (org/mcp/nerves-traffic.jsonl) has never been created on disk (0 hits in the rail log or run sink either) -- a genuine declarative/architecture drift between claimed and actual role, safe to delete pending a decision to actually wire it in. nerves-edges.json and nerves-risk-edges.json (both live-consumed by comp_pulse.py/comp-pulse) sit closest to the 'dangerous quadrant' (dated snapshot + live consumer) but are mitigated differently: the risk map self-heals on every comp-pulse read (subprocess nerves_lexical.py build), while the co-change edges only print a 'stale' flag and tell the operator to rerun nerves_accrete build manually -- both disclose their own vintage rather than silently asserting freshness, so neither is classified AT-RISK, but nerves-edges.json's lack of auto-heal is the closer of the two to that quadrant.
- **?**: Audited 5 subtrees under org/modules/graph/ (gold-nan, postmerge-cols, shadow-detect, types-index, vectorize-audit). All five are output/index directories for live comp-tools (comp-validate, comp-pipescript x2, comp-types, comp-perf), each with a confirmed .tools/ wrapper and engine file -- none is orphaned tooling. types-index/ is the one actively-refreshed, actively-consumed directory (touched today by CTO~C via comp-types) -> NECESSARY. gold-nan/, postmerge-cols/, and vectorize-audit/ are dormant point-in-time snapshots from a single 2026-06-11/06-15 run each, self-healing on next invocation and read by no downstream gate -> GENERATED with noted staleness (gold-nan's REPORT.md carries a frozen 'Total 79' count that double-counts a since-completed bare->INF_ script rename, and its INF_09 manifest's cited emit-site line numbers no longer match current source). shadow-detect/ gets the sharpest flag -> AT-RISK: one of its three per-function manifests (D_04.client_portal_summary.compute_hh_lifecycle.yaml) points at a script path that no longer exists on disk (renamed to INF_D_04.client_portal_summary.py) and a function-line range (339-420) that is now off by ~660 lines in a file that grew from small to 4378 lines -- exactly the dated-snapshot-with-dead-pointer shape the audit is hunting for, though its blast radius is confined to human/agent misdirection since no code gate consumes it.
- **?**: Audited org/modules/graph/coverage-report/ and org/modules/graph/compproof/. coverage-report/ (62 tracked files) is a frozen 2026-05-14 comp-coverage snapshot whose own headline number (8.4%/11.3% coverage) was proven wrong by commit 33146f0297 (2026-07-10, true figure 17.1%, itself a disclosed lower bound); the tool was subsequently made stdout-only by default specifically to stop this directory's churn, a gitignore-it recommendation was raised the same day and never actioned, and my consumer sweep found zero readers -- TRASH-CANDIDATE, safe to regenerate on demand or delete. compproof/ is the opposite case: a NECESSARY, actively-maintained clean-room blind-solver harness (edited as recently as 2026-07-29) whose corpus_loader.py/harness.py are reused un-forked by the live NFRA_TOOLHEALTH TH-A/TH-B mechanism (comp_tool_health.py + 8 test files consume it directly) -- but the directory also carries real debris worth cleaning: stray untracked org/mcp/ telemetry copied in by a misrouted solver spawn, a 192K __pycache__, an inconsistently-tracked set of solver_view_B-02..20.txt scratch files (only B-01 was committed), and an untracked 'canonical' append-only probe log (effective_probe_log.jsonl) whose accrual history is device-local only. The original B1 run's output files (report.json, JUDGE_REPORT*.md, judge_axes.json, etc., all 2026-07-01/02/07) are a harmless historical record of a completed one-time experiment, not a live-tracked metric."
- **?**: 42 files audited (org/modules/graph 'comp_*' compiler-tool engines). 34/42 are NECESSARY -- confirmed live via a .tools/comp-* shell wrapper and/or a real Python import chain from another live module (comp_log_auto.py and comp_output_contract.py are the highest-blast-radius: consumed by 60+ wrappers / 6+ modules respectively, both touched today 2026-07-30). 5/42 are HISTORICAL-KEEP: comp_learns_leg4_exercise.py, comp_rail_audit.py, comp_promote_lifecycle.py, comp_promote_materializer.py are one-time acceptance/closeout deliverables for programs (COMPLEARN leg-4, COMPRAIL TO-5, NFRA_PROMOTE P1/P2) that appear to have already converged/landed, with no live wrapper or importer found in the bounded sweep -- harmless as a record but comp_promote_lifecycle.py's docstring claims an enforcement relationship to comp_promote_materializer.py that a direct-import check could NOT confirm (likely file-interface coupling, unverified). 2/42 are AT-RISK: comp_route_affinity_ic.py and comp_route_outcome.py form a charter-2 pair, each self-declared/observably SHADOW-mode and built 2026-07-07, with ZERO consumer anywhere in org/.tools/docs except each other -- comp_route.py's live engine never imports comp_route_affinity_ic, so the intent-conditioned learning increment appears silently forgotten rather than deliberately shelved (worth a one-line CTO check). No RENAMED/DELETED-name staleness of the disqualifying kind was found: all 'pipescript' mentions are either (a) references to comp-pipescript, which CLAUDE.md confirms is still the live current io/deployed tool (not the renamed estate-traversal tool), (b) clearly-labeled historical narrative about a past incident, or (c) regex tolerance for parsing old corpus rows that still carry the bare pre-tombstone name. The one comp-opalbizsem mention (comp_output_contract.py:219) is a dated historical measurement note about a refuted causal hypothesis, inert prose not a runtime reference. No TRASH-CANDIDATE or GENERATED files in this batch; no untracked files (all 42 have git history).
- **?**: Audited 42 files under org/modules/graph/ (the comp_toolgraph/estate/drift/IAM/extract-pipeline family). All are git-tracked (no UNTRACKED devices-local risk in this batch). Overwhelming majority (35/42) are NECESSARY live infrastructure with confirmed .tools/comp-* wrappers or direct importers -- the extract_*.py family forms the trace_graph extraction pipeline consumed by comp-blast/comp-trace/comp-diff/comp-xref/comp-build; the extract_iam/iam_cli/grain_sentinel/contract_engine/drift_cli/comp_trigger/comp_toolgraph family each back a live comp-* wrapper. Three files (corpus.py, execution_graph.py, graph_compiler.py) are dead code intentionally ported from a separate 'corporeal' codebase in one April commit ('Port 14 deterministic compiler modules from corporeal-dev') and never wired into anything in this estate since -- TRASH-CANDIDATEs, ~130KB combined, domain-mismatched (federal-contractor/LangGraph content sitting inside Opal's dependency-graph directory). One GENERATED snapshot (comp_toolgraph_census.json) is stale: its committed 'pipescript' node still points at the now-renamed pipescript_cli.py path and its 63-tool universe count predates today's comp-semantic-estates/comp-opalbizsem deletion -- needs a `comp-toolgraph census --write` refresh. One file (gen-estate-resolver.py) has cosmetic docstring/comment staleness calling itself 'the pipescript CLI read-source' post-rename (should say comp-estate) -- functionally unaffected. The most consequential finding is critical-surfaces.yaml: a live, portal-enforced SEV1 blocking gate (comp-surface-check) whose frontend-carve paths were last human-verified 2026-06-11/12, ~7 weeks stale relative to today -- the dangerous quadrant (dated baseline + hard live consumer), flagged AT-RISK and worth a fresh carve-review. grain_baseline.json is live-consumed (found via a wider-than-bounded sweep at infra/aws/globgrph/derive_stitch.py) but is NOT wired into comp_aws_cli.py's own two grain_sentinel calls, so AC-GRAIN.2's magnitude-band check silently never fires via the `comp-aws` CLI itself -- only via the separate stitch-derive path. estate-coverage-resolver.json and graph-call-manifest.yaml (both touched today) are exemplary: fresh, and graph-call-manifest.yaml explicitly self-documents the pipescript->comp-estate naming lineage rather than silently going stale.
- **?**: Audited 42 paths in org/modules/graph/ (top1 batch). Findings by classification: NECESSARY=27 (live tools with .tools/comp-* wrappers or genuine in-process imports: adapter engines, comp-coverage/comp-constants/comp-dataflow/comp-debris/comp-depth/comp-cache/comp-aws/comp-assets/comp-clobber/comp-chainrun/cli.py, plus today's ontology/estate-model docs and the gate-enforced registries comp-coverage-map.yaml/comp-output-contracts.yaml/comp-tools.yaml/canon-patterns.yaml), GENERATED=2 (TOOL_MASTER.yaml, .manifest_check_advisory_tally.jsonl -- both correctly derived/gitignored, audit their sources instead), HISTORICAL-KEEP=9 (dated snapshots/rulings/reference cards with no live functional consumer -- D8-findings.md, DESIGN.md, comp-aws-agent-usage.yaml, comp-shell-dup-source-baseline.json, comp-tool-universe.md, comp-tools-segment-scope.md, comp_aggregate_honesty.py, comp_desc_sensitivity.py), TRASH-CANDIDATE=4 (all comp-constants-seed-{bd,cot,inf,multifirm}.yaml -- traced comp_constants_cli.py's DEFAULT_CONFIG_PATH and confirmed the live tool reads comp-constants.config.yaml at workspace root, never these seed files, despite the seed files' own headers claiming to be 'Consumed by comp-constants'; safe to delete, content already folded into the live config which self-regenerates via `comp-constants index`), AT-RISK=1 (adapter_audit_cli.py -- live-wrapped AND its own coverage denominator, 19-of-122 adapters, is a hand-frozen 2026-07-10 census with no re-census trigger). Notable systemic finding: comp-coverage-map.yaml (NECESSARY, gate-enforced) carries a hand-frozen comment 'union(tools,meta_tools)=49 as of 2026-07-01' now ~4 weeks stale against TOOL_MASTER.yaml's live count of 91 -- this is a comment (not gate logic) but is the literal instance-class CLAUDE.md's own text already calls out ('the prior frozen 62/49 drifted to 78->79 within one session'). Re the naming consolidation context: comp-tools.yaml, comp-coverage-map.yaml, comp-output-contracts.yaml, comp_api.py, and ESTATE_WORLD_MODEL_PROCESS.md (all touched 2026-07-30, today) are already fully reconciled with the comp-semantic-estates/opal_business_estates/pipescript_cli rename -- no drift found there. Two files reference bare 'pipescript' in clearly historical/past-tense framing (comp-tool-universe.md, comp-coverage-map.yaml's own commentary) which is accurate-as-history but readable as current by a skimming reader. cli.py's own docstring names nonexistent wrapper files (opal-trace/opal-blast instead of the real .tools/comp-trace/.tools/comp-blast) -- pure in-file doc drift, runtime unaffected.
- **?**: Batch = 6 assigned subtrees under org/modules/graph/ (debtscan, aws-shapes, org, comp_debt, adapter-audit, potion), reported as 8 items (3 of the 6 top-level dirs decompose into a live NECESSARY tree plus a nested accidental org/mcp/agent_telemetry/ TRASH-CANDIDATE subdirectory sharing one root-cause bug). Headline finding: a systemic cwd-relative-path defect writes agent_telemetry/<serial>.jsonl into THREE wrong nested locations inside org/modules/graph/ (debtscan/org/, aws-shapes/org/, and the bare org/modules/graph/org/ itself, 11 files / 8 distinct agent serials total) whenever a hook runs with cwd set under this tree instead of the workspace root; all three are gitignored (`**/org/`, .gitignore:415) so they're invisible on a fresh clone, and they directly starve org/modules/graph/comp_debt/signals/usage.py's telemetry-based staleness signal of real invocation evidence for the affected agents. All 6 top-level engines/tool-backing directories (debtscan's dup_scan.py/comp_similar.py/summary_corpus.py, aws-shapes's hand-audit cert fixtures, comp_debt's in-progress PRD milestone code, adapter-audit's D1-gate-consumed generated manifests, potion's live-wired semantic router model) verified NECESSARY with named, grep-confirmed consumers -- no dead code found among the actual tool engines. Two secondary findings worth owner follow-up: (1) debtscan/2026-07-09_LIVE_DO-NOT-DELETE_bd-allocation-processor.md is a prose-only production-protection notice not wired into suppression_v1.yaml or keep-dormant.yaml -- an automated reap sweep would not see it, and its own stated review-gate condition is now 3 weeks unverified; (2) aws-shapes/eventing-hand-audit-fixture-v0.1.yaml has zero found consumers unlike its s3/iam-ec2/stepfunctions sibling fixtures (all three of which ARE actively loaded by comp_aws_cli.py), suggesting either an unbuilt cert leg or a silently orphaned fixture. No stale references to today's pipescript/comp-semantic-estates rename found in any live (non-historical-dated) code in this batch.

## Cross-cutting root-cause finding

MISROUTED-TELEMETRY CLASS (found independently by 3 auditors): a PostToolUse telemetry hook
resolves its output path RELATIVE TO CWD, so agents working inside subdirectories leave stray
org/mcp/agent_telemetry shadow trees wherever they stand. Instances: org/modules/graph/org/,
debtscan/org/, aws-shapes/org/, tsgraph_spike/org/, compproof/org/. Deleting the droppings
without fixing the producer regrows them -- FIX THE HOOK (route to its owner) then sweep.