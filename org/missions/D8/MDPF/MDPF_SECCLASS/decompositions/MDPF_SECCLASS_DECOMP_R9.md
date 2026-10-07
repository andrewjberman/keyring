# MDPF_SECCLASS decomposition -- ROUND 9 (2.0.0_SA_COO~M1, dell1, 2026-10-07 ~11:3xZ; NOT ISSUED)

**Status: DECOMPOSED, NOT ISSUED.** The issuer is this seat (laptop 1.0.0_SA_CTO ruling 106036; 1.0.0_SA_CTO~DELL1 msg 181: "recut round 9
in ONE issuance from the analysis's section 4").

**Cut on:**
- PRD v0.13 @90f99888cd (`org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md`), L4-R ADMITTED (ratified-text re-signed by
  3.0.0_SA_CVO against the v0.13 ENDPOINT; brief auto). FWD-12's title amended in place (S44).
- The round-8 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md` @1ca9e97fc9:
  section 4 items 1-7 are this round's rectangle, read with section 2 (ENDPOINT rulings 2.1-2.10) and section 3 (row rulings).
  Item 8's rows are carried, not cells (see "Carried rows").
- The round-8 drain-end read `deliverables/2.0.0_SA_COO~M1/DRAIN_END_R8_20261007.md` @572829ce3b and the CVO's compile
  (ADJUDICATION_v6/v7, REMEDIATION_v6).

**State the round starts from (measured this session, 2026-10-07):**
1. The six-class module is on the trunk and in both firm buckets (`code/gold/lib/_shared/etf_classification.py` ETag 3a033c04 in
   opal-data-bd and opal-data-cot; rows S51, S52). S46 and S50 closed (S52, S53). No seed run (option b).
2. The old list's reader trace (`M/OLD_LIST_READER_TRACE_20261007.md`, 46-file census) reads 5 NEEDS-OLD-LIST sections:
   a07 (`data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py`, never reads `etf-classifications`), `resolve_tickers.py`
   (reads `asset_name_raw` and `name_aliases`, which the canonical table does not carry), `bd_securities_fallback.py` and
   `holdings_snapshot.py` (IRPT Holdings: canonical-first already, old-list fallback for a miss), and `etf_classification_scheduled.py`
   (the canonical producer; its only wired input is the old list). CANONICAL-PRODUCER is NONE for every real reader: `e18-scheduled`
   0 rows, `mdpf-secclass-scheduled` 348 rows, all CUSIP-keyed, 2026-09-30.
3. The census excluded the Black Diamond tree: 13 non-test files under `data/black_diamond/` name the table literally (re-read now; W25-S5
   said 16 with tests), and the IRPT fallback assembles the name at run time (W25-S5).
4. SC-e-35/36/37's served code is kept on branch `wk-MDPF_SECCLASS-27` (42239a4f2a, b8b17cbbdd, 6a996787eb), off every pushed range.
5. SC-e-28's sector writer is built (proof VALID @fdc388f145), not applied: dell1 holds no Terraform provider; the apply is a laptop
   cloud-operations seat's act through `safe-apply` (rule 13 lane, laptop 1.0.0_SA_CTO msg 106176).
6. Contract `org/standards/MDPF_SECCLASS_CONTRACT.json` reads 0.5.0 (gics_sector 10 values, gics_industry_group 23, NAME key form).
7. dell1's principal is denied the three firm buckets (W25-S1); held sets are local producer builds, `inferred` (ruling 2.9).

## Rule 24 record

- **Domain (declared):** the analysis's section 4 items 1-7, each step of each item, with the rulings of sections 2 and 3 it cites.
- **(i) MECE by subtraction from the printed denominator.** Denominator: 7 items with 17 steps. Every step is placed once below: a cell
  (17 cells, SC-e-41..57) or an issuer act. Item 1's "one reader-switch cell per real reader" counts 3 code switches (a07,
  resolve_tickers, the producer's input); the IRPT Holdings reader is already canonical-first, so its switch condition is the producer's
  live write (SC-e-44 then an issuer act), not a code cell -- stated, not dropped.
- **(ii) Same grain.** One cell = one write set one worker serves in one worktree. Table writes, uploads, applies and model calls are
  issuer acts under their own pairs.
- **(iii) Intent coherence.** One intent per cell. The sector writer's decode-table use rides SC-e-54 (item 6), because the decode table
  is declared in the contract file that cell owns and the writer is its one consumer.
- **(iv) State coherence -- what one remedy does not move.** A reader switch does not give a first-held security a row (SC-e-44 and its
  live run do). Stopping a writer does not empty the old list. A contract value does not populate a field. A row set does not write rows.

## The cells

| cell | item | what | serves | placement | risk | depends on |
|---|---|---|---|---|---|---|
| `SC-e-41` | 1 | The widened reader census (W25-S5): the 13 BD-tree files that name the table, the runtime-assembled names (`'%s-securities'` via the naming registry), and the role-level grants (e.g. `opal-news-lambda-role` AmazonDynamoDBFullAccess); one section per reader with MISSING-ROW / SERVED-NEW / CANONICAL-PRODUCER, as SC-e-38 | FWD-5 | dell1 | LOCAL | -- |
| `SC-e-42` | 1 | a07 reads `etf-classifications` first and falls to the old list only on a miss; the switch's before/after per held key listed (delta named) | FWD-5, FWD-2 | dell1 | SERVED (shipped shared home `data/assets/scripts/gold/`: held off pushed ranges until its half signs) | -- |
| `SC-e-43` | 1 | `resolve_tickers.py` resolves a name from the canonical table's `name` first, the old list as fallback; the attributes the canonical table lacks (`asset_name_raw`, `name_aliases`) are named as the gap | FWD-5 | dell1 | SERVED | -- |
| `SC-e-44` | 1 | The canonical producer's input: `etf_classification_scheduled.py` gains a non-old-list input (the Bloomberg/GICS leg through `rivalfunds_classification`, the Schwab master) so a first-held security can get a canonical row; dry run over the latest held set (inferred) lists the keys it would now plan | FWD-5, FWD-7, FWD-10 | dell1 | SERVED (a shipped `lib/_shared` member: held until its half signs) | -- |
| `SC-e-45` | 1 | The three old-list writer stops re-presented from `wk-MDPF_SECCLASS-27` at the round-9 base: re-proved, and their halves re-written to name every real reader's switch and the producer's live write count | FWD-5 | dell1 | SERVED (shipped BD and Cottonwood gold scripts: held) | `SC-e-41`, `SC-e-42`, `SC-e-43`, `SC-e-44`, issuer act "producer live" |
| `SC-e-46` | 2 | SC-e-29 re-cut: the ETF view producer takes sector, industry group, class and sub-class from the shared list for the four Opal ETFs' held universe (2.1); before/after per holding | FWD-12, FWD-6 | build dell1; release site Z (ruling 106047 (2)) | SERVED | `SC-e-54`, issuer acts "sector writer applied" and "sector rows written" |
| `SC-e-47` | 3 | `clean_name` repair (W28-S5): acronyms, tickers used as names, small words; the test table grows with the measured failures | FWD-14 | dell1 | WORLD (gate floor for `infra/`) | -- |
| `SC-e-48` | 3 | The clean-name row set regenerated with the repaired function, plus held unnamed rows named from the custody feed's security name (2.2); dry-run writer; half request | FWD-14 | dell1 | WORLD | `SC-e-47` |
| `SC-e-49` | 4 | FWD-15 (2.3): the FWD-11 runner planned over SC-e-33's per-firm missing lists, held-first, after the direct-match plan; dry run with 0 model calls; the model-call count named for the issuer's run; half request | FWD-15, FWD-11 | dell1 | WORLD | `SC-e-54` |
| `SC-e-50` | 4 | FWD-17 (2.4, 2.5): the whole-old-list census under the held definition (non-zero market value in the latest served holdings partition; dell1 reads `inferred`, a served grade is a laptop seat's row), and the reclassification set refreshed with the 15 cash rows re-planned under the contract bound | FWD-17 | dell1 | WORLD | `SC-e-54` |
| `SC-e-51` | 5 | FWD-16: the IR securities table's Cash fold made consistent with the same tab's treemap and class bar | FWD-16 | dell1 (portal DEV) | SERVED | -- |
| `SC-e-52` | 5 | FWD-16: `PerfrpAllocation.tsx` prints display labels, not raw lower-case class tokens | FWD-16 | dell1 (portal DEV) | SERVED | -- |
| `SC-e-53` | 5 | FWD-16: Attribution's `etf-categories.ts` static list aligned to the producer's two-group funnel (Andrew-direct 2026-10-06) | FWD-16 | dell1 (portal DEV) | SERVED | -- |
| `SC-e-54` | 6 | The contract edits, one cell (2.5-2.7): every class's closed `sub_asset_class` list as the bound (cash included); `gics_sector` adds Real Estate (11); `gics_industry_group` carries the full GICS names with a vendor-spelling decode table in the same file; pin tests; the sector writer maps through the decode table (a spelling not in it leaves the field empty and is listed) | FWD-12, FWD-17, FWD-11 | dell1 | WORLD (gate floor for `infra/`) | -- |
| `SC-e-55` | 7 | C-S13: 49 Financial's firm mix serves the residual as its own "Unclassified" line so the top-level mix sums to 1.0 (`d06_firm_mix_summary.py`); half request | FWD-2, FWD-13 | dell1 | SERVED (shipped shared home: held) | -- |
| `SC-e-56` | 7 | S27: the Holdings producer falls back to `CUSIP:<security_id>` after a symbol miss | FWD-13 | **PLACEMENT OPEN** | SERVED | -- |
| `SC-e-57` | 7 | S28: the FWD-10 producer stops writing a GICS sector into `sub_asset_class` (sector lands only in `gics_sector`); existing rows not rewritten before FWD-12's writer runs | FWD-10, FWD-12 | dell1 | WORLD (gate floor for `infra/`) | -- |

17 cells. Placement: dell1 16 (SC-e-46's release at site Z), open 1.

**PLACEMENT OPEN, SC-e-56:** its one file, `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, is R8's `SC-e-39` (the same
CUSIP fallback, placed on dell2 under the `2.0.0_SA_COO~M2` Holdings workstream and never issued). One writer per file: the CTO rules
whether SC-e-56 IS SC-e-39 (cut once, on dell2) or moves to dell1. This decomposition does not resolve it.

