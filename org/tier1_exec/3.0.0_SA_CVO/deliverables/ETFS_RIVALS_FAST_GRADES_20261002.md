# ETFS_RIVALS FAST lease -- CVO grades of landed pins (3.0.0_SA_CVO~RV)

- Lease: FAST from 2026-10-02T05:08Z to 17:08Z, seat `2.0.0_SA_COO~RV` (`org/mcp/drive-mode.log` line 56, msg 28219).
- Grading rule (`/closer-drive` Review, `/closer` Step 4): PASS, FAIL or NOT_EVALUATED, graded on the real run's artifact,
  never on static markup. A FAIL becomes the builder's next item.
- This file is overwritten per grade:
  - grade 1 (NOT_EVALUATED) @f751aac898;
  - grade 2 (FAIL, ETFT YTD -188.51%) @9cca47a6cd;
  - grade 3 (PASS on F1-F4) @ea29c625e9;
  - grade 4 (PASS on CALL 6 c1-c2; G4-1 split guard refusing 7 real moves, ruled CALL 8) @6aaf6b43f6;
  - grade 5 (PASS, CALL 8 served) @eeb5fb2c7a;
  - grade 6 (PASS; G6-1 trend-sector guard, P2) @bcac012fe7;
  - grade 7 (PASS; G6-1 closed) @3e93998f8e;
  - grade 8 (10-02 page PASS on scope; P1 G8-1 BASG false FAILs, P1 G8-2 phantom 0->0 exits) @ab55da6a97;
  - grade 9 (PASS; G8-1 closed, CALL 11 re-grade verified) @33f6db4880;
  - grade 10 (PASS; G8-2 closed; G10-1 latent P2) @c3050c9b94;
  - grade 11 (PASS, the page for the 13:00Z read) @5488015d8f.

## Grade 12 -- r12 (addendum 11) at code pin 8075f97ffb, applied ~13:4xZ (no handoff; read by this seat 2026-10-02 ~14:10Z)

**Verdict: the deploy is PASS on the APPLIED plane. The served effect is NOT_EVALUATED:** r12 republished nothing, and the
served 2026-10-02 page is still `fast-a1-publish-1002e` (grade 11).

- **Deployed bytes equal the pin on both Lambdas that publish:**
  - `rivalfunds-publish-page-lambda`: 33 of 33 files byte-equal to 8075f97ffb;
  - `etfs-rivalfunds-daily-lambda`: 33 of 33;
  - positive control: the deployed `ai_accounts.py` differs from its f122e4476b version (the a1-chain/4 prompt is live).
- **The bronze-read grant is APPLIED.**
  - `iam simulate-principal-policy` on `rivalfunds-publish-page-role`, s3:GetObject: `issuer-site/etfs/bronze/holdings/...`
    allowed and `bloomberg/etfs/bronze/holdings/...` allowed.
  - Negative control: a foreign prefix reads implicitDeny.
  - `comp-iam service` reads only the DESIRED plane, by its own header.
- **The pair:** the CTO half 74aade65ea, the apply on Andrew's resume word (round-5 analysis s.1). Ledger r12 CLOSED 13:45:17Z.
- **Owed for the served grade:** the next marker-driven page shows its source URLs (no "bronze sidecar unreadable"), and the next
  AI run's prose names readings by label (F5).

## Grade 11 -- served page 2026-10-02, batch fast-a1-publish-1002e, code pin f122e4476b (handoff msg 28451), read 2026-10-02 ~12:28-12:35Z -- the page for Andrew's 13:00Z read

**Verdict: PASS.** G8-3 is closed in the trade log and G10-1 is closed. No P0 or P1 is open on the served page. Residual P2s
are listed below.

- **Deployed bytes equal the pin.** `etfs-rivalfunds-daily-lambda` has 33 of 33 `rivalfunds/*.py|*.json` files byte-equal
  to f122e4476b. Positive control: the deployed `publish_page.py` differs from its 2d511b9058 version.
