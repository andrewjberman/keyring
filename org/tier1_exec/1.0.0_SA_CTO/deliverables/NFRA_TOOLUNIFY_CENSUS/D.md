# NFRA_TOOLUNIFY Census — Lane §2.D: Tool → Source MAP

**author:** `0.8.0_AE_CloudComp~D` · 2026-07-24 · **status:** DELIVERED, awaiting CVO~Z verification
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY (off-main-fabric census group; plan §3.1)
**scope:** `docs/briefs/NFRA_TOOLUNIFY_ESTATE_CENSUS_PLAN_20260724.md` §2.D
**sidecar:** `D.sidecar.json` (this directory) — the machine-readable, full-detail register (line numbers,
code snippets, per-hit notes). This document is the narrative + a compact summary table; the sidecar is
authoritative for anything not spelled out here.
**mission grounding vintage:** measurements below taken this session against the live working tree
(`@721b68f7bb` base, no commits landed by this lane during the census — read-only per plan §3.2).

---

## 1 · Mission recap

For every `comp-*` tool (+ `pipescript`), establish which **surface + vintage** it reads, typed per the
brief's vocabulary (`LIVE-AWS` / `KUZU-CANONICAL` / `SOURCE-SCAN` / `ICEBERG-DIRECT` / `FROZEN-SNAPSHOT` /
`DERIVED-CACHE` / `CONFIG`), plus `writes[]`, `binding` (`ANSWER-BEARING` vs `GUARD`/`ROUTING`/`LABEL`/
`CONFIG`), `evaluation` (`RUNTIME` vs `DERIVED`), and `failure_mode` (`LOUD` / `FAIL-OPEN` / `SILENT-EMPTY`).
Method mandate: **import-closure + AST/call-site, never string presence** — the predecessor audit was
wrong 25% of the time because it could not tell a producer from a consumer, or a routing guard from a
data source. Acceptance gate: reproduce 3 known false positives as negatives (`comp-manifest-check`,
`comp-graph`, `comp-stitch-refresh`) and find the one known false negative (`nerves_resolve.py:73`) —
**before** trusting the method on the full sweep.

---

## 2 · Denominator (re-derived at source, not quoted)

```
find .tools -maxdepth 1 -iname "comp-*" ! -iname "*.pyc"   ->  91 files, any extension
+ .tools/pipescript (non-comp-prefixed sibling, named as its own `tool:` in graph-call-manifest.yaml)
= 92 raw entries, ALL ROWED (this census's denominator)
```

**Reconciliation to the two other numbers already in circulation** (comp-manifest-check's own
registration-invariant reported `84`; the predecessor brief cited `~85`) — both are the SAME 91 minus the
SAME 7, arrived at from different starting points:

| Path | Count | Why |
|---|---|---|
| Raw `.tools/comp-*` files, any extension | **91** | ground truth file count |
| minus 5 `.py` **backing implementations** whose extensionless wrapper is *also* in the 91 | −5 | `comp-deadgrant`/`.py`, `comp-denytest`/`.py`, `comp-firmsep-sweep`/`.py`, `comp-tagauthz`/`.py`, `comp-whoread`/`.py` — invoking the wrapper *runs* the `.py`; same tool, not two |
| minus 2 genuinely unrepresented **test harnesses** | −2 | `comp-which-routing-test.py`, `comp-v5-composite-test.sh` — no wrapper counterpart, not estate tools |
| = comp-manifest-check's own universe (globs `comp-*` only, post-dedup) | **84** | matches the live gate's own printed count |
| + `pipescript` (non-`comp-`-prefixed sibling) | +1 | |
| = predecessor brief's figure | **85** | |

