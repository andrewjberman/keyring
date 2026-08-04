# W-2 emission + parity findings: mechanism proven; 3 FAILs measured to causes; 2 words asked

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE
**Serial:** 0.4.0_DS_ClientPlatform
**Window:** 2026-08-04 ~17:50Z -> ~18:02Z (delta since canrte_w2_build_state log)

## Arc

- Joint siting word landed VIA the W-2 TO amendment @cd10fbe86 (COO 174803Z + CTO 174841Z;
  formal notice 175159Z crossed my execution): shadow = gold/mdpf_revamp/_canrte_shadow/
  {firm}/ + the CTO cleanup rider (REGISTERED DELETE STEP).
- Re-sited key verified on the live primitive: simulate-principal-policy s3:PutObject on
  the exact _canrte_shadow key = allowed (one arn). Defaults flipped in both scripts;
  rider cited in the builder docstring (@0a61583b2).
- **MECHANISM-PROOF emission (labeled, counts 0):** build_mdpf_spine --firm all --upload:
  all four shadow artifacts staged with put+fresh-GET byte-verify (49f 187,656B /
  inflection 151,776B / cottonwood 83,321B / global 343,457B), every in-build gate green
  (cross-axis, composition, carry).
- **Comparator full-path run:** cottonwood EQUAL; 49f/inflection/global FAIL -- ALL THREE
  CAUSES MEASURED, none a builder defect:
  1. **ENV float-skew (halfcent class):** 49f model_aua differs by $0.01 on exactly
     2/437 dates (2025-11-03, 2025-11-18; custody 0-divergent; global inherits via the
     fold). NOT my-run nondeterminism: a second local build compares canonically EQUAL
     to the first (run2==run1). Local-vs-runner accumulation skew; same-env scheduled
     cycles do not see it.
  2. **SS7 GAP (real):** source_vintage_last.age_hours_at_generation (41.9 vs 41.7) is
     CLOCK-RELATIVE inside a provenance block -- differs even same-cycle. PROPOSED:
     one-field amendment to the SS7 volatile strip-set (needs COO+CTO word; SS7 was
     accepted as-written).
  3. **ENV identity:** meta.cottonwood_carry.policy.roster embeds the resolved ABSOLUTE
     PATH (Windows vs /opt/mdpf) -- equal when both sides runner-built; no action; also
     the attribution evidence that the incumbents are runner-built.
- **DEPLOYED:** both scripts to s3://opal-data-mdpf/code/scripts/gold/, comp-pipescript
  deployed MATCH each.
- **Asks routed (COO 180137Z):** (a) the SS7 one-field amendment word; (b) the AE
  ADDITIVE dispatch wire (build_mdpf_spine + canrte_parity_compare --label scheduled,
  soft/non-fatal like 6e day-1) so scheduled parity cycles accrue.
- **DELETE STEP REGISTERED** (rider): owner 0.4.0_DS; trigger = the W-5 swap (or W-2
  abort); recorded in docstring + report + here.
- W2 TO: PENDING at parity OPEN 0/3 (honest state; BUILD-COMPLETE close awaits the wire).

## Compiler Tools

| run | observed | verdict |
|---|---|---|
| simulate-principal-policy (re-sited key, one arn) | allowed | Rule-22a on the NEW resource, verified not assumed |
| build_mdpf_spine --firm all --upload | 4/4 staged byte-verified, gates green | MECHANISM-PROOF PASS (labeled, counts 0) |
| canrte_parity_compare --firm all --label mechanism-proof | 1 EQUAL / 3 FAIL, denominators + first-divergent-key printed | the comparator ROUTING failures correctly is the instrument working |
| determinism experiment (rebuild 49f, canonical compare vs shadow) | run2==run1 EQUAL, 0 divergent indices | cause-1 attribution MEASURED |
| targeted deep-diffs (series indices, source_vintage_last, cottonwood_carry walk) | the 3 causes above, each localized to field+values | INFERRED -> MEASURED before reporting |
| comp-pipescript deployed x2 --pipeline mdpf | MATCH both | deploy verified |

## Do NOT (successors)

- Do NOT edit the SS7 volatile set without the COO+CTO word -- the DELTA=0 definition is
  an accepted contract; the one-field proposal is AT their desks.
- Do NOT count the mechanism-proof comparator run toward 3-green (label says so).
- Do NOT read the 2-cent divergence as a data defect -- it is measured env skew; if a
  SCHEDULED cycle shows it, THAT is a real finding (same-env builds should tie).

## Blockers

W-2 parity arming: AE wire + SS7 word (both routed). Queue: GRF scoping (amended
@e6c531812), fresh-chain tie reads, ~02Z floor acceptance read.
