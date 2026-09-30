# MDPF_SECCLASS -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~M` at the L5 cut (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`).
Lane `ANY`.
**Id grammar:** a worker's row is `MDPF_SECCLASS-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that
coordinate); a seat's row is `MDPF_SECCLASS-S<k>`; the CVO's adjudication rows live in `../adjudications/` as
`MDPF_SECCLASS-C-S<k>`. **Append-only during the round.** Never edit an existing row.

```json
{
  "id": "MDPF_SECCLASS-S1",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~M",
  "surfaced_at": "2026-09-29T21:55:00Z",
  "one_line": "etf-classifications has a third writer the PRD's C-WRITER does not name: infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py batch.put_item()s rows (AAPL's live row reads updated_by 'seed-etf-constituents (1.0.0_SA_CTO~Z, Andrew-direct 2026-08-25)', sub_asset_class = the GICS sector), beside the seed path seed-etf-classifications.py.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~M (round 1 cell SC-k-2 carries instrument_kind onto both seed scripts' rows and reports whether the constituents seeder is part of the seed path; the C-WRITER wording is 1.0.0_SA_CTO's)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws dynamodb get-item etf-classifications ticker=AAPL (2026-09-29 20:3xZ): updated_by 'seed-etf-constituents (1.0.0_SA_CTO~Z, Andrew-direct 2026-08-25)', asset_class equity, sub_asset_class Information Technology, no classified_by",
      "infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py:48 TABLE = 'etf-classifications'; :199 updated_by; :223 batch.put_item",
      "PRD C-WRITER (org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md:128): exactly two writers, seed = the seed path, scheduled = FWD-7; C-TABLE (:126) names the seed path as yang_pipeline/seed-etf-classifications.py only"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Exactly two writers of etf-classifications rows: the seed path (seed-etf-classifications.py) and FWD-7's scheduled classification.",
  "world_is": "A second seed script, seed-etf-constituents.py, writes ETF-constituent stock rows (e.g. AAPL) with its own updated_by and no classified_by. Whether it is part of 'the seed path' is unstated.",
  "notes": "Not a bd-securities path: it reads ETF constituents, not the fork. It matters to FWD-3 (one edit place) and to C-WRITER's two-value classified_by. Andrew-direct 2026-09-29 ~21:4xZ to 2.0.0_SA_COO~M ('the canonical table should not be overwritten by anything in bd-securities') is carried into every round-1 face; this row does not depend on it."
}
```

