# Session — 0.4.0_DS_ClientPlatform~XYZ — 2026-04-17 (session XYZ)

**Agent:** 0.4.0_DS_ClientPlatform~XYZ
**Window:** ~15:56Z (register) — 17:25Z (last MCP)
**Scope:** Undershoot-tapering brief (docs/briefs/ds-brief-xyz-undershoot-tapering.md) — diagnose the 2,629-account accuracy gap from the undershoot side, deliver RCA for Buckets 1-5, ship fix for the stale-unrealized-key bug that zeroed 51 fresh accounts in the tonight run.

## Current State

**HEAD:** `2a69b97e` (fix(B_01): key silver/unrealized to snapshot date — retire stale rolling parquet). Pushed to `origin/CLOUD`, S3 MATCH confirmed.

**Fix shape:** Replaced module-level `S3_UNREALIZED_KEY = 'silver/unrealized/unrealized_gain_loss.parquet'` with `_resolve_unrealized_key(snapshot_date)` helper (tries d, d-1, d-2 via head_object; hard-fails otherwise). Threaded across 4 call sites (lines 563, 726, 879, 2146 post-edit).

**Rule 3 (CP-DS1 PIVOT 2 Gate 3) root cause:** The `unrealized_gain_loss.parquet` rolling key froze on 2026-03-29 because commit `158a0026` wired the new nightly pipeline to write only date-partitioned parquets and left the monolith un-rewritten (AE brief 2026-04-17 ~17:15Z). Every account whose positions opened after 03-29 was absent from the stale snapshot → Rule 3 evaluated `silver_absent=True` → force-closed all lots (units/cost/MV/gain set to 0). Matches Bucket 2's signature exactly (51 accts / $10.7M AUA / 1,909 lots with current_units=0, is_open=False, correct prices). Confirmed on sample account `z0822744801` — 24 Buys on 2026-04-10, zero Sells, zero force_close diagnostics, yet 24 lots zeroed in run11.

**Simulation against current silver/unrealized/2026-04-15.parquet (accounting for Rule 1, Rule 2, PIVOT-6 cap):**
  - 31 of 51 B2 accts are clean recoveries (silver noncash $6.96M, uncapped expected_mv $9.62M)
  - 8 caught by Rule 1 (alloc_aua < $100 — correctly drained accts, silver AUA $165)
  - 17 caught by Rule 2 (expected_mv > 2× silver + $50K — legitimate lot-inflation close, silver AUA $737K vs expected_mv $7.99M)
  - Post-PIVOT-6 cap expected B2 recovery on rerun: **$6.96M** (bounded by silver noncash)
  - B1 top-10 undershoot: all 10/10 have DIVZ (cusip 210322731) in current silver/unrealized → sell-correction cusip-veto (line ~1188) now fires, DIVZ lots stay open. Rough gap across top-10 ~$6.0M expected recovery.

**AE context:** AE's c270a9b2 one-off refresh of the rolling key at 16:55Z was reverted in git (misread of problem), but the S3 file upload was left in place. Monolith does not need to be maintained; date-partitioned keys are authoritative. No AE code work required — the B_01 fix is the entire scope.

## Session Arc (chronological)

### 1. Startup (~15:56Z)
  - `register_agent(0.4.0_DS_ClientPlatform~XYZ)` — PID 19004.
  - check_inbox + get_agent_status — no pending, then GO message arrived (inbox-watch event).
  - Compiler context: `.comp-graph/.agent_context` — SERIAL=~XYZ, TO_ID=ds-brief-xyz-undershoot-tapering.

### 2. Brief intake
  - Read `docs/briefs/ds-brief-xyz-undershoot-tapering.md`.
  - Scope: own UNDERSHOOT side of Run 11 accuracy gap; 2,629 accts >5% off silver, ~1,080 running below silver, plus zero-MV and zero-lot accts.
  - 5 buckets: B1 moderate undershoot 925 / $256M / -$28M; B2 zero-MV lots 51 / $10.7M; B3 large undershoot 77 / $15M; B4 zero-lot 03/2025 12 / $4.4M; B5 cash-only 15 / $2.1M.

### 3. B1 cash-vs-lot-coverage split (Phase 1 blocking diagnostic)
  - Computed noncash_silver_mv = account_market_value - cash_market_value per account.
  - Population (run11_mv 5-25% below silver AUA): 910 accts / -$28.0M net (matches brief).
  - Split:
    - **Cash gap** (run11 within 5% of noncash_silver_mv): 258 accts / -$5.8M — expected, no fix.
    - **Lot-coverage gap**: 652 accts / -$22.2M — real work. 78% retail (IRA/RothIRA/Brokerage). noncash_pct_gap tight clustering 7-13% → systematic.
  - MCP report sent.