## Write sets (disjoint; `M/` = `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/`, `R11/` = `M/R11_CHECKS/`)

- **SC-e-41:** `R11/old_list_reader_census_bd.py`; `M/OLD_LIST_READER_TRACE_BD_<date>.md`.
- **SC-e-42:** `data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py`; `data/assets/scripts/gold/runners_49f/tests/test_a07_canonical_first.py`;
  `R11/a07_switch_before_after.py`; `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_A07_CANONICAL_FIRST_<date>.md`.
- **SC-e-43:** `data/black_diamond/scripts/classification/resolve_tickers.py`; `R11/resolve_tickers_switch_check.py`.
- **SC-e-44:** `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`; `infra/aws/lambda/v2_portal/_shared/tests/test_etf_classification_scheduled.py`;
  `R11/producer_input_dry_run.py`; `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_PRODUCER_INPUT_<date>.md`.
- **SC-e-45:** the six BD files and the Cottonwood and Inflection files of TO-SC-e35/36/37 (`data/black_diamond/scripts/gold/gold_dispatch.sh`,
  `.../gold/B_01b.classify_new_securities.py`, `data/black_diamond/scripts/classification/{classify_bd_securities,seed_bd_securities,seed_canonical_securities,backfill_name_aliases}.py`,
  `data/cot/scripts/gold/gold_dispatch.sh`, `data/cot/scripts/gold/B_01b.classify_new_securities.py`, `data/inf/scripts/classification/classify_assets.py`);
  the three half requests under `M/` named by TO-SC-e35/36/37.
