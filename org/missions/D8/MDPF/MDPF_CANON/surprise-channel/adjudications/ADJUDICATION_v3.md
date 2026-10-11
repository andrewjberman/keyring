# MDPF_CANON -- round 3 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-11T05:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T05:40:00Z. L8 packet: 2.0.0_SA_COO~D1 msg 3512, `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round3/ROUND3_CLOSE.md @8bf72ac31b`. Risk WORLD. 3 of 3 orders complete; deploy ledger CLOSED 7 of 7.

**L9:** CN-c-1 AC3 MET (C-S20); CN-c-2 AC4 MET (C-S21); CN-c-3 AC3 MET (C-S22). Each is graded on this seat's own reads and runs.
Not shown: the bytes read are those served now (9 of 12 basis objects rewritten 2026-10-09). The semantic arm uses copied history, so the
first new-home daily delivery is still to come.
Rows swept since v2 (watermark 2026-10-11T02:30Z): 15. Dismissed 8: W8-S1, W9-S1..S6, S12. Graduated 7 to `remediations/REMEDIATION_v3.md`:
S10, W8-S2 (ARMED), W8-S3 (ARMED), W8-S4, W8-S5 (ARMED), S11 and W9-S7. W8-S3 and W8-S4 are characterized here: the additive components,
and a cottonwood leg one key-date behind. C-S12 in REMEDIATION_v2 moves OPEN to REMEDIATED, closed true; its close condition is C-S20.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S20",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "MDPF_CANON.TO-CN-c-1 AC3 MET: this seat read the same twelve objects (opal-data-assets portal/gold/mdpf/{global,49financial,inflection,cottonwood}/{aum-metrics,account-distribution,aggregate-aua-timeseries}/2026-10-08.json, read-only get) and recomputed the basis with its own script under the file's stated match rules. Every min-firms integer reads back equal: headline sums 3, by_model 0, non_model_aua 1, inflection_non_model_aua 1 (as-of index 492 global/cottonwood, 483 49financial/inflection). Every single-firm entry's account count reads back equal: aggregate-aua-timeseries 10 of 20 single-firm (1,160,23,2,1,1,13,3,1,4; 10 of 10 value-equal), account-distribution 9 of 14 (1,2,1,1,13,3,1,162,23; 2 value-equal), aum-metrics 2 of 7 (160,23; 2 value-equal). The by_model histogram 2 null + 2 zero-firm + 10 one-firm + 1 two-firm + 5 three-firm = 20 and the 460 of 484 identity count also reproduce. r3_checks.py basis 3 of 3 on this seat's run. Not shown by this read: the objects' LastModified is 2026-10-09T13:31Z for 9 of 12 (the 2026-10-08 keys were rewritten by the 10-09 fire); the worker's read time is not recorded, so equality is with the bytes served now.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON round 3 = ledger/ROUND_ANALYSIS.round2.md @71e85b7191 (issuance @335258e392, amendments @96d6e08aea, @dac583381b, @608e838689); spine L9: graded by a seat that did none of the work.",
    "world_is": "MDPF_CANON.TO-CN-c-1 AC3 MET: this seat read the same twelve objects (opal-data-assets portal/gold/mdpf/{global,49financial,inflection,cottonwood}/{aum-metrics,account-distribution,aggregate-aua-timeseries}/2026-10-08.json, read-only get) and recomputed the basis with its own script under the file's stated match rules. Every min-firms integer reads back equal: headline sums 3, by_model 0, non_model_aua 1, inflection_non_model_aua 1 (as-of index 492 global/cottonwood, 483 49financial/inflection). Every single-firm entry's account count reads back equal: aggregate-aua-timeseries 10 of 20 single-firm (1,160,23,2,1,1,13,3,1,4; 10 of 10 value-equal), account-distribution 9 of 14 (1,2,1,1,13,3,1,162,23; 2 value-equal), aum-metrics 2 of 7 (160,23; 2 value-equal). The by_model histogram 2 null + 2 zero-firm + 10 one-firm + 1 two-firm + 5 three-firm = 20 and the 460 of 484 identity count also reproduce. r3_checks.py basis 3 of 3 on this seat's run. Not shown by this read: the objects' LastModified is 2026-10-09T13:31Z for 9 of 12 (the 2026-10-08 keys were rewritten by the 10-09 fire); the worker's read time is not recorded, so equality is with the bytes served now.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO s3api get-object x12 at 2026-10-11T05:18Z (ETags printed in session; e.g. global aggregate-aua-timeseries 92da1550..., LastModified 2026-10-09T13:31:41Z)",
        "3.0.0_SA_CVO script canon3_x2.py over the twelve objects: min-firms histogram {null 2, 0: 2, 1: 10, 2: 1, 3: 5}; snapshot single-firm 9 (AD) and 2 (AM)",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~8/X2_GLOBAL_BASIS.md (Field families; Single-firm entries; Method)",
        "python r3_checks.py basis: ROUND 3 BASIS: 3 of 3 arms"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "MDPF_CANON.TO-CN-c-1 AC3 MET: this seat read the same twelve objects (opal-data-assets portal/gold/mdpf/{global,49financial,inflection,cottonwood}/{aum-metrics,account-distribution,aggregate-aua-timeseries}/2026-10-08.json, read-only get) and recomputed the basis with its own script under the file's stated match rules. Every min-firms integer reads back equal: headline sums 3, by_model 0, non_model_aua 1, inflection_non_model_aua 1 (as-of index 492 global/cottonwood, 483 49financial/inflection). Every single-firm entry's account count reads back equal: aggregate-aua-timeseries 10 of 20 single-firm (1,160,23,2,1,1,13,3,1,4; 10 of 10 value-equal), account-distribution 9 of 14 (1,2,1,1,13,3,1,162,23; 2 value-equal), aum-metrics 2 of 7 (160,23; 2 value-equal). The by_model histogram 2 null + 2 zero-firm + 10 one-firm + 1 two-firm + 5 three-firm = 20 and the 460 of 484 identity count also reproduce. r3_checks.py basis 3 of 3 on this seat's run. Not shown by this read: the objects' LastModified is 2026-10-09T13:31Z for 9 of 12 (the 2026-10-08 keys were rewritten by the 10-09 fire); the worker's read time is not recorded, so equality is with the bytes served now."
  },
  {
    "id": "MDPF_CANON-D1-C-S21",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "MDPF_CANON.TO-CN-c-2 AC4 MET: one on-demand Stage-0 run (SSM f1b89351-3669-479a-868a-598939f07e92 on i-02448edb624a7a7cf: Status Success, ResponseCode 0, end 2026-10-11T05:03:02Z on this seat's get-command-invocation) wrote the nine model files and the meta at the builder's keys. This seat's listing of s3://opal-data-assets/mdpf/inflection/bronze/orion_model_composition/date=2026-10-11/ = 10 objects of 10 (model_83..89, 152, 153 + _meta/pull_complete.json, 05:02:57-05:03:03Z); the prefix equals lib/opal_naming.py address('mdpf','inflection','bronze','orion_model_composition','date=2026-10-11') printed on this seat's run. pull_complete.json reads overall success, errors [], items_per_model summing to 171. The whole builder prefix lists 1000 + 40 = 1040 objects (two pages; the CLI's length() is per page) = 1030 copied history + 10. The old home s3://opal-data-mdpf/mdpf/bronze/orion_model_composition/ carries no 2026-10-11 key. r3_checks.py writer 3 of 3, homes 3 of 3, libs 5 of 5 on this seat's run. A routine daily delivery has not yet landed (confirmation only).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON round 3 = ledger/ROUND_ANALYSIS.round2.md @71e85b7191 (issuance @335258e392, amendments @96d6e08aea, @dac583381b, @608e838689); spine L9: graded by a seat that did none of the work.",
    "world_is": "MDPF_CANON.TO-CN-c-2 AC4 MET: one on-demand Stage-0 run (SSM f1b89351-3669-479a-868a-598939f07e92 on i-02448edb624a7a7cf: Status Success, ResponseCode 0, end 2026-10-11T05:03:02Z on this seat's get-command-invocation) wrote the nine model files and the meta at the builder's keys. This seat's listing of s3://opal-data-assets/mdpf/inflection/bronze/orion_model_composition/date=2026-10-11/ = 10 objects of 10 (model_83..89, 152, 153 + _meta/pull_complete.json, 05:02:57-05:03:03Z); the prefix equals lib/opal_naming.py address('mdpf','inflection','bronze','orion_model_composition','date=2026-10-11') printed on this seat's run. pull_complete.json reads overall success, errors [], items_per_model summing to 171. The whole builder prefix lists 1000 + 40 = 1040 objects (two pages; the CLI's length() is per page) = 1030 copied history + 10. The old home s3://opal-data-mdpf/mdpf/bronze/orion_model_composition/ carries no 2026-10-11 key. r3_checks.py writer 3 of 3, homes 3 of 3, libs 5 of 5 on this seat's run. A routine daily delivery has not yet landed (confirmation only).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO aws s3api list-objects-v2 opal-data-assets prefix date=2026-10-11/ at 05:20Z: 10 keys with sizes",
        "3.0.0_SA_CVO aws ssm get-command-invocation f1b89351...: Success 0 2026-10-11T05:03:02.639Z",
        "3.0.0_SA_CVO aws s3 cp of _meta/pull_complete.json (overall success, errors [])",
        "org/critical_paths/change_management/20261011T0439Z_mdpf-canon-r3-bronze-intake-dell1-20261011_deploy_completion.md legs L2-L6 (CLOSED 20261011T050605Z)",
        "python r3_checks.py writer|homes|libs: 3/3, 3/3, 5/5"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "MDPF_CANON.TO-CN-c-2 AC4 MET: one on-demand Stage-0 run (SSM f1b89351-3669-479a-868a-598939f07e92 on i-02448edb624a7a7cf: Status Success, ResponseCode 0, end 2026-10-11T05:03:02Z on this seat's get-command-invocation) wrote the nine model files and the meta at the builder's keys. This seat's listing of s3://opal-data-assets/mdpf/inflection/bronze/orion_model_composition/date=2026-10-11/ = 10 objects of 10 (model_83..89, 152, 153 + _meta/pull_complete.json, 05:02:57-05:03:03Z); the prefix equals lib/opal_naming.py address('mdpf','inflection','bronze','orion_model_composition','date=2026-10-11') printed on this seat's run. pull_complete.json reads overall success, errors [], items_per_model summing to 171. The whole builder prefix lists 1000 + 40 = 1040 objects (two pages; the CLI's length() is per page) = 1030 copied history + 10. The old home s3://opal-data-mdpf/mdpf/bronze/orion_model_composition/ carries no 2026-10-11 key. r3_checks.py writer 3 of 3, homes 3 of 3, libs 5 of 5 on this seat's run. A routine daily delivery has not yet landed (confirmation only)."
  },
  {
    "id": "MDPF_CANON-D1-C-S22",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "MDPF_CANON.TO-CN-c-3 AC3 MET (/seams, writer to reader, on the DEPLOYED artifact). MECHANICAL: the deployed feeder and bronze_homes.json at s3://opal-data-mdpf/code/ are byte-equal to the repo (cmp on this seat's read); this seat ran the feeder with --bronze-source s3 --bronze-date 2026-10-11 and it read the pull's own partition: 9 models, 171 items (= pull_complete items_per_model), model_composition as_of 2026-10-11, weights summing to 1.0 per model. DECLARATIVE: the docstring (builder address from the generated bronze_homes.json, old home retired) matches bronze_partition_prefix(), which reads the file with no fallback; this seat's census of 'mdpf/bronze' (82 hits / 80427 files) finds no code reader of the old home, only the feeder's docstring and records, so the READER_CENSUS one-reader claim holds. SEMANTIC: this seat's run --date 2026-10-09 --eclipse-date 2026-10-09 --bronze-source s3 (new home, copied history) against the live s3://opal-data-mdpf/mdpf/feeds/*/inflection/2026-10-09.parquet (built from the old home, LastModified 2026-10-09T12:52:54Z): 171 + 578 + 1 = 750 rows, same columns, DELTA=0 on every data-bearing column after one cast; the negative control (one cell +1) fails equality in each of the three. The cast: as_of_date is datetime64[us] from this seat's pandas 3.0.6 against [ns] in the runner-built file, equal values. Not shown: a NEW-home daily delivery feeding the feeder (the semantic arm uses copied history), which arrives with the first routine fire.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON round 3 = ledger/ROUND_ANALYSIS.round2.md @71e85b7191 (issuance @335258e392, amendments @96d6e08aea, @dac583381b, @608e838689); spine L9: graded by a seat that did none of the work.",
    "world_is": "MDPF_CANON.TO-CN-c-3 AC3 MET (/seams, writer to reader, on the DEPLOYED artifact). MECHANICAL: the deployed feeder and bronze_homes.json at s3://opal-data-mdpf/code/ are byte-equal to the repo (cmp on this seat's read); this seat ran the feeder with --bronze-source s3 --bronze-date 2026-10-11 and it read the pull's own partition: 9 models, 171 items (= pull_complete items_per_model), model_composition as_of 2026-10-11, weights summing to 1.0 per model. DECLARATIVE: the docstring (builder address from the generated bronze_homes.json, old home retired) matches bronze_partition_prefix(), which reads the file with no fallback; this seat's census of 'mdpf/bronze' (82 hits / 80427 files) finds no code reader of the old home, only the feeder's docstring and records, so the READER_CENSUS one-reader claim holds. SEMANTIC: this seat's run --date 2026-10-09 --eclipse-date 2026-10-09 --bronze-source s3 (new home, copied history) against the live s3://opal-data-mdpf/mdpf/feeds/*/inflection/2026-10-09.parquet (built from the old home, LastModified 2026-10-09T12:52:54Z): 171 + 578 + 1 = 750 rows, same columns, DELTA=0 on every data-bearing column after one cast; the negative control (one cell +1) fails equality in each of the three. The cast: as_of_date is datetime64[us] from this seat's pandas 3.0.6 against [ns] in the runner-built file, equal values. Not shown: a NEW-home daily delivery feeding the feeder (the semantic arm uses copied history), which arrives with the first routine fire.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO aws s3 cp code/config/bronze_homes.json and code/scripts/gold/build_mdpf_wsc_inflection_feeder.py | cmp repo: equal",
        "3.0.0_SA_CVO ran build_mdpf_wsc_inflection_feeder.py --date 2026-10-09 --eclipse-date 2026-10-09 --bronze-source s3 --out-dir <scratch>: rc 0, 171/578/1 rows, nothing uploaded",
        "3.0.0_SA_CVO compare vs live parquets: DELTA0 True x3 after as_of_date unit cast; negative control False x3",
        "3.0.0_SA_CVO ran the feeder --bronze-date 2026-10-11: 'Orion bronze: 9 models, 171 items', rc 0",
        "comp-find 'mdpf/bronze': 82 hit(s) across 80427 file(s), HEAD 25 / SURFACED 31; no code literal of the old home",
        "python r3_checks.py reader: ROUND 3 READER: 3 of 3 arms"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "MDPF_CANON.TO-CN-c-3 AC3 MET (/seams, writer to reader, on the DEPLOYED artifact). MECHANICAL: the deployed feeder and bronze_homes.json at s3://opal-data-mdpf/code/ are byte-equal to the repo (cmp on this seat's read); this seat ran the feeder with --bronze-source s3 --bronze-date 2026-10-11 and it read the pull's own partition: 9 models, 171 items (= pull_complete items_per_model), model_composition as_of 2026-10-11, weights summing to 1.0 per model. DECLARATIVE: the docstring (builder address from the generated bronze_homes.json, old home retired) matches bronze_partition_prefix(), which reads the file with no fallback; this seat's census of 'mdpf/bronze' (82 hits / 80427 files) finds no code reader of the old home, only the feeder's docstring and records, so the READER_CENSUS one-reader claim holds. SEMANTIC: this seat's run --date 2026-10-09 --eclipse-date 2026-10-09 --bronze-source s3 (new home, copied history) against the live s3://opal-data-mdpf/mdpf/feeds/*/inflection/2026-10-09.parquet (built from the old home, LastModified 2026-10-09T12:52:54Z): 171 + 578 + 1 = 750 rows, same columns, DELTA=0 on every data-bearing column after one cast; the negative control (one cell +1) fails equality in each of the three. The cast: as_of_date is datetime64[us] from this seat's pandas 3.0.6 against [ns] in the runner-built file, equal values. Not shown: a NEW-home daily delivery feeding the feeder (the semantic arm uses copied history), which arrives with the first routine fire."
  },
  {
    "id": "MDPF_CANON-D1-C-S23",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "D1-S10 graduated INERT to REMEDIATION_v3, owner 1.0.0_SA_CTO~DELL1: the smartx value leg (fact_model_aum_daily) ends one trading day behind the T-1 frontier on every Saturday and Sunday partition (7 of 7 weekend partitions over four weekends end Thursday), so a weekend gold fire's cross-axis gate (v) refuses global. It bears on reading the 2026-10-11 and 2026-10-12 13:30Z fires for FWD-1 and on D1-S9's close condition. Taken as filed (the row's own partition read); not re-measured by this seat.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S10"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every row is dispositioned on grounded evidence before the L10 slug.",
    "world_is": "D1-S10 graduated INERT to REMEDIATION_v3, owner 1.0.0_SA_CTO~DELL1: the smartx value leg (fact_model_aum_daily) ends one trading day behind the T-1 frontier on every Saturday and Sunday partition (7 of 7 weekend partitions over four weekends end Thursday), so a weekend gold fire's cross-axis gate (v) refuses global. It bears on reading the 2026-10-11 and 2026-10-12 13:30Z fires for FWD-1 and on D1-S9's close condition. Taken as filed (the row's own partition read); not re-measured by this seat.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-S10",
        "remediation row MDPF_CANON-D1-S9 (REMEDIATION_v2)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S10 graduated INERT to REMEDIATION_v3, owner 1.0.0_SA_CTO~DELL1: the smartx value leg (fact_model_aum_daily) ends one trading day behind the T-1 frontier on every Saturday and Sunday partition (7 of 7 weekend partitions over four weekends end Thursday), so a weekend gold fire's cross-axis gate (v) refuses global. It bears on reading the 2026-10-11 and 2026-10-12 13:30Z fires for FWD-1 and on D1-S9's close condition. Taken as filed (the row's own partition read); not re-measured by this seat."
  },
  {
    "id": "MDPF_CANON-D1-C-S24",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "D1-W8-S1 dismissed: under the basis's key-match rule the single-firm count in aggregate-aua-timeseries is 10, and this seat reproduces 10 (row C-S20). The 12 the cell cited came from this seat's own round-2 grade (ADJUDICATION_v2 row C-S12: '12 single-firm, 1 two-firm, 5 three-firm' over 18 valued models). That read counted opal_growth_sma and opal_div_sma, which no firm holds at the as-of and which 49financial last held on 2026-07-17 (row W8-S2), as single-firm. The correct partition is 10 one-firm + 2 zero-firm. CN-b-2's NOT MET does not depend on 12 against 10.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W8-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every row is dispositioned on grounded evidence before the L10 slug.",
    "world_is": "D1-W8-S1 dismissed: under the basis's key-match rule the single-firm count in aggregate-aua-timeseries is 10, and this seat reproduces 10 (row C-S20). The 12 the cell cited came from this seat's own round-2 grade (ADJUDICATION_v2 row C-S12: '12 single-firm, 1 two-firm, 5 three-firm' over 18 valued models). That read counted opal_growth_sma and opal_div_sma, which no firm holds at the as-of and which 49financial last held on 2026-07-17 (row W8-S2), as single-firm. The correct partition is 10 one-firm + 2 zero-firm. CN-b-2's NOT MET does not depend on 12 against 10.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-W8-S1",
        "ADJUDICATION_v2 row MDPF_CANON-D1-C-S12",
        "row MDPF_CANON-D1-C-S20"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W8-S1 dismissed: under the basis's key-match rule the single-firm count in aggregate-aua-timeseries is 10, and this seat reproduces 10 (row C-S20). The 12 the cell cited came from this seat's own round-2 grade (ADJUDICATION_v2 row C-S12: '12 single-firm, 1 two-firm, 5 three-firm' over 18 valued models). That read counted opal_growth_sma and opal_div_sma, which no firm holds at the as-of and which 49financial last held on 2026-07-17 (row W8-S2), as single-firm. The correct partition is 10 one-firm + 2 zero-firm. CN-b-2's NOT MET does not depend on 12 against 10."
  },
  {
    "id": "MDPF_CANON-D1-C-S25",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "D1-W8-S2 graduated ARMED to REMEDIATION_v3 (owner 1.0.0_SA_CTO~DELL1 to route to the owner of the global fold): global by_model opal_growth_sma (45 accounts) and opal_div_sma (40) carry a non-null value and nonzero count at 2026-10-08 with no firm holding either; this seat's read confirms min firms 0 for both (row C-S20). The count is frozen at 49financial's 2026-07-17 value while the value moves.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W8-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every row is dispositioned on grounded evidence before the L10 slug.",
    "world_is": "D1-W8-S2 graduated ARMED to REMEDIATION_v3 (owner 1.0.0_SA_CTO~DELL1 to route to the owner of the global fold): global by_model opal_growth_sma (45 accounts) and opal_div_sma (40) carry a non-null value and nonzero count at 2026-10-08 with no firm holding either; this seat's read confirms min firms 0 for both (row C-S20). The count is frozen at 49financial's 2026-07-17 value while the value moves.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-W8-S2",
        "row MDPF_CANON-D1-C-S20"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W8-S2 graduated ARMED to REMEDIATION_v3 (owner 1.0.0_SA_CTO~DELL1 to route to the owner of the global fold): global by_model opal_growth_sma (45 accounts) and opal_div_sma (40) carry a non-null value and nonzero count at 2026-10-08 with no firm holding either; this seat's read confirms min firms 0 for both (row C-S20). The count is frozen at 49financial's 2026-07-17 value while the value moves."
  },
  {
    "id": "MDPF_CANON-D1-C-S26",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "D1-W8-S3 graduated ARMED to REMEDIATION_v3, characterized by this seat: on all 24 dates where served global opal_aggregate_aua differs from model_aua + non_model_aua (2026-08-26 .. 2026-10-08, every gap positive), the gap equals sma_additive_aua + tax_additive_aua within 0.011 (24 of 24; at 2026-10-08 the gap is 1.36% of the total, tax additive 28.8M plus SMA additive 0.41M). The served total therefore carries the declared additive components (TXA1, dim_mdpf_aggregate_aua_timeseries.py:3126-3133), and the docstring identity at :2256-2257 ('at EVERY date') is stale against the later additive step. The open question for the fold's owner: the same docstring says the front end derives the non-model band as total minus model, so if it still does, the band carries the additive components on those 24 dates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W8-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every row is dispositioned on grounded evidence before the L10 slug.",
    "world_is": "D1-W8-S3 graduated ARMED to REMEDIATION_v3, characterized by this seat: on all 24 dates where served global opal_aggregate_aua differs from model_aua + non_model_aua (2026-08-26 .. 2026-10-08, every gap positive), the gap equals sma_additive_aua + tax_additive_aua within 0.011 (24 of 24; at 2026-10-08 the gap is 1.36% of the total, tax additive 28.8M plus SMA additive 0.41M). The served total therefore carries the declared additive components (TXA1, dim_mdpf_aggregate_aua_timeseries.py:3126-3133), and the docstring identity at :2256-2257 ('at EVERY date') is stale against the later additive step. The open question for the fold's owner: the same docstring says the front end derives the non-model band as total minus model, so if it still does, the band carries the additive components on those 24 dates.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-W8-S3",
        "3.0.0_SA_CVO read of global aggregate-aua-timeseries/2026-10-08.json: failing 24, explained by sma+tax 24, sign + 24",
        "data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:2250-2262, :3126-3133, :3177"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W8-S3 graduated ARMED to REMEDIATION_v3, characterized by this seat: on all 24 dates where served global opal_aggregate_aua differs from model_aua + non_model_aua (2026-08-26 .. 2026-10-08, every gap positive), the gap equals sma_additive_aua + tax_additive_aua within 0.011 (24 of 24; at 2026-10-08 the gap is 1.36% of the total, tax additive 28.8M plus SMA additive 0.41M). The served total therefore carries the declared additive components (TXA1, dim_mdpf_aggregate_aua_timeseries.py:3126-3133), and the docstring identity at :2256-2257 ('at EVERY date') is stale against the later additive step. The open question for the fold's owner: the same docstring says the front end derives the non-model band as total minus model, so if it still does, the band carries the additive components on those 24 dates."
  },
  {
    "id": "MDPF_CANON-D1-C-S27",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "D1-W8-S4 graduated INERT to REMEDIATION_v3, cause measured by this seat: the global account-distribution keyed 2026-10-08 (generated 2026-10-08T13:31:28Z) carries the cottonwood object keyed 2026-10-07 (generated 2026-10-08T13:30:56Z, in the same fire): the 7 cottonwood-held entries' total_aum equal that object 7 of 7 and the 2026-10-08-keyed cottonwood object (generated 2026-10-09) 0 of 7. The global snapshot thus composes cottonwood one key-date behind its own label. Owner 1.0.0_SA_CTO~DELL1 to route to the account-distribution producer.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W8-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every row is dispositioned on grounded evidence before the L10 slug.",
    "world_is": "D1-W8-S4 graduated INERT to REMEDIATION_v3, cause measured by this seat: the global account-distribution keyed 2026-10-08 (generated 2026-10-08T13:31:28Z) carries the cottonwood object keyed 2026-10-07 (generated 2026-10-08T13:30:56Z, in the same fire): the 7 cottonwood-held entries' total_aum equal that object 7 of 7 and the 2026-10-08-keyed cottonwood object (generated 2026-10-09) 0 of 7. The global snapshot thus composes cottonwood one key-date behind its own label. Owner 1.0.0_SA_CTO~DELL1 to route to the account-distribution producer.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-W8-S4",
        "3.0.0_SA_CVO s3api get-object cottonwood/account-distribution/2026-10-07.json and 2026-10-08.json; generated_at compared; equality 7/7 vs 0/7"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W8-S4 graduated INERT to REMEDIATION_v3, cause measured by this seat: the global account-distribution keyed 2026-10-08 (generated 2026-10-08T13:31:28Z) carries the cottonwood object keyed 2026-10-07 (generated 2026-10-08T13:30:56Z, in the same fire): the 7 cottonwood-held entries' total_aum equal that object 7 of 7 and the 2026-10-08-keyed cottonwood object (generated 2026-10-09) 0 of 7. The global snapshot thus composes cottonwood one key-date behind its own label. Owner 1.0.0_SA_CTO~DELL1 to route to the account-distribution producer."
  },
  {
    "id": "MDPF_CANON-D1-C-S28",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "D1-W8-S5 graduated ARMED to REMEDIATION_v3, owner 1.0.0_SA_CTO~DELL1 to put to Andrew as an open call (this seat cannot address him): infra/logic/06_CONFORMANCE_LEDGER.md carries X2 GRANTED (Andrew-direct 2026-09-15) on the round-2 basis; the round-3 basis, which this seat reads back equal (row C-S20), shows min firms 0 for by_model and 1 for both non-model series. Whether the grant stands on the new basis is Andrew's.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W8-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every row is dispositioned on grounded evidence before the L10 slug.",
    "world_is": "D1-W8-S5 graduated ARMED to REMEDIATION_v3, owner 1.0.0_SA_CTO~DELL1 to put to Andrew as an open call (this seat cannot address him): infra/logic/06_CONFORMANCE_LEDGER.md carries X2 GRANTED (Andrew-direct 2026-09-15) on the round-2 basis; the round-3 basis, which this seat reads back equal (row C-S20), shows min firms 0 for by_model and 1 for both non-model series. Whether the grant stands on the new basis is Andrew's.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-W8-S5",
        "row MDPF_CANON-D1-C-S20",
        "infra/logic/06_CONFORMANCE_LEDGER.md line 136"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W8-S5 graduated ARMED to REMEDIATION_v3, owner 1.0.0_SA_CTO~DELL1 to put to Andrew as an open call (this seat cannot address him): infra/logic/06_CONFORMANCE_LEDGER.md carries X2 GRANTED (Andrew-direct 2026-09-15) on the round-2 basis; the round-3 basis, which this seat reads back equal (row C-S20), shows min firms 0 for by_model and 1 for both non-model series. Whether the grant stands on the new basis is Andrew's."
  },
  {
    "id": "MDPF_CANON-D1-C-S29",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "D1-S11 graduated INERT to REMEDIATION_v3, owner 1.0.0_SA_CTO~DELL1 (outside MDPF_CANON; LGIC_ENFORCE's round-2 fixed input): re-run by this seat at box/dell1 HEAD, org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py still reads FAIL-HEADER-STALE (data/firm_registry.json, firm-config.mjs and directory_runner.py marks ffa41913935c3281 do not hash scopes.json at HEAD), FAIL-UNDECLARED-FILE-MOVES-A-VIEW and FAIL-GENERATE-DIFFERS. The libs arm of round 3 (r6-declared-moves, r6-delta0-ordered) passes and does not read these three.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S11"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every row is dispositioned on grounded evidence before the L10 slug.",
    "world_is": "D1-S11 graduated INERT to REMEDIATION_v3, owner 1.0.0_SA_CTO~DELL1 (outside MDPF_CANON; LGIC_ENFORCE's round-2 fixed input): re-run by this seat at box/dell1 HEAD, org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py still reads FAIL-HEADER-STALE (data/firm_registry.json, firm-config.mjs and directory_runner.py marks ffa41913935c3281 do not hash scopes.json at HEAD), FAIL-UNDECLARED-FILE-MOVES-A-VIEW and FAIL-GENERATE-DIFFERS. The libs arm of round 3 (r6-declared-moves, r6-delta0-ordered) passes and does not read these three.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-S11",
        "3.0.0_SA_CVO python -I check_en_r2.py r6-headers-current|r6-undeclared-inert|r6-reproduces at 05:27Z"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S11 graduated INERT to REMEDIATION_v3, owner 1.0.0_SA_CTO~DELL1 (outside MDPF_CANON; LGIC_ENFORCE's round-2 fixed input): re-run by this seat at box/dell1 HEAD, org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py still reads FAIL-HEADER-STALE (data/firm_registry.json, firm-config.mjs and directory_runner.py marks ffa41913935c3281 do not hash scopes.json at HEAD), FAIL-UNDECLARED-FILE-MOVES-A-VIEW and FAIL-GENERATE-DIFFERS. The libs arm of round 3 (r6-declared-moves, r6-delta0-ordered) passes and does not read these three."
  },
  {
    "id": "MDPF_CANON-D1-C-S30",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "D1-W9-S1 dismissed, resolved by AMENDMENT 1 (CTO msg 3417, the generated-config shape): pull_orion_model_composition.py imports no lib module (imports :38-50 are stdlib, boto3, requests) and reads ../../config/bronze_homes.json (:62, :88); on the runner it ran exit 0 from /opt/mdpf/scripts/bronze (row C-S21).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W9-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every row is dispositioned on grounded evidence before the L10 slug.",
    "world_is": "D1-W9-S1 dismissed, resolved by AMENDMENT 1 (CTO msg 3417, the generated-config shape): pull_orion_model_composition.py imports no lib module (imports :38-50 are stdlib, boto3, requests) and reads ../../config/bronze_homes.json (:62, :88); on the runner it ran exit 0 from /opt/mdpf/scripts/bronze (row C-S21).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-W9-S1",
        "data/mdpf/scripts/bronze/pull_orion_model_composition.py:38-62",
        "row MDPF_CANON-D1-C-S21"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W9-S1 dismissed, resolved by AMENDMENT 1 (CTO msg 3417, the generated-config shape): pull_orion_model_composition.py imports no lib module (imports :38-50 are stdlib, boto3, requests) and reads ../../config/bronze_homes.json (:62, :88); on the runner it ran exit 0 from /opt/mdpf/scripts/bronze (row C-S21)."
  },
  {
    "id": "MDPF_CANON-D1-C-S31",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "D1-W9-S2 dismissed, resolved: the grant composes from the module output module.mdpf_scope_buckets.bronze_homes['orion_model_composition'] (infra/aws/terraform/mdpf-pipeline/iam.tf:69-80); r3_checks.py writer ARM 3 GRANT passes on this seat's run, and ledger leg L1 reads the two statements live on mdpf-runner-scoped.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W9-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every row is dispositioned on grounded evidence before the L10 slug.",
    "world_is": "D1-W9-S2 dismissed, resolved: the grant composes from the module output module.mdpf_scope_buckets.bronze_homes['orion_model_composition'] (infra/aws/terraform/mdpf-pipeline/iam.tf:69-80); r3_checks.py writer ARM 3 GRANT passes on this seat's run, and ledger leg L1 reads the two statements live on mdpf-runner-scoped.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-W9-S2",
        "infra/aws/terraform/mdpf-pipeline/iam.tf:69-80",
        "python r3_checks.py writer: ARM 3 GRANT PASS"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W9-S2 dismissed, resolved: the grant composes from the module output module.mdpf_scope_buckets.bronze_homes['orion_model_composition'] (infra/aws/terraform/mdpf-pipeline/iam.tf:69-80); r3_checks.py writer ARM 3 GRANT passes on this seat's run, and ledger leg L1 reads the two statements live on mdpf-runner-scoped."
  },
  {
    "id": "MDPF_CANON-D1-C-S32",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "D1-W9-S3 dismissed, resolved by AMENDMENT 2 (CTO msg 3431): .tools/gen_mdpf_bronze_homes.py does not exist; data/mdpf/config/bronze_homes.json is lib/opal_naming.py generate output (its _generated mark names registry@bd1619b411e1330c) and the code commit landed (5055246d57). r3_checks.py homes 3 of 3, including the negative arm, on this seat's run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W9-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every row is dispositioned on grounded evidence before the L10 slug.",
    "world_is": "D1-W9-S3 dismissed, resolved by AMENDMENT 2 (CTO msg 3431): .tools/gen_mdpf_bronze_homes.py does not exist; data/mdpf/config/bronze_homes.json is lib/opal_naming.py generate output (its _generated mark names registry@bd1619b411e1330c) and the code commit landed (5055246d57). r3_checks.py homes 3 of 3, including the negative arm, on this seat's run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-W9-S3",
        "data/mdpf/config/bronze_homes.json _generated",
        "python r3_checks.py homes: 3 of 3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W9-S3 dismissed, resolved by AMENDMENT 2 (CTO msg 3431): .tools/gen_mdpf_bronze_homes.py does not exist; data/mdpf/config/bronze_homes.json is lib/opal_naming.py generate output (its _generated mark names registry@bd1619b411e1330c) and the code commit landed (5055246d57). r3_checks.py homes 3 of 3, including the negative arm, on this seat's run."
  },
  {
    "id": "MDPF_CANON-D1-C-S33",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "D1-W9-S4 dismissed, resolved by AMENDMENT 3 (CTO msg 3457): lib/opal_naming.py carries no BRONZE_HOME_FEEDS literal (0 occurrences at HEAD); the feed is a registry row (infra/logic/registry/feeds.json:10, feed orion_model_composition) the renderer reads.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W9-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every row is dispositioned on grounded evidence before the L10 slug.",
    "world_is": "D1-W9-S4 dismissed, resolved by AMENDMENT 3 (CTO msg 3457): lib/opal_naming.py carries no BRONZE_HOME_FEEDS literal (0 occurrences at HEAD); the feed is a registry row (infra/logic/registry/feeds.json:10, feed orion_model_composition) the renderer reads.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-W9-S4",
        "grep -c BRONZE_HOME_FEEDS lib/opal_naming.py = 0",
        "infra/logic/registry/feeds.json:10"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W9-S4 dismissed, resolved by AMENDMENT 3 (CTO msg 3457): lib/opal_naming.py carries no BRONZE_HOME_FEEDS literal (0 occurrences at HEAD); the feed is a registry row (infra/logic/registry/feeds.json:10, feed orion_model_composition) the renderer reads."
  },
  {
    "id": "MDPF_CANON-D1-C-S34",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "D1-W9-S5 dismissed, resolved: 'lib/opal_naming.py targets' returns rc 0 on this seat's run and classifies data/mdpf/config/bronze_homes.json SHIP runner-code (measured from mdpf-daily-dispatch.sh :130); r3_checks.py libs 5 of 5.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W9-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every row is dispositioned on grounded evidence before the L10 slug.",
    "world_is": "D1-W9-S5 dismissed, resolved: 'lib/opal_naming.py targets' returns rc 0 on this seat's run and classifies data/mdpf/config/bronze_homes.json SHIP runner-code (measured from mdpf-daily-dispatch.sh :130); r3_checks.py libs 5 of 5.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-W9-S5",
        "python lib/opal_naming.py targets: rc=0",
        "python r3_checks.py libs: 5 of 5"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W9-S5 dismissed, resolved: 'lib/opal_naming.py targets' returns rc 0 on this seat's run and classifies data/mdpf/config/bronze_homes.json SHIP runner-code (measured from mdpf-daily-dispatch.sh :130); r3_checks.py libs 5 of 5."
  },
  {
    "id": "MDPF_CANON-D1-C-S35",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "D1-W9-S6 dismissed: the committed infra/aws/terraform/modules/opal_name/generated_locals.tf now carries the four '4698' keys the generator writes (4 lines at HEAD), so HEAD equals generator output; the drift predated round 3 and the regeneration resolves it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W9-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every row is dispositioned on grounded evidence before the L10 slug.",
    "world_is": "D1-W9-S6 dismissed: the committed infra/aws/terraform/modules/opal_name/generated_locals.tf now carries the four '4698' keys the generator writes (4 lines at HEAD), so HEAD equals generator output; the drift predated round 3 and the regeneration resolves it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-W9-S6",
        "grep -c 4698 generated_locals.tf = 4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W9-S6 dismissed: the committed infra/aws/terraform/modules/opal_name/generated_locals.tf now carries the four '4698' keys the generator writes (4 lines at HEAD), so HEAD equals generator output; the drift predated round 3 and the regeneration resolves it."
  },
  {
    "id": "MDPF_CANON-D1-C-S36",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "D1-W9-S7 graduated INERT to REMEDIATION_v3 (owner 1.0.0_SA_CTO~DELL1): its disarm condition, the hand sync before the first post-deploy daily run, is met (row C-S37; this seat measured bronze_homes.json and the feeder at code/ byte-equal to the repo). What stays open is structural: no tracked script writes s3://opal-data-mdpf/code/, so the runner's code reaches it only by hand (iam.tf :196 notes the prefix about 20 commits behind HEAD); whether to automate the repo-to-code copy is a CTO or CloudOps ruling.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W9-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every row is dispositioned on grounded evidence before the L10 slug.",
    "world_is": "D1-W9-S7 graduated INERT to REMEDIATION_v3 (owner 1.0.0_SA_CTO~DELL1): its disarm condition, the hand sync before the first post-deploy daily run, is met (row C-S37; this seat measured bronze_homes.json and the feeder at code/ byte-equal to the repo). What stays open is structural: no tracked script writes s3://opal-data-mdpf/code/, so the runner's code reaches it only by hand (iam.tf :196 notes the prefix about 20 commits behind HEAD); whether to automate the repo-to-code copy is a CTO or CloudOps ruling.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-W9-S7",
        "investigation row MDPF_CANON-D1-S12",
        "3.0.0_SA_CVO cmp of code/config/bronze_homes.json and code/scripts/gold/build_mdpf_wsc_inflection_feeder.py: equal"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W9-S7 graduated INERT to REMEDIATION_v3 (owner 1.0.0_SA_CTO~DELL1): its disarm condition, the hand sync before the first post-deploy daily run, is met (row C-S37; this seat measured bronze_homes.json and the feeder at code/ byte-equal to the repo). What stays open is structural: no tracked script writes s3://opal-data-mdpf/code/, so the runner's code reaches it only by hand (iam.tf :196 notes the prefix about 20 commits behind HEAD); whether to automate the repo-to-code copy is a CTO or CloudOps ruling."
  },
  {
    "id": "MDPF_CANON-D1-C-S37",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:40:00Z",
    "one_line": "D1-S12 dismissed, confirmed: this seat measured the hand sync (two of the three code/ objects byte-equal to the repo by cmp; the pull script's live ETag e64b70fe... matches ledger leg L4), the pull's 10 of 10 objects at the builder's keys, and its own DELTA=0 feeder read (rows C-S21, C-S22).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S12"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every row is dispositioned on grounded evidence before the L10 slug.",
    "world_is": "D1-S12 dismissed, confirmed: this seat measured the hand sync (two of the three code/ objects byte-equal to the repo by cmp; the pull script's live ETag e64b70fe... matches ledger leg L4), the pull's 10 of 10 objects at the builder's keys, and its own DELTA=0 feeder read (rows C-S21, C-S22).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-S12",
        "rows MDPF_CANON-D1-C-S21 and C-S22"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S12 dismissed, confirmed: this seat measured the hand sync (two of the three code/ objects byte-equal to the repo by cmp; the pull script's live ETag e64b70fe... matches ledger leg L4), the pull's 10 of 10 objects at the builder's keys, and its own DELTA=0 feeder read (rows C-S21, C-S22)."
  }
]
```
