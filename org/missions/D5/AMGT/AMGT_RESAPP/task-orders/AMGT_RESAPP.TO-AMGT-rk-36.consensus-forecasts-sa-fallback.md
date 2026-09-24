# AMGT_RESAPP task order -- `AMGT-rk-36` -- forecasts FY1-FY3 from Bloomberg `BEST_` with the explicit override, the Seeking Alpha fallback per cell, source and fiscal year on every cell, headers from `BEST_PERIOD_END_DATE`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-36</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~39</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the forecast refresh
  cadence stays Andrew's (C-MODEL-FORECASTS, last sentence); no scheduled Seeking Alpha or Bloomberg read is created;
  the standing collection-stays-off / no-monitor moratorium is unaffected.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to already-provisioned prefixes (`raw/bloomberg/`,
  `raw/seekingalpha/`, `derived/model_block/` in `opal-data-harvest`) under credentials the two producers already run
  with on this box, and redeploys the existing Lambda `opal-amgt-scoped-api` through the existing Terraform
  resource `module.scoped_amgt_api.aws_lambda_function.this` with NO change to its role, policies, layers, memory,
  timeout or environment; it grants no permission and provisions no resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~39`, continuing CHAIN M's queue in the SAME worktree: `AMGT-rk-35` (done),
`AMGT-rk-36` (this one), `AMGT-rk-37` (next).** Your first act on this order prints `git rev-parse --short=10 HEAD` and
confirms `AMGT-rk-35`'s `<status>` reads `complete` and its change-management entry reads CLOSED; if either is false,
STOP with a row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~39;`. **NEVER RUN AN INSTALL.**
**Bloomberg, ANY scenario: READ `integrations/bloomberg/READ_HERE.md` FIRST.** This order's Bloomberg budget is FIVE
requests per validation name (the two of rk-35's pull plus THREE `ReferenceDataRequest`s with the override), fifteen in
all, on the three validation names and NOTHING for any covered name. **This order also makes Seeking Alpha reads on the
three validation names** -- authorized by name (section 1) -- through `integrations/seekingalpha/rest_fetch.py`'s parked
session, GET only, never a sign-in, never a re-harvest.

## 1. THE CELL, inlined in full -- `AMGT-rk-36` (R14-M3; FWD-1, FWD-16; Model brief M3, M4; Andrew's card 1 of the six)

**The analysis row, verbatim** (`ledger/ROUND_ANALYSIS.round13.md` s.4 @`9c8e04cd9a`, chain M, `R14-M2 -> M3 -> M4`):
*"... M3 forecasts FY1-FY3 from Bloomberg `BEST_` with the explicit override, SA fallback per cell, source and fiscal
year on every cell, headers from `BEST_PERIOD_END_DATE`; ..."* -- serves FWD-1, FWD-16, M2-M5, L8; co-sign **yes,
each**.

**The measured state** (Model brief @`f48864fce6` s.2 :83-108; intake rows M3, M4): no estimate field is pulled
(`HIST_FIELDS` `model_block_pull.py:78-98` and `HEADER_FIELDS` `:57-73` carry no `BEST_` mnemonic); the CRO measured
Bloomberg consensus over the 33 with ONE `ReferenceDataRequest` per fiscal year and an EXPLICIT `BEST_FPERIOD_OVERRIDE`
of `1FY` / `2FY` / `3FY`: `BEST_EPS` 33/33/33, `BEST_SALES` 33/33/32, `BEST_EBITDA` 31/31/31, `BEST_PE_RATIO`
31/32/32, `BEST_DPS` 33/33/33, `BEST_PERIOD_END_DATE` 33/33/33; control Boeing FY2026-28 EPS -0.83 / 3.95 / 8.05 with
period ends 2026-12-31 / 2027-12-31 / 2028-12-31. **Two instrument traps, both measured (brief s.7):** a `BEST_` field
WITHOUT the override returns the next QUARTER, which reads as a plausible annual value; and a Bloomberg id without its
yellow key returned 33 of 33 security errors. The estate client supports overrides:
`integrations/bloomberg/mcp/blp_client.py` `reference_data(securities, fields, overrides=None, ...)` `:135-140`, applied
at `:158-163`; a bad or unentitled field surfaces under `__field_errors__` `:201-221`, never as silence.

**The PRD constraints this cell serves** (PRD v0.13 @`1699960261`):
- `C-MODEL-FORECASTS` (`:861-870`), verbatim in its load-bearing sentences: *"The Model carries forecast years FY1-FY3
  beside the history. **Bloomberg is primary**: the `BEST_` consensus fields (`BEST_EPS`, `BEST_SALES`, `BEST_EBITDA`,
  `BEST_PE_RATIO`, `BEST_DPS`), each pulled with an EXPLICIT `BEST_FPERIOD_OVERRIDE` per year ... **Seeking Alpha fills
  a cell only where Bloomberg has none.** Every cell carries its fiscal year and `source` = `BBG` | `SA_FALLBACK`.
  Column headers come from `BEST_PERIOD_END_DATE`, never from a counted offset. The page labels the columns CONSENSUS,
  never reported. **The SA fallback is a Seeking Alpha production read, AUTHORIZED for this path by name** (v0.12,
  Andrew-direct ~19:4xZ, *"Yes use SA thats fine"*); `C-SA-TERMS-BEFORE-SCHEDULE` is satisfied for it (v0.13, *"I have
  already clarified SA ToS, we are good"*). The refresh cadence is Andrew's."*
- `C-SA-VENDOR-WORD` (`:1098-1112`): LIFTED BY NAME (`:1108`) for exactly two paths, `C-PEER-SET-SA` and the
  `SA_FALLBACK` cells of `C-MODEL-FORECASTS`, at instantiation and in validation; TERMS CLEARED (`:1109`). Every OTHER
  Seeking Alpha route stays NOT AUTHORIZED -- this order reads the estimates endpoint for the fallback cells and nothing
  else (no articles, no news, no report, no peers).
- `C-VALIDATION-NAMES` (`:1652-1658`): proven on Caterpillar / CSL / Keyence; *"Seeking Alpha on the two paths
  `C-SA-VENDOR-WORD` names as lifted"* is inside the validation; no fleet run, no re-run of the 33.
- `C-MODEL-WINDOW-AND-ROWS` (4) (`:872-885`): every Bloomberg call names `<RESOLVED bloomberg id> Equity` or reads the
  block's own security string. `C-RAW-BEFORE-DERIVED` (`:899-901`), `C-BLOOMBERG-BASIS` (`:891-895`),
  `C-UNIT-MAP-MEASURED` (`:848-859`): the `BEST_` figures carry a MEASURED unit like every other figure.
- The value-carries-its-claim rule (CLAUDE.md s.4): every forecast cell carries `source`, its fiscal year, its period
  end date, `estimate_basis: "consensus"`, and -- for a fallback -- the SA field it came from.

**RULED -- what you build:**

1. **The pull** (`integrations/bloomberg/research/model_block_pull.py`, `stage_pull` `:217-253` as rk-35 left it):
   after the header and history requests, THREE `reference_data([security], FORECAST_FIELDS + ["BEST_PERIOD_END_DATE"],
   overrides={"BEST_FPERIOD_OVERRIDE": fp})` calls, `fp` in `("1FY", "2FY", "3FY")`, with
   `FORECAST_FIELDS = ["BEST_EPS", "BEST_SALES", "BEST_EBITDA", "BEST_PE_RATIO", "BEST_DPS"]` (the PRD's five, in that
   order). The three responses land UNTOUCHED, exactly as the client returns them, as ONE object
   `raw/bloomberg/<key>/<stamp>/bestdata.json` = `{"1FY": <response>, "2FY": <response>, "3FY": <response>,
   "requests": [<each request's fields and overrides>]}` in the SAME stamp prefix as `refdata.json` / `histdata.json`
   (`:242-245`), before anything derives from it. The pull record (`:230-240`) gains the three requests with their
   overrides. A dry run prints them and writes nothing.
2. **The derive** (`stage_derive` `:369-461`): reads `bestdata.json` back from S3 for the raw stamp it is deriving; if
   the stamp carries none (every covered name's 2026-09-16 landing), the block gets `forecast_figures: []` -- expressed
   as zero figures of the new scope plus ONE `unresolved` record `{"scope": "forecast", "reason": "raw stamp <s>
   carries no bestdata.json (pulled before C-MODEL-FORECASTS)"}`. Otherwise, per period and per field, ONE figure:
   `{"scope": "forecast", "fiscal_period": "FY1"|"FY2"|"FY3", "override": "1FY"|..., "period_end_date": <BEST_PERIOD_END_DATE
   for that period>, "fiscal_year": <the year of that date -- Bloomberg names a fiscal year by its end year, so a March
   2027 period end is FY2027>, "mnemonic": ..., "value": ..., "unit": <from the map>, "sign": ..., "basis": {...},
   "vintage": ..., "source": "BBG", "estimate_basis": "consensus"}`. **THE HEADER IS THE DATE, NEVER AN OFFSET:** a period
   whose `BEST_PERIOD_END_DATE` is missing yields NO figures for that period, only `unresolved` records naming it.
   **THE QUARTER-TRAP GUARD:** the three period end dates must be at least 300 days apart in sequence and each later
   than the block's `latest_closed_fiscal_year`'s end; a set that fails is REFUSED as a whole (`unresolved` reason
   `"period end dates not annual: BEST_FPERIOD_OVERRIDE not honoured"`) and no forecast figure is written -- a
   plausible quarterly number never reaches the block as a year.
3. **The scope contract** (`lib/research/checkface/scopes.py:33-41`): add `SCOPE_FORECAST = "forecast"` to
   `MODEL_BLOCK_SCOPES`. The contract test `lib/research/api/tests/test_fiscal_scope_contract.py` parses the producer's
   source for its `"scope": "..."` literals and asserts equality with that set in both directions -- both files move
   together or the test fails; run it (AC4). Its pinned BABA counts (`:35-37`) do not move: BABA is not re-derived here.
4. **Units for the five `BEST_` mnemonics** join `AMGT-rk-34`'s builder families (`integrations/bloomberg/research/build_unit_map.py`):
   `BEST_EPS`, `BEST_DPS` per-share; `BEST_SALES`, `BEST_EBITDA` financial-statement scale (millions vs absolute,
   measured by magnitude as the builder already does); `BEST_PE_RATIO` ratio; `BEST_PERIOD_END_DATE` is a DATE, not
   a figure, and never enters `figures`. Basis text (`FIELD_BASIS` `:107-144`) for each: Bloomberg's consensus
   estimate (BEST) of the named quantity for the overridden fiscal period -- consensus, never reported.
5. **The Seeking Alpha fallback**, a new module beside the producer `integrations/bloomberg/research/sa_forecast_fallback.py`,
   called by the derive ONLY for the (period, field) cells Bloomberg left empty (`gaps`). It loads
   `integrations/seekingalpha/rest_fetch.py` by path (as `_load_blp_client` `:147-156` loads the Bloomberg client) and
   rides its measured contract unchanged: `load_config()` (`:84-86`; `config.json`: vendor `seekingalpha`,
   `store_bucket` `opal-data-harvest`, `pace_seconds` 2.0, `max_tickers_per_run` 3), `build_session()` (`:98-143`, the
   PARKED session, Chrome impersonation, residential proxy -- the module never signs in), `_do_get()` (`:153-204`,
   per-ticker Referer, full logging, `detectors.classify`), `land_raw()` (`:211-218`, raw bytes at
   `raw/seekingalpha/<security_key>/<stamp>/<endpoint>.json`, C-RAW-BEFORE-DERIVED). Every request is a GET.
   **The sequence per security with gaps:**
   (a) **candidate SA symbols**: the crosswalk record's `sa_symbol` if `R14-P1` has landed one (read, never required),
   else the Bloomberg root ticker (first token of the security string: `CAT`; a NUMERIC root such as `6861` is not
   an SA symbol -> no candidate); no candidate -> `fallback_status: "UNRESOLVED: no SA symbol candidate"`, cells stay
   ABSENT, nothing fetched;
   (b) **the entity test, BEFORE any metric is read**: `GET /api/v3/symbols/{candidate}` (`rest_fetch.py:22`, `:274-298`),
   then a folded-token name agreement between SA's company name and the block's own `NAME` header (the same class of
   test as `org/tier1_exec/4.0.0_SA_CRO/scripts/sa_symbol_resolve_pass.py:108 name_matches`, written INTO this module
   -- production never imports a seat's script). **`ROG` = Rogers Corporation against Roche is the standing negative
   control** (Peers brief P5; analysis s.4 R14-P1): a candidate failing the test is `fallback_status: "UNRESOLVED:
   entity test refused <sa name> for <block NAME>"` and NOTHING from it is used -- never the first hit;
   (c) **the metrics read**: `GET /api/v3/metrics?filter[fields]=<fields>&filter[slugs]=<slug>` (Peers brief
   @`a2fdbad164` s.2 :67, measured; one value per field with a `meaningful` flag). **The only SA estimate fields
   MEASURED so far are `pe_nongaap_fy1` / `_fy2` / `_fy3`** (Peers brief :90, the FY P/E); the SA field names for
   EPS, revenue, EBITDA and DPS FY1-FY3 are UNMEASURED -- you MEASURE candidates on Caterpillar first (one metrics
   call naming your candidate fields; a field SA does not carry comes back absent) and record, per `BEST_` mnemonic,
   the SA field adopted or `NOT-MAPPABLE` with the candidates tried. Raw landed (`land_raw`, endpoint name
   `metrics`) before any cell is filled;
   (d) **the fill**: a gap cell is filled ONLY when SA carries the mapped field for that period with `meaningful` true;
   the figure is written exactly as (2) with `source: "SA_FALLBACK"`, `sa_field`, `sa_symbol`, `sa_raw_key`, and its
   fiscal year from Bloomberg's `BEST_PERIOD_END_DATE` for that period (SA's FY1 is joined to Bloomberg's FY1 by
   period ORDER and the join is recorded; if Bloomberg had no period end date the cell stays ABSENT -- no header, no
   cell). A gap SA cannot fill stays ABSENT with `fallback_status: "ATTEMPTED-NO-VALUE: <sa field absent | meaningful
   false>"`. A `not meaningful` value is NEVER filled (a bank's EBITDA, a loss-maker's P/E -- brief s.7);
   (e) **session health is a STOP**: a `REHARVEST` classification stops the fallback for the run (`ReHarvestNeeded`),
   every remaining gap gets `fallback_status: "STOPPED: REHARVEST"`, the run continues WITHOUT SA, and you file a
   row; a `TRANSPORT_ERROR` is recorded as such, never as "SA has no value".
   The block records the whole attempt under `forecast_fallback: {sa_symbol_candidates, sa_symbol, entity_test,
   classification, gaps_before, filled_by_sa, sa_raw_key, reason}` so the record explains every cell.
6. **The adapter** (`lib/research/api/scoped_amgt.py`, `read_model()` `:2511-2535`): serve, beside `fiscal_year_figures`,
   `forecast_figures` (the `forecast`-scope figures via `_figures(model_block, SCOPE_FORECAST)`), `forecast_periods`
   (`[{fiscal_period, fiscal_year, period_end_date}]`, from the figures' own dates, in period order),
   `forecast_source_counts` (`{"BBG": n, "SA_FALLBACK": n, "ABSENT": n}` over 15 possible cells), and
   `forecast_reason` (the `unresolved` forecast reason when there are no figures -- every covered name until its next
   pull). `read_thesis_bundle()` (`:1939-1976`) includes the forecast figures in `check_face` (`:1965-1967`) so a forecast
   with an unmeasured unit REFUSES like any other figure. The `/thesis` payload is the one route that reaches the model
   block (`:2517-2519`); no route is added.
7. **NOT IN THIS CELL:** the PAGE (the CONSENSUS column label, the forecast columns on `ModelTab.tsx` / `modelSheet.ts`)
   -- the portal is frozen and not on this order's surface; the adapter carries `estimate_basis: "consensus"` on every
   cell so the page can label without guessing. The Base case (consensus EPS x trailing-median P/E) is `AMGT-rk-37`'s
   (C-MODEL-WINDOW-AND-ROWS (5)), which reads the `BEST_EPS` FY1 cell this order lands.
8. **The act, in order:** dry run (prints the three override requests per name); `pull` then `derive` on exactly
   `"CAT US Equity" "CSL AU Equity" "6861 JP Equity"` with the fallback enabled; the tests (AC4); the deploy (section 3).
   **The 33 covered names are NOT pulled and NOT re-derived** -- their served `forecast_figures` read `[]` with
   `forecast_reason` after the deploy, which is the honest state and is what AC5 asserts.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis s.4 chain M row `R14-M3` and s.5 card 3
@`9c8e04cd9a`, ANSWERED by Andrew ~19:4xZ (*"1.) Yes use SA thats fine"*, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_194xZ_AMGT_RESAPP_SIX_CARDS_ANSWERED.md`, frame card 1)
and ~20:0xZ (*"I have already clarified SA ToS, we are good"*, `ANDREW_DIRECT_20260918_20xxZ_AMGT_RESAPP_SA_TERMS_CLEARED.md`);
Model brief @`f48864fce6` s.2, s.5 item 3, s.6 "Forecasts", s.7; Peers brief @`a2fdbad164` s.2 (the SA instrument and
endpoints, :56-68, :90, :101-103, P5). PRD **v0.13 @`1699960261`** (`C-MODEL-FORECASTS` :861-870 with the v0.12 lift and
the v0.13 terms clearance; `C-SA-VENDOR-WORD` :1098-1112; `C-VALIDATION-NAMES` :1652-1658). Code cited @HEAD (draft-time
HEAD `8a788d2eaf`; `scoped_amgt.py` last touched `e2d89be7da`; rk-34 and rk-35 will have moved `model_block_pull.py`'s
line numbers -- re-read at spawn).

**ISSUER RULE -- ADAPTER SINGLE-WRITER QUEUE (`2.0.0_SA_COO~Z`, at the cut):** this order is one of the round-14 cells
that edit `lib/research/api/scoped_amgt.py` and/or redeploy `opal-amgt-scoped-api` (rk-36, rk-37, rk-43, rk-45, rk-53,
rk-61). The issuer spawns those cells ONE AT A TIME -- the next is cut from HEAD only after the previous has DRAINED --
so a worktree never carries adapter bytes behind the shared branch. Two obligations follow. (1) IMMEDIATELY BEFORE
`build-and-upload-scoped-amgt.sh`, run `git log --oneline $(git merge-base HEAD SITEZ)..SITEZ -- lib/research/api
lib/research/checkface infra/aws/lambda/research/scoped_amgt_api infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`
and paste its output into the change-management entry: it MUST print nothing; if it prints a commit, STOP -- do not
build, do not apply -- file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`) and report; a deploy from bytes behind the
shared branch would REWIND another cell's served change. (2) The rollback target is the pre-act `CodeSha256` and the
artifact `VersionId` YOU read immediately before the apply (never a value copied from another order), recorded in the
entry before the build runs. THE ROLLBACK MECHANISM, as RULED on `1.0.0_SA_CTO~Z`'s source read (msg 23830): the Terraform
module (`infra/aws/terraform/modules/yang-lambda/main.tf:17-20`, `:38`) declares `data "aws_s3_object" "artifact"` with
bucket and key only and ALWAYS resolves the CURRENT version, so a rollback NEVER edits the module and never names a
VersionId to Terraform. Rollback = restore the pre-act bytes as the current version -- `aws s3api copy-object --bucket
opal-313476888478-lambda-artifacts --key research/opal-amgt-scoped-api.zip --copy-source
"opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip?versionId=<pre-act VersionId>"` (bucket versioning
MEASURED `Enabled` by the issuer 2026-09-18 ~22:4xZ; RE-MEASURE it with `get-bucket-versioning` into the entry before the
build, and STOP if it reads anything else) -- then the SAME targeted `safe-apply`, and `get-function-configuration` must
print the pre-act `CodeSha256` again. Exercise nothing of this unless rolling back; record all of it before acting.

**ISSUER RULE -- WHERE THE NEVER-WIDEN PAIR LIVES (`2.0.0_SA_COO~Z`, at the cut):** this order is CO-SIGNED. The pair
for chain M is TWO ledger files, one section per cell: the COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_M_COO_HALVES.md` and the CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_M_CTO_HALVES.md`. "The pair is on file" MEANS: both
files exist in your worktree, each carries a section headed `AMGT-rk-36`, and that section names this order's blast radius
(the keys/prefixes and, for an adapter cell, the Lambda) and the per-key rollback. Read both before your first live act,
paste both files' sha256 into the change-management entry, and record every pre-act hash the halves tell you to measure
FRESH (never a value copied from another order). Either file absent or its `AMGT-rk-36` section missing: run the read-only and
dry-run criteria, file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half.

## 3. SURFACES -- what you may read and write

<paths>
integrations/bloomberg/research/
lib/research/api/scoped_amgt.py
lib/research/checkface/scopes.py
lib/research/api/tests/test_fiscal_scope_contract.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~39/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-36.consensus-forecasts-sa-fallback.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_M_*_HALVES.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (`rest_fetch.py`, `detectors.py`,
  `config.json`, `blp_client.py`, `run_checks.py`, the pool, the crosswalk, the two Andrew-direct records); this block
  governs WRITES. `integrations/seekingalpha/` is READ-ONLY to you: the fallback module lives beside the Bloomberg
  producer and loads `rest_fetch.py` by path. New tests go under `integrations/bloomberg/research/tests/` (inside the
  directory grant). Scratch is `<your worktree>/.scratch/` only. **Secrets through the module's own Secrets Manager
  read only (`rest_fetch.py:89-95`); no secret value is ever printed, logged, landed or committed; the HAR is not
  yours to read.**
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~39 <0.9.0_WK_AMGT_RESAPP~39@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Every `.py` edit passes `.tools/commit-gate.sh`. Never push, merge,
  rebase, `checkout --`, `stash` or `clean`.
- **THE DEPLOY -- served output moves, so this is co-signed.** Blast radius, stated so the pair can name it: the
  `/thesis` payload for ALL 33 keyed names gains `model.forecast_figures` (`[]`), `model.forecast_periods` (`[]`),
  `model.forecast_source_counts` and `model.forecast_reason` (the no-bestdata reason) -- shape only, no value changes
  for the 33 because none is re-pulled; `check_face` length for the 33 is UNCHANGED; the three validation names are
  unserved (not in the crosswalk). Writers of the Lambda's bytes: ONE (`infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`
  packaging THIS worktree). ROLLBACK, from the LIVE pre-act hash of THIS act: record `aws lambda
  get-function-configuration --function-name opal-amgt-scoped-api --query CodeSha256` and the artifact's S3 VersionId
  BEFORE the act; rollback re-points the Terraform resource at that VersionId (the exact precedent:
  `org/critical_paths/change_management/20260916T1606Z_amgt-scoped-api-rk2-rollback-20260916_deploy_completion.md`).
  **BEFORE YOU BUILD -- THE STALE-BYTES CHECK, NON-NEGOTIABLE:** the zip is built from YOUR worktree's bytes, and every
  other round-14 cell that redeploys this Lambda builds from ITS worktree; a deploy from a worktree behind the shared
  branch REVERTS whatever landed there. Print
  `git log --oneline $(git merge-base HEAD SITEZ)..SITEZ -- lib/research/api lib/research/checkface infra/aws/lambda/research/scoped_amgt_api infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`;
  if it is NON-EMPTY, STOP and file a row naming the commits (`2.0.0_SA_COO~Z` merges forward; you never merge). Only an
  EMPTY output licenses the build. Then: the halt gate's session file per the `AMGT-ri-2` order (`:22`), the
  change-management entry OPENED BEFORE the build:
  `python .tools/deploy_ledger.py open --slug amgt-rk36-forecasts-adapter-20260918 --title "AMGT-rk-36: forecasts FY1-FY3 (BEST_ + SA fallback) on the model block; read_model serves forecast_*; co-signed rk-36 pair" --author 0.9.0_WK_AMGT_RESAPP~39 --leg "L1|git|producer + fallback module + scopes + adapter committed|commit hash" --leg "L2|activation|module.scoped_amgt_api.aws_lambda_function.this redeployed|TF apply 0 destroy + 0-diff replan + deployed CodeSha256 == uploaded sha" --leg "L3|verify|13 of 13 GET routes 200 pre/post, LOST=[] GAINED=[]; AC5|census + AC5 output" --window-hours 4`
  with its sentinel COMMITTED; the build `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`; the apply
  in the EXACT form the rk-19 and rk-30 completion records name (`HALT_ACK=1`, `.tools/safe-apply.sh` with
  `-target=module.scoped_amgt_api.aws_lambda_function.this`; read
  `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~27/AMGT_RESAPP.TO-AMGT-rk-19.adapter-second-join.SESSION_LOG.md`
  `:43-65` for the byte-exact invocation) -- NEVER bare `terraform apply`, NEVER `aws lambda update-function-code`;
  the 13-route census pre and post (the rk-30 record's shape); CLOSE with every leg proven before your grading read.

## 4. BOUNDS

**BLOOMBERG:** fifteen requests, all on the three validation names, none on a covered name; the override is EXPLICIT
on every `BEST_` request (a request without it is a violation, not a shortcut). **SEEKING ALPHA:** GET only, the
`symbols` and `metrics` endpoints only, on the three validation names only, through the parked session only; a
`REHARVEST` or auth signal STOPS the fallback and is a row -- never a sign-in, never a browser, never a retry loop, never
`sa_harvest_session.py`; pace `config["pace_seconds"]`; no other SA endpoint (articles, news, report, peers) is called
by this order. **No other vendor call.** **PORTAL FROZEN** (not your surface; the page label is named for the COO in
section 1 item 7). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness checker.** No
Terraform change beyond the targeted apply of the existing resource; no IAM. No non-ASCII in anything you write. **PUSH:
never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name. A gap SA cannot fill is an HONEST cell, not a
failure; a filled cell from an entity-untested symbol IS a failure.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** (15 possible forecast cells per name:
3 periods x 5 fields).
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W39-S<k>`, `<k>` continuing from rk-35; `"project": "AMGT_RESAPP"` and `"fabric":
"site-z"`; textual splice, never re-serialize, never edit an existing row. **Found something off-task? APPEND ONE ROW AND
KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-36"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json, datetime
s3 = boto3.client('s3'); B = 'opal-data-harvest'; pg = s3.get_paginator('list_objects_v2')
F = ['BEST_EPS', 'BEST_SALES', 'BEST_EBITDA', 'BEST_PE_RATIO', 'BEST_DPS']
for k, sec in [('CAT_US_Equity', 'CAT US Equity'), ('CSL_AU_Equity', 'CSL AU Equity'), ('6861_JP_Equity', '6861 JP Equity')]:
    ks = sorted(o['Key'] for pp in pg.paginate(Bucket=B, Prefix='raw/bloomberg/' + k + '/') for o in pp.get('Contents', []) if o['Key'].endswith('/bestdata.json'))
    if not ks:
        print(k, 'NO_BESTDATA'); continue
    d = json.loads(s3.get_object(Bucket=B, Key=ks[-1])['Body'].read())
    reqs = d.get('requests') or []
    ovr = [r.get('overrides', {}).get('BEST_FPERIOD_OVERRIDE') for r in reqs]
    dates = []
    for fp in ['1FY', '2FY', '3FY']:
        row = (d.get(fp) or {}).get(sec) or {}
        ped = row.get('BEST_PERIOD_END_DATE'); dates.append(str(ped)[:10] if ped else None)
        print(k, fp, 'period_end', ped, 'fields_with_value', sum(1 for f in F if row.get(f) not in (None, '')), 'of', len(F), 'field_errors', sorted((row.get('__field_errors__') or {}).keys()), 'security_error', row.get('__error__'))
    ds = [datetime.date.fromisoformat(x) for x in dates if x]
    gaps = [(ds[i + 1] - ds[i]).days for i in range(len(ds) - 1)]
    print(k, 'raw', ks[-1], 'overrides_recorded', ovr, 'period_end_dates', dates, 'day_gaps', gaps, 'annual_spacing', len(ds) == 3 and all(g >= 300 for g in gaps))
"</invocation><expect>THE RAW LANDING WITH THE OVERRIDE, ON THE THREE VALIDATION NAMES: each has a bestdata.json in its newest raw stamp whose recorded requests carry overrides_recorded ['1FY', '2FY', '3FY'] (explicit, every request); each of the three periods returns a BEST_PERIOD_END_DATE with no security_error (the yellow-keyed string worked); day_gaps are all at least 300 and annual_spacing True -- THE DISCRIMINATOR against the measured quarter trap (a call without the override returns the next quarter and would print gaps of about 90); CAT's period ends fall on 12-31 of 2026/2027/2028 (December FYE, the same shape as the brief's Boeing control), CSL's on 06-30 and Keyence's on 03-31 of consecutive years; fields_with_value printed per period out of 5 with any field_errors named. A missing bestdata.json, a period with no end date, a gap under 300 days, or an unrecorded override is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-36"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json, sys
sys.path.insert(0, '.')
from lib.research.checkface.scopes import unknown_scopes, MODEL_BLOCK_SCOPES
s3 = boto3.client('s3'); B = 'opal-data-harvest'; pg = s3.get_paginator('list_objects_v2')
print('scopes_declared', sorted(MODEL_BLOCK_SCOPES))
for k in ['CAT_US_Equity', 'CSL_AU_Equity', '6861_JP_Equity']:
    ks = sorted(o['Key'] for pp in pg.paginate(Bucket=B, Prefix='derived/model_block/' + k + '/') for o in pp.get('Contents', []) if o['Key'].endswith('/model_block.json'))
    if not ks:
        print(k, 'NO_BLOCK'); continue
    b = json.loads(s3.get_object(Bucket=B, Key=ks[-1])['Body'].read())
    figs = b.get('figures') or []; fc = [f for f in figs if f.get('scope') == 'forecast']
    bad = [f for f in fc if not f.get('fiscal_year') or not f.get('period_end_date') or f.get('source') not in ('BBG', 'SA_FALLBACK') or f.get('estimate_basis') != 'consensus' or f.get('fiscal_period') not in ('FY1', 'FY2', 'FY3')]
    unres = [u for u in (b.get('unresolved') or []) if u.get('scope') == 'forecast']
    src = {}
    for f in fc: src[f['source']] = src.get(f['source'], 0) + 1
    print(k, 'block', ks[-1], 'forecast_figures', len(fc), 'of 15 possible', 'by_source', src, 'malformed', len(bad), 'unresolved_forecast', len(unres), 'unknown_scopes', sorted(unknown_scopes(figs)))
    print('  periods', sorted(set((f.get('fiscal_period'), f.get('fiscal_year'), str(f.get('period_end_date'))[:10]) for f in fc)))
    print('  absent_cells', [(u.get('fiscal_period'), u.get('mnemonic'), u.get('fallback_status'), u.get('reason')) for u in unres][:15])
    ff = b.get('forecast_fallback') or {}
    print('  forecast_fallback', json.dumps({x: ff.get(x) for x in ['sa_symbol_candidates', 'sa_symbol', 'entity_test', 'classification', 'gaps_before', 'filled_by_sa', 'sa_raw_key', 'reason']}, sort_keys=True))
"</invocation><expect>THE DERIVED FORECAST CELLS: scopes_declared includes forecast beside header and fiscal_year_line_item; on each of the three validation names forecast_figures is greater than 0 (at least one BBG cell per name -- the brief measured BEST_EPS and BEST_DPS on 33 of 33), malformed 0 (every cell carries fiscal_period, fiscal_year, period_end_date, source in {BBG, SA_FALLBACK}, estimate_basis consensus), forecast_figures + unresolved_forecast accounts for every one of the 15 possible cells (a cell is a figure or an unresolved record with a fallback_status -- never silently missing), unknown_scopes [] (the contract moved with the producer), and periods show three distinct fiscal years labelled from their own period end dates. The forecast_fallback record is printed for each name. A malformed cell, an unaccounted cell, or a non-empty unknown_scopes is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-36"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import importlib.util as u, boto3, json
s = u.spec_from_file_location('fb', 'integrations/bloomberg/research/sa_forecast_fallback.py'); fb = u.module_from_spec(s); s.loader.exec_module(fb)
print('ROG_control', fb.entity_test('Roche Holding AG', 'Rogers Corporation'))
print('CAT_positive', fb.entity_test('Caterpillar Inc', 'Caterpillar Inc.'))
s3 = boto3.client('s3'); B = 'opal-data-harvest'; pg = s3.get_paginator('list_objects_v2')
for k in ['CAT_US_Equity', 'CSL_AU_Equity', '6861_JP_Equity']:
    ks = sorted(o['Key'] for pp in pg.paginate(Bucket=B, Prefix='derived/model_block/' + k + '/') for o in pp.get('Contents', []) if o['Key'].endswith('/model_block.json'))
    b = json.loads(s3.get_object(Bucket=B, Key=ks[-1])['Body'].read()) if ks else {}
    ff = b.get('forecast_fallback') or {}
    sa_cells = [f for f in b.get('figures') or [] if f.get('source') == 'SA_FALLBACK']
    raw = sorted(o['Key'] for pp in pg.paginate(Bucket=B, Prefix='raw/seekingalpha/' + k + '/') for o in pp.get('Contents', []) if o['Key'].endswith('/metrics.json'))
    print(k, 'gaps_before', ff.get('gaps_before'), 'sa_symbol', ff.get('sa_symbol'), 'entity_test', ff.get('entity_test'), 'classification', ff.get('classification'), 'filled_by_sa', ff.get('filled_by_sa'), 'sa_cells_on_block', len(sa_cells), 'metrics_raw_landed', len(raw), 'newest', raw[-1] if raw else None, 'reason', ff.get('reason'))
    print('  sa_cells', [(f.get('fiscal_period'), f.get('mnemonic'), f.get('sa_field'), f.get('value')) for f in sa_cells])
    print('  field_map', ff.get('sa_field_map'))
"</invocation><expect>THE SEEKING ALPHA FALLBACK, EXERCISED ON THE THREE VALIDATION NAMES UNDER THE v0.12 LIFT AND THE v0.13 TERMS CLEARANCE: ROG_control reads REFUSED (or False -- the module's own refusal value, printed) and CAT_positive reads PASS (or True): the entity test discriminates. For EACH name the record shows ONE of these honest terminal states, printed with its reason: (a) gaps_before 0 -- Bloomberg left no cell empty, nothing to fill, no metrics call needed (state it; this is a legitimate exercise of the gap rule); (b) gaps_before greater than 0 with an entity-tested sa_symbol, classification OK, metrics_raw_landed at least 1 (the raw bytes under raw/seekingalpha/<key>/<stamp>/metrics.json BEFORE any fill), filled_by_sa equal to sa_cells_on_block and every SA cell naming its sa_field; (c) UNRESOLVED with the reason (no SA symbol candidate -- the expected state for the numeric-root Keyence unless R14-P1 landed a symbol; or entity test refused; or STOPPED: REHARVEST with a row filed). sa_field_map names, per BEST_ mnemonic, the SA field adopted or NOT-MAPPABLE with the candidates tried (pe_nongaap_fy1/_fy2/_fy3 is the one measured mapping and must appear). NEVER MET: a filled cell whose entity_test is not PASS, a fill with no landed raw, a fill of a not-meaningful value, or a name with no printed terminal state. The number of names with gaps is a measurement, not a target -- CAT with gaps_before 0 across all five fields is a PASS of this criterion, and the fixture test in AC4 is what proves the fill logic when no live gap exists</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-36"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest -q integrations/bloomberg/research/tests/test_forecast_fallback.py lib/research/api/tests/test_fiscal_scope_contract.py -p no:cacheprovider 2>&1 | tail -25</invocation><expect>THE PLANTED CASES, OFFLINE (no vendor call in any test): test_forecast_fallback.py carries, at minimum, (1) a planted GAP -- a recorded Bloomberg bestdata fixture with BEST_EBITDA FY2 empty plus a recorded SA metrics response (the raw bytes this order landed on a validation name, or a fixture in the same shape) -- and asserts the derived cell reads source SA_FALLBACK with the SA value and sa_field named; (2) the same gap with an SA response LACKING the field -- the cell stays ABSENT with fallback_status ATTEMPTED-NO-VALUE; (3) an SA value flagged meaningful false -- never filled; (4) THE QUARTER TRAP -- three period end dates about 90 days apart -- the whole forecast set REFUSED with the not-annual reason and zero forecast figures written; (5) a candidate symbol failing the entity test -- nothing fetched past the symbol call, nothing filled; and test_fiscal_scope_contract.py still passes with its BABA counts unmoved (196 / 183 / 13) because the scope set and the producer's literals moved together. The tail shows N passed, 0 failed, 0 errors, with N at least 5 plus the contract tests -- print the line. Any failure or a skipped planted case is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-36"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, boto3
lam = boto3.client('lambda')
cfg = lam.get_function_configuration(FunctionName='opal-amgt-scoped-api'); print('CodeSha256', cfg.get('CodeSha256'), 'LastModified', cfg.get('LastModified'))
for key in ['BA_US_Equity', 'HOLLOW_NONEXISTENT_KEY_Equity']:
    payload = json.dumps({'rawPath': '/api/scoped/amgt/security/' + key + '/thesis', 'headers': {'x-firm-id': 'bd'}, 'requestContext': {'http': {'method': 'GET'}}}).encode()
    resp = lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=payload)
    body = json.loads(resp['Payload'].read())
    inner = json.loads(body.get('body', '{}')) if isinstance(body.get('body'), str) else body.get('body', {})
    m = inner.get('model') or {}
    print(key, 'statusCode', body.get('statusCode'), 'model_status', m.get('model_status'), 'has_forecast_keys', all(x in m for x in ['forecast_figures', 'forecast_periods', 'forecast_source_counts', 'forecast_reason']), 'forecast_figures', len(m.get('forecast_figures') or []), 'forecast_source_counts', m.get('forecast_source_counts'), 'forecast_reason', m.get('forecast_reason'), 'check_face_len', len(inner.get('check_face') or []), 'fiscal_row_count', m.get('fiscal_row_count'))
"</invocation><expect>THE SERVED PLANE AFTER THE REDEPLOY (post-act CodeSha256 printed and equal to the uploaded artifact's sha recorded in the change-management entry): BA_US_Equity answers 200 with model_status SERVED, has_forecast_keys True, forecast_figures 0 with forecast_reason naming the missing bestdata.json (BA was pulled 2026-09-16, before C-MODEL-FORECASTS, and is NOT re-pulled by this order -- the honest served state), forecast_source_counts printed, and check_face_len and fiscal_row_count EQUAL to the values you recorded for BA in the PRE-DEPLOY census (record them; the shape gained keys and no figure moved); the PLANTED NEGATIVE HOLLOW_NONEXISTENT_KEY_Equity answers with model_status ABSENT and has_forecast_keys True with forecast_figures 0 -- the new keys never fabricate a forecast for a name with no block. Any BA figure count that moved, a missing key, or a forecast on the hollow name is NOT met</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.
AC1-AC3 run after the derive lands; AC4 before the deploy; AC5 only AFTER the redeploy, against the LIVE deployed plane.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~39/AMGT_RESAPP.TO-AMGT-rk-36.consensus-forecasts-sa-fallback.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict); the change-management entry
CLOSED with all three legs proven and its sentinel removal committed; flip `<status>` to `complete`; commit with
`--only -- <paths>`. **Do not stop here** -- `AMGT-rk-37` (the five sheet rows, `CIE_DES`, the Base case) is handed
to you next as a continuation in the SAME worktree; wait for it. Report once, naming: the fifteen Bloomberg requests;
every Seeking Alpha GET (endpoint, symbol, classification, raw key -- never a header or cookie value); the per-name
fallback terminal state; the SA field map measured; the pre/post CodeSha256 and the 13-route census; the rows filed.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~39</slot>
<fabric>site-z</fabric>
