# NFRA_TOOLUNIFY REC-1 — Predicate-Exercise of the §2.D Register's `failure_mode` Column

**author:** `0.8.0_AE_CloudComp~D` · 2026-07-25 · **status:** DELIVERED + CVO~Z-VERIFIED, closed
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY (off-main-fabric census group)
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T035435Z, "DISPATCH NFRA_TOOLUNIFY REC-1 — predicate-exercise the
register's failure_mode column"
**sidecar:** `REC1_EXERCISE.sidecar.json` (this directory) — per-invocation raw results, verbatim output
paths, exit codes.
**scope discipline:** v1, one change-type (empty/mismatched/stale input), light-cycle sample — not the
full L0b vocabulary, not exhaustive over the 92-tool register, per the dispatch's own explicit scope.

---

## 1 · Mission recap

The §2.D register's `failure_mode` column (`LOUD` / `FAIL-OPEN` / `SILENT-EMPTY`) was **AST-derived** — read
from a tool's error-handling code, never exercised against a real input. The six §0.2 through-line instances
were found by *accident*, only where a lane happened to hit the runtime. This deliverable systematizes that
discovery: feed a sample of tools a mismatched/stale/empty input, record the OBSERVED verdict, and compare it
to the register's DECLARED `failure_mode`.

## 2 · Denominator

**5 tools exercised directly + 1 dedicated positive control = 6 invocations, 5 distinct tools, against the
92-tool register (5/92, ~5%).** This is a v1 sample, not a sweep — selected to (a) satisfy the acceptance
gate's two mandatory anchors and (b) span the register's two populated `failure_mode` values (`LOUD`,
`FAIL-OPEN`; the register's third value, `SILENT-EMPTY`, is **discussed in §5 as a finding in its own right**
— see below). Why 5, not more: each exercise required reading the tool's actual dispatch idiom (two of five
hit idiom-2 shebang-file-is-the-entry and needed a re-invocation — see §6) and, for the mutant, tracing a real
call site outside the tool itself; this is deliberately manual-inspection-depth per tool, not a scripted sweep
across all 92 — consistent with the dispatch's "does not need the full L0b vocabulary yet" scope note.

**Selection logic:** the acceptance gate names its two anchors explicitly (a known-LOUD positive control, a
known-SILENT-EMPTY mutant drawn from the six through-line instances). I added three more spanning
`FAIL-OPEN` and touching two more of the still-open through-line themes (comp-iam's Rule-22a-flagged
resource-blindness; the freshness/absence-probe theme from the §0.2 sixth instance).

## 3 · Method

For each tool: identify its real dispatch idiom (per D.md §3.1 — bash-wrapper vs shebang-file vs
runpy-thin-wrapper vs shim-of-a-shim; a `bash .tools/comp-X` invocation on an idiom-2 tool silently
mis-dispatches into bash trying to parse Python source, which is itself informative and is logged, not
hidden, in §6). Feed a genuinely mismatched/stale/empty input (a nonexistent resource name, an absent S3
prefix, a synthetic anti-pattern file, or — for the mutant — today's actual live repo state, which already
contains the real condition under investigation, not a fabricated one). Capture exit code + full stdout/stderr
verbatim. Classify OBSERVED as:
- **LOUD** — nonzero exit AND/OR an explicit BLOCKED/ERROR/FAIL verdict a human or a script would both catch.
- **FAIL-OPEN** — zero exit, a human-readable note may be present, but nothing a script gating on exit code
  alone would catch.
- **SILENT-EMPTY** — zero exit, no signal reaches the consumer at all (this can be a property of the
  **invocation site**, not the tool — see §5.1, the headline finding).

**Safety constraint (binding for this lane, plan §3.2 read-only discipline):** no exercise may write to a
production S3 key, mutate live infra, or trigger a real git commit. Where a tool's only interface is
write-coupled (`comp-stitch-refresh` always publishes to S3 on invocation — confirmed by reading its source,
no dry-run flag exists), I exercised its underlying **read-only** producer script directly
(`derive_stitch.py --out <scratch>`, confirmed via source read to contain zero `put_object`/`upload_file`
calls — only `get_object` reads) instead of the writing wrapper. This is documented per-row in the sidecar.

