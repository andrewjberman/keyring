# /self-drive AMGT_RESAPP -- tick 16 (1.0.0_SA_CTO~Z), 2026-09-21 ~22:5xZ

**Arming record:** `.../ANDREW_DIRECT_20260921_145xZ_SELF_DRIVE_AMGT_RESAPP_POST_REBOOT_REARM.md`. **state: ARMED.**
Cursor: tick 15's log @`45498244d2`.

## Since tick 15

- **rk-81 (H0-store) drained** @`0731c87fca`, 7/7 PASS.
- **rk-82 (H0-iam) drained** @`bf0f9a30ce`, 7/7; its targeted apply landed.
- **This seat's post-act read-back of rk-82**, against its signed CTO half (`iam get-role-policy`, rail-checked):
  - `opal-amgt-scoped-api-grants`: 4 statements; the read and list statements hold 21 resources and 21 prefixes (13 ->
    21); the 8 new entries are exactly the builder prefixes named in the pair, each `{p}*`, with no wildcard ahead of
    `/harvest/`. The other two statements are unmoved (2 and 1 resources).
  - `amgt-resapp-chatter-axis-lambda-policy`: 4 statements; 8 and 8 (4 -> 8); the 4 new entries are
    barrons/wsj/ft/seeking-alpha silver. The other two statements are unmoved.
  - **The act stayed inside its signed radius.** Rollback was not needed.
- rk-83..86 are unblocked by rk-81's drain (their AC0).

## Open calls in scope: 2 RESERVED at Andrew (unchanged)

CAT's EDGAR fetch (REC yes); the Lusha profile URL (REC keep).

## State

- AMGT_RESAPP: `active` / `EXECUTING`. 0 unread. Sequence: 0 flags.
- The portal pushes (rk-78, rk-80) remain at MSTR~Z.
- **COMPLETION TEST: NOT DONE.**

## Compiler Tools

`iam get-role-policy` (post-act read-back), `git log`, `safe-commit.sh`.

-- `1.0.0_SA_CTO~Z`
