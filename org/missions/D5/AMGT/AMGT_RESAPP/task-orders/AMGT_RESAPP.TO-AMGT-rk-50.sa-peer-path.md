# AMGT_RESAPP task order -- `AMGT-rk-50` -- the Seeking Alpha peer path: entity-tested slug, four GETs through the existing rest_fetch.py, raw landed at a builder address before derivation, R-1 with a source on every cell, the Bloomberg growth fill name-checked

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-50</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~51</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the Peers read it
  builds runs ONCE per named security by hand invocation, never on a schedule (C-PEER-SET-SA names one read per
  security at instantiation; no recurring read is stood up here); the standing no-monitor moratorium is unaffected.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes S3 objects only, under the credentials this box already
  holds, to ONE already-provisioned bucket, opal-data-harvest (bronze raw bytes at the builder's registry-gated address, and the
  peers/v1 pool object the adapter already reads); it grants no permission, provisions no bucket, touches no
  Lambda role and applies no Terraform. It adds NO registry row: the `amgt` scope row is
  NOT adopted -- Andrew answered the card ~21:1xZ (msg 23774: *"register opal-data-harvest, go with your rec"*, option (b), no
  scope row) -- so bronze raw lands under the EXISTING COMPOSITE `global` scope row.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~51`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/`, `lib/research/peers/`,