```json
[
{
  "id": "MDPF_SECCLASS-W3-S1",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~3",
  "surfaced_at": "2026-09-29T22:15Z",
  "one_line": "SC1-t1-AC2's own check (PLACED) and SC-k-1's check (PINNED) both assume GLD, PHYS and VXX already carry canonical etf-classifications rows; PHYS does not, so AC2 fails on real data as written.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~M (SC-k-1's backfill PINS PHYS as already-present and so will never write it; the round needs an owner to seed PHYS's row, or the PLACED/PINNED checks amended, before AC2 can pass on live data)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws dynamodb get-item etf-classifications ticker=PHYS, region us-east-1, 2026-09-29 ~22:0xZ: no Item; a full ProjectionExpression=ticker scan of all 344 rows confirms PHYS absent while GLD and VXX are present",
      "aws dynamodb get-item bd-securities ticker=PHYS, 2026-09-29: Item present, asset_class=alternatives, sub_asset_class=Gold, classified_by=gpt-4o-mini, last_updated 2026-04-09 -- PHYS was AI-classified into the OLD table and never carried into the canonical one",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_CHECKS/r1_bd_resolution_census.py:16 PLACED={'GLD':('commodities','Metals'),'PHYS':('commodities','Metals'),'VXX':('structured','Hedge')}; r1_backfill_census.py:8,19 'GLD, PHYS and VXX already have rows' / PINNED={'GLD','PHYS','VXX'}",
      "s3://opal-data-bd/gold/holdings_lots/2026-09-25.parquet (the day E_18 reads): 2 open lots ticker=PHYS, asset_name='SPROTT ASSET MANAGEMENT LP PHYSICAL GOLD TR' -- PHYS is a real, currently-held BD security, not a hypothetical",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BD_RESOLUTION_CENSUS_20260929.json@(this commit): PHYS move before={'asset_class':'alternatives','sub_asset':'Gold'} after={'asset_class':'','sub_asset':''}; python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_CHECKS/r1_bd_resolution_census.py -> 'NOT-CENSUSED: PHYS lands {...}, placed (commodities, Metals)' rc=1"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "SC1-t1-AC2's check (r1_bd_resolution_census.py PLACED) and SC-k-1's check (r1_backfill_census.py PINNED) both assert GLD, PHYS and VXX already carry canonical etf-classifications rows.",
  "world_is": "etf-classifications (344 rows, live scan 2026-09-29) carries GLD and VXX but not PHYS; PHYS exists only in the legacy bd-securities table. The library built for SC-t-1 reads the canonical table faithfully (no fold, no guess) and correctly reports PHYS UNCLASSIFIED, which the AC2 check refuses because it was written assuming PHYS already resolves.",
  "notes": "Not a defect in the library under test: classify('PHYS') answering '' is exactly SC-t-1's spec (a holding the table lacks is unclassified, by name, never a guess). The mismatch is between the two checks' shared assumption and the table's measured contents. AC2 is recorded FAIL against this order's own invocation per the refusal clause -- the census JSON itself is honest and complete."
},
{
  "id": "MDPF_SECCLASS-W3-S2",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~3",
  "surfaced_at": "2026-09-29T22:15Z",
  "one_line": "Removing layers 2-4 (SC-t-1's build item 2) drops the private _ticker_map/_name_map attributes that data/black_diamond/scripts/silver/build_bd_assets_dim.py:156 reads directly for a diagnostic print, so that reader now raises AttributeError on its very next real run.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~M (build_bd_assets_dim.py is explicitly a read-only reader of this cell and moves in SC-t-2/SC-t-3 of this worker's own queue -- the fix belongs there, before this LOCAL-only build is ever deployed)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/black_diamond/scripts/silver/build_bd_assets_dim.py:156 (HEAD @c1e9b60e63): print(f'  {len(clf._ticker_map):,} tickers, {len(clf._name_map):,} name aliases loaded', flush=True) -- the only external reference to these two private attributes in the estate (comp-find '_ticker_map|_name_map' data/black_diamond, SURFACED=17, single external hit)",
      "data/black_diamond/scripts/gold/lib/etf_classifier.py (this commit): the rewritten ETFClassifier wraps the shared etf-classifications client and carries no _ticker_map/_name_map attribute -- the task order's Build item 2 scopes the kept public API to instance/classify/get_sub_asset_class/resolve_ticker only, none of which is this private pair"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BOUNDS: 'Readers are read-only here... move in the next orders of your queue (SC-t-2, SC-t-3)', and Build item 2's kept-API list names only instance/classify/get_sub_asset_class/resolve_ticker.",
  "world_is": "build_bd_assets_dim.py's apply_blend() reads clf._ticker_map and clf._name_map directly (not through the kept public API) one line after instantiating the new classifier, so it raises immediately rather than degrading gracefully. No production impact today -- this order is LOCAL build + record only, no upload, no deploy -- but the next deploy of this file breaks that reader until SC-t-2/SC-t-3 lands.",
  "notes": "Not fixed here: build_bd_assets_dim.py is outside this order's <paths> write grant."
},
{
  "id": "MDPF_SECCLASS-W3-S3",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~3",
  "surfaced_at": "2026-09-30T02:30Z",
  "one_line": "D_04.client_portal_summary.py has a FOURTH classify site the cell's reader list did not name -- build_advisor_positions's _classify_ticker (:2766) -- whose positions[] items still lack the canonical class/sub-class/class_source fields SC-t-3 adds everywhere else in this file.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~M (a future round-1 enrichment can route build_advisor_positions through the same _classify_with_canonical helper this cell added, or the issuer can rule the frozen ADVI_49EXEC.md Section 4.5 wire contract out of scope entirely)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "The cell's own reader list names exactly three classify sites: D_03.classify_series (:116), D_04._classify near :1235, and C_06 generally -- build_advisor_positions's _classify_ticker (D_04.client_portal_summary.py:2766, pre-cell line number) is a distinct closure the cell text does not mention",
      "build_advisor_positions's docstring names a FROZEN wire contract (PRD ADVI_49EXEC.md Section 4.5, with explicit 'CTO redlines' on the exact field list): {ticker, security_name, asset_class, market_value, cost_basis, unrealized_gain, unrealized_gain_pct, pct_of_advisor_aum, account_count, lot_count, first_acquisition_date, last_acquisition_date, oldest_lot_holding_days} -- adding fields here is a different governance surface than the composition/summary/timeseries artifacts this cell's BOUNDS grants",
      "This worker's own new helper, D_04._classify_with_canonical (added this cell, near line 152), is reused by build_account_summaries (the named :1235 site) but NOT by build_advisor_positions, which still calls its own local _classify_ticker returning a single coarse string"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Build item 1: 'D_03, D_04 and C_06 carry each holding's canonical class and sub-class, plus a class_source' -- read at the FILE level, this covers every classify site in D_04.",
  "world_is": "platinum/advisors/{id}/positions.json's positions[] carry only the coarse asset_class (equity/fixed_income/alternatives/cash/other); GLD/PHYS/VXX (and every other moved ticker) show their new canonical class everywhere else this cell touches, but not on this one served artifact.",
  "notes": "Not fixed here: the cell's own reader enumeration stops at three named sites, and build_advisor_positions serves a separately-governed frozen wire contract (ADVI_49EXEC.md) this order's BOUNDS does not name. Referenced from this cell's own never-widen half (NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_20260929.md, Blast radius section 2) as a known gap."
}
]
```

