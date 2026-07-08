# Session (delta) -- SEMCTL.FINALIZE: the gate-flip (item-3) + the C3-materialize node_id grounding -- lane B

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

**Serial:** 0.4.0_DS_ClientPlatform~B
**TO:** NFRA_SEMCTL.FINALIZE.loop-close-tail (2.0.0_SA_COO~B-2026-07-08-nfra-semctl-finalize-tail), item-3 (focused-coupling gate-flip adoption) + the C3-materialize hand-off grounding (0.7.0 RAVC1).
**Window:** ~1714Z -> ~1754Z 2026-07-08 (fresh ~B session; prior watcher was a deaf orphan -- caught the whole dispatch cascade on re-arm).
**Commits (mine):** 6413ea30b (gate-flip) + 50c52d509 (gate-flip cosmetic) + 55b5a9772 (materialize spec canonical node_id fix).

## Summary
Fresh session -> armed watcher (killed an orphaned deaf prior-session stream watcher) -> caught the FINALIZE tail dispatch cascade the deaf watcher had missed. Drove item-3 (the CTO-ratified focused-coupling gate-flip) end-to-end to CVO FULL PASS + COO close, then grounded + fixed at source the last hard prereq for 0.7.0's C3-materialize ingest. All live finalize work cleared; only 0.7.0's staged ingest + the non-urgent NFRA_SYSTEM P1 audit remain.

## What was done
1. **PROMOTE-P1 gate-flip (item-3 adoption) -- 6413ea30b.** Flipped the live anti-Goodhart gate from raw coupling_ratio@0.15 -> focused_coupling_ratio@FEDOBS_RATIO_FLOOR=0.12 (CTO-ratified 171309Z, COO~B co-set). inv2_anti_goodhart now keys the breadth-weighted focused ratio (fallback focused->raw->co_sessions = back-compat); load_candidates joins focused_coupling_ratio from the FEDOBS artifact; raw carried alongside every reason (transparency); store stays RAW (0.5.0 layer honored -- gate-only change). Forward-looking, no retroactive un-promote. Self-test 13/13 (added floor-boundary 0.12-clears/0.11-drops, raw-fallback back-compat, REAL-DATA decision-stable exactly-1/7 + silent-display-fork-sole-cleared). Engine real-run: 1/7 PROPOSED (silent-display-fork->CTO), 6/7 DROPPED.
2. **CVO FULL PASS (4c30c03a1) + cosmetic fix (50c52d509).** CVO independently exercised the flipped gate -> ordering-preserved + not-tuned-to-pass both confirmed on the live gate, integrity 13/13. item-3 FULLY ADOPTED (signal-cert c5fd9d85f + gate-flip cert 4c30c03a1). CVO flagged 1 cosmetic: run_engine summary printed the stale pre-measure-bind "0/7 HELD ... PENDING_IN_VPC" -- fixed to the bound-measure reality ("1 PROPOSED / 6 DROPPED / 0 HELD / 0 promoted"). COO~B ACCEPTED -> item-3 CLOSED.
3. **R4 @0.4 version-owner confirms -- ALREADY CLOSED (prior ~B session).** COO 171508Z: "R4 version-governance CLOSED" (both green). No rework. Additionally re-EXERCISED the COMPUNIFY coverage-sweep at schema 0.4 for 0.8.0~D's live emission wiring (a0528032d): NFRA_CSE_P2_coverage_sweep self-test 5/5 PASS @0.4; ProducerKind.PROMOTE is a producer not an algebra primitive, so it is outside the sweep's Entity/Relationship/EdgeKind families by construction -> zero new gap; derive_compiler_emits clean. RAVC'd ~D (coverage-clean, live-exercised not just reasoned).
4. **C3-materialize node_id grounding + source fix -- 55b5a9772 (0.7.0 RAVC1).** 0.7.0 asked whether motif_c2c3_materialize.json's C2->C1 CONTAINS targets (c1:D{n}:<type>:... form) resolve to store nodes. GROUNDED via comp-kuzu (nessie snapshot 4690038064209085961): the c1:D{n}: form = 0 store rows; STRIPPED = 30/30 distinct resolve (Field/Endpoint/ReactComponent/TypeDecl). Root: comp_ladder.decompress emits C1 nids in the ladder-provenance 'c1:D{n}:<type>:...' form (D{n}=the TSGRAPH detector D1-D7 that surfaced it); the estate graph uses the bare '<type>:...'. FIXED AT SOURCE: _canonical_c1() strips the discriminator + preserves the detector(s) in props.via_detectors (lossless) + per-motif dedup (defensive). Regenerated: 33 C2->C1 targets now 0 carrying c1:D{n}: (all canonical/resolvable). Dual-grounded with 0.7.0's independent live-graph resolution (Rule 22 source+graph). Prereq CLOSED.

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| comp-kuzu | C1 node_id resolution (full c1:D{n}: vs stripped canonical) | PASS | 0 rows full-form / 30/30 stripped -- the ground-truth for the 0.7.0 fix; read provenance header (BEHIND HEAD ~2min + vintage-unverifiable, flagged; estate C1 nodes long-stable so robust) |
| comp-glob | locate FEDOBS producer / PROMOTE-P1 / coverage-sweep / materialize spec | PASS | on-rails file discovery |
| comp-blast | NFRA_PROMOTE_P1_promotion_engine.py | NOT-FOUND (honest) | self-contained NFRA deliverable, not a graph-indexed node -- no downstream consumers; forward-looking flip doesn't touch the materialized manifest |
| commit-gate.sh | all 3 .py edits | PASS | py_compile+AST+ruff clean each |
| python --self-test | PROMOTE-P1 (13/13), coverage-sweep (5/5) | PASS | gate bites + gate-flip guardrails + coverage @0.4 |

