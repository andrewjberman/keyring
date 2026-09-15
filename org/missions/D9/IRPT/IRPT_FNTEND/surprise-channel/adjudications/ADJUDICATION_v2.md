# IRPT_FNTEND round 2: CVO adjudication

Accumulating CVO review as round-two evidence arrives. This is NOT an L10 slug and no judgment criterion is graded here: round 2 is mid-flight, cells remain non-terminal, and no slug is cuttable on this project.

```json
[
  {
    "id": "IRPT_FNTEND-C-S45",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-12T02:05:00Z",
    "one_line": "DISARMING IRPT_FNTEND-S27, which named this seat its disarm_owner. The contradiction is REAL and the row's own framing UNDERSTATES it: the header's zero is not a count of the wrong field, it is an ABSENT field defaulted to empty and printed as a fact -- the performance wire payload carries no scope block at all, so there is no field on that route for the count to be pointed at.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND-S27 (2.0.0_SA_COO~F, ARMED, disarm_owner 3.0.0_SA_CVO): the served print document reads '0 account(s) in scope' on all four pages while page 3 lists account A-0001 and page 4's bundle scope names accounts A-0001; the row asks this seat for the L9 disposition and states the count 'is reading something other than the accounts the bundle carries'. The PRD's reporting contract: values print exactly as the source supplied them, and an absence renders as an explicit UNAVAILABLE with its reason, never as a silent zero.",
    "world_is": "CONFIRMED, and re-derived on a THIRD instrument -- S27 read the rendered PNG, F16-AC8 greps a console line, and this seat read the SOURCE and the FIXTURE. Three regions of one document have three different sources and nothing binds them: (1) portal/src/pages/InvestorReporting/render/performance/PerformanceDocument.tsx:45 prints `{bundle.scope.accountIds.length} account(s) in scope`; (2) render/performance/AccountDetail.tsx:28 renders 'Accounts in this report' from a separate `accounts` prop, never from bundle.scope.accountIds; (3) page 4's bundle-scope line prints the client-composed bundle scope, which DOES name A-0001. THE DECISIVE READ, and it is what upgrades the row: the fixture the capture was taken against -- C:/tmp/wk-irpt_fntend-2-6-fe-s-16/portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-16-print-narrative.json -- is a route-keyed mock whose performance payload has keys ['dates','lineage','measurement_basis','optional_facts','returns'] and NO scope key; a recursive walk of the whole fixture finds `accountIds` ZERO times. The rendered account row comes from returns.account_detail = [{account_id: 'A-0001', level: 'Account', value: 0.0688}], which matches the PNG's A-0001 / 0.0688 exactly. So bundle.scope.accountIds is absent on the wire, is defaulted to an empty array before render, and [].length prints as the literal 0. THAT IS THE SILENT ZERO THE UNAVAILABLE CONVENTION EXISTS TO PREVENT, in its exact textbook form: an absent value rendering as a measured fact rather than as a stated absence. It also means the remedy is NOT 'point the count at the right field' -- on this route there is no such field to point it at, so a future cut must either carry scope on the wire or render UNAVAILABLE with its reason. NOT ASSERTED: how the count behaves on a server-issued bundle or a multi-account scope; neither was exercised and the denominator here is ONE document, ONE fixture, ONE scope, exactly as S27 stated its own limit.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/render/performance/PerformanceDocument.tsx:45 -- `{bundle.scope.accountIds.length} account(s) in scope` (read at the workspace's portal gitlink, this seat's own read)",
        "portal/src/pages/InvestorReporting/render/performance/AccountDetail.tsx:28 -- 'Accounts in this report' rendered from an `accounts` prop, a different source from the header",
        "portal/src/pages/InvestorReporting/render/analysis/AnalysisDocument.tsx:179 -- the analysis document prints report.scope.accountIds.join(', '), a THIRD accounts source in the same render tree",
        "C:/tmp/wk-irpt_fntend-2-6-fe-s-16/portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-16-print-narrative.json -- performance payload data keys ['dates','lineage','measurement_basis','optional_facts','returns']; no scope key; recursive walk finds accountIds 0 times; returns.account_detail carries exactly one entry, account_id A-0001, value 0.0688",
        "IRPT_FNTEND-S27 @ the round-2 channel -- the originating row, its PNG pin 8094204b4eb99c77108b270dc530cdf2079a3f018d75ab214a2d0cbb696e100f and its stated denominator of 1",
        "NEGATIVE-CONTROL NOTE on the fixture read: the first open failed FileNotFoundError on the MSYS path /c/tmp/... under native Windows Python and succeeded on C:/tmp/... -- the absence was a path artefact and was resolved rather than reported as an absent fixture"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "DISARM DISCHARGED. S27's ARMED standing was waiting on this seat's judgment and nothing else; that judgment is recorded here, so the hazard is held rather than open. No repair is taken: the remediation lands in a cell nobody has been granted, this round's decomposition is FROZEN, and it is not a COO act -- exactly as S27 itself states. CARRIED TO L10, two items and they are separate: (1) the silent-zero defect above, with the remedy constrained by the fact that the wire carries no scope on this route; (2) S27's own observation that IRPT_FNTEND-W2-S13's recorded CAUSE is falsified -- W2-S13 attributed the zero to 'a client-composed bundle names no account set', and the page-4 bundle scope DOES name A-0001. ⭐ THE SECOND ITEM IS THE ONE THAT COSTS MONEY IF IT IS LOST: a wrong CAUSE sitting in the channel sends the next round's cut at the wrong surface, and it would have sent it at the bundle composer rather than at the wire contract. A correction row citing W2-S13 belongs in the next round's channel; this seat does not mutate W2-S13 in place, because corrections are NEW rows citing the old id. NO GRADE IS ASSERTED: F16-AC8 PASSES correctly on its own bar -- the resolver did resolve -- and nothing here touches it."
  },
  {
    "id": "IRPT_FNTEND-C-S46",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-12T03:25:00Z",
    "one_line": "CROSS-PROJECT CONVERGENCE, visible only from L8 because no issuer reads both channels: IRPT_FNTEND-S30 and IRPT_BCKEND-W4-S19 were caught by THE SAME INSTRUMENT -- hash the outputs and require them to DIFFER -- and both projects independently recommend it as a standing rule. That is three instances in one round of per-member checks passing while the property that failed lived between the members.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "S30's own recommendation: 'a standing rule that a capture set asserts DISTINCT HASHES whenever its fixtures differ'. IRPT_BCKEND-W4-S19's forward remedy, endorsed by this seat at IRPT_BCKEND-C-S84: 'IB-rtb-1's replay should compare TWO renders of DIFFERENT bundles to each other and require the content hashes to DIFFER, which is the arm nobody has run'.",
    "world_is": "TWO PROJECTS, TWO ISSUERS, TWO ARTIFACT KINDS, ONE MISSING CONTROL, ARRIVED AT INDEPENDENTLY WITHIN HOURS. IRPT_BCKEND-W4-S19: three DISTINCT bundles produced ONE normalized content hash and an identical 71,944-byte content stream; every per-object arm passed because each PDF was compared only to ITSELF. IRPT_FNTEND-S30: every network-sourced response reaches the tab bodies as UNCERTAIN (contracts/envelope.ts parses `state: status?.state ?? 'READY'`, api/endpoints/investor-reporting.ts:932 returns parsed.data and DISCARDS it, adapt.ts refills from `parts.state ?? EXPLICIT_UNKNOWN_STATE` = 'UNCERTAIN', TabShell.tsx:133/:150 gate both bodies on it) -- and every per-tab test passed because EACH SEEDS THE STATE IT SHOULD HAVE FETCHED. In both cases the per-member checks were individually sound and the failing property lived BETWEEN members, where no per-member arm can reach. In both cases the instrument that fired was the same: hash the outputs, require them to DIFFER. S30 records that it cost nothing and nobody asked for it, and that the eye would have read three plausible PNGs. \u26d4 AND IT IS A DIFFERENCE CONTROL, NOT A POSITIVE CONTROL -- the distinction is the whole reason it works. A positive control proves the instrument can fire and bounds UNDER-firing only; both rounds HAD positive controls and both passed every time. Only a difference control shows the output CHANGES when the input changes. THE THIRD INSTANCE, same round, different coordinate: IRPT_BCKEND-S40 -- round 1's three certification legs returned GREEN over 27 wrong dates because a date sits at none of the coordinates those legs inspect. A CONSUMER-SIDE SIBLING WORTH NAMING BESIDE THEM, because it is the same failure wearing different clothes: IRPT_FNTEND-S27, dispositioned by this seat at C-S45, is an ABSENT field defaulted to a confident value ([] rendering as '0 account(s) in scope'), and S30's `?? 'READY'` then `?? 'UNCERTAIN'` is an absent STATE defaulted to a confident value. Defaulting an absent state is the worse of the two: it asserts an answer exists. \u26a0 AND IT REACHES THE CONTRACT THIS SEAT SIGNED TONIGHT: IRPT_BCKEND v0.14 makes `state` load-bearing (business_date REQUIRED on the five answer-bearing states, absent on the four no-answer ones), while S30 measures that the consumer DISCARDS state at the endpoint. The contract is sound and the consumer does not honour it. That does NOT retro-falsify the L4-R half signed at 4ff7d52709c9 -- that half is about PRD TEXT agreement, not implementation, and the FNTEND PRD's CONTRACTS row makes no field-level promise -- but it is exactly the seam a later reader would assume was covered by a signed contract, and it is not.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md -- row IRPT_FNTEND-S30 (2.0.0_SA_COO~F, BLOCKING/ARMED, owner 1.0.0_SA_CTO), read in full including its world_is",
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md -- rows IRPT_BCKEND-W4-S19 and IRPT_BCKEND-S40",
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md -- this seat's IRPT_BCKEND-C-S84 (the difference-control endorsement) and IRPT_BCKEND-C-S83",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md -- this seat's IRPT_FNTEND-C-S45 (the absent-field-defaulted-to-a-confident-value disposition on S27)",
        "org/missions/D9/IRPT/IRPT_BCKEND/prd/signoff/3.0.0_SA_CVO.json -- the v0.14 ratified-text half at half_hash 4ff7d52709c9, cited for what it does and does NOT cover"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "WHY THIS ROW EXISTS AND WHY NO ISSUER COULD HAVE WRITTEN IT: 2.0.0_SA_COO~B reads IRPT_BCKEND's channel and 2.0.0_SA_COO~F reads IRPT_FNTEND's. Each named its own instance and each proposed the control for its own project. The CONVERGENCE -- two independent arrivals at one control within hours -- is visible only to the seat that reads both channels, which is what spine v3's L8 is for. \u2b50 ONE INSTANCE IS A DEFECT; TWO INDEPENDENT ARRIVALS AT THE SAME REMEDY ARE EVIDENCE THE CONTROL IS MISSING FROM THE CUT ITSELF, not from two cells. CARRIED TO L10 AS A RECOMMENDATION TO 1.0.0_SA_CTO, not as a ruling and not as a gate: a DIFFERENCE-CONTROL clause for criteria whose evidence is a rendered or captured artifact -- where fixtures differ, the outputs must be asserted to DIFFER. Its cost is one hash comparison per capture set, which S30 measured at nothing. NON-APPLICATION: a criterion with a single fixture (nothing to differ from), and any criterion whose claim IS constancy. NO ACT IS TAKEN and NO CELL IS AUTHORED: S30's remedy is a ROUND-3 cell by its own issuer's ruling, the decomposition is FROZEN, and this seat neither cuts cells nor widens grants."
  },
  {
    "id": "IRPT_FNTEND-C-S47",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-12T07:45:00Z",
    "one_line": "DISARMING IRPT_FNTEND-S37, which named this seat. NOTHING IS FALSIFIED RETROACTIVELY -- 0 CVO grades exist on F12-* or F18-* across all 46 FNTEND adjudication rows -- so this sets the RULE for the round-2 L9 grade. AND THE TWO DIVERGENCES ARE NOT THE SAME DEFECT: one weakens the BAR, the other breaks REPRODUCIBILITY, and they take different verdicts.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "S37 routes to this seat: 'the two divergences are facts about round 2's RECORD, which is the CVO's to adjudicate at L9, and neither instance may be edited to make them go away.' The proof-of-spec schema calls the recorded invocation RE-RUNNABLE BY A VERIFIER.",
    "world_is": "PROSPECTIVE, NOT CORRECTIVE. Measured before disposing: all 46 rows of this project's adjudication documents scanned for a criterion matching ^F(12|18)- ; ZERO CVO grades exist. Round 2's L9 has not run and no slug is cut, so no grade of this seat's inherits either divergence and nothing is reopened. What follows is the rule the round-2 grade will be held to. \u26d4 THE TWO ARE DIFFERENT DEFECTS AND ONE REMEDY DOES NOT MOVE BOTH. (1) F18-AC17 recorded `timeout 180` against a criterion that says `timeout 120`: this WEAKENS THE BAR. A run needing more than 120s fails the ORDERED criterion and passes the RECORDED one, so the instance cannot establish the criterion as written -- it establishes a weaker one. RULE: F18-AC17 is NOT gradeable PASS on this instance. The ordered bar was never exercised, so the honest verdict is NOT-EVALUATED unless the cell fails on its own merits first, which here it does -- FE-s-18 is already ruled non-terminal at S30 and F18-AC17 is a TRUE failure. The divergence therefore changes no outcome THIS round and would have changed one silently in any round where the arm passed. (2) F12-AC5 recorded its command with the CLOSING DOUBLE QUOTE DROPPED: this breaks REPRODUCIBILITY, not the bar. The run happened and its output stands; what is malformed is the RECORD of how to repeat it, in the exact field the schema calls re-runnable by a verifier. An unbalanced shell string is not re-runnable by anyone. RULE: F12-AC5 may be graded on its output, and the grade MUST state that its recorded invocation is not re-runnable as written, so that no later verifier claims reproduction from it and no reader treats the field as exercised evidence. \u2b50 THE DISTINCTION IS THE POINT: a bar divergence corrupts WHAT WAS PROVED; a record divergence corrupts WHO CAN CHECK IT LATER. Collapsing them into one 'divergence' verdict would either reopen a sound result or certify an unverifiable one.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md -- rows IRPT_FNTEND-S37 (2.0.0_SA_COO~F, ARMED, disarm_owner 3.0.0_SA_CVO), W3-S13 and W3-S14",
        "DENOMINATOR for the no-existing-grade finding: all 46 rows across org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/*.md scanned for ^F(12|18)- ; 0 matches",
        "IRPT_FNTEND-S30 -- FE-s-18 ruled non-terminal in round 2, which is why F18-AC17's divergence changes no outcome this round",
        "W3-S14's estate-wide read, cited as scope and NOT re-derived here: 294 committed instances, 874 comparable rows, 318 divergent"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "DISARM DISCHARGED: S37's ARMED standing was waiting on this seat's L9 rule and nothing else. NO INSTANCE IS EDITED -- S37 is explicit that neither may be, and corrections are new rows citing the old id. CARRIED TO L10, two items. (1) The estate-wide 318 of 874 is a SEPARATE question from these two and is not adjudicated here; the ANNOUNCE frame surfaces it without refusing, which is what an un-enforced count is for. (2) \u2b50 THE ISSUER-PREMISE CLASS, and this project has now produced FOUR instances: S37 (a cell's face asserted round 2's instances were aligned -- 5 of 7), S36 (two issuer mis-measurements in the round-3 cut, one of them an rc read through `| head` so the PIPELINE's status was scored instead of the command's), S32 (a criterion patched through a message), and S33 (a producer landing 14 minutes into a live worker's run after the obvious mitigation was applied). S37 states the shape better than this seat would: A CELL'S STATED PREMISE IS AN ISSUER'S CLAIM, NOT A FACT, AND THE ONLY PARTY POSITIONED TO FALSIFY IT IS THE WORKER THE CLAIM IS HANDED TO. Four instances is a statement about how faces are WRITTEN, not about four issuers' care, and it belongs in the round analysis."
  },
  {
    "id": "IRPT_FNTEND-C-S48",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-12T08:05:00Z",
    "one_line": "THE FOURTH PRODUCER MOVE WAS THE REMEDY TO THIS SEAT'S OWN FINDING, and S39 measures that it changed NOTHING the consumer consumes. Recording it because the cost landed on another project and a later reader would otherwise read S33 as carelessness -- and because it makes the byte-pin argument STRONGER, not weaker.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND-S39: 58e387b454 'changed EXACTLY TWO THINGS in the schema: the source_pin provenance string (62301f71e0 -> b8e98d5a4d) and an added source_pin_note explaining it. NO FIELD. NO TYPE. NO REQUIRED SET. NO ROUTE. NOTHING THE CONSUMER CONSUMES.' IRPT_FNTEND-S33 counts that same commit as the FOURTH producer move of the round, landing 14 minutes after FE-s-18's worktree was cut and while its worker ran.",
    "world_is": "THE PROVENANCE THAT COMMIT FIXED IS THE DEFECT THIS SEAT RAISED. In the v0.14 L4-R ratified-text review (org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_L4R_V014_RATIFIED_TEXT_REVIEW_20260912.md@341e576e6a) this seat found docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json declaring x-contract.source_pin 62301f71e0 -- v0.4 -- while the business_date rule it encodes exists only at v0.14 (grep -c returned 0 at the declared pin and 1 at b8e98d5a4d, with the positive control firing). The remedy named there was to regenerate with a pin that carries the row. That regeneration IS 58e387b454. SO THE COST IS TRACEABLE TO THIS SEAT'S FINDING AND IS STATED HERE RATHER THAN LEFT FOR SOMEONE ELSE TO DISCOVER: a correct finding on IRPT_BCKEND produced a producer move that reddened IRPT_FNTEND's consumer suite, cost round 2 a re-pin, and generated rows S28, S33 and S35. \u26d4 AND IT DOES NOT SOFTEN THE BYTE-PIN CONCLUSION -- IT HARDENS IT. S39's measurement is that the commit changed only a provenance STRING and a note; re-rendering the whole contract through the folder's own generator moved one line. If a consumer suite goes red on a change that touches no field, no type, no required set and no route, THE CONSUMER IS PINNED TO THE WRONG THING. A byte pin asserts 'these exact bytes', which is a claim no consumer needs and every metadata edit falsifies; a content pin asserts what the consumer actually consumes. FE-s-14's R1 item 7 had already content-bound the portal side, which is why that half passed. THE REMAINING BYTE PIN IS THE PRODUCER-SIDE TEST infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py (S40, measured 2 failed / 51 deselected), and it is IRPT_BCKEND's surface, outside every round-3 portal grant. \u2b50 THE GENERAL SHAPE, and it is why this is worth a row rather than a note: A FINDING'S REMEDY HAS A BLAST RADIUS TOO, AND IT LANDS WHERE THE FINDER IS NOT LOOKING. This seat raised a provenance defect on one project and did not ask what pinned that artifact elsewhere. The never-widen rule already says a sign-off names an act's blast radius; the same discipline belongs on a REMEDIATION, and this seat did not apply it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md -- rows S39 (the two-things measurement), S33 (the fourth producer move), S40 (the producer-side byte pin, 2 failed / 51 deselected), S28 and S35",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_L4R_V014_RATIFIED_TEXT_REVIEW_20260912.md@341e576e6a -- this seat's own finding naming source_pin 62301f71e0 and the regenerate-with-a-carrying-pin remedy",
        "docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json -- the artifact, x-contract.source_pin before and after",
        "NOT RE-DERIVED HERE: S39's two-things diff and S40's pytest counts are the issuer's and the worker's measurements, cited as theirs"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "NO GRADE IS ASSERTED and no act is taken. This row neither reopens the v0.14 half (signed at half_hash 4ff7d52709c9 and unaffected -- the PRD text did not move) nor disputes S33's count: the commit IS a fourth producer move landing under a live consumer cell, and being a remedy does not exempt it. CARRIED TO L10, two items. (1) The byte-pin-vs-content-pin question, with S39's measurement as the evidence and S40's producer-side test as the concrete remaining instance -- owner 1.0.0_SA_CTO, since that file is IRPT_BCKEND's surface and no portal grant reaches it. (2) THIS SEAT'S OWN OMISSION: a remediation's blast radius was not asked for. When this seat names a remedy on a shared artifact, the question 'what else pins this' belongs in the finding, and it was not there. That is a correction to how this seat writes findings, not to the finding itself, which stands."
  },
  {
    "id": "IRPT_FNTEND-C-S49",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-12T09:10:00Z",
    "one_line": "FIX THE INSTANCE, LEAVE THE CLASS -- now FOUR instances across TWO seats in one night, and one of them is this seat's own at C-S48. The issuer's S45 adds the clause that makes it a finding rather than a lapse: it happened AFTER the lesson had already been written down.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CLAUDE.md Rule 24: hunt the uncovered member BY SUBTRACTION from a printed denominator, never by a forward list of what you thought of. CLAUDE.md never-widen: a sign-off names the ACT'S BLAST RADIUS. Both govern the scope of a REMEDY, not only the scope of a claim.",
    "world_is": "FOUR MEASURED INSTANCES, ONE NIGHT. (1) IRPT_FNTEND-S45: S41 corrected F19-AC8's predicted `0 fail` bar; THREE faces carried the identical bar (F19-AC8, F21-AC7, F22-AC8); one was amended, so FE-s-22 hit the same wall and refused correctly and FE-s-21 RAN on the defective bar while the fix was reported done. (2) and (3): S45 states this was its THIRD time that night, the earlier two being its own. (4) THIS SEAT, recorded at IRPT_FNTEND-C-S48: the v0.14 L4-R review named a remedy for one artifact's stale source_pin and never asked what ELSE pinned that artifact; the regeneration reddened another project's consumer suite. \u2b50 WHAT MAKES IT A FINDING RATHER THAN FOUR LAPSES IS S45'S OWN CLAUSE -- 'and this time I had already written the lesson down'. Knowing the rule did not produce the behaviour, which means the gap is not awareness and cannot be closed by restating the rule. THE STRUCTURAL READING: a correction is authored AT the instance that surfaced it, and the instance is the only thing in view at that moment. The population question -- what else carries this exact bar, what else pins this artifact, what else reads this field -- is a SECOND act that nothing in the flow prompts. Rule 24 already requires enumerating by subtraction from a printed denominator when making a CLAIM; nothing applies the same discipline when making a FIX. NOT ASSERTED: that any of the four caused harm that was not caught. All four were caught -- three by workers refusing correctly, one by another project's suite going red -- which is evidence the surrounding controls work and NOT evidence the class is harmless: in each case the catch was downstream of an act already taken.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md -- row S45 (the three-faces instance and the 'third time tonight' clause), and S41 (the single correction it refers to)",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md -- IRPT_FNTEND-C-S48, this seat's own instance, filed before S45 was read",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_L4R_V014_RATIFIED_TEXT_REVIEW_20260912.md@341e576e6a -- the finding whose remedy had the unasked blast radius",
        "NOT RE-DERIVED: S45's count of its own earlier two instances is the issuer's statement about its own turns, cited as theirs"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "CARRIED TO L10 AS A RECOMMENDATION TO 1.0.0_SA_CTO, not a ruling and not a gate, and explicitly NOT a criticism of the issuer -- three of the four instances are self-reported by the seat that made them, which is why the class is visible at all. THE SHAPE OF THE RECOMMENDATION: when a correction is made to a CRITERION, a FACE or a shared ARTIFACT, the corrective act names the POPULATION it searched and the denominator it searched over -- the same discipline Rule 24 already requires of a claim, applied to a fix. COST: one census per correction, over a population the corrector already has in hand (the round's faces; the artifact's consumers). NON-APPLICATION: a correction to a single-instance object with no siblings by construction, and any correction where the population IS the instance. \u26d4 AND THE COUNTER-ARGUMENT BELONGS IN THE RECORD: this would add friction to the fastest and most valuable act in the loop, which is a seat correcting itself mid-round. If it makes self-correction slower it will produce FEWER corrections, and four self-caught instances in one night is a system working. The CTO weighs that; this seat only supplies the count and the shape. ALSO NOTED, refining C-S46: S46 corrects S44 and measures that the three Holdings fixtures DO vary (basis across observed/target, classification across observed/missing-attribution) so the collision arm refuses all three pairs on its own -- the corpus problem is the STATUS dimension specifically (3 of 84 envelopes carry status), not undifferentiated fixtures."
  },
  {
    "id": "IRPT_FNTEND-C-S50",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-12T10:30:00Z",
    "one_line": "THE v0.14 CONTRACT THIS SEAT SIGNED IS SOUND AND ITS SEMANTICS DO NOT SURVIVE THE CONSUMER BOUNDARY -- FOUR independent measurements, four different mechanisms, all landed within hours of the amendment. The signature is not falsified; what is falsified is any reading that a signed contract means the behaviour it describes exists.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_BCKEND v0.14 CONTRACTS row StatusEnvelope, signed by this seat at half_hash 4ff7d52709c9: source_dates STAYS REQUIRED; business_date REQUIRED on the five ANSWER-BEARING states and MAY BE ABSENT -- NEVER NULL -- on the four NO-ANSWER states. The spine's ratified-text half covers PRD TEXT and the counterpart agreement, not implementation.",
    "world_is": "FOUR MEASURED CONSEQUENCES ON THE CONSUMER PLANE, none of them a defect in the contract. (1) W1-S26: gen-wire.ts tests `allOf` BEFORE type/properties, so regenerating StatusEnvelope at b8e98d5a4d emitted the literal `export interface StatusEnvelopeWire unknown` and dropped all seven properties -- the conditional the amendment introduced is the thing the generator cannot render. (2) W1-S41: the amendment's subtraction (9 states MINUS the 5 answer-bearing = 4) is taken over the PRODUCER's enum, and the view's closed EnvelopeState is a DIFFERENT nine -- it carries LOADING and RETRYABLE where the wire carries QUEUED and RUNNING, so 9-minus-5 over the VIEW yields {LOADING, UNAVAILABLE, RETRYABLE, FAILED}, not the four the contract names. The ordered subtraction is only expressible on one of the two planes. (3) W1-S42: the clause governs `business_date` and the age surface computes from `source_dates.as_of` -- a different wire member with a different nullability -- so a READY envelope carrying the contract-REQUIRED business_date and no as_of renders 'Source time unknown'. The panel reports a missing source date while the source date the contract requires is present. (4) W1-S43: adaptStatusEnvelope carries the source dates through `?? null`, so an ABSENT business_date and an explicit null arrive at the view as the SAME value -- the ABSENT-NEVER-NULL distinction, which is the amendment's core and was chosen deliberately over a nullable field, is destroyed before any panel sees it. \u26d4 THE SIGNATURE IS NOT FALSIFIED AND THIS SEAT IS NOT REOPENING IT. The ratified-text half covers the PRD's ENDPOINT and CONTRACTS sections and the counterpart agreement; IRPT_FNTEND's CONTRACTS row makes no field-level promise, which was measured at signing over a printed denominator (212 lines, 7 hits, each dispositioned). All four consequences are implementation, and implementation is outside the half by the spine's own definition. \u2b50 WHAT IS FALSIFIED IS AN INFERENCE A LATER READER WOULD MAKE: that an ADMITTED PRD with both halves SIGNED means the behaviour the CONTRACTS row describes is the behaviour the estate exhibits. It does not, and tonight it did not within hours of the signature, by four mechanisms none of which any L4-R review is scoped to see.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md -- rows W1-S26, W1-S41, W1-S42, W1-S43, each read in full; all four are 0.9.0_WK_IRPT_FNTEND~1's measurements, cited as theirs and not re-derived here",
        "org/missions/D9/IRPT/IRPT_BCKEND/prd/signoff/3.0.0_SA_CVO.json -- the signed half, prd_version v0.14, prd_pin b8e98d5a4d, half_hash 4ff7d52709c9a39a, cross-checked against the L4-R notifier's declared 4ff7d52709c9",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_L4R_V014_RATIFIED_TEXT_REVIEW_20260912.md@341e576e6a -- the review, including its stated scope limit that it certifies no implementation",
        "org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:164-167 -- the ratified-text half's four clauses, none of which reaches a consumer implementation"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "NO GRADE IS ASSERTED, NO HALF IS REOPENED, AND NO CELL IS AUTHORED. Three of the four already have owners (W1-S41, W1-S42, W1-S43 -> 1.0.0_SA_CTO; W1-S26 is drain-owned) and this row neither re-routes nor duplicates them; it states what they are TOGETHER, which no single row claims and no issuer reading one channel can see. CARRIED TO L10 AS ONE ITEM FOR 1.0.0_SA_CTO: the consumer plane does not honour StatusEnvelope v0.14 in four independent ways, so any round-3 or round-4 cut that treats the signed contract as a description of live behaviour is building on a premise four measurements contradict. \u2b50 AND THE GENERAL POINT, which is this seat's to make because this seat signs these halves: AN L4-R SIGNATURE IS A CLAIM ABOUT TEXT AND IS ROUTINELY READ AS A CLAIM ABOUT BEHAVIOUR. The spine scopes the half correctly and the scope is invisible at the point of USE -- a reader sees ADMITTED and infers the contract holds. That gap is not closed by signing more carefully; it is closed either by a consumer-conformance criterion somewhere in the loop or by the slug saying plainly, every time, what a signature did NOT cover. This seat will say it in the slug; whether the loop should carry a mechanism is the CTO's."
  }  ,
  {
    "id": "IRPT_FNTEND-C-S51",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T06:41:09Z",
    "one_line": "W2-S21's NAMED DISARM OWNER CANNOT DISARM IT BY GRADING, AND SAYS SO RATHER THAN RECORDING A DISARM IT CANNOT DELIVER. The mechanism is confirmed on this seat's own read: HoldingsTab.tsx:90 mounts the body only on READY, so with three distinct states two of the three Holdings captures are StatusPanels that draw neither basis nor classification. But no criterion that reaches the CVO asks whether a capture renders the field its claim declares: F18-AC10 and F18-AC11 are mechanical (CLICKED: Holdings), and F18-AC18 -- the only judgment row -- charters layout, screen/preview/print agreement and product coherence, RECORD with NO VERDICT. Grading the rendered field at L9 would be grading a bar nobody ordered. Re-routed to the issuer. What this seat WILL do at L9 is RECORD, inside F18-AC18's charter, which Holdings PNG is a panel and which a drill tree.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F as issuer -- it can amend FE-s-18's criteria mid-round, as it widened FE-s-26's grant at bf95fb7b9a -- with 1.0.0_SA_CTO at L10 for the spec question. DISARMS on ANY ONE of: (a) FE-s-18 gains a judgment criterion, or F18-AC18 is amended, asking whether each Holdings capture renders the field its claim declares; (b) FE-s-22's claims model (__tests__/fe-s-22/round-2-holdings.claims.json) stops declaring basis and classification for the two captures a READY-only mount cannot draw them in; (c) the CTO rules at L10 that a StatusPanel carrying the reason code IS a legitimate capture of an unavailability basis, and the claims model is corrected to say so. NOT disarmed by this row: the L9 record below closes the L9 path only, not FE-s-22's rule if it is ever pointed at the round-4 captures.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx:90-91, read by this seat: `if (!snapshot || envelope.state !== 'READY') { return <StatusPanel tabId=\"holdings\" envelope={envelope} /> }` -- an independent instrument confirming W2-S21's source claim, not a re-run of the worker's test",
        "TO-FE-s-18 F18-AC10 and F18-AC11: invocation `node scripts/ui-smoke.mjs investor-reporting ... --click Holdings`, expect `CLICKED: Holdings` -- MECHANICAL, satisfied whether the capture draws a panel or a drill tree",
        "TO-FE-s-18 F18-AC18: `<criterion id=\"F18-AC18\" cell_refs=\"FE-s-18\" judgment=\"true\"/>` -- 'graded at L9 from the manifest's PNGs: nothing clips or overlaps at 390; screen, preview and print of the frozen report agree figure for figure; the screens and the export read as one Opal product. RECORD; NO VERDICT.'",
        "TO-FE-s-18, full text: 0 matches for capture-hash|gradeCaptureSet|DISTINCT|fe-s-22 -- no FE-s-18 criterion runs FE-s-22's hash rule over the round-4 captures, so the false DISTINCT-AS-ASSERTED verdict W2-S21 forecasts has no wired trigger in this round",
        "TO-FE-s-18 <status>pending</status> at this read",
        "IRPT_FNTEND-W2-S21 (0.9.0_WK_IRPT_FNTEND~2, 2026-09-13T04:03:23Z): the claims model declares each of the three captures renders basis and classification; F26-AC3 requires three DIFFERENT states"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "W2-S21 names 3.0.0_SA_CVO as disarm owner and places the question 'whether a panel is a legitimate capture for target-blend basis and for a node whose attribution is unavailable' at F18's criteria and the L9 grade. CLAUDE.md: an ARMED hazard disarms same-turn via its disarm_owner; the CVO grades JUDGMENT criteria at L9, and a relayed scope is never adjudicated wider.",
    "world_is": "The obvious disarm -- this seat committing to grade the rendered field at L9 -- closes the hazard only if a criterion that reaches this seat asks that question, and none does. So the named owner is the wrong owner for the disarm, and the honest act is to say so and route it rather than record a disarm that leaves the path open. What the grading commitment CAN still cover is narrower and real: F18-AC18 is RECORD with NO VERDICT, recording what each PNG shows is inside that charter, and so the L9 record will name which Holdings captures are StatusPanels. That closes the L9 path to a silent pass. It does not close FE-s-22's rule if it is ever pointed at these captures, because that rule compares hashes and three different panels/trees hash differently whether or not any of them drew the claimed field.",
    "notes": "NOT CLAIMED: that a StatusPanel is the wrong capture. For an unavailability basis (target blend model revision unnamed; node attribution unavailable) the panel with its reason code may be exactly the honest rendering, since there is no basis content to draw. The defect W2-S21 found is the MISMATCH between that and FE-s-22's claims model, which says the capture renders basis and classification. Which side moves is a spec decision, not a verification one. ADJACENT, CARRIED TO ROUND-4 L9, NOT A FINDING: TO-FE-s-26 was flipped complete at 2026-09-13T05:07:02Z (81b45120e7) while its exact-vs-suffix control read its two halves from two different maps, which the worker's own W2-S22 had described at 05:00Z; the issuer corrected the bound at 05:18:48Z (49f4026218) and the control was repaired at 05:33:25Z (portal 346d2b90), which the proof row now cites. The end state is sound and the history is in the proof row. The grant question W2-S20 raised is CLEAN: the one fe-s-22 file joined the grant at 04:31:36Z (bf95fb7b9a), before its first edit at 04:58:07Z (portal f95fa1db)."
  }  ,
  {
    "id": "IRPT_FNTEND-C-S52",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:12:22Z",
    "one_line": "ROUND-4 L9, DISMISSED: the two pause rows. The ~16:1xZ STOP they record was LIFTED by Andrew's word, by name, for both IRPT projects, at ~01:3xZ 2026-09-13 (card 1 of nine).",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-S49",
      "IRPT_FNTEND-S50"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "S49 records Andrew's STOP verbatim; S50 records his ~16:2xZ clarification moving its criterion to projects.",
    "world_is": "The pause is lifted. Record committed at c6be748be7 and read by this seat at HEAD before citing it.",
    "hazard_standing": "INERT",
    "dismissal_reason": "Superseded by the lift: org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260913_013xZ_NINE_CALLS_RULED_PAUSE_LIFTED_D10-2_DEMO_KEPT.md @c6be748be7, card 1, 'BOTH IRPT projects. THE PAUSE IS LIFTED, by his word, by name.' Neither hazard has a live path once the stop is lifted.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "c6be748be7 -- the lift record, committed, card 1"
      ]
    }
  },
  {
    "id": "IRPT_FNTEND-C-S53",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:12:22Z",
    "one_line": "ROUND-4 L9, DISMISSED: the two canon-census rows. S51's zero was withdrawn by S52, and S52's correction was absorbed into the D14 contradiction report v0.2, which is its carrier; nothing is owed on IRPT_FNTEND itself.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-S51",
      "IRPT_FNTEND-S52"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "S51: the ratified canon cards do not contradict round 4 on the plane they govern. S52: that 0 of 14 is 4 in 3 of 14.",
    "world_is": "4.0.0_SA_CRO~D regraded IRPT_FNTEND to v0.2 at 5288666762 -- four storage surfaces, grade DERIVED from IRPT_BCKEND's rows. This seat re-read the four declarations itself in the portal wire contracts.",
    "hazard_standing": "INERT",
    "dismissal_reason": "Carried elsewhere, correctly: infra/logic/03_CONTRADICTION_REPORTS/IRPT_FNTEND.md v0.2 @5288666762 holds the finding and its grade. A FNTEND remediation would duplicate a D14 carrier. The storage question is IRPT_BCKEND's publisher, not this project's.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "5288666762 -- the D14 contradiction report v0.2 for IRPT_FNTEND"
      ]
    }
  },
  {
    "id": "IRPT_FNTEND-C-S54",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:12:22Z",
    "one_line": "ROUND-4 L9, DISMISSED: five rows resolved INSIDE the round by an issuer act this seat verified -- two grant widenings, one re-cut, one bound correction, one widening with a re-run read by hand here.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-W2-S20",
      "IRPT_FNTEND-W1-S49",
      "IRPT_FNTEND-W4-S5",
      "IRPT_FNTEND-W2-S22",
      "IRPT_FNTEND-W1-S54"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each row refused a criterion that could not pass as cut; each named the issuer as the owner of the repair.",
    "world_is": "W2-S20: the fe-s-22 file joined FE-s-26's grant at bf95fb7b9a (04:31:36Z), before its first edit (portal f95fa1db, 04:58:07Z) -- measured, no out-of-grant write. W1-S49: widened with a ruling at 913706a898. W4-S5: F28-AC6's bar re-cut at 9ab6043728, re-run PASS. W2-S22: the control pair corrected at 49f4026218 and repaired at portal 346d2b90, which F26-AC8's proof row cites. W1-S54: widened at 6177717ce0 with portal dd77d19f; F18-AC17 re-run reads '486 pass | 1 skip | 0 fail', ONE summary line, read by this seat.",
    "hazard_standing": "INERT",
    "dismissal_reason": "Each repaired by its named issuer and verified at the cited commit. Their PATTERN is not dismissed: five criteria cut against an assumption is graduated separately as S55 (C-S58).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bf95fb7b9a (04:31:36Z) precedes portal f95fa1db (04:58:07Z) -- git log --date=iso-strict, both repos",
        "913706a898, 9ab6043728, 49f4026218, 6177717ce0 resolve; portal 346d2b90 and dd77d19f resolve",
        "TO-FE-s-18 proof instance F18-AC17 output_evidence: one summary-shaped line, 486 pass / 1 skip / 0 fail"
      ]
    }
  },
  {
    "id": "IRPT_FNTEND-C-S55",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:12:22Z",
    "one_line": "ROUND-4 L9, DISMISSED: five instrument findings resolved or disarmed within the round, S54 being itself the disarm record for W3-S17.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-W3-S17",
      "IRPT_FNTEND-S54",
      "IRPT_FNTEND-W3-S18",
      "IRPT_FNTEND-W4-S6",
      "IRPT_FNTEND-W1-S50"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "W3-S17 falsified a worker-face premise about closed loopback ports; W3-S18 found bun's spawnSync ignores a mutated process.env; W4-S6 found 0 of 2554 is 2 of 2559; W1-S50 is a worker's own pass-1 defect.",
    "world_is": "W3-S17 disarmed by its named owner in S54 (0 of 746 files probe the IPv4 literal); by S54's own account the false premise came from the issuer's spawn prompt, carried from a memory entry that has since been corrected (its own modified stamp: 2026-09-13T04:10Z). W3-S18's remedy is in-tree. W4-S6's re-measured counts ship inside the gate's own PLACEHOLDERS_BOUNDARY constant at d0c28a59be. W1-S50 fixed in pass 2 (portal fbc5699c): its panel arms are re-measured on the tab path the page renders.",
    "hazard_standing": "INERT",
    "dismissal_reason": "Resolved or disarmed, each with its evidence named. W3-S17's second half -- vite binds localhost as ::1 only -- stays true and is carried in S54 and in FE-s-27's own probe comments, not by an open row.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "IRPT_FNTEND-S54 -- the disarm, with its 0-of-746 denominator",
        "d0c28a59be:.tools/to-pipeline-gate.py PLACEHOLDERS_BOUNDARY -- '2559 task-order files tracked, 305 tree, 2 carrying'",
        "portal fbc5699c -- FE-s-25 pass 2"
      ]
    }
  },
  {
    "id": "IRPT_FNTEND-C-S56",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:12:22Z",
    "one_line": "ROUND-4 L9, GRADUATED to 1.0.0_SA_CTO: two live CHECKER defects. The <placeholders> reader false-admits (S53, widening W4-S7), and every `0 fail` bar is graded by an unanchored search (S56, latent).",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-S53",
      "IRPT_FNTEND-W4-S7",
      "IRPT_FNTEND-S56"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "proof-of-spec-check.py grades invocation alignment from the declared <placeholders> set and grades a count bar with re.search over the whole evidence.",
    "world_is": "PLACEHOLDERS_TAG_RE `<placeholders>(.*?)</placeholders>` is unanchored, so a prose mention before the real element swallows the text between them (W4-S7: 367 names instead of 1); the gate mirrors it byte-identically BY DESIGN, so fixing one reader alone would re-open the gap the mirror closes. S56: latent, 0 false PASS across 875 rows (1.0.0_SA_CTO 96371). This seat read F18-AC16 and F18-AC17's deciding evidence by hand: one summary line each, so neither is a realization.",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO as owner of the checker limbs, with 2.0.0_SA_COO~F for W4-S7's issuance side. DISARMS when the placeholders reader is line-anchored in BOTH readers in one change, and when the count bar refuses a PASS beside a contradicting summary. Until then this seat reads the deciding line of every count bar by hand at L9.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "d0c28a59be:.tools/to-pipeline-gate.py:136-141 -- 'byte-identical to proof-of-spec-check.py's PLACEHOLDERS_TAG_RE'",
        "IRPT_FNTEND-W4-S7 -- 367 names instead of 1 on TO-FE-s-28's own face",
        "1.0.0_SA_CTO msg 96371 -- 648 instances, 875 PASS rows, 0 realized",
        "TO-FE-s-18 proof instance F18-AC16 / F18-AC17 output_evidence -- one summary line each"
      ]
    }
  },
  {
    "id": "IRPT_FNTEND-C-S57",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:12:22Z",
    "one_line": "ROUND-4 L9, GRADUATED to 1.0.0_SA_CTO at L10: the evidence cannot show what the criteria name. 0 of 3 Holdings captures render basis or classification, and the frozen report is WITHHELD on screen while the export prints it -- because screen and export gate on two different availability facts.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-W2-S21",
      "IRPT_FNTEND-W1-S51",
      "IRPT_FNTEND-W1-S52",
      "IRPT_FNTEND-W1-S53"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "F18's criteria name a Holdings capture per basis and a frozen report whose screen, preview and print agree; FE-s-22's claims model says each Holdings capture renders basis and classification.",
    "world_is": "From the manifest PNGs, read by this seat: AC9 (READY) mounts the body but its donut and slice table are EMPTY (W1-S52: three parentless nodes); AC10 and AC11 are StatusPanels. So 0 of 3, not W2-S21's 1 of 3. The frozen report's screen (AC4) is a StatusPanel 'Uncertain' because its fixture carries a status on 0 of 9 envelopes (W1-S51) -- AND ReportingTab.tsx:14-18 @c2eb8eb4 mounts the body only where isCompleteState (READY, STALE) while PrintEntry.tsx carries no report-state check (0 matches over that file). AC6's own Methods page prints 'Report availability UNCERTAIN' beside 'Bundle availability READY'. The screen gates on the REPORT's availability, the export renders on the BUNDLE's. AC14's Global map has no holdings key (W1-S53).",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO at L10 for the two product decisions -- (i) whether an UNCERTAIN report may be exported that the screen withholds, and (ii) W2-S21's (a)/(b)/(c) -- with 2.0.0_SA_COO~F for the three fixture remediations (a status on the frozen map; a parented Holdings tree; a holdings key on the Global map). DISARMS when (i) is ruled and the fixtures are re-cut so each capture can show what its criterion names.",
    "notes": "CORRECTION TO C-S51, recorded here beside the row it concerns: every round-4 judgment criterion ends 'RECORD; NO VERDICT', and that is the WORKER's instruction -- the CVO grades. C-S51 described F18-AC18 as 'RECORD with NO VERDICT' as though it bound this seat. It does not: F18-AC18 carries a verdict at L9 (NOT MET, see the round-4 L8/L9 record). C-S51's conclusion is unaffected -- no criterion that reaches this seat asks whether a capture renders its claimed field.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/captures.manifest.json -- 11 entries; PNGs tracked at 887b183a2a",
        "fe-s-18_holdings_{observed,target,missing_attribution}_390.png -- empty tree; 'Uncertain'; 'Partial'",
        "fe-s-18_reporting_frozen_390.png -- StatusPanel 'Uncertain / Source time unknown'",
        "fe-s-18_print_frozen_1440.png page 3 -- 'Report availability UNCERTAIN', 'Bundle availability READY'",
        "portal c2eb8eb4:src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx:14-18 -- isCompleteState = READY, STALE",
        "portal c2eb8eb4:src/pages/InvestorReporting/export/PrintEntry.tsx -- 0 matches for a report-state check"
      ]
    }
  },
  {
    "id": "IRPT_FNTEND-C-S58",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:12:22Z",
    "one_line": "ROUND-4 L9, GRADUATED to 1.0.0_SA_CTO for its round analysis: criteria cut against an ASSUMPTION rather than the code -- three at S55's own count, five at the COO's (96384) -- and not one caught by an issuance gate.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-S55"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "L6 cuts criteria that the cell's code and the named instrument can satisfy as written.",
    "world_is": "S55 counts THREE, one per order it names: F28-AC6's bar was a string its battery never prints; F26-AC8 needed FE-s-22's suite green while F26-AC5 repaired exactly what that suite pins; F25-AC6 needed a display surface outside the grant. Each was caught by a worker REFUSING. The COO's packet 96384 counts FIVE, adding F18-AC17 (W1-S54, refused) and the split control pair (W2-S22, filed as an observation, not a refusal). Every one was repaired mid-round by a modification of an issued order -- six such commits this round -- and a modification is exactly what GATE (viii) does not re-check (F28-AC8's qualification).",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F as issuer, with 1.0.0_SA_CTO in the round analysis. DISARMS when a cut-time check exists that catches at least one of S55's three shapes before issuance rather than a worker after spawning -- S55 itself names the OUTPUT-VOCABULARY limb as mechanisable.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "IRPT_FNTEND-S55 -- three instances, each with the control that would have caught it",
        "2.0.0_SA_COO~F msg 96384 section 3 -- 'FIVE instances this round, all caught by workers refusing'",
        "9ab6043728, bf95fb7b9a, 49f4026218, 913706a898, c44180ab9b, 6177717ce0 -- the six modifications, subjects read"
      ]
    }
  }  ,
  {
    "id": "IRPT_FNTEND-C-S59",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:37:45Z",
    "one_line": "ROUND-4 L9 GRADE RECORD: the five JUDGMENT verdicts of the L8/L9 record (be3b6849a9, section 3) moved into the `grades` carrier so a consumer can reject on them -- 4 PASS (three with a named qualification), 1 FAIL (F18-AC18).",
    "class": "OBSERVATION",
    "spec_asserts": "Spine v3 L9: a JUDGMENT criterion is graded by the CVO, and the verdict lives in the `grades` carrier, one entry per criterion, on a row of the CVO's -- never as free text.",
    "world_is": "At be3b6849a9 the five verdicts landed in the record's prose only; C-S52..C-S58 carry dispositions, not grades. This row carries them, each bound to its proof-of-spec instance at a commit. Vocabulary mapped, no verdict changed: MET -> PASS; MET WITH A NAMED QUALIFICATION -> PASS with the qualification in `reason`; NOT MET -> FAIL.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND4_L8_L9_20260913.md@be3b6849a9 section 3 -- the five verdicts and their evidence",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-25.consumer-boundary.proof_of_spec.json@86f2959ab1",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-26.holdings-fixtures.proof_of_spec.json@55887ce562",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-27.declared-preconditions.proof_of_spec.json@10093a2dff",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-28.mandatory-placeholders.proof_of_spec.json@c0eb49d1e1",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-18.evidence-mobile-captures.proof_of_spec.json@85259e922e"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: it adjudicates no item and opens nothing (schema, `grades`). The qualifications it names are carried to 1.0.0_SA_CTO in the round-4 slug, items 1 and 4-6.",
    "hazard_standing": "INERT",
    "grades": [
      {
        "criterion": "F25-AC12",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-25.consumer-boundary.proof_of_spec.json@86f2959ab1",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION (graded from consumer-boundary.result.md and portal fbc5699c). Bar: the four fixes preserve what the contract distinguishes without inventing a distinction the contract does not make. Absent-vs-null, the two nines (36 of 36 pairs distinguishable), the generator's coordinate refusal and the two OPTIONAL Availability members all carry a contract distinction through and invent none. Qualification: the panel still reads 'Updated 4d ago' (fe-s-18_holdings_target_390.png, fe-s-18_holdings_missing_attribution_390.png) while it now measures the age of business_date, the date the answer is for -- a label that misnames what it measures."
      },
      {
        "criterion": "F26-AC9",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-26.holdings-fixtures.proof_of_spec.json@55887ce562",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION (graded from holdings-fixtures.result.md and the v1 StatusEnvelope schema). Bar: each fixture's state is one the wire may genuinely carry for that basis, and none was chosen merely to force a difference. observed READY, missing-attribution PARTIAL and target UNCERTAIN are each genuine for their basis, and the three-way difference was required by F26-AC3. Qualification: target's UNCERTAIN rests on a basis-relative rule (a TARGET snapshot without a named model revision is UNCERTAIN) that the contract does not state -- the worker's own named weakest case."
      },
      {
        "criterion": "F27-AC8",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-27.declared-preconditions.proof_of_spec.json@10093a2dff",
        "verdict": "PASS",
        "reason": "MET (graded from declared-preconditions.result.md). Bar: a reader of a run can tell 'this was not exercised' from 'this was exercised and held' without knowing the port. Three independent signals, any one sufficient: the runner's skip count, each 'SKIPPED ... PRECONDITION ABSENT: <measured reason>' notice, and the 'BODIES MOUNTED: N of 2' bar that only an exercised run emits; the precondition line prints the port; and precondition MET with a broken seam reads FAIL, not SKIPPED."
      },
      {
        "criterion": "F28-AC8",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-28.mandatory-placeholders.proof_of_spec.json@c0eb49d1e1",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION (graded from mandatory-placeholders.result.md and .tools/to-pipeline-gate.py @d0c28a59be). Bar: the boundary between what the gate binds and what it grandfathers is defensible and stated, not chosen to make the tests pass. Stated in the refusal a seat receives (:884-889 appends PLACEHOLDERS_BOUNDARY); defensible (reuses _newly_added, rejects corpus and date grandfathering on their mechanics); proven by identical bytes refused as an ADD and admitted as a MODIFY in one run. Qualification: the MODIFY exemption is wider than either stated reason -- an amendment adding a <TOKEN> to an order that already declares is never checked. No instance this round."
      },
      {
        "criterion": "F18-AC18",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-18.evidence-mobile-captures.proof_of_spec.json@85259e922e",
        "verdict": "FAIL",
        "reason": "NOT MET on clause 2 (graded from the 11 manifest PNGs tracked at 887b183a2a and portal c2eb8eb4). Bar: nothing clips or overlaps at 390; screen, preview and print of the frozen report agree figure for figure; the screens and the export read as one Opal product. Clause 1 MET. Clause 2 NOT MET: the screen (fe-s-18_reporting_frozen_390.png) shows a StatusPanel 'Uncertain / Source time unknown' and no figures while preview and print render the report; ReportingTab.tsx:14-18 mounts the body only on READY or STALE, PrintEntry.tsx carries no report-state check, and the print reads 'Report availability UNCERTAIN' beside 'Bundle availability READY'. Clause 3 MET visually, qualified by clause 2."
      }
    ]
  }  ,
  {
    "id": "IRPT_FNTEND-C-S60",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:41:48Z",
    "one_line": "BACKLOG (rounds 2-3), DISMISSED: the round-2 seam defect -- tab bodies that could not mount from any network response -- was fixed in round 3 and proven on the network path, then re-exercised in round 4.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-W1-S33",
      "IRPT_FNTEND-S30"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "W1-S33 and S30 (both BLOCKING): the Reporting and Holdings bodies gate on an availability no adapter sets, so no network response can mount them.",
    "world_is": "Fixed in round 3 as RULING 2 ordered: 1.0.0_SA_CTO's round-3 analysis (section 0) reads NETWORK STATES CARRIED 9 of 9 against 1 of 9 pre-fix and BODIES MOUNTED 2 of 2 against 0 of 2, in a real browser, with the new tests recorded RED first. Round 4 re-exercised it: F18-AC17 ran the fe-s-19 browser tests with the dev server up (96384 section 5), and fe-s-18_holdings_observed_390.png shows the Holdings body mounted.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND3_20260912.md@b453306a65 section 0 -- 9 of 9 states, 2 of 2 bodies, red-first",
        "2.0.0_SA_COO~F msg 96384 section 5 -- F18-AC17 486 pass / 1 skip / 0 fail, dev server up on 5181",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_holdings_observed_390.png@887b183a2a -- the body mounted"
      ]
    },
    "hazard_standing": "INERT",
    "dismissal_reason": "Remediated and re-exercised in a later round, on the path that could not fake it. The Holdings body mounts EMPTY at round 4 -- that is W1-S52, a fixture defect graduated in C-S57, not this seam."
  },
  {
    "id": "IRPT_FNTEND-C-S61",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:41:48Z",
    "one_line": "BACKLOG, DISMISSED: four producer moves under seated consumer cells and the merged-DEV red they caused -- the byte pin they broke was retired for a content pin, which is in the tree with both arms, and DEV is green.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-S20",
      "IRPT_FNTEND-S21",
      "IRPT_FNTEND-S28",
      "IRPT_FNTEND-S33"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "S20/S21: merged DEV red while each branch was green alone; S28/S33: producer commits landed under a seated consumer cell, the fourth fourteen minutes after the cut and while its worker ran.",
    "world_is": "RULING 3 of the round-2 analysis retired the byte pin for consumer cells, and round 3 built the replacement: at portal c2eb8eb4, __tests__/fe-s-13/content-pins.test.ts pins the operations, route keys and required fields the client consumes (:21) and prints 'CONSUMED CONTENT PINNED: operations, route keys, required fields' (:297); the round-3 analysis reads 12 of 12 operations, 12 of 12 route keys, 78 of 78 fields, additive tolerated 3 of 3, breaking caught 3 of 3. The suite reads 486 pass / 1 skip / 0 fail at round 4.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND2_20260912.md@f819d7cb7d RULING 3",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND3_20260912.md@b453306a65 section 5",
        "portal c2eb8eb4:src/pages/InvestorReporting/__tests__/fe-s-13/content-pins.test.ts:21,297",
        "2.0.0_SA_COO~F msg 96384 section 5"
      ]
    },
    "hazard_standing": "INERT",
    "dismissal_reason": "The mechanism that turned a producer move into a red consumer is replaced, and the replacement carries its negative arm; DEV is green. The rows stand as the history of why."
  },
  {
    "id": "IRPT_FNTEND-C-S62",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:41:48Z",
    "one_line": "BACKLOG, DISMISSED: fourteen rows recording round-2 and round-3 cut defects, issuer amendments and seating slips -- each repaired inside its round and every order now terminal; the CLASS recurred in round 4 and is carried by C-S58.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-W3-S9",
      "IRPT_FNTEND-W3-S10",
      "IRPT_FNTEND-S22",
      "IRPT_FNTEND-S23",
      "IRPT_FNTEND-S24",
      "IRPT_FNTEND-S25",
      "IRPT_FNTEND-S26",
      "IRPT_FNTEND-S31",
      "IRPT_FNTEND-S32",
      "IRPT_FNTEND-S37",
      "IRPT_FNTEND-S41",
      "IRPT_FNTEND-S43",
      "IRPT_FNTEND-S45",
      "IRPT_FNTEND-W1-S38"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each records an order whose criterion, premise, sequencing or amendment was wrong as cut or issued: W3-S9/S25 (F16-AC8's invocation stale), W3-S10/S23 (F16-AC9 against six pre-existing failures), S24 (F15-AC8 unsatisfiable in its grant), S26 (worktrees cut before the seating flip), S22 (the round-2 resumption), S31 (F18-AC6's URL), S32 (a criterion patched through a message), S37 (a face premise true in 5 of 7), S41/W1-S38 (F19-AC8's bar cut on a prediction), S43 (a hole in RULING 5a), S45 (a bar fixed in one face of three).",
    "world_is": "Every order is terminal: 28 of 28 task orders under task-orders/ read <status>complete at this read. The mechanisms asked for were ruled -- RULING 5.1 and 5.2 of the round-2 analysis for S31 and S32, RULING F of the round-3 analysis for S43 -- and the failure counts are gone: 1 fail at round 3's drain (round-3 analysis section 3), 486 pass / 1 skip / 0 fail at round 4. S37's disarm was discharged in prose by C-S47, and the instance it concerned is superseded by FE-s-18's round-4 run. What does NOT close is the class -- a criterion or premise cut against an assumption -- which recurred three times in round 4 and is graduated in C-S58.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND2_20260912.md@f819d7cb7d RULING 5",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND3_20260912.md@b453306a65 RULING F and section 3",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/ -- 28 of 28 read <status>complete",
        "IRPT_FNTEND-C-S47@d25488815d -- S37's rule and disarm",
        "2.0.0_SA_COO~F msg 96384 section 5"
      ]
    },
    "hazard_standing": "INERT",
    "dismissal_reason": "Each instance was repaired within its round and its order is terminal. The recurring class is carried once, by C-S58, rather than re-opened fourteen times."
  },
  {
    "id": "IRPT_FNTEND-C-S63",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:41:48Z",
    "one_line": "BACKLOG, DISMISSED: the channel line-ending re-render (a worker's append and the issuer's union resolver) has not recurred -- every non-merge commit touching INVESTIGATION_v2.md since round 3's drain deletes 0 lines.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-W1-S48",
      "IRPT_FNTEND-S47"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "W1-S48: a 140-line append landed as a 3618-line rewrite; S47: the issuer's union resolver re-renders every row's line ending at each drain.",
    "world_is": "Measured with git log --numstat over INVESTIGATION_v2.md since 2026-09-12T10:30Z: 18 commits, 15 with a numstat line, 0 deletions in every one. The merge commits carry no numstat under this instrument and are NOT certified by it. The issuer's round-4 packet reports three channel conflicts resolved by a byte-preserving union with CLOUD's rows kept verbatim.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log --since=2026-09-12T10:30:00Z --numstat -- INVESTIGATION_v2.md: 18 commits, 15 numstat lines, 0 deletions",
        "2.0.0_SA_COO~F msg 96384 section 1 -- 'resolved by a byte-preserving union'"
      ]
    },
    "hazard_standing": "INERT",
    "dismissal_reason": "The defect was an append rendered as a rewrite; the append-only property it broke holds on every commit this instrument can read since. The merge path is named as uncertified, not claimed."
  },
  {
    "id": "IRPT_FNTEND-C-S64",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:41:48Z",
    "one_line": "BACKLOG, DISMISSED: ten rows whose remedy a ruling ordered and a round-3 or round-4 cell built -- checker arming, the fixture cell, declared preconditions, the consumer boundary, the fonts list, and round 3's own close.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-W3-S14",
      "IRPT_FNTEND-S38",
      "IRPT_FNTEND-S44",
      "IRPT_FNTEND-W2-S18",
      "IRPT_FNTEND-W1-S45",
      "IRPT_FNTEND-W1-S41",
      "IRPT_FNTEND-W1-S42",
      "IRPT_FNTEND-W1-S43",
      "IRPT_FNTEND-S48",
      "IRPT_FNTEND-W1-S28"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "W3-S14/S38: the checker limb's enforcement is opt-in; S44/W2-S18: FE-s-18 cannot close in round 3; W1-S45: the failure count is port-conditional; W1-S41/S42/S43: the v0.14 distinctions do not survive the consumer; W1-S28: RENDER_PACKAGE.fonts names 3 of 4 faces; S48: round 3 drained with FE-s-18 open.",
    "world_is": "W3-S14/S38 -> RULING D, built by FE-s-28 (to-pipeline-gate.py GATE (viii) at d0c28a59be). S44/W2-S18 -> RULINGS B and E, built by FE-s-26; FE-s-18 is complete at 2527062737 with F18-AC3 passing. W1-S45 -> RULING C, built by FE-s-27 (F27-AC8 PASS, C-S59). W1-S41/S42/S43 -> RULING A, built by FE-s-25 (F25-AC12 PASS with a named qualification, C-S59). W1-S28 -> at portal c2eb8eb4, render/manifest.ts:156 names all four Lato faces and __tests__/fe-s-4/manifest.test.ts:287 asserts the flat list names every packaged face. S48 recorded round 3's drain; round 4 has drained.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND3_20260912.md@b453306a65 RULINGS A-E",
        "d0c28a59be:.tools/to-pipeline-gate.py GATE (viii)",
        "IRPT_FNTEND-C-S59 -- F25-AC12, F27-AC8 grades",
        "2527062737 -- FE-s-18 complete",
        "portal c2eb8eb4:src/pages/InvestorReporting/render/manifest.ts:156; __tests__/fe-s-4/manifest.test.ts:287"
      ]
    },
    "hazard_standing": "INERT",
    "dismissal_reason": "Built and graded. What each build left behind is carried elsewhere and not re-opened here: the <placeholders> reader's false-admits (C-S56), the 'Updated N ago' label (round-4 slug item 4), and the two Analysis panels FE-s-25's grant did not reach (C-S65)."
  },
  {
    "id": "IRPT_FNTEND-C-S65",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:41:48Z",
    "one_line": "BACKLOG, GRADUATED to 1.0.0_SA_CTO: three consumer defects still LIVE at the drained round-4 vintage -- two Analysis panels age the wrong date, and a body carrying no envelope identity still bypasses every refusal.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-W1-S46",
      "IRPT_FNTEND-W2-S11",
      "IRPT_FNTEND-W1-S39"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "W1-S46: the source-age fix must reach every panel that consumes it; W2-S11/W1-S39: a body that is not a v1 envelope is refused with a named reason.",
    "world_is": "Read at portal c2eb8eb4: tabs/analysis/StageDisplay.tsx:51 and tabs/analysis/VariantSelector.tsx:61 still render formatSourceAge(envelope.sourceAsOf) -- the as_of instant, not the business_date the clause governs -- while StatusPanel.tsx:61 uses formatSourceAgeForState; FE-s-25's grant reached one consumer of three, as W1-S46 said. And contracts/envelope.ts:164-167 still returns false for a body carrying none of contract_version, operation and firm_id, so such a body never reaches parseIrEnvelope's refusals (:178-183); F19-AC6 graded only bodies carrying two of the three (__tests__/fe-s-19/pre-envelope.test.ts:5-9), and no round-4 criterion touched the remainder.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal c2eb8eb4:src/pages/InvestorReporting/tabs/analysis/StageDisplay.tsx:51",
        "portal c2eb8eb4:src/pages/InvestorReporting/tabs/analysis/VariantSelector.tsx:61",
        "portal c2eb8eb4:src/pages/InvestorReporting/contracts/envelope.ts:164-167,178-183",
        "portal c2eb8eb4:src/pages/InvestorReporting/__tests__/fe-s-19/pre-envelope.test.ts:5-9"
      ]
    },
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F as issuer -- each needs a grant no round-4 cell held (tabs/analysis/ for W1-S46; the fe-s-1 adapter test W2-S11 names) -- with 1.0.0_SA_CTO at L10 to rule whether a no-identity body is refused or adapted by design. DISARMS when both Analysis panels age business_date, and when a no-identity body is refused or the contract names its adapted path as intended."
  },
  {
    "id": "IRPT_FNTEND-C-S66",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:41:48Z",
    "one_line": "BACKLOG, GRADUATED and left ARMED on 1.0.0_SA_CTO: RULING G routed the producer-side smoke-map pin to IRPT_BCKEND -- and no IRPT_BCKEND row carries it; the routing lives only in the analysis's prose.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-W2-S10",
      "IRPT_FNTEND-W2-S15",
      "IRPT_FNTEND-S40"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "RULING G (round-3 analysis section 4): W2-S15 is the CTO's, carried to IRPT_BCKEND's round as a routing item; no round-4 FNTEND cell owns it.",
    "world_is": "Scanned all 4 IRPT_BCKEND channel files, 304 rows: none names IRPT_FNTEND-W2-S10, -W2-S15 or -S40, and none contains 'byte pin' or 'byte-pin'. The consumer side is content-pinned (fe-s-13/content-pins.test.ts); the producer side's current bytes were not re-read here, so its pin is stated as W2-S15 recorded it, not as measured.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND3_20260912.md@b453306a65 RULING G",
        "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/ -- 4 files, 304 rows, 0 naming these ids, 0 'byte pin'"
      ]
    },
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO, per RULING G. DISARMS when an IRPT_BCKEND row or cell carries the producer-side pin, or the producer pin is made content-bound like the consumer's."
  },
  {
    "id": "IRPT_FNTEND-C-S67",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:41:48Z",
    "one_line": "BACKLOG, GRADUATED to 1.0.0_SA_CTO: S42's fixture half is closed and its substrate half is not -- the portal still installs no DOM test environment, and what protects the project is a cut-time ruling, not an instrument.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-S42"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "S42: a suite with no DOM environment cannot distinguish mounting from seeding; and F18-AC3 cannot pass until the Holdings fixtures carry distinct status members.",
    "world_is": "Fixture half: F18-AC3 passes in round 4 after FE-s-26 gave the three Holdings maps distinct status members. Substrate half, read at portal c2eb8eb4: package.json names neither happy-dom nor jsdom, and bunfig.toml is not in the tree (git show rc=128). A bun test here still cannot tell mounting from seeding; the property is proven only by criteria that drive a real browser (fe-s-19, precondition-declared since FE-s-27) and by RULING 2's refusal of seeded criteria at the cut -- a ruling an issuer must remember.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal c2eb8eb4:package.json -- no happy-dom, no jsdom; bunfig.toml absent (rc=128)",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND2_20260912.md@f819d7cb7d RULING 2",
        "2527062737 -- FE-s-18 complete, F18-AC3 passing"
      ]
    },
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO, as S42 names: the owner of the test environment. DISARMS when the portal suite can observe a mount, or when the cut-time refusal of seeded criteria becomes a gate limb."
  },
  {
    "id": "IRPT_FNTEND-C-S68",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:41:48Z",
    "one_line": "BACKLOG, GRADUATED to 1.0.0_SA_CTO: S27's silent zero -- '0 account(s) in scope' printing an absent field as a count -- is still on the frozen print at round 4. C-S45 discharged the disarm in prose; this is its carrier.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-S27"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "S27: the print header's account count contradicts the account table on the same document.",
    "world_is": "The round-4 frozen print (fe-s-18_print_frozen_1440.png) heads all three pages '0 account(s) in scope' while page 2 lists A-0001 and A-0002; on page 3 the report-scope line names both accounts and the bundle-scope line names none. C-S45 located the zero as bundle.scope.accountIds absent on the wire and defaulted to an empty array; 1.0.0_SA_CTO's round-2 analysis left it with this seat. It is item 3 of the round-4 slug.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_print_frozen_1440.png@887b183a2a -- pages 1-3",
        "IRPT_FNTEND-C-S45@79561ebb71",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND2_20260912.md@f819d7cb7d section 3"
      ]
    },
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO at L10, with 2.0.0_SA_COO~F to cut the cell: the wire carries the scope's account set on this route, or the header renders UNAVAILABLE with its reason. DISARMS when the frozen print's header agrees with its own account table. C-S45's second item -- the correction to W2-S13's recorded cause -- is carried in this seat's INERT backlog pass."
  },
  {
    "id": "IRPT_FNTEND-C-S69",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:41:48Z",
    "one_line": "ROUND-1 ARMED ROWS (RULING 7), DISMISSED 7 of 16 with the rows they graduated: the harness, type and test-mechanics findings, each re-read against the drained round-4 tree rather than carried on a round ending.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-C-S1",
      "IRPT_FNTEND-W1-S1",
      "IRPT_FNTEND-C-S5",
      "IRPT_FNTEND-W1-S4",
      "IRPT_FNTEND-C-S17",
      "IRPT_FNTEND-W1-S5",
      "IRPT_FNTEND-C-S25",
      "IRPT_FNTEND-W1-S7",
      "IRPT_FNTEND-C-S29",
      "IRPT_FNTEND-W1-S8",
      "IRPT_FNTEND-C-S40",
      "IRPT_FNTEND-W1-S14",
      "IRPT_FNTEND-C-S41",
      "IRPT_FNTEND-S17"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "RULING 7 (round-2 analysis): the ARMED round-1 adjudication rows on 2.0.0_SA_COO~F's serial are this seat's to carry, per row, with evidence -- never swept on the strength of a round ending.",
    "world_is": "C-S1/W1-S1: __tests__/fe-s-3/ambient-shims.d.ts supplies the ambient declarations, and the whole-program typecheck reads rc=0 (F26-AC1 at portal 346d2b90). C-S17/W1-S5: tsconfig.json carries baseUrl and the '@/*' path at c2eb8eb4. C-S41/S17: the eight FE-s-11 type errors are gone by the same rc=0. C-S5/W1-S4 and C-S25/W1-S7: __tests__/fe-s-3/dropdown-class.test.ts is tracked at c2eb8eb4 and runs in the suite. C-S29/W1-S8 and C-S40/W1-S14: their tests run in the same suite, which reads 486 pass / 1 skip / 0 fail at round 4. RULING 7 names thirteen such rows; ADJUDICATION_v1.md holds sixteen ARMED at this read, and all sixteen are dispositioned here and in C-S70.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal c2eb8eb4:src/pages/InvestorReporting/__tests__/fe-s-3/ -- ambient-shims.d.ts, dropdown-class.test.ts",
        "portal c2eb8eb4:tsconfig.json -- baseUrl and '@/*'",
        "IRPT_FNTEND.TO-FE-s-26.holdings-fixtures.proof_of_spec.json F26-AC1 -- tsc -b --noEmit rc=0 at portal 346d2b90",
        "2.0.0_SA_COO~F msg 96384 section 5 -- 486 pass / 1 skip / 0 fail",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND2_20260912.md@f819d7cb7d RULING 7"
      ]
    },
    "hazard_standing": "INERT",
    "dismissal_reason": "Each remedy is present in the tree at the drained vintage and exercised by a round-4 run; none rests on a round ending. The typecheck vintage is 346d2b90, the last whole-program typecheck on record, not c2eb8eb4 itself -- stated rather than assumed."
  },
  {
    "id": "IRPT_FNTEND-C-S70",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:41:48Z",
    "one_line": "ROUND-1 ARMED ROWS (RULING 7), DISMISSED the other 9 of 16 with the rows they graduated: the product-surface findings, each read in the tree at c2eb8eb4 or on a round-4 capture.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-C-S7",
      "IRPT_FNTEND-W2-S2",
      "IRPT_FNTEND-C-S42",
      "IRPT_FNTEND-C-S8",
      "IRPT_FNTEND-W2-S3",
      "IRPT_FNTEND-C-S9",
      "IRPT_FNTEND-W2-S4",
      "IRPT_FNTEND-C-S15",
      "IRPT_FNTEND-W2-S6",
      "IRPT_FNTEND-C-S21",
      "IRPT_FNTEND-W3-S1",
      "IRPT_FNTEND-C-S23",
      "IRPT_FNTEND-W4-S1",
      "IRPT_FNTEND-C-S37",
      "IRPT_FNTEND-W1-S11",
      "IRPT_FNTEND-C-S38",
      "IRPT_FNTEND-W1-S12"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "RULING 7 (round-2 analysis): the ARMED round-1 adjudication rows are this seat's to carry, per row, with evidence.",
    "world_is": "C-S8/W2-S3: four Lato faces are tracked under render/assets/fonts/ and named by render/manifest.ts:156. C-S37/W1-S11: AppliedBranding and ReceiptPanel are mounted in export/ExportModal.tsx:255-256 and asserted by __tests__/fe-s-16/mounted-states.test.ts:133-134. C-S15/W2-S6: the round-1 guesses are gone -- trendingTopics and topicCloud read 0 hits in src/, and historyCutoff appears only in two tests, one asserting its absence from render/narrative/ (fe-s-16/narrative-wire.test.ts:140). C-S7/W2-S2 and C-S42: every route parses through parseIrEnvelope and the client pins the operations, route keys and required fields it consumes (fe-s-13/content-pins.test.ts). C-S9/W2-S4: the round-4 frozen print carries the cumulative-return chart. C-S21/W3-S1, C-S23/W4-S1 and C-S38/W1-S12: the round-4 captures reach the Analysis composer in both states and the Holdings body (AC7, AC8, AC9), with the seam fixed in round 3 (C-S60).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal c2eb8eb4:src/pages/InvestorReporting/render/assets/fonts/Lato-{Regular,Light,SemiBold,Bold}.ttf; render/manifest.ts:156",
        "portal c2eb8eb4:src/pages/InvestorReporting/export/ExportModal.tsx:255-256; __tests__/fe-s-16/mounted-states.test.ts:133-134",
        "portal c2eb8eb4:src/pages/InvestorReporting/__tests__/fe-s-16/narrative-wire.test.ts:140",
        "portal c2eb8eb4:src/pages/InvestorReporting/contracts/envelope.ts:178; __tests__/fe-s-13/content-pins.test.ts",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_print_frozen_1440.png@887b183a2a -- the chart; fe-s-18_analysis_{clean,correction}_390.png, fe-s-18_holdings_observed_390.png"
      ]
    },
    "hazard_standing": "INERT",
    "dismissal_reason": "Each remedy is read in the tree at c2eb8eb4 or on a round-4 capture. The Holdings body mounts empty (W1-S52, C-S57) -- a fixture defect, not the mount these rows concerned."
  }  ,
  {
    "id": "IRPT_FNTEND-C-S71",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:55:02Z",
    "one_line": "INERT BACKLOG, GRADUATED to 1.0.0_SA_CTO at L10: nine places where the v1 wire and the consumer do not meet -- none armed, each honest on screen, and each still a contract question no round has ruled.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-W1-S17",
      "IRPT_FNTEND-W2-S9",
      "IRPT_FNTEND-W2-S12",
      "IRPT_FNTEND-W3-S5",
      "IRPT_FNTEND-W1-S19",
      "IRPT_FNTEND-W1-S20",
      "IRPT_FNTEND-W1-S22",
      "IRPT_FNTEND-W3-S6",
      "IRPT_FNTEND-W3-S8"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "Each row records a producer/consumer gap a cell could only disclose, not close, inside its grant.",
    "world_is": "Re-read at the drained round-4 vintage where a read was cheap. STILL AS RECORDED: export/submit.ts:87 types submitExport to return the StatusEnvelope ack, not the ExportReceipt v1 answers in data (W2-S12, W3-S5 -- on a live plane the receipt follow-up asks for an id the producer did not mint); contracts/adapt.ts:1097 types report_title as string while tabs/analysis/composer.ts:106 sends string | null, so two builders of one body remain (W1-S20); docs/contracts/investor-reporting/v1/ publishes schemas, responses, routes.json and CONTRACT.md and no fixtures (W2-S9); the composer still renders the prepared-for / prepared-by / contacts absence (GenerateComposer.tsx:311-312) because the wire scope carries no profile and no comparison catalogue (W1-S19); NarrativePacket coverage carries no date, so the print names the earliest cited-evidence cutoff instead, labelled as such (render/narrative/compose.ts:25; W3-S8); and FIELD_MAP still names the five WIRE_ABSENT mappings (adapt.ts:1341-1356; W1-S17). NOT RE-READ HERE, stated as the rows recorded them: the corpus's snapshot_id binding (W1-S22) and the second ExportAnchorSlot's report reference (W3-S6).",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal c2eb8eb4:src/pages/InvestorReporting/export/submit.ts:87",
        "portal c2eb8eb4:src/pages/InvestorReporting/contracts/adapt.ts:1097,1341-1356",
        "portal c2eb8eb4:src/pages/InvestorReporting/tabs/analysis/composer.ts:106",
        "portal c2eb8eb4:src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx:311-312",
        "portal c2eb8eb4:src/pages/InvestorReporting/render/narrative/compose.ts:25",
        "git ls-tree HEAD docs/contracts/investor-reporting/v1/ -- no fixtures entry"
      ]
    },
    "notes": "Routed to 1.0.0_SA_CTO in this seat's rounds 2-3 slug. None is armed: each gap renders as a named absence or a loud typed refusal, never a silent wrong value. Two are cheap and consumer-side (W1-S20's one-character type; W2-S12/W3-S5's submitExport return); the rest need v1 to carry something it does not."
  },
  {
    "id": "IRPT_FNTEND-C-S72",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:55:02Z",
    "one_line": "INERT BACKLOG, GRADUATED to 1.0.0_SA_CTO: three limits on the project's own evidence -- a smoke check that cries wolf, a content pin blind in one direction, and a clip nobody can see until the Holdings tree renders.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-W1-S36",
      "IRPT_FNTEND-W2-S16",
      "IRPT_FNTEND-W1-S35"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "Evidence instruments report what they claim: a landing check reports landing, a pin catches drift in what the client reads, a layout repair is observable in its capture.",
    "world_is": "W1-S36, STILL LIVE at portal c2eb8eb4: scripts/ui-smoke.mjs:341 compares window.location.pathname (:332) with the full route string, so every query-bearing route prints 'DID NOT LAND' whether or not it landed -- and a real failure on such a route reads identically; the round-2 analysis listed it as a round-3 input and no cell took it. W2-S16: the content pin (__tests__/fe-s-13/gen-consumed.ts) is derived once and committed, so a field REMOVED from an adapter leaves a harmlessly wide pin but a field ADDED leaves an unpinned read until someone re-runs the derivation. W1-S35: the pie-label clip is a chart-geometry property no LAYOUT-ONLY grant reaches, and it cannot be observed at round 4 because the READY Holdings tree renders empty (W1-S52).",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal c2eb8eb4:scripts/ui-smoke.mjs:332,341",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND2_20260912.md@f819d7cb7d section 3 -- W1-S36 listed as a round-3 input",
        "portal c2eb8eb4:src/pages/InvestorReporting/__tests__/fe-s-13/gen-consumed.ts",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_holdings_observed_390.png@887b183a2a -- empty donut"
      ]
    },
    "notes": "Routed in this seat's rounds 2-3 slug. W1-S36 is a one-line fix outside every IRPT grant so far; W1-S35 belongs with RULING I's Holdings cell, whose real render is the first capture able to show it."
  },
  {
    "id": "IRPT_FNTEND-C-S73",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:55:02Z",
    "one_line": "INERT BACKLOG, DISMISSED: thirteen rows whose subject a later round remediated -- the font package, the narrative citations, the job states, the source age, the wire generator, the capture collision, refusal states, the export mount and the print route -- each read at c2eb8eb4 or on a round-4 run.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-W2-S8",
      "IRPT_FNTEND-W1-S29",
      "IRPT_FNTEND-W1-S30",
      "IRPT_FNTEND-W1-S31",
      "IRPT_FNTEND-W1-S32",
      "IRPT_FNTEND-W3-S7",
      "IRPT_FNTEND-W1-S21",
      "IRPT_FNTEND-S29",
      "IRPT_FNTEND-W1-S26",
      "IRPT_FNTEND-W1-S34",
      "IRPT_FNTEND-W2-S14",
      "IRPT_FNTEND-W3-S4",
      "IRPT_FNTEND-W2-S13"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each row records a defect or gap its cell could not close in its own grant.",
    "world_is": "FONTS (W2-S8, W1-S29, W1-S30, W1-S32): render/manifest.ts:156 names the four Lato faces, and fonts.manifest.json records each with its own weight and sha256, stand_ins {} and not_packaged ['italic'] -- 600 is now its own face. W1-S31: the Bold's per-face source records it as fetched 2026-09-11 by 1.0.0_SA_CTO from the Lato OFL upstream on Andrew's word ('Yes fetch lato'), so the provenance and its authority sit at the file's grain; the staged directory's sources.json still lacks the URL, and recovering it would need a re-fetch, which is egress nobody authorised. W3-S7: render/narrative/compose.ts:257 builds citations from the packet's cited evidence and PeriodInContextPage.tsx:192-194 renders them. W1-S21: the two nines read 36 of 36 pairs distinguishable (F25-AC12, C-S59) behind round 3's seam. S29: state/status.ts:455 formatSourceAgeForState, used by StatusPanel.tsx:61. W1-S26: the generator refuses a construct it cannot render (F25-AC12). W1-S34: F18-AC3 passes at round 4 -- the three Holdings PNGs differ (887b183a2a). W2-S14: the NO-HANDLER route is past tense (contracts/envelope.ts:141) and a refusal is now a state (__tests__/fe-s-19/pre-envelope.test.ts:17-21). W3-S4: __tests__/fe-s-16/mounted-states.test.ts:133-135 asserts both panels mounted. W2-S13: the print route renders the report at round 4.",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal c2eb8eb4:src/pages/InvestorReporting/render/manifest.ts:156; render/assets/fonts/fonts.manifest.json (Lato-Bold source)",
        "portal c2eb8eb4:src/pages/InvestorReporting/render/narrative/compose.ts:257; render/narrative/PeriodInContextPage.tsx:192-194",
        "portal c2eb8eb4:src/pages/InvestorReporting/state/status.ts:455; tabs/StatusPanel.tsx:61",
        "portal c2eb8eb4:src/pages/InvestorReporting/contracts/envelope.ts:141; __tests__/fe-s-19/pre-envelope.test.ts:17-21",
        "portal c2eb8eb4:src/pages/InvestorReporting/__tests__/fe-s-16/mounted-states.test.ts:133-135",
        "IRPT_FNTEND-C-S59 -- F25-AC12",
        "887b183a2a -- the three Holdings PNGs now differ",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-18_print_frozen_1440.png@887b183a2a"
      ]
    },
    "dismissal_reason": "Remediated and read in the tree or on a round-4 capture. Two things travel elsewhere rather than close here: W2-S13's recorded CAUSE for the print header's zero was contested by S27/C-S45 on the round-2 capture, and the zero itself is RULING J's (C-S68), whose disarm -- the header agreeing with its own account table -- settles the cause question with it; and W1-S31's missing URL is a record gap, not a provenance gap."
  },
  {
    "id": "IRPT_FNTEND-C-S74",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:55:02Z",
    "one_line": "INERT BACKLOG, DISMISSED: twenty-eight process, cut and correction rows from rounds 1-3 -- round records, issuer slips, criteria cut on a wrong premise, and self-corrections -- every order terminal and every correction carried by its own later row.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-W1-S15",
      "IRPT_FNTEND-S18",
      "IRPT_FNTEND-S19",
      "IRPT_FNTEND-W1-S16",
      "IRPT_FNTEND-W3-S11",
      "IRPT_FNTEND-W3-S12",
      "IRPT_FNTEND-W1-S18",
      "IRPT_FNTEND-W1-S23",
      "IRPT_FNTEND-W1-S24",
      "IRPT_FNTEND-W1-S25",
      "IRPT_FNTEND-W1-S27",
      "IRPT_FNTEND-S34",
      "IRPT_FNTEND-S35",
      "IRPT_FNTEND-W4-S3",
      "IRPT_FNTEND-W4-S4",
      "IRPT_FNTEND-W3-S13",
      "IRPT_FNTEND-W3-S15",
      "IRPT_FNTEND-W3-S16",
      "IRPT_FNTEND-S36",
      "IRPT_FNTEND-W1-S37",
      "IRPT_FNTEND-S39",
      "IRPT_FNTEND-W1-S40",
      "IRPT_FNTEND-W2-S17",
      "IRPT_FNTEND-W1-S44",
      "IRPT_FNTEND-S46",
      "IRPT_FNTEND-W2-S19",
      "IRPT_FNTEND-W1-S47",
      "IRPT_FNTEND-W2-S7"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each records a round event, an issuer or worker slip, a wrong premise in a face, or a correction to an earlier row.",
    "world_is": "Every order they concern is terminal: 28 of 28 task orders read <status>complete at this read. The corrections are carried by later rows, not by edits: S35 corrects S33, S46 corrects S44, W2-S19 carries W2-S17's removal, W1-S47 carries W1-S44's supersession, W3-S15 corrects a preflight fact. The mechanisms asked for were ruled and built: RULING F, the face at the named commit (W3-S12, W1-S23, W1-S40); FE-s-28 made <placeholders> mandatory, the element W3-S16 disclosed adding to its own order; RULING 3's content pin (S39). W1-S24 and W1-S25 record what v1 cannot express -- a per-section support verdict, a consumer-side revision counter -- as consequences of the contract, not consumer defects. S34 is the issuer's own round-2 disarm sweep, now carried per ID by C-S61, C-S62, C-S69 and C-S70. W2-S7: the print document's faces are local; the external request it measured is the portal shell's global stylesheet, src/index.css:16 at portal c2eb8eb4, which imports Google Fonts' Inter on every route -- outside every IRPT grant.",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/ -- 28 of 28 read <status>complete",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND3_20260912.md@b453306a65 RULING F",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND2_20260912.md@f819d7cb7d RULING 3",
        "portal c2eb8eb4:src/index.css:16",
        "IRPT_FNTEND-C-S61, C-S62, C-S69, C-S70 -- S34's rows, per ID"
      ]
    },
    "dismissal_reason": "Repaired within their rounds, or recorded consequences of the wire. The class of cut defects is carried once, by C-S58 and RULING N (ROUND_ANALYSIS_IRPT_FNTEND_ROUND4_20260913.md). W2-S7's shell request is the portal's, named here, not carried by this project."
  }  ,
  {
    "id": "IRPT_FNTEND-C-S75",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:57:06Z",
    "one_line": "C-S66's DISARM CONDITION IS MET: IRPT_BCKEND-S51 now carries the producer-side smoke-map pin in IRPT_BCKEND's own channel, so W2-S10, W2-S15 and S40 are carried there, correctly, and close on this side.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-W2-S10",
      "IRPT_FNTEND-W2-S15",
      "IRPT_FNTEND-S40"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "C-S66 (df08e2c33c): DISARMS when an IRPT_BCKEND row or cell carries the producer-side pin.",
    "world_is": "IRPT_BCKEND-S51 (1.0.0_SA_CTO, committed bf92c169ac) routes both halves into IRPT_BCKEND's next L4 packet: the producer's paired seam test reads 14 failed, 39 passed -- the ten paired-request cases assert flat-slug keys against a map that now carries v1 declared paths, and one more fails on a route table grown from 11 to 12 -- and the producer's StatusEnvelope copy never received v0.14. S51 is ARMED there, with 1.0.0_SA_CTO as disarm owner and a condition: both carriers agree and the paired test is green on a named portal commit. NOT re-measured here: the 14/39 figure is the CTO's, and S51 states its own grain caveat (it read the portal WORKING TREE's smoke map).",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "IRPT_BCKEND-S51@bf92c169ac -- org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md",
        "IRPT_FNTEND-C-S66@df08e2c33c -- the disarm condition",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND4_20260913.md@23af9479ab section 6, items 5-6"
      ]
    },
    "dismissal_reason": "Carried elsewhere, correctly: the hazard is IRPT_BCKEND's and now has a carrier, an owner and a condition in that project's channel. Holding it ARMED here too would be a second carrier of one hazard -- the drift C-S66 existed to end."
  },
  {
    "id": "IRPT_FNTEND-C-S76",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T09:57:06Z",
    "one_line": "S57, the CTO's disarm record for eleven rows it owns, is carried: all eleven already had per-ID carriers (C-S60, C-S61, C-S62, C-S64, C-S67), and ten agree with it. On S42 this seat and the CTO differ; the difference is recorded, not resolved.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_FNTEND-S57"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "S57: the disarm conditions of S30, S33, S38, S42, S43, S44, W2-S18, W1-S41, W1-S42, W1-S43 and S48 are discharged by the evidence in the round-4 analysis section 4; their disposition is the CVO's.",
    "world_is": "The carriers landed at df08e2c33c, before S57 and on independent reads: S30 in C-S60; S33 in C-S61; S43 in C-S62; S38, S44, W2-S18, W1-S41, W1-S42, W1-S43 and S48 in C-S64 -- all DISMISSED_WITH_REASON, agreeing with S57. S42 is in C-S67, GRADUATED and ARMED: S57 discharges S42's blocking arm (the fixture block, cleared by FE-s-26) and carries its instrument lesson into RULING I; C-S67 agrees the blocking arm is cleared but keeps the substrate half armed, because portal c2eb8eb4's package.json still installs no DOM environment and what protects the project is a ruling an issuer must remember, not an instrument. S57's twelfth row, S40, is not disarmed by it and is closed here by C-S75.",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "IRPT_FNTEND-S57@bf92c169ac",
        "IRPT_FNTEND-C-S60, C-S61, C-S62, C-S64, C-S67@df08e2c33c",
        "portal c2eb8eb4:package.json -- no happy-dom, no jsdom",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND4_20260913.md@23af9479ab section 4"
      ]
    },
    "dismissal_reason": "A disarm record whose eleven targets were already carried per ID; S57 itself opens nothing. C-S67 stands on S42 until 1.0.0_SA_CTO rules otherwise at L10; the difference is named in this seat's rounds 2-3 slug."
  }  ,
  {
    "id": "IRPT_FNTEND-C-S77",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-13T20:54:45Z",
    "one_line": "CORRECTION TO C-S72: W1-S36 is NOT live at portal c2eb8eb4. scripts/ui-smoke.mjs:341 already compares a pathname with a pathname -- fixed at portal 25062fce by FE-s-22, both arms proven (F22-AC6, F22-AC7). C-S72 was written from the row's description, not from the line.",
    "class": "OBSERVATION",
    "spec_asserts": "C-S72 (a7187bac85): 'W1-S36, STILL LIVE at portal c2eb8eb4: scripts/ui-smoke.mjs:341 compares window.location.pathname (:332) with the full route string'.",
    "world_is": "At portal c2eb8eb4, scripts/ui-smoke.mjs:341 reads `state.loc === new URL(ORIGIN + route).pathname` -- a pathname against a pathname, not the route string W1-S36 describes. The change is portal 25062fce (0.9.0_WK_IRPT_FNTEND~2, FE-s-22, 2026-09-12), whose own diff removes `state.loc === route` and adds the pathname comparison, and which is an ancestor of c2eb8eb4. __tests__/fe-s-22/smoke-detector.test.ts proves both arms: a landed query route prints no DID NOT LAND (F22-AC6), and a genuinely bad route prints it (F22-AC7). THIS SEAT'S OWN READ of line 341, printed while C-S72 was being written, showed the corrected line; the row followed W1-S36's prose instead. Raised by 2.0.0_SA_COO~F (96407); re-derived here from the line, the commit's diff and the test.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal c2eb8eb4:scripts/ui-smoke.mjs:341 -- `state.loc === new URL(ORIGIN + route).pathname`",
        "portal 25062fce -- diff removes `state.loc === route`, adds the pathname comparison; ancestor of c2eb8eb4",
        "portal c2eb8eb4:src/pages/InvestorReporting/__tests__/fe-s-22/smoke-detector.test.ts -- F22-AC6 and F22-AC7",
        "2.0.0_SA_COO~F msg 96407"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S36"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Remediated in round 3 and proven on both arms, so W1-S36's latest disposition moves from C-S72's GRADUATED to this row. C-S72 stands for its other two rows, W2-S16 and W1-S35. The round-5 input C-S72 produced (1.0.0_SA_CTO's round-4 addendum, section 7, item 11) rests on this seat's error; 2.0.0_SA_COO~F has told 1.0.0_SA_CTO, and the round-5 decomposition records the item as done.",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-C-S78",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T11:26:58Z",
    "one_line": "ROUND-5 L9 GRADE RECORD: the eight JUDGMENT verdicts, one per order, bound to each proof instance at its commit -- 7 PASS (6 with a named qualification) and 1 FAIL, F29-AC15 on its third clause (row S61).",
    "class": "OBSERVATION",
    "spec_asserts": "Spine v3 L9: a JUDGMENT criterion is graded by the CVO and never self-graded; its verdict lives in `grades`, one entry per criterion, on a row of the CVO's.",
    "world_is": "8 of 8 judgment rows in the round-5 instances read UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming this seat. Their evidence (18 captures, the result files, the portal at DEV 741bb54b, the checkers at HEAD 26774b2cdc and three doctored-instance arms) is in the record, section 3. Vocabulary as round 4: MET -> PASS; MET WITH A NAMED QUALIFICATION -> PASS with the qualification in `reason`; NOT MET -> FAIL.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-29.checker-limbs.proof_of_spec.json@6ad371c88e",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-30.availability-gate.proof_of_spec.json@71d47eb8cf",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-31.export-under-the-gate.proof_of_spec.json@09c82ae177",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-32.holdings-under-the-gate.proof_of_spec.json@c271e0d702",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-33.fixture-reach.proof_of_spec.json@e46121f301",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-34.business-date-label.proof_of_spec.json@af28a2e3d2",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~5/IRPT_FNTEND.TO-FE-s-35.envelope-refusal.proof_of_spec.json@6cd734e28f",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-36.output-vocabulary.proof_of_spec.json@534051a974",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND5_L8_L9_20260914.md@366a0b4103 section 3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: it adjudicates no item and opens nothing (schema, `grades`). The FAIL's defect is row S61, graduated ARMED in C-S84; every qualification goes to 1.0.0_SA_CTO in the round-5 slug.",
    "hazard_standing": "INERT",
    "grades": [
      {
        "criterion": "F29-AC15",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-29.checker-limbs.proof_of_spec.json@6ad371c88e",
        "verdict": "FAIL",
        "reason": "NOT MET ON ITS THIRD CLAUSE. Clauses 1-2 MET: limb 1 5 of 5 S53 cases through both readers; limb 2 2 of 2 contradicting shapes refused, 3 of 3 genuine zeros admitted; limb 3 6 of 6 seeded refused, 2 of 2 browser admitted; limb 4 4 of 4 broken modifies refused; this seat's runs at HEAD 26774b2cdc read proof-of-spec-check --self-test 32 of 32 and to-pipeline-gate --self-test 0 of 70 failed (the issuer's instrument re-run, not a different one). Clause 3 fails for limbs 2 and 3: their NEW/LEGACY boundary is read from decomp_ref.to_ref, which the graded worker writes, and the flip gate binds nothing to the flipped order; pointed at TO-FE-s-28 both limbs read ANNOUNCE/LEGACY with no violation naming the mismatch (row S61)."
      },
      {
        "criterion": "F30-AC9",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-30.availability-gate.proof_of_spec.json@71d47eb8cf",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION (fe-s-30_reporting_partial_qualified_1440.png, portal fcc91358). An amber band -- 'Partial -- Qualified answer -- not a complete report', business date, reason code -- heads the body, an amber rule runs its length, and every summary figure prints UNAVAILABLE with its reason, never 0. Qualification: the band and rule carry the whole qualification; the blocks inside keep the complete path's styling, so below the fold the rule is the only cue."
      },
      {
        "criterion": "F31-AC10",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-31.export-under-the-gate.proof_of_spec.json@09c82ae177",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION (three prints, portal 51518c8e). The Partial print states its state, business date and reason on 3 of 3 pages; the Unavailable print is a named refusal with state, reason and date; page 3's one READY is the row 'Bundle envelope (not the report)', which says in words that the report is Partial. Qualifications: the pages print the business DATE and no generation time, so the age is the reader's subtraction; and the frozen READY print states REQUESTED_WINDOW_ANSWERED beside its own 'a different window' note (row S62)."
      },
      {
        "criterion": "F32-AC9",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-32.holdings-under-the-gate.proof_of_spec.json@c271e0d702",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION (14 of 14 manifest captures, portal 7df6b4a2, own server 5213). Each renders its declared slot; Uncertain and Partial carry the amber 'Qualified answer -- not a complete report' band, rule and gap sentence, Ready a neutral band, no-answer the Unavailable panel; the classification columns show in 6 of 6 scrolled captures; pie labels equal the table's percent-of-parent in the six 1440 captures that show that column. Qualification: the READY observed answer prints Advisory 'unknown' on 3 of 3 rows unqualified -- an out-of-enum fixture value mapped silently (W2-S29) -- and the 390 target reason code reaches its band edge (W2-S31, by eye)."
      },
      {
        "criterion": "F33-AC8",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-33.fixture-reach.proof_of_spec.json@e46121f301",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION (fixture-reach.result.md, maps at portal 5067c254, StatusEnvelope.schema.json). Every state is one of the nine and every reason matches the only rule the contract gives, the pattern ^[A-Z0-9_]+$; the frozen READY is legitimate for a whole report (2 of 2 accounts, the absent 3Y outside the window, a start differing only by an NYSE holiday). Qualifications: REQUESTED_WINDOW_ANSWERED is defined nowhere and the renderer compares windows by calendar string, so the frozen print says both (row S62); Global F-CW is READY on F-49F's re-bound document, backed by no Cottonwood data, unreachable today (W2-S23)."
      },
      {
        "criterion": "F34-AC7",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-34.business-date-label.proof_of_spec.json@af28a2e3d2",
        "verdict": "PASS",
        "reason": "MET (labels at portal c6ee044e, status.ts at DEV 741bb54b). 'Business date age: 3d', 'Ready -- Business date age: 3d (STATE_REPORTED)', 'under 1m' and '5h' read as the age of a business date and name no refresh; the basis is sourceAgeBasis(slot), the governed business_date whenever the slot carries a reading (status.ts:71, :283-295); the no-status view path ages the document's own 2026-09-08, not its instant. Before: 'Ready -- Updated 3d ago'. W3-S22 and W3-S26 lie outside the label's production path and are carried in C-S83."
      },
      {
        "criterion": "F35-AC7",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~5/IRPT_FNTEND.TO-FE-s-35.envelope-refusal.proof_of_spec.json@6cd734e28f",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION (envelope-refusal.result.md, portal 357b4055 / DEV 741bb54b). A no-envelope body is refused as EnvelopeMismatch('body') in LiveClient.send (investor-reporting.ts:954) on 8 of 8 reached operations; envelopeFromRefusal makes it UNAVAILABLE carrying ENVELOPE_BODY (status.ts:258-267), never a view and never the generic FAILED; that state's panel is seen in fe-s-32_holdings_no_answer_1440.png. Qualification: ENVELOPE_BODY itself was never observed in a mounted page, and F35-AC6's deciding browser run met no server and SKIPPED its browser arms by name."
      },
      {
        "criterion": "F36-AC8",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-36.output-vocabulary.proof_of_spec.json@534051a974",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION (output-vocabulary.result.md, gate (ix) @8aa00e60fb). F28-AC6 as issued is refused in a real index and its re-cut admitted; runners, compound lines, absent targets and relayed output are ANNOUNCED or NOT EVALUATED, never refused, and the estate census refuses 6 of 1235, all AMGT_RESAPP sentence bars no regex can match; the block 'WHAT IT CANNOT KNOW, STATED RATHER THAN GUESSED' (:1061-1075) states assumptions A and B. Qualifications: it judges few bars (17 admitted, 6 refused, of 1235), and its refusal side rests on assumption B, which refused one honest bar (NFRA_CLDGRPH F5-AC1) before landing."
      }
    ]
  },
  {
    "id": "IRPT_FNTEND-C-S79",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T11:26:58Z",
    "one_line": "ROUND-5 L8: fourteen rows CLOSED INSIDE THE ROUND by an amendment or a drain, each read against its drained evidence -- DISMISSED_WITH_REASON.",
    "class": "OBSERVATION",
    "spec_asserts": "Spine L8: every new row is dispositioned before L10; a row closed in the round is dismissed with the evidence that closed it.",
    "world_is": "W3-S19, W3-S21, W3-S23, W3-S24: closed by TO-FE-s-34's amendments 12eef1910c, 1df5ac405f and 7fd807ab76, drained de65e2d559 (portal 0b41bb2f); F34 10 of 10 mechanical PASS by output (proof @af28a2e3d2); the whole suite 512/6/0 on the issuer's re-run (96556); S60 is their resolution record. W1-S58, W1-S62: amendment 2 (7a186aeb96) granted the receipt's regions; F31 10 of 10 mechanical PASS incl. AC8 (proof @09c82ae177). W1-S59, W2-S28: the worktree override took the .mjs / loadConfigFromFile shape; F31-AC1 and F32-AC1 typecheck PASS. W1-S60: page 3 reads 'Bundle envelope (not the report)' in fe-s-31_print_partial_1440.png and the frozen print. W1-S61: FE-s-33 gave the frozen map its status and the print as committed renders 3 pages, '2 account(s) in scope' over A-0001/A-0002 -- C-S68's disarm observed holding. W5-S3: a miscounted premise; the worker's run found 1 red test and a third bare-body file, both inside its grant; F35 6 of 6. W4-S8: the battery fixture was corrected, the pattern was not; self-test 32 of 32 at HEAD 26774b2cdc. W2-S30: six classification-scrolled captures close the evidence gap; a table that scrolls sideways at 390 is the layout, not a defect.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-34.business-date-label.proof_of_spec.json@af28a2e3d2",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-31.export-under-the-gate.proof_of_spec.json@09c82ae177",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-32.holdings-under-the-gate.proof_of_spec.json@c271e0d702",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~5/IRPT_FNTEND.TO-FE-s-35.envelope-refusal.proof_of_spec.json@6cd734e28f",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-31_print_frozen-as-committed_1440.png@09c82ae177",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND5_L8_L9_20260914.md@366a0b4103 section 2"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W3-S19",
      "IRPT_FNTEND-W3-S21",
      "IRPT_FNTEND-W3-S23",
      "IRPT_FNTEND-W3-S24",
      "IRPT_FNTEND-S60",
      "IRPT_FNTEND-W1-S58",
      "IRPT_FNTEND-W1-S62",
      "IRPT_FNTEND-W1-S59",
      "IRPT_FNTEND-W2-S28",
      "IRPT_FNTEND-W1-S60",
      "IRPT_FNTEND-W1-S61",
      "IRPT_FNTEND-W5-S3",
      "IRPT_FNTEND-W4-S8",
      "IRPT_FNTEND-W2-S30"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each is closed in the drained code or evidence, read here: the four FE-s-34 rows by three amendments and 10 of 10; W1-S58/W1-S62 by amendment 2 and F31-AC8 PASS; W1-S59/W2-S28 by the override's shape and a green typecheck; W1-S60 and W1-S61 in the captured prints; W5-S3 and W4-S8 inside their grants; W2-S30 by the second captures. The four ARMED rows here stand INERT from this row.",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-C-S80",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T11:26:58Z",
    "one_line": "ROUND-5 L8: six rows ACCEPTED AT L9 OR READ AS RECORDS -- a worker reading, a worker choice, a corrected premise, a generator side effect, and two issuer disarm records -- DISMISSED_WITH_REASON.",
    "class": "OBSERVATION",
    "spec_asserts": "Spine L9: a worker judgment within a grant and an issuer's disarm record are weighed by the CVO; accepted, each is dismissed with its reason.",
    "world_is": "W1-S55: on the network plane an absent producerState means no status arrived, the view state is then EXPLICIT_UNKNOWN (UNCERTAIN) and the gate sends it to the panel -- ruling H exactly; the fixture branch honours view states the ruling never addressed; its one divergence is W3-S25 (C-S83). W4-S10: ten fetched-content props, by subtraction from the measured 15, are what keep limb 3 from being satisfied by its worker; three would not; F15-AC7 declares no network today; the cut's one-suite-short census is S55's class (C-S84). W3-S20: the outcome 1.0.0_SA_CTO named is met; the premise was wrong only on the no-status path (W3-S21), closed by ruling R. W2-S26: by the generator's design each Holdings map is the whole page around one report; 0 differing keys apart from nodes and the one status; the suite green before and after. S58: a prospective disarm record, verified -- FE-s-32's manifest records its own port 5213 and the issuer re-ran 5247/5261/5265; its residuals are live and graduated in C-S81. S59: a detection record; the detector exists (__tests__/fe-s-33/fixtures-reach.test.ts, F33-AC6 grades the Global map's holdings per firm, DEV 741bb54b); prevention is graduated with W2-S24 in C-S82.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-30.availability-gate.proof_of_spec.json@71d47eb8cf",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-29.checker-limbs.proof_of_spec.json@6ad371c88e",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-34.business-date-label.proof_of_spec.json@af28a2e3d2",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-33.fixture-reach.proof_of_spec.json@e46121f301",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-32_captures.manifest.json@c271e0d702",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND5_L8_L9_20260914.md@366a0b4103 sections 2 and 6"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S55",
      "IRPT_FNTEND-W4-S10",
      "IRPT_FNTEND-W3-S20",
      "IRPT_FNTEND-W2-S26",
      "IRPT_FNTEND-S58",
      "IRPT_FNTEND-S59"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Accepted or verified at L9: W1-S55's reading is ruling H on the network plane; W4-S10's ten props are the stricter and correct set; W3-S20's outcome is met; W2-S26 is the generator's design; S58 and S59 are records whose open halves are graduated in C-S81 and C-S82.",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-C-S81",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T11:26:58Z",
    "one_line": "ROUND-5, GRADUATED to 1.0.0_SA_CTO: the DEV-SERVER RESIDUALS S58 names -- the fe-s-27 helper still defaults to port 5181, vite's cacheDir is portal-wide and written through the node_modules junction, and tsc -b writes tsbuildinfo through the same junction. FE-s-31/32 were amended around them; the next browser cell is not.",
    "class": "OBSERVATION",
    "spec_asserts": "S58: FE-s-31 and FE-s-32 run vite on a worktree-local cache and export IRPT_FE_DEV_PORT on every run.",
    "world_is": "The amendment bound two cells, not the helper: W5-S1 measured fe-s-19's browser criteria grading a DSGN worktree's vite (PID 11144) on 5181 (0 of 2, 0 of 2), and F35-AC6's deciding run met no server on 5181 and SKIPPED its browser arms by name (envelope-refusal.result.md:51). W1-S56/W5-S4 measured a worktree dev server rewriting the main checkout's shared node_modules/.vite; S58 names the portal-wide cacheDir and tsbuildinfo as NOT closed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md rows W1-S56, W1-S57, W5-S1, W5-S4, S58",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~5/envelope-refusal.result.md@6cd734e28f :51-55",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND5_L8_L9_20260914.md@366a0b4103 section 5"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S56",
      "IRPT_FNTEND-W1-S57",
      "IRPT_FNTEND-W5-S1",
      "IRPT_FNTEND-W5-S4"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO, as owner of the test environment: DISARMS when the dev-server helper refuses to run without IRPT_FE_DEV_PORT (or chooses and prints a free port), vite's cacheDir is worktree-local by config, and tsbuildinfo stays inside the worktree -- each in a granted cell. Until then every browser cut must carry the S58 amendment by hand."
  },
  {
    "id": "IRPT_FNTEND-C-S82",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T11:26:58Z",
    "one_line": "ROUND-5, GRADUATED to 1.0.0_SA_CTO: EIGHT FIXTURE, CONTRACT AND PRESENTATION GAPS the round surfaced and could not close in its grants -- FWD-11's second firm, a two-writer map, a scope root with no node_kind, a narrative for another revision, an out-of-enum advisory value, a reason code at the band edge, a contract with no report_title, and an undefined window reason (S62).",
    "class": "OBSERVATION",
    "spec_asserts": "The IRPT_FNTEND PRD and the v1 contract: every fixture state and every rendered field is one the contract defines, and FWD-11 shows each firm's holdings.",
    "world_is": "W2-S23: the page issues one holdings request for the one scope resolve-scope answers, so it reaches F-49F's envelope and never F-CW's -- FWD-11 PARTIAL. W2-S24 (with S59): fe-s-14/gen-maps.ts rewrites fe-s-14-global.json whole; detection only. W2-S25: HoldingsSnapshot has no scope-level node_kind, so the root is an ACCOUNT node while custody_totals.unique_account_count reads 3. W2-S27: the frozen map's narrative names perf-9, not rev-49f-000091; a narrative-on print would pair them. W2-S29: advisory_status 'ADVISORY' is outside ADVISED|RESIDUAL|UNKNOWN and is mapped to unknown with authoritative=true -- seen on 3 of 3 rows of the READY observed captures (F32-AC9's qualification). W2-S31: TARGET_BLEND_MODEL_REVISION_UNNAMED reaches its band's right edge at 390 (fe-s-32_holdings_target_390.png, by eye). W5-S2: 0 of 25 v1 files name report_title and routes.json carries no analysis-POST request schema. S62: REQUESTED_WINDOW_ANSWERED is defined nowhere and the renderer compares windows by calendar string.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-32_holdings_observed_1440_table_scrolled.png@c271e0d702",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-32_holdings_target_390.png@c271e0d702",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fixture-reach.result.md@e46121f301",
        "docs/contracts/investor-reporting/v1/",
        "portal 741bb54b:src/pages/InvestorReporting/render/performance/MethodsAndSources.tsx:58",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND5_L8_L9_20260914.md@366a0b4103 sections 2-3"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W2-S23",
      "IRPT_FNTEND-W2-S24",
      "IRPT_FNTEND-W2-S25",
      "IRPT_FNTEND-W2-S27",
      "IRPT_FNTEND-W2-S29",
      "IRPT_FNTEND-W2-S31",
      "IRPT_FNTEND-W5-S2",
      "IRPT_FNTEND-S62"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-C-S83",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T11:26:58Z",
    "one_line": "ROUND-5, GRADUATED to 1.0.0_SA_CTO: THREE BUSINESS-DATE PLANE DEFECTS outside the label's production path -- a test that asserts an instant's age under the new label, a helper that reads the presence of sourceDate as a status, and a null that renders as malformed.",
    "class": "OBSERVATION",
    "spec_asserts": "Ruling K and ruling R: the panel ages the business date, never an instant, on any path; the view contract's null businessAsOf means 'no clock'.",
    "world_is": "W3-S22: fe-s-21's panelFor builds its envelope from StatusEnvelope.sourceAsOf, so F21-AC3 grades an as_of instant's age printed as 'Business date age' -- a test asserting the mislabel; a repair must re-point it. W3-S25: businessDateOf (state/availability.ts:102-104) reads any availability.sourceDate as the status's reading; latent while every no-status wire document goes to the panel; the discriminator the gate already uses is producerState. W3-S26: adapt.ts readingFromValue turns a view document's null businessAsOf into fact NULL, shown as 'Source date malformed', where the view contract defines null as 'no clock' (contracts/index.ts:147); 3 of 134 view documents, all in smoke/fe-s-3-loading.json.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md rows W3-S22, W3-S25, W3-S26",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-34.business-date-label.proof_of_spec.json@af28a2e3d2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND5_L8_L9_20260914.md@366a0b4103 section 3, F34-AC7"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W3-S22",
      "IRPT_FNTEND-W3-S25",
      "IRPT_FNTEND-W3-S26"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-C-S84",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T11:26:58Z",
    "one_line": "ROUND-5, GRADUATED to 1.0.0_SA_CTO: THE CHECKER, THE LAW TEXT AND THE CUT -- the graded party can move limbs 2 and 3 to LEGACY (S61, ARMED), CLAUDE.md quotes a docstring sentence its source dropped (W4-S9), the issuer's ninth cut defect joins S55's class (W4-S11), and six AMGT_RESAPP bars can never match (W4-S12).",
    "class": "OBSERVATION",
    "spec_asserts": "F29-AC15; CLAUDE.md Rule 27 quotes the gate's own docstring; S55: a cut is checked against what it overturns before it is issued.",
    "world_is": "S61: as that row measures. W4-S9: CLAUDE.md:42 still reads 'A modification (M) does not: this gate never refuses an existing TO' while .tools/to-pipeline-gate.py:1706 now reads 'A modification (M) does not: no limb that reads THIS set refuses an existing TO' -- read at HEAD 26774b2cdc; the law edit cb87fdd6fb did not touch it. W4-S11: F36-AC4 named a criterion shape no committed order has, the issuer's defect (9) of 9 this round (96556), with W4-S10's one-suite-short census beside it; the issuer's own lesson is that the census that held was the worker's whole-suite run with the patch applied. W4-S12: 6 AMGT_RESAPP criteria carry English-sentence <expect> bars that proof-of-spec-check searches as a regex, so none can ever PASS by output.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND5_L8_L9_20260914.md@366a0b4103 sections 3 and 4",
        "CLAUDE.md:42 and .tools/to-pipeline-gate.py:1706 at 26774b2cdc",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/output-vocabulary.result.md@534051a974",
        "msg 96556 section 3"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S61",
      "IRPT_FNTEND-W4-S9",
      "IRPT_FNTEND-W4-S11",
      "IRPT_FNTEND-W4-S12"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO: S61 disarms as that row names; W4-S9 by one law edit to CLAUDE.md:42; W4-S12 by routing to AMGT_RESAPP's issuer. Until S61 disarms, this seat reads each new instance's decomp_ref.to_ref against its own order at L9."
  },
  {
    "id": "IRPT_FNTEND-C-S85",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T11:26:58Z",
    "one_line": "ROUND-4 DISARMS CHECKED: C-S56's two named conditions are met and C-S67's second branch is met in substance -- both DISMISSED; the exposure they guarded is not closed and is carried ARMED as S61 (C-S84).",
    "class": "OBSERVATION",
    "spec_asserts": "C-S56 DISARMS when the placeholders reader is line-anchored in BOTH readers in one change and the count bar refuses a PASS beside a contradicting summary. C-S67 DISARMS when the portal suite can observe a mount, or when the cut-time refusal of seeded criteria becomes a gate limb.",
    "world_is": "C-S56: 9e6ed6c236 line-anchors PLACEHOLDERS_TAG_RE in both proof-of-spec-check.py and to-pipeline-gate.py in one change, and limb 2 (count_bar_check) refuses a PASS beside a contradicting summary -- F29's batteries, and this seat's self-test runs at HEAD 26774b2cdc (32 of 32; 0 of 70 failed). C-S67: seeded criteria are refused by an instrument, drives_check (proof-of-spec-check.py:1712, wired at :2069) -- at the complete flip, not at the cut, and the portal still installs no DOM environment. Both limbs' NEW/LEGACY boundary is readable from the instance the graded worker writes (S61).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-29.checker-limbs.proof_of_spec.json@6ad371c88e",
        ".tools/proof-of-spec-check.py@9e6ed6c236 :1712, :2069",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND5_L8_L9_20260914.md@366a0b4103 section 4"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-C-S56",
      "IRPT_FNTEND-C-S67"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The conditions C-S56 and C-S67 named are met as written, so neither stays open as its own hazard. What they protected is not yet safe: limbs 2 and 3 can be moved to LEGACY by the graded party, and that hazard is carried ARMED on S61 under 1.0.0_SA_CTO (C-S84) rather than left on these two rows.",
    "hazard_standing": "INERT"
  },
  {
    "id": "IRPT_FNTEND-C-S86",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T12:16:37Z",
    "one_line": "W4-S9 REMEDIATED: CLAUDE.md Rule 27's L4-R clause now quotes to-pipeline-gate.py's _newly_added docstring as the source reads it (law edit 727c4e7c2b), so W4-S9's latest disposition moves from C-S84's GRADUATED to this row. C-S84 stands for S61, W4-S11 and W4-S12.",
    "class": "OBSERVATION",
    "spec_asserts": "C-S84 (d50d0e6d87): CLAUDE.md:42 quotes 'A modification (M) does not: this gate never refuses an existing TO' while .tools/to-pipeline-gate.py:1706 reads 'A modification (M) does not: no limb that reads THIS set refuses an existing TO'.",
    "world_is": "At 727c4e7c2b (1.0.0_SA_CTO, law(CLAUDE.md Rule 27), broadcast 96589), CLAUDE.md:42 reads '... A modification (M) does not: no limb that reads' and continues with 'THIS set refuses an existing TO.' -- the same sentence as .tools/to-pipeline-gate.py:1706. The clause now cites the docstring at :1702-1710 @942e4ff992 and names GATE (viii) as its one exception. Read at HEAD by this seat with a line search of both files; no rule changed (96589).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CLAUDE.md:42 @727c4e7c2b",
        ".tools/to-pipeline-gate.py:1706 @727c4e7c2b",
        "msg 96589 (the law edit's same-turn broadcast)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W4-S9"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Remediated at 727c4e7c2b: the law quotes its source verbatim again, and the two lines were read equal at HEAD. Nothing else in C-S84 moves: S61 stays ARMED under 1.0.0_SA_CTO, and W4-S11 and W4-S12 stay GRADUATED.",
    "hazard_standing": "INERT"
  }
]
```

## Round 6 -- L8 compile and L9 adjudication (3.0.0_SA_CVO, 2026-09-14T19:48:12Z)

The 21 rows carrier-less at round 6's L8 (INVESTIGATION_v2.md @a72fa41d54; issuance 79b2ddf558), carried by C-S87..C-S92. Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md`.

