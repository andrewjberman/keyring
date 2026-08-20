# CVO EXIT-BAR CERT — Lifecycle_Stage value-enum mint (registry v3.11, @510a616350)

**archetype:** VALIDATE
**Certifier:** 3.0.0_SA_CVO (base) — requested by 4.0.0_SA_CRO (msg 63044, 20260820T134024Z) per the
standing SoD cut on the s4 exit bar.
**Verdict: PASS.** The sixth declared cell's disposition path is EXECUTED as claimed.

## SoD declaration (on the face, per my own exclusion discipline)

Proposal authored by `3.0.0_SA_CVO~Z` (site-Z lane; SS2.3 postulates + SS2.4 census), mint executed by
`4.0.0_SA_CRO`, ratified Andrew-direct ~1340Z ("approved with the amendment"). **I authored none of the
three minted artifacts and none of the proposal.** The falsifier retains with CVO~Z, not this seat.
Base and ~Z are distinct seats under LD-0325; the ferry chain (CVO~Z → MSTR → CRO → Andrew) is recorded
in the commit's own provenance block.

## Legs run (every claim re-derived at this seat, not accepted from the mint message)

| Leg | Claim | My read | Result |
|---|---|---|---|
| 1 | Mint commit exists, 4 files | `git show --stat 510a616350`: SYSTEM_DEFINITIONS.yaml (6±), C2C3_CANONICAL.yaml (4±=2 lines), RULE_BANK.yaml (+20), record MD (+27) | MATCH |
| 2 | Enum at its HOME | `NFRA_ONTOLOGY_RULE_BANK.yaml:408-422` `dynamic_rails.D3_contract_obligation.lifecycle.stage`: enum `[EMERGING, ACTIVE, WINDING_DOWN, DISSOLVING, DISSOLVED]` + `UNASSERTED` sentinel (`:412-413`) | MATCH |
| 3 | Exit discriminator | `:420` — container-survival form, both exits with opposite obligations/failure modes named | MATCH |
| 4 | Falsifier | `:421` — undecidable-container case RETURNS THE ENUM to proposer `3.0.0_SA_CVO~Z` | MATCH |
| 5 | THE AMENDMENT (Rule-24 postulate iii) | `:416` ACTIVE carries no health clause; "OPERATIONAL HEALTH IS A SEPARATE AXIS... a defective-but-not-being-retired vertical remains ACTIVE" with the amendment provenance in-value | MATCH |
| 6 | Token hygiene | `:422` — six tokens censused UNOCCUPIED; excluded tokens each named with home axis | PRESENT |
| 7 | Registry v3.11, entry ABSTRACT | `SYSTEM_DEFINITIONS.yaml:20` `version: "3.11"`; `:470-475` Lifecycle_Stage carries no member list, `resolves_via` → the rule-bank home | MATCH |
| 8 | Checker | **Independent re-run at this seat:** `python infra/system/ontology/check_system_definitions.py` → `65 entries checked, 0 violation(s)`, rc=0 | MATCH (65/0 rc=0) |
| 9 | Canonical = vocabulary hygiene only | Both RETIREMENT-PENDING occurrences respelled WINDING_DOWN (`C2C3_CANONICAL.yaml:154,:525`), each carrying the "not a walk assertion" marker; `lifecycle_stage:` field occurrences in canonical = **0** — every vertical remains UNASSERTED; population stays the walk's act (CTO arch leg) | MATCH |
| 10 | Two-phase (LD-0362) | Override declared in the mint commit's own trailer; discharged in-session `@ff58d8e687` (comp-system 06 recompile at HEAD) | DISCHARGED |

## Exit-bar cell census at v3.11 (declared cells, post-act)

- **deprecated (4):** `Substrate_Side:105` · `Territory:111` · `Semantic_Estates:302` · `Lifecycle_Value:480`
  — Lifecycle_Value's entry records its own discharge: naming-history alias of Lifecycle_Stage, the
  do_not prohibition discharged by naming act, open-not-decaying at resolution.
- **contested_unresolved (1):** `Unreconciled_Aua:548` — unchanged by this act; stays CVO-owned with the
  P4/P5 vocabulary-unification disposition path, CTO gate. **This act neither touches nor claims it.**

The cell this cert covers — the Lifecycle_Stage/Lifecycle_Value contest — now reads: contest resolved by
the 08-19 two-objects ruling, value enum ratified 08-20, enum landed at the entry-bar home, registry
abstract-with-pointer, alias deprecated with discharge recorded. **Disposition path EXECUTED, not merely
declared.**

## Instrument caveat (stated so the cert does not overclaim)

Leg 8 re-runs the same checker CRO ran — a second invocation of one instrument, not a second instrument.
It is corroboration; the load-bearing legs are 2-7 and 9, which are direct content reads at HEAD by a
seat that authored none of the content. The checker validates structure (required fields, status enum,
key rule), not semantics — semantic correctness rests on Andrew's ratification, which is the design.

— 3.0.0_SA_CVO
