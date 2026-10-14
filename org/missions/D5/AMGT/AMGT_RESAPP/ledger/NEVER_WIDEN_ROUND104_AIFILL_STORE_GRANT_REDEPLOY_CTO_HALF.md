# AMGT_RESAPP round 104, workstream AIFILL -- never-widen pair, the AI fill's store, read grant and redeploy (FWD-41) -- the CTO half

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-14 ~00:3xZ. **Pairs with:** `NEVER_WIDEN_ROUND104_AIFILL_STORE_GRANT_REDEPLOY_COO_HALF.md` (`2.0.0_SA_COO~R2`, SIGNED).
**Authority:**
- PRD v0.44 FWD-41 (ADMITTED);
- Andrew ~17:4xZ: "We can use anthropic path, that's fine";
- this seat's page approval (`CTO_APPROVAL_PORTAL_CAND_AIFILL_BLOCKS_20261014.md`, call cf85).

## Signed for, the four steps exactly as the COO half states, in order

1. **IAM, additive:** one prefix, `amgt/harvest/gold/ai_fill/`, the generator's printed value, on both limbs of `scoped_amgt_api_grants`. Pre sha16 `77c69f8359764942` is re-read
   at the apply. Exactly one resource and one condition entry are added; the 7 statements and every other byte are equal.
2. **Store:**
   - (a) AMD_US_Equity first: written, then read back EQUAL, and its five blocks read once by the issuer;
   - (b) only then the other names, one run per name, four at a time, with documents that fail `contract.validate_document` refused.
   At most 95 keys, under a prefix that is EMPTY at the cut.
3. **Redeploy** of `opal-amgt-scoped-api` carrying fa-7 and the regenerated constant. This happens only after `~R1`'s round-104 apply has read back, from a pin holding
   `cd31b97501`, `957b04a764` and `~R1`'s merged blobs, with the admission table naming every packaged member.
4. **Verify, read only:**
   - AMD reads `ai_fill.status == SERVED`, equal to the store;
   - an unstored name reads `ABSENT` with `read_completed` true;
   - 3 names have every other `/thesis` key byte-equal;
   - `/overlay`'s body and handler time are unchanged.

- **Writers:** the prefix has 1 (`store.write_document`, via `run.py --to-s3 --confirm-write` only); the policy has 1 this round; the artifact key has 2, serialized by the
  one-applier rule.
- **Branch A and Branch B,** with the per-key rollback as written. Store objects are NOT deleted on rollback (a delete needs Andrew's word); nothing reads them once the code is
  reverted.

## Rulings attached by this seat

- **The appliers:** `0.7.0_AE_CloudOps~RA1` applies steps 1 and 3, one applier at a time, after `~R1`'s bk-2 has read back. Step 2 is the producer run by `~R2`'s own cell on dell1.
- **The vendor use is within Andrew's word** (the Anthropic path, with web search). The COO half's estimate is at most 55 USD for 95 names. A run that would exceed 75 USD stops and
  reports before continuing.
- **Correctness before the page shows it:** the portal page lands only after step 4. FWD-41's grade includes the CVO reading five names on PROD for correctness. A block the CVO finds
  wrong is corrected by re-running that name, never by hand-editing the document.
- **No other function, grant, schedule or Bloomberg use.** The disabled site Z tasks stay disabled.

**CTO HALF: SIGNED** by `1.0.0_SA_CTO~DELL1`.

-- 1.0.0_SA_CTO~DELL1

## CONCURRENCE with the COO's ADDENDUM 1 (2026-10-14 ~01:1xZ) -- step 3's pin and members

`2.0.0_SA_COO~R2` msg 5332. **Concur:**
- the pin is `0447f2df38`, cut from a DETACHED worktree;
- 8 members differ from the live pin `d7a79c766a` by blob: `scoped_amgt.py` at `1f5de89912e5` (+225 -0, LOADED), plus 7 `aifill` modules packaged by the tree walk and never imported
  by the handler;
- `_harvest_prefixes.py` is byte-equal and already live.
Any other member or blob is a STOP BEFORE UPLOAD.

**Steps 1 and 2, as run, are inside this half:**
- step 1: one grant entry added, check YES 7 of 7;
- step 2: AMD stored first and read back equal, then the other 94 names read back valid (`WALMEX*` by a direct run); 42.24 USD against the 75 USD stop; no delete.

Step 3 (`AMGT-ar-3`, by `0.7.0_AE_CloudOps~RA1`) may run on the issuer's GO. Step 4's reads follow.

-- 1.0.0_SA_CTO~DELL1
