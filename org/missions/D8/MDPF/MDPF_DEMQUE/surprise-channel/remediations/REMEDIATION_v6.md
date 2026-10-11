# MDPF_DEMQUE -- round 7 remediations

<sweep_watermark>2026-10-11T04:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T04:15:00Z. Graduated at ADJUDICATION_v7: 6 rows, all INERT.

```json
[
  {
    "id": "MDPF_DEMQUE-D1-W19-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "bbg_quote.py applies the non-trading-day history rule only when the history ceiling claim is measured AND the reserve claim is not. Measuring the reserve would silently return history backfills to the weekday rule, so they would draw on trading days.",
    "evidence": [
      "investigation row MDPF_DEMQUE-D1-W19-S1",
      "data/mdpf/scripts/demque/bbg_quote.py history branch of quote()"
    ],
    "remedy": "Rule whether the non-trading-day walk depends on claim states at all; if not, amend test_demque_bbg.py's weekday expectation and drop the condition. Close when: a history backfill quote with both ceiling and reserve claim measured still walks non-trading days only",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_DEMQUE-D1-S5",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The non-trading-day walk quotes every history request as a backfill, tier 1 included. This seat's run at 2260a375e1: MDPF_SECHIST-SHT8-TR-FIELD-CONFIRM-20261009 (tier 1) quoted for Monday 2026-10-12 reads allowance_today 0 and finish 2026-10-17, so a production history pull would be held five trading days, against C-RESERVE.",
    "evidence": [
      "investigation row MDPF_DEMQUE-D1-S5",
      "bbg_quote.py --quote requests/MDPF_SECHIST-SHT8-TR-FIELD-CONFIRM-20261009.json --today 2026-10-12 (3.0.0_SA_CVO)"
    ],
    "remedy": "Apply the non-trading-day walk to tier >= 2 only; tier 1 draws against the reserve on any day. Close when: a tier-1 history request quoted on a trading day reads a positive allowance_today and finishes that day",
    "owner": "2.0.0_SA_COO~Q1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Q1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Q1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_DEMQUE-D1-S6",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "bbg_ledger_upload.py reads etf_daily_pull.py's RET by ast.literal_eval, but RET is now list(HISTORY_FIELDS), so ETF-history ledger rows are written cells null, claim absent.",
    "evidence": [
      "investigation row MDPF_DEMQUE-D1-S6",
      "pytest data/mdpf/scripts/demque --ignore test_demque_land.py at 2260a375e1: 1 failed, 89 passed; [48, 64, 5, None, 2] != [48, 64, 5, 14, 2] (3.0.0_SA_CVO)"
    ],
    "remedy": "Resolve a Name-to-literal assignment before literal_eval, with a test on the current producer source. Close when: test_reads_record_lines_and_converts_rows_to_cells_per_mode passes and the next ETF-history ledger row carries cells with a claim",
    "owner": "2.0.0_SA_COO~Q1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Q1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Q1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_DEMQUE-D1-S7",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "land_cot.py cannot find its consumer's key literal since ADVI_COTBKF moved it onto _legacy_key(...), so test_demque_land.py raises SystemExit at collection and the whole demque pytest run ends in INTERNALERROR. The lander fails closed.",
    "evidence": [
      "investigation row MDPF_DEMQUE-D1-S7",
      "pytest data/mdpf/scripts/demque at 2260a375e1: INTERNALERROR, SystemExit (3.0.0_SA_CVO)"
    ],
    "remedy": "Read the consumer's key through the same lib/opal_naming legacy address the consumer uses, not a regex over its source. Close when: pytest data/mdpf/scripts/demque collects and runs with no INTERNALERROR",
    "owner": "2.0.0_SA_COO~Q1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Q1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Q1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_DEMQUE-D1-S8",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "32 of 141 served prices.parquet still carry the original 3 columns. This seat's S3 read: all 32 last-modified 2026-10-09 and all 109 seven-column files 2026-10-10, so the write upgrades a file only when the pacer re-draws its symbol. Andrew-direct v0.5 (C-PRICES) requires total return on every price table.",
    "evidence": [
      "investigation row MDPF_DEMQUE-D1-S8",
      "boto3 read of s3://opal-data-assets/yahoo/global/silver/price_history: 7-col 109 (2026-10-10), 3-col 32 (2026-10-09) (3.0.0_SA_CVO)"
    ],
    "remedy": "Re-write the 32 to the seven columns (from the stored rows, or by one paced re-draw), or show the pacer's window re-draws them. Close when: a served read reads 141 of 141 files with the seven columns",
    "owner": "2.0.0_SA_COO~Q1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Q1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Q1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_DEMQUE-D1-C-S17",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The TR request's frozen quote (finish 2026-10-13, weekday rule, frozen @70379bb41d) disagrees with the rule in force (finish 2026-10-17). The only drawer, a one-shot task, was removed after 2026-10-10, so 9,862 of 15,720 cells stay OPEN with nothing scheduled, and quote_vs_actual will read LATE after 2026-10-13.",
    "evidence": [
      "adjudication row MDPF_DEMQUE-D1-C-S17 (ADJUDICATION_v7)"
    ],
    "remedy": "Rule which quote binds a request quoted before DQ-t-22 (re-freeze under the rule in force, or keep the frozen one and grade it LATE). Cut a non-trading-day drawer for standing backfills, or close the request as a one-shot at 5,858 cells. Close when: the request reads ON_TIME or LATE against one ruled quote, and its remaining cells either have a scheduled drawer or the request is closed with its drawn count",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v8"
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
