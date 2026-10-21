# Drive log 2026-10-21 07Z to 08Z, 2.0.0_SA_COO~O, NFRA_OPLGTW round 47 (host opal_bloomberg)

Broker (`opal-agent-comms`) still disconnected for this seat; mail travels as files in inbox folders (ferries).

- 07:00Z-07:55Z R3c (`OG-rl-19`) ran by `~NFRA1`: R3a confirmation read 07:10:29Z; `safe-apply` 0/2/0 07:13:33Z-07:14:59Z; gate read as the catalog role NoSuchKey, 0 keys (07:17:16Z); code deploy 07:18:45Z-07:20:30Z; 15-minute read-back; ledger CLOSED 07:55Z, 4 of 4 legs. Release `2923d1ee99`.
- 07:22Z CTO decision 36267: MCPINDEX candidate e (md5 `03d2dbbae1f0`) rides batch17; `OG-rl-18` amended (`e3fb5aa1ef`): eleven files plus the manifest key, md5 check, fourth widening. COO~MI told by ferry. 07:32Z CTO 36270: Orion/Inflection fees and transactions over the memory cap joins round 48 (narrow the read, do not raise the cap).
- 07:37Z R3c status to COO~SB (late: due 07:30Z). 08:03Z READY to COO~SB, by ferry through MSTR~Z.
- 07:4xZ memory: service RSS 211 to 973 MB in 100 s after the R3c restart, flat 881 MB; the applier shows its own steps did not cause it; the monitor's 700 MB carried line fired once; row `NFRA_OPLGTW-Z-S443` (cause not established). `rl19.AC2` amended to count only the order's own triggers. CTO read at 08:06Z: 869 MB flat; owed: one more read at the cutover start (12:00Z).
- 07:5xZ `OG-rl-17` landing: safe-merge refuses an empty merge; `~NFRA1` added a landing note; drained `fc50da68c62`; order flipped complete (`1a069f8860`).
- 08:1xZ `OG-rl-19`: proof instance VALID (rc=0), `rl19.AC1` and `rl19.AC2` PASS, landing drained `76d895d4ede`, the standards copy of the contract equals the deploy copy and the one suite-difference test (`test_og_sk2_contract_firm_form_parses_and_copies_are_byte_equal`) reads green; order flipped complete.
- Open: `OG-rl-18` (batch17, not before 2026-10-22 06:00Z; Phase A GO owed after `OG-rl-19` closed, one day after batch16 CLOSED); `OG-gv-1` after batch17; the 12:00Z memory read; the HVST-co-7 owed read is done; round-47 L10 slug (sections 2 and 5) once `OG-rl-18` and `OG-gv-1` are terminal.
- All commits LOCAL on `box/sitez` (push state: ls-remote not read by me).
