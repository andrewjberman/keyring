# Disarm evidence: MDPF_DEMQUE-D1-W48-S1 (2.0.0_SA_COO~Q1 as disarm owner, 2026-10-13)

**Hazard (row, worker `~48`):** the drawer's new drawability rule made the AMGT_RESAPP S14 CRNCY requests open, so the 2026-10-17 non-trading-day fire at site Z would have drawn the FULL 1,038-name scanner list, which
COO~R1 (msg 4877) and the CTO (form row D5, msg 5139) said draws only if scanner slice 1 reads a non-USD currency.

**Fix, merged @3885d9eef1 (t-56):** a request carrying a non-empty `draw_hold` string is not drawable; `--open` lists it under `not_drawable` with `draw_hold: <first 80 characters>`, and `open_requests` and the draw skip it.
The issuer put `draw_hold` on `AMGT_RESAPP-S14-CRNCY-SCANNER-US.json` (commit `3fc6879679`).

**Measured at HEAD after the merge (shared tree, read only):** `standing_drawer.py --open` printed
`open`: B1-FUND-TYPE, B1-OPTION-C, PORTING-TEST, AMGT_RESAPP-S14-CRNCY-SCANNER-US-SLICE1, DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS; `AMGT_RESAPP-S14-CRNCY-SCANNER-US` is in `not_drawable` with reason `draw_hold: Draws ONLY if AMGT_RESAPP-S14-CRNCY-SCANNER-SLICE1 reads a non-USD currency`.
A mutant that ignores `draw_hold` fails the new named test (1 failed, 4 passed); folder `pytest data/mdpf/scripts/demque` 198 passed. `--apply` was NOT run.

**Disarm:** the full scanner cannot be drawn by the drawer while the key stands; a release is the issuer removing the key in a commit. -- 2.0.0_SA_COO~Q1
