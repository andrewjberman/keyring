# CTO never-widen half -- MDPF_SECCLASS SC-e-48, clean names v2 (FWD-14), 1,349 conditional name updates on `etf-classifications`

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~18:0xZ, release mode request 7 (msg 497). **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CLEAN_NAMES_V2_20261007.md` @b59fb7fea3
(COO half SIGNED). Function `security_name.py` last touched at 9e01f8ee64; set `CLEAN_NAME_ROW_SET_V2_20261007.tsv` (1,740 rows).

## VERDICT: REFUSED -- the names the act would write are not yet "properly written" (FWD-14). Nothing else in the half is contested.

## Read by this seat

- **The mechanism reads true.** Blast radius is `name` + `updated_by` on 1,349 keys. Both conditions (`name = :current`;
  `attribute_not_exists(name)`) are sound, the writers count (N = 8) is read with each rule, and the snapshot rollback is per key. The
  13 seed rows are listed, not written. Had the names been right, this would sign.
- **The function, run at the branch on the request's own inputs:**
  - `ABB LTD SPONSORED ADR` -> `Abb LTD Sponsored Adr`
  - `CAPGEMINI S E UNSPONSORED ADR` -> `Capgemini S E Unsponsored Adr`
  - `PGIM AAA CLO ETF` -> `Pgim Aaa Clo ETF`
  - `ZURICH INSURANCE GROUP LTD` -> `Zurich Insurance Group LTD`
  - W28-S5's pins hold (`BP PLC` -> `BP PLC`, `WMT` -> `WMT`).
- **Census of the set's `clean_name` column** (1,740 rows, word-boundary, case-sensitive):
  - WRITE rows with a title-cased acronym (`Adr`, `Ads`, `Abb`, `Etf`, `Sa`, `Se`, `Ag`): **25**.
  - WRITE rows with an all-caps corporate form (`LTD`, `PLC`, `INC`, `CORP`, `CO`): **48**.
  - The same form in both casings across the set: `LTD` 21 / `Ltd` 16; `PLC` 39 / `Plc` 4; `ADR` / `Adr` 15; `ETF` / `Etf` 2.
  - So 73 of 1,349 writes (5.4%) would land a visibly wrong name, and the column would carry two spellings of one word.
- `clean_name` is idempotent, so it keeps mixed input mixed. A held row arriving as `Ferguson Plc Ord` stays that way while
  `AstraZeneca PLC` stays upper. Fixing that is a function change, not a set edit.

## What re-opens this half (one re-request, same pair, no new cell)

1. In `clean_name()`, each depositary and fund form reads upper: ADR, ADS, ETF.
2. Each corporate form reads ONE casing whatever the input's casing. The W28-S5 pin fixes `PLC` upper, so LTD and the
   foreign forms (SA, SE, AG, NV) follow the same all-caps rule. `Inc`/`Corp`/`Co` keep the title case already pinned. A pin test
   covers each form in both input casings.
3. Short all-caps tokens that are not dictionary words read upper (`ABB`, `AAA`, `CLO`, `PGIM`). Where the rule cannot be made
   exact, list the exceptions in the pin test and say so in the re-request.
4. Rebuild the set and re-run the dry run. The re-request prints the census above at zero for WRITE rows, plus the new totals.
5. The SC-e-34 request stays superseded and unsigned. Nothing is written under either until this half signs.

The dell1 principal's untested WRITE on `etf-classifications` is fine as the request states it: a first-update refusal writes
nothing and moves the act to a laptop seat under the same pair.
