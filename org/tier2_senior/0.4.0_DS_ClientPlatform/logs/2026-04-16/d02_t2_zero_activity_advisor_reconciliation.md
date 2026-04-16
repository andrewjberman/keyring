# Session log — 0.4.0_DS_ClientPlatform~B (2026-04-16)

**TO:** `ADVI_ROLLUP.D02-T2.ds-zero-activity-advisor-summary-vs-role-breakdown-inconsistency` (self-authored this session per COO GO 2026-04-15T22:18:47Z)
**Trigger:** ~C side finding in D00c-T1 closeout (log `d00c_t1_leaderboard_advisor_count_reconciliation.md` L57-64).

## Outcome

**Path (b) — NOT A BUG.** Current S3 artifacts reconcile exactly for all 7 zero-current-activity advisors. ~C's reported inconsistency (`summary.tagged_aua=$0 + account_count=0` vs `role_breakdown.{role}.aua != $0`) is contradicted by the live data. Doc-only close; no D_02 / D_04 code change.

## Reconciliation Table

Source: `platinum/advisors/{slug}/summary.json` (D_04 producer, reads `gold/entities/advisors/{slug}/book.json` from D_02). Artifacts dated 2026-04-15T19:27:25Z (last nightly).

| slug            | book.total    | book.tagged   | book.acct | sum(role.aua) | diff_aua | sum(role.acct) | diff_acct |
|-----------------|---------------|---------------|-----------|---------------|----------|----------------|-----------|
| andrew_rose     | 66,036.79     | 66,036.79     | 2         | 66,036.79     | 0.00     | 2              | 0         |
| austin_bost     | 3,321,857.57  | 3,321,857.57  | 12        | 3,321,857.57  | 0.00     | 12             | 0         |
| connor_haney    | 0.00          | 0.00          | 1         | 0.00          | 0.00     | 1              | 0         |
| justin_jones    | 927,192.87    | 927,192.87    | 3         | 927,192.87    | 0.00     | 3              | 0         |
| logan_tingley   | 565,388.40    | 565,388.40    | 2         | 565,388.40    | 0.00     | 2              | 0         |
| nathan_grande   | 412,271.42    | 412,271.42    | 2         | 412,271.42    | 0.00     | 2              | 0         |
| presley_lawson  | 2,093,965.92  | 2,093,965.92  | 9         | 2,093,965.92  | 0.00     | 9              | 0         |

**All 7 reconcile: `book.tagged_aua == sum(role_breakdown.*.aua)` within $0.01 AND `book.account_count == sum(role_breakdown.*.account_count)` exactly.** No inconsistency.

## Upstream verification — D_02 book.json

Spot-checked 3 of 7 at `gold/entities/advisors/{slug}/book.json` (the D_04 input):

| slug         | book.summary.tagged_aua | role_breakdown (top role) |
|--------------|-------------------------|---------------------------|
| andrew_rose  | $66,036.79              | implementor.aua=$66,036.79 (2 accts) |
| austin_bost  | $3,321,857.57           | implementor.aua=$3,321,857.57 (12 accts) |
| connor_haney | $0.00                   | architect.aua=$0.00 (1 acct) |

D_02 emits the `.summary` subobject and `.role_breakdown` from the same underlying `snap_latest` pass (D_02 `build_advisor_books`). D_04 L622-623 passes through: `book_summary = book.get('summary', {}); adv_aua = book_summary.get('tagged_aua', 0)` → populates platinum `.book.tagged_aua`. Same for `.role_breakdown` (L709 `'role_breakdown': book.get('role_breakdown', {})`). Single code path, no dual-source basis split.

## Why ~C's claim didn't replicate

Most likely explanation: **null-as-zero conflation**. ~C reported "spot-checked summary.json: all show `summary.tagged_aua = 0`". In jq, `.summary.tagged_aua` at the **platinum layer** returns `null` (there is no top-level `.summary` subobject — only `.book`, `.role_breakdown`, etc.). `null` formats as `0` in many numeric contexts, which would match the reported symptom. The **gold-layer** `book.json` DOES have `.summary.tagged_aua` (see table above), and it is populated correctly.

Secondary possibility: ~C inspected gold/entities book.json for connor_haney (the one advisor with genuinely $0 book — single $0-AUA architect account) and generalized to all 7. Connor_haney does have `book.summary.tagged_aua=0 + role_breakdown.architect.account_count=1 (aua=$0)`. This is NOT inconsistent — it is accurate: one account is assigned to connor but carries $0 AUA. The "snap_latest non-empty with $0-AUA accounts" hypothesis is partially valid for connor_haney only, and even there it is correct data not a bug.

