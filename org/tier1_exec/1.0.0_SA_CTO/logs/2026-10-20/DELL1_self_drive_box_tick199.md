# DELL1 self-drive box -- ticks 198-199, 2026-10-20 ~17:48-18:19Z (delta: Track A hold lifted, 49F xref owner routed)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 18:19Z. Acked since tick 197: 8741.
- open_calls.json: 161 rows, 3 OPEN, all acts only Andrew can do.

## Calls ruled
- **NFRA_FIDUPL, my own hold on Track A (msg 8728): LIFTED.**
  - REC (b) was offered to Andrew at 18:17Z and is ruled at this tick. Nothing waits on him: the hold was mine, his hand session had not
    started (no screen command on the box since 17:22Z), and every fix is on the box (REPAIR 9 delivered at 17:25Z).
  - P1 runs ONE attempt now. If the profile is held, it stops and does not kill Andrew's Chrome.
  - If the attempt stops at the password 403, Andrew's hand sign-in becomes the next act.
- **Site Z (8741): who owns the 49F Black Diamond `dim_account_xref`?** Not dell1.
  - The `opal-assets-bd49f-*` Lambdas were last changed by 0.6.0_AE_PartnerETL and 0.5.0_AE_OpalETL~A.
  - Routed to the laptop CTO through MSTR, with a datum: dim-convert's last log event is today at 07:11:51Z, and no schedule targets
    either Lambda.

## Scope state
- **NFRA_FIDUPL:** 15 of 17 orders complete; FU-x-1 and FU-s-11 are pending. 0 objects under `fidelity/`. The 3 fetch rules are
  DISABLED. The box is running.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **The Fidelity hand sign-in** (`tmp/fidupl`), only if Track A stops at device trust (his login).
- **5013:** `claude /login` on the box (his plan). Optional.
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).

## Compiler Tools
- `comp-find` (dim_account_xref).
- `lambda get-function-configuration`.
- `events list-rule-names-by-target`.
- `logs describe-log-streams`.
- `ssm list-commands`.
