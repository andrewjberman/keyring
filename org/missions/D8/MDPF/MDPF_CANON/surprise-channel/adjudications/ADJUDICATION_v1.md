# MDPF_CANON -- round 1 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-09T21:41Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T21:41:00Z. L8 packet: 2.0.0_SA_COO~D1 msg 3220, `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round1/ROUND1_CLOSE.md`. Risk WORLD. 3 of 3 orders complete.

**L9:** CN-a-1 AC3 MET; CN-a-2 AC3 NOT MET (the live daily-path write, 'unchanged' and legacy byte-identity are unexercised); CN-a-3 AC3 MET;
FWD-1 PARTIAL (the dated question is answered from the name; daily addition, full history and the legacy second home remain).
Rows: ARMED D1-S3..S6 dismissed (disarmed, each re-read); D1-S7 dismissed; D1-S1, D1-W1-S1, D1-S2 and new D1-C-S9, D1-C-S2 graduated INERT
to `remediations/REMEDIATION_v1.md`.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S1",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T21:41:00Z",
    "one_line": "MDPF_CANON.TO-CN-a-1 AC3 MET: on the live plane each name() role (mdpf-49f-, mdpf-inf-, mdpf-cot-gold-writer-role) trusts only mdpf-gold-lambda-role and may write only its own firm's four gold prefixes, and the gold Lambda's live env carries the three ARNs; the firm bucket's DenyForeignFirmPrincipals admits the firm's role unedited.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON PRD v2.9 @12adb87963 (FWD-1, the firm gold writer contract); spine L9: graded by a seat that did none of the work.",
    "world_is": "MDPF_CANON.TO-CN-a-1 AC3 MET: on the live plane each name() role (mdpf-49f-, mdpf-inf-, mdpf-cot-gold-writer-role) trusts only mdpf-gold-lambda-role and may write only its own firm's four gold prefixes, and the gold Lambda's live env carries the three ARNs; the firm bucket's DenyForeignFirmPrincipals admits the firm's role unedited.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO aws iam get-role / get-role-policy on mdpf-49f-, mdpf-inf-, mdpf-cot-gold-writer-role (~21:4xZ): trust principal arn:aws:iam::313476888478:role/mdpf-gold-lambda-role only; inline Allow s3:PutObject,s3:GetObject on exactly the four opal-data-{firm}/mdpf/{firm}/gold/{account_distribution,account_units,aggregate_aua_timeseries,aum_metrics}/* prefixes of that firm, plus s3:ListBucket on that firm's bucket only; no attached policies; no platinum, no other firm",
        "3.0.0_SA_CVO: lib/opal_naming name('mdpf', firm, 'gold-writer', 'role') = mdpf-49f-gold-writer-role, mdpf-inf-gold-writer-role, mdpf-cot-gold-writer-role (equal to the live names)",
        "3.0.0_SA_CVO: lambda get-function-configuration mdpf-gold-lambda env GOLD_WRITER_ROLE_ARN_49FINANCIAL / _INFLECTION / _COTTONWOOD = the three ARNs (LastModified 2026-10-09T21:10:34Z); mdpf-gold-lambda-role inline sts:AssumeRole on exactly the three roles",
        "3.0.0_SA_CVO: s3api get-bucket-policy opal-data-49financial: DenyForeignFirmPrincipals ArnNotLike aws:PrincipalArn role/*-49f-* admits mdpf-49f-gold-writer-role with no edit"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard: a judgment criterion graded by a seat that did none of the work."
  },
  {
    "id": "MDPF_CANON-D1-C-S2",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T21:41:00Z",
    "one_line": "MDPF_CANON.TO-CN-a-2 AC3 NOT MET as written: the order asks that one ad-hoc QA run of the deployed gold Lambda WRITE data.parquet at address() for each built scope and artifact, that a second run read 'unchanged', and that the legacy JSON be byte-identical to a run without the change. On the live plane the qa_local run writes nothing by design (21:11:54Z: 16 of 16 green, 0 keys added); the backfill writes history through the same emitter (540 partitions, verified); but no live run of the DAILY path has written a partition, no live second run has read 'unchanged' (that arm is proven only in r1_emit.py's fake-S3 test), and no byte comparison of the legacy JSON with and without the change exists. Reading the 2026-10-10 13:30Z scheduled fire (written; then unchanged on a re-invoke of the same day; legacy JSON sha equal to the prior build's) meets it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON PRD v2.9 @12adb87963 (FWD-1, the firm gold writer contract); spine L9: graded by a seat that did none of the work.",
    "world_is": "MDPF_CANON.TO-CN-a-2 AC3 NOT MET as written: the order asks that one ad-hoc QA run of the deployed gold Lambda WRITE data.parquet at address() for each built scope and artifact, that a second run read 'unchanged', and that the legacy JSON be byte-identical to a run without the change. On the live plane the qa_local run writes nothing by design (21:11:54Z: 16 of 16 green, 0 keys added); the backfill writes history through the same emitter (540 partitions, verified); but no live run of the DAILY path has written a partition, no live second run has read 'unchanged' (that arm is proven only in r1_emit.py's fake-S3 test), and no byte comparison of the legacy JSON with and without the change exists. Reading the 2026-10-10 13:30Z scheduled fire (written; then unchanged on a re-invoke of the same day; legacy JSON sha equal to the prior build's) meets it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/critical_paths/change_management/20261009T2106Z_mdpf-stratid-r2-keyset-f3f4-dell1-20261009_deploy_completion.md F2-VERIFY: qa_local 21:11:54Z {status green, errors [], a4_objects_built 16}, 0 keys added (537 before, 537 after)",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round1/ROUND1_CLOSE.md: 'The scheduled 13:30Z floor on 2026-10-10 writes the daily path's first real partitions'",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round1/checks/r1_emit.py arm WRITE ONCE (fake S3)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard: a judgment criterion graded by a seat that did none of the work."
  },
  {
    "id": "MDPF_CANON-D1-C-S3",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T21:41:00Z",
    "one_line": "MDPF_CANON.TO-CN-a-3 AC3 MET: the backfill printed one BACKFILL n-of-m line per series with a legacy source and its tally accounts for every planned row (537 written of 537 planned, then the 3 global 10-08 rows after the fixtures were removed); the partitions it wrote are exactly the legacy dates not already present -- this seat's own date-set compare reads 16 of 16 series equal, 540 partitions, 0 missing, 0 extra; and 49 Financial's total assets on 2026-09-15 are answered from the key's date alone (mdpf/49financial/gold/aum_metrics/date=2026-09-15/data.parquet), whose 113 values equal that day's legacy object.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON PRD v2.9 @12adb87963 (FWD-1, the firm gold writer contract); spine L9: graded by a seat that did none of the work.",
    "world_is": "MDPF_CANON.TO-CN-a-3 AC3 MET: the backfill printed one BACKFILL n-of-m line per series with a legacy source and its tally accounts for every planned row (537 written of 537 planned, then the 3 global 10-08 rows after the fixtures were removed); the partitions it wrote are exactly the legacy dates not already present -- this seat's own date-set compare reads 16 of 16 series equal, 540 partitions, 0 missing, 0 extra; and 49 Financial's total assets on 2026-09-15 are answered from the key's date alone (mdpf/49financial/gold/aum_metrics/date=2026-09-15/data.parquet), whose 113 values equal that day's legacy object.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO listed (read-only, paginated) every address() gold prefix of the 16 series and the legacy opal-data-assets/portal/gold/mdpf/{scope}/{type}/{date}.json objects: DATE SETS equal on all 16 (49financial 42/44/51/0, inflection 41/58/50/0, cottonwood 34/34/42/32, global 33/37/42/0), 0 missing, 0 extra, total 540 partitions",
        "3.0.0_SA_CVO read mdpf/49financial/gold/aum_metrics/date=2026-09-15/data.parquet (113 rows) and mdpf/global/gold/aum_metrics/date=2026-09-15/data.parquet (173 rows) against their legacy JSON flattened by path: 113 of 113 and 172 of 173 values equal, 0 parquet paths missing from legacy; the one global difference is meta.fee_basis_components.cottonwood.carried, a boolean stored as text (row D1-C-S9); _provenance leaves are not carried",
        "3.0.0_SA_CVO negative control: head mdpf/49financial/gold/aum_metrics/date=2026-09-13/data.parquet (a Sunday) -> 404",
        "org/critical_paths/change_management/20261009T1958Z_mdpf-canon-r1-gold-redeploy-backfill-dell1-20261009_deploy_completion.md L4: backfill response {status backfill, planned 537, tally {written 537}} and the per-series BACKFILL lines"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard: a judgment criterion graded by a seat that did none of the work."
  },
  {
    "id": "MDPF_CANON-D1-C-S4",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T21:41:00Z",
    "one_line": "FWD-1 (THE THREAD): DONE WHEN met, ACCEPT not yet whole -- PARTIAL, not REALIZED. Met: a dated question ('what did 49 Financial's total assets read on 2026-09-15') is answered from the stored file's name alone, and the file under that name holds that day's figures (113 of 113 equal to the legacy object); every dated object of the four artifacts that the legacy tree holds now sits where address() puts it (firm bucket for firms, opal-data-mdpf for the composite; 540 of 540). Open in the ACCEPT: 'one addition per day' is unproven until the daily path writes on the 2026-10-10 13:30Z fire; 'full history' is the dated tree only -- the longer aggregate history (2024-11-01..) and account_units for 49financial, inflection and global are carried to round 2; and the legacy tree still holds the same figures in a second place.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON PRD v2.9 @12adb87963 (FWD-1, the firm gold writer contract); spine L9: graded by a seat that did none of the work.",
    "world_is": "FWD-1 (THE THREAD): DONE WHEN met, ACCEPT not yet whole -- PARTIAL, not REALIZED. Met: a dated question ('what did 49 Financial's total assets read on 2026-09-15') is answered from the stored file's name alone, and the file under that name holds that day's figures (113 of 113 equal to the legacy object); every dated object of the four artifacts that the legacy tree holds now sits where address() puts it (firm bucket for firms, opal-data-mdpf for the composite; 540 of 540). Open in the ACCEPT: 'one addition per day' is unproven until the daily path writes on the 2026-10-10 13:30Z fire; 'full history' is the dated tree only -- the longer aggregate history (2024-11-01..) and account_units for 49financial, inflection and global are carried to round 2; and the legacy tree still holds the same figures in a second place.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO listed (read-only, paginated) every address() gold prefix of the 16 series and the legacy opal-data-assets/portal/gold/mdpf/{scope}/{type}/{date}.json objects: DATE SETS equal on all 16 (49financial 42/44/51/0, inflection 41/58/50/0, cottonwood 34/34/42/32, global 33/37/42/0), 0 missing, 0 extra, total 540 partitions",
        "3.0.0_SA_CVO read mdpf/49financial/gold/aum_metrics/date=2026-09-15/data.parquet (113 rows) and mdpf/global/gold/aum_metrics/date=2026-09-15/data.parquet (173 rows) against their legacy JSON flattened by path: 113 of 113 and 172 of 173 values equal, 0 parquet paths missing from legacy; the one global difference is meta.fee_basis_components.cottonwood.carried, a boolean stored as text (row D1-C-S9); _provenance leaves are not carried",
        "3.0.0_SA_CVO negative control: head mdpf/49financial/gold/aum_metrics/date=2026-09-13/data.parquet (a Sunday) -> 404",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round1/ROUND1_CLOSE.md: 'Carried to round 2'",
        "PRD v2.9 FWD-1 DONE WHEN and ACCEPT (lines 99-110)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record of an endpoint outcome, not a hazard."
  },
  {
    "id": "MDPF_CANON-D1-C-S5",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T21:41:00Z",
    "one_line": "D1-S3 (ARMED) dismissed, disarmed: the gold package now carries opal_unidentified.py and the cottonwood and global scopes build; the live qa_local read is green, 16 of 16, errors [] (21:11:54Z).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S3"
    ],
    "spec_asserts": "MDPF_CANON PRD v2.9 @12adb87963 (FWD-1, the firm gold writer contract); spine L9: graded by a seat that did none of the work.",
    "world_is": "D1-S3 (ARMED) dismissed, disarmed: the gold package now carries opal_unidentified.py and the cottonwood and global scopes build; the live qa_local read is green, 16 of 16, errors [] (21:11:54Z).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_CANON-D1-S3, -D1-S7",
        "org/critical_paths/change_management/20261009T2106Z_mdpf-stratid-r2-keyset-f3f4-dell1-20261009_deploy_completion.md F2-VERIFY"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S3 (ARMED) dismissed, disarmed: the gold package now carries opal_unidentified.py and the cottonwood and global scopes build; the live qa_local read is green, 16 of 16, errors [] (21:11:54Z)."
  },
  {
    "id": "MDPF_CANON-D1-C-S6",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T21:41:00Z",
    "one_line": "D1-S4 (ARMED) dismissed, disarmed: the four synthetic composite partitions are gone (delete on Andrew's word, @991c4cae64) and the real 10-08 figures stand in their place -- this seat read global 10-08 aum_metrics 188 rows, account_distribution 934, aggregate_aua_timeseries 493 (written 21:25:24Z), and no account_units partition (no legacy source).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S4"
    ],
    "spec_asserts": "MDPF_CANON PRD v2.9 @12adb87963 (FWD-1, the firm gold writer contract); spine L9: graded by a seat that did none of the work.",
    "world_is": "D1-S4 (ARMED) dismissed, disarmed: the four synthetic composite partitions are gone (delete on Andrew's word, @991c4cae64) and the real 10-08 figures stand in their place -- this seat read global 10-08 aum_metrics 188 rows, account_distribution 934, aggregate_aua_timeseries 493 (written 21:25:24Z), and no account_units partition (no legacy source).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_CANON-D1-S4, -D1-S7",
        "3.0.0_SA_CVO get-object of the four opal-data-mdpf mdpf/global/gold/*/date=2026-10-08/data.parquet keys"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S4 (ARMED) dismissed, disarmed: the four synthetic composite partitions are gone (delete on Andrew's word, @991c4cae64) and the real 10-08 figures stand in their place -- this seat read global 10-08 aum_metrics 188 rows, account_distribution 934, aggregate_aua_timeseries 493 (written 21:25:24Z), and no account_units partition (no legacy source)."
  },
  {
    "id": "MDPF_CANON-D1-C-S7",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T21:41:00Z",
    "one_line": "D1-S5 (ARMED) dismissed, disarmed: MDPF_STRATID's key-set fix (@88e974ca10, live pin 79e30151a6) lets the run pass the L-1 key-set assertion; qa_local reads green 16 of 16 on the live build.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S5"
    ],
    "spec_asserts": "MDPF_CANON PRD v2.9 @12adb87963 (FWD-1, the firm gold writer contract); spine L9: graded by a seat that did none of the work.",
    "world_is": "D1-S5 (ARMED) dismissed, disarmed: MDPF_STRATID's key-set fix (@88e974ca10, live pin 79e30151a6) lets the run pass the L-1 key-set assertion; qa_local reads green 16 of 16 on the live build.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_CANON-D1-S5, -D1-S7",
        "org/critical_paths/change_management/20261009T2106Z_mdpf-stratid-r2-keyset-f3f4-dell1-20261009_deploy_completion.md F2-VERIFY and F4-VERIFY"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S5 (ARMED) dismissed, disarmed: MDPF_STRATID's key-set fix (@88e974ca10, live pin 79e30151a6) lets the run pass the L-1 key-set assertion; qa_local reads green 16 of 16 on the live build."
  },
  {
    "id": "MDPF_CANON-D1-C-S8",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T21:41:00Z",
    "one_line": "D1-S6 (ARMED) dismissed, disarmed: the composite ListBucket grant landed as AMENDMENT 4 (GoldCompositeListScoped @601f623b8c) and the composite backfill then wrote global's 112 partitions (33/37/42), date sets equal to legacy.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S6"
    ],
    "spec_asserts": "MDPF_CANON PRD v2.9 @12adb87963 (FWD-1, the firm gold writer contract); spine L9: graded by a seat that did none of the work.",
    "world_is": "D1-S6 (ARMED) dismissed, disarmed: the composite ListBucket grant landed as AMENDMENT 4 (GoldCompositeListScoped @601f623b8c) and the composite backfill then wrote global's 112 partitions (33/37/42), date sets equal to legacy.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_CANON-D1-S6, -D1-S7",
        "org/critical_paths/change_management/20261009T1958Z_mdpf-canon-r1-gold-redeploy-backfill-dell1-20261009_deploy_completion.md L4 note on AMENDMENT 4",
        "3.0.0_SA_CVO listed (read-only, paginated) every address() gold prefix of the 16 series and the legacy opal-data-assets/portal/gold/mdpf/{scope}/{type}/{date}.json objects: DATE SETS equal on all 16 (49financial 42/44/51/0, inflection 41/58/50/0, cottonwood 34/34/42/32, global 33/37/42/0), 0 missing, 0 extra, total 540 partitions"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S6 (ARMED) dismissed, disarmed: the composite ListBucket grant landed as AMENDMENT 4 (GoldCompositeListScoped @601f623b8c) and the composite backfill then wrote global's 112 partitions (33/37/42), date sets equal to legacy."
  },
  {
    "id": "MDPF_CANON-D1-C-S9",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T21:41:00Z",
    "one_line": "New observation: the parquet partition stores a JSON boolean as text -- global 2026-09-15 aum_metrics meta.fee_basis_components.cottonwood.carried is a bool in the legacy object and a str in value_text. The value reads the same, but its type is lost, and the _provenance leaves (10-11 per object) are not carried into the partition.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON PRD v2.9 M2 the emitter: the partition holds the artifact's values as written.",
    "world_is": "New observation: the parquet partition stores a JSON boolean as text -- global 2026-09-15 aum_metrics meta.fee_basis_components.cottonwood.carried is a bool in the legacy object and a str in value_text. The value reads the same, but its type is lost, and the _provenance leaves (10-11 per object) are not carried into the partition.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO read mdpf/49financial/gold/aum_metrics/date=2026-09-15/data.parquet (113 rows) and mdpf/global/gold/aum_metrics/date=2026-09-15/data.parquet (173 rows) against their legacy JSON flattened by path: 113 of 113 and 172 of 173 values equal, 0 parquet paths missing from legacy; the one global difference is meta.fee_basis_components.cottonwood.carried, a boolean stored as text (row D1-C-S9); _provenance leaves are not carried"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "INERT: no figure differs; graduated for the emitter's owner to type booleans or rule the loss."
  },
  {
    "id": "MDPF_CANON-D1-C-S10",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T21:41:00Z",
    "one_line": "D1-S7 dismissed: it is the disarm record of D1-S3..S6, each confirmed above on this seat's own reads.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S7"
    ],
    "spec_asserts": "MDPF_CANON PRD v2.9 @12adb87963 (FWD-1, the firm gold writer contract); spine L9: graded by a seat that did none of the work.",
    "world_is": "D1-S7 dismissed: it is the disarm record of D1-S3..S6, each confirmed above on this seat's own reads.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_CANON-D1-S7"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-S7 dismissed: it is the disarm record of D1-S3..S6, each confirmed above on this seat's own reads."
  }
]
```
