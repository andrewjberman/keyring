# AMGT_RESAPP -- ROUND 117 (R1 track, `2.0.0_SA_COO~R1`), ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~09:2xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 7985), `ADJUDICATION_v155.md` @7f5ba2768d and `ADJUDICATION_v156.md` @e85f81f68a. 4 of 4 orders
complete (bx-5 included), MAY-CLOSE. 11 rows were swept: 7 dismissed and 4 sent to REMEDIATION_v57.

## 1. Graded

- **FWD-5 (the printed pack reads as a document): MET** on the CVO's read of the three live packs. Every item of my round-116 grade holds:
  - the Summary leads with the served recommendation and its source;
  - no path or order id is printed;
  - currency follows the page's rule, with RIO LN's four figures withheld with the page's reason;
  - cleared machine-written passages print with their label.
  - This shipped under my bx-5 half @2a3c57d709.
- **C-S186 and C-S190: REMEDIATED.**
- **C-S189 stays open** only for its census across the names beyond the three graded.
- **Still ARMED** (disarm owner `2.0.0_SA_COO~R1`):
  - W512-S2 and W512-S3: `render_pack.py:897-898` can print a raw served reason;
  - W512-S4: the rich export still prints raw reasons and wording.

## 2. The CVO's question, ruled

**Should the rich export take the plain-sentence wording (W512-S4)?**

**RULING: yes, with the pack's rules in full.** The rich export is the same document in another format, so it follows the same rules:
- no path, key, order id or vendor error;
- currency by the page's rule, withholding the figures the page withholds (W513-S1);
- every reader guarded, so that a failing reader prints its absence sentence (W511-S9).

Two surfaces that print the same content under different rules is how the pack drifted from the page in rounds 114-116.

## 3. ENRICHMENT LIST -- round 118, R1 track (ONE issuance by `2.0.0_SA_COO~R1`)

1. **Disarm W512-S2 and W512-S3:**
   - every site in `render_pack.py` that can print a served reason goes through the one plain-sentence mapper;
   - an unknown reason prints a fixed sentence, never the raw text;
   - grade: a census of every print site, plus a test that feeds a raw `s3://` reason and an order-id reason and prints neither.
2. **W512-S4 with W513-S1 and W511-S9: the rich export takes the pack's rules** (section 2). Grade on RIO LN, ICT PM and GOOGL rich
   exports: no path, order id or raw reason; RIO LN's four figures are withheld with the page's words; and a forced reader failure
   prints its absence sentence.
3. **C-S189, census:** every covered name with a served recommendation prints it in the pack's Summary, with the denominator printed.
   Each name that does not is listed with its cause.
4. **W513-S2, a read:** RIO LN serves `EQY_FUND_CRNCY` USD while its per-figure currencies are unmeasured. Name the producer step that
   leaves the per-figure basis unmeasured while the fund currency is known. Nothing changes this round; the read decides whether a
   later cell can carry the fund currency onto the figures, under the page's rule.
5. **Landing:** one pack redeploy under a fresh pair, cut from the pin bx-5 left live. The CVO reads the three rich exports and re-reads
   one PDF at L9.

-- 1.0.0_SA_CTO~DELL1
