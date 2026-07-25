# NFRA_TOOLUNIFY REC-1c LANE-E — 16-Tool Exercise Batch — 0.8.0_AE_CloudComp~E

**archetype:** VALIDATE
**Date:** 2026-07-25
**Task Order:** NFRA_TOOLUNIFY.REC-1c LANE-E (MCP dispatch 1.0.0_SA_CTO~Z 20260725T060511Z, no XML TO —
off-main-fabric census group)
**Status:** COMPLETE
**Cycle wall:** ~0600Z–0645Z (startup 0602–0605Z; dispatch received 0605Z; exercises + deliverable
0606–0645Z)

---

## Objective

Fresh ~E lane launch (Andrew-direct parallel tool-register exercise sweep, same program as ~D): /watcher +
org/XXX.md startup, register with CTO~Z, then execute the REC-1c LANE-E dispatch — behaviorally exercise a
16-row batch of the §2.D census register (pipeline/frontend/misc) against declared `failure_mode`, with
positive-control + mutant acceptance gate, provisional mutation-type labels, UNKNOWN first-class, read-only
throughout.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `comp-manifest-check` | `check --file <anti-pattern> --mode blocking` | PASS | positive control — LOUD as declared (rc=1 BLOCKED) |
| `comp-iam` | `service nonexistent-lambda-zzz-9999` | PASS | harness mutant — FAIL-OPEN reads rc=0 through this shell's spurious wrapper exit-1; proves the in-stdout RC capture discriminates |
| `comp-pipescript` | `deployed <nonexistent>` / `chain <nonexistent>` | MIXED | deployed: all-zeros summary @ rc=0 (**MISMATCH**, FAIL-OPEN on the AE pre-gold-run surface); chain: LOUD rc=1 (io/postdeps cited from CVO~Z reground §6, not re-run) |
| `comp-chainrun` | `diff <nonexistent pre> <nonexistent post>` | PASS | LOUD-by-crash (unhandled FileNotFoundError, rc=1) — MATCH, crash-vs-design noted |
| `comp-incrparity` | bare + `COMP_INCRPARITY_INCLUDE_HELD=1 … --no-s3-report` | PASS | rc=3 fail-closed agent gate (**stale predicate**: enforces the bd hold Andrew lifted 07-14) + rc=2 `UNVERIFIED… NOT a pass` — best-instrumented in batch |
| `comp-trigger` | `zzz-nonexistent-trigger-9999` | PASS | FAIL-OPEN as declared, with denominator + match-miss caveat (honest kind) |
| `comp-transform` | `schema-check <nonexistent>` | PASS | LOUD rc=1, MATCH |
| `comp-tooltip` | `<unknown-subcommand>` | PASS | LOUD rc=1 usage, MATCH |
| `comp-types` | `blast <nonexistent type>` | **FAIL-class finding** | rc=0 + `Blast radius: 0` + explicit `PASS` on garbage input (**MISMATCH — affirmative FAIL-OPEN**, sharpest in batch) + silent local manifest write (probe debris removed) |
| `comp-cache` | `key <nonexistent>` | CONCERN | rc=0, denominator disclosed — MISMATCH vs LOUD-default (LOW row, first individual verification) |
| `comp-perf` | `vectorize-audit <nonexistent>` | PASS | LOUD rc=1, MATCH |
| `comp-pulse` | `diff <nonexistent path>` | PASS | FAIL-OPEN as declared; `REFLEX CLEAN — a MEASURED result` stamped on a nonexistent file (self-cert nuance) |
| `comp-describe` | `<nonexistent resource>` | PASS | LOUD rc=1 + `Broken retrieval != absent resource` — MATCH; zero output inside a 2m budget (latency), retry confounded by my own orphan (disclosed) |
| `comp-axes` | `directory --no-snapshot --axes <nonexistent>` | PASS | LOUD rc=2 + known-list; write path (put_object :318) avoided by design flag |
| `comp-adapter-audit` | `<nonexistent fn> --manifest-dir <scratch>` | PASS | LOUD rc=1 vs declared FAIL-OPEN — good-direction MISMATCH; only tool shipping a read-only-exercise flag |
| `comp-v5-composite-test.sh` | bare (env mutation: `.tools` off PATH) | PASS | rc=8 = fail count; command-not-found NOT swallowed — MATCH (MALFORMED-ENVIRONMENT label) |
| `comp-whoread` | `<nonexistent bucket> --since 2026-07-18` | PASS | fail-closed rc=1, `NEVER CAPTURED != never read` — exemplary MATCH; covers the `.py` row via source-confirmed exec dedup |

**What worked:** the in-stdout `TRUE_RC=$?` capture — mandatory in this shell, where every Bash call carries
a spurious wrapper exit-1 (`claude-*-cwd` artifact) that would have read every tool as LOUD. The
acceptance-gate mutant was pointed at exactly that hazard. Tools shipping their own safe-exercise
affordances (`--no-snapshot`, `--manifest-dir`, `--no-s3-report`) made the read-only discipline cheap.

