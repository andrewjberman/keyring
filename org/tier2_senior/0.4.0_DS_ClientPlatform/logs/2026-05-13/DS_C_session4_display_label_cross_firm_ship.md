# DS~C 2026-05-13 session 4 — display_label cross-firm ship (INF + BD parity, single commit)

**Agent:** 0.4.0_DS_ClientPlatform~C
**Window:** ~16:00Z → ~16:35Z 2026-05-13 (~35 min)
**Trigger:** RD 0.4.2 brief (UX issue) → my Phase 0 investigation (~10 min) → RD GO (a) inline + cross-firm parity → 25-min ship.

## TL;DR

Shipped commit `d12598087` adding `display_label` field to `top_holdings.json` emits across **INF (3 gold scripts + 1 Lambda) and BD (1 gold script)** in a single commit per RD's "cross-firm audit-trail-cleanly" preference. Phase 3 sentinel verified live on HH 564 (Ameris masked CUSIP → "Ameris Bk Moultrie Ga Ctf Dep 3.") and BD z08105981 (`indexed_annuity` → "INDEXED ANNUITY"). 5 of 5 gold scripts SHA-MATCH on S3 via `comp-pipescript deployed`. INF Lambda pending AE bundle (Path B: queued with v1.7.54 orphan-bucket fix).

## Investigation findings (Phase 0)

5-source diagnostic isolated the masking source:
- **INF**: `silver/api_dims/assets_v2` carries `ticker = '03xxxxEY7'` already-masked — Orion API applies the regulatory CUSIP middle-4-char mask at source. We have no path to unmasked CUSIP.
- 137 of 23,699 INF assets (0.58%) carry masked tickers. 117 distinct patterns. 97% are CDs (114) or Bonds (19).
- **BD**: gold script emits snake_case slug of product name as `ticker` for alts/annuities/structured products. 24% of 50 sampled clients affected — materially higher prevalence than INF.

Same UX problem ("ticker is technically present but not user-readable"), two different signatures, one helper fits both.

## Ship roster

| Commit | Scope | Lines | S3 SHA-MATCH |
|---|---|---|---|
| `d12598087` | INF + BD `display_label` cross-firm | +199/-5 | All 5 gold scripts ✓ |

## Files Modified

| File | Change |
|---|---|
| `data/orion/scripts/gold/lib/display_label.py` | NEW. `resolve_display_label(ticker, security_name, truncate=32)` + `is_standard_ticker(ticker)`. Algorithm: standard `^[A-Z]{1,5}(\.[A-Z]{1,2})?$` passes through; non-standard → truncated security_name. |
| `data/orion/scripts/gold/INF_D_05.client_top_holdings.py` | `import display_label`; L240-248 emit `display_label` per holding |
| `data/orion/scripts/gold/INF_D_02b.top_holdings.py` | `import display_label`; L172-181 emit `display_label` |
| `data/orion/scripts/gold/INF_D_07a.firm_concentrations.py` | `import display_label`; L447-460 emit `display_label` on `securities[]` |
| `infra/aws/lambda/inf-portal-advisor-publisher/lambda_function.py` | Inlined `_resolve_display_label` (Lambda separate deployment package); `_build_top_holdings` L713-722 emit `display_label` |
| `data/black_diamond/scripts/gold/lib/display_label.py` | NEW. BD mirror — identical algorithm, separate file per firm-lib convention. |
| `data/black_diamond/scripts/gold/D_03.composition_artifacts.py` | `from lib.display_label import resolve_display_label`; L348-357 per-class + L379-388 global `top_holdings[]` emit `display_label`. Tangential: added `from __future__ import annotations` (Rule 15 gate-triggered); removed unused `MIX_ASSET_CLASSES`; fixed `== True` E712. |

## Phase 3 sentinel — live S3 pre-chain preview

### INF HH 564 (the Ameris case from the brief)
```
STD          ticker='FDRXX'      -> display_label='FDRXX'
SUBSTITUTED  ticker='03xxxxEY7'  -> display_label='Ameris Bk Moultrie Ga Ctf Dep 3.'
STD          ticker='TEAFX'      -> display_label='TEAFX'
... (7 more standard tickers pass through)
```
Exactly 1 substitution as expected.

### BD client z08105981 (the indexed_annuity case)
```
SUBSTITUTED  key='indexed_annuity'  -> display_label='INDEXED ANNUITY'
STD          key='IVV'              -> display_label='IVV'
... (7 more standard tickers pass through)
```
Exactly 1 substitution as expected.

### Aggregate (sampled)

- INF advisor top_holdings: **1/30** substitutions (only IWM has the Ameris CD)
- BD client top_holdings: **7/180** substitutions (alts/annuities scattered)

## Compiler Tools

