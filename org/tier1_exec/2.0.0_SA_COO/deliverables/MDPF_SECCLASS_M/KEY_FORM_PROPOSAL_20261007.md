# Key form for a security with neither a ticker nor a CUSIP -- proposal (MDPF_SECCLASS TO-SC-e26, FWD-17 / FWD-15, ADDENDUM v0.7)

**Author:** `0.9.0_WK_MDPF_SECCLASS~25`, 2026-10-07. **Read-only measurement; no table write.** Companion: `OLD_LIST_CENSUS_20261007.json`.

PROPOSED KEY FORM: `NAME::<slug>` where slug = the security's name upper-cased, every run of characters outside `A-Z`, `0-9` and `-` replaced by ONE space, trimmed, cut to the first 80 characters (the rule `classify_bd_securities.normalize_key` already applies); an empty slug yields no key and the write is refused.

## How many old rows it keys

Old list `bd-securities`, consistent paginated scan 2026-10-07: **10,965 rows** (the research seat's brief read 10,873; the difference is +92 rows between the brief and this scan).

| form of the old key | rows | note |
|---|---|---|
| bare ticker (`[A-Z0-9]{1,6}([.-][A-Z0-9]{1,4})?`) | 3,825 | 2,376 of them also in `etf-classifications` |
| `NAME::<slug>` | **7,133** | the rows this form keys |
| `CUSIP:` | 0 | the old list never used it |
| none or other | 7 | `DEST_LCAP_I`, `JPM_STRUCT_0029`, `The Hartford`, `WALDROP_DAF`, `CASH_USD`, `Xometry`, `DEST_INTL_I`: not keyed by this form (named, not re-keyed) |

Of the 7,133 `NAME::` rows: 6,304 already read exactly in the proposed form; **829 differ** (they keep `/` `.` `%` `&` `$` `(` `)` or lower case that the rule removes); 1 has an empty slug (`NAME::`). The 7,133 split by membership: in both lists 0, held today and not in the shared list 1,097, the rest 6,036. Re-slugging the 829 under the rule makes **822 of them collide** with a conforming row (the list holds the same security twice, once with punctuation); a writer re-keying them must merge, not overwrite, and the empty row is refused.

## The four postulates

**MECE.** Domain: every security the shared list can be asked to hold. Partition by the identifier a security has: a valid ticker -> the ticker; else a 9-character CUSIP -> `CUSIP:<9>`; else a Bloomberg-only identifier -> `BBG:<...>` (626 rows today); else (none of these) -> `NAME::<slug>`. Each security takes the first form that applies, so exactly one. Subtraction from a printed denominator: the 10,965 old rows = 3,825 ticker + 7,133 `NAME::` + 0 `CUSIP:` + 7 other; the 7 other are the uncovered members and are listed above, not folded in.

**SAME GRAIN.** One key = one security as the old list's own writers identify it (one name, one row). The slug is the security's normalised NAME, never an account, lot or position: the grain `normalize_key` in `data/black_diamond/scripts/classification/classify_bd_securities.py:56-70`, `E_18.detect_new_securities.py:175-188`, `B_01b.classify_new_securities.py` and `data/inf/scripts/classification/classify_assets.py:98-113` already share. The silver `_synth_asset_id` in `data/cot/scripts/gold/A_05.assets_dimension.py:94-103` and `data/inf/scripts/silver/build_assets_dim.py:118-128` use a different slug (underscores, 60 characters) for an asset dimension id, a different object; they are not the table key and the proposal does not adopt them.

**INTENT COHERENCE.** One axis, one intent: the prefix says "no ticker and no CUSIP, keyed by name". It never also means "name alias" or "needs review" (those are attributes `name_aliases`, `needs_review` on the row). It cannot be mistaken for a ticker or CUSIP: a ticker has no `:`, and the only `:` forms in the shared list today are `CUSIP:` (425 rows) and `BBG:` (626 rows); the old list has no non-`NAME::` key containing `:` (0 of 3,832).

**STATE COHERENCE.** Values this form does NOT move: a ticker row and a `CUSIP:` row keep their keys; a `NAME::` row's classification attributes (`asset_class`, `sub_asset_class`, `classified_by`, `confidence`) are untouched by choosing the key form; the 7 other rows keep their keys until a separate decision names them. One remedy per state: re-keying the 829 non-conforming rows is a merge decision (822 collisions) and is NOT done by adopting this form. Cost: a name slug of 80 characters can collide for two distinct securities with identical first 80 normalised characters; the old list's longest slug is 75 characters (0 rows at 80), so no truncation occurs in today's 7,133.

## Word-boundary token census of the prefix over the repo

`comp-find '\bNAME::' --all` (corpus=all, run 2026-10-07 on this worktree): **3,733 hit(s) across 58,833 file(s) scanned** | 36 ephemeral-floor, 1 unreadable, 3,372 binary NOT searched. Bands (true totals): SURFACED 58, CONFIG 3,617, DOC 58. Distinct files by band: first-party source 18, config/data 8, doc 37. The 18 first-party source files are the four `bd-securities` key writers named above, `data/black_diamond/scripts/classification/{backfill_name_aliases,resolve_tickers}.py`, `data/cot/scripts/gold/{A_05.assets_dimension,B_01b.classify_new_securities,E_18.detect_new_securities}.py`, `data/inf/scripts/silver/build_assets_dim.py`, `infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py`, `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/bd_securities_write_{batch_a,cot_new}.py`, two `build_assets_dim.py` copies under `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/door5_decollide_20260715/bank/`, and three files this run produced (`.scratch/scan.py`, `R10_CHECKS/old_list_census.py`, `R10_CHECKS/issuer_check_sc_e26.py`). The file names and the writer docstrings read (not every one of the 3,733 hits) use the prefix in one sense, a name-keyed security with no ticker. The prefix is already the live form of the old list, so adopting it adds no new token to the repo.

## Collision check

- vs `CUSIP:` -- different prefix; 0 old keys and 0 shared keys carry both.
- vs `BBG:` -- different prefix; the shared list's 626 `BBG:` rows keep their form.
- vs a valid ticker -- a ticker matches `[A-Z0-9]{1,6}([.-][A-Z0-9]{1,4})?` and contains no `:`; `NAME::` always does. 12 old `NAME::` slugs are themselves 1-6 alphanumeric characters (they look like tickers without the prefix); the prefix keeps them apart. 0 of the 3,507 shared keys contain `::`.
