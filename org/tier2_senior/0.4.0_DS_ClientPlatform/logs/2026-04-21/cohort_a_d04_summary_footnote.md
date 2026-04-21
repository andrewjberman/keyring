# ADVI_STAUDT.COHORT-A — D_04 Cohort A Summary Footnote

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-04-21
**TO:** ADVI_STAUDT.COHORT-A.ds-d04-summary-footnote.md
**Status at write-time:** Phase 2 gate PASS, ready to commit + S3 upload.

---

## Compiler Tools Mandate (Phase 1 — before write)

| Step | Run | Result | Note |
|------|-----|--------|------|
| 1 | `comp-pipescript io D_04` | silver/allocations NOT in READS (new consumer) | Added as new READ per mandate `<if_mismatch>` clause |
| 2 | `comp-blast D_04` | No downstream consumers for D_04 script node | Terminal in gold graph |
| 3 | `comp-platinum reverse cohort_a_summary` | Genuinely absent (new key, no collision) | Key: `gold/platinum/firm/cohort_a_summary.json` |
| 4 | Cohort A definition sanity | Deferred to post-S3-upload qa-runner (no local silver access) | Baseline: ~599 accts / ~$44.7M AUA; validator gates this post-run |

Phase 1 Step 4 note: local Cohort A sanity check requires live S3 access (silver/allocations + canonical/holdings). Moved to post-upload qa-runner validation via `comp-validate cohort_a_summary --artifact /tmp/cohort_a_summary.json`. Validator block gates `account_count` (400-2000 WARN) and `total_aua` ($30M-$60M WARN) with hard-ERROR on zero.

---

## Pre-commit Gate (Phase 2)

| Check | Result |
|-------|--------|
| `ds-commit-gate.sh D_04.client_portal_summary.py` | EXIT 0 — py_compile + AST scan clean |

---

## Design Notes

### Cohort A Derivation

Cohort A = accounts in `silver/allocations[latest_date]` with `account_market_value > 0` that are absent from `gold/canonical/holdings[latest_date]`.

**AUA column resolution**: `account_market_value` (primary) → `market_value` → `total_value` → `aua` — same fallback order as A_03.

**AUA semantics**: `account_market_value` in silver/allocations already includes cash. The TO reference to `cash_market_value + amv` maps to `account_market_value` (the full account value per BD's allocation report). No double-count.

**Account dedup**: silver/allocations can have multiple rows per account (one per sleeve/position). Grouped by `account_id`, summed AUA before computing active set.

**Client count**: derived via `relationship_id` from accounts_dimension join. If relationship_id unavailable, falls back to account_count (conservative).

**State distribution**: `client_state` from accounts_dimension. Accounts without a match default to 'Unknown'.

**top_n_named**: top 20 by AUA, using `account_name` from accounts_dimension. Portal RBAC gating is the DE sub-deliverable responsibility.

### Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | NEW `build_cohort_a_summary()` function. Added `ACCOUNTS_DIMENSION` to s3_layout imports. Wired as Step 13 in `main()`. |
| `data/black_diamond/scripts/gold/gold_validate_config.yaml` | NEW `cohort_a_summary` block with 7 checks (account_count ERROR+WARN, total_aua ERROR+WARN, state_distribution ERROR, top_n_named WARN, snapshot_date ERROR, methodology_note WARN). |

### Artifact Key

`gold/platinum/firm/cohort_a_summary.json` — confirmed no collision via `comp-platinum reverse cohort_a_summary`.

### Wire Contract Compliance

- Zero impact on canonical AUA, leaderboards, charts, or per-advisor attributions.
- Only new S3 key: `gold/platinum/firm/cohort_a_summary.json`.
- No changes to A_03 / B_00 / C_01 / filter logic / `gold/canonical/` shape.

---

## Blockers

None. S3 upload sequence:
1. CHART-ALIGN S3 upload must land first (D_00c → qa-runner `--group D` ordering).
2. After CHART-ALIGN qa-runner + COHORT-A upload both land, run `--group D` or `--from D_04` to capture Cohort A artifact.
3. Run `comp-validate cohort_a_summary --artifact /tmp/cohort_a_summary.json` post-run.

---

## Next Steps

1. **[0.4.0_DS~B]** Await CHART-ALIGN RAVC4 close from base lane.
2. **[0.4.0_DS~B]** On RAVC4 close + CHART-ALIGN S3 upload: commit + push COHORT-A files.
3. **[0.4.0_DS~B]** `aws s3 cp` D_04 to `s3://opal-data-bd/code/gold/D_04.client_portal_summary.py`.
4. **[0.4.0_DS~B]** Dispatch qa-runner `--group D` (covers both D_00c and D_04).
5. **[0.4.0_DS~B]** Run `comp-validate cohort_a_summary --artifact /tmp/cohort_a_summary.json`.
6. **[0.4.0_DS~B]** MCP DE (0.4.0_DE_ClientPlatform) with artifact-ready + key + expected 7 fields.
7. **[0.4.0_DS~B]** MCP COO COMPLETE with commit hash + qa-runner evidence + validator exit code.
