# NFRA_TOOLUNIFY Census — Lane §2.B: LOCAL + COMMITTED bridge span

**author:** `0.8.0_AE_CloudComp~B` · **date:** 2026-07-24 · **status:** CENSUS (read-only, scope-only)
**vintage:** all measurements below taken this session at workspace `HEAD=9da59d7ced` (full: `9da59d7cede73ecb0509e14ac347142dedc31047`), 2026-07-24T22:07:21Z, unless a different vintage is stated inline.
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` only, per plan §3.1 isolation.
**plan:** `docs/briefs/NFRA_TOOLUNIFY_ESTATE_CENSUS_PLAN_20260724.md` §2.B.

---

## 0 · Verdict summary (read this first)

| Must-close question | Verdict |
|---|---|
| What does `graph.json` capture? | **Working-tree only, self-healing to current-disk-state.** Never a committed/historical snapshot. |
| Is `source_sha` a git blob hash? | **No.** Plain `sha256(file bytes)`, no git object header. Byte-incompatible with `git hash-object`. |
| Does `source_sha` enable LOCAL↔COMMITTED drift detection? | **No, as built.** Its one consumer compares index-time-local vs read-time-local (both working-tree). Algorithmically *adaptable* to a LOCAL↔COMMITTED comparison (git-independent hash), but nothing does this today. |
| Does anything ingest git commit history into the graph? | **CTO~Z's negative CONFIRMED for the cross-layer graph** (`graph.json`/kuzu: zero git-derived fields, zero COMMIT node type, schema-verified across all 2,255/2,255 live nodes). **REFUTED as a whole-estate claim**: `nerves_traffic.py`+`nerves_accrete.py` (NFRA_NERVES L2/L3a, also CTO~Z-authored, 2026-07-14) DO walk git log and persist a derived artifact — but bounded, single-repo, and architecturally separate from `graph.json` (see §3). |
| What does portal contribute that the workspace scan misses? | Portal's **files** are already captured (162/2,255 nodes, plain directory walk — no repo-boundary awareness). Portal's **git identity** (its own 2,110-commit history, its DEV/PROD branch state, its live HEAD) is captured **nowhere** — and the one place the parent repo *does* track portal as a distinct entity (the gitlink pointer) is currently measured **5 commits stale** against portal's actual checked-out HEAD (see §4). |

---

## 1 · What `graph.json` captures (LOCAL, not COMMITTED)

**Source:** `org/modules/graph/trace_graph.py` (the sole builder; `TraceGraph.save`/`.load`, `Node`/`Edge` dataclasses).

- **Mechanism:** `_compute_file_sha` (`trace_graph.py:73-83`) opens the file **directly off disk** (`open(path, 'rb')`) and hashes raw bytes. `_compute_dir_sha` (`:95-126`) walks a directory (`path.rglob("*")`) the same way, for Lambda-bundle-root nodes. Both are pure filesystem reads — **no git object access anywhere in this file.** The module's own docstring: *"Zero API calls. Pure static analysis."*
- **Extraction passes** (`build_graph`, `:402-446`) orchestrate 9 extractors (`extract_s3`, `extract_api`, `extract_eventbridge`, `extract_lambda_ec2`, `extract_lambda_routes`, `extract_pipeline`/assets, `extract_sfn`, `extract_event_invoke`) — a targeted grep for git-invocation patterns (`git log`/`rev-list`/`subprocess.*git`/`GitPython`/a `COMMIT` node-type literal) across `org/modules/graph/*.py` returns **zero hits in any of the 9 extractor files** (grounded: 26 files matched estate-wide; every extractor is absent from that list — positive-controlled below in §3).
- **Not a snapshot — a self-healing cache.** `cli.py:_get_graph()` (`:39-64`) reloads the cached `graph.json` only if `check_node_freshness` finds **zero** source-SHA drift against the current working tree; **any** drift triggers a full rebuild (`"serve the cache ONLY if it reflects the CURRENT source... A drifted cache -> rebuild"`). There is structurally no path by which `graph.json` can represent a *past* or *committed* state — it is forced to converge on **whatever is on disk right now**.
- **Empirically confirmed, full denominator (2,255/2,255 live nodes, not a sample):** the complete key-set observed across every node in the live cache is exactly `{node_type, function_name, source_sha, label, id, file_path, run_order, metadata}`. No `commit`, `commit_sha`, `author`, `commit_date`, or any git-derived field exists in the schema or the live data.
- **Live vintage:** `built_at=1784925049.4178` → **2026-07-24T20:30:49Z** (built ~1h37m before this citation); file mtime 2026-07-24T20:31:40-04:00 (20:31:40Z), consistent. 2,255 nodes / 2,947 edges — matches CTO~Z's §1 count exactly, confirming same vintage.
- **Concrete illustration of "LOCAL" (measured live, this session):** the workspace working tree currently carries **207 uncommitted changes** (`git status --porcelain=v1 | wc -l`, this vintage). `graph.json`, being working-tree-sourced, reflects whichever of those 207 files it indexes **as they sit on disk right now** — including any not yet committed. A hypothetical committed-state graph would differ from today's `graph.json` on every one of those paths it covers. This is not a hypothetical risk; it is the file's designed behavior.

**Node-type census (denominator: 2,255 nodes, this vintage):** `GOLD_SCRIPT` 1,365 · `LAMBDA` 333 · `S3_ARTIFACT` 321 · `ENDPOINT` 138 · `EVENTBRIDGE` 63 · `COMPONENT` 24 · `STATE_MACHINE` 1 · `SQS_QUEUE` 5 · `SNS_TOPIC` 1 · `S3_BUCKET` 4.

---

## 2 · `source_sha`: not a git blob hash, and what it actually enables

**Source:** `trace_graph.py:70-137` (`Node.source_sha` field + `_compute_file_sha`/`_compute_dir_sha`/`_compute_path_sha`).

- **What it is:** `hashlib.sha256(raw file bytes).hexdigest()[:12]` — a bare content hash, truncated to 12 hex chars. For a directory (Lambda bundle root), a deterministic aggregate over sorted `(relpath, per-file-sha)` pairs.
- **What a git blob hash is:** `sha1("blob " + str(len(content)) + "\0" + content)` (or SHA-256 in a `--object-format=sha256` repo, still with the `blob <size>\0` header). **`git hash-object <path>` prepends that header before hashing; `_compute_file_sha` does not.** The two hashes are computed differently and will not match for identical content, even setting aside the SHA-1-vs-SHA-256 algorithm question — **this repo confirms SHA-1**: `surface_check_cli.py:394-396` shells out to `git hash-object` and gets 40-hex-char (SHA-1) output, vs `source_sha`'s 12-hex-char (truncated SHA-256) output — visibly incompatible formats, not just different values.
- **What it is used for today:** the ONE consumer is `check_node_freshness` (`trace_graph.py:336-373`), which recomputes `_compute_path_sha` against the **current working-tree file** and compares it to the **indexed** `source_sha` — both ends are LOCAL, at two points in wall-clock time (index-time vs read-time). This answers *"has the graph cache gone stale since it was last built,"* not *"does the working tree differ from what's committed."*
- **Could it be adapted to LOCAL↔COMMITTED drift detection?** In principle, yes — the algorithm itself (`sha256` of raw bytes) is git-independent, so computing the identical function over `git show <ref>:<path>` output and comparing it to the node's `source_sha` would work. **Nothing in the estate does this today.** Per BOUNDARY (scope-only, design nothing), this is recorded as an open capability gap, not a proposal.

---

## 3 · The git-history-ingestion gap: confirmed narrow, refuted broad

**Positive-controlled sweep** (grep for `git log|git rev-list|rev-list|git show|subprocess.*git|GitPython|import git\b|COMMIT_NODE|"COMMIT"|node_type.*COMMIT` across `org/modules/graph/**/*.py`, this vintage): **26 files matched.** Categorized by what the match actually is (read at source, not by grep hit alone):

| Category | Files | What it does with git |
|---|---|---|
| **Graph-build path (trace_graph.py + all 9 extractors)** | 0 of 26 | **Zero matches.** Confirms §1. |
| **comp-gitdrill** (the drill tool named in my mission) | `comp_gitdrill.py` | Query-time only: resolves a node/file, shells `git log`/`show`/`rev-parse`/`diff` **on demand**, returns text/JSON to the caller. **Never writes back into `graph.json`** — no persistence, no node mutation. It *reads* `.comp-graph/graph.json` (via `cli._get_graph()`) only to resolve a node-id → `file_path`, i.e. it consumes the graph to find files, then queries git separately. This is exactly "queried ad-hoc only," as CTO~Z's plan characterized it. |
| **Simple file-enumeration (`git ls-files`)** | `comp_coverage_check.py`, `nerves_resolve.py`, `debtscan/dup_scan.py` | Lists tracked filenames only — no commit/history data at all. |
| **Single-commit stamping** | `comp_passcraft.py` (`git rev-parse --short HEAD`), `comp_pulse.py` (`git diff --cached --name-only`) | Labels current state with the current commit / staged-diff list. Not history ingestion. |
| **On-demand ad-hoc query (CLI flag, not baked into any persisted graph)** | `pipeline_cli.py` (`--recent-failures`, `git log -S <pickaxe>`), `state_scan.py` (comp-state's BM25 drift linter — walks `git log` for last-commit-ts per path, live at query time) | Both walk git history **at call time**, in-process, and return an answer — neither persists a git-derived artifact that other tools then read as "the graph." |
| **`surface_check_cli.py`** | git diff/rev-parse/hash-object | Portal-surface pre-commit diffing logic; unrelated to the cross-layer graph. |
| **Test fixtures** | 2 files | Irrelevant (spin up throwaway git repos for unit tests). |
| **The one real exception — `nerves_traffic.py` + `nerves_accrete.py`** | see below | **DOES persist a git-derived artifact.** |

### The nerves exception (a real refutation of the broad claim, precisely bounded)

`nerves_traffic.py` (NFRA_NERVES L2, author `1.0.0_SA_CTO~Z`, 2026-07-14 — the same author as this census's negative) walks `git log --since=<N> days ago --name-only` (`nerves_traffic.py:98-119`) to extract `{commit, actor, date, files[]}` events. `nerves_accrete.py` consumes that stream and computes **decayed CO_CHANGE edges between files** (half-life 21 days), persisted at `org/modules/graph/nerves-edges.json` (this vintage: 3,796 lines / 270 edges at `min_support=3`, derived from **6,688 commits scanned over a 35-day window**, 5,281 distinct files, 28 sweep-commits excluded).

**This genuinely ingests git commit history into a persisted, machine-readable artifact — the strong form of "nothing ingests commits" is false.** But it is precisely bounded, and the bounds matter:

1. **Windowed and decaying**, not full-history: `--since=35 days ago`, half-life 21 days. The repo's actual history runs to 2025-11-18 (**19,882 HEAD commits**, §5) — the artifact covers roughly the most recent **~4%** of that span at any moment (35d / ~248d elapsed, this vintage) and is explicitly designed to keep forgetting the rest ("Regenerate: nerves_accrete build").
2. **File-level co-change only** — no per-commit metadata (author/date/subject) survives into the persisted edges; no `COMMIT` node type; entity keys are `"file:<path>"`, a scheme **disjoint from** `trace_graph.py`'s node-id space (`gold:...`, `lambda:...`, etc. — confirmed no cross-referencing constant or shared ID prefix between the two files).
3. **Architecturally separate from `graph.json`**: `nerves_resolve.py:72-74` *reads* `.comp-graph/graph.json` (`TraceGraph.load`) as one of several ref-resolution sources — but that is nerves **consuming** the trace graph, not the trace graph **absorbing** nerves. Nothing in `trace_graph.py`/`cli.py` reads `nerves-edges.json`. The two artifacts sit side by side, never merged.
4. **Workspace-repo-only.** Both `nerves_traffic.py:52` and `nerves_accrete.py:50` resolve `_WS` to the workspace root and invoke every git call as `git -C {_WS} ...` — **never** `-C portal`. Portal's commit history is invisible to this pipeline too (see §4). The one `"portal/package.json"` string in `nerves_accrete.py:213` is a synthetic test-fixture pair for a discrimination unit test, not a real observed co-change edge — workspace's own `git log --name-only` cannot show individual portal-internal paths at all, because portal is a gitlink (§4): workspace git only ever sees the literal path `portal` change, opaquely, when someone bumps the pointer.

**Net verdict:** CTO~Z's negative is **correct as stated about "the graph"** (the cross-layer `graph.json`/kuzu artifact this plan is unifying) and **not correct if read as "nothing in the estate ever ingests git history"** — a real, CTO~Z-authored precedent exists, 10 days old, un-cross-referenced by the plan. Flagging this as the "confirm or refute, positive-controlled" deliverable requires: **CONFIRMED (narrow) + REFUTED (broad), both grounded above.**

---

## 4 · What portal contributes that the workspace scan misses

**Portal is tracked as a gitlink, not a registered submodule — and its pointer is currently stale.**

- `git ls-tree HEAD -- portal` → `160000 commit 343e7b2afd4b71f6bf5391250d2eab46ff587586	portal` (mode `160000` = gitlink/commit-pointer, standard git submodule mechanics).
- **`.gitmodules` does not list `portal`** — it registers exactly one submodule, `tools/analytics_dashboard`. Neither has a `.git/modules/<name>` entry (this workspace does not use the `git submodule add`-managed gitdir layout for either nested repo — both are plain nested clones that git auto-detects as gitlinks). Portal is *less* formally registered than the one nominally-declared submodule: `.gitmodules`-driven tooling (`git submodule status`, etc.) would enumerate `tools/analytics_dashboard` and never even see `portal` exists.
- **Portal is a fully independent repo** (own `.git/` directory, own remote `https://github.com/Opal-Capital/portal.git`, own branches, currently checked out on `DEV`) — confirmed via `git -C portal branch --show-current` / `remote -v`.
- **Live drift, measured this session:** workspace's committed pointer for portal is `343e7b2a` (a real portal commit, 2026-07-23T17:37:58-04:00, subject `"fix(P1, suspect-b CONFIRMED): the 147 tooltip value-anchor..."`). Portal's **actual current HEAD** is `d1ba89b93` — **5 commits ahead** of the pinned pointer (`git -C portal rev-list --count 343e7b2a..HEAD` = 5). `git status --porcelain -- portal` confirms the parent sees this as a dirty gitlink (` M portal`). **Contrast control:** `tools/analytics_dashboard`'s gitlink shows clean (no drift) at this same vintage — so this is not a structural inevitability of gitlinks in this repo, it is portal's *measured current state*, consistent with portal being under continuous active development while analytics_dashboard is not.
- **This is the LOCAL↔COMMITTED bridge gap, concretely instantiated at the repo-pointer grain**, not just the file grain: neither `graph.json` nor any comp-tool surfaces this 5-commit gap. You can only see it by directly running `git -C portal rev-parse HEAD` against the parent's recorded gitlink SHA — exactly the kind of manual, ad-hoc reconciliation the census's bridge model exists to replace.

