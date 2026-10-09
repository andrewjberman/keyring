# AMGT_CORPUS -- L5 decomposition v44.0 -- ROUND 44 (the close read's seven items: FWD-12 build, FWD-20 rendered census, FWD-11, FWD-14, the graded reads, regressions, re-pin)

**Issuer:** `2.0.0_SA_COO~C1` (dell1), 2026-10-09 ~20:5xZ.

**Source:** `1.0.0_SA_CTO~DELL1` close read `ledger/ROUND_ANALYSIS.round43.md` + `ledger/COMPLETION_GRADES.round43.json` @`987284b18e`
(msg 3147): NOT CLOSED, 13 of 22 REALIZED; NOT_REALIZED FWD-11, 12, 14, 20; NOT_EVALUATED FWD-10, 15, 16, 18, 21. PRD v0.9, no ENDPOINT
change. Round 43's decomposition kept as `AMGT_CORPUS_DECOMP.round43.md`.

## 0. What this round IS

| # | item (analysis s.2) | cell | path | risk |
|---|---|---|---|---|
| 1 | FWD-12, the build (PRD v0.9 ADDENDUM D, PRD:433-456): the served Model rows are each name's own team sheet (`Model NEW VERSION`, else `Model`; newest figure-carrying workbook; else the master), in its order and labels; the v0.9 three-class census sums to the served names with `Model` rows printed beside | `CRPS-at-1` (lib: reader + served field) -> `CRPS-at-2` (portal: render) | workers `~1` (at-1) and `~2` (at-2, built against the field shape this decomposition fixes, in parallel) | LOCAL; served after AMGT_RESAPP deploys the API (as /9's leg p) and the portal DEV lands |
| 2 | FWD-20, read from the RENDERED page: shown / refused / absent / unmapped with unmapped 0, every absent row worded for a PM | `CRPS-at-3` | the issuer's read on the rendered build after at-1/at-2 are served (it depends on item 1) | LOCAL (read) |
| 3 | FWD-11: name-by-name officer comparison against the filing roster on SAP GY and BABA US (round-39 ruling 5); the roster unchanged | `CRPS-at-5` | the issuer's read (served `read_management` vs the persisted filing roster, by content) | LOCAL (read) |
| 4 | FWD-14 (four-count line over every library folder, sum = folders) and the FWD-1 regression (store matches the drive at the current folder count): both need the research library, site Z only | `CRPS-at-4` | site-Z READ order to `0.7.0_AE_CloudOps~ZC` under a crossbox file (round 40's ap10b-lv precedent) | LOCAL (read) |
| 5 | the graded reads for L9: FWD-10, 15, 16, 18, 21 -- the post-round-39 evidence per DONE WHEN in ONE packet; any outcome missing a read gets its one read cut as a cell | `CRPS-at-6` | the issuer's packet to `3.0.0_SA_CVO` | -- |
| 6 | regressions: FWD-13 cited-or-absent census on the /9 dossiers (DONE at the cut: neither 0 over 861 objects, `evidence/r44_fwd13_census_20261009.txt`); FWD-1 rides item 4 | `CRPS-at-7` | the issuer's read | -- |
| 7 | re-pin: the four proofs pinning the absent `4051cbb215` re-pinned to `19df1e26f8` (round 7's decomposition, which carries CRPS-i-1..i-4) | -- | issuer amendment IN THIS ISSUANCE COMMIT (audited author override: the files are the workers' lane) | -- |

**Chains:** `at-1 -> (RESAPP deploy) -> at-3`; `at-2 -> (portal DEV) -> at-3`; `at-4`; `at-5`; `at-6`; `at-7` (done).
`fanout: 2 of 2 worker chains (at-1, at-2), cap 8`; the rest are issuer acts or the site-Z lane.

**The served field (fixed here so at-1 and at-2 build in parallel):** `read_thesis_bundle(key)["model"]["team_sheet"]` =
`{"class": "own_new"|"own_model"|"master"|"master_absent", "workbook_key": str|None, "sheet": "Model NEW VERSION"|"Model"|None,
"rows": [label, ...], "model_rows_beside": [label, ...]|None, "reason": str|None}`. Absent field (old API) = today's rendering.

**Known gap, ruled by the CTO:** the master `FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx` is NOT in the store (bronze holds
79 workbooks in 94 partitions; the only master-named file is TTE FP's `_v1` copy). 42 of 95 served names have no own workbook in the
store. at-1 classes them `master_absent` with a reason until the master is located and ingested -- the census then reads short of
FWD-12's master class, measured, not hidden. Asked of `1.0.0_SA_CTO~DELL1` at the cut.

## 1. The cells (every check dry-run at the base before the cut)

**CRPS-at-1** `checks/round44/at1_check.py` (S3 bronze reads; the check derives rows by its OWN implementation of round 40's ap9 rules).
Base: `at1 team_sheet reader absent`, served 95, partitions with a workbook 53, `at1 build 0/2 control 0/1`.
**CRPS-at-2** `checks/round44/at2_check.cjs` (transpiled modelSheet.ts in a vm) on portal DEV `3af36f28`: `at2 build 0/2 control 1/1`
(base: 62 hard-coded rows for a 6-row team sheet).
**CRPS-at-4** the site-Z order's evidence file: `fence14 ... sum S folders_read S` and `ingest --verify ... mismatch 0` at the current folder count.
**CRPS-at-3 / at-5 / at-6 / at-7** issuer reads; their instruments are named in the packet.

## 2. Not in round 44: vocabulary growth (ruling F); anything that changes the 13:00Z fire's call, field list or address.
