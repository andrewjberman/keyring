# MDPF_CANON -- round 4 L9, after the un-park (dell1)

<sweep_watermark>2026-10-11T07:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T07:10:00Z. 2.0.0_SA_COO~D1 msg 3591: TO-CN-d-1 and TO-CN-d-4 complete at HEAD.
**L9:** CN-d-4 AC3 MET on re-grade (C-S52, superseding C-S40). CN-d-1 AC1 MET on this seat's run (C-S53).
Rows swept since v4 (watermark 06:56Z): 0 new. REMEDIATION_v4 (D1-S16) lands from the held file
`org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_CANON_R4_SLUG_HELD_REMEDIATION_v4_20261011.md`.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S52",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T07:10:00Z",
    "one_line": "MDPF_CANON.TO-CN-d-4 AC3 MET on re-grade. It supersedes this seat's NOT MET row MDPF_CANON-D1-C-S40 (ADJUDICATION_v4, @f334fa1334), whose one failing clause was the census row. DECLARATIVE now holds: READER_CENSUS.md (commit e019012c69, the only change since f918c9205a, +2 -1) splits the old row in two. :23 keeps verify_mdpf_revamp_conditions.py on gold/mdpf_revamp/ (cited :34, which this seat read: the legacy global key, so that row is still true) and marks it not examined in round 4. :24 names the audit on the gold tier at the builder address, citing :147 (def latest_gold_artifact) and :163 (the partition_uri read at the newest partition), both read by this seat at HEAD. r4_cn_d_4_census.py reads 4 of 4 on this seat's run. MECHANICAL and SEMANTIC stand as graded in C-S40 (the audit file is unchanged since; reader 3 of 3 and seam 2 of 2, 3388 cells per firm with unequal 0, re-run by this seat now).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-C-S40"
    ],
    "spec_asserts": "MDPF_CANON round 4 = ledger/ROUND_ANALYSIS.round3.md @ae094ea51d as re-cut by ADDENDUM 1 @187b53dbe6; CN-d-4 AMENDMENT 2 @8a6efab30a; CN-d-1 AMENDMENT 2 @742bed9e98 / @0d39789fdf; spine L9: graded by a seat that did none of the work.",
    "world_is": "MDPF_CANON.TO-CN-d-4 AC3 MET on re-grade. It supersedes this seat's NOT MET row MDPF_CANON-D1-C-S40 (ADJUDICATION_v4, @f334fa1334), whose one failing clause was the census row. DECLARATIVE now holds: READER_CENSUS.md (commit e019012c69, the only change since f918c9205a, +2 -1) splits the old row in two. :23 keeps verify_mdpf_revamp_conditions.py on gold/mdpf_revamp/ (cited :34, which this seat read: the legacy global key, so that row is still true) and marks it not examined in round 4. :24 names the audit on the gold tier at the builder address, citing :147 (def latest_gold_artifact) and :163 (the partition_uri read at the newest partition), both read by this seat at HEAD. r4_cn_d_4_census.py reads 4 of 4 on this seat's run. MECHANICAL and SEMANTIC stand as graded in C-S40 (the audit file is unchanged since; reader 3 of 3 and seam 2 of 2, 3388 cells per firm with unequal 0, re-run by this seat now).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row MDPF_CANON-D1-C-S40 (ADJUDICATION_v4)",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~4/READER_CENSUS.md:23-24 (git diff f918c9205a HEAD: +2 -1)",
        "data/mdpf/scripts/gold/mdpf_revamp_count_source_audit.py:147, :163; verify_mdpf_revamp_conditions.py:34",
        "python r4_cn_d_4_census.py: ROUND 4 CENSUS: 4 of 4 arms; r4_cn_d_4.py reader 3 of 3; seam 2 of 2"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "MDPF_CANON.TO-CN-d-4 AC3 MET on re-grade. It supersedes this seat's NOT MET row MDPF_CANON-D1-C-S40 (ADJUDICATION_v4, @f334fa1334), whose one failing clause was the census row. DECLARATIVE now holds: READER_CENSUS.md (commit e019012c69, the only change since f918c9205a, +2 -1) splits the old row in two. :23 keeps verify_mdpf_revamp_conditions.py on gold/mdpf_revamp/ (cited :34, which this seat read: the legacy global key, so that row is still true) and marks it not examined in round 4. :24 names the audit on the gold tier at the builder address, citing :147 (def latest_gold_artifact) and :163 (the partition_uri read at the newest partition), both read by this seat at HEAD. r4_cn_d_4_census.py reads 4 of 4 on this seat's run. MECHANICAL and SEMANTIC stand as graded in C-S40 (the audit file is unchanged since; reader 3 of 3 and seam 2 of 2, 3388 cells per firm with unequal 0, re-run by this seat now)."
  },
  {
    "id": "MDPF_CANON-D1-C-S53",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T07:10:00Z",
    "one_line": "MDPF_CANON.TO-CN-d-1 AC1 MET on this seat's own run at box/dell1 HEAD: r4_cn_d_1.py reads ROUND 4 IDENTITY: 6 of 6 arms. A6, the arm AMENDMENT 2 added (guard isolated), passes: on the control global=True is kept; on the planted fault global goes None, the firm scopes are unchanged and the error is recorded. A1-A5 hold (A4: the served 2026-10-08 object holds the 4-term identity on 484 non-null dates). This seat's earlier run (C-S46) read 5 of 6 before the fix landed. The order reads complete.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON round 4 = ledger/ROUND_ANALYSIS.round3.md @ae094ea51d as re-cut by ADDENDUM 1 @187b53dbe6; CN-d-4 AMENDMENT 2 @8a6efab30a; CN-d-1 AMENDMENT 2 @742bed9e98 / @0d39789fdf; spine L9: graded by a seat that did none of the work.",
    "world_is": "MDPF_CANON.TO-CN-d-1 AC1 MET on this seat's own run at box/dell1 HEAD: r4_cn_d_1.py reads ROUND 4 IDENTITY: 6 of 6 arms. A6, the arm AMENDMENT 2 added (guard isolated), passes: on the control global=True is kept; on the planted fault global goes None, the firm scopes are unchanged and the error is recorded. A1-A5 hold (A4: the served 2026-10-08 object holds the 4-term identity on 484 non-null dates). This seat's earlier run (C-S46) read 5 of 6 before the fix landed. The order reads complete.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_1.py: 6 of 6",
        "task-orders/MDPF_CANON.TO-CN-d-1.served-identity-and-cottonwood-vintage.md <status>complete</status>",
        "row MDPF_CANON-D1-C-S46"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "MDPF_CANON.TO-CN-d-1 AC1 MET on this seat's own run at box/dell1 HEAD: r4_cn_d_1.py reads ROUND 4 IDENTITY: 6 of 6 arms. A6, the arm AMENDMENT 2 added (guard isolated), passes: on the control global=True is kept; on the planted fault global goes None, the firm scopes are unchanged and the error is recorded. A1-A5 hold (A4: the served 2026-10-08 object holds the 4-term identity on 484 non-null dates). This seat's earlier run (C-S46) read 5 of 6 before the fix landed. The order reads complete."
  }
]
```
