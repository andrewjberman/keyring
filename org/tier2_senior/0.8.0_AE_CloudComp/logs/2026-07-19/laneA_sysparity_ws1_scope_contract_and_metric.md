# NFRA_SYSPARITY WS-1 -- scope contract + reproducible per-domain parity metric (0.8.0_AE_CloudComp~A)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

## Summary

COO sequenced my next NFRA item off the NESTEDABSTRACT P2 close: NFRA_SYSPARITY WS-1 (GO @201229Z, TO
@d60d4584a). WS-1 = the FIRST + gating workstream -- it defines the parity-metric DENOMINATOR that all
WS-2..8 measurement rests on, and its landing is the charter signal for NFRA_ONTOCLARITY. Delivered both
halves + landed @62b28c5fb. Doctrinal core: VERIFICATION-LAW #6 (print the denominator; never count the
out-of-scope estate as a gap) + CONTROLS-OVER-CARE (the metric is the honest denominator the WS-2/WS-3
fail-closed controls measure against).

## What shipped (commit @62b28c5fb, origin/CLOUD)

- **(A) infra/system/README.md -- the SCOPE CONTRACT.** Commits the tree to the 4 charter domains
  (engineering / ontology / comp-tools / infrastructure, LD-0318). ONTOLOGY ruled IN (PRD S2.1) -- closes
  the brief's un-declared omission: the ontology's thin representation is a gap to CLOSE (WS-4), NOT a
  boundary; its prior absence was oversight, not scoping. SCOPING-not-OVERSIGHT made grep-provable. The 2
  excluded estates (client-data pipeline INF/49F/COT/TAXSMA/OPAL_ASSETS + taxonomy/consolidation plane)
  marked CONFIRMED OUT not widened (PRD S2.2) with sibling-class + pointer.
- **(B) infra/system/scope_contract.json** -- the README contract's machine-readable DATA TWIN = the
  metric's DENOMINATOR source (so the printed contract + measured denominator can never drift apart).
  Per-domain declared in-scope UNITS (each a grounded check) + the NAMED exclusions.
- **(B) infra/system/system_parity.py** -- the reproducible per-domain parity command. parity =
  (declared in-scope units mechanically PRESENT + CURRENT) / (mechanical units), per domain. Denominator
  PRINTED, exclusions NAMED + never counted (VL#6). Currency REUSES comp-system's own signal (invokes
  `python org/modules/graph/comp_system.py --check`, no parallel axis). `--json` for CVO reproducibility.
  rc 0 (a REPORT, not a gate -- WS-2/WS-3 are the fail-closed controls).

## Exercised (TO compiler-tools-mandate phases 1-3)

| Phase | Run | Result |
|---|---|---|
| 1 | `comp-system --check` | SYSTEM CURRENT (0 drifted) -- the PRD S1 STALE premise HAS MOVED (see baseline-shift) |
| 1 | `ls infra/system/ + read README/06` | enumerated; ontology absent from core docs (0 files) = the gap the contract closes |
| 2 | `python system_parity.py` | per-domain parity emitted, denominator PRINTED, exclusions NAMED; out-of-scope NOT counted (VL#6 verified) |
| 3 | grep README exclusion pointers | ontology stated IN (2x) + both exclusions named + CONFIRMED-OUT + SCOPING-not-OVERSIGHT + scope_contract/metric pointers -- all grep-provable |

PARITY @HEAD (mechanical-coverage axis): **comp-tools 100% / infrastructure 75% / engineering 80% /
ontology 50%.** VL#6 verified: no out-of-scope estate (INF/49F/COT/TAXSMA/OPAL_ASSETS/taxonomy) is a
scored unit -- they appear ONLY in the named exclusions.

## Baseline-shift finding (surfaced per the TO phase-1 if_mismatch)

comp-system --check reports CURRENT, not the PRD S1 STALE premise. Grounded cause = a COORDINATED sibling
landing: **0.8.0_AE_CloudComp~D's WS-2 part-a @4e5a78abc** (9 min before I picked up WS-1) de-staled 06 to
CURRENT + bumped cse_schema 0.4->0.5 -- SINCE the brief was written. So several brief assumptions are
ALREADY CLOSED, and my metric measures the IMPROVED state (why comp-tools/eng score above the brief's
~85/70-75). This IS the LD-0318 regime working: the brief numbers were assumptions; the live metric
re-grounds them. Surfaced to COO + flagged to CVO for the standing burn-down. Not an alarm.

## Cross-domain coordination (WS-4 / ~C, resolved same-session)

3 calls from ~C's WS-4 landed in my lane; all answered grounded: (1) grep_present = ANY-of (a hand-doc
citation satisfies the ontology unit; no 06 change); (2) sdk/00_manifest/schema.json is NOT in my
drift-gate surface_map (33 surfaces, 0 sdk/ paths) -> WS-4's SDK-binding half needs no trailer; (3)
static-vs-forward split confirmed (WS-4 static binding; my NESTEDABSTRACT forward loop stays mine; WS-6
SLAs the debt). RULED the one open call: ~C's Part-A ontology-citation-add to a 0*_*.md core doc (which IS
my NFRA_SYSTEM surface) carries `abstraction-ledger: n-a` -- a doc citation of an already-ratified artifact
is not a mechanism enhancement (the ontology->SDK abstraction is tracked in WS-4's SDK half + NESTEDABSTRACT
NA rows, not lost).

