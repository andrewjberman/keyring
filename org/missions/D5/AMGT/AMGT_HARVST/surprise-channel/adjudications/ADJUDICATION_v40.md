# AMGT_HARVST ROUND 30 -- L8 COMPILE (no judgment criterion; two WORLD acts)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~20:0xZ
**Input:** `2.0.0_SA_COO~H`'s `round30/ROUND30_DRAIN_END_PACKET.md` @`c592913bf7`, msg 27349. The packet was read to EOF (4,671 B).
**L7 re-measured:** `ac-1`, `ac-2` and `ac-3` read `complete` on their LAST `<status>` tag. There are 0 judgment criteria.

---

## 1. RE-READ BY THIS SEAT

- **`ac-3`, the paired `chatter_daily` rebuild:** `amgt/harvest/gold/chatter_daily/date=2026-09-30/part-20260930T181745Z.parquet` is
  **49,679 bytes and 52,143 rows**. All 5 expected rows carry `bbg` in `publishers_found_codes`:
  - 992_HK 2026-08-13 is found `[bbg, sa, wsj]`, covered `[bbg, wsj]`;
  - 992_HK 09-01 is found `[bbg]`;
  - AAPL, C and MU 08-13 are found with bbg, covered `[]`.
- **The deployed route now serves the found set.** `/api/scoped/amgt/security/992_HK_Equity/timeline` returns 08-13 found `[bbg, sa, wsj]`,
  covered `[bbg, wsj]`, with 3 articles, and 09-01 found `[bbg]`.
  - `C-HV-COVERED-VS-FOUND` (v0.4, signed by this seat) now works end to end on the served plane: sa is found and not covered, so it
    is never counted as searched.
  - This also carries the route half that DSGN n-3/m-4's found wording waited on.
- **`ac-2`, the sa probe** (`~85/ac2_probe.json`):
  - account read `/api/v3/account/1btfwdu/info` 200 `authorized: true`;
  - listing `/api/v3/symbols/lnvgy/news` 200, with 20 hits, all 20 dated (2026-01-13..09-15), 0 pre-floor;
  - `requests_made` 2, `sign_in_calls` 0, `refresh_calls` 0.
  - The token source is `saved_session_file` (`.runtime/.../sa.dpapi`), not Secrets Manager. That is the gap round-31 cell 1 closes,
    and it is consistent with this seat's v0.9 review note.
  - **The caveat is the packet's own (`Z-W85-S2`):** the account id is hard-coded, so "authorized" proves the token reads THAT account.
    It proves the account is active and paid (no 402), which is the question `Z-W37-S4` asked.

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W37-S4` (the sa 402: was the account lapsed?) | **GRADUATED** | CTO msg 27213 tied its standing to the probe, and the probe reads 200 `authorized: true` with a working listing (section 1). No persistent 402 exists, so the account is active, as Andrew said. |
| `Z-W84-S3` (BLOCKING: the q6 test log expects the forbidden re-check) | **GRADUATED** | ruled as `ac-1` A3, a test update; ac-1 is complete, and the collector suite reads 335 passed, 0 regressed |
| `Z-W85-S2` (sa `check()` hard-codes the account id `1btfwdu`) | **CARRIED** -> round-31 cell 1 | the token store; the check should read `{user_id}` from `contracts.json` |
| `Z-W84-S1`, `Z-W84-S2`, `Z-W85-S1`, `Z-W85-S3` | **CARRIED**, INERT or ruled | as the packet |

## 3. FOR THE ROUND-30 ANALYSIS

1. **sa is the one publisher with a measured working REST path on its stored token.** Collecting from sa on that path, under a pair,
   is available now if the CTO lists it. It is the first non-empty route toward a declared set (v0.8 needs a universe-scope job).
2. The cloud ruling's cells 1 and 4. `Z-W85-S2` belongs to cell 1.
3. The issuer's defects are named in the packet. The premise correction at the cut ("four kept bodies", really 2) is the fourth
   restated-count premise this seat has seen in two days, across CORPUS z-1 and HARVST.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 3 of 3. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W84-S3` GRADUATED; `Z-W37-S4` GRADUATED. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S50",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T20:00:00Z",
    "one_line": "L8 round 30: chatter_daily part-181745Z re-read (52,143 rows; bbg found on all 5 expected rows); the deployed /timeline now serves publishers_found_codes (992_HK 08-13 found [bbg,sa,wsj], covered [bbg,wsj]) -- covered-vs-found live end to end; the sa probe read 200 authorized with 2 requests and 0 sign-ins, so Z-W37-S4 graduates; Z-W84-S3 graduates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-HVST-ac-1, ac-2, ac-3 read 'complete' on their LAST <status> tag.",
        "S3 opal-data-harvest amgt/harvest/gold/chatter_daily/date=2026-09-30/part-20260930T181745Z.parquet: 49679 bytes, 52143 rows; 992_HK 2026-08-13 found ['bbg','sa','wsj'] covered ['bbg','wsj']; 09-01 found ['bbg']; AAPL/C/MU 08-13 found incl. bbg.",
        "Invoke /api/scoped/amgt/security/992_HK_Equity/timeline: 2026-08-13 found ['bbg','sa','wsj'] covered ['bbg','wsj'] articles 3; 2026-09-01 found ['bbg'] articles 1.",
        "~85/ac2_probe.json: account /api/v3/account/1btfwdu/info 200 authorized true; listing /api/v3/symbols/lnvgy/news 200 hits 20 dated 20 pre_floor 0; requests_made 2; sign_in_calls 0; token_source saved_session_file (sa.dpapi)."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W37-S4",
      "AMGT_HARVST-Z-W84-S3"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @c592913bf7 asserts 3/3 complete, the bbg articles on the page with found codes, sa working on its stored token, and Z-W37-S4 cleared.",
    "world_is": "True as read, on S3, the deployed route and the probe record. The sa token was read from the local saved-session file, not Secrets.",
    "notes": "FOR THE ROUND-30 ANALYSIS: sa collection on its working path under a pair is available now; Z-W85-S2's hard-coded account id goes with the token-store cell."
  }
]
```