```json
{
  "id": "MDPF_SECCLASS-W2-S1",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~2",
  "surfaced_at": "2026-09-30T00:05:00Z",
  "one_line": "The canonical seed source etf_classification.py has at least 2 other physical copies in the estate (yang_pipeline/portfolios/yang-generate-etf-returns/, partners/lambdas/opal-partners-data/) that carry no etf_classifications_dynamodb.py peer, so a live resolve() import in the canonical file would ImportError those Lambdas on their next sync -- wrote the pre-resolved literal industry value instead.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ls infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-generate-etf-returns/ and infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/ (2026-09-29): each carries its own etf_classification.py, neither carries etf_classifications_dynamodb.py",
      "python -c \"import etf_classifications_dynamodb as m; print(m.resolve('Consumer Staples Distribution'))\" -> ('Consumer Staples Distribution & Retail', 'inferred-from-truncation'), 2026-09-29, verifying the literal ETF_INDUSTRY['WMT'] value in etf_classification.py rather than hand-deriving it",
      "infra/aws/lambda/v2_portal/_shared/etf_classification.py (this cell's edit): the GICS INDUSTRY GROUP section comment records the exact invocation and states the no-live-import decision"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-SC-k2 step 1: industry is 'filled from Bloomberg's GICS industry group as an input and decoded through the one client's resolve() (etf_classifications_dynamodb.py:262)'.",
  "world_is": "etf_classification.py is a physically-copied module with no guaranteed etf_classifications_dynamodb.py peer at every copy site; a runtime import of resolve() from the canonical _shared/ file would be safe there but break the other copies whenever they are next synced from it. This cell computes the decoded value once, offline, and records the exact resolve() call and output in a comment instead of importing the function.",
  "notes": "Not a defect in this cell's own file (my <paths> grant is only _shared/etf_classification.py); flagged so a future fold of GICS decode logic into the seed source picks the same non-import path, or first fixes the copy-fragility (adds etf_classifications_dynamodb.py to every etf_classification.py deploy target) before adding a live dependency."
}
```

