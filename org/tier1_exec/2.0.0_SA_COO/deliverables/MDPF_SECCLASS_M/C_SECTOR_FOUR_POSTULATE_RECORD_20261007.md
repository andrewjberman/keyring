# C-SECTOR four-postulate record -- sector and industry group on `etf-classifications` (MDPF_SECCLASS SC-e-25, FWD-12)

Author: 0.9.0_WK_MDPF_SECCLASS~24 for TO-SC-e25. Measured 2026-10-07 (UTC), read-only, us-east-1.
Values file (the evidence): `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/SECTOR_INDUSTRY_GROUP_VALUES_20261007.json`
(measuring script `R10_CHECKS/sector_industry_group_values.py`). Contract note C-SECTOR and C-NOCHAR (PRD ADDENDUM v0.5, v0.10) bind:
both attributes are labels; no measurement enters the table; the legacy `sector` attribute and `sub_asset_class` keep their bytes.

## Denominators printed (what was read)

- Bloomberg characteristics file, EVERY partition under `s3://opal-data-etfs/bbg/` that carries `characteristics.parquet`:
  32 partitions, 2026-08-20 .. 2026-10-05. Newest `bbg/2026-10-05/`, 114 rows.
- Column presence: `GICS_SECTOR_NAME` is present in all 32 partitions; `GICS_INDUSTRY_GROUP_NAME` is present only from
  2026-08-27 (27 partitions); the five partitions 2026-08-20..2026-08-26 carry no industry-group column (0 values, not a null).
- Sector: 10 distinct values in the newest partition AND in the union over all 32 partitions (the union adds nothing; each of the 10
  is seen from 2026-08-20 to 2026-10-05). The producer's `GICS_SECTORS` (`etf_positioning_gold.py:125`) has 11 names.
- Industry group: 23 distinct in the newest partition AND in the union over the 27 partitions that carry the column; each is
  seen from 2026-08-27 to 2026-10-05.
- Served ETF artifact `s3://opal-data-etfs/gold/holding/date=2026-10-05/holding.parquet`, 188 rows: `sub_asset_class` 11 distinct,
  57 null; `industry_group` 23 distinct, 65 null; `industry_group_basis` counts observed 123, security-not-in-characteristics 57,
  not-applicable-non-equity 8 (sum 188).

## Diffs between the three value sets (characteristics newest, served, producer `GICS_SECTORS`)