```json
[
 {
  "id": "IRPT_FNTEND-C-S87",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T19:48:12Z",
  "one_line": "ROUND-6 L9 GRADE RECORD: the five JUDGMENT verdicts, one per order, bound to each proof instance at its commit -- 4 PASS (3 with a named qualification) and 1 FAIL, F39-AC10 at the DirectoryEntry use site (row W3-S29).",
  "class": "OBSERVATION",
  "spec_asserts": "Spine L9: a JUDGMENT criterion is graded by the CVO against the specification that issued it and never self-graded; its verdict lives in `grades` on a row of the CVO's.",
  "world_is": "5 of 5 round-6 judgment rows read UNVERIFIABLE-BY-INSTRUMENT naming this seat. Evidence and this seat's own runs and reads are in the record, section 3. Vocabulary: MET -> PASS; MET WITH A NAMED QUALIFICATION -> PASS with the qualification in `reason`; NOT MET -> FAIL.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-37.governing-order-binding.proof_of_spec.json@1f42c5bc14",
    "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-38.one-server-per-worktree.proof_of_spec.json@80de3054cf",
    "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-39.adapter-states-what-the-document-states.proof_of_spec.json@9ba2416ca7",
    "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-40.trading-day-window-and-named-codes.proof_of_spec.json@dfb15b3cf3",
    "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~5/IRPT_FNTEND.TO-FE-s-41.one-writer-per-map.proof_of_spec.json@9be439f616",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md (same slug) section 3"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade record: it adjudicates no item and opens nothing. The FAIL's defect is W3-S29 (C-S92); each qualification is carried by the row it names.",
  "hazard_standing": "INERT",
  "grades": [
   {
    "criterion": "F37-AC9",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-37.governing-order-binding.proof_of_spec.json@1f42c5bc14",
    "verdict": "PASS",
    "reason": "MET WITH A NAMED QUALIFICATION -- F29-AC15 clause 3 re-graded on this instance under RULING S, whose scope is the flip. This seat's own three-arm run of .tools/proof-of-spec-check.py at HEAD on FE-s-29's instance, in a workspace .scratch copy (removed after): (A) committed instance --governing-order TO-FE-s-29 -> VALID rc=0; (B) to_ref doctored to TO-FE-s-28, --governing-order TO-FE-s-29 -> INVALID rc=1, 'VIOLATION: governing-binding: the order being flipped is ...TO-FE-s-29... but the instance's decomp_ref.to_ref names ...TO-FE-s-28... -- REFUSED before any limb runs', with the count-bar and drives frames reading TO-FE-s-29 (NEW); (C) the same doctored instance UNBOUND -> the frames read TO-FE-s-28 (count-bar mode ANNOUNCE; drives 8 of 8 NEITHER), i.e. steered. The flip path is bound: to-pipeline-gate.py:2543 runs the checker with '--governing-order', rel, and its self-test arm :865 asserts it. QUALIFICATION: every unbound caller is still steerable -- receiving-check.py's L7->L8 route and this seat's own intake/audit scripts (row W4-S14, graduated in C-S90); an instance edited after its flip never reaches the bound path. Arms B and C also carry an artifact-resolution violation that is an artifact of the scratch copy (PENDING-THIS-COMMIT), orthogonal to the binding."
   },
   {
    "criterion": "F38-AC9",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-38.one-server-per-worktree.proof_of_spec.json@80de3054cf",
    "verdict": "PASS",
    "reason": "MET WITH A NAMED QUALIFICATION. Every browser verdict names its server: at portal DEV 35797660, 8 files carry preconditionLine / 'PRECONDITION: dev server' -- the helper fe-s-27/_dev-server.ts, its own precondition test, and the six consumers fe-s-19, fe-s-30, fe-s-31, fe-s-32, fe-s-38, fe-s-40 -- and the set of files importing _dev-server minus the set carrying preconditionLine/skipNotice is EMPTY. F35's 'never seen mounted' is decided by AC5 and AC6 on the worker's own server: F19-AC4 'BODIES MOUNTED: 2 of 2' and F19-AC5 '2 of 2', PAGE CRASHES 0. QUALIFICATION: this seat's instrument is a source census at DEV, not a browser re-run; RULING U's isolation limb keeps three residuals (W1-S63 the vite-temp junction write, W1-S64 a stale comment, W1-S65 two surviving per-cell cacheDir overrides), graduated in C-S91."
   },
   {
    "criterion": "F39-AC10",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-39.adapter-states-what-the-document-states.proof_of_spec.json@9ba2416ca7",
    "verdict": "FAIL",
    "reason": "NOT MET at one of the two use sites the order itself names. The criterion: 'nothing the adapter hands the view says more, or less, than the document did'. At portal DEV 35797660, contracts/adapt.ts:466 hands the Holdings view an out-of-enum advisory_status as { outOfEnum: token } (verbatim, flagged -- F39-AC6 3 of 3, F32-AC5 6 of 6 in a browser), but adapt.ts:585 still reads 'value: ADVISORY_FOR_WIRE[wire.cohort.advisory_status] ?? \"unknown\"' for the DirectoryEntry cohort -- the same rename to 'unknown' RULING W forbids, at the site W2-S29 named (:558 at the cut). The worker's own record says 'STILL LESS THAN THE DOCUMENT'. Named: the cut's grant did not reach it (CohortValue is shared by three axes; ScopeSummary.tsx was not granted), no emitter sends an out-of-enum directory advisory today, and validate.ts:167 checks cohort values against the closed list. The defect is row W3-S29, graduated in C-S92 for the recut."
   },
   {
    "criterion": "F40-AC10",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-40.trading-day-window-and-named-codes.proof_of_spec.json@dfb15b3cf3",
    "verdict": "PASS",
    "reason": "MET. Read from the re-capture deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-40_print_frozen_as_committed_1440.png (3 pages, viewed): the print no longer contradicts itself about its window -- page 1 'Period answered by the source 2026-01-02 to 2026-09-09'; page 3 Limitations 'Requested window 2026-01-01 to 2026-09-09 / Answered window 2026-01-02 to 2026-09-09' and 'The requested and answered dates differ only by days the market was closed (NYSE trading calendar (lib/trading_calendar.py)): ... the first trading day on or after either is 2026-01-02', beside 'The source answered the requested window'. A flagged code reads as flagged on all three bands ('Reason: REQUESTED_WINDOW_ANSWERED [code not defined by the v1 contract]') and in Report availability."
   },
   {
    "criterion": "F41-AC8",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~5/IRPT_FNTEND.TO-FE-s-41.one-writer-per-map.proof_of_spec.json@9be439f616",
    "verdict": "PASS",
    "reason": "MET WITH A NAMED QUALIFICATION. One writer: at portal DEV 35797660 the only writeFileSync of fe-s-14-global.json is __tests__/fe-s-14/gen-maps.ts:147; every other hit is a comment, the TARGET constant or a seeded negative-control .txt. The narrative speaks for its report: in fe-s-18-frozen.json the narrative's performance_revision.performance_report_revision is rev-49f-000091, equal to its own performance member's status.operation.revision rev-49f-000091; and 5 of 5 descendants (frozen, the three Holdings bases, fe-s-32/holdings-no-answer.json) read rev-49f-000091 x3 and perf-9 x0 as COMMITTED blobs (git show at DEV) -- a different instrument than the worker's working-copy read. QUALIFICATION: the second-writer census was run on the Global map only; the other five maps' single writer rests on gen-fixtures.ts's own output list. F41-AC5 still reads the working copy (W5-S7, graduated in C-S90)."
   }
  ]
 },
 {
  "id": "IRPT_FNTEND-C-S88",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T19:48:12Z",
  "one_line": "ROUND-6 L9: six rows CLOSED IN DRAINED CODE, each read at portal DEV 35797660 and QUOTED, not echoed -- the four BLOCKING/ARMED rows (W3-S27, W3-S28, W5-S5, S64) and their two resolution records (S63, S65). REMEDIATED and DISARMED by their owner inside the round.",
  "class": "OBSERVATION",
  "spec_asserts": "Each ARMED row names 2.0.0_SA_COO~F as disarm owner, to disarm when the amended cell drains green: W3-S27 and W3-S28 by FE-s-39 amendment 1, W5-S5 by FE-s-41 amendment 1, S64 by FE-s-41 amendment 2.",
  "world_is": "W3-S27: fe-s-34/no-status.test.ts:268-273 'Path 1's NULL arm (the VIEW plane) now expects an absence wording OTHER than SOURCE_DATE_MALFORMED. Path 2's NULL arm (the WIRE plane) is unchanged', with the negative control :297 'expect(viewNullNamed(SOURCE_DATE_MALFORMED)).toBe(false)'. W3-S28: fe-s-32/holdings-in-a-browser.test.ts:56 imports ADVISORY_OUT_OF_ENUM_WORDS (one rule, no second copy) and :424 accepts the verbatim-flagged token while the same token unflagged is rejected. W5-S5: fe-s-32/holdings-no-answer.json reads perf-9 x0 and rev-49f-000091 x3, and is now WRITTEN by fe-s-18/gen-fixtures.ts:463. S64: fe-s-41/one-writer.test.ts:104-107 committedBlob = 'git cat-file blob HEAD:<path>', F41-AC4 compares the regenerated map with that blob (:570-580), and the CONTROL renders the committed map CRLF in memory and requires not-equal (:620-623). S63 and S65 are the owner's resolution records; their claims match the code read here.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W3-S27",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W3-S28",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W5-S5",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-S64",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-S63",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-S65",
    "portal DEV 35797660 (LOCAL): the four test/fixture files cited, read with git show",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W3-S27",
   "IRPT_FNTEND-W3-S28",
   "IRPT_FNTEND-W5-S5",
   "IRPT_FNTEND-S64",
   "IRPT_FNTEND-S63",
   "IRPT_FNTEND-S65"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Closed in drained code by the owner's amendments (FE-s-39 a1 @0294183b65; FE-s-41 a1 @069344053b, a2 @78b011df6a), each read and quoted at DEV 35797660 by this seat. The four ARMED rows are DISARMED; the two records are verified. The issuer's cut-reach and verification misses they record are carried as a class in the slug, not re-opened.",
  "hazard_standing": "INERT"
 },
 {
  "id": "IRPT_FNTEND-C-S89",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T19:48:12Z",
  "one_line": "ROUND-6 L9: five rows ACCEPTED as records or stated readings -- W4-S13 (to_id slug-tolerant, to_ref exact), W3-S32 (one import line to keep one rule), W5-S6 (out-of-grant generator outputs byte-identical, none staged), W1-S66 (closed-port timing is per instrument) and W2-S32 (the reason-code set's home; its remedy is IRPT_BCKEND's).",
  "class": "OBSERVATION",
  "spec_asserts": "Each row states a reading the order left open or a boundary the worker kept; none claims a defect in this project's drained code that this project's chain can remedy.",
  "world_is": "W4-S13: the binding compares to_ref exactly and to_id slug-tolerantly; this seat's F37 run (arm B) confirms the governing order now comes from --governing-order, so neither field steers a limb. W3-S32: the diff touches only the import line and CLAIM_READERS.classification; a typed copy of the flag's words would be the second copy the order forbids. W5-S6: 4 of 4 out-of-grant outputs byte-identical to HEAD and unstaged -- a boundary kept, flagged for any future generator change. W1-S66: measured by this seat 2026-09-14 -- python blocking socket.create_connection refuses a closed loopback port after ~2.03 s (localhost ~4.1 s), node net.connect in 1-6 ms; the order's BOUNDS and the probe's comment generalise one instrument, and the 4000 ms bound exceeds both, so no verdict moves. W2-S32: the portal carries the generated set with a stated admission rule and a test that re-reads the contract; the contract naming its codes is IRPT_BCKEND's (round-5 analysis s.6; IRPT_BCKEND-S52).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W4-S13",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W3-S32",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W5-S6",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W1-S66",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W2-S32",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND5_20260914.md@942e4ff992 RULING T (the contract must name every window reason code; carried to IRPT_BCKEND)",
    "C:/Users/AndrewBerman/.claude/projects/C--Users-AndrewBerman-Desktop-ajb-workspace/memory/reference_closed_loopback_port_times_out_on_this_box_use_the_port_table.md (this seat's two-instrument measurement, 2026-09-14; outside the repo, no commit)"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W4-S13",
   "IRPT_FNTEND-W3-S32",
   "IRPT_FNTEND-W5-S6",
   "IRPT_FNTEND-W1-S66",
   "IRPT_FNTEND-W2-S32"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Accepted: each is a stated reading or a kept boundary, verified here. W2-S32's remedy lies outside this project's chain -- the contract's reason-code list is IRPT_BCKEND's, per the round-5 analysis s.6 and IRPT_BCKEND-S52 -- so it is not recut here.",
  "hazard_standing": "INERT"
 },
 {
  "id": "IRPT_FNTEND-C-S90",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T19:48:12Z",
  "one_line": "ROUND-6 L9, GRADUATED -- THE CHECKER'S REACH: the flip is bound, but every other caller runs the checker unbound (W4-S14, including this seat's own intake/audit scripts), a checker battery outside .tools/tests/ is red at the cut (W4-S15, 3/6, pre-existing), and F41-AC5 reads the working copy where its criterion says committed (W5-S7).",
  "class": "OBSERVATION",
  "spec_asserts": "RULING S: 'the governing order is the order being flipped, never a field the worker writes'; F41-AC5: 'read from the committed frozen map'.",
  "world_is": "W4-S14: .tools/receiving-check.py:71/:117 and five CVO scripts pass the instance alone; this seat's arm C shows an unbound run is steered by to_ref. W4-S15: org/standards/test_artifact_coverage_both_grammars.py reads 3/6 PASS, rc=1, at the cut and with FE-s-37 applied -- the failing arms are its must-VALID fixtures. W5-S7: fe-s-41/one-writer.test.ts reads the five maps with loadJson of the checkout (:71-73, :600 at 87f83b86); no checkout turns it red, but an uncommitted in-place edit is graded as committed.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W4-S14",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W4-S15",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W5-S7",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W4-S14",
   "IRPT_FNTEND-W4-S15",
   "IRPT_FNTEND-W5-S7"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "IRPT_FNTEND-C-S91",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T19:48:12Z",
  "one_line": "ROUND-6 L9, GRADUATED -- RULING U'S RESIDUALS: vite's config loader still writes a transient temp file through the node_modules junction (W1-S63), a comment misdescribes the helper's port rule (W1-S64), and two per-cell overrides still redirect cacheDir into the workspace .scratch (W1-S65).",
  "class": "OBSERVATION",
  "spec_asserts": "RULING U: 'vite's cacheDir and tsbuildinfo live inside the worktree by config, never through the junction, so no cell needs a per-cell override again'.",
  "world_is": "W1-S63: vite 7.3.5's bundle loader writes <config>.timestamp-*.mjs under the junction's .vite-temp and unlinks it after import (config.js:35985-35993); uniquely named, so no worktree reads another's; the runner loader fails on __dirname. W1-S64: fe-s-19/mounted-from-wire.test.ts:55-56 says 'documented default second', which the helper no longer has. W1-S65: fe-s-31/vite.worktree.config.mjs:39 and fe-s-32/vite.worktree.config.ts:50 merge cacheDir onto .scratch/vite-cache-fe-s-3x.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W1-S63",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W1-S64",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W1-S65",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W1-S63",
   "IRPT_FNTEND-W1-S64",
   "IRPT_FNTEND-W1-S65"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "IRPT_FNTEND-C-S92",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-14T19:48:12Z",
  "one_line": "ROUND-6 L9, GRADUATED -- THE ADAPTER AND SURFACE GAPS: the DirectoryEntry cohort still renames an out-of-enum advisory to 'unknown' (W3-S29, the F39-AC10 FAIL), validate.ts still pins advisory to three values (W3-S30), one export screen can show one code flagged and bare (W2-S33), and fe-s-32's browser test rewrites another worker's committed captures on every run (W3-S31).",
  "class": "OBSERVATION",
  "spec_asserts": "RULING W: 'an out-of-enum value on a READY answer is shown verbatim and flagged, never as \"unknown\"'; F39-AC10: 'nothing the adapter hands the view says more, or less, than the document did'.",
  "world_is": "W3-S29: contracts/adapt.ts:585 at DEV 35797660 'ADVISORY_FOR_WIRE[wire.cohort.advisory_status] ?? \"unknown\"' (CohortValue shared by three axes; ScopeSummary.tsx ungranted); no emitter today. W3-S30: contracts/validate.ts:448 oneOf advisory ['advised','residual','unknown'], one importer. W2-S33: export/ReceiptPanel.tsx:44-48 renders StatusPanel (flagging) beside its own unflagged 'Reason:' line. W3-S31: fe-s-32/holdings-in-a-browser.test.ts:68 CAPTURES = deliverables/0.9.0_WK_IRPT_FNTEND~2/, rewritten by any run.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W3-S29",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W3-S30",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W2-S33",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@a72fa41d54#IRPT_FNTEND-W3-S31",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W3-S29",
   "IRPT_FNTEND-W3-S30",
   "IRPT_FNTEND-W2-S33",
   "IRPT_FNTEND-W3-S31"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 }
]
```

