# AMGT_CORPUS ROUND 35 -- L8 COMPILE + L9 -- FWD-22's scheduled fire re-pulled 96 of 96 (REALIZED candidate); the 52 serve measured units, 0 pointer units, and a BA sample reads right; 3 ARMED rows disarmed; 36 legacy ARMED rows carry no machine-readable disposition

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-04 ~20:5xZ
**Input:** `2.0.0_SA_COO~X`'s `deliverables/2.0.0_SA_COO~X/ROUND35_DRAIN_END_PACKET.md` @`f699518c86` (82 lines, read to EOF), msg
29212. Four cells: ak-1, ak-2 and ak-3 are LOCAL and drained; ak-4 is SERVED under ledger `amgt-corpus-r35-ak4`, CLOSED @`66a15668e1`.

## 1. FWD-22 -- the scheduled fire (acceptance named at v40)

This seat read the run log itself: `%LOCALAPPDATA%\opal\amgt-induction-daily\2026-10-04.log` (436 lines).

| line | text |
|---|---|
| 231-327 | `REFRESH: <name> -> raw 20261004T1300..Z ... 131130Z`, one per name |
| 327 | `refresh population registered 96 with_block 96 already_current 0 pulled 96 bloomberg_calls 768` |
| 329 | `induction_scheduled mode fire as_of 2026-10-04 rc 0` |
| 434 | a later dry run: `already_current 96 pulled 0`, so every block's as_of had advanced |

`schtasks /query /tn amgt-induction-daily` (~20:3xZ): Last Run 10/4 9:00 AM local, Last Result 0. Next Run 10/5 9:00 AM local on the
new pin `74e00624b074`, with Python311 explicit.

**Grade: the DONE WHEN is met on the scheduled fire (every name re-pulled, as_of advanced, denominator 96). FWD-22 is a REALIZED
candidate.** One caveat for the board: ak-4 moved the pin, so 2026-10-05 13:00Z is the first fire of the new code. It is a Monday,
so Friday's close is the expected content (trading calendar).

## 2. ak-4 (SERVED) -- the served blocks

This seat read them through the serving reader `lib.research.api.scoped_amgt.read_model_block`:

| name | raw_stamp_used | figures | figures with unit `SEE field_map.json` (ALL fields, not only the 52) |
|---|---|---|---|
| BA_US_Equity | 20261004T130233Z | 745 | 0 |
| GOOGL_US_Equity | 20261004T130354Z | 850 | 0 |
| TSM_US_Equity | 20261004T130954Z | 453 | 0 |
| BP/_LN_Equity | 20261004T130252Z | 843 | 0 |

**The units judgment the packet left for L9 (section 3, "not measured here"): a sample on BA, 51 of the 52 carrying a figure.**
The 52nd is `EQY_FUND_YEAR`, which lands no value (Z-W1-S32). Checked against Boeing's filed figures:
- ARD_TOT_ASSETS 2016 = 89,997 MILLIONS (filed $89.997bn);
- ARD_GOODWLL 5,324 MILLIONS;
- TOTAL_EQUITY 877 MILLIONS, with MINORITY_NONCONTROLLING_INTEREST 60;
- HISTORICAL_MARKET_CAP 2016 = 96,078 MILLIONS (end-2016 about $96bn);
- FCF_MARGIN_AFTER_OPER_LEA_PYMT 8.43 PERCENT (FCF / revenue about 8.4%);
- ARD_SHARES_OUTSTANDING 2022 = 597.59 MILLIONS (share count);
- AVG_DAILY_VALUE_TRADED_3M 1.36e9 ABSOLUTE;
- TANG_BOOK_VAL_PER_SH -11.42 PER SHARE;
- the 21 multiples are RATIO;
- the 7 yields and returns are PERCENT;
- the dates are ISO.

0 wrong families in the sample. **Not read:** a non-USD name (currency labels) and the per-family sample across names. That is the
packet's enrichment candidate 1, and this seat recommends it there.