```json
{
  "id": "MDPF_SECCLASS-W2-S2",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~2",
  "surfaced_at": "2026-09-30T00:06:00Z",
  "one_line": "3 of the 167 tickers in seed-etf-constituents.py's served-artifact universe are not single-security stocks: SALXX/FXFXX are money-market mutual funds and CASH is a derived cash-residual line -- classified as 'fund' and absent respectively, not blanket 'single_security'.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python load_constituents() on the served platinum/etfs/positioning_data.json artifact (2026-09-29): SALXX={'name': 'State Street U.S. Government MMKT', 'asset_class': 'Fixed Income', ...}, FXFXX={'name': 'First American Treasury Obligations Fund', ...}, CASH={'name': 'Cash & Cash Equivalents', ...}; Counter of asset_class over all 167 = {'Equity': 164, 'Fixed Income': 3}",
      "infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py NAME_CORRECTIONS comment (pre-existing): 'MONEY-MARKET / CASH LINES. SALXX is Andrew's own string ... a money-market fund has none [maturity date]' -- the module's own text already distinguishes these from ordinary stocks",
      "this cell's seed-etf-constituents.py instrument_kind_for()/build_row(): SALXX/FXFXX -> 'fund', CASH/CASH&OTHER -> None (absent)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-SC-k2 step 2: 'The constituents seeder writes instrument_kind = single_security for its stock rows.'",
  "world_is": "Its universe (the served ETF holdings artifact) is not 100% stocks: 2 money-market mutual funds and 1 cash-residual line are mixed in among the 164 genuine single-security stocks, under the same 'Fixed Income' asset_class label the served data assigns cash too.",
  "notes": "Classified per the MECE domain instrument_kind already uses in etf_classification.py (fund / single_security / absent-for-cash), not the order's literal 'single_security for its stock rows' read as covering every row unconditionally -- test_seed_fields.py::test_constituent_money_market_funds_are_fund_not_single_security and ::test_constituent_cash_residual_has_no_instrument_kind cover both."
}
```

```json
{
  "id": "MDPF_SECCLASS-W2-S3",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~2",
  "surfaced_at": "2026-09-30T00:07:00Z",
  "one_line": "The census's 'kinds' map asserts instrument_kind for all 302 tickers both seed sources know (the full seed-source domain), but the ACTUAL seed-etf-constituents.py act (no --force-names) only writes instrument_kind to the 10 net-new constituent tickers this cycle -- the other 157 already-existing constituent rows keep their current state (no instrument_kind) until a later run touches them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python seed-etf-constituents.py --dry-run (2026-09-29 live table): 'PLAN: 10 create / 0 update / 157 preserve-existing' -- the 157 preserve-existing tickers receive no put_item call at all under the default (non --force-names) run this cell's never-widen half describes",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_SEED_FIELDS_CENSUS_20260929.json: kinds carries 302 entries (all 137 module tickers minus CASH_USD, plus all 167 constituent tickers minus CASH), independent of which of those rows this specific run would actually touch",
      "NEVER_WIDEN_HALF_REQUEST_SECCLASS_SEED_FIELDS_20260929.md 'The act', point 2: '--force-names is NOT part of this act (name stays preserved on the 157 already-existing constituent rows; only the 10 net-new tickers get a full row)'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-SC-k2 step 4: the census's kinds map is 'every seed row's kind', read together with step 2's 'the constituents seeder writes instrument_kind ... for its stock rows.'",
  "world_is": "The seed SOURCE (module + served artifact) asserts a kind for all 302 tickers; the seed PATH's actual write plan for this act covers only 10 of the 167 constituent tickers (the net-new ones), because the pre-existing preserve-by-default behavior (protecting a curated `name`) skips the whole row, not just `name`, for an already-existing ticker. A full backfill of instrument_kind onto the other 157 needs either --force-names (which would also rewrite name) or a future instrument_kind-only backfill mode -- neither is part of this cell's act.",
  "notes": "Not a defect in this cell's code: the census correctly distinguishes 'what the seed source knows' from 'what this run writes', and the half names the 10/157 split explicitly. Flagged so a future FWD-4 census or the CTO's round-2 addendum on folding the constituents seeder into the seed path also closes this instrument_kind backfill gap, not just the classified_by ownership question RULING 103050 already answers."
}
```

