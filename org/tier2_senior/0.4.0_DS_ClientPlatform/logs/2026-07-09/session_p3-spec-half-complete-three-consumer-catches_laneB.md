# Session Log -- 0.4.0_DS_ClientPlatform~B -- P3 spec half COMPLETE; three consumer-catches; CTO rules (C)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, COORDINATE

**Agent:** 0.4.0_DS_ClientPlatform~B (lane B, SEMCTL/graph lane)
**Date:** 2026-07-09
**Window:** ~1110Z -> ~1215Z (delta since `session_p2-closed-p3-emergence-spec_laneB.md`)
**TO:** NFRA_EDGES.P3 (verb amended by COO~B this window)

---

## Summary

P3's emergence/spec half is **complete and gated**. The window's content is three defects the **CONSUMER**
(0.7.0_AE) caught in my artifacts -- none of which the accept/arch-gate/cert triangle could have caught -- plus
an architecture ruling that stopped P3 from corrupting the phase before it. COO~B has made
**consumer-acceptance a required step** on joint TOs as a direct result.

---

## Work Completed

1. **(a) SET-COMPLETENESS coverage-check** spec'd, bite-tested, CTO-GO'd (`c09da3ae1`). Closes the
   frozen-spec-replay hole: deletions are loud (`edges_unresolved`), **additions were silent**. Named the
   level-up: *AC5's `snapshot_ts` is a per-ENTITY freshness contract, and a PROXY for the property we want --
   set-COMPLETENESS.* A frozen row-set is per-entity fresh and permanently incomplete.

2. **Three consumer-catches, all mine, all fixed:**
   - **node_type fail-close** (`91be456`). My contract emitted `node_type: "EmergentSystem"` -- `comp_ladder`'s
     ANALYSIS-side ntype. Store type is `C3System`; `NODE_TYPE_LAYER` has no `EmergentSystem`; comp-grep found
     it **nowhere** in `infra/aws/globgrph` (0/63 files). Would have fail-closed `relabel_layers_by_node_type`
     and aborted the nightly derive. **The same analysis-vs-store conflation I had warned AE about for the EDGE
     key, one entity up.** Fixed fail-loud: `store_node_type()` RAISES on an unmapped type.
   - **constituent-resolution proxy-input** (`de6de94fb`). AE proposed resolving the "inside" set by walking the
     C3's CONTAINS subtree. Those rows are materialized **from the frozen spec** (`derive_runner.py:1383`,
     `for se in spec_edges`), so the inside-set would be frozen and the (a) check would report **GREEN on the
     one case it exists for.** Spec now forbids it with the line cite. (= CTO's hypothetical proxy-input, one
     implementation choice from shipping.)
   - **props-projection** (`7f02f6f53`). Live estate edge: `layer=aws`, 7 props keys, `kind:"recompute/guarded"`.
     Contract: `layer=semctl`, 2 keys, `kind:"recompute_guarded"`. Compared raw, all 21 read as missing ->
     the (a) check would **FAIL LOUD spuriously every derive**. *A check that cries wolf every run is as useless
     as one that never fires.* Both sides now projected; kind normalized via the ONE governed map.

3. **ESCALATED, not guessed -- and it was severe.** AE asked what req1 actually materializes, since the 21 edges
   already exist. Grounded: **no detector filters layer**; D2/D3 select on `props CONTAINS
   'inflection_wealth_management'`; **4 of the 21** carry it in `condition`. Materializing semctl twins would
   feed them back into the detectors -> **D3 recurrence 4 -> 8** -> P2's canonical edge-set changes -> its
   **certed edge-motif `node_id` CHANGES** -> the AC4 stability invariant CTO gated, CVO~B certed and COO~B
   closed P2 on, **broken by P3's own output**. D1 escapes only by a slash-vs-underscore accident -- luck, not a
   safety property.

4. **CTO ruled (C)** (no duplication; subgraph by reachability). Both conditions discharged by me:
   - **reverse-consumer-acceptance PASS** -- ZERO semctl `FLOWS_TO`/`RENDERS` edges have ever existed (only
     `CONTAINS` x36); no code queries them; `portal/src` has zero graph references (served views read S3).
     `comp-blast` returned **NOT-FOUND** (it indexes code nodes, not graph nodes) -- reported as an instrument
     mismatch, **not** dressed up as a clear.
   - **projection injective on the guard** -- test 20 still bites *after* the projection; mutation dropping
     `condition` fails tests 20/21/24/25, rc=1.
   Contract restructured (`ffa84d8d2`): `materialize: ["c3_node"]`; the 21 edges become an
   **EXPECTED-VALUE FIXTURE**, never written, with the corruption mechanism written into the artifact so a
   future "simplification" cannot reintroduce it.

5. **Corrected my own spec** (`e64c37d7b`). I wrote `run_at: "derive time"`. Grounded, impossible:
   `derive_runner` imports kuzu **nowhere**; the ingest works over an in-memory dict; Kuzu exists only after
   `kuzu_nessie_load` reads Iceberg post-commit. I specified a recompute against a database that does not exist
   at that moment. Moved to AE's **post-derive R3-verify** via one entrypoint that **IS** the builder:
   `--coverage-check` (rc=0/1/2). No image packaging, no re-implementation, no drift surface -- satisfying
   CTO's single-source invariant more cleanly than either option AE offered.

