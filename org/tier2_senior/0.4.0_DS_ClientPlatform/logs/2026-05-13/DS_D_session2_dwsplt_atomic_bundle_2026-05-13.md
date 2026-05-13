# DS~D 2026-05-13 session 2 — ADVI_DWSPLT atomic bundle ship (silver Rule 17 + INF gold consumer migration)

**Agent:** `0.4.0_DS_ClientPlatform~D`
**Window:** ~14:33Z 2026-05-13 (boot) → ~18:07Z 2026-05-13 (atomic commit + push + RAVC2). ~3h35m total wall; ~2h15m hands-on-code during a CTO/COO ping-pong cycle that resolved cleanly.
**Triggers (chronological):**
1. Andrew "0.4.0_DS_ClientPlatform~D. Boot up." (14:33Z)
2. Inbox carry-over: DE Brief #9 RAVC4 ACK + AE 0.6.1 chain #22 RAVC1+RAVC2 (closed in session 1; this session 2 starts at COO GO)
3. COO 2.0.0_SA_COO GO Phase 0 silver/transactions probe (14:36Z, ~2-3h scope)
4. Phase 0 ship `984ae22b3` + bucket-vs-label audit (~17:04Z) → CTO §3.3a/§3.3b clarification
5. CTO `d59af9f7c` DWSPLT PRD v0.1 + COO co-sign + Andrew path-(a) ratify (17:11-17:30Z)
6. COO TO-2/3 atomic-bundle dispatch (~17:33Z) + Path A+A.2 ratification (~17:00Z)
7. Two surface-before-ship triggers caught structural issues (LEGACY+NEW coexistence; 5 LEGACY-only cols at INF_A_00 with no REST source)
8. Atomic commit `f69461357` (18:04Z) + safe-deploy SHA-MATCH + CLOUD push
9. RAVC2 to COO + AE 0.6.1 + COO RAVC4 ACCEPT (18:07Z)

---

## TL;DR

**12-file atomic bundle + 1 new shared lib shipped in commit `f69461357`** under the freshly-codified CLAUDE.md Rule 17 (added by Andrew on the canonical DWSPLT incident earlier in the day) + DWSPLT PRD v0.1 (CTO `d59af9f7c`, joint converged scope after a 3-reversal cross-traffic cycle that the framing-discipline rule resolved cleanly).

Two surface-before-ship triggers materially shaped the final scope:
- Surface 1 (LEGACY+NEW silver coexistence): CTO+COO+Andrew converged on Path A.2 source-selection pattern — cache reader picks the latest bronze-name canonical snapshot rather than directory-concat across schema-incompatible partitions.
- Surface 2 (INF_A_00 has 5 LEGACY-only cols with no REST source): in-place empirical probe of accounts_v2 silver schema (read-only, no code change) resolved Path α-feasibility — 3 of 5 cols direct from accounts_v2 + 2 derive from rep_id via shared lib helper, collapsing scope from "potential 3-4 day mega-atomic" to "9-12h tractable bundle."

ds-commit-gate PASS on every file (py_compile + AST + ruff py39). safe-commit.sh clean (no owned-paths violation; no FORCE-BYPASS). safe-deploy.sh pre-push hook SHA-MATCH all 12 files on `s3://opal-data-inf/code/`. Chain validation pending AE 0.6.1 dispatch (PROD trigger is AE-exclusive per protocol).

---

## Ship roster

| Time (UTC) | Commit | Scope |
|---|---|---|
| ~16:00Z | `984ae22b3` | docs(silver-txn-probe) Phase 0 four-phase probe brief (path-(a) feasibility synthesis) |
| ~16:11Z | `6383ed987` | log(DS~D session1 2026-05-13) |
| ~17:30Z | `d59af9f7c` (CTO) | docs/architecture/ADVI_DWSPLT.md PRD v0.1 + project JSON + REGISTRY |
| ~18:04Z | **`f69461357`** | **feat(ADVI_DWSPLT TO-2/3/5): atomic bundle — silver Rule 17 strict + INF gold consumer migration** |

