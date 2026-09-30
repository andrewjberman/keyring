# AMGT_CORPUS ROUND 24 -- L8 COMPILE (no judgment criterion; one WORLD act; the r-1 acceptance)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~14:3xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND24_DRAIN_END_PACKET.md` @`97d992d947`, msg 27191. The packet was read to EOF (7,280 B).
**L7 re-measured:** `z-1`, `z-2` and `z-4` read `complete` on their LAST `<status>` tag. z-3 is the issuer's read of a scheduled
fire. There are 0 judgment criteria.

---

## 0. LEAD -- `Z-S69` IS A SERVED WRONG FACT, NOT AN INERT ONE

- **What is served.** The deployed `opal-amgt-scoped-api` `/api/scoped/amgt/security/TSM_US_Equity/thesis` (read by this seat) serves:
  - `CUR_MKT_CAP` value **2,339,877,750,964.95**, currency **TWD**, basis "reporting (EQY_FUND_CRNCY)";
  - `PX_LAST` 451.15 USD (quote, CRNCY);
  - `EQY_FUND_CRNCY` TWD and `CRNCY` USD.
- **Why it is wrong.** At USD 451 per ADR, TSM's market cap is of order **USD 2.3 trillion**, so the value is in USD. Labelled TWD,
  it reads as about TWD 2.3T, roughly a 30-fold understatement.
- **The payload contradicts itself.** Its own `CURR_ENTP_VAL` unit text says "reporting currency TWD differs from the **market-cap
  currency USD**".
- **Standing.** The packet carries `Z-S69` as INERT and names 79 header figures on 27 mixed-currency securities as reachable, with 1
  measured wrong. The label is served now, so this seat reads it as a live wrong statement.
- **The fix belongs to the round-24 analysis:** the per-field currency denomination of the three header fields on the 27 securities,
  then the label rule. Until then, the page should not print a currency on a mixed-currency name's `CUR_MKT_CAP`.

## 1. RE-READ BY THIS SEAT

- **Units.** Census over the newest `derived/model_block/<key>/<stamp>/model_block.json` for the 98 slash-free keys (12 slash-key
  objects are skipped; that is Z-S64):
  - 36,280 numeric figures, **UNRESOLVED 49**, POINTER 0;
  - by key: 6861_JP 26, 939_HK 10, BBSE3_BZ 10, BA_US 2, TSM_US 1.
  - That is exactly the packet's 602 -> 49 and its five-class split.
- **Signs.** 35,781 plain-signed figures, **0 contradicting their own value**. Signed figures rose from 35,678 at v26, by +103, which
  equals the packet's "103 UNRESOLVED -> POSITIVE".
- **The r-1 acceptance (z-3).** `Get-ScheduledTaskInfo amgt-induction-daily` reads LastRun **2026-09-30T13:00:00Z**, LastTaskResult
  **0**, NextRun 2026-10-01T13:00:00Z.
  - The scheduled fire is the acceptance, which this seat deferred at v25 section 1.
  - The issuer reads branch 1 (population 0; 0 calls; 0 puts). The CTO grades the FWD.

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W4-S8`, `Z-W4-S9` (z-4's own `stage_derive` test wrote `field_map.json`) | **GRADUATED** | closed by the stub; the packet reads `field_map.json` clean after the run |
| `Z-S69` (TSM `CUR_MKT_CAP` is USD, labelled TWD) | **CARRIED**, standing contested | section 0: it is served, not inert. The label rule is the round-25 cell. |
| `Z-W1-S19`, `Z-W1-S20` | **CARRIED**, ruled @`717cbb0a14` | the premise was a restatement miss; the zero rule stays |
| `Z-W4-S6`, `Z-W4-S7` | **CARRIED** -> RESAPP r53 cell 3 | preconditions and the gate of the slash-key move |
| `Z-W2-S16` | **CARRIED** | no TSM anchor in 13 sources |
| `Z-S64` | **CARRIED** | the move is RESAPP r53 cell 3; 40 objects per the full listing |

## 3. FOR THE ROUND-24 ANALYSIS

1. **`Z-S69` first (section 0).** It is the only item this round that leaves a wrong fact on the served state.
2. **The issuer's own defect 3 (two writers for about 6 minutes).**
   - A survivor check that matches the command line cannot see a stdin script.
   - The remedy the issuer names (named scripts, `python -u`, match on CreationDate) is the right one.
   - The writes were idempotent this time, so the output was correct by construction, not by the check.
3. The 49 remaining figures by class, then BP/NG after the move.
4. The dossier `/5` objects wait on RESAPP r53's redeploy.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 3 of 3, plus z-3 read. The ledger is CLOSED. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** the packet lists none ARMED or BLOCKING, and `Z-S69`'s standing is contested
   above. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S27",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T14:30:00Z",
    "one_line": "L8 round 24: served census re-read -- UNRESOLVED 49 (6861 26, 939 10, BBSE3 10, BA 2, TSM 1), 0 sign contradictions over 35,781; r-1 accepted (13:00Z fire, rc 0); LEAD: Z-S69 is served, not inert -- TSM CUR_MKT_CAP 2.34e12 (a USD value) is served labelled TWD, ~30x understated, and the same payload names USD as the market-cap currency.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-CRPS-z-1, z-2, z-4 read 'complete' on their LAST <status> tag.",
        "S3 opal-data-harvest derived/model_block/ newest per key, 98 keys: numeric 36280, UNRESOLVED 49 (6861_JP 26, 939_HK 10, BBSE3_BZ 10, BA_US 2, TSM_US 1), POINTER 0; plain-signed 35781, contradicting 0.",
        "Get-ScheduledTaskInfo amgt-induction-daily: LastRunTime 2026-09-30T13:00:00Z, LastTaskResult 0, NextRunTime 2026-10-01T13:00:00Z.",
        "Invoke /api/scoped/amgt/security/TSM_US_Equity/thesis: header_figures CUR_MKT_CAP value 2339877750964.9497 currency TWD basis 'reporting (EQY_FUND_CRNCY)'; PX_LAST 451.15 USD; CURR_ENTP_VAL unit text 'reporting currency TWD differs from the market-cap currency USD'."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-W4-S8",
      "AMGT_CORPUS-Z-W4-S9"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @97d992d947 asserts 602 -> 49 not-measured, 0 sign contradictions, the r-1 acceptance at 13:00Z, and Z-S69 as INERT and carried.",
    "world_is": "Units, signs and the r-1 fire are true as read. Z-S69 is a live served mislabel on TSM's market cap.",
    "notes": "FOR THE ROUND-24 ANALYSIS: Z-S69 first (per-field currency denomination, then the label rule; meanwhile print no currency on a mixed-currency CUR_MKT_CAP); a survivor check must match on CreationDate, not the command line."
  }
]
```
