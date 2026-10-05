# L4-R ratified-text half -- ETFS_RIVALS v0.16 -- SIGN

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-05 ~03:2xZ
**Delivery:** `1.0.0_SA_CTO~Z` msgs 29440 and 29441 at `646ce7f4b8`. The half hash, recomputed by this seat, is `63679063dbbb` and
equals the delivery.
**Method:** ENDPOINT and CONTRACTS at `e99a733d4c` (v0.15, signed @`142c94e01a`) diffed against `646ce7f4b8`. ENDPOINT gains FWD-21
(+15 lines). CONTRACTS: 0 lines. The pin is Andrew's verbatim in
`org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261005_03xxZ_RIVALFUNDS_BENCHMARKS_CLICKABLE_TICKERS_ETFCLASSIFIER_BACKFILL.md`
(@`41158af7f9`).

## Against the verbatim

Andrew: *"anytime a stock/ticker is mentioned, it should be clickable to the modal, and we should be able to see backfill on it."*

- **FWD-21:**
  - DONE WHEN: every security named in the rankings, the buying trend, the AI accounts and the detail lists opens its holding modal,
    and the modal shows its history (price and the fund's holding over time) as far back as the store holds it.
  - ACCEPT: no ticker is dead text; a security not yet backfilled says so in its modal, never an empty chart.
  - **This carries both clauses** ("clickable to the modal", "see backfill on it") and invents nothing.

## Review

- **The rest of the same transcript is placed correctly outside the ratified text:**
  - The benchmarks (ACWI for IDVZ, IWM for PFOE) were already ratified at v0.8. ENDPOINT FWD-6/7 and CONTRACTS "Index controls" read
    ACWI and IWM, with SCHY kept as an IDVZ group member, not its benchmark.
  - The ETFClassifier full-backfill routine is routed to MDPF_SECCLASS (laptop), per the CTO's note. It is not an outcome of this
    PRD.
- **Andrew's later word** (~04:0xZ, "a cap on all lookback of 3 years for rivalfunds inclusions") does not conflict. FWD-21's "as far
  back as the store holds it" sits inside a 3-year ceiling.
- **No-script rule:** stated as standing.

**Verdict: SIGN.**

-- 3.0.0_SA_CVO~Z
