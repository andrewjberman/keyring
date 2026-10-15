# L4-R review -- IRPT_ANLREQ PRD v0.13 @43c7157f1f, brief half -- REFUSED (one row)

**Reviewer:** `4.0.0_SA_CRO~DELL2`, 2026-10-15 ~15:3xZ. **Delivery:** msg 8387. **Half hash:** ae60b7677e30.

**What passes:**
- **FWD-7 and C-PRICES** now carry Andrew's 10-14 ~17:5xZ price order: Yahoo first, YCharts second per symbol, then the replacement, else a
  named absence. This matches record `ANDREW_DIRECT_20261014_175xZ_PRICE_ORDER_YAHOO_THEN_YCHARTS_THEN_REPLACEMENT.md` @827959566f.
- **Step (0), the estate's own stores first,** is consistent with his word, which concerned securities the estate lacks
  (@895de345f4, @c00103ac47).
- **Bloomberg is dropped from the chain.** That is a reading of his word, not his word. His chain ends at "generate the report without the
  missing security", which leaves no Bloomberg step. The reading is stated in the PRD, so it is noted, not refused.

## R1 -- BRIEF COVERAGE row 4 carries superseded content (blocking)

At `IRPT_ANLREQ_PRD.md:159`@43c7157f1f, row 4 still reads:
- "then a deterministic proxy from the designated-proxy table (MDPF_SECCLASS, dell1, a pre-arranged input)";
- "The model-proposed swap is retired".

Both are false at these bytes:
- **No designated-proxy table exists.** Provider QA @30ceaa97fa, finding 9: `org/standards/MDPF_SECCLASS_CONTRACT.json` has no proxy key.
- **The replacement is now defined differently.** The CTO's C-SWAP replacement ruling (@5deb868819, on Andrew-direct ~18:5xZ @8874273e51)
  makes the pool class-matched `etf-classifications` rows PLUS class-matched model proposals, with the longest Yahoo history winning. C-PRICES
  step (3) at v0.13 says the same.
- **The classify step changed too.** The QA found it runs on kimi-k2.6 with web search (kimi-k3's search fails at Moonshot), with the
  tool-call loop the code lacks today.
- **The frontend half changed.** C-FILING-HINT (v0.12) puts only a "Did you mean" hint on the form, and "Swaps are never offered on the
  form". Row 4's "frontend and backend" pointer to S1 should say so.

**Correction:** row 4 carries the current content:
- the form shows one catalogue "Did you mean" hint (C-FILING-HINT);
- the backend pass is KNOWN -> Yahoo -> YCharts -> classify with web search (kimi-k2.6, the loop) -> the replacement from the class-matched
  pool (registry rows plus model proposals that pass the class match and Yahoo), longest Yahoo history, ties by ticker -> RECORD `proxy_for`
  / `method` / `confidence`, named in the report;
- proof gap: one unknown holding (BREIT, SREIT or KPEC, the QA cases) through that pass.

-- 4.0.0_SA_CRO~DELL2
