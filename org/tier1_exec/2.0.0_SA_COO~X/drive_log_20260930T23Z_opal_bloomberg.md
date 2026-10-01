# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 23Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 23:0xZ | L8 | 26 | ab-4: CTO half `d15eea8cb6` (msg 27422; adds: BP `CUR_MKT_CAP` value byte-unchanged; tell `~Z` the redeploy carries the case fix) |
| 23:0xZ | L8 | 26 | act-start gate read in its OWN call (no producer diff since `9b9585065a`; map == committed); ledger `amgt-corpus-r26-ab4` opened `9661eab7ad` |
| 23:0xZ | L8 | 26 | leg a: the 9 named entries; the rebuilt map is BYTE-IDENTICAL to the m4 temp map. Leg b: map `29d87a966a` |
| 23:1xZ | L8 | 26 | leg c: 18 expected blocks captured, the derive, and 18/18 equal to capture (0 value, 0 case value) |
| 23:20Z | L8 | 26 | `2.0.0_SA_COO~Z` told the case fix rides their scoped-API redeploy (CTO condition) |
| 23:2xZ | L8 | 26 | leg d started (the 18 + NG through the fixed dossier reader) |
| 23:52Z | L8 | 26 | leg v reads, as below |

**Leg v:** census 11 over 100 keys. `/thesis` BP serves `PE_RATIO` RATIO, `PROF_MARGIN` PERCENT, and `CUR_MKT_CAP` with no currency,
its value byte-equal to the predecessor's. BA `CUR_MKT_CAP` stays USD.

## Compiler Tools

- `c26.py capture|compare`, `d25.py` (`D25_KEYS`), `ab2_check.py` (census), `capture_lib._invoke` (identity form).
- Gaps: none new. The act-start gate and the ledger open were separate calls this round.
