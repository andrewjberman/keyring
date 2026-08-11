# C3.i COMPOSITION -- STATE (DONE) + THE F1 WIRING PATH

**Author:** `4.0.0_SA_CRO~B` · Andrew-direct 2026-08-11 ("sort out the C3.i composition, which should be
done already even if it's not wired up to this just yet"). **Verdict: Andrew's premise CONFIRMED -- the
composition is done and persisted; F1 is a CONSUMPTION join over it, not a rebuild.**

## 1. THE COMPOSITION IS DONE (grounded)

| what | where |
|---|---|
| **Composer** (structural union-find over C0, recurrence >=2) | `NFRA_MOTIF_P2_c3_emergence.py` (org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/) |
| **Persisted output** | `org/modules/graph/NFRA_ONTOLOGY_C2C3_CANONICAL.yaml` -- 14 C3.i structures, each `kind` + `chain_count` + `spans_verticals`; 138 chains total |
| **Authority** | Andrew-direct SOVEREIGN 2026-07-30 (CVO terminal): *"...persisted in a manner that there is never any confusion about this again."* Author `3.0.0_SA_CVO` |
| **Served** | `comp-estate --matrix` (14 structures x 29 verticals over 138 chains) |
| **Honesty invariant (in-file)** | c2_c3 *"DISCOVERED, never declared -- membership comes from recurrence (>=2) and structural union-find"* |

This IS the design's "compose -> classify -> persist" (OPAL_KIMIPIPELINE s.13's "CVO's materializer").
It was done 2026-07-30.

## 2. RECORD DRIFT FOUND (flag, not adjudicate)

**`OPAL_KIMIPIPELINE_STATE_FRICTION_DESIGN.md` s.13 (2026-08-06) says F1 "remains UNBUILDABLE until the
deterministic composition exists."** The composition existed on 07-30 -- SIX DAYS BEFORE s.13 declared it
absent. So the Kimi design's own F1 critical-path line is STALE: it holds F1 on a dependency that was
already satisfied. Same dead-gate-live-in-record class as the A.2 finding earlier today. Routed to the
Kimi-design owners (CTO~B / CVO) for the record fix; F1 is NOT actually blocked.

## 3. WHAT F1 NEEDS -- AND IT EXISTS

F1 (s.3) = comp-blast over the vertical's changed C0 nodes -> which C3.i structures the radius touches;
**structures touched K of 14.** The mapping is the DUAL KEY the canonical yaml legislates: *"the DUAL
KEY lives on every chain: (family -> C3.i, named_thread -> C3.ii)."* CONFIRMED live on the resolver:
every thread carries `family`. mdpf's chains: `family=cot-and-mdpf` (-> sys-cot-mdpf-assets) +
`family=partners-portal-infra` (-> sys-partner-serving-platform) -> mdpf spans 2 of 14 structures,
matching the matrix.

## 4. THE F1 WIRING (consumption, not a build)

```
comp-blast --function <mdpf changed C0 node> --json      # the radius (existing tool)
  -> each touched node -> its thread/chain (resolver producers/resources)
  -> chain.family -> legacy_family_key -> C3.i structure  (canonical yaml)
  -> F1 = |distinct structures touched| of 14 + WHICH ones
```
Every leg uses an existing artifact (comp-blast, the resolver's `family`, the canonical yaml). **No new
composition build. The gap is the JOIN, which is a spec/consumption task, not a materializer build.**
This resolves exactly the ambiguity the F4 live call surfaced -- HEATING (radius stays inside mdpf's
own structures) vs SPREADING (radius touches many of the 14).

## 5. NEXT
- Assemble the blast->family->structure join, compute mdpf's REAL F1 (of-14 + which), fire the
  F1-enriched friction call (the resolving axis).
- Coordinate the consumption contract with CVO (composition owner) + route the stale-s.13 record fix.
- Wiring F1 INTO the runner is a later BUILD (CTO gate + AE); computing F1 for the spec is research/measurement.
