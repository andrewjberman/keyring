# AMGT_RESAPP -- round 85 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-09T14:13Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T14:13:00Z. L8 packet: 2.0.0_SA_COO~R1 msg 2516, org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85/DRAIN_END_PACKET.md @b6eac72a7c. 5 of 5 complete; real run on live HZoC2x: 0 of 123 served
sentences glued or restated, typed ASML resolves to ASML_NA_Equity, no regression. 9 rows: 5 dismissed (incl. BLOCKING D1-S13), 4 graduated
INERT to `remediations/REMEDIATION_v31.md` (incl. BLOCKING W338-S1, no served change). REMEDIATION_v29 W332-S1 (language stamp) and
REMEDIATION_v27 D1-S7 (recorder field) are REMEDIATED.

**L9 -- CTO condition 12: NU's served /thesis draft is clean** (row D1-C-S22): 38 served, 0 duplicated, 0 glued, 0 restated, 38 of 38 verbatim and cited.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S22",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T14:13:00Z",
    "one_line": "Round 85 L9 (CTO condition 12, jj-2): NU_US_Equity's served draft after the in-place repair is clean. Read on the stored object the live /thesis route serves (s3://opal-data-harvest/drafting/v1/NU_US_Equity.json, VersionId I.NWiDvQCJPaU6FLUMRycOhwkVGzWxUb, 13:19:01Z), not a signed-in page: 38 served sentences (company_description 10, investment_thesis 9, risks 9, recommendation 10; ceo_bio absent with its reason); 0 duplicated, 0 glued 'X.Y' joins, 0 restating their own text -- the round-84 doubled-sentence defect ('...in 2024.Total revenue for the year ended...') is gone; 38 of 38 verbatim in NU's latest silver filing_source excerpt (parser 2.0.0, excerpt_sha256 898afb6e..., 210,108 chars, Items 4.B / 3.D / 5); 38 of 38 carry evidence with an item + paragraph location (e.g. ITEM 5 > paragraph 250 for the US$15,774.8 million revenue line). Two sentences my repeat test flagged are genuine parallel filing sentences ('US$0.8 ... US$0.8 and US$0.8'), not restatements. Observation carried, not this criterion: the section named company_description holds 10 Item 5 financial sentences (revenue, interest income, deposits), not a description of the business; the page shows them under 'From the filing' (DSGN zzp-1), but the producer's section label is misleading.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 85 L9 (CTO condition 12, jj-2): NU_US_Equity's served draft after the in-place repair is clean. Read on the stored object the live /thesis route serves (s3://opal-data-harvest/drafting/v1/NU_US_Equity.json, VersionId I.NWiDvQCJPaU6FLUMRycOhwkVGzWxUb, 13:19:01Z), not a signed-in page: 38 served sentences (company_description 10, investment_thesis 9, risks 9, recommendation 10; ceo_bio absent with its reason); 0 duplicated, 0 glued 'X.Y' joins, 0 restating their own text -- the round-84 doubled-sentence defect ('...in 2024.Total revenue for the year ended...') is gone; 38 of 38 verbatim in NU's latest silver filing_source excerpt (parser 2.0.0, excerpt_sha256 898afb6e..., 210,108 chars, Items 4.B / 3.D / 5); 38 of 38 carry evidence with an item + paragraph location (e.g. ITEM 5 > paragraph 250 for the US$15,774.8 million revenue line). Two sentences my repeat test flagged are genuine parallel filing sentences ('US$0.8 ... US$0.8 and US$0.8'), not restatements. Observation carried, not this criterion: the section named company_description holds 10 Item 5 financial sentences (revenue, interest income, deposits), not a description of the business; the page shows them under 'From the filing' (DSGN zzp-1), but the producer's section label is misleading.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO read the served draft object and lib.research.harvest.store.silver_latest('sec','filing_source') for NU (fetched_at 2026-10-09 09:49:08Z) at 14:1xZ; counts computed over every served sentence",
        "draft denominators: sentences_drafted 40, served 38, served_on_span 38, verbatim_pass 38, with_evidence 38, refused 2",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85/DRAIN_END_PACKET.md @b6eac72a7c s.2: r85_sentences deployed YES (0 of 123 restated or glued; NU 38)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 record, not a hazard: CTO condition 12 read by a seat that did none of the work."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S23",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T14:13:00Z",
    "one_line": "W340-S1 dismissed: resolved by AMENDMENT 1 @6c93b9c2f8, which granted crosswalk.schema.json; the published list validates and r85_crosswalk reads YES.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W340-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W340-S1 dismissed: resolved by AMENDMENT 1 @6c93b9c2f8, which granted crosswalk.schema.json; the published list validates and r85_crosswalk reads YES.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-W340-S1",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85/DRAIN_END_PACKET.md @b6eac72a7c s.1 jj-3 and s.2 r85_crosswalk YES"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "W340-S1 dismissed: resolved by AMENDMENT 1 @6c93b9c2f8, which granted crosswalk.schema.json; the published list validates and r85_crosswalk reads YES."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S24",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T14:13:00Z",
    "one_line": "W338-S2 dismissed: joining blocks with a space only at a sentence end is the correct reading (a blanket space corrupts mid-sentence quote splits); the served result has 0 glued joins on this seat's read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W338-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W338-S2 dismissed: joining blocks with a space only at a sentence end is the correct reading (a blanket space corrupts mid-sentence quote splits); the served result has 0 glued joins on this seat's read.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-W338-S2",
        "this seat's count: 0 glued joins over 38 served NU sentences"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "W338-S2 dismissed: joining blocks with a space only at a sentence end is the correct reading (a blanket space corrupts mid-sentence quote splits); the served result has 0 glued joins on this seat's read."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S25",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T14:13:00Z",
    "one_line": "W341-S2 dismissed: ruled -- the CTO half's form (a versioned re-put of today's key with 2026-10-07.json's bytes, never a delete or a future-dated key) is the recorded rollback.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W341-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W341-S2 dismissed: ruled -- the CTO half's form (a versioned re-put of today's key with 2026-10-07.json's bytes, never a delete or a future-dated key) is the recorded rollback.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-W341-S2",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85/DRAIN_END_PACKET.md @b6eac72a7c s.1 jj-4 ('ruled')"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "W341-S2 dismissed: ruled -- the CTO half's form (a versioned re-put of today's key with 2026-10-07.json's bytes, never a delete or a future-dated key) is the recorded rollback."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S26",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T14:13:00Z",
    "one_line": "W339-S1 dismissed: corrected in-round -- the stale-digest first put was re-put with the right document-sha256 before the served reads; the served version is I.NWiDvQCJPaU6FLUMRycOhwkVGzWxUb (the one this seat read).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W339-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W339-S1 dismissed: corrected in-round -- the stale-digest first put was re-put with the right document-sha256 before the served reads; the served version is I.NWiDvQCJPaU6FLUMRycOhwkVGzWxUb (the one this seat read).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-W339-S1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "W339-S1 dismissed: corrected in-round -- the stale-digest first put was re-put with the right document-sha256 before the served reads; the served version is I.NWiDvQCJPaU6FLUMRycOhwkVGzWxUb (the one this seat read)."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S27",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T14:13:00Z",
    "one_line": "D1-S13 (BLOCKING) dismissed: the STOP was right and was ruled -- COO ADDENDUM 1 @734476e427 and CTO ADDENDUM 2 @22bc71e80c admitted the four identity modules on a measured 0 request-path reach; the deploy landed (live HZoC2x) and the real run reads no regression.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-S13"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "D1-S13 (BLOCKING) dismissed: the STOP was right and was ruled -- COO ADDENDUM 1 @734476e427 and CTO ADDENDUM 2 @22bc71e80c admitted the four identity modules on a measured 0 request-path reach; the deploy landed (live HZoC2x) and the real run reads no regression.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-S13",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85/DRAIN_END_PACKET.md @b6eac72a7c s.1 jj-5, s.2"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S13 (BLOCKING) dismissed: the STOP was right and was ruled -- COO ADDENDUM 1 @734476e427 and CTO ADDENDUM 2 @22bc71e80c admitted the four identity modules on a measured 0 request-path reach; the deploy landed (live HZoC2x) and the real run reads no regression."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S28",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T14:13:00Z",
    "one_line": "Remediation clocks advanced: REMEDIATION_v29 W332-S1 (language stamp) REMEDIATED -- r84_store AC1 reads all five stored 20-F sources stamped en and AC2 100% English served sentences, re-read YES 5 of 5 in this round's real run; REMEDIATION_v27 D1-S7 (recorder last_deployed_commit) REMEDIATED by jj-5 act 1 -- the recorders no longer write the top-level _last_deploy_recorded key and the last deploy is derived (r85_sourcemap YES, 183 of 235).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Remediation clocks advanced: REMEDIATION_v29 W332-S1 (language stamp) REMEDIATED -- r84_store AC1 reads all five stored 20-F sources stamped en and AC2 100% English served sentences, re-read YES 5 of 5 in this round's real run; REMEDIATION_v27 D1-S7 (recorder last_deployed_commit) REMEDIATED by jj-5 act 1 -- the recorders no longer write the top-level _last_deploy_recorded key and the last deploy is derived (r85_sourcemap YES, 183 of 235).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85/DRAIN_END_PACKET.md @b6eac72a7c s.1 jj-5 act 1 and s.2 (r84_store AC1/AC2 YES 5 of 5; r85_sourcemap YES)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Remediation clocks advanced: REMEDIATION_v29 W332-S1 (language stamp) REMEDIATED -- r84_store AC1 reads all five stored 20-F sources stamped en and AC2 100% English served sentences, re-read YES 5 of 5 in this round's real run; REMEDIATION_v27 D1-S7 (recorder last_deployed_commit) REMEDIATED by jj-5 act 1 -- the recorders no longer write the top-level _last_deploy_recorded key and the last deploy is derived (r85_sourcemap YES, 183 of 235)."
  }
]
```
