# VERDICT — TO-W3-CCX3 · NFRA_SUBSTRATECARDING wave 3 · 0.8.0_AE_CloudComp~X

**Verifier:** 3.0.0_SA_CVO~X · **Verdict:** **VERIFIED PASS at TO level** · 2026-08-27 ~07:1xZ
**Delivery:** @`b253369632` (cards) + rework @`06935043aa` (instance) — lane-declared LOCAL behind
the LD-0367 integrator rail, with their own firing ancestor controls; recorded as stated.

## The rework round, and why it is on the record

First gate run AT THIS SEAT returned **INVALID — 11 violations**, all in the instance wrapper
(7 free-text `method` values vs the contract enum, missing `controls.determinism` and
`controls.mutant.status`, 3 non-contract `controls` properties, `decomp_ref.pin_note`). The three
cards were clean throughout. Rework 74889 → 74897: the lane answered the asked question plainly
(**"I did not run it"** — no instrument divergence; they then reproduced all 11 exactly), and named
the transferable shape better than I would have: **rigour on the object does not transfer to the
wrapper that reports it** — six mutants and a gated negative control on the cards, zero instruments
on the instance, and the care spent on the cards is what made the instance feel already-checked.

Re-gate at my seat: **VALID, 0 violations, alignment 8/8 · 21/21 · 21/21.** Cards proven unchanged
(clean `git status` over the directory; the lane's digest comparison agrees). `controls.determinism`
was **run, not back-filled** — two same-input builds byte-identical on 3/3 digests with a
comparator negative control.

## The M4 status call — ACCEPTED as shipped

`FIRED-AS-EXPECTED` with the distinction stated in `observed` is correct: M4 probes the CONTRACT
(forward_disposition unenforced — a real finding, routed to the schema owner, which caught the
lane's own first pass), and this deliverable COMPLIES with the rule M4 tests. Marking DID-NOT-FIRE
would declare the deliverable invalid for a schema hole it obeys. Floor-to-the-enum with declared
specificity is the established handling (74869) and the enum's missing member ("control fired; a
sibling probe found a contract gap") is one more row for the schema owner.

## Carried into the record

- **QUALIFIED ×3, none SOUND** — and SOUND was *available* under the validator for both
  derive_runner cards (the contract permits SOUND over inferred rows); they ship QUALIFIED because
  the enum's words bind. The lane refused a green the validator would have given.
- **The three-writer census correction** (two → three writers of graph_nodes, by a second
  instrument over 7,236 files) with the set-level contention finding — full-overwrite
  (derive_runner PATH A, comp_aws_cli:3051) vs scoped `overwrite_filter` (lambda_function:501),
  the 409 race visible at one site of three — carded as a disclaimed limit on all three cards
  because no per-subject cell owns a relationship.
- **AC5's trap fired exactly as written:** taskdef `command=null`, CMD from BUILD INPUT against a
  MUTABLE `:latest` tag — `actual_trigger` ships basis=inferred; both trigger planes swept with
  printed denominators. PATH A additionally EXERCISED (the 02:10Z run observed live, including the
  PATH A/PATH B authority boundary firing in its own log line).
- **Two deliberate no-verdicts** (dormancy with no instrument — a producer's "2 invocations ever"
  self-report NOT converted into a measured value; coverage denominator with Nessie unreachable) —
  and the scope note where the artifact beat the respawn brief, measured before starting.

## Scope

PASS closes the TO against itself and the certified decomp id space (@`049ff4ca4a` freeze, CERT
@`d2f7dffeeb`). The two unenforced-contract findings and the enum gap ride to the schema owner;
the set-level multi-writer hazard is the issuer's record (74893).

— 3.0.0_SA_CVO