**What the workspace scan DOES capture from portal:** files. `162 / 2,255` live `graph.json` nodes have `file_path` starting `portal/` — `trace_graph.py`'s extractors walk the filesystem with no regard for the gitlink boundary (a plain `Path.rglob`/`os.walk` does not know or care that `portal/` is a separate repo). Several extractors explicitly target portal by path convention, not by accident — e.g. `extract_api.py:2-5,68-73`: *"extract FETCHES edges from portal components... Scans `portal/src/api/endpoints/*.ts`..."*, `portal_dir = workspace_root / "portal"`. Nine extractor files reference `portal` by name (`extract_routes.py`, `extract_ts_source.py`, `extract_api.py`, `extract_iam.py`, `extract_pipeline.py`, `extract_transforms.py`, `extract_s3.py`, `extract_lambda_routes.py`, `extract_eventbridge.py`).

**What the workspace scan does NOT capture from portal (and nothing else in the estate does either):**
- Portal's own commit history (2,110 HEAD commits, §5) — invisible to every git-history mechanism characterized in §3, all of which are workspace-`_WS`-scoped.
- Portal's branch identity (`DEV` vs `PROD`) — `graph.json` nodes carry no branch field; a portal file's node is identical whether portal happens to be checked out on `DEV` or `PROD` at index time.
- The gitlink-pointer-vs-live-HEAD drift itself (§4 above) — surfaced by neither `graph.json` nor any comp-tool swept in §3.

