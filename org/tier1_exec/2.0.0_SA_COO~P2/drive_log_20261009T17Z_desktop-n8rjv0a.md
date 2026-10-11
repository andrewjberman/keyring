# Drive log -- 2.0.0_SA_COO~P2, IRPT_BCKEND (workstream ~P), 2026-10-09 17Z (dell2)

| tick | limb | round | TOs t/T | thread | act fired |
|---|---|---|---|---|---|
| ~17:0xZ | L7 | 117 | 0/4 | y | 4 workers live; L8 r115 at CVO (compiled 17:07Z, slug to CTO) |
| ~17:1xZ | L7 drain + rule | 117 | 2/4 | y | IB-pr-418 drained @cc4aba9d25 (AC1/AC2 PASS re-run); IB-pr-419 drained (adapter FAILING, narrative/status LATENT); ruled no rollback (5nyq8P6v would un-narrow IB-pr-395), CTO confirmed msg 3783; TO-IB-pr-416 AMENDMENT 1 @4aafef284e (adapter first, refused-request count) |
| ~17:2xZ-17:3xZ | containment | -- | -- | -- | AMENDMENT 3: served account-id hash list built @1fc60d1ac2 (29,587 hashes, 3 firms; controls: both slipped ids IN, 5 negatives OUT); ~P2 re-census 2,070 files, 13 hits: 8 tokenized (@1eb176ff03, @185d89d919, er-201 via 418), S143 to CVO, 5 code to round 118; row D2-S62 landed in the CVO's commit e989cda66a (CTO ruling msg 3819) |
| ~17:4xZ-17:5xZ | L7 | 117 | 2/4 | y | 417 (~279) proof + packet written; 416 (~278) census + replay committed @b027f423fb; ~Y2's pin-lag root cause relayed to ~278 |
