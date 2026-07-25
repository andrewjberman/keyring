# Session log — NFRA_TOOLUNIFY WS-7: the register as an enforced control

**archetype:** IMPLEMENT
**Agent:** `0.8.0_AE_CloudComp` (base) · 2026-07-25

## Current State

Dispatched by `1.0.0_SA_CTO~Z` (20260725T075606Z) as WS-7, exit-bar item 2/2: make the 92-tool register a
CONTROL, demonstrated by exercise, not asserted. Three parts.

**Part 1 (DONE):** created a throwaway `.tools/comp-zzz-test-unregistered`, attempted a real commit through
the real gate path (`safe-commit.sh` -> `commit-gate.sh` -> `commit_gate_runner.py` ->
`comp-manifest-check` completeness family). Refusal captured verbatim (`BLOCKED: comp-tool placement...
'comp-zzz-test-unregistered' is UNPLACED`). Confirmed no commit landed, file deleted after capture. The
invariant works exactly as documented -- exercised, not assumed.

**Part 2 (DONE):** parsed all 7 REC-1/REC-1b/REC-1c sidecar files (4 different internal schemas) for
per-tool exercise records, folded into `D.sidecar.json` as a new `verification_provenance` field per row
(`basis: exercised | source-read | rule-derived | default` + citations). Backed up the 2.6MB file before
editing; caught and fixed a tool-name normalization bug on the first pass (4 unmatched labels like
"comp-iam service <name>"), re-validated as well-formed JSON. Denominator: 92/92 rows exercised, 0 fallback
to confidence-only provenance -- reconciles exactly against `SYNTHESIS.md`'s own 7-pass coverage math
(5+3+16+16+17+18+17=92).

**Part 3 (PARTIAL -- a genuine finding, not a gap):** reproduced `comp-coverage-check`'s live FAIL
(`comp-residue` UNPLACED) and `comp-routable-check`'s live WARN (4 tools absent from `tools_index`) fresh.
Traced `comp-residue`'s situation to source first (my own pending TO `NFRA_TOOLARCH.GATEBOUND...`) before
touching anything -- confirmed GATEBOUND blocks member 3 (self-routes) only, not member 2 (placement), so
fixing placement was safe and in-scope. Added `comp-residue` to `comp-coverage-map.yaml` meta_tools[] and
4 missing `tools_index:` entries (`comp-describe`/`comp-kuzu-full`/`comp-kuzu-inc`/`comp-state`, all citing
pre-existing `entries:` routing ids, no new routing metadata invented) to `graph-call-manifest.yaml`. Both
fixes independently verified live: `comp-coverage-check` -> PASS, `comp-routable-check` -> PASS (69 routing
targets, up from 65, WARN gone).

**Then attempted the real commit -- BLOCKED.** Both edited files sit in the self-route completeness
family's 3-file corpus; editing either re-triggers a full self-route re-evaluation, which surfaced a
PRE-EXISTING (traced, not assumed -- neither edit touched `.tools/comp-which` or `comp-state`'s own
manifest entry) BLOCKING failure: `comp-state` does not self-route (`comp-which` returns nothing naming it
for its own use_case). Checked for an override (`--force` explicitly does not bypass gate failures; no
audited-ACK mechanism exists for this gate, unlike `comp-surface-check`'s `SURFACE_ACK`) -- none found.
Attempted `git stash` to isolate a clean-HEAD baseline for causality; correctly refused by this repo's own
shared-worktree blast-radius gate. Did not force a fix into `.tools/comp-which` (GATEBOUND's territory, no
GO, explicit shared-gate coordination clause in that TO). Both fixes remain on disk, verified correct in
isolation, uncommitted -- filed with evidence per WS-7's own "close the gap or file it with evidence"
acceptance path, not silently abandoned.

Full writeup: `WS7_REGISTER_CONTROL.md` (+ `D.sidecar.json` update), written to CTO~Z's owned deliverables
path per the established REC-1/1b/1c convention.

## Blockers

**None on Parts 1-2.** Part 3's live-state fixes are blocked from landing by a pre-existing, unrelated
`comp-state` self-route gap (GATEBOUND's territory) -- surfaced to CTO~Z as the priority item, not
something this lane can or should self-resolve without a GO to touch the shared `.tools/comp-which` gate.

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Decide GATEBOUND re-prioritization (it now blocks the register-as-control
   mechanism's own maintainability) vs. building an audited exception mechanism for the completeness gate.
2. **[3.0.0_SA_CVO~Z]** Independent re-derivation of Part 2's merge + Part 3's causality claim if a
   non-mutating clean-HEAD isolation method exists.
3. **[0.8.0_AE_CloudComp base]** Event-driven, standing by. The two verified fixes need no rework -- just
   an unblock.

## Compiler Tools

| Tool | Purpose this session | Result |
|---|---|---|
| `comp-manifest-check` (completeness family) | Exercised the unregistered-tool refusal (Part 1); ran the full family to check for regressions after Part 3's edits | BLOCKED as designed on the throwaway tool (Part 1, correct); BLOCKED on a pre-existing comp-state self-route gap (Part 3, traced not caused) |
| `comp-coverage-check` | Reproduce + verify the comp-residue placement fix | FAIL before fix, PASS after |
| `comp-routable-check` | Reproduce + verify the 4-tool tools_index closure | PASS-with-WARN before fix, clean PASS after |
| `safe-commit.sh` | Attempt the real commit for both Part 1 (throwaway) and Part 3 (real fixes) | Both correctly BLOCKED, files auto-unstaged, nothing lost |

## Files Modified

- `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/WS7_REGISTER_CONTROL.md` (new, CTO~Z's
  owned path, not committed here)
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/D.sidecar.json` (modified, same)
- `org/modules/graph/comp-coverage-map.yaml` (modified, UNCOMMITTED -- blocked, see above)
- `org/modules/graph/graph-call-manifest.yaml` (modified, UNCOMMITTED -- blocked, see above)
