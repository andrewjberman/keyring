# NFRA_TOOLUNIFY REC-1c LANE-E — Exercise Batch (16 tools, pipeline/frontend/misc)

**author:** `0.8.0_AE_CloudComp~E` · 2026-07-25 · **status:** DELIVERED
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY (off-main-fabric census group)
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T060511Z, "DISPATCH NFRA_TOOLUNIFY REC-1c LANE-E — exercise batch
(16 tools, pipeline/frontend/misc)"
**sidecar:** `REC1C_E.sidecar.json` (this directory) — per-invocation raw results, verbatim excerpts, true
exit codes, per-row write-safety notes.

> **Mutation-type labels here are PROVISIONAL, pending the L0b change-type vocabulary
> (IMPLEMENTATION_LEVELS_AND_SEQUENCING.md s4/L0b) — this sweep records candidate vocabulary, it does not
> settle it.**

---

## 1 · Denominator

**16 register rows dispatched → 15 distinct tools (the `comp-whoread` / `comp-whoread.py` pair is ONE tool
— wrapper is `exec python .tools/comp-whoread.py`, read at source this session, matching D.md:43's own
dedup note) → 15 of 15 distinct tools exercised, 0 skipped.** No UNTESTABLE-SAFELY rows: the two tools with
real write paths both had safe exercise routes (`comp-axes --no-snapshot` / delta-only; `comp-adapter-audit
--manifest-dir`, a flag the tool ships explicitly "for read-only exercise"). `comp-pipescript`'s
`io`/`postdeps` mutations are **cited** from CVO~Z's reground per the dispatch, not re-derived; its other
subcommands were exercised fresh (`deployed`, `chain`). One row (`comp-describe`) required an extended
latency budget — see §4.3.

## 2 · Harness + acceptance gate (run FIRST, separate invocations)

**This session's shell has a live harness hazard the gate was pointed at:** every Bash invocation in this
`/cygdrive`-mount Cygwin shell appends a spurious wrapper-level exit-1 (`claude-*-cwd: No such file or
directory`). An exerciser trusting the wrapper-reported exit code would read **every** tool as LOUD. All
exit codes in this deliverable are therefore captured **in-stdout** (`; echo TRUE_RC=$?` /
`${PIPESTATUS[0]}`) — control on the retrieval, not the pattern.

- **Positive control** (`comp-manifest-check check --file <synthetic anti-pattern> --mode blocking`):
  TRUE_RC=1, explicit `BLOCKED` → known-LOUD reads LOUD. **PASS.**
- **Harness mutant** (`comp-iam service nonexistent-lambda-zzz-9999`, REC-1-exercise-confirmed FAIL-OPEN):
  TRUE_RC=0 + human-readable note → known-FAIL-OPEN reads rc=0 **through the wrapper noise**. **PASS — the
  capture discriminates; the harness is not biased toward LOUD.**

## 3 · Results — 15 tools

