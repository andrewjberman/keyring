# Drive log -- 2.0.0_SA_COO~P2 (IRPT_BCKEND ~P, dell2), 2026-10-14 ~13:40Z to ~14:45Z

Substantive ticks since the 13Z log (drive_log_20261014T13Z_desktop-n8rjv0a.md). Push state: LOCAL on box/dell2 (ls-remote read 435b8f0798 at 14:44Z, HEAD bfe336aef3).

| time (Z) | round | act | result |
|---|---|---|---|
| ~13:50 | 194 | worker 383 reported: packet v2 (73 moved-member rows, calendar holiday sets and T-1 identical, write addresses equal, matcher importer rebalancer_schemas.py, re-measure equal to the signed counts); AC1 FAIL on MY check (the stop evidence lists are flat, my check and control read count-and-path pairs); check repaired 90a0952879; merged 55d4929a90; AC1 row re-graded 7b46d4a24d (audited override); round-close-check MAY-CLOSE | the live holdings_snapshot.py matches no commit and differs per firm (rows D2-W383-S2, S3) |
| ~14:12 | 194 | packet 98209c1a0c + row D2-S173 + order 538 flipped; sent to 3.0.0_SA_CVO~DELL2; I held my COO half pending a measured live-against-pin differential | CVO slug v95 and the CTO's round-195 analysis (msg 7686) agreed |
| ~14:25 | 195 | issuer direct differential read (scratch, outside the repo; same receipts for both codes): 49financial 32 changed nodes (asset_class only, to cash), Inflection 841 (same), Cottonwood 485 (asset_class 253, asset_class_basis 236, sub_asset_class 51); no node added or removed | Cottonwood has a measured scope beyond the signed rule: 4 class, 236 basis, 51 sub-class changes |
| ~14:40 | 195 | ONE issuance 69f5437523: IB-pr-539 (the differential, attribution, packet v3) to worker 384; check r195 base FAIL, control PASS, 20 negatives | the apply is NOT cut; neither half signs until v3 |

Waiting on others: worker 384 (the differential cell, in flight); then both halves' signature on v3 (mine, then the CTO's); then the apply order. Andrew's PROD execution ID for IB-pr-456 (open act f61b) still unmet. My own scratch member-swap experiment (Cottonwood, outside the repo) is still running; it informs, it does not substitute for the cell.
