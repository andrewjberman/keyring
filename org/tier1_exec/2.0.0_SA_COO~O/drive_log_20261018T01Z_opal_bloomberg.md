# Drive log -- 2.0.0_SA_COO~O -- NFRA_OPLGTW -- 2026-10-18 01Z to 02Z (host opal_bloomberg)

## Substantive ticks since the 00Z log (ticks 215 to 219)

- Round 42 issued at `2550dab3df` (8 orders, ENRICH-R42-A); three workers drained and verified on my runs: `OG-en-27` (`9c8f21f8cd`, `en27.AC1` PASS), `OG-en-28` (`26090b1a17`, `en28.AC1` PASS, 12 codes documented, `tools.py` line count unchanged, 29 of 29 in both orders), `OG-sec-1` (`92d4fbd5e4`, `sec1.AC1` PASS, SSRF audit CLEAN, 0 of 18 call sites controllable; I read the riskiest rows myself: every Graph path is a leading-slash string, the JWKS URLs are config-sourced). Ruling row `Z-S384` (`49e1c766de`) on the worker rows `Z-W143-S1`, `Z-W145-S1`, `Z-W145-S2`.
- `OG-sec-1` CLEAN released `OG-pr-1`: worker `~146` provisioned and spawned (the loopback probe listener). Its branch carries the listener commit and three ARMED observation rows read at 02:26Z (not yet ruled, the worker has not reported): the two-tool restriction is an allowlist inside the module (no stored restricted profile can be created from code); the probe calls the tool functions directly so `_run`'s guard chain and its audit line do not run for probe calls (the probe enforces its own lease, tool and account checks and writes its own `probe:<order>` audit line); the fixed principal carries an Opal-domain display address that exists only in code. These go in the never-widen ask for the CTO and the CVO.
- dell1's `HVST-cg-3` deploy (CTO msgs 35600 and 35603): landed 02:06:03Z, live `4257a2aa42`, `harvest_research.py` blob `574959b682d4a13a0a429c45fa00b77b6caa2ab5` verified by the CTO. Amendments A1 (`6615c7f7b3`: never overlap the window) and A2 (`3155640ed2`: cut on `4257a2aa42`, blob pinned in `ap39.AC1` and `ap40.AC1`) to `OG-ap-39` and `OG-ap-40`. `~NFRA1` told twice: start `OG-ev-6` only after the cg-3 ledger reads CLOSED (it read OPEN at 02:25Z); no GO yet for the two releases.
- Round-43 candidates carrier committed (`48854a89e9`).
- Still ARMED (mine): `Z-S375`, `Z-S338` (both disarm only through the listener), `Z-S177`, `Z-W94-S2`.

## Next

`~146`'s report, my runs of `pr1` AC1 to AC3 and the proof check, the drain; the cg-3 ledger CLOSED, then `OG-ev-6` and `ev6.AC1`; `OG-en-29` if the sweep chooses above 30; then `OG-ap-39` and `OG-ap-40`, each under its own never-widen.

Push state: LOCAL (box/sitez ahead of origin; not pushed this hour).
