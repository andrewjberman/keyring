# ADVI_COTBKF -- rounds 2 and 3 remediations

<sweep_watermark>2026-10-07T02:21Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-07 ~03:4xZ. Graduated at this compile (ADJUDICATION_v2.md): 7 rows; and 3 round-1 rows (W2-S1, S3, S2) that ADJUDICATION_v1.md graduated without a row, written here closed. Three were ARMED and are DISARMED and
closed here (W6-S4, W10-S3, W11-S3). Four are OPEN and INERT (W6-S2, W6-S5, W10-S4, W11-S2). W10-S5 rides W6-S5; S4, S5 and S6 are the
disarm evidence.

```json
[
  {
    "id": "ADVI_COTBKF-W6-S2",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The price-coverage read counts a security UNPRICED when the stores it read do not price it. It did not read any position-level store, and it did not name opal-data-49financial gold/advi/canonical/canonical_positions, which holds a CUSIP-keyed closing price for 565 daily partitions. The read also uses the bd and inf price files for a Cottonwood universe, and whether a price read may cross a firm's bucket is not ruled.",
    "evidence": [
      "adjudication row ADVI_COTBKF-C-S3 (ADJUDICATION_v2.md): 912 of 4,634 Commonwealth CUSIPs priced in the 2026-10-05 partition alone; 30 of 40 buckets not named by the census",
      "PRICE_COVERAGE_20261006.md: 0 securities matched by CUSIP in the five large stores; Fixed Income 0 of 778 priced"
    ],
    "remedy": "Two acts. (1) 1.0.0_SA_CTO rules whether a Commonwealth price read may use another firm's bucket for MARKET prices (49 Financial's custodian marks; the bd and inf files already read), under the cross-firm law. (2) On that ruling, the coverage read is re-run with every position-level store it may use (CUSIP match first), and the unpriced count is restated. REMEDIATED when the census names every bucket with its verdict and the coverage line is re-read.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~C",
      "round": "v4"
    },
    "closed": true
  },
  {
    "id": "ADVI_COTBKF-W6-S4",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "CB2b3-AC2 meets its 120-second bound only against a filtered cache; the cache sat in worker 6's worktree, which was due for removal.",
    "evidence": [
      "this seat, 2026-10-07 03:3xZ, shared tree: CB2b3-AC2 rc 0 in 9.7 s, PRICE-COVERAGE universe=4634 stores_checked=22",
      "adjudication row ADVI_COTBKF-C-S4 (ADJUDICATION_v2.md)"
    ],
    "remedy": "Done: the cache is in the shared tree's .scratch/price_cache and the criterion re-ran inside its bound at this seat. A clean tree on another device needs one cold run first.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~C",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~C",
      "at": "2026-10-07T00:04Z"
    },
    "closed": true
  },
  {
    "id": "ADVI_COTBKF-W10-S3",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "CB3c3-AC2 meets its 120-second bound only against a column-projected cache; the cache sat in worker 10's worktree.",
    "evidence": [
      "this seat, 2026-10-07 02:5xZ, shared tree: CB3c3-AC2 rc 0 in 6.4 s, CROSSWALK commonwealth_accounts=1533 every_account_listed=True",
      "adjudication row ADVI_COTBKF-C-S4 (ADJUDICATION_v2.md)"
    ],
    "remedy": "Done: the cache is in the shared tree's .scratch/advi_cotbkf/cache and the criterion re-ran inside its bound at this seat.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~C",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~C",
      "at": "2026-10-07T02:07Z"
    },
    "closed": true
  },
  {
    "id": "ADVI_COTBKF-W11-S3",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "CB3c4-AC2 meets its 120-second bound only against a primed transactions cache; the cache sat in worker 11's worktree.",
    "evidence": [
      "this seat, 2026-10-07 02:5xZ, shared tree: CB3c4-AC2 rc 0 in 3.1 s, ACCOUNT-LINKS old_accounts=459 every_old_account_listed=True",
      "adjudication row ADVI_COTBKF-C-S4 (ADJUDICATION_v2.md)"
    ],
    "remedy": "Done: the cache is in the shared tree's .scratch/advi_cotbkf/tx_cache and the criterion re-ran inside its bound at this seat.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~C",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~C",
      "at": "2026-10-07T02:21Z"
    },
    "closed": true
  },
  {
    "id": "ADVI_COTBKF-W6-S5",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two new scripts read existing S3 stores at addresses the builders do not emit. The naming gate refused the typed addresses, and both scripts now read them from record files under org/, which the gate does not grade. Rule 30 says a refusal is a missing registry row; its non-application covers existing pipelines; which applies to a new READ of an old store is not ruled.",
    "evidence": [
      "adjudication row ADVI_COTBKF-C-S5 (ADJUDICATION_v2.md); investigation rows ADVI_COTBKF-W6-S5 and -W10-S5"
    ],
    "remedy": "1.0.0_SA_CTO rules it: either registry rows for the legacy stores a new script may read, or a stated non-application for reads of existing stores. The two record files then follow the ruling. REMEDIATED when the ruling is recorded and the two scripts match it.",
    "owner": "1.0.0_SA_CTO",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v4"
    },
    "closed": true
  },
  {
    "id": "ADVI_COTBKF-W10-S4",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The crosswalk never scores a Commonwealth account whose last activity is before 2026-04-22. One such account, acct#a2618be7, left in kind on 2026-04-07. Seventeen NOT_MATCHED accounts score 0.65 to 0.8 against one candidate and wait for a person.",
    "evidence": [
      "adjudication row ADVI_COTBKF-C-S6 (ADJUDICATION_v2.md): 11 of 758 closed-before rows end in 2026; acct#a2618be7's seven lo rows on 2026-04-07"
    ],
    "remedy": "P3: score every account whose final rows are an in-kind exit, whatever its date, and list the 17 near-matches for Andrew's or the advisor's read. REMEDIATED when the crosswalk line is re-read with acct#a2618be7 scored.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~C",
      "round": "v4"
    },
    "closed": true
  },
  {
    "id": "ADVI_COTBKF-W11-S2",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Account links exist only for the 459 accounts that ended before 2018. A client's line therefore stops at the first account that is not old, and 46 of the 148 such targets themselves stopped trading before 2026, so FWD-9's line from the oldest account to the newest is not shown for those clients.",
    "evidence": [
      "adjudication row ADVI_COTBKF-C-S7 (ADJUDICATION_v2.md): 180 links, 2,652 of 2,652 evidence items verified; investigation row ADVI_COTBKF-W11-S2"
    ],
    "remedy": "Extend the link rule to every account that ends before the delivery's last day (2026-06-23), so a chain is followed to its newest account. It is a cut for the next round, placed by 1.0.0_SA_CTO's analysis. REMEDIATED when the 46 targets each carry a row.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~C",
      "round": "v4"
    },
    "closed": true
  },
  {
    "id": "ADVI_COTBKF-W2-S1",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Round 1's silver rule dropped 1,360 record-level repeats, so silver held fewer rows than the delivery had records.",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md@51a7c07278",
      "adjudication row ADVI_COTBKF-C-S1 (ADJUDICATION_v1.md), which graduated this item with no remediation row; the row is written at this compile",
      ".scratch/advi_cotbkf/cache/transactions.parquet read at this seat 2026-10-07: 1,416,497 rows, 1,533 accounts"
    ],
    "remedy": "Done in round 2: PRD v0.4 C-SILVER keeps every record and TO-CB-b-1 rebuilt silver; the table this seat read holds 1,416,497 rows.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~C",
      "round": "v4"
    },
    "closed": true
  },
  {
    "id": "ADVI_COTBKF-S3",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PRD v0.4's addendum first counted 1,416,500 physical lines where the delivery has 1,416,497 records.",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md@51a7c07278",
      "adjudication row ADVI_COTBKF-C-S1 (ADJUDICATION_v1.md), which graduated this item with no remediation row; the row is written at this compile",
      ".scratch/advi_cotbkf/cache/transactions.parquet read at this seat 2026-10-07: 1,416,497 rows, 1,533 accounts"
    ],
    "remedy": "Done: the PRD and TO-CB-b-1 state 1,416,497 records, and the rebuilt silver holds that many rows.",
    "owner": "1.0.0_SA_CTO",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v4"
    },
    "closed": true
  },
  {
    "id": "ADVI_COTBKF-S2",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FWD-1 as first worded asked for one account's history from 2013 to June 2026; no delivered account spans both years.",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md@51a7c07278",
      "adjudication row ADVI_COTBKF-C-S1 (ADJUDICATION_v1.md), which graduated this item with no remediation row; the row is written at this compile"
    ],
    "remedy": "Done: PRD v0.4 words FWD-1 as far back as Commonwealth recorded it, and adds FWD-9 for a client across an account change; round 3's account links (CB-c-4) exercise FWD-9.",
    "owner": "1.0.0_SA_CTO",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v4"
    },
    "closed": true
  }
]
```
