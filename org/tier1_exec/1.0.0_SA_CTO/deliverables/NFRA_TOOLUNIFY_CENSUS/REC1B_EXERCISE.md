# NFRA_TOOLUNIFY REC-1b — Widen by Criticality (GATE-BLOCKING/PRODUCER exhaustive, rest sampled)

**author:** `0.8.0_AE_CloudComp~D` · 2026-07-25 · **status:** DELIVERED + CVO~Z-VERIFIED, closed
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY (off-main-fabric census group)
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T050449Z, "DISPATCH NFRA_TOOLUNIFY REC-1b — widen by criticality"
**builds on:** `REC1_EXERCISE.md` (same directory) — v1 sample, positive control + mutant already
gate-verified there; this pass widens using the register's own `role_flags[]` as the filter.
**sidecar:** `REC1B_EXERCISE.sidecar.json` (this directory).

---

## 1 · Denominator (printed per dispatch instruction)

Parsed all 92 rows of `D.md`'s register table programmatically (not by eye) for `role_flags`:

| Category | Count | Tools |
|---|---|---|
| `GATE-BLOCKING` confirmed (no `?`) | **1** | `comp-manifest-check` |
| `GATE-BLOCKING?` candidate | 8 | `comp-coverage-check`, `comp-denytest`, `comp-denytest.py`, `comp-kit-striplist-gate`, `comp-routable-check`, `comp-surface-check`, `comp-tool-health-gate`, `comp-validate` |
| `PRODUCER` confirmed (no `?`) | **1** | `comp-stitch-refresh` |
| `PRODUCER?` candidate | 56 | (61% of the register — see D.md, most tools that write anything at all default to the `?`-suffixed candidate unless individually source-verified) |
| `ADVISORY` | 28 | |
| `CONFIG`-only | 1 | `comp-to` |

**Union of CONFIRMED (non-`?`) `GATE-BLOCKING` or `PRODUCER`, deduplicated: exactly 2 tools —
`comp-manifest-check` and `comp-stitch-refresh`.** Both were already exercised, gate-verified, and reported
in REC-1 (positive control and mutant respectively) — **the exhaustive confirmed-criticality pass is
therefore already 100% complete (2/2) as of REC-1; this deliverable does not re-run them** (their results
are cited, not repeated, in §2 below) and instead spends this pass on (a) the candidate-flagged tier the
dispatch specifically asked me to re-confirm against the six through-line instances, and (b) a further
sample of the ADVISORY/LOW-confidence tier.

**New this pass:** 3 tools, 5 invocations (`comp-gitdrill` self-test + mismatched-target;
`comp-surface-check scan` against a missing input + an empty/degenerate input; `comp-dispatch` against a
nonexistent firm alias). **Cumulative across REC-1 + REC-1b: 8 distinct tools exercised of 92 (~9%).**

## 2 · Exhaustive confirmed set — status carried forward, not re-run

| Tool | role_flags | Declared `failure_mode` | REC-1 result | Carried verdict |
|---|---|---|---|---|
| `comp-manifest-check` | `GATE-BLOCKING` | LOUD (HIGH) | Positive control: LOUD, rc=1, `BLOCKED` (REC1_EXERCISE.md §4a) | MATCH |
| `comp-stitch-refresh` | `PRODUCER` | LOUD (HIGH) | Mutant: LOUD at tool level (rc=2), **SILENT-EMPTY at call site** (REC1_EXERCISE.md §4b/§4c) | MATCH at tool level, **MISMATCH at call-site level (headline finding)** |

No new exercise needed to satisfy "exhaustive over the confirmed set" — it was already exhaustive by
construction the moment the denominator was counted (2 tools, 2 already done).

## 3 · Re-confirming the six through-line instances against the role_flags filter (dispatch's specific ask)

**Only 3 of the six §0.2 through-line instances are representable as rows in the 92-tool register at all**
(`opal-critical-surface-alerts`, `ms_heat`, `mdpf-daily`, and the 9 undeployed guard dirs are AWS/CI
resources, not `comp-*` tools — they have no register row to carry a `role_flags` value in the first place).
Of the 3 that are:

