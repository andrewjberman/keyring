# AMGT_RESAPP -- round 94 L8/L9 adjudication, packet FINAL (dell1)

<sweep_watermark>2026-10-11T15:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T15:55:00Z. L8 packet: 2.0.0_SA_COO~R1 msg 3940,
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94/DRAIN_END_PACKET.md @6e285b8a14 (blob 95cf08d5f4, verified).
5 of 5 orders complete; ff-4 redeploy VNcX9ntm held; ff-5 SAP 0 -> 3 points. L9 HOLDS on this seat's own runs (C-S73); round-93 items
1-3 MET on a browser walk of portal DEV (C-S74). REMEDIATION_v37 D1-S23 closed REMEDIATED (C-S75). 10 rows swept since v113 (watermark
2026-10-11T12:20Z; 10 of 1064 investigation rows after it): D1-S24 and D1-S26 graduated ARMED, 8 dismissed (W387-S3, W387-S2 and S25
disarmed). New observation C-S82 (2 intermittent 500s on /compare, raised in front of the function) left UNDER_INVESTIGATION, INERT.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S73",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:55:00Z",
    "one_line": "L9 read of the round-94 packet section 2: HOLDS on this seat's own runs at box/dell1 HEAD d339f3f554. Live function CodeSha256 VNcX9ntm83qe07/eOOD16AYsDmoEp20eCzj9ljfGvGE= (LastModified 2026-10-11T14:57:44Z). ff-4: r94_name_census.py --where deployed: 243 of 243 subjects judged, DIFFERENT company 0 (C1), ranked lists 0 of 126 judged (C3), rank series 0 of 82 judged (C4), R94 NAME CENSUS: YES; --where local YES. ff-5: r94_sap_served.py V1 SAP 2023 = 13.745, 2024 = 18.078, 2025 = 21.05 (stated million, million, billion), V2 ASML none, V3 BABA FY2025 118,028 and FY2026 158,132, R94 SAP SERVED: YES. ff-1/ff-3 local: r94_display_name.py 12 of 12, r94_rescale.py YES. No-regression: r92_minor_unit_census.py YES; this seat's census 0 minor-unit rows with 155 members serving a currency; R93 SELF PEER CENSUS YES; R89 PEERS DEPLOYED YES; R89 DEPLOYED CLOSE YES at amgt-corpus-dossier/12 (the build carries AMGT_CORPUS leg p). lib/research/api/tests + peers + filings 1478 passed. round-close-check --round 94: 5 of 5, MAY-CLOSE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L9 read of the round-94 packet section 2: HOLDS on this seat's own runs at box/dell1 HEAD d339f3f554. Live function CodeSha256 VNcX9ntm83qe07/eOOD16AYsDmoEp20eCzj9ljfGvGE= (LastModified 2026-10-11T14:57:44Z). ff-4: r94_name_census.py --where deployed: 243 of 243 subjects judged, DIFFERENT company 0 (C1), ranked lists 0 of 126 judged (C3), rank series 0 of 82 judged (C4), R94 NAME CENSUS: YES; --where local YES. ff-5: r94_sap_served.py V1 SAP 2023 = 13.745, 2024 = 18.078, 2025 = 21.05 (stated million, million, billion), V2 ASML none, V3 BABA FY2025 118,028 and FY2026 158,132, R94 SAP SERVED: YES. ff-1/ff-3 local: r94_display_name.py 12 of 12, r94_rescale.py YES. No-regression: r92_minor_unit_census.py YES; this seat's census 0 minor-unit rows with 155 members serving a currency; R93 SELF PEER CENSUS YES; R89 PEERS DEPLOYED YES; R89 DEPLOYED CLOSE YES at amgt-corpus-dossier/12 (the build carries AMGT_CORPUS leg p). lib/research/api/tests + peers + filings 1478 passed. round-close-check --round 94: 5 of 5, MAY-CLOSE.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py --where deployed and --where local, r94_sap_served.py, r94_display_name.py, r94_rescale.py: YES x5",
        "3.0.0_SA_CVO ran round92 r92_minor_unit_census.py, round93 r93_self_peer_census.py (packet args), r89 deployed pair (--want amgt-corpus-dossier/12), org/tier1_exec/3.0.0_SA_CVO/deliverables/checks/amgt_minor_unit_census.py: all pass, 0 minor-unit rows",
        "3.0.0_SA_CVO aws lambda get-function-configuration opal-amgt-scoped-api 2026-10-11T15:2xZ: VNcX9ntm..",
        "3.0.0_SA_CVO python .tools/round-close-check.py --project AMGT_RESAPP --round 94: verdict=MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "L9 read of the round-94 packet section 2: HOLDS on this seat's own runs at box/dell1 HEAD d339f3f554. Live function CodeSha256 VNcX9ntm83qe07/eOOD16AYsDmoEp20eCzj9ljfGvGE= (LastModified 2026-10-11T14:57:44Z). ff-4: r94_name_census.py --where deployed: 243 of 243 subjects judged, DIFFERENT company 0 (C1), ranked lists 0 of 126 judged (C3), rank series 0 of 82 judged (C4), R94 NAME CENSUS: YES; --where local YES. ff-5: r94_sap_served.py V1 SAP 2023 = 13.745, 2024 = 18.078, 2025 = 21.05 (stated million, million, billion), V2 ASML none, V3 BABA FY2025 118,028 and FY2026 158,132, R94 SAP SERVED: YES. ff-1/ff-3 local: r94_display_name.py 12 of 12, r94_rescale.py YES. No-regression: r92_minor_unit_census.py YES; this seat's census 0 minor-unit rows with 155 members serving a currency; R93 SELF PEER CENSUS YES; R89 PEERS DEPLOYED YES; R89 DEPLOYED CLOSE YES at amgt-corpus-dossier/12 (the build carries AMGT_CORPUS leg p). lib/research/api/tests + peers + filings 1478 passed. round-close-check --round 94: 5 of 5, MAY-CLOSE."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S74",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:55:00Z",
    "one_line": "Round-93 items 1-3 graded on a BROWSER walk (ui-walk, the dormant walker account armed and disarmed, post-disarm login REFUSED 401) of /security-analysis on the 5174 dev build over portal DEV cb76f857 (contains ff-2 582ffe6eb8; merge-base --is-ancestor read). Item 1: the SAN FP header names 'Sanofi' ('Health Care -- FR'); the CSL AU header names 'Csl Ltd' ('Health Care -- AU'); neither names Santander or Carlisle. Items 2 and 3: the peers headings read ASML 'Mkt Cap (EUR, USD)', ROG 'Mkt Cap (CHF, USD)', BA 'Mkt Cap (USD)' (Price and EV headings likewise name their codes), and the Ticker cell reads 'no ticker held' for Tencent, SK hynix and Samsung (ASML) and Novo Nordisk (ROG). The round-93 caveat sentence still renders under each table. Scope: five names, one walk; the walk ran on a 5174 server another seat had started at 15:08Z, serving the same portal/ checkout.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Round-93 items 1-3 graded on a BROWSER walk (ui-walk, the dormant walker account armed and disarmed, post-disarm login REFUSED 401) of /security-analysis on the 5174 dev build over portal DEV cb76f857 (contains ff-2 582ffe6eb8; merge-base --is-ancestor read). Item 1: the SAN FP header names 'Sanofi' ('Health Care -- FR'); the CSL AU header names 'Csl Ltd' ('Health Care -- AU'); neither names Santander or Carlisle. Items 2 and 3: the peers headings read ASML 'Mkt Cap (EUR, USD)', ROG 'Mkt Cap (CHF, USD)', BA 'Mkt Cap (USD)' (Price and EV headings likewise name their codes), and the Ticker cell reads 'no ticker held' for Tencent, SK hynix and Samsung (ASML) and Novo Nordisk (ROG). The round-93 caveat sentence still renders under each table. Scope: five names, one walk; the walk ran on a 5174 server another seat had started at 15:08Z, serving the same portal/ checkout.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran node .claude/skills/ui-walk/walk.mjs --route /security-analysis --security ASML --security ROG --security BA --security 'SAN FP' --security 'CSL AU' 2026-10-11T15:34Z-15:43Z: 147 screenshots, 0 guard aborts, walk void no",
        "screenshots (local, not committed): tmp/ui-walk/20261011T153440Z/shots/013-ASML-Peers.png, 041-ROG-Peers.png, 075-BA-Peers.png, 097-SAN-FP-overlay.png, 124-CSL-AU-overlay.png",
        "git -C portal merge-base --is-ancestor 582ffe6eb8 HEAD (HEAD cb76f857): true"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Round-93 items 1-3 graded on a BROWSER walk (ui-walk, the dormant walker account armed and disarmed, post-disarm login REFUSED 401) of /security-analysis on the 5174 dev build over portal DEV cb76f857 (contains ff-2 582ffe6eb8; merge-base --is-ancestor read). Item 1: the SAN FP header names 'Sanofi' ('Health Care -- FR'); the CSL AU header names 'Csl Ltd' ('Health Care -- AU'); neither names Santander or Carlisle. Items 2 and 3: the peers headings read ASML 'Mkt Cap (EUR, USD)', ROG 'Mkt Cap (CHF, USD)', BA 'Mkt Cap (USD)' (Price and EV headings likewise name their codes), and the Ticker cell reads 'no ticker held' for Tencent, SK hynix and Samsung (ASML) and Novo Nordisk (ROG). The round-93 caveat sentence still renders under each table. Scope: five names, one walk; the walk ran on a 5174 server another seat had started at 15:08Z, serving the same portal/ checkout.",
    "notes": "'Csl Ltd' is the casing limit the packet names (section 6 item 3); cosmetic."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S75",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:55:00Z",
    "one_line": "REMEDIATION_v37 D1-S23 closed: disarm ARMED -> DISARMED and remediation OPEN -> REMEDIATED, nothing else moved. Its close condition holds on this seat's reads: GET /security/SAN_FP_Equity/overlay serves display_name 'Sanofi' (source crosswalk); _held_name_index at HEAD (106 tokens) maps 'banco santander s a' to nothing and 'sanofi' to SAN_FP_Equity; the control ASML_NA_Equity still serves 'ASML Holding NV' (etf-classifications), unchanged. The deployed census C1 reads 0 different on 243.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-S23"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "REMEDIATION_v37 D1-S23 closed: disarm ARMED -> DISARMED and remediation OPEN -> REMEDIATED, nothing else moved. Its close condition holds on this seat's reads: GET /security/SAN_FP_Equity/overlay serves display_name 'Sanofi' (source crosswalk); _held_name_index at HEAD (106 tokens) maps 'banco santander s a' to nothing and 'sanofi' to SAN_FP_Equity; the control ASML_NA_Equity still serves 'ASML Holding NV' (etf-classifications), unchanged. The deployed census C1 reads 0 different on 243.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO lambda invoke GET /security/{SAN_FP_Equity,CSL_AU_Equity,ASML_NA_Equity}/overlay 2026-10-11T15:3xZ",
        "3.0.0_SA_CVO python: lib.research.api.scoped_amgt._held_name_index() at d339f3f554",
        "adjudication row AMGT_RESAPP-D1-C-S73"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "REMEDIATION_v37 D1-S23 closed: disarm ARMED -> DISARMED and remediation OPEN -> REMEDIATED, nothing else moved. Its close condition holds on this seat's reads: GET /security/SAN_FP_Equity/overlay serves display_name 'Sanofi' (source crosswalk); _held_name_index at HEAD (106 tokens) maps 'banco santander s a' to nothing and 'sanofi' to SAN_FP_Equity; the control ASML_NA_Equity still serves 'ASML Holding NV' (etf-classifications), unchanged. The deployed census C1 reads 0 different on 243."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S76",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:55:00Z",
    "one_line": "D1-S24 (ARMED) graduated ARMED to REMEDIATION_v38 (owner and disarm owner 2.0.0_SA_COO~R1; the CTO's round-95 first cell, msg 3887): reverify_stored_thesis_driver re-derives from each point's rescaled value, so a second re-verification of SAP's object would keep 1 of 3 points. Served today: SAP's 3 points are correct (C-S73 V1); the hazard is the next re-verification, held off by the ff-5 ledger leg L8 instruction only.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-S24"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S24 (ARMED) graduated ARMED to REMEDIATION_v38 (owner and disarm owner 2.0.0_SA_COO~R1; the CTO's round-95 first cell, msg 3887): reverify_stored_thesis_driver re-derives from each point's rescaled value, so a second re-verification of SAP's object would keep 1 of 3 points. Served today: SAP's 3 points are correct (C-S73 V1); the hazard is the next re-verification, held off by the ff-5 ledger leg L8 instruction only.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-S24",
        "round94/DRAIN_END_PACKET.md section 3 item 2 and section 6 item 1"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v38.md."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S77",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:55:00Z",
    "one_line": "D1-S26 (ARMED) graduated ARMED to REMEDIATION_v38 (owner and disarm owner 2.0.0_SA_COO~R1; the CTO's round-95 second cell): CSL AU is served Carlisle's classification. This seat's live read of /lead-panel/timeseries/TRENDING/PRICE?tickers=SAN FP,CSL AU,BA US returns CSL AU as name 'Carlisle Cos Inc' (SERVED, 0 points) with sub_asset_class 'US Large Cap', sector null; SAN FP reads 'Sanofi', Health Care. The by-ticker series name for CSL AU (D1-S25's residual) is carried here, since it is the same bare-ticker collision.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-S26"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S26 (ARMED) graduated ARMED to REMEDIATION_v38 (owner and disarm owner 2.0.0_SA_COO~R1; the CTO's round-95 second cell): CSL AU is served Carlisle's classification. This seat's live read of /lead-panel/timeseries/TRENDING/PRICE?tickers=SAN FP,CSL AU,BA US returns CSL AU as name 'Carlisle Cos Inc' (SERVED, 0 points) with sub_asset_class 'US Large Cap', sector null; SAN FP reads 'Sanofi', Health Care. The by-ticker series name for CSL AU (D1-S25's residual) is carried here, since it is the same bare-ticker collision.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_RESAPP-D1-S26, D1-S25",
        "3.0.0_SA_CVO lambda invoke GET /lead-panel/timeseries/TRENDING/PRICE?tickers=SAN FP,CSL AU,BA US 2026-10-11T15:4xZ"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v38.md."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S78",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:55:00Z",
    "one_line": "D1-S25 (ARMED) dismissed, disarmed for every series a page asks for: the deployed census C4 reads 0 of 82 judged rank series naming another company, and SAN FP's series reads 'Sanofi' live. The residual (CSL AU asked for by ticker still reads 'Carlisle Cos Inc'; it is on no ranked list, so no page asks) is carried on REMEDIATION_v38's D1-S26 row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-S25"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S25 (ARMED) dismissed, disarmed for every series a page asks for: the deployed census C4 reads 0 of 82 judged rank series naming another company, and SAN FP's series reads 'Sanofi' live. The residual (CSL AU asked for by ticker still reads 'Carlisle Cos Inc'; it is on no ranked list, so no page asks) is carried on REMEDIATION_v38's D1-S26 row.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-S25",
        "adjudication rows AMGT_RESAPP-D1-C-S73 (C4) and D1-C-S77"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S25 (ARMED) dismissed, disarmed for every series a page asks for: the deployed census C4 reads 0 of 82 judged rank series naming another company, and SAN FP's series reads 'Sanofi' live. The residual (CSL AU asked for by ticker still reads 'Carlisle Cos Inc'; it is on no ranked list, so no page asks) is carried on REMEDIATION_v38's D1-S26 row."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S79",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:55:00Z",
    "one_line": "D1-W387-S3 (BLOCKING, ARMED) dismissed, disarmed: ff-1 AMENDMENT 2 widened the order to re-pin the test that held the superseded precedence; this seat's pytest over the whole lib/research/api/tests directory with peers and filings reads 1478 passed, 0 failed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W387-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W387-S3 (BLOCKING, ARMED) dismissed, disarmed: ff-1 AMENDMENT 2 widened the order to re-pin the test that held the superseded precedence; this seat's pytest over the whole lib/research/api/tests directory with peers and filings reads 1478 passed, 0 failed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-W387-S3",
        "ff-1 AMENDMENT 2 @4cd8c70913",
        "3.0.0_SA_CVO pytest -q lib/research/api/tests lib/research/peers lib/research/filings: 1478 passed"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W387-S3 (BLOCKING, ARMED) dismissed, disarmed: ff-1 AMENDMENT 2 widened the order to re-pin the test that held the superseded precedence; this seat's pytest over the whole lib/research/api/tests directory with peers and filings reads 1478 passed, 0 failed."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S80",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:55:00Z",
    "one_line": "D1-W387-S2 (ARMED) and D1-W389-S3 (INERT) dismissed: the investigation file is many fenced blocks of one row each, not one array; every row uses that form and the row gate and this seat's compile read it whole (1064 rows parsed, 0 parse failures). The header sentence that says one block is the stale carrier, a note for the channel's owner; no row is lost or misread.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W387-S2",
      "AMGT_RESAPP-D1-W389-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W387-S2 (ARMED) and D1-W389-S3 (INERT) dismissed: the investigation file is many fenced blocks of one row each, not one array; every row uses that form and the row gate and this seat's compile read it whole (1064 rows parsed, 0 parse failures). The header sentence that says one block is the stale carrier, a note for the channel's owner; no row is lost or misread.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_RESAPP-D1-W387-S2, D1-W389-S3",
        "3.0.0_SA_CVO parse of INVESTIGATION_v1.md at d339f3f554: 1064 rows"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W387-S2 (ARMED) and D1-W389-S3 (INERT) dismissed: the investigation file is many fenced blocks of one row each, not one array; every row uses that form and the row gate and this seat's compile read it whole (1064 rows parsed, 0 parse failures). The header sentence that says one block is the stale carrier, a note for the channel's owner; no row is lost or misread."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S81",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:55:00Z",
    "one_line": "D1-W388-S1, D1-W389-S1, D1-W389-S2 and D1-W387-S1 (INERT) dismissed: the issuer's rulings stand (the nested portal repo's missing committer identity, the worktree base six drain merges ahead, the unit passed before a driver object exists, a docstring that states the name rule more narrowly than the order the code follows); none changes a verdict above.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W388-S1",
      "AMGT_RESAPP-D1-W389-S1",
      "AMGT_RESAPP-D1-W389-S2",
      "AMGT_RESAPP-D1-W387-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W388-S1, D1-W389-S1, D1-W389-S2 and D1-W387-S1 (INERT) dismissed: the issuer's rulings stand (the nested portal repo's missing committer identity, the worktree base six drain merges ahead, the unit passed before a driver object exists, a docstring that states the name rule more narrowly than the order the code follows); none changes a verdict above.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_RESAPP-D1-W388-S1, D1-W389-S1, D1-W389-S2, D1-W387-S1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W388-S1, D1-W389-S1, D1-W389-S2 and D1-W387-S1 (INERT) dismissed: the issuer's rulings stand (the nested portal repo's missing committer identity, the worktree base six drain merges ahead, the unit passed before a driver object exists, a docstring that states the name rule more narrowly than the order the code follows); none changes a verdict above."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S82",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:55:00Z",
    "one_line": "Observed off-task during the walk: 2 of 70 GET /security/<ticker>/compare calls answered HTTP 500 (ROG on the Model tab, BA on the Posture tab); the other 68, including 14 and 15 calls for those same names, answered 200, and this seat's direct invokes of the same paths answer 200. The function's log group shows 0 ERROR, Traceback, timeout or runtime-exit lines over 15:34Z-15:44Z, so the 500 is raised in front of the function (the API layer), not by it. Round 93's walk on the same tabs saw 0 API issues. Cause not read; filed for the CTO's round-95 read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Observed off-task during the walk: 2 of 70 GET /security/<ticker>/compare calls answered HTTP 500 (ROG on the Model tab, BA on the Posture tab); the other 68, including 14 and 15 calls for those same names, answered 200, and this seat's direct invokes of the same paths answer 200. The function's log group shows 0 ERROR, Traceback, timeout or runtime-exit lines over 15:34Z-15:44Z, so the 500 is raised in front of the function (the API layer), not by it. Round 93's walk on the same tabs saw 0 API issues. Cause not read; filed for the CTO's round-95 read.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "tmp/ui-walk/20261011T153440Z/netlog.tsv: compare 200 x68, 500 x2; findings.json api_issues 2",
        "3.0.0_SA_CVO lambda invoke GET /security/{ROG,BA,ROG_SW_Equity,ASML}/compare: 200 x4",
        "3.0.0_SA_CVO logs filter_log_events /aws/lambda/opal-amgt-scoped-api 15:34Z-15:44Z error pattern: 0 lines"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  }
]
```
