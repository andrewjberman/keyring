# ETFS_RIVALS -- surprise channel, INVESTIGATION v1 (site-Z fabric)

**Home:** the project tree's channel. Lane `ANY`; `.tools/surprise-row-gate.py` validates every NEW row
(schema, identity, coordinate, folder == project). **Append-only.**

**Id grammar on this fabric:** a seat's row is `ETFS_RIVALS-Z-S<k>`; a worker's row is
`ETFS_RIVALS-Z-W<n>-S<k>` with `<n>` its slot; `<k>` restarts at 1 per coordinate. `"project":
"ETFS_RIVALS"` and `"fabric": "site-z"` on every new row. The CVO's adjudication rows live in
`adjudications/`, never here.

---

```json
[
  {
    "id": "ETFS_RIVALS-Z-S1",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~RV",
    "surfaced_at": "2026-09-30T06:40Z",
    "one_line": "PRD v0.2 C-SHAPES says a GICS sector never stands in for a sub-asset class, but the ETF positioning vocabulary the PRD names as the classification source defines the equity sub_asset_class AS the GICS sector (a consumer-ratified mixed-source axis), so the two cannot both hold for an equity row once GICS arrives.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D4/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md @01e5499ae7, C-SHAPES classification bullet: 'A GICS sector never stands in for a sub-asset class'.",
        "Same PRD, PATHS: 'data/etfs/scripts/gold/etf_positioning_gold.py (the vocabulary)' is read, never edited.",
        "data/etfs/scripts/gold/etf_positioning_gold.py:150 `SUB_ASSET_CLASS_VOCAB = GICS_SECTORS + (CASH_SUB_ASSET_CLASS, ULTRA_SHORT_SUB_ASSET_CLASS)`; :158-160 comment 'sub_asset_class THE SERVED ALLOCATION AXIS. Deliberately MIXED-SOURCE -- the 11 GICS sectors PLUS ...'.",
        "data/etfs/scripts/gold/etf_positioning_gold.py:986-1010 classify(): a non-cash row with GICS sector in GICS_SECTORS returns (ASSET_CLASS_EQUITY, <the GICS sector>) as its sub_asset_class."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.2 C-SHAPES: canonical_shape carries Opal asset_class/sub_asset_class and the GICS hierarchy as separate fields, and a GICS sector never stands in for a sub-asset class; the vocabulary is etf_positioning_gold.py.",
    "world_is": "The named vocabulary's equity sub_asset_class values ARE the 11 GICS sector names, by a ratified design (1.0.0_SA_CTO~Z msg 11384); reusing it puts a GICS sector in sub_asset_class for every classified equity.",
    "notes": "Does NOT block round 1: the BASG thread has no GICS source (GICS is Bloomberg enrichment under R-21), so round 1 carries equity sub_asset_class as null with status UNRESOLVED and no GICS value, which satisfies both readings. It binds the enrichment round that lands GICS. Two readings, the CTO's to pick: (a) the PRD line means the GICS FIELD is never copied into sub_asset_class without the vocabulary's mapping, and the vocabulary's sector-valued sub-asset classes stand; (b) rivalfunds needs its own equity sub-asset vocabulary distinct from GICS, which is a new schema act with its Rule 24 record."
  },
  {
    "id": "ETFS_RIVALS-Z-W2-S1",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~2",
    "surfaced_at": "2026-09-30T08:00Z",
    "one_line": "The order's status flip to complete is outside this worker's <paths>, so the TO file's <status> stays pending for the issuer to flip.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Worker standing rules: flip the task order's <status> to complete once the proof instance is valid and every mechanical criterion passes.",
    "world_is": "<paths> in the worker face lists no task-order file (the write grant is the six product paths, the channel file and my deliverables folder), and the lane gate admits exactly those paths; the TO at task-orders/ETFS_RIVALS.TO-RIV-w-1.gateway-routes-and-read-grant.md line 155 reads <status>pending</status>.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/task-orders/ETFS_RIVALS.TO-RIV-w-1.gateway-routes-and-read-grant.md:155 <status>pending</status>",
        "proof-of-spec-check rc=0 on the instance under deliverables/0.9.0_WK_ETFS_RIVALS~2/, AC1-AC3 PASS"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Criteria are met and the instance is VALID; the flip is the issuer's at the merge."
  },
  {
    "id": "ETFS_RIVALS-Z-W1-S1",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~1",
    "surfaced_at": "2026-09-30T07:58Z",
    "one_line": "The cell says daily mode fetches T-1 = prev_trading_day(today ET) while the event contract and check c-1.AC1 pass event date = T-1, so the meaning of event 'date' in daily mode is under-specified.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/collector_issuer.py handler_entry/_days_for (this worker's branch wk-ETFS_RIVALS-1)",
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/c-1.AC1.py: d = prev_trading_day(today ET); ev date = d"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-c-1 cell: `daily`: fetch BASG's file for T-1, prev_trading_day(<today in America/New_York>); stage entry contract: event {\"date\": \"YYYY-MM-DD\", \"mode\": ...}, markers at date=<D>.",
    "world_is": "collector_issuer.handler_entry in daily mode computes the requested day itself (T-1 from the ET clock) and uses event['date'] only as the marker partition (default: the requested day); a daily event whose date differs from T-1 records a detail note and still fetches T-1. Check c-1.AC1 passes date = T-1, so both readings satisfy it.",
    "notes": "Downstream cells (RIV-d-1 daily Lambda, RIV-s-1 silver marker lookup) must agree on which date the daily trigger passes and which partition the fetch-holdings marker sits under; the issuer or CTO may want one sentence in the decomposition."
  },
  {
    "id": "ETFS_RIVALS-Z-W1-S2",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~1",
    "surfaced_at": "2026-09-30T07:58Z",
    "one_line": "Raw and sidecar object keys are basg-<ts>-<sha[:12]>, so the same bytes captured in the same second for two requested dates share one key and the later sidecar overwrites the earlier.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/collector_issuer.py land_bronze stem construction",
        "c-1.AC2 run: ok and mismatch bronze_uri are the same key"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-c-1 cell: raw lands at basg-<ts>-<sha256[:12]>.txt with a JSON sidecar beside it carrying requested_date and status, one file per day in backfill.",
    "world_is": "The key carries no requested date, so land_bronze of identical bytes with identical captured_at and different requested_date (check c-1.AC2 does exactly this: OK arm then DATE-MISMATCH arm) writes the same raw key and the same sidecar key; the last sidecar wins on the object store. The returned dict per call is correct; only the stored sidecar of the earlier call is lost.",
    "notes": "INERT in round 1: a real backfill fetches one distinct URL per day so distinct bytes and timestamps normally differ; it only bites when the issuer serves one stale file for several requested days inside one second. The key format is the cell's; left as specified."
  },
  {
    "id": "ETFS_RIVALS-Z-W3-S1",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~3",
    "surfaced_at": "2026-09-30T08:06Z",
    "one_line": "The Lambda package the cell names (five sources) cannot resolve address() or grade() on its own: lib/opal_naming.py reads org/standards/NAMING_SCHEMA.json at run time, which the cell's staging list omits.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lib/opal_naming.py:52 SCHEMA_PATH; :1080 _schema(); :1708 key() reads _schema()['key']['tier'].",
        "infra/aws/lambda/etfs-pipeline/rivalfunds_package.py STAGED tuple carries org/standards/NAMING_SCHEMA.json as a sixth source; data/etfs/scripts/rivalfunds/tests/test_d1_sweep.py::test_the_staged_lambda_tree_resolves_builder_addresses_on_its_own runs address() from each staged tree with nothing of the repo on sys.path (passes)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-d-1 cell text: rivalfunds_package.py stages data/etfs/scripts/rivalfunds/, lib/opal_naming.py, lib/trading_calendar.py, lib/research/identity/ and infra/logic/registry/ into the build directory.",
    "world_is": "lib/opal_naming.py:52 SCHEMA_PATH = <repo>/org/standards/NAMING_SCHEMA.json, read by _schema() (:1080) inside key() (:1708) and grade(); a staged tree without that file cannot call address(), so every stage would fail at its first location.",
    "notes": "Handled inside the cell (a sixth staged source, one file, read-only copy into the gitignored build directory); nothing outside the cell's paths was edited. Filed because the staging list in the cell text is not the whole set opal_naming needs; any other packager that stages lib/opal_naming.py on the same list inherits the gap."
  },
  {
    "id": "ETFS_RIVALS-Z-W3-S2",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~3",
    "surfaced_at": "2026-09-30T08:06Z",
    "one_line": "A Lambda invoked by EventBridge or Scheduler receives an S3 Object Created event or a scheduler input, not the stage entry contract event, so the wrappers need one normaliser beyond 'one import and one call'; the gold Lambda runs two stage modules.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/etfs-pipeline/*/lambda_function.py (five wrappers); data/etfs/scripts/rivalfunds/sweep.py trigger_event().",
        "data/etfs/scripts/rivalfunds/tests/test_d1_sweep.py trigger_event tests (scheduler input, S3 marker key, contract passthrough) pass."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-d-1 cell text: wrappers wrap one stage's handler_entry, one import and one call each; the stage entry contract is {date, mode, batch_id, sink}.",
    "world_is": "The marker rules deliver {'detail-type': 'Object Created', 'detail': {'object': {'key': ...}}} and the schedules deliver their own JSON input; neither carries the contract event. data/etfs/scripts/rivalfunds/sweep.py trigger_event() derives date and batch_id from the marker key (or cuts the scheduler's <aws.scheduler.scheduled-time> to a date); four of the five wrappers import trigger_event beside their stage module, and rivalfunds-build-canonical-shape-lambda imports both gold modules and runs canonical_shape then trade_schedule.",
    "notes": "The normaliser lives in sweep.py (inside the cell's paths) so no stage cell needs to know about EventBridge. The gold Lambda runs both gold stages in one invocation because the decomposition puts both in one Lambda and gives one trigger to it; the trade_schedule stage runs only when canonical_shape wrote its marker."
  },
  {
    "id": "ETFS_RIVALS-Z-W3-S3",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~3",
    "surfaced_at": "2026-09-30T08:06Z",
    "one_line": "The sweep Lambda runs every stage in process, so its role is the union of all five stages' grants; and the builder prefixes counted are ten (five data, five state), not the eight the cell text names.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/etfs-rivalfunds/gen_policies.py spec(); infra/aws/terraform/etfs-rivalfunds/policies/*.json (five files).",
        "d-1.AC3.py: IAM simulate_custom_policy finds no PutObject outside the builder prefixes and no DeleteObject for any of the five policies (AC3 PASS)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-d-1 cell text: one IAM role per Lambda with Put/Get only under the eight builder prefixes it needs, and Get on opal-data-harvest/crosswalk/v1/* for the build stage.",
    "world_is": "gen_policies.py derives, from address(): bronze holdings, silver holdings, gold canonical_shape, gold trade_schedule, platinum page, plus one state prefix per stage (five) = ten prefixes on opal-data-etfs; the sweep's handler_entry binds the real stage modules, so its policy is the union (Put/Get on all ten, Get on the crosswalk); the crosswalk Get is granted to the build-canonical-shape and sweep roles only.",
    "notes": "The face's 'eight' is not derivable from the builder set (it depends on whether the five state prefixes count as one); the count printed here is the generated one. 'The build stage' was read as the gold canonical_shape stage, the only one that resolves identity; if build-silver reads the crosswalk the grant is one line in gen_policies.py and a regeneration."
  },
  {
    "id": "ETFS_RIVALS-Z-W3-S4",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~3",
    "surfaced_at": "2026-09-30T08:06Z",
    "one_line": "A stage the sweep completes writes a marker that the EventBridge rule for the next stage also sees, so that next stage can run twice for one batch (once in the sweep, once from the rule); both are idempotent on batch_id only if the stage cells are.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/etfs-rivalfunds/triggers.tf aws_cloudwatch_event_rule.marker (no filter on the writer); data/etfs/scripts/rivalfunds/sweep.py run_sweep (in-process runners).",
        "RIV-s-1 AC2 / RIV-p-1 AC3 check second-run idempotence of the silver and page stages on the same batch; the gold stages carry the same expectation in their own checks."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-d-1 cell text: EventBridge rules on Object Created under each stage's state prefix invoke the next stage, and the sweep runs any stage missing its output marker; idempotent.",
    "world_is": "Both paths stay armed by design (C-TRIGGERS): the rule fires on every marker put, including one written by the sweep's own in-process run. The sweep is at 09:00 ET, two hours after the 07:00 fetch, so an overlap arises only when the chain stalled and the sweep repairs it.",
    "notes": "Recorded, not resolved: it binds RIV-d-2's live fire. If a stage cell's second run on one batch is not byte-idempotent, the sweep and the rule race; the disarm is either a writer filter on the rule or the stage's own guard, the CTO's or the stage cell's."
  },
  {
    "id": "ETFS_RIVALS-Z-W3-S5",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~3",
    "surfaced_at": "2026-09-30T08:22Z",
    "one_line": "The ruled stage names (fetch-holdings, build-silver, ...) used as the state-tier TABLE make hyphenated S3 keys that the ENFORCE naming gate grades OUT-OF-PATTERN (canonical snake_case), so the six generated files that carry those prefixes cannot be committed.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md rulings: address('rivalfunds','etfs','state','<stage>','date=<D>') with stage names fetch-holdings, build-silver, build-canonical-shape, build-trade-schedule, publish-page; the round-1 checks (d-1.AC2.py) pass those hyphenated names to markers.write_marker.",
        "bash .tools/safe-commit.sh on this cell: 'BLOCKED -- the naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode)'; NAMING REFUSE rivalfunds/etfs/state/build-silver/ -> rivalfunds/etfs/state/build_silver/, why: NEW and OUT-OF-PATTERN as S3Key: REFUSE (15 lines across generated.auto.tfvars.json and the five policies/*.json, which carry the resolved state prefixes).",
        "lib/opal_naming.py address() (line 1713) accepts the hyphenated table and returns s3://opal-data-etfs/rivalfunds/etfs/state/build-silver/date=...; only the gate's grade() refuses the same string, so the builder and the grader disagree."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-d-1 cell text and the decomposition's rulings: every location is address() output with the stage name as the state table; committed generated files (generated.auto.tfvars.json and policies/<lambda-name>.json) are the stack's inputs (rule 30).",
    "world_is": "address() output for a hyphenated state table is a NEW out-of-pattern S3Key to the commit-time naming gate in ENFORCE mode, so the six generated files (infra/aws/terraform/etfs-rivalfunds/generated.auto.tfvars.json and policies/*.json) are NOT in this commit; they are present and untracked in worktree C:/tmp/wk-rivals-3 and are reproduced byte for byte by `python infra/aws/terraform/etfs-rivalfunds/gen_policies.py --out infra/aws/terraform/etfs-rivalfunds`. AC1 and AC3 pass in the worktree with them present and fail on a tree without them until they land.",
    "notes": "Not worked around: no wildcard grant, no renamed table, no split token. The remedy is the issuer's or the CTO's and is one of: (a) rename the state-tier tables to snake_case (fetch_holdings, ...) in RIV-c-1's homes.py marker mapping and in gen_policies.py `_state_table()` (the one seam, a one-line change here), keeping the stage names hyphenated everywhere else (Lambda names, markers API arguments, AC2); (b) a registry or gate ruling that admits hyphenated state tables. Under either, the generated files are then committed by one regeneration. The same refusal will reach any other file that carries a resolved state prefix (RIV-d-2's apply evidence, RIV-p-1 if it types one). Also fixed inside this cell, not a row: gen_policies.py typed the etfs token in seven places the gate reads as hand-kept carriers; it now reads it through lookup('etfs') and inline name()/address() arguments."
  },
  {
    "id": "ETFS_RIVALS-Z-W1-S3",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~1",
    "surfaced_at": "2026-09-30T08:20Z",
    "one_line": "Check s-1.AC2 cannot pass from RIV-s-1's paths: its DATE-MISMATCH arm lands the same bytes with the same captured_at as the last real file, which is the S2 bronze key collision, so the last real file's OK sidecar is overwritten and its rows are (correctly) skipped by silver.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round1/checks/s-1.AC2.py: c.land(files) then land_bronze(raw=files[-1].read_bytes(), requested_date='2099-01-02', captured_at=meta['at']) -- same bytes, same captured_at as files[-1]",
        "data/etfs/scripts/rivalfunds/collector_issuer.py land_bronze: stem = basg-<ts>-<sha12>, no requested date (row ETFS_RIVALS-Z-W1-S2)",
        "probe run 2026-09-30: land_bronze OK arm then DATE-MISMATCH arm -> sidecar_uri equal True; the stored sidecar reads status DATE-MISMATCH, requested_date 2099-01-02",
        "s-1.AC2 run on silver_issuer.py: 'FAIL: first replay: 356 rows == 533 source rows' (356 = 2 x 178; the missing 177 are files[-1]); second replay adds no rows OK; no silver partition for the mismatched date OK; detail.skipped_not_ok == 1 OK"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-s-1 AC2 expects, after landing 3 real days plus one DATE-MISMATCH object, 533 silver rows (all 3 real files) and skipped_not_ok == 1; RIV-c-1 says the object key is basg-<ts>-<sha256[:12]>.",
    "world_is": "With that key, the DATE-MISMATCH landing and the last real file are ONE object pair; the sidecar that survives is the mismatch, so exactly one bronze object exists and it is not OK. silver_issuer skips it as the cell requires (sidecar status decides), giving 356 rows and skipped_not_ok 1. Both expectations cannot hold at once: 533 rows needs the OK sidecar, skipped_not_ok == 1 needs a second, non-OK object.",
    "notes": "Not fixable inside RIV-s-1: silver may not re-date or re-classify a bronze object against its sidecar (C-SHAPES), and collector_issuer.py is RIV-c-1's file (outside this order's paths). Two fixes, the issuer's or CTO's to pick: (a) the bronze stem carries the requested date (basg-<requested>-<ts>-<sha12>), which also closes row ETFS_RIVALS-Z-W1-S2; (b) check s-1.AC2 passes a different captured_at to its mismatch land. AC1 is unaffected and passes."
  },
  {
    "id": "ETFS_RIVALS-Z-W1-S4",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~1",
    "surfaced_at": "2026-09-30T09:10Z",
    "one_line": "The crosswalk resolves none of the issuer's plain identifiers: all 35 BASG positions (34 equities) land UNRESOLVED on real days, though the crosswalk holds MSFT under 'MSFT US'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "g-1.AC1 run 2026-09-30 on gold_canonical_shape.py: '2026-09-28: rows 35 resolved 0 unresolved 35' (same 0/35 on 09-24 and 09-25)",
        "crosswalk.load_crosswalk() pool object s3://opal-data-harvest/crosswalk/v1/2026-09-29.json: 237 records, all MEASURED, 1044 index forms; forms are Bloomberg-style (display_ticker 'ASML NA', 'ADBE US')",
        "probe: resolve('MSFT')=UNRESOLVED, resolve('MSFT US')=MEASURED, resolve('MSFT US Equity')=MEASURED, resolve('594918104')/('US5949181045')/('2588173') (MSFT CUSIP/ISIN/SEDOL) = UNRESOLVED"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-g-1: identity through lib/research/identity/crosswalk.resolve() tried on CUSIP, then ISIN, then SEDOL, then ticker; a miss keeps the position UNRESOLVED with the raw identifier, never a guessed key.",
    "world_is": "The crosswalk indexes only Bloomberg-form identifiers (ticker plus exchange code, and that form plus ' Equity'); it holds no CUSIP, ISIN or SEDOL forms and a bare issuer ticker never matches. So the four tried forms miss for every BASG position and the gold shape has security_id null throughout. The cell follows its spec (no suffix appended, no guessed key), so nothing is wrong in gold; the identity join is empty until a crosswalk carries CUSIP/ISIN/SEDOL forms or an exchange-aware adapter is authorised.",
    "notes": "Not fixable inside RIV-g-1: appending ' US' would be the guessed key the cell forbids, and the crosswalk is not in this order's paths. The trade_schedule and page cells key on security_id at their peril: on real BASG data they see 0 resolved securities and must fall back to raw_identifier."
  },
  {
    "id": "ETFS_RIVALS-Z-W1-S5",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_ETFS_RIVALS~1",
    "surfaced_at": "2026-09-30T09:35Z",
    "one_line": "RIV-p-1: a page whose guardrail fails returns status PARTIAL with no batch marker (the contract names no status for a published not-updated page), and identity_coverage's resolved-fraction floor is 0.0 because the crosswalk resolves 0 of 35.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/publish_page.py handler_entry: failed checks -> out('PARTIAL', [index, manifest], None, detail) and write_marker only on OK",
        "data/etfs/scripts/rivalfunds/guardrails_config.json: min_resolved_fraction 0.0 PROVISIONAL; min_identified_fraction 0.9 PROVISIONAL",
        "p-1.AC1 run 2026-09-30: identity_coverage PASS '34 of 34 non-cash lines identified (min 0.9); 0 of 34 resolved by the crosswalk (min 0.0)'; p-1.AC2 run: planted completeness returns status PARTIAL, marker None, page not-updated"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RIV-p-1: a failed check publishes the page with BASG data-status=not-updated; the stage contract returns status OK|PARTIAL|FAILED|SKIPPED and writes a batch marker only when its batch is whole; identity coverage is one of the six checks with PROVISIONAL thresholds.",
    "world_is": "The order and the contract name no status or marker rule for a stage that publishes a deliberately not-updated page, and no identity threshold that a 0-of-35 crosswalk can meet. The cell chose PARTIAL with no marker (a rerun of the same batch re-evaluates, and a wrapper reading the status sees the day was not fully published) and graded identity on 'has a resolved id or a raw identifier' (>= 0.9) with a 0.0 resolved floor, so the round-1 real days pass while the crosswalk is empty (row ETFS_RIVALS-Z-W1-S4).",
    "notes": "RIV-d-1 (Lambda wrapper) and RIV-d-2 (fire) read the stage status: PARTIAL here means the page IS published as not-updated, not that nothing was written. The real thresholds, including a resolved floor above 0.0 once the crosswalk carries CUSIP/ISIN/SEDOL forms, belong to the named enrichment cell."
  }
]
```
