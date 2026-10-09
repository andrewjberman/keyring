# IRPT_DASHBD -- round 1 (workstream B) L8/L9 adjudication

<sweep_watermark>2026-10-02T02:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-02 ~05:0xZ. Asked by 1.0.0_SA_CTO msg 104054. L8 input: the issuer's drain-end record deliverables/2.0.0_SA_COO~P/IRPT_DASHBD_ROUND1_B_DRAIN_END_20261002.md @cdd81865b6; the round-2 analysis @57304c750b was issued in parallel. 13 of 13 rows (watermark 0 of 13 before this compile): 8 dismissed by the 4 rows below (S1, S2, S7, S9, S10, S11, W1-S2, and W1-S1 into its successor S12); 5 graduated in remediations/REMEDIATION_v1.md, of which 3 arrive REMEDIATED and closed (S3, S4, S5) and 2 stay OPEN (S6 limb (e) and S8), both in no round-2 cell, for the CTO's addendum. Row S12 (05:05Z, item E2) is after the watermark and is not compiled here. Each issuer 'answered by ruling X' was checked finding by finding against the code at HEAD, the served gold and the contract files; the one finding a ruling does not reach is S6 limb (e).

```json
[
  {
    "id": "IRPT_DASHBD-C-S1",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T05:00:00Z",
    "one_line": "S1 and S2 are answered and done: ruling 16 removes gold from the reporting-policy register, and the two contract files S2 could not land were landed by the issuer on the seat's behalf (S2's own remedy 1).",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_DASHBD-S1",
      "IRPT_DASHBD-S2"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an issuer's 'answered by ruling X' is checked against each finding the row holds.",
    "world_is": "infra/logic/registry/reporting_policies.json at HEAD carries no gold tier and carries the platinum policy irpt-dashbd-served-reporting; org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json and IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json exist at contract_version 0.2.0.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD v0.3 ruling 16 (@c812be9885), printed at prd/IRPT_DASHBD_PRD.md:353-361: 'the eight gold tables need NO policy row; rule 30 is satisfied for them by address() and name() output alone ... The round-1 policy rows are for the PLATINUM served files only'",
        "reporting_policies.json at HEAD (this seat): the string \"gold\" absent; policy irpt-dashbd-served-reporting present",
        "amendment 4 @b116670d7c: contract files under org/standards/ are written by the DS seat and landed by the issuer; git log on the account_return_daily contract: 6a23aee53d 'contract(IRPT_DASHBD account_return_daily 0.2.0, 2.0.0_SA_COO~P on behalf of 0.4.0_DS_ClientPlatform~S)'; both contract files read contract_version 0.2.0"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S1 is out of scope by ruling 16 and the policy file holds no gold row; S2's ownership mismatch was resolved by the issuer landing the files, and both are on CLOUD."
  },
  {
    "id": "IRPT_DASHBD-C-S2",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T05:00:00Z",
    "one_line": "S9, S10 and S11 are ruled (PRD v0.5 rulings 20-21; v0.6 rulings 22-24) and the served method row and gold read as those rulings say; S11 is the correction of S10.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_DASHBD-S9",
      "IRPT_DASHBD-S10",
      "IRPT_DASHBD-S11"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an issuer's 'answered by ruling X' is checked against each finding the row holds.",
    "world_is": "Ruling 18 stands for a short-by-design book with one short-position member; the excluded-weight ceiling is derived (amendment 6); the tie-out tolerance is not adopted and no preferred convention is recorded. The served gold carries exactly that, and the count ruling 20 asked for is small: 7 of 377 outside-domain account-days carry a flow above the tolerance.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD v0.5 rulings 20-21 (prd/IRPT_DASHBD_PRD.md:404-416) and v0.6 rulings 22-24 (:429-445), printed at HEAD",
        "served gold read by this seat 2026-10-02 ~04:5xZ, s3://opal-data-49financial/irpt/49financial/gold/: dim_return_method/method_version=1 (1 row, LastModified 2026-10-01 15:12:57Z): flow_convention END, fee_basis GROSS_ONLY, tolerance 0.001244, large_flow_share 0.002535, band [-0.5, 0.5], comparability_max_excluded_weight 0.002488, tieout_tolerance_proposed 0.037, no tieout_tolerance column; account_return_daily 559 of 559 partitions, 1,105 rows, 6 accounts: return_basis TWR 1,071 / NOT_MEASURABLE 34 (no HOLDINGS_INCOME_FALLBACK), guard_state GRADED_AGREED 700 / NOT_GRADED_OUTSIDE_DOMAIN 377 / GUARD_NOT_REACHED 20 / GRADED_DISAGREED 8, emitted total_return_daily 1,071 all inside the band (min -0.0735, max 0.0484), 0 NOT_MEASURABLE rows with a number",
        "the derived ceiling checks: 0.001244 / max(|-0.5|, |0.5|) = 0.002488, the served comparability_max_excluded_weight (amendment 6 @34ae583549)",
        "ruling 20's count, from the served gold: NOT_GRADED_OUTSIDE_DOMAIN rows by account and day_quality: acct#e7ab8585 MEASURED 113 / FLOW_UNRECONCILED 1; acct#23898664 114 / NOT_MEASURABLE 1; acct#7e343f56 75 / 1; acct#37ac6e23 33 / 3; acct#a4af74fa 36 / 0 -- 7 of 377 above the tolerance",
        "row S11 corrects S10's 'identical on all five' to three of five; S10's findings stand and ruling 23 grades agreement only on like day sets (0 of 5 in round 1)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Ruled, and the served artifacts match the rulings. The like-day tie-out stays on Andrew's per-use vendor word (ruling 23), carried in the round-2 analysis, not a channel item."
  },
  {
    "id": "IRPT_DASHBD-C-S3",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T05:00:00Z",
    "one_line": "S7 corrects only the routing of S6 limb (d) (the four checks are the issuer's files), and the issuer rewrote them; W1-S2's naming refusal was accepted and the builder's scope-less key is in use.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_DASHBD-S7",
      "IRPT_DASHBD-W1-S2"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an issuer's 'answered by ruling X' is checked against each finding the row holds.",
    "world_is": "The four checks were rewritten counterexample-first on 2026-10-01 (amendment 5 (i)); the rewritten guard check passes live. The source-map keys are the scope-less builder names and the function names are the firm-scoped builder output, which the CTO's analysis checks against name().",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the issuer's rewritten check org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/p1_1_ac2_guard_seam.py (last change ea2e7145ee) run live by this seat: 40 of 559 partitions sampled, 65 rows, DB-1-AC2 PASS",
        "git log on checks/r1: p1_1_ac2_guard_seam.py, p1_2_ac2_series_link_and_plan.py, p1_3_ac1_tieout_record.py, p1_3_ac2_method_winner_written.py last changed ea2e7145ee (2026-10-01); their docstrings state a null breaks the link and 'is never read as 0.0', abs_diff 'recomputed from the row's own stated returns', the band on the emitted value",
        "amendment 1 of TO-DB-b-4 @4b45d5d089 and CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_1_B_20261002.md section 2: 'the short scope 49f is refused by the builder, as row W1-S2 found. Rule 30 holds for the publish root.'"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S7 is a routing correction whose subject is remedied; W1-S2 is a gate working as designed with the builder's name adopted."
  },
  {
    "id": "IRPT_DASHBD-C-S4",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T05:00:00Z",
    "one_line": "W1-S1 (series.json.gz has no X10 retention family) is carried into round 2 by its own successor row: the issuer filed IRPT_DASHBD-S12 at the round-2 issuance as item E2's one carried row, restating the same finding.",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_DASHBD-W1-S1"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an issuer's 'answered by ruling X' is checked against each finding the row holds.",
    "world_is": "series.json.gz still has no family (the register admits csv/json/pdf and one family per table); that is now row S12's, with disarm_owner 4.0.0_SA_CRO (the X10 register's incumbent). S12 was surfaced 2026-10-02T05:05Z, after this compile's watermark, and is compiled at the next pass.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row IRPT_DASHBD-S12 (2.0.0_SA_COO~P, 05:05Z): 'The served platinum file series.json.gz has NO retention family in the X10 register ... (row W1-S1) ... CTO round-1 analysis E2'",
        "issuance 97eaff05ff body: 'E2 is row IRPT_DASHBD-S12 (disarm_owner 4.0.0_SA_CRO, the X10 register's incumbent), not a cell'",
        "CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_1_B_20261002.md (@57304c750b) section 3, E2: 'carried as one row; not a build cell in this round. The served file is not blocked on it.'"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Superseded by S12, which carries the same finding into round 2 as item E2; one finding, one open row."
  }
]
```