## 4 · Acceptance gate — both anchors, run as separate invocations (Rule 22a discipline)

### 4a · Positive control — `comp-manifest-check` (known-LOUD, HIGH-confidence register row)

Invocation: `comp-manifest-check check --file <synthetic anti-pattern file> --mode blocking`, where the file
was seeded with the exact three violation classes the tool's own `selfcheck` subcommand (AC4) uses (raw
Cypher outside comp-kuzu; a direct `comp-aws derive` rebuild-path call in query position).

**OBSERVED:**
```
MANIFEST-CHECK [ERROR] .../anti_pattern_probe.py:2 (C_adhoc_reimplementation)
    > q = "MATCH (n:CloudNode) RETURN n.id"
    embeds raw Cypher outside comp-kuzu. ...
MANIFEST-CHECK [WARN] .../anti_pattern_probe.py:3 (B_rebuild_when_query)
    > subprocess.run(["comp-aws", "derive", "--out", "/tmp/g"])
    ...
BLOCKED: 1 ERROR-class graph-access finding(s). Use the canonical manifest call, or justify the exception.
RC=1
```
**VERDICT: LOUD. Matches DECLARED (`LOUD`, HIGH confidence). Positive control PASSES** — the harness
correctly reads a known-LOUD tool as LOUD; the exercise methodology is not systematically biased toward
either verdict.

### 4b · Mutant — `comp-stitch-refresh` / `derive_stitch.py` (§0.2 through-line instance #1, "stitch
83d-silent")

Invocation, tool-level (read-only producer, no S3 write — see §3 safety constraint): `python3
infra/aws/globgrph/derive_stitch.py --out <scratch>`, against **today's actual live repo + AWS-snapshot
state** — no fabricated mismatch was needed; the live state already contains the real anomaly under
investigation (`EXTERNAL_ENDPOINT` count = 0).

**OBSERVED (tool level):**
```
GRAIN-SENTINEL: FAIL (6 violation group(s))
  [AC-GRAIN.2] EXTERNAL_ENDPOINT: count 0 vs baseline 3 = 0.00x (outside [0.4, 2.5]x band)
  [AC-GRAIN.2] REACT_QUERY_KEY: count 85 vs baseline 32 = 2.66x (outside [0.4, 2.5]x band)
  [AC-GRAIN.2] SQS_QUEUE: count 12 vs baseline 4 = 3.00x (outside [0.4, 2.5]x band)
  [AC-GRAIN.2] ECS_TASK_DEFINITION: count 7 vs baseline 2 = 3.50x (outside [0.4, 2.5]x band)
  [AC-GRAIN.2] SCHEDULE: count 10 vs baseline 3 = 3.33x (outside [0.4, 2.5]x band)
  [AC-GRAIN.2] IAM_USER: count 4 vs baseline 1 = 4.00x (outside [0.4, 2.5]x band)
ERROR: GRAIN_SENTINEL_FAIL -- refusing to emit grain-violating stitch graph
RC=2
```
**At the tool boundary this is LOUD** (nonzero exit, explicit stderr, matches the register's DECLARED `LOUD`,
HIGH confidence) — **the register's tool-level classification is CORRECT and now exercise-confirmed, not just
AST-inferred.**