```json
{
  "id": "MDPF_SECCLASS-W1-S1",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~1",
  "surfaced_at": "2026-09-29T22:40:00Z",
  "one_line": "Cell SC-k-1's own task-order text asserts 'GLD, PHYS and VXX already have rows' in etf-classifications; a live get_item on PHYS at build time reads no row at all (GLD and VXX do).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws dynamodb get-item etf-classifications ticker=PHYS (boto3, 2026-09-29 ~22:3xZ): {} (no Item) -- ticker=GLD and ticker=VXX both return full Items the same read",
      "org/missions/D8/MDPF/MDPF_SECCLASS/task-orders/MDPF_SECCLASS.TO-SC-k1.scheduled-classification.md step 4: 'GLD, PHYS and VXX already have rows in the table'",
      "org/missions/D8/MDPF/MDPF_SECCLASS/task-orders/MDPF_SECCLASS.TO-SC-k2.seed-kind-and-industry.md step 1: 'Keep IB-mr-251's PHYS row exactly as it landed' -- names IB-mr-251 (a different project, IRPT_BCKEND) as PHYS's actual writer, not yet observed live"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "GLD, PHYS and VXX already carry rows in etf-classifications at the time cell SC-k-1 builds against it.",
  "world_is": "GLD and VXX carry rows; PHYS does not, as of this build. PHYS's row is apparently pending from a different workstream (IB-mr-251, IRPT_BCKEND), not yet landed live.",
  "notes": "No effect on this cell's own output: PHYS's only input here is bd-securities' alternatives/Gold, which is a fold against the canonical vocabulary (alternatives only carries Real Estate) regardless of whether PHYS already has a row, so PHYS lands in 'unresolved' either way (see R1_BACKFILL_CENSUS_20260929.json, bd firm unresolved list) and the r1_backfill_census.py PINNED check (GLD/PHYS/VXX never would-write) passes without relying on the stale premise. Flagged because a DIFFERENT cell's half (e.g. SC-k-2's, or any thread half computing a 'before' snapshot that assumes PHYS is already classified) could read a false state if IB-mr-251 has not landed by the time it runs."
}
```

