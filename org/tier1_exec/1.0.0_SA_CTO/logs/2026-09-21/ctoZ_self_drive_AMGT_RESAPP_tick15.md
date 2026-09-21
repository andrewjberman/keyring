# /self-drive AMGT_RESAPP -- tick 15 (1.0.0_SA_CTO~Z), 2026-09-21 ~22:2xZ

**Arming record:** `.../ANDREW_DIRECT_20260921_145xZ_SELF_DRIVE_AMGT_RESAPP_POST_REBOOT_REARM.md`. **state: ARMED.**
Cursor: tick 14's log @`41bf31fa86`.

## Since tick 14

- **Round-21 spec calls ruled** (msg 24106): SA key `sa:<id>`; Bloomberg bronze is the client's deterministic JSON
  (`received_form: "bbg-client-json"`, to be written into C-BRONZE-AS-RECEIVED at the next bump); UNRESOLVED filings
  markers go to state; the filings silver table is `filing_source`; the six Lambda-packaged files are WALLS,
  byte-compared against the build input.
- **Round 20 CLOSED.**
  - The CVO's slug (msg 24108, `ADJUDICATION_v22` @`e94c1c3a0c`): 2 of 2, 17/0/0, and the channel reads ZERO open
    items.
  - rk-79 was measured inside its radius by the CVO's own read.
  - This seat's analysis `ROUND_ANALYSIS.round20.md` @`ab54fb15e0` (msg 24109): rk-32 and rk-50/51/52 are SUPERSEDED
    by the H-chain (C-DEDUPE-BY-KEY; rk-50's bronze broke form (a)); rk-49 stays HELD.
- **Round 21 ISSUED** @`6fb0f4d0bf`: rk-81..86 plus the four supersede flips; rk-81 (H0-store) is spawned.
- **rk-82 CTO half SIGNED** @`b3d76bc9c1`.
  - The live policy reads equal the COO's cut, and the new prefixes are empty (0 of 6, control 18).
  - Pre-granting was ACCEPTED, on the condition that each move re-reads its new grant before removing the old one.

## Open calls in scope: 2 RESERVED at Andrew

1. One EDGAR fetch for CAT's Item 1D (`C-FILINGS-ANALYZER` per-use word). REC yes.
2. Keep the Lusha public profile URL under `C-LUSHA-EXCEPTION`. REC keep.

## State

- AMGT_RESAPP: `active` / `EXECUTING`. Round 21: rk-81 running; rk-82 may spawn; rk-83..86 follow rk-81's drain.
- Still owed: the portal pushes (rk-78, rk-80) at MSTR~Z, then PROD. 0 unread. Sequence: 0 flags.
- **COMPLETION TEST: NOT DONE.**

## Compiler Tools

`iam get-role-policy` (rail-checked; exact counts and hash), `s3api list-objects-v2` (client-side count with a
control), `safe-commit.sh`, `send_message`.

-- `1.0.0_SA_CTO~Z`
