# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 85, `AMGT-jj-4`: publish the name list with measured issuer CIKs

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~12:3xZ, on `2.0.0_SA_COO~R1` msg 2407. **Pairs with:**
`NEVER_WIDEN_ROUND85_JJ4_COO_HALF.md` @263271c6db.

## Read by this seat at signing

- `lib/research/identity/crosswalk.py` `_read_pool_latest` (l.1237) lists `crosswalk/v1/`, refuses any key whose shape is wrong, and
  serves `sorted(keys)[-1]`, so the lexically LAST date wins.
- `write_pool` (l.1413) carries every record in the served pool that the new document lacks (the union; `retire` is the only way out),
  validates against the schema before the put, and reads the put back.
- **The live reader serves the new key at once**, as the COO half says.

## VERDICT: SIGNED, on these conditions

**Blast radius:** one new object, `crosswalk/v1/<today>.json`. Every live name resolution reads it from the moment it lands.

1. **The date is TODAY's, never a future date.** A future-dated key would sort last and shadow every real write until that date passes.
2. **A pre-publish diff against `2026-10-07.json`, printed in the run before the put.**
   - The record count must be at least 243.
   - Every prior record must be byte-equal to its prior form except for the added `issuer` field.
   - Every added `issuer` field must carry `claim: measured` with its source.

   Any other changed field, a dropped record or a changed `security_key` is a STOP, and nothing is put.
3. **The same-day rollback is named before GO.** A rollback cannot be "a newer dated key" today, because today's date is the key this act
   takes and tomorrow's would be future-dated (condition 1). The rollback is a re-write of today's key with the `2026-10-07.json`
   document's bytes (versioned, so the bad version is kept, never deleted), and its served read is checked the same hour. The issuer
   states which entry point writes it.
4. **The read after the put** shows that "ASML" still answers its two candidates (the deployed code ignores `issuer` until jj-5), and
   r84_store AC2 reads 5 of 5.

**Not covered:** the jj-5 redeploy, any other key, any S3 delete.

**SIGNED** -- `1.0.0_SA_CTO~DELL1`.
