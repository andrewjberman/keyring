# MDPF_SECCLASS decomposition -- ROUND 8 (drafted by 2.0.0_SA_COO~M on the laptop, 2026-10-07 ~07:4xZ; NOT ISSUED)

**Status: DECOMPOSED, NOT ISSUED.** This seat issues nothing. The round's one issuer is the successor `2.0.0_SA_COO~M1` on dell1
(1.0.0_SA_CTO msg 106024, on Andrew-direct ~07:0xZ 2026-10-07, record `ANDREW_DIRECT_20261007_070xZ_DELLS_ARE_WORKHORSES_*`).
The issuer reads this file through `<decomp_ref>` and derives the fan-out from the edges below.

**Cut on:**
- PRD v0.12 @87ad6d2e4c (`org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md`), RATIFIED, FWD-1 to FWD-17. Addenda v0.4 to
  v0.12 each place their work in "the next MDPF_SECCLASS round"; this is that round.
- 1.0.0_SA_CTO msg 106024: run the v0.12 decomposition on the laptop now.
- 1.0.0_SA_CTO's half `CTO_HALF_MDPF_SECCLASS_MULTI_ASSET_REMAP_B_20261007.md` @ed687ec668, condition 1: the seed module, the AI
  classifier's vocabulary, the Holdings contract enum and the portal class lists are "the next cell".
