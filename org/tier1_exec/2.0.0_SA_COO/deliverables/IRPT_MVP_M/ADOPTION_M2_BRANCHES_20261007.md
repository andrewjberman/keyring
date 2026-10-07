# IRPT_BCKEND workstream M -- adopted laptop branches, read by 2.0.0_SA_COO~M2 (dell2)

Measured 2026-10-07 ~07:4xZ against dell2 HEAD c59c5420ca after `git fetch origin` (all 27 dell2 rows on origin per
0.0.0_AB_MSTR~DELL2 msg 38). Inventory: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ADOPTED_WORK_INVENTORY_FOR_THE_DELLS_20261007.md`
(origin 83d5e34919). Prior per-file census: `R23_M_BRANCH_CENSUS_20260929.md` (09-29, CLOUD 75b5cdcba2). Issuer for M:
2.0.0_SA_COO~M2, per laptop ~M's final handoff 1640a0e86e (CTO msg 106037).

Claim words: `measured` = read at this write; `held` = from the 09-29 census, not re-read.

| Branch (origin) | Census 09-29 (held) | At HEAD today (measured) | Reading |
|---|---|---|---|
| irpt-m-s125-20260924 | WORLD-DONE | 0 of 2 files differ | done; ref is cleanup |
| irpt-m-s125-publish | DRAIN (CHANGELOG.json append only) | 2 of 5 differ; CHANGELOG.json moved 24 commits, source map 217 | the one CHANGELOG append is the only carry; not a cut |
| irpt-m-s152-cloud | DRAIN | `mix_views.py` at HEAD already lists cash and other plus structured and commodities (line 24); branch lists 5 classes | SUPERSEDED by HEAD; draining would narrow the list |
| irpt-m-cot-cash-line-act / -cot-b1 / -cot-cash-line | DRAIN (COT gold half HELD on S173) | COT C_06/D_03/D_04 moved 3-4 commits since the fork, by the MDPF_SECCLASS S29 work and its restore (a62580ef8f) | COT gold class lists are now MDPF_SECCLASS's surface (2.0.0_SA_COO~M1); not drained here |
| irpt-m-b01b-skip | DRAIN | B_01b moved 3 commits since the fork; rolled back in S3 and repo on 10-07 (2332d9a5df, rows S39-S40) | MDPF_SECCLASS's surface; a drain would undo a CTO-ruled rollback |
| irpt-m-s152 (0.4.0_DS_ClientPlatform~X) | DRAIN, tied to ARMED S155 | 49F a07/d06 and the four ~X deliverables unchanged since the fork; BD gold moved 7-9 commits | tied to S155; Andrew's six-class word (10-07) changes the class lists it widens |

Result: NO branch is drained or cut against by this seat. None carries M work that HEAD lacks and no later act
overtook, except the one CHANGELOG.json append (record-only). The COT and BD gold branches are on files that
MDPF_SECCLASS now owns. Worker branches wk-IRPT_BCKEND-84, -61 and wk-irpt_bckend-6-1f and the ~P, portal and scratch
rows are not M's and were not graded here.
