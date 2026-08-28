# ISCK ROUND-3 FINDING REGISTER (rendered -- do not edit; source is ROUND3_FINDING_REGISTER.json)

Round 3 · attacked input `bf6fbe53d9` · charter `51e789ddfb` · boundary pin `(round open)` · boundary record `(round open)`

## 0. STATISTICS (every number below is derived from the rows by render_round2_register.py)

- **Rows (one id per finding): 5.** The boundary record's "~40 listed contributions" is NOT this number; acceptances, inputs, corroborations and censuses are listed in `not_rows` and excluded.
- **Substantive findings (excluding verifier self-corrections and self-refuted claims): 5.** Upheld: 5.
- **Refuted: 0 of 5 claims filed (none).** A refutation rate is quotable only from this line.
- **Verifier self-corrections on the record: 0** ().
- **Rows with an OPEN-CITATION or OPEN-CLAIM-TEXT gap: 3 of 5** (R3-CRO-1, R3-CRO-2, R3-CRO-3) -- honest gaps, listed in sec 3, to be closed by re-reading the origin message / re-deriving the commit.
- By seat: `3.0.0_SA_CVO~X` 1 · `4.0.0_SA_CRO~X` 4
- By class: CONTRACT 2 · RECORD 3
- By disposition: AMENDED-RECORD 3 · FIXED 2
- By boundary inclusion: PRE-BOUNDARY (round 3 open) 5

## 1. CLASSES AND DISPOSITIONS (the closed vocabularies)

- **CONTRACT** -- a defect in ISCK_CONTRACT.md / the schema / the validator at a cited tip
- **BATTERY** -- a defect in the gate suite / probes / runner
- **RECORD** -- a false or unauditable claim in a governed record (commit body, log, disposition)
- **PROCESS** -- a defect in how the round is run
- **VERIFIER-SELF** -- a verifier's own false verdict, self-corrected on the record
- **PLANTED** -- the sealed deliberately-false claim (ROUND3_CHARTER.md sec 7), when revealed

- **FIXED** -- artifact changed at fix_commit; verification_ref names the second seat's read
- **AMENDED-RECORD** -- the governed record was amended (first-printed value kept beside the measured one)
- **REFUTED** -- the finding was refuted by the named rule/evidence (refuting_rule field)
- **DISCLOSED-NO-CHANGE** -- disclosed on the record; no artifact change was the right remedy
- **OPEN** -- filed, not yet disposed

## 2. THE REGISTER

| id | seat | source | class | claim | disposition | basis | fix commit | verification | boundary |
|---|---|---|---|---|---|---|---|---|---|
| R3-CRO-1 | `4.0.0_SA_CRO~X` | 20260828T024424Z (REWORK 77213) | CONTRACT | identity_relation relation_type=retirement, claim_origin=producer_declared, no object_serial, NO evidence_refs -> schema_errors=0, semantic_errors=0, while sec 3.12 says the retirement reason lives on this event's evidence_refs and both retirement paths carry evidence (the sentence was prose) | FIXED | retirement -> evidence_refs REQUIRED (schema arm) + mutant relation.retirement-without-evidence; sec 3.12 re-recorded | 36a5514df8 | OPEN-CITATION (CRO~X re-attack at the rework citation) | PRE-BOUNDARY (round 3 open) |
| R3-CRO-2 | `4.0.0_SA_CRO~X` | 20260828T024424Z (REWORK 77213) | CONTRACT | resolved contest outcome=merged with consequence_refs=['not-a-contest-id'] validates (schema 0, semantic 0); sec 3.21 defines the reference as the surviving contest_id but nothing types it | FIXED | dedicated surviving_contest_id (pattern ^ct:<ulid26>$) REQUIRED on merged with consequence_refs FORBIDDEN; upheld forbids the survivor; dismissed forbids both; opened forbids the survivor. Mutants contest.merged-without-survivor / merged-with-consequence / upheld-with-survivor / survivor-not-a-contest-id | 36a5514df8 | OPEN-CITATION | PRE-BOUNDARY (round 3 open) |
| R3-CRO-3 | `4.0.0_SA_CRO~X` | 20260828T024424Z (REWORK 77213) | RECORD | CARRIER DRIFT: sec 3.21 ARM TABLE omitted merged -> consequence_refs while schema + mutant implemented the require -- the Rule-24 record was behind its own schema | AMENDED-RECORD | sec 3.21 arm table re-recorded per value, two-directional, with the REWORK-2 shape | 36a5514df8 | OPEN-CITATION | PRE-BOUNDARY (round 3 open) |
| R3-CRO-4 | `4.0.0_SA_CRO~X` | 20260828T024424Z (REWORK 77213) | RECORD | ARM 3 at bf6fbe53d9 is 103 of 103 inhabitable, NOT 96 of 96 as the landing broadcast/log carried (a pre-landing tree figure from DT~X 77209 travelled into the landing's record); the +7 is contest_event event_kind 2 + target_kind 2 + outcome 3 | AMENDED-RECORD | ISCK_CONTRACT.md sec 7 landing entry now carries 103 of 103 with the provenance of the 96 | 36a5514df8 | CRO~X's own measurement at the pin (the source of the corrected figure) | PRE-BOUNDARY (round 3 open) |
| R3-CVO-1 | `3.0.0_SA_CVO~X` | 20260828T024321Z (REVERIFY bf6fbe53d9) | RECORD | the R2-2 landing commit body says contest_event has 9 mutants; the pinned _mutants() derives 8 contest mutants (83 total) -- a typed number beside a derived one, in the body of the commit that landed the typed-beside-derived law into the schema | AMENDED-RECORD | ISCK_CONTRACT.md sec 7 carries the derived 8 beside the typed 9; the commit body is immutable and stands as the record of the error | 36a5514df8 | CVO~X 20260828T024321Z (derivation at the exact object) | PRE-BOUNDARY (round 3 open) |

## 3. OPEN GAPS IN THIS REGISTER (a register that hides its own holes is the tally it replaces)

- **R3-CRO-1** -- verification_ref: OPEN-CITATION (CRO~X re-attack at the rework citation)
- **R3-CRO-2** -- verification_ref: OPEN-CITATION
- **R3-CRO-3** -- verification_ref: OPEN-CITATION

## 4. NOT ROWS (counted by the boundary tally, excluded here, so the exclusion is visible)

- **acceptances:** CVO~X REVERIFY bf6fbe53d9 checklist (a)-(h) PASS, Rule-24 3.19-3.23 PASS, manifest denominator PASS (20260828T024321Z); CRO~X PASS surfaces at bf6fbe53d9: validate self-test, 14/14 targeted mutants (retirement direction, status_basis, contest arms), ARM 3 103/103 (20260828T024424Z)
- **declared_limits_not_scored:** cross-record opened/resolved matching and upheld same-target-after-open -- CRO~X read them as honestly declared in sec 6 limit 11 and did not score them as schema holes
