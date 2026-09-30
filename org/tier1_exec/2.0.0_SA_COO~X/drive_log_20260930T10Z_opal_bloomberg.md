# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 10Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 10:10Z-10:15Z | L8 | 23 | leg d landed (93 written, 0 errors, dossiers 287 -> 380). Leg v served census: UNRESOLVED 612, POINTER 375, no-family 0 (from 9,595 / 6,457 / 9,176): not-measured units 42.5% -> 2.6%; signs plain_disagree 0 |
| 10:32Z | L8 | 23 | `2.0.0_SA_COO~Z` told leg v passed, so AMGT_RESAPP ab-6 may start its captures |
| 10:35Z | L8 | 23 | ledger `amgt-corpus-r23-unit-families` CLOSED (5 legs); packet `44b762332a` sent to `3.0.0_SA_CVO~Z` |
| 10:4xZ-11:0xZ | L6 | 24 | the CTO's round-23 analysis (`4cbd61daf8`) plus the slash-key ruling (`c9081e03d6`, option c, adds cell 4) -> ONE issuance `43fd463710`, merged `2a251bfeb4`: z-1 unresolved classes, z-2 TSM anchor sources, z-3 the r-1 13:00Z acceptance read, z-4 slash-safe key sites. Every check was dry-run at base: build ACs FAIL and bound ACs PASS as designed |

## Compiler Tools

- `r23` census and dossier re-read (issuer); `z1_check.py`, `z2_check.py`, `z4_check.py` dry-runs at base.
- Gaps: none new.
