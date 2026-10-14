# CTO ruling -- IRPT_ANLREQ price sources after the CRO's coverage read; call 3dab is superseded by one YCharts-route question for Andrew (2026-10-14 ~16:2xZ)

From `1.0.0_SA_CTO~DELL2`, on `4.0.0_SA_CRO~DELL2` msg 7753 (`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261014_ANALYSIS_REPORT_PRICE_COVERAGE.md`
@895de345f4).

## What the read changed

- **MDPF_SECHIST's series store holds 0 objects** (its writer ships off). The estate's live per-security prices are MDPF_DEMQUE's Yahoo price
  store (483 securities), plus the Opal ETFs' Bloomberg history and the model series.
- **The "single YCharts data call" does not exist today.** The gateway's YCharts tools replay a shared signed-in session cookie, one symbol
  per call, and no official YCharts API key exists.
- **The benchmark ^SPXTR** (beta, alpha) and 4 holdings (DGRO, SPHY, SPYM, VGSH) are held nowhere. 4 more are thin (about 6 months).

## Ruling

1. **FWD-1 is unaffected.** The report renders with NOT_AVAILABLE sections (round-40 ADDENDUM). Prices are trace hop 9, the first
   enrichment AFTER FWD-1.
2. **C-PRICES is restated at hop 9's cut, not now.** No cell reads it before then, and a CONTRACTS change re-opens the ratified half. The
   restatement is:
   - the estate's live stores first: the MDPF_DEMQUE price store and the Opal ETFs' Bloomberg history. These are dell1-owned stores, read
     only;
   - then the YCharts route Andrew chooses (call below);
   - then yfinance, labelled UNVERIFIED;
   - and Bloomberg through its queue for anything still absent, ^SPXTR first.
3. **Call `dell2-20261014T155942Z-3dab`** (YCharts before or after yfinance) is SUPERSEDED. Its premise, that a single data call exists, is
   false. It is replaced by ONE call for Andrew on the YCharts route.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM (~17:4xZ): Andrew-direct ~17:3xZ answers call 91d4

Verbatim: "We can use yahoofinance for this if it works. If it does not work, keep in mind we keep a long-term trust token, and the associated
ec2 crawl/lambda rest api pattern for authenticated access." Record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_173xZ_YFINANCE_FOR_GAPS_ELSE_YCHARTS_TRUST_TOKEN.md`.
The CRO's probe (17:38Z): `^SP500TR` (the benchmark's real symbol, not `^SPXTR`) from 1988, and all 8 missing or thin holdings at full
history. 16 symbols took 2.21 s. The last row is today's intraday.

**C-PRICES, restated at hop 9's cut:**
1. The estate's live stores: the MDPF_DEMQUE price store and the Opal ETFs' Bloomberg history.
2. yfinance for the gaps, each row cut at T-1 by `lib/trading_calendar.py` (never today's intraday row), each price carrying `source: yfinance`.
3. YCharts through the long-term trust token's EC2-crawl / Lambda REST pattern, only where yfinance fails. The CRO measured it at ~17:4xZ
   (@17a04396f2): `fund_data` 200 in 0.1-0.5 s, about 2.3 s per symbol at the client's 2 s spacing, 5 years per symbol, ONE symbol per call.
   **It cannot batch,** so the PRD v0.9 words "one ... call ... batched" are replaced at hop 9's cut by "only for the symbols yfinance
   lacks, one per call".
4. Bloomberg through its queue, last.

Calls 91d4 and 3dab are CLOSED on this record.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 2 (~18:1xZ): Andrew-direct ~17:5xZ sets the full chain (it supersedes ADDENDUM 1's list)

Verbatim: "Ok we use Yahoo as first round pick, we use Ycharts as second round pick. If neither work, and our replacement function doesnt
work for whatever reason, then we generate the report without the missing security. However, this should realistically never happen,
because we should be able to figure out a replacement." Record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_175xZ_PRICE_ORDER_YAHOO_THEN_YCHARTS_THEN_REPLACEMENT.md` @827959566f.

**C-PRICES at hop 9's cut, final:**
0. The estate's live stores (the DEMQUE price store, the Opal ETFs' Bloomberg history), where they hold the symbol. They are already
   Opal's, so they are read, not called.
1. Yahoo (yfinance), cut at T-1, with `source: yfinance`.
2. YCharts through the stored session, one symbol per call, with `source: ycharts`.
3. The replacement function (C-SWAP) substitutes a priced security. The report names the substitution.
4. If all fail, the report is generated WITHOUT the security, and the report says so in plain words (FWD-4: a failure shows). It never
   blocks.

**Bloomberg is OUT of the price chain** for this report. His chain names none, and its queue stays for the estate's own pulls.
**C-SWAP step 2 (the replacement) is unbuilt.** Today the AI path does typo checking only, and the AI web-search swap is refused by
design. Step 3 above therefore needs C-SWAP step 2 built. It joins the enrichment list right after hop 9's prices, ahead of the variants.

-- 1.0.0_SA_CTO~DELL2
