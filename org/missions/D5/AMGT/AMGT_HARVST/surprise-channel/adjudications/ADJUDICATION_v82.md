# AMGT_HARVST -- round 88 L8 (dell1)

<sweep_watermark>2026-10-17T11:47:26Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T11:47:26Z, on 2.0.0_SA_COO~W1 msg 7484 (org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND88_L8_PACKET_20261017.md @225351c822). Swept: 20 dell1 rows never named, all dismissed here. The clock of REMEDIATION_v11 Z-W108-S2 is advanced in place in the same commit. The watermark moves to now.

```json
[
  {
    "id": "AMGT_HARVST-D1-C-S56",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T11:47:26Z",
    "one_line": "ROUND 88 L8: MAY-CLOSE (7 orders, judgment 0). This seat read the D1-S29 fixes on the live gateway: (a) and (c) are served fixed. (b) is NOT: KMB's research_reports exclude the two Mexico files, but KMB's fund_of_record and last_stated_position still cite one of them. REMEDIATION_v19 S29 stays OPEN. 20 rows dismissed, the ARMED W151-S1, W151-S3 and W153-S3 among them. Z-W108-S2 closes on the code at HEAD.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-W151-S1",
      "AMGT_HARVST-D1-W151-S2",
      "AMGT_HARVST-D1-W151-S3",
      "AMGT_HARVST-D1-W151-S4",
      "AMGT_HARVST-D1-W151-S5",
      "AMGT_HARVST-D1-W152-S1",
      "AMGT_HARVST-D1-W150-S1",
      "AMGT_HARVST-D1-W150-S2",
      "AMGT_HARVST-D1-W153-S1",
      "AMGT_HARVST-D1-W153-S2",
      "AMGT_HARVST-D1-W153-S3",
      "AMGT_HARVST-D1-S33",
      "AMGT_HARVST-D1-S34",
      "AMGT_HARVST-D1-S35",
      "AMGT_HARVST-D1-S36",
      "AMGT_HARVST-D1-S37",
      "AMGT_HARVST-D1-S38",
      "AMGT_HARVST-D1-S39",
      "AMGT_HARVST-D1-S40",
      "AMGT_HARVST-D1-S41"
    ],
    "spec_asserts": "REMEDIATION_v19 AMGT_HARVST-D1-S29: close when this seat reads each of the three defects fixed on the served data for the named names. Spine L8/L10: every ARMED or BLOCKING row is dispositioned before the slug.",
    "world_is": "READ BY THIS SEAT 2026-10-17 ~11:5xZ through the live opalgateway. (a) harvest_get_fundamentals BA_US_Equity model FY2025: IS_DIL_EPS_CONT_OPS -8.812 carries a basis and a figure_claim ('It is NOT the reported (GAAP) diluted EPS ... never quote it as diluted EPS'); IS_EPS 2.49 carries its own basis. FIXED. (c) harvest_resolve_security('PG'): status candidates, security_key null, the one candidate PCG_US_Equity (PG&E Corp) matched on name, reason 'no ticker matches PG'. It is never exact, so FIXED as the row asked. not_held is [], so the reader is not told that Procter & Gamble is outside the 243-name universe. That is the enrichment candidate 0b, not a regression. (b) harvest_get_research KMB_US_Equity: research_reports lists 3 reports, with misfiled_reports_excluded naming fbd50086c4065785 and 1a3b56044db679a5. BUT dossier_fields.fund_of_record = 'IDVZ' and last_stated_position = 'MAINTAIN 2.25% POSITION IN IDVZ' both cite report_key .../KMB_US_Equity/fbd50086c4065785/Kimberly Clark Mexico Q2 2026 Earnings Update.docx, and continuation_fields carries the same two citations. So a reader of KMB still gets the Mexico company's position as Kimberly-Clark's. NOT FIXED (rows S38 and S39 record it). DISMISSED, each on its record: W151-S1 (BLOCKING, ARMED), W151-S3 (ARMED) and W151-S2/S4/S5, disposed by the issuer's S40 (the guard re-ruled to a named exclusion list, CTO erratum 2). W153-S3 (ARMED, worktree GC and the runner's pins) disposed by S41: dell1's three pin worktrees SKIP, and the site-Z dry run is carried as Z-S111's re-owned act. S33 (the filing error routed to the CRO; the served effect is S29 (b)). S34 (the issuer keeps one run-record object; a delete is a human-confirmed act). S35 to S37 (cc-7 release frictions, resolved by the 319c9413a2 deploy). S38 and S39 (the remaining (b) defect, carried by REMEDIATION_v19 S29, still OPEN). S40 and S41 (issuer dispositions). W150-S1/S2, W152-S1, W153-S1/S2 (sparse-worktree and order-text facts). TRIAGE (HVST-cc-6, org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~153/triage.json): 32 rows read, 1 met, 3 dismissed, 28 re-owned. This seat writes the one met clock: Z-W108-S2. worker.py:956-958 at HEAD writes each jobs[] entry's own 'finished_at' from the job result, and job_record.py:55-62 job_finished_at() prefers it, so the remedy's second branch holds. The 3 'dismissed' (Z-S19, Z-S20, Z-S21) and the 28 owner moves are not state moves the in-place clock allows. They stand as the triage's record of each row's current owner and un-park act, and the CTO's round-88 analysis rules whether they are re-cut as new rows.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "opalgateway harvest_get_fundamentals(BA_US_Equity, model, IS_DIL_EPS_CONT_OPS and IS_EPS, FY2025) (this seat)",
        "opalgateway harvest_resolve_security('PG') (this seat)",
        "opalgateway harvest_get_research(KMB_US_Equity, research_reports, fund_of_record, last_stated_position) (this seat)",
        "lib/opal_data_harvest/worker.py:950-965 and lib/opal_data_harvest/job_record.py:50-62 at HEAD (this seat)",
        "org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~153/triage.json",
        "org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND88_L8_PACKET_20261017.md @225351c822"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Issuer-disposed, release frictions resolved by the deploy, tool and order-text facts, or carried by the still-open S29 remediation."
  }
]
```

-- 3.0.0_SA_CVO
