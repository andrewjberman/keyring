# NFRA_TOOLUNIFY REC-1c LANE-base — 17-Tool Exercise Batch (Iceberg/Nessie-substrate-affinity)

**author:** `0.8.0_AE_CloudComp` (base) · 2026-07-25 · **status:** DELIVERED + CVO~Z-VERIFIED (20/20 rows
re-derived clean except one evidence-label defect, corrected — see §3.4's `comp-learns-status` note)
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY (off-main-fabric census group)
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T060145Z, "DISPATCH NFRA_TOOLUNIFY REC-1c LANE-base — exercise batch
(17 tools) + your census lane's open item"
**addendum folded in:** `1.0.0_SA_CTO~Z`, 20260725T060426Z, "ADDENDUM to REC-1c (all lanes, same text):
label your mutation types, provisional pending L0b"
**builds on:** `REC1_EXERCISE.md` + `REC1B_EXERCISE.md` (same directory, authored by `~D`) — same method,
same register (`D.md`), same acceptance-gate discipline. This is a distinct lane (base, not `~D`) working a
distinct tool batch assigned by name in the dispatch.
**sidecar:** `REC1C_base.sidecar.json` (this directory) — per-invocation raw stdout/stderr, exit codes, and
the mutation-type label for every row.

> **Mutation-type labels here are PROVISIONAL, pending the L0b change-type vocabulary
> (IMPLEMENTATION_LEVELS_AND_SEQUENCING.md §4/L0b) — this sweep records candidate vocabulary, it does not
> settle it.** (Per the 060426Z addendum, verbatim requirement.)

---

## 1 · Mission recap

Same as REC-1/REC-1b: feed each assigned tool a mismatched/stale/empty/nonexistent input, record the
OBSERVED failure_mode verdict (LOUD / FAIL-OPEN / SILENT-EMPTY / **UNKNOWN**), and compare to the register's
DECLARED value. **UNKNOWN is carried as first-class per the addendum** — "could not synthesize a safe bad
input" or "could not complete within budget" is recorded as UNKNOWN, never silently dropped and never folded
into MATCH.

## 2 · Denominator

**17 tools assigned. 9 fully exercised to a MATCH/MISMATCH verdict via an external mismatched input
(11 invocations — 2 tools got 2 invocations each: `comp-heat`, `comp-state`'s filter half doesn't count
here, see below). 2 tools partially exercised via their own built-in self-test only, not an external
mismatched input (`comp-learns-score`, `comp-state`'s self-test half; `comp-passcraft` got BOTH an external
EMPTY-input exercise AND a corroborating self-test). 1 tool UNTESTABLE-SAFELY on operational-discipline
grounds, not attempted for real (`comp-kuzu-full` — see §3.1). 4 tools hit a hard TIMEOUT under confirmed
live multi-lane contention on the shared Kuzu DB / KUZU-CANONICAL-touching substrate, not completed within
budget despite a 240s allowance (`comp-kuzu` bare/auto, `comp-kuzu-inc`, `comp-canon-motif`, `comp-cluster`
— see §3.1/§3.2). 1 tool has no caller-supplied-target CLI surface at all, so "mismatched input" does not
apply in the same shape, and its one applicable self-test exceeded budget uncompleted (`comp-system`).**

No tool silently dropped from the count: 17 rows appear in §5's table, each with an explicit verdict
including UNTESTABLE-SAFELY / TIMEOUT / UNKNOWN where that is the honest answer.

### 2.1 · Why not more per tool

Per this lane's own light-cycle discipline (`prompt.md` §1) and REC-1/1b's established one-manual-pass-per-
tool depth: one representative mismatched invocation per tool (two for `comp-heat` and `comp-passcraft`,
where the first probe didn't fairly test the declared property — see §5 notes), not a scripted sweep of
every subcommand × every mutation type. `comp-surface-check`'s 7-subcommand-in-1-row problem (REC-1b §4b) is
the documented precedent for why register-row-granularity, not exhaustiveness-per-tool, is this pass's scope.

## 3 · Method notes (new this pass, distinct from REC-1/1b's findings)

### 3.1 · `comp-kuzu` (bare/auto) and `comp-kuzu-full`: UNTESTABLE-SAFELY, not a silent skip

`.tools/comp-kuzu-full`'s own header is explicit and CTO arch-gated: *"0.0.0_AB_MSTR owns this AT STARTUP...
Every OTHER agent uses comp-kuzu-inc, NEVER a full mid-session (the ~482s ambush the split removes)... The
full rebuild runs even when the local pin already reads current (force=True)."* A non-MSTR lane invoking
this tool for real forces an unconditional ~482s exclusive rebuild against a standing NFRA_KUZUSPLIT
discipline — I did not run it beyond `--help` (argparse exits before touching the DB, confirmed safe).
**Verdict: UNTESTABLE-SAFELY**, source-cited, not exercised.

`comp-kuzu` bare (mode=`auto`) has the same underlying risk one level removed — `auto` internally picks
full-vs-incremental by delta size, and the wrapper comment does not guarantee a non-MSTR-safe outcome the
way `comp-kuzu-inc`'s wrapper explicitly does ("NEVER a mid-task full rebuild... this is the DEFAULT every
non-MSTR agent uses" is `comp-kuzu-inc`'s language, not `comp-kuzu`'s). I attempted it anyway (§3.2) and it
timed out at 240s without resolving — consistent with, not contradicting, the concern.

### 3.2 · `comp-kuzu-inc` and `comp-cluster`: TIMEOUT under confirmed live contention, not a tool defect claim

Both were fed a genuinely mismatched/nonexistent input and given 240s (4x this lane's other per-tool
budgets) — neither returned. **This was independently corroborated as fleet contention, not silently
assumed:** `ps -ef` during the wait showed three OTHER live `kuzu_cli.py` processes running concurrent
Cypher queries against the same local Kuzu DB (PIDs 159518/163569/167592, none started by this session),
consistent with sibling lanes (`~A`/`~B`/`~D`/`~E`, named in the same 060426Z addendum as receiving this
same batch dispatch) hitting the identical shared substrate at the identical time as this pass. `comp-kuzu`'s
own wrapper documents a mkdir-mutex rebuild lock with a ~90s stale-lock steal window — plausible mechanism
for why a nominally-~5s incremental query queued past 240s under concurrent multi-lane load.
**Verdict: TIMEOUT (UNKNOWN on failure_mode), not LOUD/FAIL-OPEN/SILENT-EMPTY, and explicitly not read as
either tool being broken** — this is a load/contention observation on the shared substrate during a
parallel multi-lane sweep, itself worth surfacing to CTO~Z as a scheduling consideration for any future
parallel census wave that touches `KUZU-CANONICAL` tools.

### 3.3 · Dispatch-idiom mismatch, reproduced live (same class REC-1 §6 named)

First invocation attempts on `comp-fedobs`, `comp-state`, and `comp-heat` used `bash .tools/comp-X` (this
lane's initial default). All three are idiom-2 (python shebang IS the entry — confirmed via `head -1`).
Bash tried to parse the Python source and threw syntax errors unrelated to the tool's own logic (`syntax
error near unexpected token '('`, `import: command not found`) — reproducing REC-1 §6 exactly, this time by
this lane hitting it fresh rather than reading about it. Corrected to `python3 .tools/comp-X` before
recording any result; the bash-mismatch outputs are preserved in the sidecar (`*_firstattempt` keys) rather
than discarded, per this project's own disclosure discipline. **`comp-system` is the opposite case**: it
IS a bash wrapper (`#!/bin/bash`, idiom-1) despite superficially resembling the idiom-2 tools by name-
pattern; an initial `python3 .tools/comp-system --self-test` attempt threw a Python `SyntaxError` on the
wrapper's own bash syntax (`WORKSPACE="$(cd ...)"`), the mirror-image mistake. Both directions are recorded,
not smoothed over.

### 3.4 · A new, environment-level artifact: leading-`/` argument path-mangling under python3 dispatch

Feeding `comp-fedobs --uri /definitely/nonexistent/path/zzz9999.json` (idiom-2, `python3`-dispatched) and
`comp-learns-status --source /definitely/nonexistent/path/zzz9999.json` (idiom-1, `bash`-dispatched —
**CORRECTED 20260725T0847Z**: this row's sidecar `invocation` field originally mislabeled the interpreter
as `python3`; `comp-learns-status` is `#!/usr/bin/env bash` and was actually run correctly under `bash`
the whole time, confirmed by a byte-identical fresh re-run — see the sidecar's `correction_20260725T0847Z`
note. `3.0.0_SA_CVO~Z` caught this by literally reproducing the mislabeled invocation string and getting a
genuine Python SyntaxError, correctly flagging the row's recorded evidence as unsound even though the
verdict happened to hold either way)
produced an error message citing `C:/Program Files/Git/definitely/nonexistent/path/zzz9999.json` — the
leading `/` was silently rewritten to `C:/Program Files/Git/` before the argument reached the Python
process, in this Cygwin-mounted (`/cygdrive/c/...`) session. **This did not invalidate either result** — the
rewritten path is still genuinely nonexistent, so both tools still correctly failed LOUD on a real absence —
but it is a distinct, newly-observed instance of the MSYS/Cygwin path-mangling class already banked in
memory (`feedback_aws_shim_delimiter_slash_msys_mangle`) and in this same census's own §10 finding (REC1B
`/c/` vs `/cygdrive/c/` mismatch) — this time hitting a bare leading-`/` CLI argument passed through to a
Python argparse consumer, not an `aws` call or a git hook path. Flagged for CTO~Z/CVO~Z as a third
independent sighting of the mount-alias hazard class, not chased further this pass (read-only scope; no
mutation to any shim).

## 4 · Acceptance gate

REC-1's positive control (`comp-manifest-check`, LOUD, confirmed) and mutant (`comp-stitch-refresh`,
SILENT-EMPTY at call site) are **not re-run here** — neither tool is in this lane's 17-tool batch, and
REC-1/REC-1b already hold them CVO~Z-verified. This batch's own internal anchor: `comp-icedrill` (§5) is a
known-LOUD-by-design row (its own output text says *"an empty result is a FINDING, not a clean"*) and reads
LOUD exactly as declared — the harness is not systematically biased toward finding mismatches even though
4 of 9 fully-exercised rows below are mismatches (5 MATCH, 4 MISMATCH).

## 5 · Results (17 rows, all tools in the batch)

| # | Tool | Declared `failure_mode` (conf) | Mutation type | Input fed | Observed | Verdict |
|---|---|---|---|---|---|---|
| 1 | `comp-kuzu` (bare/auto) | FAIL-OPEN (MED) | NONEXISTENT | `MATCH (n:NonexistentNodeType_zzz9999) RETURN n.id LIMIT 5` | TIMEOUT at 240s, live sibling-lane contention confirmed via `ps` (§3.2) | **UNKNOWN** (timeout, not tool-attributable) |
| 2 | `comp-kuzu-full` | FAIL-OPEN (MED) | n/a | not run for real (§3.1) | `--help` only: rc=0, argparse exit pre-DB-touch | **UNTESTABLE-SAFELY** (source-cited, CTO-gated non-MSTR restriction) |
| 3 | `comp-kuzu-inc` | FAIL-OPEN (MED) | NONEXISTENT | same query, `--mode inc` | TIMEOUT at 240s, same contention (§3.2) | **UNKNOWN** (timeout, not tool-attributable) |
| 4 | `comp-icedrill` | LOUD (default, LOW) | NONEXISTENT | `s3://opal-data-inf/definitely-nonexistent-prefix-zzz9999/` | rc=3, explicit multi-line: *"an empty result is a FINDING, not a clean"* | **MATCH** |
| 5 | `comp-aws` (`derive`) | LOUD (MED) | NONEXISTENT | `--class LAMBDA --resource arn:...:function:definitely-nonexistent-zzz9999 --out <scratch>` | rc=0, `nodes=0`, informative "NOT PUBLISHED" note | **MISMATCH** — observed FAIL-OPEN |
| 6 | `comp-assets` | LOUD (MED) | NONEXISTENT | `--channel definitely_nonexistent_zzz9999 --json` | rc=0, clean JSON `{"channels": [], "objects_scanned": 0}` | **MISMATCH** — observed FAIL-OPEN |
| 7 | `comp-genesis` | LOUD (MED) | NONEXISTENT | `validate definitely_nonexistent_tenant_zzz9999` | rc=1, `ERROR: no manifest for '...'` | **MATCH** |
| 8a | `comp-heat score` | LOUD (MED) | NONEXISTENT (not a fair test — see note) | `score definitely_nonexistent_item_zzz9999 --age-days 9999` | rc=0, clean computed answer (`band=COLD`) | **NOT-A-FAIR-TEST** — `score` is a stateless calculator; `id` is never looked up against anything real, so "nonexistent id" tests nothing |
| 8b | `comp-heat freshness` | LOUD (MED) | NONEXISTENT | `freshness definitely_nonexistent_subtree_zzz9999/ --json` | rc=0, explicit: *"no tracked/untracked files under '...'"* | **MISMATCH** — observed FAIL-OPEN |
| 9 | `comp-fedobs` | LOUD (MED) | NONEXISTENT (path-mangled, still absent — §3.4) | `--uri /definitely/nonexistent/path/zzz9999.json` | rc=1, explicit 2-line `ERROR: comp-fedobs could not read...` | **MATCH** |
| 10 | `comp-learns-score` | LOUD (MED) | n/a — ran built-in `--self-test` instead (write-risk avoidance, §5 note) | `--self-test` | rc=0, 8/8 internal PASS incl. Goodhart-honesty checks | **MATCH-VIA-SELFTEST** (external bad-input not independently exercised this pass) |
| 11 | `comp-learns-status` | LOUD (default, LOW) | NONEXISTENT (path-mangled, still absent — §3.4) | `--source /definitely/nonexistent/path/zzz9999.json` | rc=2, explicit `FileNotFoundError`-based 2-line message | **MATCH** |
| 12 | `comp-canon-motif` | FAIL-OPEN (MED) | STALE (default, no `--allow-stale`) | bare invocation | TIMEOUT at 240s, same contention class as #1/#3 (touches `KUZU-CANONICAL`) | **UNKNOWN** (timeout, not tool-attributable) |
| 13 | `comp-cluster` | FAIL-OPEN (MED) | NONEXISTENT | `DefinitelyNonexistentPageZzz9999` | TIMEOUT at 240s, same contention class as #1/#3/#12 (touches `KUZU-CANONICAL`, confirmed via `ps`) | **UNKNOWN** (timeout, not tool-attributable) |
| 14a | `comp-passcraft` (`emit`, no args) | LOUD (MED) | EMPTY | `emit` (zero args) | rc=2, argparse: `error: the following arguments are required: tool, --audit` | **MATCH** |
| 14b | `comp-passcraft --self-test` | LOUD (MED) | n/a (built-in) | `--self-test` | rc=0, 10/10 internal PASS (anti-harness synthetic-bad-input suite) | **MATCH-VIA-SELFTEST** (corroborating, not primary) |
| 15 | `comp-system` | LOUD (MED) | n/a — no caller-supplied target on this CLI | `--check` (health probe, not a mismatch test) + `--self-test` (budget-exceeded) | `--check`: rc=0 `SYSTEM CURRENT`; `--self-test`: exceeded 60s, not completed | **UNKNOWN** — no natural bad-input surface; self-test not completed within budget, not silently dropped |
| 16a | `comp-state --self-test` | LOUD (MED) | n/a (built-in) | `--self-test` | rc=0, `PASS (3/3 -- the instrument discriminates)` (planted BEHIND/CURRENT/QUIET cases) | **MATCH-VIA-SELFTEST** |
| 16b | `comp-state --project` | LOUD (MED) | NONEXISTENT (not a fair test — see note) | `--project definitely_nonexistent_zzz9999` | rc=0, `no drift found in window` (0 of 400-commit corpus matched the filter) | **NOT-A-FAIR-TEST** — a substring filter legitimately returning zero matches is a correct empty-set answer, not a masked failure; distinct from "artifact wholly absent" |
| 17 | `pipescript` (bare) | FAIL-OPEN (MED) | NONEXISTENT | `definitely-nonexistent-thread-zzz9999` | rc=2, explicit `'...' is NOT a known named thread` + full valid-alternatives list | **MISMATCH (reverse polarity)** — observed LOUD, stricter than declared FAIL-OPEN |

## 6 · Headline finding: a sixth, seventh, and (reverse-polarity) instance of the total-absence pattern

REC-1 (§5.1, `comp-freshness`) and REC-1b (§5, `comp-surface-check scan`) each independently found ONE
instance of *"declared LOUD, but a wholly-absent (not merely stale/malformed) input reads FAIL-OPEN — rc=0,
a human-readable note if any, nothing a script gating on exit code would catch."* **This batch adds THREE
more, independently, across three structurally different tools** (`comp-aws derive`, `comp-assets`,
`comp-heat freshness`): a `derive`, a census/backfill reader, and a git-heat scanner — none share
implementation, none share an author, none share a register-confidence tier beyond MED.
(`comp-canon-motif` and `comp-cluster`, both candidates for a similar result on a STALE/NONEXISTENT input,
instead hit the TIMEOUT class in §3.2 and did not produce a failure_mode observation either way — not
counted toward this pattern, not silently folded in either.)

> **CORRECTION (20260725T0638Z, `3.0.0_SA_CVO~Z` verify, folded in by this lane the same turn):** the "5
> independent sightings" figure below was written from this lane's own vantage (REC-1 + REC-1b + this
> batch's 3) and is a **structural undercount, not this lane's error** — `3.0.0_SA_CVO~Z` independently
> made the identical mistake 30 minutes earlier from lane-C's vantage (also computing "5," unaware of this
> lane's batch), and lane-C separately landed 3 MORE instances (`comp-tool-health`, `comp-tool-health-gate`,
> `comp-coverage`) this lane could not have seen. **True cross-lane union: 8 distinct instances across 4
> authoring passes** (7 at MED-or-better declared confidence). Any single lane computing a program-wide
> total from its own vantage is computing a number that is already stale at write time — CVO~Z's own
> recommendation, adopted here: **lanes report their own batch counts; cross-lane aggregation is one
> owner's job, not inferred by whoever writes second-to-last.** The paragraph below is left as originally
> written (this lane's honestly-scoped 3-instance contribution) with this correction standing next to it,
> rather than silently rewritten to a now-superseded "8" this lane did not itself verify.
>
> **Disclosure-limb refinement (CVO~Z's ask, checked against this lane's own 3 instances):** the
> declared-vs-observed axis is not the only useful one — whether the tool's stdout tells a human the
> absence occurred is a SEPARATE, non-uniform axis even within these 3: `comp-heat freshness` prose-flags
> it explicitly ("no tracked/untracked files under..."); `comp-aws derive` prints the `nodes=0` fact but
> nothing marks it as anomalous (indistinguishable from a real-but-edge-sparse resource without already
> knowing to look); `comp-assets` is pure structured JSON (`"channels": [], "objects_scanned": 0`) with no
> narrative flag at all — closest of these 3 to lane-C's `comp-coverage` outlier. A 3-point scale
> (prose-flagged / number-present-unflagged / structurally-silent) captures this better than a binary
> disclose-vs-silent split.

**Independent of the exact cross-lane count, the shape itself is no longer a pattern candidate; it is a
property of how this estate's AWS/repo-listing-style tools are written**: they treat "I searched and found
nothing" as a legitimate, quiet, zero-exit answer (often, but not always, with a genuinely well-written
explanatory note — see the disclosure-limb refinement above), not as the LOUD-failure condition the
register's rule-derived heuristic assumed. **This is not, on its own, a defect** — a listing tool returning
"0 results" for a genuinely-absent target is arguably the CORRECT behavior; the defect risk (per REC-1
§4c's own framing) is downstream, at whatever call site is gating dispatch/certify decisions on exit code
alone and would silently treat "0 legitimate objects" and "the target never existed" as the same green
light.

**Pipescript's result (row 17) is the interesting counter-case**: the register under-stated ITS rigor
(declared FAIL-OPEN, observed genuinely LOUD with an actionable message) — the first "safer than declared"
instance across REC-1/1b/1c combined. Worth naming alongside the six FAIL-OPEN instances so the pattern
reads as "declared failure_mode has now been shown wrong in both directions on total-absence input," not
"this register only ever over-promises."

## 7 · What this lane did NOT do

No apply, deploy, re-point, or write to any production S3 key, DynamoDB table, or Terraform-managed
resource. `comp-aws derive --out` targeted a scratch path under this session's own scratchpad, not any
shared or production location (confirmed via the tool's own "NOT PUBLISHED... local file" output). Did not
force a full Kuzu rebuild as a non-MSTR lane (`comp-kuzu-full` untested for real, §3.1). Did not chase the
path-mangling artifact (§3.4) to a fix — surfaced, not actioned, per read-only scope. Did not retry
`comp-kuzu`/`comp-kuzu-inc`/`comp-canon-motif`/`comp-cluster` a third time beyond the 240s budget each
already received, once live sibling-lane contention was independently confirmed via `ps` — continuing to
hammer a visibly-contended shared resource from multiple concurrent probes would itself degrade the same
census this pass is part of.

## 8 · Handoff

- **`1.0.0_SA_CTO~Z`**: §6's six-instance total-absence pattern (now spanning REC-1/1b/1c, 3 independent
  authoring passes) is a strong candidate for a register-level or call-site-level follow-up, not further
  per-tool sampling. §3.2's live multi-lane Kuzu contention (independently `ps`-confirmed) is a scheduling
  note for any future parallel census wave touching `KUZU-CANONICAL` tools. §3.4's path-mangling sighting is
  a third independent instance of the mount-alias hazard class.
- **`3.0.0_SA_CVO~Z`**: all 9 fully-exercised MATCH/MISMATCH rows + the 2 self-test-only rows have full
  verbatim output in the sidecar for independent re-derivation. The 4 TIMEOUT rows (`comp-kuzu`,
  `comp-kuzu-inc`, `comp-canon-motif`, `comp-cluster`) are independently re-checkable against the sidecar's
  `ps` snapshot evidence (§3.2) without needing to re-run the queries yourself.

## 9a · ADDENDUM (20260725T0652Z): serial re-run of the 4 TIMEOUT rows — discriminator resolved

Per `1.0.0_SA_CTO~Z`'s dispatch (20260725T065150Z): re-run `comp-kuzu`, `comp-kuzu-inc`, `comp-canon-motif`,
`comp-cluster` strictly serially, one at a time, with a confirmed-quiet-substrate precondition, to
discriminate "sweep contention explains the 4 timeouts" from "real fleet-wide degradation."

**Precondition check (printed per the dispatch's own requirement):**
```
ps -ef | grep -iE "kuzu_cli|canon_motif|comp_cluster|comp-canon-motif|comp-cluster" | grep -v grep
TRUE_RC=1   (empty match — zero concurrent processes; substrate confirmed quiet before starting)
```

**Serial re-run results (each run in-stdout `TRUE_RC` capture, one at a time, no concurrent invocation):**

| Tool | Wall time | TRUE_RC | Observed | vs. declared (FAIL-OPEN MED, all 4) | Verdict |
|---|---|---|---|---|---|
| `comp-kuzu` (bare/auto) | 2.74s | 1 | `ERROR: query failed: Binder exception: Table NonexistentNodeType_zzz9999 does not exist.` | LOUD, not FAIL-OPEN | **MISMATCH (reverse polarity)** |
| `comp-kuzu-inc` | 2.77s | 1 | identical Binder-exception error | LOUD, not FAIL-OPEN | **MISMATCH (reverse polarity)** |
| `comp-canon-motif` (default, no `--allow-stale`) | 2.73s | 0 | clean full scorecard; graph read `status=current` this run (NOT stale) — the intended STALE mutation did not actually manifest, the estate's own graph state had moved since the original attempt | n/a — input was not actually a mismatch this time | **NOT-A-FAIR-TEST-THIS-RUN** (would need a genuinely stale marker to test the declared property; not re-attempted, see below) |
| `comp-cluster` | 2.82s | 1 | `ERROR: no Page node 'DefinitelyNonexistentPageZzz9999'. Try: comp-cluster --list` | LOUD, not FAIL-OPEN | **MISMATCH (reverse polarity)** |

**Discriminator reading: RESOLVED — sweep contention, not fleet degradation.** All 4 completed serially in
2.7-2.8s each (previously 240s+ timeout, twice, under live multi-lane load) once the substrate was
independently confirmed quiet immediately beforehand. This confirms the original 6 prior timeouts (this
lane's 4 + `~B`'s 2, per the dispatch) are fully explained by concurrent multi-lane Kuzu-substrate
contention during the parallel sweep — **no fleet-degradation thread opens.**

**Substantive new finding, not just a discriminator result:** 3 of 4 re-run tools produced a THIRD instance
of the reverse-polarity pattern first seen with `pipescript` in §5 — the register under-states these tools'
actual rigor (declared FAIL-OPEN, observed genuinely LOUD with an explicit, actionable error). Combined
with `pipescript`, this batch alone now shows **4 reverse-polarity mismatches vs. 3 declared-LOUD-observed-
FAIL-OPEN mismatches** — the "declared wrong in both directions" finding from §6 is itself now
asymmetric within this one lane's data, weighted toward the register under-stating rigor rather than
over-stating it. Worth flagging to CTO~Z/CVO~Z as a possible correction to §6's framing once the full
cross-lane synthesis lands.

`comp-kuzu-full` was NOT re-run, per the dispatch's explicit instruction — its UNTESTABLE-SAFELY verdict
(§3.1, CTO arch-gated non-MSTR restriction) stands as correct restraint, unrelated to the contention
question this addendum resolves.

**What this addendum did NOT do:** did not re-attempt `comp-canon-motif` with a genuinely stale input
(would require either waiting for the marker to actually drift or synthesizing a stale local pin — the
latter risks a real state mutation this lane's read-only discipline does not permit without a separate
gate); did not re-run any of the other 13 tools (their MATCH/MISMATCH verdicts from §5 are unaffected by
this contention question, since none of them touch `KUZU-CANONICAL` or hit a timeout).

## 9 · Secondary item (dispatch's own wording): canonical mdpf refresh — grounded, not executed

Per the dispatch: *"the canonical mdpf refresh -- CANON's one open acceptance criterion, base-owned per its
coordination clause, confirmed still blocked as of yesterday. Ground what it would take; don't execute a
refresh without my gate."*

**Current state, re-grounded against this session's own commit log (not re-derived from scratch — this
lane's sibling `~D` and `3.0.0_SA_CVO~Z` already did the load-bearing work earlier today, cited here rather
than duplicated):**

- `0e97e0350f` (CTO~Z, earlier this session): `grain_baseline.json` `EXTERNAL_ENDPOINT` recertified 3→0 —
  root cause was a stale pre-taxonomy-change baseline (certified 2026-06-11, 15 days before a sovereign
  CTO-arch-gated `EXTERNAL_ENDPOINT` taxonomy drop on 2026-06-26), not a broken extractor. Scoped to this
  one dimension only.
- `9331f9ce01` (CVO~Z, independent re-verify, most recent commit on this branch as of session start):
  confirmed all 3 legs of that recert independently (source content, the skip-mechanism, and a live
  post-fix mutant re-run of `derive_stitch.py` — **5 violations now, not 6; `EXTERNAL_ENDPOINT` gone**).
  Same commit also carries an Andrew-direct-relayed ruling reopening the NFRA_GRAPHUNI.P2/D2
  `comp_marker_read.py` re-point architectural decision (CANON2's Leg B blocker, per
  `NFRA_TOOLARCH_CANON_CANON2_STATUS_AUDIT_20260725.md` §4-5) — dispatched to `~D` as a fresh
  coverage-parity re-measurement first, decision held pending that.

**What this means for "what it would take":** the canonical mdpf refresh (`derive_stitch.py` →
`stitch_graph.json`, gated by `grain_sentinel.py`'s AC-GRAIN.2 check) is **still blocked**, but the
denominator just shrank from 6 violation classes to 5 (`REACT_QUERY_KEY`, `SQS_QUEUE`,
`ECS_TASK_DEFINITION`, `SCHEDULE`, `IAM_USER` remain; `EXTERNAL_ENDPOINT` is closed). Each of the
remaining 5 needs its own individually-verified reason before recert, per the same discipline
`0e97e0350f` established for `EXTERNAL_ENDPOINT` — this is NOT a bundle-fix; each dimension is a
separate grounding exercise. **This lane did not execute any of those 5 recerts** (no gate from CTO~Z
to do so, per the dispatch's own explicit hold) and did not duplicate `~D`'s already-dispatched
coverage-parity re-measurement work on the separate NFRA_GRAPHUNI thread. Flagging the updated
denominator (6→5) as the concrete, actionable delta since CANON's audit was last read, not asserting
readiness to refresh.
