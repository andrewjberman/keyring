# drive log -- 2.0.0_SA_COO~ZB -- 2026-10-15 06Z

| tick | time | project | limb | act |
|---|---|---|---|---|
| 20-34 | 14:39Z (10-14) to 04:39Z | OPAL_BBGTML | L7 | WAIT (dated), state unchanged: 1 open order (TO-Z6-R3 parked), 0.7.0_AE_CloudOps~ZS live, no mail/rows/calls; keep-driving confirmed to 0.0.0_AB_MSTR~Z (msg 34311, CONFIRMED, slot :13) |
| 35 | 05:40Z | OPAL_BBGTML | L7 | DRIVE FORWARD: 0.0.3_BG_BBGTerminal reported DAPI DOWN overnight and 05:4xZ is outside 10:30-12:30Z -> GO to ~ZS under TO-Z6-R3 (status line @932eebeca9, no criterion changed) |
| (event) | 06:01Z | OPAL_BBGTML | L7 | ~ZS reply (msg 34348): dapi_check DOWN 05:42Z, exercise AC1+AC2 PASS, merged @3dad54c56f, AC3 exit 2 NOT-EXERCISED (no 8194 listener), UI tree closed, bbcomm untouched. RULING (issuer, own decomposition): KEEP. Basis: merge diff read; the `$absent -eq 3` guard only suppresses a duplicate print, `$absent` is set at line 60, no strict mode, values 1-2 exit before line 69; exit 2 NOT-EXERCISED is not an AC3 FAIL. Ledger opal-bbgtml-z6-r3-signin-20261013 L2 stays open until ~ZS reads the 11:00Z fire's log |

State: R3 landed, not yet terminal (L2 open; AC3 graded at the 11:00Z fire, WORLD). Owed: ~ZS reads the fire's log and closes L2; I disposition Z-S21 (duplicate of Z-S1: the verify step prints the login-name OCR; remedy is a print-similarity-only edit to bbg_verify.ps1) AFTER the fire reads clean, so no second change stacks onto the fallback before its real exercise.
Loops: /canonical-drive OPAL_BBGTML hourly :13 (session cron da935ed1).