---

## 5 · Git-history magnitude, both repos (denominators + vintage stated; this session)

| Repo | Current branch | HEAD commit count | All-refs commit count | First commit | Last commit (this vintage) | Local branches | Notable remote branches |
|---|---|---|---|---|---|---|---|
| **ajb_workspace** (this repo) | `CLOUD` | **19,882** | **23,957** (Δ 4,075 reachable only off non-`CLOUD` refs) | 2025-11-18T10:45:33-05:00 | 2026-07-24T17:58:59-04:00 | `CLOUD`, `CLOUD_test`, `COMP`, `PROD`, `backup-pre-strip-20260714`, `comp-learns/_stub`, 3× `rescue/*`, `scratch-r4-mutant-v2`, `scty-mcpguard-deploy-build`, `smart-lint-backup-20260223_160750`, 2× `worktree-agent-*` (15 total) | `origin/CLOUD`, `origin/COMP`, `origin/PROD`, `origin/main` (= `origin/HEAD`) |
| **portal** (`portal/`, separate repo — §4) | `DEV` | **2,110** | **2,178** (Δ 68) | 2025-11-12T16:10:35-05:00 | 2026-07-24T11:40:41-04:00 | `DEV`, `PROD`, `hotfix/global-monthly-axis-key` (3 total) | `origin/DEV`, `origin/PROD`, `origin/main` (= `origin/HEAD`), `origin/backup-attribution-dense-view`, `origin/demo/portal-optimized`, `origin/feature/advisor-intelligence`, `origin/feature/bullish-bearish-layout`, `origin/hotfix/global-monthly-axis-key`, `origin/testing` |
| **TOTAL (both repos, primary working branches: `CLOUD`+`DEV`)** | — | **21,992** | **26,135** (all-refs, both repos) | 2025-11-12 (portal is 6 days older) | 2026-07-24 (both actively committed today) | 18 combined | — |

