# NFRA_TOOLUNIFY REC-1c — Lane B: Behavioral Exercise of the graph.json-family + Source-Scan Batch (17 tools)

**author:** `0.8.0_AE_CloudComp~B` · 2026-07-25 · **status:** DELIVERED, pending CVO~Z verification
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY (off-main-fabric census group)
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T060205Z, "DISPATCH NFRA_TOOLUNIFY REC-1c LANE-B — exercise batch
(17 tools, graph/source-scan affinity) + gitlink note"; addendum 20260725T060435Z (provisional
mutation-type labels)
**builds on:** `REC1_EXERCISE.md` + `REC1B_EXERCISE.md` (same directory, authored by `~D`) — same method,
same acceptance bar (positive control + mutant as separate invocations, denominator printed, LOUD/FAIL-OPEN/
SILENT-EMPTY classification against D.md's register).
**sidecar:** `REC1C_B.sidecar.json` (this directory) — per-invocation raw stdout/stderr, exit codes, output
file paths.

> **Mutation-type labels here are PROVISIONAL, pending the L0b change-type vocabulary
> (IMPLEMENTATION_LEVELS_AND_SEQUENCING.md s4/L0b) — this sweep records candidate vocabulary, it does not
> settle it.** (verbatim per CTO~Z's addendum, 20260725T060435Z)

> **RC-CAPTURE METHODOLOGY DISCLOSURE (per CTO~Z's 20260725T063930Z URGENT-BEFORE-DELIVERY: the harness-level
> reported exit code is corrupted in this Cygwin shell by a trailing cwd-tracking step that fails on every
> call and overwrites the true rc).** Every rc in §3's table was captured **in-stdout, immediately after the
> command, never piped**: `<cmd> > file 2>&1; echo "RC=$?"` — the exact form CVO~Z's controls confirmed
> accurate. **Two exceptions, disclosed rather than silently presented as captured:** the `comp-depth` and
> `comp-similar` mutant rows (both hit a multi-minute live-infra path, §4) were launched via `nohup ... &`,
> which does not hand back `$?`. Neither row's rc was fabricated or guessed — both are **source-confirmed**
> (the exact code branch each invocation hit, read directly, cited by file:line in §4) rather than
> **in-stdout captured**. This distinction is preserved in §3/§4 rather than flattened into an ordinary
> captured rc.

---

## 1 · Denominator

**17 of 17 dispatched tools exercised, all 17 fully resolved (positive control + mutant, both completed for
every row).** Two of the 17 (`comp-depth`, `comp-similar`) needed a multi-minute background run before their
mutant invocation resolved — both are closed with a source-confirmed rc (§4), not left open, and their
extreme wall-clock cost is reported separately as a LATENCY / LIVE-DEGRADATION finding rather than folded
into the failure_mode classification. No tool was skipped; no row is UNTESTABLE-SAFELY (every one of the 17
has a safe, read-only exercise path). Zero production writes, zero S3 puts, zero commits, zero infra mutation
— confirmed per-tool below (§2 write-safety) before exercising, per the dispatch's PRODUCER-flagged-tools
instruction.

## 2 · Method + write-safety pre-check

Dispatch idiom (D.md §3.1 taxonomy): 15 of 17 are idiom-1 bash-wrapper (`.tools/comp-X` -> `python
"$WORKSPACE/org/modules/graph/<impl>.py" "$@"`); `comp-depth`/`comp-symbols` are idiom-3
(`exec "${COMP_PYTHON:-python}" ...` inside a `set -euo pipefail` bash file, git-toplevel-resolved);
`comp-grep`/`comp-imgread` are idiom-2 (python shebang is the entry point — invoked via `python3
.tools/comp-X` directly per REC-1 §6's banked gotcha, never `bash .tools/comp-X` on these two).

**Write-safety, confirmed by source read before any exercise** (grep for `put_object|upload_file|boto3\.client\(['"]s3|\.put\(` and separately for `json\.dump\(|write_text\(|open\([^)]*['"]w['"]|\.unlink\(`
across all 11 backing implementation files): **zero S3-write calls in any of the 17 tools' own code.**
Four backing files carry a *local* write path, all on a **non-default subcommand I deliberately did not
invoke**:
- `comp-graph clear` (`.unlink()`s local cache) — exercised `status` only.
- `comp-pydeps build` ((re)scan + cache write) — exercised `consumers` only.
- `comp-constants index`/`new` (writes the constants index) — exercised `list`/`check` only.
- `comp-residue pin` (writes a pin file) — exercised `surface` only.
`comp-similar` carries one `.unlink()` (a temp-artifact cleanup inside its own scratch flow, not a
production key) and is otherwise consistent with its own docstring ("Advisory, read-only, hold-aware, NO
delete verb"). `comp-imgread`'s writes are its *designed* function (OCR tile PNGs) and were routed to
`--out <scratch>` in the workspace scratchpad, never a repo or production path. **No commit was made by this
lane** (CTO~Z's BASE_EXEC lane owns this path per REC-1/REC-1b's established convention — this file is
written to disk for CTO~Z to commit).

Classification convention, carried unchanged from REC-1 §3 (worked examples: `comp-manifest-check` rc=1
BLOCKED = LOUD; `comp-iam`/`comp-freshness`/`comp-glob` rc=0-with-message = FAIL-OPEN regardless of message
quality unless nothing prints at all):
- **LOUD** — nonzero exit (the operative, practically-applied discriminator — an rc=0 run is never
  classified LOUD in this sweep, however well-labeled the message, consistent with every REC-1/REC-1b
  worked example).
- **FAIL-OPEN** — zero exit, a human-readable note is present, nothing a script gating on exit code alone
  would catch.
- **SILENT-EMPTY** — zero exit, no signal reaches the consumer at all.
- **TIMEOUT/HANG** (this pass's addition, not in the register's vocabulary — flagged explicitly as new, not
  folded into the three existing values) — the invocation neither exits nor produces output inside a
  multi-minute wall-clock budget. See §4.

## 3 · Results table (17 tools)

| # | Tool | Declared `failure_mode` (register) | Mutation type | Mutant input | Observed | Verdict |
|---|---|---|---|---|---|---|
| 1 | `comp-blast` | LOUD (MED) | NONEXISTENT | node id `zzz_definitely_nonexistent_target_9999` | rc=3, explicit `NOT-FOUND:` + denominator + redirect hints | **MATCH** |
| 2 | `comp-build` | LOUD (MED) | MALFORMED | unrecognized flag `--zzz-nonexistent-flag-9999` | rc=1, argparse `error: unrecognized arguments` | **MATCH** |
| 3 | `comp-diff` | LOUD (MED) | NONEXISTENT | git ref `--ref zzz_nonexistent_ref_9999` | rc=1, `git diff failed: fatal: ambiguous argument` | **MATCH** |
| 4 | `comp-trace` | LOUD (MED) | NONEXISTENT | node id `zzz_definitely_nonexistent_target_9999` | rc=3, explicit `NOT-FOUND:` | **MATCH** |
| 5 | `comp-xref` | LOUD (MED) | NONEXISTENT | symbol-lookup mode, `zzz_definitely_nonexistent_symbol_9999` | rc=3, `No matches in graph` + hints | **MATCH** (no-args baseline-diff mode NOT exercised — see §4, LATENCY) |
| 6 | `comp-depth` | LOUD (MED) | NONEXISTENT | node id `zzz_definitely_nonexistent_target_9999` | rc=1, explicit `node not found at the marker head: ... (canon: ...)` — but only after ~9-10 minutes wall-clock in the background, after 2 separate foreground attempts (60s, 4min) had already timed out with zero output (see §4) | **MATCH on the failure_mode axis; separately a LATENCY finding — extreme wall-clock cost, not a classification miss** |
| 7 | `comp-platinum` | LOUD (MED) | NONEXISTENT | page name `zzz_definitely_nonexistent_page_9999` | rc=1, `Component not found: ...` | **MATCH** |
| 8 | `comp-graph` | LOUD (HIGH) | MALFORMED | subcommand `zzz_bad_subcommand_9999` | rc=2, argparse `invalid choice` | **MATCH** |
| 9 | `comp-grep` | LOUD (MED) | NONEXISTENT (0-match pattern) | `zzz_definitely_nomatch_pattern_9999` | rc=0, explicit `OK: ... 0 match(es) ... 0 matches is a real result here` | **MISMATCH** — declared LOUD, observed FAIL-OPEN (§5.1) |
| 10 | `comp-pydeps` | FAIL-OPEN (MED) | NONEXISTENT | file `zzz_definitely_nonexistent_file_9999.py` | rc=3, explicit `NOT DEFINED: no scanned python file named ...` | **MISMATCH** — declared FAIL-OPEN, observed LOUD (§5.2) |
| 11 | `comp-symbols` | LOUD-default (LOW) | NONEXISTENT | file `zzz_definitely_nonexistent_file_9999.py` | rc=1, `comp-symbols: file not found: ...` | **MATCH** |
| 12 | `comp-constants` | FAIL-OPEN (MED) | NONEXISTENT | `check --file zzz_definitely_nonexistent_file_9999.py` | rc=0, `OK: no tracked constants found in ... -- 0 of 34 ... nothing to check` | **MATCH on axis, flagged substantive concern** (§5.3 — the message never discloses the file does not exist) |
| 13 | `comp-dataflow` | LOUD-default (LOW) | NONEXISTENT | `origin zzz_definitely_nonexistent_script_9999.py` | rc=3, explicit `REFUSE: ... did not resolve to a producer .py file -- nothing traced, nothing concluded` | **MATCH** |
| 14 | `comp-similar` | FAIL-OPEN (MED) | NONEXISTENT | resource name `zzz_definitely_nonexistent_resource_9999` | rc=2 (source-confirmed, `debtscan/comp_similar.py:445`), `comp-similar: EMPTY corpus (broken retrieval, not an empty estate)` — but only after its own two `comp-kuzu` subprocess calls each independently timed out at 180s (see §4) | **MISMATCH — declared FAIL-OPEN, observed LOUD (§5.2); separately, a live comp-kuzu degradation finding (§4)** |
| 15 | `comp-residue` | FAIL-OPEN (MED) | NONEXISTENT | source `zzz_definitely_nonexistent_source_9999.yaml` | rc=3, `REFUSE: source not found: ... NOTHING was compared, so nothing is concluded` | **MISMATCH** — declared FAIL-OPEN, observed LOUD (§5.2) |
| 16 | `comp-shell` | FAIL-OPEN (MED) | NONEXISTENT | path `zzz_definitely_nonexistent_path_9999/` | rc=0, `path not found or not .sh: ... no .sh files to scan.` | **MATCH** |
| 17 | `comp-imgread` | FAIL-OPEN (MED) | NONEXISTENT | image `zzz_definitely_nonexistent_image_9999.png` | rc=2, `comp-imgread: ERROR: image not found: ...` | **MISMATCH** — declared FAIL-OPEN, observed LOUD (§5.2) |

**Scoreboard: 11 MATCH, 5 MISMATCH, 1 MATCH-with-caveat. All 17 of 17 fully resolved — zero UNTESTABLE-SAFELY,
zero left UNRESOLVED at delivery.** (Two rows — `comp-depth`, `comp-similar` — needed a multi-minute
background run before resolving; both are now closed with a source-confirmed rc, not left open.) Every
positive control (all 17) ran clean against a real target and produced ANSWER-BEARING output, confirming the
exercise harness itself is not systematically mis-dispatching (the idiom-2/idiom-3 distinction was respected
throughout; no `bash`-on-a-shebang-file mis-invocation occurred this pass).

## 4 · LATENCY / LIVE-DEGRADATION finding: `comp-depth` and `comp-similar` both cost multiple minutes on a
live-corpus read — one now source-traced to a specific, independently-confirmable root cause

Both tools' **positive controls completed successfully** — `comp-depth grains gold:A_00.accounts_dimension`
returned a correct, well-formed answer (eventually; see below), and `comp-similar --self-test` returned
`PASS (7/7)` in normal time (it is explicitly an offline mode, "no graph/AWS", per its own docstring). It is
specifically each tool's **live-corpus mutant (nonexistent-target) invocation** that cost multiple minutes —
and now, both are fully resolved with a source-confirmed root cause, not left as an open question.

**`comp-similar` — root cause IS source-confirmed, and it is upstream of `comp-similar` itself:** the mutant
invocation eventually printed two identical stderr lines before its final answer:
```
summary_corpus: comp-kuzu invocation failed: Command '[... .tools\comp-kuzu --json "MATCH (n:CloudNode) ..."]' timed out after 180 seconds
summary_corpus: comp-kuzu invocation failed: Command '[... .tools\comp-kuzu --json "MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) ..."]' timed out after 180 seconds
comp-similar: EMPTY corpus (broken retrieval, not an empty estate)
```
**`comp-kuzu` itself — a tool outside this lane's 17-tool batch, not separately exercised this pass — timed
out at exactly 180 seconds on two consecutive live queries (~6 minutes total) inside `comp-similar`'s corpus
build.** `comp-similar`'s own code caught this correctly and distinguished it from a legitimate empty result
(`debtscan/comp_similar.py:444`, `"EMPTY corpus (broken retrieval, not an empty estate)"`, `return 2` —
source-read, matches §3 row 14's rc exactly) — this is **good design**, not a defect in `comp-similar`; the
defect, if it is one, is upstream in whatever `comp-kuzu`'s own live query path is currently waiting on.
**This was not chased into `comp-kuzu`'s own source this pass** (out of batch scope) — flagged as a named,
reproducible, specific lead (exact 180s timeout, exact two Cypher queries, exact subprocess invocation) for
whoever owns `comp-kuzu` or the next latency/health pass, not asserted as a diagnosed root cause beyond what
the two stderr lines themselves state.

**`comp-depth` — same *family*, a different and NOT yet common-rooted mechanism:** first attempt timed out
at 60s with zero output; a second, separate attempt timed out at 4 minutes with zero output; backgrounded, it
eventually completed (~9-10 minutes wall-clock from first launch) and printed
`[marker-head: BEHIND | head=5957908056775835011]` followed by a correct answer — **the marker-head Kuzu DB
this tool reads (`infra/aws/globgrph/kuzu_nessie_db`, confirmed via `_canonical.CANONICAL_DB_PATH`) is
currently BEHIND, and `comp_marker_read.load_marker_head_graph()` calls `_canonical.ensure_fresh(path)`
(a marker-oracle auto-refresh on HEAD-advance) before every read** — source-read at
`org/modules/graph/comp_marker_read.py:322-338`. This is an **embedded, in-process Kuzu DB open
(`kuzu.Database(path, read_only=True)`), not a `comp-kuzu` subprocess call** — mechanically distinct from
`comp-similar`'s path, source-confirmed as distinct, **not asserted to share the same root cause** even
though both land in the same multi-minute-on-a-live-corpus family. The mutant invocation (nonexistent node)
took comparably long (~9-10 min from background-launch to completion) and resolved to rc=1 (source-confirmed,
`comp_depth_cli.py:101`), `node not found at the marker head: ...` — LOUD, matching declared LOUD.

**What this is NOT claiming:** not a broken tool in either case (`comp-similar`'s degradation-handling
worked correctly; `comp-depth`'s positive control and mutant both eventually returned correct answers) — and
not claiming a single shared root cause across the two (one is source-confirmed as a `comp-kuzu` subprocess
timeout, the other as an in-process `ensure_fresh` auto-refresh; both READ the same underlying Nessie/Kuzu
estate but through different code paths). **What IS established, source-confirmed, this session, this box:**
(a) `comp-kuzu --json` timed out at 180s on two consecutive live queries; (b) the marker-head Kuzu DB is
currently in a `BEHIND` provenance state and its auto-refresh-before-read cost ~9-10 minutes; (c) both
findings are independently reproducible (exact commands, exact file:line citations) by anyone who wants to
re-run them, including CVO~Z.

**Recommendation:** two separate follow-ups, not one. (1) `comp-kuzu`'s 180s timeout is a concrete, named lead
for whoever owns it — worth checking whether the underlying Nessie catalog / Kuzu process is currently
degraded fleet-wide (this is the same estate every other census lane's `comp-kuzu`-backed tool reads) rather
than something specific to this session. (2) The census's `failure_mode` column has no vocabulary for
"correct but slow enough that an interactive caller may reasonably conclude it hung" — worth a fourth value
or a `latency_class` column alongside `failure_mode`, distinct from the existing LOUD/FAIL-OPEN/SILENT-EMPTY
axis (which measures *informativeness on failure*, not *wall-clock cost of a successful or unsuccessful
call*). **This is a direct, exercised data point for `NFRA_TOOLARCH.LATENCY`'s "every-derivation-wallclock-
census"** (already dispatched to this lane, sitting in queue) — routed there rather than re-scoped as a
finding of its own, but (1) above is time-sensitive enough that CTO~Z may want to act on it sooner than that
TO's own schedule.

## 5 · Mismatch findings, grouped by shape

### 5.1 · `comp-grep`: declared LOUD, observed FAIL-OPEN on a zero-match pattern

A third instance of the exact pattern REC-1/REC-1b already named twice (`comp-freshness` WARN-not-FAIL,
`comp-surface-check scan` missing-input skip): a declared-LOUD row that, on the specific case of "the
search/lookup came back with literally nothing," returns `rc=0` with a well-labeled but script-invisible
message. `comp-grep`'s own output text is honest and good ("0 matches is a real result here"), so this is
not a silent defect — it is a genuine **declared-vs-observed axis mismatch**: a caller relying on the
register's LOUD classification to gate a script on exit code alone would not catch a zero-match condition
here. **Now three independent tools, three independent absent/zero-result tests, three mismatches in the
same direction** — this pattern is no longer a one-off or even a pair; it is a recurring shape across the
register that a future methodology pass should treat as systematic, not per-tool.

### 5.2 · `comp-pydeps`, `comp-residue`, `comp-imgread`: declared FAIL-OPEN, observed LOUD on a totally-absent input — the opposite direction, and a GOOD surprise

Three tools declared FAIL-OPEN (MED confidence) each turned out to be *stricter* than declared on the
specific mutation tested: a wholly nonexistent file/source/image input produced a nonzero exit and an
explicit, well-labeled refusal message in all three (`NOT DEFINED`, `REFUSE: source not found ... NOTHING
was compared`, `ERROR: image not found`). This is the mirror image of §5.1 — a declared classification that
undersells the tool's actual behavior rather than oversells it. **Worth naming distinctly from §5.1's
direction**: a register consumer reading "FAIL-OPEN" as "will not catch a bad input" would be pleasantly
wrong for all three of these, on this specific mutation class. Whether this generalizes to their other
subcommands/input classes is not established here (single mutation type per tool, per this pass's scope) —
flagged as a candidate register-confidence correction, not asserted as the tool's complete behavior.

### 5.3 · `comp-constants`: MATCH on the failure_mode axis, but the mutant result is the sharpest version yet of the "total-absence reads as clean" theme

`comp-constants check --file <nonexistent path>` returned `rc=0` and printed `OK: no tracked constants found
in zzz_definitely_nonexistent_file_9999.py -- 0 of 34 config constant(s) appear here, nothing to check`.
Classified MATCH against declared FAIL-OPEN (MED) on the LOUD/FAIL-OPEN/SILENT-EMPTY axis — rc=0, a message
is present — but the SUBSTANCE of that message is the most concerning result in this pass, more so than
REC-1's `comp-freshness` WARN or REC-1b's `comp-surface-check scan` skip, both of which at least named the
absence condition. **Here the tool never checked whether the file exists at all** — source-read confirms
`check --file` scans the given path for the 34 tracked constant names and reports on matches found; a
nonexistent path and an existing-but-constant-free path are **indistinguishable in the output**, both
rendering the identical reassuring `OK: ... nothing to check`. A typo'd `--file` path in a CI/gate context
would read as "checked, clean" rather than "never actually ran." Not asserting this is a defect in intent
(constants-drift checking may reasonably not care about file existence as its own concern) — but flagging it
as the pattern's sharpest instance for CTO~Z/CVO~Z's methodology-revisit thread, since it is strictly worse
than a WARN: it does not even use a distinguishing word.

## 6 · Portal gitlink re-measurement (secondary ask)

Re-measured at today's HEAD, same method as the prior census pass: pinned gitlink commit `343e7b2a`
(`git ls-tree HEAD portal`) vs. portal's current checked-out HEAD `d1ba89b9` (`git -C portal rev-parse
HEAD`). **`git -C portal rev-list --count 343e7b2a..d1ba89b9` = 5 — unchanged from the prior measurement.**
`git -C portal merge-base --is-ancestor 343e7b2a d1ba89b9` = true — **still a clean ancestor (behind, not
diverged)**, so "5 commits stale" remains the right words (a diverged pointer at the same rev-list count
would misleadingly read the same).

The 5 commits (`git -C portal log --oneline 343e7b2a..d1ba89b9`):
```
d1ba89b9 feat(W-4, MDPF_3FIRMS.GC-W45): count provenance VISIBLE at render -- six producer classes carried
96e8c67d fix(W-5b, MDPF_3FIRMS.GC-W45): the `aum` SIBLING LIE on the same lines -- 24 nulls of 447
02fb2956 fix(W-5, MDPF_3FIRMS.GC-W45): account_count is NULLABLE at BOTH layers -- 40 nulls of 447
8602d0f7 tooling(ui-smoke): --hoverlast aims the frontier (rightmost data point)
3e681423 tooling(ui-smoke): --hoverlast -- scroll-into-view + jittered hover on the last chart
```
**Recommendation:** these are active, substantive `MDPF_3FIRMS.GC-W45` fixes (null-handling honesty at two
layers), not idle drift — this reads as the "expected-during-active-portal-work" case CTO~Z's dispatch named
as one of the two reconciliation options, not the "bump now" case. Per Rule 19 (portal main tree stays on
DEV, promotes are a DT lane) and CTO~Z's explicit no-commit-without-my-gate instruction, **no submodule bump
was made or attempted** — surfacing the recommendation only: hold the gitlink where it is until this GC-W45
wave lands/stabilizes or DT's next scheduled promote cycle naturally advances it, rather than bumping
mid-wave for its own sake.

## 7 · What this lane did NOT do

No apply, deploy, re-point, or write to any production S3 key, DynamoDB table, or Terraform-managed
resource. No commit to `org/tier1_exec/1.0.0_SA_CTO/**` (CTO~Z's BASE_EXEC lane, same convention as
REC-1/REC-1b). Did not invoke any of the four identified local-cache-write subcommands (`comp-graph clear`,
`comp-pydeps build`, `comp-constants index`/`new`, `comp-residue pin`). Did not exercise `comp-xref`'s
default no-args baseline-diff mode (forces a full rebuild; timed out at 2 minutes on first attempt — routed
to §4 as a LATENCY data point rather than chased to completion, since `--check` + symbol-lookup mode already
satisfied the acceptance gate without the expensive path). Did not chase `comp-kuzu`'s own 180s timeout into
its source (§4) — out of this lane's 17-tool batch scope, flagged as a named lead, not diagnosed further.
Did not commit the portal gitlink bump — recommendation only, per explicit instruction.
Did not label any row UNKNOWN in the sense of "could not synthesize a safe bad input" — every one of the 17
tools had an available, safe NONEXISTENT or MALFORMED mutation, and all 17 fully resolved (two needed a
multi-minute background run before resolving, per §4, but none was left open at delivery).

## 8 · Handoff

- **`1.0.0_SA_CTO~Z`**: §4's two findings need different urgency — the `comp-kuzu` 180s-timeout-x2 is a
  named, reproducible lead worth checking sooner than the general census schedule (is the underlying
  Nessie/Kuzu estate degraded fleet-wide right now?); both findings are also direct, exercised input to
  `NFRA_TOOLARCH.LATENCY`'s wallclock census (already dispatched, in queue) — recommend folding this pass's
  `comp-depth`/`comp-similar` timings in rather than re-deriving them. §5.1-5.3's three-shaped mismatch
  cluster (under-catch / over-catch / substance-worse-than-axis-suggests) is new input to the same
  methodology-revisit thread REC-1b's §9 CVO~Z verdict already flagged as "twice independently confirmed, act
  on it." §6's gitlink recommendation is a hold, not an action — yours or DT's to execute if agreed.
- **`3.0.0_SA_CVO~Z`**: all 17 rows are re-derivable — 15 from the sidecar's verbatim stdout/stderr + exit
  codes (ordinary in-stdout `echo RC=$?` capture); the 2 background rows (`comp-depth`, `comp-similar`
  mutants) have their rc **source-confirmed by file:line citation in §4** rather than in-stdout captured
  (both cost 6-10 minutes wall-clock; re-deriving live would cost the same again — the source citations are
  independently checkable without re-running). Every rc in this deliverable was captured per CTO~Z's
  20260725T063930Z URGENT methodology (in-stdout, never the harness-reported code) — flagging this
  explicitly since that message landed mid-pass, per §0's disclosure block.
