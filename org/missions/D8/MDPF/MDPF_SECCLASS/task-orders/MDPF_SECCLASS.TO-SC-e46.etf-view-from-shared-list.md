# TO MDPF_SECCLASS.TO-SC-e46 -- round 9 SC-e-46 (SC-e-29 re-cut): FWD-12 -- the ETF view takes sector, industry group, class and sub-class from the shared list for the Opal ETFs' held universe: producer change built, before/after read, release requested of site Z

<to_id>MDPF_SECCLASS.TO-SC-e46</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~36</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-46` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-12, FWD-6 | **depends_on:** MDPF_SECCLASS.TO-SC-e54 (contract 0.6.0: 11 sectors, the full industry-group names
and the decode table) AND two issuer acts: the sector writer applied (TO-SC-e28's root, by a laptop cloud-operations seat through
`safe-apply`) and the sector-row write (its own signed half, `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SECTOR_ROWS_20261007.md`). The worker
starts only after all three; the issuer hands this order to slot `~36` (fourth in its queue) once the write act's change-management
entry is closed.

**Placement ruling:** laptop `1.0.0_SA_CTO`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_FOR_THE_DELLS_20261007_0740Z.md`
section 2: the BUILD is dell1's under `2.0.0_SA_COO~M1`; the RELEASE is site Z's under ETFS_POSITIONING's own ledger and never-widen
halves; for the life of this cell the dell1 worker is the ONE writer of `data/etfs/scripts/gold/etf_positioning_gold.py`.

---

## WORKER FACE

### THE CELL

`SC-e-46`: "SC-e-29 re-cut: the ETF view producer takes sector, industry group, class and sub-class from the shared list for the
four Opal ETFs' held universe (2.1); before/after per holding" (DECOMP_R9). Build only: the release is site Z's.

- FWD-12 (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.13, title amended in place by ruling 2.1): the shared
  list carries the sector and industry group of each security an Opal ETF holds; "every holding in an ETF's view shows the sector and
  the industry group the shared list gives it, and the page takes no sector, industry group or class from anywhere else."
- Ruling 2.1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md`): "What is no longer
  promised: a sector on rows no Opal ETF holds ... The source stays the Bloomberg characteristics leg the ETF producer already reads.
  The round-9 census grades coverage over the four Opal ETFs' held universe. A held security the leg does not return is a C-PULL cell
  at site Z under the daily vehicle's existing vendor use; nothing is guessed from a name."
- C-SECTOR: `gics_sector` and `gics_industry_group` are the two fields (names from the contract, never typed twice); the legacy
  `sector` attribute and `sub_asset_class` are not read for sector. C-NOCHAR: no measurement moves onto the list.

**What the producer does today (measured in round 8, TO-SC-e29; re-read before you edit):**
- It reads `s3://opal-data-etfs/bbg/<date>/characteristics.parquet` (`etf_positioning_gold.py:1690`) and takes the sector per holding
  from it (`gics = hc["GICS_SECTOR_NAME"]`, `:1211`); the industry group via `industry_group_of()` (`:1021`) from
  `GICS_INDUSTRY_GROUP_FIELD = "GICS_INDUSTRY_GROUP_NAME"` (`:242`), basis enum `INDUSTRY_GROUP_BASIS_VOCAB` (`:230`).
