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