- **SC-e-46:** `data/etfs/scripts/gold/etf_positioning_gold.py` and its tests; `R11/etf_view_before_after.py`; `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_ETF_VIEW_<date>.md`.
- **SC-e-47:** `infra/aws/lambda/v2_portal/_shared/security_name.py`; `infra/aws/lambda/v2_portal/_shared/tests/test_security_name.py`;
  (the issuer-owned table `M/R10_CHECKS/sc_e30_clean_name_table.py` gains the W28-S5 cases at the cut; the worker does not edit it).
- **SC-e-48:** `R11/clean_name_row_set_v2.py`; `R11/clean_name_write_v2.py`; `M/CLEAN_NAME_ROW_SET_V2_<date>.tsv`; `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CLEAN_NAMES_V2_<date>.md`.
- **SC-e-49:** `R11/fwd15_ai_plan.py`; `M/FWD15_AI_PLAN_<firm>_<date>.json` (three); `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD15_AI_<date>.md`.
- **SC-e-50:** `R11/old_list_census_held.py`; `M/OLD_LIST_CENSUS_HELD_<date>.json`; `M/OLD_LIST_RECLASSIFY_SET_V2_<date>.tsv`.
- **SC-e-51:** `portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx` and its test.
- **SC-e-52:** `portal/src/pages/AdvisorIntelligence/_shared/perfrp/PerfrpAllocation.tsx` and its test.
- **SC-e-53:** `portal/src/pages/Attribution/constants/etf-categories.ts` and its readers' test.
- **SC-e-54:** `org/standards/MDPF_SECCLASS_CONTRACT.json`; `infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py`;
  `infra/aws/lambda/mdpf-secclass/sector-writer/lambda_function.py` and `.../sector-writer/tests/`.