**This census rows all 92 raw entries** (satisfies plan §2.D's "row all 91" instruction plus `pipescript`),
including the 5 backing-impl duplicates (each cross-referenced to its wrapper — same closure, not
re-derived) and the 2 test harnesses (rowed honestly as `role_flags: TEST`, not silently dropped). **Zero
tools excluded from the sweep; every exclusion above is a *labeling* decision for the 84/85 figures, not a
missing row.**

---

## 3 · Method

**Three-stage pipeline**, each stage a standalone script under `.comp-graph/tmp/` (gitignored scratch,
not a registered comp-tool — this is a one-time census instrument, not a fabric addition):

1. **`census_classifier.py`** — entry resolution (4 distinct dispatch idioms found and handled, see §3.1)
   → full **transitive** import closure via `ast` (not depth-1: walks function bodies too, catching
   deferred/lazy imports) → call-site classification (an `ast.Call` node whose `func` resolves through
   real import bindings — **never** a string match against file text, which is exactly the class of error
   that produced the 3 known FPs).
2. **`census_annotate.py`** — second pass deriving `evaluation`/`failure_mode`/`binding` **candidates**
   from the grounded `reads[]`/`writes[]` via explicit, general rules (never a per-tool special case —
   CVO~Z's held-back verification specifically tests generalization past the 4 published cases).
3. **`census_finalize.py`** — merges both passes, applies documented manual overrides for the tools I
   source-read directly (the 4 gate cases + spot-checks), and stamps a **confidence level per row**
   (`HIGH` = full source read, `MEDIUM` = AST-grounded reads/writes + rule-derived judgment fields,
   `LOW` = a named-reason convention default). **Zero `UNKNOWN` in any of `reads[]`/`evaluation`/
   `failure_mode` — every field that isn't source-verified carries an explicit reason and confidence
   label instead of a bare unknown or a silent guess.**

### 3.1 · Four dispatch idioms found (the estate's own diversity, not documented anywhere as a set)

1. **Bash wrapper → `python "$WORKSPACE/path/to/mod.py" "$@"`** (majority pattern).
2. **Python file with a `#!/usr/bin/env python3` shebang IS the entry** (`comp-which`, `comp-freshness`,
   `comp-secrets`, `comp-tagauthz.py`, ...).
3. **"Thin PATH wrapper" + `runpy.run_path(_ENGINE, run_name="__main__")`** — a wrapper with almost no
   content of its own, dispatching DYNAMICALLY (not a static `import`) to the real engine
   (`comp-clobber`→`clobber_scan.py`, `comp-dups`→`debtscan/dup_scan.py`, `comp-honesty`→`comp_honesty.py`,
   `comp-state`→`state_scan.py`, `comp-coverage-check`→`comp_coverage_check.py`). **A depth-1 or even a
   naive full-file AST-import scanner sees a near-empty wrapper and calls it done — the entire real tool
   is one dynamic call away and invisible to both.** Found because these 5 tools came back with zero
   detected signal on the first classifier pass, which was itself the tell.
4. **Shim-of-a-shim via an extensionless intermediate** — `comp-genesis` → `infra/system/sdk/genesis`
   (no `.py` extension at all) → `genesis_cli.py` referenced by a **bare filename** (`"$here/genesis_cli.py"`,
   no `org/`/`infra/`/`.tools/`/`data/` prefix in the text), resolved relative to the intermediate shim's
   own directory. One tool, but a real fourth shape.

### 3.2 · Real bugs found in my own instrument while building it (disclosed, not smoothed over)

Per this project's own governing principle ("care is not a control" — an instrument's failures must be
found by exercising it against a known-present case, not by trusting the build): six concrete bugs were
found and fixed, each because a specific known-source case disagreed with the classifier's first answer.

| # | Bug | Found via | Fix |
|---|---|---|---|
| 1 | No data-flow: `_MANIFEST = _THIS_DIR / "graph-call-manifest.yaml"` then `_MANIFEST.open()` — bare-Name args never resolved | `comp-freshness`/`comp-tagauthz` came back EMPTY despite plainly shelling to `aws` | whole-module `ConstCollector` resolving Name→literal, forward-pass, self-referential |
| 2 | No wrapper-function taint: `def sh(cmd): subprocess.run([exe, *cmd[1:]])` called as `sh(["aws",...])` — the literal lives at the CALL SITE, not the wrapper body | same as #1 | structural taint (does the body shell out / read a file AT ALL, regardless of whether its own args resolve) + call-site-specific re-resolution |
| 3 | Bash write-direction check inspected the LAST TOKEN OF THE WHOLE LINE, which was inside a trailing `\|\| { echo ERROR; exit 1; }` handler, not the `s3://` destination | **comp-stitch-refresh gate case itself** — its two `aws s3 cp` uploads read as consumer reads, not producer writes | isolate the command before `\|\|`/`&&`/`;`, THEN check the last non-flag token |
| 4 | Same check then failed AGAIN: the destination token is shell-quoted (`"s3://..."`), so `.startswith("s3://")` never matches a string starting with `"` | same regression check, still wrong after fix #3 | strip quote characters before the prefix check |
| 5 | `json.loads` (parses an in-memory STRING, never a file) was lumped into the same taint set as `json.load`/`open` (file operations) | **held-out self-check on `comp-secrets`**: `_shape(value)` calls `json.loads(raw)` on an already-fetched secret value, got false-tagged FILE-WRAPPER | removed `"loads"` from the file-taint name set (kept `"safe_load"`, flagged as a residual ambiguity) |
| 6 | Method-style calls (`stitch.exists()`, `kuzu.stat()`) take **zero positional args**, so the arg-only resolver always saw `""` and fell through to the generic dynamic-fallback even when the RECEIVER (`stitch`) resolved cleanly to a real literal | writing this document, checking why `FROZEN-SNAPSHOT`/`KUZU-CANONICAL` appeared for only 1 tool estate-wide (implausibly low) | resolve the method-call RECEIVER via the same const machinery, not just `node.args` |

Bug #3/#4 is the one worth dwelling on: it reproduced the **exact producer-vs-consumer defect class** the
whole census exists to catch, inside the tool built to detect that class, on the exact gate case testing
for it. It was caught only because the acceptance gate was run against **actual classifier output**, not
my own manual read of the source — the two disagreed, and the classifier was wrong. Fix #6 similarly
would have shipped a materially incomplete artifact-touch picture (`FROZEN-SNAPSHOT` at 1/92 tools instead
of the true 12/92) had I not checked why a number looked too clean.

---

## 4 · Acceptance gate — all 4 cases, confirmed against actual tool output (not my prose)

**Case 1 — `comp-manifest-check` (reproduce FP as negative): CONFIRMED.** `reads[] = {CONFIG, SOURCE-SCAN,
SOURCE-SCAN-DYNAMIC}` — **zero** `KUZU-CANONICAL`/graph-content hits. The predecessor's string-presence
method would see `kuzu.Connection`/`graph.json` as literal substrings inside `manifest_check_cli.py`'s own
source and tag it a content reader of both — but those substrings live **inside `re.compile(...)` pattern
literals** (`ADHOC_PATTERNS`, :184-228) that this tool uses to scan *other files'* text for anti-patterns,
never as code this tool itself executes. AST call-site resolution correctly sees `re.compile(...)` as the
call (with a string argument), not `kuzu.Connection(...)`/`open(graph.json)` as call targets.
`binding=GUARD` (every read decides a PASS/BLOCK verdict across 7 fail-closed invariant functions,
:438-1098); `failure_mode=LOUD` (7 separate `except Exception: print BLOCKED; return 1` sites — an
unevaluable gate blocks, never silently passes).

**Case 2 — `comp-graph` (reproduce FP as negative): CONFIRMED, with a sharper answer than "never touches
it."** Post-bug-#6-fix, `comp-graph` DOES show `KUZU-CANONICAL` (5 hits) and `FROZEN-SNAPSHOT` (4 hits) in
`reads[]` — but **every single one is `meta_only: true`**: `.exists()`/`.stat()`/a 512-byte `read_bytes()`
header peek (:74-239). It never opens `kuzu_db`/`stitch_graph.json`/`graph.json` for content, never issues
a Cypher query, never full-parses the trace graph. The register **shows the touch and its metadata-only
qualifier together** — closer to the truth than either "reads the graph" (the FP) or "doesn't touch it at
all" (an over-correction I'd have shipped without the receiver-resolution fix). `binding=LABEL` (reports
freshness labels about other artifacts, delegating the one real verdict it needs to the actual enforcer
via `cli.trace_freshness()` rather than re-modeling the predicate, :111-117).

