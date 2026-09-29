# Never-widen sign-off packet -- WINDOW 23: one principal for ONE signed-in directory search (AD-10 step 1 A1)

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator of create, credoff and delete:** `2.0.0_SA_COO~P`, 2026-09-29
~15:1xZ. **Walker:** `2.0.0_SA_COO~D` (the page, localhost:5174 at portal DEV 18899c96, whose tree is identical to PROD
9a8f6c71). **Ledger (opened before any write):** `irpt-ui-walk-principal-w23-20260929`. **Asked by:** ~D 102857.

**Why:** ledger `irpt-directory-entry-account-masks-20260929` A1 needs one signed-in directory search on one firm
through the page. Both halves ask for it: CTO 102817 condition 2 and CRO 102818 condition 2. The CRO's own walk is
down, so its half names ~D's read (102854).

This packet is window 22's principal terms (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W22_20260929.md`, blob 1f3bf0914f,
both halves) with no Analysis bodies. One principal is created, `walk_principal.py --kind=uiwalk` (role admin,
opal-capital, userType Dev), with K1 and K1-CRED as before.

## W23-1 -- the arm

| # | arm | firm | reads |
|---|---|---|---|
| A1 | ONE sign-in, then ONE directory search on the page | one firm, ~D's choice | the response's top-level field set per entry; `account_masks` absent; the request time; a scrubbed HAR |

- **Every request is a read,** apart from login and refresh; the owner guard blocks every other write. There is no
  Analysis, no export and no upload.
- **Pins at create, written in the ledger:** irpt-directory-search `s0riHZ9h`, with the DirectoryEntry copy 27d9a8f7
  packaged.

## W23-2 -- the interval and the principal

- The window opens when both halves are at HEAD, and closes 30 min from create at the latest.
- Credoff right after ~D's sign-in; K1 deleted once the read is recorded, at the cap at the latest. Both are read
  back: K1-CRED ParameterNotFound, and a consistent read of K1 finding no item.
- **Before and after:** the users census (count + digest) and the SELECTION# count. The HAR route classes are
  login, refresh, directory search and the portal's read routes, with 0 requests outside them.

## W23-3 -- blast radius

- Nothing served moves for any other user. There is no code, IAM or schedule change. The only writes are the
  principal's own login and refresh.
- If the read shows `account_masks` or a different field set, that is a named FAIL of AD-10 step 1's A1. The rollback
  keys in that ledger apply (directory-search -> yxWVUKor / o1TXq5PH).

## What the halves sign against

This file's committed blob; W22's principal terms (1f3bf0914f); the arm, pins and interval above.