`f69461357` diff: 12 files / +1040 / −562 LOC + 1 NEW shared lib (`lib/inflection_rep_scope.py`).

---

## Files modified (atomic bundle)

| File | Project task | Scope |
|---|---|---|
| `data/orion/scripts/silver/convert_transactions_to_silver.py` | TO-2 silver Rule 17 strict | Remove `output_cols` + rename map + `_derive_category` + `fillna("Unknown")`; add `coerce_silver_ids()` on bronze ID names; keep mechanical dict-decode + dedup + metadata + rep_id JOIN |
| `data/orion/scripts/silver/convert_orion_to_silver.py` | TO-5 accelerated LEGACY decom | Comment-out `build_trn_silver()` call from `main()`; preserve `build_accounts_dim` + `build_aum_silver` writers (DS~B Bug B orthogonality) |
| `data/orion/scripts/gold/lib/txn_cache_reader.py` | TO-3a cache A.2 | Replace directory-concat with `_load_canonical_snapshot` source-selection; fail-loud on missing canonical cols; CACHE_COLUMNS shrinks 16 LEGACY names → 5 bronze names |
| `data/orion/scripts/gold/lib/inflection_rep_scope.py` | TO-3b new shared lib | NEW — `derive_advisor_key(rep_name)` + `derive_rep_bucket(rep_name)`; mirrors LEGACY `_advisor_key`/`_rep_bucket` slug-normalize + firm/routing membership |
| `data/orion/scripts/gold/INF_A_-1.materialize_txn_cache.py` | TO-3b materializer | Adjust to canonical-snapshot pattern (calls `_load_canonical_snapshot`); ID coercion on bronze names |
| `data/orion/scripts/gold/INF_A_00.accounts_dimension.py` | TO-3b α+β | Full refactor — accounts_v2 silver as primary source + walk-back-to-healthy + 1:1 cosmetic rename (Path α direct: `representative_name → rep_name`, `last_name → client_last_name`, `account_number → account_code`, `account_type → reg_type`) + Path β derivation (advisor_key + rep_bucket from rep_name via shared lib) + minimal txn cache for trade_date bounds + registrationName display |
| `data/orion/scripts/gold/INF_A_01.advisor_assignments.py` | TO-3b | accounts_v2 silver source (txn cache no longer needed); collision detection degrades to point-in-time only per `rep_id_is_historical=False` semantic (acceptable) |
| `data/orion/scripts/gold/INF_A_03.positions_cube.py` | TO-3b | Bronze-name reads on cache + 1:1 cosmetic rename at load |
| `data/orion/scripts/gold/INF_C_01.canonical_nna.py` | TO-3c yaml v3 + source-select | `_load_cashflow_taxonomy` auto-detects yaml v3 (`trans_type_desc` key) with v2/v1 fallback; `load_all_transactions` replaced directory-concat with source-selection (Path A.2 mirror); `_normalize_silver_schema` replaced LEGACY+NEW coalesce shim with 1:1 cosmetic rename map; REQUIRED_COLS drops `activity_category` (informational only post-Stage-0b) |
| `data/orion/scripts/gold/INF_D_06.cash_drag.py` | TO-3d compat-shim removal | Removed rename-on-the-fly compat-shim (was line 267-274 — silent-fallback class §3.3a violation); `load_qualifying_trades` replaced with source-selection + 1:1 cosmetic rename (explicit, auditable) |
| `data/orion/scripts/gold/INF_B_02.canonical_lots.py` | TO-3e mechanical | Source-selection + 1:1 cosmetic rename |
| `data/orion/scripts/gold/INF_build_canonical_prices.py` | TO-3e mechanical | Source-selection + 1:1 cosmetic rename |

