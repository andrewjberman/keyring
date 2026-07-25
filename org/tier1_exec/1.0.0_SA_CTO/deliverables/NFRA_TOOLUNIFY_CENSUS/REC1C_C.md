# NFRA_TOOLUNIFY REC-1c LANE-C — Exercise Batch: Routing / Registry / Validation Family (16 tools)

**author:** `0.8.0_AE_CloudComp~C` · 2026-07-25 · **status:** DELIVERED, pending CVO~Z verify
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY (off-main-fabric census group)
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T060457Z, "DISPATCH NFRA_TOOLUNIFY REC-1c LANE-C — exercise batch
(16 tools, routing/validation affinity) + ms_heat disposition"
**sidecar:** `REC1C_C.sidecar.json` (this directory) — per-invocation verbatim key output, exit codes,
mutation labels, per-row notes.
**builds on:** `REC1_EXERCISE.md` + `REC1B_EXERCISE.md` (method, acceptance-gate bar, banked gotchas).

> **Mutation-type labels here are PROVISIONAL, pending the L0b change-type vocabulary
> (IMPLEMENTATION_LEVELS_AND_SEQUENCING.md s4/L0b) -- this sweep records candidate vocabulary, it does not
> settle it.**

---

## 1 · Denominator (printed per dispatch instruction)

**16 of 16 batch tools invoked — 0 skipped.** 14/16 exercised with a synthesized mismatched/absent input;
2/16 recorded **UNKNOWN** (`comp-routable-check`, `comp-toolgraph`) because no safe bad-input could be
synthesized — their only inputs are the live manifest/register files themselves, with no path flag to point
at a mutated copy, and mutating the live files is a production write outside this lane's read-only scope.
Per the dispatch's labeling rule, UNKNOWN is recorded as UNKNOWN — not coerced to MATCH, not dropped —
and both rows carry a live-state observation in lieu.

**Verdicts: 10 MATCH · 4 MISMATCH · 2 UNKNOWN.** Mutation-type mix: NONEXISTENT ×11, MALFORMED ×1,
EMPTY ×1, LIVE-DRIFT ×1 (named extension), UNKNOWN ×2.

## 2 · Acceptance gate — both anchors, separate invocations (Rule 22a)

- **Positive control** — `comp-manifest-check check --mode blocking` on a synthetic anti-pattern file
  (REC-1 4a recipe): **rc=1, explicit `BLOCKED`. Known-LOUD reads LOUD. PASS.**
- **Mutant** — `comp-freshness artifact` on a wholly nonexistent S3 prefix (REC-1 s5.1's known
  declared-LOUD/observed-WARN mismatch, CVO~Z-reproduced): **rc=0, `STATUS=WARN`. Known non-LOUD reads
  non-LOUD. PASS — the harness discriminates in both directions.**
- Harness self-correction disclosed: my first rc-capture ran the tool through a pipe and read `head`'s exit
  code, not the tool's. Caught before anything was recorded; every recorded RC below is from an unpiped
  invocation (control-the-retrieval class; disclosed per this program's own discipline, sidecar
  `harness_validation.note`).

## 3 · Results

