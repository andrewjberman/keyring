# NEVER-WIDEN -- CTO HALF: `HVST-cf-4`, the gold continuation and dossier rebuild of 17 names that corrects C-S61 (round 91)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-17 ~21:3xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round91/NEVER_WIDEN_HALF_COO_CF4_GOLD_REBUILD_C_S61.md` as committed at
74ff9ed727, sha256 `275d5739cb747a2be93c5ad32bb06bc83530f3028bb60199167c100c719695b0`. Any edit to that file voids this half.

## Basis

- **cf-2 merged @80d0701876.** fund_of_record and last_stated_position take a fund only from a holding verb, under the classification I
  ratified (msg 7734 reply).
- W1's census read: 17 names change, with HOLDING_CHANGED = 0. Controls BABA, SHOP_CN and WALMEX are unchanged.
  - 13 names lose a fund_of_record that came from a candidate, initiate, interest or template line.
  - The four JP names (8306, 8316, 8766, 9433) lose a company-description paragraph served as their position.
- N = 2 writers, as in ce-4: `continuation.write_one` and `dossier.write_one`.

## Blast radius

- **Writes:** NEW gold continuation and dossier objects only, in `opal-data-harvest`, for the 17 names on the hashed list (221a63c3...ee48).
  That is 34 keys at most.
- **Nothing is overwritten:** the writer is write-once (GoldImmutableError).
- **Untouched:** fund_form, every other name, silver, bronze, the gateway code, IAM and Terraform.
- **Served move:** the gateway serves the newest object, so these 17 names' two fields change at once.

## Both branches

As the COO half states them:
- Branch A: each built name equals its census line, and is written.
- Branch B: a name's build differs from its census line. That name STOPS before its write, and nothing is written for it.

## Rollback

The act is ADD-ONLY. Removing the new keys is an S3 delete: Andrew's act, not pre-approved here. The seats' correction is a fixed rebuild
that writes a newer object. `cf4_written.out` is the key list.

## Conditions of this signature

1. **C-1 to C-10 of the COO half bind as written:** the pin at 80d0701876 with no fund_form change, NEVER-2, the manifest, no new grant, the
   canary MNST then 8306_JP read served first, UNH and CPA unchanged, the post-run reads, no delete, and site Z told first.
2. **The S44 rule:** each name runs as a foreground command, and the manifest is checked after every write. A gap or a missing line is a
   STOP. The run is never a background process left unwatched.
3. **The ledger close is COMMITTED,** with the manifest.

## VERDICT: SIGNED (CTO).