**Case 3 — `comp-stitch-refresh` (reproduce FP as negative): CONFIRMED**, after fixing bugs #3/#4 in my
own tool (see §3.2 — this IS the finding, not just infrastructure). Final: `reads[] = {LIVE-AWS
(boto3 AWS-snapshot fetch), SOURCE-SCAN-DYNAMIC, DERIVED-CACHE}`, `writes[] = {LIVE-AWS}` — the two
`aws s3 cp` uploads of `stitch_graph.json`/`stitch_marker.json` to
`s3://opal-313476888478-globgrph/stitch/`. `role_flags=[PRODUCER]`. The predecessor's producer-vs-consumer
confusion is closed: this tool WRITES the artifact everything else in the estate reads.

**Case 4 — `nerves_resolve.py:73` (find the known FN): CONFIRMED.** `nerves_resolve.py` appears in the
**transitive closure** (30 modules deep) of `comp-blast`/`comp-trace`/`comp-diff`/`comp-xref` (all backed
by `org/modules/graph/cli.py`), reachable only via `cli.py:376-392`'s `_print_risk_by_ref()` — a
**function-local, exception-guarded, deferred import** (`from nerves_resolve import resolve as _resolve`
at :383) fired only on the NOT-FOUND path of a node lookup. A depth-1 or module-top-level-only import
scanner structurally cannot see this: it's neither a top-level import nor reachable without descending
into a function body 2+ calls deep. Ground truth on the read itself: `nerves_resolve.py:73-74`
(`_trace_graph()`) does `TraceGraph.load(cache) if cache.exists() else None` — existence-guarded but
**not** vintage/freshness-guarded (no content-SHA drift check), unlike `cli.py`'s own primary graph-read
path. **Same `graph.json`, two different vintage-discipline levels depending on which internal path
reaches it, inside the SAME tool** — itself a finding worth carrying into WS-3 (artifact census):
`comp-blast` et al. show `vintage_discipline` as effectively split between `GUARDED-REBUILD` (primary
path, SHA-drift-checked, per CVO~Z's 222928Z note that this path can even rebuild-on-read) and `SILENT`
(the `nerves_resolve.py`-mediated fallback path). `comp-pulse` (also grep-flagged for a `nerves_*`
mention) was checked and found NOT to import `nerves_resolve` — it shells out to `nerves_lexical.py` as a
**separate process** (`subprocess.run([sys.executable, ".../nerves_lexical.py", "build"])`, comp_pulse.py
:183) and reads that process's JSON *output artifacts* (`nerves-edges.json`, `nerves-risk-edges.json`),
which is a legitimately different relationship (execution dependency, not import/closure) — correctly
absent from `comp-pulse`'s closure.

**Held-out self-check (CVO~Z's request, run before delivery, not part of the published 4):**
`comp-secrets` and `comp-lambdamap` were read in full independently, predictions written down, then
compared against classifier output. `comp-secrets` matched closely (LIVE-AWS via `boto3.client` +
4 call-site-resolved wrapper propagations through `_client()`; SOURCE-SCAN via a `git grep` subprocess for
consumers) and surfaced bug #5 above. `comp-lambdamap` correctly showed a genuinely multi-valued
`reads[] = {SOURCE-SCAN-DYNAMIC, LIVE-AWS, SOURCE-SCAN, CONFIG}` — the multi-value discipline CVO~Z asked
me to verify is populated in the data, not merely permitted by the schema (see §5).

---

## 5 · Multi-valued discipline (CVO~Z's specific check)

**80/92 tools (87%) show 2+ distinct surface types in `reads[]`∪`writes[]`** (post-§10 rework; was 77/92 at
first delivery). Frequency across the full 92-tool population (a tool can contribute to multiple rows):

| Type | # tools touching it |
|---|---|
| `SOURCE-SCAN-DYNAMIC` (caller-supplied path, resolved at runtime — a legitimate distinct sub-case, not a failure to resolve) | 86 |
| `SOURCE-SCAN` (fixed repo/local target) | 66 |
| `CONFIG` | 66 |
| `LIVE-AWS` | 55 |
| `KUZU-CANONICAL` | 20 |
| `ICEBERG-DIRECT` | 20 |
| `DERIVED-CACHE` | 16 |
| `FROZEN-SNAPSHOT` | 12 |

No tool collapsed to a single label when its closure genuinely touched more than one surface — the exact
defect class (comp-pipescript's guard-vs-source distinction, hidden by a single-label predecessor scan)
this project names as the reason multi-valued fields exist at all.

---

## 6 · The register (92 rows, compact form — full detail incl. line numbers + snippets in `D.sidecar.json`)

**Confidence key:** `HIGH` = full source read by me, cited to file:line (4 gate cases + `comp-to`).
`MED` = `reads[]`/`writes[]`/`closure` are AST/call-site-grounded (same instrument, same confidence as the
HIGH rows); `binding`/`evaluation`/`failure_mode` are rule-derived from that grounded data via general,
documented rules (§3), not individually source-verified. `LOW` = `failure_mode` specifically defaulted to
this codebase's own repeatedly-observed LOUD convention because the quick text-scan found no direct
`sys.exit(1|2)` literal (almost always the `def main() -> int: ...; sys.exit(main())` indirect-return
idiom) — a **named reason**, not a silent guess, but not source-verified for that specific tool either.

`role_flags`: a bare name = confirmed from source/docstring; a trailing `?` = `-CANDIDATE`, i.e.
plausible from the mechanical signal (e.g. any `writes[]` → `PRODUCER?`) but not individually confirmed.
`GATE-BLOCKING` (no `?`) is reserved for tools I confirmed enforce at commit/PR time from their own
docstring or CLAUDE.md's own compiler-tools table.

| Tool | reads[] | writes[] | binding | evaluation | failure_mode | role_flags | conf |
|---|---|---|---|---|---|---|---|
| `comp-adapter-audit` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | CONFIG, SOURCE-SCAN | ANSWER-BEARING | RUNTIME | FAIL-OPEN | PRODUCER? | MED |
| `comp-assets` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-aws` | CONFIG, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | DERIVED | LOUD | PRODUCER? | MED |
| `comp-axes` | LIVE-AWS, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-blast` | CONFIG, DERIVED-CACHE, FROZEN-SNAPSHOT, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | ANSWER-BEARING | DERIVED | LOUD | PRODUCER? | MED |
| `comp-build` | CONFIG, DERIVED-CACHE, FROZEN-SNAPSHOT, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | ANSWER-BEARING | DERIVED | LOUD | PRODUCER? | MED |
| `comp-cache` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD (default) | PRODUCER? | LOW |
| `comp-canon-motif` | CONFIG, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN-DYNAMIC | ANSWER-BEARING | DERIVED | FAIL-OPEN | PRODUCER? | MED |
| `comp-chainrun` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-clobber` | LIVE-AWS | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-cluster` | CONFIG, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | DERIVED | FAIL-OPEN | PRODUCER? | MED |
| `comp-constants` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | ANSWER-BEARING | RUNTIME | FAIL-OPEN | PRODUCER? | MED |
| `comp-coverage` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | CONFIG, SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD (default) | PRODUCER? | LOW |
| `comp-coverage-check` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | (none) | GUARD | RUNTIME | LOUD | GATE-BLOCKING? | MED |
| `comp-dataflow` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD (default) | PRODUCER? | LOW |
| `comp-deadgrant` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-deadgrant.py` | LIVE-AWS, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-debris` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-denytest` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | GUARD | RUNTIME | LOUD | GATE-BLOCKING?,PRODUCER? | MED |
| `comp-denytest.py` | LIVE-AWS, SOURCE-SCAN-DYNAMIC | (none) | GUARD | RUNTIME | LOUD | GATE-BLOCKING? | MED |
| `comp-depth` | CONFIG, FROZEN-SNAPSHOT, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | LIVE-AWS, SOURCE-SCAN-DYNAMIC | ANSWER-BEARING | DERIVED | LOUD | PRODUCER? | MED |
| `comp-describe` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-diff` | CONFIG, DERIVED-CACHE, FROZEN-SNAPSHOT, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | ANSWER-BEARING | DERIVED | LOUD | PRODUCER? | MED |
| `comp-dispatch` | SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD (default) | ADVISORY | LOW |
| `comp-drift` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | LIVE-AWS, SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-dups` | LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-fedobs` | LIVE-AWS, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-firmsep-sweep` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD (default) | PRODUCER? | LOW |
| `comp-firmsep-sweep.py` | LIVE-AWS | (none) | ANSWER-BEARING | RUNTIME | LOUD (default) | ADVISORY | LOW |
| `comp-freshness` | CONFIG, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-genesis` | CONFIG, ICEBERG-DIRECT, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | DERIVED | LOUD | PRODUCER? | MED |
| `comp-gitdrill` | CONFIG, DERIVED-CACHE, FROZEN-SNAPSHOT, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | ANSWER-BEARING | DERIVED | LOUD | PRODUCER? | MED |
| `comp-glob` | SOURCE-SCAN | (none) | ANSWER-BEARING | RUNTIME | FAIL-OPEN | ADVISORY | MED |
| `comp-graph` | CONFIG, DERIVED-CACHE, FROZEN-SNAPSHOT, KUZU-CANONICAL, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | LABEL | DERIVED | LOUD | ADVISORY,PRODUCER?(clear-mode-only, local-cache-delete) | HIGH |
| `comp-grep` | SOURCE-SCAN | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-heat` | LIVE-AWS, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-honesty` | SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-iam` | CONFIG, DERIVED-CACHE, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | DERIVED-CACHE, SOURCE-SCAN | ANSWER-BEARING | DERIVED | FAIL-OPEN | PRODUCER? | MED |
| `comp-iam-usage` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-icedrill` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD (default) | PRODUCER? | LOW |
| `comp-imgread` | SOURCE-SCAN | (none) | ANSWER-BEARING | RUNTIME | FAIL-OPEN | ADVISORY | MED |
| `comp-incrparity` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-keys` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-kit-striplist-gate` | SOURCE-SCAN-DYNAMIC | (none) | GUARD | RUNTIME | LOUD | GATE-BLOCKING? | MED |
| `comp-kuzu` | CONFIG, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | DERIVED | FAIL-OPEN | PRODUCER? | MED |
| `comp-kuzu-full` | CONFIG, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | DERIVED | FAIL-OPEN | PRODUCER? | MED |
| `comp-kuzu-inc` | CONFIG, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | DERIVED | FAIL-OPEN | PRODUCER? | MED |
| `comp-lambdamap` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | FAIL-OPEN | PRODUCER? | MED |
| `comp-learns-score` | CONFIG, DERIVED-CACHE, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | DERIVED | LOUD | PRODUCER? | MED |
| `comp-learns-status` | LIVE-AWS, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD (default) | ADVISORY | LOW |
| `comp-manifest-check` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | GUARD | RUNTIME | LOUD | GATE-BLOCKING | HIGH |
| `comp-ontolint` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-parity` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD (default) | PRODUCER? | LOW |
| `comp-passcraft` | CONFIG, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | DERIVED | LOUD | ADVISORY | MED |
| `comp-perf` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | CONFIG, SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-pii` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-pipescript` | CONFIG, FROZEN-SNAPSHOT, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | ANSWER-BEARING | DERIVED | LOUD | PRODUCER? | MED |
| `comp-platinum` | CONFIG, FROZEN-SNAPSHOT, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | ANSWER-BEARING | DERIVED | LOUD | PRODUCER? | MED |
| `comp-pulse` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | FAIL-OPEN | PRODUCER? | MED |
| `comp-pydeps` | CONFIG, DERIVED-CACHE, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | DERIVED | FAIL-OPEN | PRODUCER? | MED |
| `comp-registry` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | FAIL-OPEN | PRODUCER? | MED |
| `comp-residue` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | FAIL-OPEN | PRODUCER? | MED |
| `comp-routable-check` | CONFIG, SOURCE-SCAN-DYNAMIC | (none) | GUARD | RUNTIME | LOUD | GATE-BLOCKING? | MED |
| `comp-routes` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-secrets` | LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-shell` | SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | FAIL-OPEN | ADVISORY | MED |
| `comp-similar` | CONFIG, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | FAIL-OPEN | PRODUCER? | MED |
| `comp-state` | LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-stitch-refresh` | DERIVED-CACHE, LIVE-AWS, SOURCE-SCAN-DYNAMIC | LIVE-AWS | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER | HIGH |
| `comp-surface-check` | CONFIG, DERIVED-CACHE, FROZEN-SNAPSHOT, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | GUARD | DERIVED | LOUD | GATE-BLOCKING?,PRODUCER? | MED |
| `comp-symbols` | SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD (default) | ADVISORY | LOW |
| `comp-system` | CONFIG, DERIVED-CACHE, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | DERIVED | LOUD | PRODUCER? | MED |
| `comp-tagauthz` | LIVE-AWS, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-tagauthz.py` | LIVE-AWS, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-to` | (none) | CONFIG | CONFIG | RUNTIME | FAIL-OPEN | CONFIG | HIGH |
| `comp-tool-health` | CONFIG, DERIVED-CACHE, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | DERIVED | LOUD | ADVISORY | MED |
| `comp-tool-health-gate` | SOURCE-SCAN-DYNAMIC | (none) | GUARD | RUNTIME | LOUD | GATE-BLOCKING? | MED |
| `comp-toolgraph` | CONFIG, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | FAIL-OPEN | ADVISORY | MED |
| `comp-tooltip` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-trace` | CONFIG, DERIVED-CACHE, FROZEN-SNAPSHOT, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | ANSWER-BEARING | DERIVED | LOUD | PRODUCER? | MED |
| `comp-transform` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-trigger` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | FAIL-OPEN | PRODUCER? | MED |
| `comp-types` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | CONFIG, SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-v5-composite-test.sh` | LIVE-AWS, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-validate` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | GUARD | RUNTIME | LOUD | GATE-BLOCKING?,PRODUCER? | MED |
| `comp-which` | CONFIG, DERIVED-CACHE, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | DERIVED | FAIL-OPEN | ADVISORY | MED |
| `comp-which-routing-test.py` | CONFIG, DERIVED-CACHE, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN-DYNAMIC | ANSWER-BEARING | DERIVED | LOUD | PRODUCER? | MED |
| `comp-whoread` | LIVE-AWS, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-whoread.py` | LIVE-AWS, SOURCE-SCAN-DYNAMIC | (none) | ANSWER-BEARING | RUNTIME | LOUD | ADVISORY | MED |
| `comp-xray` | CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | RUNTIME | LOUD | PRODUCER? | MED |
| `comp-xref` | CONFIG, DERIVED-CACHE, FROZEN-SNAPSHOT, ICEBERG-DIRECT, KUZU-CANONICAL, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | ANSWER-BEARING | DERIVED | LOUD | PRODUCER? | MED |
| `pipescript` | CONFIG, FROZEN-SNAPSHOT, ICEBERG-DIRECT, LIVE-AWS, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC | SOURCE-SCAN | ANSWER-BEARING | DERIVED | FAIL-OPEN | PRODUCER? | MED |

**Note on the two 5-tool "backing implementation" pairs and the 2 test harnesses** (accounted in the
denominator, §2, not re-listed as separate closures here where identical to their wrapper): `comp-deadgrant`
↔ `comp-deadgrant.py`, `comp-denytest` ↔ `comp-denytest.py`, `comp-firmsep-sweep` ↔ `comp-firmsep-sweep.py`,
`comp-tagauthz` ↔ `comp-tagauthz.py`, `comp-whoread` ↔ `comp-whoread.py` — each pair's extensionless wrapper
and `.py` backing file are rowed separately above (both ARE distinct entries in the 92, since invoking
either happens to resolve to compatible-but-independently-parsed entry points in a few cases); treat them
as one tool for registry purposes per §2's reconciliation. `comp-which-routing-test.py` and
`comp-v5-composite-test.sh` are rowed honestly as real files with real signal (both surprisingly touch
LIVE-AWS/CONFIG — test harnesses that exercise real machinery, not pure mocks) rather than dropped as
"not really tools."

---

## 7 · Findings surfaced along the way (not asked for, recorded because it's the discipline this project is about)

1. **`comp-residue` is registered nowhere.** `comp-manifest-check`'s own `registration_invariant`
   (run live during this census) reports it `BLOCKED`: "in NEITHER `tools_index` NOR
   `excluded_not_graph_use_cases` NOR any `entries:` row" and "absent from `comp-coverage-map.yaml`" — a
   tool `comp-which` can never route to. It IS on disk, tracked, and runnable (confirmed: reads
   `{CONFIG, SOURCE-SCAN, SOURCE-SCAN-DYNAMIC}`, writes `SOURCE-SCAN`). This is exactly the "a tool nobody
   can find is indistinguishable from a tool that was never built" class the gate's own message names.
   Routed to CTO~Z/CVO~Z as a WS-2/WS-7 input, not actioned (read-only scope, plan §3.2).
2. **The `graph.json` dual-discipline split** (§4 Case 4) — the same artifact is read through both a
   SHA-drift-checked "guarded-rebuild" path and an unguarded raw-load path inside the SAME closure
   (`comp-blast` et al.), depending on internal call order. Worth a named row in WS-3's artifact census
   rather than a single `vintage_discipline` value per artifact.
3. **Two "central hub" closures dominate the wide-multi-surface rows**: `org/modules/graph/cli.py`
   (backs `comp-blast`/`comp-trace`/`comp-diff`/`comp-xref`/`comp-build`, 30-module closure) and
   `org/modules/graph/comp_aws_cli.py` (backs `comp-aws`, 14-module closure) — both legitimately touch
   `LIVE-AWS`+`ICEBERG-DIRECT`+`KUZU-CANONICAL`+`SOURCE-SCAN`+`CONFIG` because they ARE the estate's
   central derive/query engines, not a classifier artifact (verified distinct `entry_modules` +
   `closure_size` per tool — no closure-merging bug). Flagged because a tool touching 6+ surface types is
   structurally the highest-blast-radius / hardest-to-reason-about class in the whole population, which is
   exactly the kind of thing WS-4's crosswalk work will want to know first.
4. **`comp-graph clear`** (a subcommand of an otherwise read-only status tool) `.unlink()`s local cache
   files (`graph.json`, `platinum.*.cache`) — a real, if narrow, write/mutate role живущий alongside its
   primary `ADVISORY` read-only `status` mode. Captured as a compound `role_flags` entry rather than
   picking one.
5. **11 tools' `failure_mode` could not be pinned by a quick text scan** (the `def main() -> int:
   ...; sys.exit(main())` indirect-return idiom routes the real exit code through a `return`, which a
   literal `sys.exit(1|2)` regex doesn't trace) — defaulted to this codebase's own well-evidenced LOUD
   convention, LOW confidence, named reason, listed individually in the sidecar. **Genuine
   could-not-fully-verify, not smoothed over**: `comp-cache`, `comp-coverage`, `comp-dataflow`,
   `comp-dispatch`, `comp-firmsep-sweep`, `comp-firmsep-sweep.py`, `comp-icedrill`, `comp-learns-status`,
   `comp-parity`, `comp-symbols`. (`comp-to` was fully source-read by hand instead — see its row.)

---

## 8 · What this lane did NOT do (plan §3.2 discipline)

No apply, deploy, re-point, regenerate, or schema change. No commits from this lane (owned-paths gates
`org/tier1_exec/1.0.0_SA_CTO/**` to CTO~Z's BASE_EXEC lane per their 221714Z policy note — this file is
written to disk for CTO~Z to commit). Did not re-characterize base/~A/~B/~C's surfaces — consumed their
type vocabulary as given by the plan, mapped tools onto it. Did not touch `comp-residue`'s registration gap
or the `graph.json` dual-discipline finding beyond recording them.

## 9 · Handoff

- **`1.0.0_SA_CTO~Z`**: consolidation input for the 5-lane estate map; `comp-residue`'s registration gap
  and the `graph.json` dual-discipline finding are candidate WS-2/WS-3/WS-7 items.
- **`3.0.0_SA_CVO~Z`**: register + sidecar re-delivered post-rework (§10) for re-verification.

---

## 10 · Rework addendum (CVO~Z held-back control, 20260725T000124Z-000358Z)

**VERDICT ON THE ORIGINAL DELIVERY: PASS at 85% (35/41 real pairs)** on CVO~Z's sealed held-back set
(committed `45ec1d7ee`, before this deliverable existed). CVO~Z disclosed first that their OWN control was
32% wrong on its own hits (19 of 25 apparent "misses" were the verifier's false positives, caught by
CVO~Z validating before reporting) — the same string-presence-adjacent disease this whole census exists to
catch, aimed at the instrument measuring it. **Corrected score: 41 real pairs, 35 surfaced, 85%, PASS.**

**The 6 real misses were ONE class**, all variable-bound paths: `rp = os.path.join(..., "nerves-risk-
edges.json")` then `open(rp)` later — the literal lives at an assignment, not the read call's own
arguments. `comp-gitdrill`/`comp-surface-check` missed `nerves-edges.json`/`nerves-risk-edges.json`
(`cli.py:338,422`); `comp-iam` missed `managed_policy_actions_cache.json`/`comp_aws_derive_iam.json`
(`extract_iam.py:116`, `comp_iam_live.py:78`) — the second pair prioritized by CVO~Z ahead of its numeric
weight: `comp-iam` is the tool CLAUDE.md Rule 22a already names as failing GREEN, and both misses are
caches sitting behind it.

**ROOT CAUSE (mine, superseding CVO~Z's own "variable-bound paths aren't resolved" description of the
symptom):** `ConstCollector` was a SINGLE FLAT DICT across an entire module — one forward pass, one
namespace. A short, commonly-reused local name (`rp`, or any generic 2-3 letter name) collides across
UNRELATED functions in a 700-line file; whichever assignment the flat pass visits last for that name wins,
for every call site using that name anywhere in the file.

**CVO~Z's follow-up (000358Z) found the sharper implication before I had measured it: a flat namespace
doesn't only DROP bindings — it can hand a DIFFERENT call site a CONFIDENTLY WRONG artifact**, indistinguishable
in the register from a correct resolution. The held-back control (a false-negative test) structurally
cannot see this false-positive-shaped risk. Requested bar: measure every existing resolved call site
before vs. after the fix, not just confirm the 6 reappear.

### Fix

`census_classifier.py` (now committed at
`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_TOOLUNIFY_CENSUS_TOOLS/`, `@2779752ac` — see §9):
1. **Function-scoped const resolution** (`ShallowVisitor`) — each function gets an independent
   local-variable namespace seeded from module-level consts, never a flat whole-file dict.
2. **Return-value resolution** (`_collect_return_consts`) for simple single-return path-builder helpers
   (`_managed_policy_cache_path(ws) -> ws/".comp-graph"/"managed_policy_actions_cache.json"` — the
   comp-iam miss: the caller sees only an opaque `p = helper(x); p.read_text()`).
3. Four new `DERIVED-CACHE` vocabulary entries (`nerves-edges.json`, `nerves-risk-edges.json`,
   `managed_policy_actions_cache.json`, `comp_aws_derive_iam.json`) — resolution and vocabulary were
   separate gaps; fixing one without the other still under-reports.

**A regression the measurement itself caught, not guessed:** the first version of return-value resolution
treated every single-return helper as a fixed constant, including `_abs(p): return os.path.join(
WORKSPACE_ROOT, p)` — where the parameter IS the meaningful, call-site-varying part. Caching one resolved
value for `_abs` and reusing it at every call site discarded each call's actual argument (`_abs(ROLLING_LOG)`
resolved to `WORKSPACE_ROOT`'s own path fragments instead of `ROLLING_LOG`'s literal). Fixed with a
guard: skip the fast path only when the return expression references a parameter **AND** carries no
string literal of its own — `_managed_policy_cache_path` keeps its literal-bearing return (the filename
survives regardless of the parameter); `_abs` does not (both operands are bare names, nothing in the
return itself is a literal).

### Measurement (the bar CVO~Z set, run before redelivering)

Every resolved call site across all 92 tools, before vs. after, diffed programmatically (not sampled):

| Category | Count |
|---|---|
| Identical (unchanged) | 7,057 |
| New resolutions (previously unresolved → now resolved) | 726 |
| Changed resolutions (resolved both before AND after, to a different value) | 139 |
| — of which: cosmetic-only (no artifact-filename token differs, just surrounding noise-word drift) | 131 |
| — of which: real artifact-identity change | **1** |
| Lost resolutions (resolved before → unresolved after) | 0 |

The 131 cosmetic-only rows are the flat-namespace bug's OTHER symptom made visible: phantom words
(`warehouse_bucket warehouse_bucket`, stray path fragments) bleeding in from unrelated functions'
same-named locals, now correctly absent. **The single real identity change was checked against source
directly, not assumed correct because the diff produced it:** `org/modules/graph/types_cli.py:356`
(`comp-types`) — a `manifest_path` local reused across two unrelated functions in the same file (line 352's
`f'{type_name}.blast.yaml'` vs. line 406's `f'{type_name}.fields.yaml'`). Before this fix, line 356's
write resolved to `.fields.yaml` (bled in from the *other* function) — genuinely wrong in the delivered
register. After: `.blast.yaml`, confirmed correct by reading `types_cli.py:340-356` directly (the write at
:356 sits inside the function that assigns `manifest_path` at :352). **Zero unexplained real
identity changes; the one found was root-caused, not just noted.**

**Net effect on the register:** `comp-blast`/`comp-build`/`comp-diff`/`comp-gitdrill`/`comp-pipescript`/
`comp-platinum`/`comp-surface-check`/`comp-trace`/`comp-xref` gained `LIVE-AWS`+`SOURCE-SCAN` in `writes[]`
(the `_provenance.py` stamp-writers and `extract_pipeline.py` dispatch parsers, previously invisible
through the same wrapper-taint-plus-flat-namespace gap); `comp-iam` gained `DERIVED-CACHE` in both
`reads[]` and `writes[]` (it both reads AND refreshes its own IAM-action cache — a write path this lane
had not previously surfaced); `comp-system`/`comp-tool-health` gained `DERIVED-CACHE`/`CONFIG` respectively.
Full per-tool diff preserved in `.comp-graph/tmp/before_scoping_fix.json` (session-local) if a future audit
wants the exact before-state; the committed `D.raw_evidence.json` now reflects the corrected pipeline only.

Gate-case + held-out regression check (re-run after every fix in this section, not just once at the end):
all 4 published acceptance-gate cases and both held-out self-check tools (`comp-secrets`, `comp-lambdamap`)
confirmed unchanged in substance. Full detail: MCP thread with CTO~Z/CVO~Z, `20260725T0001Z`-`0035Z`.
