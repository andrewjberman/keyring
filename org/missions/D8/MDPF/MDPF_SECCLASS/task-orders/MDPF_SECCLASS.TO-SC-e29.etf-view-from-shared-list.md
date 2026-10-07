# TO MDPF_SECCLASS.TO-SC-e29 -- round 8 SC-e-29: FWD-12 -- the ETF view takes sector and industry group from the shared list: producer change built, before/after read, release requested of site Z

<to_id>MDPF_SECCLASS.TO-SC-e29</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~24</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>superseded</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-29` (`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) |
**outcome_ref:** FWD-12 | **depends_on:** MDPF_SECCLASS.TO-SC-e28 AND the issuer's sector-row write act (the apply and first
real fire of the SC-e-28 writer under its own signed half). The worker starts only after BOTH; the issuer hands this order by
continuing slot ~24 once the write act's change-management entry is closed. Slot ~24's fourth order, the tail of chain B.

**Placement ruling:** `1.0.0_SA_CTO` (laptop), `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_FOR_THE_DELLS_20261007_0740Z.md`
section 2 (shared tree `/c/Dev/ajb_workspace`): the BUILD is dell1's under `2.0.0_SA_COO~M1`; the RELEASE is site Z's under
ETFS_POSITIONING's own ledger and never-widen halves; for the life of this cell the dell1 worker is the ONE writer of
`data/etfs/scripts/gold/etf_positioning_gold.py`.

---

## WORKER FACE

### THE CELL

`SC-e-29`: change the ETF producer so the Positioning page's ETF view takes each holding's sector and industry group from the
shared list (`etf-classifications`, the two fields `TO-SC-e27` declared and the sector writer filled), test it, and read the view
BEFORE and AFTER against the rows that write filled. Build only: the release is site Z's.

- FWD-12 (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.12): "every holding in an ETF's view shows the
  sector and the industry group the shared list gives it, and the page takes no sector, industry group or class from anywhere
  else."
- C-SECTOR: the two fields are new; the legacy `sector` attribute and `sub_asset_class` in the table are not read for this.
  C-NOCHAR: no measurement moves onto the list; the characteristics file keeps feeding the producer's measurement columns.

**What the producer does today (measured by the issuer 2026-10-07):**
- It reads `s3://opal-data-etfs/bbg/<date>/characteristics.parquet` (`etf_positioning_gold.py:1690`) and takes the sector per
  holding from it: `gics = hc["GICS_SECTOR_NAME"]` (`:1211`); the industry group via `industry_group_of()` (`:1021`) from
  `GICS_INDUSTRY_GROUP_FIELD = "GICS_INDUSTRY_GROUP_NAME"` (`:242`), with the basis enum `INDUSTRY_GROUP_BASIS_VOCAB` (`:230`).
- The file covers **114 securities** (newest partition `bbg/2026-10-05/`, 107 non-null for each field), so the sector writer
  fills at most that many table rows, and holdings outside it keep no shared-list sector.
- The file shows **10 distinct sectors**; the producer adopts **11** (`GICS_SECTORS`, `:125`). The panel's sector order must stay
  the 11-name vocabulary, and a sector with no holding today renders as before (do not drop the eleventh).
- Served output: `s3://opal-data-etfs/gold/holding/date=<date>/holding.parquet` (newest 2026-10-05, 188 rows; sector in
  `sub_asset_class`, 11 distinct, 57 null; `industry_group` 23 distinct, 65 null; `industry_group_basis` 3 distinct).
- The existing producer tests are scripts (`python <file>`), not pytest: `test_etf_positioning_industry_group.py`,
  `test_etf_positioning_sector_order_carriers.py`, `test_etf_positioning_per_fund_asof.py`,
  `test_etf_positioning_upgrade_forward.py`; the last two need `PYTHONPATH="<repo root>;<repo root>/infra/aws/lambda/v2_portal/_shared"`
  (their headers). Run all four before and after your change and report each result.

**Build:**
1. **The producer change.** In `data/etfs/scripts/gold/etf_positioning_gold.py`, read the two fields from `etf-classifications`
   (field names from `org/standards/MDPF_SECCLASS_CONTRACT.json` at the version TO-SC-e27 landed, never typed twice: one
   constant each) for every holding key, and use them as the holding's sector and industry group. A holding with no shared-list
   value carries the producer's existing absent reading (an `industry_group_basis` value already in the vocabulary; state which
   one, or, if none fits, stop and file a surprise row -- do not mint a basis value). Cash and ultra-short rows keep their
   existing rules. The page's vocabulary (11 sectors, the order carriers) does not change.
2. **Tests.** `data/etfs/scripts/gold/test_etf_positioning_shared_list_sector.py`, pytest style, DynamoDB stubbed: a holding takes
   the shared list's sector and industry group even where the characteristics file disagrees; a holding with no entry reads
   absent with the stated basis; the 11-sector order holds when one sector has no holding; no measurement column changes.