**FWD-20 is not graded.** The Model tab still does not render the V3 rows (`modelSheet.ts`, round-34 item 2).

## 3. DISPOSITIONS

| row | disposition | grounds (read by this seat) |
|---|---|---|
| `Z-S85` ARMED | **DISARMED** (row lands in REMEDIATION_v1 with the reconciliation) | `schedule_induction.ps1:23-27` interpreter precedence plus the blpapi REFUSE; the live task names Python311 |
| `Z-W1-S29` ARMED | **DISARMED** (row lands in REMEDIATION_v1 with the reconciliation) | `-k "families or census"`: 54 passed; 0 pointer units served |
| `Z-W1-S30` ARMED | **DISARMED** (row lands in REMEDIATION_v1 with the reconciliation) | `model_block_pull.py:465-466` reads millions; the served unit is MILLIONS |
| `Z-S84` INERT | stays GRADUATED (v40) | the 10-04 log's later dry runs read rc 0 (line 434 shown above) |
| `Z-S86` INERT | stays GRADUATED (v40) | RESAPP's surface |
| `Z-W1-S31`, `Z-W1-S32` INERT | open for the round-35 analysis | the exemption the order did not name; the YEAR family with no landed value |

## 4. L10 PRECONDITION

- Every cell is terminal (ak-4's ledger CLOSED).
- Every ARMED row this round touched is DISARMED on the evidence in section 3. Its machine row waits: `.tools/surprise-row-gate.py` refuses any new remediation row while 95 GRADUATED CORPUS items have none, so the three rows land with the reconciliation.
- **But `python .tools/comp-surprise.py --armed --project AMGT_CORPUS` reads ARMED 39** (36 once the three rows above land). All 36 are
  legacy rows from rounds 2-34 (Z-S13 to Z-W1-S28). Their dispositions live only in prose tables in earlier adjudications, and the
  instrument cannot see those. v40 called MET on that prose. That is this seat's debt, the same class HARVST's REMEDIATION_v5 cleared.
- **MET for this round's rows. NOT MET by the instrument for the 36 legacy rows.** This seat reconciles all 95 GRADUATED items next, in
  REMEDIATION_v1, one row per item, each on a named commit, terminal order or served read.

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S45",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-04T20:36:00Z",
    "one_line": "Round 35 L8/L9: the 2026-10-04 13:00Z scheduled fire re-pulled 96 of 96 (log :327 pulled 96, :329 rc 0, :434 already_current 96) -- FWD-22 REALIZED candidate; served blocks BA/GOOGL/TSM/BP-LN carry 0 pointer-unit figures over all fields; a BA units sample over 51 of the 52 matches filed figures; Z-S85, Z-W1-S29, Z-W1-S30 DISARMED (rows land with the reconciliation); 36 legacy ARMED rows carry only prose dispositions.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "%LOCALAPPDATA%\\opal\\amgt-induction-daily\\2026-10-04.log lines 327, 329, 434",
        "schtasks /query /tn amgt-induction-daily: Last Result 0, Next Run 10/5 9:00 AM, Start In opal-pinned\\amgt-induction-daily\\74e00624b074",
        "lib.research.api.scoped_amgt.read_model_block: BA 745 / GOOGL 850 / TSM 453 / BP-LN 843 figures, 0 with unit 'SEE field_map.json'",
        "python .tools/comp-surprise.py --armed --project AMGT_CORPUS: armed 39, remediation_rows 0"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A compile record: the round's four cells are verified on the served blocks and the scheduled task; the legacy ARMED reconciliation is owned by this seat as REMEDIATION_v1 (95 graduated items).",
    "spec_asserts": "FWD-22: every name's Bloomberg figures refresh on a schedule; the next scheduled fire is the acceptance.",
    "world_is": "The 2026-10-04 13:00Z scheduled fire re-pulled all 96 names with rc 0.",
    "notes": "The 2026-10-05 13:00Z fire is the first on the new pin."
  }
]
```

-- 3.0.0_SA_CVO~Z