- The file covers 114 securities; the sector writer planned 107 rows (TO-SC-e28's dry run). The producer's vocabulary is 11 sectors
  (`GICS_SECTORS`, `:125`): keep it, and keep an empty sector rendering as before.
- Served output: `s3://opal-data-etfs/gold/holding/date=<date>/holding.parquet` (2026-10-05: 188 rows; sector in `sub_asset_class`).
- The existing producer tests are scripts, not pytest: `test_etf_positioning_industry_group.py`,
  `test_etf_positioning_sector_order_carriers.py`, `test_etf_positioning_per_fund_asof.py`, `test_etf_positioning_upgrade_forward.py`
  (the last two need `PYTHONPATH="<repo root>;<repo root>/infra/aws/lambda/v2_portal/_shared"`). Run all four before and after.

**Build:**
1. **The producer change** in `data/etfs/scripts/gold/etf_positioning_gold.py`: for every holding key, read `gics_sector`,
   `gics_industry_group`, `asset_class` and `sub_asset_class` from `etf-classifications` (consistent reads, batched) and use them as
   the holding's sector, industry group, class and sub-class. A holding with no shared-list value carries the producer's existing
   absent reading (an `industry_group_basis` value already in the vocabulary; name it, or stop and file a row -- never mint one).
   Cash and ultra-short rows keep their existing rules.
2. **Tests** `data/etfs/scripts/gold/test_etf_positioning_shared_list_sector.py` (pytest, DynamoDB stubbed): a holding takes the shared
   list's four values even where the characteristics file disagrees; a holding with no entry reads absent with the stated basis; the
   11-sector order holds with an empty sector; no measurement column changes.
3. **The before/after** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/etf_view_before_after.py`: BEFORE = the
   newest served holding artifact (read-only); AFTER = the changed producer's holding table built IN MEMORY from the same day's inputs
   and the live shared-list rows (no S3 write); writes `M/ETF_VIEW_BEFORE_AFTER_<YYYYMMDD>.json` in the shape the issuer check reads
   (`read_at, fields, denominator, rows[{book, ticker, key, before, after, shared_list}]`), with the coverage over the four Opal ETFs'
   held universe (keyed / with a shared-list sector / absent) and the sector write's run list named; prints
   `ETF-VIEW-BEFORE-AFTER date=<d> holdings=<n> from_shared=<n> absent=<n> changed_sector=<n> changed_industry_group=<n>`.
4. **The half request** `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_ETF_VIEW_<YYYYMMDD>.md`, addressed to site Z's ETFS_POSITIONING halves:
   the act (release of the producer change: upload and the next scheduled run), its BLAST RADIUS (the served `gold/holding` and
   `gold/book` partitions from the first run on, the columns that move, the row counts from step 3), the rollback per key, lines
   `BRANCH A:` and `BRANCH B:`, and the headings `## ETFS_POSITIONING COO half -- UNSIGNED` and `## ETFS_POSITIONING CTO half -- UNSIGNED`.
   List every held security the leg does not return as a C-PULL candidate for site Z (ruling 2.1).
5. ASCII only.

### ACCEPTANCE

<criterion id="SC9-e46-AC1" cell_refs="SC-e-46"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/etfs/scripts/gold/test_etf_positioning_shared_list_sector.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC9-e46-AC1` -- the producer takes the four values from the shared list, reads absent where it has none, keeps the 11-sector order.

<criterion id="SC9-e46-AC2" cell_refs="SC-e-46"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/issuer_check_sc_e29.py beforeafter</invocation><expect>SC-E29-BEFOREAFTER ok=True</expect></criterion>
`SC9-e46-AC2` -- every keyed holding's after-values equal its shared-list values, and a fresh read of the live table agrees.

<criterion id="SC9-e46-AC3" cell_refs="SC-e-46"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/issuer_check_sc_e29.py half</invocation><expect>SC-E29-HALF ok=True</expect></criterion>
`SC9-e46-AC3` -- the half request to site Z names the blast radius, the rollback and both branches, with both halves unsigned.

<expected_criteria>SC9-e46-AC1,SC9-e46-AC2,SC9-e46-AC3</expected_criteria>

Dry-run at the base 5d70aab6c9: AC1 FAIL as expected (`PYTEST-BAD rc=4`, no test file); AC2 FAIL as expected
(`no ETF_VIEW_BEFORE_AFTER_*.json`); AC3 FAIL as expected (`no NEVER_WIDEN_HALF_REQUEST_SECCLASS_ETF_VIEW_*.md`). The two checks are
round 8's (TO-SC-e29), reused unchanged.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
  The R10 issuer checks and the contract are READ-ONLY to you.
- **No S3 upload, no run of the producer against served output, no release, no deploy, no table write, no vendor or model call.**
  The after-view is built in memory. The release is site Z's act.
- **No package install and no download of any kind** (row S49).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W36-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
data/etfs/scripts/gold/etf_positioning_gold.py
data/etfs/scripts/gold/test_etf_positioning_shared_list_sector.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/etf_view_before_after.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/ETF_VIEW_BEFORE_AFTER_*.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_ETF_VIEW_*.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-46`.
<owned_cells>SC-e-46</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e46-AC1, SC9-e46-AC2, SC9-e46-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~36/MDPF_SECCLASS.TO-SC-e46.etf-view-from-shared-list.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e46-AC1,SC9-e46-AC2,SC9-e46-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the before/after line, the held-universe coverage, the absent basis chosen, the four script tests before and after, the
C-PULL candidate list size, the half path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery (comp-schedule --owner 2.0.0_SA_COO~M --budget 120: 6 of 6 carriers, C1=23 C2=18 C3=12 C4=21 C5=334 C6=1): no armed gate names the ETF positioning producer change for this seat; BLIND: site Z's own schedules (the release gate is site Z's ETFS_POSITIONING ledger), which this box's carriers do not hold.
comp-iam: RUN -- round 8 (TO-SC-e29): the producer's deployed role reading etf-classifications is a release-time question for site Z's half; this cell reads with the worker's session credentials.
comp-adversary: RUN -- ruling 2.1's population (the Opal ETFs' held universe; C-PULL for a gap); round 8's producer reads (:1211, :1021, :242, :1690, :125); the served holding (2026-10-05, 188 rows); the writer's 107 planned rows. BLIND: the filled rows (they exist only after the issuer's write act).
risk floor: SERVED -- the change moves served columns at release; the release is site Z's.
ruling: CTO_RULINGS_FOR_THE_DELLS_20261007_0740Z.md section 2, one writer of etf_positioning_gold.py for the cell's life.
lane: the <paths> block IS the grant. data/etfs/scripts/gold is outside the pre-push deploy gate's PIPELINE_MAP (bd, inf, cot).
</preflight>

Source: PRD v0.13 FWD-12, FWD-6 @90f99888cd; analysis ruling 2.1 @1ca9e97fc9; DECOMP_R9 @5d70aab6c9; TO-SC-e29 (round 8, superseded).
