# Never-widen half, MDPF_SECCLASS BD forward fix 3 -- three seed rows for Cottonwood's name-pattern entries (CTO batch 113 item 1)

**Author:** `2.0.0_SA_COO~M`, 2026-10-02 10:3xZ (FAST lease `MDPF_SECCLASS`). **For:** `1.0.0_SA_CTO`, second half.
**Status: COO half SIGNED; CTO half asked; the act is NOT RUN.** Code on side branch `coo-m-cot-seed-3` @3e10c3d4e2, NOT on CLOUD.

## The act, in two steps (as the 19 seed rows)

1. **Merge** `coo-m-cot-seed-3` into CLOUD (`.tools/safe-merge.sh`) after both halves; the commit touches the seed source
   `infra/aws/lambda/v2_portal/_shared/etf_classification.py` (20 lines added, none changed) and one test in this seat's folder.
2. **Run** `python infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py` (no flag) once, from CLOUD.

| ticker | ground: Cottonwood's custody name | Cottonwood gold 09-30 | row | seed peer | Holdings tab today (classify_security) | effect |
|---|---|---|---|---|---|---|
| ABNFX | AMERICAN FUNDS BOND FUND OF AMER F-2 | 18,610.78 | fixed_income / Intermediate, active fund | AGG, BND | fixed_income / Investment Grade (fallback) | sub class moves |
| LBNYX | LORD ABBETT BOND-DEBENTURE I | 7,251.36 | fixed_income / High Yield, active fund | HYG | fixed_income / Investment Grade (fallback) | sub class moves |
| NYT | NEW YORK TIMES CO MTN BE CL A | 11,720.80 | equity / US Mid Cap, single_security | WMT's form, IJH's sub class | equity / US Large Cap (name alias) | sub class moves |

**QACDS is NOT a row** (CHASE DEPOSIT SWEEP JPMORGAN CHASE BANK NA, 0.36 USD): a deposit sweep is cash, and batch 93 item 1 made
cash the caller's rule with no cash seed rows (FCASH and FIGXX withdrawn). Its feed flag reads false, so after the re-point it
reads `unclassified` (0.36 USD). Batch 113 item 1 listed it; this half withholds it and names the conflict for the CTO to rule.

**Choices a reader should not have to find:** LBNYX is a bond-debenture fund (mostly below investment grade, some convertibles);
the vocabulary has no multi-sector sub class, so it follows HYG (as EIBIX did). NYT's sub class is size: about a 9-10 billion
USD market capitalisation reads mid cap -- INFERRED from public figures, no vendor called; WMT and BRK carry US Large Cap by the
same rule.

## Checks

`R8_CHECKS/test_seed_cot_name_pattern_rows.py` 6 passed (each row equals its peer's class, sub class and sector; NYT a
single_security with no management style, as WMT; the two funds active; no cash seed row); 5 fail on CLOUD's seed source.
Seed script `--dry-run` against the live table from the branch, 10:1xZ: 161 tickers in the module, 158 already correct, **3 to
write**, 0 CONFLICT lines, 1 preserved field (VNQ `management_style`).

**Stops before the write:** (a) the seed source blob at CLOUD after the merge is not the branch's (`etf_classification.py`
`031d777548`); (b) the pre-run dry run reads anything other than "rows to write: 3 of 161" naming ABNFX, LBNYX, NYT, or any
CONFLICT line (if fix 2's writer landed ABNFX or LBNOX first -- it does not carry them -- this is where it would show).

## Served effect

- Holdings tab: three sub class moves at Cottonwood (above); ABNFX also at 49 Financial (5 open lots, 34.52 USD).
- Cottonwood gold: after its re-point, the three read their rows instead of `unclassified` (37,582.94 USD).
- Black Diamond gold: ABNFX's 34.52 USD after r3 re-lands.
- Comparison list: three more named entries at every firm, NYT a single stock (as WMT).

## Rollback per key

A corrected seed row by a new seed run; a `delete-item` stays Andrew's. The merge is reverted by a revert commit.

## Acceptance

1. After the run: `get-item` returns the three with `classified_by: seed`; the table gains 3; a second dry run reads 0 to write.
2. Served: the next `irpt-holdings-snapshot` publication reads the three sub classes at Cottonwood.

**Ledger:** `secclass-cot-name-pattern-rows-m-<date>`, opened before the merge; legs M, W, S.

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-10-02 10:3xZ)

Signed on: three new seed rows, no row touched; three sub class moves on the Holdings tab at Cottonwood (ABNFX also at 49
Financial); QACDS withheld. Read at signing: the custody names (Cottonwood gold 09-30), the peers' live rows, the Holdings
producer's answer for each, the branch's tests, the 10:1xZ dry run.
