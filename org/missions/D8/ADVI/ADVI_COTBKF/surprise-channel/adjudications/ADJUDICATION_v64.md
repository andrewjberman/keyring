# ADVI_COTBKF: CVO adjudication, rounds 96-98 (and the dell1 rows of rounds 89-95) (dell1)

<sweep_watermark>2026-10-16T07:26:46Z</sweep_watermark>

`3.0.0_SA_CVO` (dell1), 2026-10-16T07:26:46Z, on 2.0.0_SA_COO~C1 msg 6576, org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/R98_DRAIN_PACKET_FOR_CVO.md @776a0edddf (sha256 5faddc7ed1d57f7f, verified).
Rows swept by id-set difference: 21 dell1 rows never named, all dispositioned here (C-S8 dismisses 20, C-S9 graduates 1). Two dell2 park rows (D2-S137, D2-S138)
are left to their owner 1.0.0_SA_CTO~DELL2, so the watermark moves for dell1 rows only.

```json
[
  {
    "id": "ADVI_COTBKF-D1-C-S7",
    "project": "ADVI_COTBKF",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T07:26:46Z",
    "one_line": "ROUNDS 96-98 L8/L9, on the served artifact: MET. No NOT_YAHOO label sits on a row priced on a Yahoo-sourced or interpolated point (0 of 3,709,042). No label sits elsewhere. Each labelled security's class matches its V2 membership (702 of 702 NOT_FOR_ACTIVE in V2, 0 of 66 INACTIVE_USE). No pre-existing value moved (every prior column equal in all three tables).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The packet's L9 items: (1) NOT_YAHOO appears on no row priced on a yahoo_finance or linear_interpolation point, and a labelled row carries the class its security's V2 membership gives (NOT_FOR_ACTIVE in the active set, INACTIVE_USE otherwise) under policy interim; (2) no pre-existing value moved.",
    "world_is": "READ BY THIS SEAT, 2026-10-16T07:2xZ. The current objects come from s3://opal-data-assets/commonwealth/cottonwood/silver/{daily_returns,account_day_value,month_grades}/date=2026-06-23/part-00000.parquet, and the prior versions by VersionId (w9j5YeV1..., qIWjLLwC..., QI5Ks8vQ...). (2) DELTA 0: rows 1,691,729 / 21,102,041 / 82,593, equal before and after. On every prior column except run_commit, the current column equals the prior column position by position (pyarrow Array.equals true on all of them). The only columns added are use_class and porting_verdict. (1) LABELS: account_day_value was joined on (cusip, date) to the regrade's price file .scratch/cotbkf_r97/regrade/after/security_day_price.parquet (2,130,163 points: yahoo_finance 1,325,110, linear_interpolation 705,133, others 99,920). Priced non-cash rows on a Yahoo-sourced or interpolated point: 3,709,042, and 0 of them are labelled NOT_YAHOO. Labelled rows on any other point: 0. CLASSES: 768 labelled securities, none with two classes. All 702 NOT_FOR_ACTIVE securities are in the V2 active set (deliverables/2.0.0_SA_COO~C2/ACTIVE_COTTONWOOD_SET_V2.csv, 3,368 cusips), and none of the 66 INACTIVE_USE securities is. porting_verdict reads UNVERIFIED on every labelled row and NOT_YAHOO elsewhere, as the packet states. SHARED DEPENDENCY, stated: the price file is the build's own input, so this read confirms the labels against that file; it does not re-derive which points are Yahoo-sourced. The served price_source column names the store, not the point source (row W187-S1), so it cannot be the instrument.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws s3 cp of the three current objects and s3api get-object of the three prior VersionIds, compared with pyarrow by this seat",
        ".scratch/cotbkf_r97/regrade/after/security_day_price.parquet (off-git, client data; never committed)",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ACTIVE_COTTONWOOD_SET_V2.csv",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/R98_DRAIN_PACKET_FOR_CVO.md @776a0edddf (sha256 5faddc7ed1d57f7f, verified)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: rounds 96-98 MET on the served artifact."
  },
  {
    "id": "ADVI_COTBKF-D1-C-S8",
    "project": "ADVI_COTBKF",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T07:26:46Z",
    "one_line": "Rounds 89-98 rows dismissed (20). The four BLOCKING rows were resolved: W178-S1/S2 by the cell completing with porting_verdict last; W185-S1 by the Yahoo cache arriving (D1-S11). W186-S1, W187-S1 and D1-S12 were resolved by the regrade (D1-S13, confirmed in C-S7). The rest are the issuer's dispositions or observations with no act. Three of this seat's remediation rows are met: C-S3, W173-S3 with D1-S2, and W170-S3 (by design, D1-S6).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D1-S6",
      "ADVI_COTBKF-D1-W178-S1",
      "ADVI_COTBKF-D1-W178-S2",
      "ADVI_COTBKF-D1-W180-S1",
      "ADVI_COTBKF-D1-W180-S2",
      "ADVI_COTBKF-D1-W180-S3",
      "ADVI_COTBKF-D1-S7",
      "ADVI_COTBKF-D1-W183-S1",
      "ADVI_COTBKF-D1-W183-S2",
      "ADVI_COTBKF-D1-S8",
      "ADVI_COTBKF-D1-W185-S1",
      "ADVI_COTBKF-D1-W185-S2",
      "ADVI_COTBKF-D1-S9",
      "ADVI_COTBKF-D1-S10",
      "ADVI_COTBKF-D1-W186-S1",
      "ADVI_COTBKF-D1-W186-S2",
      "ADVI_COTBKF-D1-S11",
      "ADVI_COTBKF-D1-S12",
      "ADVI_COTBKF-D1-W187-S1",
      "ADVI_COTBKF-D1-S13"
    ],
    "spec_asserts": "Spine L8/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence; a remediation row closes on its stated condition.",
    "world_is": "W178-S2 (BLOCKING): the served tables now end ..., run_commit, use_class, porting_verdict (schemas read here), so 'porting_verdict last' holds. W178-S1 (BLOCKING): a sparse-cone defect; the cell ran afterwards. W185-S1 (BLOCKING): the 3,580-file cache arrived from dell2 (D1-S11) and round 96 compared with it. W185-S2 and D1-S9: the served run_commit is read from the served objects. W186-S1, W187-S1 and D1-S12: price_source names the store, so the first build read NOT_YAHOO everywhere; the regrade carries the per-point source (D1-S13), confirmed by this seat's join in C-S7. W186-S2: a 1500 s bound instead of 120 s, recorded. W180-S1..S3, W183-S1/S2: form and count observations the issuer dispositioned (D1-S8). D1-S7: corrected by D1-S8 (its ARMED was an error; only W181-S1 stays live). REMEDIATION CLOSURES (this seat's rows, recorded here): C-S3 (REMEDIATION_v52) MET: data/assets/scripts/silver/cotbkf_crm_match_job.py at HEAD (fix afbd09f46e) records per member a column count, role counts and first_line_is_header, never header text; columns_used records role names; a first line that is not a header is skipped. tests/test_cotbkf_crm_match_job.py: 25 passed on this seat's run. W173-S3 and D1-S2 MET: every Yahoo-priced row now carries its use_class (C-S7). W170-S3 CLOSED BY DESIGN on the issuer's D1-S6, which cites Andrew's 10-09 word setting the hashed id list aside and the CTO's withdrawal of round-88 item 3. That word was not re-read by this seat.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "pyarrow schemas of the three current served objects (3.0.0_SA_CVO, 2026-10-16T07:2xZ)",
        "data/assets/scripts/silver/cotbkf_crm_match_job.py:301-343 at HEAD; python -m pytest data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py -> 25 passed",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/R98_DRAIN_PACKET_FOR_CVO.md @776a0edddf (sha256 5faddc7ed1d57f7f, verified)",
        "investigation rows listed in adjudicates"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each row is resolved in the world, ruled by the issuer, or a form observation; the three remediation closures are met on this seat's own reads."
  },
  {
    "id": "ADVI_COTBKF-D1-C-S9",
    "project": "ADVI_COTBKF",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T07:26:46Z",
    "one_line": "Graduated to REMEDIATION_v53: W181-S1 (ARMED, latent). read_sechist labels every row source 'sechist', and the use_class guard keys only on yahoo_finance and linear_interpolation, so a Yahoo-derived SECHIST series would read NOT_YAHOO. Its trigger is the first object under the SECHIST security_series prefix.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~C1",
    "adjudicates": [
      "ADVI_COTBKF-D1-W181-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): a live latent hazard graduates with an owner and a close condition.",
    "world_is": "Row W181-S1 and the issuer's D1-S7/D1-S8: the hazard stays ARMED with its trigger named; round 98's write did not touch it (packet section 'Open rows carried').",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_COTBKF-D1-W181-S1, D1-S7, D1-S8",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/R98_DRAIN_PACKET_FOR_CVO.md @776a0edddf (sha256 5faddc7ed1d57f7f, verified)"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation row in REMEDIATION_v53."
  }
]
```

-- 3.0.0_SA_CVO
