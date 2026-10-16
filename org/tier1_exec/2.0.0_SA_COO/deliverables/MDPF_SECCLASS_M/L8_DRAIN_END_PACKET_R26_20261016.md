# L8 drain-end packet -- MDPF_SECCLASS round 26 (2.0.0_SA_COO~M1, dell1, 2026-10-16 ~04:1xZ)

**For:** 3.0.0_SA_CVO (and the record for 1.0.0_SA_CTO~DELL1). **Decomposition:** `org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R26.md`.
**Issuance:** @9fc445a18b (`fanout: 4 of 4 chains, cap 8`), on the CTO round-25 analysis (msg 6457, CVO slug msg 6456). **Round-close check:**
`round-close-check.py --project MDPF_SECCLASS --round 26`: `orders=21 judgment=0 verdict=MAY-CLOSE` (proofs 17/17; TO-DEPLOY-e57e61 outside the verdict). Claim words: `measured` = read this session at trunk; `held` = cited from a record.

| cell | order | slot | risk | drained | criteria (worker run, re-run by the issuer in the worker tree and at trunk) |
|---|---|---|---|---|---|
| SC-e-103 | TO-SC-e103 | ~93 | LOCAL, direct act | @35a91f73c4 | AC1 `FWD45-DISPOSITION ok=True live=24 rows=24`; AC2 0 code files changed |
| SC-e-104 | TO-SC-e104 | ~94 | LOCAL, direct act | @b8bc2db5aa | AC1 `4 passed` (the same test fails 4 of 4 against the base E_25); AC2 `E25-REAL ok=True` on a 2,297-date real C_06 body |
| SC-e-105 | TO-SC-e105 | ~95 | LOCAL, direct act | @e8d8b06ec8 | AC1 `FIRMMIX-RECORD ok=True census=8 rows=8`; AC2 0 code files changed |
| SC-e-106 | TO-SC-e106 | ~96 | LOCAL, direct act | @df9cd47bf7 | AC1 `FOURTICKER ok=True`; AC2 0 code files changed |

The issuer's one real run of each outcome, at trunk, is committed: `R26_CHECKS/ROUND26_CLOSE_RUN_20261016.txt` (all four checks ok, the E_25 test 4 passed, py_compile OK).

## What the round established (measured)

- **FWD-4 / FWD-5 -- no code moved, by design.** `FWD45_B01B_E18_DISPOSITION.md` records all 24 lines of B_01b (7) and E_18 (17) that name the old list, each with a class and a replacement, and the measured facts the CTO's item rested on: no `etf-classifications` row carries `asset_name_raw` (5 rows read; 5,673 `NAME::` rows of 11,362, 3 pages); the shared `default_bd_securities_lookup` has 3 code lines in 2 files (22 hits across 7,203 files by `comp-find`) and no caller passes the flag that uses it; **B_02 reads no bd-securities** (gold-tree census 48 hits across 128 files, B_02 zero), so the `gold_dispatch.sh:562` comment is stale. Worker decisions: `DECISION-B_01b: RETIRE-FROM-CHAIN` (its OpenAI call and put are the old list's only writer in the gold tree, and nothing reads what it writes); `DECISION-E_18: OTHER` (the known set repoints to `etf-classifications`; the lookup and the name-prefix read are removed, not repointed, because `plan_rows` skips every ticker the canonical table carries, so a repointed lookup would do nothing). **Consequence to state, not hide:** removing E_18's lookup stops it writing canonical rows for a ticker whose only class source is the old list; such a ticker is listed unresolved. How many candidates that touches is unmeasured: row D1-W93-S2, ARMED, owner this seat, stays armed until round 27 measures it.
- **W92-S4 (E_25) closed in code.** `load_mix_summary_latest` reads `firm`, returns every class under `classes` with `pct` for each, and a note that is true now (cash and unclassified are classes). E_25 is in no chain and nothing is deployed. Row D1-W94-S1 (INERT): the nine-key class row holds on 19 of 2,297 dates; 2,278 carry four keys; the reader handles both.
- **`firm_mix_summary` (SC-e-105):** the writer is `data/black_diamond/scripts/gold/D_04.client_portal_summary.py:578` (firm 49financial, `json.dumps` without `sort_keys`); the cot, inf and 49f scripts write other firms' buckets or the advi twin. All 8 census readers read by key name, walk arrays, or sort first; the 4 readers the census misses (`.mjs`, YAML, a listing-driven census, an indirect portal consumer) are all `no` in prose. **`DECISION-FIRM-MIX-SUMMARY: NO-ORDER-DEPENDENT-READER`: no sort pair is needed, the question closes.** Issuer note: my order told the worker to add rows for readers the census misses while the check refuses an extra row (row D1-W95-S2, my defect; the prose carries them).
- **The four tickers (SC-e-106):** `seed-etf-classifications.py` reads no Bloomberg GICS data and no Schwab master (the order's premise did not hold, row D1-W96-S1); its one class source is the hardcoded `_shared/etf_classification.py`, which holds no row for HPI, CUBE, GLPI, PCEF or their CUSIPs. Open lots on 2026-10-09: HPI $51,050.86, CUBE $7,570.00, GLPI $4,285.56 (canonical holdings carry 1 row), PCEF $0.00: $62,906.42 (the CVO's $63,967.82 differs; 95,429 lots rows with a null ticker were not matched). `proposed_row` is null for all four; no outside model.

## Not shown

How many E_18 candidates today get their class only from the old list (D1-W93-S2); that the name-prefix read's removal changes no canonical write (argued from the code, not exercised); a Bloomberg or Schwab source for the four tickers (none exists in the seed path; getting one is a Bloomberg queue request or Andrew's word for an outside model, neither made); that the evidence figure for the four equals the CVO's (it differs by about $1,061).

## Rows at this packet

Open: D1-W93-S2 (ARMED, owner this seat, disarm = the measurement above), D1-W93-S1 and S3, D1-W94-S1, D1-W95-S1 and S2, D1-W96-S1 (INERT observations; W95-S1: `lib/platinum_dest` and `lib/config` are imported by the writers and untracked at HEAD).

## Owed at the round-27 recut (on the CTO's round-26 analysis)

The six-item build from `FWD45_B01B_E18_DISPOSITION.md` section f, with the item-4 grant for the shared module `_shared/etf_classification_scheduled.py` and a stated consequence for the CVO; the measurement that disarms D1-W93-S2; a source for the four tickers; the DEMQUE<->SECCLASS sync cell; e57e61 (run date by the 10-20 14:00Z run, else the seeded exercise). Open at Andrew: the client-facing Black Diamond Mix restated-history PROD push.