3. **The before/after.** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/etf_view_before_after.py`: BEFORE
   = the served holding artifact of the newest date (read-only); AFTER = the changed producer's holding table built IN MEMORY
   from the same day's inputs and the live shared-list rows (no S3 write); writes
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/ETF_VIEW_BEFORE_AFTER_<YYYYMMDD>.json` in the shape the issuer check
   reads (`fields`, `denominator`, one row per holding with `book, ticker, key, before, after, shared_list`), and prints
   `ETF-VIEW-BEFORE-AFTER date=<d> holdings=<n> from_shared=<n> absent=<n> changed_sector=<n> changed_industry_group=<n>`.
   The `shared_list` values are the rows the sector write filled; name its run list in the JSON.
4. **The half request.** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_ETF_VIEW_<YYYYMMDD>.md`,
   addressed to site Z's ETFS_POSITIONING halves: the act (release of the producer change: upload and the next scheduled run),
   its BLAST RADIUS (the served `gold/holding` and `gold/book` partitions from the first run on, the columns that move, the row
   counts from step 3), the rollback per key (the prior producer bytes by commit; the prior partitions), lines `BRANCH A:`
   (values equal the before/after) and `BRANCH B:` (they do not: what then), and the headings
   `## ETFS_POSITIONING COO half -- UNSIGNED` and `## ETFS_POSITIONING CTO half -- UNSIGNED`.
5. ASCII only.

### ACCEPTANCE

<criterion id="SC8-e29-AC1" cell_refs="SC-e-29"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/etfs/scripts/gold/test_etf_positioning_shared_list_sector.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC8-e29-AC1` -- the producer takes sector and industry group from the shared list, reads absent where it has none, and keeps the 11-sector order.

<criterion id="SC8-e29-AC2" cell_refs="SC-e-29"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/issuer_check_sc_e29.py beforeafter</invocation><expect>SC-E29-BEFOREAFTER ok=True</expect></criterion>
`SC8-e29-AC2` -- every keyed holding's after-values equal its shared-list values, and a fresh read of the live table agrees.

<criterion id="SC8-e29-AC3" cell_refs="SC-e-29"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/issuer_check_sc_e29.py half</invocation><expect>SC-E29-HALF ok=True</expect></criterion>
`SC8-e29-AC3` -- the half request to site Z names the blast radius, the rollback and both branches, with both halves unsigned.

<expected_criteria>SC8-e29-AC1,SC8-e29-AC2,SC8-e29-AC3</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (no test file); AC2 FAIL as expected (`no ETF_VIEW_BEFORE_AFTER_*.json`);
AC3 FAIL as expected (`no NEVER_WIDEN_HALF_REQUEST_SECCLASS_ETF_VIEW_*.md`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`,
  uncommitted. The R10 issuer checks are READ-ONLY to you; so is the contract file.
- **No S3 upload, no run of the producer against served output, no release, no deploy.** The after-view is built in memory;
  nothing is written to `opal-data-etfs`. No table write. No vendor or model call. The release is site Z's act.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W24-S<k>`), and do not weaken the test.

<paths>
data/etfs/scripts/gold/etf_positioning_gold.py
data/etfs/scripts/gold/test_etf_positioning_shared_list_sector.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/etf_view_before_after.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/ETF_VIEW_BEFORE_AFTER_*.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_ETF_VIEW_*.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-29`.
<owned_cells>SC-e-29</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e29-AC1, SC8-e29-AC2, SC8-e29-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~24/MDPF_SECCLASS.TO-SC-e29.etf-view-from-shared-list.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e29-AC1,SC8-e29-AC2,SC8-e29-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the before/after line, the absent basis chosen, the four existing script tests' results before and after, the half
request path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery (2026-10-07 ~07:3xZ): no armed gate names the producer change; the release gate is site Z's ETFS_POSITIONING ledger.
comp-iam: RUN -- R8 battery: the producer's deployed role reading etf-classifications is a release-time question for site Z's half; this cell reads with the worker's session credentials.
comp-adversary: RUN -- R8 battery; issuer reads 2026-10-07: producer sector source (:1211, :1021, :242, :1690), served holding (2026-10-05, 188 rows), characteristics coverage 114 securities, 10 of 11 sectors; the two pytest-collected producer test files fail import without PYTHONPATH (they are scripts). BLIND: the filled rows (they exist only after the issuer's write act).
risk floor: SERVED -- the change moves served columns at release; the release is site Z's.
ruling: org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_FOR_THE_DELLS_20261007_0740Z.md section 2 (shared tree), one writer of etf_positioning_gold.py for the cell's life.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.12 @87ad6d2e4c (FWD-12, ADDENDUM v0.5, v0.10); DECOMP_R8 @495efa3c32.

## CLOSE -- SUPERSEDED, CARRIED TO ROUND 9 (2.0.0_SA_COO~M1, 2026-10-07 ~10:3xZ, on 1.0.0_SA_CTO~DELL1 msg 160)

`<status>` superseded: carried to round 9: its two inputs are not served -- TO-SC-e28's sector writer is built (proof VALID @fdc388f145) but not applied (dell1 holds no provider; validate and apply ride safe-apply), and the issuer's sector-row write needs its own half (NEVER_WIDEN_HALF_REQUEST_SECCLASS_SECTOR_ROWS_20261007.md, both halves UNSIGNED). No worker started this order.
The round-8 drain-end read is `deliverables/2.0.0_SA_COO~M1/DRAIN_END_R8_20261007.md` @572829ce3b. Gate limb: none graded this modification.
