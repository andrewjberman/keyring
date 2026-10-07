# TO MDPF_SECCLASS.TO-SC-e25 -- round 8 SC-e-25: FWD-12 (C-SECTOR) -- the sector and industry-group values measured, with their token census and four-postulate record

<to_id>MDPF_SECCLASS.TO-SC-e25</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~24</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-25` (`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) |
**outcome_ref:** FWD-12 | **depends_on:** none. Slot ~24's queue: this order, then `TO-SC-e27`, then `TO-SC-e28`.

---

## WORKER FACE

### THE CELL

`SC-e-25`: measure the sector and industry-group values, in the Bloomberg characteristics file the ETF producer reads and in the
served ETF artifact; write the token census and the four-postulate record for both attributes. A MEASUREMENT cell: no code
outside the one measuring script, no table write.

FWD-12 (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.12): "The shared list carries each security's sector
and industry group, and the Positioning page's ETF view shows sector, industry group, class and sub-class from the shared list."

Contract notes that bind this cell (PRD ADDENDUM v0.5 and v0.10):
- **C-SECTOR.** One NEW attribute on `etf-classifications` for the sector and one NEW attribute for the industry group, their names
  and closed values declared as data in `org/standards/MDPF_SECCLASS_CONTRACT.json` (cell `SC-e-27` declares them; this cell
  measures them) with the four-postulate record and a token census (rule 24). It is NOT the legacy `sector` attribute (179 seed
  rows of another grain), which keeps its bytes. `sub_asset_class` is not rewritten. The sector values are the names the ETF
  producer already adopts, so the page's vocabulary does not change.
- The industry-group source is the Bloomberg field the producer reads, `GICS_INDUSTRY_GROUP_FIELD = "GICS_INDUSTRY_GROUP_NAME"`
  (`data/etfs/scripts/gold/etf_positioning_gold.py:242`). The producer's header (`:153-196`) says the field's values were not yet
  measured in the served artifact: **the values are measured before they are declared** -- that is this cell.
- **C-NOCHAR.** Sector and industry group are labels. No measurement (ratio, market value, yield, duration, beta, price) enters the
  table.

**Inputs (measured by the issuer 2026-10-07, read-only; re-measure, do not copy):**
- **The Bloomberg characteristics file:** `s3://opal-data-etfs/bbg/<date>/characteristics.parquet`
  (`etf_positioning_gold.py:91` `BBG_ROOT = "bbg"`, `:1690` `_bbg_key(as_of, "characteristics.parquet")`). Newest partition with
  the file at the cut: `bbg/2026-10-05/`, 114 rows, columns `security, NAME, GICS_SECTOR_NAME, GICS_INDUSTRY_GROUP_NAME,
  GICS_INDUSTRY_GROUP, CNTRY_OF_DOMICILE, ...`; `GICS_SECTOR_NAME` 107 non-null, 10 distinct; `GICS_INDUSTRY_GROUP_NAME` 107
  non-null, 23 distinct. Read EVERY partition under `bbg/` that carries the file (32 partitions listed at the cut) and report the
  union and the per-partition sets, so a value seen once is not lost.
- **The served ETF artifact:** `s3://opal-data-etfs/gold/holding/date=<date>/holding.parquet` (newest at the cut 2026-10-05,
  188 rows, 31 columns). The sector there is `sub_asset_class` (11 distinct, 57 null), the industry group `industry_group`
  (23 distinct, 65 null), with `industry_group_basis` (3 distinct).
- **The producer's adopted vocabulary:** `GICS_SECTORS` at `etf_positioning_gold.py:125` (11 names, byte-identical to Bloomberg
  `GICS_SECTOR_NAME` per its comment), `SUB_ASSET_CLASS_VOCAB` at `:150`, `INDUSTRY_GROUP_BASIS_VOCAB` at `:230`.

