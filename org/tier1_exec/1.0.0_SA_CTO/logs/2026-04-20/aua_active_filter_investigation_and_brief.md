# 1.0.0_SA_CTO — Session 34 continuation log (PM)

**Date:** 2026-04-20 (Mon, evening)
**Scope:** Post-dinner continuation — ~A ad-hoc investigation output, per-account silver-vs-canonical diff, 2020-2021 historical NNA re-examination, root-cause reframe from "un-enriched accounts" to "allocation-universe filter over-drops BD-excluded active accounts," active-filter redesign brief authored.
**Continuity from:** earlier session 34 log `staudt_bd_anchor_reframe_and_watchdog_rca.md`. That log closed after Andrew's "we don't track that" call + revised BFIX scope (cancel BFIX3/BFIX4, reshape KPI). This log picks up from the $120M 2020 NNA clarifying question.

---

## 1. Andrew's 2020-2021 NNA clarifying question

Andrew: *"explain to me again why we're getting ~120m for NNA in 2020 and 2021"*

Pulled INV1 evidence (`data/black_diamond/diagnostics/STAUDT/INV1/historical_nna_mechanism.md`) — cum NNA year-end values:

| Year-end | Cum NNA | Firm AUA | Ratio |
|---|---:|---:|---:|
| 2020-12-31 | $118.20M | $27.65M | 4.28× |
| 2021-12-31 | $226.26M | $59.16M | 3.82× |
| 2022-12-30 | $347.57M | $122.00M | 2.85× |
| 2023-12-29 | $738.21M | $529.37M | 1.39× |
| 2024-12-31 | $864.47M | $953.00M | 0.91× |
| 2025-12-31 | $1,156.84M | $1,452.32M | 0.80× |

Relayed INV1's original "universe asymmetry / un-enriched house accounts" framing as the mechanism (441 flow-only accts at 2020-12-31, $84M orphan NNA, attribution to `49F House` / `rel_id=0`).

## 2. Andrew challenge — "I'm not really tracking, are you 100% sure?"

Andrew: *"if transactions were happening, that would be AUA, and we would track that as AUA."*

Acknowledged the challenge was correct. Walked back the "un-enriched" framing as plausible-sounding inheritance from INV1 without independent verification. Stated the more defensible position: we don't fully understand the 2020-2021 asymmetry and the INV1 diagnosis may be incomplete. Offered to trace an actual flow-only account end-to-end.

## 3. Andrew's architectural clarification

Andrew: *"we dont have any snapshots before 1/27/2026 via silver allocations. those are daily releases only, no PIT, so we didnt start tracking it til then. the only things before then are transactions and realized capital gains records."*

This is load-bearing context I didn't previously understand:
- Pre-2026-01-27 AUA must be FIFO-reconstructed from silver/transactions + realized_gains
- No point-in-time snapshot source exists historically
- `silver/allocations/*.parquet` earliest date is 2026-01-16 in bucket (`gold/canonical/nna/{2020-12-31}.parquet` still exists — derived, not snapshotted)

## 4. End-to-end trace — account z0814305021 (SLAT - Managed)

Selected the largest flow-only account from nna_atomic/2020-12-31 ($11.38M cum_nna, $11.38M cum_inflow, $0 outflow).

**2020 silver/transactions for this acct:**

| Date | Type | Amount | Asset |
|---|---|---:|---|
| 2020-12-21 | Cash Deposit | $11,382,740 | CASH |
| 2020-12-21 | Buy | $11,382,740 | Fidelity Phillips Street Trust Govt Cash Resv (CUSIP 316067107) × 11,382,740 units @ $1 |
| 2020-12-31 | Dividend | $31.19 | Same fund |
| 2020-12-31 | Div Reinvestment | $31.19 | 31.19 shares |

**Multi-year tx sample (same account):**
- 2021-Q1: 15 tx (Dividends + 1 Buy — investing the cash into real equities)
- 2022-06: 18 tx (Buy/Sale/Capital Gains — actively trading)
- 2024+: 0 tx (dormant / likely transferred)

