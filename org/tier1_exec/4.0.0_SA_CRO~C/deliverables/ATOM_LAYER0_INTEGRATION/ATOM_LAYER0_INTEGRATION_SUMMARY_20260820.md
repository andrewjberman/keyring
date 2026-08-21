# ATOM_LAYER0 integration roadmap - CRO~C (rendered view)

**Status:** PROPOSED | **Seat:** 4.0.0_SA_CRO~C | **Date:** 2026-08-20
**Machine source of truth:** `ATOM_LAYER0_INTEGRATION_ROADMAP_20260820.yaml` (this document is its
rendered view). Schema record: `rule24/DISPOSITION_SCHEMA_RECORD.json`. Guard:
`vintage_guard_report.json`. Bundles: `run_bundles/R###_run.json` (30).

**Mandate:** apply ~A's atom_layer0 mechanics (@47e3a54027) to ~B's resolution census
(@50f35b1099) and disposition every unresolved row (Andrew banked order via MSTR 63326; base CRO
scope-ack 63335 adding the per-row vintage-drift guard).

## Result

All **30 unresolved census rows are dispositioned; residue not_dispositioned = 0.** All 30
compiled through ~A's `--compile-census-row` interface at scale (30/30, 0 failures) -- the
integration seam works as designed. The vintage guard read **30/30 CURRENT_AT_HEAD** (every
evidence surface blob-identical to its pin), so zero rows take `ALREADY_RESOLVED_SINCE_CENSUS`
and no census finding went stale between the census and this integration.

**The headline finding: zero of the 30 is an atomicity failure.** Through the framework's stages:

| framework_closing_stage | rows | meaning |
|---|---:|---|
| S4_BINDING_REPAIR | 17 | a binding to a DECLARED authority fails the resolution predicate |
| S0_NOT_CONCEPT_GRAIN | 8 | record-vs-reality status drift; no authority binding; owner reconciles + banners |
| S3_LEGISLATION_GAP | 3 | no target population declared (C0, C1, Estate_Contracts) |
| INSTRUMENT_GAP | 2 | closing act blocked on a missing instrument capability (R045, R059) |
| S2_CHALLENGE_REQUIRED | 0 | zero rows need an atomicity challenge to close -- itself a finding |

Display dispositions (founding vocabulary, derived by precedence): **1 ATOMIC_BUT_UNBOUND**
(R015 Contract_Record -- ~A's proving certificate stands while 4 bindings stay unresolved) and
**29 FINDING_ROUTED_TO_OWNER**. `DECOMPOSES`, `FULL_RUN_SCHEDULED`, and
`ALREADY_RESOLVED_SINCE_CENSUS` are retained at zero occupancy for layer coverage.

## The collapse: 30 rows -> 14 workstreams

| WS | owner | rows | act |
|---|---|---:|---|
| WS-05 (**ranked first among new acts**) | CTO | 1 | resolves_via run-mode in check_system_definitions.py -- mechanizes the resolution predicate for all 18 resolves_via terms; unblocks the 9/18 completion drive |
| WS-01 | CTO | 2 | comp_legacywriter compile-from-authority (pattern proven in-tree: comp_ontolint loads from rule bank); also discharges R015 binding 4 |
| WS-02 | CTO | 1 | Contract_Record two-homes reconcile (the 4 bindings from ~A's S4 contract table; never silently bundled into method registration) |
| WS-03a | CTO | 7 | ontology-doc status banner sweep -- one repeated delta: "not landed/not built/draft" surviving after the target landed |
| WS-03b | CRO | 3 | derived-doc reconcile (LAYER_FIELD_ANATOMY x2, README index) |
| WS-03c | CVO | 1 | CONTENT_MODULE_DESIGN status update |
| WS-04 | COO | 6 | **HELD BY DESIGN** -- W15 resolver-commit sync; fires on the resolver commit COO already holds; NO dispatch |
| WS-06 | CTO | 2 | Substrate/Estate member reconcile (codebase=0, the lock-down's screaming instance) |
| WS-07 | DS | 1 | Domain anchors 9 declared vs 5 materialized |
| WS-08 | CRO | 1 | Segment one-member reconcile per declared block precedence |
| WS-09a | CRO | 2 | C0/C1 target-population legislation |
| WS-09b | CTO | 1 | Estate_Contracts target-population legislation |
| WS-10 | AE CloudComp | 1 | Chain independent derivation (sequence after WS-04) |
| WS-11 | CTO | 1 | manifest subcommand checker extension (48 UNKNOWN shapes) + 10 drift fixes |

13 dispatchable workstreams cover 24 rows; 1 held-by-design workstream covers 6. Owner row
tallies: CTO 15, CRO 6, COO 5 (held), AE 2, DS 1, CVO 1.

## Full-run nominations (framework track; no row waits on these)

Ranked: **Substrate (PRIME)**, C0, C1 (HIGH), Domain, Estate_Contracts (MEDIUM), Segment
(SECONDARY). Sequencing is base CRO's and Andrew's call.

## Schema note (Rule 24, as widened and scoped 2026-08-20)

The founding parenthetical (decomposes / atomic-but-unbound / finding-routed-to-owner) flattened
three intents on one axis -- "finding-routed-to-owner" is true of EVERY census row by census law.
Split per ~B's own precedent into `census_currency` (guard verdict, carrying base's mandated
`ALREADY_RESOLVED_SINCE_CENSUS`), `framework_closing_stage`, and `atomicity_certificate`, with the
founding vocabulary retained as the derived display mapping. Four-postulate records + word-boundary
token census (14 minted tokens all unoccupied; positive control RESOLVED=218) in
`rule24/DISPOSITION_SCHEMA_RECORD.json`. The `framework_closing_stage` axis's stability frame is a
NAMED partial failure by design: it partitions remedies, so one remedy does not move all values.

## Controls run

- validate_run.py --self-test: PASS 10/10 (failure limbs discriminate) before any compile.
- Batch compile: 30/30 OK, 0 failed (denominator printed by the driver).
- Vintage guard: blob-compare pin-vs-HEAD per evidence surface, all 30 rows, zero moved.
- Tie-outs (scripted, not hand-checked): roadmap row set == census unresolved set (exact);
  owner parity vs census PASS; workstream coverage = each row exactly once; 30/30 bundle files
  present; stage occupancy sums to 30.

## Bounds

No owner surface touched (characterize-not-fix). Everything PROPOSED until ratified. The census's
named next allocations (59-engine sweep, 9/18 resolves_via drive) and the cloud execution space
remain out of this seat's scope, carried as residue.