## Compiler Tools

| Tool | Verdict | Note |
|---|---|---|
| `comp-system --check` (phase 1) | STALE->CURRENT | premise-move detected + grounded to ~D's WS-2 part-a @4e5a78abc |
| `system_parity.py` (built) | PASS | reproducible per-domain metric; denominator printed, exclusions named, VL#6-clean; reuses comp-system |
| `.tools/commit-gate.sh` | PASS | system_parity.py: py_compile + ds-precommit + ruff py39 clean |
| `safe-commit` surface-check + risk-reflex | CLEAN | 3 files, no critical surface |

What worked: the machine-twin design (scope_contract.json) makes the printed contract and the measured
denominator the SAME artifact -- they cannot drift, the exact frozen-vs-live discipline SYSPARITY is about.
What the exercise caught: (1) the .tools/comp-system PATH shim is not subprocess-executable on Windows ->
invoke the impl (`python comp_system.py`) directly; (2) comp-system's staleness is HEAD-advance-sensitive
(a snapshot goes stale on any commit since regen, distinct from a managed-metric content drift -- the
message now distinguishes them); (3) the PRD S1 premise had already moved (~D). Gap found: none blocking;
the metric's axis + numbers are ASSUMPTIONS until CVO re-grounds (LD-0318).

## Files Modified

See commit message: 62b28c5fb (infra/system/: scope_contract.json [new], system_parity.py [new],
README.md [scope-contract section + boundary CONFIRMED-OUT mark]).

## Blockers

NONE. WS-1 landed. It is NOT "done" until CVO re-grounds the denominator + metric (LD-0318 / PRD S7 gate,
in ADDITION to RAVC) -- pinged CVO @214204Z. That is the gate, not a blocker.

## Current State (handoff, zero-context)

NFRA_SYSPARITY WS-1 landed @62b28c5fb. The scope contract lives in infra/system/README.md ("## Scope
contract") + its machine twin infra/system/scope_contract.json. The parity metric is
`python infra/system/system_parity.py` (add `--json` for machine output; `--domain <name>` to scope one).
It emits per-domain parity (comp-tools 100 / infra 75 / eng 80 / ontology 50 @ this HEAD), prints the
DECLARED-scope denominator, names the 2 exclusions, and never counts an out-of-scope estate as a gap. The
denominator is deterministic given HEAD (grep/presence over the tracked /system tree + one comp-system
--check). It reuses comp-system's staleness signal (no parallel axis). WS-1 gates all downstream
measurement + is the ONTOCLARITY charter signal (pinged MSTR).

## Next Steps

1. **[3.0.0_SA_CVO]** LD-0318 verify (WS-1 not done until): re-ground the denominator (verify no out-of-scope
   estate is counted) + the per-domain numbers (against LIVE state, noting the brief baseline moved via ~D's
   WS-2 part-a) + the metric axis. /molecule scope_contract + /verify system_parity + /prd-delta WS-1.
   Pinged @214204Z; I fold corrections same-turn.
2. **[2.0.0_SA_COO]** sequence WS-2 (part-b fail-closed gate, CTO arch-gate; ~D did part-a) + WS-3 (drift-gate
   denominator -- fold RULE_BANK.yaml/variance_dimensions.yaml into my NFRA_ONTOLOGY surface) -- both now have
   the honest WS-1 denominator to measure against. GO when ready.
3. **[0.0.0_AB_MSTR]** charter NFRA_ONTOCLARITY on this WS-1 land (PRD S8); its clarified definitions feed WS-4.
4. **[0.8.0_AE_CloudComp~A / me]** available for WS-3 (my drift-gate denominator lane -- natural continuity)
   or a CVO-driven metric correction, on COO's sequence.
