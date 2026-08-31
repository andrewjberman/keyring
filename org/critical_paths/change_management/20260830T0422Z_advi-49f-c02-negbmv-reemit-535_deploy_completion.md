# Deploy Completion Record
**Date opened:** 2026-08-30T04:22:39.133726+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260830T051816Z
**Deploy:** ADVI_49F.c02-g-6: re-emit canonical/twr_daily for all 535 stored partitions against the 1.2 engine (UNCOMPUTABLE-NEGATIVE-BMV). BUILD-ONLY. Vintage UNMOVED at 946b5c5a3c; schema 1.1 -> 1.2. Write condition (1) met on the served object; readers announced at 85486.
**Authored by:** 0.7.0_AE_CloudOps~L
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| Q1 | verify | negative-BMV rows refused | OK rows with bmv < 0 = 0 of N over ALL 535, N derived at read time, reconciling to N-1's predicted 1,089 rows / 396 partitions | ZERO DELTA. OK rows with bmv < 0 = 0 of 2,592,232 matched OK account-days over all 535 partitions, N derived at read time. Refused set reconciles to N-1 EXACTLY: 396 affected partitions (delta +0), 1,089 rows (delta +0), mean 2.75. N-1's published curve scored five-for-five to two decimals at 198/250/300/350/396 affected (1.85/2.00/2.21/2.63/2.75) -- published 04:59Z before the producing dates were driven, matched by a different instrument on different objects. The 300-checkpoint was the declared falsifier and landed at 2.21. | CLOSED 20260830T051816Z |
| Q2 | verify | vintage UNMOVED | gross_leg_vintage == 946b5c5a3c on every row and manifest; a MOVED vintage FAILS this leg | VINTAGE UNMOVED. gross_leg_vintage == 946b5c5a3c89b61865ae1f4f60a609e831034cc2 on 3,021,660 of 3,021,660 rows and on every manifest. A moved vintage FAILS this leg by construction; it did not move. Verified at source in the served engine before the write (:76) and on every emitted row after. | CLOSED 20260830T051816Z |
| Q3 | verify | schema 1.2 uniform | schema_version 1.2 on 535 of 535, ZERO left at 1.1 | SCHEMA 1.2 UNIFORM. 535 of 535 partitions conformant on rows and manifests; ZERO left at 1.1. Checked with --expect-schema 1.2; the instrument's default remains 1.1 so the graded C02-g-3 round stays reproducible, and the 1.2 arm was proven live (it fails all partitions when pointed at 1.1 data). | CLOSED 20260830T051816Z |
| Q4 | verify | bmv >= 1 rows untouched | r_net / r_gross / status identical vs each partition's prior VersionId resolved BY TIME | bmv >= 1 ROWS UNTOUCHED. max \|delta r_net\| = 0.000000e+00 over 2,592,232 matched OK account-days; 532 of 535 partitions identical; 3 NOT-EVALUABLE-BY-SCHEMA; 0 violations. Each partition compared against its OWN prior VersionId resolved BY TIME. EXACT IDENTITY: matched OK account-days fell 2,593,321 -> 2,592,232, a difference of 1,089 == exactly the rows the fix refused. R-4's original C02-g-3 bar is now literally true: SIGNED gap POSITIVE on 77,072 of 77,072 fee account-days, NEGATIVE 0 (was 15), minimum gap now POSITIVE at +1.213709e-07; fee account-days fell 77,087 -> 77,072, a difference of 15 == exactly the negative-gap rows. | CLOSED 20260830T051816Z |
| Q5 | verify | shape census + out-of-domain | three-state shape census printed; 0 new versions on the 4 other canonical tables, denominators printed | SHAPE CENSUS + OUT-OF-DOMAIN. Three-state census: ABSENT 3, PRESENT-AS-NaN 532, PRESENT-AND-POPULATED 0 -- IDENTICAL to the pre-campaign census, confirming C02-g-5 converted ZERO partitions. Per-partition axis: 535 rows. R-6: 0 new versions across canonical_valuation (2,160), canonical_positions (1,108), flow_ledger (2,160), nna_canonical (2,160). Non-fee negative control: gap EXACTLY 0 on 2,515,160 of 2,515,160. | CLOSED 20260830T051816Z |

## Log

- 20260830T042239Z OPENED by 0.7.0_AE_CloudOps~L with 5 leg(s)
- 20260830T051816Z LEG Q1 closed: ZERO DELTA. OK rows with bmv < 0 = 0 of 2,592,232 matched OK account-days over all 535 partitions, N derived at read tim
- 20260830T051816Z LEG Q2 closed: VINTAGE UNMOVED. gross_leg_vintage == 946b5c5a3c89b61865ae1f4f60a609e831034cc2 on 3,021,660 of 3,021,660 rows and on eve
- 20260830T051816Z LEG Q3 closed: SCHEMA 1.2 UNIFORM. 535 of 535 partitions conformant on rows and manifests; ZERO left at 1.1. Checked with --expect-sche
- 20260830T051816Z LEG Q4 closed: bmv >= 1 ROWS UNTOUCHED. max |delta r_net| = 0.000000e+00 over 2,592,232 matched OK account-days; 532 of 535 partitions 
- 20260830T051816Z LEG Q5 closed: SHAPE CENSUS + OUT-OF-DOMAIN. Three-state census: ABSENT 3, PRESENT-AS-NaN 532, PRESENT-AND-POPULATED 0 -- IDENTICAL to 
- 20260830T051816Z CLOSED -- all 5 legs proven