- **SC-e-55:** `data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py` and its test; `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_D06_UNCLASSIFIED_<date>.md`.
- **SC-e-56:** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` and its tests (PLACEMENT OPEN).
- **SC-e-57:** `infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py`; `infra/aws/lambda/v2_portal/_shared/tests/test_rivalfunds_classification.py`;
  `infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py` only if the producer itself writes the field.
- Every cell may append its own rows to `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`.

## Dependency edges

- `SC-e-41`, `SC-e-42`, `SC-e-43`, `SC-e-44` -> `SC-e-45`; and the issuer act "producer live" (SC-e-44 deployed, a run with a live
  canonical write count above 0) -> `SC-e-45` (ruling 2.10).
- `SC-e-47` -> `SC-e-48`.
- `SC-e-54` -> `SC-e-46`, `SC-e-49`, `SC-e-50`; issuer acts "sector writer applied" and "sector rows written" -> `SC-e-46`.
- Independent: `SC-e-51`, `SC-e-52`, `SC-e-53`, `SC-e-55`, `SC-e-56`, `SC-e-57`.

**Chains:** A {41, 42, 43, 44 -> 45}; B {47 -> 48}; C {54 -> 46, 49, 50}; singles 51, 52, 53, 55, 56, 57. M = 9.
First wave (no unmet edge): 41, 42, 43, 44, 47, 51, 52, 53, 54, 55, 57 (11 cells; 56 waits on its placement).
Recommended fan-out: 8 of 9 chains, cap 8 (56 excluded until placed).

## Outcome coverage (denominator 17)

| outcome | this round | carried or deferred |
|---|---|---|
| FWD-1 | -- | the BD thread waits on FWD-5's order (2.10) |
| FWD-2 | `SC-e-42`, `SC-e-55` | -- |
| FWD-3 | -- | done (round 8, option b) |
| FWD-4 | -- | round 8's census instrument stands |
| FWD-5 | `SC-e-41`..`SC-e-45` | the delete is Andrew's (FWD-5 DONE WHEN) |
| FWD-6 | `SC-e-46` | -- |
| FWD-7 | `SC-e-44` | -- |
| FWD-8 | -- | deferred: rides FWD-11's path |
| FWD-9 | -- | owned by MDPF_SECHIST (v0.12); W14-S5's 7 rival stocks (section 3) are a row carried to that project's cut |
| FWD-10 | `SC-e-44`, `SC-e-57` | -- |
| FWD-11 | `SC-e-49`, `SC-e-54` | the first model run is an issuer act |
| FWD-12 | `SC-e-46`, `SC-e-54`, `SC-e-57` | -- |
| FWD-13 | `SC-e-55`, `SC-e-56` | -- |
| FWD-14 | `SC-e-47`, `SC-e-48` | the write is an issuer act |
| FWD-15 | `SC-e-49` | -- |
| FWD-16 | `SC-e-51`, `SC-e-52`, `SC-e-53` | -- |
| FWD-17 | `SC-e-50`, `SC-e-54` | the reclassification write is an issuer act |

## Issuer acts this round creates or inherits (not cells)

- Inherited: SC-e-28's apply (a laptop cloud-operations seat via `safe-apply`, its half `NEVER_WIDEN_HALF_REQUEST_SECCLASS_SECTOR_ROWS_20261007.md`
  both halves UNSIGNED) and the sector-row write; the AI first run and the old-list reclassification write (e31/e32 half, UNSIGNED);
  COO condition 3 of the SC-e-21 half (the next E_18 run's log).
- Created: SC-e-44's deploy and its "producer live" run; SC-e-42/45/55's uploads; the clean-name write (SC-e-48); the FWD-15 model run
  (SC-e-49); a served-bytes held read by a laptop seat (2.9) wherever a cell's held set is `inferred`; the C-ROLE-REQUEST to the laptop
  for a read-only firm-bucket grant (2.9). Each upload, write, apply or model call has its own never-widen pair and ledger entry.

## Carried rows (section 4 item 8; none is a cell)

S11, S14, S15, S20, S22, S29/S36 reads, W13-S1/S3/S5, W15-S1/S2, W16-S3/S4, W20-S1, S32, W22-S1, W23-S5, W24-S3/S4/S6, W25-S3/S4,
W26-S3/S7, S49 (every worker face forbids every install and download). S30 goes to the laptop CTO for placement (section 3).
Riding a cell: W24-S6 (the seed-wins dicts) rides SC-e-54's writer edit if the cell's worker finds it in the same function; otherwise carried.

## Battery

- `comp-schedule --owner 2.0.0_SA_COO~M1 --budget 90` (2026-10-07 ~11:3xZ): "no armed gates found" for this serial; the eight open
  deploy-ledger entries listed in R8 are still owned by `2.0.0_SA_COO~M` (the closed laptop lane) in their files -- a re-owning act for
  this seat, not a cell.
- `comp-iam`: not run at this cut; SC-e-42, SC-e-44, SC-e-55 and SC-e-57 each run `comp-iam` on the role their code runs under.
- `comp-adversary`: not run at this cut.

## Not read at this cut

Which test files exist for `d06_firm_mix_summary.py` and the portal screens; whether the FWD-10 producer or `rivalfunds_classification`
writes the GICS sector into `sub_asset_class` (SC-e-57's worker names it); the custody feeds' name columns per firm (SC-e-48); whether
any BD-tree reader beyond SC-e-38's set NEEDS the old list (SC-e-41 measures it and an amendment adds a switch cell if so).
