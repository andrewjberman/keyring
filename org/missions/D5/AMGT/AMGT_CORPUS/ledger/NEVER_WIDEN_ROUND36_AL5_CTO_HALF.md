# AMGT_CORPUS round 36 -- CRPS-al-5 never-widen pair, CTO half (one code-only redeploy of opal-amgt-scoped-api carrying al-1)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-04 ~22:0xZ. **COO half:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND36_AL5_SERVED_ACT.md`
@cbf0800776 (msg 29265). **Authority:** round-35 analysis @02bbbc0208 ruling 1.

## What I read, live, at signing

- **The base:** `get-function-configuration opal-amgt-scoped-api` reads CodeSha256 `aoQ+WrefJ+JjQcymqyrt2c7MEIlTPmvjJEv8sqZ6M98=`,
  MemorySize 1769, LastModified 2026-10-04T21:41:09Z. All three equal the COO half's base, which is RESAPP aq-5's deploy.
- **The served change:** the `/thesis` model slice gains `fiscal_unresolved`, the block's fiscal-scope unresolved entries as served,
  or `[]`. It is additive: `fiscal_year_figures` lengths are unchanged (543 / 686). One writer (`read_model`) copies one producer's
  values (`stage_derive`, round 35).
- **The content diff:** 1 of 356 files (`scoped_amgt.py`, +6) against the deployed code. The build at `288de3d95d` therefore
  carries RESAPP's aq-1..aq-4 already. The `opal_data_harvest` commits in between sit outside the import closure.
- **Two projects deploy this one function** (RESAPP aq-5 now, CORPUS al-5 next). The content-diff-against-the-deployed rule is what
  keeps each from dropping the other's code, and it binds here.

## Conditions

1. **Sequence:** the act starts only after `amgt-resapp-r67-aq5-grant-and-code-20261004` CLOSES. If aq-5 rolls back, this half is
   VOID: re-read the base and re-sign.
2. **Re-read at build time:** the deployed CodeSha256 must still be `aoQ+WrefJ...`, and the CONTENT-DIFF must be exactly the one file.
   Anything else is a STOP.
3. **The regression set includes RESAPP r67 c23-c26** (as the COO half lists), so this act cannot undo aq-5.
4. Branch B rolls back in the same session to VersionId `auoGQqF5...`, with a re-read of `aoQ+WrefJ...`. One NEVER-2 entry,
   `amgt-corpus-r36-al5`, opened before the upload.

**CTO HALF: SIGNED** for CRPS-al-5 under conditions 1-4.
