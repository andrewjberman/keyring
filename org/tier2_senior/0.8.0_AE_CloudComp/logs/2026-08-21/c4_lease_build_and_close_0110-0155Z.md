# 0.8.0_AE_CloudComp -- NFRA_EPISTEMY.C4-LEASE: build + close; R1-RARITY S0 + design round (0110-0155Z)
**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Window
2026-08-21 ~0110Z -> ~0155Z. Event-driven under Andrew's "GO on" (relayed verbatim-scope 63962) + COO's /drive GOs. Prior log: c3_identity_closure_compiler_2130-2230Z.md (2026-08-20).

## What happened (in order)
1. R1-RARITY GO (COO 64034) -> S0: liveness oracle self-test PASS (frozen 19/4 reproduce; PREDICATE UNUSABLE -- grain field absent from the deployed vintage; verdict INDETERMINATE, honest); BEFORE snapshot saved. FINDING (log-grounded): the nightly derive (/ecs/globgrph/derive-runner, 24h, filter C2C3) shows the 2-spec static ingest and ZERO compose-arm lines -- the DEPLOYED image predates _compose_c2c3_live entirely; the composer (CVO harness, 6,138 instances, 13 A/B families + grain:class marking) is BUILT AND UNLANDED. Key-space gap stacked on it: A/B family keys intersect the canonical twelve = ZERO (three family key-spaces now named; CRO banking the disambiguation clause at v3.17). Design 64080 -> CRO RATIFIED 64086 (canonical-family composer, motif_family under its own name, SL-first with api-serve excluded-and-stated, fixture-side tonight, rebuild routed to CTO/CTO~B). R1 build resumes on CVO home-call + CTO routing.
2. C4-LEASE GO (COO 64063, Andrew-scoped /drive "NFRA_EPISTEMY to close"). Phase 1: TO + Knowledge_Basis 0.1.1 schema + the normative digest home (precondition_token.py _request_hash, IMPORTED) + precursor anchors; token census over the PINNED set (clean; rule-bank EXPIRED adjacency named). Sketch 64100 -> base cert 64109 (CERTIFIED-WITH-ONE-ADJUDICATED-DEVIATION; D1 RULED for the partition tree: moved-identity -> EXPIRED supersedes Response III's changed-digest -> INVALID) + FIRST BASIS MINTED (kb-20260821-6ce229dd, five nulls, @053b83f414; COO independently re-derived the digest with a negative control 64116) -> CTO arch gate 64118 PASSES NO CONDITIONS (four properties verified at source; the D1 remedy argument: INVALID names the wrong remedy).
3. Build: comp_lease.py + .tools/comp-lease. Battery 14/14 first run. load_basis defect caught in-flight: the kb-*.json glob MISSED the mint's filename -- fixed to content-found + digest REPRODUCED through the normative home (refuses a non-reproducing mint). Fixture basis RETIRED at the mint.
4. L5 live: first mint round raced peer commits (2 honest INELIGIBLE -- repo_head moved between compile and evaluate) + the stale committed closure evaluated INELIGIBLE; re-mint back-to-back -> 3 leases on the minted basis, printed VALID at 5d453a6b9b24. Landing commit BLOCKED once by the routability invariant (comp-which could not return comp-lease) -> curated rule added, rank-1 -> landed @d0b9f67ca9 + discharge @9600a042d0. THE FLIP, PRINTED: post-commit state reads -> 4/4 EXPIRED naming repo_head 5d453a6b -> 89a5bc8a ("out of scope, not out-ranked"). Proof L1-L7 + this log follow in the close commit.
5. Meanwhile absorbed: MSTR merge window 63969/63989 (held commits through it earlier); COO 64098 (content-addressed ids name their derivation home -- applied); COO 64121 precisions (arch gate != TO close; untracked-bytes gate vintage -- the landing hash now cites it); CRO routing packet 64078 (queued BEHIND C4+R1, explicitly).

## MCP traffic
~20 messages handled, all acked. Sent: R1 ack + S0 finding/design (64080-83), C4 sketch (64100-102), acks/replies. RAVC2 close for C4 follows this log; R1 continues.

## Compiler Tools
| tool | invocation | result | note |
|---|---|---|---|
| comp-lease | --self-test / evaluate x7 / state x8 | PASS | 14/14; flip printed 4/4 EXPIRED |
| comp-closure | compile x6 | PASS | fresh vintages; back-to-back after the race |
| c2c3_liveness_acceptance.py | --self-test / --snapshot | PASS | R1 S0 oracle; INDETERMINATE-honest on the frozen layer |
| comp-kuzu / kuzu_cli | edge+node censuses | PASS | served-plane vocabulary for the R1 composer |
| comp-manifest-check | completeness x3 | PASS | BLOCKED the first C4 commit on routability -- the invariant discriminates |
| comp-which | routing probe | PASS | comp-lease rank-1 after the curated rule |
| comp-system | regen discharge | PASS | @9600a042d0 |
| comp-find | name/content locates | PASS | spec JSONs' true home; _request_hash home |
What worked: the schema route at full speed (sketch->cert->gate inside one hour, twice tonight); consuming normative homes instead of re-implementing. What failed and was owned: the kb-glob filename miss; the routability block; the peer-commit race (now a declared blind spot). Gap: comp-blast has no function-grain node for derive_runner internals (graph universe is resource-grain) -- noted, not chased.

## Blockers
None for C4. R1 Leg-1 build awaits CVO's composer-home call + CTO's hook/rebuild routing (design ratified 64086); the globgrph image rebuild is CTO~B's production path.

## Current State (zero-context handoff)
- comp-lease live at .tools/comp-lease (engine org/modules/graph/comp_lease.py @d0b9f67ca9). Leases/evaluations under org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_EPISTEMY.C4-LEASE/leases/; flip transcript LIVE_FLIP_TRANSCRIPT_20260821.txt; proof NFRA_EPISTEMY.C4-LEASE_PROOF_OF_SPEC.json (L1-L7).
- Basis: kb-20260821-6ce229dd consumed (content-found, digest reproduced); fixture retired.
- R1-RARITY: S0 complete (BEFORE snapshot in deliverables/NFRA_ONTOLOGY.R1-RARITY/), design ratified, build pending two named answers; rider Leg 2 computes after Leg 1.
- Commits tonight (all CLOUD, unpushed, LD-0367 window): @1c7fc9b44e, @a07cd48767, @21fe7c95cd, @d652c88490, @b9cc3922be (C3); @d0b9f67ca9, @9600a042d0 (C4); proof+log commit next.

## Next Steps
- [2.0.0_SA_COO] C4 RAVC2 close (this turn) -> your validation activates C6 per 64121.
- [3.0.0_SA_CVO] composer home call for c2_canonical_compose (R1 Leg 1). [1.0.0_SA_CTO] derive hook + image rebuild routing.
- [4.0.0_SA_CRO] Pass-3 routing packet dispositions queue behind C4+R1 per your 64078.
