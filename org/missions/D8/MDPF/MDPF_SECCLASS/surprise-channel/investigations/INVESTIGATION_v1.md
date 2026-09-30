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
{
  "id": "MDPF_SECCLASS-S3",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~M",
  "surfaced_at": "2026-09-30T05:20:00Z",
  "one_line": "The issuer's drain of the MDPF_SECCLASS thread (@ae7aa281b0, SC-t-1) moved data/black_diamond/scripts/gold/lib/etf_classifier.py onto etf-classifications and removed its private _ticker_map/_name_map, which IRPT_BCKEND's Holdings producer (holdings_snapshot.py canonical_classifier/_classifier_basis) reads -- CLOUD's investor_reporting suite now reads 30 failed / 16 errors, and a Holdings package re-mint from CLOUD would fail.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~M (IRPT_BCKEND IB-mr-291: Holdings moves to canonical-first with a declared bd-securities fallback module of its own and stops importing the BD library)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "r27_suite_whole.py data/assets/scripts/gold/investor_reporting/tests at CLOUD @874ab56b33: SUITE-BROKEN rc=1 (30 failed, 268 passed, 16 errors); at CLOUD @6c0317e55c before the thread drain it read SUITE-WHOLE 314 passed",
      "holdings_snapshot.py:828-919 reads clf._ticker_map / clf._name_map of the BD library; data/black_diamond/scripts/gold/lib/etf_classifier.py at CLOUD no longer defines them (SC-t-1, drained @ae7aa281b0)",
      "served Holdings are unaffected: the standalone packages were minted 2026-09-29 16:21Z from the pre-thread library (IB-mr-222 Part 1); no Holdings re-mint has run since"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "A cell's drain keeps every other suite whole (the issuer runs the drain's hygiene).",
  "world_is": "The thread's drain re-ran only the thread's own tests; the IRPT Holdings producer also imported the BD library, so the drain broke another project's suite on CLOUD unnoticed until 05:2xZ.",
  "notes": "The issuer's miss: the drain-time hygiene did not include suites that import a changed shared module. The narrowed release cell IB-mr-291 removes the cross-project import."
}
```

```json
{
  "id": "MDPF_SECCLASS-W6-S1",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~6",
  "surfaced_at": "2026-09-30T03:40:00Z",
  "one_line": "BD's own round-1 E_18 caller (data/black_diamond/scripts/gold/E_18.detect_new_securities.py) computes _REPO_ROOT via Path(__file__).resolve().parents[3], one hop short of repo root for a 4-deep nesting (gold/scripts/black_diamond/data) -- its own comment says '4 levels up' but the index used is 3, not 4 -- so _SHARED resolves to <repo>/data/infra/aws/lambda/v2_portal/_shared, which does not exist, and the deferred `from etf_classification_scheduled import (...)` inside detect_new_securities() raises ModuleNotFoundError whenever this file is invoked from the real repo layout (not just under test).",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~M (a one-line fix in BD's own file, parents[3] -> parents[4]; outside this cell's <paths> write grant, which names only COT's own E_18.detect_new_securities.py)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python: Path('data/black_diamond/scripts/gold/E_18.detect_new_securities.py').resolve().parents[3] == '<repo>/data'; parents[4] == '<repo>' (measured 2026-09-30 in this worktree)",
      "(root/'infra'/'aws'/'lambda'/'v2_portal'/'_shared').is_dir() is False via parents[3], True via parents[4] -- the same check performed against this cell's own (now-fixed) copy of the file, data/cot/scripts/gold/E_18.detect_new_securities.py, before its correction",
      "data/black_diamond/scripts/gold/E_18.detect_new_securities.py:47-52 (HEAD): comment 'four levels up (gold -> scripts -> black_diamond -> data -> repo root)', code 'Path(__file__).resolve().parents[3]' -- comment names 4 hops, index used is 3",
      "No existing test imports and calls BD's E_18.detect_new_securities() end-to-end (infra/aws/lambda/v2_portal/_shared/tests/test_etf_classification_scheduled.py tests the shared module directly, never the BD caller file), so this path was never exercised by SC1-k1-AC1"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "SC1-k1's Build item 2: BD's E_18 'feeds its new tickers to the module instead of writing stubs to bd-securities' on the BD gold-layer's existing schedule -- FWD-7's first live scheduled caller.",
  "world_is": "Run from the real repo layout (not a test harness that pre-inserts the _shared directory onto sys.path some other way), BD's detect_new_securities(upload=True) raises ModuleNotFoundError at the deferred import and never reaches plan_rows/scheduled_write; the daily gold-layer invocation is wrapped '|| true' (per this file's own usage comment), so the failure is silent and FWD-7's BD backfill/schedule has not actually been running live since SC1-k1 landed.",
  "notes": "Found while wiring this cell's own analogous COT caller (SC-e-4) with the identical pattern copied from BD's file; caught only because this cell's own copy failed loudly under its own new test (test_e18_scheduled_caller.py) before the index was corrected to parents[4] here. Not fixed in BD's file: data/black_diamond/scripts/gold/E_18.detect_new_securities.py is outside this order's <paths> write grant."
}
```

```json
{
  "id": "MDPF_SECCLASS-W6-S2",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~6",
  "surfaced_at": "2026-09-30T04:20:00Z",
  "one_line": "SC-e-7's Build step 2 names infra/aws/terraform/bd-pipeline/iam.tf as the file carrying the E_18 principal's bd-securities PutItem to remove, but that grant does not live there -- it is infra/aws/terraform/shared-infra/main.tf's aws_iam_policy.bd_securities_access (unconditional PutItem/UpdateItem/BatchWriteItem/Scan/GetItem on BOTH bd-securities and etf-classifications), attached to bd-exporter-ec2-role AND partners-lambda-role, a file outside this cell's <paths> write grant.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~M (a follow-on task order scoped to infra/aws/terraform/shared-infra/main.tf must edit aws_iam_policy.bd_securities_access -- drop bd-securities from its Action/Resource pair and, per this row's grounding, note that DynamoDB IAM condition keys cannot express attribute_not_exists -- and must give its own half, since the same policy is also attached to partners-lambda-role, an unrelated BD lambda)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "comp-find/Grep 'PutItem|dynamodb:' across infra/aws/terraform/bd-pipeline/iam.tf (2026-09-30, this worktree HEAD before this cell's edit): the only dynamodb Action present is dynamodb:Scan on bd-securities (Sid AdviChainBdSecuritiesScan, a07/etf_classifier control-import read, unrelated to E_18) -- zero PutItem grants of any kind in this file",
      "infra/aws/terraform/shared-infra/main.tf:395-421 (this worktree HEAD): resource aws_iam_policy.bd_securities_access grants ['dynamodb:Scan','dynamodb:GetItem','dynamodb:PutItem','dynamodb:UpdateItem','dynamodb:BatchWriteItem'] on [aws_dynamodb_table.bd_securities.arn, 'arn:aws:dynamodb:us-east-1:313476888478:table/etf-classifications'], no Condition block; attached via aws_iam_role_policy_attachment.ec2_bd_securities (role='bd-exporter-ec2-role') and .lambda_bd_securities (role='partners-lambda-role')",
      "infra/aws/terraform/bd-pipeline/iam.tf:340-358 (aws_iam_role.bd_exporter, name='bd-exporter-ec2-role'): the exact role name shared-infra/main.tf's ec2_bd_securities attachment names -- confirming the LIVE bd-securities PutItem for BD's E_18 production principal is carried by the shared-infra policy, not by anything in bd-pipeline/iam.tf",
      "infra/aws/terraform/partners-api/iam.tf:9-33: aws_iam_role.partners_lambda (name='partners-lambda-role') is a separate BD partners-API lambda, not an E_18 caller -- the shared policy's second attachment is to an unrelated consumer, so editing it in place has a second blast-radius surface"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-SC-e7 Build step 2, verbatim: 'In infra/aws/terraform/bd-pipeline/iam.tf, add PutItem on etf-classifications ... Remove the bd-securities PutItem.'",
  "world_is": "bd-pipeline/iam.tf carries no bd-securities PutItem to remove; the actual live, unconditional PutItem (plus UpdateItem/BatchWriteItem/Scan/GetItem) on bd-securities for the exact same production principal (bd-exporter-ec2-role) is granted by a DIFFERENT file, infra/aws/terraform/shared-infra/main.tf, which this order's <paths> does not include. This cell's evidence JSON (R2_E18_IAM_20260930.json putitem_bd_securities=false) is accurate for bd-pipeline/iam.tf alone and is NOT a true statement of the principal's overall live grants.",
  "notes": "This cell still adds a genuine least-privilege PutItem-on-etf-classifications grant to bd-pipeline/iam.tf (aws_iam_role_policy.bd_exporter_e18_etf_classifications_put) per the letter of step 2's first half, and documents this gap inline in that file's comment plus in the cell's NEVER_WIDEN half (NEVER_WIDEN_HALF_REQUEST_SECCLASS_E18_IAM_20260930.md, SURPRISE / gap section) so the issuer does not sign off 'bd-securities PutItem removed' on the strength of this commit alone."
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
  "id": "MDPF_SECCLASS-W8-S1",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~8",
  "surfaced_at": "2026-09-30T07:10:00Z",
  "one_line": "kimi-k3 spends a large, variable HIDDEN reasoning-token budget before emitting the visible JSON content; a naive max_tokens (e.g. 300, comparable to a short structured-JSON call elsewhere in the estate) makes EVERY call finish_reason=length with ZERO content tokens, which this module's own refusal rule turns into a legitimate-looking 'asset_class null, reason KIMI_LENGTH_STARVED' result -- a systematic starvation would have silently produced a 100%-refused census that still passes SC4-e10-AC2's own shape checks (a reason is present on every null row).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Live probe 2026-09-30 ~07:0xZ, etf_classification_model.classify_one('JPMORGAN INCOME ETF', None, vocab, send=default_send, api_key=<live secret>) at max_tokens=300: result {'asset_class': None, 'confidence': None, 'reason': 'refused: KIMI_LENGTH_STARVED'}",
      "Same input, max_tokens=4000: real Chat Completions body returned finish_reason='stop', usage.completion_tokens_details.reasoning_tokens=391, message.content a full parseable JSON classification with confidence 0.8",
      "estate_report_runner.py's own history comment (this file, ~line 66-98) already documents an unrelated instance of the identical class of mistake for a different call (a 120s timeout inherited from a captcha-solve workload applied to a richer prompt, causing KIMI_TIMEOUT) -- this row is the same failure MODE (inheriting a budget/ceiling tuned for a different-shaped call) recurring on a THIRD dimension (max_tokens, for a reasoning-heavy model) that estate_report_runner's own call_kimi_sub/KIMI_BUDGETS pattern does not surface as a generic warning"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-SC-e10 Build step 1: 'Reuse the estate's Chat Completions JSON pattern: call_kimi_sub ... and the bounded client resolution_kimi.py (model kimi-k3). Do not add a dependency.'",
  "world_is": "Reusing the JSON REQUEST/RESPONSE SHAPE from those two references is safe and was done; reusing either reference's own numeric max_tokens BUDGET value (call_kimi_sub's per-kind KIMI_BUDGETS, or resolution_kimi.py's BUDGETS of 16000/32000 for a check/swap call) is a separate decision this order does not make for this NEW call shape, and the naive choice (a small budget appropriate to a short structured reply) fails 100% of calls silently rather than loudly, because a starved call still produces a spec-shaped null-with-reason result.",
  "notes": "Not a defect in either reused reference -- call_kimi_sub's KIMI_BUDGETS are correctly sized for THEIR OWN call kinds, and this module never imported or altered them. Fixed here by measuring live rather than guessing (CLAUDE.md Rule 4 build ladder does not reach 'guess a constant'); the module's own comment above MAX_TOKENS records the exact probe so a future reader does not have to re-derive it."
},
{
  "id": "MDPF_SECCLASS-W8-S2",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~8",
  "surfaced_at": "2026-09-30T07:15:00Z",
  "one_line": "This worker's Grep/Glob tool calls default to the base ajb_workspace checkout (branch CLOUD) rather than this worker's own worktree (wk-MDPF_SECCLASS-8) unless a worktree-scoped path is explicitly passed -- measured: a Grep for a filename with no explicit path surfaced infra/aws/lambda/v2_portal/_shared/tests/test_etf_classification_cusip.py, a file that does not exist in this worktree at all (ls of the real directory: 5 files, no such name).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Grep (no path argument) surfaced infra\\aws\\lambda\\v2_portal\\_shared\\tests\\test_etf_classification_cusip.py among 96 hits for 'classified_by', 2026-09-30 ~07:0xZ",
      "ls C:/Users/AndrewBerman/Desktop/wk_mdpf_secclass_8/infra/aws/lambda/v2_portal/_shared/tests/ (this worktree, same timestamp): __pycache__, test_classified_by_v2.py, test_etf_classification_scheduled.py, test_model_classifier.py, test_seed_fields.py, test_set_instrument_kind.py -- no test_etf_classification_cusip.py",
      "git -C <worktree> log -1 --format=%H -> a29da4ac98..., branch wk-MDPF_SECCLASS-8 -- a different tip than the base checkout's CLOUD, confirming the two trees can genuinely diverge (this file is presumably a later SC-e-9 (slot ~4) commit on CLOUD not yet in this worker's branch)",
      "Every fact this cell's build actually relied on (org/standards/MDPF_SECCLASS_CONTRACT.json, the decomp cell text, R2_UNRESOLVED_REVIEW_20260930.json, infra/aws/terraform/estate-report/instance.tf's three ESTATE_KIMI_* lines, etf_classification_scheduled.py) was independently re-read via an explicit worktree-rooted path (Read tool absolute path, or a bash cd into the worktree) and confirmed identical/consistent -- this row records the TOOL-DEFAULT trap, not a defect in this cell's own deliverables"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The worker rules: 'You execute ONE task order at a time in your own git worktree' and '<paths> IS your write grant' -- implicitly, everything this worker reads to build against should be read FROM that worktree.",
  "world_is": "The Grep/Glob tools' default search root is the base ajb_workspace directory, not the calling worker's own worktree, so an un-pathed search can surface a file (or a version of a file) that does not exist on the worker's own branch -- a silent cross-tree read that looks identical to a same-tree one in the tool's own output.",
  "notes": "No effect on this cell's own artifacts (verified above); flagged because a future worker relying on an un-pathed Grep/Glob result to WRITE code (rather than merely to orient) could silently build against the wrong tree's shape. Not fixed here: the tool's default search root is outside this order's <paths> write grant and outside any repo file this worker could edit."
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

```json
{
  "id": "MDPF_SECCLASS-W4-S1",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~4",
  "surfaced_at": "2026-09-30T00:45:00Z",
  "one_line": "Round 1's resolution-stage (library) generator was never committed (correctly, per the uncommitted-.scratch/ rule), so round 2 cannot reproduce R1's exact 3,992-ticker holdings population byte-for-byte; round 2's re-census used its own defensible population (2,220 distinct held tickers via the same production ghost+AP-gate+open filters D_03 applies) rather than R1's unrecoverable one, so a raw 3,992-vs-2,220 'rows' comparison across the two census files is NOT a like-for-like population diff.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_CHECKS/ contains only the ACCEPTANCE checkers (r1_bd_resolution_census.py etc.), not the generator that built R1_BD_RESOLUTION_CENSUS_20260929.json -- confirmed by reading every file in that directory",
      "R1_BD_SILVER_CENSUS_20260929.json 'artifacts': ['C:/Users/AndrewBerman/Desktop/wk_mdpf_secclass_3/.scratch/bd_assets_dim_local_20260929.parquet'] -- a sibling worker's own worktree .scratch path, absent from this worktree and never committed (CLAUDE.md rule 16b: scratch is uncommitted build scaffolding)",
      "this cell's own generator (.scratch/gen_thread_census.py, uncommitted) measured 2,220 distinct held tickers via gold/holdings_lots/2026-09-25.parquet filtered open+ghost+AP-gated -- the SAME real filters D_03.composition_artifacts.py applies (imported unmodified from lib.exclusions), producing a real but independently-derived population, not R1's"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-SC-e3 step 1: 're-census the three thread stages ... on the latest BD day, reading the LIVE table' -- read together with the round-1 cell text, this implies the SAME population re-measured, not a newly-defined one.",
  "world_is": "The round-1 resolution-stage population's exact construction is not recoverable from committed artifacts; round 2 instead defined its own real, filter-faithful population and named the substitution in both the evidence file and the fresh half rather than silently reusing R1's row count.",
  "notes": "No effect on this cell's own acceptance (SC2-e3-AC1/AC2 check internal consistency, not population identity with round 1) or on the silver/gold stages, which each read their own live, real, currently-served population directly (bd_assets_dim.parquet, holdings_lots) rather than depending on R1's resolution-stage number. Flagged so a later round or the CVO's compile does not read the 3,992-vs-2,220 difference as an unexplained regression."
}
```

```json
{
  "id": "MDPF_SECCLASS-W4-S2",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~4",
  "surfaced_at": "2026-09-30T03:10:00Z",
  "one_line": "TO-SC-e9's own text asserts the contract is already v0.2.0 with C-FIELD identifier_namespace in {TICKER, CUSIP} (\"the contract v0.2.0 (SC-e-1, which rides the field) gives C-FIELD identifier_namespace...\"), but org/standards/MDPF_SECCLASS_CONTRACT.json at this worktree's HEAD is still v0.1.0, has no identifier_namespace field at all, and classified_by carries only [seed, scheduled] (not the four-value [seed, scheduled, constituents, legacy] the round-2 label check and standing rulings already assume) -- SC-e-1's own commit has not landed on this branch.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~M (SC-e-1 is a separate worker slot's cell in this same round; its commit lands via the normal drain, not this cell)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git log --oneline -- org/standards/MDPF_SECCLASS_CONTRACT.json on wk-MDPF_SECCLASS-4 @8aa241c9b1: one commit only, b9680cfe86 (the original L4 PRD, contract_version 0.1.0) -- no SC-e-1 amendment commit present",
      "python -c \"json.load(open('org/standards/MDPF_SECCLASS_CONTRACT.json'))['contract_version']\" -> '0.1.0'; ['fields'].keys() -> ['instrument_kind', 'classified_by']; ['classified_by']['values'] -> ['seed', 'scheduled']",
      "org/missions/D8/MDPF/MDPF_SECCLASS/task-orders/MDPF_SECCLASS.TO-SC-e1.contract-and-legacy-label.md:33 states the amendment as a fact of this round, and the round-2 evidence checker (R2_CHECKS/r2_evidence.py check_label) already REQUIRES classified_by_values sorted == ['constituents','legacy','scheduled','seed']"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The contract is v0.2.0 with identifier_namespace already a C-FIELD member, on this branch, right now.",
  "world_is": "The contract file this worktree can read is v0.1.0 with two fields (instrument_kind, classified_by) and classified_by's two-value enum -- SC-e-1's amendment is a sibling worker's cell in the same round, not yet merged into this worktree's history.",
  "notes": "No effect on this cell's own build: SC-e-9's bounds never grant a write to org/standards/MDPF_SECCLASS_CONTRACT.json, and the planner/tests/census/half all carry identifier_namespace as a plain data attribute on the planned rows themselves, independent of whether the contract JSON file has been amended yet. Named so the round-3 compile does not assume the contract file already reflects SC-e-1's text merely because a sibling task order describes it that way."
}
```

## MDPF_SECCLASS-S4 -- the additive updates would mint a row on a missing key

```json
{
  "id": "MDPF_SECCLASS-S4",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~M",
  "surfaced_at": "2026-09-30T07:27:00Z",
  "one_line": "label_row_if_unlabelled() and set_kind_if_absent() condition only on the ONE attribute being absent, so an update_item on a ticker with no row would MINT a skeleton row carrying only that attribute.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~M (round-N analysis: add attribute_exists(ticker) to both conditions)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/v2_portal/yang_pipeline/label-legacy-classified-by.py:80-97 and set-instrument-kind.py:84-104: ConditionExpression attribute_not_exists(<attr>) only; DynamoDB UpdateItem on a missing key creates the item when the condition holds",
      "the issuer's runs @7e171f5510 dropped any census ticker with no row BEFORE writing (FRESHNESS: 0 of 238 and 0 of 156 dropped), and the read-back shows 2,309 -> 2,309 rows",
      "both CLIs refuse a live run, so no path calls either function without a caller-side pre-read today"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The label and kind updates are additive on an EXISTING row and never create one.",
  "world_is": "The functions' own condition does not require the row to exist; only the caller's pre-read kept today's runs from minting rows.",
  "notes": "Inert because both CLIs are blocked and the issuer's driver guards the runs. A one-clause fix, carried to the analysis."
}
```

## MDPF_SECCLASS-W9-S1 -- the live CUSIP-keyed row count is 0, so the live dry-run line is trivially 0

```json
{
  "id": "MDPF_SECCLASS-W9-S1",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~9",
  "surfaced_at": "2026-09-30T15:00:00Z",
  "one_line": "The live etf-classifications table holds 0 CUSIP:-keyed rows today, so CUSIP-GUARD bd_delta_from_cusip=0 is true before the guard is even consulted; the discriminating line is CUSIP-GUARD-PLANNED.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R5_CHECKS/r5_cusip_guard_dryrun.py -> CUSIP-GUARD etf_rows=2309 cusip_rows=0 bd_rows=10929 bd_delta_from_cusip=0 ; CUSIP-GUARD-PLANNED planned=349 would_copy_to_bd=0 ; stderr control: unguarded planned copy would be 349"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The dry-run's bd_delta_from_cusip=0 reading shows the guard holds against live CUSIP rows.",
  "world_is": "cusip_rows=0 of etf_rows=2309 at 2026-09-30: SC-e-9's 349 rows are not yet written, so the live line has nothing to guard; only the planned line (349 planned, 0 would copy; unguarded control 349) exercises the guard.",
  "notes": "The half's standing condition (a fresh dry-run immediately before the act) is what makes the live line meaningful, and the act's own post-write re-run would then show cusip_rows=349 with bd_delta_from_cusip=0. No effect on this cell."
}
```

## MDPF_SECCLASS-W9-S2 -- seed_bd_securities.py's 'Seeded N items' count now excludes skipped CUSIP rows

```json
{
  "id": "MDPF_SECCLASS-W9-S2",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~9",
  "surfaced_at": "2026-09-30T15:00:00Z",
  "one_line": "The order says keep the seeder's output lines; the 'Seeded/Would seed <n> items' number is now len(items)-skipped_cusip so it states rows actually copied, and a new skipped_cusip=<n> line precedes it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/black_diamond/scripts/classification/seed_bd_securities.py lines 99-101 (diff on wk-MDPF_SECCLASS-9)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Output lines stay as they are; the guard adds skipped_cusip=<n>.",
  "world_is": "With no CUSIP rows (today) the line is byte-identical to before; with CUSIP rows offered, reporting len(items) would claim seeding rows the guard skipped.",
  "notes": "Judged a truthfulness fix inside the guard's own edit, not a copy-logic change. Revert to len(items) if the issuer wants the literal old line."
}
```

## MDPF_SECCLASS-W9-S3 -- tree-check INDEX-DRIFT blocks every org/missions commit

```json
{
  "id": "MDPF_SECCLASS-W9-S3",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~9",
  "surfaced_at": "2026-09-30T15:10:00Z",
  "one_line": "safe-commit's missions-tree-check refuses every commit that stages a path under org/missions/ because the committed index org/projects/NFRA_TRNSPT.json says dep_stage PRD while its tree row says EXECUTING.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "0.0.0_AB_MSTR (regenerate the NFRA_TRNSPT index row; the shared checkout already carries it as an uncommitted modification)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python .tools/missions-tree-index.py check on wk-MDPF_SECCLASS-9 @6d44575a7f -> [INDEX-DRIFT] org/projects/NFRA_TRNSPT.json: dep_stage: index='PRD' tree='EXECUTING'; RESULT: 1 violation(s)",
      "git log -- org/projects/NFRA_TRNSPT.json -> last commit 1d8905b007 (L3 register, PRD); 81e350ba0a moved the tree row to EXECUTING without the index"
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Base defect, not this cell: the NFRA_TRNSPT issuance omitted its generated index. Fixed by the issuer at 17ad3ea043, cherry-picked onto wk-MDPF_SECCLASS-9 as b622e6a245; python .tools/missions-tree-index.py check now reads RESULT: 0 violation(s). Issuer-ruled state RESOLVED is not in the ratified disposition enum, so DISMISSED_WITH_REASON carries it.",
  "spec_asserts": "A worker's commit of its proof, flip and surprise rows under org/missions/ passes safe-commit.",
  "world_is": "The tree check fails at HEAD independent of this cell, so the proof instance, the status flip and rows W9-S1..S3 could not be committed; the code, test, R5 check and half (outside org/missions/) were committed separately. org/projects/ is outside this order's paths, so no edit was made there and no bypass was used.",
  "notes": "DISARMED: base defect fixed by the issuer; commit b622e6a245 on wk-MDPF_SECCLASS-9 (cherry-pick of 17ad3ea043) regenerates org/projects/NFRA_TRNSPT.json; evidence: python .tools/missions-tree-index.py check in this worktree -> RESULT: 0 violation(s). Once the index row is regenerated, one commit of the three org/missions paths (proof instance dir, INVESTIGATION_v1.md, this order file with status complete) finishes the order; those files sit valid and uncommitted in the worktree."
}
```


## MDPF_SECCLASS-S5 -- the BD thread library cannot import the shared client on the flat gold runner (C_06 crashed; rolled back)

```json
{
  "id": "MDPF_SECCLASS-S5",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~M",
  "surfaced_at": "2026-09-30T18:05:00Z",
  "one_line": "The BD thread library data/black_diamond/scripts/gold/lib/etf_classifier.py reaches the shared client through a repo-relative hop (Path(__file__).resolve().parents[5] / infra/aws/lambda/v2_portal/_shared, :19); the gold runner syncs scripts flat to /tmp/gold_layer_scripts/, which has no fifth ancestor and no shared client, so the deployed C_06 crashed at import (IndexError: 5) in the 16:36Z exercise run and D_03/D_04 never ran. E_18 carries the same class of hop (parents[4], :54). Every in-repo test passed because the repo tree supplies the ancestors the runner lacks.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~M (disarmed 18:16:09Z by rolling the five BD code objects back to their pre-window versions; the fix-forward needs a new half, CTO condition 7)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3://opal-data-bd/logs/gold-layer/gold_incremental_2026-09-30_20260930_174903.log -- 17:47:29Z C_06: 'File \"/tmp/gold_layer_scripts/lib/etf_classifier.py\", line 19 ... parents[5] ... IndexError: 5'; 'C_06 done (rc=1)'; '=== COMPLETE (exit code: 1) ===' at 17:49:03Z; D_03/D_04 absent from the run.",
      "Served keys unchanged across the run (watch 17:49:54Z, changed=0 of 4): firm_composition AUXYImvT.., mix_daily_summary oIyAV02C.., z08327149 summary RMmQy.i3.., firm mix_summary 4iHMfpRA.. -- no served value moved.",
      "Rollback 18:16:09Z, copy-object from the prior VersionId, ETag verified per key: lib/etf_classifier.py 884889c0.., silver/build_bd_assets_dim.py 662ef035.., D_03 346e7b0f.., D_04 a4b867d4.., C_06 8b1f012c.. (the versions the 04:00Z run executed successfully).",
      "E_18: 0 occurrences in the cumulative gold log (5.6M lines); E_18.detect_new_securities.py:54 _REPO_ROOT = parents[4] would IndexError on the same flat layout."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "BD_THREAD_R2 half step 1: the five committed files deploy to opal-data-bd/code/{gold,silver} and step 3's ordinary run executes them; the round-1 thread cells SC-t-1..t-4 graded the library's import of the shared client as working.",
  "world_is": "The runner executes a flat copy of code/gold/ with no infra/ tree beside it, so any module-level repo-relative hop into infra/aws/lambda/v2_portal/_shared fails at import. The thread cannot run on the runner until the shared client ships with the gold code (or the library resolves it from the runner's own layout) and a real runner exercise proves the import.",
  "notes": "Same class as W6-S1 (E_18's hop), which was fixed for the repo tree only. Fix-forward is a code cell plus a new half (a new file on the runner is a deviation the signed half does not name). E18 IAM+deploy half's acceptance (first 04:00Z scheduled run of E_18) is unreachable as written: E_18 is not in the gold chain."
}
```


## MDPF_SECCLASS-W11-S1 -- SC-e-14's attribute_exists(ticker) breaks four older tests that pin the condition string

```json
{
  "id": "MDPF_SECCLASS-W11-S1",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~11",
  "surfaced_at": "2026-09-30T20:10:00Z",
  "one_line": "Adding attribute_exists(ticker) to the two S4 update conditions (as SC-e-14 orders) makes four existing tests in test_classified_by_v2.py and test_set_instrument_kind.py fail: they pin the exact string attribute_not_exists(<attr>) and their stubs key the refusal on it; both files are outside SC-e-14's paths.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python -m pytest infra/aws/lambda/v2_portal/_shared/tests infra/aws/lambda/v2_portal/yang_pipeline/tests -q -p no:cacheprovider on wk-MDPF_SECCLASS-11 -> 7 failed, 78 passed. Four are caused by this cell: test_classified_by_v2.py::test_label_update_writes_only_classified_by (asserts ConditionExpression == 'attribute_not_exists(classified_by)', lines 201/216), ::test_label_update_refuses_an_already_labelled_row, test_set_instrument_kind.py::test_only_instrument_kind_changes (lines 54/73/94) and ::test_row_with_existing_kind_is_refused.",
      "Three are NOT caused by this cell: test_classified_by_v2.py::test_contract_version_is_0_2_0 and ::test_contract_classified_by_has_four_values (contract is 0.3.0), and test_seed_etf_constituents.py::test_positioning_universe_plan_unchanged (expects table.batched but the script writes conditional puts) -- the last reproduced by running HEAD's unmodified seed-etf-constituents.py and test in a scratch copy: 1 failed, 7 passed."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "SC-e-14 (c): add attribute_exists(ticker) to each S4 update condition, one clause each; the order's AC1 names only the two new test files, and its paths grant does not include the older tests that pin the condition string.",
  "world_is": "The new condition reads 'attribute_exists(ticker) AND attribute_not_exists(<attr>)'. The two older test files compare the condition string for equality, so they fail until updated (their stub refusal keys on the old string); the new test_update_requires_existing_row.py covers the new behaviour with a clause-evaluating stub. Also: an update on an absent key now raises RowAlreadyLabelled / KindAlreadySet (the same ConditionalCheckFailedException), whose names say 'already' -- no skeleton row is created, but the message is imprecise. No test was weakened; no out-of-grant file was edited.",
  "notes": "Owner of the fix: the issuer (extend <paths> with the two older test files, or an L10 cell); the required edit is to their expected string and their stub's condition match."
}
```


## MDPF_SECCLASS-W11-S2 -- correction to W11-S1: S4/contract assertions resolved by amendment 1; constituents-plan test failure is pre-existing on CLOUD

```json
{
  "id": "MDPF_SECCLASS-W11-S2",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~11",
  "surfaced_at": "2026-09-30T21:00:00Z",
  "one_line": "Correction to MDPF_SECCLASS-W11-S1 (amendment 1 resolves its four S4 assertions and two contract assertions; test_seed_etf_constituents.py::test_positioning_universe_plan_unchanged is pre-existing on CLOUD at line 202): recorded as a new row because the surprise-row gate refuses an in-place edit of W11-S1.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Amendment 1 (2.0.0_SA_COO~M, b4df4b3630) resolution of W11-S1: the four S4-string assertions in test_classified_by_v2.py and test_set_instrument_kind.py now pin 'attribute_exists(ticker) AND attribute_not_exists(<attr>)' and their stubs refuse on it (an already-set row still raises RowAlreadyLabelled / KindAlreadySet); the two contract assertions read contract_version and classified_by values from org/standards/MDPF_SECCLASS_CONTRACT.json at HEAD (the version check is now a floor of 0.2.0 and the values check a superset of the original four with a definition for every listed value, because the order forbids typing the version or values). python -m pytest test_classified_by_v2.py test_set_instrument_kind.py -q -p no:cacheprovider -> 24 passed; AC1 over four files -> 33 passed. test_set_instrument_kind.py's stub also still refuses seed-etf-constituents.py's kind-only condition 'attribute_not_exists(instrument_kind)', which is not an S4 script and is unchanged.",
      "PRE-EXISTING on CLOUD, not granted, left alone: infra/aws/lambda/v2_portal/yang_pipeline/tests/test_seed_etf_constituents.py::test_positioning_universe_plan_unchanged fails at line 202 (assert [i['ticker'] for i in table.batched] == ['JPM'] -> AssertionError: assert [] == ['JPM']). Reproduced on CLOUD's UNMODIFIED script and test: git archive of infra/aws/lambda/v2_portal at 05f0a0b5af (the parent of this order's build commit cf24f07493) extracted to .scratch/base, python -m pytest test_seed_etf_constituents.py -q -p no:cacheprovider -> 1 failed, 7 passed, same line 202, same assertion. The script writes conditional puts where the test expects table.batched, so the failure does not come from SC-e-14's PRE-READ count edit."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Amendment 1 to MDPF_SECCLASS.TO-SC-e14: record the failing test and line of test_seed_etf_constituents.py::test_positioning_universe_plan_unchanged as pre-existing in row W11-S1.",
  "world_is": "Row W11-S1 cannot be edited in place: .tools/surprise-row-gate.py refuses a mutated existing row ('Corrections are NEW items citing the old id'), so the record lives in this new row citing MDPF_SECCLASS-W11-S1, which stays exactly as committed. The constituents-plan test failure is open and unowned; its repair is outside this order's grant.",
  "notes": "Owner of the remaining failure: whoever owns seed-etf-constituents.py and its test (a separate cell). W11-S1's S4 and contract assertions are resolved by amendment 1."
}
```

## MDPF_SECCLASS-W12-S1 -- seed-etf-classifications.py merge_item() carries classification_confidence and low_confidence onto a classifie

```json
{
  "id": "MDPF_SECCLASS-W12-S1",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~12",
  "surfaced_at": "2026-09-30T22:15:00Z",
  "one_line": "seed-etf-classifications.py merge_item() carries classification_confidence and low_confidence onto a classified_by='seed' row when a model row's ticker is added to the seed source, which contradicts MDPF_SECCLASS_CONTRACT 0.3.0 (a seed correction 'drops low_confidence entirely'; both fields present ONLY on a model row).",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~M (issue a code cell in the seed script's owner lane: merge_item() must drop classification_confidence and low_confidence, or the contract sentence must be corrected, BEFORE any model row's ticker enters etf_classification.py; r6_model_reader_census.py re-grades this reader on the same exercise)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_model_reader_census.py -> reader infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py FAILS-CONTRACT: merge_item(ACSG, <model row with classification_confidence=Decimal('0.62'), low_confidence=True>) returns classified_by='seed' together with both model attributes (R6_MODEL_READER_CENSUS_20260930.json, readers[].evidence).",
      "infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py:113-117 '# Carry forward any attribute a curator added that this script does not derive' copies every existing attribute not already in item and not in PROVENANCE_FIELDS (line 45: last_updated, updated_by, classified_by); the two model fields are in neither.",
      "org/standards/MDPF_SECCLASS_CONTRACT.json fields.low_confidence.rule24_record.state_coherence: 'a later seed correction of a model row replaces classified_by = seed and drops low_confidence entirely, same as classification_confidence'; fields.classification_confidence.absent: present ONLY on a model row.",
      "Population today: the 260 classified R4 tickers overlap the seed source (etf_classification.ETF_CLASSIFICATIONS) by 0; live table read 2026-09-30 (2657 rows) holds classified_by scheduled 2281, legacy 238, seed 138, model 0, so no live row is wrong; the defect fires on the contract's own documented correction path."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order SC-e-15 step 2/3 and the CTO's ruling 2: every reader of etf-classifications tolerates a model row with no crash, no refusal and no strict-contract failure; MDPF_SECCLASS_CONTRACT 0.3.0 promises a seed correction drops both model attributes.",
  "world_is": "The seed reader/merger runs without error on a model row but its merge loop preserves classification_confidence and low_confidence onto the rewritten seed row, leaving a seed row that claims a model confidence. The census reports FAILS-CONTRACT for this reader, so MODEL-READER-TOLERATED is not printed and the MODEL_ROWS act stays refused.",
  "notes": "I did not change the reader (outside the order's paths). Independent of the classify_holdings row (W12-S2). Same grain as the contract's state_coherence statement for both fields."
}
```

## MDPF_SECCLASS-W12-S2 -- ETFClassifier.classify_holdings (static) raises KeyError on any asset_class outside fixed_income/equity/hedge/

```json
{
  "id": "MDPF_SECCLASS-W12-S2",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~12",
  "surfaced_at": "2026-09-30T22:15:00Z",
  "one_line": "ETFClassifier.classify_holdings (static) raises KeyError on any asset_class outside fixed_income/equity/hedge/unknown, so it crashes on a model row classed alternatives, commodities or structured, and already on live rows of those classes (live: alternatives 4, commodities 8, structured 5); zero functional call sites, three byte-identical copies.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R6_CHECKS/r6_model_reader_census.py -> 3 readers CRASHES: ETFClassifier.classify_holdings in _shared/etf_classifications_dynamodb.py and the two positioning Lambda copies (md5 e62906eff240a853029181715fc9b451 on all three): KeyError('alternatives') on model row MDLX009; the control seed row ALTSEED (alternatives, classified_by=seed) raises the same KeyError.",
      "infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py:165-200 result = {fixed_income, equity, hedge, unknown, unknown_tickers}; `result[asset_class] += weight` with no default.",
      "comp-find 'classify_holdings(' --all (2026-09-30, 46476 files scanned, 8 hits): 7 definitions (3 copies of this method, 3 copies of a different static-module function, 1 unrelated INF _classify_holdings) and 1 call of the INF function; no caller of ETFClassifier.classify_holdings.",
      "Live read of etf-classifications 2026-09-30: 2657 rows, asset_class equity 2054, fixed_income 586, commodities 8, structured 5, alternatives 4, so the crash is not new with the model rows."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order SC-e-15: find every reader of the table and exercise each reader's real function on a model row; a reader that crashes is the finding.",
  "world_is": "The one client's static classify_holdings would crash on a model row of three of the five classes the model produces (alternatives/commodities/structured), but it has no caller and crashes identically on rows already live. The census grades it CRASHES because the order says do not weaken the check.",
  "notes": "Whether a zero-caller method belongs in the reader set is the issuer's or CTO's ruling; I did not exclude it. Fix shape if kept: seed the result dict from the ratified class list and use setdefault, in three byte-identical copies (packaged into Lambdas, so a change is a deploy act). INERT because nothing calls it."
}
```

## MDPF_SECCLASS-W12-S3 -- The census universe is the tracked tree at the worktree pin: the shared checkout holds untracked files (data/a

```json
{
  "id": "MDPF_SECCLASS-W12-S3",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECCLASS~12",
  "surfaced_at": "2026-09-30T22:15:00Z",
  "one_line": "The census universe is the tracked tree at the worktree pin: the shared checkout holds untracked files (data/assets/scripts/gold/irpt_reporting/, data/black_diamond/scripts/silver/lib/config.py and __init__.py, data/etfs/scripts/dedup/) this census cannot see, and the portal submodule is not checked out in the worktree, so the portal rows are READ-ONLY at the gitlink pin 3e2233de92.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git status at session start lists `?? data/assets/scripts/gold/irpt_reporting/`, `?? data/black_diamond/scripts/silver/lib/__init__.py`, `?? data/black_diamond/scripts/silver/lib/config.py`, `?? data/etfs/scripts/dedup/` in the shared checkout; none is in the worktree at 05f0a0b5af.",
      "ls C:/Users/AndrewBerman/Desktop/wk_mdpf_secclass_12/portal is empty (git ls-tree HEAD portal = 160000 commit 3e2233de920b19e47bd37adad81d599ec7ffd12f); portal files were read with git show at that pin from the shared checkout's portal object store.",
      "r6_model_reader_census.py completeness guard: code files naming the table outside org/docs/archive, tracked, are all in READERS/NOT_READERS or are tests; 0 UNCENSUSED at build."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Order SC-e-15 step 1: find every reader of the table by re-running the comp-find searches; the half's census section binds a fresh census immediately before the act.",
  "world_is": "Readers that exist only as untracked files in the shared checkout, or that arrive on the integrated tree after this cut, are outside this run. The check prints UNCENSUSED for any tracked code file naming the table that is in neither READERS nor NOT_READERS, so the act-time re-run on the integrated tree closes this; the portal rows re-verify their deciding lines automatically when portal/ is checked out.",
  "notes": "Not a defect in the census; a stated bound. No untracked file was read."
}
```
