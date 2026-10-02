# ETFS_RIVALS FAST lease -- CVO grades of landed pins (3.0.0_SA_CVO~RV)

- Lease: FAST from 2026-10-02T05:08Z to 17:08Z, seat `2.0.0_SA_COO~RV` (`org/mcp/drive-mode.log` line 56, msg 28219).
- Grading rule (`/closer-drive` Review, `/closer` Step 4): PASS, FAIL or NOT_EVALUATED, graded on the real run's artifact,
  never on static markup. A FAIL becomes the builder's next item.
- This file is overwritten per grade. Grade 1 (NOT_EVALUATED, no real run yet) is at f751aac898.

## Grade 2 -- served page 2026-10-01, batch fast-a1-publish-1001, code pin 7aa0186d45 (handoff msg 28289), read 2026-10-02 ~07:50-08:20Z

**Verdict: FAIL.** One finding (F1) puts a figure on the served demo page that cannot be true. F2-F5 are demo-visible
defects that do not block on their own.

### What PASSES (this seat's own reads)

- **Deployed bytes equal the pin.**
  - `etfs-rivalfunds-daily-lambda` (the runtime the manifest names; CodeSha256 PJr6l0z..., LastModified 07:36:33Z).
  - All 33 of its `rivalfunds/*.py|*.json` files are byte-equal to `git show 7aa0186d45:data/etfs/scripts/...`.
  - Positive control: the deployed `ai_accounts.py` differs from the 38ec58bc5a revision, so the comparator can see a
    difference.
- **The never-widen pair exists, both halves before the deploy:** COO half 4df699fa92 (07:29Z), CTO half dd7d03eaed
  (07:31Z). Ledger `20261002T0734Z_etfs-rivalfunds-fast-a1_deploy_completion.md` was opened 07:34Z and closed 07:42Z.
- **The served manifest** (`platinum/page/date=2026-10-01/manifest.json`):
  - status `published` (ruling 7), 12 of 13 updated, page_version publish_page/3, readback true;
  - `a1_produced`: holding_contribution OK 3939 rows, buying_trend OK 311, input_census OK 1568.
- **The served HTML** (1,603,171 bytes, 0 `<script>`), rendered headless and looked at:
  - it leads with the components;
  - the headline reads "12 of 13 funds current", naming GQGU's freshness lag;
  - fund and period switches render;
  - AI accounts carry Observed / Inferred / "What would prove this wrong" / Cited rows / Grounded.
- **Fund-level YTD totals are plausible for 12 of 13 funds:** -5.0% to +11.5% (sum of holding contributions, served
  gold).

### F1 (FAIL; P0 before the demo) -- ETFT's YTD contributions are wrong by about -190 points

- **What serves:**
  - the ETFT YTD sector panel reads `Unclassified -102.57%`;
  - in the served gold, ETFT YTD holding contributions sum to **-188.51%**;
  - 25 ETFT YTD holdings are each at or below -5%: AAPL -6.7%, GOOGL -6.7%, META -6.7%, AMZN -6.1%, V -5.6%, and more.
  - A long-only fund cannot lose 188% of its value.
- **Mechanism (measured in served G1, `gold/canonical_shape`, ETFT rows, Jan-Sep 2026, 186 dates):**
  - ETFT's non-cash market_value collapses on two dates while quantities hold:
    - 2026-02-04: 989,585, against 15.1M the next day;
    - 2026-04-10: 660,844, against 14.3M the next day.
  - AAPL on both dates: quantity 1683 / 2183, market_value **0.00**, so its holding-implied price is 0.
  - The rk-1 producer reads each such day as a -100% return. Each holding then loses about twice its weight, and the
    sum lands near -190%.
  - The rebound day (price 0 -> real, an infinite return) does not offset it. Read from the totals, not from the code.
- **Scope:** the YTD period of ETFT only. ETFT's QTD (+2.04%), MTD and R30 are unaffected, because both dates fall before
  July. The other 12 funds' YTD totals are plausible. The ETFT AI account cites R30 rows, not YTD.
- **Remedy class (not drafted here):**
  - the contribution producer treats a zero or absent implied price as NO PRICE (missing), never as a -100% return;
  - whether G1 should carry a Bloomberg market_value of 0 on a held line as null is the upstream half.
  - The proof is ETFT YTD in a plausible range, plus a planted zero-value day in a test.

### F2 (P1) -- a money-market fund ranks as a holding and as a BET

- IDVZ MTD "Top contributors" #10 and YTD "Leaned into" #5 (17 windows, BET) is "STATE STREET INST U.S. GOVERNMENT MMKT
  ADMN CLASS".
- ETFT's YTD top list and AI account carry IJGXX (a money-market fund).
- A cash vehicle read as a manager's bet is a wrong reading on the face. A cash line belongs out of the rankings and
  trend, or marked as cash.

### F3 (P1) -- missing data is shown as "no trade"

- In the YTD buying trend, the header says "2026-01-01 to 2026-10-01" and the legend says "0 no trade".
- IDVZ's holdings history starts 2026-08-21, PFOE's 2026-08-24 and WCMG's 2026-04-23 (served gold `period_start`).
- So their pre-history months print `0` = "no trade" where the truth is "no data".
- The contribution panel states its own window; the trend panel does not.

### F4 (P2) -- sector panels on the home funds

- IDVZ's (and PFOE's) sector panel is two rows, one of them "Unclassified" carrying -3.13% of a -3.05% month.
- With two sectors, "Strongest" lists a negative sector and "Weakest" a positive one.
- IDVZ is the first fund section Andrew sees.

### F5 (P2) -- AI prose shows raw identifiers and float artifacts

- "857492656 at 2.1 million" (IDVZ); "211861.2200000001" and "-46818.259999999995" (ETFT).
- "fear_greed/market_volatility_vix at 50": a 0-100 sub-score named like a VIX level.
- The prompt revision a1-chain/2 (38ec58bc5a, "names over identifiers, display-form figures") is on `rv-fast` and not
  drained. The AI rows came from a seat's ad-hoc run (CALL 5), so the served text changes only when that run is repeated
  at the new prompt.
- Display-naming a 0-100 score as "VIX" would be a new error. Name it as a score.

### Limits of this grade

- Graded on the served S3 bytes. The gateway route `/rivalfunds` is SSO-gated, and its signed-in read is FWD-1, Andrew's.
- The ranking method (holding-implied, price-only) was checked for plausibility at fund level only, not holding by holding
  against an independent price.
- Only the 2026-10-01 page is graded. Tomorrow's scheduled page (the publish producers on their own clock) is a separate
  read.

-- 3.0.0_SA_CVO~RV
