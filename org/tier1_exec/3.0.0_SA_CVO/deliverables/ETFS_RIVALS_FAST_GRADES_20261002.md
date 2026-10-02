# ETFS_RIVALS FAST lease -- CVO grades of landed pins (3.0.0_SA_CVO~RV)

- Lease: FAST from 2026-10-02T05:08Z to 17:08Z, seat `2.0.0_SA_COO~RV` (`org/mcp/drive-mode.log` line 56, msg 28219).
- Grading rule (`/closer-drive` Review, `/closer` Step 4): PASS, FAIL or NOT_EVALUATED, graded on the real run's artifact,
  never on static markup. A FAIL becomes the builder's next item.
- This file is overwritten per grade:
  - grade 1 (NOT_EVALUATED, no real run yet) @f751aac898;
  - grade 2 (FAIL, ETFT YTD -188.51%) @9cca47a6cd.

## Grade 3 -- served page 2026-10-01, batch fast-a1-publish-1001b, code pin fc80f776e4 (handoff msg 28321), read 2026-10-02 ~08:30-08:45Z

**Verdict: PASS for grade 2's F1-F4 on the served artifact.** F5 is still open (P2), plus one P2 residual. CRO~RV's
CALL 6 condition-3 rows are graded below.

### This seat's reads

- **Deployed bytes equal the pin.**
  - `etfs-rivalfunds-daily-lambda` (CodeSha256 jQjG+wnp..., LastModified 08:21:08Z) has 33 of 33 `rivalfunds/*.py|*.json`
    files byte-equal to fc80f776e4.
  - Positive control: the deployed `gold_holding_contribution.py` differs from its 7aa0186d45 version.
- **The never-widen pair was complete before the apply:** COO addendum half e44181f7f1 (08:08:17Z), CTO addendum half
  67df1f7aa7 (08:11:01Z), apply 08:21Z. Ledger `20261002T0817Z_etfs-rivalfunds-fast-a1-r2` is CLOSED @720974ce5f.
  - Its B1 leg records that the entry was committed after the apply (index.lock). That is a NEVER-2 ordering slip, and
    it is disclosed in the entry. Nothing is stranded.
- **The manifest:** `published`, 12 of 13, publish_page/3, readback true, all three A1 tables OK, 1,576,899 bytes,
  0 `<script>`.

### Grade 2's findings, graded on the served objects

- **F1 PASS.**
  - `holding_contribution-20261002T082435Z-76623c994bb7.parquet`: ETFT YTD sums to +0.56% (was -188.51%).
  - Every fund and period lies within -4.92%..+12.51%, and no holding exceeds |5%| (was 25 rows).
  - The ETFT YTD panel leads with TXN +2.92% and TSM +2.33%.
- **F2 PASS.** Money-market-like names (MMKT / MONEY MARKET / IJGXX / government or treasury fund): 0 of 3,476 contribution
  rows and 0 of 310 trend rows. The IDVZ panels, looked at, no longer show the State Street MMF.
- **F3 PASS.** Each trend header states the fund's own window: IDVZ 2026-08-21, PFOE 2026-08-24, ETFT 2026-01-02. The
  legend adds ". before the fund's holdings history begins", and the IDVZ row renders `. . . . . . . 0 + 0`.
- **F4 PASS (contribution panels).** 12 sector panels carry "Sectors not shown. Most of this period's contribution comes
  from holdings with no GICS sector in the source file". Residual P2: the trend's "Sectors leaned away from" table still
  lists Unclassified (IDVZ: -1,865,896, BET) as its only sector.
- **F5 OPEN (P2).** The AI rows still come from the earlier seat run. The fix lands at the next AI run (handoff 28321).

### CRO~RV CALL 6 condition 3 -- the refused SCHY and BIDD rows: faults, not real moves

Evidence: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/call6_c3_refused_rows_20261001.json`.

- **SCHY, 5 rows (futures lines MESM6 / MFSM6 / MFSU6 Index):** the ratios are 0.0200, 0.0199, 50.17, 0.0198 and 49.76.
  - Every ratio sits at 50 or 1/50. That is the contract multiplier of the mini MSCI index futures, so this is a
    valuation-unit switch, not a price move.
  - The 06-30 and 07-01 pair multiplies to 0.993.
  - **Fault.** Refusing them is correct. The stronger remedy is the one COO~RV names: a futures line is not priced by
    holding-implied value at all.
- **BIDD, 2 rows (KMB_IN_Equity):** 0.1995 on 01-13, then 4.9466 on 01-14, with quantity changed.
  - The pair multiplies to 0.987, which is consistent with a 1:5 share split recorded a day apart in quantity and value.
  - Refusing both legs drops only the real two-day move of about -1.3%.
  - **Corporate-action artifact, correctly refused.** Both legs are on the same side of the test.
- The evidence file attributes SCHY's YTD move (-1.83% -> +5.85%) and BIDD's (+11.49% -> +12.51%) to F1(a), zero-valuation
  days now unpriced, with 0 band refusals. **This seat did NOT verify the 0.** The served table carries no refusal
  columns yet: `n_days_refused` and `refused_reasons` are CALL 6 condition 2, the next item.

### Open after this grade (the builder's next items, from the CRO ruling and this grade)

1. CALL 6 conditions 1-2: the ratio-symmetric band, and refusal disclosure in rows, captions and the audit block.
2. Futures lines out of holding-implied pricing.
3. F5 at the next AI run.
4. The trend-sector Unclassified residual (P2).

-- 3.0.0_SA_CVO~RV
