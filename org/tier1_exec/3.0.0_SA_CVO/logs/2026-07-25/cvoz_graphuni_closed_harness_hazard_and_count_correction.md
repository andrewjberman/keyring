# CVO~Z session log — 2026-07-25, GRAPHUNI closed + harness rc hazard root-caused + count correction

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · branch CLOUD · Monitor `bb2a28twe`

---

## 1 · HARNESS rc HAZARD — confirmed, root-caused, and it is a defect we already found today

`0.8.0_AE_CloudComp~E` banked a hazard: this shell environment appends a spurious wrapper-level exit-1 to
every Bash call, so any lane reading the harness-reported exit code sees uniform LOUD. CTO~Z explicitly
asked whether my OWN rc reads this session were affected — a threat to all of my evidence.

**Tested rather than assumed.** Three controls in one call: `true` -> `IN_STDOUT_RC=0`; `bash -c 'exit 3'`
-> `IN_STDOUT_RC=3`; `git rev-parse` -> `IN_STDOUT_RC=0` (printed CLOUD). All correct — while the harness
reported "Exit code 1" for the whole call. **In-stdout `$?` capture is accurate; the harness-level code is
not.**

**ROOT CAUSE — same defect as the stitch post-commit hook.** Every call ends with
`/usr/bin/bash: line N: /c/Users/ANDREW~1/AppData/Local/Temp/claude-XXXX-cwd: No such file or directory`.
The wrapper appends a cwd-tracking step at an **MSYS-style `/c/Users/...` path this Cygwin shell cannot
resolve** (it needs `/cygdrive/c/...`); that step fails and its failure becomes the call's exit status.
This is the identical class as the hook bug I flagged and CTO~Z fixed at `fbc91c6e28`. One root, two
manifestations: one silently stopped a producer for 17 days, this one silently corrupts every exit code the
fabric reads.

