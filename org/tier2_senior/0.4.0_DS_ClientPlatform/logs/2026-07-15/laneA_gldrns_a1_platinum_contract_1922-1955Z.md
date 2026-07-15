# OPAL_GLDRNS.A1 COMPLETE — the 49F Group-D platinum output contract pinned (8/8 publishers, measured fan-out, consumer-anchored)

**archetype:** TRACE
**secondary_archetypes:** VALIDATE, SCRIBE
**serial:** 0.4.0_DS_ClientPlatform~A | **window:** 2026-07-15 19:22Z -> ~19:55Z
**TO:** OPAL_GLDRNS.A1 (GO 192248Z from CTO, batch A1->A2->A3)

## Summary

A1 executed end-to-end in one window. Deliverable:
`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/PLATINUM_OUTPUT_CONTRACT_49F_20260715.md` —
the S4/S5 target artifact. 8/8 D scripts pinned: 46 distinct output key patterns, measured fan-out
from a full served-bucket listing (23,593 platinum objects @ ~19:35Z), field-level shapes from
emit-code cites spot-verified on 34 downloaded served artifacts (>=2 per surface class, 12 classes),
21 portal consumer cites (ai.ts @ portal 3df9231e) + Lambda/edge anchors, 12 D-to-D edges mapped,
runner box live-verified (bd-gold-layer-runner r6i.4xlarge, stopped between runs), D-phase ordering
pinned from gold_dispatch.sh:467-485, nightly cadence measured from the 07-15 run timeline
(00:46-01:26Z). Basis-labeled BLACK DIAMOND 0833 throughout; no summed 0824+0833 quantity anywhere.

10 findings recorded in the contract (sec-6), the load-bearing ones: (1) platinum
employee_leaderboard.json ORPHAN (writer-less since 04-09 + consumer-less — retirement candidate);
(2) exec_summary.json CONSUMED-BUT-FROZEN (160 files @ 05-04, generator absent from all 8 scripts,
FE still fetches at ai.ts:941 — cleanup is artifact-type-blind for current advisors); (3) cohort_a
PATH MISMATCH (written gold/platinum/firm/, consumed platinum/firm/, no router in between, consumed
key absent); (4) advisor_nna_canonical.json is GZIP AT REST (parse-fail on raw read is expected);
(5) legacy dual-writes still burning nightly with no found consumer (D_01 gran files, D_03
gold/advisors/ 454 objects) + frozen fargate-era relics.

## Compiler Tools

| tool | run | result | note |
|---|---|---|---|
| comp-pipescript io | 8x (all D scripts) | PASS-EMPTY | D-group manifests empty (dynamic keys); tool prints "manual review required" — the contract IS that review. D_01/D_03 dynamic-read hints correct |
| comp-blast | 1x D_04.client_portal_summary | PARTIAL + DEFECT | 2 corpus HOLD claims surfaced + read (clients_tab envelope FE contract; inflection mirror doctrine); **cp1252 UnicodeEncodeError crash** in cli.py:_render_risk on U+2192 in a corpus quote — retried PYTHONIOENCODING=utf-8, full output OK. GAP BANKED: cli.py _p() should encode-safe (ASCII-only law, CLAUDE.md Code Quality). No downstream EXTRACTED edges for D_04 (lower bound; dynamic consumers invisible — correct per its own caveat) |
| comp-grep / comp-which | 0x | — | file-scoped greps used native Grep (light escape per rail); bucket listings + downloads rail-marked inline per TO mandate |
| commit-gate.sh | n/a | — | no .py edited (read-only TO) |

Appended line to org/compiler-tools-log.md same commit.

## Evidence trail

- Listings + 34 samples in session scratchpad (bd_platinum_listing.txt, bd_gold_artifacts_listing.txt,
  bd_gold_entities_listing.txt, samples/) — evidence quoted with keys/sizes/dates in the contract.
- Live primitives: ListObjectsV2 (fan-out), get_object x34 (shapes), describe-instances (runner box).
- Vintages pinned in contract sec-1 (repo 0f248d7f9, portal 3df9231e, listing ~19:35Z).

## MCP traffic

IN: CTO GO (BATCH A1->A2->A3) 192248Z. OUT: startup broadcasts to CTO/COO/MSTR (~1922Z, Andrew-direct
P0 record per XXX.md law); RAVC ACK to CTO 192444Z; A1 RAVC close to CTO (this window's end).

## Blockers

NONE. A2 opens immediately per the batch GO.

## Current State / Next Steps

1. **[NOW]** A1 closed -> flip OPAL_GLDRNS.A2 to pending; column-level D-consumed input census +
   B/C->D sufficiency verdict (verdicts CARRIED/RENAMED/DERIVED-IN-D/MISSING; MISSING -> CTO before
   Wave-3 C-port spec freezes). A1's sec-5 edge map + per-script input lists are the census spine.
2. **[THEN]** A3: fit harness + read-only dry-fit (D_04 preferred), consumes A2's pre-declared
   divergence list; scratch-sink absolute.
3. Watchers: inbox Monitor bmzbcge9k LIVE.