**Descoped to follow-on tech debt (CTO §3.3a/§3.3b ratify):**
- INF_D_00.portal_aggregates.py + INF_D_02.advisor_client_detail.py — have pre-existing forward-rename shims (lines 437-459 + 1005-1012); §3.3b aesthetic violation only, not §3.3a load-bearing. Surfaced as follow-on cleanup TO (DS~A natural fit per COO).

---

## CTO §3.3a/§3.3b semantic clarification (worth absorbing)

Captured per COO directive 18:06Z. The §3.3 rule has two implicit sub-classes:

**§3.3a (load-bearing fail-loud):** silent-fallback / silent-translation patterns. Example: `if 'trans_type_desc' missing, fall through to 'type_desc'`. Would absorb both LEGACY and NEW schemas transparently. Hid the dual-writer regression in DS~A's audit. **REQUIRED REMOVAL.**

**§3.3b (aesthetic):** forward-rename patterns. Example: `df.rename(columns={'amount': 'trans_amount'})`. REQUIRES the upstream col to exist; fails loud if missing. **REMEDIATE OPPORTUNISTICALLY**, not a load-bearing concern.

INF_D_06's removed shim was §3.3a (silent-fallback). INF_D_00/D_02's remaining shims are §3.3b (forward-rename) — defer to cleanup TO. Future PRD ratchet may codify the split formally.

---

## Surface-before-ship in action (two triggers, both resolved cleanly)

### Surface 1: PRD §6 7-day-soak structural impossibility (~17:36Z)

**Empirical finding:** LEGACY `convert_orion_to_silver.py` writes daily per-day silver partitions in LEGACY names AT THE SAME TIME the NEW writer puts down its bronze-named snapshot. Original PRD plan (TO-2/3 ship first → 7-day soak → TO-5 retire LEGACY) was structurally impossible: cache reader concat across 1,512+ LEGACY-named partitions + 1 NEW-named snapshot creates schema-incompatible rows; rename-shim translation would violate the §3.3 rule the bundle was explicitly enforcing.

**Resolution (joint CTO+COO+Andrew convergence ~17:00Z):** Path A + Path A.2:
- Path A: accelerate TO-5 LEGACY TRN-write decom into the atomic bundle (eliminates coexistence permanently). accounts_dim + aum_snapshot writers preserved per Bug B orthogonality.
- Path A.2: cache reader source-selects the latest canonical bronze-name snapshot rather than directory-concat. Source-selection is gold-tier business logic (Rule 17 permits); translation/rename-shims are forbidden (§3.3 fail-loud).

### Surface 2: INF_A_00 has 5 LEGACY-only cols with no REST source (~17:45Z)

**Empirical finding:** INF_A_00's `KEEP_COLS` includes 5 LEGACY-only cols (`rep_name`, `advisor_key`, `rep_bucket`, `is_managed`, `client_last_name`) that don't exist in REST bronze. Initial framing risked "potential 3-4 day mega-atomic refactor."

**In-place probe while held (~17:47Z):** read-only S3 inspection of accounts_v2 silver schema. Empirical resolved Path α-feasibility definitively:

| LEGACY col INF_A_00 needs | accounts_v2 silver equivalent | Path |
|---|---|---|
| `rep_name` | `representative_name` | α direct (1:1 cosmetic rename) |
| `is_managed` | `is_managed` (identical) | α direct |
| `client_last_name` | `last_name` | α direct |
| `advisor_key` | DERIVED from rep_name (slug-normalize via shared lib) | β derive |
| `rep_bucket` | DERIVED from rep_name (firm/routing/individual via shared lib) | β derive |

3 of 5 direct in accounts_v2 silver; 2 of 5 mechanically derivable. Scope collapsed to 9-12h tractable.

