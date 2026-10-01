# AMGT_RESAPP ROUND 58 -- L8 COMPILE (the name fix redeploy; FWD-35 on the scheduled generation)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~11:4xZ
**Input:** `2.0.0_SA_COO~Z`'s `round58/DRAIN_END_PACKET.md` @`3373f73c27` (3,189 B, read to EOF), msg 27780.
**L7:** `TO-AMGT-ah-2` (the redeploy, WORLD, AE~A) complete per its proof `174cf144e9`; `ah-1`, `ah-3`, `ah-4` are landed issuer acts.

---

## 1. RE-READ BY THIS SEAT -- the DEPLOYED `opal-amgt-scoped-api`

- **Code:** CodeSha256 `g9H0TW2garLGS0zMoLmJgFQU8a/6ZJUGMwJaYFSkc/c=`, LastModified 2026-10-01T09:48:26Z, equal to the packet.
- **The name fix (`Z-S331`):** the monthly chatter route serves 95 rows and **0 serve `display_name == security_key`** (32 in
  v69). Names read as people would: "AIA GROUP LTD", "TOKYO ELECTRON LTD", "2317 TT" (the ticker fallback). `Z-S331` is satisfied
  on the deployed function.
- **FWD-35, the price ranking** (`/lead-panel/rankings/trending/price`): 200; **94 rows**, `as_of_date` 2026-09-30,
  `stale_trading_days` 0; every row carries `return_30d_pct` (94 of 94); top three AMD US +29.96, 992 HK +14.98, ASML NA +9.99.
  This equals the packet's scheduled-generation read (94 + 1 excluded = 95).
- **Valero, FWD-1's thread:** rank 5, `security_key` `VLO_US_Equity`, `name` "Valero Energy Corp", `identity_status` MEASURED. The
  demo's thread can open it from the bars.

## 2. WHAT THE PACKET DOES NOT SAY -- the price bars' identity

On the same deployed price ranking:
- **62 of 94 rows read `identity_status` UNRESOLVED with `security_key` null.** Six of the top ten have no key (AMD US, TSM US, ISRG
  US, PWR US, 8035 JP, 8766 JP).
- **59 of 94 rows read `name_state` ABSENT**; `name` is null on 58 (COST US among them: keyed, but unnamed).
- `ticker` is present on all 94.

A bar is labelled at least by its ticker. But **62 of the 94 bars, two thirds, have no key to open**. On the demo's price face, the
biggest movers are mostly bars that do not lead anywhere. DSGN FWD-22's ACCEPT ("the PM reads the biggest mover first") holds;
FWD-2 v0.6 ("identity ... read on each FWD-22 bar") does not, for 59 to 62 rows. The chatter name fix closed the bubbles. The price
side has the same class of gap, wider, and no row names it. This is RESAPP's served identity (CONTRACT section 0: every served field
is RESAPP's).

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S331` (32 of 95 raw-key names) | **GRADUATED** | 0 of 95 on the deployed function (section 1) |

No new rows from the issuer. This seat's section 2 is filed as the observation below for the round-58 analysis.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 1 of 1 (+ three landed direct acts). **MET**
2. **Every BLOCKING or ARMED row dispositioned:** none open. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

## 5. FOR THE ROUND-58 ANALYSIS (freeze 22:00Z)

The price ranking's identity: 62 of 94 rows unkeyed, 59 unnamed. Whether the price bars must open a name for Friday is the CTO's
call. If they must, it is the same shape as `Z-S331`'s fix, applied to the price generation's identity resolution, with "0 of 94
unkeyed among covered names" as its positive arm (62 today).

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S440",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T11:45:00Z",
    "one_line": "L8 round 58: the deployed function (g9H0TW2..., 09:48:26Z) serves 0 of 95 raw-key bubble names (Z-S331 satisfied) and FWD-35's price ranking at 94 rows, as_of 2026-09-30, stale 0; Valero keyed and named at rank 5; NOT IN THE PACKET: 62 of 94 price rows are identity UNRESOLVED with no security_key (6 of the top 10) and 59 have no name -- two thirds of the price bars cannot open a name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda get-function-configuration opal-amgt-scoped-api: CodeSha256 g9H0TW2garLGS0zMoLmJgFQU8a/6ZJUGMwJaYFSkc/c= LastModified 2026-10-01T09:48:26Z.",
        "Deployed /lead-panel/timeseries/collected/chatter: rows 95, display_name == security_key 0.",
        "Deployed /lead-panel/rankings/trending/price: 200, rows 94, as_of_date 2026-09-30, stale_trading_days 0, return_30d_pct on 94; security_key null 62, identity_status UNRESOLVED 62 / MEASURED 32; name_state ABSENT 59 / SERVED 35; ticker null 0; top-10 without key AMD US, TSM US, ISRG US, PWR US, 8035 JP, 8766 JP; VLO US rank 5 VLO_US_Equity 'Valero Energy Corp' MEASURED."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-S331"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @3373f73c27 asserts the name fix live (0 of 95 raw keys) and FWD-35 realized on the scheduled generation, all four Friday outcomes on the served plane.",
    "world_is": "True for the bubbles and FWD-35; the price ranking's identity is unresolved on 62 of 94 rows, which the packet does not report.",
    "notes": "FOR THE ROUND-58 ANALYSIS: decide whether the price bars must open a name for Friday; if so, the Z-S331-shaped fix on the price generation, positive arm 62 -> 0."
  }
]
```
