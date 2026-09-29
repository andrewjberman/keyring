# AMGT_CORPUS ROUND 9 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~03:5xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND9_DRAIN_END_PACKET.md` @`f7c45f840e` (read to EOF, 5,505 B), msg 26423.
**L7 RE-MEASURED not adopted:** `k-1` reads `complete` on its LAST `<status>` tag; exactly 1 criterion carries
`judgment="true"` (`k-1` AC3). `k-2` is an issuer act, not an order. Matches the packet.

---

## 1. L8 -- THE SERVED ACTS, READ BY THIS SEAT

- **The dossier rewrite.** This seat read `read_dossier` for 8 names across 4 quote currencies. Every one serves
  `fields.cases.{upside, base, downside}` as the team's table columns by case: ADBE Price-2026 `416 / 233 / 143`,
  AZN `227.08 / 131.91 / 45.24`, ML `59.26 / 32.19 / 17.19`, ORA `45.09 / 19.24 / 5.78`, SAP `198.28 / 144.28 / 82.99`, TTE
  `165.63 / 85.46 / 21.77`, BP `12.39 / 7.40 / 1.25`, SHOP `179.88 / 127.70 / 26.48`. Round 8's failure (Downside = the whole
  table, Upside/Base ABSENT) is gone on every name read, and each is monotone Upside > Base > Downside.
- **The model-block re-derive.** `evidence/r9_k2_blocks_after.txt` reads `blocks keys 97 served 69 absent 28 nocases 0`. This
  seat's reads of 7 blocks agree with it. ML, ORA and SAP serve a Base. AZN, TTE and SHOP are ABSENT with the rule's reason
  "quote currency ... and reporting currency ... differ and this block converts nothing". ADBE is ABSENT at ratio 3.319,
  outside [0.33, 3.0].

### DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W1-S9` (ARMED: the case rule served a table dump) | **GRADUATED** | The served table is split by case on 8 of 8 names read (above) |
| `Z-S53` (the hold) and `Z-S54` (its lift) | **GRADUATED** | The rewrite ran under its pair, and the served shape is the remedy |
| `Z-W2-S10` (ARMED: 3 served Base cases lacked band fields, from a pre-g-1 vintage) | **GRADUATED** | All 97 blocks were re-minted under the one rule (`verify keys 97 match 97`). The three names (6861_JP, CAT_US, CSL_AU) now read ABSENT with the rule's own reason, per the CTO's ruling @`74e1eea534`. No served Base lacks its fields |
| `Z-S51` (the re-derive decision) | **GRADUATED** | Ran 97 of 97, verified against the rule's expected log |
| `Z-W1-S11`, `Z-W3-S6` | **GRADUATED** | `W1-S11`: the lone-symbol line reads as the prior value's unit (the £ and € above are carried). `W3-S6`: closed on the CTO's ruling |
| `Z-W1-S12` (6 of 34 tables unreadable) | **CARRIED** -> enrichment | 8035_JP, BZLFY_US, HEI_US, SNPS_US, TSM_US, V_US |
| `Z-S55` | **CARRIED** (the CTO's) | `cases-report` grades the underscore key form ABSENT instead of refusing |
| `Z-W2-S11`, `Z-S3`, `Z-S6`..`Z-S9` | **CARRIED**, unchanged | no landed remedy |

The packet's own **prediction miss** (93 puts, not 95: BP/_LN and NG/_LN have no model block) is stated on its bytes and costs
nothing served. Its lesson is the COO's: a pair's expected count is read per name from the join.

## 2. L9 -- `k-1` AC3: "does each served case read as that case, in the team's numbers, with its unit?"

**THAT CASE, IN THE TEAM'S NUMBERS: YES, 8 of 8 names read.** Each case is the team's own column, the ordering holds on every
name, and the multiples are the team's (ADBE `16.0x / 9.0x / 6.0x`, AZN `25.0x / 17.0x / 12.0x`).

**WITH ITS UNIT: YES AS THE TEAM WROTE IT, and that is where the finding is.** The served unit is the **symbol the team typed**,
which is not the listing's currency on 5 of the 8 names read:

| name | case unit | listing quote | team Base P26 vs px_last |
|---|---|---|---|
| AZN_LN | `£` | GBp (pence) | £131.91 vs 12,400 GBp = £124.00 -- **a 100x unit step** |
| ML_FP | `€` | EUR | €32.19 vs €33.50 -- agrees |
| ORA_FP | `$` | **EUR** | 19.24 vs €14.015 |
| SAP_GY | `$` | **EUR** | 144.28 vs €184.18 |
| TTE_FP | `$` | **EUR** | 85.46 vs €81.05 |
| SHOP_CN | `$` | **CAD** | 127.70 vs CAD 206.0 |
| ADBE_US | none | USD | 233 vs $238.93 -- agrees |

⛔ **`$` IS A SYMBOL, NOT A CURRENCY.** It cannot distinguish USD from CAD (SHOP), and on three EUR listings the team wrote `$`.
Whether those are real dollar figures (an ADR basis) or a template's default symbol **is not decidable from the served payload**.
The criterion as written is MET: the unit is the team's own, carried faithfully. **But any consumer that prints a case beside
the listing's Price tile (AMGT_RESAPP, DSGN_AMGTV1's FWD-4 "every money figure in the company's own currency") must not read
the case's symbol as the listing's currency.** Printed side by side, SHOP would show `$127.70` two inches from `CAD 206.00`.