**Verified rep_id alignment** during probe:
- accounts_v2 silver rep_id values {3, 6, 11, 12} = EXACTLY LEGACY `INFLECTION_REP_IDS` allowlist
- `representative_name` values produce canonical slugs identical to LEGACY `_advisor_key`:
  - rep_id=3 "Inflection Wealth Management" → `inflection_wealth_management` / bucket=firm
  - rep_id=6 "Joe Brandenburg" → `joe_brandenburg` / individual
  - rep_id=11 "Patrick Scanlan" → `patrick_scanlan` / individual (note: NOT "IWM Keil" as I initially guessed in an earlier draft of the shared lib — corrected after empirical)
  - rep_id=12 "Peter Lee" → `peter_lee` / individual
- accounts_v2 silver `account_type` vocabulary IDENTICAL to LEGACY `reg_type` (verified against `lib/tax_status.py` empirical map) → tax_status derivation works unchanged

**Resolution (joint convergence ~17:47Z):** Path α + β hybrid scope locked. Cache-reader surface stays minimal (`accountId, transDate, ticker, noUnits, registrationName`).

### Discipline pattern review

Both surfaces correctly applied the framing-discipline rule that was codified earlier in the day (commit `69bf69394` and CTO prompt parallel `a3cc3651e`):
1. Worker surfaces structural issue mid-dispatch (NOT mid-code-change)
2. COO holds + MCPs CTO + surfaces Andrew BEFORE flipping framing alone
3. Joint converged call returns as ONE unified message
4. Worker resumes with locked scope

CTO's own note in the convergence: *"I had the architectural call right the first time. Switching to Shape A when you surfaced it = sacrificing Rule 17 strict for in-flight-dispatch continuity. Wrong trade."* The discipline rule that captured this lesson is THIS afternoon's commit; the pattern works.

---

## Architectural wins (worth carrying forward)

1. **Source-selection vs translation pattern (CTO A.2):** Reading the canonical file (source-selection) is gold-tier business logic — Rule 17 permits. Translating field names on-the-fly (rename-shim) buries upstream provenance — Rule 17 forbids. The distinction unblocks Rule 17 strict architecture without forcing impossible coexistence-window engineering.

2. **accounts_v2 silver as REST-canonical accounts dim source:** Empirically confirmed has direct equivalents for 3 of 5 LEGACY-only cols + supports tax_status derivation via `account_type` ≡ `reg_type` vocabulary alignment. Reduces txn-cache surface to truly-transactional fields (accountId + transDate + per-position fields for cumsum).

3. **Walk-back-to-healthy on Bug B defense:** INF_A_00/A_01 inherit Bug B (empty-partition silent fallback) risk via accounts_v2 silver source. Walk-back-to-latest-with-≥100-rows guards within 14 days; raises RuntimeError surfacing "Bug B has spread" if no healthy partition found. Pattern from `feedback_walk_back_to_healthy_snapshot.md`.

4. **Shared lib for cross-script derivation (`lib/inflection_rep_scope.py`):** advisor_key + rep_bucket derivation lifted into shared helper. Both INF_A_00 + INF_A_01 use it; LEGACY `_advisor_key`/`_rep_bucket` in `convert_orion_to_silver.py` retained as source-of-truth reference. When LEGACY is eventually fully decommissioned, the shared lib stays canonical.

5. **§3.3a/§3.3b spirit-vs-letter distinction (CTO):** silent-fallback class is load-bearing; forward-rename class is aesthetic. Lets us ship Rule 17 architecture without forcing 3000-line file refactors when the pre-existing shims are fail-loud already.

---

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `comp-pipescript io` per gold script | Skipped — no I/O graph change at column-level (bronze cols = REST returns); structural schema inspection via parquet headers was authoritative | n/a |
| `ds-commit-gate.sh` per file | 12× (silver + cache reader + materializer + INF_A_-1/00/01/03 + lib + INF_C_01 + INF_D_06 + INF_B_02 + INF_build_canonical_prices) + several re-gates after ruff unused-import fixes | All PASS final |
| `.tools/safe-commit.sh` | 1× atomic | Clean (no owned-paths violation; no FORCE-BYPASS) |
| `safe-deploy.sh` pre-push hook | 1× (push of `f69461357`) | DEPLOYED + SHA-MATCH on 12 files |
| `comp-pipescript deployed` post-push | Implicit via safe-deploy SHA-MATCH | All 12 MATCH |
| Phase 0c live REST probe | Deferred (bronze parquet IS the REST response per pull script docstring) | n/a |
| `comp-validate` post-chain | Pending AE chain dispatch + completion | (TBD) |

