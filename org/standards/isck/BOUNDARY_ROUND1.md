# ISCK ADVERSARIAL PASS — ROUND-1 BOUNDARY RECORD

**Pass released by Andrew** 2026-08-27 ~18:4xZ, scoped: `2.0.0_SA_COO~X`,
`0.4.0_DT_ClientPlatform~X`, `3.0.0_SA_CVO~X`. **Target frozen for the whole round at
@8ba18439dd** (all three seats verified the freeze before attacking; no edit landed mid-round).
**v0.1 is the single boundary revision** — every upheld finding fixed in one commit, per the
target-discipline rule (the contract owner is not the moving target).

## TALLY — 21 findings + 3 refutations/nulls, ALL adjudicated

| seat | findings | refuted/null |
|---|---|---|
| `2.0.0_SA_COO~X` | F1–F7 (+ probe-2 self-falsification of F4's denominator) | 2 attacks refuted; isolation 19/19 |
| `0.4.0_DT_ClientPlatform~X` | DT-1–8 + run-status set | attribution probe = null (named as repetition of the isolation result, with the isolation-vs-attribution distinction banked) |
| `3.0.0_SA_CVO~X` | CV-1–6 | condition-2 re-expressibility: CONFIRMED, strictly sharper, one carried requirement |

Every finding's disposition and fix is mapped in `ISCK_CONTRACT.md` §7 (changelog). Self-test at
this commit: **4/4 axes + 11/11 fixtures + 36/36 reason-asserted mutants + 6/6 semantic mutants +
gutted-schema meta-control, exit 0.**

## THE ORGANIZING STATEMENT (DT~X's synthesis, adopted)

v0 was DENSE ON SHAPE (patterns/enums/required/additionalProperties — negative arm verified 19/19,
twice, by two differently-shaped probes) and NEARLY EMPTY ON FIELD-TO-FIELD OBLIGATION — which is
precisely where a record can validate while lying. v0.1's fixes are almost entirely
field-relation conditionals; the record types now carrying conditionals: entity_binding,
state_observation, identity_relation, materializer_version, materialization_run,
coherence_evaluation (6 of 10).

## REGISTERED PREDICTION (testable at round 2 — DT~X, verbatim commitment)

If the thinness was STRUCTURAL, round-2 findings cluster in the record types STILL without
field-relation conditionals after this commit: **materializer, source_frontier, surface_version,
entity** (4 of 10). If round 2 instead finds its next tranche inside the newly-conditioned records,
the characterization was wrong. ARM 1 re-differencing adjudicates.

## INDEPENDENCE LEDGER — who converged with whom, honestly

- **F5 ↔ DT-1/DT-5: ONE finding class, semi-independent members.** Ordering MEASURED: the F5
  disposition reached DT~X's inbox 18:52:49Z; DT's report left 19:05:34Z (12m43s, wrong
  direction; DT~X confirmed reading it pre-probe). Instrument-independence: upgraded from
  "plausible" to **measured once** (ARM 1 emitted DT-7, a class sibling, mechanically in a staging
  run with no disposition naming its subject) **with the BUILD-TIME ANCHOR unresolved and
  unresolvable** — anchoring can enter at which-tool-to-build, not only which-finding-to-report,
  and a tool cannot see its own origin. (Named class, new to the estate this session.)
- **CV-3 extends F5's class to record #10** — reported after the F5 disposition broadcast;
  same semi-independent standing, disclosed inline by its author.
- **Isolation (COO~X) vs attribution (DT~X) on the negative arm: REPETITION by the authors' own
  labels** — different questions ("exactly one rule" vs "the RIGHT rule") that agreed at v0; both
  now standing arms.
- **CVO~X's round was SEMI-BLIND by my own act** (the disposition broadcasts anchored headline
  grain before their round opened) — their per-limit sec-6 verdicts and CV-3/CV-4/CV-5 subjects
  were not named in any broadcast and carry full weight; classifications overlapping DT-2 carry
  semi-blind weight. **Integrator lesson, now practiced: disposition broadcasts are ANCHORING
  EVENTS — dispositions go to the finding's own seat while other rounds run; the tally goes to
  everyone at the boundary. This document is that tally.**
- **ROUND 2 IS INHERENTLY NON-BLIND FOR EVERYONE** (this record publishes everything). Round-2
  agreement is shared-context convergence and MAY NOT be cited as corroboration. The one blind
  still purchasable: a method no seat has run.

## WHAT WAS NOT ATTACKED (named, so silence is not coverage)

- The BRIDGE_ASSERTION record does not exist yet — CV-1's carried requirement
  (`admitted -> evidence_refs`) binds its author; nothing could attack an absent record.
- The evidence-independence limit (§6 item 2) entered at this boundary — its designated
  non-author attack (`3.0.0_SA_CVO~X`) is ROUND-2 work, scheduled.
- Cross-fabric reconciliation flows (candidate_equivalence at scale) — no multi-fabric instance
  data exists to attack; WP-3 territory.
- The three COO~X gate probes and DT~X's coverage module attack the CONTRACT+BATTERY; nobody has
  yet adversarially attacked THE PROBES themselves beyond their self-controls.

## FIXTURE COVERAGE (DT-6's lens, applied)

11 fixtures over 10 record types; both bundle_completeness arms now positively inhabited; every
conditional then-arm carries >=1 negative mutant; accepting else-branches inhabited by fixtures
except: `disputed` binding, `partial`/`failed` runs, `held`/`inadmissible` registry rows (no record
carries registry_standing until BRIDGE_ASSERTION), `provisional`/`contested` entities —
**round-2 fixture debt, listed rather than implied covered.**

## PROCESS ARTIFACTS THE PASS PRODUCED (beyond the contract)

The anchoring-events rule · the build-time-anchor class · the sender-unverified-ACK tell (an
unverified ACK evidences a process, not a seat) · isolation-vs-attribution as distinct negative-arm
questions · the F4 self-falsification (a census over 10 declared enums when the schema holds 18 —
the tool falsified its own author's headline, and the author reported it) · COO~X's uniform-rejects
instrument catch (a uniform result is an instrument signature) · the tail-pipe rc trap re-measured.

— boundary compiled by `1.0.0_SA_CTO~X`, 2026-08-27; probe modules land beside this record under
their authors' own lines; round 2 opens when they land.
