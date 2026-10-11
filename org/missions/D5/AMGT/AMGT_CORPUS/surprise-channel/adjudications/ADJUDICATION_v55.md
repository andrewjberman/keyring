# AMGT_CORPUS -- round 44 at-10 leg v and CRPS-at-4 AC2 grades (dell1)

<sweep_watermark>2026-10-11T03:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T03:55:00Z. Asked by 2.0.0_SA_COO~C1 msg 3448 (packet `deliverables/2.0.0_SA_COO~C1/ROUND44_AT10_LEG_V_PACKET.md` @c8f7662637). Leg v reads Branch A as signed. CRPS-at-4 AC2 is NOT MET: the drive lists 378 files and the store holds 356 objects.

```json
[
  {
    "id": "AMGT_CORPUS-D1-C-S21",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T03:55:00Z",
    "one_line": "CRPS-at-10 leg v reads Branch A as signed. On this seat's re-run over the WRITTEN /11 objects: 95 names, 2280 fields, 2090 same, NEWFIELD team_sheet on all 95 and nothing else, CHANGED model_rows only (95), DROPPED 0, stored team_sheet equal to the reader 95/95, build 1/1. This seat's own row-level read of all 95 model_rows pairs: 9567 rows, the same length and the same mnemonic or label and source on every row. 1860 rows are equal; in the 7707 that differ, only figure moved: 7135 stamp only, 572 stamp and value (18 daily market mnemonics, e.g. AVG_DAILY_VALUE_TRADED_3M 93, CUR_MKT_CAP 82). Every changed stamp moves from 2026-10-09 to 2026-10-10. The CTO half's leg 0 condition holds: --pre lists 0 names without a /10 object, and 95 of 95 carry a /11 object. Served state stays /10 until leg p.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND44_AT10_SERVED_ACT.md @46ed5d889f leg v expectation and Branch A/C; ledger/NEVER_WIDEN_ROUND44_AT10_CTO_HALF.md @fda1c4f0cc condition (leg 0 prints per name whether a /10 object exists, 95 of 95).",
    "world_is": "Branch A: NEWFIELD = {team_sheet} on 95 of 95, CHANGED = model_rows only, each printed whole, DROPPED 0, stored team_sheet equal to the reader 95/95. The model_rows change is the daily model block's 10-09 to 10-10 pull and nothing else (7135 stamp-only + 572 stamp+value = 7707 changed rows, no row identity moved). team_sheet classes: own_new 21, own_model 11, master_absent 63, sum 95.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran PYTHONPATH=. python deliverables/2.0.0_SA_COO~C1/checks/round44/at10_diff.py --post at ~03:4xZ, rc 0: 'at10 names 95 fields 2280 same 2090 newfield 95 changed 95 dropped 0 changed_outside_inputs 0 ts_equal_reader 95/95', 'at10 build 1/1', 0 UNREAD / NOT-AT-11 / TS-DIFFERS lines; NEWFIELD lines 95 all team_sheet, CHANGED lines 95 all model_rows",
        "3.0.0_SA_CVO's own classifier over the 95 WHOLE /10 and /11 model_rows pairs from that run (independent of at10_diff.py's logic): row-length mismatch 0, mnemonic/source mismatch 0, figure key-diff classes {stamp: 7135, stamp+value: 572}, stamp day transitions {20261009 -> 20261010: 7707}",
        "3.0.0_SA_CVO ran at10_diff.py --pre at ~03:5xZ: 'at10 pre names 95 with_a_/11_object 95', 0 PRE-NOT-AT-10 lines (every name's /10 read returns a /10 object)",
        "git diff 3bff293266 HEAD -- lib/research/corpus/dossier.py lib/research/corpus/team_sheet.py: empty"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard. Branch A lets the CTO amend the RESAPP half for leg p."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S22",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T03:55:00Z",
    "one_line": "CRPS-at-4 AC2 (the store matches the drive at the current folder count) is NOT MET. FWD-1's DONE WHEN requires 'the count of objects equals the count of files scanned, both printed'. The site-Z read prints the store as objects 356, files 356, match 356, mismatch 0, but the library census as folders 102, files 378. The verify's denominator is the store's own 356, so it says nothing about the 22 listed drive files with no stored object. The store is internally sound and byte-true for what it holds; it is not the drive at 102 folders. Also on that read: 11 of the 378 are unhydrated OneDrive placeholders, so the drive-side count was read on a partially synced tree. Closing it needs an ingest of the current library at site Z, then --verify reading objects equal to the census file count.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "AMGT_CORPUS PRD FWD-1 DONE WHEN (prd:190-197): for every file the library's folder list resolves to, the stored object matches byte for byte, and the count of objects equals the count of files scanned, both printed. TO-READ-R44-at-4 AC2 (judgment): the store matches the drive at the current folder count.",
    "world_is": "store 356 objects / 356 matched; drive 102 folders / 378 files (ext .docx 88, .html 1, .pdf 193, .png 17, .xlsx 79; placeholders 11 of 378). 378 != 356, so the object count does not equal the files-scanned count at the current folder count. Which 22 files are missing is not printed by the read; it cannot be read from dell1 (the library resolves only at site Z).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.7.0_AE_CloudOps~Z/evidence/r44_at4_fence14_store_match_sitez.txt @2274227184 (0.7.0_AE_CloudOps~ZC, HEAD 3865f3fd34 box/sitez, 2026-10-11T02:38:54Z): 'objects 356 files 356 match 356 mismatch 0'; 'folders 102 files 378'; 'placeholders 11 of 378'",
        "the same file's own delta note: 'The store's verify denominator is the store's OWN population, so match 356 says nothing about the 22 drive files (378 - 356) outside it'",
        "AC1 (mechanical) reads 1 on the same file: 'fence14 resolved 84 ambiguous 0 empty-or-workbook-only 12 unresolved-with-reason 6 sum 102 folders_read 102'",
        "master-template zero is controlled: positive control *.xlsx 79 equals the census 'ext .xlsx 79'; near-miss *ONE PAGER* 60, *TEMPLATE* 30; only the un-prefixed _v1 under 'Total Energies TTE FP' exists. This supports the 63 master_absent names stored with their reason in words; FWD-12 itself is not graded here."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record: AC2 NOT MET. The gap is an ingest owed at site Z, and the next FWD-1 cell is the issuer's to cut."
  }
]
```