| # | Tool | Declared (D.md) | Mutation fed | Observed (TRUE_RC) | Verdict |
|---|---|---|---|---|---|
| 1 | `comp-pipescript` (io/postdeps) | LOUD (MED) | — cited, CVO~Z reground §6 | io: loud-text @ rc=0; postdeps: **affirmative-sounding negative** @ rc=0; oos-guard rc=2 | **MISMATCH (cited)** |
| 1 | `comp-pipescript deployed` | LOUD (MED) | NONEXISTENT script filter | all-zeros summary + "No scripts matched" @ **rc=0** | **MISMATCH — FAIL-OPEN** |
| 1 | `comp-pipescript chain` | LOUD (MED) | NONEXISTENT chain | "Unknown chain" + valid list @ rc=1 | MATCH |
| 2 | `comp-chainrun diff` | LOUD (MED) | NONEXISTENT snapshot files | unhandled `FileNotFoundError` traceback @ rc=1 | MATCH (LOUD-by-crash) |
| 3 | `comp-incrparity` | LOUD (MED) | NONEXISTENT script id, both entry layers | agent entry: `BLOCKED` @ rc=3 (stale hold, §4.2); semantic path: `PARITY UNVERIFIED… NOT a pass` @ rc=2 | **MATCH — best-instrumented in batch** |
| 4 | `comp-trigger` | FAIL-OPEN (MED) | NONEXISTENT rule/ARN substring | `NO MATCH… not proof no trigger exists` + denominator @ rc=0 | MATCH (disclosed FAIL-OPEN) |
| 5 | `comp-transform schema-check` | LOUD (MED) | NONEXISTENT component | `Component not found` @ rc=1 | MATCH |
| 6 | `comp-tooltip` | LOUD (MED) | MALFORMED ext: UNKNOWN-SUBCOMMAND | usage text @ rc=1 | MATCH |
| 7 | `comp-types blast` | LOUD (MED) | NONEXISTENT type | `Blast radius: 0 file(s)… PASS` @ **rc=0** + silent local manifest write | **MISMATCH — affirmative FAIL-OPEN (§4.1)** |
| 8 | `comp-cache key` | LOUD-default (LOW) | NONEXISTENT key substring | `0 hit(s)` + denominator + scope caveat @ **rc=0** | **MISMATCH (disclosed)** — first individual verification of a LOW row |
| 9 | `comp-perf vectorize-audit` | LOUD (MED) | NONEXISTENT gold script | `ERROR: script … not found` @ rc=1 | MATCH |
| 10 | `comp-pulse diff` | FAIL-OPEN (MED) | NONEXISTENT file path | `REFLEX CLEAN — a MEASURED result` @ rc=0 **on a file that does not exist** | MATCH (self-cert nuance, §4.4) |
| 11 | `comp-describe` | LOUD (MED) | NONEXISTENT resource | `did NOT resolve… (Broken retrieval != absent resource.)` @ rc=1, after 2×180s comp-kuzu timeouts | MATCH (latency + confound, §4.3) |
| 12 | `comp-axes` | LOUD (MED) | NONEXISTENT axis (`--no-snapshot`) | `ERROR: unknown axes… known: […]` @ rc=2 | MATCH |
| 13 | `comp-adapter-audit` | FAIL-OPEN (MED) | NONEXISTENT adapter fn (scratch `--manifest-dir`) | `ERROR… could not locate the adapter` @ rc=1 | **MISMATCH — good direction (tool better than register)** |
| 14 | `comp-v5-composite-test.sh` | LOUD (MED) | MALFORMED ext: MALFORMED-ENVIRONMENT (bare `comp-X` names, `.tools` off PATH) | `0 pass, 8 fail` @ rc=8; command-not-found NOT swallowed | MATCH |
| 15 | `comp-whoread` (+`.py`, dedup) | LOUD (MED) | NONEXISTENT bucket | `CANNOT ANSWER… Failing closed (rc=1) rather than reporting a false clean` | **MATCH — exemplary** |

**Score vs register (15 distinct tools): 11 MATCH · 4 MISMATCH-bearing tools** (`comp-pipescript` — the
`deployed` exercise plus the cited `postdeps`/`io` results; `comp-types`; `comp-cache`;
`comp-adapter-audit`). Three of the four are declared-LOUD rows observed FAIL-OPEN on the exercised
subcommand; one is the inverse (declared FAIL-OPEN, observed LOUD). Zero UNKNOWN rows; zero skips.

## 4 · Findings

### 4.1 · The affirmative-PASS shape — `comp-types blast` is this batch's sharpest instance

A NONEXISTENT type returns rc=0, "Blast radius: 0 file(s)", and an explicit **"PASS: comp-types blast
complete"**. A nonexistent type is byte-indistinguishable from a real type with zero consumers — so a
typo'd type name in a pre-shape-change blast check reads as **"safe to change."** This is one step worse
than the REC-1/1b "total-absence FAIL-OPEN" pattern (comp-freshness, comp-surface-check scan,
comp-pipescript postdeps): those return a *neutral* empty; this one **stamps an affirmative verdict on the
absence**. Candidate sub-vocabulary for L0b: FAIL-OPEN-NEUTRAL vs **FAIL-OPEN-AFFIRMATIVE**. It also
silently writes a manifest into the repo tree (`types-index/<garbage>.blast.yaml`) on a pure query — probe
debris removed this session; pre-existing untracked manifests from prior sessions left in place, noted for
CTO~Z (the `types-index/` dir accumulates untracked files).

### 4.2 · `comp-incrparity`'s agent gate enforces a hold Andrew LIFTED — a live stale-guard

The agent-entry gate (incrparity_cli.py:108-117) rc=3-BLOCKs on "the sovereign hold" over `opal-data-bd`
reads — the 49F/Schwab/bd block **lifted completely, Andrew-direct 2026-07-14**
([[project_49f_bd_scope_parked_and_the_retracted_a00_carveout]]). The retraction never propagated to this
enforcing copy — exactly the "a retracted prohibition is only as dead as its last-surviving copy" class
(VERIFICATION LAW 8). The gate itself is well-built (fail-closed, distinct exit code, designed override) —
it is the *predicate* that is stale. **Surfaced for CTO~Z routing, not fixed (read-only scope).** Behind
the gate, the tool is the batch's best-instrumented: unknown id → rc=2 `PARITY UNVERIFIED … NOT a pass`.

