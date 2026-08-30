# Deploy Completion Record
**Date opened:** 2026-08-30T02:51:17.315481+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260830T034622Z
**Deploy:** ADVI_49F.c02-REEMIT: re-emit canonical/twr_daily for all 535 stored partitions under ONE gross-leg convention (cell C02-g-3, CVO 84078/84079 as narrowed). BUILD-ONLY: no serve, no publisher, no platinum key. Runs while advi-49f-gold-floor is HELD DISABLED; the hold's lift condition is THIS campaign's R-5.
**Authored by:** 0.7.0_AE_CloudOps~L
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | domain census | every stored twr_daily partition censused at start, paginated, with the ledger set-compare printed | S3 census at drive time, paginated and counted client-side: 535 partitions from 1,070 objects over 2 PAGES, 2024-07-08..2026-08-28. Set-compared against the P14 ledger: 534 in both, 1 S3-only (2026-08-28), 0 ledger-only. Denominator ratified by 2.0.0_SA_COO 84341 and 3.0.0_SA_CVO 84356 as 535, replacing the cell's typed 534. First comm(1) returned zero-overlap on a CRLF artifact and was re-derived with a CR strip -- disclosed, not hidden. | CLOSED 20260830T034620Z |
| L2 | verify | R-3 r_net value-identical | max abs delta r_net = 0.000e+00 over matched OK account-days, denominators partitions AND account-days, null-typed partitions on their own line | R-3 PASS. max \|delta r_net\| = 0.000000e+00 over 2,593,321 matched OK account-days; 532 of 535 partitions identical; 3 NOT-EVALUABLE-BY-SCHEMA (2024-07-08 / 2025-01-09 / 2026-08-18, where bmv/emv/cf_net/cf_gross are ABSENT not null, per 0.4.0_DS_ClientPlatform~C 84413) printed on their own line; violations 0. Each partition compared against its OWN prior VersionId, resolved BY TIME (newest preceding that date's send_time), never by position. | CLOSED 20260830T034621Z |
| L3 | verify | R-4 signed gross-net gap | r_gross > r_net on EVERY fee day, SIGNED gap published never abs(), non-fee-day equality as the negative control, both denominators | R-4 PASS on its declared domain, GRADED 3.0.0_SA_CVO 85166 after this seat reported it NOT MET AS WRITTEN. Amended bar measured on the whole population: the RELATION (r_gross - r_net)*BMV == cf_net - cf_gross holds 77,087 of 77,087 fee account-days, violations 0, including all 15 negative-BMV rows; inequality r_gross > r_net on 77,072 of 77,072 (BMV > 0); 15 BMV<=0 NOT-EVALUABLE-BY-DOMAIN on their own line; SIGNED gap never abs(), range [-22.645283, +584.121739]; negative control non-fee gap EXACTLY 0 on 2,516,234 of 2,516,234. | CLOSED 20260830T034621Z |
| L4 | verify | R-5 vintage on 535 of 535 | gross_leg_vintage == 946b5c5a3c... and schema_version 1.1 on every partition and manifest, ZERO left at 1.0 | R-5 PASS. gross_leg_vintage == 946b5c5a3c89b61865ae1f4f60a609e831034cc2 on 3,021,660 of 3,021,660 ROWS (row grain, not merely the manifest); schema_version 1.1 on 535 of 535 partitions and manifests; ZERO partitions left at 1.0. Start condition verified at the sharpest grain before the drive: md5sum ON THE BOX = 3c2b659b5317e735c7e11d134c1e1f5d with the constant at :65. THIS IS THE H-4 LIFT CONDITION AND IT IS MET AND READ. | CLOSED 20260830T034621Z |
| L5 | verify | R-6 out-of-domain tables unmoved | every other canonical table key+VersionId identical before vs after, 0 new versions, denominator printed | R-6 PASS. 0 new versions since campaign start across all 4 out-of-domain canonical tables, denominators printed: canonical_valuation 0 of 2,160 \| canonical_positions 0 of 1,108 \| flow_ledger 0 of 2,160 \| nna_canonical 0 of 2,160 (7,588 versions scanned). Every newest timestamp PRECEDES the first write. True BY CONSTRUCTION on this vehicle -- c02_twr_engine's only write is rc.emit(TABLE_DAILY) and the mirror pull performs no put/copy/delete -- so this is a confirmation, not a hope. | CLOSED 20260830T034621Z |
| L6 | verify | R-7 build-only | no serve, no publisher, no platinum key touched | R-7 PASS. Build-only: no serve, no publisher, no platinum key touched; advi-49f-publisher verified DISABLED alongside the floor before every one of 22 batches. Cadence honoured from the ledger, never a projection: date-1 (84747), per-100 #1 84813 / #2 84911 / #3 84943, completion 85113. 535 of 535 ARTIFACT-COMPLETE, 0 halt-class rows, driver exit 0. | CLOSED 20260830T034622Z |

## Log

- 20260830T025117Z OPENED by 0.7.0_AE_CloudOps~L with 6 leg(s)
- 20260830T034620Z LEG L1 closed: S3 census at drive time, paginated and counted client-side: 535 partitions from 1,070 objects over 2 PAGES, 2024-07-08..
- 20260830T034621Z LEG L2 closed: R-3 PASS. max |delta r_net| = 0.000000e+00 over 2,593,321 matched OK account-days; 532 of 535 partitions identical; 3 NO
- 20260830T034621Z LEG L3 closed: R-4 PASS on its declared domain, GRADED 3.0.0_SA_CVO 85166 after this seat reported it NOT MET AS WRITTEN. Amended bar m
- 20260830T034621Z LEG L4 closed: R-5 PASS. gross_leg_vintage == 946b5c5a3c89b61865ae1f4f60a609e831034cc2 on 3,021,660 of 3,021,660 ROWS (row grain, not m
- 20260830T034621Z LEG L5 closed: R-6 PASS. 0 new versions since campaign start across all 4 out-of-domain canonical tables, denominators printed: canonic
- 20260830T034622Z LEG L6 closed: R-7 PASS. Build-only: no serve, no publisher, no platinum key touched; advi-49f-publisher verified DISABLED alongside th
- 20260830T034622Z CLOSED -- all 6 legs proven