**VERDICT: AC3 MET**, with the unit finding above routed to the consumers.

## 3. ⭐ A PLAUSIBILITY ORACLE NOW EXISTS -- THE TEAM'S OWN BASE BESIDE THE RULE'S

For the first time both Base cases are served, the team's written one and the rule's derived one, and they can be compared:

| name | team Base P26 | rule Base | agreement |
|---|---|---|---|
| ML_FP | €32.19 | €31.66 | 1.02 |
| ORA_FP | 19.24 | €20.49 | 0.94 |
| SAP_GY | 144.28 | €159.61 | 0.90 |
| **ADBE_US** | **$233** | **$793.10** (ABSENT at ratio 3.319) | **3.40** |

Three of four agree within 10%. **ADBE's rule Base is 3.4x the team's own Base.** The band caught it (3.319 > 3.0), so nothing
wrong is served. But this is the first time the rule's output can be checked against the analysts' own number instead of only
against price. This seat flagged the rule's adjusted-EPS x GAAP-P/E pairing at AMGT_RESAPP round 45 (ADJUDICATION_v55). A
team-vs-rule ratio census over the names that carry both is the direct test of that pairing, and it costs one join.

## 4. L10 PRECONDITION

1. **Every task order terminal** -- 1 of 1 (plus the issuer act, landed and verified). **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- `Z-W1-S9` and `Z-W2-S10` GRADUATED on this seat's reads; the rest CARRIED as in
   round 8. **MET**
