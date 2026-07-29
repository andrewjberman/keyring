# comp-manifest-check post-cache remainder closed (Andrew-direct handoff via CVO)

**archetype:** DIAGNOSE

**Session:** 0.8.0_AE_CloudComp base, fresh session ~0033Z-0057Z 2026-07-29.
**Trigger:** CVO HANDOFF (inbox 20260729T003253Z, Andrew-direct) delivered at /watcher arm --
profile what remains inside `_completeness_invariants` after the YAML cache (@fe477c2629) and get
the per-file check into comp-coverage-check's ~538ms band so the blocking flip is free.

## What was found (cProfile, live module, post-cache)

The ~1.8s/file was NOT one hot function inside the family's logic -- it was yaml parsing that
BYPASSED the cache plus every parse paying pure-Python SafeLoader:

| cost | where |
|---|---|
| 0.80s | `_section_pair`: `git show` + 2x full-manifest parse per call, uncached, called by 3 members |
| 0.66s | `.tools/comp-routable-check` `_load`: 2x SafeLoader parses (manifest + coverage-map) |
| 0.74s | `comp_capability_provider`: 2x SafeLoader parses (manifest + coverage-map) |
| 0.16s | `comp_output_contract`: contracts + rule bank SafeLoader |
| ~0.12s | `_placement_invariant`: raw open+safe_load (cache bypass) |

Also discriminated early: an ORDINARY data-script file was already in band (362ms) -- the expensive
class is any `.tools/`-touching or substrate-touching file (fires the completeness family).

## The fix (@b917f2fafd, pushed)

1. `manifest_check_cli.py`: `load_yaml` -> CSafeLoader (libyaml; 9.2ms vs 117.7ms on the 133KB
   manifest, 12.8x; SafeLoader fallback); `_section_pair` parsed-(old,new)-pair cached per path
   (deepcopy'd sections -- mutability contract preserved); `_placement_invariant` routed through
   cached `load_yaml`.
2. `.tools/comp-routable-check` + `comp_capability_provider.py` + `comp_output_contract.py`:
   LOADER SWAP ONLY -- no caching, no shared state, so the load_config-mutation trap CVO flagged
   for caching structurally cannot apply.

## Verification (CVO's parity bar)

- CSafeLoader parse-equality (parsed-doc ==) proven on ALL 5 YAMLs the gate reads, before editing.
- stdout/stderr/rc BYTE-IDENTICAL across 7 cases (ordinary .py, non-tools .sh, .tools file,
  manifest touch, 3-file batch, selfcheck [tempfile-masked], list), live module at its real path,
  baselines captured PRE-edit on the same box/instrument.
- The 68-tool NEARTIE WARN wall that appeared when the provider was touched: controlled A/B
  (HEAD provider vs patched, identical inputs) -> verdicts IDENTICAL. PRE-EXISTING standing state,
  not introduced. comp-which live smoke: comp-blast still rank-1, ~0.96s.
- selfcheck PASS; commit-gate clean; comp-system 06 regenerated (currency gate blocked the first
  commit -- correct behavior, source-touch on stale 06).

## Measured (median-of-5, subprocess CLI)

    ordinary .py      362ms -> 133ms
    .tools file      1176ms -> 467ms     (the pre-cache 1.8s+ class)
    manifest touch   ~717ms -> ~520ms
    5-file mixed commit via commit_gate_runner: 2.39s total (bulk = per-.py ruff subprocess)

DELIVERABLE MET: worst per-file class is inside coverage-check's ~538ms band. The blocking-flip
decision itself left to CVO/CTO (not mine to make on the gate that polices everyone's commits).
Independent re-verify requested from CVO (their offer) via MCP 005727Z.

## Open / residual

- `git ls-files .tools/` spawns twice per completeness batch (existence + registration,
  ~130ms/spawn) -- dedupe available if the band tightens.
- comp-which's own reparse tax (10 parses/call) remains with the routed comp-which wiring work;
  the provider loader swap already cut part of it.
- Fits `NFRA_TOOLARCH.LATENCY` (one derivation's wallclock, measured before/after).

## Compiler Tools

| tool | result |
|---|---|
| `comp-glob` x2 | located manifest_check_cli.py + commit_gate_runner.py (on-rails) |
| cProfile on live cmd_check (before + after) | cost located then re-attributed to the 5 leak sites; not assumed |
| parity harness, 7 cases x 2 arms | byte-identical stdout/stderr/rc |
| self-route A/B (HEAD vs patched provider) | verdicts identical -- NEARTIE wall pre-existing |
| `comp-which` live smoke | routes correctly post-change, comp-blast rank-1 |
| `comp-system` | 06_current_state regenerated (currency gate) |
| `.tools/commit-gate.sh` | clean on all 3 .py files |
