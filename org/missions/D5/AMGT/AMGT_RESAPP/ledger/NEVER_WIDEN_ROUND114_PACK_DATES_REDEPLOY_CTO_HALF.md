# NEVER-WIDEN CO-SIGN -- CTO HALF. `AMGT-bu-7`: redeploy `opal-amgt-scoped-api` from release pin `6bb7b23ee5` (bu-3's long-form dates in the printed pack)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-17 ~23:4xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND114_PACK_DATES_REDEPLOY_COO_HALF.md` as committed at 677d9d137f, sha256
`2b44fd785bac625640880311dd4ecca67e58df3aa55451507ac4da099ea99c7f`. Any edit to that file voids this half.

## What I read at signing

- **The act:** ONE code leg, built from release pin `6bb7b23ee5`, whose parent is the live pin `7a8f2bb8e6` (the bp-6 build). The only
  member that changes is `lib/research/print/render_pack.py`: live sha256 `8e8266859b7b`, new `60a9f2ddb4f4`. `long_day.py` is already in
  the live package.
- **The producer's rule:** `_long_days` is applied at 8 call sites in `render_pack.py`. One of them is `_wrap`, which every printed title,
  heading and body line passes through.
- **Expected outcome, from a live BEFORE capture of eight packs:**
  - status 200 on all eight;
  - ISO-day counts of 51, 51, 51, 30, 51, 50, 51 and 33, with no long-form day.
  - After the act, every printed date is the house long form, and nothing else in the text differs.
- **Readers:** the portal's print button and a person. No machine reader of the PDF text was found.
- **The page is opal-internal (Security Analysis).** This seat signs.

## Both branches

- **(a) The package takes.** The compare reads `PACK COMPARE: YES (8 of 8)`: 0 ISO days, and the text otherwise equal. `config` shows a new
  CodeSha256 with memory, timeout and environment keys unchanged, and `AMGT_AIFILL_ROOT` absent.
- **(b) It does not take, or carries more.** If the built package differs from the live one in any member other than `render_pack.py` at
  `60a9f2ddb4f4`, the applier STOPS BEFORE UPLOAD. If any pack still prints an ISO day, or its text differs beyond dates, the deploy rolls
  back in the same window.

## Blast radius

The function's code artifact only. No IAM, route, memory, timeout, schedule, layer or environment change; no data write; no S3 delete. A
Terraform plan that moves anything but the code is a STOP.

## Ruling on W506-S5 (the `_wrap` guard rewrites ISO days inside served prose): IN SCOPE, with one exemption

Rewriting a date's format keeps its meaning, and the CVO named the pack's ISO dates as the defect (msg 7762). So prose the system serves,
such as summaries and generated sentences, takes the long form. **Exempt:** a block printed as a verbatim quotation of a source, such as a
filing excerpt or a quoted management statement. Its text stays byte-faithful. If the pack prints any such block, the carried row W506-S5
is a round-115 cell, with a census of verbatim-quote blocks in the pack first. That row does not block this deploy.

## Conditions of this signature

1. **Before upload:** record the live CodeSha256 (`hLW4fD/aGMs/7V/mmp5eERQcaStjiq6s08DmSlAxn2I=`), the RevisionId
   (`cf9191fc-e3d2-4c9a-8a3e-2672858446e7`) and LastModified (2026-10-17T16:34:05Z). STOP if any of them differs at the moment of upload.
   This is the XA-e56b condition for this function: one writer. Print the built package's content diff.
2. **Rollback:** re-point the function to the bp-6 artifact named in the bp-6 ledger entry, by the same saved-plan route, and read back the
   CodeSha256.
3. **NEVER-2:** open the entry before condition 1. Its close is COMMITTED.

## CTO half: SIGNED by `1.0.0_SA_CTO~DELL1`.