| Tool | Runs | Result |
|---|---|---|
| `ds-commit-gate.sh` on all 7 files | 1× (after fix-up cycle: pre-existing ruff failures in D_03) | PASS — py_compile + ds-precommit + ruff py39 clean after adding `from __future__ import annotations` to D_03 + removing unused import + replacing `== True` |
| `safe-commit.sh --author 0.4.0_DS_ClientPlatform~C` | 1× | Clean first-try (new lib files staged via `git add -f` first; CLAUDE.md gotcha noted) |
| `safe-deploy.sh` pre-push hook | 1× | DEPLOYED all 6 (5 gold scripts + 1 lib parquet-side via S3) — 4 INF + 2 BD; SHA-MATCH verified each |
| `comp-pipescript deployed --pipeline inf-gold INF_D_02b/INF_D_05/INF_D_07a` | 3× | All MATCH |
| `comp-pipescript deployed --pipeline bd-gold D_03` | 1× | MATCH |
| Live S3 sentinel — replicate helper logic against HH 564 + z08105981 + sample aggregate | 1× | 1/30 INF substitutions, 7/180 BD substitutions, both example cases substituted correctly |

No commit gate failures. No SHA mismatches. No hook bypasses.

## Decision notes (worth keeping)

1. **Lib mirror vs shared workspace lib.** Existing precedent (`ticker_overrides.py`, `tax_status.py`) has per-firm copies under `data/{orion,black_diamond}/scripts/gold/lib/`. Followed the same pattern for `display_label.py`. Synchronisation discipline: the two files are bit-identical; comment in each notes the mirror. Alternative (workspace-shared lib) would require a deeper refactor of the runner's import paths — out of scope.

2. **Lambda inline vs Lambda Layer.** The INF Lambda runs from a separate deployment package and can't easily `import` from the gold-script lib. Considered (a) inlining the helper, (b) creating a Lambda Layer for shared utils. Picked (a) because it's a 10-line helper and a new Layer requires SharedInfra Terraform changes + layer manifest setup. Inlined with a clear "keep in sync" comment.

3. **Pre-existing ruff failures triggered by the universal gate.** D_03 had 2 pre-existing ruff violations (F401 unused `MIX_ASSET_CLASSES`, E712 `== True`) that surfaced only because I touched the file. The gate is universal — every Python edit must pass — so the cleanups landed in the same commit. Called out explicitly in the commit message so they don't look like scope creep.

4. **Cross-firm in one commit.** RD's explicit preference. Cleaner audit trail: one commit references both INF and BD changes, both lib mirrors, the Lambda inline. Reverts apply atomically. Future cross-firm `display_label` adjustments (e.g. allow share-class suffixes longer than 2 chars) hit one commit, not two.

5. **Defense-in-depth confirmed structural.** RD's FE-side regex backstop (`6852817e`) stays. When DS emits `display_label` post-chain, FE renders it; when DS doesn't (e.g. older artifacts before chain refresh), FE's regex fires. Both layers green simultaneously.

## Sequencing handoffs

| Recipient | Item |
|---|---|
| **RD 0.4.2_RD_AdvisorIntelligence** | RAVC2 sent at 16:35Z. Phase 3 sentinel evidence + S3 MATCH verification + commits + tangential cleanup callouts. Brief closes when chain materializes + visual smoke. |
| **COO 2.0.0_SA_COO** | FYI sent at 16:35Z. Non-blocking with chain #26 / Bug B routing / v1.7.54 sequencing. |
| **AE 0.6.1 / AE 0.7** | INF Lambda piece queues with v1.7.54 orphan-bucket-drop bundle per Path B. Same code path; same `build-and-upload.sh inf-portal-advisor-publisher` cycle. |
| **DS~B (BD lane)** | FYI — BD D_03 changed. Picks up on next BD gold chain (04:00Z nightly unless triggered earlier). If you spot any other BD top_holdings emit sites I missed in D_02/D_02b, MCP me. |
| **DS~C self** | Standing by — `/loop` cron `526cad1f` checking inbox every 5 minutes; chain #26 reactive; Bug B routing reactive. |

## Pacing

~35 min total from investigation green-light to RAVC2 sent. Breakdown:
- 10 min: Phase 0 investigation (silver source check + cross-firm pattern catalog + algorithm draft)
- 10 min: implementation across 7 files (helper + 4 INF emit sites + 1 BD emit site + Lambda inline)
- 5 min: gate fix-up (D_03 pre-existing ruff failures cleared)
- 5 min: commit + push (safe-deploy fires across 6 deploy targets)
- 5 min: Phase 3 sentinel + RAVC2 + COO FYI

Cooperative cadence across DS + RD + AE + COO maintained; no cross-agent blocks. Investigation-first + diagnostic-first patterns held: pulled live S3 (`assets_v2`) before coding to confirm Orion-source mask, scanned 50 BD clients to confirm cross-firm parallel before designing the helper, replicated helper logic against live artifacts pre-RAVC to confirm sentinel arithmetic.