| # | Tool | Declared (conf) | Mutation | RC | Observed | Verdict |
|---|---|---|---|---|---|---|
| 1 | `comp-which` | FAIL-OPEN (MED) | MALFORMED gibberish question | 0 | FAIL-OPEN — announces "no rich comp-tool fits", degrades to `comp-grep` | **MATCH** |
| 2 | `comp-which-routing-test.py` | LOUD (MED) | NONEXISTENT snapshot | 1 | LOUD — raw traceback | **MATCH** |
| 3 | `comp-registry` | FAIL-OPEN (MED) | NONEXISTENT project code | 1 | LOUD — explicit one-line error | **MISMATCH (louder)** |
| 4 | `comp-routable-check` | LOUD (MED) | UNKNOWN — no safe bad-input channel | 0 | live: OK + advisory WARN class | **UNKNOWN** |
| 5 | `comp-ontolint` | LOUD (MED) | NONEXISTENT rule-bank | 2 | LOUD — graceful explicit ERROR | **MATCH** |
| 6 | `comp-toolgraph` | FAIL-OPEN (MED) | UNKNOWN — no external-input channel | 0 | live: well-formed report | **UNKNOWN** |
| 7 | `comp-tool-health` | LOUD (MED) | NONEXISTENT tool name | 0 | FAIL-OPEN — "not found" note, rc=0 | **MISMATCH** |
| 8 | `comp-tool-health-gate` | LOUD (MED, weak) | NONEXISTENT --effective-feed path | 0 | FAIL-OPEN **by documented design** | **MISMATCH** |
| 9 | `comp-validate` | LOUD (MED) | NONEXISTENT script id + artifact | 1 | LOUD — graceful, actionable | **MATCH** |
| 10 | `comp-coverage` | LOUD (default, LOW) | NONEXISTENT pipeline filter | 0 | FAIL-OPEN — well-formed all-zeros report | **MISMATCH** |
| 11 | `comp-coverage-check` | LOUD (MED) | LIVE-DRIFT (real violation live) | 1 | LOUD — explicit FAIL | **MATCH** + live finding |
| 12 | `comp-parity` | LOUD (default, LOW) | NONEXISTENT firm | 1 | LOUD — raw traceback | **MATCH** |
| 13 | `comp-honesty` | LOUD (MED) | NONEXISTENT case.json | 1 | LOUD — raw traceback | **MATCH** |
| 14 | `comp-kit-striplist-gate` | LOUD (MED, weak) | NONEXISTENT kit_root | 2 | LOUD — graceful explicit ERROR | **MATCH** |
| 15 | `comp-to` | FAIL-OPEN (HIGH) | EMPTY (session-id env unset) | 0 | FAIL-OPEN — WARN + fallback, writes nothing | **MATCH** |
| 16 | `comp-xray` | LOUD (MED) | NONEXISTENT S3 key | 2 | LOUD — rc=2 UNVERIFIABLE per its own printed contract | **MATCH** |

Verbatim outputs, full invocations, and per-row notes: sidecar.

## 4 · Findings

### F1 · The absent-input FAIL-OPEN pattern is now a confirmed register-wide theme, not a candidate

REC-1b closed saying the pattern (declared-LOUD rows failing open specifically on **wholly absent** input)
was "2/2 so far... warrant[s] a targeted third check before generalizing." **This batch supplies instances
3, 4, and 5:**

| # | Tool | Absent input | Behavior |
|---|---|---|---|
| 1 | `comp-freshness artifact` (REC-1) | nonexistent S3 prefix | WARN, rc=0 |
| 2 | `comp-surface-check scan` (REC-1b) | missing --current file | ADVISORY skip, rc=0, "never crash the nightly" |
| 3 | `comp-tool-health` | nonexistent tool name | note printed, rc=0 (`comp_tool_health.py:600` — returns a string, no exit code) |
| 4 | `comp-tool-health-gate` | nonexistent --effective-feed path | silently coerced to "no feed", full ledger proceeds, rc=0 (`comp_tool_health.py:392,396-402` — "missing/unreadable file returns {} ... never a crash", by docstring design) |
| 5 | `comp-coverage report` | filter matching nothing | well-formed all-zeros report, rc=0 |

Five instances, four independent tool families, every one exercised (not AST-inferred). Three are
**documented design** ("never a crash" / "never crash the nightly" / advisory-gate semantics) — which is
the sharper point: **the estate has a real, recurring design convention of degrade-on-absence, and the
register's LOUD/FAIL-OPEN column cannot express "LOUD on bad content, SILENT on missing input."** A
register consumer reading `LOUD` will assume absence alarms. It demonstrably does not, five times over.
Recommend: absence-behavior becomes its own register dimension (or the L0b vocabulary carries an
ABSENT-input axis distinct from MALFORMED/STALE), rather than more per-tool one-off corrections.

### F2 · `comp-coverage`'s empty-filter report is the dangerous shape of the five