**Branch-grain note (per plan's ask):** workspace's own `CLAUDE.md` names `CLOUD` as *the* working branch (parent repo) and `DEV`/`PROD` for portal — matching the two repos' actual primary branches measured here. `main` exists as the default/mirror ref in both remotes but is not where either agent fabric commits day-to-day (0 of the last several commits I sampled in either repo's `log -1` are against `main`). The ~4,075-commit (workspace) and 68-commit (portal) all-refs deltas sit on rescue/scratch/worktree-agent/backup/feature/demo branches — a full-history surfacer needs an explicit ref-scope decision (CLOUD+DEV only, vs all-refs) since these populations differ by an order of magnitude in the workspace case's *proportion* (~20%) even though CLOUD is still the large majority.

---

## 6 · Sized (not designed): what surfacing full git history would take

Per BOUNDARY, this is magnitude and decision-points only — no architecture, no schema, no tool proposed.

**Scale established (§5):** ~22K commits across 2 repos' primary branches today (~26K if all refs count), growing at workspace's measured rate of hundreds of commits/day (19,882 commits since 2025-11-18 ≈ 250 days ≈ ~80 commits/day average, almost certainly front-loaded toward the present given the multi-agent fabric's recent scale-up — the 2026-07-24 session alone already shows dozens of commits in `git log` before this measurement).

**What already exists to build from (a precedent, not a solution — §3):** `nerves_traffic.py`'s `_git_events()` proves the raw git-walk mechanics are cheap and already solved for a bounded slice (6,688 commits/35 days ran fast enough to be a routine `nerves_accrete build` step). A full-history equivalent is the same mechanism at ~3x the per-repo commit count (workspace) with the windowing/decay removed — the walk itself is not the hard part.

**What is NOT solved by any existing piece, and would need an explicit decision (open, not answered here):**
1. **Two independent repos, not one.** Every existing git-touching tool in §3 is single-repo (`_WS`-scoped or portal-blind). A unified surfacer needs to run the walk twice, with two distinct remote identities, and decide how a portal commit's node ID relates to a workspace commit's node ID in one shared space (today: no shared ID scheme exists between the two — `graph.json` doesn't have a commit-ID space at all, and nerves' `file:<path>` keys collide across repos with no repo qualifier, e.g. `file:README.md` could mean either repo's README).
2. **The gitlink boundary is a real seam, not a formality** — §4 showed the parent repo's own git log sees `portal` only as an opaque 40-hex pointer touch, never portal's internal file changes. A surfacer walking workspace's `git log --name-only` and a surfacer walking portal's own `git log --name-only` are NOT the same operation stitched together automatically; the stitch (recognizing "workspace commit X bumped portal's pointer from A to B" and connecting that to portal's own commit-B metadata) is unbuilt and would need explicit design.
3. **Ref-scope policy** (§5): CLOUD+DEV only (~22K) vs all-refs both repos (~26K) is a ~19% size difference in the workspace repo alone, concentrated in rescue/scratch/worktree-agent branches whose canonical-history status is itself a judgment call (rescue branches are recovery artifacts; worktree-agent branches are ephemeral automation branches per the `EnterWorktree`-style tooling) — not this census's call to make.
4. **Retention policy.** Nerves' precedent (35-day window, 21-day half-life) is a real working default for a co-change signal, but the plan's stated goal ("bridge from the user's local device... up to the federated cloud surface") reads as wanting durable historical grounding (e.g., for `comp-gitdrill`-style "what did this look like at vintage V" queries across the FULL life of a file), which is a different retention shape than a decaying recency signal — full-history retention at ~22-26K commits is not itself a scale problem (git already stores it; even a naive per-commit metadata table at that count is small), but it is a different design goal than what nerves solved, and conflating the two would under-serve one of them.
5. **Incremental wiring is a separate decision from historical backfill.** A one-time backfill over ~22-26K commits is a bounded, cheap-per-commit walk (same shape as nerves' existing walk, just unwindowed). Keeping it current afterward needs a trigger — hook, poll, or on-demand-query-only (comp-gitdrill's existing model) — each with different freshness/cost tradeoffs; this census does not choose between them.
6. **`source_sha` adaptation (§2)** — if LOCAL↔COMMITTED *file-content* drift detection (as opposed to commit-history surfacing) is also in scope for "the bridge," that is a smaller, separable unit of work (one new function computing the same hash over `git show <ref>:<path>`), distinct from the commit-history-ingestion question above; conflating the two in one design would mix a cheap addition with a genuinely large one.

**What this census does NOT attempt to answer:** which of (1)-(6) the eventual PRD should choose, what schema a COMMIT node/edge would use, or whether nerves should be extended vs a new mechanism built. That is explicitly CTO~Z's consolidation step (plan §4), not this lane's.

---

## 7 · Could-not-verify / residual unknowns

- **Why `graph.json` was freshly rebuilt ~1h37m before this citation (20:30:49Z) is not established** — plausibly another lane's or CVO~Z's `_get_graph()` call during concurrent census work (the mechanism in §1 auto-rebuilds on any drift), but I did not trace which specific call triggered it. Not load-bearing for this lane's MUST-CLOSE items.
- **Whether any non-`org/modules/graph` location in the estate ingests git history** (e.g., a Lambda, an Iceberg producer) is outside this lane's BOUNDARY (Iceberg/cloud truth is base/`~A`'s scope) and is not swept here — my grep and source-reads are scoped to `org/modules/graph/`, which is where the plan's own §1 places both `graph.json`'s builder and `comp_gitdrill.py`.
- **The exact commit-rate trend** (accelerating/steady) is stated as a rough average (~80/day over 250 days) from two endpoint dates only — not a fitted trend. Adequate for scale-sizing (§6), not precise enough for capacity planning.

---

## Acceptance (per plan §2.B)

- [x] Grounded statement of what LOCAL (`graph.json`) and COMMITTED (git, both repos) planes contain today — §1, §4, §5.
- [x] The drift mechanism `source_sha` does/doesn't enable, stated precisely — §2.
- [x] Git-history-ingestion gap confirmed or refuted, positive-controlled — §3 (both: narrow-confirmed, broad-refuted, with the refuting artifact named and bounded).
- [x] A sized (not designed) gap for surfacing git — §6.
- [x] Every count carries its denominator + vintage (stated inline throughout; live cache = 2,255/2,255 nodes exhaustively schema-checked, not sampled; git counts are exact `rev-list --count` outputs at the stated commit).
- [x] Could-not-verify items stated as findings, not papered over — §7.
