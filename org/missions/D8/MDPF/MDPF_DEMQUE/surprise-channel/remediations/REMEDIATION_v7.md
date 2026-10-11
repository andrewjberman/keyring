# MDPF_DEMQUE -- round 8 remediations (dell1)

<sweep_watermark>2026-10-11T15:35Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T15:35:00Z. Graduated at ADJUDICATION_v8: 4 rows, all INERT.

```json
[
  {
    "id": "MDPF_DEMQUE-D1-W22-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The D1-S8 re-draw builds each request from the file's own window, so the 18 rewritten files end 2026-06-23; every one of the 141 served price files ends 2026-06-22 or 2026-06-23, 76 trading days before the T-1 frontier 2026-10-09.",
    "evidence": [
      "investigation row MDPF_DEMQUE-D1-W22-S1",
      "adjudication rows MDPF_DEMQUE-D1-C-S19, C-S20"
    ],
    "remedy": "Rule whether the price_history store must reach the frontier (and on what cadence), or record that its window is fixed by design. Close when: the ruling is recorded and, if the frontier is required, a served read shows max(date) at the T-1 frontier on 141 of 141 files.",
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
    "id": "MDPF_DEMQUE-D1-S9",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "14 names (LCEYX, FTHSX, HLMEX, IWS, IWP, IWN, IWO, VSEIX, PFORX, RPIFX, VSS, VWO, MISIX, PIMSX) re-drew and were REJECTED:LOW_TRADE_AGREEMENT under lock.py's 90 pct floor (79.2 to 87.6 pct agreeing, two near 40 pct), so their three-column files stand; D1-S8 cannot close at 141 of 141.",
    "evidence": [
      "investigation row MDPF_DEMQUE-D1-S9",
      "adjudication row MDPF_DEMQUE-D1-C-S21",
      "data/mdpf/scripts/demque/lock.py:19, :85"
    ],
    "remedy": "Rule the lock's treatment of these names: keep the file, re-draw on a wider type band, or serve with a reason. Close when: dq_t28_stale.py reads stale 0 of 141, or each remaining name serves a stated reason the CTO ruled.",
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
    "id": "MDPF_DEMQUE-Z-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "bbg_quote.quote() prices the FULL request from today's fire days and never subtracts drawn cells, so a mid-draw re-quote of the TR request reads 2026-10-18 against the frozen 2026-10-17: a reader comparing the two sees a slip that is not one.",
    "evidence": [
      "investigation row MDPF_DEMQUE-Z-S2",
      "adjudication row MDPF_DEMQUE-D1-C-S25"
    ],
    "remedy": "Quote the remaining cells (quoted minus drawn) when re-quoting a partly drawn request, or label the re-quote as full-request. Close when: a re-quote at 2026-10-11 of the TR request reads the frozen finish or carries the label.",
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
    "id": "MDPF_DEMQUE-Z-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The TR quote counts 1,310 weekdays per security (15,720 cells) while the vendor returns 1,260 trading days (15,120 cells), so drawn < quoted forever: the request never closes, and from 2026-10-18 every non-trading-day fire appends a DRAWN line with 0 cells.",
    "evidence": [
      "investigation row MDPF_DEMQUE-Z-S3",
      "adjudication row MDPF_DEMQUE-D1-C-S25"
    ],
    "remedy": "Price a history request on trading days (lib/trading_calendar), or close a request when every security reaches its end date. Close when: the TR request reads ON_TIME or LATE against one ruled quote, and no fire after its completion appends a 0-cell DRAWN line.",
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
  }
]
```