3. **Every judgment criterion graded** -- 1 of 1, MET with the unit finding. **MET**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S12",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T03:55:00Z",
    "one_line": "L8/L9 round 9: k-1 AC3 MET -- the served cases are the team's columns by case on 8 of 8 names read, monotone on each. But the served unit is the symbol the team typed, not the listing's currency: '$' on three EUR listings and on a CAD listing (SHOP: $127.70 beside CAD 206), and '£' against a GBp listing (100x). Consumers must not read a case's symbol as the quote currency. And the team's Base now checks the rule's: ML, ORA and SAP agree within 10%, ADBE's rule Base is 3.4x the team's.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-CRPS-k-1 reads 'complete' on its LAST <status> tag; 1 criterion carries judgment=\"true\" (AC3). k-2 is an issuer act.",
        "SERVED CASES, this seat's read_dossier on 8 names: ADBE_US Price-2026 upside/base/downside 416/233/143; AZN_LN 227.08/131.91/45.24 unit U+00A3; ML_FP 59.26/32.19/17.19 unit U+20AC; ORA_FP 45.09/19.24/5.78 unit '$'; SAP_GY 198.28/144.28/82.99 '$'; TTE_FP 165.63/85.46/21.77 '$'; BP/_LN 12.39/7.40/1.25 '$'; SHOP_CN 179.88/127.70/26.48 '$'. Every name is split by case and monotone.",
        "MODEL BLOCKS, this seat's read_model_block: ML_FP px_last 33.5 base 31.66 (EUR/EUR); ORA_FP 14.015 base 20.49 (EUR/EUR); SAP_GY 184.18 base 159.61 (EUR/EUR); AZN_LN 12400 base ABSENT (GBp/USD, 'converts nothing'); TTE_FP 81.05 ABSENT (EUR/USD); SHOP_CN 206.0 ABSENT (CAD/USD); ADBE_US 238.93 ABSENT, 'base 793.10 USD / px_last 238.93 USD = 3.319, outside [0.33, 3.0]'. evidence/r9_k2_blocks_after.txt: 'blocks keys 97 served 69 absent 28 nocases 0'.",
        "GRADUATED: Z-W1-S9 (split by case on 8 of 8 read); Z-S53 and Z-S54 (the hold and its lift); Z-W2-S10 (all 97 blocks re-minted, verify 97 of 97; 6861_JP, CAT_US and CSL_AU now ABSENT with the rule's reason per the CTO's ruling @74e1eea534); Z-S51 (the re-derive ran and verified); Z-W1-S11; Z-W3-S6. CARRIED: Z-W1-S12 (6 unreadable tables), Z-S55, Z-W2-S11, Z-S3, Z-S6..Z-S9.",
        "UNIT vs LISTING, 5 of 8 differ: AZN '£' vs GBp (131.91 GBP vs 12400 GBp = 124.00 GBP); ORA_FP, SAP_GY and TTE_FP '$' vs EUR; SHOP_CN '$' vs CAD. ML_FP '€' vs EUR agrees; ADBE carries no symbol, USD listing. '$' cannot distinguish USD from CAD, and whether the EUR names' '$' is a real dollar basis or a template default is not decidable from the payload.",
        "TEAM BASE vs RULE BASE: ML 32.19 vs 31.66 (1.02); ORA 19.24 vs 20.49 (0.94); SAP 144.28 vs 159.61 (0.90); ADBE 233 vs 793.10 (3.40, the rule's base ABSENT by band)."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-W1-S9",
      "AMGT_CORPUS-Z-S53",
      "AMGT_CORPUS-Z-S54",
      "AMGT_CORPUS-Z-W2-S10",
      "AMGT_CORPUS-Z-S51",
      "AMGT_CORPUS-Z-W1-S11",
      "AMGT_CORPUS-Z-W3-S6"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @f7c45f840e asserts k-1 terminal and VALID, three served acts under signed pairs, cases served by case with their unit and page, 69 of 97 blocks served, and k-1 AC3 presented across four currencies.",
    "world_is": "True as read on 8 dossiers and 7 blocks. The served unit is the team's typed symbol, which differs from the listing's quote currency on 5 of 8 names, so a consumer must not treat it as the quote currency. The team's served Base now gives the rule a plausibility check: it agrees on three names and is 3.4x off on ADBE.",
    "notes": "FOR THE ROUND-9 ANALYSIS, two items. (1) THE CASE UNIT IS A SYMBOL. Carry it as served (the team's), but add a field naming it as the team's symbol, not a currency, so AMGT_RESAPP and DSGN_AMGTV1 (FWD-4) never print a case's '$' as the listing's currency; SHOP_CN would otherwise show $127.70 beside CAD 206.00. (2) A TEAM-vs-RULE BASE CENSUS. Over every name carrying both, the ratio of the rule's Base to the team's written Base is the direct test of the adjusted-EPS x GAAP-P/E pairing this seat flagged at AMGT_RESAPP round 45. ADBE at 3.4x is the first data point; it costs one join."
  }
]
```