```json
{
  "id": "MDPF_SECCLASS-S2",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~M",
  "surfaced_at": "2026-09-30T00:25:00Z",
  "one_line": "The FWD-7 backfill census (TO-SC-k1, drained @d0e5b687f3) covers cottonwood with ZERO held tickers ('no-ticker-keyed-source-live': opal-data-cot gold/positions_cube has no ticker column) and inflection from a 2026-08-07 holdings file, while the IR Holdings census (IB-mr-251) reads 1,324 cottonwood securities -- so the backfill as built cannot resolve cottonwood's tickers, and IRPT_BCKEND IB-mr-251's cottonwood refusals survive it.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~M (cottonwood and inflection each need their own firm-tree caller of the scheduled classification, C-FIRM; carried to the round-1 analysis as enrichment; IB-mr-251's release waits on it for cottonwood)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "R1_BACKFILL_CENSUS_20260929.json cottonwood: as_of 'no-ticker-keyed-source-live', held 0, source 'opal-data-cot:gold/positions_cube (no ticker column)'",
      "R1_BACKFILL_CENSUS_20260929.json inflection: as_of 2026-08-07, source opal-data-inf:gold/holdings/2026-08-07.parquet, held 285",
      "R25_ETF_CLASS_CENSUS_20260929.json (IRPT_BCKEND IB-mr-251): cottonwood=151/1324 securities, a ticker-bearing build (holdings_snapshot build_cot)",
      "every would-write row in the census (3,317 across bd/49financial/inflection) has input bd-securities; GICS and Schwab inputs resolved none; instrument_kind and industry absent on all of them"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-7: a security that newly appears in ANY firm's daily holdings gets its entry on a schedule; CTO 103036: backfill every held security.",
  "world_is": "The census reads held tickers for bd, 49financial and inflection (stale), none for cottonwood; every planned row comes from bd-securities input, so Andrew's open question on bd-securities values in new rows decides whether the backfill writes anything.",
  "notes": "Not a cell defect: TO-SC-k1 named 'each firm's own latest holdings source, where one exists'. The IR Holdings producer's per-firm symbol sets (a ticker-keyed read at all three firms) are the nearest held source for the enrichment caller."
}
```

