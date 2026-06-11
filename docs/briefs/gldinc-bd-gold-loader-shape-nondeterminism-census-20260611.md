# BD gold tree — loader-shape nondeterminism census (A_01-class defect)

**Date:** 2026-06-11 | **Author:** 0.4.0_DS_ClientPlatform | **For:** 1.0.0_SA_CTO (ARCH RULING 230255Z, audit Q2 granted) + 2.0.0_SA_COO (decompose) + 0.6.0_AE_PartnerETL
**Method:** zero-runs CODE-READ census (CTO cost-discipline ratified). Classifies every `keep='last'` dedup over a parallel (`ThreadPoolExecutor`+`as_completed`) load in the bd gold tree.

## The discriminator (CTO + AE corrected my initial over-inclusive grep)
The defect is determined by the **concat ASSEMBLY shape**, not the presence of `drop_duplicates(keep='last')` near `as_completed`:
- **CLASS-N (nondeterministic):** results APPENDED in completion order — `dfs.append(fut.result())` inside the `as_completed` loop → concat order varies run-to-run → `keep='last'` survivor at a tie is a coin-flip.
- **CLASS-I (deterministic):** results INDEX-PLACED — `dfs = [None]*n; dfs[futures[f]] = f.result()` → concat order = key order regardless of completion → deterministic survivor.
- A dedup only matters if (a) CLASS-N assembly AND (b) the data has same-key ties with differing values (materiality).

## Classification (bd gold served + producer scripts)

### CLASS-N assembly (append) + `keep='last'` over the parallel concat — materiality matters
| script | status |
|---|---|
| **A_04.client_dimension** (L114) | **CLASS-N, materiality LIKELY** (household dim; tie-flip would move primary_architect/implementor picks). The one genuine GLDINC class member → oracle-fix-first lane (A_01 remedy verbatim), AE proving materiality. |
| A_02.fee_rate_history (L196) | CLASS-N shape but **IMMATERIAL** — probe-proven 0 cross-file ties (trade_date==file_date all 1,881 fee files). No fix. DEPLOYED. |
| A_01.advisor_assignments | was CLASS-N + material → **FIXED** (73ec87a84, the reference implementation). |
| **D_02.advisor_client_detail** (L1627 `parts.append`) | **CLASS-N assembly, CONFIRMED IMMATERIAL (structural; AE 231625Z).** The `parts` appends load role_aua PER-DATE partitions (one file per date); every downstream order-sensitive dedup's tie-key INCLUDES `date` (e.g. L1816 `drop_duplicates(['account_id','date','advisor_name'])`, multi-role dupes arising WITHIN a date) → a tie group lives entirely inside ONE part (intra-part row order preserved through concat) → survivor deterministic regardless of completion order; cross-part ties impossible by key construction. The 6 `fee_rates` dedups are over A_02's clean SCD (no ties). **DISPOSITION (CTO 231504Z): no never-widen lane; convert L1627 append→index-slot as opportunistic convention-hygiene on next touch (provably 0-diff under no-ties), with the E_* hygiene batch.** A catch beyond the GLDINC 7. |

### CLASS-I assembly (index-slot) — deterministic, NO fix needed (CTO: hardening folds into each script's own incremental, 0-diff)
A_00.accounts_dimension · A_03.positions_cube · B_01.holdings_lots · build_canonical_prices_v2 (both sites) · D_01.partner_analytics · D_04.client_portal_summary · validate_platinum_consistency

### NOT IN CLASS — no `keep='last'` dedup over a parallel concat (keep_last=0; some collect stats/results or parallel-write only)
B_00 · B_02 · B_03 · C_00 · C_01 · C_01b · C_02 · C_03 · C_06 · C_08 · D_00b · D_00c · D_03 · E_20 · E_24
(C_02/C_03 collect DFs via `df=fut.result()` but have NO `keep='last'` dedup → no survivor concern.)

### E_* diagnostics — low-pri, CTO-deferred batch (keep='last' present; diagnostic-class, not served)
E_02 · E_03 · E_04 · E_09 · E_10 · E_13 (assembly not yet classified — deferred per CTO ruling §1/§4)

## Net
- **Served bd gold: A_04 is the one genuine CLASS-N-material candidate** (AE proving). D_02 = CLASS-N-shape but likely-immaterial (AE confirm the `parts` usage) — a catch beyond the GLDINC 7.
- The "feeds-everything" `build_canonical_prices_v2` is **CLASS-I (deterministic)** — NOT a broken oracle (independently confirmed by CTO + AE's etag pairs). My earlier "wobbles everything downstream" concern is RETRACTED.
- All other B_*/C_*/D_* producers: no `keep='last'`-over-parallel-concat survivor concern.

## Recommendations
1. **A_04**: oracle-fix-first (A_01 lane) — AE proves materiality + engineers; DS deploys under never-widen sign-off + per-script audit record.
2. **D_02**: AE confirm the `parts` append-concat is not `keep='last'`-deduped-over-ties; if it is, it joins A_04's lane; else no action (the fee_rates dedups are deterministic).
3. **CLASS-I scripts**: no standalone fix (CTO §2); explicit provenance+total-order hardening folds into each script's GLDINC incremental as 0-diff (trivially never-widen).
4. **E_* diagnostics**: classify assembly in the deferred low-pri batch.
5. **Cross-tree (inf/cot)**: forked copies likely carry the same loader shapes — re-run this code-read census per tree (fixes route per-firm). COO decomposes ownership/sequencing.