**Build:**
1. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/sector_industry_group_values.py`: reads the inputs above
   (read-only, us-east-1) and writes
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/SECTOR_INDUSTRY_GROUP_VALUES_<YYYYMMDD>.json` (UTC run date) in
   exactly this shape (the issuer's check reads it):
   `{"measured_at": "<iso>", "sources": {"characteristics": {"key": "s3://opal-data-etfs/bbg/<newest date>/characteristics.parquet",
   "rows": N, "sector_values": [...], "industry_group_values": [...]}, "served_holding": {"key": "s3://...holding.parquet",
   "rows": N, "sector_values": [...], "industry_group_values": [...]}}, "union_over_partitions": {...}, "per_partition": {...},
   "producer_vocab": {"GICS_SECTORS": [...]}, "diffs": {...}}`. The `characteristics` source is the NEWEST partition's file.
   `diffs` names every value in one set and not another (characteristics vs served vs the producer's `GICS_SECTORS`).
2. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/C_SECTOR_FOUR_POSTULATE_RECORD_<YYYYMMDD>.md`: for EACH of the two
   attributes, the four postulates by name -- (i) MECE over the declared domain, hunted by subtraction from the printed
   denominator; (ii) SAME GRAIN; (iii) INTENT COHERENCE; (iv) STATE COHERENCE (which values one remedy does not move) -- the
   proposed attribute name (not `sector`, not `sub_asset_class`), the proposed closed value list, how a null/absent value reads,
   and a token census line `token census: <n> hits over <files> files, denominator <files scanned>` for each proposed name
   (word-boundary, over the repo, via `comp-find`).
3. ASCII only.

### ACCEPTANCE

<criterion id="SC8-e25-AC1" cell_refs="SC-e-25"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/issuer_check_sc_e25.py values</invocation><expect>SC-E25-VALUES ok=True</expect></criterion>
`SC8-e25-AC1` -- the values file carries both sources with keys, denominators and value sets, and its characteristics sets equal a fresh read of that S3 file.

<criterion id="SC8-e25-AC2" cell_refs="SC-e-25"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/issuer_check_sc_e25.py record</invocation><expect>SC-E25-RECORD ok=True</expect></criterion>
`SC8-e25-AC2` -- the record states the four postulates for both attributes and a token census with its denominator.

<expected_criteria>SC8-e25-AC1,SC8-e25-AC2</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`no SECTOR_INDUSTRY_GROUP_VALUES_*.json`); AC2 FAIL as expected. Green arm
(a values file built from the live 2026-10-05 file): `SC-E25-VALUES ok=True sector=10 industry_group=23 rows=114`; negative arm
(one sector dropped): `ok=False sector values differ from a fresh read`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted. The issuer check `R10_CHECKS/issuer_check_sc_e25.py` is READ-ONLY to you.
- **Read-only against AWS.** No S3 write, no table write, no deploy. No vendor or model call.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W24-S<k>`), and do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/sector_industry_group_values.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/SECTOR_INDUSTRY_GROUP_VALUES_*.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/C_SECTOR_FOUR_POSTULATE_RECORD_*.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-25`.
<owned_cells>SC-e-25</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e25-AC1, SC8-e25-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~24/MDPF_SECCLASS.TO-SC-e25.sector-industry-group-values.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e25-AC1,SC8-e25-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the two proposed attribute names and value lists, every diff between the three value sets, the partitions read, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery (comp-schedule --owner 2.0.0_SA_COO~M --budget 120, 2026-10-07 ~07:3xZ): 8 gates name the lane, all open deploy-ledger entries; none names C-SECTOR or the characteristics file. A measurement cell arms nothing.
comp-iam: RUN -- R8 battery (comp-iam gaps): 0 gap lines name etf-classifications or secclass. This cell reads S3 only with the worker's session credentials; it declares no role.
comp-adversary: RUN -- R8 battery on the decomposition; cell-specific reads by the issuer 2026-10-07: the characteristics home (etf_positioning_gold.py:91, :1690; 32 bbg partitions, newest with the file 2026-10-05, 114 rows), the served holding artifact (gold/holding/date=2026-10-05/holding.parquet, 188 rows). BLIND: whether values outside the newest partition exist (step 1 reads all partitions); bbg/2026-10-06/ was not listed at ~07:4xZ 2026-10-07.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.12 @87ad6d2e4c (FWD-12, ADDENDUM v0.5 C-SECTOR, v0.10); DECOMP_R8 @495efa3c32.