```json
[
{
  "id": "MDPF_SECCLASS-W5-S1",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~5",
  "surfaced_at": "2026-09-30T03:15:00Z",
  "one_line": "TO-SC-e1's sanctioned C-WRITER change (seed-etf-constituents.py now sets classified_by='constituents' on every row it writes) makes round-1's own test_seed_fields.py::test_constituent_seeder_never_sets_classified_by fail; that test file encodes the now-superseded RULING 103050 text and sits outside this order's <paths> write grant.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~M (test_seed_fields.py is round-1's file, not in TO-SC-e1's write grant; its one assertion needs updating -- or removing as superseded -- in SC-e-2 or a later cell before a repo-wide test run is clean again)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND1_ANALYSIS_MDPF_SECCLASS_20260930.md@151c890591 section 1: 'The constituents seeder (seed-etf-classifications.py, my ruling 103050) now sets classified_by = constituents on every row it writes' -- the round-2 ruling this task order (MDPF_SECCLASS.TO-SC-e1) implements",
      "infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py (this commit): build_row() now returns 'classified_by': 'constituents' on every row",
      "infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py:137-140 (HEAD, pre-existing, round-1 SC-k-2 file): def test_constituent_seeder_never_sets_classified_by(...): assert 'classified_by' not in row -- this is the literal, now-contradicted assertion",
      "python -m pytest infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py -q -p no:cacheprovider (this build, after the SC-e-1 edit): '1 failed, 18 passed' -- AssertionError: assert 'classified_by' not in {..., 'classified_by': 'constituents', ...}"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "test_seed_fields.py (round-1 SC-k-2, RULING 103050): 'the constituents seeder never sets classified_by and refuses to overwrite a row that already carries one.'",
  "world_is": "The round-2 C-WRITER ruling supersedes RULING 103050's first half: the seeder now DOES set classified_by='constituents' (the refuse-to-overwrite half is unchanged and still passes). TO-SC-e1's <paths> grant does not include test_seed_fields.py, so this worker cannot update the stale assertion itself.",
  "notes": "Not fixed here: test_seed_fields.py is outside this order's write grant (refusal clause). TO-SC-e1's own acceptance criterion (SC2-e1-AC1) runs only test_classified_by_v2.py, which is unaffected and passes 13/13. This row exists so the repo-wide suite's one known regression is tracked and closed by whichever cell/owner next holds test_seed_fields.py."
},
{
  "id": "MDPF_SECCLASS-W5-S2",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~5",
  "surfaced_at": "2026-09-30T03:40:00Z",
  "one_line": "Amendment 1's new etf-classifications field identifier_namespace {TICKER, CUSIP} shares its exact name with an existing, wider identifier_namespace field on IRPT_BCKEND's own wire contract (portal/src/pages/InvestorReporting/contracts/wire/AnalysisRequest.ts: TICKER|CUSIP|ISIN|CASH|MODEL|UNMATCHED) -- same token, disjoint domain, no write-path collision.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/MDPF/MDPF_SECCLASS/task-orders/MDPF_SECCLASS.TO-SC-e1.contract-and-legacy-label.md amendment 1 (CTO RULING 103140, E9), landed @1302fa149e: 'the contract ALSO gains the field identifier_namespace with values {TICKER, CUSIP}'",
      "comp-find 'identifier_namespace' portal/src --all (2026-09-30 ~03:3xZ): 8 hits, SURFACED=3 CONFIG=2 TEST=3, all in IRPT_BCKEND's own tree -- portal/src/pages/InvestorReporting/contracts/wire/AnalysisRequest.ts:35: \"readonly identifier_namespace: 'TICKER' | 'CUSIP' | 'ISIN' | 'CASH' | 'MODEL' | 'UNMATCHED'\"; adapt.ts:859 and :1544 read/build it from a normalized_holdings wire shape",
      "comp-find 'identifier_namespace' infra/aws/lambda/v2_portal --all and data --all (same build): 0 hits each -- no etf-classifications code path references the token yet (this cell only adds it to the contract JSON and one test)",
      "org/standards/MDPF_SECCLASS_CONTRACT.json (this commit): identifier_namespace.values = [TICKER, CUSIP], a strict subset of IRPT's six -- the two fields are never read or written by the same code path today"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CLAUDE.md Rule 24: a value-enum proposal carries a word-boundary token census as part of its four-postulate record, so a collision is surfaced rather than silently accepted.",
  "world_is": "The token identifier_namespace already exists in the estate on a DIFFERENT schema (IRPT_BCKEND's wire contract) with a wider value set; etf-classifications' new field of the same name is a narrower, unrelated enum on a different table. No consumer reads both today, so there is no live collision, only a shared name a future reader could confuse.",
  "notes": "Not fixed here: amendment 1 named this exact field name and value set (CTO RULING 103140), and this cell's <paths> grant does not include the IRPT wire contract. Flagged so a future fold or shared-vocabulary decision between the two identifier_namespace fields is deliberate, not accidental."
},
{
  "id": "MDPF_SECCLASS-W5-S3",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~5",
  "surfaced_at": "2026-09-30T04:05:00Z",
  "one_line": "A mid-task coordinator message claimed 'CLOUD now carries a cross-device union of seed-etf-constituents.py' (site Z's --universe amgt-library path) and asked this worker to build on it and add classified_by/instrument_kind handling to that path; measured, the local CLOUD branch in this worktree does NOT contain that commit -- it exists only on origin/CLOUD, 1,245 commits ahead of local CLOUD, which this worktree has not fetched/merged. This worker did not perform that merge or edit the amgt-library path: doing so is a repo-wide branch integration far outside TO-SC-e1's LOCAL-build-and-record BOUNDS and <paths> grant, not a same-file edit.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~M (the cross-fabric merge of origin/CLOUD into this device's local CLOUD -- or a targeted cherry-pick of 8757ce95eb -- is a branch-integration act for the issuer/integrator, not a single worker's LOCAL-build task order; until it lands locally, this worker's seed-etf-constituents.py edit cannot see or extend the amgt-library path)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git merge --no-edit CLOUD (this build, twice): both fast-forwards, neither touches infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py",
      "git log --all --oneline -- infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py: 8757ce95eb 'build(AMGT_RESAPP round 48, AMGT-ww-3, 0.9.0_WK_AMGT_RESAPP~172): the etf-classifications writer gains --universe amgt-library' exists in the repo's object store but is not an ancestor of local CLOUD",
      "git merge-base --is-ancestor 8757ce95eb CLOUD -> NOT-ANCESTOR-OF-CLOUD; git branch --all --contains 8757ce95eb -> remotes/origin/CLOUD, remotes/origin/HEAD only",
      "git rev-parse CLOUD origin/CLOUD: 8b7d5738af vs fd3b3b7bf2; git log CLOUD..origin/CLOUD --oneline | count = 1245; git log origin/CLOUD..CLOUD --oneline | count = 176 -- large, two-way divergence, not a simple fast-forward gap",
      "comp-find 'test_positioning_universe_plan_unchanged' --all (this build): measured zero across 45,686 scanned files -- the named test does not exist anywhere reachable from local CLOUD either"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Coordinator message (2026-09-30, this session): 'CLOUD now carries a cross-device union of ...seed-etf-constituents.py ... the union merge stands.'",
  "world_is": "This worktree's local CLOUD branch (the one named 'CLOUD' that 'git merge CLOUD' resolves) does not carry that commit; it is reachable only via origin/CLOUD, itself 1,245 commits ahead of and 176 commits behind local CLOUD. No fetch/merge of that scale was performed.",
  "notes": "Not executed here: TO-SC-e1's BOUNDS name LOCAL build + record and a specific <paths> write grant; reconciling a 1,245-commit cross-fabric divergence is a branch-integration act, not this cell's. This worker's own contract and test edits (identifier_namespace, classified_by='constituents') stand on the verified, in-branch amendment @1302fa149e and are unaffected by this row."
},
{
  "id": "MDPF_SECCLASS-W5-S4",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~5",
  "surfaced_at": "2026-09-30T04:30:00Z",
  "one_line": "MDPF_SECCLASS-W5-S1's stale assertion is fixed under this order (TO-SC-e2, amendment 1, row MDPF_SECCLASS-W5-S1): test_seed_fields.py::test_constituent_seeder_never_sets_classified_by is replaced by test_constituent_seeder_sets_constituents_label_and_refuses_seed_or_scheduled, which asserts the constituents label on a written row and the refusal of a seed or scheduled row; the file's own suite is green again (19 passed).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py (this commit): test_constituent_seeder_never_sets_classified_by removed, replaced by test_constituent_seeder_sets_constituents_label_and_refuses_seed_or_scheduled, asserting row['classified_by'] == 'constituents' and RowProtected on a seed-labelled and a scheduled-labelled ticker alike",
      "python -m pytest infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py -q -p no:cacheprovider (this build, before the edit): '1 failed, 18 passed' (the W5-S1 regression); after the edit: '19 passed in 0.23s'",
      "MDPF_SECCLASS.TO-SC-e2.instrument-kind-population.md amendment 1 (row MDPF_SECCLASS-W5-S1): 'Under the CTO's four-label ruling and SC-e-1, the constituents seeder sets classified_by = \"constituents\". Update that one test to assert the constituents label on a written row and the refusal of a seed or scheduled row. Loosen nothing else.' -- this row's edit is that exact, sole change; no other assertion in the file was touched."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "MDPF_SECCLASS-W5-S1: 'disarm_owner: 2.0.0_SA_COO~M ... its one assertion needs updating -- or removing as superseded -- in SC-e-2 or a later cell before a repo-wide test run is clean again.'",
  "world_is": "This IS that cell (TO-SC-e2), and its own amendment 1 directs exactly this fix (row MDPF_SECCLASS-W5-S1 named verbatim in the order). The disarm is performed here, by the worker the amendment addressed, not by 2.0.0_SA_COO~M directly executing a keystroke -- the issuing seat's own task order is the disarm act's authorization. This row does not itself flip W5-S1's hazard_standing (append-only; a worker does not edit or adjudicate an existing row) -- it records that the named condition is now met, for the issuer/CVO to close at L8/L9.",
  "notes": "Loosened nothing else in test_seed_fields.py, per the order's refusal clause; the other 18 pre-existing tests in the file are unchanged and still pass."
}
]
```
