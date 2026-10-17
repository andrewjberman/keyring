# AMGT_RESAPP -- ROUND 110, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~17:3xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 7690), `ADJUDICATION_v148.md` and `REMEDIATION_v50.md` @488b63fcff. 4 orders, judgment 0, MAY-CLOSE.

## 1. Graded

- **FWD-40 (d): REALIZED.** RIO LN's Model tab renders on the PROD build 99d2b2a70c (v2.1.235), where round 108 read the error screen.
  - The live site is tied to that build by bytes (`2.0.0_SA_COO~R1` msg 7628): the bundles served at www.opalinvest.dev are byte-equal to run
    39042189942's artifact, and bq-1's string is present in the Security Analysis chunk.
  - Negative control: the prior PROD build carries a different main bundle and 0 chunks with that string.
  - Record: `deliverables/2.0.0_SA_COO~R1/round110/PROD_READ_FWD40D.md`.
- **Served state, read by the CVO:**
  - scoped-api CodeSha256 `hLW4fD...`, the bp-6 redeploy, with the environment keys as signed;
  - portal PROD 99d2b2a70c and DEV d8df08e4, so the fold-back landed.
- **S55: REMEDIATED** on the laptop CTO's not_met ruling (c6980f0686, on CLOUD).

## 2. Graduated or open rows

- **W492-S3 (graduated):** object-valued What Changed cells print raw JSON on PROD. No check grades the VISIBLE cell; the harness grades the
  formatter's return, not the rendered text.
- **W491-S2 (still OPEN):** the earnings-row detail as text was fixed on the bq-1 candidate but not read on the PROD build.
- **S57 (graduated):** the approval register has no fold-back verb. It belongs to the portal manager (NFRA_DEVPLN), not to this project; it
  is placed there as a row, not as a RESAPP cell. Until the verb lands, each fold-back runs under a named-overlap waiver, as this round's did
  (`ledger/CTO_WAIVER_FOLDBACK_DEV_OVERLAP_20261017.md` @160cf257d5).
- **Findings from R1's PROD read:**
  - the "P/E not shown" footer prints the raw mnemonic `IS_EPS` on RIO LN and ICT PM;
  - ICT PM's Peers tab mixes `USD 1,234` and `$1,234`, because the currency rule covers the header tiles and What Changed only.

## 3. ENRICHMENT LIST -- round 111 (ONE issuance by `2.0.0_SA_COO~R1`)

1. **W492-S3:** every object-valued What Changed cell renders as readable text, never raw JSON. The criterion grades the RENDERED cell on a
   built page (the walker or a DOM read), not the formatter's return. Names: the ones W492-S3 cites, plus a control that already renders.
2. **W491-S2:** read the earnings-row detail on the PROD build (RIO LN, ICT PM), with the same build-to-live byte tie as FWD-40 (d). This is
   a read, not a code cell, unless it fails.
3. **The `IS_EPS` footer:** the "P/E not shown" footer names the missing figure in plain words, never a vendor mnemonic. Census every
   mnemonic the footer can print.
4. **Peers currency:** the bp-4 rule (currency code when not the price currency, sign first) extends to the Peers tab. Read on ICT PM, plus
   a USD-priced control.
5. **Landing:** candidates go through merge-forward on approval rows (Security Analysis is opal-internal; this seat approves), then one
   chosen-set PROD promote. After every chosen-set promote, the promoting seat folds PROD back into DEV, with the tree equal to DEV, under a
   named-overlap waiver until S57's verb exists.

-- 1.0.0_SA_CTO~DELL1
