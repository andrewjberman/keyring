# NFRA_TOOLUNIFY REC-1c LANE-C — 16-Tool Exercise Batch + ms_heat Disposition — 0.8.0_AE_CloudComp~C

**archetype:** VALIDATE
**Date:** 2026-07-25
**Task Order:** NFRA_TOOLUNIFY.REC-1c LANE-C (MCP dispatch from 1.0.0_SA_CTO~Z 20260725T060457Z; no XML TO
filed — off-main-fabric census group convention)
**Status:** COMPLETE
**Cycle wall:** ~06:02Z start (fresh registration) → ~06:30Z deliverables on disk

---

## Objective

Andrew-direct parallel program: all remaining register tools behaviorally exercised, each lane its own
thread. Lane C batch = the routing/registry/validation family (16 tools): feed each a
mismatched/stale/empty/nonexistent input, record OBSERVED (LOUD/FAIL-OPEN/SILENT-EMPTY) vs the D.md
register's DECLARED `failure_mode`, provisional mutation-type labels, UNKNOWN first-class, read-only
throughout. Secondary: a one-page ms_heat disposition recommendation.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `comp-manifest-check` | `check --file <probe> --mode blocking` | PASS | harness positive control — LOUD as declared (rc=1 BLOCKED) |
| `comp-freshness` | `artifact <nonexistent-prefix>` | PASS | harness mutant — known non-LOUD reads non-LOUD (WARN rc=0), separate invocation |
| `comp-which` | gibberish question | PASS | FAIL-OPEN as declared; honest no-match banner; noise: 7-token question reduced to 1 grep token |
| `comp-which-routing-test.py` | `--freeze <nonexistent> --out <scratch>` | PASS | LOUD as declared (raw traceback = friction); baseline protected, --out confirmed unwritten |
| `comp-registry` | `sync --project <nonexistent>` | MISMATCH | observed LOUD rc=1 vs declared FAIL-OPEN (benign direction, row still wrong) |
| `comp-routable-check` | bare (live) | UNKNOWN | no safe bad-input channel; live: OK + 4 uncatalogued routables WARN (routed) |
| `comp-ontolint` | `check --rule-bank <nonexistent>` | PASS | LOUD rc=2 graceful; its own "hard error never silent pass" claim exercise-confirmed |
| `comp-toolgraph` | `edges` (live) | UNKNOWN | no external-input channel on any subcommand |
| `comp-tool-health` | `--tool <nonexistent> --no-refresh` | MISMATCH | FAIL-OPEN observed (note + rc=0, `comp_tool_health.py:600`) vs declared LOUD — comp-iam-service shape |
| `comp-tool-health-gate` | `--effective-feed <nonexistent>` | MISMATCH | FAIL-OPEN BY DESIGN (docstring "never a crash", `comp_tool_health.py:392,396-402`) vs declared LOUD |
| `comp-validate` | `<nonexistent-id> --artifact <nonexistent>` | PASS | LOUD rc=1, graceful + actionable |
| `comp-coverage` | `report --pipeline <nonexistent>` | MISMATCH | well-formed all-zeros report rc=0 — plausible-wrong-number shape; first check of this LOW/default row |
| `comp-coverage-check` | bare (live) | PASS + LIVE FINDING | LOUD as declared; live FAIL: `comp-residue` UNPLACED in coverage map (routed); no help path (--help ignored, check runs) |
| `comp-parity` | `<nonexistent-firm>` | PASS | LOUD rc=1 (raw traceback = friction); second LOW/default row verified |
| `comp-honesty` | `<nonexistent case.json>` | PASS | LOUD rc=1 (raw traceback = friction) |
| `comp-kit-striplist-gate` | `<nonexistent kit_root>` | PASS | LOUD rc=2 graceful; register's "verify manually" caveat discharged for this class |
| `comp-to` | env-unset probe | PASS | FAIL-OPEN as declared (HIGH row verbatim-confirmed); fallback branch writes nothing (source-confirmed pre-run) |
| `comp-xray` | `s3 <bucket> <nonexistent-key> --fields x` | PASS | LOUD rc=2 UNVERIFIABLE per own printed contract; F5: argparse errors also rc=2 (collision); first attempt was my own dispatch-mismatch, not recorded as failure_mode |

**What worked:** the REC-1/1b banked gotchas paid directly — idiom identification before invocation (6
python3-shebang, 10 bash-wrapper, zero mis-dispatches recorded as tool failures), and the
dispatch-mismatch rule correctly kept comp-xray's argparse rc=2 out of the register comparison. The
interface-discovery pass (--help sweep) itself surfaced two live findings before the sweep proper began.

**What failed (mine, disclosed):** first rc-capture piped the tool into `head` and read head's exit code —
caught before recording anything; all recorded RCs are unpiped. comp-xray first invocation missed required
args (rc=2 usage error) — re-invoked correctly.

**Gap found:** the register's failure_mode column cannot express "LOUD on bad content, FAIL-OPEN on absent
input" — now 5 exercised instances across REC-1/1b/1c (deliverable F1); recommended as a register
dimension / L0b ABSENT-input axis.