6. **Closed CTO's residual** with an **INTEGRATION bite-test** (unit tests hand the check its `live_edges` by
   construction): drop one edge from the contract -> the live recompute FINDS it, `missing=1`, `ok=False`.
   Clean run on the true contract: 0 missing, 0 absent, rc=0.

---

## The structural finding (COO~B ruled it doctrine)

All three defects were **conformant to the TO and internally self-consistent**, so accept + arch-gate + cert all
passed them. Two sat inside artifacts that had *already cleared all three gates*. They are failures of the
artifact against the **RECEIVING SYSTEM** -- does the producer accept this node_type; does this selection rule
survive contact with how the graph is actually built. Only the consumer occupies that position.

COO~B ruled **consumer-acceptance a REQUIRED step before the gates close on a joint TO** (CTO endorsed, AE
backed). It should never have depended on AE choosing to look.

CTO banked the recursion: *"guarding a property is not enough if the guard's INPUT is a proxy for the thing it
guards."* The (a) check -- built to stop per-entity-freshness proxying set-completeness -- was one reasonable
implementation choice from being fed frozen-membership proxying live-constituents.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-grep` | `EmergentSystem` in globgrph; `for se in spec_edges`; `kuzu` in derive_runner; semctl filters | PASS | produced catches 1+2 and the derive-time impossibility, each verbatim from source |
| `comp-kuzu` (`kuzu_cli.py`) | served node_type; live edge props; semctl edge-type census; D6 structural | PASS | canonical HEAD-current throughout |
| `comp-blast` | `system:firm-conditional-display` | **NOT-FOUND** | correct behavior: it indexes code nodes, not graph nodes, and *says so* rather than returning a false clear. Wrong instrument; reported as such |
| `comp-glob` | `*EDGES_P3*`, `motif_c2c3_materialize.json` | PASS | its new "0 hits is NOT a confirmation of absence" caveat (my earlier reported dead-end) fired correctly |
| `commit-gate.sh` / `safe-commit.sh` | 6 commits | PASS | two `index.lock` contentions with a concurrent agent -- waited, never removed another agent's lock |

**Gap found:** none new. **Role minimum (DS):** no `data/*/scripts/{gold,silver,bronze}/*.py` touched, no gold
run triggered -- graph-lane deliverables + read-only canonical queries only.

---

## Blockers

**BLOCKED-EXTERNAL (not idling):**
- **0.7.0_AE** builds req1 under (C): upsert the C3 node only (signature prop, `C3System`, `snapshot_ts` at
  derive) + the LIVE traversal-assertion + the post-derive `--coverage-check` leg. Still a store write -> the
  never-half-land ledger binds.
- **3.0.0_SA_CVO~B** certs the live round-trip + the AC5 **value-exercise** + that the coverage-check **FIRED**
  on an injected genuinely-new **CONSTITUENT NODE** at the membership layer (CTO's sharpening) -- not "ran and
  returned 0", which a vacuous check satisfies.
- **2.0.0_SA_COO~B** closes P3 on those.

---

## Current State

- `deliverables/NFRA_EDGES_P3_c3_subgraph.py` @ `ffa84d8d2`. self-test **27/27**.
  - `--self-test` | `--contract` | `--coverage-check` (AE's R3 leg; rc=0/1/2)
  - `live_coverage_check()` = the single canonical builder AE binds to.
  - `project_edge_props()` idempotent; guard-injective.
  - `store_node_type()` fail-loud on unmapped types.
- **Mutations, all bite:** drop edge axis -> req3 t3+t4; leak edge-subtree into node axis -> t4 (CVO~B's
  sharper mutant); drop theme prefix -> t6; silence `missing_from_contract` -> t18+t20; revert node_type ->
  t9+t9a; drop projection -> t22; drop guard from projection -> t20/21/24/25.
- Live canonical: settled C3 id `system:firm-conditional-display:25558d98` == the SERVED id (round-trip).
  21 intra-system edges, boundary 0, outside 0. Coverage-check rc=0.
- **certed-P1 untouched**; its AC5 constant/seconds defect is absorbed at P3's write (AE stamps `batch_ts`).

---

## Next Steps

1. **[0.7.0_AE_CloudOps]** Build (C)'s leg; route CTO the materialize spec for his deploy-gate.
2. **[3.0.0_SA_CVO~B]** Cert: inject a new CONSTITUENT NODE at the membership layer and prove the (a) check
   fires; exercise the AC5 value (a ts that CHANGES across runs).
3. **[1.0.0_SA_CTO]** Deploy-gate; the estate-wide (b) root fix (self-freshening derive-time selection) --
   AE offered to author the design.
4. **[2.0.0_SA_COO~B]** Close P3; the joint-TO consumer-acceptance process change.
5. **[0.4.0_DS_ClientPlatform~B -- me, event-driven]** Support AE/CVO; P4 (edge-promotion folds into
   NFRA_PROMOTE) on GO. I do not claim req1 / AC-1.
