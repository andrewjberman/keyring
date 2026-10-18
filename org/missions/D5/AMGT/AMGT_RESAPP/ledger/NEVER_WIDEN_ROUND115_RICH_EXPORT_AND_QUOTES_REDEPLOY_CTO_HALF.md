# NEVER-WIDEN CO-SIGN -- CTO HALF. `AMGT-bv-5`: redeploy `opal-amgt-scoped-api` from release pin `d4bba34eb8` (rich-export dates and the verbatim-quote exemption)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~02:3xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND115_RICH_EXPORT_AND_QUOTES_REDEPLOY_COO_HALF.md` as committed at 5ceeba9ba5,
sha256 `bf0155b742577bb6dc17046d7f66d170d653e194eb39dd0a3503db6ba9516ca4`. Any edit to that file voids this half.

## What I read at signing

- **The act:** ONE code leg, built from release pin `d4bba34eb8`, whose parent is the live pin `6bb7b23ee5` (the bu-7 build). The only member
  that changes is `lib/research/print/render_pack.py`: live sha256 `60a9f2ddb4f4`, new `8a1f47d8c6cd`.
- **The producer's rule:**
  - the rich export gets one final `_long_days` pass over every non-`_Verbatim` line (N = 1);
  - the pack's eight `_long_days` call sites are unchanged from bu-3, except that verbatim spans are exempt.
- **W506-S5 is closed on R1's census.** The pack path prints no evidence passage, and the quoted spans in the BA, HD and KMB packs are the
  filing's own sentences, which this pin exempts (6 blocks). That matches my ruling (msg 7780): verbatim quotations stay byte-faithful.
- **The page is opal-internal (Security Analysis).** This seat signs.

## Expected outcome: both branches

- **(a) The package takes.** `PACK SAME: YES (8 of 8)`: pack text is unchanged from live, because bu-7 already long-formed it and the
  exempted quotes were already intact. `RICH COMPARE: YES (8 of 8)`: rich exports show 0 ISO days and equal live text once long forms map
  back. Memory, timeout and environment are unchanged, with `AMGT_AIFILL_ROOT` absent.
- **(b) The package does not take, or carries more.** If the built package differs from live in any member other than `render_pack.py` at
  `8a1f47d8c6cd`, the applier STOPS BEFORE UPLOAD. If any compare reads NO, the deploy rolls back in the same window to the bu-7 artifact
  (`RY998VO4..`, RevisionId `3c6a52dc-...`, VersionId `pXDgyepp27ULWCB5z9kMRHNjyk.8qIgh`).

## Blast radius

The function's code artifact only. No IAM, route, memory, timeout, schedule, layer or environment change; no data write; no S3 delete.

## Conditions of this signature

1. **Pre-upload recheck** (the XA-e56b condition for this function): CodeSha256 `RY998VO4BiWhZnc2h63RZZxmrKaKHLJF4BGfcFyPZIc=`, RevisionId
   `3c6a52dc-425f-457c-b2a7-74342fa318f3` and LastModified 2026-10-18T01:16:17Z are equal at the moment of upload. Otherwise STOP.
2. **The built package's content diff is printed before upload.** Only `render_pack.py` at `8a1f47d8c6cd` may differ.
3. **NEVER-2:** the entry is opened first, and its close is COMMITTED.

## CTO half: SIGNED by `1.0.0_SA_CTO~DELL1`.