- Sector, characteristics vs served `sub_asset_class`: served has one value characteristics lacks, `Ultra Short Duration` (the
  producer's canonical cash-line sub-class, `ULTRA_SHORT_SUB_ASSET_CLASS`); characteristics has no value served lacks.
- Sector, characteristics vs producer `GICS_SECTORS`: producer has one value characteristics lacks, `Real Estate`; characteristics has
  no value the producer lacks (the ten are byte-identical to the producer's spelling).
- Sector, served vs producer: served lacks `Real Estate`; served has `Ultra Short Duration` which is not in `GICS_SECTORS`
  (it is in `SUB_ASSET_CLASS_VOCAB`). `Cash & Cash Equivalents` is in the producer vocab and not in the served artifact today.
- Industry group, characteristics vs served `industry_group`: NO diff, the 23 strings are identical in both.

## Observation that bears on the value list: the industry-group strings are vendor-truncated

Six of the 23 industry-group strings are exactly 30 characters and `Consumer Staples Distribution` / `Household & Personal Products`
are 29: `Commercial & Professional Serv`, `Consumer Discretionary Distrib`, `Health Care Equipment & Servic`, `Pharmaceuticals, Biotechnology`,
`Semiconductors & Semiconductor`, `Technology Hardware & Equipmen`. The producer header (`etf_positioning_gold.py:153-196`) records
that completing a truncated name is a SERVING-tier act (`inferred-from-truncation`), not gold. The served artifact carries the
truncated strings verbatim (no `inferred-from-truncation` row in the 188). This record proposes the values AS MEASURED.

---

## Attribute 1: SECTOR

Proposed attribute name: `gics_sector` (not `sector`, not `sub_asset_class`). Source field: Bloomberg `GICS_SECTOR_NAME`.
token census: 246 hits over 94 files, denominator 58819 files scanned (`comp-find '\bgics_sector\b' -i`, corpus=all, word-boundary).
Reading of the census: the hits are the rivalfunds gold shape (`data/etfs/scripts/rivalfunds/gold_canonical_shape.py` carries a
`gics_sector` column of another table and grain), the `mdpf-secclass` new-security-classifier column list, check scripts and audit
logs. No hit is an `etf-classifications` attribute; the name is a spelling the estate already uses for the same fact at another
grain, which is the reason to adopt it rather than mint a fresh one.

Proposed closed value list (11): `Communication Services`, `Consumer Discretionary`, `Consumer Staples`, `Energy`, `Financials`,
`Health Care`, `Industrials`, `Information Technology`, `Materials`, `Utilities` (these ten MEASURED in 32 of 32 partitions) and
`Real Estate` (HELD, not measured: the producer's `GICS_SECTORS` carries it and no characteristics partition has ever emitted it;
zero rows today). `Ultra Short Duration` and `Cash & Cash Equivalents` are NOT sector values.

Null / absent: no value is stored as a spelling of "unknown". A row with no `gics_sector` is one whose security is absent from the
characteristics file (57 of 188 served rows today) or is non-equity cash/fixed-income (served as `Ultra Short Duration` in
`sub_asset_class`, which is the other attribute's grain); the table row simply omits the attribute.

(i) MECE over the declared domain. Domain: "the GICS sector Bloomberg assigns to a security". The 11-name list is exhaustive of the
GICS sector level (11 sectors); hunted by subtraction from the printed denominator: measured 10 of 11 over 32 partitions, the
uncovered member is `Real Estate`, held and not measured; the reason it is absent from the
measurement is not measured here. Nothing measured falls outside the 11 (characteristics minus producer vocab is empty).
(ii) SAME GRAIN. One value per security (one row of `etf-classifications`), the grain of the characteristics file's row. It is
not the served `sub_asset_class` grain (allocation axis mixing 11 sectors with cash and ultra-short values), which is why
`sub_asset_class` is not re-pointed.
(iii) INTENT COHERENCE. One axis, one intent: the GICS sector label of the security. It carries no class, no cash marker, no
provenance and no measurement (C-NOCHAR).
(iv) STATE COHERENCE. A remedy that adds a security to the characteristics pull moves a row from absent to a value and moves
nothing else; a new GICS sector from the vendor moves the closed list only by a contract amendment; the legacy `sector` seed
attribute (179 rows) is not moved by either.

## Attribute 2: INDUSTRY GROUP

Proposed attribute name: `gics_industry_group` (not `sector`, not `sub_asset_class`, not the served `industry_group` column of the
holding artifact, which is a different table). Source field: Bloomberg `GICS_INDUSTRY_GROUP_NAME` (`GICS_INDUSTRY_GROUP_FIELD`).
token census: 155 hits over 43 files, denominator 58819 files scanned (`comp-find '\bgics_industry_group\b' -i`, corpus=all,
word-boundary). Reading: the same rivalfunds gold shape, the Bloomberg enrichment and daily-pull modules and checks; none is an
`etf-classifications` attribute.

Proposed closed value list (23, the measured set, verbatim including the vendor truncation): `Automobiles & Components`, `Banks`,
`Capital Goods`, `Commercial & Professional Serv`, `Consumer Discretionary Distrib`, `Consumer Durables & Apparel`,
`Consumer Services`, `Consumer Staples Distribution`, `Energy`, `Financial Services`, `Food, Beverage & Tobacco`,
`Health Care Equipment & Servic`, `Household & Personal Products`, `Insurance`, `Materials`, `Media & Entertainment`,
`Pharmaceuticals, Biotechnology`, `Semiconductors & Semiconductor`, `Software & Services`, `Technology Hardware & Equipmen`,
`Telecommunication Services`, `Transportation`, `Utilities`. Three values (`Energy`, `Materials`, `Utilities`) are spelled
identically to sector values; that is a GICS fact (single-group sectors), disambiguated by the attribute, never by the value.

Null / absent: an absent attribute, never a placeholder string. 65 of 188 served rows are null today: 57 security-not-in-characteristics
and 8 not-applicable-non-equity (the producer's `industry_group_basis`, which stays the served explanation and is not copied here).

(i) MECE over the declared domain. Domain: "the GICS industry group Bloomberg emits for this security in the characteristics file".
Subtraction from the printed denominator: the union over 27 partitions equals the newest partition equals the served set (23 = 23 =
23, empty diffs both directions), so no measured member lies outside the list; the list is closed over what was measured and is
NOT a claim about the full GICS group level (groups the book has never held, for example real-estate groups, are absent from
the measurement and would arrive as an unknown value, which the contract surfaces rather than admits).
(ii) SAME GRAIN. One value per security, one level finer than the sector and the same row grain as `gics_sector`; not a holding-row
grain (the holding artifact's `industry_group` is per holding row).
(iii) INTENT COHERENCE. One axis, one intent: the vendor's industry-group label for the security. It does not carry the truncation
repair, the basis/provenance word or any lifecycle rung; those stay on the publisher and the producer.
(iv) STATE COHERENCE. A completed-name decode at the serving tier moves the DISPLAYED spelling of six truncated values and none
of the stored ones; adding a security to the characteristics pull moves a row from absent to a value; neither moves
`gics_sector`, and a change to the sector list does not move this list.

## Cross-attribute check

The two attributes do not share an axis: sector (11-name, security grain) and industry group (23 measured names, finer level, same
security grain). Neither reads the other's source field, and neither carries `Ultra Short Duration`, `Cash & Cash Equivalents`
or `inferred-from-truncation`.
