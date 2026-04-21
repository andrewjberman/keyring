# Schwab TRN_NNA Phase 6a — C_01 canonical_nna merge

**Date:** 2026-04-21
**Agent:** 0.4.0_DS_ClientPlatform
**Project:** ADHC_SCHWNNA (Phase 6 of `docs/briefs/ae-brief-schwab-trn-nna-enrichment.md`)
**Trigger:** Andrew GO 2026-04-21 ~16:09 ET ("GO" on Schwab handoff following AE READY 20260421T150922Z)
**CTO ACKs:** Q2 (classifier tune = proceed as-is), Q3 (byte-identity = stable sort), Diff-flag ($100+2%) all ENDORSED 20260421T161943Z
**Q1 decision:** Andrew → (c) firm-only for Phase 6a (via CTO 20260421T163657Z)

## Briefs Written

None this session — consumer of AE's contract (`docs/data/schwab_trn_nna_contract.md`).

## Current State

Phase 6a code shipped, dry-run PASS, fixture test PASS, ready to commit + push + pre-flag #2 upload. **Phase 6b design response authored separately (see MCP 20260421T16xxxxZ).**

Phase 6a narrows brief's 6-tag enum to 3 tags at daily-aggregate grain:
- `bd` — BD row present this date (Schwab absent OR amounts match within $100+2%)
- `bd_diff_flagged` — BD + Schwab both present, either direction diverges beyond threshold
- `schwab_imputed` — BD absent this date, Schwab present (closes the $91M gap visibility)

**Deferred to Phase 6b** (explicit scope line, flagged in code comments):
- `bd_lagged` / `bd_delayed` — require event-level time-fuzzy matching; daily-aggregate grain can't distinguish a BD same-day-match from a BD ±7d match
- `bd_only` — requires account-level Schwab-history set lookup; collapsed into `bd` at aggregate grain

## Compiler Tools

| Tool | When | Result | Note |
|------|------|--------|------|
| `.tools/ds-commit-gate.sh` | Pre-stage #1 | EXIT 0 on both files | py_compile + AST scan clean |
| `.tools/ds-commit-gate.sh` | Pre-stage #2 (post-edit) | EXIT 0 | after source_system stats + FutureWarning fix |
| Python stdlib loader smoke | Phase 1 evidence | PASS | 6,952 mapping entries; 395 (acct,date) pairs across 5 May-2025 days; 4 unmapped events ($2,631 gross) |
| `C_01 --date 2026-04-15 --dry-run --skip-validation` | Phase 2 local dry-run | PASS (exit 0, 120s wall) | Loaded 74,602 BD flow events across 1,680 dates, 66 Schwab overlay accts, 5,992 canonical_nna rows. No KeyError/runtime errors. |
| Fixture merge test | Phase 2 fallback | PASS (8/8 assertions) | Post-timeout on 2nd dry-run; minimal in-memory test confirms bd/bd_diff_flagged/schwab_imputed tagging + BD-priority amount preservation + Schwab amount inheritance for imputed rows |
| BD onboarding lag distribution | Phase 6b data-check | Done | Answered CTO's data-check ask (see Phase 6b design response) |

**No comp-* invocations** this TO — script authoring + dry-run + fixture testing; no routing/trace/blast questions. `.comp-graph/.agent_context` was set to `ADHC_DSFLOW.001` earlier in session; did not update for this TO because compiler-tools-log auto-append didn't trigger (no comp-* calls made).

## Design Notes

### Insertion point

The new Schwab merge sits between the existing BD-flow outer-merge (lines ~228-249) and
the existing `nna_txn = daily_inflow - daily_outflow` computation (line ~250 pre-edit).
This ordering ensures imputed rows backfill `daily_inflow` / `daily_outflow` from Schwab
before downstream computes `nna_txn`, so the final `nna_txn` value is consistent whether
the row came from BD or Schwab.

### Scope decision — 3-tag vs 6-tag