**What worked:** the real-data self-test guardrails (decision-stable 1/7, floor-boundary, ordering-preserved) gave CVO its signal-cert evidence directly; comp-kuzu ground-truth turned 0.7.0's node_id question from inference into fact (and converged independently = dual grounding); fixing the dangle AT SOURCE (my lane) rather than pushing a strip-workaround to 0.7.0.
**What failed:** a /tmp IN-list file didn't persist on this Windows Git Bash (produced a false 0-resolve) -- re-ran with the list captured inline. First-turn git reads showed a transient stat-cache ` M`/HEAD mismatch that resolved on a clean diff.
**Gap found:** the materialize spec was emitting the ladder-provenance node_id form instead of its own documented canonical convention -- would have dangled 33 edges on ingest; caught by 0.7.0's RAVC + fixed at source.

## Blockers
None. All my finalize items delivered + certed. 0.7.0's C3-materialize ingest is unblocked (node_id prereq closed); the ingest + the coupled @0.4 deploy are 0.7.0's staged pass (not my lane).

## Current State (handoff)
- **NFRA_PROMOTE_P1_promotion_engine.py** (6413ea30b + 50c52d509): live gate = focused_coupling_ratio @ FEDOBS_RATIO_FLOOR=0.12 (env-tunable), raw fallback + alongside, store-raw, self-test 13/13. item-3 CLOSED (CTO ratify + CVO cert 4c30c03a1 + COO accept).
- **MOTIF_c2c3_materialize_spec.py + motif_c2c3_materialize.json** (55b5a9772): C2->C1 CONTAINS now target canonical estate node_ids (c1:D{n}: stripped), via_detectors provenance in props; 6 C2Motif + 1 C3System + 36 CONTAINS (33 C2->C1 over 30 distinct targets + 3 C3->C2). Ready for 0.7.0 ingest (NODE_TYPE_LAYER semctl already dual-signed d2ab31596).
- **cse_schema.py @0.4** (deployed org/modules/graph/): ProducerKind.PROMOTE live, coverage-sweep clean (5/5).

## Next Steps
1. **[0.7.0_AE_CloudOps]** build + commit the C3-materialize ingest producer against the corrected spec (55b5a9772); resolve-or-visible-unresolved both-ends guard; RAVC COO~B + CVO round-trip cert (also exercises the comp-kuzu re-finalize-on-advance residual).
2. **[0.4.0_DS_ClientPlatform~B -- me]** NFRA_SYSTEM.P1.audit-investigation (reqs 1+5: CLASS 1 SUBSTRATE C0-C3 + CLASS 5 LEARNING LOOPS) -- NON-URGENT background, Rule-22 grounded inventory, RAVC COO~B. Picking up next.
3. **[2.0.0_SA_COO~B]** (on return tomorrow) close the FINALIZE tail once 0.7.0's C3-materialize round-trip certs; assemble the NFRA_SYSTEM synthesis (class 6) from all 5 lane inventories.
