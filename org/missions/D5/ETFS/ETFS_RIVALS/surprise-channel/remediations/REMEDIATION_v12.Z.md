# ETFS_RIVALS -- rounds 14 to 19 remediations (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~13:20Z. Graduated at the L9 of rounds 14 to 19 (`adjudications/ADJUDICATION_v17.Z.md`
to `ADJUDICATION_v21.Z.md`).

Round 14 is deployed and graded on the served 13:07Z page. Rounds 15 to 19 (and round 20, which carries no judgment
criterion) are merged on site-Z CLOUD and NOT deployed; their grades are on the issuer's round-19 real run.

REMEDIATED: Z-S54, Z-S55, Z-S56, Z-S58 (all four BLOCKING), C-S53, C-S54, C-S57, C-S61; in place, REMEDIATION_v11 S43.
OPEN: Z-S57 with C-S58 and C-S59 (two keys in GQGU, served); Z-S59 and C-S60 (month strips; four display items);
C-S55 (SUNB); Z-S60, Z-S61 and C-S62 (round 20's repairs, built and not yet exercised live). Still OPEN from earlier: C-S36 (the four names), S24, W6-S2.
Owed after the deploy: RIV-md-1 J1 and RIV-pd-2 J1 on the served page; the served re-read of Z-S55's proof.

```json
[
  {
    "id": "ETFS_RIVALS-Z-S54",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The AI step ran before the table rebuild, so an account quoted an earlier build than the panels beside it under a plain 'Grounded' (149 of 197 cited figures moved on the served 2026-10-06 page).",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S54",
      "adjudications/ADJUDICATION_v21.Z.md ETFS_RIVALS-Z-C-S61"
    ],
    "remedy": "Cell RIV-ab-1 (deploy cc02eeac7d): the table refresh runs before the AI step and the badge says 'Grounded on an earlier build' when an account's cited rows are not the served revision. Proof on the served 2026-10-07 page of the 13:00Z sweep: 25 of 26 accounts 'Grounded' on the served build, 1 FAIL of its own; 157 of 157 parsed cited figures equal a ranking row; the served 2026-10-06 republish shows 24 of 24 PASS accounts on the earlier-build badge.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v12",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v12"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-C-S61",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-14 grade record that adjudicates Z-S54; it also closes S43 on the served page and re-reads C-S36 and Z-S57.",
    "evidence": [
      "adjudications/ADJUDICATION_v21.Z.md ETFS_RIVALS-Z-C-S61"
    ],
    "remedy": "As Z-S54 above. S43 is moved in place in REMEDIATION_v11 (OPEN to REMEDIATED). C-S36 stays OPEN in REMEDIATION_v8: the four names still read as tickers on the 13:07Z page.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v12",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v12"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-S55",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "price_series joined Bloomberg closes in the listing's quote currency to holding-implied prices in US dollars, so a non-dollar security's curve was not one price. The row's 3x census (152 of 598) was a floor (C-S52).",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S55",
      "adjudications/ADJUDICATION_v17.Z.md ETFS_RIVALS-Z-C-S53",
      "adjudications/ADJUDICATION_v20.Z.md ETFS_RIVALS-Z-C-S60"
    ],
    "remedy": "CTO ruling msg 30787, cell RIV-pc-1: an implied price is drawn only for a security whose stored quote currency is USD; the object and the dialog carry the currency. Proof on the round-19 real run: 0 fund-securities carry an implied point outside USD; 334 of 335 non-dollar frames print their currency. Re-read on the served objects after the deploy.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v12",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v12"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-C-S53",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The grade record that adjudicates Z-S55.",
    "evidence": [
      "adjudications/ADJUDICATION_v17.Z.md ETFS_RIVALS-Z-C-S53"
    ],
    "remedy": "As Z-S55 above.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v12",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v12"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-C-S54",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A security with no stored currency carried the sentence 'this listing is not quoted in US dollars'; 43 of the 96 were US-listed keys, for which it was false.",
    "evidence": [
      "adjudications/ADJUDICATION_v17.Z.md ETFS_RIVALS-Z-C-S54",
      "adjudications/ADJUDICATION_v18.Z.md ETFS_RIVALS-Z-C-S57",
      "adjudications/ADJUDICATION_v20.Z.md ETFS_RIVALS-Z-C-S60"
    ],
    "remedy": "CTO ruling msg 30817 term 2, cell RIV-nc-1: a holding with no stored currency draws no curve and says 'No price history is stored for this holding yet.' Proof on the round-19 real run in a browser: 97 of 97 such frames show the sentence and no chart. The backfill's security list with formerly-held keys (term 1) is the path that gives them a curve.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v12",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v12"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-C-S57",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-17 grade record that adjudicates C-S54.",
    "evidence": [
      "adjudications/ADJUDICATION_v18.Z.md ETFS_RIVALS-Z-C-S57"
    ],
    "remedy": "As C-S54 above.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v12",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v12"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-S56",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "A dialog's static trade list said 'No trades in the last 365 days' for a fund-security whose chart object held markers in those days (618 frames said it).",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S56",
      "adjudications/ADJUDICATION_v20.Z.md ETFS_RIVALS-Z-C-S60"
    ],
    "remedy": "Cell RIV-tl-1: the list is written from the chart object's markers. Proof on the round-19 real run in a browser, by this seat: 702 of 702 frames' lists agree with their markers; 0 static elements say 'No trades' before the script runs.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v12",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v12"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-S58",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The month strip labelled its cells January to December by position while the trend's months start at the window's first month.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S58",
      "adjudications/ADJUDICATION_v20.Z.md ETFS_RIVALS-Z-C-S60"
    ],
    "remedy": "Cell RIV-ml-1: each cell carries the month it is, counted back from the page month. Proof on the round-19 real run: 393 of 393 strips labelled on every cell and ending in Oct.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v12",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v12"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-S59",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "11 of 393 month strips disagree with the year-months their fund-security's markers end in (cause unread). Separately, a year strip is 12 cells from November 2025, so 56 strips cannot show October 2025 trades that the 365-day list shows.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S59",
      "adjudications/ADJUDICATION_v20.Z.md ETFS_RIVALS-Z-C-S60",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/etfs_rivals_r19/analyse2.py @0c69a8829e (the 11 are printed)"
    ],
    "remedy": "Establish the cause of the 11 (the strip reads buying_trend month tokens; the markers read the trade schedule) and rule on the window's oldest partial month. Proof: analyse2.py on a real day's page prints 0 strips disagreeing inside their span, and either 0 year strips with a marker month that has no cell or a stated reason on the strip.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v12",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v12"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-C-S60",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The rounds 15-19 browser grade. Beyond Z-S59 it carries: 141 dialogs put a 30-day or 90-day buying section above a 365-day trade list; BIDD 6475395Z_GR_Equity has 4 markers, 0 prices and draws nothing; the 'Price in <currency>' label prints over a long top axis figure; markers ride the top edge when a range has almost no prices. RIV-md-1 J1 and RIV-pd-2 J1 are owed on the served page.",
    "evidence": [
      "adjudications/ADJUDICATION_v20.Z.md ETFS_RIVALS-Z-C-S60"
    ],
    "remedy": "The CTO's round analysis rules which of the four are cut. Proof for each cut: the named frame or count re-read by r19grade.py on a real day's page. md-1 J1 and pd-2 J1 are graded on the served page after the deploy.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v12",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v12"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-C-S55",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "INEQ SUNB_US_Equity: stored currency USD, market close 77.39 against the fund's same-day implied 63.49 (2026-10-05). Cause not established. 1 of 217 dollar securities compared.",
    "evidence": [
      "adjudications/ADJUDICATION_v17.Z.md ETFS_RIVALS-Z-C-S55"
    ],
    "remedy": "Establish the cause from INEQ's holding row and the key's Bloomberg security, then correct the key or record why the two differ. Proof: the same-day close and implied price agree within 3 percent, or a row states the cause with the fund's reported identifier beside the key's.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v12",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v12"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-S57",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "After the parsekey landed, GQGU's securities split across a CUSIP key and a Bloomberg key: buying_trend merged 2, split 7 (issuer's read); on the served pages 6 names appear under two keys each.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S57",
      "adjudications/ADJUDICATION_v19.Z.md ETFS_RIVALS-Z-C-S59",
      "adjudications/ADJUDICATION_v21.Z.md ETFS_RIVALS-Z-C-S61"
    ],
    "remedy": "Establish why the trend (and the page's dialogs) keep the CUSIP key where holding_contribution merged 13 of 13, and make the one-key rule hold there. Proof on a served page: for GQGU, 0 security names under two keys; the issuer's census reads buying_trend SPLIT 0.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v12",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v12"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-C-S58",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The same split seen on the round-17 real run's GQGU chart object: 7 names under two keys, the CUSIP key holding the markers.",
    "evidence": [
      "adjudications/ADJUDICATION_v18.Z.md ETFS_RIVALS-Z-C-S58"
    ],
    "remedy": "As Z-S57 above; the chart object is one more reader of the split key.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v12",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v12"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-C-S59",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The grade record that adjudicates Z-S57 on the served 2026-10-06 republish.",
    "evidence": [
      "adjudications/ADJUDICATION_v19.Z.md ETFS_RIVALS-Z-C-S59"
    ],
    "remedy": "As Z-S57 above.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v12",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v12"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-S60",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "As first built, the Bloomberg range backfill would have moved the served rankings (a newer G4 object marks the day's table stale), would not have given a formerly-held key its currency, and did not fit one day's budget.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S60",
      "adjudications/ADJUDICATION_v21.Z.md ETFS_RIVALS-Z-C-S62",
      "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round20/delta0_2026-10-06.json @0192e63608"
    ],
    "remedy": "CTO ruling msg 30897, cell RIV-bk-1 (merge 42462181c1): backfill rows are marked and the rankings ignore them; one CRNCY request supplies a missing currency; held dates carry over to later days. Built and proved on the table (13 of 13 funds equal with marked rows, 0 of 13 with the control). Proof still owed on the vendor plane: the dry run, then after the first backfill day the served rankings of a page day inside the backfilled window equal their figures from before it, and the ledger shows the day inside its allowance.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v12",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v12"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-S61",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "buying_trend's G4 read did not load security_parsekey, so its parsekey join was always empty: the cause of Z-S57's split keys.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S61",
      "adjudications/ADJUDICATION_v21.Z.md ETFS_RIVALS-Z-C-S62"
    ],
    "remedy": "Cell RIV-bk-1: the read names the column (gold_buying_trend.py line 313). Proof is Z-S57's: on a served page after the deploy and a vehicle run, 0 GQGU security names under two keys.",
    "owner": "2.0.0_SA_COO~RV",
    "round": "v12",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~RV",
      "round": "v12"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-C-S62",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-20 record that adjudicates Z-S60 and Z-S61.",
    "evidence": [
      "adjudications/ADJUDICATION_v21.Z.md ETFS_RIVALS-Z-C-S62"
    ],
    "remedy": "As Z-S60 and Z-S61 above.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v12",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v12"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~RV
