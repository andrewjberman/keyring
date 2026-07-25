# NFRA_TOOLUNIFY §2.D rework — CVO~Z held-back control (PASS 85%) + a false-positive risk it couldn't test — 0.8.0_AE_CloudComp~D

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, VALIDATE

**Date:** 2026-07-24 (continued into 2026-07-25 UTC)
**Task Order:** NFRA_TOOLUNIFY census rework, follow-on to the §2.D delivery earlier this session
**Status:** COMPLETE

---

## Objective

Respond to CVO~Z's held-back verification result (sealed set, committed before my deliverable existed):
PASS at 85% (35/41 real pairs), 6 real misses in one class (variable-bound artifact paths). Fix the root
cause, then — per CVO~Z's sharper follow-up — measure whether the fix silently changed any EXISTING
attribution across the whole 92-tool register, not just filled in the 6 known misses.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| Native `Grep`/`Read` | source verification of the 3 real-looking identity changes the before/after diff surfaced | PASS | needed to confirm which value (before or after) was actually correct — 2 turned out to be a regression in my own new feature, 1 confirmed the AFTER value fixed a genuine bug in the originally-delivered register |
| `.tools/commit-gate.sh` | py_compile + ds-precommit-check + ruff on the 3 durable classifier scripts | PASS (1 ruff finding fixed: unused `sys` import) | |
| `comp-manifest-check` (indirect, via safe-commit's auto-invoked advisory scan) | fired on my OWN documentation text describing the false-positive class (matched "kuzu.Connection"/"graph.json" substrings inside an explanatory string, not live code) | ADVISORY, not blocking | a small, apt illustration of the exact defect class this whole census documents, tripped by prose ABOUT it |

**What worked:** writing a purpose-built before/after diff script (not sampling, not reasoning) was the only way to actually answer CVO~Z's question — and it caught a real regression in my OWN rework (the return-value-resolution feature) before it shipped a second time.

**What failed:** N/A this session.

**Gap found:** N/A — see prior session's compiler-tools log entry for the standing gap (no comp-tool for cross-tool import-closure analysis).

Appended to `org/compiler-tools-log.md`.

---

## Work Completed

### 1. Diagnosed the held-back control's 6 real misses
All one class: a path bound to a local variable (`rp = os.path.join(..., "nerves-risk-edges.json")`) then
read later (`open(rp)`) — the classifier's `ConstCollector` was a single flat dict across an entire module,
so a short, commonly-reused local name collides across unrelated functions in a 700-line file.

### 2. Fixed via function-scoped const resolution
Added `ShallowVisitor` (collects a scope's own statements without descending into nested Function/Class
defs) and restructured `analyze_module` so each function gets an independent local-variable namespace
seeded from module-level consts, rather than one flat whole-file dict. Also added return-value resolution
for simple single-return path-builder helper functions (the `comp-iam` miss specifically: the literal lives
inside a callee's `return`, not the call site's own args) and 4 new `DERIVED-CACHE` vocabulary entries.

### 3. CVO~Z's follow-up: measure the false-positive risk, not just the false-negative fix
A flat namespace doesn't only drop bindings — it can hand a DIFFERENT call site a confidently wrong
artifact. Wrote `diff_before_after.py`: indexed every resolved (module, lineno, kind) call site before and
after the fix across all 92 tools, diffed. Result: 7057 identical, 726 new correct resolutions, 139 changed,
0 lost. Triaged the 139 by whether an actual file-identity token differed (vs. cosmetic noise-word drift):
131 cosmetic, 8 apparent real changes.

### 4. Ran the 8 down individually rather than trusting the diff
7 of 8 traced to a REGRESSION in my own new return-value-resolution feature: `_abs(p): return
os.path.join(WORKSPACE_ROOT, p)` was being treated as a fixed constant, discarding the parameter that was
the actually-meaningful part (`_abs(ROLLING_LOG)` resolved to `WORKSPACE_ROOT`'s own fragments instead of
`ROLLING_LOG`'s literal). Fixed with a guard: only treat a single-return helper as a safe constant if its
return expression carries its own string literal (survives regardless of parameter value) — disqualify it
if the return is entirely parameter/external-name-derived with no self-contained literal.

The 8th (`comp-types`, `types_cli.py:356`) was a GENUINE bug in the ORIGINALLY DELIVERED register: a
`manifest_path` local reused across two unrelated functions in the same file resolved to the WRONG
function's filename (`.fields.yaml` instead of `.blast.yaml`). Confirmed by reading `types_cli.py:340-356`
directly — the write at :356 sits inside the function that assigns `.blast.yaml` at :352.

### 5. Re-ran the full diff after the guard fix
Final: 1 real identity change (the confirmed-correct comp-types fix), 0 unexplained. Regression-checked all
4 published gate cases + both held-out self-check tools (comp-secrets, comp-lambdamap) after every fix in
this chain, not just once at the end.

### 6. Moved the classifier to a durable, committed location
Per CVO~Z's explicit ask: `census_classifier.py`/`census_annotate.py`/`census_finalize.py` had lived in
gitignored `.comp-graph/tmp/` and would have died with the session. Copied to
`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_TOOLUNIFY_CENSUS_TOOLS/` (own owned path),
made the classifier self-contained (live tool-universe enumeration instead of a companion scratch file),
documented known residual limitations in the module docstring, ran the commit gate (caught + fixed one
unused-import lint finding), committed at `2779752ac`.

### 7. Redelivered
Updated `D.md` (new §10 addendum covering the whole arc + the measurement table), `D.sidecar.json`,
`D.raw_evidence.json` in place on disk (same owned-paths constraint as the original delivery — cannot
commit into `org/tier1_exec/1.0.0_SA_CTO/**` myself). Notified CTO~Z (re-commit needed; flagged that their
`CONSOLIDATED_ESTATE_MAP.md` already tracks this as a known pending item at line 146, which now closes) and
CVO~Z (full measurement) by MCP.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Function-scoped (not fully lexically-scoped) const resolution — nested functions seed from module consts only, not their immediate enclosing function's locals | Bounded, documented gap; rare in this codebase's flat-top-level-function style; building a full scope tree was disproportionate to the actual defect class found |
| Guard return-value resolution on "has its own literal", not "references no parameters" | The blunter guard would have DISQUALIFIED `_managed_policy_cache_path` (the actual comp-iam fix target) along with `_abs` (the regression) — both reference a parameter, but only one carries a meaningful literal independent of it |
| Run the before/after diff BEFORE redelivering, even though CVO~Z said "no rush" | The measurement is what makes the register trustworthy rather than merely re-asserted; matches the standing project discipline (measure, don't reason) |
| Make the durable classifier self-contained (live enumeration) rather than shipping the companion scratch file too | A committed instrument with a hidden dependency on an uncommitted file is the same "artifact with no producer" shape CVO~Z flagged, one layer down |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_TOOLUNIFY_CENSUS_TOOLS/census_classifier.py` | New (moved + fixed + made self-contained) | Yes — `2779752ac` |
| `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_TOOLUNIFY_CENSUS_TOOLS/census_annotate.py` | New (moved) | Yes — `2779752ac` |
| `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_TOOLUNIFY_CENSUS_TOOLS/census_finalize.py` | New (moved) | Yes — `2779752ac` |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/D.md` | Updated table + new §10 addendum | No — owned-paths gated to CTO~Z, written to disk for their re-commit |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/D.sidecar.json` | Regenerated | No — same as above |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/D.raw_evidence.json` | Regenerated | No — same as above |

This log itself, committed under my own path.

---

## Blockers

None.

---

## Current State

Rework complete and measured. All 6 of CVO~Z's held-back misses now resolve; the false-positive risk CVO~Z
flagged was measured (not reasoned about) and found real but small (1/7196 resolved-in-both call sites),
confirmed correct against source. A regression in my own rework was caught by the same measurement before
it shipped a second time. Durable classifier committed; deliverable redelivered on disk; both CTO~Z and
CVO~Z notified with the full measurement. Standing by for CVO~Z's re-verification or a next dispatch.

---

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Re-commit the updated `D.md`/`D.sidecar.json`/`D.raw_evidence.json`; close the
   line-146 tracked item in `CONSOLIDATED_ESTATE_MAP.md`.
2. **[3.0.0_SA_CVO~Z]** Re-verify against the redelivered register; the durable classifier scripts are now
   at a committed path if a fresh re-run is wanted instead of trusting this log.
3. **[0.8.0_AE_CloudComp~D]** Event-driven, standing by.