### 4.3 · `comp-describe` — LOUD MATCH on the verdict; latency is the operational concern

Final: **rc=1, LOUD, MATCH** — explicit `did NOT resolve`, both underlying comp-kuzu failures printed to
stderr, and the exact right epistemic caveat (`Broken retrieval != absent resource.`) plus a refresh hint.
Two operational nuances, disclosed with their confound:
- **Latency:** the first invocation produced **zero output inside a 2m budget** (unconfounded fact); the
  completed retry took ~7.5m wall, driven by two 180s comp-kuzu timeouts. **Confound disclosed:** the first
  attempt's python worker **survived the 2m wrapper kill** and overlapped the retry for ~2min (reaped by
  this lane) — the retry's kuzu timeouts may be self-inflicted lock contention, so do NOT quote 7.5m as
  clean single-invocation latency. Either way, a describe surface that cannot answer a nonexistent name
  inside 2m is operationally out of interactive reach, and its `--help`'s "0 matches -> comp-kuzu-inc
  refresh hint" contract sits behind that wall.
- **The 0-matches line is derived from FAILED retrievals** and the tool says so — loud and honest — but a
  consumer parsing only the verdict line inherits a broken-retrieval zero.
- Secondary, environment-class: the 2m timeout killed the bash wrapper but **the python worker kept
  deriving** — the detached-child-survives-the-kill shape the fabric already banked for
  `TaskStop`/watchers, reproduced on a comp tool.

### 4.4 · `comp-pulse diff` self-certifies "MEASURED" on a nonexistent file

Register-level MATCH (FAIL-OPEN as declared), but it prints `REFLEX CLEAN -- a MEASURED result (map read,
every file checked), not a default.` for a path that does not exist. The membership test is well-defined on
a nonexistent path, so the sentence is not technically false — but the "MEASURED, not a default" language
is exactly the self-certification an instrument uses to *end* inspection, and it does not discriminate
can't-read-input from read-and-clean (VERIFICATION LAW 5 shape). Candidate register nuance rather than a
defect claim.

### 4.5 · Per-subcommand heterogeneity, third confirmation

`comp-pipescript` is now the third multi-subcommand tool (after REC-1b's `comp-surface-check`, and the
seven-subcommand point made there) where one register `failure_mode` value cannot represent the surface:
`chain` LOUD / `deployed` FAIL-OPEN / `io` loud-text-rc0 / `postdeps` affirmative-negative-rc0. The
mismatch rate concentrates on exactly the subcommands that sit in operational pre-run checklists
(`deployed` is the XXX.md AE minimum before every gold-run trigger; `postdeps` is the Rule-13 pre-ad-hoc
check) — the loud subcommands are the informational ones, the quiet ones are the gates.

### 4.6 · Good-direction mismatches exist too

`comp-adapter-audit` (declared FAIL-OPEN) is loud (rc=1, double ERROR) on a nonexistent adapter — and ships
its own `--manifest-dir` flag documented "for read-only exercise," the only tool in the batch that
anticipates being exercised. The register under-sells it. Mismatch handling should not presume drift is
always in the dangerous direction.

## 5 · What this lane did NOT do

No production S3/DDB write, no terraform, no commit to `org/tier1_exec/**` (this file + sidecar are on disk
for CTO~Z to commit, per the lane convention). No PATH-carrying re-run of `comp-v5-composite-test.sh` (its
8/8 scenario failures here are environment-dispatch results, NOT estate state — do not read §3 row 14 as a
regression signal). No fix to the comp-incrparity stale hold, the comp-types affirmative-PASS, or the
types-index untracked accumulation — all routed as findings. `comp-whoread.py` not separately invoked
(source-confirmed same tool; a second identical invocation adds noise, not information). io/postdeps
mutations for comp-pipescript cited from `cvoz_NFRA_TOOLARCH_CANON_REGROUND_20260724.md` §6, not re-derived.

## 6 · Handoff

- **`1.0.0_SA_CTO~Z`**: commit this + sidecar; route §4.2 (stale hold predicate — one-line fix candidate,
  needs your call given the tool guards a bd read) and §4.1 (FAIL-OPEN-AFFIRMATIVE as an L0b candidate
  sub-class; comp-types is now the named exemplar). The §4.5 concentration (quiet subcommands = the gate
  subcommands) may deserve its own register dimension ahead of the L0b vocabulary.
- **`3.0.0_SA_CVO~Z`**: every row re-derivable from the sidecar's verbatim invocations; the acceptance-gate
  pair (§2) is the harness-validity anchor — note the in-stdout RC-capture rationale before re-running in a
  shell with the same wrapper artifact.
