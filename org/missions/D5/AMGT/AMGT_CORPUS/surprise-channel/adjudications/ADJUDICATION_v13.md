# AMGT_CORPUS ROUND 10 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~07:2xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND10_DRAIN_END_PACKET.md` @`bc50ea89cf` (read to EOF, 7,770 B), msg 26478.
**L7 RE-MEASURED not adopted:** `l-1`..`l-4` all `complete` on their LAST `<status>` tag; exactly 1 judgment criterion (`l-1` AC3).

---

## 1. L8 -- THE SERVED ACT, READ BY THIS SEAT, AND THE ROWS

`read_dossier` over **all 95 resolved keys: 95 of 95 at `amgt-corpus-dossier/3`, 0 read errors.** The `/3` rewrite landed on every
name, as the packet says.

| row | disposition | grounds |
|---|---|---|
| `Z-W1-S13` (ARMED: three tests pinned what the order changed) and its disarm `Z-S56` | **GRADUATED** | AMENDMENT 2 granted and ruled the test update; l-1 AC1 11 passed, corpus suite 409 passed |
| `Z-W1-S12` (the six unreadable tables) | **GRADUATED** | Served ABSENT with the specific reason (14 of 15 cells, position not recoverable); `l3_six.py` `absent_specific 6 absent_generic 0`. The worker's arithmetic places the blank at Base 2030E and is rightly not served |
| `Z-S55` (the CTO's: `cases-report` read the underscore key as ABSENT) | **GRADUATED** | l-4 refuses it (`planted_underscore rc 2`) and the 97-key regression through the refusal moves nothing |
| `Z-W3-S7` | **GRADUATED** | the corrected mechanism behind `Z-S55`, now remedied |
| `Z-W2-S12` (dollar team figures on EUR listings) | **CARRIED** -> analysis | not decidable from the payload |
| `Z-W2-S11`, `Z-S3`, `Z-S6`..`Z-S9` | **CARRIED**, unchanged | no landed remedy |

## 2. L9 -- `l-1` AC3: "does every served case's unit say only what the pack states, with a currency only where the pack and the listing agree on exactly one?"

This seat read the Base case of **all 95 dossiers**. **10** carry a symbol as written, and **1** sets a currency:

| name | `unit_as_written` | `currency` | `currency_basis` |
|---|---|---|---|
| ML_FP | `€` (U+20AC) | **EUR** | "symbol maps to one ISO code equal to the listing" |
| AZN_LN | `£` (U+00A3) | null | "symbol's currency differs from the listing" (GBp) |
| CPA_US, SPOT_US, UNVGY_US | `$` | null | "symbol is ambiguous across currencies" |
| ORA_FP, SAP_GY, TTE_FP, SHOP_CN, BP/_LN | `$` | null | (the same class) |

**VERDICT: MET.** Every served unit is the symbol the pack printed, labelled as written. The one currency set (ML, EUR) is the one
case where a single-ISO symbol equals the listing, and each null names its reason. The round-9 hazard is closed: `$127.70` on
SHOP_CN can no longer be read as CAD, and ORA's `$` can no longer be read as EUR. **Every null claims nothing.**

⚠ **Conservative on 3 names, not wrong:** CPA, SPOT and UNVGY print `$` on USD listings. Under "the pack and the listing agree on
exactly one", the intersection of `$`'s ISO set with the listing is {USD}, so a reader could set USD there. The implementation
requires the symbol ALONE to map to one code. That leaves 3 correct currencies unset, but it can never set a false one, which is
the direction this criterion exists to protect. Recorded, not held.

## 3. ⭐ THE TEAM-vs-RULE CENSUS CORROBORATES THIS SEAT'S OWN, BY A SECOND IMPLEMENTATION

l-2's `base_census`: `both 22`, **`median_ratio 0.6931` (team / rule)**, `beyond_2x 8`, **all 8 with the rule higher**. This
seat's independent join at AMGT_RESAPP round 46 (ADJUDICATION_v56, 20 names, rule / team) read **median 1.44**, and
1 / 0.6931 = **1.443**. Two implementations, different populations (20 vs 22) and a different year pairing (l-2 pairs on the
rule's FY1 year, which is 2027E on INTU, NKE and WDAY) agree on the median and the direction. **The finding is corroborated,
not a single instrument's artifact.** The 8 names are the same growth set (ADBE, CELH, MELI, NFLX, NOW, UBER, WDAY, ZTS). The
call on whether to anchor the Base to the team's multiple or the historical one is already routed as methodology.

## 4. L10 PRECONDITION

1. **Every task order terminal** -- 4 of 4. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- `Z-W1-S13` GRADUATED; the older set CARRIED as before. **MET**
3. **Every judgment criterion graded** -- 1 of 1, MET on all 95 served dossiers. **MET**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S13",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T07:25:00Z",
    "one_line": "L8/L9 round 10: l-1 AC3 MET on all 95 served dossiers (95 of 95 at /3) -- 10 carry the pack's symbol as written, only ML sets a currency (EUR, the one single-ISO symbol equal to its listing), and every null names its reason, so round 9's '$ read as the listing currency' hazard is closed. It is conservative on CPA, SPOT and UNVGY ($ on USD listings, left null), never wrong. l-2's census corroborates this seat's own join by a second implementation: team/rule median 0.6931 = 1/1.443, and all 8 names beyond 2x have the rule higher.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-CRPS-l-1..l-4 read 'complete' on their LAST <status> tag; judgment=\"true\" on l-1 AC3 only.",
        "SERVED, this seat's read_dossier over dossier._resolved_security_keys: 95 keys, method_version 'amgt-corpus-dossier/3' on 95 of 95, 0 errors.",
        "UNITS on the 95 Base cases: 10 symbol-bearing, 1 currency set. ML_FP unit_as_written U+20AC, currency 'EUR', currency_basis 'symbol maps to one ISO code equal to the listing'; AZN_LN U+00A3, null, \"symbol's currency differs from the listing\"; CPA_US '$', null, 'symbol is ambiguous across currencies'; likewise '$' null on BP/_LN, ORA_FP, SAP_GY, SHOP_CN, SPOT_US, TTE_FP, UNVGY_US.",
        "GRADUATED: Z-W1-S13 and Z-S56 (AMENDMENT 2 @b40840e09a; l-1 AC1 11 passed); Z-W1-S12 (six ABSENT with the specific 14-of-15-cells reason; l3 absent_specific 6 absent_generic 0); Z-S55 and Z-W3-S7 (l-4 refuses the underscore key, planted_underscore rc 2; 97-key regression unserved_vs_base 0 ratio_moved 0). CARRIED: Z-W2-S12, Z-W2-S11, Z-S3, Z-S6..Z-S9.",
        "CORROBORATION: l-2 base_census 'names 95 both 22 ... within_10pct 5 beyond_2x 8 median_ratio 0.6931' (team/rule), all 8 beyond 2x rule-higher; ADJUDICATION_v56 (this seat, 20 names, rule/team) median 1.44; 1/0.6931 = 1.443."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-W1-S13",
      "AMGT_CORPUS-Z-S56",
      "AMGT_CORPUS-Z-W1-S12",
      "AMGT_CORPUS-Z-S55",
      "AMGT_CORPUS-Z-W3-S7"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @bc50ea89cf asserts 4 orders terminal and VALID, the /3 rewrite landed 95 of 95 as predicted, unit_carried 10 currency_set 1, and a team-vs-rule census with all 8 beyond-2x names rule-higher.",
    "world_is": "True as read on all 95 served dossiers: every unit is the pack's as written with its basis, and only ML sets a currency. The census median is corroborated by this seat's independent round-46 join. The currency rule is conservative on three USD listings and never sets a false currency.",
    "notes": "FOR THE ROUND-10 ANALYSIS: (1) optional -- let a '$' on a USD listing set USD, since the symbol's ISO set intersected with the listing is exactly one; this is safe and would add 3 correct currencies; (2) the team-vs-rule gap is now corroborated by two implementations, so the methodology call it feeds no longer rests on one instrument."
  }
]
```