**But the register characterizes the tool, not its call site — and the call site is where the mutant actually
lives.** Read `.tools/git-hooks/stitch-refresh-post-commit.sh:26` (the tool's **only** production invocation
path per the census's own D.md §3 mission scope): it backgrounds `comp-stitch-refresh` in a detached
subshell, redirects **all** stdout+stderr to `${TMPDIR}/stitch-refresh.log`, and the hook script itself
**unconditionally `exit 0`** regardless of what the backgrounded process does. Corroboration, not
speculation: `stitch-refresh.log` on this machine carries **166 `GRAIN_SENTINEL_FAIL`-class lines** (83
occurrences × 2 lines each), matching the estate map's "83 straight since 07-08" finding exactly, and
`s3://opal-313476888478-globgrph/stitch/stitch_marker.json`'s live `LastModified` is `2026-07-08`
— 17 days stale, independently confirming no successful publish has landed since the failures began (and
confirming this exercise itself performed no write).

**OBSERVED (operational/call-site level, the only vantage the committer ever has):** rc=0 to git, zero
visible output, zero indication anything failed, across 83 real historical commits.
**VERDICT: SILENT-EMPTY. Matches the through-line's own characterization ("stitch 83d-silent") and satisfies
the acceptance gate's mutant requirement — but not at the layer the register measures.**

### 4c · What the gate result actually proves

Both anchors pass on their own terms, but 4b's two-layer result is the substantive finding, not a clean
pass/fail: **`failure_mode` as currently scoped is a per-tool property. A tool can be genuinely,
exercise-confirmed LOUD at its own boundary and still be operationally indistinguishable from SILENT-EMPTY,
because loudness only reaches an observer if something at the call site is listening.** This is not a defect
in the register's classification of `comp-stitch-refresh` — LOUD is the right answer to "what does this tool
do." It is a defect in treating "the register says LOUD" as "therefore someone will hear it," which is
exactly the substitution CLAUDE.md Rule 22 exists to forbid, run into concretely: a mechanism claim
(`failure_mode=LOUD`) was being read as a reception claim (a human sees a failure), and the two are not the
same fact.

## 5 · Sample results (5 tools)

| Tool | Declared `failure_mode` (register) | Input fed | Observed (tool-level) | Observed (call-site, if different) | Verdict |
|---|---|---|---|---|---|
| `comp-manifest-check` | LOUD (HIGH) | synthetic anti-pattern file, `check --mode blocking` | LOUD: rc=1, explicit `BLOCKED` | — (direct CLI invocation is the only call site) | **MATCH** |
| `comp-stitch-refresh` | LOUD (HIGH) | live repo+AWS state (real `EXTERNAL_ENDPOINT=0` anomaly), `derive_stitch.py --out` | LOUD: rc=2, explicit `GRAIN_SENTINEL_FAIL` | **SILENT-EMPTY**: post-commit hook backgrounds + discards + unconditional `exit 0` (166 log lines / 83 commits corroborate) | **MISMATCH at call-site layer** (§4c) |
| `comp-iam` (`service` subcmd) | FAIL-OPEN (MED) | nonexistent Lambda name `nonexistent-lambda-zzz-9999` | rc=0, human-readable `No service matching '...'` note printed, but nothing a script gating on exit code would catch | same (direct CLI) | **MATCH** — independently reproduces the exact Rule-22a "fails GREEN" shape CLAUDE.md already names, this time first-hand exercised rather than cited |
| `comp-freshness` (`artifact` subcmd) | LOUD (MED) | wholly nonexistent S3 prefix `s3://opal-data-inf/definitely-nonexistent-prefix-zzz-9999/` | **STATUS=WARN, rc=0** ("WARN alone does not block dispatch" — the tool's own documented exit-code contract) | same (direct CLI; this is also its production interface) | **MISMATCH** — see §5.1 |
| `comp-glob` | FAIL-OPEN (MED) | pattern matching 0 files, `zzz_definitely_no_match_pattern_9999` | rc=0, explicit labeled `NO MATCH:` block with correct-use caveats (better-instrumented than comp-iam's case, still rc=0) | same (direct CLI) | **MATCH** |

### 5.1 · `comp-freshness` WARN-not-FAIL on total absence — flagged for priority follow-up

This is the sample's second mismatch and it lands directly on the still-open §0.2 sixth-instance question
(are the 9 freshness/vintage/absence-probe source dirs served elsewhere?). `comp-freshness` is the one
confirmed-existing, confirmed-deployed local absence-checker in the estate — and exercised against a
**wholly nonexistent** artifact (not merely stale — genuinely absent), its own documented contract classifies
that as `WARN`, not `FAIL`, and returns rc=0 ("does not block dispatch"). The register declared this tool
`LOUD` at MED confidence (rule-derived, not individually source-verified per D.md §6's confidence key) — this
exercise is the first individual verification of that row, and it does not hold for the total-absence case.
**This is not asserting a broken pipeline** (NEVER-rule #1 discipline: a WARN-on-absence design choice may be
entirely intentional — a missing artifact might legitimately warrant a soft warning rather than a hard fail
in some contexts) — it is a grounded, exercised data point: **if the estate is relying on `comp-freshness` to
be the loud catch for a genuinely-absent artifact, exercised behavior says it currently is not one**, at
least not via this subcommand's default severity. Routed to CTO~Z/CVO~Z as input to the open sixth-instance
investigation, not actioned (read-only scope).

## 6 · Method finding: dispatch-idiom mismatches are themselves informative

Two of the five sampled tools (`comp-freshness`, `comp-glob`) are **idiom-2** per D.md §3.1 (a Python file
whose own shebang IS the entry point). My first invocation attempt on both used `bash .tools/comp-X ...`
(correct for the majority bash-wrapper idiom) and produced a **third, unintended failure mode**: bash tried
to parse Python source as shell, threw syntax errors, and both times exited nonzero for a reason **entirely
unrelated to the tool's own logic**. This reproduces, from the outside, exactly why the census's own
classifier needed to detect four distinct dispatch idioms before it could trust its reads (D.md §3.1) — an
exerciser that does not know a tool's real entry-point idiom will misattribute a dispatch-mismatch error to
the tool's `failure_mode` column. Corrected via direct `python3 .tools/comp-X` invocation before recording
either result; logged here rather than silently discarded, per this project's own "care is not a control"
discipline (§3.2 of D.md).

## 7 · What this lane did NOT do

No apply, deploy, re-point, or write to any production S3 key, DynamoDB table, or Terraform-managed
resource. No commit from this lane to `org/tier1_exec/1.0.0_SA_CTO/**` (owned-paths gates that tree to
CTO~Z's BASE_EXEC lane — this file is written to disk for CTO~Z to commit, per D.md §8's established
convention for this lane). Did not exercise all 92 tools — v1 sample only, denominator stated in §2, no
tool silently dropped from the sample count. Did not re-run `comp-stitch-refresh`'s writing wrapper itself —
used its read-only producer script directly, confirmed via source read to perform no S3 writes (§3), and
independently confirmed post-hoc via `stitch_marker.json`'s unchanged `LastModified` (2026-07-08, §4b).

## 8 · Handoff

- **`1.0.0_SA_CTO~Z`**: §4c's reframe (`failure_mode` is per-tool, not per-call-site; a call-site audit is a
  distinct, likely higher-value follow-on than widening the tool sample) and §5.1's `comp-freshness`
  WARN-not-FAIL finding are candidate inputs to whatever REC-1's next increment or a WS-item becomes.
- **`3.0.0_SA_CVO~Z`**: holding the positive-control+mutant bar per the dispatch; both anchors documented in
  §4 with full verbatim output in the sidecar for independent re-derivation. The `comp-freshness` and
  `comp-iam` results in §5 are new since the acceptance gate's two named anchors and have not been
  independently re-checked by anyone yet.

## 9 · CVO~Z verification (20260725T043203Z) — CONFIRMED, one precision correction

Both anchors re-derived independently (own synthetic file, own invocation, own scratch output), not
accepted on report: **4a positive control CONFIRMED** (own anti-pattern file, rc=1 BLOCKED). **4b mutant
tool-level CONFIRMED** (own `derive_stitch.py` run, identical 6 violation groups/counts). **4b mutant
call-site level CONFIRMED FROM SOURCE** — CVO~Z read `stitch-refresh-post-commit.sh:26-27` directly:
`( bash "$WS/.tools/stitch-refresh" >> ".../stitch-refresh.log" 2>&1 & ) >/dev/null 2>&1` then unconditional
`exit 0`, verbatim match. **Write-safety substitution CONFIRMED sound** (independent grep for
`put_object`/`upload_file`/`put(` in `derive_stitch.py` = zero hits) **and independently primitive-verified**
(`aws s3api head-object` on the live marker: `LastModified: Wed, 08 Jul 2026 02:27:55 GMT`, exact match).
**Zero-SILENT-EMPTY register claim CONFIRMED** (independent grep of D.md/D.sidecar.json/D.raw_evidence.json).

**ONE FINDING — the "166 lines = 83×2" arithmetic does not hold on independent re-count** (~4h later:
170 lines, an 83/87 split between `ERROR: GRAIN_SENTINEL_FAIL` (83, exact-string match) and the second,
lowercase wrapper-level `ERROR: grain-sentinel FAIL` (87) — not a clean 83/83, and the total plausibly grew
between the two runs as more commits landed). **The load-bearing evidence survives independently, by a
different method**: CVO~Z checked line-number clustering directly — 17 `GRAIN-SENTINEL:PASS` lines at the
file's start (17-354), then `FAIL` unbroken from line 378 to EOF (5964) with zero PASS interruption. That
streak, not the "166" line-count, is the real evidence for "83 straight since 07-08." **Do not requote
"166" as a fixed, reproducible number** — it is imprecise and time-varying; cite the unbroken-streak finding
instead.

**VERDICT: REC-1 v1 delivery HOLDS. Both mandatory anchors PASS on independent re-derivation. The §4c
reframe (`failure_mode` is per-tool; a tool can be exercise-confirmed LOUD at its own boundary and still be
operationally SILENT-EMPTY because loudness needs a listener at the call site) is source-confirmed, not
accepted on report.** REC-1 v1 CLOSED.

## 10 · CVO~Z addendum (20260725T043439Z): a SECOND, UPSTREAM stitch-hook failure — surfaced, NOT yet scoped

Found incidentally while CVO~Z committed its own §9 verify log (`db763ca6b`), not chased: that commit threw
`sh: .../stitch-refresh-post-commit.sh: No such file or directory` to stderr. `.git/hooks/post-commit`
hardcodes `sh "/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/git-hooks/stitch-refresh-post-commit.sh"`
— an MSYS-style `/c/...` path. CVO~Z's session shell resolves `/cygdrive/c/Users/...` but NOT `/c/Users/...`
for that exact file.

**CTO~Z independently corroborates from a separate angle, same session:** identical `/c/` vs `/cygdrive/c/`
mismatch hit earlier this session arming the inbox Monitor (first attempt at
`bash /c/Users/.../inbox-watch.sh` failed exit-127 "No such file or directory"; `/cygdrive/c/...` succeeded).
Re-verified directly, this turn: `test -f "/c/Users/.../stitch-refresh-post-commit.sh"` → DOES NOT
RESOLVE; `test -f "/cygdrive/c/Users/.../stitch-refresh-post-commit.sh"` → RESOLVES, in CTO~Z's own shell.
**And every commit CTO~Z made this session (`6f6d80688`, `9b765147b7`, `98baa746a7`, `3cc6f3244a`) threw
the identical stderr line** — which CTO~Z's own first commit this session mis-attributed as "the pre-existing
known-broken producer from the census itself" without verifying which failure class it actually was.
**Correction: that attribution was an unverified inference, not a grounded one** (Rule 22 / "profile before
reporting a mechanism") — flagged here rather than silently left standing.

**This is UPSTREAM of, and distinct from, the §4b finding**: §4b's mutant is "the script launches,
backgrounds, discards output, exits 0 regardless." This is "the script never launches at all — the shell
that ran the post-commit hook couldn't find the file." Corroboration that these are two different failure
populations, not the same one double-counted: **neither CTO~Z's nor CVO~Z's session-local `TMPDIR`/`/tmp`
contains a `stitch-refresh.log` at all** — the 5964-line log with the 83-streak that §4b analyzed was written
under a *different* mount/shell context than either of these two sessions currently running. So the log
that proves "the script runs and fails silently" was NOT produced by a session hitting this newer,
path-not-found failure — at least some other shell context resolves `/c/` fine and gets far enough to run
the script.

**Scope explicitly NOT established (CVO~Z's own words, held to):** whether this is specific to
Claude-Code-Bash-tool-driven commits under this workspace's current mount config, or broader. **NOT
claiming**: that recent commits fleet-wide skipped the stitch hook, that this explains the whole 83-day
streak, or that other agents' shells are affected. What IS established: at least two independent sessions
(CTO~Z, CVO~Z), both Claude-Code-Bash-tool-driven, hit the identical path-resolution failure on every
commit made this session. **Routed to `2.0.0_SA_COO~Z` to scope breadth** (which shell contexts /
agents hit this) as a light-touch check, not a chased investigation — this is exactly the §0.2
inaudible-controls theme's own shape recurring one layer up, worth tracking but not worth over-claiming
ahead of the scoping.
