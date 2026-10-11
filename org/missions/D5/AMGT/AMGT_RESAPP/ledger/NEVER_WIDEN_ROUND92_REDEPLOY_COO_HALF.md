# NEVER-WIDEN CO-SIGN -- COO HALF. Round 92, `AMGT-qq-5`: the ONE redeploy of `opal-amgt-scoped-api` carrying the name-matched identity and the unit-aware currency

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-11 ~09:0xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND92_REDEPLOY_CTO_HALF.md`. Model: round 91's redeploy pair
(`NEVER_WIDEN_ROUND91_REDEPLOY_COO_HALF.md`, ADDENDA 1-2). Applier: `0.7.0_AE_CloudOps~RA1`. Source: CTO round-91 analysis @f6eb45c478 item 1;
order `task-orders/AMGT_RESAPP.TO-AMGT-qq-5.redeploy-the-scoped-api-with-identity-and-the-unit-aware-currency.md`.
**This half is written from a MEMBER-BY-MEMBER MEASUREMENT, not from the cells' descriptions** (the lesson of round 91's pp-6): evidence file
`deliverables/2.0.0_SA_COO~R1/round92_prep/MEMBER_TABLE_BASELINE_vs_MERGED_20261011.json`, instrument `checks/r92_member_table.py`.

## THE ACT

One CODE leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at the build pin the GO names (a box/dell1 commit
carrying `AMGT-pp-1` @62c242efc4 and `AMGT-qq-1` @5b8736efac). Live pre-act: `l8egBo/rfEH4ddCEFyWnUOb9BvN3bGu/azarul5Ho0g=` (pin a943b1b412,
restored by round 91's pp-6 rollback, dossier /11).

## THE MEASUREMENT (the expected outcome is its reading, member by member)

Instrument: for each of the 243 MEASURED crosswalk subjects, the LIVE function's `/security/<key>/peers` response (Lambda invoke, GET) against the
merged tree's own `scoped_amgt.handler` on the same live pool; every member compared on every field. Denominator: **243 subjects, 2,230 members**.

| | count |
|---|---|
| subjects compared / member-count changes / subject-level fields changed outside `members` | 243 / 0 / 0 |
| members changed | **180** |
| members changed in a field OUTSIDE `identity`, `security_key`, `price_currency`, `price_currency_reason` | **0** |
| members byte-equal | 2,050 |

The 180 changed members fall into FOUR classes, each read from the writer's rule:

| class | count | live serves | merged serves | rule (code, merged) |
|---|---|---|---|---|
| A. a currency already served keeps its code and LOSES the producer's stale reason text | 144 | `price_currency` USD 120, CHF 9, EUR 8, JPY 6, HKD 1, plus the stored reason | the same code, no `price_currency_reason` | `scoped_amgt._with_price_currency` (qq-1): a served currency pops the stale reason |
| B. a minor-unit record currency is NOT served | 12 | `price_currency` GBp beside a pound price | no currency, `price_currency_reason` = the minor-unit sentence | `price_currency.price_currency_fields` + `is_minor_unit` (qq-1): refusal, no GBp-to-GBP conversion |
| C. a member gains its held company's identity (pp-1), the record's currency is a major unit | 11 | none, the stored reason | `identity` MEASURED `matched_as` `company_name`, `security_key`, and `price_currency` EUR 6, SGD 3, CHF 2; no reason | `numeric_tickers.name_match_fields` (pp-1), then class A's rule |
| D. a member gains identity, no currency is served | 13 | none, the stored reason | `identity` as in C; 12 carry the minor-unit reason (UK GBp records), 1 (`B0744B` of `BZLFY_US_Equity`) carries `price_listing`'s reason ("... home exchange ... its United States listing") | pp-1, then class B's rule; the listing rule (`price_listing.py`) for the 1 |

Classes C and D together are RA1's 24 members of round 91's pp-6 compare (`deliverables/0.7.0_AE_CloudOps~RA1/PP6_CHANGED_MEMBERS_20261011.json`):
**the two sets are equal member for member, with equal keys** (24 of 24). Round 91's 12 "GBp" rows among them are class D here (the only difference the guard makes).

### Class B -- the 12 live GBp rows (C-S55), subject / member ticker / name / scanner price

| subject | ticker | name | price |
|---|---|---|---|
| `GSK_LN_Equity` | 098952 | AstraZeneca PLC | 120.32 |
| `LLY_US_Equity` | 098952 | AstraZeneca PLC | 120.32 |
| `NOVN_SW_Equity` | 098952 | AstraZeneca PLC | 120.32 |
| `ROG_SW_Equity` | 098952 | AstraZeneca PLC | 120.32 |
| `PBR_US_Equity` | 079805 | BP PLC | 5.571 |
| `TTE_FP_Equity` | 079805 | BP PLC | 5.571 |
| `BATS_LN_Equity` | 045449 | Imperial Brands PLC | 24.24 |
| `RKT_LN_Equity` | 045449 | Imperial Brands PLC | 24.24 |
| `ULVR_LN_Equity` | 045449 | Imperial Brands PLC | 24.24 |
| `AI_FP_Equity` | 071887 | Rio Tinto plc | 69.54 |
| `NG/_LN_Equity` | 079087 | SSE PLC | 24.73 |
| `RWE_GR_Equity` | 079087 | SSE PLC | 24.73 |

### Classes C and D -- the 24 members that gain an identity

| subject | ticker | name | key gained | currency after | reason after |
|---|---|---|---|---|---|
| `RIO_LN_Equity` | B1YXBJ | Air Liquide SA | `AI_FP_Equity` | EUR | none |
| `BZLFY_US_Equity` | B0744B | Bunzl plc | `BZLFY_US_Equity` | none | home-exchange listing |
| `AZN_LN_Equity` | BN7SWP | GSK plc | `GSK_LN_Equity` | none | minor unit |
| `CSL_AU_Equity` | BN7SWP | GSK plc | `GSK_LN_Equity` | none | minor unit |
| `SAN_FP_Equity` | BN7SWP | GSK plc | `GSK_LN_Equity` | none | minor unit |
| `ENEL_IM_Equity` | B288C9 | Iberdrola SA | `IBE_SM_Equity` | EUR | none |
| `MER_PM_Equity` | B288C9 | Iberdrola SA | `IBE_SM_Equity` | EUR | none |
| `ENEL_IM_Equity` | BDR05C | National Grid plc | `NG/_LN_Equity` | none | minor unit |
| `IBE_SM_Equity` | BDR05C | National Grid plc | `NG/_LN_Equity` | none | minor unit |
| `SSE_LN_Equity` | BDR05C | National Grid plc | `NG/_LN_Equity` | none | minor unit |
| `BATS_LN_Equity` | BSZBP5 | Reckitt Benckiser Group plc | `RKT_LN_Equity` | none | minor unit |
| `IMB_LN_Equity` | BSZBP5 | Reckitt Benckiser Group plc | `RKT_LN_Equity` | none | minor unit |
| `ULVR_LN_Equity` | BSZBP5 | Reckitt Benckiser Group plc | `RKT_LN_Equity` | none | minor unit |
| `ST_SP_Equity` | B02PY1 | Singapore Telecommunications L | `ST_SP_Equity` | SGD | none |
| `T_US_Equity` | B02PY1 | Singapore Telecommunications L | `ST_SP_Equity` | SGD | none |
| `VZ_US_Equity` | B02PY1 | Singapore Telecommunications L | `ST_SP_Equity` | SGD | none |
| `CVX_US_Equity` | B15C55 | TotalEnergies SE | `TTE_FP_Equity` | EUR | none |
| `PBR_US_Equity` | B15C55 | TotalEnergies SE | `TTE_FP_Equity` | EUR | none |
| `XOM_US_Equity` | B15C55 | TotalEnergies SE | `TTE_FP_Equity` | EUR | none |
| `UBSG_SW_Equity` | BRJL17 | UBS Group AG | `UBSG_SW_Equity` | CHF | none |
| `ZURN_SW_Equity` | BRJL17 | UBS Group AG | `UBSG_SW_Equity` | CHF | none |
| `BATS_LN_Equity` | BVZK7T | Unilever PLC | `ULVR_LN_Equity` | none | minor unit |
| `NESN_SW_Equity` | BVZK7T | Unilever PLC | `ULVR_LN_Equity` | none | minor unit |
| `RKT_LN_Equity` | BVZK7T | Unilever PLC | `ULVR_LN_Equity` | none | minor unit |

### Class A -- the 144 (counts; the per-member rows are in the evidence file)

USD 120 (109 with the standard reason text, 11 with the company-specific one), CHF 9, EUR 8, JPY 6, HKD 1. Each keeps its served code byte-equal and
loses ONLY `price_currency_reason`.

## BLAST RADIUS -- the CONTENT-DIFF the build may print against the live package, each member admitted by BLOB at the GO

`git diff a943b1b412 HEAD` over every non-test file of `lib/`, measured at the cut (box/dell1 HEAD): eight files. Four are the function's closure and
are admitted below; four are NOT in the function's closure or are another project's.

| member | admitted for | blob at the live pin | blob at the cut | the only change admitted |
|---|---|---|---|---|
| `lib/research/peers/numeric_tickers.py` | `AMGT-pp-1` | `85db6ab86b6f` | `cbb960ff4e36` (moves with pp-1) | `name_match_fields`, `name_candidate`: pure functions; `numeric_fields`, `name_token`, `japan_forms` unchanged |
| `lib/research/api/scoped_amgt.py` | `AMGT-pp-1`, `AMGT-qq-1` | `cbccb2d08b3f` | `0662ef5b08de` (moves) | **16 lines**: pp-1's exact-name arm inside `_with_numeric_tickers` (13 added, 3 removed) and qq-1's two lines in `_with_price_currency` (pop the stale reason when a currency is served). Diff since the pin printed and read at the cut: nothing else |
| `lib/research/peers/price_currency.py` | `AMGT-oo-5` (merged @a423f1d667), `AMGT-qq-1` | `7e994be8b475` | `9d8099e5efa0` (moves) | oo-5: the `answered` parameter and `answered_currency` (NOT exercised: no answer has landed; nothing is served from it); qq-1: `is_minor_unit`, `REASON_MINOR_UNIT`, the refusal branch (16 lines) |
| `lib/research/identity/crosswalk.py` | `AMGT-nn-5` (merged @04ecb2d528), by blob | `48d7e7d9983b` | `3603be4be89a` (by blob, nn-5) | `write_pool` guard and `main` early refusal: producer-CLI paths the function never calls |
| `lib/opal_naming.py` | **another project's** (LGIC/FIRMBKTS: `e1267f773c`, `b0eebb018d`, `56b271d8ff`) | `dc613fe9fe26` | `3fc88f348059` (moves) | PACKAGED, not imported by the adapter at import; reached at request time on the dossier path (`corpus.dossier -> harvest.store`). Diff since the pin: +250 lines, ADDITIVE (new registry readers and validators, generated views, platinum/bronze builders, one extra branch for an inline PascalCase IAM policy name that used to RAISE). No row of `address()` the function's `_harvest_prefixes` module holds changes: `lib/research/api/tests/test_harvest_prefixes.py` 6 passed at the cut. **Admitted only with that test re-run at the pin, its output printed** |

NOT admitted (not in the function's closure; if the content-diff names one, STOP): `lib/research/identity/add_security.py` (producer CLI),
`lib/research/filings/analyze.py` (qq-3, producer-side), `lib/research/peers/universe.py` (qq-2, producer-side), `.tools/git-hooks/mass-deletion-check.sh`.
Any other member is a STOP. NO IAM, route, memory, schedule, store write or S3 delete.

## WRITER CENSUS of the moved served properties (N printed)

- `members[].security_key` / `members[].identity`: THREE writers in `read_peer_set`, disjoint by ticker form: `_with_listed_identity` (a United
  States alphabetic ticker, nn-2), `_with_numeric_tickers` numeric arm (an all-digit ticker: the Japan code, then the exact name), and its exact-name arm (any other non-US ticker, pp-1). **N = 3 rules read.**
- `members[].price_currency` / `price_currency_reason`: ONE serve-time writer, `_with_price_currency`; it reads the stored member's own
  fields as input and, after this act, drops the stored reason when it serves a code. **N = 1 rule read.** The answered-currency branch is ABSENT (no answer file).
- NOT moved, and the compare must show it: `price`, `cap_currency`, `price_currency_claim`, `price_currency_source`, `name`, `country`, `rank`/order, member count, every subject-level field.

## EXPECTED OUTCOME -- both branches, read from the producer's rules

- **Branch 1 (a member the table names):** exactly the 180 above, each with the fields before and after the table lists. Every other member (2,050) byte-equal.
- **Branch 2 (anything else):** a member that changes and is not in the table, a changed field outside the four, a changed member count, or a
  subject-level change is a **STOP** and, inside the same hour, a rollback unless the CTO names KEEP on the evidence (order bound 8).
- **The measurement's own limit, stated:** the AFTER arm is the merged tree's handler run locally against the live pool with the caller's
  credentials; the deployed function reads the same pool and the same held-name index through its role. The post-apply compare (condition 3) is the control for any difference.

## PER-KEY ROLLBACK

The kept live package (downloaded and hash-checked as `l8egBo/rf..`), one `safe-apply`, same hour (round 91's pp-6 rollback is the specimen: applied 07:37Z, rolled back 07:50Z, R89 YES twice). No store object is written; there is no per-key rollback beyond the function's code.

## SEQUENCING (CTO half, round 91)

`AMGT-qq-4` (the stored-driver write into three names' `filings/v1` and `drafting/v1`) and this act NEVER share a window; whichever runs second re-measures its expected table against the state the first left and prints both. The issuer proposes **this act first**: it changes the function's code and the peers route only, and qq-4's writes change the `/thesis` and drafting objects only (the compare of this act's 2,230 members is unaffected by qq-4, and the reverse).

## CONDITIONS (issuer's, binding on the GO)

1. The pin carries `AMGT-pp-1` @62c242efc4 and `AMGT-qq-1` @5b8736efac (ancestry read by the applier at the pin, not taken on the issuer's word); `AMGT-oo-5` @a423f1d667 and `AMGT-nn-5` @04ecb2d528 are ancestors.
2. The blob of every admitted member at the pin is printed beside this table's column; the content diff of the built package against the kept live package is printed WHOLE before any upload; `lib/opal_naming.py`'s admission requires `test_harvest_prefixes.py` run and printed at the pin.
3. BEFORE the apply, read the baseline of all 243 subjects' peers routes at `l8egBo..`; AFTER, BEFORE flipping anything, compare every member (about 2,230) and print each changed member's fields before and after against THIS table (180, in four classes). `checks/r92_member_table.py` is the instrument (its AFTER arm becomes the deployed function).
4. After the act: `r89_peers_deployed.sh` reads `R89 PEERS DEPLOYED: YES`, `r89_deployed_close.sh --want amgt-corpus-dossier/11` reads `R89 DEPLOYED CLOSE: YES` (the no-regression arm), `r92_minor_unit_census.py` reads `R92 MINOR-UNIT CENSUS: YES` (M1 0 minor-unit labels beside a scanner price, M2 0 rows serving a currency beside a stale reason, M3 the 149 major-unit codes kept) and `r91_name_match_deployed.py` reads `R91 NAME MATCH DEPLOYED: YES`, each with the CodeSha256 re-read in the same output.
5. The source map records the deploy (`record-terraform-deploy.sh`, entry before and after). The change-management entry is opened before and closed after.
6. AMGT_CORPUS (`2.0.0_SA_COO~C1`) is asked in the GO whether a leg rides; a leg that rides brings its own pair and blobs. `AMGT-pp-4` (the DEMQUE answer) is NOT a wait and rides a later redeploy.
7. The act is re-measured on the day of the GO: if the pool objects or the held-name index moved, the issuer replaces the counts above and the CTO half is signed on the replacement.

-- 2.0.0_SA_COO~R1
