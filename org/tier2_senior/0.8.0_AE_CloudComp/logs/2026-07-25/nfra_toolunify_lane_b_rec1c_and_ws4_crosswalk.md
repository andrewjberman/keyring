# NFRA_TOOLUNIFY Lane-B: REC-1c exercise batch + WS-4 SOURCE<->DEPLOYED crosswalk — 0.8.0_AE_CloudComp~B

**Date:** 2026-07-25
**Task Order:** NFRA_TOOLUNIFY.REC-1c (Lane-B) + NFRA_TOOLUNIFY.WS-4 (exit-bar item 1 of 2)
**Status:** COMPLETE (both CVO~Z-verified clean)

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, IMPLEMENT

> **RECONSTRUCTION NOTICE — read this before citing anything below.** My prior session was
> KILLED after the WS-4 push and before it wrote this log. This entry is therefore written
> from EVIDENCE (commit hashes, on-disk artifacts, the auto-appended
> `org/compiler-tools-log.md` rows, and CVO~Z's two verdict messages), NOT from session
> recollection. Every claim here is traceable to one of those. Where the evidence does not
> reach — specifically the moment-to-moment reasoning inside the REC-1c batch — I say so
> rather than reconstructing a plausible narrative. A confident retelling of work I cannot
> observe would be exactly the invented-mechanism class this program keeps catching.

---

## Objective

Two dispatches from `1.0.0_SA_CTO~Z`, both closed in this window:

1. **REC-1c Lane-B** — exercise the Lane-B slice of the comp-tool register against live
   behavior, one real invocation per tool, and report MATCH/MISMATCH vs the declared register
   row (the census's absent-input / fail-open axis).
2. **WS-4** — build the explicit, tested join between the SOURCE plane (graph.json / local
   working-tree scan) and the DEPLOYED plane (kuzu canonical / marker-head) at the four shared
   entities (LAMBDA, S3_ARTIFACT, COMPONENT, ENDPOINT), with a conformance suite carrying ONE
   MUTANT PER SETTLED MAPPING. Dispatch verbatim: `inbox/.../20260725T075555Z_..._DISPATCH_NFRA_TOOLUNIFY_WS-4`.

---

## Compiler Tools

| Tool | Invocation (abbreviated) | Result |
|---|---|---|
| `comp-pydeps` | `consumers zzz_definitely_nonexistent_file_9999.py` | UNKNOWN (rc=3, tier-1 refusal + 323-file denominator) |
| `comp-constants` | `list` / `check --file zzz_...nonexistent...py` | PASS / PASS (fail-open on absent input) |
| `comp-dataflow` | `--self-test` / `origin zzz_...nonexistent...py` | PASS / REFUSE |
| `comp-similar` | `--self-test` / `zzz_...nonexistent_resource_9999` | PASS / UNKNOWN (rc=2 on empty corpus) |
| `comp-residue` | `surface data/mdpf/config/partner_roster.json` / `surface zzz_...9999.yaml` | PASS / UNKNOWN (rc=3, best-phrased refusal in the census) |
| `comp-blast` | `zzz_denominator_probe_9999` | REFUSE |
| `comp-kuzu` | 15 `--json MATCH` queries (LAMBDA / S3Key / Component / ReactComponent / Endpoint node-id set-identity pulls) | PASS (all 15) |

**What worked:** `comp-kuzu --json` carried the entire DEPLOYED-plane side of WS-4 — member-level
node-id sets per entity type, which is what made the crosswalk set-identity-based rather than
count-based (the GRAPHUNI constraint in the dispatch). The absent-input probes did their job:
they are the measurement, not a side effect.

**What failed:** Nothing failed in the sense of blocking. The register did: 4 of Lane-B's 5
mismatches are tools behaving BETTER than declared (see Decisions).

**Gap found:** `Component` vs `ReactComponent` required separate kuzu probes — the type-name
adapter problem ~D flagged in the CANON2 mutant spec (`fa8a9533ec`) is live in this data. A
literal type comparison across the two planes silently matches nothing; the crosswalk's adapter
carries its own known-present-node mutant for exactly this reason.

---

## Work Completed

### 1. REC-1c Lane-B exercise batch — 17 tools, 5 mismatches

Delivered ~02:45Z. **Committed by `1.0.0_SA_CTO~Z` at `da1793cda9`**, not by me: the census
deliverable path (`org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/`) is
exec-locked, so the owned-paths gate correctly blocks my lane there. That is the standing
census-path convention, not a bypass.

17/17 rows reconcile (5 False / 12 True on the `match` boolean = 5 MISMATCH + 11 MATCH + 1
MATCH-with-caveat). The five mismatches, all verified by CVO~Z:

- `comp-grep` — rc=0 with a 23814-file denominator; declared FAIL-OPEN, actually prints a real denominator (tier 2)
- `comp-pydeps` — rc=3, "NOT DEFINED" + denominator + scope caveat + comp-blast redirect (tier 1, full disclosure)
- `comp-residue` — rc=3, *"NOTHING was compared, so nothing is concluded"* (tier 1)
- `comp-imgread` — rc=2, explicit ERROR (tier 1, plain)
- `comp-similar` — rc=2 on empty corpus; **cited at source (`comp_similar.py:438`, `:500-505`), not re-run**, because the original capture went through `nohup` and `$?` was unrecoverable after the fact. I disclosed WHY rather than presenting a captured rc I did not have.

### 2. WS-4 SOURCE<->DEPLOYED crosswalk + conformance suite

**Commit `03c1855a28`** (my ownpath) — 526 insertions:
- `org/modules/graph/comp_ws4_crosswalk.py` (248 lines) — the join rules per entity
- `org/modules/graph/comp_ws4_crosswalk_test.py` (276 lines) — 12-test conformance suite
- `pytest.ini` (2 lines)

Memo `WS4_CROSSWALK.md` at the census path, CTO~Z-committed per the same convention.

Suite: 12 tests including **four mutants** (corrupted normalizer / broken prefix-check /
permissive predicate / corrupted bucket map), each confirmed to actually flip in-session —
not written-and-assumed. The live tier prints its own denominators each run instead of
quoting a frozen number.

---

## Decisions Made

1. **Cite source rather than fabricate a captured rc.** For `comp-similar` I could not recover
   `$?`. I cited `file:line` and disclosed the reason. CVO~Z verified it in seconds instead of
   6-10 minutes and recorded it as the right call.
2. **Floors, not equalities, for the live tier — and labeled as such.** `>= 22` (COMPONENT) and
   `>= 10` (ENDPOINT) are regression detectors. **They carry ZERO correctness force**: a
   threshold fitted to today's observed value cannot distinguish "22 is right" from "22 is what
   we measured." 22/24 must NOT be reported as validated coverage — it is an observed baseline
   with 2 unexplained misses that the floor is structurally unable to surface. CVO~Z upheld
   this labeling and told CTO~Z to state it that way.
3. **Reported the ENDPOINT node over-broadness as a source defect, not a crosswalk gap.**
   `extract_api.py:134-141` builds `endpoint_node_id = f"endpoint:{fn_name}"` then calls
   `graph.add_node(...)` **unconditionally** — no urls-empty guard. Confirmed at source by CVO~Z.

---

## Files Modified

See commit messages: `03c1855a28` (mine), `da1793cda9` + `157f38541e` (CTO~Z, census path).

| File | Note |
|---|---|
| `org/modules/graph/comp_ws4_crosswalk.py` | new — join rules, 4 entities |
| `org/modules/graph/comp_ws4_crosswalk_test.py` | new — 12 tests, 4 mutants |
| `pytest.ini` | new — 2 lines, test discovery |
| `org/mcp/sessions/{session}.serial` | LD-0290 file found MISSING on push and written |

---

## Deployment Sequence

**None — no AWS/Terraform surface touched this window.** WS-4 is a repo-local analysis module
plus its test suite; REC-1c is read-only tool exercise. No Lambda, no bucket, no TF plan/apply,
so Rules 1-6 and the safe-apply HALT gate do not engage. Recorded explicitly because a blank
deployment section on an AE log should never be read as "not checked."

## Verification

Independent, by `3.0.0_SA_CVO~Z`, both green — and both RE-RUN rather than read:

- **WS-4** (`20260725T082210Z`): *"12/12 PASSED including all four mutants ... 5.61s, TRUE_RC=0."*
  ENDPOINT over-broadness citation confirmed at source, line numbers accurate.
- **Lane-B REC-1c** (`20260725T083610Z`): *"17/17 reconciles"*, all 5 mismatches verified —
  4 live-re-derived with CVO~Z's own probe strings, 1 by the source citation as committed.

CVO~Z's denominator note, banked: my `comp-grep` denominator was 23754, theirs 23814. That is
**correct live behavior, not drift** — the tool counts the real working set each run. A *moving*
live denominator is a feature; only a *frozen* one is suspect.

---

## Blockers

None.

---

## Current State

Both dispatches are CLOSED and independently verified. Nothing is pending on me.

- **WS-4** = TOOLUNIFY exit-bar item 1 of 2. Code at `03c1855a28`; memo `WS4_CROSSWALK.md` at
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/`. Suite runs green from the
  workspace root via `pytest org/modules/graph/comp_ws4_crosswalk_test.py`.
- **Lane-B REC-1c** = closed; all five lane batches + REC-1/1b are now fully CVO~Z-verified
  (`c2f28c521c`, `14c7a819a5`). Per CTO~Z's dispatch, WS-4 + WS-7 green means **COMPLEARNS
  opens** per the ontology docs.
- **Lane-B's census contribution, stated as CVO~Z ranked it:** 4 of 5 mismatches are the
  register UNDER-stating its tools. Every prior framing in this program was "the register
  over-promises." A reader hitting a MED-confidence FAIL-OPEN row should now distrust **the row**
  before the tool.

**OPEN ITEMS I RAISED AND DID NOT CHASE — they are `1.0.0_SA_CTO~Z`'s call, not mine, and my
floors are structurally unable to catch them:**
- 2 unexplained COMPONENT misses (22/24).
- The ENDPOINT 55-miss partition's 10 genuine deployed gaps.

**Session/infra state:** registered LIVE (PID 19112); inbox Monitor armed as task `bjy0steda`
(proc 908038, ppid live); inbox empty on both probes; zero crons. LD-0290 session-serial file
written this session.

**Environment hazards live in this shell, both already banked in MEMORY:** the Cygwin harness
appends a spurious exit-1 to every Bash call (capture `TRUE_RC` in-stdout), and this shell
resolves `/cygdrive/c/...`, NOT `/c/...` — a `cd /c/...` fails outright.

---

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Disposition the two open items above (2 COMPONENT misses; 10 ENDPOINT
   deployed gaps). Also holds the WS-4 + WS-7 exit-bar call that opens COMPLEARNS.
2. **[1.0.0_SA_CTO~Z]** Andrew-direct first task this cycle is a review of message-inbox work
   across all six CloudComp lanes — Lane-B's inbox is drained and its two threads are closed;
   available on request.
3. **[0.8.0_AE_CloudComp~B]** Standing by, event-driven. No self-armed loops (LD-0157).
