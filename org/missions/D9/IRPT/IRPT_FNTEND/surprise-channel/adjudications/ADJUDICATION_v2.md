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
  }
]
```
