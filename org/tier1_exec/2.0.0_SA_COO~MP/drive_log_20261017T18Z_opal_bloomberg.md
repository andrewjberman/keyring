# Drive log -- 2.0.0_SA_COO~MP, NFRA_MCPORTAL, 2026-10-17 ~17:2xZ to ~18:5xZ (host opal_bloomberg, site Z)

Substantive ticks only; the runtime file is `org/mcp/drive_ticks/2.0.0_SA_COO~MP.md` (gitignored). Push state, measured by `git fetch origin box/sitez` then `merge-base --is-ancestor` against origin/box/sitez 95226555af: ea0b9f3fe4 (the 17Z log) is ON origin.

| time (Z) | limb | outcome | act |
|---|---|---|---|
| ~17:29 | wait | WAIT | no mail; calls f0d2, 8ed7, def4 open and Andrew's; /next-calls --drive found no FREE option; wait recorded against f0d2 |
| ~18:00 | measure | WAIT | `~NFRA1`'s OG-ap-36 Phase B gateway release is deployed (efcc8ae19f); `pf11.host.sh` (SSM 5ad78dc8) PASS: the host still serves the 59e802a bundle; `deny_guard_host.sh` PASS: andrew and opalbloomberg proceed, alyssa 403 (control) |
| ~18:28 | wait | WAIT | unchanged: no mail, lease FULL, same three calls open; same record |
| ~18:57 | wait | WAIT | unchanged; same record |

Open: the second MP-v-2 window as Opal Bloomberg (call f0d2; needs Andrew's "again" and Andrew at the screen, Opal Bloomberg chosen explicitly, a fresh profile `profile-edge-opalbloomberg`); calls 8ed7 and def4 are his acts; PD held by the CTO until OG-cp-1 and Andrew's sitting; MP-pd-7 staged to ~NFRA1 (MSTR~Z told at the GO); Z-W28-S1 and Z-W32-S1 are the issuer's two armed rows, carried on purpose (Z-S73).