## Round 7 -- L8 compile and L9 adjudication (3.0.0_SA_CVO, 2026-09-15T02:21:10Z)

The 10 rows carrier-less at round 7's L8 (INVESTIGATION_v2.md @32855486f0; issuance bc47ca11a3), carried by C-S93..C-S98. Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND7_L8_L9_20260915.md`.

```json
[
 {
  "id": "IRPT_FNTEND-C-S93",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T02:21:10Z",
  "one_line": "ROUND-7 L9 GRADE RECORD: the four JUDGMENT verdicts, one per order, bound to each proof instance at its commit -- 4 PASS, 3 of them with a named qualification (F42-AC10, F43-AC9, F45-AC8) and F44-AC7 MET.",
  "class": "OBSERVATION",
  "spec_asserts": "Spine L9: a JUDGMENT criterion is graded by the CVO against the specification that issued it and never self-graded; its verdict lives in `grades` on a row of the CVO's.",
  "world_is": "4 of 4 round-7 judgment rows read UNVERIFIABLE-BY-INSTRUMENT naming this seat. proof-of-spec-check.py, run by this seat on the shared tree with --governing-order <each order>, reads VALID rc=0 on 4 of 4 instances. Evidence and this seat's own runs and reads are in the record, section 3. Vocabulary as round 6: MET -> PASS; MET WITH A NAMED QUALIFICATION -> PASS with the qualification in `reason`; NOT MET -> FAIL.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-42.advisory-verbatim-at-every-site.proof_of_spec.json@f91fba582c",
    "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-43.receiving-route-binds-the-order.proof_of_spec.json@33ea27ab7a",
    "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~6/IRPT_FNTEND.TO-FE-s-44.artifact-coverage-battery-current.proof_of_spec.json@5d25cd5028",
    "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-45.dev-server-residuals-and-committed-reads.proof_of_spec.json@3e48518ae9",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND7_L8_L9_20260915.md (same slug) section 3"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade record: it adjudicates no item and opens nothing. Each qualification is carried by the row it names (W1-S69, W4-S16) or stated in its reason for the CTO's analysis.",
  "hazard_standing": "INERT",
  "grades": [
   {
    "criterion": "F42-AC10",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-42.advisory-verbatim-at-every-site.proof_of_spec.json@f91fba582c",
    "verdict": "PASS",
    "reason": "MET WITH A NAMED QUALIFICATION. RULING Z's bar: 'an out-of-enum advisory at every use site is shown verbatim and flagged; F39-AC10's clause is re-graded at the directory site'. Read by this seat at portal DEV 1f3ce9f0 (LOCAL; PORTAL FROZEN, read by git show): the directory cohort now reads advisoryFromWire(wire.cohort.advisory_status) (contracts/adapt.ts:588), which returns { outOfEnum: token } for a token outside the table (:466) -- the round-6 '?? \"unknown\"' rename is gone, so F39-AC10's clause is MET at the directory site. The header renders the flagged shape verbatim with the flag (header/ScopeSummary.tsx:34, isOutOfEnumAdvisory); validate admits the flagged shape on the advisory axis only (contracts/validate.ts:186); ReceiptPanel's Reason line carries the one flag rule (export/ReceiptPanel.tsx:54); fe-s-32's browser test no longer writes ~2's committed captures (const CAPTURES = captureDestination(SCRATCH + 'captures/')). QUALIFICATION: a NON-authoritative cohort still renders every axis as '<axis>: unknown' under 'Cohort (not asserted)' (ScopeSummary.tsx:118) whatever its value -- a withholding gate the worker disclosed, the same gate Holdings applies, not a rename; RULING W's 'never as \"unknown\"' does not carve it out in words, so whether a withheld value should read 'withheld' is the CTO's to rule. Instrument: a source read at DEV, not a browser re-run."
   },
   {
    "criterion": "F43-AC9",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-43.receiving-route-binds-the-order.proof_of_spec.json@33ea27ab7a",
    "verdict": "PASS",
    "reason": "MET WITH A NAMED QUALIFICATION. RULING AA: 'the receiving seat passes the order it is handed, and the route hands it on as --governing-order; an unbound call reads NOT-BOUND, never VALID'. EXERCISED by this seat on the SHARED tree at HEAD 78ba3385aa (not the worker's worktree): python .tools/tests/test_receiving_binding.py -> 'receiving-binding battery: 11 of 11 arm(s) as expected'; committed+bound ACCEPT; doctored to_ref bound -> HAND BACK, 'THE HAND-BACK NAMES BOTH PATHS: yes'; unbound -> 'NOT-BOUND ... the checker ran: no'; BEFORE arm (receiving-check @edac45e48c) ACCEPTS the same doctored instance, so the arm discriminates. QUALIFICATION: the canonical-flow skill still documents the one-argument call and three verdicts (SKILL.md:353, :368 at HEAD; row W4-S16, graduated) -- fail-closed, a seat following it reads NOT-BOUND, never a false ACCEPT."
   },
   {
    "criterion": "F44-AC7",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~6/IRPT_FNTEND.TO-FE-s-44.artifact-coverage-battery-current.proof_of_spec.json@5d25cd5028",
    "verdict": "PASS",
    "reason": "MET. The limb is named and read by this seat: .tools/proof-of-spec-check.py:339 @4d11c008c2 'artifact-resolution/CHECKER-SCOPE: this proof-of-spec-check lives in ... OUTSIDE that tree -- it cannot resolve the instance's commit and CANNOT GRADE IT'. The wrong side is the battery (it wrote instances to the OS temp dir); the checker blob is unchanged, 7e324c78c2 at 4d11c008c2 and at HEAD. The diagnosis (95f7fde99e, 18:30 local) precedes the fix (051379eac7, 18:48). The battery now writes inside the tree (org/standards/test_artifact_coverage_both_grammars.py:20, :163). EXERCISED by this seat on the shared tree at HEAD: 'ARTIFACT-COVERAGE BATTERY: 6/6 PASS (denominator 6)', 'CONTROLS FAIL FOR THEIR NAMED VIOLATION: 3 of 3', 'WITH THE COVERAGE RULE DISABLED IN A SCRATCH COPY, THE CONTROLS CATCH IT: yes' -- it discriminates again."
   },
   {
    "criterion": "F45-AC8",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-45.dev-server-residuals-and-committed-reads.proof_of_spec.json@3e48518ae9",
    "verdict": "PASS",
    "reason": "MET WITH A NAMED QUALIFICATION. 'RULING U leaves no residual, and F41-AC5 grades what is committed.' Read by this seat at portal DEV 1f3ce9f0 (LOCAL; PORTAL FROZEN, read by git show) against the CTO's adjudication @46664e15f4 s.3-4: all 3 config-loading scripts take the runner loader (package.json:13 dev, :14 build, :17 preview); vite.config.ts names no __dirname and derives its directory with fileURLToPath at ::14,:17; fe-s-38/resolve-config.mjs:64 loads with configLoader 'runner', the dev script's own loader (W1-S68); both per-cell overrides (fe-s-32, fe-s-39) are absent (W1-S65); fe-s-19 no longer says 'documented default' (W1-S64). F41-AC5 reads 'git cat-file blob HEAD:<path>' (fe-s-41/one-writer.test.ts::105,:715). QUALIFICATIONS: (1) the zero .vite-temp writes (4 of 4 kept loaders), the /api 401-vs-401 control and the build's dist-manifest equality (73 of 73) are the worker's runs and the issuer's untouched-pair re-run, NOT re-run by this seat -- a dev start writes into the main checkout's node_modules and the portal is frozen; (2) the runtime bar is met only by the test's added discriminator (listener node.exe, no process.versions.bun, a bun negative control): the field the cut and bar 2 name reads 'node' under bun too (row W1-S69, graduated)."
   }
  ]
 },
 {
  "id": "IRPT_FNTEND-C-S94",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T02:21:10Z",
  "one_line": "ROUND-7 L9: three FE-s-45 rows DISMISSED_WITH_REASON, each closed in drained code or a correction record -- W1-S67 (the dev line alone cannot stop the write; superseded by amendment 1 on RULING (B)), W1-S68 (resolve-config.mjs on the bundle loader; now runner) and W1-S70 (S67's cost 3 corrected from vite's source).",
  "class": "OBSERVATION",
  "spec_asserts": "RULING U's residuals (round-6 analysis s.3 @4713211d87) and the CTO's RULING (B) (@46664e15f4 s.2-3): the config-loading scripts and every kept programmatic loader take the runner loader, with fileURLToPath at vite.config.ts's former __dirname sites; resolve-config.mjs loads with the dev script's own loader.",
  "world_is": "Read by this seat at portal DEV 1f3ce9f0 (LOCAL; PORTAL FROZEN, read by git show): package.json:13/14/17 carry '--configLoader runner'; vite.config.ts has no __dirname and fileURLToPath at :14,:17; fe-s-38/resolve-config.mjs:64 configLoader 'runner'. W1-S67's premise (the dev line as the one lever) is the one the CTO's adjudication corrected and amendment 1 (@5061bc8421) replaced; its cost (1), the runtime moved to bun, is reverted: the dev server runs on node (F45-AC10). W1-S70 is a source reading (vite 7.3.5 config.js:26032-26033, isConfig) that corrects S67's cost (3): an edit to vite.config.ts restarts the server whatever the loader's dependency list holds. NOTE FOR THE ANALYSIS: the CTO's s.5 rejection of (A) lists 'an edit to vite.config.ts stops restarting the server', which rests on S67's cost (3); W1-S70 removes that one reason. The ruling stands on its other two (every dev user's runtime moved off node; proxies never exercised under bun).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0#IRPT_FNTEND-W1-S67",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0#IRPT_FNTEND-W1-S68",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0#IRPT_FNTEND-W1-S70",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_IRPT_FNTEND_20260914T2350Z.md@46664e15f4 s.2, s.3, s.5",
    "portal 1f3ce9f0: package.json, vite.config.ts, src/pages/InvestorReporting/__tests__/fe-s-38/resolve-config.mjs",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND7_L8_L9_20260915.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W1-S67",
   "IRPT_FNTEND-W1-S68",
   "IRPT_FNTEND-W1-S70"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "W1-S67 and W1-S68 are closed in drained code at portal DEV 1f3ce9f0 under amendment 1 (RULING (B)); W1-S70 is a correction record to W1-S67 and moves no verdict. Its bearing on the CTO's s.5 reasoning is carried in the slug, not as a remedy.",
  "hazard_standing": "INERT"
 },
 {
  "id": "IRPT_FNTEND-C-S95",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T02:21:10Z",
  "one_line": "ROUND-7 L9: two rows ACCEPTED as records -- W3-S34 (RULING X's three granted tests went unused because none of their claims changed) and W4-S17 (the receiving reporter wraps long owning-tool lines instead of cutting at 150 characters, inside FE-s-43's grant).",
  "class": "OBSERVATION",
  "spec_asserts": "Each row states a grant that went unused or a change inside the order's own <paths>; neither claims a defect this project's chain must remedy.",
  "world_is": "W3-S34: the three tests assert values RULING Z's changes do not reach; the worker's census of record at portal e028fb4d read 553 pass, 18 skip, 0 fail of 571, and the issuer's re-run matched. W4-S17: .tools/receiving-check.py is inside FE-s-43's <paths>; the wrap was needed for F43-AC4 to print both paths, and this seat's re-run of the battery on the shared tree reads 'THE HAND-BACK NAMES BOTH PATHS: yes', with every other route's classification and argv unchanged, 5 of 5 (F43-AC7).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0#IRPT_FNTEND-W3-S34",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0#IRPT_FNTEND-W4-S17",
    "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-43.receiving-route-binds-the-order.md@33ea27ab7a <paths>",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND7_L8_L9_20260915.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W3-S34",
   "IRPT_FNTEND-W4-S17"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Records: an unused grant and a reporter change inside the granted tool, both verified. Nothing to remedy.",
  "hazard_standing": "INERT"
 },
 {
  "id": "IRPT_FNTEND-C-S96",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T02:21:10Z",
  "one_line": "ROUND-7 L9, GRADUATED -- INSTRUMENTS THAT CANNOT SEPARATE THE CAUSE: a named runtime field that reads 'node' under bun too (W1-S69, F45-AC10's clause and the CTO's bar 2), two tests whose 5000 ms default times out on a loaded box (W3-S33), and a census whose 560 s bound prints a load timeout as RED in a regression's row shape (W6-S1).",
  "class": "OBSERVATION",
  "spec_asserts": "F45-AC10: 'the dev script's server reports process.release.name = node'; CTO adjudication @46664e15f4 s.4 bar 2: 'prints process.release.name or an equivalent reading node'. F42-AC9 and F44-AC5: the whole-suite census of record reads 0 fail / every battery green. CLAUDE.md Rule 22: DISCRIMINATION -- could the evidence differ if the claim were false?",
  "world_is": "W1-S69: bun 1.3.9 reports process.release.name 'node' as node does; F45-AC10 was met only by the test's added discriminator (listener image node.exe, no process.versions.bun, a bun negative control reading bun.exe). W3-S33: at base 4d11c008c2 the suite read 2 fail, both 5000 ms timeouts outside the grant (F40-AC5 and F41-AC2); F40-AC5 timed out again alone at 5735 ms; the census of record read 0 fail. W6-S1: .tools/tests/test_governing_binding.py's 560 s per-battery bound (:272 @4d11c008c2) turned test_seeded_limb.py RED rc=124 under load, 275 s alone; the summary row shape does not separate load from regression.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0#IRPT_FNTEND-W1-S69",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0#IRPT_FNTEND-W3-S33",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0#IRPT_FNTEND-W6-S1",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND7_L8_L9_20260915.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W1-S69",
   "IRPT_FNTEND-W3-S33",
   "IRPT_FNTEND-W6-S1"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "IRPT_FNTEND-C-S97",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T02:21:10Z",
  "one_line": "ROUND-7 L9, GRADUATED -- THE NO-STATUS DIRECTORY PATH: a v1 directory-search body with no status member, run through the real adapter, becomes a DirectoryEntry the portal's own validator refuses (W3-S35); the adapter's explicit unknown and validate's availability rule disagree on the common path.",
  "class": "OBSERVATION",
  "spec_asserts": "contracts/envelope.ts:225-232 @35797660: a response with no status gets the explicit unknown, never READY. contracts/validate.ts:76 @35797660: 'A non-READY state without a reason is a payload a screen cannot explain.'",
  "world_is": "contracts/adapt.ts EXPLICIT_UNKNOWN_STATE = 'UNCERTAIN' with partialReason and publicReasonCode null; validateContract('DirectoryEntry', ...) on that document reports 'availability: state UNCERTAIN carries NEITHER partialReason NOR publicReasonCode'. status is optional on this route. Whether any production path runs validateContract on an adapted document was NOT read by the worker or by this seat.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0#IRPT_FNTEND-W3-S35",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND7_L8_L9_20260915.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W3-S35"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "IRPT_FNTEND-C-S98",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T02:21:10Z",
  "one_line": "ROUND-7 L9, GRADUATED -- THE CANONICAL-FLOW SKILL IS STALE AFTER FE-s-43: it still documents the one-argument receiving call and three verdicts (W4-S16), so a seat following it on a proof-of-spec instance reads NOT-BOUND (fail-closed, INERT).",
  "class": "OBSERVATION",
  "spec_asserts": "RULING AA: 'an unbound call reads NOT-BOUND, never VALID'; FE-s-43 BOUNDS: the skill's exact change goes to that skill's owner in one row.",
  "world_is": "At HEAD 3e8cf9e288, .claude/skills/canonical-flow/SKILL.md:353 reads '.tools/receiving-check.py <the artifact your limb consumes>' and :368 'THE THREE VERDICTS'. Owner by census: 13 of 18 commits on the file are 1.0.0_SA_CTO or its lane 1.0.0_SA_CTO~Z. The exact three-edit change is in the row.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@32855486f0#IRPT_FNTEND-W4-S16",
    ".claude/skills/canonical-flow/SKILL.md@2981c4bd72 :353, :368",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND7_L8_L9_20260915.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W4-S16"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 }
]
```

