# NEVER-WIDEN -- CTO HALF: `HVST-ce-4`, the gold continuation and dossier rebuild of 31 securities (round 90)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-17 ~17:0xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round90/NEVER_WIDEN_HALF_COO_CE4_GOLD_REBUILD.md` as committed at 2fe63a70d6,
sha256 `5b486cda583f96ac546085975496b1f0675b1d7ebb4f9e73a1ff1df2223c6149`. Any edit to that file voids this half.

## Blast radius (the act may touch only this)

- **Writes:** NEW gold objects only, in `opal-data-harvest`: for each of the 31 names in `ce4_securities.txt` (sha256 7881772d...), one
  `research-continuation` object and one `research_dossier` object. That is 62 keys at most.
- **Nothing is overwritten:** `GoldImmutableError` refuses any overwrite. No existing object is changed or deleted.
- **Served move:** the gateway serves the newest object, so `harvest_get_research` for these 31 names changes at once.
- **Untouched:** the gateway code, every other security, silver, bronze, `fund_form` and `sector_template`, schedules, IAM and Terraform.

## The rules read for the outcome

- N = 2 writers of the property: `continuation.write_one`, which derives through `_resolve_fund_and_position`, and `dossier.write_one`,
  which copies both fields from the stored continuation (`dossier.py:1490-1502`). No schedule runs either.
- The census (`ce2_census.out`, 94 of 94) gives 30 names going from absent to a value, and 0 changing value to value.

## Both branches (as the COO half states them)

- **The 30 names:**
  - Branch A: the built value equals the census line, and it is written.
  - Branch B: the built value differs from the census line. That security STOPS before its write, and nothing is written for it.
- **KMB:**
  - Branch X: the fields are absent after the exclusion.
  - Branch Y: the fields carry a value from a remaining report.
  - Either branch is valid only if the built JSON contains 0 occurrences each of `fbd50086c4065785` and `1a3b56044db679a5`. Otherwise
    STOP before the write.

## Rollback

The act is ADD-ONLY, and the pre-act state returns when the new keys are removed. Removing them is an S3 delete, which is Andrew's act. It is
not taken by any seat, and this half does not pre-approve it. The seats' own correction for a wrong value is a fixed rebuild that writes a
still newer object. The manifest `ce4_written.out` (C-3) is the key list for either route. The two-name canary (C-6) bounds the exposure
before the other 29 are written.

## Conditions of this signature

1. **C-1 to C-8 of the COO half bind as written:** the code pin proof, NEVER-2, the write manifest, no new grant, serial order, the canary
   read served before the other 29, the control `CPA_US_Equity` unchanged, and no S3 delete.
2. **Added, C-9: site Z is told first.** AMGT_HARVST also runs on site Z (the gateway release lineage, cd-2's C-8). Before the first write,
   `0.0.0_AB_MSTR~DELL1` relays to site Z that dell1 writes up to 62 gold objects in `opal-data-harvest` for these 31 names. The relay
   names the window, and asks that no site Z rebuild of any of them run during it. A site Z rebuild in flight on any of the 31 is a STOP.
3. **The ledger close is COMMITTED,** and the manifest is committed with it.

## VERDICT: SIGNED (CTO).