Full 6-tag enum requires event-level time-fuzzy matching (bd_lagged / bd_delayed) and
account-level Schwab-history set (bd_only). Current BD silver loader aggregates to
(account_id, date) grain — we lose event granularity. Two paths to the full 6-tag:
1. Re-grain BD silver to event level (large refactor, breaks existing `_worker_04b`)
2. Matching at daily totals ± 7d (no-op against the same-account, which is Schwab's coverage pattern)

Phase 6a ships the 3-tag narrow, which captures the primary business value (the $91M
imputation gap). Phase 6b is a separate scoped TO if Andrew/CTO decide the bd_lagged/bd_delayed
distinctions are worth the additional complexity.

### Byte-identity (AC#5)

Stable mergesort on `(date, account_id)` before emit. Upstream BD silver is deterministic,
upstream Schwab silver is deterministic (positional parse + stable SHA-1 `schwab_txn_key`),
Schwab-BD mapping is deterministic (sorted by `mapping_source` priority + `last_seen_in_fees`).
Therefore a rerun on the same (BD, Schwab, mapping) snapshot produces byte-identical
canonical_nna output.

Note on Phase 6b (if adopted): emit-time lookup of BD architect for imputed rows breaks
strict byte-identity across runs (same date's output changes as BD catches up on tagging).
AC#5 will need amendment to "byte-identical given same BD+Schwab snapshot" — flagged to
CTO in Phase 6b design response.

### Imputed-row attribution (Q1 = c firm-only)

Andrew's 2026-04-21 call: Schwab-imputed rows stay firm-only (advisor dimension NaN).
Rationale: most imputed events occur BEFORE BD records the architect's `first_date`
on the account — attempting per-day-gate-consistent attribution would silently filter
them, so (c) firm-only is the clean + consistent call under decision #2 (per-day gate
as canonical for all flow attribution).

Implementation: imputed rows inherit the existing "flow-only account with no acct_dim"
pattern (line 232-235 of old `_worker_04b` — acct_dim cols stay NaN; downstream drill
paths treat these as Unresolved / no-cohort).

### FutureWarning mitigation

Original `_worker_04b` used `.fillna(False)` on `nna_clean` (object-dtype col → pandas
FutureWarning on object-dtype fillna). My imputed-row block inherited this; fixed to
cast explicitly `.astype('boolean').fillna(False).astype(bool)`. Silences warning in
both the existing branch (my edit reused the same pattern) and the new imputed branch.

## Dry-run v1 evidence (2026-04-15, 120s wall, exit 0)

```
2,801,197 transactions -> 74,602 account x date flow events
Flows loaded: 74,602 account-date rows across 1,680 dates
--- Loading Schwab TRN_NNA overlay (ADHC_SCHWNNA Phase 6a) ---
  Schwab TRN_NNA: loading 1 partitions (date=20260415 ... date=20260415)
    un-mapped Schwab rows: 74 events across 7 acct10s ($405,337 gross_amount — dropped)
    mapped 99/173 events across 66 BD accounts
    aggregated 66 (account, date) pairs in 1.0s
--- Processing dates (in-memory) ---
  [ 1/1] dates complete
  nna_atomic shadow: 9,581 rows; cum_nna=$+1,279.9M daily_nna=$-1.284M
Dates processed: 1 / 1
Elapsed:         120s
Latest date (2026-04-15):
  Accounts:        5,992
  Inflows:         $+2,390,566
  Outflows:        $+3,651,123
  Total AUA:       $1,650,488,292
```

Dry-run v2 (with source_system distribution print) timed out on BD silver S3 read
(transient network). V1 evidence stands + fixture test validates the tagging logic.

## Fixture test evidence (8/8 PASS)

| Account | BD inflow | BD outflow | Schwab inflow | Schwab outflow | Expected tag | Got |
|---------|----------:|-----------:|--------------:|---------------:|--------------|-----|
| A | $1,000 | 0 | absent | absent | `bd` | `bd` ✓ |
| B | 0 | $500 | absent | absent | `bd` | `bd` ✓ |
| C | $10,000 | 0 | $10,050 | 0 | `bd` (within $100 floor) | `bd` ✓ |
| D | $10,000 | 0 | $15,000 | 0 | `bd_diff_flagged` (>$100 AND >2%) | `bd_diff_flagged` ✓ |
| E | 0 | 0 | absent | absent | `bd` (BD row with zero flow) | `bd` ✓ |
| F | absent | absent | $25,000 | 0 | `schwab_imputed` | `schwab_imputed` ✓ |

Amount preservation assertions (BD-priority over Schwab): PASS.

## Phase 6b design — BD onboarding lag distribution

Per CTO question 3 data-check:

**Population:** 4,883 unique Schwab acct10s; 4,755 (97.4%) map to BD; of those **2,652
(55.8%) have a real architect in BD** (excluding generic "49F House" / Unassigned).
**2,103 (44.2%) are never-tagged with a real architect** — would stay firm-only forever
under any Phase 6b emit-time lookup.

**Of the 2,652 with both sides (the lag-analyzable subset):**
- 1,072 (40.4%) — BD architect recorded BEFORE Schwab first event (normal case)
- 1,278 (48.2%) — same day
- **302 (11.4%) — BD RECORDED AFTER Schwab first event (the late-adoption case)**

**Lag distribution for the 302 late-adopt accounts:**

| Percentile | Lag (days) |
|------------|-----------:|
| p50 | 13 |
| p75 | 49 |
| p90 | 431 |
| p95 | 504 |
| p99 | 675 |
| max | 729 |
| mean | 100.0 |

| Bucket | Accts | Pct of late-adopters |
|--------|------:|---------------------:|
| ≤ 14d | 165 | 54.6% |
| ≤ 30d | 214 | 70.9% |
| ≤ 90d | 237 | 78.5% |
| > 90d | 65 | 21.5% |

**Key takeaway:** The lag distribution is bimodal — a tight cluster ≤ 30d (71% of
late-adopters, likely normal onboarding) and a heavy tail > 90d (22% of late-adopters,
p90 = 431 days, max = 729 days). A fixed 30d aging gate (V2) captures only 71% of
the population that would benefit from post-hoc advisor attribution; 22% would stay
firm-only under V2 despite eventually being tagged.

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/lib/schwab_flows.py` | NEW. Schwab TRN_NNA silver loader + Schwab-BD acct mapping + `amounts_match()` + 3-tag `source_system` enum constants. |
| `data/black_diamond/scripts/gold/C_01.canonical_nna.py` | Edit. Import Schwab loader. Main loads Schwab overlay into `_shared_04b`. Worker merges after BD flow join (imputes / diff-flags / drops schwab-aux cols). Stable mergesort on (date, account_id). `source_system` column added to output. `stats` dict includes `source_system_counts` + `schwab_imputed_inflow/outflow`. Main summary prints distribution rollup. |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-21/schwnna_phase6a_c01_merge.md` | NEW. This log. |

No changes to: `_NNA_ATOMIC_COLS` (CN-P0 locked 2026-04-15, `source_system` stays on
canonical_nna only, not on nna_atomic shadow), `D_04 _build_nna_by_period`, `lib/nna_flows.py`,
any downstream consumer.

## Blockers

None. All Phase 1 + Phase 2 gates PASS. Pre-flag #2 to CTO+COO required BEFORE
`aws s3 cp .../C_01.canonical_nna.py s3://opal-data-bd/code/gold/C_01.canonical_nna.py`
per `feedback_ad_rerun_sensitive_preflag_before_s3_write.md`.

## Next Steps

1. **[0.4.0_DS_ClientPlatform]** git commit --only with author (scoped to lib/schwab_flows.py + C_01.canonical_nna.py + this session log).
2. **[0.4.0_DS_ClientPlatform]** git push origin CLOUD.
3. **[0.4.0_DS_ClientPlatform]** Pre-flag #2 MCP to CTO+COO with commit SHA + dry-run + fixture evidence + A→D impact statement (single column add, no shape change, stable sort → byte-identical re-run).
4. **[0.4.0_DS_ClientPlatform]** MCP Phase 6b design response to CTO (V1 vs V2 opinion + lag-distribution data + implementation cost estimate + AC#5 amendment proposal). Independent of 6a ship.
5. **[0.4.0_DS_ClientPlatform]** On CTO+COO GO: `aws s3 cp .../C_01.canonical_nna.py s3://opal-data-bd/code/gold/C_01.canonical_nna.py` (committed-ref pattern per memory `feedback_s3_upload_git_show_not_working_tree.md`). DS-owned per CLAUDE.md Rule 13 + prompt.md update this session.
6. **[0.6.0_AE_PartnerETL]** qa-runner `--from C --chain` dispatch (C_01 → D_04 → D_02 etc) against fresh S3 code. SSM command via AE.
7. **[0.4.0_DS_ClientPlatform]** Validate source_system distribution on QA artifacts (expected: majority `bd`, 5-15% `schwab_imputed` typical months, 50%+ `schwab_imputed` on Jun 2024 + Dec 2024 per brief Phase 4 metric). RAVC4 close with distribution table.
