# Deploy Completion Record
**Date opened:** 2026-10-09T09:35:21.156272+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T095406Z
**Deploy:** AMGT_RESAPP round 83 AMGT-hh-4: re-cut and re-analyze four stored 20-F names with paragraph passages (ASML NA first, PBR held), dell1
**Authored by:** 0.9.0_WK_AMGT_RESAPP~332
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | ASML_NA_Equity silver part + analysis + drafting rewritten; AC1 and AC2 YES; four-prefix before/after diff | new VersionIds, AC1 AC2 output lines, diff | ASML NA re-cut + re-analyzed, AC1 YES AC2 YES (6 Item 4.B locations of 23, refusal x0): fetch 09:37:37Z parser 2.0.0 (3 items) silver part-20261009T093737Z VersionId CDXA6a7ynA4Dc0cGqrv7QTmuy8vziLUs; analysis 8efbNTID4hOuPskOa9yzCteRZJrEigVI (prior j8Na7vbs); drafting AHblHQYsQKRuezgUjaX9aNuVzcqgpI6A (prior iaClXu9Z); 2 model calls USD 0.6133; four-prefix diff added 3 removed 0 outside 0 (diff_ASML_NA_Equity.txt) | CLOSED 20261009T094207Z |
| L2 | verify | BABA_US_Equity silver part + analysis + drafting rewritten, or rolled back; four-prefix diff | new VersionIds or rollback proof, diff | BABA rolled back, no delete: fetch 09:42:53Z parser 2.0.0 (silver yvAd_0diu...), analyze 2 model calls USD 0.7846 but fetch stamped language=pt on an English 20-F so the draft was Portuguese, 0 of 40 sentences served; rolled back 09:47Z: analysis yIcDOS4HT5Q6_gLfUt0lbYCj90Qm1tPR (=DmJ7NkDk), drafting qUdrTs_2twkBesSoTueePYoDsVGcWite (=VFL1upyK), silver part-20261009T094719Z (prior row 3556dca9d0de); current == prior bytes verified; four-prefix diff outside=0 (diff_BABA_US_Equity.txt); row AMGT_RESAPP-D1-W332-S1 | CLOSED 20261009T095321Z |
| L3 | verify | NU_US_Equity silver part + analysis + drafting rewritten, or rolled back; four-prefix diff | new VersionIds or rollback proof, diff | NU landed: fetch 09:49:08Z parser 2.0.0 silver part-20261009T094908Z VersionId aXu_8tLc_qOYlmJ3eIZ6DAl7WstkcNec; analysis AWjDrLYseYOF7AJXok1PFFJfzXM9HLIQ (prior 9TdrmvW.), drafting xe0hxE3lFtEuonqh_ij9dIqQnWUC7Qrt (prior IOc9Qbp8); 2 model calls USD 0.8039; 38 of 40 sentences on span (prior 8); four-prefix diff outside=0 (diff_NU_US_Equity.txt) | CLOSED 20261009T095322Z |
| L4 | verify | SAP_GY_Equity silver part + analysis + drafting rewritten, or rolled back; four-prefix diff | new VersionIds or rollback proof, diff | NOT EXECUTED, no write: SAP's fetch stamps language=es on an English 20-F (read-only local fetch, no --write-pool), so a run would write a Spanish draft that serves nothing (row AMGT_RESAPP-D1-W332-S1); SAP untouched: no silver part, analysis and drafting keys equal the pre-act record, diff_SAP_GY_Equity.txt shows only other names' shared-prefix silver parts | CLOSED 20261009T095322Z |

## Log

- 20261009T093521Z OPENED by 0.9.0_WK_AMGT_RESAPP~332 with 4 leg(s)
- 20261009T094207Z LEG L1 closed: ASML NA re-cut + re-analyzed, AC1 YES AC2 YES (6 Item 4.B locations of 23, refusal x0): fetch 09:37:37Z parser 2.0.0 (3 
- 20261009T095321Z LEG L2 closed: BABA rolled back, no delete: fetch 09:42:53Z parser 2.0.0 (silver yvAd_0diu...), analyze 2 model calls USD 0.7846 but fe
- 20261009T095322Z LEG L3 closed: NU landed: fetch 09:49:08Z parser 2.0.0 silver part-20261009T094908Z VersionId aXu_8tLc_qOYlmJ3eIZ6DAl7WstkcNec; analysi
- 20261009T095322Z LEG L4 closed: NOT EXECUTED, no write: SAP's fetch stamps language=es on an English 20-F (read-only local fetch, no --write-pool), so a
- 20261009T095406Z CLOSED -- all 4 legs proven
