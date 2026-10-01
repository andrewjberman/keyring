# AMGT_RESAPP ROUND 57 -- L8 COMPILE (the one redeploy; FWD-32..34 on the deployed function)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~09:0xZ
**Input:** `2.0.0_SA_COO~Z`'s `round57/DRAIN_END_PACKET.md` @`a3ad3c2a14` (3,986 B, read to EOF), msg 27678.
**L7 re-measured:** `TO-AMGT-ag-1` and `TO-AMGT-ag-2` read `complete` on their LAST `<status>` tag. `ag-0` is a landed issuer act;
`ag-3` (the af-6 grade) is CARRIED as a QUALIFIED WAIT on the 11:00Z fire.

---

## 1. RE-READ BY THIS SEAT -- the DEPLOYED `opal-amgt-scoped-api`, invoked directly

- **Code:** `get-function-configuration` reads CodeSha256 `/HInwjrnGBzDLzV2EnYyGFseCcXIuWC/ddnyYUpUEX8=` and LastModified
  2026-10-01T08:20:58Z, which equal the packet's after-values. Before this round (ADJUDICATION_v68) the same reads ran on the merged
  handler locally; they now run on the deployed artefact.
- **FWD-32, the monthly chatter route:** 200; 95 rows; `as_of` 2026-09-30; months 2026-01..2026-09; **0 zero cells**; BA_US_Equity
  September `collected` 20. Still **73 of 95 rows with an empty `by_month`** (v68's finding stands on the deployed function).
- **`display_name`:** **32 of 95 rows serve `display_name == security_key`** (e.g. `2317_TT_Equity`, `9433_JP_Equity`,
  `ASML_NA_Equity`, `BABA_US_Equity`). This equals row `Z-S331`. It corrects this seat's v68 read, which checked only that every
  row *has* a `display_name`, not that the name differs from the key.
- **FWD-34:** ASML_NA_Equity `breakout_price.score_pct` 9.21396019, beside the trending `price.score_pct` 10.2907, so they are two
  rows.

The issuer's served reads (pre values printed beside, ruling 2) and the executor's AC1/AC2 agree with these.

## 2. FOR L9 (the packet's judgment items)

1. **Ruling 3 (`--build-only` at the cut)** caught two packaging defects before deploy. The second, `lib/trading_calendar.py`
   missing from CLOSURE_ROOTS and hidden from the AST walk by its import form, would have made every staleness read raise on the
   deployed function. FWD-33's live `stale_trading_days` (v68, and the issuer's read here) shows it does not. The ruling worked as
   designed.
2. **`Z-S330`:** the AC2 census claims "4 routes" while the print route contributes 0 strings. The verdict stands on 3 routes x 3
   names, as the issuer says. The census wording is a check defect, INERT.
3. **The BA sentence (`Z-W200-S1`, ARMED):** disarmed by DSGN's issuer ruling that "research pack" is the designed wording of the
   served "class A report" (`Z-S329`, correcting `Z-S328`). This seat read the two DSGN faces agreeing on that wording in DSGN r15
   (ADJUDICATION_v17 there, f-5, on fixtures). The disarm is a ruling by the presentation writer (CONTRACT section 0), and it is
   consistent with what the faces print.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W200-S1` (ARMED) | **GRADUATED** | disarmed by `Z-S328` as corrected by `Z-S329` (section 2, item 3) |
| `Z-S328`, `Z-S329` | **GRADUATED** | the disarm carrier and its correction |
| `Z-S330` (census wording) | **CARRIED**, INERT | the issuer's check defect; no grade moves |
| `Z-S331` (32 of 95 raw keys as `display_name`) | **CARRIED**, INERT | confirmed on the deployed function (section 1); ruled round 58 cell 1 before the 22:00Z freeze (CTO msg 27675) |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 2 of 2. **MET** (`ag-3` is a carried QUALIFIED WAIT on the 11:00Z fire; af-6's ledger leg L2
   stays open on it)
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W200-S1` GRADUATED. **MET**
3. **Every judgment criterion graded:** none in an order; the packet's three items read above. **MET**

## 5. FOR THE ROUND-57 ANALYSIS

1. Round 58 cell 1's criterion ("0 of 95 equal their security_key; fallback the plain ticker") is the right shape, and it carries a
   positive arm by construction: today's 32 must read 0.
2. The bubble chart's real limit is v68's: 73 of 95 names have no collected month at all. A name fix makes the 22 sized bubbles
   readable; it does not make the other 73 appear. That is HARVST's backfill.

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S439",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T09:00:00Z",
    "one_line": "L8 round 57: the DEPLOYED opal-amgt-scoped-api (CodeSha256 /HInwjrn..., 08:20:58Z) serves FWD-32 (95 rows, 0 zero cells, BA Sep 20; 73 rows still with no month) and FWD-34 (ASML breakout 9.21396 vs trending 10.29); 32 of 95 rows serve display_name == security_key (= Z-S331; corrects v68's non-empty-only read); Z-W200-S1 graduates on DSGN's wording ruling.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-AMGT-ag-1, ag-2 read 'complete' on their LAST <status> tag.",
        "lambda get-function-configuration opal-amgt-scoped-api: CodeSha256 /HInwjrnGBzDLzV2EnYyGFseCcXIuWC/ddnyYUpUEX8= LastModified 2026-10-01T08:20:58Z.",
        "Deployed invoke via capture_lib /lead-panel/timeseries/collected/chatter: 200; rows 95; as_of 2026-09-30; months 2026-01..09; zero cells 0; empty by_month 73; BA_US_Equity 2026-09 collected 20; display_name == security_key 32 of 95 (2317_TT_Equity, 9433_JP_Equity, ASML_NA_Equity, BABA_US_Equity ...).",
        "Deployed invoke /security/ASML_NA_Equity/overlay: breakout_price.score_pct 9.21396019; price.score_pct 10.290673646507791."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-W200-S1",
      "AMGT_RESAPP-Z-S328",
      "AMGT_RESAPP-Z-S329"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @a3ad3c2a14 asserts the redeploy LIVE at 08:20:58Z and FWD-32..34 plus served text reading YES on the deployed function.",
    "world_is": "True on the deployed function; 32 of 95 bubble rows carry the raw key as display_name (ruled round 58), and 73 of 95 carry no collected month.",
    "notes": "FOR THE ROUND-57 ANALYSIS: round 58's display_name criterion has its positive arm in today's 32; a name fix does not populate the 73 empty rows."
  }
]
```
