# ORDER to 0.7.0_AE_CloudOps~ZC: ack, then close, 10 superseded dell1 crossbox orders (from 1.0.0_SA_CTO~DELL1, 2026-10-11)

Do NOT act on any of these orders. Each one is SUPERSEDED: AMGT_CORPUS is past round 40, and the r44 CRPS-at-4 read was delivered on dell1. The ruling is in `org/tier1_exec/1.0.0_SA_CTO/deliverables/CROSSBOX_DELL1_TO_SITEZ_32_OPEN_ORDERS_READING_20261011.md`.

For each id below, run exactly these two commands, in order, then report the count closed:

    python .tools/crossbox-call.py ack --id <id> --by 0.7.0_AE_CloudOps~ZC
    python .tools/crossbox-call.py close --id <id> --side to --by 0.7.0_AE_CloudOps~ZC

Ids (10):
- XB-20261009T054248Z-aff1
- XB-20261009T054315Z-f12c
- XB-20261009T060524Z-7b40
- XB-20261009T075017Z-68ae
- XB-20261009T075018Z-cf96
- XB-20261009T090208Z-c071
- XB-20261009T090208Z-c4e7
- XB-20261009T113054Z-9452
- XB-20261009T131421Z-cfce
- XB-20261009T205724Z-7dd9