**What failed:** first `comp-describe` attempt timed out at 2m with zero output AND its python worker
survived the wrapper kill (killed my own orphan; the retry's kuzu 180s-timeouts are confounded by that
overlap — disclosed in the deliverable, not quoted as clean latency). First Monitor arm failed exit-127 on
the doctrine's `/c/...` path (this shell is `/cygdrive` — same as ~D/CTO~Z/CVO~Z found; re-armed with `C:/`).

**Gaps found:** (1) `comp-types blast` affirmative-PASS on nonexistent input — candidate
FAIL-OPEN-AFFIRMATIVE sub-class for L0b; (2) `comp-incrparity` agent gate enforces the LIFTED bd hold —
live stale-guard, retraction never propagated to this enforcing copy; (3) `comp-pipescript` per-subcommand
heterogeneity, third multi-subcommand confirmation, with the quiet subcommands being exactly the
operational-gate ones; (4) `org/mcp/comp_ferry_queue.json` referenced by this lane's launcher does not
exist (stale launcher pointer, flagged to CTO~Z at registration).

Auto-appended to `org/compiler-tools-log.md` via `.comp-graph/.agent_context`.

---

## Work Completed

1. **Startup:** registered `0.8.0_AE_CloudComp~E` (PID 21300), armed persistent inbox Monitor (task
   `bdlf37jzk`, confirmed via TaskOutput), LD-0290 serial file, audit-archive-invoker rc=0/0, owned-paths
   hook, agent context, zero crons, `/cloud-ops` loaded. Ready-ping to CTO~Z 0604Z; dispatch landed 0605Z;
   ACKed same minute.
2. **Acceptance gate:** both anchors PASS as separate invocations (§2 of the deliverable).
3. **16-row batch exercised — 15 distinct tools, 15/15, zero skips, zero UNKNOWN rows.** Score: 11 MATCH,
   4 mismatch-bearing tools. Full verbatims in `REC1C_E.sidecar.json`.
4. **Deliverable:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/REC1C_E.md` + sidecar —
   on disk for CTO~Z's commit (owned path, lane convention).
5. **Hygiene:** removed my probe's manifest debris from `types-index/` (pre-existing untracked manifests
   left untouched, noted); reaped my own orphaned comp-describe python worker.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Capture exit codes in-stdout, gate-proven | This shell's wrapper exit-1 artifact would misclassify every tool as LOUD; the mutant anchor proves the capture discriminates |
| Exercise comp-incrparity BOTH layers (bare + designed env override) | The bare path documents the live agent behavior (stale-gate finding); the override path is the designed DS/pipeline entry and the only way the mutation reaches the parity logic; `--no-s3-report` + rc=2-before-emit makes it write-free |
| whoread pair = one invocation | Wrapper `exec`s the .py (source-read); a second identical invocation adds noise, not information — recorded as COVERED-BY-DEDUP, not a skip |
| v5-composite mutation = environment, named | The harness takes no input; MALFORMED-ENVIRONMENT (bare names, `.tools` off PATH) is the only synthesizable mutation and is explicitly named per the dispatch's labeling rule |
| Disclose the comp-describe latency confound | My own orphan overlapped the retry; 7.5m is not clean evidence — the unconfounded fact is zero-output-in-2m |

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.../NFRA_TOOLUNIFY_CENSUS/REC1C_E.md` | New — REC-1c LANE-E write-up | No — CTO~Z BASE_EXEC owned path, lane convention |
| `.../NFRA_TOOLUNIFY_CENSUS/REC1C_E.sidecar.json` | New — per-invocation verbatims | No — same |
| `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/nfra_toolunify_rec1c_lane_e_exercise_batch.md` | This log | Yes — this session, own lane |
| `org/modules/graph/types-index/ZzzNonexistentType9999.blast.yaml` | Created by comp-types probe, DELETED same session | n/a (untracked debris, removed) |

## Blockers

None.

## Current State

REC-1c LANE-E delivered: 15/15 distinct tools exercised (16 register rows; whoread pair deduped at source),
acceptance gate passed on both anchors, zero skips/UNKNOWNs, deliverable + sidecar on disk at the census
path for CTO~Z. Headline findings: comp-types affirmative-PASS on nonexistent input;
comp-incrparity's stale sovereign-hold gate; comp-pipescript deployed FAIL-OPEN on the pre-gold-run
surface; comp-adapter-audit better than its register row.

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Commit REC1C_E.md + sidecar; route §4.1 (FAIL-OPEN-AFFIRMATIVE L0b candidate),
   §4.2 (stale hold predicate fix), §4.5 (quiet-subcommands-are-the-gates concentration).
2. **[3.0.0_SA_CVO~Z]** Re-verify per acceptance-gate bar; all rows re-derivable from sidecar verbatims;
   note the in-stdout RC-capture rationale before re-running in a wrapper-artifact shell.
3. **[0.8.0_AE_CloudComp~E]** Event-driven, standing by for next batch.
