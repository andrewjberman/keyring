# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 117, `AMGT-bx-5`: redeploy `opal-amgt-scoped-api` from release pin `9ab6d36305` (served recommendation, page currency rule, labelled cleared passages)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~07:3xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND117_PACK_SUMMARY_CURRENCY_AND_PASSAGES_REDEPLOY_COO_HALF.md` as committed at
871379e429, sha256 `60734f0e8167154f8c732b86ebf71cc97141959b3c24fa941395ce9db487f041`. Any edit to that file voids this half.

## What I read at signing

- **The pin:**
  - `9ab6d36305` has the single parent `fe04d740bf`, the build input of the live package since bw-5.
  - `git diff --stat fe04d740bf 9ab6d36305` lists exactly one file, `render_pack.py`.
  - Its blob in the pin is `329f8b4e9304`, equal to `0367a39372`'s and to the half's table.
- **The cleared-passage rule** (`_cleared_passage`, `render_pack.py:913-929` in the pin). A machine-written block prints only when all
  of these hold:
  - the fill is SERVED;
  - the block's text is non-empty and comes from a page source class;
  - its validation is CLEARED with verdict PASS and a dated check.
  - In any other state nothing prints, with no label and no placeholder.
  - That is my round-116 ruling: what the page shows, cleared only.
- **The other rules**, as the half states them:
  - the Summary reads one field, `dossier_fields.last_stated_position`, the one the page's Posture tab reads;
  - a figure is withheld when its `currency_basis` begins UNMEASURED, which is the page's rule and my corrected item-3 grade;
  - state sentences name no path, key or order id.
- **The measurement:**
  - PACK FORM reads YES 8 of 8, against the live base control NO 3 of 8;
  - MONEY VS PAGE reads YES 16 of 16, against the base NO 12 of 16;
  - RIO LN leads with MAINTAIN 2.75% IDVZ and prints the labelled Trott profile;
  - HD US and TSM US print no passage, because their fills carry no text.
- **The page is opal-internal (Security Analysis).** This seat signs.

## Blast radius

The function's code artifact only, carrying the one member at the blob above. No IAM, route, memory, timeout, schedule, layer or
environment change; no data write; no S3 delete. The Terraform plan shows the code artifact only.

## Both branches

- **(a) The package takes:**
  - a new CodeSha256, with memory 1769, timeout 29 and the environment keys unchanged (`AMGT_AIFILL_ROOT` absent);
  - PACK FORM YES 8 of 8 and MONEY VS PAGE YES 16 of 16 on the live packs;
  - the print route under 20 s for KMB US, RIO LN and GOOGL US.
- **(b) It does not take, or carries more:**
  - any other differing member, or this member at another blob, is a STOP BEFORE UPLOAD;
  - any after-read reading NO, or a print route over 20 s, is a same-window rollback to the bw-5 build: `lNWo6Cm6..`, RevisionId
    `2eecd7e1-...`, S3 VersionId `EVD2sGd8Bb.DGRU1XjvuhPJ6cOJo.otg`.

## Conditions of this signature

1. **Pre-upload recheck.** CodeSha256 `lNWo6Cm6AjLrkBeu2rB25cpbcaVTXLgVH7RQ+dQGmtg=`, RevisionId
   `2eecd7e1-03b4-4f34-bec7-767bbd437a6e` and LastModified 2026-10-18T05:52:41Z are equal at upload. Otherwise STOP.
2. **The built package's content diff is printed before upload.** Only `render_pack.py` may differ, at the blob above.
3. **A negative control on passages after the act:** one live name whose fill holds an uncleared block prints no passage and no label
   for that block. Name it and read it. If no such name exists in the live pool, state that.
4. **NEVER-2:** the entry is opened first, and its close is COMMITTED.

## Not covered, and routed

These stay with their rows:
- the `format=rich` export's raw amounts and verbatim reasons (W513-S1, W512-S4);
- RIO LN's served `EQY_FUND_CRNCY` USD beside per-figure currencies that are not served (W513-S2).

## CTO half: SIGNED by `1.0.0_SA_CTO~DELL1`.
