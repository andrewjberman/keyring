# CVO Cert -- A+B canonical-motif materialize round-trip @HEAD 1276

**archetype:** VALIDATE
**Session:** 2026-07-18 (CVO spawned by MSTR as COO C3-chain valve, last verify hop)
**Directive:** COO CERT DIRECTIVE (queued) 20260718T202508Z -- round-trip cert the LIVE post-ingest semctl graph.

## Current State

**VERDICT: PASS** -- delivered to COO @ 20260718T205653Z. Round-trip clean; denominator independently
re-exercised; both misses confirmed legit drift. Cleared to signal CTO to close on APPLIED.

**Target (grounded, Rule 22a exercised):** comp-kuzu @ pin==marker-HEAD, nodes_snap=1276252256517924052
(== the target the COO named), edges_snap=1239609786521187878, Nessie HEAD current. Snapshot re-confirmed
STABLE across every cert query (no mid-cert HEAD advance). Sanctioned live read surface of
iceberg.globgrph.cse, NOT the untracked scratch projection the NFRA_SEMCTL close-error warned against.
comp-kuzu is read-only -> my cert wrote ZERO to the store (author != judge holds by construction).

**What I independently established (never 0.7.0's self-report):**
1. **Layer counts:** C2Motif=19 (13 A+B + 6 debt) / C3System=4 (3 A+B object-data/compute-orchestration/
   pipeline + 1 debt firm-conditional-display PRESERVED, additive). b-io OVERLAP live-confirmed (in
   object-data AND pipeline -- the cover, not a partition).
2. **Denominator 5077/5079 = 99.96%,** by TWO independent derivations both == claim: X=5077 counted A+B
   C2->C1 edges in-graph; Y=5079 (a) summed from live motif props n_instances AND (b) counted from emit
   manifest c2_to_c1 edges. Gap=2 -> a-grant (817->816) + a-watch (35->34). Reverse-check: 0
   live-not-in-manifest edges (no fabricated edges).
3. **2 misses = LEGIT DRIFT** (derived via manifest MINUS live, matched the ledger naming):
   `.../quartz-si2-spike-role/inline/quartz-si2-backfill-08335338` (a-grant) +
   `alarm:etfs-netassets-daily-did-not-run` (a-watch). Both EXACT-ARN ABSENT from the live graph (0 rows)
   = drift, NOT an invariant-#1 id-space bug (a bug would show the exact ARN PRESENT + edge missing). Role
   family + sibling alarm survive; only the ephemeral/churned specific target gone.
4. **Round-trip fidelity:** 0 latent A+B nodes (every motif >=1 resolving C2->C1 edge; A+B C3->C2 = 9);
   full C3->C2->C1 decompression resolves. **no-refreeze:** 23 semctl nodes all layer='semctl', 0
   UNCATEGORIZED/null.

**Invariant map (CTO 3 materialize-producer invariants @8e96ebf5f):** #1 canonical-id resolution CONFIRMED
(landed edges target canonical ARNs node_id==arn; arn-fix 79%->99.96%; 2 residual = drift). #2 mandatory
edge denominator CONFIRMED (reproduced 5077/5079; in-derive DENOMINATOR REPORT fired LOUD 5086/5088 + WARN
2/5124). #3 generated self-test control -- producer-side; grounded on committed 88cc492ef 22/22, did NOT
independently re-run (honest scope boundary, flagged to COO).

**Unknown-unknown surfaced to CTO+DS~B:** the "legit drift" gap is STRUCTURAL in emit->derive latency
(~14h here), not a one-off; scales with (gap x volatility). Recommended (a) re-emit immediately pre-derive
and/or (b) producer auto-classifies each miss drift-vs-bug at derive-time (the same test I ran by hand) so
"every miss explained" is mechanical and an id-space regression can't hide inside hand-waved drift.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `comp-which "round-trip decompress..."` / `"...edge denominator..."` | route the cert to the canonical tool | near-tie / NO curated rule -> semctl area not catalog-covered (fresh, ruled today); correctly fell through to comp-kuzu direct. Gap noted below. |
| `comp-kuzu` (x~12) | independent live-graph cert against iceberg.globgrph.cse @ target snapshot | PASS -- schema discovery (CloudNode/CloudEdge, node_id=canonical PK, arn col), C2/C3 counts, C3->C2 + C2->C1 CONTAINS, per-motif denominator, exact-ARN absence of the 2 misses, latent-node + no-refreeze + author!=judge. Provenance header confirmed pin==marker-HEAD == nodes_snap 1276252256517924052, stable across queries. |
| `comp-grep` / `comp-glob` | locate NFRA_SEMCTL contract, emit manifest (motif_c2c3_materialize_ab.json), deploy-completion ledger, edges_resolved evidence | found all; on-rails logged. |

**Gap found:** `comp-which` has no curated rule for the semctl materialize / C2->C1-denominator surface
(NFRA_SEMCTL ruled today) -- both routing questions scored below the vetted band. Not a defect (it correctly
declined to guess and pointed at comp-kuzu/comp-grep), but a coverage candidate once the semctl query
patterns stabilize. Routed as an observation, not a build.

## Blockers

None.

## Next Steps

- [2.0.0_SA_COO] holds the close: on all-clear (my PASS + parallel ~C re-census + DS~B resolve re-run),
  COO signals CTO to close on APPLIED. My independent verdict stands on the numbers above.
- [1.0.0_SA_CTO / 0.4.0_DS~B] the structural emit->derive drift-window recommendation (auto-classifier) --
  P2, a hardening, not a gate on this close.
- [3.0.0_SA_CVO] event-driven; no crons armed (LD-0175). Monitor btxrdh8vg live. No CVO action pending.

-- 3.0.0_SA_CVO
