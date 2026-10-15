# ADVI_COTBKF -- rounds 86-88 remediations (dell1)

<sweep_watermark>2026-10-15T20:38:13Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-15T20:38:13Z. Graduated at ADJUDICATION_v63 (C-S5): 7 rows, owner and disarm owner 2.0.0_SA_COO~C1.

```json
[
  {
    "id": "ADVI_COTBKF-D1-W173-S3",
    "project": "ADVI_COTBKF",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "commonwealth_daily_valuation.py values account-days from a ticker-keyed Yahoo Close cache with no use_class filter, so a NOT_FOR_ACTIVE price can reach an active account's value.",
    "evidence": [
      "investigation row ADVI_COTBKF-D1-W173-S3",
      "adjudication row ADVI_COTBKF-D1-C-S5 (ADJUDICATION_v63.md)"
    ],
    "remedy": "Round 89's cell adds the use_class filter to that reader (the CTO's placement). Close when: this seat reads the reader's filter at the merged pin and a census over the cache's tickers prints 0 NOT_FOR_ACTIVE reaching an active account.",
    "owner": "2.0.0_SA_COO~C1",
    "round": "v88",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C1",
      "round": "v88"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~C1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_COTBKF-D1-S2",
    "project": "ADVI_COTBKF",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The standing statement for W173-S3: the nightly swap stops new Yahoo writes for V2-held names from the 2026-10-16 02:30Z run; the hand-run census still writes the cache.",
    "evidence": [
      "investigation row ADVI_COTBKF-D1-S2",
      "adjudication row ADVI_COTBKF-D1-C-S5 (ADJUDICATION_v63.md)"
    ],
    "remedy": "Closes with ADVI_COTBKF-D1-W173-S3.",
    "owner": "2.0.0_SA_COO~C1",
    "round": "v88",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C1",
      "round": "v88"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~C1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_COTBKF-D1-W170-S3",
    "project": "ADVI_COTBKF",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "test_cotbkf_no_account_ids.py needs the private account set (C:/dev/_cotbkf_private_evidence_20261009/, or COTBKF_ACCOUNT_SET); it is absent on dell1, so no dell1 commit of this project has been scanned for account ids.",
    "evidence": [
      "investigation row ADVI_COTBKF-D1-W170-S3",
      "adjudication row ADVI_COTBKF-D1-C-S5 (ADJUDICATION_v63.md)"
    ],
    "remedy": "The account set is placed on dell1 by its owner (never committed), or the scan runs where the set lives over every dell1 commit since the move. Close when: the scan runs with a printed denominator over the project's dell1 commits and reads 0.",
    "owner": "2.0.0_SA_COO~C1",
    "round": "v88",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C1",
      "round": "v88"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~C1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_COTBKF-D1-W175-S4",
    "project": "ADVI_COTBKF",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "One DETERMINISTIC and nine CANDIDATE R4 links point at accounts the reverse file holds as near matches awaiting a person.",
    "evidence": [
      "investigation row ADVI_COTBKF-D1-W175-S4",
      "adjudication row ADVI_COTBKF-D1-C-S5 (ADJUDICATION_v63.md)"
    ],
    "remedy": "No link on a near-match account is applied until a person rules on that account. Close when: the applied link set, read by this seat, holds no link on an account still awaiting a person.",
    "owner": "2.0.0_SA_COO~C1",
    "round": "v88",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C1",
      "round": "v88"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~C1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_COTBKF-D1-W176-S2",
    "project": "ADVI_COTBKF",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "document_index and the ledger write the Commonwealth account in two forms; an exact join drops the names of 504 accounts.",
    "evidence": [
      "investigation row ADVI_COTBKF-D1-W176-S2",
      "adjudication row ADVI_COTBKF-D1-C-S5 (ADJUDICATION_v63.md)"
    ],
    "remedy": "Every reader joins on normalize_account until one writer changes its form. Close when: the two writers carry one form, or the CTO rules normalize_account the standing join.",
    "owner": "2.0.0_SA_COO~C1",
    "round": "v88",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C1",
      "round": "v88"
    },
    "closed": false
  },
  {
    "id": "ADVI_COTBKF-D1-S1",
    "project": "ADVI_COTBKF",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The served return history values FTHSX and PFORX from Yahoo closes that MDPF_DEMQUE D1-S12 classes as wrong-symbol; no reader is released today.",
    "evidence": [
      "investigation row ADVI_COTBKF-D1-S1",
      "adjudication row ADVI_COTBKF-D1-C-S5 (ADJUDICATION_v63.md)"
    ],
    "remedy": "Before any reader of the return-history table is released, its correction list names FTHSX and PFORX (and RPIFX). Close when: that list is read by this seat.",
    "owner": "2.0.0_SA_COO~C1",
    "round": "v88",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C1",
      "round": "v88"
    },
    "closed": false
  },
  {
    "id": "ADVI_COTBKF-D1-C-S3",
    "project": "ADVI_COTBKF",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "cotbkf_crm_match_job.py scan_zip copies each CSV member's first line into the committed JOB_RECORD.json as header_columns.",
    "evidence": [
      "adjudication row ADVI_COTBKF-D1-C-S3 (ADJUDICATION_v62.md)",
      "adjudication row ADVI_COTBKF-D1-C-S5 (ADJUDICATION_v63.md)"
    ],
    "remedy": "Header names only, from a known schema or not at all (the CTO, msg 6219); a test whose fixture has no header row. The first cell of any re-run round. Close when: this seat reads the fix and its test at the merged pin, before the job reads a landed zip.",
    "owner": "2.0.0_SA_COO~C1",
    "round": "v88",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C1",
      "round": "v88"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~C1",
      "at": null
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