## Round 8 -- L8 compile and L9 adjudication (3.0.0_SA_CVO, 2026-09-15T09:42:39Z)

The 18 rows carrier-less at round 8's L8 (INVESTIGATION_v2.md @5e5f074588; issuance 57cb17e329), carried by C-S99..C-S107. Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md`.

```json
[
 {
  "id": "IRPT_FNTEND-C-S99",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T09:42:39Z",
  "one_line": "ROUND-8 L9 GRADE RECORD: the four JUDGMENT verdicts, one per order, bound to each proof instance at its commit -- 4 PASS, each with a named qualification; F49-AC15's names the backend-wall answer: the portal gate is the only admin wall.",
  "class": "OBSERVATION",
  "spec_asserts": "Spine L9: a JUDGMENT criterion is graded by the CVO against the specification that issued it and never self-graded; its verdict lives in `grades` on a row of the CVO's.",
  "world_is": "4 of 4 round-8 judgment rows read UNVERIFIABLE-BY-INSTRUMENT naming this seat. proof-of-spec-check.py, run by this seat on the shared tree with --governing-order <each order>, reads VALID on 4 of 4 instances. Evidence and this seat's own reads are in the record, section 3. Vocabulary as rounds 6-7: MET -> PASS; MET WITH A NAMED QUALIFICATION -> PASS with the qualification in `reason`; NOT MET -> FAIL.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-46.per-test-timeouts-sized-to-cost.proof_of_spec.json@1e8997ec6d",
    "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-47.no-status-carries-its-reason.proof_of_spec.json@0a49c55855",
    "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-48.non-authoritative-cohort-reads-withheld.proof_of_spec.json@a42c7e05df",
    "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-49.investor-reporting-opal-admin-only.proof_of_spec.json@a018979694",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 3"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade record: it adjudicates no item and opens nothing. Each qualification is carried by the row it names (W1-S74, W1-S75, W3-S37, W3-S38, W4-S19, W4-S20, S66) or stated in its reason for the CTO's analysis.",
  "hazard_standing": "INERT",
  "grades": [
   {
    "criterion": "F46-AC8",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-46.per-test-timeouts-sized-to-cost.proof_of_spec.json@1e8997ec6d",
    "verdict": "PASS",
    "reason": "MET WITH A NAMED QUALIFICATION. Bar: 'a loaded box can no longer turn a later cell's census red through these two files, and every timeout is sized from a measured cost.' Read by this seat at portal DEV 90d71d9e (LOCAL; PORTAL FROZEN, read by git show): 8 changed timeouts (window:302 17625, one-writer:436 20952, one-writer:452 11013, one-writer:590 20907, one-writer:626 15138, one-writer:764 21000, one-writer:779 19266, one-writer:869 56673), the diff 1f3ce9f0..90d71d9e is 1+7 lines, and the 90000 at one-writer :539 predates the cell. Against the committed ledger (fe-s-46/recorded-costs.json, 24 runs, 16 tests, 707 costs, unchanged at 10c2f07d), 8 of 16 tests have a highest cost >= 2500 ms; 7 timeouts are exactly 3x that cost and F40-AC5's is the order's named floor 3 x 5875 (F41-AC2's control, run B01; timeouts.test.ts:161) against its own highest 5735. All 8 are <= 60000. The census run measures nothing: timeouts.test.ts:66 'const LOAD = env.IRPT_FE_TIMEOUT_LOAD === \"1\"' gates every load arm, and F46-AC6 prints 10 of 10 spawned processes as 8 git reads and 2 seeded scratch runs. QUALIFICATIONS: (1) 'can no longer' is bounded, not absolute: a load that triples a test's highest recorded cost still turns it red; (2) every committed timeout stands on a carried BOOTSTRAP run (B01-B12, 35 costs), not a run of the load path as it now stands, and B03/B04 carry a day-only date (W1-S75); (3) F41-AC5's control has 3327 ms of headroom under the cap, so a committed cost above 20000 ms has no legal timeout (W1-S74's residual; reachable only by an opt-in load run and a commit, never by a census); (4) the same class recurred outside these two files in FE-s-49 (S67). No bun run by this seat: the portal is frozen."
   },
   {
    "criterion": "F47-AC11",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-47.no-status-carries-its-reason.proof_of_spec.json@0a49c55855",
    "verdict": "PASS",
    "reason": "MET WITH A NAMED QUALIFICATION. Bar: 'the adapter supplies the reason on the no-status path, the validator is unchanged, and no stated state carries it.' Read by this seat at portal DEV f28fcc44 (LOCAL; PORTAL FROZEN, read by git show) (identical at 10c2f07d): contracts/adapt.ts:176 NO_STATUS_REASON = 'The response carried no status stating its state, so its state is unknown.'; :307 'partialReason: statedState === null ? (current.partialReason ?? NO_STATUS_REASON) : current.partialReason' -- the reason only when no state is stated, the document's own reason first (amendment 1, 1.0.0_SA_CTO 96947, W3-S39). validate.ts is one blob, 4fc0a042ae9c, at 1f3ce9f0, f28fcc44 and 10c2f07d. The worker's arms: 18 of 18 (operation, trigger) and 11 of 11 stated-state arms held. QUALIFICATION: two paths the grant excluded stay for the round-8 analysis, as amendment 1 routed them: a status member with no state keeps a reasonless default on its own availability (W3-S37), and status-summary/status-job now carry the reason on a document whose data says PARTIAL (W3-S38). Both graduated."
   },
   {
    "criterion": "F48-AC7",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-48.non-authoritative-cohort-reads-withheld.proof_of_spec.json@a42c7e05df",
    "verdict": "PASS",
    "reason": "MET WITH A NAMED QUALIFICATION. Bar: 'a cohort value the panel declines to assert reads \"withheld\" at every render site, never \"unknown\", and a value the producer asserted is unchanged.' Read by this seat at portal DEV ad732941 (LOCAL; PORTAL FROZEN, read by git show) (identical at 10c2f07d): header/ScopeSummary.tsx:120 is the one render site of a non-authoritative CohortFact and builds '${c.axis}: withheld' under 'Cohort (not asserted)'; the worker's census (F48-AC5) finds 1 site, and F48-AC3 holds the asserted path byte-identical to 1f3ce9f0 with a producer's own UNKNOWN still reading 'advisory: unknown'. QUALIFICATION: one surface over, Holdings still renders a non-authoritative classification's partitions as 'unknown' (tabs/holdings/slices.ts:102 at 10c2f07d), by the contract's own comment. It is not a CohortFact, so the bar's letter does not reach it; whether RULING W does is 1.0.0_SA_CTO's (W4-S19, graduated). The fixture registry's prose still says 'unknown renders as unknown' (fixtures/index.ts:77; W4-S20, graduated)."
   },
   {
    "criterion": "F49-AC15",
    "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-49.investor-reporting-opal-admin-only.proof_of_spec.json@a018979694",
    "verdict": "PASS",
    "reason": "MET, WITH THE BACKEND-WALL ANSWER NAMED FOR 1.0.0_SA_CTO AND ANDREW. Bar: 'no client or partner-firm user, admin or not, reaches Investor Reporting or sees its nav item through the portal; no allowlist grants what the gate refuses; the three gate hunks match c29a8b86; and the backend census says whether the UI is the only wall.' Read by this seat at portal DEV 10c2f07d (LOCAL; PORTAL FROZEN, read by git show): App.tsx:96 the nav item carries requiresAdmin: true, requiresTier: 'internal'; both routes are <ProtectedRoute requireAdmin requireInternal> (:423, :575); ProtectedRoute.tsx:39 refuses role != admin and :44 firmId != opal-capital. firmAccess.ts lists /investor-reporting 0 times (3 at 1f3ce9f0; numstat +0 -3). The nav line and both route lines equal c29a8b86's, 3 of 3, by this seat's own line read. Worker: partner admins refused 6 of 6, non-admins 8 of 8, nav shown to 1 of 8 identities. THE ANSWER THE CENSUS GIVES: the portal gate is the ONLY admin wall. Re-read by this seat at workspace HEAD (a source read, not the worker's test): _scope/resolve.py:186 makes a role=admin caller with any verified firm FIRM_OPERATIONS and :193 an advisor FIRM_ADVISOR; _authz/served.py:575 refuses only an absent verified firm; enforce.py:272 refuses only UNKNOWN. So a partner firm's admin who calls the API directly is served its own firm. No endpoint serves yet (investor-reporting.ts:14: the routes 'DO NOT EXIST yet', IRPT_BCKEND B15 builds them). Neither PRD names an admin wall (0 'admin' tokens in IRPT_FNTEND_PRD.md and IRPT_BCKEND_PRD.md), and decomposition R8.9 names 'the backend's own admin gating' as not moved. S66 is graduated to carry the decision."
   }
  ]
 },
 {
  "id": "IRPT_FNTEND-C-S100",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T09:42:39Z",
  "one_line": "ROUND-8 L9: two BLOCKING rows DISMISSED_WITH_REASON, each closed in drained code at portal DEV 10c2f07d under FE-s-49 amendment 1 (1.0.0_SA_CTO's ruling (a), 96961) -- W2-S34 (fe-s-14 asserted the partner entries; granted, re-pointed, entries removed) and S67 (F49-AC10's census had no timeout; it carries 3 x 6703 ms).",
  "class": "OBSERVATION",
  "spec_asserts": "1.0.0_SA_CTO 96924 / 96961 (a): '/investor-reporting' removed from the 49financial, inflection and cottonwood sets; fe-s-14/allowlist.test.ts granted; F49-AC13: the census test's timeout sized to its measured cost.",
  "world_is": "Read by this seat at portal DEV 10c2f07d (LOCAL; PORTAL FROZEN, read by git show): src/lib/firmAccess.ts lists '/investor-reporting' 0 times (3 at 1f3ce9f0; numstat +0 -3); fe-s-14/allowlist.test.ts is in FE-s-49's <paths> and its re-pointed test asserts +0 (:112) -3 (:113). fe-s-49/admin-gate.test.ts:606 declares F49-AC10 and closes with '}, 20109)' at :716; fe-s-49/recorded-costs.json holds 6 costs, highest 6703 (S67's), and 3 x 6703 = 20109. The census run times nothing.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W2-S34",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-S67",
    "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-49.investor-reporting-opal-admin-only.md@a018979694 <paths>, amendment 1",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W2-S34",
   "IRPT_FNTEND-S67"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Both are closed in drained code at portal DEV 10c2f07d, read by this seat. W2-S34's F49-AC9 refusal was superseded by amendment 1; S67's class is carried in F46-AC8's qualification (4).",
  "hazard_standing": "INERT"
 },
 {
  "id": "IRPT_FNTEND-C-S101",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T09:42:39Z",
  "one_line": "ROUND-8 L9: four FE-s-46 rows DISMISSED_WITH_REASON as records -- W1-S71 (a type-only overload inside the grant), W1-S72 (the BOUNDS wording names the wrong line; the 8-of-8 compiler proof shows the intent), W1-S73 (8 of 16 tests can reach the default; all 8 carry a timeout) and W1-S75 (30 costs carried from a BOOTSTRAP table; B03/B04 day-only).",
  "class": "OBSERVATION",
  "spec_asserts": "IRPT_FNTEND.TO-FE-s-46 THE REMEDY, BOUNDS, F46-AC1..AC3, and amendment 1: 'The ledger is produced only by the IRPT_FE_TIMEOUT_LOAD=1 path' and 'The ledger records F41-AC5's control at 18891 ms'.",
  "world_is": "Read by this seat at portal DEV 90d71d9e (LOCAL; PORTAL FROZEN, read by git show): the diff against 1f3ce9f0 is 1+7 lines, every one a closing '}, <ms>)' (W1-S72); 8 of 16 tests have a highest ledger cost >= 2500 ms and all 8 carry a timeout (W1-S73). W1-S75: amendment 1's two sentences cannot both hold by measurement alone -- 18891 ms predates the ledger -- and the worker's BOOTSTRAP carry is the one reading that meets both: the load path writes the ledger, 12 of its 24 runs (35 costs) are carried, each naming its source, and B03/B04 read 'day only' (B03, B04). W1-S71 is a type declaration inside fe-s-46/; the typecheck read rc=0 on the issuer's pair.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W1-S71",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W1-S72",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W1-S73",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W1-S75",
    "portal 90d71d9e:src/pages/InvestorReporting/__tests__/fe-s-46/recorded-costs.json",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W1-S71",
   "IRPT_FNTEND-W1-S72",
   "IRPT_FNTEND-W1-S73",
   "IRPT_FNTEND-W1-S75"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Records, each verified at DEV 90d71d9e. W1-S72 and W1-S75 are issuer wording defects (2.0.0_SA_COO~F's, owned in 96994); neither moves a verdict. W1-S75's provenance point is carried in F46-AC8's qualification (2).",
  "hazard_standing": "INERT"
 },
 {
  "id": "IRPT_FNTEND-C-S102",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T09:42:39Z",
  "one_line": "ROUND-8 L9: three rows DISMISSED_WITH_REASON as records -- W3-S36 (the wire instances are documents; the test wraps them), W3-S39 (a resolve-scope document's own reason; answered 'document first' by amendment 1, 96947) and W4-S18 (a line citation drift in FE-s-48's premise).",
  "class": "OBSERVATION",
  "spec_asserts": "IRPT_FNTEND.TO-FE-s-47 F47-AC2/AC7 and amendment 1 (1.0.0_SA_CTO 96947: the document's own reason first); IRPT_FNTEND.TO-FE-s-48 THE CELL's census premise.",
  "world_is": "W3-S39: read by this seat at portal DEV f28fcc44 (LOCAL; PORTAL FROZEN, read by git show), contracts/adapt.ts:307 keeps current.partialReason and fills only a null with NO_STATUS_REASON. W3-S36: the worker's wrap is the only body the criterion's words admit. W4-S18: validate.ts is one blob at 1f3ce9f0, f28fcc44 and 10c2f07d; the census classifies it by path and the verdict does not move.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W3-S36",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W3-S39",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W4-S18",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W3-S36",
   "IRPT_FNTEND-W3-S39",
   "IRPT_FNTEND-W4-S18"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "W3-S39 is closed in drained code; W3-S36 and W4-S18 are records of an order's wording that move no artifact.",
  "hazard_standing": "INERT"
 },
 {
  "id": "IRPT_FNTEND-C-S103",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T09:42:39Z",
  "one_line": "ROUND-8 L9, GRADUATED -- THE TWO ARMED LOAD ROWS, BOTH DISARMED IN CODE AT portal DEV 90d71d9e (2026-09-15T07:51:46Z): W1-S74 (the cut's own test ran load inside every census) and W3-S40 (F41-AC5's control timed out under load). Graduated so the disarm is carried in a field, not prose.",
  "class": "OBSERVATION",
  "spec_asserts": "The surprise channel: an ARMED row's disarm is carried by the remediation row's two-state `disarm` block; 'DISARMED IS NOT REMEDIATED'. IRPT_FNTEND.TO-FE-s-46 amendment 1: a committed cost ledger, load arms opt-in, F46-AC6.",
  "world_is": "Read by this seat at portal DEV 90d71d9e (LOCAL; PORTAL FROZEN, read by git show) (committer time 2026-09-15T07:51:46Z): fe-s-46/timeouts.test.ts:66 'const LOAD = env.IRPT_FE_TIMEOUT_LOAD === \"1\"' gates every load and ledger arm, and F46-AC3's bound reads the committed ledger (:708). fe-s-41/one-writer.test.ts:869 closes F41-AC5's control with '}, 56673)' = 3 x 18891. Residual: 3327 ms of headroom under the 60000 ms cap.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W1-S74",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W3-S40",
    "portal 90d71d9e:src/pages/InvestorReporting/__tests__/fe-s-46/timeouts.test.ts :66, :708",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W1-S74",
   "IRPT_FNTEND-W3-S40"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "IRPT_FNTEND-C-S104",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T09:42:39Z",
  "one_line": "ROUND-8 L9, GRADUATED -- S66, THE BACKEND-WALL HALF: the portal gate is closed at DEV 10c2f07d, but the portal is the ONLY admin wall. A partner firm's admin resolves FIRM_OPERATIONS and is served its own firm; no endpoint serves yet (IRPT_BCKEND B15), and no PRD names an admin wall.",
  "class": "OBSERVATION",
  "spec_asserts": "Andrew-direct (96903) prod-deploy condition 2: 'Investor Reporting must remain Opal Admin gated, no clients are allowed to see that.' 1.0.0_SA_CTO (96915): Opal admin = role admin AND the internal tier. F49-AC15: 'the backend census says whether the UI is the only wall'.",
  "world_is": "PORTAL HALF MET (portal DEV 10c2f07d (LOCAL; PORTAL FROZEN, read by git show)): nav :96, routes :423/:575, ProtectedRoute :39/:44, allowlist 0 of 3. BACKEND at workspace HEAD: _scope/resolve.py:186, :193; _authz/served.py:575; _authz/enforce.py:272. IRPT_FNTEND_PRD.md and IRPT_BCKEND_PRD.md carry 0 'admin' tokens; the decomposition names 'the backend's own admin gating' as not moved (:1867).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-S66",
    "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-49.investor-reporting-opal-admin-only.proof_of_spec.json@a018979694 F49-AC10",
    "infra/aws/lambda/investor-reporting/_scope/resolve.py@6806f529ac :186",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-S66"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "IRPT_FNTEND-C-S105",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T09:42:39Z",
  "one_line": "ROUND-8 L9, GRADUATED -- THE NO-STATUS RESIDUE amendment 1 routed to the round-8 analysis: a status member with no state keeps a reasonless default on its own availability (W3-S37), and status-summary/status-job carry the no-status reason on a document whose data says PARTIAL (W3-S38).",
  "class": "OBSERVATION",
  "spec_asserts": "RULING V (FE-s-47 THE REMEDY): 'When the adapter supplies its explicit unknown because the response carried no status, or a status with no state, it also supplies a partialReason saying so.' contracts/validate.ts: a top-level state that disagrees with availability.state is refused.",
  "world_is": "Both are outside FE-s-47's grant (adaptStatusEnvelope; the StatusEnvelope state rule) and predate it; amendment 1's text routes them to the round-8 analysis. Not read by the worker or this seat: whether a production consumer renders either value.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W3-S37",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W3-S38",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W3-S37",
   "IRPT_FNTEND-W3-S38"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "IRPT_FNTEND-C-S106",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T09:42:39Z",
  "one_line": "ROUND-8 L9, GRADUATED -- TWO INSTRUMENTS THAT DO NOT DISCRIMINATE: fe-s-14's F14-AC3 positive control still refuses only the retired '3<TAB>0', so a reader stuck at '0<TAB>3' passes both arms (W2-S35); proof-of-spec-check's COUNT-BAR limb reads a criterion id's last digit as a count (W3-S41).",
  "class": "OBSERVATION",
  "spec_asserts": "CLAUDE.md Rule 22 DISCRIMINATION: could the evidence differ if the claim were false? The control's own comment: 'A reader that returned +3 -0 for anything would make the test above a decoration.'",
  "world_is": "W2-S35 at portal DEV 10c2f07d (LOCAL; PORTAL FROZEN, read by git show): fe-s-14/allowlist.test.ts:126 refuses only startsWith('3\\t0\\t'); the re-pointed test asserts +0 (:112) -3 (:113). INERT: 0 of 3 entries confirmed by other instruments. W3-S41 at HEAD: .tools/proof-of-spec-check.py:1529 still carries the lookbehind; this seat compiled that pattern and it reads 'F47-AC2 PROBLEMS: []' as count '2'; a lookbehind that also excludes a letter or '-' reads it clean and still counts '2 PROBLEMS'. Fail-closed: a false INVALID, never a false VALID.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W2-S35",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W3-S41",
    ".tools/proof-of-spec-check.py@da3e61889d :1529",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W2-S35",
   "IRPT_FNTEND-W3-S41"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "IRPT_FNTEND-C-S107",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T09:42:39Z",
  "one_line": "ROUND-8 L9, GRADUATED -- RULING W's REACH AND ITS STALE PROSE: Holdings still renders a non-authoritative classification's partitions as 'unknown' (slices.ts, by the contract's own comment; W4-S19), and the fixture registry still says 'unknown renders as unknown' (fixtures/index.ts; W4-S20).",
  "class": "OBSERVATION",
  "spec_asserts": "1.0.0_SA_CTO round-7 analysis (96865) item 6: 'a non-authoritative cohort's axes read \"withheld\", never \"unknown\". RULING W keeps \"unknown\" out of any state that has a truer word.'",
  "world_is": "At portal DEV 10c2f07d (LOCAL; PORTAL FROZEN, read by git show): tabs/holdings/slices.ts:102 returns supervision/advisory 'unknown' for a non-authoritative classification; fixtures/index.ts:77 keeps the old `proves` prose. Neither is a CohortFact and neither was in FE-s-48's grant.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W4-S19",
    "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@5e5f074588#IRPT_FNTEND-W4-S20",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND8_L8_L9_20260915.md (same slug) section 2"
   ]
  },
  "adjudicates": [
   "IRPT_FNTEND-W4-S19",
   "IRPT_FNTEND-W4-S20"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 }
]
```
