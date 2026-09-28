# Investor Reporting UI cleanup -- remediation status, 2026-09-28

**Register graded:** `docs/briefs/irpt-ui-cleanup-findings-20260927.json` (UIC-01..23, placed in DSGN_IRPTV1 PRD v0.18).
**Instrument:** `/ui-walk --deep`, stamp `20260928T133602Z`, the same three clients as the 09-27 baseline walk
(`20260927T203155Z`). The build was portal DEV `4b9df1e7` on localhost:5174. There were 187 screenshots and 0 blocked writes, and
the walker was disarmed at 13:54:31Z. Screenshots stay in the gitignored `tmp/ui-walk/<stamp>/shots/` and are cited here as `<stamp>#<shot number>`, and clients are named here
only by description.
**Author:** 4.0.0_SA_CRO, on Andrew's ask. This is a development read, not a CVO grade.

## Result: 3 of 23 MET

| MET | PARTIAL | NOT MET | NOT OBSERVED |
|---|---|---|---|
| 3 | 3 | 16 | 1 |

- **MET: UIC-01, 02 and 08.**
- **PARTIAL: UIC-04, 05 and 07.** In all three, the wording moved and the behaviour did not.
- **UIC-09 is NOT MET.** The worker graded it "already holds" and left it unchanged. The screen still shows "No
  source age yet" before any source exists, which is exactly what its acceptance line forbids.
- **The other 15 NOT MET items have no fix landed:**
  - 11 are on round-9 task orders that are all still pending with no commits: IV-e-70, 72, 74, 75 and 77 (UIC-22,
    on IV-e-75 too, is NOT OBSERVED);
  - UIC-03 has no task order;
  - UIC-06 is ~P's backend half, with no work recorded;
  - UIC-16's fix sits unmerged on ~M's branch, and UIC-15 waits on the R4 Holdings enable.
- **Two new defects:**
  - **NEW-01 (HIGH):** an invested 49F account shows YTD -100.00%, which is a wrong figure on the face.
  - **NEW-02:** the COT eleven-account pie no longer draws.

| id | status | owner | fix of record |
|---|---|---|---|
| UIC-01 | MET | COO~D | TO-IV-e-69 |
| UIC-02 | MET | COO~D | TO-IV-e-69 |
| UIC-03 | NOT MET | COO~D | NONE: no round-9 task order cites UIC-03 (it is in the write-set map only) |
| UIC-04 | PARTIAL | COO~D | TO-IV-e-69 |
| UIC-05 | PARTIAL | COO~D | TO-IV-e-69 |
| UIC-06 | NOT MET | COO~P | NONE recorded (IRPT_BCKEND backend half) |
| UIC-07 | PARTIAL | COO~D | TO-IV-e-69 |
| UIC-08 | MET | COO~D | TO-IV-e-69 |
| UIC-09 | NOT MET | COO~D | TO-IV-e-69 graded it 'already holds', no change |
| UIC-10 | NOT MET | COO~D | TO-IV-e-72 |
| UIC-11 | NOT MET | COO~D | TO-IV-e-70 |
| UIC-12 | NOT MET | COO~D | TO-IV-e-72 |
| UIC-13 | NOT MET | COO~D | TO-IV-e-72 |
| UIC-14 | NOT MET | COO~D | TO-IV-e-77 |
| UIC-15 | NOT MET | COO~M | Parked on the R4 Holdings enable (INF name fill, 09-28); not yet applied |
| UIC-16 | NOT MET | COO~M | 9ddc01dbc5 on branch irpt-m-uic16: NOT merged to CLOUD, NOT served |
| UIC-17 | NOT MET | COO~D | TO-IV-e-77 |
| UIC-18 | NOT MET | COO~D | TO-IV-e-75 |
| UIC-19 | NOT MET | COO~D | TO-IV-e-75 |
| UIC-20 | NOT MET | COO~D | TO-IV-e-75 |
| UIC-21 | NOT MET | COO~D | TO-IV-e-75 |
| UIC-22 | NOT OBSERVED | COO~D | TO-IV-e-75 |
| UIC-23 | NOT MET | COO~D | TO-IV-e-74 |

