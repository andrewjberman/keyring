# Drive log -- 2.0.0_SA_COO~C1, ADVI_COTBKF, 2026-10-16 20Z to 22Z (written ~22:55Z, desktop-hk1uu7n)

One row per substantive tick: project | limb | round | TOs t/T | cells c/F | thread | act fired. Counts and ids only; no account, name or dollar value.

| tick | project | limb | round | TOs | cells | thread | act fired |
|---|---|---|---|---|---|---|---|
| ~20:20Z to ~21:20Z | ADVI_COTBKF | L7 wait | 106 | 1/1 | 1/1 | n | dated wait on `schedule:cot-silver-run` until 2026-10-17 13:00Z each tick; nothing moved (silver 1 partition, manifest and the 2026-08-19 partition unchanged, document at version 5); one free option taken the tick before (the close-read script, tested) |
| ~21:40Z | ADVI_COTBKF | FWD-2/4/7 | - | - | - | n | Andrew-direct recorded verbatim (@2bc556fe20, on origin box/dell1 by 21:42Z): the CRM archive is in Downloads on the laptop and the laptop CTO works out the upload; relayed through `0.0.0_AB_MSTR~DELL1` (msgs 7009, 7012); CTO msg 7011 added: ask whether the laptop's mapping scripts are the CRM silver builder (build ladder rung 2) |
| ~21:55Z | ADVI_COTBKF | FWD-2/4/7 | - | - | - | n | laptop CTO answered (MSTR msg 7014): the key is `s3://opal-data-cottonwood/commonwealth/cottonwood/bronze/crm/date=2026-06-23/CRM_CottonwoodCapitalAdvisors.zip`; only the break-glass role (trusting Andrew's console identity) may write it, so the laptop CTO is walking Andrew through the one upload; the mapping scripts are PARTLY reusable (the table reader and the household-id map only); CTO msg 7017: one builder cell when the archive lands, reusing those two pieces, with the sensitive-field exclusion before any byte is stored, built and tested on synthetic rows until Andrew names the reader |

**Decisions closed this hour.** (1) The CRM archive lands through Andrew's console, with the laptop CTO guiding. (2) FWD-4 and FWD-7 need ONE builder cell, cut when the archive lands. (3) No agent reads the real archive before Andrew names the reader (FWD-7).

**Owed.** The close read after the first scheduled silver fire (about 2026-10-17 midday) and the gold run that follows: `dc1_fire_read.py fire`, `snapshot` after each build, `compare` for C-1. Andrew: the console upload of the CRM zip; name who confirms the match pairs; name the reader (FWD-7); send the one ask to Commonwealth. Bloomberg tranche result from `2.0.0_SA_COO~Q1` about 2026-10-17 15:00Z. Push state: record commit @2bc556fe20 on origin box/dell1 (ls-remote 3f0ccf834c read by MSTR at 21:42Z); later commits LOCAL.
