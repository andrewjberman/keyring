# MDPF_SECCLASS -- rounds 6-8 remediations

<sweep_watermark>2026-10-07T09:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-07. Graduated at this compile (ADJUDICATION_v6.md): 46 investigation rows and one new
compiler row (C-S13, 49 Financial's top-level mix leaves $6,502,294.55 in no class). ARMED: S46 (the six-class fix is on the
unmerged `q/dell1/secclass-e21/r1` @63fa1a2e32; `_shared/etf_classification.py` reads 25 `multi_asset` at this head, 0 there) and
S49 (a worker's PyPI download). Owners: `2.0.0_SA_COO~M1`, successor of the closed laptop lane `2.0.0_SA_COO~M`; ENDPOINT or
ruling questions to `1.0.0_SA_CTO~DELL1`. Carried unchanged: every row of REMEDIATION_v1 to v5 that is not closed (S2 and W6-S2
ARMED, S7 ARMED, and the INERT rows).

```json
[
  {
    "id": "MDPF_SECCLASS-C-S13",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "49 Financial's served platinum/firm/mix_summary.json (data_as_of 2026-10-05) divides its top-level mix by total_aua $2,007,761,226.11 while its eight classes sum to $2,001,258,931.56, so $6,502,294.55 (0.32 pct) sits in no class and the top-level percentages sum to 0.99676; composition.mix in the same file sums to 1.0.",
    "evidence": [
      "s3 cp s3://opal-data-bd/platinum/firm/mix_summary.json (LastModified 2026-10-07T05:49:01Z) and recompute by 3.0.0_SA_CVO 2026-10-07 10:0xZ: sum(mix.pct)=0.9967614, sum(mix.market_value)=2,001,258,931.56, mix_periods[2026-Q4].total_aua=2,007,761,226.11; composition.mix pct sum 1.000001",
      "first seen by this seat's fork while reading S11 (secclass_A); differs from S36's $5,491,967.16 composition gap, so carried separately until shown to be the same"
    ],
    "remedy": "Name which holdings make up the $6.5M (unpriced, cash-like or dropped by the class join) and either class them or state the residual as its own line. Close when sum(mix.pct) reads 1.0 to 4 places on the next served 49F file, or 1.0.0_SA_CTO~DELL1 rules the residual is intended and the page labels it.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S11",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The name-resolution table read by E_18 and the classifier's blank-ticker path has no live writer; it is six months stale, and 49 Financial's served mix carries 7.06 pct unclassified on 2026-10-05.",
    "evidence": [
      "s3api head-object opal-data-bd gold/dimensions/ticker_resolution.parquet: LastModified 2026-04-07T21:54:55Z, ContentLength 181,478 -- unchanged since the row",
      "served platinum/firm/mix_summary.json (2026-10-07T05:49Z, data_as_of 2026-10-05): unclassified 141,722,269.22 = 7.06 pct of the firm mix, above the 5.0 pct re-land bar the row names",
      "investigation row MDPF_SECCLASS-S11 (2.0.0_SA_COO~M)"
    ],
    "remedy": "One run of resolve_tickers under its own never-widen packet (CTO batch 150), after confirming whether it calls an outside service (Andrew's per-use word if so). Close when: head-object reads a LastModified after the run and the next served 49F mix reads unclassified at or under 5.0 pct, or the CTO rules the bar moved.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S14",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Black Diamond's feed puts one ticker on several securities for 274 tickers (S10's GLDM included); positions with a ticker are classed by it, so a different fund sharing the ticker takes its class.",
    "evidence": [
      "dynamodb get-item etf-classifications GLDM: commodities / Metals, seed -- the table is still keyed by ticker with no CUSIP disambiguation; no later row or commit in this channel reports a feed fix",
      "investigation row MDPF_SECCLASS-S14 (2.0.0_SA_COO~M)"
    ],
    "remedy": "Measure how many of the 274 are different funds rather than share classes of one fund; route the different-fund set to the feed or silver-builder owner, or a CUSIP read in the classifier. Close when: a census file names, for each of the 274, share-class or different-fund, and every different-fund ticker has an owner and a fix or a CTO acceptance.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S15",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "One served row carries a non-ASCII name and the CUSIP-row writer has no ASCII refusal.",
    "evidence": [
      "dynamodb get-item etf-classifications CUSIP:025083882 (ConsistentRead): name 'AMERICAN CENTURY ULTRA\\xae INV', 1 non-ASCII character, updated_by mdpf-secclass-cusip-rows, last_updated 2026-10-02T12:18:51Z -- unchanged",
      "investigation row MDPF_SECCLASS-S15 (3.0.0_SA_CVO)"
    ],
    "remedy": "Rewrite the name in ASCII through the same writer path and add an ASCII refusal to plan_rows. Close when: get-item reads an ASCII name and plan_rows refuses a non-ASCII name in a test.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S20",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "account_is_open reads True for pre-2026 accounts whether or not they still exist; any consumer keying liveness on it alone over-counts (B_00.load_account_closures uses ~account_is_open).",
    "evidence": [
      "data/black_diamond/scripts/gold/A_00.accounts_dimension.py:6-13 at HEAD: status enrichment from silver/allocations 'latest snapshot (left join, Jan 2026+ accounts only)' -- unchanged, so pre-2026 accounts keep a default status",
      "investigation row MDPF_SECCLASS-S20 (2.0.0_SA_COO~M)"
    ],
    "remedy": "Census the consumers of ACCOUNTS_DIMENSION that key inclusion on account_is_open alone, and route the field's semantics to A_00's producer owner (POD4) or document it as 'not a liveness signal before 2026'. Close when: the consumer census is filed and each consumer keying on the field alone is fixed, or the field's contract states its pre-2026 meaning and the CTO accepts.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S22",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The BD gold runner runs the chain on every boot and at least five paths boot it, so a hold that disables rules does not stop BD gold. INERT: no hold is in force and the live code is the fixed cell.",
    "evidence": [
      "events list-rules: bd-gold-nightly-fallback ENABLED, bd-canonical-prices-daily ENABLED, bd-gold-layer-monthly-trigger DISABLED; bucket notification GoldLayerPricesTrigger -> bd-gold-trigger present -- at least three boot paths live today besides the 49F dispatcher",
      "investigation row MDPF_SECCLASS-S22 (2.0.0_SA_COO~M)"
    ],
    "remedy": "Write the BD gold hold procedure into the next BD gold half: hold the host (stop plus deny StartInstances, or reserved concurrency 0 on bd-gold-trigger and advi-49f-gold-dispatch), and list every boot path. Close when: the next BD gold never-widen half names every boot path and holds the host, read back during its act.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W13-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Not live today (0 of 626 BLOOMBERG rows carry a name, so none is listed), but the catalogue has no BLOOMBERG filter: any later name on a BLOOMBERG row (for example a clean-name write, SC-e-34) lists a key the resolver refuses.",
    "evidence": [
      "aws dynamodb scan etf-classifications (auto-paginated) 2026-10-07: ScannedCount 3507, BLOOMBERG rows 626, BLOOMBERG rows with a name 0",
      "comparison_catalogue.py build_catalogue lists a classified ticker only when _row_name is non-empty; its scan drops only identifier_namespace CUSIP (no BLOOMBERG filter)",
      "_scope/maintained_sources.py:539 CLASSIFIED_ETF_TICKER = [A-Z][A-Z0-9.]{0,9} still rejects BBG:REL:LN",
      "investigation row MDPF_SECCLASS-W13-S1 (0.9.0_WK_MDPF_SECCLASS~13)"
    ],
    "remedy": "Either the catalogue drops identifier_namespace BLOOMBERG rows, or the clean-name write (SC-e-34) excludes BLOOMBERG rows by a stated rule. Close when: A scan reads 0 named BLOOMBERG rows after the clean-name write, or build_catalogue skips BLOOMBERG rows at HEAD.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W13-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "scoped_amgt reduces a Bloomberg ticker ('REL LN') to its first token, so a London ranking row joins the US REL row and never the BBG:REL:LN row FWD-9 wrote; pre-existing.",
    "evidence": [
      "lib/research/api/scoped_amgt.py:704, :723, :760, :780, :1014 still key the table on str(ticker).strip().split(' ')[0]",
      "investigation row MDPF_SECCLASS-W13-S3 (0.9.0_WK_MDPF_SECCLASS~13)"
    ],
    "remedy": "scoped_amgt maps a Bloomberg ticker with a non-US yellow key to its BBG:<T>:<CC> table key before the bare-token fallback. Close when: A read of 'REL LN' through _classification_for_ticker returns the BBG:REL:LN row.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W13-S5",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-6 model-reader census has drifted further than the row recorded (now crashes=1, fails_contract=2, 9 uncensused), so it cannot certify MODEL-READER-TOLERATED; SC-e-40 is the FWD-4 copy census, a different instrument.",
    "evidence": [
      "bare run of R6_CHECKS/r6_model_reader_census.py at 572829ce3b on dell1 2026-10-07: rc=0, MODEL-READER-CENSUS readers=37 tolerates=26 read_only=8 crashes=1 refuses=0 fails_contract=2; 9 UNCENSUSED files (incl. mdpf-secclass/sector-writer, ai-index/index_writer, rivalfunds_classification.py)",
      "investigation row MDPF_SECCLASS-W13-S5 (0.9.0_WK_MDPF_SECCLASS~13)"
    ],
    "remedy": "Re-baseline the model-reader census over the current readers, or retire it for a named successor, in the next issuance. Close when: The census (or its named successor) prints MODEL-READER-TOLERATED with crashes=0, fails_contract=0 and 0 UNCENSUSED at the round head.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W15-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FWD-9's history half is unfilled: security_market holds four trading days, so no Rival Funds stock has a three-year series.",
    "evidence": [
      "list-objects-v2 opal-data-etfs rivalfunds/etfs/gold/security_market/ 2026-10-07: 7 objects, partitions 2026-09-29, 10-01, 10-02, 10-05 only",
      "investigation row MDPF_SECCLASS-W15-S1 (0.9.0_WK_MDPF_SECCLASS~15)"
    ],
    "remedy": "A history backfill cell for security_market (under the Bloomberg budget and Andrew's vendor word), or a PRD statement that FWD-9's history half waits. Close when: r7_fwd9_history_coverage.py reads COVERED_3Y > 0, or the PRD re-scopes the history half.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W15-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "security_market keys some rows by '/cusip/<cusip>' in security_bloomberg, which joins no canonical_shape stock; a join on security_bloomberg alone loses them.",
    "evidence": [
      "same listing: the 2026-10-02 partition still has three revisions (10-04, 10-05 12:33Z, 10-05 12:46Z); the /cusip/ identity form was not re-read from the parquet here",
      "investigation row MDPF_SECCLASS-W15-S2 (0.9.0_WK_MDPF_SECCLASS~15)"
    ],
    "remedy": "Every FWD-9 history consumer joins on security_bloomberg then security_id (as the coverage check does), or the producer writes one identity form. Close when: A coverage read reports 0 unmatched /cusip/ rows, or the join rule is written into the series consumer.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W14-S5",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Under the ruled batch 259 rule, Rival Funds stocks with no Bloomberg id stay OUT; 7 collected stocks still have no row, so FWD-9 (every collected stock has a row) is unmet for them.",
    "evidence": [
      "live get-item 2026-10-07: BRK/B, CRWV, EPAM, FPS, MDLN, ORI, SLDE have no etf-classifications row",
      "investigation row MDPF_SECCLASS-W14-S5 (0.9.0_WK_MDPF_SECCLASS~14)"
    ],
    "remedy": "1.0.0_SA_CTO~DELL1 rules whether a TICKER-namespace row is written for a stock with no Bloomberg id, or the PRD names the 7 out of FWD-9's domain. Close when: get-item reads a row for each of the 7, or the PRD names them out of the domain.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W16-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A criterion that invokes .tools/terraform.exe cannot run on dell1: there is no terraform binary on the box (W24-S5 carries the provider half).",
    "evidence": [
      "dell1 2026-10-07: no .tools/terraform*.exe in this worktree or in the base checkout C:/Dev/ajb_workspace; C: 8% used (the row's disk-full half was the laptop and does not hold here)",
      "investigation row MDPF_SECCLASS-W16-S3 (0.9.0_WK_MDPF_SECCLASS~16)"
    ],
    "remedy": "The issuer cuts terraform-validate criteria to a box holding the binary and provider, or provisions both on dell1 by a named act. Close when: A terraform-invoking criterion runs rc=0 on the box it is issued to.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W16-S4",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The new-stock rule compares today's canonical_shape to the previous day, but partitions carry different fund sets and keep being revised, so new_stocks can read 0 (or list old stocks) for reasons unrelated to holdings.",
    "evidence": [
      "list-objects-v2 opal-data-etfs rivalfunds/etfs/gold/canonical_shape/date=2026-10*: date=2026-10-01 revisions written 10-02 (2), 10-03, 10-04, 10-05; date=2026-10-02 written 10-03, 10-04, 10-05 (2), 10-06 -- revisions keep landing, weekends included; fund counts per partition not re-read",
      "investigation row MDPF_SECCLASS-W16-S4 (0.9.0_WK_MDPF_SECCLASS~16)"
    ],
    "remedy": "The producer compares only funds present on both days (or the newest complete revision) and prints the rule in its output. Close when: A dry run on a day whose partitions carry different fund sets prints the fund intersection it compared and lists no stock outside it.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S27",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The 808516306 instance is resolved by a SCGB1 ticker row from the rule-B remap, but the producer still classifies by display.symbol only, so a CUSIP row never serves a node whose ticker the table lacks.",
    "evidence": [
      "dynamodb get-item etf-classifications: SCGB1 -> equity, updated_by mdpf-secclass-remap-b 2026-10-07T07:09:27Z; CUSIP:808516306 -> equity (same remap)",
      "data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:1010 at HEAD: annotate_classification still calls classify_security with disp.get('symbol'); security_id is not consulted",
      "investigation row MDPF_SECCLASS-S27 (2.0.0_SA_COO~M)"
    ],
    "remedy": "A producer fallback to CUSIP:<security_id> after a symbol miss (a served move under never-widen), or a ruling that ticker rows are the only route. Close when: the producer reads CUSIP:<security_id> after a symbol miss (a test with a CUSIP-only row), or 1.0.0_SA_CTO~DELL1 rules the fallback out",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S28",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "BG's sub_asset_class holds a GICS sector where its held nodes read a region (Developed); sector has no field of its own until FWD-12 lands, so the producer keeps writing sectors into sub_asset_class for new US tickers.",
    "evidence": [
      "dynamodb get-item etf-classifications: BG equity / Consumer Staples, BKD equity / Health Care, NBIS equity / Information Technology, gics_sector absent on all three, updated_by rivalfunds-backfill 2026-10-06T14:00:25Z; JAN absent",
      "investigation row MDPF_SECCLASS-S28 (2.0.0_SA_COO~M)"
    ],
    "remedy": "1.0.0_SA_CTO~DELL1 answers the row's question (skip a US key whose held node already reads a sub-class until FWD-12), or FWD-12 moves sector into gics_sector. Close when: BG reads its sector in gics_sector and sub_asset_class carries the ruled value, or the CTO rules the write stands",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S29",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Four Cottonwood client mixes sum below 1 on the 10-05 point because positions were classed multi_asset at run time and the gold lists drop that class; the remap removed every multi_asset row at 07:09Z, but no Cottonwood run has read the remapped table yet.",
    "evidence": [
      "s3 opal-data-cot platinum/firm/mix_summary.json LastModified 2026-10-06T11:38:31Z data_as_of 2026-10-05: no Cottonwood run since; class keys carry no multi_asset",
      "dynamodb scan etf-classifications filter asset_class=multi_asset: Count 0 of ScannedCount 3507 (2026-10-07 ~09:5xZ)",
      "investigation row MDPF_SECCLASS-S29 (2.0.0_SA_COO~M)"
    ],
    "remedy": "Read the first scheduled Cottonwood run after 2026-10-07T07:09Z. Close when: that run's latest point reads 219 of 219 client mixes summing to 1 within 0.001, including z09305578, z09305621, z09305679, z09305703",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W20-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Cottonwood's C_06 skips the advisor-level mix aggregation because gold/views/rel_architect_lookup.parquet does not exist in opal-data-cot.",
    "evidence": [
      "aws s3api head-object opal-data-cot gold/views/rel_architect_lookup.parquet 2026-10-07: 404 Not Found (the bucket answered, so absence, not denial)",
      "investigation row MDPF_SECCLASS-W20-S1 (0.9.0_WK_MDPF_SECCLASS~20)"
    ],
    "remedy": "Name the producer of rel_architect_lookup for Cottonwood, or declare advisor-level mix out of scope for Cottonwood in the PRD. Close when: head-object reads 200, or the PRD names the advisor mix out of scope for Cottonwood.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S30",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Inflection's served firm_concentrations reports a firm AUA 1.873x the same-day firm_composition total; cause unread. Not a classification defect, so likely outside this project's write surface.",
    "evidence": [
      "s3 cp + read opal-data-inf platinum/firm/firm_concentrations.json (LastModified 2026-10-06T12:52:58Z, data_as_of 2026-10-05): total_firm_aua 389,707,543.56; firm_composition.json (12:51:23Z, same date): total_market_value 208,044,040.13 -- unchanged since the row",
      "investigation row MDPF_SECCLASS-S30 (2.0.0_SA_COO~M)"
    ],
    "remedy": "Read INF_D_07a's input join and route the fix to the Inflection gold owner (a served move under never-widen), or 1.0.0_SA_CTO~DELL1 places it outside MDPF_SECCLASS. Close when: a served Inflection run reads total_firm_aua equal to firm_composition total_market_value within $0.01, or the CTO re-homes the row",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S32",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Both gold folders ship a top-level lib package, so a single pytest process over both is order-dependent and fails four Cottonwood tests on a clean tree; the basename-collision half of the row is moot.",
    "evidence": [
      "python -m pytest over data/black_diamond/scripts/gold/tests and data/cot/scripts/gold/tests in one process at HEAD: 4 failed, 93 passed ('ETFClassifier' object has no attribute 'classify_position' in cot tests); data/cot/scripts/gold/tests alone: 21 passed",
      "git ls-files: test_mix_publishes_every_class.py exists only under data/cot (the basename collision is gone)",
      "investigation row MDPF_SECCLASS-S32 (2.0.0_SA_COO~M)"
    ],
    "remedy": "Any criterion running both folders names two pytest invocations, or a conftest / --import-mode=importlib change isolates lib per folder. Close when: the one-process run over both folders reads 0 failed, or the issuer's standing rule names per-folder invocations",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S36",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The served BD firm composition still shows a $5,491,967.16 class-sum gap (re-rendered 05:28Z today, before the 07:09Z remap); the 00:26Z off-schedule runner is not identified (compare S21/S22 boot-time runs).",
    "evidence": [
      "s3 opal-data-bd gold/views/firm_composition.json generated 2026-10-07T05:28:10Z data_as_of 2026-10-02: total 2,007,761,226.11, sum of 7 class market_values 2,002,269,258.95, gap 5,491,967.16; mix_daily_summary.json LastModified 2026-10-07T05:27:03Z",
      "investigation row MDPF_SECCLASS-S36 (2.0.0_SA_COO~M)"
    ],
    "remedy": "Read the first BD gold run after 2026-10-07T07:09Z. Close when: firm_composition total equals the class sum within $0.01, and mix_daily_summary is rewritten by the same run",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S44",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FWD-12's only planned source (the Bloomberg characteristics file) covers ~114 securities of 3,507 table rows, so the sector writer cannot meet 'every row carries a sector and industry group'; the T-1 partition 2026-10-06 is also absent at ~10Z today.",
    "evidence": [
      "aws s3 ls s3://opal-data-etfs/bbg/ 2026-10-07 ~10Z: newest partitions 2026-10-01, 2026-10-02, 2026-10-05; no 2026-10-06 (a trading day, T-1 of today)",
      "row's own SC8-e25 green arm: rows=114 sector=10",
      "investigation row MDPF_SECCLASS-S44 (2.0.0_SA_COO~M1)"
    ],
    "remedy": "ENDPOINT question for the round-8 analysis: name the second sector source for the other ~3,390 rows, or narrow FWD-12's population. Close when: a PRD addendum names the second source (or narrows FWD-12) and a census reads sector coverage over the named population",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S45",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "2,624 of 3,507 rows carry no name, so FWD-14's clean name cannot be produced from table names alone; no cash rows exist for an AI cash verdict to land against.",
    "evidence": [
      "aws dynamodb scan etf-classifications --consistent-read --select COUNT filter attribute_not_exists(name): Count 2624 of ScannedCount 3507 (2026-10-07 ~10Z)",
      "investigation row MDPF_SECCLASS-S45 (2.0.0_SA_COO~M1)"
    ],
    "remedy": "ENDPOINT question: name the name source for unnamed rows (or narrow FWD-14 to named rows) in the round-8 analysis. Close when: a PRD addendum names the source and a scan reads named rows over the stated population",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S46",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The seed module at HEAD still carries multi_asset; the six-class fix is on an unmerged branch, so a seed run today would write multi_asset back over the remap; the low_confidence question is open with the CTO.",
    "evidence": [
      "git show HEAD:infra/aws/lambda/v2_portal/_shared/etf_classification.py | grep -c multi_asset -> 25; at 63fa1a2e32 (q/dell1/secclass-e21/r1) -> 0",
      "63fa1a2e32 is NOT an ancestor of the round branch and NOT on origin/CLOUD (merge-base read)",
      "63fa1a2e32 body: 0 mentions of low_confidence",
      "investigation row MDPF_SECCLASS-S46 (2.0.0_SA_COO~M1)"
    ],
    "remedy": "Land TO-SC-e21 (63fa1a2e32) on CLOUD after the laptop CTO's read and get the low_confidence answer; no seed run before. Close when: CLOUD's seed module reads 0 multi_asset and SC8-e21-AC2 reads 0 CONFLICT at HEAD, with the low_confidence ruling recorded",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S47",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PRD manifest paths for S26 and S13 do not exist at the depth written; the census resolved them by suffix.",
    "evidence": [
      "ls infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py exists; MDPF_SECCLASS_PRD.md:561 still writes `yang-generate-positioning/lambda_function.py:95` (bare path)",
      "W28-S1: FWD4_CENSUS_20261007.json s13_resolution maps all four S13 files to yang_pipeline/... and 01_market_overview/... paths",
      "investigation row MDPF_SECCLASS-S47 (2.0.0_SA_COO~M1)"
    ],
    "remedy": "Correct S13 and S26 paths at the next PRD addendum (absorbs W28-S1). Close when: PRD manifest S13/S26 paths resolve by ls at HEAD",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S48",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "An Inflection B_01b body sits on S3 with no dispatcher reading it; comp-pipescript deployed --firm cot misreads Cottonwood gold as missing (tool defect, outside this project).",
    "evidence": [
      "aws s3api list-object-versions opal-data-inf code/gold/B_01b.classify_new_securities.py: latest 2026-06-11T15:15:01Z ETag 840cdd1f09f49d9c9953040e610b6462",
      "investigation row MDPF_SECCLASS-S48 (2.0.0_SA_COO~M1)"
    ],
    "remedy": "Carry the Inflection object in TO-SC-e37's half request (remove or account for it); file the comp-pipescript defect with its owner. Close when: TO-SC-e37's half names the object's disposition and it is acted on, or the object is shown to be read by a dispatcher",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W24-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Six of the 23 measured GICS industry-group values are vendor-truncated at 30 characters and were declared verbatim into the contract's closed list.",
    "evidence": [
      "SECTOR_INDUSTRY_GROUP_VALUES_20261007.json present (keys diffs, measured_at, per_partition, producer_vocab, sources, union_over_partitions)",
      "investigation row MDPF_SECCLASS-W24-S1 (0.9.0_WK_MDPF_SECCLASS~24)"
    ],
    "remedy": "Rule whether the closed list carries vendor spellings or full names (with a serving-tier decode). Close when: a ruling recorded and the contract list matches it",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W22-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "iv-e-26's byte-identity arm fails on HoldingsSnapshot.ts between SC-e-23's hand edit and SC-e-22's schema change (dell2 ~M2 workstream); its content-pin/ExportBundle arms already failed at DEV 8ddfe40994.",
    "evidence": [
      "git -C portal log 91d29d17a0: worker ~22's e23 commit, only on branch wk-MDPF_SECCLASS-22-portal (held candidate)",
      "investigation row MDPF_SECCLASS-W22-S1 (0.9.0_WK_MDPF_SECCLASS~22)"
    ],
    "remedy": "Land SC-e-23's portal candidate only together with or after SC-e-22's schema enum change; keep dsgn-irptv1 tests out of the drain's portal run until then. Close when: iv-e-26 reads WIRE-REGEN-OK on portal DEV after both SC-e-22 and SC-e-23 land",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W23-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Three screen disagreements found by the FWD-16 census are recorded, not resolved: IR securities table folds Cash into Fixed Income while its treemap shows Cash; PerfrpAllocation prints raw lower-case tokens; Attribution etf-categories.ts lists a four-class order while the producer funnels to two.",
    "evidence": [
      "git -C portal show 8ddfe40994:src/components/holdings/HoldingsBreakdownTable.tsx lines 330-334: displayClass = asset_class === 'Cash' ? 'Fixed Income' : asset_class",
      "investigation row MDPF_SECCLASS-W23-S2 (0.9.0_WK_MDPF_SECCLASS~23)"
    ],
    "remedy": "Rule per screen in the round-8 analysis whether each is a FWD-16 cell (enrichment list). Close when: each of the three has a cell or a written ruling that it stays",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W23-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Workers on dell1 have no native Grep and a denied recursive grep, so searches run through ad-hoc scratch walkers that are not committed instruments.",
    "evidence": [
      "command -v rg -> /c/Users/Test/bin/rg; file: PE32+ executable, named 'rg' with no .exe suffix (so the native Grep tool's spawn of 'rg' ENOENTs on Windows); the Bash rail denies recursive grep",
      "investigation row MDPF_SECCLASS-W23-S3 (0.9.0_WK_MDPF_SECCLASS~23)"
    ],
    "remedy": "Box fix (dell1 fabric manager): expose rg as rg.exe on the harness PATH; meanwhile orders name comp-find or a committed instrument for every census. Close when: the native Grep tool returns results in a dell1 worker session",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W25-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The firm primary buckets deny dell1's agent principal by resource policy, so every held-set read on dell1 is a local producer build (claim inferred), never the served bytes.",
    "evidence": [
      "aws s3api head-object opal-data-49financial irpt/49financial/platinum/holdings/current/manifest.json as this box's identity, 2026-10-07 ~10Z: 403 Forbidden",
      "investigation row MDPF_SECCLASS-W25-S1 (0.9.0_WK_MDPF_SECCLASS~25)"
    ],
    "remedy": "A principal the firm buckets admit for read-only served reads from dell1 (access is the laptop's), or a ruling that dell1 grades held sets as inferred only. Close when: a served-bytes read of one firm manifest succeeds from dell1, or the ruling is recorded",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W25-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The order's '58 held' is not reproduced by any stated definition (1,449 held with no shared entry), and FWD-17's zero-gap gate also spans 6,036 unheld NAME:: rows.",
    "evidence": [
      "OLD_LIST_CENSUS_20261007.json: held_today_not_in_shared 1500, held_securities_not_in_shared 1449, held_not_in_shared_with_no_old_row 1046, in_both_lists 2381, held_claim inferred",
      "investigation row MDPF_SECCLASS-W25-S2 (0.9.0_WK_MDPF_SECCLASS~25)"
    ],
    "remedy": "Rule FWD-17's population (held only, or all old rows) and the held definition at the round-8 analysis. Close when: a ruling recorded and the census re-run under it",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S49",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A worker downloaded ruff from PyPI without a grant; the download cannot be undone and nothing on record yet stops the next worker doing the same.",
    "evidence": [
      "ls C:/Dev/wk-secclass-r8-26/.scratch/venv15/Lib/site-packages: ruff and ruff-0.15.11.dist-info present",
      "task orders touched after 09:20Z (TO-SC-e28, TO-SC-e38): 0 mentions of 'install'; worker spawn prompts are not in the repo, so the packet's 'every later spawn forbids installs' is UNREAD",
      "investigation row MDPF_SECCLASS-S49 (2.0.0_SA_COO~M1)"
    ],
    "remedy": "The next issuance's worker faces state 'no package install and no download of any kind'; 0.0.0_AB_MSTR~DELL1 disposes of or records the scratch venv; Andrew is told of the egress. Close when: the next issued order's worker face carries the prohibition and the venv is removed or recorded as kept",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W24-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The contract carries 10 measured sectors and holds Real Estate outside the values, against the four-postulate record's 11; a Real Estate security would read as an unknown sector.",
    "evidence": [
      "org/standards/MDPF_SECCLASS_CONTRACT.json at 572829ce3b: contract_version 0.5.0, gics_sector values 10, held_not_measured ['Real Estate']",
      "investigation row MDPF_SECCLASS-W24-S2 (0.9.0_WK_MDPF_SECCLASS~24)"
    ],
    "remedy": "Rule 10 or 11 at the round-8 analysis; an 11 is one list entry plus the pinned test and the issuer check. Close when: a ruling recorded and the contract's gics_sector values match it",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W23-S5",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-SC-e33's 'no entry' (neither symbol nor CUSIP:<cusip>) is wider than the producer's lookup (symbol only), so 238 held securities (49financial 51, cottonwood 187) the producer serves unclassified-by-table are absent from the missing lists.",
    "evidence": [
      "holdings_snapshot.py:882-887 canonical_lookup calls self._canonical.get_classification(t) with the symbol only; no CUSIP: key read",
      "investigation row MDPF_SECCLASS-W23-S5 (0.9.0_WK_MDPF_SECCLASS~23)"
    ],
    "remedy": "Issuer picks one definition (the producer's lookup is the served truth) and the lists are regenerated, or the producer's lookup gains the CUSIP: key. Close when: the missing lists and the producer's lookup use the same key set, shown by a re-run naming the 238",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W24-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The characteristics input home s3://opal-data-etfs/bbg/<day>/ is not builder-addressable, so the sector writer takes it as var.bbg_prefix: a rule-30 departure.",
    "evidence": [
      "python opal_naming.address('bbg','etfs','bronze','characteristics',...) -> REFUSED: source 'bbg' is not a systems.json key; address('mdpf','etfs','gold','sector_writer_runs',...) -> s3://opal-data-etfs/mdpf/etfs/gold/sector_writer_runs/...",
      "investigation row MDPF_SECCLASS-W24-S3 (0.9.0_WK_MDPF_SECCLASS~24)"
    ],
    "remedy": "An R20 register entry Andrew acknowledges (same shape as W16-S1), or a registry row that makes the bbg home builder output, before the root is applied. Close when: an R20 entry exists naming the bbg prefix, or address() resolves it",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W24-S4",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The sector-writer Lambda reads MDPF_SECCLASS_CONTRACT.json at runtime and has no lambda-source-map row, so the CI build would not package the contract file.",
    "evidence": [
      "infra/aws/lambda/ci/lambda-source-map.json at 572829ce3b: 0 occurrences of 'sector-writer'",
      "investigation row MDPF_SECCLASS-W24-S4 (0.9.0_WK_MDPF_SECCLASS~24)"
    ],
    "remedy": "Add the function's lambda-source-map row (handler, _shared imports, org/standards contract) before its first build. Close when: lambda-source-map.json carries the sector-writer row and a packaged build lists the contract file",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W24-S6",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The seed-wins rule reads two module dicts (ETF_GICS_SECTOR / ETF_GICS_INDUSTRY_GROUP) that do not exist yet; their names are a contract the future seed-fields cell must adopt.",
    "evidence": [
      "seed-etf-classifications.py:38 SEED_FIELDS lists no gics_sector/gics_industry_group; _shared/etf_classification.py: 0 occurrences of ETF_GICS_SECTOR",
      "investigation row MDPF_SECCLASS-W24-S6 (0.9.0_WK_MDPF_SECCLASS~24)"
    ],
    "remedy": "The cell that gives the seed source sector fields uses those two names (or renames them in the writer in the same commit). Close when: the seed module carries the dicts under the names the writer reads, or the writer is changed to match",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W26-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The AI runner's dry run used a 2026-09-30 residual for Inflection, not today's held set, so it shows the model path's reach, not the live plan; no current held input is readable on dell1 (W25-S1).",
    "evidence": [
      "R2_UNRESOLVED_REVIEW_20260930.json present at the drain head (generated 2026-09-30, keys generated_at/cell/denominator...)",
      "investigation row MDPF_SECCLASS-W26-S3 (0.9.0_WK_MDPF_SECCLASS~26)"
    ],
    "remedy": "FWD-11's real run uses a current held input from a box that can read it. Close when: an AI dry or real run over a current held set is recorded",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W28-S5",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "clean_name() mis-cases acronyms, ticker-shaped names and small words, and TO-SC-e34's row set carries that output; the clean-name write is not signable until it is repaired.",
    "evidence": [
      "python clean_name at 572829ce3b: 'BP PLC' -> 'Bp Plc', 'WMT' -> 'Wmt', 'BANK OF AMERICA NA' -> 'Bank Of America Na'; KEEP_UPPER holds 10 tokens only",
      "investigation row MDPF_SECCLASS-W28-S5 (0.9.0_WK_MDPF_SECCLASS~28)"
    ],
    "remedy": "Repair clean_name (acronym/ticker handling, small words) and regenerate the e34 row set before its half is signed. Close when: clean_name('BP PLC') == 'BP PLC' and clean_name('WMT') == 'WMT' and the regenerated row set carries the fixed output",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W26-S6",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "With 0 cash rows the table vocabulary has no cash sub-class, so cash is unreachable by DIRECT or AI; the 15 old cash rows will end UNRESOLVED although cash is one of the six classes.",
    "evidence": [
      "classify-residual-model.py:143-147 apply_bound returns 'no sub-class for %s' when the table carries no sub-class for the class",
      "investigation row MDPF_SECCLASS-W26-S6 (0.9.0_WK_MDPF_SECCLASS~26)"
    ],
    "remedy": "Rule the cash sub-classes (seed them, or admit the contract's list as the bound) at the round-8 analysis. Close when: a cash row can land through the bound, shown by a dry run that places the 15",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W26-S7",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "For the 2,482 NAME::-keyed AI rows the model receives the synthetic key 'NAME::<SLUG>' as its ticker; effect on classification quality is unmeasured.",
    "evidence": [
      "classify-residual-model.py:206 entries = [{'name': n, 'ticker': t} for t, n in pairs]",
      "investigation row MDPF_SECCLASS-W26-S7 (0.9.0_WK_MDPF_SECCLASS~26)"
    ],
    "remedy": "Send an empty ticker for NAME:: keys, or grade a sample of the first model run for this case. Close when: the first model run's grade covers NAME::-keyed rows, or the runner sends no synthetic ticker",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W26-S8",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The reclassification set is built per old key, so 1,046 held securities with no old row stay without an entry and FWD-15 cannot reach zero through it.",
    "evidence": [
      "OLD_LIST_CENSUS_20261007.json: held_not_in_shared_with_no_old_row 1046 of held_securities_not_in_shared 1449",
      "investigation row MDPF_SECCLASS-W26-S8 (0.9.0_WK_MDPF_SECCLASS~26)"
    ],
    "remedy": "Name the path for the 1,046 (the missing lists plus a producer for them) in the round-8 analysis. Close when: a measured FWD-15 count reads zero, or the remaining path is cut",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W25-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "dell1's principal cannot read opal/mcp/graph-read-token, so comp-find --corpus aws is BLOCKED on this box; live-plane traces fall back to direct scans with named blind spots (AWS-managed policies, resource policies, boundaries).",
    "evidence": [
      "comp-find --corpus aws 'bd-securities' on dell1 2026-10-07 ~10Z: 'BLOCKED: served-graph pull failed ... AccessDeniedException ... GetSecretValue ... cloudops-dell1-agent-user'",
      "investigation row MDPF_SECCLASS-W25-S3 (0.9.0_WK_MDPF_SECCLASS~25)"
    ],
    "remedy": "Grant dell1's principal read on the graph token (laptop access act), or orders on dell1 name the direct-scan instrument and its blind spots. Close when: comp-find --corpus aws returns a DENOMINATOR line on dell1",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W25-S4",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PRD S22's reader is a dead read (no trigger), and the live news curation role carries AmazonDynamoDBFullAccess, a blanket grant that can read the old list with no code naming it.",
    "evidence": [
      "infra/aws/terraform/news-pipeline/eventbridge.tf:11-17: 'semantic layer3 -> semantic-news-layer3-curation (DELETED) ... Lambda functions are retained'",
      "investigation row MDPF_SECCLASS-W25-S4 (0.9.0_WK_MDPF_SECCLASS~25)"
    ],
    "remedy": "Record S22 as DEAD-READ in the reader-switch list; route the opal-news-lambda-role blanket grant to the CTO as an access finding outside this project. Close when: the reader-switch list carries S22 as DEAD-READ and the role grant has an owner",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W25-S5",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The 46-file reader census misses readers that assemble the table name at runtime and excluded the 16 data/black_diamond files that name it, so the reader set behind the writer stops is incomplete.",
    "evidence": [
      "bd_securities_fallback.py:35-46 builds the table name as '%s-securities' % slot at runtime",
      "investigation row MDPF_SECCLASS-W25-S5 (0.9.0_WK_MDPF_SECCLASS~25)"
    ],
    "remedy": "The next reader trace covers data/black_diamond and runtime-assembled names before any writer stop uploads. Close when: a reader census with data/black_diamond in its denominator lands",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W25-S6",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "After the old-list writers stop, every fallback reader classifies a newly held security by name and ticker shape alone: no canonical producer has a live write (E_18 canonical path wrote 0). INERT only while TO-SC-e35..e37 stay off any pushed range.",
    "evidence": [
      "etf_classification_scheduled.py:43-46: GICS and Schwab lookups default to None, bd-securities is the one live input",
      "E_18.detect_new_securities.py:244-245: unguarded table = dynamodb.Table(BD_SECURITIES_TABLE) scan",
      "investigation row MDPF_SECCLASS-W25-S6 (0.9.0_WK_MDPF_SECCLASS~25)"
    ],
    "remedy": "Before any writer stop uploads, each real reader names a CANONICAL-PRODUCER with a measured live write count > 0 (packet analysis item 3). Close when: CANONICAL-PRODUCER reads non-NONE with a live write count for every real reader; re-arms to ARMED if a writer stop uploads first",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v9"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  }
]
```