### 4. B2 zero-MV lots RCA (Phase 2)
  - Sample-set inspection: 1,908/1,909 lot rows have `linear_interpolation` price_quality, REAL prices, but current_units=0 and is_open=False on every lot. Not a price bug.
  - Cross-ref silver/unrealized: ALL 51 accts appear with 507 position rows → silver is NOT stale; FIFO over-depleting.
  - Sample-acct depletion trace (z0822773771 97% cash, poor choice; pivoted to z0822744801 silver $2.30M / cash $38K / noncash $2.26M):
    - 24 Buys on 2026-04-10 (matches unrealized exactly)
    - ZERO Sells across 1000 silver/transactions partitions
    - 0 rows in rps_force_close_alerts + resolved
    - ALL 24 lot's current_units zeroed in run11
  - STOP sent per brief rule (candidate-(a) CP-DS1 territory).

### 5. B1 position-coverage forensic (top-10)
  - Classification of per-(acct,cusip) pairs across 10 largest-delta undershoot accts:
    - over_counted: 142 (run11 > unrl, normal FIFO tax-lot split)
    - extra_in_run11: 78 (closed lots leaked into run11)
    - matched: 63
    - missing: 27 (unrl has position, run11 has zero open lots)
  - Missing-cusip concentration: DIVZ (210322731, Polen Dividend Income ETF) missing in 10/10 top accts. CASH missing in 10/10 (expected). Others (CLIP, QQQ, SPHY, VGSH, BPRE) sparsely.
  - Unified-hypothesis assessment MCP sent: undershoot mirror of overshoot per Andrew/CTO framing, same unit-confidence uncertainty, but B2 specifically is ACTIVE over-depletion with no documented trigger — floor patch would MASK not FIX.

### 6. B4 / B5 diagnostics
  - B4: 7 accts (not 12 in brief; strict 03/2025 create filter) / $4.2M silver AUA / 100% noncash, all "No Account Type Assigned" / ZERO silver/transactions across 14 scanned dates. AE confirmed: BD export gap across 1000 partitions, 8 accounts (7 + z0822755411 outlier) never appeared. BD data-team escalation, not fixable in silver/gold.
  - B5: 14/15 cash-only confirmed (noncash ≈ 0). 1 outlier z0822755411 (SIMPLE, $88K noncash) forwarded to AE. Presentation gap only.

### 7. DIVZ name-change deep dive (Andrew hypothesis)
  - bd_assets_dim inspection:
    - DIVZ (210322731) asset_name="POLEN DIVIDEND INCOME ETF" (168,768 txns) — OLD name, single row
    - IDVZ (210322707) asset_name="OPAL INTERNATIONAL DIVIDEND INCOME ETF" (118,704 txns) — NEW name
    - Asymmetric rename: IDVZ renamed, DIVZ not
  - NAME_ALIASES in B_01 (lines 160-164):
    - `'OPAL DIVIDEND INCOME ETF': 'POLEN DIVIDEND INCOME ETF'` (confirms rename existed)
    - `'EVENTIDE HIGH DIVIDEND ETF': 'POLEN DIVIDEND INCOME ETF'`
    - `'OPAL INTERNATIONAL DIVIDEND INCOME ETF': 'OPAL INTERNATIONAL DIVIDEND INCOME ETF'` (no-op)
  - z0822744801 DIVZ buy recorded as "POLEN DIVIDEND INCOME ETF" with cusip 210322731 — consistent with dim. Alias map is collapsing correctly. **Name-change hypothesis ruled out as primary driver.**

### 8. Root cause: stale S3 key
  - B_01 line 447: `S3_UNREALIZED_KEY = 'silver/unrealized/unrealized_gain_loss.parquet'` (module-level constant, hardcoded rolling key).
  - `head_object` on that key: LastModified **2026-03-29 08:08:57 UTC**, 19 days stale. 7,244 unique accts, no z0822744801.
  - Date-partitioned keys exist in same prefix and are refreshed nightly (per AE brief, wired by commit 158a0026 which never re-wired the monolith).
  - Rule 3 path at lines 2119-2191 of B_01.holdings_lots.py runs BEFORE RPS synthetic injection and BEFORE sell-correction pass, zeroing ALL four lot fields (units/cost/mv/gain) for any account not in the stale set.
  - RCA MCP sent (20260417T163611Z).
  - Durable brief written: `docs/briefs/data-scientist-b01-stale-unrealized-key-2026-04-17.md`.

