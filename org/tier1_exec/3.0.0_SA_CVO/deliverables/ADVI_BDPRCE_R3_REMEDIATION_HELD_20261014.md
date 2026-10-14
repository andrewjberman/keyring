# ADVI_BDPRCE round 3 -- graduates HELD for REMEDIATION_v3 (3.0.0_SA_CVO, dell1)

Status: HELD. Written 2026-10-14T06:20:00Z. The row gate (LD-0521) refuses a new remediation row while any ADVI_BDPRCE order is non-terminal; BP-c-2 (pending) and BP-c-3 (staged) were reopened at @13167533b7 under R1 Amendment 4.
Un-parks when: 2.0.0_SA_COO~K1's second round-3 close message arrives and every round-3 order is terminal. Owner of the landing: 3.0.0_SA_CVO, who copies these rows to
`org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/remediations/REMEDIATION_v3.md` (re-reading each against the R1.4 re-run first) and then sends the round-3 slug.
Adjudicated in `org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/adjudications/ADJUDICATION_v3.md`. 10 rows: 8 ARMED, 2 INERT.

```json
[
  {
    "id": "ADVI_BDPRCE-D1-W16-S2",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The count is exactly 500000 on 15 of the 67 non-stub days, every one from 2026-07-08 on, and the 52 earlier non-stub days vary with the book from 408467 to 489203. The round-2 fixture 2026-10-09 holds the same 500000 rows. No repo setting yields 500000, so the cap sits on the Black Diamond side and is inferred from the count pattern; lots beyond the cap are not in those exports, and any silver partition built from them carries the same truncation (not measured here). The apply of the Units and Cost Basis switch waits on this row's disposition.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W16-S2",
      "adjudications/ADJUDICATION_v3.md"
    ],
    "remedy": "The paging design for the exact-lot export, then the apply. Close when: an export day at the cap is completed by pages whose row total exceeds 500,000 on a day the single export reads exactly 500,000, read from S3.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v3"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W16-S1",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Keys sit on most weekdays from 2026-03-27 to 2026-07-09 (with 9 header-only stubs), then only on 2026-07-10, 07-17, 07-24, 07-31, 08-07, 08-14, 08-21, 08-28, 09-04, 09-11, 09-18, 09-25, 10-02 and 10-09, all Fridays. The matching _complete sidecars exist only for the same Fridays. The cause (runner cadence, lifecycle expiry or a move) is not established by this read, and the cell's 14-day count is therefore 2 dates, not 14.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W16-S1",
      "adjudications/ADJUDICATION_v3.md"
    ],
    "remedy": "Named in the paging design. Close when: the design states which bronze unrealized key serves each calendar day and the Friday-only gap is either filled or declared with its reader.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v3"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W17-S1",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Under the ruled key 192 rows of the recorded export fold into 191 colliding groups, and all 191 differ on Market Value (one also on Inherited Date). The export has no lot identifier column, so no recorded column separates them. Within one snapshot one asset has one price, so the differing Market Value most likely reflects distinct quantities, which would mean distinct lots; this is INFERRED, not measured, because the export carries no Units. Applied under this key, the lot table would drop those 192 rows. Armed for the apply: the apply's author decides a key that separates them (a units-bearing key is untested on this fixture) before any template switch.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W17-S1",
      "adjudications/ADJUDICATION_v3.md"
    ],
    "remedy": "The key gains units (PRD v1.3). Close when: the first real export under the apply's pair reads 0 folded rows under the v1.3 key, read by a seat other than the apply's author.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v3"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W23-S1",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The recorded export has no Units column, so the v1.3 key cannot be evaluated on it. The only v1.3 lot table this fixture writes is built on synthetic units, a hash of all 15 recorded columns, which separates every differing row by construction: lot_rows 500000 and 0 folded are true of the hash, not of the export. The grader's lots=500000 carries no basis field and reads as a measured count. The record labels the figure and reads no result from it; the zero is read on the first real export under the apply's pair (PRD v1.3, call 67ac). Armed: the apply's author must not take the printed lots figure or the synthetic zero as evidence.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W23-S1",
      "adjudications/ADJUDICATION_v3.md"
    ],
    "remedy": "Close when: the zero for W17-S1 is read on a real export with a Units column; the synthetic-units figure is never cited as evidence.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v3"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W18-S4",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The Monday and Tuesday windows are not genuinely empty: SENTINEL.json gives EXPORT_WINDOW_RULE, and the last published trade day lies outside the span. The runner still accepts the empty transactions table, so the sentinels for 10-12 and 10-13 exist over zero transaction rows, and the sentinel is what triggers bd-silver-merge (BP-b-5 record). Whether silver for those two dates was built on the header-only content is not read in this cell.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W18-S4",
      "adjudications/ADJUDICATION_v3.md"
    ],
    "remedy": "A producer change in the shared bronze module: anchor the newest transactions chunk to the last published business day and decide whether a measured-empty window may complete a day. Close when: a Monday and a Tuesday run each land a non-empty transactions export, and the ten Monday/Tuesday dates are re-landed.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v3"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W20-S8",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The served series moved again between the replay's read and this probe. The probe's per-unit and per-100 readings, and every row it draws from the canonical series, rest on the 04:03 object. Whether REPLAY2's figures still hold on that object is not measured here; the probe does not compare the two objects.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W20-S8",
      "adjudications/ADJUDICATION_v3.md"
    ],
    "remedy": "Close when: the writers of silver/prices/canonical_prices.parquet are named and counted (N printed), and every replay record prints the ETag it read.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v3"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W20-S11",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The clause is built as written and the count is its measured consequence of served-map coverage and the bands. The 190 rows of the 17 unserved assets carry no served unit, so R1 prices none of them on those dates. The 12 ISHARES rows read per-unit-shaped on their own ratio (1.0) and are withheld only because the served median is outside both bands (see W20-S12 and W20-S13). Nothing is adjusted; the counts are as measured.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W20-S11",
      "adjudications/ADJUDICATION_v3.md"
    ],
    "remedy": "A CTO call on the band for fixed-income funds (ratios 1.04 to 1.09) and on the 59 served assets with no pair. Close when: the ruling is recorded and the replay reads the withheld Fixed Income count it predicts.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W20-S13",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The median is taken over all pairs as ruled. For this asset the usable lot pairs sit far from its trade pairs (the lot ratios spread widely), so the lot source sets the median against the asset's own same-date trades, which read 1.0 (per unit) on the served date. The extract's market_value/quantity does not track the trade-implied unit for this asset. Nothing is adjusted: the record prints the unreadable unit and this row carries the measured disagreement. Whether lot pairs belong in the median is the CTO's call.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W20-S13",
      "adjudications/ADJUDICATION_v3.md"
    ],
    "remedy": "One served-unit map for every caller of the module. Close when: the R1.4 module fixes the pair source inside served_unit_map (or one helper every writer calls), and the probe and the replay print the same per100 / per_unit / unreadable counts, with ISHARES CORE U.S. AGGREGATE BOND ETF and SIX FLAGS read once.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v3"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W19-S2",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The RPS source has no partition after 2026-07-23, so a lot dated 2026-10-09 cannot take its price from a same-day RPS row. This is a fact about the partition listing; it is not a finding about any served price.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W19-S2",
      "adjudications/ADJUDICATION_v3.md"
    ],
    "remedy": "Round-4 enrichment item 4. Close when: the 431 unexplained lots (34 'nan') and the 1,118 lots priced by the 2026-07-23 RPS partition each carry a named source or a stated exclusion.",
    "owner": "2.0.0_SA_COO~K1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~K1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~K1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_BDPRCE-D1-W22-S1",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The extract's current_price for these lots is not the served old_price of the asset: 93 of 819 agree. The packet states the headline on the served basis, as the formula says, and the lot-price basis beside it. Which basis is the true change for the book is not settled by the order, and the page asks Andrew to see both.",
    "evidence": [
      "investigation row ADVI_BDPRCE-D1-W22-S1",
      "adjudications/ADJUDICATION_v3.md"
    ],
    "remedy": "Close when: the CTO rules which basis is the change in Andrew's book, and the R1.4 packet prints that basis first with the other two beside it.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  }
]
```