**Universe presence check (2026-04-13 / 2026-04-16):**

| Data source | Present? | Value |
|---|---|---|
| `gold/holdings_lots` (open) | **YES** | 725 lots, 276 open, **$11.13M MV** (ABT, ACN, ADBE, AEM, ADIDAS, etc.) |
| `silver/allocations` (2026-04-16) | **NO** | BD excludes |
| `gold/positions_cube` | **NO** | Downstream inherits silver universe |
| `gold/canonical/holdings` | **NO** | Downstream of positions_cube |
| `gold/canonical/nna` | **NO** (any year checked) | Inherits via account_gains |
| `gold/canonical/account_gains` | **NO** (any year checked) | The universe filter lives upstream of this |
| `gold/canonical/nna_atomic` | **YES** | 2021/2024/2026: $8.28M cum_nna |

**Finding:** the account has never appeared in `account_gains` in any year checked (2020 → 2026). Our pipeline has full lot-level position data ($11.13M open-lot MV today, 725 lots, real equity names). The account is a SLAT (Spousal Lifetime Access Trust), relationship `z0880615`. BD categorically excludes SLATs from allocations — so our AUA aggregator inherits the exclusion, even though our transaction-derived lot reconstruction is correct.

## 5. Universe hierarchy finding (2026-04-13 / 2026-04-16)

| Data source | Accts | MV |
|---|---:|---:|
| `gold/holdings_lots/` (open lots only) | **8,075** | **$1.910B** |
| `silver/allocations/` | 6,554 | $1.698B |
| `gold/canonical/holdings/` | 5,967 | $1.651B |

**Dropped cohort (in holdings_lots but not silver):** 2,066 accts / **$251M**

### Cohort decomposition by transactional recency

| Subpopulation | Accts | MV | Interpretation |
|---|---:|---:|---|
| Silent ≥ 2 years (no tx since 2024-01-01) | 1,900 | $209M | Likely-stale lots from transferred/closed accts. Current filter CORRECTLY drops. |
| Active (tx within last ~2.5 years) | 166 | **$41M** | Real BD-excluded account types. Current filter INCORRECTLY drops. |

**Finer breakdown of active cohort (by most recent tx year):**
- 2026 YTD: 24 accts, $3.6M
- 2025: 38 accts, $24.6M
- 2024 only: 104 accts, $13.0M

### Top named accts in the incorrectly-dropped cohort
- Waldrop DAF $4.8M
- Phillip Wuest Corporation $4.5M
- HealthEquity HSA $7.9M
- Various SLAT / TODI / JWROS / LLC / Corporate with recent tx

**Our trace acct z0814305021 is in the silent cohort** (dormant since 2022) — so the current filter is correctly catching it. My earlier framing that "we're missing real SLAT AUA" was right about mechanism but wrong about this specific recovery value. Real loss from the current over-drop is the $41M active cohort, not the full $251M.

## 6. Root cause reframe — INV1 diagnosis was incomplete

Original INV1 ruling (2026-04-20 AM): "universe asymmetry between silver/transactions-derived NNA (wider) and holdings_lots-derived AUA (narrower), driven by un-enriched house accounts." Ruled (a)+(b) jointly IN, (c) OUT.

**Revised understanding (post per-account trace):**
- The 441 flow-only accts at 2020-12-31 are NOT primarily "un-enriched house accounts"
- They are accounts where BD applies an account-type exclusion in their allocations release (SLATs, DAFs, HSAs, trusts, corporate entities, etc.)
- Our pipeline has full lot-level data via `holdings_lots` (FIFO-built from transactions)
- The AUA aggregator (`A_03.positions_cube` → `B_00.canonical_holdings` → `C_01.canonical_nna`) keys off the silver/allocations universe, inheriting BD's exclusion filter
- Historical $84M orphan NNA = same mechanism as today's $41M over-drop, just at a different magnitude

**INV1 should be reopened** with the updated mechanism. Not urgent — its original conclusion (flows are real, AUA is under-represented) is still directionally correct. Only the causal attribution is refined.

## 7. Multi-signal active-account detector design