### 9. Fix implementation
  - Pre-checks: `comp-pipescript io B_01` → manifest unchanged; `comp-pipescript deployed B_01` → MATCH.
  - Edits:
    - Replaced module-level constant with `_resolve_unrealized_key(snapshot_date)` helper (d, d-1, d-2 fallback via head_object; FileNotFoundError otherwise).
    - `replace_all` on `_read_parquet_from_s3(S3_UNREALIZED_KEY)` → `_read_parquet_from_s3(_resolve_unrealized_key(snapshot_date))` across 4 call sites.
  - py_compile: passed.
  - `git commit --only --author="XYZ <XYZ@opal.agent>"` → SHA 2a69b97e.
  - `git push origin CLOUD` → up-to-date.
  - `aws s3 cp` → code/gold/B_01.holdings_lots.py uploaded.
  - `comp-pipescript deployed B_01` post-upload: MATCH.

### 10. Fix simulation (no runner fire)
  - Rolling unrl file state at 17:00Z: refreshed to 2026-04-17 16:55:37Z (AE one-off upload; code reverted but S3 file remains).
  - Both rolling and dated parquets now contain the same 7,330 accts / 93,951 rows — content-identical.
  - B2 post-fix classification (accounting for Rule 1, Rule 2, PIVOT 6 cap): **31 clean recoveries / $6.96M capped MV recovery, 8 Rule-1-closed (alloc<$100), 17 Rule-2-closed (expected_mv>>silver)**.
  - B1 DIVZ top-10: all 10/10 have DIVZ in current unrl → cusip-veto fires, expected recovery ~$6M across top-10.
  - Firm naive: +$17M delta pre-cap; actual rerun needed for post-cap number.

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/B_01.holdings_lots.py` | Replaced module-level `S3_UNREALIZED_KEY` constant with `_resolve_unrealized_key(snapshot_date)` helper (d/d-1/d-2 fallback, hard-fail otherwise). Threaded across 4 call sites. +27/-5 lines. Commit 2a69b97e. |
| `docs/briefs/data-scientist-b01-stale-unrealized-key-2026-04-17.md` | NEW — durable RCA brief for primary DS reference |
| `data/black_diamond/diagnostics/undershoot_xyz_bucket1_2026-04-15.py` / `.json` | NEW — B1 split diagnostic (910 accts → 258 cash / 652 lot-cov) |
| `data/black_diamond/diagnostics/undershoot_xyz_bucket2_2026-04-15.py` / `.json` | NEW — B2 zero-MV lot analysis (current_units=0 on all) |
| `data/black_diamond/diagnostics/undershoot_xyz_bucket2_unrealized_xref.py` | NEW — 51 B2 accts all in silver/unrealized |
| `data/black_diamond/diagnostics/undershoot_xyz_bucket2_depletion_trace.py` | NEW — z0822773771 / z0822744801 full txn+RPS history |
| `data/black_diamond/diagnostics/undershoot_xyz_bucket1_position_coverage.py` / `.json` | NEW — top-10 forensic (DIVZ 10/10 missing pattern) |
| `data/black_diamond/diagnostics/undershoot_xyz_bucket1_deep_2026-04-15.py` / `.json` | NEW — stuck-at-cost rejection (1.1% of open lots) |
| `data/black_diamond/diagnostics/undershoot_xyz_bucket4_5_2026-04-15.py` / `.json` | NEW — B4 zero-txn confirmation / B5 cash-only confirmation |
| `data/black_diamond/diagnostics/undershoot_xyz_fix_simulation_2026-04-15.py` / `.json` | NEW — post-fix recovery estimate w/ Rule 1/2/PIVOT-6 accounting |

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| Stale-unrl-key RCA | `docs/briefs/data-scientist-b01-stale-unrealized-key-2026-04-17.md` | Primary DS (durable ref) |
| AE audit request | (MCP 20260417T165401Z) | AE 0.6.0 — why rolling key froze on 03-29 + resume publish |

## Next Steps

- [**Primary DS (0.4.0_DS_ClientPlatform) / 2.0.0_SA_COO**] Coordinate QA runner fire on `bd-gold-qa-runner` (i-0090b823a4a0997e3) for snapshot_date 2026-04-15, `--single B_01` or equivalent. CP-DS1 Run 9 is pending per session_k; do not collide.
- [~XYZ] On rerun artifact: run before/after diagnostic. Verify (i) 31 clean-recovery B2 accts current_units > 0, (ii) post-fix MV ~$6.96M for 51 B2 accts, (iii) DIVZ lots open on all 10 B1 top-undershoot accts, (iv) firm MV delta shift vs silver noncash $1,660.3M.
- [~XYZ] Post-rerun: flag the 17 Rule-2-close accts to primary DS as a **separate** structural issue — FIFO has accumulated ~$8M of phantom units on accts where silver now reports pennies. Not blocking; worth its own TO.
- [**0.6.0_AE_PartnerETL**] Per AE brief, no code work needed. AE has clarified monolith wiring history (commit 158a0026).
- [~XYZ] Optional follow-up TOs if authorized: B1 non-DIVZ residual mechanism (-$22.2M minus DIVZ slice = still ~$16M unexplained post-DIVZ veto).
- [CTO] Consider whether the 17 Rule-2-close accts should route through a different mechanism (bronze txn exit-transaction absence, per ADVI_PRICES-001 pattern).

## Commit Chain (this session, 2026-04-17)

| Commit | Purpose | Scope |
|---|---|---|
| **`2a69b97e`** | **fix(B_01): key silver/unrealized to snapshot date — retire stale rolling parquet** | B_01 |

## Compiler Tools

Phase 1 (before write):

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-pipescript | `comp-pipescript io B_01` | OK — READS (2): accounts_dimension, bd_assets_dim. silver/unrealized not in declared manifest (loaded via dynamic S3_UNREALIZED_KEY — stays dynamic post-fix via `_resolve_unrealized_key`) | Manifest shape unchanged by fix |
| comp-pipescript | `comp-pipescript deployed B_01` | MATCH (before edit) | Confirmed local == S3 before modification |

Phase 2 (before commit):

| Tool | Command | Result |
|---|---|---|
| py_compile | `python -m py_compile data/black_diamond/scripts/gold/B_01.holdings_lots.py` | exit 0 |

Phase 3 (after commit + S3 upload):

| Tool | Command | Result |
|---|---|---|
| comp-pipescript | `comp-pipescript deployed B_01` | MATCH — local == S3 post-upload |

No `comp-validate B_01` run — no `gold_validate_config.yaml` entry for B_01 holdings_lots. The artifact gate for this fix is the QA-runner rerun result (AE-fired), not a validate config.

No `comp-blast` / `comp-pipescript postdeps` runs — fix is local to a single script's input-key resolution path; no new downstream nodes introduced, no new post-step dependencies changed. Script read/write manifest (from `comp-pipescript io B_01`) is unchanged pre/post fix (silver/unrealized was never in the declared READS list because it's loaded via dynamic S3 key; that remains true with the helper-resolved version).

## MCP / RAVC

Today's XYZ-lane message volume: ~20 outbound + ~10 inbound. Major RAVC loops:

- Primary DS GO (undershoot brief) → ACK → B1 split → B2 RCA → B1 deep dive (stale-pricing reject) → B4/B5 → DIVZ name-change hypothesis → stale-key ROOT CAUSE → fix shipped → simulation. All closed cleanly.
- STOP (candidate-a) → primary DS acknowledged via assessment request (unified hypothesis) → redirect to DIVZ hypothesis → redirect to ROOT CAUSE → GO on fix. Brief rule honored throughout (no code until ROOT CAUSE authorized fix-GO).
- AE audit request (20260417T165401Z): AE responded via Andrew brief — monolith wiring gap in commit 158a0026, no AE work needed. Loop closed.
- Primary DS BRIEF pointer (20260417T163952Z): durable reference landed.

Zero silent receipts.

## Do NOT

- Do NOT fire the gold runner without primary DS / COO coordination — CP-DS1 Run 9 is active on ~B's lane; overlapping SSM commands prohibited by feedback-memory rule.
- Do NOT revert `2a69b97e` without a simultaneous plan for date-partitioned key alternatives. The module-level rolling key WILL re-freeze (AE brief: it is not being maintained). Reverting returns the Rule 3 false-positive on every post-03/29 onboarding.
- Do NOT treat the 20 Rule-1/Rule-2-closed accts from the B2 simulation as "still broken" — they are correctly closed by the right authority layer post-fix. Do not widen the fix scope to "save" them.
- Do NOT try to restart the monolith `unrealized_gain_loss.parquet`. Per AE brief, it is intentionally not maintained; the date-partitioned parquets are the authoritative source.
- Do NOT re-add a fallback to `unrealized_gain_loss.parquet` in `_resolve_unrealized_key`. Hard-fail-within-2-days is the correct posture; falling back to the stale monolith is the exact bug we just removed.

## Current State (verbatim repeat for grep)

- Commit HEAD: `2a69b97e`
- Push: origin/CLOUD up-to-date
- S3 MATCH: YES (comp-pipescript deployed B_01 post-upload)
- Runner: NOT FIRED (awaiting primary DS / COO coordination)
- TO status: ds-brief-xyz-undershoot-tapering — in progress (fix shipped, validation pending on rerun)
- Expected B2 recovery on rerun: ~$6.96M across 31 clean accts (bounded by PIVOT-6 per-acct cap)
- Expected B1 DIVZ recovery on rerun: ~$6M across top-10 undershoot accts
