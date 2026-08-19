# DASHBOARD UPDATE + TAX SMA REPORTING (internal call 2026-07-16, 36m51s) -- INGESTED 2026-08-19
# per Andrew's open-calls ruling 8 ("All approved"; record ANDREW_RULED_20260819_OPEN_CALLS_ALL_TEN_APPROVED.md)

**Participants:** Yang Liu (lead), Alyssa (the "Opal Bloomberg" seat operator), Manav Shah (49F),
Andrew. **Raw:** `20260716_dashboard_update_and_tax_sma_reporting.{docx,vtt}` beside this file
(byte-faithful copies; docx = Teams transcript, extracted 33,730 chars). **Companion working
files:** `taxsma_smartx_ledgers/` -- the Chan/Johnson-Chan TEN-COM SMARTX_ADVISORY account:
activity ledgers base(572 rows, 07-13) / v3(574 rows, 07-14, superset+1day) / v2(19 rows, a
May-2026 accrual slice) + holdings (13 positions: BIV/CLIP/SPHY bond-ETF book, ~$830K visible
rows). Downloads also held a ZERO-BYTE "(1)" ledger variant -- noted, not copied (empty).
**Primary consumer: the D9 (Tax SMA) STATE ASSESSMENT running at sitez** -- this is its
workflow-as-designed ops detail, ingested so the assessment reads it in one pass.

## 1. TAX SMA QUARTERLY REPORTING -- the workflow as DESIGNED on the call (D9's core input)

- **Population then:** 5 accounts on Yang's tax-SMA list; **3 LIVE (traded)**, identified by
  inception-date presence (accounts 1/3/5 on the sheet; column K = the live indicator);
  ~$140M pipeline context mentioned. First two live accounts report SINCE APR 8; third <1 month.
- **Cadence:** QUARTERLY, one file per client (template -> per-client Excel, saved to the same
  SharePoint folder `.../OCIO models/Dashboard/<...>/2026 Q2/`). Yang: "only once a quarter."
- **Template (Yang-authored, 2 pages):** p1 = client name / account # / strategy / reporting
  quarter / inception date / benchmark + BMV / contributions-withdrawals / gains-losses / EMV +
  returns (QTD/YTD/1Y/3Y/SI). p2 = the "wish list": tax detail (realized/unrealized x
  short/long-term FOR THE PERIOD -- Yang confirmed the BD report's date-ranged form is "what we
  need"), positioning + sectors.
- **SOURCE MAP, with the load-bearing rationale:**
  - **Returns NET-OF-FEES <- BLACK DIAMOND** -- because 49F TURNED OFF Schwab's client
    performance function, so neither client nor Opal can pull performance from Schwab; BD is
    also the billing tool (fees incl. margin + advisor fees). Andrew's on-call counter,
    unresolved then: "I suspect we can get it... it's all there in a fact table and we can just
    make it" -- i.e. compute from our own Schwab-derived data. [D9/D2 NOTE: that is exactly what
    the 49F canonical TWR chain now does -- the call PREDATES it; the assessment should mark
    this source-map cell as potentially SUPERSEDED-BY-ESTATE.]
  - **Cost basis + realized/unrealized gain-loss <- SCHWAB** (Yang: the original data are
    Schwab's; BD's role is the fee-inclusive return).
  - **Sectors + holdings <- FACTSET** (Yang pre-pulled `sector allocation` + `holdings` files
    per account; top-10 holdings copied into the template -- "throw those files to Claude").
  - **Benchmark returns <- BLOOMBERG**; benchmarks are the 49F CUSTOM long-term benchmarks
    (49F declined S&P/AGG on the report).
  - **BMV:** not directly available -- BACKED INTO from performance + EMV (Excel formula
    agreed on-call). Cost basis explicitly != starting value (Yang caught that confusion).
- **Rulings on the call:** ENTIRE-ACCOUNT reporting, NO sleeve separation (Yang: competitors
  don't, and it's a rabbit hole). Report period = Apr 8 -> Jun 30 for Q2.
- **Access gaps then:** Alyssa had NO BD access (to request via Manav, for 49F AND Cottonwood);
  Andrew's BD login = "Andrew Berman 49" + a Cottonwood one. BD concerns Andrew voiced: lag +
  revision behavior unknown [D2 parity note: BD revises closed periods ~0.03% per CRO~A's
  same-day endpoint doc -- the concern is now measured].
- **Prior art confirmed live on the call:** Andrew's tax-pt1/2/3 skills (short-sale-avail
  intake w/ corruption check + SharePoint record -> API pull -> FactSet-format conversion),
  installable on the terminal device; Andrew planned to work them ON the terminal. [Matches
  D9's run C1 census; the assessment verifies their current state.]

## 2. THE DAILY DASHBOARD REFRESH (first half of the call -- Item-0/ops context, not D9)

Procedure Alyssa was trained on: Bloomberg terminal login (NO MFA -- username/password only)
-> VS Code -> run-all on two notebooks (market data pull) -> two pickles (`model_2026_MMDD.pk`,
`data_2026_MMDD.pk`) under the OCIO-models SharePoint output folder -> opalinvest.dev ->
Data Refresh -> drag-drop both -> ~5min pipeline -> market-overview tables stamp yesterday's
close. Andrew had already built a ONE-CLICK batch (download + upload through the same refresh
endpoint). Yang's automation ask ON THE CALL: a scheduled job on that laptop under Alyssa's
login, ~08:00 ET +/- random 5min jitter (once daily, never every-5-min), Andrew to test
whether Bloomberg tolerates scripted re-login. [ESTATE NOTE: this is the tplus1/BBG pull
lineage now WDAC-hardened at sitez -- the call is its design moment; the no-MFA fact is
load-bearing for the box's unattended-reboot acceptance already landed.]

## 3. WHAT THIS CHANGES FOR THE D9 ASSESSMENT (pointers, not conclusions -- assess-first stands)

(a) The workflow-as-designed map (assessment part 2) now has its primary source: section 1
above IS the designed Q2 flow, with named owners (Alyssa fill / Manav data-access / Andrew
automate). (b) The SharePoint doc-sync review (part 4) has named artifacts to locate: the
tax-SMA account list w/ inception+trade labels, the Q2 template, the FactSet sector/holdings
pulls, the per-client report files Alyssa built. (c) The source-map cell "returns <- BD
because Schwab performance is off" should be tested against the estate's own TWR chain
(potentially superseded; Andrew's own on-call instinct). (d) The SMARTX ledgers here are
specimen WORKING DATA for the daily-tracking design (accrual events + holdings grain visible).
(e) Population/scale facts (3-of-5 live, growth expectation, once-a-quarter cadence) size the
(c1) daily-tracking and roll-in legs.