Andrew: *"we did that as a means to close out any accounts that didn't have an official closeout… There is probably a better solution to that end, but I'm not sure what it is."*

Proposed replacement for the single-source `account ∈ silver/allocations[d]` filter:

```python
def is_active_account(acct_id, d):
    return (
        acct_id in alloc_accts[d]                       # BD confirms
        or tx_last_seen[acct_id] >= d - 365             # pipeline confirms
        or acct_id in schwab_rps_accts_last[d, 7]       # custodian confirms
    )
```

Drop from canonical/holdings only when all three signals silent for their respective windows. Permissive-OR intentionally — any evidence of life keeps the account.

**Properties:**
- Recovers ~$41M of incorrectly-dropped active cohort (today's over-drop)
- Retains the $209M stale-lot suppression (silent-2-year cohort)
- Applies retroactively — would substantially close the 2020-2021 historical gap by re-admitting flow-only accts with recent-at-the-time tx activity
- Observable — new `gold/canonical/account_activity/{date}.parquet` artifact with diagnostic columns (`active_reason`, `last_tx_date`, `in_alloc_today`, `in_rps_last_7d`)

**Rollout proposed as 4 phases:** Validation diff → Shadow emit (parallel to current) → Cutover (firm AUA moves $1.651B → ~$1.692B) → optional historical backfill.

## 8. Brief authored

`docs/briefs/aua_active_account_filter_redesign.md` — full design doc covering:
- Problem statement + evidence
- Historical parallel (2020-2021 NNA/AUA asymmetry)
- Proposed multi-signal detector with thresholds
- Implementation structure (A_03 / B_00 / C_01 / C_03 touchpoints, new `account_activity` artifact, 3 observability metrics)
- Tradeoffs (threshold tuning, non-Schwab reconciliation status, orthogonal close-signal improvements)
- Relationship to BFIX1+2 (complements, ships independent), BFIX3/BFIX4 (partially supersedes — the BD-excluded-active cohort gets admitted by Signal B without cash synthesis), B_00 mini-PRD (foundation)
- 4-phase rollout
- 6 open questions

Status: DRAFT — not circulated to COO yet. Andrew reviewing.

## 9. Commits this session (continuation)

Nothing committed by me this segment. Written:
- `docs/briefs/aua_active_account_filter_redesign.md` (new file, uncommitted)
- This log (`aua_active_filter_investigation_and_brief.md`, uncommitted)
- Earlier log from this session written but also uncommitted: `staudt_bd_anchor_reframe_and_watchdog_rca.md`

Commit decision pending: wait for Andrew read on brief before committing the whole bundle under a single `1.0.0_SA_CTO` commit.

Observations of other-agent commits during this window (not mine):
- `42be5b21` / `6f724293` / `035352c3` (~D D_02 stacked commits — small_account_clients / role_aua denominator / NNA date-gate)
- `4299e1c0` (~D D_00 firm-level fee splits)
- `8593ea51` (~D D_04 slim builder widening)
- DT uploaded D_00 + D_02 + D_04 via committed-ref pattern (parallel to BFIX1+2 upload being held)
- AE fired `bd-gold-trigger` for FIX-wave PROD; SSM `3e06059f` complete 19:49:33Z, all FIX1/2/6/7 validated PROD
- AE reverted QA c6i→c6a

## 10. Key quantitative findings (for future-session reference)

### Silver allocations (62 partitions, 2026-01-16 → 2026-04-16)
- Firm AUA range: $1.534B – $1.698B (first $1.550B, last $1.698B)
- Firm cash range: $25.1M – $43.7M, median $31.2M, mean $31.7M
- Cash as % AUA: 157-274bps, median 194bps
- Cash has been structurally ~$31M median for the entire 62-day window

### Per-account cash distribution
- Median per-acct cash: $624 (across 6,687 unique accts, 62 dates)
- 502 accts always-zero cash (fully-invested), 5,715 always-positive, 184 margin-debit ever
- Top 56 accts (≥$100K median cash) carry ~$21M of the firm's $31M

### Gap attribution on 2026-04-16
- Silver AMV $1,697.68M vs Canon MV $1,651.45M = -$46.23M total firm gap
- Dropped 599 / canon-only 12 / overlap 5,955
- Overlap is 21bps short of BD on amv basis (essentially perfect)
- ~A's re-analysis: 654 untracked (599 absent + 55 effective-zero) = $52.47M

### holdings_lots vs silver diff (the bigger finding)
- holdings_lots 8,075 accts / $1.910B (open lots)
- silver 6,554 accts / $1.698B
- Dropped 2,066 accts / $251M
- Split: 1,900 silent $209M (correctly dropped) + 166 active $41M (incorrectly dropped)

### Trace account z0814305021
- SLAT - Managed, relationship z0880615
- Dec 2020: $11.38M inflow → MM Fund → equity buildout through 2022
- Today: 725 lots, 276 open, $11.13M MV
- Never in account_gains / canonical/nna / silver/allocations in any year
- In silent cohort (no tx since 2022)

## 11. Open items / next steps

**Awaiting Andrew:**
- Read brief `docs/briefs/aua_active_account_filter_redesign.md`
- Decision: circulate to COO for decomposition (Phase 0 + Phase 1 worth authoring as TOs now; Phase 2/3/4 depend on Phase 1 findings)
- Commit bundle authorization (this log + earlier log + brief under 1.0.0_SA_CTO)

**Pending (unchanged from earlier log):**
- MCP COO + ~A with revised BFIX scope (BFIX1/2 ships; BFIX3/BFIX4 cancelled; KPI reshaped; B_00 mini-PRD authored)
- DT holds `081223b5` S3 upload until scope decision lands
- qa-runner full --group ABCD for BFIX1+2 when green-lit

**Parked:**
- OPB (likely cancel/re-scope post this brief — the universe-unification framing is superseded)
- EOP2025 $32M intra-portal inconsistency diagnostic (~B, P3)
- Q4 watchdog coverage test (AE, this week)
- Q6 process-tagging TO (AE, post-STAUDT)

## 12. Compiler Tools (this continuation)

| Tool / Approach | Result | Purpose |
|---|---|---|
| Direct `pd.read_parquet` bulk reads (62 silver/allocations partitions, 2 canonical/nna historical dates, holdings_lots 2026-04-13, silver/transactions multi-year samples) | OK | Data investigation — this session was pure parquet analysis, no compiler-graph work |
| `aws s3 ls` + `boto3.get_object` | OK | Schema probing + per-account retrieval |
| `git show` on INV1 evidence | OK | Re-reading INV1 diagnosis |

No `comp-*` runs this continuation segment — the investigation was data-level not dependency-level. One item for the compiler backlog: it'd be useful to have a `comp-universe diff <source_a> <source_b>` tool that enumerates accts in one universe and not another, across partitions. That's the shape of analysis we did manually here and would recur. Flag for ADHC_ROUTER Phase 2.

## 13. Insight carry-forward

1. **The filter is a closure-detection heuristic.** Andrew's framing clarified this — the current alloc-universe check was introduced to prevent stale-lot inflation when accounts transfer out without a terminal Sale tx. Any redesign must preserve that stale-lot suppression; the multi-signal detector does (silent-2-year cohort stays excluded).
2. **Our `holdings_lots` is more comprehensive than we were using it as.** We've been keying canonical off a narrower downstream universe. The lot-level reconstruction has been correct all along; the AUA aggregator just didn't trust it.
3. **BD applies account-type exclusions in allocations.** SLATs, DAFs, HSAs, corporate entities, trusts — BD treats these as out-of-scope for their client-visible allocations release even though they tick on at the custodial level. Our pipeline inheriting that filter was inadvertent, not deliberate.
4. **"Active" is a multi-dimensional property.** BD allocation presence, tx recency, custodian feed presence, explicit close flags — each is a partial signal. Combining them is strictly more robust than any single-source check.
5. **INV1 reopen worth logging.** Original diagnosis (a)+(b) ruled IN was directionally correct but causally incomplete. Not urgent to reopen formally until the new filter design matures, but should note in STAUDT closeout.
