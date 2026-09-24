# /self-drive AMGT_RESAPP -- tick 13 (1.0.0_SA_CTO~Z), 2026-09-21 ~21:2xZ

**Arming record:** `.../ANDREW_DIRECT_20260921_145xZ_SELF_DRIVE_AMGT_RESAPP_POST_REBOOT_REARM.md`. **state: ARMED.**
Cursor: tick 12's log @`2eba5c60bf`.

## Since tick 12

- **The registry union defect** (MSTR~Z, ~20:44Z). After the CLOUD-into-SITEZ merge, `validate()` refused
  resources.json [197]/[215]/[216]/[226] as "redundant", and with naming-gate ENFORCE that blocked every
  .py/.json commit on this fabric (COO~Z [STUCK] msg 24069; rk-79 and rk-80 were stalled).
  - Measured: all 4 rows DISAGREE with the tokens (tokens give bright-data/lusha; the rows give prospecting,
    Andrew's CALL 2). `grade()` never reads resources.json.
  - The laptop CRO's deletion (110a50f59f) is held unpushed. Both fabrics converged on keeping the rows. The laptop
    1.0.0_SA_CTO is the ONE writer for grader edit (2).
  - **Unblock @`55c24a8b8a`:** one line in `lib/opal_naming.py` (`if not rph and _rsysv == system:`).
    - validate went from 4 refusals to 0.
    - The positive control (a row whose system equals the tokens) is still refused.
    - It passed the enforcing gate.
    - The same line was sent to the laptop CTO byte-for-byte (msg 24073).
- **Z-S203 filed @`39731fbda7` (ARMED, disarm_owner 4.0.0_SA_CRO).**
  - The problem: scopes.json carries two `harvest` rows, and `lookup()` takes the PRODUCT one. So `address()` prints
    AMGT bronze and silver into opal-data-assets (Andrew's veto) and platinum into opal-data-portal-v2.
  - The fix: deleting row [8] alone puts all tiers in opal-data-harvest. 4.0.0_SA_CRO~Z confirmed this with controls
    (msg 24080).
  - Only PLATFORM_LOGIC_DOCS lanes may write it, and ~Z is not one of them. It is routed to the laptop CRO via
    MSTR~Z (msg 24082).
  - It is an EXPOSURE: no harvest writer has been cut.
- **Ruled: platinum's home is the builder's output**, opal-data-harvest (Rule 30 and Andrew's "whole pipeline in
  harvest"). The v0.16 C-HARVEST-HOME "R6" clause is the defect, and v0.17 corrects it (msg 24085).
- **The backfill registry precondition is now ONE row deletion.** tiers.json GENERAL and the five vendor rows are on
  SITEZ.
- MSTR~Z's stray scopes.json in the shared tree (its unstaged merge edit) is reverted, so the tree is clean.

## Open calls in scope: 2 RESERVED at Andrew

1. Who deletes scopes.json [8]: (a) the laptop CRO via MSTR, already routed; or (b) a one-act override for this seat.
   Citation: `.owned-paths.yaml` PLATFORM_LOGIC_DOCS, with the lane escape being `GIT_COMMIT_AUTHOR_OVERRIDE`, audited
   (CLAUDE.md 14a). REC (a), with (b) if it is slow.
2. One EDGAR fetch for CAT's Item 1D. Citation: `C-FILINGS-ANALYZER`, *"A validation run needs his per-use word."* REC
   yes.

## State

- AMGT_RESAPP: `active` / `EXECUTING`. Round 20: rk-80's portal is at MSTR for the DEV push; rk-79 is re-trying its
  commit after the unblock. 0 unread. Sequence: 0 flags.
- **Next:** rk-79's read-back and the S197/S200 disarms; v0.17 (Lusha s.11 close plus the platinum clause); round 20's
  L8/L9.
- **COMPLETION TEST: NOT DONE.**

## Compiler Tools

`lib.opal_naming.validate`/`grade`/`address`/`lookup` (live plus scratch-registry probes), `safe-commit.sh`,
`send_message`.

-- `1.0.0_SA_CTO~Z`
