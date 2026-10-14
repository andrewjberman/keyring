# ADVI_BDPRCE -- round 1 remediations (dell1)

<sweep_watermark>2026-10-13T15:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T15:55:00Z. Graduated at ADJUDICATION_v1: 15 rows (7 ARMED, disarm owner 2.0.0_SA_COO~K1; 8 INERT).

```json
[
  {
    "id": "ADVI_BDPRCE-D1-W2-S2",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Repeats are the norm in this partition, not an edge case: 6210 of 6278 rows share a transaction_id with another row. The sample's four rows are identical, so the median equals the one value and match is true. Where repeats carry different prices the median is weighted by repetition. Left alone, every transaction_observed price written from the daily path is computed this way. The instrument reproduces that faithfully and reports distinct_trade_ids beside rows_used so the divergence is visible.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W2-S2",
      "carried to C6 (FWD-4) (packet section 4)",
      "this seat's read of silver/transactions/2026-10-09.parquet for the thread asset: 4 rows, 1 distinct transaction_id (745369343)"
    ],
    "remedy": "De-duplicate on transaction_id before the T-1 median (FWD-4). Close when: the daily path's median counts each transaction once, beside a control asset whose single trade still prices equal.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W2-S4",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The same transaction_observed rule has two readers. Backfilled history (new assets) is computed over de-duplicated trades; the daily path is not. A backfill-written row can therefore disagree with this instrument's recompute and show match false while being correct for its writer. The canonical object does not record which path wrote a row, so the instrument cannot tell the two apart and says so in the rule text. The reproduction is exact for the daily path only.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W2-S4",
      "carried to C5 build half (FWD-2) (packet section 4)"
    ],
    "remedy": "One rule, imported by every writer (FWD-2). Close when: backfill and the daily path compute the same median from the same partition.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W1-S3",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two literal rank copies differ in their keys and order. The live Lambda copy lacks the scoped_override key that the silver copy ranks first. Standing effect, from the code: each daily Lambda write can replace a scoped override row for the target date until S_00 rebuilds the table about four hours later. Not executed in this read.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W1-S3",
      "carried to C5 build half (FWD-2) (packet section 4)"
    ],
    "remedy": "The deployed bd-price-update Lambda imports the one rule (or is retired). Close when: its rank table carries scoped_override, or the Lambda no longer writes canonical.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W3-S3",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The served values follow a de-duplicated median or the price-first observed rule far more often than the rule as written. Which writer produced each served row is not established by this read (lambda_function.py:441 and build_canonical_prices_v2.py:660 are named writers; their T1 rule was read only for lambda_function.py, which matches the file as written). The gap is the writer's rule, not a day's data.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W3-S3",
      "carried to C5 build half, C6 (packet section 4)"
    ],
    "remedy": "A ruling on which of the three live rules is THE rule (T1 as written, JOB 2 price-first, the dividend-excluding price-column median), then one home. Close when: the served transaction_observed rows equal the one rule on the census.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W3-S4",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The rule keeps cash-dividend rows, whose ratio is the dividend amount per cash unit (1.0 in these rows), so the median is 1.0 for assets whose cash rows outnumber trade rows on that day. The rule as written therefore yields a price that is not a price for these rows. The residue of 64 UNEXPLAINED rows includes these; no version reproduces them.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W3-S4",
      "carried to C6 (new item) (packet section 4)"
    ],
    "remedy": "Exclude non-trade rows (cash dividends: price 1.0, units = cash amount) from the median; a served rule change under FWD-7. Close when: BLACKROCK INC COM 2026-09-22 and the other 18 such rows recompute to a trade price.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W4-S2",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "61 of 586 sampled untickered lots carry a price that no canonical row on the as-of date reproduces; 83.78 appears in no canonical row for the asset on any date. The lot object does not say which source priced the lot, so the price cannot be traced from the served object alone. Those lots are excluded from the thread candidates and are not counted as chain or direct candidates.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W4-S2",
      "carried to new item after C5 (packet section 4)"
    ],
    "remedy": "A read-only census over all 3,509 client objects of lots priced off no canonical row on the as-of date, then a fix of their source under FWD-7. Close when: the census reads 0 such lots, or each is named with its source.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W4-S8",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Measured on one client object: 7 of 110 lots break the identity, two of them the Exxon lots. The scope across the served home is not measured (outside the cell's bounds). For those lots a valuation read from market_value would differ from one read from quantity times price.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W4-S8",
      "carried to C4 (FWD-8) (packet section 4)",
      "this seat's read of z08334146/detail.json VersionId ZCjWpzPR1n2u...: 73 x 168.94 = 12,332.62 against a served market_value of 5,000.7866 (cost_basis 10,007.57)"
    ],
    "remedy": "The cap's per-lot UNVERIFIED (Andrew's ~12:2xZ ruling; FWD-8): value and gain absent with status, never scaled. Close when: no served lot shows a scaled market value beside an unscaled cost.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W3-S2",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "For six of the twenty window dates there is no daily file in any version. On the two dates compared (2026-09-17 and 09-30), about 40% of assets present in both the daily file and the served canonical rows carry different prices, mostly yahoo_finance rows, and the served transaction_observed price matched some daily-file version for only 2 of the 462 non-equal rows. The daily file is therefore not a faithful anchor for the served value. Write time must come from canonical object versions, which were not read.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W3-S2"
    ],
    "remedy": "Find why silver/prices/<date>.parquet is absent on six trading days (2026-09-21, 09-22, 09-28, 09-29, 10-05, 10-06: every one a Monday or Tuesday, each a trading day by lib/trading_calendar.py). Close when: the cause is named and either the files exist or the reader is told they never will.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W4-S1",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The served detail objects carry the as-of date 2026-10-09, a day with transaction_observed rows in both silver/prices/2026-10-09.parquet and canonical_prices.parquet. The holding read for BP-a-4 is therefore a direct (shape a) candidate on 2026-10-09, not a chain on 2026-10-12. The key carries no date; the as-of date lives only in the body.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W4-S1"
    ],
    "remedy": "Route to the producer of the served 49F client detail objects: on a 2026-10-13 read the objects carry data_as_of 2026-10-09 while the last trading day is Monday 2026-10-12 (trading by lib/trading_calendar.py), one trading day behind T-1. Close when: a read after the producer's run shows data_as_of equal to T-1, or the lag is a stated design.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W4-S10",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The served home holds client objects whose as-of date is months old, alongside objects dated 2026-10-09. The served T-1 object is therefore not uniform across client objects; the thread uses each object's own data_as_of.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W4-S10"
    ],
    "remedy": "Nine of 120 sampled normal client objects are far older (six at 2026-04-02). Close when: each is named as a closed or inactive relationship, or refreshed.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W2-S3",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The two objects disagree on the source label for the same date. The values agree within the match tolerance (the gap is float32 rounding of 99.6). The instrument reports tie true, lists both rows, and takes the daily row as the stable pick. Only the label and the B_01 keep decision differ. The rank rule would have kept transaction_observed in canonical, so the daily row did not reach canonical by that rule.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W2-S3"
    ],
    "remedy": "A same-date source disagreement between the daily silver/prices file and canonical (here transaction_observed vs linear_interpolation, with a float32 canonical price). With W4-S3 and W4-S5 this is the S33 re-read the packet asks of the CTO (FWD-5).",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W4-S3",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The served lot carries the canonical value, so the tie was resolved toward canonical for this holding, while the tool's emulated stable pick names the daily file. The daily value 92.216667 is not the median of the same day's trades (91.983333). The record therefore cites the canonical row and states the tie in THREAD_TRACE.md.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W4-S3"
    ],
    "remedy": "Same class as W2-S3: daily and canonical disagree on the same date (92.216667 vs 91.983333, both transaction_observed). Carried to the S33 re-read (FWD-5).",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W4-S5",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The two price objects carry different sources for the same asset and date (carry_forward against transaction_observed). The served lot follows the canonical row. The daily row is not reproduced by any trade on 2026-10-09 for this asset (the trade partition gives 168.94 for the asset, the daily value is 162.155).",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W4-S5"
    ],
    "remedy": "Same class, inside the thread's own row: daily carry_forward 162.155 vs canonical transaction_observed 168.94; the served lot took canonical. Carried to the S33 re-read (FWD-5): the brief's 'latent, 0 of 11,108' does not hold for served rows.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W4-S6",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "For this tie the stable pick is the daily row, whose carry-forward value matches a row two trading days earlier than the one the tool names. The tool's rule attribution for that daily row is therefore not the rule that produced it. The canonical row, which the lot carries, is traced only by a call with the canonical object alone (trace_canonical_only.py, which calls the instrument's trace_asset_date unchanged).",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W4-S6"
    ],
    "remedy": "The trace instrument's default stable pick reads the daily row while the served lot reads canonical, so it reports a false mismatch on such assets. FWD-3's grade (DEC-10) must trace what is served. Close when: the instrument reads the source the served object used, beside the thread recompute still equal.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "ADVI_BDPRCE-D1-W4-S9",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The operational rule is satisfied and the outcome sentence (a security with no public ticker) is not established by the rule. The first fitting holding is a common-stock name. The thread record states the rule used and does not claim the asset has no listing.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W4-S9"
    ],
    "remedy": "The no-public-ticker rule selects a listed common stock (EXXONMOBIL HOLDINGS CORP COM SHS) whose served ticker is null: a ticker-mapping gap. Close when: the read-only census over all client objects names the listed-but-untickered holdings, and FWD-1's exemplar is a genuinely unlisted holding.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  }
]
```
