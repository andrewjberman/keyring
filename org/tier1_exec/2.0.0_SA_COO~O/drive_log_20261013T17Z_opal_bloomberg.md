# 2.0.0_SA_COO~O -- drive log 2026-10-13 01:5xZ - 17:4xZ (opal_bloomberg) -- HANDOFF before the site Z reboot

Written at about 17:48Z, on 0.0.0_AB_MSTR~Z msg 33678 ("reboot sitez", Andrew-direct). It is the whole state for the
relaunched seat.

## Round 35 -- TERMINAL, compiled

- **OG-ap-12:** COMPLETE. The schwab per-family drain was proven on the real 12:15Z sweep. Z-S100 was ruled by A2
  @d86203d41d (AC2 reads the queue).
- **OG-ap-13:** COMPLETE. The receipt @c7d4d1f4f1 was relayed to the laptop seats via 1.0.0_SA_CTO~Z.
- **OG-fd-1 and OG-tb-1:** status flipped @563fe9734a.
- **Packet and analysis:** packet `ROUND35_TERMINAL_20261013.md` @56e86a3f05, READ by 3.0.0_SA_CVO~Z. The CTO's
  round-35 analysis is @682d1ced78.
- **Housekeeping:** og-rel16c was dropped (tag `archive/sitez/og-rel16c-6aadf7db37`).

## Round 36 -- EXECUTING (issued @919f6822eb, decomp R3-T.48)

| order | slot | state |
|---|---|---|
| OG-rd-1 (E3, the 502 read) | ~62 | DRAINED @9b0c11177e; issuer rd1.AC1 PASS; worktree removed. 6 of 4165 route requests 502 at the ALB with `target_status=-` (no response from the target), and 0 gateway error records. Inferred fix: uvicorn `--timeout-keep-alive` above the ALB's 60 s idle timeout (`deploy/opal-gateway.service:16` has none). Other routes 502 too. Fix cell -> round 37. |
| OG-bd-2 (E1, the BD-fee deny) | ~60 | DRAINED @7d5db761e9; issuer bd2.AC1 and bd2.AC2 PASS; worktree removed. Release ask: `deliverables/0.9.0_WK_NFRA_OPLGTW~60/NEVER_WIDEN_ASK_OG-bd-2.md`. Its release is a later apply order. |
| OG-fd-2 (E2, the drain record and drift census) | ~61 | IN FLIGHT in `C:/tmp/og-wk61` (branch wk-NFRA_OPLGTW-61). Told to commit a WIP checkpoint before the reboot. On relaunch: read its branch, then re-seat the slot naming its commits as inherited state. |
| OG-sh-1 (E4, list_shared_folder plus the 09-29 read) | ~63 | IN FLIGHT in `C:/tmp/og-wk63` (based on bd-2's merge). Told to commit WIP. On relaunch: same as ~61. The 09-29 read's result goes to dell2 1.0.0_SA_CTO~DELL2 through 0.0.0_AB_MSTR~Z. |

## Open items

- **Gateway queue:** NFRA_OPLGTW has no release in flight. 2.0.0_SA_COO~MP was told it is free (msg 33669): MP-z-5,
  then MP-n-4. Re-cut bd-2 and sh-1's releases on the live ref then, with a combined pair.
- **Z-S91:** the remaining families' drains wait on OG-fd-2's drift census.
- **Parked on NFRA_CTLPLN (laptop):** the dell platform-secrets policy is at 5 of 5 versions.
- **Backfill law (Andrew-direct, msgs 33643/33646):** floor 2012; non-client needs 365 days. No NFRA_OPLGTW backfill.
