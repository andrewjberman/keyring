# ARM-4 ADJUDICATION — 25 require-only candidates: 4 forbid-mirrors CUT, 21 ruled NO with reasons

**Adjudicator:** `1.0.0_SA_CTO~X` (the forbid-mirror decision is this seat's, per the ARM-4
routing) · **Instrument:** `isck_coverage_probes.py` ARM 4 (`0.4.0_DT_ClientPlatform~X`'s gate),
run at the adjudication commit · **Test applied per candidate (the probe's own instruction):**
construct the record the missing forbid-partner would reject and ask whether the field's PRESENCE
CONTRADICTS the discriminant value. A forbid-mirror is cut ONLY on contradiction — the paired-arm
idiom exists to kill stale-transition drift and costume states, never to ban harmless surplus.

**Denominator: 25 of 25 adjudicated. This record is the consuming half — a candidate list nobody
adjudicates re-flags forever, and each NO below names the reason a future run must overcome to
re-open it.**

## CUT — 4 forbid-mirrors (each landed as a schema arm + a target-declared mutant)

| # | record · arm | ruling |
|---|---|---|
| 1 | `bridge_assertion` `held` -> `held_on` | **FORBID on `registry_standing != held`.** `held_on` names the item a hold rests on; append-only doctrine cuts a NEW assertion per transition, so a non-held standing still carrying `held_on` is stale-field drift surviving a transition — exactly the class the paired-arm idiom kills. Mutant `bridge.held_on-outside-held`. |
| 2 | `bridge_assertion` `inadmissible` -> `store_owner` | **FORBID on `registry_standing != inadmissible`.** `store_owner` exists to name who refused at the door (F2's value-carries-owner); on any other standing it conflates the inadmissibility door with the merits door — `rejected` + `store_owner` reads as refused-at-the-door when it was adjudicated on merits. Mutant `bridge.store_owner-outside-inadmissible`. |
| 3 | `materializer_version` `complete` -> six digests · the INVERSE arm | **FORBID `absent_components` on `bundle_completeness = complete`.** A complete bundle LISTING absent components is a direct contradiction (complete means the absent set is empty). Survives the R2-2 3d split unchanged — `complete` still forbids a cause-of-absence carrier. Mutant `mv.complete-with-absent-components`. |
| 4 | `coherence_evaluation` `mismatch` -> `delta_summary` | **FORBID `delta_summary` on `integrity in {verified, unverified}`.** A delta summary is the PRODUCT of a comparison; on `verified` it asserts a mismatch the value denies, on `unverified` it asserts a check the value says has not run — **the CITATION my first cut lacked: §3.14's remedy column defines `unverified` by "run the check — checker", i.e. the check has not been run.** `4.0.0_SA_CRO~X`'s re-dry finding was RIGHT that the premise was uncited and that §3.14's "FREE by design" read as contradicting the arm; I first NARROWED to `verified` (@c1edaf9638), then `3.0.0_SA_CVO~X` (CV-3's author) supplied the rubric — FREE meant free of REQUIRED WARRANTS, never free of forbids — and the choice became (B): keep the wide arm and fix the DOCTRINE sentence, landed atomically with this row. The alternative (A: unverified carries a provisional delta as observation-not-verdict) would need its own claim field, new surface for a state nobody has asked for. Mutant `ce.delta-summary-on-verified`. |

## NO — 21 candidates, by class (the reason IS the record)

**CLASS A — evidence is MONOTONE (12 candidates: every `-> evidence_refs` arm across
bridge_assertion, coherence_evaluation, entity_binding, identity_relation, mint_receipt,
state_observation).** Evidence presence contradicts NO status value: an `unverified` record MAY
carry evidence that exists but has not been weighed; a `candidate` MAY carry the evidence it will
be adjudicated on; `declared_by_author` origin MAY still attach substantiation. A forbid here
would BAN documentation on exactly the records that most need to accumulate it before their next
transition. The require-direction (strong values must show evidence) is the whole law; the
forbid-direction is anti-law.

**CLASS B — partial bundles digest what they DO carry (6 candidates: `complete` -> each of
`configuration_digest`, `declared_opinions_digest`, `dependency_lock_digest`,
`normalizer_versions`, `runtime_contract_version`, `source_tree_digest`).** A `partial_legacy`
(post-R2-2: `partial`) bundle legitimately digests its PRESENT components — forbidding digests on
partial would punish partial bundles for documenting themselves, inverting the incentive the
completeness axis exists to create. Presence contradicts nothing; absence of the ABSENT ones is
already the `absent_components` carrier's job (and its inverse is CUT #3).

**CLASS C — RE-RULED on DT-R2-6 (1 candidate: bridge_assertion `contradicted` ->
`adjudicated_by`).** My first row declined the mirror because it would "manufacture" ARM-3
unsatisfiability. `0.4.0_DT_ClientPlatform~X` showed the unsatisfiability ALREADY EXISTED —
allOf[4] (candidate forbids adjudicated_by) x allOf[7] (contradicted requires it) made
candidate x contradicted UNINHABITABLE, with a positive control (admitted x contradicted VALID) —
so the reason given did not distinguish the mirror from the status quo. Re-ruling: candidate x
contradicted SHOULD be expressible (a parse-derived candidate contradicted on evidence before any
registry act is a real state). Contradiction is EVIDENTIAL; adjudication is a registry/contest
act — the `contradicted -> adjudicated_by` REQUIRE was the wrong arm and is RETIRED on BOTH
consumers (DT-R2-2's shared-enum rule; `3.0.0_SA_CVO~X` 77053 caught the bridge-only draft),
with §3.2 re-recorded (enter on evidence, leave by adjudication via `contest_resolved`). The
candidate is therefore MOOT, not NO: no require arm remains to mirror.

**CLASS D — DEFERRED BY LANDED DESIGN (2 candidates: `superseded` -> `superseded_by` on
bridge_assertion and identity_relation).** The attacked-dry R2-2 design makes `superseded_by`
PRESENCE the supersession carrier and `corroborated` + `superseded_by` the desired, expressible
state — a forbid-mirror cut today ("superseded_by only on superseded") would be REVERSED at the
R2-2 landing, and the require arm itself dies there (`superseded` leaves the axis). Cutting a
control scheduled for reversal is churn, not coverage. Re-adjudicate iff R2-2 fails to land.

**Coverage check: 4 + 12 + 6 + 1 + 2 = 25.**
