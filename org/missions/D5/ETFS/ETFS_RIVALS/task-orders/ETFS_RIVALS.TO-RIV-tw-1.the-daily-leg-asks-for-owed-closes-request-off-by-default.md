# ETFS_RIVALS task order -- `RIV-tw-1` -- ROUND 27: THE DAILY LEG ASKS FOR OWED CLOSES INSIDE THE BUDGET; THE REQUEST IS OFF BY DEFAULT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-tw-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~19</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (the enrichment leg's own module; it writes only under gold/security_market, which the leg already writes)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files, the CTO's rulings of 2026-10-07 on round 25 and the rows they cite
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. Round 15 moved every period on the page to the last 30 / 90 / 365 calendar days. The buying trend shows, beside its net figure, a month-by-month strip (bought / sold / no trade per month). Each security dialog also lists the fund's trades in the security and draws a price chart by the page's one inline script. A security named in a table or in an account's text is a button that opens that security's one dialog, which carries a section per fund. The page's price charts and rankings read closes from the gold table `security_market`, which today holds five trading days. PRD outcome FWD-24: every security a tracked fund held in the last 365 days has its year of closes, kept by the daily Bloomberg leg, which prints what is owed, asks inside the budget and carries the rest. **This order, round 27, is one of three cells of that outcome; the standing request to the vendor stays OFF in everything you build and test.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-tw-1` -- the daily leg asks for owed closes inside the budget and lands each date's top-up as its own object, each close carrying its trading date; the request is OFF by default (FWD-24, C-OWED-GRAIN, C-OWED-IN-THE-LEG, C-OWED-BUDGET; CTO ruling R13)
- Measured: `enrichment_bloomberg.py` mode `daily` asks for the securities held today and lands ONE object per date;
  mode `market-range` (the hand-run backfill) skips any date that already holds a `market-*` object
  (`_held_dates`), checks `bbg_budget.check_points` before any request and records every request sent. The vehicle runs
  `python -m rivalfunds.enrichment_bloomberg --mode daily` FROM THE WORKING TREE every day at 11:00Z (rows Z-S62, Z-S72):
  this file's merge is its deploy to that job.
- Interface (`enrichment_bloomberg.py` only, plus the module of RIV-ho-1 which it imports lazily):
  1. A switch, environment variable `RIVALFUNDS_HISTORY_OWED`, read once per run: unset, empty or `"0"` = OFF. With it
     OFF the `daily` run is byte-for-byte what it is today: it does not import `history_owed`, makes no additional sink
     list or get, sends no additional request, prints no additional line and returns the same result dict. `"print"` =
     compute the owed set after the daily pull lands and print one line `HISTORY OWED: owed <units> units, <securities>
     securities, <dates> dates; asked 0 (request off); carried <units>`, send nothing, write nothing. `"ask"` = compute,
     ask, land, print `HISTORY OWED: owed <o>; asked <a>; landed <l>; carried <c>`.
  2. With `"ask"`: the units to ask are the first `HISTORY_OWED_CAP` (a named module constant, 5,000) of the owed set in
     its own order (newest dates first); `bbg_budget.check_points(n)` is called BEFORE any request with the count to
     ask, and a refusal asks nothing and prints the refusal with `carried <all>`; every request sent is recorded with
     `bbg_budget.record("history-owed", <points requested>, batch_id)`; what is not asked is carried (counted, never
     stored: the next run recomputes the owed set).
  3. Landing: per date, ONE new object in that date's partition, named by `market_target_uri(date, revision)` with a
     revision that carries the capture time (as `_market_pull` builds it), never overwriting a name and never touching
     another object. Every row carries, beside the existing columns, **`price_date`**: the ISO trading date the vendor
     returned for that close. A returned close whose own date is not the partition's date is NOT written (and is
     counted in the printed line as `misdated <n>`). Rows are marked `as_of_source = "backfill"` and `source` as
     `market-range` marks them today.
  4. The result dict of the `daily` run gains a key `history_owed` only when the switch is not OFF.
  5. The Bloomberg client is reached only through the function `market-range` already uses for a history request; no
     file under `integrations/` is edited or imported in a new way.
- Rulings at the cut (issuer): NOTHING in this cell or its checks calls a vendor: every check and test stubs the client
  hook, as `bf-1.AC1.py` / `bf-1.AC2.py` do. The switch stays OFF in the repository and on the vehicle; turning it on is
  Andrew's recorded answer relayed by 1.0.0_SA_CTO~Z, never a merge. `market-range` and its `_held_dates` are left as
  they are.
- Rulings on the check drafter's questions (issuer): any value of the switch other than exactly `print` or `ask`
  (case-sensitive) is OFF. ONLY the top-up objects carry `price_date`: they are written with the market schema plus
  that one string column; the daily pull's object and `market-range`'s objects are written exactly as today.
  "Misdated" means: a close the vendor returns for a date that is NOT one of the units asked for that security; it is
  not written and is counted. A close is landed in the partition of its own returned date, with `price_date` equal to
  it, only when that (security, date) was asked. `landed` may count rows or objects. A refusal's line format is free
  beyond containing `HISTORY OWED:` and `carried <all>`. `tw-1.AC1.py` compares the switch-OFF run with the module as
  it is at commit 361b735308, read from git: the OFF path stays identical to that commit's behaviour.
