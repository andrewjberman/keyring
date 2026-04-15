# D00c-T1 leaderboard advisor count reconciliation — 2026-04-15 PM

**Agent:** 0.4.0_DS_ClientPlatform~C
**TO:** ADVI_ROLLUP.D00c-T1.ds-leaderboard-advisor-count-reconciliation (authored + executed by ~C per COO 22:06Z)
**Code commit:** none (path b doc-only)
**Doc:** `docs/data/d00c_leaderboard_eligibility_criteria.md`

## Outcome

Path (b) DELIBERATE. Leaderboard is intentionally narrower than the advisor-summary universe — D_00c uses `account_team` current snapshot; D_02 reaches across all `account_performance` dates. The 11-advisor gap is correct semantics, not a bug. No code change.

## Hypothesis verification

Validator T1d reported leaderboard QTD 152 entries vs advisor summary 163. ~C investigated:

| Window | leaderboard | folders | gap |
|---|---|---|---|
| QTD | 152 | 166 | 14 |
| YTD | 155 | 166 | 11 |
| MAX | 155 | 166 | 11 |

11 folders missing from MAX leaderboard:
- **4 sentinels (correct exclusion):** `49f_house`, `unassigned`, `unknown`, `unresolved`
- **7 zero-current-activity advisors:** andrew_rose, austin_bost, connor_haney, justin_jones, logan_tingley, nathan_grande, presley_lawson

Spot-checked andrew_rose / austin_bost / connor_haney summary.json: all show `summary.tagged_aua = 0` and `summary.account_count = 0`.

3 additional folders missing from QTD only (have MAX but no QTD activity): dominic_depizzol, jimmy_evans, kate_gotta — correct window-specific exclusion.

## Producer mechanism

D_00c L734-739 melts `account_team` (current snapshot) and explicitly filters `'unassigned'`. Other sentinels and zero-current-activity advisors don't appear because their account_team rows are empty.

D_02 builds books from `acct = account_performance` joined across all dates; an advisor with role assignments at any historical date gets a summary book.

## Path (b) decision rationale

- Leaderboard purpose: rank currently-active advisors. Including zero-current-activity entries clutters rankings.
- Summary book purpose: historical record. Advisors who left/transitioned still need accurate history.
- Different sources (current snapshot vs full timeseries) → semantic gap is correct.

Documented in `docs/data/d00c_leaderboard_eligibility_criteria.md`. No code change. Optional `excluded` metadata on `employee_leaderboard.json` deferred until FE asks.

## Compiler Tools

| Phase | Tool | Command | Result | Note |
|---|---|---|---|---|
| 1 (before write) | comp-pipescript | `comp-pipescript io D_00c` | PASS | READS account_team + advisor_fee_detail + role_aua; WRITES employee_leaderboard.json |
| 1 (before write) | comp-blast | `comp-blast D_00c` | EXPECTED-EMPTY | Script-node lookup empty (per memory: use fn name) |
| 1 (before write) | aws s3 ls | `aws s3 ls s3://opal-data-bd/platinum/advisors/` + leaderboard diff | PASS | 166 folders identified; 11 missing from MAX classified |
| 1 (before write) | aws s3 cp | `aws s3 cp .../summary.json -` for missing advisors | PASS | Confirmed tagged_aua=$0 + account_count=0 for samples |
| 2 (before commit) | py_compile | (skipped) | SKIPPED | Path b doc-only; no D_00c code change |
| 3 (after commit) | post-nightly | (deferred) | DEFERRED | No code change to verify; counts will remain stable absent advisor-roster changes |

## Side finding flagged for separate triage

D_02 produces `summary.json` for zero-current-activity advisors with internally inconsistent values:
- `summary.tagged_aua = 0`, `summary.account_count = 0`
- `role_breakdown.{role}.aua` non-zero (e.g. austin_bost: implementor.aua = $3,321,857.57 / 12 accounts)
- `role_breakdown.{role}.account_count` non-zero (despite `summary.account_count = 0`)

Both branches use `snap_latest` per the same code path (D_02 build_advisor_books L1151-1287). Either snap_latest is non-empty with $0-AUA accounts, or role_breakdown takes a different code path for these cases. **Likely cause:** the `role_breakdown.aua` may have been pulled from canonical role_aua snapshot (RA-P2 path) which equal-splits across all historical role assignments, while `summary.tagged_aua` correctly sums latest_date snap_latest. **Wait** — RA-P2 my cutover only landed at S3 17:45 ET; PROD platinum was generated 15:34 ET, so it's pre-RA-P2. Then the inconsistency is in the OLD code path. Worth investigating.

For FE: the Snapshot panel for these advisors will show $0 in headline but $X.XM in role breakdown — visually contradictory. Surface for separate ADVI follow-up TO.

## TO acceptance criteria status

- (1) hypothesis verified with quantitative evidence (table + spot-checks): DONE
- (2) path chosen + documented in commit / TO closeout: DONE (path b)
- (3) N/A (path b chosen, not a)
- (4) rationale doc shipped + DE notification via COMPLETE MCP: DONE
- (5) compiler tools section: DONE (above)
- (6) MCP COMPLETE to COO: pending
