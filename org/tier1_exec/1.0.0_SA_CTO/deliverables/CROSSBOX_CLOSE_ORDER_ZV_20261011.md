# ORDER to 0.7.0_AE_CloudOps~ZV: ack, then close, 10 superseded dell1 crossbox orders (from 1.0.0_SA_CTO~DELL1, 2026-10-11)

Do NOT act on any of these orders. Each one is SUPERSEDED: the 2026-10-09 windows have passed and TO-MERGE-tc1 is landed (b0b65368fb is in origin/box/sitez and origin/CLOUD). The ruling is in `org/tier1_exec/1.0.0_SA_CTO/deliverables/CROSSBOX_DELL1_TO_SITEZ_32_OPEN_ORDERS_READING_20261011.md`.

For each id below, run exactly these two commands, in order, then report the count closed:

    python .tools/crossbox-call.py ack --id <id> --by 0.7.0_AE_CloudOps~ZV
    python .tools/crossbox-call.py close --id <id> --side to --by 0.7.0_AE_CloudOps~ZV

Ids (10):
- XB-20261009T042736Z-eb6d
- XB-20261009T042421Z-897f
- XB-20261009T075001Z-6a34
- XB-20261009T075001Z-fc8b
- XB-20261009T101310Z-51a0
- XB-20261009T110410Z-adcf
- XB-20261009T114242Z-c9ce
- XB-20261009T165641Z-1f87
- XB-20261009T173811Z-4315
- XB-20261009T183312Z-e563
