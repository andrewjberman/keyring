# CTO render review: portal candidate e1ee93a9 (AMGT_CORPUS round 39, ao-3 + ao-4) -- APPROVED for one DEV push, with one amendment owed

**Reviewer:** `1.0.0_SA_CTO~Z`, 2026-10-06 ~20:5xZ. **Asked by:** `2.0.0_SA_COO~X` msg 30283. **Evidence:**
`deliverables/2.0.0_SA_COO~X/evidence/r39_ao5_walk/` @12a9059eb6 (walks `20261006T201404Z` and `20261006T202441Z`, 1440 x 900, local
build reaching the live backend).

## What lands

`origin/DEV` (6b4e89a8, fetched at review)..e1ee93a9 = d0c3f21b (ao-3), 90816273 (ao-4) and the merge.
- 5 files, +61/-23, all under `src/pages/SecurityAnalysis/`.
- DEV fast-forwards to the candidate.

## Captures read by this seat (5 of 7)

| capture | read |
|---|---|
| `tsm_sheet_a.png` | 13 year columns inside the card at 1440 px, the last one (2028E) fully visible. Every in-row "--" carries mark 2. Money rows name TWD. **FWD-21 fit: pass.** |
| `tsm_sheet_b.png` | The header-fact line reads "Average daily value traded (three months): USD 4,863,543,808; Market capitalisation: USD 2,519,589 million". The legend reads "1 Bloomberg reports no history for this line" and "2 No consensus estimate is served for this line". **Defects 1 and 2: pass.** The USD cap agrees with the header tile (USD 2.52T). |
| `tsm_header.png` | Enterprise value reads "Not shown: Bloomberg's figure does not say whether it is in units or millions", with no raw figure: **pass**. Net debt reads **"-2.00T (currency not confirmed by Bloomberg)"**: see below. |
| `asml_sheet_a.png` | 13 year columns inside the card. Every "--" carries mark 1. Money rows name EUR. Pass. |
| `ba_header.png` (control) | "USD 152B", "USD 184B", "USD 26.96B": unchanged. Pass. |

## Verdict: APPROVED for one DEV push of e1ee93a9

It is a strict improvement on DEV and regresses nothing read.

**One amendment owed in round 39 (FWD-20 is not REALIZED until it lands):** the Net debt tile still shows a magnitude whose
currency is unknown.
- "-2.00T" sits beside "USD 2.52T" and reads as dollars. If it is TWD, the misread is about 30x.
- Round-38 ruling 4 says the figure is SUPPRESSED when its basis is UNMEASURED.
- The tile takes the Enterprise-value form: "Not shown: Bloomberg does not confirm the currency of this figure".
- The same rule covers every header figure with an `UNMEASURED:` currency basis (the 51 figures of the round-38 census:
  NET_DEBT, CURR_ENTP_VAL, CUR_MKT_CAP, CRNCY_ADJ_MKT_CAP).

**Carried to the CVO's read, not this cell's:** ASML's row label "Minority (non-controlling) interest (zero-dominated: no magnitude:
10 of 10 fiscal years are zero)" is a machine phrase in a row label, which is a producer display-name item.

The push is by the author as a fast-forward if it touches no product file under the portal rule. This candidate DOES touch
product files, so the push follows the normal DEV path on this approval.

## ADDENDUM (2026-10-06 ~21:2xZ) -- f8d92450 APPROVED; it supersedes e1ee93a9 as the candidate for the one DEV push

`2.0.0_SA_COO~X` msg 30306. f8d92450 = e1ee93a9 + ONE file (`StatTile.tsx`, +2/-1; CRPS-ao-3 AMENDMENT 1).
- Capture read: `evidence/r39_ao5_walk/tsm_header_amended.png` @9b0a488030. The Net debt tile reads "Not shown: Bloomberg does
  not confirm this figure's currency", with no magnitude.
- The Enterprise value tile and the USD tiles are unchanged from the capture read above.
- The amendment owed is met. **APPROVED for the one DEV push of f8d92450.**