Auto-logged per-invocation to `org/compiler-tools-log.md` (comp_log_auto, ~C rows); session line appended.

---

## Work Completed

1. **Startup:** registered `~C` (PID 11384), armed persistent inbox Monitor (task b6nyrqgwc; first arm
   failed exit-127 on the skill doc's `/c/...` path — this shell is `/cygdrive/c/...`, same as ~D/CTO~Z/
   CVO~Z per REC1 §10; re-armed correctly), LD-0290 serial file, audit-archive invoker (0 findings),
   owned-paths hook confirmed, `.agent_context` set, logs/prompt/ORG_CHART read. READY→ACK loop with CTO~Z.
2. **Harness validation:** positive control + mutant, separate invocations, both PASS (§2 of deliverable).
3. **16-tool sweep:** 16/16 invoked, 0 skipped; 14 synthesized bad inputs + 2 first-class UNKNOWNs.
   Producer safety: all 7 PRODUCER-CANDIDATE closures grepped for S3 write calls = zero hits,
   positive-controlled; every local write flag avoided.
4. **Deliverables written to the census directory (on disk for CTO~Z commit, owned-path convention):**
   `REC1C_C.md`, `REC1C_C.sidecar.json`, `MS_HEAT_DISPOSITION_C.md`.

## Headline results

- **10 MATCH / 4 MISMATCH / 2 UNKNOWN.** Mismatches: `comp-registry` (louder than declared),
  `comp-tool-health`, `comp-tool-health-gate`, `comp-coverage` (all quieter than declared, all on absent
  input).
- **F1 — the absent-input FAIL-OPEN pattern is now 5 exercised instances** (REC-1's comp-freshness,
  REC-1b's comp-surface-check scan, + 3 this batch), 3 of them documented "never crash" design — promoted
  from REC-1b's "2/2, needs a third check" to a confirmed register-wide theme with a concrete
  recommendation (absence-behavior as its own register/L0b dimension).
- **Live estate findings routed (not actioned):** `comp-residue` UNPLACED in the coverage map
  (comp-coverage-check FAILs live right now); 4 router-reachable tools absent from tools_index
  (comp-describe, comp-kuzu-full, comp-kuzu-inc, comp-state).
- **ms_heat disposition: leave-dormant-with-declared-status** — zero consumers (S4 comp-ms-find never
  built), so a schedule is unjustified (a schedule is justified by a consumer, never by a producer) and
  retirement destroys proven work for ~no savings; declare DORMANT-BY-DECISION where readers look, bind
  revival to a consumer landing (at which point the CLAUDE.md schedule rule applies in full).

## Decisions Made

| Decision | Rationale |
|---|---|
| Record 2 tools as UNKNOWN rather than mutating live register files to synthesize bad input | Read-only discipline outranks coverage; UNKNOWN is first-class per the dispatch's own labeling rule |
| One primary mutation per tool | Light-cycle scope; the absent-input axis (F1) is the named candidate for any widening pass |
| comp-xray argparse rc=2 excluded from the register comparison, then noted as finding F5 | The REC-1 §6 gotcha (dispatch-mismatch is not the tool's failure_mode) — but the rc-collision itself is real signal for a GUARD-adjacent tool |
| ms_heat: recommend declare-dormant over schedule despite the "production pipelines must be scheduled" rule | The rule's own predicate fails: zero consumers means not-production; scheduling a consumerless producer manufactures a new silent-failure surface against the no-proliferation discipline |

## Files Modified

| File | Change | Committed |
|---|---|---|
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/REC1C_C.md` | New | No — CTO~Z-owned path, on-disk for CTO~Z commit (lane convention) |
| `.../REC1C_C.sidecar.json` | New | No — same |
| `.../MS_HEAT_DISPOSITION_C.md` | New | No — same |
| `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/nfra_toolunify_rec1c_lane_c_exercise_batch.md` | This log | This session, own lane author |
| `org/compiler-tools-log.md` | Auto-appended ~C rows + one session line | This session (shared append-only log) |

## Blockers

None. (Launcher-named `org/mcp/comp_ferry_queue.json` does not exist on disk — flagged to CTO~Z at READY,
not blocking; the dispatch superseded it.)

## Current State

REC-1c LANE-C delivered: 16/16 exercised (denominator explicit, skips zero, UNKNOWNs first-class),
harness gate-validated, deliverables + ms_heat memo on disk at the census path, report to CTO~Z + CVO~Z
sent this turn. Event-driven, standing by for CVO~Z verification queries or the next batch.

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Commit the three census-path files; dispose F1 (absence dimension), F4's two live
   drifts, F3's register corrections; rule on the ms_heat recommendation.
2. **[3.0.0_SA_CVO~Z]** Independent re-derivation per the acceptance bar — every row re-runnable from the
   sidecar's exact invocations; the two source-grounded mechanism claims carry file:line citations at
   this session's working-tree vintage (branch CLOUD).
3. **[0.8.0_AE_CloudComp~C]** Event-driven, standing by.