`integrations/seekingalpha/rest_fetch.py` and `lib/opal_naming.py` exist; if any is absent, STOP with a BLOCKING row.
Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~51;`. **NEVER RUN AN INSTALL.** This order is
chain P's head: `AMGT-rk-51` (Peers V over the set you land) waits on your `complete` flip.

## 1. THE CELL, inlined in full -- `AMGT-rk-50` (R14-P1; FWD-8; Peers brief rows P1-P7)

**THE ANALYSIS ROW, verbatim** (`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round13.md` @9c8e04cd9a `:137`):
*"the Seeking Alpha peer path: entity-tested SA slug (`ROG` = Rogers Corporation is the standing negative control), the
four GETs through the existing `rest_fetch.py`, raw landed before derivation (at a builder-made address), derivation to
R-1 with a source on every cell and the Bloomberg growth fill -- each PEER ticker's Bloomberg join also passes a
name-agreement check, the same trap as ROG; a REHARVEST stops the run."* Its closing clause *"Proven on the validation
names only until card 3(a)"* is OVERTAKEN: card 3 was answered YES (analysis s.5 `:166-172`) and the terms question was
cleared by Andrew himself (PRD v0.13 @1699960261 `:634-637`, `:1094`, `:1109`). Production use of this path is
AUTHORIZED BY NAME; what still binds is `C-VALIDATION-NAMES` -- this order proves the path on CAT, CSL and Keyence and
runs NOTHING over the covered 33.

**THE CONTRACT YOU BUILD TO -- `C-PEER-SET-SA`, PRD v0.13 @1699960261 `:614-641`, every clause:**
- SET (`:615-618`): a subject's peers are SA's suggested peers, 5 per subject, `GET /api/v3/symbols/{slug}/suggested?source_type=peers_similarities&variation=ds_v2`,
  fetched through the EXISTING `integrations/seekingalpha/rest_fetch.py` -- its `load_config` (`:84-86`),
  `build_session` (`:98-143`, the PARKED session bundle + residential proxy) and `_do_get` (`:153-204`, per-page
  Referer, request log, `detectors.classify`). GET only (`:30`: the proxy refuses every POST). No new fetcher, never the
  crawler. `basis` = `sa` | `absent`; an absent set names its reason from exactly this set: `no SA slug`,
  `entity test failed`, `no suggested peers`, `REHARVEST`.
- IDENTITY FIRST (`:619-622`): the subject's SA slug passes an ENTITY test before any peer call. The test is the CRO's
  measured rule, ported: `org/tier1_exec/4.0.0_SA_CRO/scripts/sa_symbol_resolve_pass.py:108-135` `name_matches()` --
  accent-fold (`:92-99`), strip SA's `<b>` tags (`:81-89`), distinctive tokens of length >= 4 minus corporate stop
  tokens (`:102-105`), ACCEPT on containment of the concatenated forms or jaccard >= 0.5; never rank, never score.
  `ROG` -> Rogers Corporation, not Roche, is the standing control and MUST be refused. **Each PEER ticker's Bloomberg
  join passes the SAME name-agreement check** (Bloomberg `NAME` against SA's company name) before its values are used.
- TABLE (`:623`): SA's shape covering 17 of 17 CSC columns (`lib/research/peers/csc.py:61-79` is the declared
  denominator; today 5 of 17 present, `:84-90`). Preferred + Minority is ONE rendered column, SA's `other_cap_struct`,
  covering BOTH declared columns -- so 16 rendered columns cover 17 of 17 declared, and the object says so in those words.
- SOURCE RULE (`:624-628`): a column SA carries comes from SA; a column SA lacks comes from Bloomberg, the SA ticker
  queried as `<TICKER> US Equity`; where Bloomberg has no value, SA's nearest measure is used, LABELLED as that
  measure. Every cell carries `source` = `SA` | `BBG` | `SA_FALLBACK:<field>`. A cell derived from SA inputs (Shares =
  marketcap / close; equity = marketcap / pb_ratio; Debt/Equity, Net Debt/Equity, Net Debt/Capital from total_debt,
  total_cash and that equity) is `source: SA` with a `derivation` string naming the formula.
- NOT MEANINGFUL (`:629-630`): an SA value flagged `meaningful: false`, or absent, is ABSENT with SA's reason -- never
  zero-filled, never filled from another source. The Bloomberg fill applies ONLY to the two columns SA lacks.
- SESSION (`:631-633`): a 403 that `detectors.classify` (`integrations/seekingalpha/detectors.py:39-48`) reads as
  `REHARVEST` STOPS the run and says so (`rest_fetch.py` `ReHarvestNeeded` `:70-71`; the pattern at `:282-283`, rc 3 at
  `:463-468`). Never sign in, never retry around the challenge, never launch the harvester. **Raw bytes land BEFORE
  derivation at an address built by `lib/opal_naming.py`** (Rule 30) -- NOT through `rest_fetch.land_raw()` (`:211-218`),
  whose key is hand-typed (`raw/%s/%s/%s/%s.json` into `config["store_bucket"]`); you write the same `response.content`
  bytes to the builder's address with your own put.

**THE MEASURED CURRENT STATE, file:line @4de34f0d95 (the code is byte-identical at 1699960261, which touched only the PRD
and one record):**
- `lib/research/peers/engine.py:72` `BASES = ("analyst", "derived", "absent")` and `_make()` `:619-621` RAISES on any
  other basis -- `sa` is refused today. `:286-325` `sa_candidates()` still records `ABSENT-ACCESS ... not called` and
  `summary_lines()` `:1114-1117` prints it -- stale once this order lands. `write_pool_object()` `:1138-1163` (PUT +
  read-back, `Metadata document-sha256`) and `pool_key()` `:1134-1135` (`peers/v1/<key>/<as_of>.json`) are the ONE
  pool writer you reuse. `resolve_identity()` `:232-283` and `build_widened_identity_index()` `:206-229` are the X-1
  identity join you reuse for every member.
- `lib/research/scores/run_scores.py:118-130` `_latest_peer_set()` picks the NEWEST `peers/v1/<key>/*.json` by string
  sort -- the object you land becomes the one Peers V (`AMGT-rk-51`) reads.
- `lib/research/api/scoped_amgt.py:1244-1278` `read_peer_set()` serves the landed object WHOLE (`:1276-1278`) on
  `/peers` (`:3331-3334`): your new fields ride through without an adapter change. The adapter is NOT your surface.
- `lib/opal_naming.py:1558-1571` `address(source, scope, tier, table, partition, object=None)` builds
  `s3://{bucket}/{source}/{scope}/{tier}/{table}/{partition}[/{object}]`; the bucket comes from the tier home rule
  (`infra/logic/registry/tiers.json`: PRODUCT bronze -> shared `opal-data-harvest` (registry-gated, see the issuer amendment)), never an argument. **MEASURED at the
  cut:** `address('seeking-alpha','amgt','bronze','peers','CAT_US_Equity')` REFUSES with exactly
  `scope 'amgt' resolves to no scopes.json row` -- `amgt` is a PRODUCT SYSTEM (`infra/logic/registry/systems.json:47`)
  with NO scope row. Rule 30, CLAUDE.md s.4: *"a builder REFUSAL is a missing registry row to add
  (`infra/logic/registry/`), never a hand-typed workaround."* `validate()` (`lib/opal_naming.py:285-548`) admits a
  PRODUCT row only with `bucket == "opal-data-" + long` (`:342-343`), a boolean `bucket_provisioned` (`:358-359`) and,
  if present, a non-empty `note` (`:340-341`); `validate` reads 0 refusals / 16 warnings today.
- The validation names' keys, minted the way `lib/research/identity/crosswalk.py:334` mints every key
  (`"%s_%s_Equity" % (root, exchange)`) from the yellow keys the validation report names
  (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/INSTANTIATION_VALIDATION_REPORT_20260918.md:30-32`): **`CAT_US_Equity`**
  (Caterpillar Inc.), **`CSL_AU_Equity`** (CSL Limited), **`6861_JP_Equity`** (Keyence Corporation). None is in the
  crosswalk yet (R14-I1 lands identity); you pass `--name` explicitly and the object records `identity` as the
  crosswalk resolves it today (UNRESOLVED, honestly) -- when I1 lands, the same code path resolves it.
- The CRO measured the four calls through this exact module on BA/SAP/KDDIY: 15 GETs, all `OK`, nothing landed
  (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/BRIEF_PEERS_CURRENT_TO_DESIRED_20260918.md:54-78` @a2fdbad164; the
  Andrew-direct record `ANDREW_DIRECT_20260918_17xxZ_PEERS_SEEKING_ALPHA.md:43-54` @1ea17fef52). SA fields per column,
  brief `:80-96`: `close`, `marketcap`, `tev`, `total_debt`, `total_cash`, `other_cap_struct`, `pe_nongaap_fy1/_fy2/_fy3`,
  `revenue_growth5`, `pb_ratio`; Bloomberg supplies `GEO_GROW_OPER_INC` (5-yr EBIT growth) and
  `FREE_CASH_FLOW_5_YEAR_GROWTH` (5-yr FCF growth), 15 of 18 rows each, queried as `<SA ticker> US Equity` with no
  mapping step (`:105-107`).

**RULED -- what you build, in this order:**

0. **The address (Rule 30, as RULED at the cut).** The builder REFUSES `scope 'amgt'` today and that row is NOT
   coming: Andrew answered the card ~21:1xZ (relayed by `1.0.0_SA_CTO~Z`, msg 23774, VERBATIM *"register opal-data-harvest,
   go with your rec"*) -- option (b), `opal-data-harvest` registered as a pool home by `0.0.0_AB_MSTR~Z`, NO `amgt` scope row.
   Do NOT edit `infra/logic/registry/scopes.json` (it is not in `<paths>`; the lane refuses it). Land every raw vendor
   byte under the COMPOSITE `global` scope row that EXISTS (`infra/logic/registry/scopes.json` key `global`, class GLOBAL,
   tenancy COMPOSITE) -- MEASURED at the cut: `address('seeking-alpha','harvest','bronze','peers','CAT_US_Equity')` BUILDS
   `s3://opal-data-harvest/seeking-alpha/harvest/bronze/peers/CAT_US_Equity` and
   `address('bloomberg','harvest','bronze','peers-growth','CAT_US_Equity')` BUILDS the bloomberg twin, both from
   `lib/opal_naming.py address()` with no registry change. Run `python lib/opal_naming.py validate` once (0 refusals, or
   STOP with a row). File ONE surprise row (`spec_asserts`: Rule 30 / C-PRODUCTION-HOME name a product-scoped bronze
   home; `world_is`: Andrew declined an `amgt` scope row ~21:1xZ (msg 23774) and chose registering opal-data-harvest as the pool
   home, so this order's raw sits under `global` and the R-1 pool objects stay at `peers/v1/` in opal-data-harvest, which is
   exactly where every AMGT reader keys today) and keep
   working. Do NOT run `generate` and do NOT touch any generated view.
1. **`lib/research/peers/sa_peers.py` (new, in the existing package).** Loads `rest_fetch` and `detectors` BY PATH the
   way `integrations/bloomberg/research/model_block_pull.py:147-157` loads `blp_client` (integrations/ has no
   `__init__`), and `lib/opal_naming.py` by path (lib/ has no `__init__`, `lib/opal_naming.py:28`). Functions:
   `entity_test(subject_name, sa_name) -> (passed, overlap)` -- the port of `name_matches()` with its `fold`, `strip_tags`
   and `_words`, the stop-token set copied IN with its source cited (production code never imports a seat's `org/`
   script); `resolve_slug(session, config, subject_name, log)` -- `GET /api/v3/searches?filter[query]=<name>&filter[type]=symbols&page[size]=10`
   through `_do_get`, candidates from `payload["symbols"]` (`name` = symbol, `content` = company name), the FIRST
   candidate passing `entity_test` wins, none -> `UNRESOLVED` with every rejected `(symbol, sa_company, overlap)`
   recorded; `fetch_peers(...)` -- the four GETs (suggested; `tickers?filter[slugs]=<subject,peers>&include[gics]=true`;
   `metrics?filter[fields]=<the field list>&filter[slugs]=<subject,peers>`; `ticker_metric_grades?...&filter[algos][]=main_quant`),
   each `OK` response's raw `response.content` landed at
   `address("seeking-alpha","harvest","bronze","peers",<security_key>, object="<utc_stamp>-<endpoint>.json")` BEFORE any
   derivation, `REHARVEST` -> raise `ReHarvestNeeded` and STOP; `growth_fill(tickers, sa_names)` -- ONE
   `blp_client.reference_data([<T> US Equity ...], ["NAME","GEO_GROW_OPER_INC","FREE_CASH_FLOW_5_YEAR_GROWTH"])`
   (`integrations/bloomberg/mcp/blp_client.py:135-145`; a security-level error is `{"__error__": msg}` `:143-144`),
   raw landed at `address("bloomberg","harvest","bronze","peers-growth",<security_key>, object="<utc_stamp>.json")`,
   then per ticker `entity_test(sa_company, NAME)`: DISAGREE -> that ticker's two BBG cells are NOT used (recorded
   `name_agreement: false` with both names) and fall to SA's nearest measure `SA_FALLBACK:<field>` if SA carries one,
   else ABSENT with that reason; `derive(...)` -> the R-1 object: `basis: "sa"`, `subject` and 5 `members` each with
   `sa_slug`, `sa_company`, `name_agreement`, `identity` (via `engine.resolve_identity`), and `cells: {<declared CSC
   column>: {value, source, meaningful, reason, derivation, sa_field|bbg_field}}` over ALL 17 declared columns
   (`Preferred` and `Minority` both carry `merged_into: "other_cap_struct"`), `csc_columns` = `csc.build_csc_map()`
   extended with `sa_shape: {rendered_columns: 16, declared_covered: "17 of 17", merged: {...}}`, `raw_refs` = every
   bronze address landed, `source_counts` = cells by `SA` / `BBG` / `SA_FALLBACK` / `ABSENT`, `reason` naming the
   slug, the entity test's overlap and the counts; written through `engine.write_pool_object()`.
   CLI: `python -m lib.research.peers.sa_peers plan --security-key K --name "N"` -- ZERO requests, ZERO writes,
   prints the four planned GET paths, both builder addresses (naming `lib/opal_naming.py address()` as the builder),
   the pool key, and a built-in control line `ENTITY-CONTROL "Roche Holding AG" vs "Rogers Corporation" REFUSED`
   computed live by `entity_test` at every invocation; `run --security-key K --name "N" [--write-pool]` -- the path;
   without `--write-pool` it lands raw and prints the derived object but does not write `peers/v1`. Every summary line
   prints its denominator. rc 3 on REHARVEST, rc 4 on AUTH_FAIL, rc 0 otherwise (an `absent` set with a named reason
   is a correct terminal state, rc 0).
2. **`lib/research/peers/engine.py`:** `BASES` gains `"sa"` (`:72`); `sa_candidates()` (`:286-325`) returns
   `{"status": "SUPERSEDED-BY-C-PEER-SET-SA", "module": "lib/research/peers/sa_peers.py", "called": False, ...}` so
   `:1114-1117` no longer prints a stale ABSENT-ACCESS. Nothing else in the ranker moves (FWD-19's comparable still
   runs it, PRD `:638-639`).
3. **`lib/research/peers/tests/test_peers.py`:** a `unittest.TestCase` class `SaEntityTest` (the file's own rule,
   `:4-8`: classes, never bare functions) with at least: `test_rog_is_rogers_not_roche_refused`
   (`entity_test("Roche Holding AG","Rogers Corporation")` is False), `test_caterpillar_accepted`
   (`entity_test("Caterpillar Inc.","Caterpillar Inc.")` and the `<b>`-tagged form both True),
   `test_america_movil_vs_liberty_latin_america_refused` (the CRO's measured false positive, `:112-125`),
   `test_growth_fill_name_disagreement_refuses_bbg_cells` (a stubbed reference_data return whose NAME disagrees ->
   both BBG cells fall to fallback/ABSENT with `name_agreement: false`), and `test_not_meaningful_never_zero`
   (`meaningful: false` -> value None, source None, reason SA's). NO NETWORK in any test.

**The validation bar (`C-VALIDATION-NAMES`, `:1652-1658`):** the three names above, one `run --write-pool` each. Keyence
and CSL resolve through their US ADRs (brief `:140`, *"Non-US names resolve through their US ADR"*); if SA carries no
suggested peers or no estimates for an ADR, the object is `absent` with that reason and the path has still been
exercised honestly -- that is a PASS of THIS cell, not a defect to work around. NO other name is run.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis @9c8e04cd9a s.4 row R14-P1 (`:137`),
s.2 (`:56-61`, the production-home class), s.5 cards 1-3 as answered (`:166-172`). PRD v0.13 @1699960261:
`C-PEER-SET-SA` (`:614-641`), `C-SA-VENDOR-WORD` LIFTED BY NAME (`:1108`) and TERMS CLEARED (`:1109`),
`C-SA-TERMS-BEFORE-SCHEDULE` SATISFIED for this path (`:1094`), `C-PRODUCTION-HOME` (`:1643-1650`),
`C-VALIDATION-NAMES` (`:1652-1658`). Both L4-R halves signed at v0.13 before this order was cut.

**ISSUER AMENDMENT at the cut (`2.0.0_SA_COO~Z`, 2026-09-18 ~21:0xZ):** the draft's step 0 added an `amgt` row to
`infra/logic/registry/scopes.json`. That edit is WITHDRAWN: `1.0.0_SA_CTO~Z` adjudicated (@44702e4e90) that the
`amgt` scope row was Andrew's card; Andrew answered ~21:1xZ (msg 23774) with NO scope row, and this fabric treats it as it treats `AMGT-rk-33`'s move -- a builder-refusal ROW,
never a hand-typed workaround and never a registry row minted by a worker. Every address in this order therefore uses
the COMPOSITE `global` scope, which BUILDS today; `scopes.json` is not on this order's surface.

**ISSUER AMENDMENT -- THE REGISTRY GATE (`2.0.0_SA_COO~Z`, 2026-09-18 ~21:3xZ, on Andrew's words relayed by
`1.0.0_SA_CTO~Z` msg 23778):** Andrew, VERBATIM: *"Yeah i hope its clear and foundational in all associated AMGT_RESAPP art
that the opal-data-harvest bucket is the designated folder for all RESAPP data content/pipelines"* and *"then it has to be
structured in said bucket in proper form"*. So: EVERY AMGT_RESAPP byte this order lands -- bronze raw included -- lands in
`opal-data-harvest`, at an address PRINTED BY `lib/opal_naming.py address()`, never typed. MEASURED at the cut: the registry
(`infra/logic/registry/tiers.json:27`) still homes bronze/silver in the shared `opal-data-assets`; the two registry rows that
re-home this project (the home registration + the R20 departure entry) are being placed by `0.0.0_AB_MSTR~Z` on the laptop
fabric and land here by merge. THE RULE, replacing every literal bucket in this order: before ANY live write at a builder
address, print the builder's output for the address the order names with the scope token `harvest` (the L4 RULING,
`1.0.0_SA_CTO~Z` @2560e04f46: vendor bronze is `<vendor>/harvest/bronze/<table>/<partition>/<object>`, our own derivations
`amgt/harvest/<tier>/<table>/...`; NO `global` route and NO `amgt` scope row -- a scope spelled `amgt` is refused by the
builder, and `global` is not this project's route; where this order's older text says `global`, read `harvest`); the naming gate at commit is ENFORCING and its grader is WIDER than the builder, so a
hand-typed key can pass the commit and resolve nowhere -- never type one); the live
arm is LIVE iff that address's bucket is `opal-data-harvest`. If the builder REFUSES or returns any other bucket, DO NOT
WRITE THERE: the offline, read-only and dry-run criteria run in full; each live criterion is recorded with the builder's
printed line as its output and the verdict REFUSED-BY-REGISTRY; ONE surprise row carries it (`spec_asserts`: Andrew's words
above and CTO msg 23778; `world_is`: the builder's exact output at spawn), and the worker keeps working. A write to
`opal-data-assets` of any AMGT_RESAPP object is NOT AUTHORIZED by this order under any branch. Where this order's text below
reads `s3://opal-data-harvest/...` for a builder address, that is the EXPECTED bucket once the rows land, and the address is
still read from the builder's print, never from this text.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/peers/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~51/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-50.sa-peer-path.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** `integrations/seekingalpha/rest_fetch.py`, `detectors.py`,
  `config.json`, `integrations/bloomberg/mcp/blp_client.py` and `lib/opal_naming.py` are READ and IMPORTED, never
  edited: a criterion that needs a change in any of them is REFUSED with a row. `lib/research/scores/` is
  `AMGT-rk-51`'s surface. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~51 <0.9.0_WK_AMGT_RESAPP~51@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Never push, merge, rebase, `checkout --`, `stash` or `clean`. The
  naming limb of safe-commit runs in WARN mode (`.tools/naming-gate.py` docstring): a registry-row literal is a
  PERMITTED context; read every WARN it prints and record it in your report.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF -- this cell's Seeking Alpha GETs are the round's
EXPLICITLY AUTHORIZED exception:** production use at instantiation and in validation is lifted BY NAME for
`C-PEER-SET-SA` (PRD v0.13 @1699960261 `:634-637`, `:1108-1109`; Andrew-direct ~19:4xZ *"Yes use SA thats fine"* and
~20:0xZ *"I have already clarified SA ToS, we are good"*). **This cell exercises CAT, CSL and Keyence and no other
name.** No RECURRING or SCHEDULED read is stood up by this order (it arms nothing; `C-SA-TERMS-BEFORE-SCHEDULE` is
satisfied for this path, `:1094`, and a cadence stays Andrew's). Bloomberg: the growth fill runs ONLY for the validation
names' subject + peer tickers (at most 18 securities, 3 fields, one `reference_data` call per subject), inside the
validation Andrew set as the bar. **Read `integrations/bloomberg/READ_HERE.md` first**; call `blp_client.health()` before
the first pull; if the terminal is signed out, do NOT sign in (the two-attempt budget is the BBG seat's) -- REFUSE the
Bloomberg-dependent parts with a row and proceed with the SA half. **NO alarm, monitor, SNS/SES-send, notification or
freshness checker.** Secrets through the module's own `_secret()` by NAME only -- **never print, log, write or commit
a cookie, proxy credential, session value, or Andrew's HAR** (`config.json` names the secrets; that is all you touch).
No non-ASCII in anything you write. **PUSH: never.** LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name. A `REHARVEST` or `AUTH_FAIL` is exactly that:
record it, rc 3/4, no retry, no harvester, no sign-in.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- re-measure at spawn: the object
counts under both bronze addresses and under `peers/v1/CAT_US_Equity/` (expected 0, 0, 0 before this order).
**A DRY RUN WRITES NOTHING, ANYWHERE** (`C-PRODUCTION-HOME`, `:1646-1647`): `plan` performs no request and no put.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W51-S<k>`, `<k>` starting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize
it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-50"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest lib.research.peers.tests.test_peers -k SaEntityTest -v 2>&1 | tail -12</invocation><expect>the verbose listing names test_rog_is_rogers_not_roche_refused, test_caterpillar_accepted, test_america_movil_vs_liberty_latin_america_refused, test_growth_fill_name_disagreement_refuses_bbg_cells and test_not_meaningful_never_zero each "ok", and the footer reads "Ran N tests" with N >= 5 followed by "OK" -- the ROG-for-Roche control REFUSED offline with no network</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-50"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import importlib.util
spec = importlib.util.spec_from_file_location('opal_naming', 'lib/opal_naming.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
r, w = m.validate()
print('validate refusals', len(r), 'warnings', len(w))
print('SA-RAW', m.address('seeking-alpha', 'harvest', 'bronze', 'peers', 'CAT_US_Equity'))
print('BBG-RAW', m.address('bloomberg', 'harvest', 'bronze', 'peers-growth', 'CAT_US_Equity', object='STAMP.json'))
try:
    m.address('seeking-alpha', 'no-such-scope', 'bronze', 'peers', 'CAT_US_Equity'); print('NEGATIVE-CONTROL not refused')
except ValueError as e:
    print('NEGATIVE-CONTROL refused:', e)
"</invocation><expect>validate refusals 0; SA-RAW s3://opal-data-harvest/seeking-alpha/harvest/bronze/peers/CAT_US_Equity and BBG-RAW s3://opal-data-harvest/bloomberg/harvest/bronze/peers-growth/CAT_US_Equity/STAMP.json are BUILT (no refusal) with NO registry edit, and the planted unknown scope is REFUSED with "resolves to no scopes.json row" (the text the `amgt` scope refuses with today; that row is Andrew's card @44702e4e90, never this order's edit)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-50"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, subprocess, sys
s3 = boto3.client('s3', region_name='us-east-1')
def count(bucket, prefix):
    return sum(len(p.get('Contents', [])) for p in s3.get_paginator('list_objects_v2').paginate(Bucket=bucket, Prefix=prefix))
targets = [('opal-data-harvest', 'seeking-alpha/harvest/bronze/peers/CAT_US_Equity/'), ('opal-data-harvest', 'bloomberg/harvest/bronze/peers-growth/CAT_US_Equity/'), ('opal-data-harvest', 'peers/v1/CAT_US_Equity/')]
before = [count(b, p) for b, p in targets]
r = subprocess.run([sys.executable, '-m', 'lib.research.peers.sa_peers', 'plan', '--security-key', 'CAT_US_Equity', '--name', 'Caterpillar Inc.'], capture_output=True, text=True)
print(r.stdout)
after = [count(b, p) for b, p in targets]
print('rc', r.returncode, 'objects before', before, 'after', after, 'UNCHANGED' if before == after else 'CHANGED')
"</invocation><expect>the plan prints four GET paths (suggested, tickers, metrics, ticker_metric_grades), RAW-ADDRESS lines built by lib/opal_naming.py address() for both bronze prefixes, POOL-KEY peers/v1/CAT_US_Equity/{date}.json, the line ENTITY-CONTROL "Roche Holding AG" vs "Rogers Corporation" REFUSED, and REQUESTS 0 WRITES 0; rc 0; and the three object counts read UNCHANGED (a dry run writes nothing, anywhere)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-50"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.peers.sa_peers run --security-key CAT_US_Equity --name "Caterpillar Inc." --write-pool 2>&1 | tail -20; echo "rc=$?"</invocation><expect>for CAT_US_Equity: ENTITY {slug} ACCEPTED with SA's company name and overlap printed; PEERS 5 of 5 with their SA tickers; RAW-LANDED 4 of 4 at s3://opal-data-harvest/seeking-alpha/harvest/bronze/peers/CAT_US_Equity/...; BBG-NAME-AGREEMENT k of 6 (subject + 5 peers, each pair of names printed); CELLS {filled} of 102 (6 rows x 17 declared columns) with SA / BBG / SA_FALLBACK / ABSENT counts summing to 102; POOL WROTE peers/v1/CAT_US_Equity/{as_of}.json read-back True; rc=0. A line reading BLOCKED: REHARVEST_NEEDED or AUTH_FAIL is a FAIL of this criterion recorded as such, never retried</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-50"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.peers.sa_peers run --security-key CSL_AU_Equity --name "CSL Limited" --write-pool 2>&1 | tail -8; echo "rc=$?"; python -m lib.research.peers.sa_peers run --security-key 6861_JP_Equity --name "Keyence Corporation" --write-pool 2>&1 | tail -8; echo "rc=$?"</invocation><expect>for EACH of CSL_AU_Equity and 6861_JP_Equity the run terminates rc=0 in one of two honest states, printed: (a) an SA set -- ENTITY {ADR slug} ACCEPTED, PEERS 5 of 5, RAW-LANDED n of 4, POOL WROTE ... read-back True; or (b) BASIS absent with a reason drawn from exactly {no SA slug; entity test failed; no suggested peers} and the rejected candidates listed. BLOCKED: REHARVEST_NEEDED / AUTH_FAIL / TRANSPORT_ERROR is a FAIL, not state (b)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-50"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json
s3 = boto3.client('s3', region_name='us-east-1')
keys = sorted(o['Key'] for p in s3.get_paginator('list_objects_v2').paginate(Bucket='opal-data-harvest', Prefix='peers/v1/CAT_US_Equity/') for o in p.get('Contents', []))
print('objects', len(keys), keys[-1:] )
doc = json.loads(s3.get_object(Bucket='opal-data-harvest', Key=keys[-1])['Body'].read())
rows = [doc.get('subject') or {}] + list(doc.get('members') or [])
cells = [(r.get('cells') or {}).get(c) for r in rows for c in doc['csc_columns']['columns']]
print('basis', doc.get('basis'), 'members', len(doc.get('members') or []), 'of 5')
print('cells', len(cells), 'with_source_field', sum(1 for c in cells if c is not None and 'source' in c), 'sourced_or_absent_with_reason', sum(1 for c in cells if c and (c.get('source') in ('SA','BBG') or str(c.get('source','')).startswith('SA_FALLBACK:') or (c.get('source') is None and c.get('reason')))))
print('members_with_identity', sum(1 for m in doc.get('members') or [] if 'identity' in m), 'members_with_name_agreement', sum(1 for m in doc.get('members') or [] if 'name_agreement' in m), 'raw_refs', len(doc.get('raw_refs') or []))
print('sa_shape', doc['csc_columns'].get('sa_shape'))
"</invocation><expect>basis sa, members 5 of 5; cells 102 with_source_field 102 and sourced_or_absent_with_reason 102 (every cell carries a source, or is ABSENT with SA's reason -- never a bare value); members_with_identity 5, members_with_name_agreement 5, raw_refs 5 (four SA endpoints + one Bloomberg refdata response); sa_shape states rendered_columns 16 covering "17 of 17" declared with the merge named</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.
AC4-AC6 read the LIVE store after your run; AC1-AC3 are offline or zero-request and run BEFORE any live call.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~51/AMGT_RESAPP.TO-AMGT-rk-50.sa-peer-path.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once: the three names' terminal states, every naming-gate WARN,
the surprise row on the generated views, and the exact bronze addresses landed.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>superseded</status>
<superseded_by>AMGT-rk-85 (H3) and AMGT-rk-83 (H1): its own text lands bronze at .../bronze/peers/CAT_US_Equity (an unnamed entity in the partition slot, no fetch timestamp), which breaks C-BRONZE-AS-RECEIVED form (a) and C-SLASH-SAFE-KEY. RULED by 1.0.0_SA_CTO~Z, ROUND_ANALYSIS.round20.md s.2 @ab54fb15e0 (msg 24109): SUPERSEDED is terminal, not acceptance (R4); the remedy stays owed by the successor. Flipped in the round-21 issuance by 2.0.0_SA_COO~Z.</superseded_by>
<round>14</round>
<slot>~51</slot>
<fabric>site-z</fabric>
