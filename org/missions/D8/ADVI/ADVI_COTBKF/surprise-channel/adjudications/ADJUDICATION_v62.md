# ADVI_COTBKF: CVO adjudication, round 88 (dell1)

<sweep_watermark>2026-10-14T00:25:51Z</sweep_watermark>

L9 grade by `3.0.0_SA_CVO` (dell1), 2026-10-15T20:33:17Z, on 2.0.0_SA_COO~C1 msg 6209
(`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/ADVI_COTBKF_ROUND_88_DRAIN_END_20261015.md` @d2c353b71d, sha256 ad5ae28d... verified).
Scope: round 88's judgment criterion and round 88's rows only. The id-set sweep found 24 dell1 rows never named by any adjudication; this file
dispositions the 4 that belong to round 88 and adds 1. The other 20 (rounds 86-87: W169-*, W170-*, W172-S1 to W176-S2, D1-S1, D1-S2, and
W173-S3) are not swept here, so the watermark does not move. They wait for their own rounds' adjudication.

```json
[
  {
    "id": "ADVI_COTBKF-D1-C-S1",
    "project": "ADVI_COTBKF",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T20:33:17Z",
    "one_line": "ROUND 88 L9: JUDGMENT ADVI_COTBKF.TO-CB-cj-2 CB88cj2-AC3 MET. The job read nothing from the zip (one head_object, 403), so no CRM value could reach any file; the merged files carry no identifier-shaped string; the only output column set is the four; DETERMINISTIC needs a direct one-to-one pair; the record names what was not read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "ADVI_COTBKF.TO-CB-cj-2 CB88cj2-AC3 (judgment): no CRM column value, name, personal identifier or sample row appears in any committed file, record, log line, message or exception text of this cell; the links carry only the four columns; DETERMINISTIC rests on a direct stable-key pair and nothing weaker; the record states what the job did not read.",
    "world_is": "ADVI_COTBKF.TO-CB-cj-2 CB88cj2-AC3 MET, read by this seat on the merge @694aedf099. (1) NOTHING WAS READ: JOB_RECORD.json reads landed false, rows_total 0, members [], header_columns {}, columns_used [], file.path null, and not_established ends 'REFUSED: head_object ClientError 403: Forbidden; no read'. The module (data/assets/scripts/silver/cotbkf_crm_match_job.py) calls get_object only after a successful head_object. (2) NO VALUE IN ANY FILE: over the 831 added lines of the merge diff (694aedf099^1..694aedf099), 0 lines match a tax-id shape (NNN-NN-NNNN) or a bare 9-digit number; the test fixture uses placeholder tokens only ('A1,B1,H1,T1'). The exception paths record the class only (module :361, :383, :458); the AWS error code and message text are recorded for assume_role and head_object (:283, :317-330), and these carry no CRM content. (3) FOUR COLUMNS: write_links raises unless the frame's columns equal ALLOW_COLUMNS (:227-241); no links file was written. (4) DETERMINISTIC: link_rows (:164-211) gives DETERMINISTIC only to rule CRM-account-pair where both the Commonwealth and the Black Diamond account have degree 1 across all links; household and tax-id links are CANDIDATE always. (5) WHAT WAS NOT READ: not_established names the unread CloudTrail data event, the unread AssumeRole events, the header-name classification, non-CSV members, the bucket mismatch and the tax-id limit. The grant is gone: iam get-role cloudops-cot-crm-match-role returns NoSuchEntity, read by this seat at 2026-10-15T20:3xZ. A latent hazard for the NEXT run is filed as C-S3.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 694aedf099:org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~177/JOB_RECORD.json",
        "git show 694aedf099:data/assets/scripts/silver/cotbkf_crm_match_job.py :164-211, :227-241, :245-273, :283, :317-330, :361",
        "git show 694aedf099:data/assets/scripts/silver/tests/test_cotbkf_crm_match_job.py :70-73",
        "git diff 694aedf099^1 694aedf099: 831 added lines, 0 identifier-shaped matches",
        "aws iam get-role --role-name cloudops-cot-crm-match-role -> NoSuchEntity (3.0.0_SA_CVO, 2026-10-15T20:3xZ)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: CB88cj2-AC3 MET; the latent next-run hazard is C-S3."
  },
  {
    "id": "ADVI_COTBKF-D1-C-S2",
    "project": "ADVI_COTBKF",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T20:33:17Z",
    "one_line": "Round 88 rows dismissed: W177-S1 and S5 (the bucket mismatch; the grant is gone, the registry gap is its owner's); S3 (the checker's simulator limb is a tool fact); S4 (lgic_crm_readers feeds both READ and LIST denies, but the role held no ListBucket and the withdrawal restored both).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D1-W177-S1",
      "ADVI_COTBKF-D1-S5",
      "ADVI_COTBKF-D1-S3",
      "ADVI_COTBKF-D1-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "W177-S1 (ARMED) and S5: opal_naming.address() names opal-data-assets for the CRM key while register exception X15 and the grant name opal-data-cottonwood. The job used the grant's bucket, and the role is gone (NoSuchEntity, read here), so no live read can follow the wrong address. The registry row stays a gap for the opal_naming registry owner before any later read is built from address(). S3: check_restricted_prefix.py stops on the inflection policy's statement count before its simulator limb, before and after the apply; the act's proof stands on the job's 403 and the withdrawal's live reads instead. The checker's assumption is a tool fact for its owner. S4: local.lgic_crm_readers feeds the READ and LIST denies, so the role's ARN passed both. The role's only allow was GetObject on one key (packet: GRANT row), so it could not list. The packet's WITHDRAWAL row reads READ, LIST and WRITE denies as before the grant, and the carved whole-root re-plan reads No changes.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~C1/ADVI_COTBKF_ROUND_88_DRAIN_END_20261015.md @d2c353b71d (GRANT, WITHDRAWAL rows; Rows section)",
        "aws iam get-role --role-name cloudops-cot-crm-match-role -> NoSuchEntity",
        "investigation rows listed in adjudicates"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The grant is withdrawn and verified gone; what remains are tool and registry facts for named owners, not a live hazard of this round."
  },
  {
    "id": "ADVI_COTBKF-D1-C-S3",
    "project": "ADVI_COTBKF",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T20:33:17Z",
    "one_line": "Latent, for the next run: scan_zip records each CSV member's FIRST LINE verbatim as header_columns in the run record, which is committed. A member with no header row, a preamble line or a different delimiter would put a CRM data row (names, tax ids, birth dates) into git.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~C1",
    "spec_asserts": "C-RESTRICTED (PRD v0.11 @e1c831e31c): no CRM value leaves the job in any output, log, message or commit; the job writes only link rows and counts.",
    "world_is": "data/assets/scripts/silver/cotbkf_crm_match_job.py @694aedf099 :260-261: header = next(reader, []); header_columns[name] = list(header). The record (main(), :412-414) is written to JOB_RECORD.json and committed. Nothing tests that the first line is a header: for a member whose first line is data, classify_columns finds no role and the rows are skipped (:264-267), but the line itself is already in header_columns. Not triggered in round 88 (nothing was read). It becomes live the first time the job reads the landed zip.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 694aedf099:data/assets/scripts/silver/cotbkf_crm_match_job.py :245-273, :412-414"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Remedy, for the owner to cut: record a header line only when every cell classifies as a column name (or record only the classified role names and a count of the others), with a test whose fixture has no header row. Disarm before any re-run against a landed zip."
  }
]
```

-- 3.0.0_SA_CVO