## Compiler Tools

| Phase | Run | Observed | vs `<expect>` |
|---|---|---|---|
| 1 | `comp-pipescript io D_02` | D_02 WRITES `gold/entities/advisors/{*}/book.json` via `advisor_book_key` (external/silver). **Does NOT write platinum/advisors/summary.json.** | Led to D_04 correction — platinum summary is D_04's output. |
| 1 | `comp-pipescript io D_04` | D_04 READS `advisor_book_key <- (external/silver)` + WRITES `platinum/advisors/{*}/summary.json` [HARDCODED] | Confirmed D_04 is producer of the artifact ~C inspected. |
| 1 | `grep -rn "platinum/advisors" data/black_diamond/scripts/gold/` | D_04 L712 `items.append((summary, f'platinum/advisors/{aid}/summary.json'))` — single emit site. | Confirmed. |
| 1 | Code-read D_04 L528-710 `_build_advisor_summaries` | Single code path: `book_summary = book.get('summary', {})` + `'role_breakdown': book.get('role_breakdown', {})` both sourced from same `book.json`. No dual basis. | Confirmed. |
| 1 | `aws s3 cp platinum/advisors/{7 slugs}/summary.json + gold/entities/advisors/{3 slugs}/book.json` | All 7 reconcile; gold upstream consistent with platinum. | PASS. |
| 1 | Python-less jq reconciliation (table above) | `diff_aua=0 + diff_acct=0` for all 7 | PASS — no bug. |
| 2 | `python -m py_compile` | N/A — path (b) doc-only, no code change. | Skipped (correctly). |
| 3 | Post-nightly re-verification | N/A — no code change to validate. Counts stable absent roster changes. | N/A. |

## Acceptance status

| # | Criterion | Status |
|---|---|---|
| 1 | Hypothesis verified or rejected with quantitative evidence on all 7 advisors | PASS — 7/7 reconcile (table above). |
| 2 | Path chosen + documented | PASS — Path (b), no bug. |
| 3 | Path (a) patch+deploy | N/A. |
| 4 | Path (b) contract note | This session log + TO closeout. FE not notified (no consumer-facing behavior change). |
| 5 | Session log Compiler Tools section | This file. |
| 6 | MCP COMPLETE to COO | Pending this-commit. |

## Files Modified

| File | Change |
|------|--------|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_ROLLUP.D02-T2.ds-zero-activity-advisor-summary-vs-role-breakdown-inconsistency.md` | authored this session; status pending → complete (path b) |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-16/d02_t2_zero_activity_advisor_reconciliation.md` | this log |

## B4 parallel-instance verification (supplementary, not closeout)

~A shipped B4 closeout at commit `80109df5` with 145/145 taxable-corrected = 100%. My parallel sweep re-classification at 148/148 = 100% reached the same ACCEPT conclusion via different denominator slicing (I classified 15 $0-taxable + 3 catch-all = 18 excluded; ~A classified 20 orphan/stale + 1 other = 21 excluded). Both conclusions agree. COO directive 12:51Z: "don't re-flip; accept ~A's conclusion". B4 L3 spot-check confirmed 3/3 clients populated at `.detail.tax.top_gain_positions` (z08327149 Chan 17 tgp, z0880615 Waldrop 20 tgp, z08296312 Lindsey 20 tgp). Noting for cross-verification; no separate closeout log.

## What I did NOT do

- Did NOT modify D_02, D_04, or any producer code (path b; no bug to fix).
- Did NOT push or upload (no script changes).
- Did NOT trigger a gold rerun.
- Did NOT update `data_contract.xml` — the existing contract is already consistent with current artifacts. If FE requests a clarifying note about the `.summary` subobject being present ONLY in gold/book.json (NOT in platinum/summary.json), that would be a separate doc TO.

## Next

- Commit scoped to 3 files (TO authored, TO flipped to complete, session log).
- MCP COMPLETE to COO + CTO cross-ref with reconciliation table.
- Stand by for:
  - Post-nightly B3 team_attribution re-validation (multi-role clients) — runs after tonight's 04:00 UTC nightly per COO 12:55Z.
  - Post-nightly B1.fix2 Dean Herndon account_count re-check — same window.
  - B4 closeout (COO driving Rule 7 ACCEPTANCE FLEX to CTO on naive→taxable-corrected denominator substitution).
