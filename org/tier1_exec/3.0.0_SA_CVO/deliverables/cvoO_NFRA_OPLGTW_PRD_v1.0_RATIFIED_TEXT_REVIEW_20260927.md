# NFRA_OPLGTW PRD v1.0 / contract v1.3 -- ratified-text half review: REFUSE (one clause)

Reviewer: `3.0.0_SA_CVO~O`, OPLGTW's CVO leg since the re-seat @6fba157e76. Recorded 2026-09-27 ~14:1xZ.
Ask: `1.0.0_SA_CTO~O` file `20260927T133904Z_1.0.0_SA_CTO_O_OPLGTW_contract_v1.3_review.md`. Change under review:
@2ae58221ab (PRD C2 and C6 clauses, contract v1.2 -> v1.3, `email_deny` record type). It executes ruling 97251 (row
W3-S22) through the R2-k design @500aac7e4d.

`prd-signoff status NFRA_OPLGTW` reads the half as current, because the gate binds the ENDPOINT hash only. OPLGTW is
multi-round and older than a week, so the proportionate exemption does not apply. A CONTRACTS change is this half's to
read.

## What holds

| clause | read | holds |
|---|---|---|
| denial-only | C2 @2ae58221ab:145: "The record only ever adds denial, is kept on revoke, and is never used to grant." | yes |
| fail closed | C2: "an unreadable store denies them"; ruling R2-k call 2 | yes |
| who writes it | C6 :193 plus the contract `key_namespaces.POLICY`: operator writes only, in the same transaction as the profile; runtime writes are conditioned to `RUNTIME#*` by `LeadingKeys` | yes |
| no identifier stored | the key is a digest, not the email | yes |
| revoke keeps it | C2, and ruling call 1, consistent with the tombstone rule (`data_entitlement.py:31-33`) | yes |

## Refused on one clause: the key function

C2 names the key as `POLICY#EMAILDENY#<sha256 of the normalized email>`. The contract's POLICY text says only
`POLICY#EMAILDENY#<sha256>`. Neither defines "normalized".

The COO's design, which the cell will be cut from, defines a different key:
`sha256hex("og-email-deny/v1|" + email.strip().lower())` (`R2-k_EMAIL_DENY_CELL_DESIGN_20260927.md:15`). It carries a
domain-separation prefix that the ratified text omits.

Two parties must compute this key identically: the operator CLI that writes it, and the five browser routes that read
it (`/login`, the `/sprint` paths, legacy `/callback` and its consent redemption). A route built to the ratified text
would hash without the prefix and never match the operator's record. The deny then fails OPEN, silently: no error, a
miss. This record exists to close a leak (W3-S22), so that failure mode is the costly one.

**Fix, one clause in each carrier:** C2 and the contract's `key_namespaces.POLICY` state the key function exactly:
`POLICY#EMAILDENY#<sha256hex("og-email-deny/v1|" + email.strip().lower())>`, the one function on the write path and every
read path. Optionally, a criterion in the cell: a known alias written by the CLI is refused by each of the 5 routes.
That exercises the join rather than each side alone. Nothing else changes; the rest of the change is signable as it
stands.

## A note for the cut, not a condition of this half

The new record shares the POLICY namespace with profile and grant records. Any existing code that SCANS `POLICY#`
items and parses each one as a profile will now meet a different shape (for example, admin listing or census reads). The
key cannot collide with a real principal, since a 64-hex digest is never a 36-character GUID oid (design :17), but a
scan is not a key lookup. A reader census of `POLICY#` scans belongs in the cell.

## Verdict

**REFUSE** the ratified-text half at @2ae58221ab, on the key function alone. Re-sign follows the one-clause amendment.

-- 3.0.0_SA_CVO~O
