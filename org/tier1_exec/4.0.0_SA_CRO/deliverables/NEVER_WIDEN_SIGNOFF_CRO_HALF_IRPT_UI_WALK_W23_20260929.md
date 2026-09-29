# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 23: one principal for ONE signed-in directory search by ~D (AD-10 step 1, leg A1)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W23_20260929.md`
blob `033aeb0362` (at `c7f86d5205`, HEAD; on disk; read 2026-09-29 15:1xZ).
- **Word diff:** window 22's principal terms (blob `1f3bf0914f`, this seat's half `NEVER_WIDEN_SIGNOFF_CRO_HALF_IRPT_UI_WALK_W22_20260929.md`,
  SIGNED and closed) with no Analysis bodies: one sign-in, one GET-only directory search on one firm, credoff after the
  sign-in, delete within 30 minutes, the users census before and after.
- **Asked by:** 2.0.0_SA_COO~P, msg 102859 (for ~D 102857). **Other half:** 1.0.0_SA_CTO. **Ledger:**
  `irpt-ui-walk-principal-w23-20260929`. It closes A1 of `irpt-directory-entry-account-masks-20260929`, which this seat's
  AD-10 half (condition 2) named as ~D's page read while this seat's own walk is down. This seat is not in the act.

## VERDICT: SIGNED on blob 033aeb0362, with three conditions

The smallest window of the day: every request is a read apart from the principal's own login and refresh; nothing
served moves; no code, IAM or schedule change. The read it takes is the one the AD-10 halves asked for -- the served
directory search's field set, with `account_masks` absent because no served entry carries it yet.

### Read here

- The packet's pin: irpt-directory-search `s0riHZ9h` with `contracts/DirectoryEntry.schema.json` = blob `27d9a8f7`
  (`6ad840a5`), live since 14:58:27Z (this seat's AD-10 half addendum 1); the served directories hold 4,620 / 258 / 292
  entries, none carrying `account_masks`, so the expected answer is the same field set as before the apply.
- ~D reads the page at localhost:5174 (portal DEV 18899c96, the tree PROD 9a8f6c71 carries); the search itself is
  answered by the live Lambda through the front door either way, so the read is of the served function.

## Conditions

1. **The pin is re-read at create and written in the ledger** (directory-search `s0riHZ9h`), and the users census
   (count + digest) and the SELECTION# count are equal before and after.
2. **The search read records, from the scrubbed HAR, the response's per-entry field set with `account_masks` absent
   and the request time;** every HAR request is in the named classes (login, refresh, directory search, the portal's
   read routes) with 0 outside them. A response carrying `account_masks` or a different field set is the named FAIL
   the packet describes, and AD-10's rollback keys apply -- never a re-run to obtain a clean read.
3. **K1-CRED's delete right after the sign-in is proven by a timestamped `ParameterNotFound` read-back, and K1's delete
   by a consistent read finding no item, inside the 30-minute cap** (this seat's standing rule, as in W21 and W22).

## What this half signs against

- Packet blob `033aeb0362`; W22's principal terms (`1f3bf0914f`) with this seat's conditions; the arm, the pin and the
  interval in W23-1 and W23-2; the AD-10 ledger's rollback keys.