**My evidence holds, with one disclosed hit.** Every rc I *reported* was captured via `echo "RC=$?"`
immediately after the command — in-stdout, proven accurate above — so the lane-C re-derivations
(comp-registry rc=1, comp-tool-health rc=0, comp-tool-health-gate rc=0, comp-coverage rc=0) and the
REC-1/1b anchors stand unchanged. **The exception, recorded rather than quietly fixed:** in the
grain_baseline mutant re-run I piped `derive_stitch.py` through `tail -25`, so that `RC=0` was *tail's*
exit code. It did not affect the finding — what I reported was stdout-derived ("5 violation groups not 6,
EXTERNAL_ENDPOINT absent") and I never claimed the rc changed — but had I written "rc=0 therefore it
passes," that would have been false. **The guard there was what I chose to claim, not the instrument.**
Three independent agents (~C, ~E, me) hit this same retrieval-layer trap in one cycle.

## 2 · COUNT CORRECTION — the absent-input pattern is 8, not 5, and one of the wrong counts was mine

Lane-base reported its results "bring the pattern to 5 independent sightings." My own lane-C verdict ~30
min earlier also said 5. **Both locally correct, both wrong at program level, because we counted different
members** — lane-base counted REC-1 + REC-1b + its own 3 (unaware of lane-C, landed in parallel); I counted
REC-1 + REC-1b + lane-C's 3 (written before lane-base existed).

**True union, enumerated from the raw sidecars myself:** comp-freshness (REC-1) · comp-surface-check scan
(REC-1b) · comp-tool-health, comp-tool-health-gate, comp-coverage (1c lane-C) · comp-aws, comp-assets,
comp-heat freshness (1c lane-base) = **8 distinct instances across 4 authoring passes**, 7 if requiring
MED-or-better declared confidence (comp-coverage's LOUD is a convention default at LOW).

**Directional effect: this STRENGTHENS the "settled" recommendation.** At 8 across 4 independent passes,
re-sampling for existence is spend without signal — same logic as my REC-1b role_flags verdict.

**Process finding, which outlives the number:** in a 6-lane parallel program, any lane computing a
program-wide total computes it from a vantage already stale at write time, and the number looks
authoritative. Recommended mitigation (a) — lanes report own-batch counts only, one owner aggregates.
**CTO~Z ADOPTED it and correctly assigned itself as aggregation owner with me as verifier** — had I become
the author I would be verifying my own number, the exact independence loss this lane exists to prevent.

**Refinement adopted FROM lane-base, over my own split:** the disclosure limb is a **3-point scale**, not
binary — clear-prose-flag (comp-heat) / number-present-but-unflagged (comp-aws `nodes=0`, reads like a
measurement) / structurally-silent (comp-assets bare JSON, comp-coverage). The middle tier is what my
2-limb version would have lost. My earlier "only comp-coverage misleads on stdout" is accordingly **too
strong** — comp-assets does the same in JSON. Corrected.

## 3 · NFRA_GRAPHUNI — CLOSED. My 306 reconciles exactly; I conceded my own label.

~D delivered the option-1-vs-2 discriminator I routed. **All citations verified on my own commands:**
`extract_gold_compute.py:63` imports and **:73 CALLS** `build_graph(_ws).save(tg_path)`; the artifact holds
exactly **192** READS_S3 (own Counter); zero consumers (own grep); `generated_at: null` (mtime Jun 30 —
a month-old pre-flip artifact, honestly flagged by ~D).

**THE EXACT RECONCILIATION.** From the artifact's own `coverage` block:
`192 emitted (Phase-A) + 112 phase_b_deferred_count + 2 S3KEY_FIRM_UNRESOLVED = 306` — against my
independently-measured requirement of **306** script-side READS_S3. Three separately-recorded components
landing exactly on it. Every edge my 0-vs-306 count called missing is accounted for in the producer's own
bookkeeping. The shortfall is a **deliberate documented deferral with an existing off-switch** (`:189-190`
skips READS_S3 where no `writer_firms`; `:230` `build(phase_a=not a.full)` — `--full` already disables it).

**CTO~Z's new citation verified, and it does more than claimed.** `extract_s3.py:447-456`:
`Edge(source=s3_node_id, target=script_node_id, edge_type="READS_S3")` under a comment "File-level S3
reads". Three things at once: script-grain **by construction** (so function-grain READS_S3 can never exist
from this path — my 0-count is a structural property, not a data gap); polarity is `s3 -> script`, matching
the fixture's 306 and **opposite** the producer's `script -> s3`, confirming my polarity warning at source
on both sides; and build_graph **never needed a rollup for READS** — it extracts them directly. The
projection's rollup was trying to synthesize what build_graph obtains a different way.

**I CONCEDED MY OWN RULING'S LABEL.** I had ruled "Option 1 — re-populate at build_graph fidelity." CTO~Z
said "neither option." CTO~Z is right: my wording implies changing the marker-head compute to *reach*
build_graph fidelity, when the actual fix is to **connect a producer that already has it**. The original
option list never contained that. Substance identical (fix layer = compute population, fresh run not the
stale JSON, 112 as named residual), so no dispatch changed — but the record carries CTO~Z's framing, not
my closest-fitting label.

**Routed the wire-in back to CTO~Z for dispatch** (producer change → scoped TO + no-regression bar) with
three acceptance conditions from what I hit: (a) polarity + namespace canonicalization BEFORE any
set-compare, else a 100%-correct wire-in false-FAILs on convention alone; (b) per-target SHA equality via
the P0-CVO recipe, **not** aggregate node/edge totals — my radius analysis showed gross counts hide
detector-specific weakness exactly as the attestation's §5 warns; (c) success bar stated as **member-level
set-identity**, since 192+112+2=306 is a COUNT reconciliation only. **Nobody may quote it as set-identity,
including me** — that's the TO's deliverable, not an inherited assumption. Also flagged the 2 named
`S3KEY_FIRM_UNRESOLVED` keys as a third item so they don't vanish into the residual.

## 4 · Queue disclosed, not assumed

REC1C_E, the remaining lane-base MATCH rows, and REC1C_A are **unverified**. Lane-base's 4 Kuzu-contention
TIMEOUT rows marked **DEFERRED-NOT-DONE** (honest UNKNOWNs, not verdicts; serial re-run recommended after
the sweep quiets — CTO~Z concurs) so synthesis cannot count them as covered.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| 3 shell controls (`true` / `exit 3` / `git rev-parse`) | PASS — hazard confirmed | proved in-stdout `$?` accurate and harness exit code unreliable; root-caused to the `/c/` vs `/cygdrive/c/` class |
| Python (own parsers) over 3 lane sidecars | PASS | independent tallies: lane-C 10/4/2, lane-base 20-row breakdown, absent-input union = 8 |
| Python over `gold_compute_producer.json` | PASS — **decisive** | 192 READS_S3 + the `coverage` block giving 112 deferred + 2 unresolved = exact 306 reconciliation |
| `grep -rln gold_compute_producer --include=*.py` | PASS | zero consumers independently confirmed |
| `sed`/`grep` over `extract_gold_compute.py`, `extract_s3.py` | PASS — 3 citations verified | `:73` build_graph CALL; `--full` flag at `:230`; `extract_s3.py:447-456` polarity + script-grain-by-construction |
| 4 comp-tool invocations (registry/tool-health/gate/coverage) | PASS | lane-C mismatches reproduced, own probe strings, rc in-stdout |
