# 0.4.0_DS_ClientPlatform — COT_ADVI_FIX: silver coerce-numeric-first + 07-21/22 re-land — COMPLETE

**archetype:** REPAIR
**secondary_archetypes:** VALIDATE, SCRIBE

**Window:** 2026-07-22 ~22:55Z → ~23:12Z. **TO:** COT_ADVI_FIX (COO GO 225533Z, CTO gate 224919Z,
bounds inline; TO file committed in parallel by COO). Deadline ~01:30Z; landed ~23:10Z, 2.5h ahead —
the anti-pressure clause never engaged.

## Summary

The cot ADVI gold chain was halting nightly: BD's 07-21+ transactions export carried two `Units`
cells as text `'9.6E-05'` (rows 157-158), `cot_silver_merge.py:417-419`'s generic object→string
sweep then stringified all units, and `A_03.positions_cube.py:1001` died on `.abs()`-of-str.
Served 3 trading days behind.

**Fix @`2ed963ef6`** (CTO bounds verbatim): coerce-numeric-FIRST on numeric-bearing object columns
(≥1 real int/float instance among non-nulls) before the sweep — all-or-nothing per column
(`errors='raise'`), pure-string columns never attempted (digit-looking text keeps its historical
string dtype), bool excluded (int subclass), forced-string ID block stays authoritative. NO fillna,
NO filter. Plus minimal `--force` (requires `--date`) — flagged to COO as an in-bounds addition:
the bronze-ETag skip predicate is structurally blind to corrupt-silver-under-clean-bronze, so the
mandated forced rewrite was otherwise impossible (alternative = hand-editing manifest state on S3,
worse). In the event neither re-run tripped it (no matching manifest etag entries — nightly failed
pre-etag-record).

**Grounding sequence:** deployed==repo first (S3 ETag == local MD5 @`5930dd45d`); defect confirmed
empirically pre-fix (07-21 silver: units object, all 12,840 stringified, iloc 155-156 = the two
text cells; 07-20 clean float64; dtype diff 07-20 vs 07-21 = exactly one column); fix exercised
against real bronze pre-commit (both dates: only `units` coerced, zero collateral).

**Verification (served artifacts, post-land):** units float64 both; row counts UNCHANGED (07-21
12,840 pre==post; 07-22 11,620 pre==post — pre-state via versioned prior object `bBVhgwxm…`);
rows 157-158 = 9.6e-05 float; 07-20 ETag `0d24e87b…` identical before/after (positive control);
added: full-schema parity vs clean 07-20 (zero divergences, 71 cols, both dates) + `.abs()` (the
halt op) clean on both. **NO ad-hoc gold run** — 02:04Z chain self-heals. Ledger CLOSED
@`d144f3963`. 0.7.0 owns tomorrow's closure (chain COMPLETE + platinum + `data_as_of`).

**Deferred by design (COO):** A_03 gold-side guard (silent coerce at gold could mask vendor drift).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-pipescript deployed` | cot_silver_merge.py filter | 0 matched (bd-tree default) | cot is a separate firm tree; grounded deploy state on direct head-object ETag==MD5 instead |
| `.tools/commit-gate.sh` | the edited .py | PASS | pre-commit, before the exercise run |
| `s3api head-object` | code + 07-20 partition, before/after | PASS | deploy content-verify + the untouched positive control |
| `s3api list-object-versions / get-object --version-id` | 07-22 prior version | PASS | closed the pre-state row-count bound the GO left open |
| empirical parquet + xlsx exercise | 07-20/21/22 + both bronze files | PASS | the defect confirmation + pre-commit fix exercise + post-land verification |
| risk-reflex (safe-commit) | HOLD citation on cot_silver_merge.py | READ | memory cot_holdings_t1_pricing_freeze — it mandated the etag-skip predicate; fix leaves that path untouched, --force covers the orthogonal blind case |

## MCP traffic

COO GO 225533Z (pivot from G8b prep) · completion reports to 0.7.0 (231204Z, closure armed) +
COO (231206Z, --force flagged for the record).

## Next

Back on the B5 gate (~03:30Z): G8 core → S5 → G8b, all prep banked. 0.7.0 verifies ADVI chain
self-heal tomorrow.
