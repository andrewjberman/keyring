# AMGT_RESAPP -- round 104, workstream AIFILL, L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-14T01:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T01:00:00Z. Scope: round 104 WORKSTREAM AIFILL only (issuer 2.0.0_SA_COO~R2, msg 5306),
packet org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104/DRAIN_END_PACKET.md (blob verified). Not graded here: ~R1's
round 104 (workstream-less) and the AIFILLREL release orders ar-1 and ar-3. round-close-check --round 104 --workstream AIFILL: 9 of 9
complete, proof_bad 0, judgment 0, MAY-CLOSE. All 28 rows of slots ~420 to ~428 are dispositioned (C-S132 to C-S135). FWD-41 NOT MET,
built not served (C-S131). Two producer defects graduate ARMED to REMEDIATION_v40 (C-S132, C-S133).

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S131",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:00:00Z",
    "one_line": "FWD-41 (the five AI-fill blocks served with source class and citations; the CVO reads five names on PROD) is NOT MET at round 104 of workstream AIFILL. Stage: BUILT, NOT SERVED. Built: the producer runs (deliverables/2.0.0_SA_COO~R2/round104/thread_run_2/AMD_US_Equity.json, 'AIFILL RUN: key=AMD_US_Equity document=VALID blocks=5 (OPAL 0 WEB 4 NONE 1)'). Stored: the packet says the prefix was empty; this seat's read at 2026-10-14T00:5xZ finds 2 objects written AFTER the packet by the issuer's step-2 driver (store_batch.py, 7a69cc8519): security_key=AMD_US_Equity/ai_fill.json (9,339 B, 00:47:13Z) and security_key=8035_JP_Equity/ai_fill.json (5,619 B, 00:49:09Z); storage has begun, it is not a round-104 deliverable. Served: NO -- opal-amgt-scoped-api is still Wkt48Y6vf4o4Dhyb9gVkfaf9IIJ75ThoI+hiMUoGrS4= (LastModified 00:07:07Z, re-read here), which does not serve ai_fill; ar-3 (the redeploy) is staged in workstream AIFILLREL. Rendered: NO -- fa-8's page is on portal branch 85d5749f, not on DEV or PROD. OWED: this seat's five-name PROD read, after the 95-name run (round 105 of this workstream, packet section 5 item 3); it is FWD-41's bar and it reads the STORED documents, not the round's thread runs.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "FWD-41 (the five AI-fill blocks served with source class and citations; the CVO reads five names on PROD) is NOT MET at round 104 of workstream AIFILL. Stage: BUILT, NOT SERVED. Built: the producer runs (deliverables/2.0.0_SA_COO~R2/round104/thread_run_2/AMD_US_Equity.json, 'AIFILL RUN: key=AMD_US_Equity document=VALID blocks=5 (OPAL 0 WEB 4 NONE 1)'). Stored: the packet says the prefix was empty; this seat's read at 2026-10-14T00:5xZ finds 2 objects written AFTER the packet by the issuer's step-2 driver (store_batch.py, 7a69cc8519): security_key=AMD_US_Equity/ai_fill.json (9,339 B, 00:47:13Z) and security_key=8035_JP_Equity/ai_fill.json (5,619 B, 00:49:09Z); storage has begun, it is not a round-104 deliverable. Served: NO -- opal-amgt-scoped-api is still Wkt48Y6vf4o4Dhyb9gVkfaf9IIJ75ThoI+hiMUoGrS4= (LastModified 00:07:07Z, re-read here), which does not serve ai_fill; ar-3 (the redeploy) is staged in workstream AIFILLREL. Rendered: NO -- fa-8's page is on portal branch 85d5749f, not on DEV or PROD. OWED: this seat's five-name PROD read, after the 95-name run (round 105 of this workstream, packet section 5 item 3); it is FWD-41's bar and it reads the STORED documents, not the round's thread runs.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104/DRAIN_END_PACKET.md section 5",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104/thread_run_2/AMD_US_Equity.json",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104/thread_run_2/run_AMD_US_Equity.txt",
        "3.0.0_SA_CVO aws s3api list-objects-v2 --prefix amgt/harvest/gold/ai_fill/ 2026-10-14T00:5xZ: 2 keys (positive control: the parent amgt/harvest/gold/ KeyCount 1 at --max-keys 1)",
        "3.0.0_SA_CVO aws lambda get-function-configuration opal-amgt-scoped-api: Wkt48Y6v.., 00:07:07Z",
        "orders AMGT_RESAPP.TO-AMGT-ar-1 and ar-3 (scope AIFILLREL, not this workstream)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "owner": "3.0.0_SA_CVO"
  },
  {
    "id": "AMGT_RESAPP-D1-C-S132",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:00:00Z",
    "one_line": "The graded AMD output (deliverables/2.0.0_SA_COO~R2/round104/thread_run_2/AMD_US_Equity.json, generated 2026-10-14T00:20:16Z), read here block by block against its cited sources. Citations: PASS -- each of the 4 filled blocks (mgmt_bio WEB 4, mgmt_recent WEB 4, mgmt_team_view WEB 4, thesis_pillars WEB 5) carries its web citations, and the empty identity_description is NONE with its reason 'The identity header already has a company description.' Figures and claims: FOUR DEFECTS, each a claim its cited source does not carry. (1) mgmt_bio: Su 'chairs the Semiconductor Industry Association board' -- the cited AMD IR biography says vice chair. (2) mgmt_recent: Awasthi 'under sales chief Darren Grasby' -- the reporting line is not in the cited appointment source. (3) mgmt_recent: Kelman 'reporting to chief administrative officer Ruth Cotter' -- not located in the cited sources on this seat's read (two fetches timed out); UNVERIFIED, not refuted. (4) thesis_pillars: 'gross margin of 56%' is AMD's non-GAAP figure, printed with no qualifier beside GAAP-basis neighbours. Under the coordinator's standard (a figure not in its cited source is a defect) the producer can store a cited block whose claims outrun its citations. Graduated ARMED to REMEDIATION_v40.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "The graded AMD output (deliverables/2.0.0_SA_COO~R2/round104/thread_run_2/AMD_US_Equity.json, generated 2026-10-14T00:20:16Z), read here block by block against its cited sources. Citations: PASS -- each of the 4 filled blocks (mgmt_bio WEB 4, mgmt_recent WEB 4, mgmt_team_view WEB 4, thesis_pillars WEB 5) carries its web citations, and the empty identity_description is NONE with its reason 'The identity header already has a company description.' Figures and claims: FOUR DEFECTS, each a claim its cited source does not carry. (1) mgmt_bio: Su 'chairs the Semiconductor Industry Association board' -- the cited AMD IR biography says vice chair. (2) mgmt_recent: Awasthi 'under sales chief Darren Grasby' -- the reporting line is not in the cited appointment source. (3) mgmt_recent: Kelman 'reporting to chief administrative officer Ruth Cotter' -- not located in the cited sources on this seat's read (two fetches timed out); UNVERIFIED, not refuted. (4) thesis_pillars: 'gross margin of 56%' is AMD's non-GAAP figure, printed with no qualifier beside GAAP-basis neighbours. Under the coordinator's standard (a figure not in its cited source is a defect) the producer can store a cited block whose claims outrun its citations. Graduated ARMED to REMEDIATION_v40.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104/thread_run_2/AMD_US_Equity.json",
        "the cited URLs of each block, fetched by 3.0.0_SA_CVO 2026-10-14T00:1xZ-00:4xZ (two fetches for the Kelman claim timed out)"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "2.0.0_SA_COO~R2"
  },
  {
    "id": "AMGT_RESAPP-D1-C-S133",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:00:00Z",
    "one_line": "The STORED AMD document (s3://opal-data-harvest/amgt/harvest/gold/ai_fill/security_key=AMD_US_Equity/ai_fill.json, generated 2026-10-14T00:46:21Z, producer claude-opus-5 / opal-aifill/1.0.0) is a fresh generation, NOT the graded thread run (the two documents differ). Its mgmt_team_view text opens with the model's own narration, joined to the first sentence with no space: \"I'll research AMD's management track record from public sources.Dr Lisa Su has been AMD's chief executive ...\". The aifill/v1 validator passed it, so it will serve verbatim once ar-3 redeploys. Also: thesis_pillars, filled with 5 citations in the graded run, is NONE here ('The web search returned no citable source, so the text was withheld.'), so a block's presence varies run to run; and mgmt_team_view cites press.farm, a substack post and (mgmt_bio) vectorshift.ai beside SEC filings, a source-quality question for the five-name read. 8035_JP_Equity's stored text shows no narration. Graduated ARMED to REMEDIATION_v40.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "The STORED AMD document (s3://opal-data-harvest/amgt/harvest/gold/ai_fill/security_key=AMD_US_Equity/ai_fill.json, generated 2026-10-14T00:46:21Z, producer claude-opus-5 / opal-aifill/1.0.0) is a fresh generation, NOT the graded thread run (the two documents differ). Its mgmt_team_view text opens with the model's own narration, joined to the first sentence with no space: \"I'll research AMD's management track record from public sources.Dr Lisa Su has been AMD's chief executive ...\". The aifill/v1 validator passed it, so it will serve verbatim once ar-3 redeploys. Also: thesis_pillars, filled with 5 citations in the graded run, is NONE here ('The web search returned no citable source, so the text was withheld.'), so a block's presence varies run to run; and mgmt_team_view cites press.farm, a substack post and (mgmt_bio) vectorshift.ai beside SEC filings, a source-quality question for the five-name read. 8035_JP_Equity's stored text shows no narration. Graduated ARMED to REMEDIATION_v40.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO aws s3 cp of both stored documents 2026-10-14T00:5xZ, read whole; dict compare with deliverables/2.0.0_SA_COO~R2/round104/thread_run_2/AMD_US_Equity.json: not equal"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "2.0.0_SA_COO~R2"
  },
  {
    "id": "AMGT_RESAPP-D1-C-S134",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:00:00Z",
    "one_line": "The 4 BLOCKING rows and 1 ARMED row (W421-S1, W423-S5, W424-S1, W426-S1; W422-S1) dismissed: each amendment, read here by content, removes its hazard. W421-S1 (059fcc6280): lib/research/aifill/inputs.py types no function name at HEAD -- FUNCTION_ENV = 'AIFILL_SERVED_FUNCTION' (:19), _resolve_function_name takes the argument, else the env, else ValueError (:30-36); comp-find 'opal-amgt-scoped-api' lib/research/aifill: 0 hits across 18 files. Limb: the LGIC naming limb of safe-commit refused the literal (it found the defect); GATE (viii) grades the modified order (placeholders NONE). W422-S1 (34599d538b): lib/research/api/tests/conftest.py:56 sets ENV_AIFILL_ROOT to an empty directory for every test; no gate limb graded the amendment (its commit says so). W423-S5 (df02062aac): portal branch 85d5749f adds one AiFillBlock stub entry (+2 lines) to each of the drafting, execFallback and execText harnesses and nothing else in them; read by content, NOT run by this seat; the page is not landed; no gate limb graded the amendment. W424-S1 (463cf262d0): check_fa3_mgmt_bio.py's OPAL arm now requires the research-team-pack citation when role_start and tenure_years are both null, consistent with the face; no gate limb. W426-S1 (a69d3efdbb): fa-5's expectation reads 20, the check's 20 arms; no arm removed; no gate limb. Four of five amendments were graded by no gate limb: the issuer's word and this seat's content read are the only grade.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W421-S1",
      "AMGT_RESAPP-D1-W422-S1",
      "AMGT_RESAPP-D1-W423-S5",
      "AMGT_RESAPP-D1-W424-S1",
      "AMGT_RESAPP-D1-W426-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "The 4 BLOCKING rows and 1 ARMED row (W421-S1, W423-S5, W424-S1, W426-S1; W422-S1) dismissed: each amendment, read here by content, removes its hazard. W421-S1 (059fcc6280): lib/research/aifill/inputs.py types no function name at HEAD -- FUNCTION_ENV = 'AIFILL_SERVED_FUNCTION' (:19), _resolve_function_name takes the argument, else the env, else ValueError (:30-36); comp-find 'opal-amgt-scoped-api' lib/research/aifill: 0 hits across 18 files. Limb: the LGIC naming limb of safe-commit refused the literal (it found the defect); GATE (viii) grades the modified order (placeholders NONE). W422-S1 (34599d538b): lib/research/api/tests/conftest.py:56 sets ENV_AIFILL_ROOT to an empty directory for every test; no gate limb graded the amendment (its commit says so). W423-S5 (df02062aac): portal branch 85d5749f adds one AiFillBlock stub entry (+2 lines) to each of the drafting, execFallback and execText harnesses and nothing else in them; read by content, NOT run by this seat; the page is not landed; no gate limb graded the amendment. W424-S1 (463cf262d0): check_fa3_mgmt_bio.py's OPAL arm now requires the research-team-pack citation when role_start and tenure_years are both null, consistent with the face; no gate limb. W426-S1 (a69d3efdbb): fa-5's expectation reads 20, the check's 20 arms; no arm removed; no gate limb. Four of five amendments were graded by no gate limb: the issuer's word and this seat's content read are the only grade.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows named",
        "git show 059fcc6280 34599d538b df02062aac 463cf262d0 a69d3efdbb (messages and diffs)",
        "lib/research/aifill/inputs.py:19,30-36,48-50 at HEAD",
        "lib/research/api/tests/conftest.py:56 at HEAD",
        "portal 85d5749f harness diffs"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The 4 BLOCKING rows and 1 ARMED row (W421-S1, W423-S5, W424-S1, W426-S1; W422-S1) dismissed: each amendment, read here by content, removes its hazard. W421-S1 (059fcc6280): lib/research/aifill/inputs.py types no function name at HEAD -- FUNCTION_ENV = 'AIFILL_SERVED_FUNCTION' (:19), _resolve_function_name takes the argument, else the env, else ValueError (:30-36); comp-find 'opal-amgt-scoped-api' lib/research/aifill: 0 hits across 18 files. Limb: the LGIC naming limb of safe-commit refused the literal (it found the defect); GATE (viii) grades the modified order (placeholders NONE). W422-S1 (34599d538b): lib/research/api/tests/conftest.py:56 sets ENV_AIFILL_ROOT to an empty directory for every test; no gate limb graded the amendment (its commit says so). W423-S5 (df02062aac): portal branch 85d5749f adds one AiFillBlock stub entry (+2 lines) to each of the drafting, execFallback and execText harnesses and nothing else in them; read by content, NOT run by this seat; the page is not landed; no gate limb graded the amendment. W424-S1 (463cf262d0): check_fa3_mgmt_bio.py's OPAL arm now requires the research-team-pack citation when role_start and tenure_years are both null, consistent with the face; no gate limb. W426-S1 (a69d3efdbb): fa-5's expectation reads 20, the check's 20 arms; no arm removed; no gate limb. Four of five amendments were graded by no gate limb: the issuer's word and this seat's content read are the only grade."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S135",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:00:00Z",
    "one_line": "The 23 INERT observations of slots ~420 to ~428 dismissed. Face-versus-base drift with no served effect: W423-S1, S2, S3 (followed the face; nothing pushed), W425-S1, S2. Channel-layout facts: W425-S3, W426-S4 (149 fences, one per row; append matches). Amendment-2 ordering choices recorded by the builders: W424-S3, W425-S4, W426-S2, W426-S3, W423-S4, W423-S6 (the five-name read judges the result on the page). Instrument noise: W423-S7 (pre-commit scanned 0 of 3 .cjs files; the harnesses are the read), W423-S8 (15 vs 18 of 21 base harnesses; AC2 graded against its own instrument), W428-S1 (PASS arms print failure text; verdict YES 8 of 8), W422-S3 (naming gate WARN on a display literal), W422-S4 (premise count did not reproduce; the sign did, 42 GETs). Code facts with no served effect: W420-S1 (escapes before commit), W420-S2 (trailing space after a dropped character), W420-S3 (Exception not BaseException), W422-S2 (validator stricter than the face), W424-S2 (one en dash in a TEST module string; production files are ASCII).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W420-S1",
      "AMGT_RESAPP-D1-W420-S2",
      "AMGT_RESAPP-D1-W420-S3",
      "AMGT_RESAPP-D1-W422-S2",
      "AMGT_RESAPP-D1-W422-S3",
      "AMGT_RESAPP-D1-W422-S4",
      "AMGT_RESAPP-D1-W423-S1",
      "AMGT_RESAPP-D1-W423-S2",
      "AMGT_RESAPP-D1-W423-S3",
      "AMGT_RESAPP-D1-W423-S4",
      "AMGT_RESAPP-D1-W423-S6",
      "AMGT_RESAPP-D1-W423-S7",
      "AMGT_RESAPP-D1-W423-S8",
      "AMGT_RESAPP-D1-W424-S2",
      "AMGT_RESAPP-D1-W424-S3",
      "AMGT_RESAPP-D1-W425-S1",
      "AMGT_RESAPP-D1-W425-S2",
      "AMGT_RESAPP-D1-W425-S3",
      "AMGT_RESAPP-D1-W425-S4",
      "AMGT_RESAPP-D1-W426-S2",
      "AMGT_RESAPP-D1-W426-S3",
      "AMGT_RESAPP-D1-W426-S4",
      "AMGT_RESAPP-D1-W428-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "The 23 INERT observations of slots ~420 to ~428 dismissed. Face-versus-base drift with no served effect: W423-S1, S2, S3 (followed the face; nothing pushed), W425-S1, S2. Channel-layout facts: W425-S3, W426-S4 (149 fences, one per row; append matches). Amendment-2 ordering choices recorded by the builders: W424-S3, W425-S4, W426-S2, W426-S3, W423-S4, W423-S6 (the five-name read judges the result on the page). Instrument noise: W423-S7 (pre-commit scanned 0 of 3 .cjs files; the harnesses are the read), W423-S8 (15 vs 18 of 21 base harnesses; AC2 graded against its own instrument), W428-S1 (PASS arms print failure text; verdict YES 8 of 8), W422-S3 (naming gate WARN on a display literal), W422-S4 (premise count did not reproduce; the sign did, 42 GETs). Code facts with no served effect: W420-S1 (escapes before commit), W420-S2 (trailing space after a dropped character), W420-S3 (Exception not BaseException), W422-S2 (validator stricter than the face), W424-S2 (one en dash in a TEST module string; production files are ASCII).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows named"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The 23 INERT observations of slots ~420 to ~428 dismissed. Face-versus-base drift with no served effect: W423-S1, S2, S3 (followed the face; nothing pushed), W425-S1, S2. Channel-layout facts: W425-S3, W426-S4 (149 fences, one per row; append matches). Amendment-2 ordering choices recorded by the builders: W424-S3, W425-S4, W426-S2, W426-S3, W423-S4, W423-S6 (the five-name read judges the result on the page). Instrument noise: W423-S7 (pre-commit scanned 0 of 3 .cjs files; the harnesses are the read), W423-S8 (15 vs 18 of 21 base harnesses; AC2 graded against its own instrument), W428-S1 (PASS arms print failure text; verdict YES 8 of 8), W422-S3 (naming gate WARN on a display literal), W422-S4 (premise count did not reproduce; the sign did, 42 GETs). Code facts with no served effect: W420-S1 (escapes before commit), W420-S2 (trailing space after a dropped character), W420-S3 (Exception not BaseException), W422-S2 (validator stricter than the face), W424-S2 (one en dash in a TEST module string; production files are ASCII)."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S136",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T01:00:00Z",
    "one_line": "Routed, not graded here: the api suite's 3 new failures against baseline_api_failures.txt belong to ~R1's bk-4 (57fb3c63f3 adds _derive_fiscal_pe to scoped_amgt.py, which withholds PE_RATIO rows whose PX_LAST and IS_EPS currencies differ), not to workstream AIFILL. They go to ~R1's round-104 compile, a separate carrier; this row does not grade them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Routed, not graded here: the api suite's 3 new failures against baseline_api_failures.txt belong to ~R1's bk-4 (57fb3c63f3 adds _derive_fiscal_pe to scoped_amgt.py, which withholds PE_RATIO rows whose PX_LAST and IS_EPS currencies differ), not to workstream AIFILL. They go to ~R1's round-104 compile, a separate carrier; this row does not grade them.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_api_suite_no_new_failures.py",
        "git show 57fb3c63f3"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "owner": "2.0.0_SA_COO~R1"
  }
]
```
