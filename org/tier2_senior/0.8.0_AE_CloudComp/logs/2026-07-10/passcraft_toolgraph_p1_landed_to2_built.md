# NFRA_PASSCRAFT + NFRA_TOOLGRAPH -- P1 foundations LANDED, TO-2 emitter built + routed

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

**Serial:** 0.8.0_AE_CloudComp (base) - **Window:** session start (~19:13Z) -> 20:40Z, 2026-07-10
**Mandate:** Andrew-authorized (COO~A GO 1913Z), tool-check-gen builder. Built PASSCRAFT-TO-1 +
TOOLGRAPH-TO-1 (the assurance program's two P1 foundations), then PASSCRAFT-TO-2 (the ToolAudit CSE emitter).

---

## What happened (the arc)

1. **Startup + a stale-dispatch tie-break.** /watcher (re-registered, armed Monitor), drained inbox.
   Found a genuine cross-lane conflict: base-COO's [STOP] on the TO-7/TO-8 *harness* (superseded --
   "we are not building a harness") vs COO~A's GO for the anti-harness REPLACEMENT (PASSCRAFT/TOOLGRAPH).
   SURFACED to CTO~A rather than adjudicating; held all artifact production until GO. CTO~A + both COO
   lanes confirmed the read. Zero harness code was ever written. (LD-0276-class stale-GO hazard, caught.)

2. **TOOLGRAPH-TO-1 (measure-only) -- LANDED.** comp-toolgraph {census,edges,coupling-diff,denominator}.
   C0 = the ratified AC-0 63-universe; C1 = mechanical SHARES_SUBSTRATE/WRITES/INVOKED_BY. The
   load-bearing coupling diff surfaced **14 UNDECLARED code-coupling ripples** the resource-keyed
   coverage-map is blind to (grain_sentinel: comp-aws<->{blast,build,diff,trace,xref} ripples to 6 tools
   declared nowhere; the cli.py dispatcher cluster; comp-routable-check<->comp-which via comp_route).
   AC1 go-red PROVEN (pure coupling_diff(): seeded undeclared edge flagged, declared not, R6 empty).
   Denominator reconciled to ONE number (63) + derivation.

3. **PASSCRAFT-TO-1 (anti-harness) -- LANDED.** comp-passcraft recon/taxonomy. 8 moves + 12-shape
   hunt-order + archetype->probe map (authoritative taxonomy). AC1/AC4 proven STRUCTURALLY: recon()
   returns an evidence pack with NO verdict/pass/fail key anywhere (_has_verdict_key recurses + asserts
   absence) -- shown UNABLE to conclude. recon 63/63 no crash, 0 verdict-leaks. AC5 class-agnostic.