| Through-line instance | Register row | `role_flags` | Confirmed or candidate? |
|---|---|---|---|
| #1 "stitch 83d-silent" | `comp-stitch-refresh` | `PRODUCER` | **Confirmed** — caught by the filter |
| #5a "two raw-cache readers" (fixed 68bbf3dd2) | `comp-gitdrill` | `PRODUCER?` | **Candidate only** — filter misses it |
| #5b "two raw-cache readers" (fixed 68bbf3dd2) | `comp-surface-check` | `GATE-BLOCKING?,PRODUCER?` | **Candidate only** — filter misses it |

**This is the exact under-catch the dispatch asked me to check for, and it is real: a strict
confirmed-only `role_flags` filter catches 1 of the 3 register-representable through-line instances and
misses the other 2.** Both misses are `?`-suffixed not because the census under-investigated them — they
are two of the four acceptance-gate cases and one held-out self-check target, all HIGH/MED confidence,
individually source-read — but because `role_flags` for a read-heavy tool with a narrow secondary write
path (both tools' primary mode is read; the write/gate behavior is real but not their headline function) was
conservatively left as a plausibility candidate rather than a hard confirmation. **`role_flags` confidence and
`failure_mode` confidence are two different axes; a HIGH-confidence `failure_mode` row can still carry a
`?`-suffixed `role_flags`.** Recommend to CTO~Z/CVO~Z: if the register's `role_flags` confirmation bar is
meant to gate future exhaustive-criticality passes like this one, it should be revisited for tools with a
real but secondary write/gate path — a purely mechanical filter on the `?` suffix will keep missing this
exact shape.

## 4 · New exercises this pass

### 4a · `comp-gitdrill` (candidate `PRODUCER?`, through-line #5a, fixed 2026-07-24)

`--self-test` (built-in, no live args needed): **6/6 PASS**, including `resolve.miss_is_empty` (empty-input
handling is itself tested) and `at.blob_parity_with_git` (the exact vintage-guard property the fix landed —
gitdrill's resolved blob SHA matches git's own, confirming the fix holds under self-test). `RC=0`.

Mismatched-target probe (`comp-gitdrill definitely_nonexistent_node_zzz_9999`):
```
NOT-RESOLVED: 'definitely_nonexistent_node_zzz_9999' is neither a repo path, a graph node with a
file_path, nor a git-tracked basename. (comp-gitdrill drills a PRODUCER file's history; a pure S3
artifact with no source file has no git axis -- try comp-icedrill for its vintages.)
RC=3
```
**VERDICT: LOUD** (explicit, informative, even redirects to the correct alternative tool). **Matches
DECLARED LOUD (MED confidence).** The 2026-07-24 vintage-guard fix appears to hold under both a built-in
self-test and a fresh mismatched-input probe — no regression found.

### 4b · `comp-surface-check scan` (candidate `GATE-BLOCKING?,PRODUCER?`, through-line #5b, fixed 2026-07-24)

Two distinct mismatched/empty inputs, since they produced genuinely different — and both informative —
results:

**Missing `--current` file** (`scan --current <nonexistent path>`):
```
ADVISORY: comp-surface-check scan could not load inputs (FileNotFoundError: ...) -- skipping
(never crash the nightly).
RC=0
```
**VERDICT: FAIL-OPEN, by explicit design** ("never crash the nightly" is a comment in the tool's own output,
not my inference). **This is a MISMATCH against the register's DECLARED LOUD (MED confidence).** On the
specific failure shape of "the current graph snapshot is simply absent" — a plausible real failure (a prior
step failed to write it, disk full, wrong path) — the tool does not error; it prints one ADVISORY line and
exits 0 with **zero SEV1/SEV2 findings emitted**, indistinguishable in an unattended nightly log stream from
"ran clean, zero drift found" unless something specifically greps for the word `ADVISORY`.

**Empty/degenerate `--current`** (`scan --current <file containing {}>`, 0 nodes vs. 2139-node baseline):
```
node delta: +0 / -2139 / ~0
SEV1 [PAGE]: REMOVED node in model_portfolios.headline -> component:...
  (21 SEV1/SEV2 lines total, all real critical-surface pages: ModelPortfolios, AdvisorIntelligence)
Layer-2 (file-SHA-watch): 13 SEV1/SEV2 CHANGED lines
RC=0
```
**VERDICT: this IS loud in substance** — comprehensive, correctly severity-tagged, names real pages — but
`RC=0` regardless. **This is NOT a mismatch once traced to source**: per the 68bbf3dd2 fix commit's own
correction note, `scan` is the ADVISORY nightly drift report; the actual BLOCKING gate
(**`cmd_check`, `surface_check_cli.py:248`** — CVO~Z's source-trace correction; `cmd_selfcheck` at line 577
is a self-test/demo harness that internally calls `cmd_check` with synthetic fixtures, not the production
path, confirmed live via `.tools/safe-commit.sh:455`) is a **separate code path that does not read
`graph.json` at all** — it reads `critical-surfaces.yaml` directly via `load_surfaces()`. `scan`'s job was
never to block, so `rc=0` here is correct-by-design, not a silent failure. Recorded to avoid over-reading a second "LOUD-declared-but-rc=0" result the same way as
§4a's real mismatch — **the two rc=0 results in this section are NOT the same finding**: one is a genuine
declared-vs-observed gap (missing-input skip), the other is a declared-mode mismatch explained entirely by
`scan` vs `selfcheck` being different subcommands the register's single row conflates.

**This itself is worth naming as a register-shape finding**: `comp-surface-check` is ONE row in the D.md
register covering SEVEN subcommands (`check`, `scan`, `list-watched-files`, `egress-check`, `list`,
`selfcheck`, `contract-selfcheck`) with materially different failure semantics (blocking vs. advisory vs.
egress-audit) collapsed into a single `failure_mode` value. The missing-input FAIL-OPEN finding (§4b, first
result) is real and specific to `scan`; it should not be read as characterizing `selfcheck`'s behavior, which
this pass did not exercise.

### 4c · `comp-dispatch` (LOW-confidence `LOUD (default)` sample, ADVISORY tier)

`comp-dispatch definitely_nonexistent_firm_zzz_9999`:
```
comp-dispatch: no gold_dispatch.sh for 'definitely_nonexistent_firm_zzz_9999' (known firms:
['bd', 'black_diamond', 'cot', 'cottonwood', 'inf', 'inflection']; or pass a path)
RC=1
```
**VERDICT: LOUD. Matches DECLARED `LOUD (default)`, LOW confidence** — this is the first individual
verification of one of the 10 rows the register's own §7 finding #5 named as "could not be pinned by a
quick text scan," and it holds for this tool.

## 5 · Summary of this pass

| Tool | Declared | Observed | Verdict |
|---|---|---|---|
| `comp-gitdrill` (self-test) | LOUD (MED) | LOUD (6/6 PASS incl. vintage-parity) | MATCH |
| `comp-gitdrill` (mismatched target) | LOUD (MED) | LOUD (rc=3, explicit) | MATCH |
| `comp-surface-check scan` (missing input) | LOUD (MED) | **FAIL-OPEN by design** ("never crash the nightly") | **MISMATCH** |
| `comp-surface-check scan` (empty input) | LOUD (MED) | Loud in substance, rc=0 by design (advisory subcommand, not the blocking one) | Explained, not a defect — register-granularity finding (§4b) |
| `comp-dispatch` | LOUD (LOW/default) | LOUD (rc=1, explicit) | MATCH |

**Net new finding this pass:** `comp-surface-check scan`'s missing-input path is a genuine, exercised
FAIL-OPEN against a declared-LOUD row — a second concrete instance (after REC-1's `comp-freshness` result)
of the register's LOUD declaration not holding for the specific case of a **wholly absent** input, as
opposed to a merely malformed or stale one. Two independent tools, two independent absent-input tests, two
mismatches — this is now a pattern worth naming explicitly to CTO~Z/CVO~Z, not a one-off.

## 6 · Environment note (per CTO~Z's ask, unrelated to the register but requested this dispatch)

CTO~Z asked me to confirm the stitch post-commit hook's `/c/`-path fix (`fbc91c6e28`) on my next commit this
session. Result reported separately to `2.0.0_SA_COO~Z` at 20260725T0438Z (the relayed light-touch ask
arrived mid-session): my own commit `c3c68389b`, made **before** the fix landed, DID throw the
`No such file or directory` stderr on the hardcoded `/c/...` path in this Cygwin-shell session. The commit
carrying this deliverable (see session log) is made **after** `fbc91c6e28` and its result is reported in that
same log's Compiler Tools / Files Modified section — confirming or flagging per CTO~Z's instruction.

## 7 · What this lane did NOT do

No apply, deploy, re-point, or write to any production resource. No commit to
`org/tier1_exec/1.0.0_SA_CTO/**` (CTO~Z's BASE_EXEC lane, same convention as REC-1). Did not exercise
`comp-surface-check`'s other 6 subcommands (`check`, `list-watched-files`, `egress-check`, `list`,
`selfcheck`, `contract-selfcheck`) — flagged in §4b as a real gap in what one register row can represent,
not silently assumed identical to `scan`. Did not widen past the 3 new tools sampled this pass — the
exhaustive confirmed-criticality set (§2) is fully covered; further ADVISORY/candidate-tier sampling is
available on request but was not run without one, per this lane's light-cycle discipline.

## 8 · Handoff

- **`1.0.0_SA_CTO~Z`**: §3's under-catch finding (role_flags `?`-suffix conservatism can hide a real
  through-line instance from a criticality filter) and §5's `comp-surface-check scan` missing-input FAIL-OPEN
  are the two new decision-relevant items.
- **`3.0.0_SA_CVO~Z`**: exhaustive-confirmed-set claim (§2, 2/2) is mechanically re-derivable from the same
  parse script used to produce §1's table; happy to hand over the parse script itself if useful for your own
  re-run rather than trusting my counts.

## 9 · CVO~Z verification (20260725T051501Z) — CONFIRMED, one precision correction, one methodology finding UPHELD

Denominator + under-catch claim re-derived **from scratch, own parser, against `D.sidecar.json`'s raw `rows`
dict** (92 entries, matches) — not ~D's script, not ~D's parse. Real field values are
`PRODUCER-CANDIDATE`/`GATE-BLOCKING-CANDIDATE` (the `?`-suffix in this doc is presentational shorthand, not
a misrepresentation). **Confirmed-union CONFIRMED: exactly `{comp-manifest-check, comp-stitch-refresh}`,
count=2.**

**The under-catch claim — independently confirmed, holds, and CVO~Z frames it as no longer hypothetical:**
queried the 3 through-line-representable rows directly — `comp-stitch-refresh` → `role_flags=['PRODUCER']`
(confirmed); `comp-gitdrill` → `role_flags=['PRODUCER-CANDIDATE']` (candidate only); `comp-surface-check` →
`role_flags=['GATE-BLOCKING-CANDIDATE','PRODUCER-CANDIDATE']` (candidate only). Both misses carry
MEDIUM-confidence, individually-derived `failure_mode=LOUD` rows. **"This means the Q2 criticality-filter
methodology (confirmed-only role_flags as the widen-by-criticality gate) genuinely needs revisiting before
further widening... not just ~D's assertion, independently re-derived from the raw register."**

All 4 new exercises re-run independently (own invocations, own inputs) — **all reproduce exactly**:
`comp-gitdrill --self-test` (6/6, RC=0), `comp-gitdrill` mismatched target (NOT-RESOLVED, RC=3),
`comp-surface-check scan` on a missing file (FAIL-OPEN advisory, RC=0), `comp-surface-check scan` on an
empty-object file (21 real SEV1/SEV2 findings, RC=0).

**Precision correction (folded into §4b above):** ~D named `cmd_selfcheck` as the production blocking gate.
CVO~Z source-traced `surface_check_cli.py` directly — `cmd_selfcheck` (line 577) is a self-test/demo
harness, not what runs in production; the real gate is `cmd_check` (line 248), confirmed live via
`.tools/safe-commit.sh:455`. The SUBSTANCE of ~D's finding is unaffected (the real gate is still a separate
code path reading `critical-surfaces.yaml`, not `graph.json`) — only the named function was wrong.

**VERDICT: REC-1b holds. Both the denominator claim and the under-catch are independently confirmed from
the raw register, not accepted on report. All 4 new exercises reproduce exactly. CVO~Z's explicit
recommendation: act on the methodology-revisit — this is now twice independently confirmed, not
hypothetical.** REC-1b CLOSED.

**METHODOLOGY NOTE FOR ANY FUTURE WIDENING PASS (CTO~Z, carrying CVO~Z's recommendation forward):**
`role_flags` confirmation status and `failure_mode` confidence are demonstrated to be two different axes —
a HIGH/MED-confidence `failure_mode=LOUD` row can carry a `?`-suffixed (candidate-only) `role_flags`. A
future exhaustive-by-criticality pass should NOT filter on confirmed-only `role_flags` alone; it should
also sweep candidate-flagged tools whose `failure_mode` confidence is HIGH/MED. No further widening is
currently scoped (WS-4/WS-5 held per Andrew's ruling), so this is banked guidance for whenever that resumes,
not an action item today.
