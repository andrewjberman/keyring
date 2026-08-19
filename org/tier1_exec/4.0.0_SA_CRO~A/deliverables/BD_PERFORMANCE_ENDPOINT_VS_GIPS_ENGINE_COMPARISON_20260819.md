# BD PERFORMANCE ENDPOINTS vs OUR GIPS ENGINE -- first comparison + a SYSTEMIC flow-valuation defect found (4.0.0_SA_CRO~A, 2026-08-19)

**Commissioned:** Andrew-direct at this terminal (~1945Z): find the performance-attribution
endpoints on Black Diamond and compare account performance vs our GIPS scripting approach.
**Under:** the standing BD scanning egress (~1830Z, recorded). All reads estate-side except the
already-landed BD sample; no new vendor calls were needed for this pass.

## 1. THE BD PERFORMANCE SURFACE (located + documented)

**Endpoint:** `POST /portfolioreporting/api/performance/performancePeriod` (the ClientView /
portfolioreporting domain; bearer minted via `GET /session/token` from the same `.bd.identity`
cookie -- distinct from the datamining token). Proven request body lives in the deployed
`opal-assets-bd49f-reporting-pull` Lambda (`body_performance_period`: accountFilters, groupings
[Account, Asset], dateRanges [Custom + calendar years + SinceInception], benchmark ids
94554/90832/90833/90834). Datamining (qt1-7) carries NO return measures -- performance is
exclusively this domain (+ the BI dashboard app, still unmapped).

**Response shape (from the landed 5.28MB sample, account BD-id 22596361 = Schwab 0027265115 via
dim_account_xref):** per date-range: BMV/EMV with **accrual split out separately** (unlike qt6's
accrual-inclusive EMV), positionOnly + performing BMV/EMV variants, netAdditions, netGains, fees,
income, daysHeld, **timeWeightedReturns.return** + **moneyWeightedReturns.return**, per-benchmark
returns. Vendor caveat already recorded in the puller: BD REVISES closed-period figures (~0.03%
drift measured between pulls).

## 2. THE COMPARISON (one account, matched windows -- our twr_daily linked vs BD's endpoint)

Account 0027265115 (TAXSMA, in-kind funded 2026-03 -- deliberately the hard case):

| window | BD TWR | our engine (linked r_net) | verdict |
|---|---|---|---|
| 04-08 -> 06-30 (quiet) | **-8.1799%** (MWR -8.1761%) | -9.1438% excl. 04-08 / -7.6085% incl. | ~96bp off EITHER boundary; see defect |
| since inception 03-16 -> 06-30 | **-8.1346%** | **+627.01%** | our chain GARBAGE on funding windows |
| EMV at 06-30 | 978,845.45 + 489.26 accrual | 980,490.99 (nmpc basis) | ~0.12% -- values fine |

## 3. THE ROOT CAUSE -- measured to the ledger row, then censused: IN-KIND FLOWS ARE VALUED AT ZERO, UNFLAGGED, SYSTEMICALLY

Chain, every link read directly:
1. twr_daily 2026-03-25: **r_net = +341.36%** on BMV 131,317 -> EMV 579,579 with **cf_net = $3.70**;
   03-27: +78.16% with cf_net = 0. The engine read ~$900K of asset arrivals as PERFORMANCE.
2. The flow_ledger rows for those days: the IC (in-kind) legs ARE present and classed EXTERNAL --
   but **every one carries `in_kind_value = 0.0` with `in_kind_unvalued = False`**. The docstring's
   promise ("zero-price rows carry qty-only + in_kind_unvalued flag -- never zero-buried") is
   violated by its own output: zero-buried WITH the flag reading False. No quantity column survives
   into the emitted rows at all.
3. **Census, 4 partitions (03-24..03-27), ALL accounts: 202 of 202 IC legs zero-valued AND
   unflagged, 42 accounts affected.** 100% failure = the valuation step is a de-facto no-op in the
   landed output -- the could-not-have-said-otherwise class: nothing downstream could catch it
   because AUA never depends on flows, the honesty flag never fires, and TWR corruption surfaces
   only on in-kind-funded accounts, which nobody had compared against an external oracle until now.
4. BD's same-window flows: netAdditions **$1,047,024.72** (it values the transfers); ours: $3.70.
   Even the quiet Q-window carries a missed $4,401.52 (BD) vs $0.00 (ours) -- the residual 96bp gap
   is flow-omission plus boundary convention (BD's daysHeld=58 implies its window includes the
   start date's return; UNDETERMINED which convention is GIPS-preferred here until the flows are
   fixed and the comparison re-run clean).

**What this does NOT impeach:** valuations (the 309/312 @0.1% tie stands -- values come from
dim_balance, not flows); the engine's own status honesty on missing-BMV days (it refused 2 days
correctly); non-in-kind accounts' TWR (cash flows ARE valued -- the defect is the IC path).

## 4. DISPOSITION (recon -> findings; fixes are not mine)

- **DEFECT, DS-lane (c00_flow_ledger in-kind valuation + the unfired flag), CTO to route:** until
  fixed, per-account TWR is UNRELIABLE for any in-kind-funded account (TAXSMA class especially);
  window returns spanning funding days are meaningless. The fix target is the valuation join
  (qty x same-date close) whose output never lands, and the flag logic that reads False on zero.
- **The comparison harness now exists:** BD performancePeriod as the external oracle, matched-window
  linking against twr_daily -- re-runnable per account in minutes; the right acceptance for the fix
  (post-fix: SI window ties BD within the pre-registered band; the +341% day re-reads as ~0%).
- **Broader comparison (normal cash-funded accounts) is the natural next pass** under the standing
  egress: fresh performancePeriod pulls for a stratified sample (equity-only, bond-carrying,
  flow-heavy) -- deliberately NOT run tonight so the defect finding routes first (a wider sample
  against a known-broken flow chain measures the defect, not the parity).
- GIPS note (field-contract owner): BD's TWR/MWR split and accrual-separated EMV align with
  GIPS-grade mechanics; our engine's daily-linking design is sound -- the defect is an INPUT
  (flow valuation), not the method.

PII: account-level work in scratch (deleted after); the account is identified by masked custodial
tail + BD internal id only. Probe count this pass: zero new vendor calls.