`report --pipeline <nonexistent>` prints `Total TOs: 0 ... Raw coverage: 0.0%`, rc=0. That is not a
missing answer — it is a **plausible wrong number** (Verification-Law-12 class: "a wrong number is more
dangerous than a zero" — here it IS a zero that reads as a measurement). A typo'd pipeline filter yields a
catastrophic-looking-but-fake 0.0% compliance figure with no "no such pipeline" signal anywhere. Cheap fix
shape (not actioned, read-only lane): a filter that matches zero TOs AND zero comp-log rows should say so
explicitly.

### F3 · Two rule-derived register rows are wrong as declared; two LOW/default rows verified

- `comp-registry`: declared FAIL-OPEN (except-swallow heuristic), observed **LOUD** on a nonexistent
  project. Benign direction, but the row is wrong as declared — the AST heuristic (swallow-count ≥
  loud-count) misread this tool.
- `comp-tool-health`: declared LOUD, observed FAIL-OPEN (F1#3) — the comp-iam-service "fails GREEN" shape
  reproduced on a register-family tool.
- First individual verifications of two LOW-confidence `LOUD (default)` convention rows: `comp-parity`
  **holds** (rc=1), `comp-coverage` **does not** (F2). The convention default is now measured at 1-for-2 in
  this batch — corroborating the census's own caveat that defaults are not verification.

### F4 · Live estate findings surfaced by the exercise itself (routed, not actioned)

1. **`comp-residue` is UNPLACED in the coverage map right now** — `comp-coverage-check` FAILs live
   (`FAIL: inventory_completeness: tool 'comp-residue' is UNPLACED (in neither tools[] nor meta_tools[])
   -- silently dropped`), reproduced on two invocations. Whoever registered `comp-residue` did not update
   `comp-coverage-map.yaml`; a blocking consumer of comp-coverage-check would currently be red.
2. **4 router-reachable capabilities are absent from the tools_index catalog** (`comp-describe`,
   `comp-kuzu-full`, `comp-kuzu-inc`, `comp-state`) — `comp-routable-check` advisory WARN, live. Agents
   browsing the catalog cannot discover tools the router can actually reach.

### F5 · `comp-xray` rc=2 collision

Its documented exit contract is `0 clean / 1 integrity-break / 2 UNVERIFIABLE` — exercise-confirmed on a
nonexistent key. But an **argparse usage error also exits 2** (observed first-hand on my own malformed
first invocation, disclosed per the REC-1 s6 gotcha). A script consumer cannot distinguish "you called me
wrong" from "the artifact is unreadable" by exit code alone. Minor, but this is a GUARD-adjacent tool whose
rc=2 is semantically load-bearing.

### F6 · Friction (not failure_mode)

- Raw tracebacks instead of error messages on nonexistent input: `comp-which-routing-test.py`,
  `comp-parity`, `comp-honesty` (all LOUD, all ungraceful).
- `comp-coverage-check` has **no help path** — `--help` is ignored and the live check runs anyway.
- `comp-which` has no help path either — `--help` is treated as a question (rc=1, no-match banner).
- `comp-which`'s no-match fallback reduced a 7-token question to a single grep token and returned 200+
  text hits that could read as answers to a garbage question (honest banner, noisy body).
- MSYS path conversion rewrites `/nonexistent/...` argv to `C:/Program Files/Git/nonexistent/...` before
  tools see it (environment note in sidecar; mutations held either way).

## 5 · Producer safety (read-only discipline)

All 7 PRODUCER-CANDIDATE closures grepped for `put_object|upload_file|copy_object|delete_object|.put(|boto3`
— **zero hits, positive-controlled** (the same grep finds known carriers in `infra/aws/globgrph/`). Write
paths that do exist are local and flag-gated, and every write flag was avoided: no `--apply`
(comp-registry), no `--write` (comp-coverage), no `--emit` (comp-tool-health-gate), `--out` scratch +
post-run confirmed-unwritten (comp-which-routing-test.py), `--no-refresh` (comp-tool-health). `comp-to`'s
fallback branch source-confirmed to write nothing before invocation. S3 access was read-only
(`comp-xray s3` object-versions listing; `comp-freshness` prefix listing).

## 6 · What this lane did NOT do

No apply, deploy, write to any production resource, or commit to `org/tier1_exec/1.0.0_SA_CTO/**` (this
file + sidecar written to disk for CTO~Z to commit, per the established lane convention). Did not exercise
the FAIL/blocking class of `comp-routable-check` or any bad-input path of `comp-toolgraph` (UNKNOWN,
reasons in §1). Did not exercise multiple mutation types per tool — one primary mutation per tool per the
light-cycle discipline; the absent-input pattern (F1) is the explicit candidate axis for any widening pass.
Did not fix, or file records for, the two live findings in F4 — routed here for CTO~Z disposition.

## 7 · Handoff

- **`1.0.0_SA_CTO~Z`**: F1 (absence-behavior as a register dimension — now 5 exercised instances) is the
  decision-relevant item; F4's two live drifts need an owner (comp-residue coverage-map placement; the 4
  uncatalogued routables); F3's two wrong-as-declared rows are register corrections.
- **`3.0.0_SA_CVO~Z`**: every row is independently re-derivable from the sidecar (exact invocations +
  RCs + key output verbatim); the two source-grounded mechanism claims carry citations
  (`comp_tool_health.py:600`; `comp_tool_health.py:383-402` + `comp_tool_health_gate.py:324-334`) at
  working-tree vintage, this session, branch CLOUD.
- **ms_heat disposition** (secondary dispatch item): separate one-pager, same directory —
  `MS_HEAT_DISPOSITION_C.md`.