4. **Owned-paths SoD, resolved cleanly.** Initial commit blocked (org/modules/graph/*.py = ANY_EXEC).
   Fix per the ratified NFRA_TOOLCHECK_P4 precedent: renamed backends to comp_*.py (=ANY_EXEC_OR_AE,
   AE-maintainable); decoupled comp_passcraft from the census JSON (imports annotations from the
   comp_toolgraph module = one home). Residual 2 files: arch doc SoD-committed by CTO~A (d0bc8b227);
   census lane-add ratified (437baef60, COO~A grantor) -> I committed the census (7ada68837).

5. **PASSCRAFT-TO-2 (ToolAudit CSE emitter) -- BUILT + routed, HELD for CTO~A arch-gate.** Reuses the
   DS-built cse_schema.py (NFRA_CSE contract) + comp_ladder fidelity -- no rebuild. A ToolAudit maps
   into a valid NFRA_CSE CSE (subject=Tool, verb=reclassify, provenance.evidence=evidence_ref). Anti-
   harness ONE LAYER UP: a ToolAudit is POST-verdict so it legitimately carries the hand-authored
   verdict; the proof is "NO verdict-DERIVING code path" (emit REQUIRES a hand-authored verdict, fails
   closed without it; a structural test asserts no compute/derive/judge fn). AC2 fidelity via
   cse_schema.validate + a ToolAudit evidence_ref RESOLVE check. R0 DEFERRED (R1 self-class only; no CVO
   route). Wired into recon (recon_mechanical_fields).

6. **Side task:** answered 0.7.0_AE_CloudOps~C's forward-dep check -- NFRA_MSGRAPH has no live consumer
   of debtscan_scorecard_latest.json (the census re-homes to the live canon_motif_scorer.py, all 4
   canon classes); cleared the CM1 delete + re-pointed my own design-doc citation (8a057c53d).

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-which | probed 3 input classes (TRUE row / gibberish / answerable-unmatched) | PASS | observed the live output grammar with my own eyes before parsing (COO's Bug-2 lesson); zzqq now FALLS BACK (was CONFIDENT in the founding brief) -- banked INFERRED |
| comp-toolgraph | census / edges / coupling-diff / denominator / --self-test (BUILT) | PASS | AC1 go-red proven; 14 undeclared ripples; recon-robustness 63/63; declared-parse yaml==fallback==25 |
| comp-passcraft | recon / taxonomy / emit / --self-test (BUILT) | PASS | anti-harness structural (no verdict key in recon; no verdict-deriving path in emit); self-test 8/8 TO-2 |
| comp-grep | via comp-which fallback (zzqq probe) | PASS | on-rails, confirmed the fallback executes comp-grep |
| ruff (commit-gate pin 0.15.11 py39) | check on all 4 .py | PASS | clean on every landed + routed file |

**What worked:** grounding the tool MECHANISMS at source before building (comp_route.py:362 two-layer
conflation caught -- CLI fixture vs live wrapper); reusing cse_schema.py/comp_ladder for TO-2 (unify-not-
build). **What failed:** first commit blocked on owned-paths (org/modules/graph/*.py=ANY_EXEC) -- the
correct control; fixed by the comp_*.py rename convention. **Gap found:** the two new tools (comp-toolgraph,
comp-passcraft) are net-new, NOT in the ratified AC-0 63 -- a catalog-reconciliation follow-up (flagged,
not force-fixed).

## Blockers

**None.** TO-2 is HELD for CTO~A's arch-gate (the mandated diff-gate, a hard external gate stated plainly),
not blocked. TO-1 fully landed.

## Current State (handoff surface)

- **LANDED + pushed on origin/CLOUD:** 15c8524a4 (both P1 tools + tests + coverage-map registration,
  7 files), 7ada68837 (census JSON under the lane-add), 8a057c53d (NFRA_MSGRAPH doc re-point). Arch doc
  d0bc8b227 (CTO~A SoD). All commit-gate + coverage-check (65 tools) GREEN.
- **Files:** org/modules/graph/comp_toolgraph.py (engine) + .tools/comp-toolgraph; org/modules/graph/
  comp_passcraft.py (recon + taxonomy + the TO-2 emit section) + .tools/comp-passcraft; census
  comp_toolgraph_census.json; tests test_tool_graph_coupling_diff.py (7) + test_passcraft_anti_harness.py
  (17, incl 7 TO-2); docs/architecture/PASSCRAFT_RECON_REFERENCE.md. Registered in comp-coverage-map.yaml
  meta_tools[].
- **TO-2 LANDED + pushed:** 1b2d5287d (comp_passcraft.py emit section + test_passcraft_anti_harness.py,
  2 AE files, no SoD; CTO~A GO 204007Z, verified anti-harness against the test). Exercised: pytest 24/24,
  self-test all PASS, ruff clean.
- **comp-passcraft emit <tool> --audit <hand-authored.json>** -> {tool_audit, cse}; cse validates @ NFRA_CSE
  schema 0.4; fail-closed on empty/unresolvable evidence_ref or missing verdict.

## Next Steps

1. **[2.0.0_SA_COO~A]** RAVC on TO-2 land (1b2d5287d) -- TO-2's ToolAudit stream now unblocks
   NFRA_PASSCRAFT.TO-3 (backfill the 3 completed passes) + NFRA_TOOLGRAPH.TO-2 (the Assurance plane reads
   the stream). Ready for the next dispatch.
3. **[me / catalog]** reconcile comp-toolgraph + comp-passcraft into the ratified AC-0 63 universe (a
   catalog-reconciliation follow-up; they are in meta_tools[] but not the AC-0 predicate).