## The structured log

```json
{
  "schema_version": "1.0",
  "register": "docs/briefs/irpt-ui-cleanup-findings-20260927.json",
  "walk": {
    "stamp": "20260928T133602Z",
    "clients": 3,
    "mode": "--deep",
    "screenshots": 187,
    "guard_aborts": 0,
    "build": "portal DEV 4b9df1e7 working tree (tracked-clean), vite on localhost:5174",
    "baseline_walk": "20260927T203155Z (the same three clients, --deep)"
  },
  "measured_at": "2026-09-28T13:36Z-13:54Z",
  "denominator": 23,
  "counts": {
    "MET": 3,
    "NOT_MET": 16,
    "NOT_OBSERVED": 1,
    "PARTIAL": 3
  },
  "items": [
    {
      "id": "UIC-01",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-69 (portal 5136087d, drained 8df1ffef)",
      "status": "MET",
      "observed_20260928": "On the 49F three-account client's computed YTD report the three missing figures (vs benchmark, ending value, beginning value) now sit on ONE line under the period return; no 'not supplied' tiles.",
      "evidence_shots": [
        "20260928T133602Z#135"
      ],
      "note": "The line still says 'not supplied' three times. The acceptance line is met; the wording could be plainer."
    },
    {
      "id": "UIC-02",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-69",
      "status": "MET",
      "observed_20260928": "The per-day table is behind a closed 'Daily series (181 observations)' disclosure; the default view is the chart and the period figures.",
      "evidence_shots": [
        "20260928T133602Z#135"
      ],
      "note": ""
    },
    {
      "id": "UIC-03",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "NONE: no round-9 task order cites UIC-03 (it is in the write-set map only)",
      "status": "NOT_MET",
      "observed_20260928": "Report details still reads 'Partial -- Qualified answer -- not a complete report', 'PERFORMANCE_PARTIAL', 'TIME_WEIGHTED', 'OPAL_ENGINE', revision hashes and a tenant id.",
      "evidence_shots": [
        "20260928T133602Z#139"
      ],
      "note": ""
    },
    {
      "id": "UIC-04",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-69",
      "status": "PARTIAL",
      "observed_20260928": "The portfolio row now states once 'No benchmark supplied for this window. Spread not supplied for this window.' The account row still reads account 'not supplied' and ending value 'not supplied'.",
      "evidence_shots": [
        "20260928T133602Z#139"
      ],
      "note": "The worker's change collapses uncovered accounts that have NO fact. An account row that has a return but no name or value still shows 'not supplied' cells."
    },
    {
      "id": "UIC-05",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-69",
      "status": "PARTIAL",
      "observed_20260928": "The picker label now follows the selected period ('3Y unavailable', 'Since inception unavailable'). But with YTD computed at 5.93% on screen, the picker still reads 'YTD pending'.",
      "evidence_shots": [
        "20260928T133602Z#135",
        "20260928T133602Z#141"
      ],
      "note": "The acceptance half 'updates when it computes' is not met."
    },
    {
      "id": "UIC-06",
      "owner_seat": "2.0.0_SA_COO~P",
      "fix_of_record": "NONE recorded (IRPT_BCKEND backend half)",
      "status": "NOT_MET",
      "observed_20260928": "3Y and Since inception still answer 'Unavailable', with the raw 'UNSUPPORTED_OPERATION' and 'Contact support', for the 49F three-account client.",
      "evidence_shots": [
        "20260928T133602Z#141",
        "20260928T133602Z#142"
      ],
      "note": ""
    },
    {
      "id": "UIC-07",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-69",
      "status": "PARTIAL",
      "observed_20260928": "The face now reads 'Requested the account's first data point to 2026-09-22'. By the worker's own record, the request still carries the 1970-01-01 sentinel, and the answer is still UNSUPPORTED_OPERATION.",
      "evidence_shots": [
        "20260928T133602Z#142"
      ],
      "note": "Wording only. The window does not yet start at the account's first data point, so the acceptance behaviour is not met."
    },
    {
      "id": "UIC-08",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-69",
      "status": "MET",
      "observed_20260928": "The INF refusal now reads why and who: 'It becomes available once the Opal Capital service team adds this account to the covered set for this firm.' The code (OBJECT_NOT_COVERED) sits behind 'Details'.",
      "evidence_shots": [
        "20260928T133602Z#009"
      ],
      "note": ""
    },
    {
      "id": "UIC-09",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-69 graded it 'already holds', no change",
      "status": "NOT_MET",
      "observed_20260928": "The canvas still reads 'Loading  No source age yet' while loading, and 'Unavailable  No source age yet' on a refusal.",
      "evidence_shots": [
        "20260928T133602Z#134",
        "20260928T133602Z#141"
      ],
      "note": "The acceptance line says 'source age' never shows before a source exists. The worker read the existing wording as compliant; it is the defect."
    },
    {
      "id": "UIC-10",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-72 (pending, no commit)",
      "status": "NOT_MET",
      "observed_20260928": "The accounts pie labels still overlap for the INF four-account client. For the COT eleven-account client the pie now does not draw at all (see NEW-02).",
      "evidence_shots": [
        "20260928T133602Z#021",
        "20260928T133602Z#086"
      ],
      "note": ""
    },
    {
      "id": "UIC-11",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-70 (pending, no commit)",
      "status": "NOT_MET",
      "observed_20260928": "The slices and legend dots are still near-identical greys and navies (4 accounts INF, 11 COT).",
      "evidence_shots": [
        "20260928T133602Z#021",
        "20260928T133602Z#086"
      ],
      "note": ""
    },
    {
      "id": "UIC-12",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-72 (pending, no commit)",
      "status": "NOT_MET",
      "observed_20260928": "The negative account (-4.59% of the client) is still a row in the shares table, and the shares include it. There is no separate labelled line.",
      "evidence_shots": [
        "20260928T133602Z#086"
      ],
      "note": ""
    },
    {
      "id": "UIC-13",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-72 (pending, no commit)",
      "status": "NOT_MET",
      "observed_20260928": "Over what for the COT eleven-account client still shows 10 rows and clips the 11th.",
      "evidence_shots": [
        "20260928T133602Z#066"
      ],
      "note": ""
    },
    {
      "id": "UIC-14",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-77 (pending, no commit)",
      "status": "NOT_MET",
      "observed_20260928": "The Allocation, Securities map and Securities footers still read 'Source: holdings_snapshot.build_cot.'",
      "evidence_shots": [
        "20260928T133602Z#091"
      ],
      "note": ""
    },
    {
      "id": "UIC-15",
      "owner_seat": "2.0.0_SA_COO~M",
      "fix_of_record": "Parked on the R4 Holdings enable (INF name fill, 09-28); not yet applied",
      "status": "NOT_MET",
      "observed_20260928": "The INF models dialog still lists bare tickers (FDRXX, CIVIX, VO, VB ...) with no names.",
      "evidence_shots": [
        "20260928T133602Z#038"
      ],
      "note": ""
    },
    {
      "id": "UIC-16",
      "owner_seat": "2.0.0_SA_COO~M",
      "fix_of_record": "9ddc01dbc5 on branch irpt-m-uic16: NOT merged to CLOUD, NOT served",
      "status": "NOT_MET",
      "observed_20260928": "INF account labels still read '****9749 / INDIVIDUAL RETIREMENT AC' in the picker, the scope panel and the pie.",
      "evidence_shots": [
        "20260928T133602Z#009",
        "20260928T133602Z#021"
      ],
      "note": ""
    },
    {
      "id": "UIC-17",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-77 (pending, no commit)",
      "status": "NOT_MET",
      "observed_20260928": "'About this scope' still shows 'SCOPE AS OF: unknown' for all three clients.",
      "evidence_shots": [
        "20260928T133602Z#134",
        "20260928T133602Z#009",
        "20260928T133602Z#066"
      ],
      "note": ""
    },
    {
      "id": "UIC-18",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-75 (pending, no commit)",
      "status": "NOT_MET",
      "observed_20260928": "Pressing Multi-Comp still leaves 'Variant: Overview (0 comparisons)' and shows 'Multi-Comp does not match 0 comparison(s); Overview does.'",
      "evidence_shots": [
        "20260928T133602Z#185"
      ],
      "note": ""
    },
    {
      "id": "UIC-19",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-75 (pending, no commit)",
      "status": "NOT_MET",
      "observed_20260928": "The default report title still names one account of three: '<client> <one account> -- Overview'.",
      "evidence_shots": [
        "20260928T133602Z#182"
      ],
      "note": ""
    },
    {
      "id": "UIC-20",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-75 (pending, no commit)",
      "status": "NOT_MET",
      "observed_20260928": "'Enter the report recipient (up to 200 characters).' still shows as a red error on first load, before any input.",
      "evidence_shots": [
        "20260928T133602Z#181",
        "20260928T133602Z#066"
      ],
      "note": ""
    },
    {
      "id": "UIC-21",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-75 (pending, no commit)",
      "status": "NOT_MET",
      "observed_20260928": "The comparison input placeholder is still cut: 'Opal model or ETF symbo'.",
      "evidence_shots": [
        "20260928T133602Z#182"
      ],
      "note": ""
    },
    {
      "id": "UIC-22",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-75 (pending, no commit)",
      "status": "NOT_OBSERVED",
      "observed_20260928": "On this walk the snapshot had already answered ('as of 2026-09-22 Ready') on the first Analysis screenshot, so the loading moment was not captured.",
      "evidence_shots": [
        "20260928T133602Z#181"
      ],
      "note": "No fix has landed, so the defect is presumed open. A walk cannot grade a transient state it did not catch."
    },
    {
      "id": "UIC-23",
      "owner_seat": "2.0.0_SA_COO~D",
      "fix_of_record": "TO-IV-e-74 (pending, no commit)",
      "status": "NOT_MET",
      "observed_20260928": "For the COT eleven-account client, 'Your analysis requests' still lists raw ids ('Open REQ-2119def... revision 1 Checking status...'), not client names.",
      "evidence_shots": [
        "20260928T133602Z#066"
      ],
      "note": ""
    }
  ],
  "new_findings": [
    {
      "id": "NEW-01",
      "severity": "HIGH",
      "surface": "performance / period return",
      "owner_seat": "2.0.0_SA_COO~P (IRPT_BCKEND, opal-gips-engine)",
      "observed_20260928": "The smallest of the 49F three-account client's three accounts answers YTD -100.00%. The cumulative line falls from 0.00% on 2026-04-15 to -100.00% on 2026-04-16 and stays there to 2026-09-22. The account is invested (Opal Long Term / Ultra Long Term on Holdings).",
      "evidence_shots": [
        "20260928T133602Z#138",
        "20260928T133602Z#139"
      ],
      "cause": {
        "claim": "inferred",
        "evidence": "The series starts the day the account first has data (04-15); a first-day flow treated as a full withdrawal would give this shape. Not measured."
      },
      "acceptance": "An account with positive holdings never answers -100%; a first-day funding flow is not a return."
    },
    {
      "id": "NEW-02",
      "severity": "MEDIUM",
      "surface": "holdings / accounts pie",
      "owner_seat": "2.0.0_SA_COO~D (TO-IV-e-72 scope)",
      "observed_20260928": "For the COT eleven-account client, the 'All holdings' pie draws nothing: 0% non-white pixels in the pie box, against 38% for the same client and step on 2026-09-27 and 72% for the INF four-account client's pie this walk. The legend and table still render.",
      "evidence_shots": [
        "20260928T133602Z#086",
        "20260927T203155Z#086"
      ],
      "cause": {
        "claim": "inferred",
        "evidence": "No portal commit since the 09-27 walk touches the pie (IV-e-72 is pending). The negative account may now stop the pie from drawing. Not measured."
      },
      "acceptance": "The accounts pie draws for every client, including one with a negative account (UIC-12)."
    }
  ]
}
```

## What this does not claim

- A walk samples paths. UIC-22 is a transient loading state, and this walk did not catch it.
- For UIC-07, "the request still carries 1970-01-01" is the worker's own record. This walk read the face, not the
  request body (the network log holds no bodies).
- The causes of NEW-01 and NEW-02 are inferred, not measured.