- **The pair was complete before the apply:** COO addendum-10 half 39b59393a8 (12:17:28Z), CTO half d874fd88ad
  (12:18:59Z), apply 12:23Z. Ledger r11 CLOSED @7af008a129.
- **G10-1 closed.** `publish_page.no_shares_moved()` now also requires `_blank(est_notional) or est_notional == 0`
  (CALL 12's last clause). The served 0 -> 0 rows (2, null notional) are still noted, not shown.
- **G8-3 closed in the trade log.**
  - In the `id="trades"` section, 0 trade rows name a money-market line (MMKT / MONEY MARKET / CMQXX / DGCXX / GVMXX /
    IJGXX). On 1002d, IDVZ's "STATE STREET INST U.S. GOVERNMENT MMKT ADMN CLASS" trades showed.
  - There are 23 `data-cash-equiv` notes summing to 23 lines ("money-market line(s) traded: cash management, not a
    holding decision, so not shown as trades").
- **Nothing else moved.** The three A1 inputs in the manifest (holding_contribution, buying_trend, input_census) are the
  same objects as 1002d's. The AI accounts are unchanged (22 PASS / 2 FAIL, BASG Grounded).
- **The page:** manifest `published`, 13 of 13, readback true, 0 `<script>`.

**Residual for the 13:00Z read (P2; none blocks):**
- CGIC's 30-day AI account still narrates flows "through CMQXX_US_Equity". The AI-facts exclusion applies to future runs,
  and today's text is the stored 11:04Z run.
- F5's source identifiers in the AI prose (`fear_greed/...`).
- Bloomberg ticker forms in the prose: style, per CALL 10.

## Grade 10 -- served page 2026-10-02, batch fast-a1-publish-1002d, code pin 2d511b9058 (handoff msg 28446), read 2026-10-02 ~12:15-12:25Z

**Verdict: PASS.** G8-2 is closed on the served page. One latent P2 (G10-1): the code does not implement CALL 12's last clause.

- **Deployed bytes equal the pin.** `etfs-rivalfunds-daily-lambda` has 33 of 33 `rivalfunds/*.py|*.json` files byte-equal
  to 2d511b9058. Positive control: the deployed `publish_page.py` differs from its b973c9fdb9 version.
- **The pair was complete before the apply:** COO addendum-9 half ca27994d07 (12:02:49Z), CTO half bad3003a27
  (12:04:20Z), apply 12:08Z. Ledger r10 CLOSED @897b17b83b.
- **The change is page-only.** b973c9fdb9..2d511b9058 touches only `publish_page.py`, `render.py` and one test. G5 is
  unchanged, as CALL 12 requires.
- **Hidden rows are counted exactly.**
  - The G5 objects the served manifest names hold 249 rows. Exactly 2 of them go 0 -> 0 (INEQ JAR_LN and TXUE ATD_CN,
    both with null notional), and both are still in G5.
  - The page carries 2 `data-no-move` notes, summing to 2 ("1 line(s) carried at zero shares and then dropped (0 -> 0)
    moved no shares: not trades, not shown").
  - 0 trade rows with shares 0 -> 0 are visible. 0 `<script>`.
- **The page:** manifest `published`, 13 of 13, readback true. The AI accounts are unchanged from grade 9.

### G10-1 (P2, latent) -- the hide rule ignores notional

- CALL 12: "If a later row shows 0 -> 0 shares with a non-zero notional, that is a data fault, not this rule. It stays
  visible."
- `publish_page.no_shares_moved()` at 2d511b9058 tests only `shares_before == 0 and shares_after == 0`, so such a fault
  row would be hidden.
- Today 0 of the 2 rows carry a notional, so nothing served differs.
- Remedy class: hide only when the notional is also null or zero.

**Open:** G10-1 (P2), G8-3 (P2, money-market lines in the trade log and AI facts), F5's source identifiers in prose (P2).

## Grade 9 -- served page 2026-10-02, batch fast-a1-publish-1002c, code pin b973c9fdb9 (handoff msg 28438), read 2026-10-02 ~12:00-12:10Z

**Verdict: PASS.** G8-1 is closed. CRO~RV CALL 11's three conditions are met on the served objects. G8-2 (phantom 0->0 exits)
stays open; it is announced as addendum 9.

- **Deployed bytes equal the pin.** `etfs-rivalfunds-daily-lambda` has 33 of 33 `rivalfunds/*.py|*.json` files byte-equal
  to b973c9fdb9. Positive control: the deployed `ai_accounts.py` differs from its 7ab3b9382f version.
- **The pair was complete before the apply:** COO addendum-8 half 86192ccc07 (11:47:17Z), CTO half 49719af491
  (11:48:52Z), apply 11:52Z. Ledger r9 CLOSED @505fe1e818.
- **A re-grade, not a re-roll.** Served `research_hypotheses-20261002T110438Z-ai-rg4` against the original
  `...110438Z-ai`: text, observed and cited rows are identical on **24 of 24** accounts.
- **The whole run, both directions (condition 1).** All 24 were re-graded. Moves: FAIL->PASS 2 (both BASG), PASS->FAIL 0,
  FAIL->FAIL 2 (IDVZ "$1.6 million, $1.3 million" and CGIC "$5.7 million", the genuine ones from grade 8).
- **This seat's own check on the demo fund.** Strip ISO dates/times and ticker forms from BASG's prose: all 37 figures
  (activity_30d) and 23 figures (direction_verdict) lie within rounding of a cited value. The two PASSes are real.
- **Both grades stay readable (condition 3).**
  - The rg4 manifest carries `regrade_of` 20261002T110438Z-ai, `grader` grounding_check/4, `regraded_at` 11:54:00Z and
    `superseded` {grader, grounding, reason}.
  - The page states, on all 24 accounts, "Re-graded ... with grounding_check/4: the same text and citations, no new model
    call. Superseded grade: ...". BASG's two now read "Grounded: every figure matches a cited row."
- **CALL 10's unknown_identifier:** the handoff reports it live, with a plant reading FAIL on the real path. This seat's
  grade-8 count of 0 invented tickers on this run's text is consistent with 0 on the page. The plant itself is unread here.
- **The page:** manifest `published`, 13 of 13, readback true.

**Open:** G8-2 (P1, addendum 9), G8-3 (P2), and F5's remaining source identifiers in prose (P2).

## Grade 8 -- served page 2026-10-02, batch fast-a1-publish-1002b, code pin 7ab3b9382f, with the 10-02 AI run (handoff msg 28424), read 2026-10-02 ~11:30-11:50Z

**Verdict: PASS on the pin's scope** (grounding_check/3, TXUE's false recheck FAIL fixed, 13 of 13 current). **Two P1s for
the next items before the demo** (G8-1, G8-2). F5 is half closed.

### What PASSES (this seat's reads)

- **Deployed bytes equal the pin.** `etfs-rivalfunds-daily-lambda` has 33 of 33 `rivalfunds/*.py|*.json` files byte-equal
  to 7ab3b9382f. Positive control: the deployed `ai_accounts.py` differs from its 93227704b7 version.
- **The pair was complete before the apply:** COO addendum-7 half 4c1db289db (11:21Z), CTO half f6c76a45a1 (11:22Z),
  apply 11:27Z. Ledger r8 CLOSED 11:29:46Z.
- **The SCHEDULED chain published today's page by itself (first production evidence for the A1 tables):**
  - issuer fetch marker `096abf8e-...` at 11:00:34Z;
  - `state/build_trade_schedule/date=2026-10-02/096abf8e...` at 11:02:58Z;
  - `state/publish_page/date=2026-10-02/096abf8e...` at 11:04:10Z, status OK, writing index.html and manifest;
  - its `produce_a1()` wrote holding_contribution (11:03:25Z), buying_trend (11:04:03Z) and input_census (11:04:06Z).
  - The two later revisions (1002a with the AI run, 1002b after r8) are seat republishes. The AI run is a seat act by
    ruling (CALL 5).
- **The page:** manifest `published`, 13 of 13 updated. report_date_freshness, content_repeat and completeness are all
  PASS. Readback true.
- **CALL 10's open gap is not exploited on this page.**
  - 83 distinct ticker-form tokens across the 24 accounts' prose; 0 are absent from that fund's own G1 keys
    (`security_bloomberg`, 43 G1 objects Aug-Oct, 786 keys).
  - Positive control: "ORA FP Equity" is in TXUE's keys.
  - A first attempt against the AI table's own manifest had no G1 list, so it read 82 of 82 "absent" with a key set of 0.
    It was discarded as a zero-denominator read.
- **Grounding FAILs shown as FAIL:** 4 of 24 accounts (a1-chain/3, gpt-5.4), each rendered "Grounding FAIL" in the FAIL
  style, never as a pass. IDVZ's "$1.6 million, $1.3 million" and CGIC's "$5.7 million" are genuine: none of their 18 / 20
  cited values rounds to them.

### G8-1 (P1, demo fund) -- BASG's two AI accounts are FALSE grounding FAILs

- `grounding_reason`: "figures not in any cited row: 10, 13, 15" (activity_30d) and "13, 15" (direction_verdict).
- Every hit sits in the model's sentence "fear_greed/fear_greed_index was 28.09 as of 2026-10-01T21:13:15+00:00". The
  check reads the timestamp's month and time fields as uncited figures.
- BASG is the FWD-1 demo fund, and both of its accounts read "Grounding FAIL" today.
- **Remedy class (not drafted here):** an ISO date or time the text quotes from a cited row's as-of is not a figure; or the
  prompt writes dates in display form without a time.
- A re-run waits on CTO condition 4 (the unknown_identifier check ships first, @314d02e516), so the two can ship together.

### G8-2 (P1, visible on today's page) -- phantom "exit" rows with shares 0 -> 0

- In served G5, Sep-Oct (the newest object per date, 22 dates), **27 of 910 trade rows are `exit` with shares_before 0 and
  shares_after 0** (est_notional null): CGIC 2331 HK, INEQ SHEL LN / 1929 HK / 2282 HK / 2502 JP / 4528 JP and more.
- Today's page shows two: TXUE ATD_CN (its first trade row, as the handoff noted) and INEQ JAR_LN.
- They predate the FAST lease (trade inference). A line at 0 shares on both sides is no trade.

### G8-3 (P2) -- money-market lines remain in the trade log and the AI facts

- Grade 2's F2 took them out of the rankings and trend only.
- Today's trade table carries IJGXX (ETFT) and DGCXX (PCLG, TSEL, WCMG) "add" rows.
- CGIC's 30-day account leads with flows "through CMQXX_US_Equity", which narrates cash management as the fund's most
  unusual activity.

### F5 -- half closed

- **Closed:** the 24 accounts' prose (text, observed, inferred) carries **0** float artifacts (6+ decimals) and **0** raw
  CUSIPs.
- **Open:**
  - 106 source identifiers in prose (`fear_greed/fear_greed_index`, `fear_greed/market_volatility_vix`, and more), so
    "names over identifiers" is not met for the market readings;
  - 268 Bloomberg ticker forms ("ORA FP Equity"), which CRO~RV CALL 10 ruled are style for the next prompt version, not a
    FAIL.

## Grade 7 -- served page 2026-10-01, batch fast-a1-publish-1001g, code pin 93227704b7 (handoff msg 28393), read 2026-10-02 ~10:25-10:40Z

**Verdict: PASS.** G6-1 is closed. CALL 9's condition is served, with one enum observation for CRO~RV.

- **Deployed bytes equal the pin.** `etfs-rivalfunds-daily-lambda` has 33 of 33 `rivalfunds/*.py|*.json` files byte-equal
  to 93227704b7. Positive control: the deployed `gold_buying_trend.py` differs from its c2b9023fc6 version.
- **The pair was complete before the apply:** COO addendum-6 half 73744489e8 (09:59:43Z), CTO half 4c73b21376
  (10:01:16Z), apply 10:06Z (handoff; ledger r7 "Apply complete 0 added 5 changed 0 destroyed", CLOSED 10:20:46Z
  @04fb5c283c).
- **Values unchanged.** The served `buying_trend-20261002T100953Z-e2dcf88d2802` joins grade 6's table 319 of 319 rows,
  with **0 value cells changed** (net, gross, windows, reading, rank, trend mark). The contribution table is the same object
  as grade 6's (092848Z).
- **The page changed exactly where claimed.** Split into 78 fund segments, 74 are byte-identical to 1001f. The 4 that differ
  are the trend cards of IDVZ, GQGU, ETFT and PCLG, each now "Sectors not shown. Most of what this fund traded this year
  sits in holdings with no GICS sector in the source file". These are exactly the four funds above 50% in grade 6's G6-1
  table (100 / 65 / 70 / 62%). WCMG (49%) and TSEL (48%) keep their sector tables under the same rule.
- **`sector_source` is served:**

  | axis | own | other_fund | mixed | null |
  |---|---|---|---|---|
  | security | 117 | 17 | 0 | 107 |
  | sector | 37 | 10 | 19 | 12 |

  - Null falls exactly on the rows with no sector from any source: the 12 Unclassified sector rows and 107 securities. It
    reads as "no sector", not as an unknown source.
  - **Observation for CRO~RV (P2, no action on the page):** CALL 9's condition names {own, other_fund}. `mixed` appears
    only on sector-axis rows that aggregate both. That is a grain-correct third value, but outside the ruled enum. It
    wants one line of ratification, together with null = no sector.

**Still open:** F5 at the 2026-10-02 AI run (handoff 28393).

## Grade 6 -- served page 2026-10-01, batch fast-a1-publish-1001f, code pin c2b9023fc6 (handoff msg 28375), read 2026-10-02 ~09:50-10:05Z

**Verdict: PASS on what was built** (trend derivatives out, CALL 7 missing_reason, cross-fund GICS fallback, contribution
values unchanged). One P2 residual is restated with numbers (G6-1).

- **Deployed bytes equal the pin.** `etfs-rivalfunds-daily-lambda` has 33 of 33 `rivalfunds/*.py|*.json` files byte-equal
  to c2b9023fc6. Positive control: the deployed `gold_buying_trend.py` differs from its 2a9a11a025 version.
- **Two applies, each after its pair:**
  - addendum 4: COO cd8e96ee5a 09:22:00Z, CTO 506d577b04 09:23:41Z, apply at 3107eae49f 09:27:23Z;
  - addendum 5 (the tb-1 handler column fix): COO 8fe72138a3 09:36:21Z, CTO a278d2187f 09:39:03Z, apply at c2b9023fc6
    09:43:02Z.
  - Ledgers r5 and r6 CLOSED @0905b21b49.
  - The r5 apply served the trend without its type columns for about 16 minutes. That is disclosed in the handoff and
    repaired by r6.
- **The served trend** (`buying_trend-20261002T094504Z-9648a7ce233b`): 319 rows, and 0 lines named `* Index|Comdty|Curncy`.
  SCHY's first sector lean-away is Energy -$27.2M (bet, 17 windows), where it was a -$1.05B futures "Unclassified" line,
  which no earlier grade caught.
- **The served contribution** (`holding_contribution-20261002T092848Z-0c1d3c4aa2eb`): 3,906 rows that join 3,906 of grade
  5's table one to one. **0 contribution values changed** (this seat's join), which is the CTO half's claim, verified.
  `missing_reason`: 70 no_price, 13 derivative_not_priced.
- **The page:** 0 `<script>`. Manifest `published`, 12 of 13, readback true. 12 "No GICS sector in the source" labels.

### G6-1 (P2) -- the trend's sector panels have no guard for an unknown-sector majority; the contribution panels do

The "No GICS sector in the source" share of each fund's gross sector notional in the served trend:

| fund | share |
|---|---|
| IDVZ | 100% |
| ETFT | 70% |
| GQGU | 65% |
| PCLG | 62% |
| WCMG | 49% |
| TSEL | 48% |
| PFOE | 32% |
| BASG | 25% |

- The label is now honest.
- The contribution panels apply "Sectors not shown" when the unknown bucket dominates (grade 3, F4). The trend panels
  apply no such rule, so IDVZ's only sector line, and GQGU's first lean-away line (-$176M), is "No GICS sector in the
  source".
- The cross-fund fallback leaves GQGU at 65% though its holdings are US large caps other funds hold. Whether its key
  misses (issuer rows versus Bloomberg rows) is unread here.
- **Recommendation:** one rule for both components.

**Still open:** F5 at the next AI run.

## Grade 5 -- served page 2026-10-01, batch fast-a1-publish-1001d, code pin 2a9a11a025 (handoff msgs 28354/28355), read 2026-10-02 ~09:12-09:20Z

**Verdict: PASS.** CRO~RV CALL 8 (@4c4fe9daf7) is served as ruled. Grade 4's G4-1 is closed.

- **Deployed bytes equal the pin.** `etfs-rivalfunds-daily-lambda` has 33 of 33 `rivalfunds/*.py|*.json` files byte-equal
  to 2a9a11a025. Positive control: the deployed `gold_holding_contribution.py` differs from its 0d4b3f6e4d version.
- **The never-widen pair was complete before the apply:** COO addendum-3 half 3a1a5ebd05 (09:00:05Z), CTO half 372c538349
  (09:03:03Z), apply 09:06:22Z. Ledger `20261002T0905Z_etfs-rivalfunds-fast-a1-r4` was committed before the apply and
  closed at 09:09:43Z.
- **The rule at the pin** (`gold_holding_contribution.py` `_implied`): a split is refused iff `out(r) AND out(k) AND NOT
  out(v)`; else an implausible move is refused iff `out(r, 0.5)`; else the day is priced. This is CALL 8 verbatim. On
  grade 4's 12-row table this seat's own replay classifies all 12 correctly. This seat's earlier value-continuity-only
  recommendation got 3 wrong (Intuit, VAL SJ, IMP SJ), and CALL 8 corrected it.
- **The served table** (`holding_contribution-20261002T090746Z-371779fe0d1c`):
  - exactly 5 YTD refused rows, each a split or a fault: KMB IN 01-13 / 01-14, Amphenol 09-02, AZN LN 02-02 and IBE/D
    07-07 implausible;
  - the 7 real moves are priced: BASG Datadog +2.09% is BASG YTD #2 behind Marvell +3.17%, BASG Intuit -1.95%, and
    Snowflake and Atlassian have 0 refused days;
  - max |holding contribution| is 3.62%, and fund YTD totals sit in -4.92..+12.51.
- **The page:** the `id="refused-days"` table lists the same 5 rows. 0 `<script>`. Manifest `published`, 12 of 13,
  readback true.

**Still open:** F5 at the next AI run; the trend-sector Unclassified residual (P2).

## Grade 4 -- served page 2026-10-01, batch fast-a1-publish-1001c, code pin 0d4b3f6e4d (handoff msg 28333), read 2026-10-02 ~08:50-09:05Z

**Verdict: PASS on what was built (CALL 6 conditions 1-2, futures unpriced).** One P1 finding (G4-1): the split guard,
which is CALL 1 condition 3 and not this pin's change, refuses 7 real price moves. The figures are disclosed and not
impossible, so this is not a FAIL. It is a call for 4.0.0_SA_CRO~RV.

### This seat's reads

- **Deployed bytes equal the pin.**
  - `etfs-rivalfunds-daily-lambda` has 33 of 33 `rivalfunds/*.py|*.json` files byte-equal to 0d4b3f6e4d.
  - Positive control: the deployed `gold_holding_contribution.py` differs from its fc80f776e4 version.
- **The never-widen pair was complete before the apply:** COO addendum-2 half c5a4b569a7 (08:35:51Z), CTO half
  1c0206039d (08:37:36Z), apply 08:41:27Z. Ledger `20261002T0840Z_etfs-rivalfunds-fast-a1-r3` was committed before the
  apply this time and is CLOSED @a92dff4229.
- **Condition 1 PASS.** `gold_holding_contribution.py:224` at 0d4b3f6e4d reads `moved = max(ratio, 1.0 / ratio) - 1.0`,
  tested against the split band (quantity changed) or the implausible band (quantity unchanged). `:220`: a zero or absent
  valuation is no price.
- **Condition 2 PASS.**
  - Served `holding_contribution-20261002T084252Z-4188ce5b7e3a` carries `n_days_refused`, `refused_reasons` and
    `refused_days`.
  - YTD: 12 refused holding-days (11 corporate_action_suspected, 1 implausible_valuation).
  - The page's `id="refused-days"` audit table lists the 12 with ratio and reason. Captions mention refusals 8 times.
  - 0 `<script>`.
- **Futures PASS.** 0 rows named `* Index` in the contribution table.
- **Grade 3's unverified attribution is now verified:** SCHY and BIDD carry 0 `implausible_valuation` refusals.
- **Fund YTD totals:** every fund sits in -4.92..+12.51 (BASG 9.77, CGIC 5.99, SCHY 5.79).

### G4-1 (P1; a call for CRO~RV) -- the split guard refuses real moves whenever the fund traded that day

**The test.** For each of the 12 refused rows, read the two G1 reports from served `gold/canonical_shape`. Value continuity
is `q1/q0 x ratio`:
- a split or consolidation moves the share count inversely to the price, so value continuity is about 1;
- a trade on a real move does not.

| fund | holding | day | price ratio | q1/q0 | value continuity | reading |
|---|---|---|---|---|---|---|
| BIDD | KMB IN | 01-13 | 0.1995 | 5.0000 | 0.997 | split, refused correctly |
| BIDD | KMB IN | 01-14 | 4.9466 | 0.2000 | 0.989 | split (reverse leg), refused correctly |
| GQGU | Amphenol | 09-02 | 0.4905 | 2.0080 | 0.985 | 2:1 split, refused correctly |
| TXUE | AZN LN | 02-02 | 2.0207 | 0.5000 | 1.010 | consolidation, refused correctly |
| CGIC | IBE/D SM | 07-07 | 43561 | 1.0000 | 43561 | rights-line valuation fault (implausible), refused correctly |
| BASG | Datadog | 05-07 | 1.3133 | 1.0027 | 1.317 | **real +31% move**, wrongly refused |
| BASG | Intuit | 05-21 | 0.7998 | 0.9984 | 0.799 | **real -20% move**, wrongly refused |
| GQGU | Snowflake | 05-28 | 1.3648 | 1.0018 | 1.367 | **real +36% move**, wrongly refused |
| GQGU | Atlassian | 05-01 | 1.2958 | 1.4886 | 1.929 | **real +30% move on a buy**, wrongly refused |
| CGIC | 8283 JP | 05-12 | 1.3568 | 1.0098 | 1.370 | **real +36% move**, wrongly refused |
| CGIC | VAL SJ | 01-30 | 0.7811 | 1.0069 | 0.786 | **real -22% move**, wrongly refused |
| CGIC | IMP SJ | 01-30 | 0.7908 | 1.0069 | 0.796 | **real -21% move**, wrongly refused |

**7 of the 11 corporate_action_suspected refusals are real moves.** The guard reads ANY quantity change as a possible
split, so a 0.2% trade on an earnings day removes the day. Two of the seven are in BASG, the FWD-1 demo fund.
- Datadog's +31% day contributes nothing to BASG's YTD ranking. Its other days still count.
- The page labels both days "corporate_action_suspected", a reading a viewer can see is wrong.

**Recommendation (for CRO~RV, amending CALL 1 condition 3):** refuse as corporate_action_suspected only when value
continuity holds, i.e. `|q1/q0 x ratio - 1|` within the split band. Otherwise price the day as a real move: the quantity
change is a trade.
- On these 12 rows this keeps 4 refusals plus IBE/D, and prices 7.
- Whether a true split day is priced on its value-continuous return or refused is the CRO's choice.
- Not drafted here.

### Still open (from grade 3)

- F5 at the next AI run.
- The trend-sector Unclassified residual (P2).

-- 3.0.0_SA_CVO~RV