- **No round-7 analysis exists** (the CTO's last round analysis on disk is round 6, `CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_6_20261001.md`).
  The spine cuts an enrichment round over the enrichment list of the round-N analysis; here the list is read from the PRD addenda's
  own "bind the next round's cells" notes. That substitution is this seat's and is stated, not hidden: a round-7 analysis that
  orders the list differently replaces this ordering.

**State the round starts from (measured this session, 2026-10-07):**
1. `etf-classifications`: 3,507 rows, 0 `multi_asset` (full consistent scan after the rule-B remap, commit 0d9457b639). Classes
   present: equity 2,785, fixed_income 679, structured 20, commodities 12, alternatives 11. **No row reads `cash`.**
2. The seed module `infra/aws/lambda/v2_portal/_shared/etf_classification.py` carries the token `multi_asset` 25 times. The seed
   script does not run until it carries the six-class values (CTO condition 1).
3. The contract `org/standards/MDPF_SECCLASS_CONTRACT.json` is v0.4.0 with seven fields (`instrument_kind`, `identifier_namespace`,
   `classified_by`, `classification_confidence`, `low_confidence`, `security_bloomberg`, `listing_country`). It carries no sector
   field, no industry-group field and no key form for a security with neither ticker nor CUSIP.
4. `multi_asset` in code outside this seat's check scripts: the three `HoldingsSnapshot.schema.json` copies (5 occurrences each),
   `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (1) and its two test files, and 17 files under `portal/src`
   (`git -C portal grep -l multi_asset -- src`; 26 on the loose pattern that adds the label `Multi-Asset`; see cell SC-e-23's write set).
5. Cottonwood `B_01b` is at its pre-8f67065e50 body in S3 and in the repo (rows S40, S41). The old list's writers W1 to W3
   (analysis `docs/briefs/one-classification-table-consolidation-analysis-20261005.md` section 4.2) still exist in the trees.
6. The push deploy gate uploads changed gold scripts and the shipped `lib/_shared/etf_classification*.py` copies to S3 at the push,
   before any half is signed (rows S35, S39; 0.0.0_AB_MSTR msg 106027 names three shipped copies written to `opal-data-cot`).
   **Every cell below that edits a shipped file names that in its risk; its half is signed before the commit reaches a pushed range.**

## Rule 24 record

- **Domain (declared):** the PRD v0.12 work no earlier round delivered: the addenda's contract notes for FWD-11 to FWD-17, FWD-6
  as amended, the new surfaces S21 to S26, and CTO condition 1.
- **(i) MECE, by subtraction from the printed denominator.** The denominator is the 17 outcomes. Each is placed exactly once in
  the table "Outcome coverage" below: served by a cell of this round, carried as an issuer act on an open ledger, or deferred to a
  named later round with the reason. 17 of 17 placed; none is in two rows.
- **(ii) Same grain.** Every cell is one write set a single worker serves in one worktree. An act that writes a live table, stops a
  scheduled writer or moves a served artifact is NOT a cell: it is the issuer's act under its own never-widen pair.
- **(iii) Intent coherence.** One cell, one intent. Where two intents meet in one file, the file has one owning cell and the other
  intent's line is deferred to that cell (stated in the write sets).
- **(iv) State coherence -- what one remedy does not move.** Filling rows (FWD-11, FWD-17) does not move a reader off the old list
  (FWD-13, FWD-5). Stopping the old list's writers does not empty it. Declaring a field in the contract does not populate it.

## The cells

Status vocabulary: `NOT-EVALUATED` (no worker has served the cell), `SERVED`, `REFUSED`, `SUPERSEDED`. Every cell starts
`NOT-EVALUATED`. Ids continue shape 1 of `org/standards/DECOMP_CELL_ID_CONVENTION.md` from round 7's `SC-e-20`.

| cell | what | serves | status | placement | risk | depends on |
|---|---|---|---|---|---|---|
| `SC-e-21` | The seed module carries the six-class values for the 19 funds (33 keys) the rule-B remap moved, so the seed plan reads 0 CONFLICT against the live table; a seed dry run printed | FWD-3, CTO condition 1 | NOT-EVALUATED | dell1 | SERVED (a shipped `_shared` module: the push gate uploads its copies) | -- |
| `SC-e-22` | The `HoldingsSnapshot` schema's class enum loses `multi_asset` in its three copies, read equal to each other after | FWD-2, FWD-16 | NOT-EVALUATED | dell2 (IRPT_BCKEND Holdings workstream, `2.0.0_SA_COO~M2`) | SERVED | `SC-e-23` |
| `SC-e-23` | The portal's class lists, legends, colours and layouts lose `multi_asset`; the two reader tests that assert it are rewritten to assert six classes | FWD-2, FWD-16, C-SERVER | NOT-EVALUATED | dell1 (portal DEV) | SERVED | -- |
| `SC-e-24` | The census of every screen that shows a mix by class: the groups it shows, and one stated mapping from the six classes to them, as data; the geography list S26 placed | FWD-16 | NOT-EVALUATED | dell1 | LOCAL | -- |
| `SC-e-25` | Measure the sector and industry-group values: in the Bloomberg characteristics file the ETF producer reads and in the served ETF artifact; the token census and the four-postulate record for both attributes | FWD-12 (C-SECTOR) | NOT-EVALUATED | dell1 | LOCAL | -- |
| `SC-e-26` | The old list measured: its 10,873 rows partitioned (already in both lists; held today; the rest) and by key form (ticker, `CUSIP:`, `NAME::<slug>`, none); a proposed key form for a security with neither ticker nor CUSIP with its four-postulate record | FWD-17, FWD-15 | NOT-EVALUATED | dell1 | LOCAL | -- |
| `SC-e-27` | The contract's next version, the one writer of the contract file this round: the two C-SECTOR attributes with their closed values, the new key form, and the pin test moved to the new version | FWD-12, FWD-17 | NOT-EVALUATED | dell1 | LOCAL | `SC-e-25`, `SC-e-26` |
| `SC-e-28` | The scheduled sector writer: copies the sector and the industry group from the Bloomberg characteristics file onto each security's row; names and homes from builder output; built, tested, dry run against live inputs; declared Terraform not applied; its half request | FWD-12 | NOT-EVALUATED | dell1 | WORLD | `SC-e-27` |
| `SC-e-29` | The ETF view's producer takes sector, industry group, class and sub-class from the shared list; per ETF, every holding's four values listed before, delta 0 expected | FWD-12, FWD-6 | NOT-EVALUATED | PLACEMENT OPEN: ETFS_POSITIONING's tree and release; the fabric is the CTO's to name | SERVED | `SC-e-28` and the issuer's write act that fills the rows |
| `SC-e-30` | The clean-name rule: one function with a test table (proper case, vendor suffixes and all-caps removed), used for every row | FWD-14, FWD-11 | NOT-EVALUATED | dell1 | LOCAL | -- |
| `SC-e-31` | The AI classifier in service after the direct-match plan: the residual writer called for what the plan leaves UNRESOLVED, the value bound (six classes, the table's own sub-classes), the conditional put, the clean name from `SC-e-30`, and the AI-made index listing rewritten by each run | FWD-11 (C-AIINDEX, C-VENDOR) | NOT-EVALUATED | dell1 | WORLD (an outside-model call under Andrew's recorded word; a new S3 address) | `SC-e-30` |
| `SC-e-32` | The old list's reclassification set: every old row not in the shared list, through the direct-match plan and then `SC-e-31`'s path, held securities first; the row set, a dry-run writer and the half request. The write is the issuer's act | FWD-17, FWD-15 | NOT-EVALUATED | dell1 | WORLD | `SC-e-26`, `SC-e-27`, `SC-e-31` |
| `SC-e-33` | The missing list on demand: for each of the three firms, the held securities with no entry in the shared list and their total | FWD-15 | NOT-EVALUATED | dell1 | LOCAL | -- |
| `SC-e-34` | The clean names for the rows the table already holds: the row set (current name, clean name) from `SC-e-30`'s function, a dry-run writer and the half request | FWD-14 | NOT-EVALUATED | dell1 | WORLD | `SC-e-30` |
| `SC-e-35` | The old list stops growing, Black Diamond tree: `B_01b`'s step leaves the gold dispatch and the four classification scripts (W3) are retired from any trigger; the half request | FWD-5 | NOT-EVALUATED | dell1 | SERVED | -- |
| `SC-e-36` | The old list stops growing, Cottonwood tree: `B_01b`'s step leaves the Cottonwood gold dispatch; the half request | FWD-5 | NOT-EVALUATED | dell1 | SERVED | -- |
| `SC-e-37` | The old list stops growing, Inflection tree: `classify_assets.py` stops writing the old list; the half request | FWD-5 | NOT-EVALUATED | dell1 | SERVED | -- |
| `SC-e-38` | The trace of who reads the old list: Advisor Intelligence's screens, the news curation function (S22) and `resolve_tickers.py` (S25), each with the artifact or call it reads and a verdict | FWD-5 | NOT-EVALUATED | dell1 | LOCAL | -- |
| `SC-e-39` | The Holdings producer tries `CUSIP:<security_id>` after a symbol miss; the 187 securities it newly places listed before; the producer's `multi_asset` line removed; the half request | FWD-13 | NOT-EVALUATED | dell2 (IRPT_BCKEND Holdings workstream, `2.0.0_SA_COO~M2`) | SERVED | -- |
| `SC-e-40` | The FWD-4 census re-run with the surfaces S22 to S26 in its denominator and the planted-copy control re-read | FWD-4 | NOT-EVALUATED | dell1 | LOCAL | -- |

20 cells. Placement: dell1 17, dell2 2, open 1.

## Write sets (disjoint; `M/` = `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/`, `R10/` = `M/R10_CHECKS/`)

- **SC-e-21:** `infra/aws/lambda/v2_portal/_shared/etf_classification.py`; `infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py`;
  `R10/seed_six_class_dry_run.py`; `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SEED_SIX_CLASS_<date>.md`.
- **SC-e-22:** `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`;
  `infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json`;
  `infra/aws/lambda/investor-reporting/holdings/contracts/HoldingsSnapshot.schema.json`; `infra/aws/terraform/investor-reporting/CHANGELOG.json`.
- **SC-e-23** (portal repo, paths under `portal/src/`). The 17 files that carry the token `multi_asset`
  (`git -C portal grep -l multi_asset -- src`, 17 of 17 listed): `lib/chartColors.ts`;
  `pages/AdvisorIntelligence/__tests__/mdpf-secclass/multi-asset.readers.test.ts`;
  `pages/AdvisorIntelligence/_partners/{49financial,cottonwood,demo,inflection}/layout.ts`;
  `pages/AdvisorIntelligence/_shared/components/{AdvisorAnalytics,PartnerAnalytics}.tsx`;
  `pages/AdvisorIntelligence/_shared/lib/composition.ts`; `pages/AdvisorIntelligence/_shared/panels/ConsolidatedOverviewPanel.tsx`;
  `pages/AdvisorIntelligence/_shared/types/TenantLayoutConfig.ts`;
  `pages/InvestorReporting/__tests__/dsgn-irptv1/{iv-e-12.cash-green.test.ts,iv-e-148.multi-asset-class-readers.test.ts}`;
  `pages/InvestorReporting/contracts/{adapt.ts,index.ts}`; `pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts`;
  `pages/InvestorReporting/tabs/holdings/assetClass.ts`.
  Six more files carry only the label `Multi-Asset` or `multiAsset` as a security class and are in the write set for the worker to
  triage: `components/holdings/HoldingsTreemapChart.tsx`; `pages/InvestorReporting/tabs/holdings/{HoldingsTreemap.tsx,SecurityList.tsx}`;
  `pages/InvestorReporting/__tests__/dsgn-irptv1/{iv-e-114.securities-map-walk.test.tsx,iv-e-115.order-and-disclosure.test.tsx}`;
  `components/market-performance/MarketRegimeIndicator.tsx`.
  NOT in the cell: the three files of the Market Performance page's Multi-Asset tab (`pages/MarketPerformance/MarketPerformance.tsx`,
  `constants.ts`, `tabs/MultiAssetTab/MultiAssetTab.tsx`); that is a market view's name, not a security class (read by file name
  only, not opened at this cut). Loose-pattern denominator: 26 files = 17 + 6 + 3.
- **SC-e-24:** `R10/screen_group_census.py`; `M/SCREEN_GROUP_MAPPING_<date>.json`; `M/SCREEN_GROUP_MAPPING_<date>.md`.
- **SC-e-25:** `R10/sector_industry_group_values.py`; `M/SECTOR_INDUSTRY_GROUP_VALUES_<date>.json`;
  `M/C_SECTOR_FOUR_POSTULATE_RECORD_<date>.md`.
- **SC-e-26:** `R10/old_list_census.py`; `M/OLD_LIST_CENSUS_<date>.json`; `M/KEY_FORM_PROPOSAL_<date>.md`.
- **SC-e-27:** `org/standards/MDPF_SECCLASS_CONTRACT.json`; `infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py`.
- **SC-e-28:** `infra/aws/lambda/mdpf-secclass/sector-writer/` (`lambda_function.py`, `tests/`);
  `infra/aws/terraform/mdpf-secclass/sector-writer/`; `infra/logic/registry/` rows ONLY if the naming builder refuses (rule 30);
  `R10/sector_writer_dry_run.py`; `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SECTOR_ROWS_<date>.md`.
- **SC-e-29:** `data/etfs/scripts/gold/etf_positioning_gold.py` and its tests; `R10/etf_view_before_after.py`;
  `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_ETF_VIEW_<date>.md`.
- **SC-e-30:** `infra/aws/lambda/v2_portal/_shared/security_name.py`; `infra/aws/lambda/v2_portal/_shared/tests/test_security_name.py`.
- **SC-e-31:** `infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py`;
  `infra/aws/lambda/v2_portal/_shared/tests/test_model_classifier.py`; `infra/aws/lambda/mdpf-secclass/ai-index/` (the listing
  writer and its tests); `R10/ai_classifier_dry_run.py`. The classifier's own class vocabulary (CTO condition 1's second member)
  is this cell's line, because this cell owns the file.
- **SC-e-32:** `R10/old_list_reclassify_set.py`; `R10/old_list_reclassify_write.py`; `M/OLD_LIST_RECLASSIFY_SET_<date>.tsv`;
  `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_OLD_LIST_RECLASSIFY_<date>.md`.
- **SC-e-33:** `R10/missing_list.py`; `M/MISSING_LIST_<firm>_<date>.json` (three files).
- **SC-e-34:** `R10/clean_name_row_set.py`; `R10/clean_name_write.py`; `M/CLEAN_NAME_ROW_SET_<date>.tsv`;
  `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CLEAN_NAMES_<date>.md`.
- **SC-e-35:** `data/black_diamond/scripts/gold/gold_dispatch.sh`; `data/black_diamond/scripts/gold/B_01b.classify_new_securities.py`;
  `data/black_diamond/scripts/classification/{classify_bd_securities.py,seed_bd_securities.py,seed_canonical_securities.py,backfill_name_aliases.py}`;
  `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_OLD_LIST_WRITERS_<date>.md`.
- **SC-e-36:** the Cottonwood gold dispatcher under `data/cot/scripts/gold/` (the worker names the file; it was not read at this
  cut); `data/cot/scripts/gold/B_01b.classify_new_securities.py`; `data/cot/scripts/gold/tests/test_other_admission.py`;
  `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_OLD_LIST_WRITER_<date>.md`.
- **SC-e-37:** `data/inf/scripts/classification/classify_assets.py` and its caller (named by the worker);
  `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_INF_OLD_LIST_WRITER_<date>.md`.
- **SC-e-38:** `R10/old_list_reader_trace.py`; `M/OLD_LIST_READER_TRACE_<date>.md`.
- **SC-e-39:** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`;
  `data/assets/scripts/gold/investor_reporting/tests/{test_holdings_snapshot.py,test_holdings_narrowed.py}`;
  `R10/holdings_cusip_lookup_before.py`; `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_HOLDINGS_CUSIP_LOOKUP_<date>.md`.
- **SC-e-40:** the FWD-4 census instrument (the worker names its path from task order `MDPF_SECCLASS.TO-SC-e3`; not read at this
  cut); `M/FWD4_CENSUS_<date>.json`.
- Every cell may append its own rows to the surprise channel
  `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`.
- **Hookups that belong to no cell** (the issuer adds them at the merge): the `.owned-paths.yaml` lane lines for the new
  directories of `SC-e-28` and `SC-e-31` (the CTO's carrier); the shipped-artifacts entry for `security_name.py`.

## Dependency edges (real data dependencies, keyed to observed completion)

- `SC-e-23` -> `SC-e-22`: the page drops the value before the published contract does (PRD addendum v0.7: the contract changes
  with its consumer first).
- `SC-e-25` -> `SC-e-27` and `SC-e-26` -> `SC-e-27`: the contract declares values and a key form only after they are measured.
- `SC-e-27` -> `SC-e-28` -> the issuer's sector write act -> `SC-e-29`.
- `SC-e-30` -> `SC-e-31` -> `SC-e-32`; `SC-e-26` -> `SC-e-32`; `SC-e-27` -> `SC-e-32` (the key form).
- `SC-e-30` -> `SC-e-34`.
- Independent: `SC-e-21`, `SC-e-24`, `SC-e-33`, `SC-e-35`, `SC-e-36`, `SC-e-37`, `SC-e-38`, `SC-e-39`, `SC-e-40`.

**Chains** (a maximal path; two cells on one chain never run at once):
A `SC-e-23` then `SC-e-22`. B `SC-e-25` then `SC-e-27` then `SC-e-28` then `SC-e-29`. C `SC-e-26` then `SC-e-27` (joins B).
D `SC-e-30` then `SC-e-31` then `SC-e-32`. E `SC-e-30` then `SC-e-34` (branches from D). Nine single-cell chains.
The fan-out is the issuer's to state as `fanout:` data; the first wave has 13 cells with no unmet edge (`SC-e-21`, `23`, `24`,
`25`, `26`, `30`, `33`, `35`, `36`, `37`, `38`, `39`, `40`), above the default cap of 8.

## Outcome coverage (denominator 17)

| outcome | this round | carried or deferred |
|---|---|---|
| FWD-1 | -- | carried: open ledgers `secclass-bd-thread-r2-and-irpt-narrowed-m-20260930`, `secclass-bd-thread-r3-m-20261001` (issuer reads) |
| FWD-2 | `SC-e-22`, `SC-e-23` | the cross-surface read (backlog item 12) is deferred until the readers of `SC-e-38` are switched |
| FWD-3 | `SC-e-21` | the one-edit exercise (backlog item 11) follows the seed run, an issuer act |
| FWD-4 | `SC-e-40` | -- |
| FWD-5 | `SC-e-35`, `SC-e-36`, `SC-e-37`, `SC-e-38` | reader switches and the delete are later rounds (Andrew's act at the end) |
| FWD-6 | `SC-e-29` | the departure register's reader-visible marking is deferred to the round after the ETF view moves |
| FWD-7 | -- | carried: live; the ordinary scheduled run is its standing check |
| FWD-8 | -- | deferred: Andrew's word of 2026-10-06 (only the AI classifier fills a blank `instrument_kind`) rides `SC-e-31`'s path in a later round |
| FWD-9 | -- | the one-year depth is owned by MDPF_SECHIST from v0.12; no cell here |
| FWD-10 | -- | carried: live since 2026-10-06 14:00Z |
| FWD-11 | `SC-e-30`, `SC-e-31` | -- |
| FWD-12 | `SC-e-25`, `SC-e-27`, `SC-e-28`, `SC-e-29` | -- |
| FWD-13 | `SC-e-39` | the removal of the Holdings fallback is deferred until `SC-e-32`'s rows are written (PRD addendum v0.7) |
| FWD-14 | `SC-e-30`, `SC-e-34` | the page printing the list's name (the `HoldingsSnapshot` name field, consumer first) is deferred until the names are written |
| FWD-15 | `SC-e-33`, `SC-e-26`, `SC-e-32` | -- |
| FWD-16 | `SC-e-24`, `SC-e-22`, `SC-e-23` | the mapping shown on each screen is deferred to the round after the census |
| FWD-17 | `SC-e-26`, `SC-e-27`, `SC-e-32` | -- |

## Issuer acts this round creates or inherits (not cells)

- The seed run after `SC-e-21` (its own pair). The sector row write after `SC-e-28`. The AI classifier's first run and the old
  list's reclassification write after `SC-e-31` and `SC-e-32`. The clean-name write after `SC-e-34`. Each stop of an old-list
  writer after `SC-e-35` to `SC-e-37`. Each has its own never-widen pair and ledger entry.
- Inherited open ledgers, 8 (comp-schedule C2, owner `2.0.0_SA_COO~M`): `bd-securities-cot-new-p1-m-20260926`,
  `cot-cash-admission-m-20260925`, `secclass-bd-residual-cusip-rows-m-20261002`, `secclass-bd-thread-r2-and-irpt-narrowed-m-20260930`,
  `secclass-bd-thread-r3-m-20261001`, `secclass-cot-cusip-rows-m-20261002`, `secclass-cot-repoint-m-20261002`,
  `secclass-multi-asset-remap-b-m-20261007` (legs H and G: each firm's next Holdings build, the next Cottonwood and Black Diamond
  gold runs).

## Battery

- **`comp-schedule`: RUN** (`comp-schedule --owner 2.0.0_SA_COO~M --budget 120`, 2026-10-07 ~07:3xZ). Complete view, 6 of 6
  carriers, denominators C1=23, C2=18, C3=12, C4=21, C5=334, C6=1. Gates naming this lane: 8, all open deploy-ledger entries,
  listed above. Blindness: the tool reads the repo only; it does not read whether a schedule fired.
- **`comp-iam`: RUN** (`comp-iam gaps`, same time). DESIRED plane only, 541 `.tf` files in 3 trees. 0 gap lines name
  `etf-classifications`, `bd-securities` or `secclass`. Blindness: it cannot see a grant Terraform does not declare, and the
  roles `SC-e-28` and `SC-e-31` need do not exist yet, so a zero here says nothing about them. Each of those two cells runs
  `comp-iam service <function>` on its own declared Terraform.
- **`comp-adversary`: RUN** (`comp-adversary compose` on this file before its commit, read-vintage HEAD @e37552ef87,
  2026-10-07T07:21:50Z). Cited commits 2 attempted, 2 verified. Cited paths 23 attempted, 21 stable, 2 flagged GONE: both are the
  new files `SC-e-30` creates (`_shared/security_name.py` and its test), so the flag is expected. Blindness, as the tool states it:
  this file is not a task order, so the neighborhood is filesystem adjacency, not the dependency chain: 899 uncited siblings, 25
  shown. Two of the shown siblings are named for `SC-e-39`'s worker to read before it edits the producer:
  `data/assets/scripts/gold/investor_reporting/holdings_49f.py` and `holdings_inf.py` (not opened at this cut).
- No other lens of the catalog was run.

## Not read at this cut

The Cottonwood gold dispatcher's file name; the FWD-4 census instrument's path; the Bloomberg characteristics file's home; which
function hosts the direct-match plan's UNRESOLVED list at run time; the brief's and the analysis's counts (10,873 old rows, 2,378
in both, 187 `CUSIP:` rows, 58 with no ticker and no CUSIP, 668 labelled by ticker shape) are held from the research seat and are
re-measured by `SC-e-26` and `SC-e-39`, not by this seat.
