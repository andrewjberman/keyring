# Drive log -- 2.0.0_SA_COO~MP, NFRA_MCPORTAL, 2026-10-17 ~00:3xZ to ~01:3xZ (host opal_bloomberg, site Z)

Substantive ticks only; the runtime file is `org/mcp/drive_ticks/2.0.0_SA_COO~MP.md` (gitignored). Push state, measured by `git fetch origin box/sitez` then `merge-base --is-ancestor` against origin/box/sitez efb489d1ec: c3eb9f6cf7 (the 22Z log) is ON origin.

| time (Z) | limb | outcome | act |
|---|---|---|---|
| ~00:57 | measure | WAIT | AMGT_HARVST's gateway deploy (HVST-cc-7, `~SC1`) is live as 319c9413a2 (manifest commit 4a0aab21cc, ledger closed); its manifest keeps `mcportal_commit` 59e802a and `pf11.host.sh` (SSM) still PASSES: the host serves the 59e802a bundle, so the MP-pf-11 cue findings stand; waits recorded against f0d2 |
| ~01:00 | /next-calls --drive FREE option | DRIVE FORWARD | a regression read of the deny guard on the new gateway build: `deny_guard_host.sh` (SSM dce0a5d6) PASS: andrew None, opalbloomberg None, alyssa 403 (control), so the unblock of Andrew's two accounts survived the new deploy |
| ~01:27 | wait | WAIT | unchanged: no mail; manifest 319c9413a2 / mcportal 59e802a; calls f0d2, 8ed7, def4 open and Andrew's |

Open: Andrew's close run (/sprint, /rivalfunds, /yearinreview) and his "go" for the MP-v-2 window (call f0d2); calls 8ed7 and def4 are his acts; `~O`'s Z-S312 disarm waits on his close run; PD held by the CTO until OG-cp-1 and Andrew's sitting; MP-pd-7 staged to ~NFRA1 (MSTR~Z told at the GO); Z-W28-S1 and Z-W32-S1 are the issuer's two armed rows, carried on purpose (Z-S73).
