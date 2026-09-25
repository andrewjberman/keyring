# Deploy Completion Record
**Date opened:** 2026-09-25T04:18:19.018371+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260925T044813Z
**Deploy:** AMGT_CORPUS FWD-12 round 4: chunked Model-block pull (<=25 hist fields per request) + derive over 89 resolved keys (R-21, CTO msg 25799; derive pair COO 2a3319e5ae / CTO 35e4cb93ef)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | PROBE: model_block_pull.py pull over 3 keys (Bloomberg identifiers with spaces) at CLOUD >= 93440f9df1 | each probe key's raw histdata READ: rows > 0 printed beside present | evidence/fwd12_r4_probe_20260925T042140Z.log rc=0; histdata READ (S3, newest since 04:21Z): ADBE_US_Equity rows 20, 2317_TT_Equity rows 12, ASML_NA_Equity rows 14 -- present 3 non-empty 3 empty 0 of 3; 14 of the 16 added history fields carry a value on each; the chunked request (25 + 14) returns history where the single 39-field request returned {} (Z-S29) | CLOSED 20260925T042334Z |
| L2 | activation | pull over the remaining 86 keys, 29 invocations of <=3, stop at first non-zero rc | per key refdata/histdata/bestdata READ: present / non-empty / empty counts over 89 | org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/evidence/fwd12_r4_pull_20260925T042440Z.log: 29 of 29 batches rc=0 over the remaining 86 keys; CONTENT READ on S3 (newest since 04:21Z) over all 89: histdata present 89 non-empty 89 empty 0 (rows 8-20 per key; of the 16 added history fields, 14 carry a value on 61 keys, 8-12 on the other 28), refdata present 89 non-empty 89, bestdata present 89 non-empty 89 | CLOSED 20260925T043539Z |
| L3 | activation | derive over the 89 keys (moves served derived/model_block, read by scoped_amgt, render_pack, peers, run_scores) | per key newest block: FY rows > 0 and figures > 0, present / non-empty / empty over 89; SA-fallback-fired count beside 89 | org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/evidence/fwd12_r4_derive_20260925T043840Z.log: 30 of 30 batches rc=0, 89 blocks with 8-11 FY rows each; CONTENT READ through scoped_amgt.read_model_block over all 89: non-empty with FY figures 89, empty 0; newest block is this run's 89 of 89 (BP/ and NG/ read by vintage 04:39Z/04:40Z, 419/367 figures); the 22 added mnemonics present as figures per key: 20 on 44 keys, 18-19 on 27, 8-17 on 18; SA fallback FIRED on 0 of 89 (the CTO's owed figure); field_map.json +56 securities, +34 field entries, 2819 of 2823 prior per-security values byte-equal and 4 a scalar->per-security reshape carrying the same value | CLOSED 20260925T044813Z |

## Log

- 20260925T041819Z OPENED by 2.0.0_SA_COO~X with 3 leg(s)
- 20260925T042334Z LEG L1 closed: evidence/fwd12_r4_probe_20260925T042140Z.log rc=0; histdata READ (S3, newest since 04:21Z): ADBE_US_Equity rows 20, 2317
- 20260925T043539Z LEG L2 closed: org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/evidence/fwd12_r4_pull_20260925T042440Z.log: 29 of 29 batch
- 20260925T044813Z LEG L3 closed: org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/evidence/fwd12_r4_derive_20260925T043840Z.log: 30 of 30 bat
- 20260925T044813Z CLOSED -- all 3 legs proven
