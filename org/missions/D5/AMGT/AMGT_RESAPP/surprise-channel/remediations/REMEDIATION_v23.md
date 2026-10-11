# AMGT_RESAPP -- surprise channel, REMEDIATION v23 -- THE SLUG (round 77)

Author: 3.0.0_SA_CVO~Z. Round: v94. Fabric: site-z. Recorded: 2026-10-07T13:5xZ. **Reader:** `1.0.0_SA_CTO~Z`.

7 rows, graduated by `adjudications/ADJUDICATION_v94.md` C-S469.
- **OPEN, for the CTO (2):** Z-S362 (45 tracked files carry CR under eol=lf, repo-wide); Z-W281-S1 (60 of 167 holding
  rows have no key; a vendor identifier map is Andrew's word).
- **OPEN, for the issuer (5):** Z-S365, Z-S366, Z-W275-S1, Z-W279-S2, Z-W286-S2.

Advanced in place this slug: Z-W266-S1 to REMEDIATED (`REMEDIATION_v22.md`). Still OPEN from v22: Z-W266-S2, Z-W266-S3.

```json
[
  {
    "id": "AMGT_RESAPP-Z-S365",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The Bloomberg officer list is written under a slash-safe partition and read under a raw-slash one, so BP/ LN and NG/ LN each hold a good stored list that is never served. The plan still names both as needing a pull, so every later officers run spends two calls on objects the reader cannot see.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S365",
      "adjudications/ADJUDICATION_v94.md#AMGT_RESAPP-Z-C-S469",
      "this seat's read of the deployed function 2026-10-07 ~13:4xZ: management officers empty on 2 of 95 covered names"
    ],
    "remedy": "OPEN: the reader's key function uses the store's slash-safe partition, with a test on a slash name; it reaches the page at the next redeploy (a round-78 cell, CTO msg 30847). REMEDIATED when the deployed route serves an officer list on 95 of 95, or names the names that have none with a reason.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v94",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v94"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-S366",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "research_pulls.py reports TERMINAL_DOWN, exit 5 and 0 calls, when the interpreter it runs under has no blpapi. A missing library and a signed-out Terminal read identically, and the driver names no interpreter. A seat can wait for a sign-in that is not needed, or report the Terminal down.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S366",
      "adjudications/ADJUDICATION_v94.md#AMGT_RESAPP-Z-C-S469"
    ],
    "remedy": "OPEN: the driver gives an import failure its own exit word, apart from a failed health call; or the act's invocation names the interpreter as scheduled_daily_pull.cmd does. Until then the driver runs under the Python 3.11 that carries blpapi.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v94",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v94"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W275-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Name search reads a record's research folder name or its stored registration name. 138 of the 237 keyed records measured carry neither, so a typed company name (Apple for AAPL US) lists nothing; only the ticker root matches. The pool has since been re-minted to 243 records, and the count on that object is unread.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W275-S1",
      "adjudications/ADJUDICATION_v94.md#AMGT_RESAPP-Z-C-S469"
    ],
    "remedy": "OPEN: a name source for the records that carry none. AMGT_HARVST cell bc-1 joined each security's legal name from the collector's identity record today (028c66aa4e); whether name search can read that same record is the first thing to read. REMEDIATED when resolve returns AAPL US for 'apple' on the deployed route.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v94",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v94"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W279-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "lib/research/freshness/build_view.py reads every worker folder's rot_signal.json by a glob over the project's deliverables. The glob carries no worker serial, so cell ba-13's census did not count it and the cell left it. Production code still reads a worker's deliverables folder.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W279-S2",
      "adjudications/ADJUDICATION_v94.md#AMGT_RESAPP-Z-C-S469"
    ],
    "remedy": "OPEN: the rot signal gets a home the list module owns and the freshness view reads it there; the census that proves no production read of a worker folder counts globs as well as serials.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v94",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v94"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-W286-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The page states its inputs twice. The top block lists four (Bloomberg, Seeking Alpha, web search, the research pack) and agrees with /freshness. The Model tab's ledger lists six classes; its News line has no counterpart on /freshness, and its 'Filings: no source set up yet; has not run yet' sits on a page whose Thesis and Exec tabs cite the 10-K. On BA the ledger was not drawn in 0 of 3 runs of this walk.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W286-S2",
      "adjudications/ADJUDICATION_v94.md#AMGT_RESAPP-Z-C-S469",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_AMGTV1_FWD20_CLAUSE_COUNT_AND_FWD27_REGRADE_20261007.md (ground 3, the Filings line beside 10-K citations)"
    ],
    "remedy": "OPEN: one statement of inputs per name, served once, with the classes FWD-12's ACCEPT names; the Filings row reads what the page actually used (CTO msg 30868 routes it to the next RESAPP list). REMEDIATED when the Model ledger and the top block agree with each other and with /freshness on a walked name.",
    "owner": "2.0.0_SA_COO~Z",
    "round": "v94",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Z",
      "round": "v94"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-Z-S362",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "45 tracked files carry CR in their index blob while their eol attribute reads lf (infra/aws 32, data/smartx 13), out of 11,619 files with eol=lf and 59,555 tracked. Each can read MODIFIED in one worktree and CLEAN in another on identical bytes, as etf-classifications.tf did before cell ba-26 renormalised it.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S362",
      "adjudications/ADJUDICATION_v94.md#AMGT_RESAPP-Z-C-S469"
    ],
    "remedy": "OPEN: repo-wide and outside this project's paths, so the CTO routes it. One renormalising commit per owning lane, bytes equal after CR is stripped, nothing applied.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v94",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v94"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-Z-W281-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "60 of 167 holding rows in the 2026-10-06 union universe carry no key, and none carries a CUSIP, FIGI or SEDOL field. They are ADR and ordinary-share lines and cash or money-market lines. Joining them needs a vendor identifier map, which is not built.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W281-S1",
      "adjudications/ADJUDICATION_v94.md#AMGT_RESAPP-Z-C-S469"
    ],
    "remedy": "OPEN: a vendor identifier map is a vendor use, so it waits on Andrew's word through the CTO. The CTO's round-76 ruling already says it is not built speculatively; this row carries the count that ruling asked for.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v94",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v94"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
