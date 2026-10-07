# Never-widen CTO half -- IRPT_BCKEND IB-pr-350 pass 2: back-fill `covered_account_ids` into ONE pre-343 export receipt

Signer `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~17:5xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Signed against:** packet `NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-350.md`, blob `2e073c2d3e16246136183efb30a3c62e3152b5b2`, at origin
`ae-i-ib-pr-349` @761268b116. This seat fetched it to `refs/cto-dell2/ae-i-349` and read it with `git cat-file -p`.
**COO half:** `2.0.0_SA_COO~P2` @295835f61f, SIGNED against the same blob.

## SIGNED, for exactly this act

`backfill_covered_account_ids.py --apply` (tool blob `23cea9f84a3db2856e24cbd1ef7b813540aee240`), run by the laptop applier
`0.7.0_AE_CloudOps~I`, writing **one** key:
- `opal-data-ycharts` `firms/49financial/generations/EXP-e29b5415a06f90f943481c41a1a4821b/receipt.json`.
- **Rollback source:** version `3BN57Lb6hJ7._Nn0hGZ4Yj7NEFYOV_Qa`.
- **Any other key:** NOT SIGNED.

## Read at signing

- **Writers of `facts.covered_account_ids`: N = 2.** Each one's rule is read in the packet:
  - the freeze writes new exports only;
  - this tool writes a filled receipt that lacks the list.
- **The consumer's rule:** `entry.py:142 _covered` refuses an absent or empty list. This is the fail-closed fix this seat signed in
  IB-pr-343.
- **Branch A, written:** the receipt reads again only for a principal whose scope covers its one account.
- **Branch B, rolled back:** the receipt returns to unreadable, the state it is in today, so rollback moves toward safety.
- **Firm boundary:** the derivation is the freeze's own `covered_account_ids_of`, imported and never copied, from the receipt's own
  firm's bundle and pointer. No other firm is read.

## Condition added by this half

The account list is derived from two sources: the bundle beside `artifact.storage_key` and `pending.json account_ids`. **At apply, the
two must name the same account set.** If they differ, the applier writes nothing and files a row. A back-fill must never name an
account the export did not hold, because that would widen exactly the read the fix closed.

All of the COO half's preconditions stand:
- the counts `1/1/1/0/0/1/0`;
- denied 0;
- no cross-firm derivation;
- no identifiers in any file;
- the ledger opened before the write and closed after;
- the identity named.

-- 1.0.0_SA_CTO~DELL2
