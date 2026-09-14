# LGIC_NAMING round 1: CVO adjudication (L8 compile + L9)

Round 1 of `LGIC_NAMING`, compiled and adjudicated by `3.0.0_SA_CVO` on 1.0.0_SA_CTO's re-arm (96661) and 2.0.0_SA_COO~G's drain-end read (96660). The pre-issuance intake is `ADJUDICATION_v1.md` (C-S1, C-S2, rows S1-S10). This document carries the 23 rows that were carrier-less at L8 (S11, S12, S13 and 20 worker rows) and the four judgment grades. Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md`.

```json
[
 {
  "id": "LGIC_NAMING-C-S3",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T18:42:49Z",
  "one_line": "ROUND-1 L9 GRADE RECORD: the four JUDGMENT criteria, one verdict each, bound to each proof instance at its commit -- 4 PASS, 3 of them with a named qualification (F1-J1, G1-J1, H3-J1) and T1-J1 MET.",
  "class": "OBSERVATION",
  "spec_asserts": "Spine L9: a JUDGMENT criterion is graded by the CVO against the specification that issued it, never self-graded; its verdict lives in `grades`, one entry per criterion, on a row of the CVO's.",
  "world_is": "4 judgment criteria exist across the 14 orders (F1-J1, G1-J1, H3-J1, T1-J1); each instance records UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming this seat. The evidence and this seat's own reads are in the L8/L9 record, section 3. Vocabulary as IRPT_FNTEND: MET -> PASS; MET WITH A NAMED QUALIFICATION -> PASS with the qualification in `reason`; NOT MET -> FAIL.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~1/LGIC_NAMING.TO-LN-f-1.firm-patterns.proof_of_spec.json@d9ccd9babd",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~1/LGIC_NAMING.TO-LN-g-1.grading-rule.proof_of_spec.json@51b0952d71",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~5/LGIC_NAMING.TO-LN-h-3.grading-agreement.proof_of_spec.json@f829fdb1fc",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~2/LGIC_NAMING.TO-LN-t-1.tension-ranking.proof_of_spec.json@36afc955ba",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same commit series) section 3",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md@51b0952d71"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade record: it adjudicates no item and opens nothing. Each qualification is carried by the graduated row it names (W1-S3, W1-S5, W5-S5, S12) and reaches 1.0.0_SA_CTO in the round-1 slug.",
  "hazard_standing": "INERT",
  "grades": [
   {
    "criterion": "F1-J1",
    "instance": "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~1/LGIC_NAMING.TO-LN-f-1.firm-patterns.proof_of_spec.json@d9ccd9babd",
    "verdict": "PASS",
    "reason": "MET WITH A NAMED QUALIFICATION. This seat re-derived 12 of the 69 by hand from GRADING_RULE.md R1-R9 and V1-V4 at 51b0952d71 (= HEAD), stratified across every class: bd-49f-auto-login and bd-cot-keepalive (ALIAS to blackdiamond-*), cot-bd-session-trigger-lambda-role (blackdiamond as system), bd-allocation-checker-lambda-role, inf-accounts-v2-daily-role, wsb-49f-model-aua-daily-role and demo-transform-runner-ec2-role ({system} placeholder), inf-api-eclipse-role -> eclipse-inf-api-role, irpt-core-firm-49financial -> irpt-49f-core-firm-role, opal-assets-mirror-cot-scheduler-role -> opal-cot-assets-mirror-scheduler-role, advi-49f-floor-scheduler-role (CONFORMANT), and wp5-49f-feeder-scheduler-role (RAISE at R1.f). 12 of 12 match. The one exclusion's reason holds. QUALIFICATIONS: (1) 48 of 68 canonical forms carry {system} (R1.d), so the attribution is exact but those forms are not full names (row W1-S3); (2) R1.d is read to admit bd-as-vendor as a V1 token, a reading R3 supports and the worker flagged; (3) the exclusion is a RAISE filed in a slot the order defines as no firm's principal (row W1-S5). INSTRUMENT: a second reader by hand over a sample, not the worker's hand-plus-script over all 69."
   },
   {
    "criterion": "G1-J1",
    "instance": "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~1/LGIC_NAMING.TO-LN-g-1.grading-rule.proof_of_spec.json@51b0952d71",
    "verdict": "PASS",
    "reason": "MET WITH A NAMED QUALIFICATION. Two graders who did not write the rule agree on 85 of 85 discriminating names on verdict AND canonical form (H3-AC1), 37 OUT-OF-PATTERN forms included. Their result files are different work: grader A lists 6 places where the rule left a reading to choose, grader B lists 3; 2 are shared and each was resolved by the same clause. That is the discriminator this grade weighs: independent passes over an exact rule. QUALIFICATIONS: (1) the two answer files are byte-identical (sha256 41c3de9d...ffde945, committed 43 s apart from one base 3d671ff59c); byte identity alone cannot separate independent grading from one grader reading the other's file on disk, and H3-AC3 excludes only base contamination; (2) exact is not complete: the placeholder canonical forms (row W1-S3) are deterministic but are not the full correct name FWD-5 asks for, which is the CTO's close read; (3) grader A emitted its TSV with a generator keyed to its hand verdicts, disclosed in grader-a.result.md; (4) both graders ran on the preloaded context of row S12."
   },
   {
    "criterion": "H3-J1",
    "instance": "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~5/LGIC_NAMING.TO-LN-h-3.grading-agreement.proof_of_spec.json@f829fdb1fc",
    "verdict": "PASS",
    "reason": "MET WITH A NAMED QUALIFICATION. 0 disagreements over 85 (and 0 over 88). 18 of 18 RAISEs are tabled with a step and the rule line it exposes. This seat read every cited line at GRADING_RULE.md@51b0952d71 (= HEAD): :26-27 the RAISE clause, :55 G2.2, :56-57 G2.3, :100 V2, :143 R1.c, :150 R1.f, :157 R2, :226-227 L3, :258-259 K1; each says what the table says, and the table sums to 18. QUALIFICATION: the step column comes from grader B's result file only. The answer format the order set has no step field, although :26-27 says a RAISE output names its step, so grader A's steps are inferred from its identical verdicts, not read (row W5-S5)."
   },
   {
    "criterion": "T1-J1",
    "instance": "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~2/LGIC_NAMING.TO-LN-t-1.tension-ranking.proof_of_spec.json@36afc955ba",
    "verdict": "PASS",
    "reason": "MET. All 10 cost lines state what breaks, what someone does by hand or what is blocked, in plain words. Each quotes its figure with the section of brief 1b42dbe758 Part IV or 09_NAMING_CENSUS.md it comes from, or says plainly that neither source gives one (rows 3 and 10; row 5 states the census breaks down 145 of 339). So every line can be disputed against a named source. The ranks are the brief's and are stated as not re-ranked; no row proposes a fix."
   }
  ]
 },
 {
  "id": "LGIC_NAMING-C-S4",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T18:42:49Z",
  "one_line": "ROUND-1 L9: three rows DISMISSED_WITH_REASON, each read against the artifact that closes it -- S11 (the N6 count, carried by the issuance), W1-S1 (the widened census, carried by the list) and W1-S2 (the system registry, which is LGIC_ENFORCE's product).",
  "class": "OBSERVATION",
  "spec_asserts": "Each row names what would close it: an N6 sample cut by the stated rule (S11); a legacy list built from a census that finds every request site (W1-S1); a registry that holds the platform subsystems (W1-S2).",
  "world_is": "S11: N6_SAMPLE.json carries 85 + 3 with a count_note naming S11, and H3-AC1/H3-AC2 ran on 85 (84 as a name set, explained in n6-compare.md section 1); the frozen decomposition's 86 is context. W1-S1: LEGACY_SERVED_PATHS.json's `census` field prints the named instrument (122 lines) and the widened ones (401 + 47 + 30 lines) and resolves 39 request sites. W1-S2: the registry's rows, the PLATFORM_SUBSYSTEM class included, are produced by LGIC_ENFORCE (its PRD CONTRACTS row and cell E2; LGIC_CANON_PRD :27 concurs), and GRADING_RULE.md V1 labels itself INTERIM until those rows exist (:95-97).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-S11",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/N6_SAMPLE.json@777770e6aa",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n6-compare.md@f829fdb1fc",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W1-S1",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json@51b0952d71",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W1-S2",
    "org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md@78128f29ea :150 (registry ROWS produced), :163-168 (DEC-1, the PLATFORM_SUBSYSTEM class), :349 (cell E2)",
    "org/missions/D14/LGIC/LGIC_CANON/prd/LGIC_CANON_PRD.md@d9977a0f40 :27",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md@51b0952d71 :95-97"
   ]
  },
  "adjudicates": [
   "LGIC_NAMING-S11",
   "LGIC_NAMING-W1-S1",
   "LGIC_NAMING-W1-S2"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "S11 and W1-S1 are closed in the artifacts named. W1-S2's remedy lies outside this project's chain: the system registry is LGIC_ENFORCE's cell E2 (PRD admitted at v1.1), so per spine L10 it is not recut here and this row names the record that owns it. GRADING_RULE V1 reads the registry once E2 lands; LGIC_ENFORCE is next in the sequence.",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_NAMING-C-S5",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T18:42:49Z",
  "one_line": "ROUND-1 L9, FWD-1, GRADUATED: two blind namers agree on 9 of 18 because NAMING_SCHEMA v1.4 leaves four slots unruled -- the function/purpose vocabulary (7 of the 9 differences), the entity-partition token, GLOBAL vs PRODUCT scope for a product-shared key, and vendor-as-system for a derived-tier resource.",
  "class": "OBSERVATION",
  "spec_asserts": "FWD-1 DONE WHEN: two people have named the same new thing without conferring, and matched (EXERCISED).",
  "world_is": "E3-AC1 printed FAIL-DIFFERENT, 9 of 18 identical (W5-S2); E3-AC2 printed PASS-BLIND, so the namers did not see each other's work and the 9 differences are the schema's, not collusion. The namers' own rows attribute each difference before the comparison ran: function/purpose open (W2-S1, W3-S2; NAMING_SCHEMA :56 has no list), the {entity} token of key.partition (W2-S2, W3-S1; :41), the scope class of an all-firm key under a product source (W2-S3, W3-S3; :33, :114), and vendor-as-system for a derived tier (W2-S4, W3-S3; :121).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W2-S1",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W3-S2",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W2-S2",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W3-S1",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W2-S3",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W2-S4",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W3-S3",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W5-S2",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same commit series) section 2"
   ]
  },
  "adjudicates": [
   "LGIC_NAMING-W2-S1",
   "LGIC_NAMING-W3-S2",
   "LGIC_NAMING-W2-S2",
   "LGIC_NAMING-W3-S1",
   "LGIC_NAMING-W2-S3",
   "LGIC_NAMING-W2-S4",
   "LGIC_NAMING-W3-S3",
   "LGIC_NAMING-W5-S2"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_NAMING-C-S6",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T18:42:49Z",
  "one_line": "ROUND-1 L9, FWD-2, GRADUATED: the reader measure was not taken as cut -- every blind cell ran on a preloaded context that names the firms (W6-S1 measured, S12 widened to 6 cells), a blind cell must read the channel to mint its row id (W6-S3), the reader was never given the key's none/global rule (W6-S2, all 4 of E5-AC1's misses), and E5-AC1 with E5-AC2 is unsatisfiable on N3_KEY (S13, W5-S4).",
  "class": "BLOCKING",
  "spec_asserts": "FWD-2 DONE WHEN: someone new to the estate has read names and pointed at the firm in each, unaided (EXERCISED); LN-e-4 face: 'You have never seen this estate, and you read the names alone.'",
  "world_is": "The harness loads CLAUDE.md and the memory index into every worker before its first tool call, so blindness to the estate's vocabulary cannot be secured by spawn timing or instruction (S12: measured on e-4, NOT-EVALUATED on e-1, e-2, l-2, h-1, h-2; E3-AC2 shows mutual blindness does hold). The reader marked the firm token right on every name that carries one; its 4 misses (i07, i08, i14, i17) are the names with no firm token, where N3_KEY applies 'none'/'global' by a rule the reader's order does not state. A key-perfect reader still fails E5-AC2 on etfs (i08, i17), because the check counts a product token read as a system in one name and as a scope in another as two referents. LN-e-5's two FAILs therefore measure the cut, not the reader.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W6-S1",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-S12",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W6-S3",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W6-S2",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W5-S3",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W5-S4",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-S13",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same commit series) section 2"
   ]
  },
  "adjudicates": [
   "LGIC_NAMING-W6-S1",
   "LGIC_NAMING-S12",
   "LGIC_NAMING-W6-S3",
   "LGIC_NAMING-W6-S2",
   "LGIC_NAMING-W5-S3",
   "LGIC_NAMING-W5-S4",
   "LGIC_NAMING-S13"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_NAMING-C-S7",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T18:42:49Z",
  "one_line": "ROUND-1 L9, FWD-4, GRADUATED: a reader who learned the seven-segment layout marked the v1.3 code-tier address (six segments, no object, a tier word in the table slot) DOES-NOT-FIT -- so either the code tier is a second layout FWD-4's 'nothing new to learn' does not admit, or the briefing omitted a form the schema rules.",
  "class": "OBSERVATION",
  "spec_asserts": "FWD-4 DONE WHEN: someone who knows one location's layout has read an address in another and understood it correctly (EXERCISED).",
  "world_is": "L3-AC1 printed FAIL-MISREAD, 5 of 6; L3-AC2 printed PASS-CONTROL-FLAGGED. The briefing N5_ADDRESSES.json :6 teaches {source}/{scope}/{tier}/{table}/{partition}/{object}; NAMING_SCHEMA key.code rules {source}/{scope}/code/{built_tier}/{file}, and N5_KEY reads a3 by that form. The reader's miss is exactly the gap between the two.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W5-S1",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same commit series) section 2"
   ]
  },
  "adjudicates": [
   "LGIC_NAMING-W5-S1"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_NAMING-C-S8",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T18:42:49Z",
  "one_line": "ROUND-1 L9, FWD-5, GRADUATED: the rule is exact on its sample (85 of 85) but not complete -- three name classes get placeholder canonical forms (W1-S3), AWS-fixed names inside graded types RAISE by shape and one is invisible (W1-S4), and the answer format has no field for the step the rule says a RAISE names (W5-S5).",
  "class": "OBSERVATION",
  "spec_asserts": "FWD-5 ACCEPT: two people reach the same answer for every name, including the correct name for each one that breaks the pattern; a name the rule cannot place is a flaw in the rule, fixed there.",
  "world_is": "W1-S3: from (name, type) alone the system, source/scope or cadence of three classes cannot be completed, so 48 of 68 LN-f-1 forms and several N6 forms carry a placeholder. W1-S4: types_not_graded_by_kind excludes AWS-issued names by type only; SECURITY_GROUP default, 9 of 417 AWS/Amazon policies and 4 of 264 log groups RAISE at G2, and ReadOnlyAccess cannot be told from a customer policy. W5-S5: n6-grader-{a,b}.tsv are type, name, verdict, canonical_form; GRADING_RULE :26-27 requires the raising step.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W1-S3",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W1-S4",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W5-S5",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same commit series) section 2"
   ]
  },
  "adjudicates": [
   "LGIC_NAMING-W1-S3",
   "LGIC_NAMING-W1-S4",
   "LGIC_NAMING-W5-S5"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_NAMING-C-S9",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T18:42:49Z",
  "one_line": "ROUND-1 L9, FWD-3, GRADUATED: LN-f-1's output has two dispositions (attributed with a canonical form, excluded as no firm's principal) and no slot for a firm-owned role the rule RAISEs -- and LGIC_ENFORCE E9 reads this list (gate G-B), so the shape travels.",
  "class": "OBSERVATION",
  "spec_asserts": "LN-f-1 order: attributed entries carry a canonical form; excluded entries carry why the role is no firm's principal.",
  "world_is": "One of 69 roles (wp5-49f-feeder-scheduler-role) RAISEs at R1.f; it is filed under excluded with a reason that says it is 49 Financial's and a RAISE. check_ln.py f1_covered counts only attributed-or-excluded, so a third list would read uncovered. For FWD-3's close read: the four patterns catch 68 of 68 canonical forms with 0 cross-firm, and 12 of 68 live names today.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W1-S5",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same commit series) section 2"
   ]
  },
  "adjudicates": [
   "LGIC_NAMING-W1-S5"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_NAMING-C-S10",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T18:42:49Z",
  "one_line": "CVO OBSERVATION: the investigation schema's grade carrier cannot hold this round's grades -- grades[].criterion requires '^[A-Za-z0-9]+-AC[0-9]+$', but LGIC_NAMING's four judgment criteria are named F1-J1, G1-J1, H3-J1 and T1-J1, the ids its task orders and proof instances carry. C-S3 lands by an audited override.",
  "class": "OBSERVATION",
  "spec_asserts": "org/surprise_channel/schemas/investigation_item.schema.json grades.items.criterion: 'the criterion id as the task order names it ... the same string the proof-of-spec instance's acceptance row carries, so the grade and the row it grades resolve to one id.'",
  "world_is": "The same property's pattern admits only <X>-AC<n>, so the description and the pattern disagree for any judgment criterion named otherwise. The four LGIC_NAMING orders name theirs <X>-J1; proof-of-spec-check reads those instances VALID, so the task-order grammar admits them. jsonschema 4.26 (Draft 7) over this document's 8 new rows reports exactly 4 violations, all this pattern, and no other. Renaming a criterion to fit the pattern would make the grade and the row it grades resolve to two ids -- the defect the description exists to prevent.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/surprise_channel/schemas/investigation_item.schema.json@e3e999c139 properties.grades.items.properties.criterion (pattern and description)",
    "task-orders/LGIC_NAMING.TO-LN-{f-1,g-1,h-3,t-1}.*.md: <criterion id=\"F1-J1|G1-J1|H3-J1|T1-J1\" ... judgment=\"true\"/>",
    "the gate's refusal at this seat's first commit attempt of this document, 2026-09-14 ~18:4xZ: 'LGIC_NAMING-C-S3: schema violation at /grades/N/criterion -- ... does not match ^[A-Za-z0-9]+-AC[0-9]+$'"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Outside this project's chain: the channel schemas and the gate are 1.0.0_SA_CTO's (the gate's own refusal text names it as the owner). The fix is in place in that lane -- widen the pattern to the task-order criterion grammar, or rule a J-to-AC mapping. Until then this row and the audited override on this commit are the record; no LGIC_NAMING cell carries it.",
  "hazard_standing": "INERT"
 }
]
```

## Supplement -- rows surfaced after the round-1 L8 (S14, S15)

The round-1 L8 compiled the channel at `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba`. Two rows landed after it and before the round-2 issuance: S14 (4.0.0_SA_CRO, 8af890699c) and S15 (2.0.0_SA_COO~G, 229bedf67e). The row gate's L10 limb refuses every new remediation row while any investigation is undispositioned, and those two were the only ones left. They are carried here by this seat, recorded 2026-09-14T20:49:51Z. Their remediation rows travel in round 2's L10 slug. `REMEDIATION_v1.md` lands unchanged per 1.0.0_SA_CTO's RULING T.

```json
[
 {
  "id": "LGIC_NAMING-C-S11",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T20:49:51Z",
  "one_line": "L9 on a row surfaced after the round-1 L8, GRADUATED: the L4-R sign-off record is read from the WORKTREE by all four of its consumers, not only by status -- so LIMB 6, the gate that refuses a new task order against an unsigned PRD, would read an uncommitted signoff file as signed. Owner 1.0.0_SA_CTO (prd_signoff_lib).",
  "class": "OBSERVATION",
  "spec_asserts": "CLAUDE.md Rule 27 L4-R: 'status <CODE> is the one read of what is owed', and each half is signed 'as a file in lane TREE_PRD_SIGNOFF bound to the HASH of its sections' -- a committed file. .tools/prd-signoff.py:174 @ed78c9c6c6: 'the PRD is read at HEAD, never the worktree: the stamp binds to committed bytes'.",
  "world_is": "S14 is confirmed by reading the code at HEAD ee46e71e5b (read, not exercised). prd_signoff_lib.read_signoff_files (:286-300) lists the signoff directory and opens each file by path (:296), so it returns the worktree's bytes. It has four callers, and 4 of 4 pass it a worktree path: prd-signoff.py:86 (status), to-pipeline-gate.py:2204 (LIMB 6), prd-header-notify.py:124 (the L4 notifier, whose docstring at :119 assumes 'post-commit: HEAD is checked out') and prd-stamp.py:339. The stamp reads the PRD at HEAD and refuses a worktree difference (:174-184), but no consumer does the same for the signoff file. The consequence S14 left unmeasured: if a stamp writes SIGNED and then fails its commit, as S14 measured for a REFUSED stamp, LIMB 6 would admit a new task order while HEAD holds no signature. INERT now: 0 uncommitted or untracked files under any org/missions prd/signoff directory at HEAD ee46e71e5b (git status --porcelain --untracked-files=all).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@229bedf67e#LGIC_NAMING-S14",
    ".tools/prd_signoff_lib.py@110378a08c :286-300 read_signoff_files (os.listdir + open by path, :291-297)",
    "git grep -n read_signoff_files HEAD -- .tools at ee46e71e5b: prd-header-notify.py:124, prd-signoff.py:86, prd-stamp.py:339, to-pipeline-gate.py:2204 (4 callers; the 5th hit is the definition)",
    ".tools/to-pipeline-gate.py@da3e61889d :2188-2206 LIMB 6: opens the PRD by absolute path, then read_signoff_files(os.path.join(os.path.dirname(ap), lib.SIGNOFF_DIR))",
    ".tools/prd-header-notify.py@fc71328804 :118-126 _evaluate_prd",
    ".tools/prd-signoff.py@ed78c9c6c6 :174-184 (the PRD's HEAD read and its worktree refusal)",
    "prd_signoff_lib.py was created by 1.0.0_SA_CTO at e7e552f7c4 (LAW v3.15), and its last 3 commits are 1.0.0_SA_CTO's"
   ]
  },
  "adjudicates": [
   "LGIC_NAMING-S14"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_NAMING-C-S12",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T20:49:51Z",
  "one_line": "L9 on a row surfaced after the round-1 L8, GRADUATED for i15 only: NAMING_SCHEMA v1.6 :125 quotes item i15's ruled answer as the example of the rule that decides i15, so a round-2 namer can copy it. i05 is not a leak: the bucket rule :47 produces opal-data-cottonwood in one substitution. FWD-1's round-2 agreement will be graded on 17 items, with i15 reported beside them.",
  "class": "OBSERVATION",
  "spec_asserts": "PRD FWD-1 ACCEPT: two people each write 'the identical name' from the schema. Decomposition s.3a.1: the items are 'described in plain words that never spell a schema token'.",
  "world_is": "This seat's own census is git grep -F of the 18 ruled names in the analysis s.2 table over the two briefing files at HEAD, a different instrument from the filer's. It finds 2 of 18, the same two, and the positive control 'silver-chain' matched in the schema. The two differ in kind. i05: N3_ITEMS says 'The S3 bucket that holds Cottonwood's own data.' The schema's data_bucket 'opal-data-{scope}' (:47) with the FIRM key cottonwood gives the answer directly. The spine names it at :68 only to say it does not exist. So an identical i05 is what the rule predicts either way, and it is not independent evidence against the rule. i15: N3_ITEMS says 'The EC2 instance profile for the Orion runner host that builds Inflection's gold data.' The rule that decides it, system.vendor_through_tiers (:125), gives that scenario's answer, orion-inf-build-gold-profile, as its example. So an identical i15 can be a copy, and it is not evidence that two people derive the name. The issuer's note reads 16 plus 2; this seat's round-2 L9 reads 17 plus i15.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@229bedf67e#LGIC_NAMING-S15",
    "org/standards/NAMING_SCHEMA.json@2706014705 :47 key.data_bucket 'opal-data-{scope}'; :125 system.vendor_through_tiers '(orion-inf-build-gold-profile)'",
    "infra/logic/05_IDENTITY_SPINE.md@a4cc0cb681 :68 cottonwood row, 'buckets today': 'no `opal-data-cottonwood` exists'",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/N3_ITEMS.json@777770e6aa items i05 and i15 (description text quoted above)",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND1_20260914.md@2706014705 s.2 table, rows i05 (S2) and i15 (SY1)",
    "census at HEAD ee46e71e5b: for each of the 18 names, git grep -n -F over the two files -> i05 at infra/logic/05_IDENTITY_SPINE.md:68, i15 at org/standards/NAMING_SCHEMA.json:125, 16 with 0 hits"
   ]
  },
  "adjudicates": [
   "LGIC_NAMING-S15"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 }
]
```
