# FWD-15 UNPLACED-KEY entries: key forms or a manual-entry route -- PROPOSAL (MDPF_SECCLASS TO-SC-e70, round 12 SC-e-70)

**Author:** `0.9.0_WK_MDPF_SECCLASS~60`, 2026-10-08. **Proposal only: no code, no row, no table write.** Every choice below is the CTO's.
Census: `UNPLACED_KEY_CENSUS_20261008.json` (script `R12_CHECKS/unplaced_key_census.py`), read from the three
`R12_CHECKS/e49_replan/FWD15_AI_PLAN_<firm>_20261007.json` files.

## Headline

`UNPLACED-CENSUS ok=True total=99 firms=3 patterns=13 usd=77296036.56` (signed sum; absolute sum 77,270,936.41 is not comparable because
the census sums signed amounts, which include two negatives: `CXMANUAL_MORTGAGE` -213,597.89 and `FID:CASH` -32,350.58).
Firms: cottonwood 87 entries USD 76,843,740.63 (99.41%), 49financial 3 entries USD 406,618.54 (0.53%), inflection 9 entries
USD 45,677.39 (0.06%). Shares below are of the USD 77,296,036.56 total.

**The contract's `identifier_namespace` (org/standards/MDPF_SECCLASS_CONTRACT.json, v0.8.0) holds four values, `["TICKER", "CUSIP", "BLOOMBERG", "NAME"]`.**
Its NAME definition, quoted: "the row's ticker attribute holds the name-keyed form for a security with NEITHER a ticker NOR a CUSIP
(contract 0.5.0, PRD ADDENDUM v0.7). PROPOSED KEY FORM: NAME::<slug>` where slug = the security's name upper-cased, every run of
characters outside `A-Z`, `0-9` and `-` replaced by ONE space, trimmed, cut to the first 80 characters ...; an empty slug yields no key
and the write is refused." So a NAME form already exists for every entry that has a name; the question is whether a name-keyed row is
the right object, not whether a form exists.

**Proposed split (shares of the 99-entry total):**
- Manual-entry route (a human supplies the class per key; no key form helps): `<digits>_<word>` 64.01%, `CXMANUAL_*` 25.16%,
  `<10 digits>` 2.51% = **91.67%** (28 entries; 7 + 19 + 2).
- Existing form, no contract change: `NAME::<slug>` for `BD<6 alnum>` 5.76%, `BA- FIDELITY.*` 1.28%, `BA- <other>` 0.18%, `CGF-<alnum>` 0.49%,
  `<8 alnum> other` 0.03% = **7.74%** (59 entries); `CUSIP:<9>` for the 2 `<ticker>+<suffix>` 0.01% (2 entries). Total existing form **7.76%**.
- Not a key question (separate decision): `dotted ticker` 0.51% (1 entry), `cash pseudo-key` 0.06% (2), `<ticker>-OLD<mmddyyyy>` 0.00% (5),
  `<ticker><space><class letter>` 0.00% (2) = **0.57%** (10 entries).
Check: 91.67 + 7.76 + 0.57 = 100.00; 28 + 61 + 10 = 99.

Meaning attributed to a prefix below (for example what `4175` or `BD` stands for) is inferred from the key and name shape, not measured; no source
defining those prefixes was read.

## Per pattern

| firm | pattern | n | USD | share | examples (key / name / USD) |
|---|---|---|---|---|---|
| cottonwood | `<digits>_<word>` | 7 | 49,474,952.11 | 64.01% | `4175_VOYA` Voya 25,973,104.32; `4175_CCA_EIGER_III_OPP` CCA Eiger III Opportunity LP Capital Values 6,150,000.00; `4175_CCA_SAXUM_OPP` 4,778,309.87; `4175_CCA_FC_HOUSTON_OPP` 4,750,000.00; `4175_CCA_EIGER_OPP` 4,500,000.00 |
| cottonwood | `CXMANUAL_*` | 19 | 19,445,877.35 | 25.16% | `CXMANUAL_HOME` Investor Manual Asset - Home 8,378,664.00; `CXMANUAL_LIMITEDLIABILITYCOMPANY` 4,125,000.00; `CXMANUAL_TRUSTACCOUNTS` 3,173,684.09; `CXMANUAL_PRIMARYRESIDENCE` 900,000.00; `CXMANUAL_INSURANCE` 568,016.86 |
| cottonwood | `BD<6 alnum>` (key = cusip column) | 43 | 4,451,531.16 | 5.76% | `BD4HOKI9` 3208 Voya Index Solution 2050 Portfolio Z 652,327.56; `BDGG24WF` EXTENDED MARKET UNITS 542,463.65; `BDN6L2T7` BALANCED FUND UNITS 418,775.91; `BD3QUUT3` EQUITY UNITS 306,815.91; `BDVROD1V` 3665 MFS Growth Fund R6 296,161.55 |
| cottonwood | `<10 digits>` | 2 | 1,937,750.00 | 2.51% | `9102026128` CCA STNL Income Opportunity LP 1,287,750.00; `9102024190` Maranello-Plano LP 650,000.00 |
| cottonwood | `BA- FIDELITY.*` | 11 | 987,586.90 | 1.28% | `BA- FIDELITY.4005` FID GR CO POOL CL 3 399,464.90; `BA- FIDELITY.6671` FID FRDM 2040 CP H 144,690.30; `BA- FIDELITY.3715` FID LOW PR STK POOL 135,879.50; `BA- FIDELITY.O89H` RETIREMENT DATE 2030 112,661.61; `BA- FIDELITY.PHXA` VG INST 500 IDX TR A 46,733.07 |
| cottonwood | `CGF-<alnum>` | 2 | 381,889.58 | 0.49% | `CGF-40H99E950` GROWTH 290,790.44; `CGF-40H99E885` CONSERVATIVE INCOME 91,099.14 |
| cottonwood | `BA- <other>` | 2 | 138,985.87 | 0.18% | `BA- INSDBNK09000` Insured Bank Deposit 138,960.97; `BA- MONEY MARKET BALANCE` MONEY MARKET 24.90 |
| cottonwood | `<8 alnum> other` (key = cusip column) | 1 | 25,167.66 | 0.03% | `07399D34` BEACON PARTNERS FUNDII LP 25,167.66 |
| 49financial | `dotted ticker` | 1 | 395,155.54 | 0.51% | `QXO.PR.B` QXO, Inc. Depositary Shares ... 5.50% Series B Mandatory Convertible Preferred 395,155.54 |
| 49financial | `<ticker>+<suffix>` | 2 | 11,463.00 | 0.01% | `VNO+L` (cusip 929042844) 8,425.00; `MS+O` (cusip 61762V861) 3,038.00 |
| inflection | `cash pseudo-key` | 2 | 45,677.39 (abs 110,378.55) | 0.06% | `CUSTODIAL_CASH` Custodial Cash 78,027.97; `FID:CASH` Fidelity Cash Fund** -32,350.58 |
| inflection | `<ticker>-OLD<mmddyyyy>` | 5 | 0.00 | 0.00% | `AZN-OLD02022026`, `OGI-OLD04032025`, `TEVA-OLD09152026`, `THMR-OLD04152026`, `TTE-OLD12092025` |
| inflection | `<ticker><space><class letter>` | 2 | 0.00 | 0.00% | `BF B` Brown-Forman Corporation Class B; `HEI A` Heico Corp Cl A |

## Proposal for each pattern

1. **`<digits>_<word>` (64.01%, 7 entries) -- manual-entry route.** These read as one balance per relationship (`4175_VOYA` is a plan-level
   balance named "Voya"; `4175_CCA_*` are private LP capital values), not as listed securities. A `NAME::VOYA` row would carry a class for
   a name shared with the `BD...` Voya funds, and an LP capital value has no public data an AI pass can classify from. Propose: a human
   enters the class (and sub-class where the contract's list for the class allows) once per key, as a row keyed `NAME::<slug>` so the
   shared list can hold it (the form exists, so no contract change). Cost: 7 manual decisions cover 64.01% of the dollars; the two
   largest, `4175_VOYA` and `4175_CCA_EIGER_III_OPP`, alone are 41.56%.
2. **`CXMANUAL_*` (25.16%, 19 entries) -- manual-entry route, as a category table, not as security rows.** The names are one fixed phrase
   "Investor Manual Asset - <category>" (Home, Car, Jewelry, Mortgage, IRA, 401K, Annuity, ...); the category, not a security, is the
   unit, and it carries a negative (`CXMANUAL_MORTGAGE`) and non-securities (Car, Jewelry). Propose: the category-to-class mapping is
   entered once by a human (19 decisions, the same 19 for every investor who uses them) and read by FWD-15 before the UNPLACED-KEY
   route, rather than 19 `NAME::INVESTOR MANUAL ASSET <X>` rows in the shared list. Whether a Home or a Mortgage belongs in an asset-class
   table at all is a product call outside this census.
3. **`BD<6 alnum>` (5.76%, 43 entries) -- `NAME::<slug>` (existing form); option B needs a contract version.** Each key equals its own
   `cusip` column and is 8 characters, so it is not a 9-character CUSIP and `CUSIP:<9>` cannot hold it; the contract has no value for a
   custodian-internal id. Option A (no contract change): `NAME::<slug>`; the names are mostly distinctive (for example "3208 Voya Index
   Solution 2050 Portfolio Z"), but four are generic ("EXTENDED MARKET UNITS", "BALANCED FUND UNITS", "EQUITY UNITS", "INTERNATIONAL
   EQUITY UNITS", USD 1,453,230.45 together) and a bare name slug can merge distinct plans' funds. Option B: a fifth `identifier_namespace`
   value for a custodian id, key form `<value>:<id>`; it needs the four-postulate record (CLAUDE.md rule 24) and a contract version bump.
   Six of the 43 are crypto (`BD58B999` BTC, `BDE2HB99` USDC, `BDN86999` ETH, `BD2DU999` SOL, `BD2EC999` SUI, `BDTUV999` FLR; USD 3,315.54)
   and one, `BDCASHIN` (USD 0.00), is cash interest; these go with the cash decision in item 9 or a manual row.
4. **`<10 digits>` (2.51%, 2 entries) -- manual-entry route.** Two private LPs (CCA STNL Income Opportunity LP, Maranello-Plano LP): same
   reasoning as item 1; the key is an account number, not an identifier a data source resolves.
5. **`BA- FIDELITY.*` (1.28%, 11 entries) and `BA- <other>` (0.18%, 2 entries) -- `NAME::<slug>`.** Names are pool or fund names
   ("FID GR CO POOL CL 3", "RETIREMENT DATE 2030") and are distinctive enough; "MONEY MARKET" and "Insured Bank Deposit" (USD 24.90 and
   138,960.97) are cash-like and follow item 9.
6. **`CGF-<alnum>` (0.49%, 2 entries) -- `NAME::<slug>`**, with the same generic-name caution ("GROWTH", "CONSERVATIVE INCOME" would
   slug to one or two common words; a manual row is safer for these two).
7. **`<8 alnum> other` (0.03%, 1 entry, `07399D34` BEACON PARTNERS FUNDII LP) -- manual-entry** with the private LPs of item 4 (an LP, not a
   listed fund).
8. **`<ticker>+<suffix>` (0.01%, 2 entries: `VNO+L`, `MS+O`) -- `CUSIP:<cusip>`.** Both entries already carry a 9-character `cusip`
   (929042844, 61762V861), and the contract's CUSIP definition is "`CUSIP:<9 chars>` (the literal 9-character CUSIP), for a security
   with no exchange ticker". The planner shape-tests the key (fwd15_ai_plan.py docstring :14-17), not the entry's `cusip` column; reading
   the column would place both. Not a contract change.
9. **Not a key-form question.** `dotted ticker` (`QXO.PR.B`, 0.51%): a two-suffix preferred ticker that the old list's one-suffix ticker
   pattern rejects; widening the planner's ticker shape, not the contract, would place it (to be checked against how the shared list
   keys other preferreds). `cash pseudo-key` (`CUSTODIAL_CASH`, `FID:CASH`, with `BA- MONEY MARKET BALANCE`, `BA- INSDBNK09000`,
   `BDCASHIN` from the other groups, USD 184,663.26 in total: the 138,985.87 of `BA- <other>` + 78,027.97 - 32,350.58 + 0.00) belongs to the CASH row decision
   already on the round-12 enrichment list, not to this one. `<ticker>-OLD<mmddyyyy>` (5 entries, USD 0.00): retired-position suffixes
   on `AZN`, `OGI`, `TEVA`, `THMR`, `TTE`; carry no dollars, so propose mapping to the base ticker or dropping them from the missing
   list. `<ticker><space><class letter>` (`BF B`, `HEI A`, USD 0.00): ticker with a share-class letter; the same decision as the previous.

## What this proposal does not do

It does not pick between option A and B in item 3, does not decide whether Home and Mortgage belong in a classification table, and
writes no key. Nothing here moves served output.
