# ADVI_BDPRCE -- round 2 remediations (dell1)

<sweep_watermark>2026-10-14T01:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T01:45:00Z. Graduated at ADJUDICATION_v2: 10 rows (5 ARMED, 5 INERT).

```json
[
  {
    "id": "ADVI_BDPRCE-D1-W7-S4",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The identity holds on 89.1% of checked lots and fails on the rest. The breaks are not one multiplier (median ratio of quantity x price to market value 4.96), and 16,297 breaks carry market_value exactly 0 while quantity is nonzero. 20,520 breaks sit on NOT_UNTICKERED lots. A valuation read from market_value differs from one read from quantity x price on these lots; the census does not say which field is right.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W7-S4"
    ],
    "remedy": "Per-lot UNVERIFIED under FWD-7 (as W4-S8): a lot whose value cannot be quantity x an exact price reads UNVERIFIED, never 0 and never scaled. Close when: the census reads 0 lots breaking the identity without the UNVERIFIED status, including the 16,297 served market_value 0 with nonzero quantity.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v2"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W10-S2",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "On the recorded export the mandated key is not one row per tax lot: 15,553 rows fold into 14,696 groups, mostly rows that differ on Relationship ID. The key ignores Relationship ID and Inherited Date and treats a null Open Date as a value. Applied as written, the lot table holds 484,447 rows where the export holds 500,000. Whether the 15,553 folded rows are distinct lots is not determined by this fixture. Armed for the apply: the apply amendment's author decides the key before any template switch.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W10-S2"
    ],
    "remedy": "The lot key per PRD v1.1 (add relationship_id or the export's own lot id). Close when: the re-run fixture proof reads 0 rows folded and 0 colliding groups still differing, before any apply.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v2"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W12-S1",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The served price for the holding on 2026-10-09 has a canonical row whose source is linear_interpolation (flat at 10.3525) and a daily partition row whose source is carry_forward (10.3525). The value agrees with R1's carry from the 2026-10-02 trades; the writing rule in the served row is the banned interpolation. The writer of this specific canonical row is not identified here; the trace names the bd_price_update.py backfill path as the interpolation source.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W12-S1"
    ],
    "remedy": "The writer stops serving linear_interpolation as a price source (R1 clause 5; FWD-2, FWD-7). Close when: no served 49F price row carries linear_interpolation, the 18,566 window rows each re-sourced under Andrew's reviewed list.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v2"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W6-S2",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "For eight changed rows the R1 price is 100.0 times the served price within 1e-3. All eight fall between 2026-09-16 and 2026-10-09 and all are bond or certificate names. The replay flags them scale_100x and does not decide the scale rule; the 8 rows need a ruling before any served price moves.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W6-S2"
    ],
    "remedy": "Par-quoted per-unit price per R1 AMENDMENT 1 (executed price / 100 where the asset class says par-quoted; ratio corroborating; disagreement withheld), in the module and the re-run replay. Close when: the 8 rows read UNCHANGED in the re-run replay and no served bond price is 100x its unit.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v2"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W9-S2",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The defect is fixed in the deployed code from 2026-10-07 (deployed md5 968b33e2 equals the repo file). Six run dates before that fix have no sentinel and no daily price file. Nothing in the current code re-emits a sentinel for a past run date, so the gaps persist until a later cell backfills them.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W9-S2"
    ],
    "remedy": "Re-classed ARMED by this seat (filed INERT): left alone, the BD runner keeps logging 'OK bronze sentinel emitted' when no _BRONZE_COMPLETE.json exists, so every Monday/Tuesday header-only failure reads green. Route to the runner's owner: the OK line follows a read-back of the object. Close when: a run whose sentinel is withheld logs no OK, beside a control run that writes and reads it back.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W5-S3",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "silver/transactions/2026-10-12.parquet exists with zero rows. The probe reads it, and R1 yields no price for any asset on 2026-10-12.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W5-S3"
    ],
    "remedy": "silver/transactions/2026-10-12.parquet (T-1 for 10-13) exists with 0 rows: the Monday header-only export (BP-b-5) reaches the silver layer as an empty day. Same cause as W3-S2 (OPEN in REMEDIATION_v1). Close when: the upstream cause is named and an empty partition is distinguishable from a no-trade day.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W6-S3",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "No 2026 partition holds a row dated before its own file date. 9,409 trade rows dated inside the window sit outside their trade-date partition, and 33 served rows price differently under own-day keying. Rows landing more than one day late fall outside the lookback's t and t+1 read, so a pre-2026 observation from the lookback may be older than the true latest. The window R1 reads every 2026 partition, so it is unaffected; trades that land after 2026-10-13 are not seen.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W6-S3"
    ],
    "remedy": "Trade rows land up to 519 days late (61,583 more than a day late in 2026): the replay's t/t+1 lookback misses them. Close when: the replay reads late-landed trades by trade_date, or its list states the limit per row (round-3 item 1).",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W6-S5",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The missing weekday partitions in 2026 are 2026-02-18, 04-03, 04-21, 05-01, 05-25, 06-19, 06-22 and 06-23. 2026-06-22 and 06-23 are not market holidays. None of the window's 20 weekday partitions is missing. In 2020-03 to 2025-12 there are 436 dates without a partition, 101 of them weekdays.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W6-S5"
    ],
    "remedy": "silver/transactions has no object for 50 dates in 2026 (8 weekdays) and 436 in 2020-2025, read by the replay as no-trade days. Close when: each missing weekday is named as a non-trading day or a gap, and the replay marks rows whose lookback crosses a gap.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W10-S1",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The S3 copy still carries VersionId VgzqQbd.3F3sAlllb6SWsjKZ2XvXgAfE at 14,419 bytes, but the repo copy at HEAD is 13,920 bytes with LF line endings. The two differ in line endings only and are equal as parsed JSON. The patched template is built from the S3 bytes.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W10-S1"
    ],
    "remedy": "PRD v1.0 CONTRACTS (the qt4 template row) states the S3 template is 'equal to the repo (sha256 equal, 14,419 bytes)'. Measured: S3 is CRLF at 14,419 bytes, the repo blob LF at 13,920 bytes; equal only after CRLF normalisation. The ratified text carries a false equality this seat did not re-measure at signing. Close when: a PRD addendum states the measured relation (normalised-equal), and the template switch's apply compares parsed JSON, not sha256.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W10-S3",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The export holds exactly 500,000 rows, which matches a row cap. The fixture cannot establish whether the export is complete. The read of :1138-1215 shows no row-count check in the step. The premise binds the legacy table and the lot table alike.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W10-S3"
    ],
    "remedy": "The recorded unrealized export holds exactly 500,000 data rows; a round count can be a truncation cap. Close when: BD's export is shown complete (a row count from BD itself, or a second export with a different total), before the Units/Cost switch is applied.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v2"
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
