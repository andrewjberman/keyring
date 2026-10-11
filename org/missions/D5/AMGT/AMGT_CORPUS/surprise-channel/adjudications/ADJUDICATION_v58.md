# AMGT_CORPUS -- round 45 L9 on FWD-1, FWD-14 and TO-WRITE-R45-au1 AC5; ADJUDICATION_v55 C-S22 superseded; D1-S3 held (dell1)

<sweep_watermark>2026-10-11T10:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T10:40:00Z. Asked by 2.0.0_SA_COO~C1 msg 3737 (packet
`deliverables/2.0.0_SA_COO~C1/ROUND45_GRADED_READS_PACKET.md` @59da914a74, blob 56139e87fa verified). FWD-1 MET on the 368 files
the folder list resolves to, the count the PRD binds (the drive's 378 printed beside it). FWD-14 MET. au1-AC5 PASS. v55 C-S22 is
superseded (C-S33). D1-S3 graduation prepared and HELD (C-S34): the gate reads a stale transport copy of the at-4 order as pending. Rows surfaced since v57's watermark (10:05Z): 0 of 188.
No L10 slug: FWD-10 is still ungraded (the IMB LN walk, au-7, is owed), and round-close-check --round 45 counts 0 orders (the
TO-WRITE-R45-au1 order is not keyed to round 45), so its MAY-CLOSE is vacuous.

```json
[
  {
    "id": "AMGT_CORPUS-D1-C-S30",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T10:40:00Z",
    "one_line": "FWD-1 MET on the count the PRD binds. PRD:194-197 DONE WHEN: 'for every file the library's own folder list resolves to, the stored object is re-opened and matches the file on the synced drive byte for byte, and the count of objects equals the count of files scanned, both printed'. The scope is the files the folder list RESOLVES to, so the count is 368, not the drive's 378 (ROUND_ANALYSIS.round44.md:32 reads 'objects = files = 378'; the PRD binds). Both numbers: drive 378 files in 102 folders = 368 in 96 resolved folders + 10 in 6 folders crosswalk/v1 does not resolve, each named with its reason (Brookfield BN CA 1, Formatting examples 5, ITOCHU 8001 JP 1, Japan Tobacco 2914 JP 1, Mitsubishi Corp 8058 JP 1, Mizuho 8411 JP 1). This seat's reads: the store holds exactly 368 objects, equal to the evidence's 368 keys with 0 extra; every object's bytes hash to the report_id in its key, 368 of 368, which is the sha256 the ingest computed from the drive file at write. The drive-side byte match itself is the executor's --verify at site Z (objects 368 files 368 match 368 mismatch 0); the synced drive is not readable from dell1, so it was not re-run here.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every judgment is graded by a seat that did none of the work, on grounded evidence.",
    "world_is": "FWD-1 MET on the count the PRD binds. PRD:194-197 DONE WHEN: 'for every file the library's own folder list resolves to, the stored object is re-opened and matches the file on the synced drive byte for byte, and the count of objects equals the count of files scanned, both printed'. The scope is the files the folder list RESOLVES to, so the count is 368, not the drive's 378 (ROUND_ANALYSIS.round44.md:32 reads 'objects = files = 378'; the PRD binds). Both numbers: drive 378 files in 102 folders = 368 in 96 resolved folders + 10 in 6 folders crosswalk/v1 does not resolve, each named with its reason (Brookfield BN CA 1, Formatting examples 5, ITOCHU 8001 JP 1, Japan Tobacco 2914 JP 1, Mitsubishi Corp 8058 JP 1, Mizuho 8411 JP 1). This seat's reads: the store holds exactly 368 objects, equal to the evidence's 368 keys with 0 extra; every object's bytes hash to the report_id in its key, 368 of 368, which is the sha256 the ingest computed from the drive file at write. The drive-side byte match itself is the executor's --verify at site Z (objects 368 files 368 match 368 mismatch 0); the synced drive is not readable from dell1, so it was not re-run here.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO re-ran AC1-AC4 on the evidence bytes: AC1 1; AC2 'au1 accounting census 378 resolved 368 unresolved 10 objects 368 identity OK'; AC3 2; AC4 1",
        "3.0.0_SA_CVO paginated list of s3://opal-data-harvest/amgt/harvest/bronze/research-report/ 2026-10-11T10:2xZ: 368 objects, 368 of 368 evidence keys present, 0 store keys not in the evidence",
        "3.0.0_SA_CVO streamed all 368 objects (312,748,396 bytes) and compared sha256[:16] to the report_id in each key (lib/research/corpus/ingest.py:16, :158-159): 368 equal, 0 mismatch",
        "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~ZC/evidence/r45_au1_bronze_ingest_and_four_count_sitez.txt @cc1f7b2dfa (blob e9c856a86b, equal at origin/box/sitez a010dd8a8e; not in box/dell1 HEAD, read by git show): '## ingest --verify ... objects 368 files 368 match 368 mismatch 0'",
        "org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md:194-197 (printed at HEAD)",
        "org/missions/D5/AMGT/AMGT_CORPUS/ledger/ROUND_ANALYSIS.round44.md:32 (printed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "FWD-1 MET on the count the PRD binds. PRD:194-197 DONE WHEN: 'for every file the library's own folder list resolves to, the stored object is re-opened and matches the file on the synced drive byte for byte, and the count of objects equals the count of files scanned, both printed'. The scope is the files the folder list RESOLVES to, so the count is 368, not the drive's 378 (ROUND_ANALYSIS.round44.md:32 reads 'objects = files = 378'; the PRD binds). Both numbers: drive 378 files in 102 folders = 368 in 96 resolved folders + 10 in 6 folders crosswalk/v1 does not resolve, each named with its reason (Brookfield BN CA 1, Formatting examples 5, ITOCHU 8001 JP 1, Japan Tobacco 2914 JP 1, Mitsubishi Corp 8058 JP 1, Mizuho 8411 JP 1). This seat's reads: the store holds exactly 368 objects, equal to the evidence's 368 keys with 0 extra; every object's bytes hash to the report_id in its key, 368 of 368, which is the sha256 the ingest computed from the drive file at write. The drive-side byte match itself is the executor's --verify at site Z (objects 368 files 368 match 368 mismatch 0); the synced drive is not readable from dell1, so it was not re-run here."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S31",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T10:40:00Z",
    "one_line": "FWD-14 MET. PRD:469-471 DONE WHEN: 'for a named folder the read returns a dossier or a reason; and the three counts (resolved / ambiguous / empty-or-workbook-only) SUM TO THE FOLDER COUNT every time', AMENDED to four counts at :474-477 (adding unresolved-with-reason). The evidence prints 'fence14 resolved 84 ambiguous 0 empty-or-workbook-only 12 unresolved-with-reason 6 sum 102 folders_read 102' before and after the write (AC3 2 on this seat's re-run), and the partition is consistent with the write: 84 + 12 = 96 resolved folders = 95 with stored files + 1 empty (Air Liquide AI FP); the store's 95 security keys equal the evidence's 95 (BP and NG written -SLASH- in the key). The named-folder arm: 95 of 95 resolved keys return a dossier on the live function (ADJUDICATION_v57 census), and the 6 unresolved folders print the crosswalk reason. Limit: the four-count census ran at site Z against the drive's folder list; this seat re-ran its line check and corroborated the resolved side from the store, not the census itself.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every judgment is graded by a seat that did none of the work, on grounded evidence.",
    "world_is": "FWD-14 MET. PRD:469-471 DONE WHEN: 'for a named folder the read returns a dossier or a reason; and the three counts (resolved / ambiguous / empty-or-workbook-only) SUM TO THE FOLDER COUNT every time', AMENDED to four counts at :474-477 (adding unresolved-with-reason). The evidence prints 'fence14 resolved 84 ambiguous 0 empty-or-workbook-only 12 unresolved-with-reason 6 sum 102 folders_read 102' before and after the write (AC3 2 on this seat's re-run), and the partition is consistent with the write: 84 + 12 = 96 resolved folders = 95 with stored files + 1 empty (Air Liquide AI FP); the store's 95 security keys equal the evidence's 95 (BP and NG written -SLASH- in the key). The named-folder arm: 95 of 95 resolved keys return a dossier on the live function (ADJUDICATION_v57 census), and the 6 unresolved folders print the crosswalk reason. Limit: the four-count census ran at site Z against the drive's folder list; this seat re-ran its line check and corroborated the resolved side from the store, not the census itself.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO re-ran AC1-AC4 on the evidence bytes: AC1 1; AC2 'au1 accounting census 378 resolved 368 unresolved 10 objects 368 identity OK'; AC3 2; AC4 1",
        "3.0.0_SA_CVO paginated list of s3://opal-data-harvest/amgt/harvest/bronze/research-report/ 2026-10-11T10:2xZ: 368 objects, 368 of 368 evidence keys present, 0 store keys not in the evidence",
        "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~ZC/evidence/r45_au1_bronze_ingest_and_four_count_sitez.txt @cc1f7b2dfa (blob e9c856a86b, equal at origin/box/sitez a010dd8a8e; not in box/dell1 HEAD, read by git show) lines 22 and 490 (fence14) and 23-28 (the six reasons)",
        "org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md:469-477 (printed at HEAD)",
        "adjudication row AMGT_CORPUS-D1-C-S25 grounding (live /thesis 95 of 95)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "FWD-14 MET. PRD:469-471 DONE WHEN: 'for a named folder the read returns a dossier or a reason; and the three counts (resolved / ambiguous / empty-or-workbook-only) SUM TO THE FOLDER COUNT every time', AMENDED to four counts at :474-477 (adding unresolved-with-reason). The evidence prints 'fence14 resolved 84 ambiguous 0 empty-or-workbook-only 12 unresolved-with-reason 6 sum 102 folders_read 102' before and after the write (AC3 2 on this seat's re-run), and the partition is consistent with the write: 84 + 12 = 96 resolved folders = 95 with stored files + 1 empty (Air Liquide AI FP); the store's 95 security keys equal the evidence's 95 (BP and NG written -SLASH- in the key). The named-folder arm: 95 of 95 resolved keys return a dossier on the live function (ADJUDICATION_v57 census), and the 6 unresolved folders print the crosswalk reason. Limit: the four-count census ran at site Z against the drive's folder list; this seat re-ran its line check and corroborated the resolved side from the store, not the census itself."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S32",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T10:40:00Z",
    "one_line": "Grade record: TO-WRITE-R45-au1 AC5 (JUDGMENT, 'FWD-1 reads as the PRD's DONE WHEN says, with the unresolved remainder named') PASS. The write stored every resolved-folder file (368 of 368, 12 new write-once keys, each LastModified inside the run window 09:55:23Z-09:59:50Z), the store's bytes are content-true on this seat's hash of all 368, and the 10 unresolved files are named per file with the crosswalk reason, never guessed. Rows C-S30 and C-S31 carry the readings.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grades": [
      {
        "criterion": "au1-AC5",
        "instance": "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/AMGT_CORPUS.TO-WRITE-R45-au1.bronze-ingest-and-four-count-sitez.proof_of_spec.json@79c9e7babb",
        "verdict": "PASS",
        "reason": "FWD-1 reads on the 368 files the folder list resolves to (PRD:194-197): store 368 = files 368, 368 of 368 content-true on this seat's hash, the executor's verify match 368 mismatch 0, and the 10 unresolved files in 6 folders named with their crosswalk reason."
      }
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every judgment is graded by a seat that did none of the work, on grounded evidence.",
    "world_is": "Grade record: TO-WRITE-R45-au1 AC5 (JUDGMENT, 'FWD-1 reads as the PRD's DONE WHEN says, with the unresolved remainder named') PASS. The write stored every resolved-folder file (368 of 368, 12 new write-once keys, each LastModified inside the run window 09:55:23Z-09:59:50Z), the store's bytes are content-true on this seat's hash of all 368, and the 10 unresolved files are named per file with the crosswalk reason, never guessed. Rows C-S30 and C-S31 carry the readings.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/AMGT_CORPUS.TO-WRITE-R45-au1.bronze-ingest-and-four-count-sitez.proof_of_spec.json@79c9e7babb",
        "3.0.0_SA_CVO re-ran AC1-AC4 on the evidence bytes: AC1 1; AC2 'au1 accounting census 378 resolved 368 unresolved 10 objects 368 identity OK'; AC3 2; AC4 1",
        "3.0.0_SA_CVO paginated list of s3://opal-data-harvest/amgt/harvest/bronze/research-report/ 2026-10-11T10:2xZ: 368 objects, 368 of 368 evidence keys present, 0 store keys not in the evidence",
        "3.0.0_SA_CVO streamed all 368 objects (312,748,396 bytes) and compared sha256[:16] to the report_id in each key (lib/research/corpus/ingest.py:16, :158-159): 368 equal, 0 mismatch",
        "3.0.0_SA_CVO head-object of the 12 put_performed keys: GOOGL x2, 6501 JP x3, NU, 8316 JP x2, 8035 JP, 8766 JP, ZTS x2; LastModified 09:55:23Z to 09:59:50Z"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record: TO-WRITE-R45-au1 AC5 (JUDGMENT, 'FWD-1 reads as the PRD's DONE WHEN says, with the unresolved remainder named') PASS. The write stored every resolved-folder file (368 of 368, 12 new write-once keys, each LastModified inside the run window 09:55:23Z-09:59:50Z), the store's bytes are content-true on this seat's hash of all 368, and the 10 unresolved files are named per file with the crosswalk reason, never guessed. Rows C-S30 and C-S31 carry the readings."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S33",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T10:40:00Z",
    "one_line": "ADJUDICATION_v55 C-S22 (CRPS-at-4 AC2 NOT MET: store 356 vs drive 378) is SUPERSEDED. Of the 22 drive files C-S22 counted as missing, 12 were resolved-folder files not yet stored (the 11 OneDrive placeholders hydrated on read and 1 more), and round 45 stored all 12; the other 10 sit in 6 folders crosswalk/v1 does not resolve, which FWD-1's DONE WHEN (files the folder list resolves to) does not cover. C-S22 graded against the census's 378, wider than the PRD binds; that part of its reasoning was this seat's error. Its finding that the store was short of the resolved files was right at its read, and is now closed: 368 of 368.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-C-S22"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): a grade is corrected by a NEW row citing the old one, never by an edit in place.",
    "world_is": "ADJUDICATION_v55 C-S22 (CRPS-at-4 AC2 NOT MET: store 356 vs drive 378) is SUPERSEDED. Of the 22 drive files C-S22 counted as missing, 12 were resolved-folder files not yet stored (the 11 OneDrive placeholders hydrated on read and 1 more), and round 45 stored all 12; the other 10 sit in 6 folders crosswalk/v1 does not resolve, which FWD-1's DONE WHEN (files the folder list resolves to) does not cover. C-S22 graded against the census's 378, wider than the PRD binds; that part of its reasoning was this seat's error. Its finding that the store was short of the resolved files was right at its read, and is now closed: 368 of 368.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/adjudications/ADJUDICATION_v55.md row AMGT_CORPUS-D1-C-S22",
        "adjudication row AMGT_CORPUS-D1-C-S30",
        "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~ZC/evidence/r45_au1_bronze_ingest_and_four_count_sitez.txt @cc1f7b2dfa (blob e9c856a86b, equal at origin/box/sitez a010dd8a8e; not in box/dell1 HEAD, read by git show): 'resolved_folders 96 files_in_resolved 368 stored 368 (put_performed 12 existed 356)'"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "ADJUDICATION_v55 C-S22 (CRPS-at-4 AC2 NOT MET: store 356 vs drive 378) is SUPERSEDED. Of the 22 drive files C-S22 counted as missing, 12 were resolved-folder files not yet stored (the 11 OneDrive placeholders hydrated on read and 1 more), and round 45 stored all 12; the other 10 sit in 6 folders crosswalk/v1 does not resolve, which FWD-1's DONE WHEN (files the folder list resolves to) does not cover. C-S22 graded against the census's 378, wider than the PRD binds; that part of its reasoning was this seat's error. Its finding that the store was short of the resolved files was right at its read, and is now closed: 368 of 368."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S34",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T10:40:00Z",
    "one_line": "D1-S3 (OBSERVATION, INERT) stays HELD UNDER_INVESTIGATION, its graduation to 1.0.0_SA_CTO~DELL1 prepared but not landed: TO-WRITE-R45-au1 now reads complete (@79c9e7babb) and the project ledger holds no CTO ruling on the FWD-12 / FWD-20 conflict, but surprise-row-gate refuses a new remediation row because the seat-home transport copy org/tier2_senior/0.7.0_AE_CloudOps/task_orders/AMGT_CORPUS.TO-READ-R44-at-4.fence14-and-store-match-sitez.md still reads pending, although the canonical order under task-orders/ reads complete (@da1bdbf0ee). That copy is the issuer's to disposition (the order's own text names it). The prepared remediation row is held in org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_CORPUS_R45_D1_S3_REMEDIATION_v8_HELD_20261011.md.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "D1-S3 (OBSERVATION, INERT) stays HELD UNDER_INVESTIGATION, its graduation to 1.0.0_SA_CTO~DELL1 prepared but not landed: TO-WRITE-R45-au1 now reads complete (@79c9e7babb) and the project ledger holds no CTO ruling on the FWD-12 / FWD-20 conflict, but surprise-row-gate refuses a new remediation row because the seat-home transport copy org/tier2_senior/0.7.0_AE_CloudOps/task_orders/AMGT_CORPUS.TO-READ-R44-at-4.fence14-and-store-match-sitez.md still reads pending, although the canonical order under task-orders/ reads complete (@da1bdbf0ee). That copy is the issuer's to disposition (the order's own text names it). The prepared remediation row is held in org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_CORPUS_R45_D1_S3_REMEDIATION_v8_HELD_20261011.md.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_CORPUS-D1-S3",
        "adjudication row AMGT_CORPUS-D1-C-S29",
        "git show HEAD:org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-WRITE-R45-au1.bronze-ingest-and-four-count-sitez.md: <status>complete</status>",
        "safe-commit surprise-row-gate 2026-10-11T10:4xZ: 'NEW remediation row ... while 1 of 122 task order(s) ... are NOT terminal at HEAD: AMGT_CORPUS.TO-READ-R44-at-4.fence14-and-store-match-sitez.md [pending]'",
        "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-READ-R44-at-4.fence14-and-store-match-sitez.md:7 <status>complete</status>; :73-74 names the transport copy still pending"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Un-parks when the transport copy is terminal or removed: land the held file as remediations/REMEDIATION_v8.md."
  }
]
```
