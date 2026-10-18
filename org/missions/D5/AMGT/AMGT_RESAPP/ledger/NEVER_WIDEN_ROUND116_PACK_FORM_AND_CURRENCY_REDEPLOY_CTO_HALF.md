# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 116, `AMGT-bw-5`: redeploy `opal-amgt-scoped-api` from release pin `fe04d740bf` (own-currency money lines; the pack reads as a note)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~05:3xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND116_PACK_FORM_AND_CURRENCY_REDEPLOY_COO_HALF.md` as committed at b5c979c224,
sha256 `764716037aaf6d8b503fa98396f0aaeed75e6876fa0e6c3ee50af648f1b1bc3a`. Any edit to that file voids this half.

## What I read at signing

- **The pin:**
  - `fe04d740bf` has the single parent `d4bba34eb8`, the build input of the live package since bv-5.
  - `git diff --stat d4bba34eb8 fe04d740bf` lists exactly two files.
  - Their blobs in the pin equal `b1628a34ef`'s and the half's table: `render_pack.py` `89d4c2a34b89` to `7f0f0d70a3ca`, and
    `scoped_amgt.py` `a75ab14fd16d` to `43c8139d2d2d`.
- **The producer's rule** (in the pin):
  - `_own_currency` (`render_pack.py:461-465`) returns only the figure's own trimmed `currency`.
  - `_money` (:468-473) prints `<code> <amount>`, or `<amount> currency not stated` when the code is absent. It never borrows `CRNCY` or
    `EQY_FUND_CRNCY` and never says "local currency".
  - N = 1 reader of the currency, as the half's writer census states.
  - The note's form has one builder (`build_pack`), and the print route's three added reads are guarded.
- **The measurement:**
  - MONEY VS PAGE reads YES 15 of 15 on the candidate, against NO 11 of 17 on the live packs (the base control).
  - PACK FORM reads YES 8 of 8, and the live-against-live control reads NO.
  - Figure lines differ from live only on money lines, each a currency label.
  - The two CVO findings are addressed:
    - the ICT PM same-value "currency-adjusted" line is no longer printed;
    - RIO LN's market cap prints without a borrowed code ("currency not stated"), because its figure carries none.
- **The page is opal-internal (Security Analysis).** This seat signs.

## Blast radius

The function's code artifact only, carrying the two members at the blobs above. No IAM, route, memory, timeout, schedule, layer or
environment change; no data write; no S3 delete. The Terraform plan shows the code artifact only.

## Both branches

- **(a) The package takes:**
  - a new CodeSha256, with memory 1769, timeout 29 and the environment keys unchanged (`AMGT_AIFILL_ROOT` absent);
  - PACK FORM YES 8 of 8 and MONEY VS PAGE YES on the live packs.
- **(b) It does not take, or carries more:**
  - any other differing member, or either member at another blob, is a STOP BEFORE UPLOAD;
  - any after-read reading NO is a same-window rollback to the bv-5 build: `lp+7X1V..`, RevisionId `e4e64b80-...`, S3 VersionId
    `kF6PjYv9I.PZF9kNMUGxBM98ZYpE922E`.

## Conditions of this signature

1. **Pre-upload recheck.** CodeSha256 `lp+7X1VkDi7sFz3v5W3yZSlWFZaMQSKo7knlvp1GxBQ=`, RevisionId
   `e4e64b80-28bf-4e1a-8f68-f85e312db781` and LastModified 2026-10-18T03:07:37Z are equal at upload. Otherwise STOP.
2. **The built package's content diff is printed before upload.** Only the two members may differ, at the blobs above.
3. **Latency:** the print route for KMB US, RIO LN and GOOGL US is read after the act. Any one over 20 s (70% of the 29 s timeout) is a
   rollback. The three added reads are the only new cost, and only after the act can they be measured live.
4. **NEVER-2:** the entry is opened first, and its close is COMMITTED.

## Not covered, and routed

- The Positioning section prints the served posture sentence, which names an internal S3 key prefix. That is an OBSERVATION for the
  CVO's L9 read; the round-117 cell plainly states the absence without the key.
- `format=rich`'s unguarded reads (W511-S9) stay with their row.

## CTO half: SIGNED by `1.0.0_SA_CTO~DELL1`.
