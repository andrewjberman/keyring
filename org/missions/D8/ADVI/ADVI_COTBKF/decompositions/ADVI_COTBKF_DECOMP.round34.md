# ADVI_COTBKF decomposition -- ROUND 34 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~11:0xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 9 @cf58046f35 (msg 3180).
- FWD-3 is re-graded NOT REALIZED: 38% of served account-days rest on dividend-adjusted prices (D2-S50, BLOCKING).
- ADDENDUM 8's interim marking is REPLACED by a reader gate. No reader, role, route or export is granted on the FWD-3 tables until the
  as-traded rebuild lands and is graded. This binds by reading; no gate is built here.

Round 34:
1. A read-only trace of `bd_txn_price`'s writer: its inputs (bucket and prefix) and account coverage. The rule is stated before the
   read, and a cross-firm input is the NEVER and BLOCKING.
2. The as-traded rebuild under a never-widen pair.

**Rule 24.** Domain: two enrichment items, three cells.

| enrichment item | cell | what it is |
|---|---|---|
| 1 | `CB-ah-1` | the trace |
| 2 | `CB-ah-2` | the as-traded basis in the chain, plus the local build and re-grade (LOCAL) |
| 2 | `CB-ah-3` | the SERVED re-mint under a pair, on the applier |

- `CB-ah-1` and `CB-ah-2` are disjoint and run now.
- `CB-ah-3` depends on both: on `CB-ah-2` for the build to apply, and on `CB-ah-1` for whether the three `bd_txn_price` CUSIPs are held.
- The served set is THREE tables (`daily_returns`, `account_day_value`, `month_grades`). The addendum says "four"; the mint @476f970245
  wrote three keys.

## Measured constraints

1. Price input: `.scratch/advi_cotbkf/yahoo_census/` holds the round-33 cached Yahoo pulls (3,580 tickers, `Close` and `Adj Close`,
   `auto_adjust=False`), copied to the shared tree before ~60's worktree was removed. No second Yahoo pass is needed.
2. The per-ticker classes are in `deliverables/0.9.0_WK_ADVI_COTBKF~60/price_basis_census.csv`: 2,079 dividend_adjusted, 79 mixed,
   175 as_traded, 872 indistinguishable, 266 other, 109 no_yahoo.
3. The builder `commonwealth_fwd3_serve.py` reads ABSENT months as `REGRESSED_UNDER_R28` (MATCH under r26, DIFF under r28). A rebuild at
   a new basis re-derives that list against its own before/after pair.
4. `deploy_ledger.py` fix @00d3393ff3 is in dell2 HEAD (read ~11:0xZ): `open` commits its own files. The interim hand-commit rule (MSTR
   msgs 2908/2974/3033) is retired for `CB-ah-3`.
5. The served keys @476f970245, with 0 readers: the three under
   `s3://opal-data-assets/commonwealth/cottonwood/silver/{daily_returns,account_day_value,month_grades}/date=2026-06-23/part-00000.parquet`.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ah-1` | read-only trace of `bd_txn_price`'s writer: inputs, outputs, accounts; class by the CTO's stated rule | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~61` |
| `CB-ah-2` | price basis `as_traded` in the chain (rule committed alone first), local build and re-grade, hold-CUSIP option | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~62` |
| `CB-ah-3` | SERVED re-mint of the three tables at the as-traded build, under a never-widen pair | FWD-3 | SERVED | CB-ah-1, CB-ah-2, both pair halves | `0.7.0_AE_CloudOps~CB2` |

**Fan-out:** `2 of 3 chains now, cap 8`. `CB-ah-3` is issued and spawned only after its dependencies and both pair halves exist. The
COO half is written on `CB-ah-2`'s build hashes.
