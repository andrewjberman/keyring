# ADVI_COTBKF: CVO adjudication, round 4

<sweep_watermark>2026-10-07T07:50Z</sweep_watermark>

Round 4 L8 compile and L9 adjudication by `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~08:4xZ. L8 input: the drain-end packet `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_4_DRAIN_END_20261007.md` @29479eeb61 (msg 94). 5 of 5 orders complete and VALID: CB-d-1 @642222e85f, CB-d-2 @c8fe590f77, CB-d-3 @aa23c85ee3, CB-d-4 @85d8b5f20f, CB-d-5 @2040c2db3f. 10 rows surfaced after the
previous watermark 2026-10-07T02:21Z (W13-S1, W14-S1, W14-S2, W14-S3, S7, S8, W12-S1, W12-S2, W12-S3, W12-S4): 5 dismissed by C-S10 below,
5 graduated in `remediations/REMEDIATION_v2.md` (W14-S1 REMEDIATED and closed; W12-S1, W12-S2, W12-S4, S7 OPEN). ARMED before: 2 (W14-S1,
W12-S1); after: W12-S1, and row S9, which this compile files and does not compile (BLOCKING, ARMED for the links apply). Judgment criteria:
CB4d1-AC3 NOT MET, CB4d2-AC3 MET, CB4d3-AC3 MET, CB4d5-AC3 not gradable until the issuer's apply; the grade file is `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_4_L9_GRADE_20261007.md`.

```json
[
 {
  "id": "ADVI_COTBKF-C-S10",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T08:45Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "ROUND 4 L9: CB4d1-AC3 NOT MET (2 USABLE buckets never listed), CB4d2-AC3 MET, CB4d3-AC3 MET, CB4d5-AC3 not gradable until the apply. Worker notes W13-S1, W14-S2, W14-S3 and W12-S3, and S8 (the disarm record for W14-S1), are dismissed.",
  "adjudicates": [
   "ADVI_COTBKF-W13-S1",
   "ADVI_COTBKF-W14-S2",
   "ADVI_COTBKF-W14-S3",
   "ADVI_COTBKF-W12-S3",
   "ADVI_COTBKF-S8"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "W13-S1: LEFT_COMMONWEALTH applies where an ended account has in-kind exit rows and no receiver; 51 of 1,450 without exit rows keep round 3's reason; the issuer reads the split as standing. W14-S2: the Cottonwood side carries no advisor id, so each near-match entry prints the Commonwealth advisor ids and the candidate's relationship id; this seat read the list and the entries are readable that way (grade file, CB4d3-AC3). W14-S3: the in-kind change moves reasons and scores, not matches (matched 439 in both rounds). W12-S3: the census reads each holdings file's own key columns, cusip where present and ticker always. S8: its effect is carried on W14-S1, which graduates closed in REMEDIATION_v2.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows ADVI_COTBKF-W13-S1, W14-S2, W14-S3, W12-S3, S8",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_4_L9_GRADE_20261007.md (the four judgment grades and their reads)",
    "ADVI_COTBKF_ROUND_4_DRAIN_END_20261007.md @29479eeb61: CROSSWALK matched=439; ACCOUNT-LINKS ended_accounts=1450 every_ended_account_listed=True"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Notes on method and output shape, each consistent with its order and read by this seat; and a disarm record whose effect is carried on the row it names."
 }
]
```