Empirical S3 read-only probes during surface-before-ship:
- `aws s3 cp s3://opal-data-inf/silver/transactions/{2026-05-12,2026-05-13}.parquet` — confirmed LEGACY 31-col vs NEW 18-col diff
- `aws s3 cp s3://opal-data-inf/bronze/transactions/2026-05-13.parquet` — confirmed REST bronze has 31 cols (not 13 as docstring claims; C.4 pattern)
- `aws s3 cp s3://opal-data-inf/silver/api_dims/accounts_v2/snapshot_date=2026-05-12/data.parquet` — confirmed accounts_v2 silver schema has 45 cols incl. representative_name/is_managed/last_name + account_type vocabulary identical to LEGACY reg_type
- 47 distinct transTypeId verified in NEW bronze (vs TO-1 dict 47-entry coverage — 100% match per DS~B's `186ba53df` empirical)

---

## Files Modified

| File | Change |
|---|---|
| `data/orion/scripts/silver/convert_transactions_to_silver.py` | Rule 17 strict refactor; remove output_cols/rename map/_derive_category/fillna; bronze-name passthrough + dict-decode + dedup + metadata; ID coerce on bronze names |
| `data/orion/scripts/silver/convert_orion_to_silver.py` | Accelerated TO-5: TRN-write block decommissioned via main() skip; preserve accounts_dim + aum_snapshot |
| `data/orion/scripts/gold/lib/txn_cache_reader.py` | A.2 source-selection (`_load_canonical_snapshot`); CACHE_COLUMNS bronze-name minimal tuple (5 cols); fail-loud REQUIRED_CANONICAL |
| `data/orion/scripts/gold/lib/inflection_rep_scope.py` | NEW — `derive_advisor_key`/`derive_rep_bucket` from rep_name slug-normalize + firm/routing membership |
| `data/orion/scripts/gold/INF_A_-1.materialize_txn_cache.py` | Adjust to canonical-snapshot pattern; bronze-name ID coerce |
| `data/orion/scripts/gold/INF_A_00.accounts_dimension.py` | Full refactor: accounts_v2 silver primary + walk-back + α+β derivation + minimal txn cache (trade_date bounds + registrationName) |
| `data/orion/scripts/gold/INF_A_01.advisor_assignments.py` | Full refactor: accounts_v2 silver-only source + walk-back + α+β derivation |
| `data/orion/scripts/gold/INF_A_03.positions_cube.py` | Bronze-name reads on cache + 1:1 cosmetic rename at load |
| `data/orion/scripts/gold/INF_C_01.canonical_nna.py` | yaml v3 auto-detect (trans_type_desc key w/ v2 fallback); source-selection replaces directory concat; 1:1 cosmetic rename replaces LEGACY+NEW coalesce shim; REQUIRED_COLS drops activity_category |
| `data/orion/scripts/gold/INF_D_06.cash_drag.py` | §3.3a silent-fallback shim REMOVED (was line 267-274); source-selection + 1:1 cosmetic rename (explicit, auditable) |
| `data/orion/scripts/gold/INF_B_02.canonical_lots.py` | Source-selection + 1:1 cosmetic rename |
| `data/orion/scripts/gold/INF_build_canonical_prices.py` | Source-selection + 1:1 cosmetic rename |

---

## Current State

| Item | Status |
|---|---|
| ADVI_DWSPLT atomic bundle `f69461357` | SHIPPED CLOUD + safe-deploy SHA-MATCH ALL 12 files |
| ds-commit-gate.sh all files | PASS |
| Chain validation (inf-gold-trigger gold-d) | PENDING AE 0.6.1 RAVC1/2 (PROD trigger is AE-exclusive per protocol) |
| COO RAVC4 ACCEPT on bundle | RECEIVED 18:07Z |
| Follow-on §3.3b cleanup TO (INF_D_00/D_02) | QUEUED to DS~A natural fit |
| Follow-on TO-4 yaml v3 promotion | QUEUED to DS lane per COO routing |
| Follow-on TO-5 full LEGACY code removal | QUEUED post 7-day soak observation |

---

## Next Steps

1. **[AE 0.6.1]** Fire `inf-gold-trigger` `gold-d` with `snapshot_date=2026-05-13`. Surface RAVC1 (chain fired) + RAVC2 (exit code + empirical pre/post platinum) to me + COO + CTO + Andrew.

2. **[Self — passive]** Absorb AE RAVC1/2. If chain GREEN: confirm sentinels (silver row count, gold/dimensions/accounts_dimension_latest 857 rows, advisor_assignments 4 rep_name distribution, canonical_nna `trans_type_desc` zero-Unknown). RAVC2 to COO + CTO + Andrew with empirical evidence.

3. **[Self — passive]** If chain RED: surface error via comp-validate output + raw chain logs. Most likely surfaces: yaml v3 path (waiting on TO-4 promotion; INF_C_01 has v2 fallback) or accounts_v2 Bug B (walk-back-to-healthy should defend within 14 days). Rollback path: `git revert f69461357`.

4. **[DS~A or DS~B per COO routing]** Author follow-on TO for §3.3b INF_D_00/D_02 cleanup. Cite CTO §3.3a/§3.3b split + this commit + the spirit-vs-letter framing.

5. **[Bench-clear after chain RAVC closes]** Ready for next dispatch.

---

## Memory feedback captured (post-session candidates)

- **Source-selection vs translation pattern (CTO A.2):** worth a memory entry. The distinction "reading the canonical file is gold business logic; translating field names is silver violation" generalizes beyond DWSPLT.
- **In-place empirical probe while held (Surface 2 pattern):** reading parquet headers / S3 schemas while waiting for joint adjudication produces sharper convergence calls + saves rework. Worth codifying.
- **§3.3a/§3.3b split (CTO):** spirit-vs-letter distinction sharpens the Rule 17 enforcement. Worth folding into a future PRD ratchet.

---

## Pacing reflection

Two surface-before-ship triggers, both caught BEFORE code touch — that's the discipline working. The first (LEGACY+NEW coexistence) was structural; without surfacing it, I'd have shipped a §3.3 violation by necessity. The second (5 LEGACY-only cols) was scope-sizing; without the in-place empirical probe, the joint call would have locked a "potential 3-4 day mega-atomic" framing that didn't match the empirical state.

The CTO/COO ping-pong cycle earlier in the day (pure-Rule-17 → Shape A → pure-Rule-17 → Shape A → pure-Rule-17 final) felt frustrating in the moment but produced the right scope. The framing-discipline rule codified `69bf69394` is operating as designed — workers hold + surface; execs converge before flipping. DS~B's parallel TO-1 ship (`186ba53df`, 4,299 'Unknown' → 0) removed the operational pressure that would have forced Shape A premature.

The single biggest empirical that shaped the final scope was the accounts_v2 silver schema probe (5 cols, ~5 min wall, read-only). It's the kind of work that makes joint convergence cheap — surface a problem, do empirical work in-place rather than waiting, return with sharpened framing. Save it as a pattern.

The ~3h35m total wall (with surface-before-ship pauses) inside the 9-12h estimate is good pacing. The estimate was correct because both surface-before-ship triggers were caught early; the empirical probes resolved them without burning code-touch time.
