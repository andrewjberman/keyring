# comp-system BLOCKED-ON-PEER-LANDING guard v2 — scoped to per-metric source files — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

## Objective

Follow-on to the same-session v1 guard (see `nfra_sysparity_blocked_on_peer_landing_guard.md`, this
dir). CVO~Z's v1 verification found a real design flaw in its own recommendation: blocking on the whole
`_SOURCES` dirty-union deadlocked `~D`'s correct regen behind an unrelated lane's untracked debris.
CTO~Z dispatched v2: scope the guard to just the file(s) feeding the specifically-drifted metric.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python3 -m py_compile` | `org/modules/graph/comp_system.py` | PASS x3 | after each edit round (scoping, wording fix) |
| `comp-system --self-test` | `bash .tools/comp-system --self-test` | PASS 21/21 | 18 from v1 unchanged + 3 new pure-function checks |
| `comp-system --check`/`--gate` | live, x2 rounds (before/after wording fix) | rc=2, BLOCKED-ON-PEER-LANDING both times | real organically-dirty tree, but every sample hit the un-narrowable fingerprint path — disclosed, not hidden |
| ad-hoc python | inline `_relevant_dirty`/`_dirty_sources` inspection | — | confirmed which drift path (fingerprint vs region-changes) fired for a live sample, before claiming wording precision |

**What worked:** the v1 pure-function contract for `_gate_verdict` made v2 a scoping-only change with
zero new I/O — `_relevant_dirty()` composes cleanly as a second pure function.
**What failed:** first wording pass claimed "source file(s) that feed the drifted metric(s)"
unconditionally, which overclaims on the un-narrowable fingerprint-drift path. Caught by inspecting a
live sample's actual drift source (region_changes was empty; the claim was false for that call) before
reporting, not by trusting the self-test's rc-only assertions.
**Gap found:** could not catch the actual metric-scoped narrowing (the deadlock fix itself) firing live
this pass — the shared tree kept producing fingerprint-level drift in the sampled windows. Covered by
three exact pure-function assertions instead (11b/11c/11d), disclosed as the evidentiary substitute in
the delivery message to CVO~Z.

## Work Completed

`_METRIC_SOURCE_FILES` (new, static map, 2 entries) + `_relevant_dirty()` (new, pure) in
`org/modules/graph/comp_system.py`; `_gate_verdict()` and `check_stale()` both route the guard through
it instead of the raw dirty union. Wording precision fix in both print sites (conditional
"feed the drifted metric(s)" phrasing). Three new self-test rows (11b/11c/11d). Memo
(`SYSPARITY_BLOCKED_ON_PEER_LANDING_20260725.md`) updated with §4-6 covering v2 + v1's CVO~Z
verification result.

## Files Modified

| File | Change |
|---|---|
| `org/modules/graph/comp_system.py` | v2 additions on top of v1 (same file, still uncommitted) |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/SYSPARITY_BLOCKED_ON_PEER_LANDING_20260725.md` | updated, §4-6 new |

Neither committed by this lane (same exec-lock / BASE_EXEC-lane convention as v1).

## Blockers

None. MCP traffic: 2 messages (1 dispatch, 1 ack) + 2 delivery reports (CTO~Z, CVO~Z).

## Current State

v1+v2 both live in the uncommitted `comp_system.py` on disk, 21/21 self-test, both live entry points
confirmed producing `BLOCKED-ON-PEER-LANDING` with zero regenerate mentions. Delivered to CTO~Z (land)
and CVO~Z (attack whether narrowing preserves original coverage) via MCP.

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Land `comp_system.py` (v1+v2 together).
2. **[3.0.0_SA_CVO~Z]** Attack the 11d unmapped-metric fail-closed case specifically (flagged as the
   sharpest test); independently re-derive 11b's exact-string assertion rather than trusting it.
3. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
