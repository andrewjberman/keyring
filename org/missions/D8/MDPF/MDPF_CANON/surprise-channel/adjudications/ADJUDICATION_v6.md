# MDPF_CANON -- round 5 L8/L9 adjudication, cell CN-e-1 (dell1)

<sweep_watermark>2026-10-11T07:39Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T07:39:00Z. L8 packet: 2.0.0_SA_COO~D1 msg 3610, `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round5/ROUND5_CELL_CLOSE_CN_E_1.md @41634b338f` (blob b8412f040d verified).
**L9:** CN-e-1 AC4 MET (C-S54). Nothing calls the instrument, and the verifier is not repointed; both are stated in the row.
Rows swept since v5 (watermark 07:10Z): 1, W15-S1, dismissed (C-S55). No remediation row.
The L10 slug is HELD: `org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_CANON_R5_SLUG_HELD_20261011.md`.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S54",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T07:39:00Z",
    "one_line": "MDPF_CANON.TO-CN-e-1 AC4 MET (/seams, instrument to artifact), on this seat's own runs at box/dell1 HEAD. MECHANICAL: dim_mdpf_aum_timeseries.py --out read the newest global partition at the builder's address and printed 'OK: internal identity PASS -- aggregate==2024-11-01..2026-10-08 (493 periods), 5-core sum', rc 0; reader 5 of 5 (newest partition, one get; no partition raises and reads nothing). SEMANTIC: the pre-change script (git show fc657a79b7, which reads gold/mdpf_revamp/global/aggregate_aua_timeseries.json, :53) run the same minute wrote a document BYTE-EQUAL to the new one (cmp; 320,740 B; 0 differing leaves; 5 models, 493 periods); seam 1 of 1 (2958 of 2958 cells, partition 2026-10-08). cohort_class comes from the registry: reader arm COHORT-FROM-REGISTRY passes (['model'] equals the registry's), and MISSING-CORE-STOPS shows the guard still raises by name on a frame without a core model. DECLARATIVE: the docstring (:6, :41), the --upload help text (:302) and the log strings name the gold tier, with no gold/mdpf_revamp text left; census row :15 names the gold tier and cites :101 (def latest_gold_aggregate) and :116 (the partition_uri read), both read by this seat; row :53 follows SERVED_KEY to :62, read; census check 4 of 4. Stated plainly: NOTHING CALLS THIS INSTRUMENT. This seat's census of 'dim_mdpf_aum_timeseries' over infra/, data/, lib/, .tools/ and portal/src reads 0 hits across 12088 files (binary and ephemeral-floor files not searched), while the positive controls hit (latest_gold_aggregate 3, and the dispatch names dim_mdpf_aggregate_aua_timeseries). So the repoint moves no consumed figure. Also plain: THE VERIFIER IS NOT REPOINTED. verify_mdpf_revamp_conditions.py stays on the staging tree (census :23, not examined), because four of its cells are not in the wide parquet; that is a ruling on the gold writer.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON round 5 = ledger round-4 analysis @c902dcb1b5 item 5, issuance @fc657a79b7 (decomposition v5); spine L9: graded by a seat that did none of the work.",
    "world_is": "MDPF_CANON.TO-CN-e-1 AC4 MET (/seams, instrument to artifact), on this seat's own runs at box/dell1 HEAD. MECHANICAL: dim_mdpf_aum_timeseries.py --out read the newest global partition at the builder's address and printed 'OK: internal identity PASS -- aggregate==2024-11-01..2026-10-08 (493 periods), 5-core sum', rc 0; reader 5 of 5 (newest partition, one get; no partition raises and reads nothing). SEMANTIC: the pre-change script (git show fc657a79b7, which reads gold/mdpf_revamp/global/aggregate_aua_timeseries.json, :53) run the same minute wrote a document BYTE-EQUAL to the new one (cmp; 320,740 B; 0 differing leaves; 5 models, 493 periods); seam 1 of 1 (2958 of 2958 cells, partition 2026-10-08). cohort_class comes from the registry: reader arm COHORT-FROM-REGISTRY passes (['model'] equals the registry's), and MISSING-CORE-STOPS shows the guard still raises by name on a frame without a core model. DECLARATIVE: the docstring (:6, :41), the --upload help text (:302) and the log strings name the gold tier, with no gold/mdpf_revamp text left; census row :15 names the gold tier and cites :101 (def latest_gold_aggregate) and :116 (the partition_uri read), both read by this seat; row :53 follows SERVED_KEY to :62, read; census check 4 of 4. Stated plainly: NOTHING CALLS THIS INSTRUMENT. This seat's census of 'dim_mdpf_aum_timeseries' over infra/, data/, lib/, .tools/ and portal/src reads 0 hits across 12088 files (binary and ephemeral-floor files not searched), while the positive controls hit (latest_gold_aggregate 3, and the dispatch names dim_mdpf_aggregate_aua_timeseries). So the repoint moves no consumed figure. Also plain: THE VERIFIER IS NOT REPOINTED. verify_mdpf_revamp_conditions.py stays on the staging tree (census :23, not examined), because four of its cells are not in the wide parquet; that is a ruling on the gold writer.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran data/mdpf/scripts/gold/dim_mdpf_aum_timeseries.py --out <scratch>/new.json: identity PASS, rc 0",
        "3.0.0_SA_CVO ran git show fc657a79b7:data/mdpf/scripts/gold/dim_mdpf_aum_timeseries.py --out <scratch>/old.json: cmp equal to new.json",
        "python round5/checks/r5_cn_e_1.py reader 5 of 5, seam 1 of 1; r5_cn_e_1_census.py 4 of 4",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~4/READER_CENSUS.md:15, :23, :53",
        "comp-find 'dim_mdpf_aum_timeseries' infra/ data/ lib/ .tools/ portal/src: 0 hit(s) across 12088 file(s); controls hit",
        "round5/CN_E_1_CANDIDATE_READ.md (the verifier's four cells)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "MDPF_CANON.TO-CN-e-1 AC4 MET (/seams, instrument to artifact), on this seat's own runs at box/dell1 HEAD. MECHANICAL: dim_mdpf_aum_timeseries.py --out read the newest global partition at the builder's address and printed 'OK: internal identity PASS -- aggregate==2024-11-01..2026-10-08 (493 periods), 5-core sum', rc 0; reader 5 of 5 (newest partition, one get; no partition raises and reads nothing). SEMANTIC: the pre-change script (git show fc657a79b7, which reads gold/mdpf_revamp/global/aggregate_aua_timeseries.json, :53) run the same minute wrote a document BYTE-EQUAL to the new one (cmp; 320,740 B; 0 differing leaves; 5 models, 493 periods); seam 1 of 1 (2958 of 2958 cells, partition 2026-10-08). cohort_class comes from the registry: reader arm COHORT-FROM-REGISTRY passes (['model'] equals the registry's), and MISSING-CORE-STOPS shows the guard still raises by name on a frame without a core model. DECLARATIVE: the docstring (:6, :41), the --upload help text (:302) and the log strings name the gold tier, with no gold/mdpf_revamp text left; census row :15 names the gold tier and cites :101 (def latest_gold_aggregate) and :116 (the partition_uri read), both read by this seat; row :53 follows SERVED_KEY to :62, read; census check 4 of 4. Stated plainly: NOTHING CALLS THIS INSTRUMENT. This seat's census of 'dim_mdpf_aum_timeseries' over infra/, data/, lib/, .tools/ and portal/src reads 0 hits across 12088 files (binary and ephemeral-floor files not searched), while the positive controls hit (latest_gold_aggregate 3, and the dispatch names dim_mdpf_aggregate_aua_timeseries). So the repoint moves no consumed figure. Also plain: THE VERIFIER IS NOT REPOINTED. verify_mdpf_revamp_conditions.py stays on the staging tree (census :23, not examined), because four of its cells are not in the wide parquet; that is a ruling on the gold writer."
  },
  {
    "id": "MDPF_CANON-D1-C-S55",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T07:39:00Z",
    "one_line": "D1-W15-S1 dismissed: the order's step 1 import line omitted UnknownModelError, which step 4's except clause needs; the worker imported it beside entry_for_key (:58, read by this seat). Behavior is the order's step 4, and reader 5 of 5 passes. An order-text slip, not a defect in the work.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W15-S1"
    ],
    "spec_asserts": "MDPF_CANON round 5 = ledger round-4 analysis @c902dcb1b5 item 5, issuance @fc657a79b7 (decomposition v5); spine L9: graded by a seat that did none of the work.",
    "world_is": "D1-W15-S1 dismissed: the order's step 1 import line omitted UnknownModelError, which step 4's except clause needs; the worker imported it beside entry_for_key (:58, read by this seat). Behavior is the order's step 4, and reader 5 of 5 passes. An order-text slip, not a defect in the work.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-W15-S1",
        "data/mdpf/scripts/gold/dim_mdpf_aum_timeseries.py:58"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W15-S1 dismissed: the order's step 1 import line omitted UnknownModelError, which step 4's except clause needs; the worker imported it beside entry_for_key (:58, read by this seat). Behavior is the order's step 4, and reader 5 of 5 passes. An order-text slip, not a defect in the work."
  }
]
```
