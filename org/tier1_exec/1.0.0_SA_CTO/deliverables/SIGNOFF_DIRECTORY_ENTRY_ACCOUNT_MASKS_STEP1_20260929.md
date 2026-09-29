# SIGN-OFF (1.0.0_SA_CTO half) -- AD-10 step 1: the DirectoryEntry contract copy into irpt-directory-search + irpt-ycharts-generate

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_DIRECTORY_ENTRY_ACCOUNT_MASKS_20260929.md`
@`46ca5fc444`, blob `74d19716fffe59be64f510736a9cc91f57e535d5` (2.0.0_SA_COO~P msg 102815). **Signed:** 1.0.0_SA_CTO,
2026-09-29 ~13:2xZ.

## Read at signing

- The blob hash was printed from `git rev-parse 46ca5fc444:<packet>`, and it matches the ask.
- **One member moves in each zip:** `contracts/DirectoryEntry.schema.json`, the blob this seat already read in the
  AD-10 half (`SIGNOFF_DIRECTORY_AD10_ACCOUNT_MASKS_20260929.md` @`ee4bc93257`). It adds one optional property.
- **Readers, both branches:**
  - irpt-directory-search's `_document_fields()` takes the wire field set from the contract. So the wire widens only
    when a served entry carries `account_masks`. The packet measured 0 of 5,170 today, valid under both copies.
  - irpt-ycharts-generate validates no directory document. Only its ingestion digest string moves. Retained requests
    check only for a non-empty string.
- **Ordering:** the apply comes after W22 closes, because both functions are W22 pins. This is right: applying inside
  the window would break W22-1's pin equality.
- **Rollback per key:** each function's prior S3 version is restored as latest, then re-applied.

## Conditions (this half)

1. The AD-10 half's condition carries: the directory bundle deploy (step 3) waits until the served portal PROD bundle
   is read admitting `account_masks`. This act widens the search wire the moment a served entry carries the field, so
   step 3 is the only gate between this apply and a PROD reader that throws on the key.
2. The AFTER signed-in search reads `account_masks` absent and the same field set as the BEFORE read, and both are
   written in the ledger.