- **Organic trigger:** none while the switch is OFF; the issuer's read is the 2026-10-08 and later vehicle logs showing
  the enrichment leg unchanged.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 66cab2698e or later)

- Read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tw-1.AC1.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tw-1.AC2.py` before you build, and the two checks whose way of stubbing the client they follow, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bf-1.AC1.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/bf-1.AC2.py`.
- **THIS FILE IS RUN BY A SCHEDULED JOB FROM THE REPOSITORY'S WORKING TREE EVERY DAY** (`python -m rivalfunds.enrichment_bloomberg --mode daily`). When your branch is merged, the job runs your code the next morning with the switch unset. `tw-1.AC1.py` compares the switch-OFF run, sink call for sink call, request for request, printed line for printed line, with the module as it is at commit 361b735308 (it reads that file from git). Nothing may be added to the OFF path, not an import, not a log line.
- `enrichment_bloomberg.py`: `handler_entry` mode `daily` calls `_market_pull`, which lands one object through `_land_market` at `market_target_uri(date, revision)`; `_market_range` is the hand-run history mode: read how it asks the client for a history range, calls `bbg_budget.check_points` before any request and `bbg_budget.record` for each request sent, and builds rows with `market_rows(..., BACKFILL_SOURCE)`. Reuse its client call; do not add a second way to reach the vendor.
- `history_owed` (another worker's cell, NOT in your worktree's package yet): you call `history_owed.owed(s, day)` -> a DataFrame with columns `security_id`, `security_bloomberg`, `date` (ISO string), `funds`, sorted newest date first, and `history_owed.summary(df)` -> `{"securities", "units", "dates", "newest", "oldest"}`. Import it lazily, inside the branch the switch opens. The checks supply a stub module; your package tests must stub it too.
- NEVER call a vendor: every test stubs the client hook. Never write the real budget ledger: point `bbg_budget` at a temp directory as the checks do.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~19/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r27tw1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the switch OFF (unset, empty, "0"): the daily run is identical to the module at commit 361b735308 in its sink calls, client requests, printed lines and result; `history_owed` is not imported; the constant and the variable exist (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tw-1.AC1.py`)
- **AC2** -- `print` and `ask`: the printed line; the budget checked before any request and every request recorded; one new timed object per date beside the untouched one, each row with `price_date`; the cap and the carry; a refusal; a misdated close not written; never overwrite (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tw-1.AC2.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real read, never by you): the 2026-10-08 and later vehicle logs show the enrichment leg's lines and exit code unchanged with the switch unset. **AMENDMENT 1 (2.0.0_SA_COO~V1, 2026-10-09, the disarm of row ETFS_RIVALS-Z-S79):** J1 is read on the FIRST scheduled vehicle run that REACHED the enrichment leg -- its log carries the `RIVALFUNDS ENRICHMENT STEP` line, an enrichment exit code other than 97, and no vendor-session-failure line (`Failed to start session`, `session pool state=Failed`, `could not start blpapi session`, `"unreachable": true`) -- never on the earliest date in the range. A run that did not reach the leg reads UNVERIFIABLE for J1, never PASS; the 2026-10-08 11:00Z run is such a run.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-tw-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tw-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-tw-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tw-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-tw-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~19/ETFS_RIVALS.TO-RIV-tw-1.the-daily-leg-asks-for-owed-closes-request-off-by-default.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-tw-1.the-daily-leg-asks-for-owed-closes-request-off-by-default`. Report once: each mechanical criterion's verdict line with the output above it; the judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; exactly which lines of the `daily` path you touched and why the OFF path is unchanged (name the one branch that guards everything new); how a history request is batched and how many points one request can carry; what `landed` counts; the schema of a top-up object; what any other switch value does; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.19 @2914a61989 (ADMITTED); decomposition v1.17 (round 27 appended). Source: PRD ADDENDUM G (FWD-24), ROUND_ANALYSIS.round22 ADDENDUM 4 and CTO ruling R13. Chain `~19`, slot `~19`, position 1 of 1. Checks drafted by a helper under the issuer's brief (@80327807d9), re-run by the issuer at base 66cab2698e: tw-1.AC1 FAIL 1 (arm e: the constant and the variable do not exist; the OFF arms a to d and the control f PASS and must keep passing); tw-1.AC2 FAIL 6 (arms a to f; the control g PASSES). The helper's simulated build passes both; six planted defects fail the arms that grade them. THE VEHICLE RUNS THIS FILE FROM THE WORKING TREE (rows Z-S62, Z-S72): the merge is a deploy to the 11:00Z job, so the merge of this chain is timed by the issuer and its first vehicle log is read.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>27</round>
<slot>~19</slot>
<fabric>site-z</fabric>

<status>complete</status>
