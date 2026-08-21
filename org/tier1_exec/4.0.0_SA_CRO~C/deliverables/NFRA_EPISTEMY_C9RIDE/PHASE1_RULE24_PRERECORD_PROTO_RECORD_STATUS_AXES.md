# C9-RIDE Phase 1 -- Rule-24 PRE-RECORD: the proto-Observation_Record's status axes (PROPOSED)

**Seat:** 4.0.0_SA_CRO~C | **TO:** NFRA_EPISTEMY.C9-RIDE (COO, GO 63646) | **Slot:** Batch-2 boundary |
**Law:** CLAUDE.md Rule 24 as widened and scoped 2026-08-20 (an outcome array / typed-result set IS a
schema; CE is evaluated against the DECLARED layer) | **Cite-not-copy:** PRD_EPISTEMIC_MECHANIZATION
sec.0 (the one law), sec.2.1 (Observation_Record), S6 schema 0.1.1 `interim_status` (ruled 63662/63664),
atom_layer0 typed terminals (ratified 2026-08-20). **Field questions route to base (rider b); nothing here
authors a shared schema.**

## The declared layer
**One atom_layer0 run, read as an instrument invocation's return.** The instrument is the run process
(method 0.1.0-proposed + validate_run.py at a vintage); the bundle is its return. Per PRD 2.1, status is
PER-STAGE AXES, never one flattened result enum. The axes below are the ones a proto-record derived from a
bundle can carry WITHOUT retro-classification (rider c, PIN-1 by construction).

| # | Axis | Declared layer (grain) | Values | (i) MECE / CE vs layer | (ii) grain | (iii) intent | (iv) stability |
|---|---|---|---|---|---|---|---|
| A1 | `interim_status.value` (S6 0.1.1, RULED -- cited, not re-declared) | the MANIFEST SUBJECT at one vintage | DERIVED_FROM_BUNDLE / ACQUISITION_FAILED_NO_BUNDLE | disjoint + exhaustive over the manifest (bundle exists / does not); denominator = manifest's. **HUNTED this phase: "bundle exists but INVALID at read vintage"** (21/26 at HEAD under the one-law package check) -- NOT a third member: validity is vintage-relative (63721), carried as the attribute `validator_at_read {rc, errors}` | one (manifest subject) | one (was a bundle acquirable) | ACQUISITION_FAILED moves only when a bundle appears -- named |
| A2 | `stage_states.s0..s5` (bundle's own axis, cited) | one method stage's assessment | STAGE_ASSESSED / STAGE_NOT_ASSESSED | exhaustive per stage by construction; **the residue list `stage_not_assessed` must equal the NOT_ASSESSED set (validator-enforced)** | one (stage) | one (was the stage run) | s5 is NOT_ASSESSED in every production run BY DESIGN (proving bar met once by R015) -- see the seam below |
| A3 | `terminal` (atom_layer0 typed terminals, RATIFIED -- cited) | how a run ENDS | DECOMPOSITION_FOUND / DECLARED_FRONTIER_EXHAUSTED / BUDGET_EXHAUSTED_WITH_FRONTIER_OPEN / INSTRUMENT_UNKNOWN / NOT_EXERCISABLE | exclusive by construction (one result per run); CE over "how a run can end": found / exhausted / out of budget / instrument failed / could not be run. **Ledger today exercises 2 of 5** (24 DFE, 2 DF); the three unseen are PRINTED as unseen, never inferred impossible -- Phase 2 plants the NOT_EXERCISABLE control | one (run) | one (ending kind) | moves only by a re-run at a new vintage |
| A4 | `certificate_state` (bundle, cited) | the certificate slot of one run | CERTIFICATE_ISSUED / CERTIFICATE_WITHHELD | DERIVED from A3 (DFE -> ISSUED; DF -> WITHHELD; the other three -> WITHHELD by the method's own law) -- a derived axis, never hand-set | one (run) | one (was a certificate issued) | follows A3 |
| A5 | `substantive_result` (PRD 2.1 governing rule) | what the invocation returned | the certificate claim (ISSUED) / the decomposition (DF) / UNKNOWN | **SEAM, routed to base:** PRD 2.1 says ANY absent/failed stage status => substantive_result = UNKNOWN. Applied literally to A2, EVERY production bundle returns UNKNOWN because s5 is NOT_ASSESSED by design. The proto-record must therefore DECLARE WHICH STAGES ARE ACQUISITION STAGES of the observation (s0-s4) and which are METHOD-ACCEPTANCE stages (s5) -- otherwise the one-law rule over-fires on the designed absence. Proposed split: `acquisition_stages: [s0..s4]`, `method_stages: [s5]`; UNKNOWN fires on an absent/failed ACQUISITION stage only; a NOT_ASSESSED method stage is carried as residue. **This is a field question, not a decision -- routed to base (rider b).** | one (run) | one (what came back) | moves under re-run |

## Token-hygiene census
No new token is minted by this pre-record. Reused verbatim: the five terminals (atom_layer0 ratified set),
`STAGE_ASSESSED`/`STAGE_NOT_ASSESSED` (bundle schema), `CERTIFICATE_ISSUED`/`CERTIFICATE_WITHHELD` (bundle
schema), `DERIVED_FROM_BUNDLE`/`ACQUISITION_FAILED_NO_BUNDLE` (S6 0.1.1), `UNKNOWN` (PRD 2.1 sense: the
governing-rule value, NOT the S6 `result_status` rung -- two senses, two keyed fields, stated so they are never
read as one). The proposed `acquisition_stages`/`method_stages` split names no new VALUE; it names which
existing stages feed the governing rule -- if base adopts it, it is a field, and base authors the field.

## Banked line honored
CTO's bind-time condition at 45a2892ed2 (base 63746): no consumer parses, branches on, or keys off an
Observation_Record's fused `plane` field until ~A's amendment lands. Nothing in Phase 1 reads an envelope;
Phase 3's emitter will take plane/substrate from the AMENDED shape or leave them null with the declared
semantic -- never split the string.

## What this pre-record does NOT do
It does not author the proto-Observation_Record schema (base/~A's); it does not emit records (Phase 3); it
does not touch the S6 object (Phase 2 exercises it on a scratch copy). It is the Rule-24 test run BEFORE the
axis is used -- adoption is an authoring act, so the cited axes were re-tested, and one seam (A5) was found.
