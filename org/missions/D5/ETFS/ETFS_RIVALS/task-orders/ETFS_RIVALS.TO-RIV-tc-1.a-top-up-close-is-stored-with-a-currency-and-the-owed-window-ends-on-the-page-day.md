# ETFS_RIVALS task order -- `RIV-tc-1` -- ROUND 28: A TOP-UP CLOSE IS STORED WITH A CURRENCY, AND THE OWED WINDOW ENDS ON THE PAGE DAY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-tc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~22</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (the enrichment leg's own module; it writes only under gold/security_market, which the leg already writes)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files, the CTO's rulings of 2026-10-07 on round 25 and the rows they cite
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. Round 15 moved every period on the page to the last 30 / 90 / 365 calendar days. The buying trend shows, beside its net figure, a month-by-month strip (bought / sold / no trade per month). Each security dialog also lists the fund's trades in the security and draws a price chart by the page's one inline script. A security named in a table or in an account's text is a button that opens that security's one dialog, which carries a section per fund. The page's price charts and rankings read closes from the gold table `security_market`, which today holds five trading days. PRD outcome FWD-24: every security a tracked fund held in the last 365 days has its year of closes, kept by the daily Bloomberg leg, which prints what is owed, asks inside the budget and carries the rest. **This order is one of the two cells of round 28; no vendor and no model is called by anything you build or test.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-tc-1` -- a top-up close is stored with a currency, and the owed window ends on the page day (CTO half C2 of round 27; ROUND_ANALYSIS.round22 ADDENDUM 6 item 2; CTO ruling R13)
- Measured (round 27 as built, `enrichment_bloomberg._history_owed`): a top-up row is written with `currency` NULL
  (`{"PX_LAST": px, "CRNCY": None}`), and a security that never had a daily pull would have closes and no stored
  currency (the chart draws no curve without one). The leg calls `history_owed.owed(s, date)` with the REPORT date, so
  the window ends one trading day before it and the report date itself is never owed for a security the daily pull
  did not ask (a formerly-held one). `market-range` already has the pattern: `_stored_currencies` first, then ONE
  `_blp_reference_data` request for the single field `CRNCY` for exactly the securities with none, counted in the
  budget before any request.
- Interface (`data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` only, inside the branch the switch opens):
  1. **The window's end.** The leg calls `history_owed.owed(s, page_day)` where `page_day` is the next trading day
     after the report date (`lib.trading_calendar`), so the report date is the newest date a unit can be owed for. In
     `print` and in `ask`.
  2. **Currency, in `ask` only.** For the securities among the units to ask: the stored currency
     (`_stored_currencies`, over the owed window) where one exists; for those with none, ONE `_blp_reference_data`
     request for the single field `CRNCY`, sent through `_blp_call`, BEFORE the history requests. Its points (one per
     security asked) are part of the count passed to `bbg_budget.check_points` (units to ask plus currency lookups) and
     are recorded with `bbg_budget.record("history-owed", <securities asked>, batch_id)`. A top-up row carries the
     currency found, NULL only when the lookup returned none for that security. If the currency request fails, no
     history request is sent, nothing lands, and the line reads `carried <all>` with the failure.
  3. **The printed line** in `ask` gains `; currency lookups <n>` after `asked <a>`; in `print` it gains
     `; currency lookups <n> (not sent)` computed from the stored currencies alone (no request).
  4. `price_date` on every top-up row stays as round 27 built it (the returned trading date; a close for a date not
     asked is not written).
  5. With the switch OFF nothing changes: `tw-1.AC1.py` still ends `PASS 0 failures` (it compares the OFF run with the
     module at commit 361b735308).
  6. **The cap (AMENDMENT 1, Andrew-direct ~17:1xZ via CTO msg 31926, ruling R24).** `HISTORY_OWED_CAP` becomes `20000`
     (an `int`): up to 20,000 units a run, each unit one security on one day, so at most 20,000 returned records. It is the
     only number that changes; `tw-1.AC1.py` arm (e), amended with this order, reads `20000`.
- Rulings at the cut (issuer): `HISTORY_OWED_CAP` is 20,000 by item 6 (ruling R24). Nothing here
  sets the switch: `ask` is set only after this cell is merged and RIV-tw-1's J1 is graded, where the vehicle reads it, in a pair. NOTHING in this cell or its checks calls a vendor: every check and test stubs the client hook and
  points the budget ledger at a temp directory. The cap counts history units only; the currency lookups are counted
  on top of it in the budget check.
- Rulings on the check drafter's questions (issuer): `_stored_currencies` is read from the window's first day THROUGH
  THE REPORT DATE, so a security the daily pull priced in this same run takes its currency from the object just written
  and is never looked up. The `currency lookups <n>` clause is OMITTED when n is 0, in `print` and in `ask` (as
  `misdated` and `failed` are): with both, round 27's `tw-1.AC2.py` still ends `PASS 0 failures` unchanged, and it must.
  The lookup is ONE reference request whose fields are exactly `["CRNCY"]`, recorded by its OWN `bbg_budget.record`
  call; a lookup that was sent and failed is recorded as spent, as `market-range` records it. After a failed lookup the
  line says `asked 0` and `carried <all>` and names the failure; the result dict's shape for that case is yours. Under
  the cap, lookups are counted over the securities of the capped units only. A security the lookup returned no currency
  for is looked up again on a later run (one point each time; stated for the cap's ruling). The read cost of
  `_stored_currencies` over the window is accepted in `ask` and in `print`.
- **Organic trigger:** none while the switch is OFF. THE VEHICLE RUNS THIS FILE FROM THE WORKING TREE: the merge is a
  deploy to the 11:00Z job, lands only after RIV-tw-1's J1 is graded on the 2026-10-09 run, and carries a pair.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 2dbad40215 or later)

- Read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tc-1.AC1.py` before you build, and round 27's `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tw-1.AC1.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tw-1.AC2.py`, which must both still end `PASS 0 failures` unchanged (tc-1.AC1 arm g runs tw-1.AC1; run tw-1.AC2 yourself).
- **THIS FILE IS RUN BY A SCHEDULED JOB FROM THE REPOSITORY'S WORKING TREE EVERY DAY** (`python -m rivalfunds.enrichment_bloomberg --mode daily`). With the switch unset nothing may change: `tw-1.AC1.py` compares the OFF run with the module at commit 361b735308, call for call.
- `enrichment_bloomberg.py`: round 27's `_history_owed` (the branch the switch opens), `_owed_line`, `_topup_table`; the hand-run `_market_range`, whose currency handling you follow: `_stored_currencies` first, then ONE `_blp_reference_data` request for the field `CRNCY` through `_blp_call` for the securities with none, counted in `bbg_budget.check_points` with the history points before any request.
- NEVER call a vendor: every test stubs the client hook and points `bbg_budget` at a temp directory, as the checks do. Never set `RIVALFUNDS_HISTORY_OWED` outside a test's own process environment.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~22/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r28tc1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the window ends on the page day; stored currencies used and only the missing ones looked up, in one CRNCY request before any history request and inside the budget check; a failed lookup sends nothing more; the printed clauses; `price_date` kept; the switch-OFF run unchanged (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tc-1.AC1.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real read, never by you): the first scheduled vehicle run after the merge shows the enrichment leg's lines and exit code unchanged with the switch unset. **AMENDMENT 2 (2.0.0_SA_COO~V1, 2026-10-09, same remedy as row Z-S79 on RIV-tw-1):** "the first scheduled vehicle run after the merge" means the first one that REACHED the enrichment leg -- its log carries the `RIVALFUNDS ENRICHMENT STEP` line, an enrichment exit code other than 97, and no vendor-session-failure line (`Failed to start session`, `session pool state=Failed`, `could not start blpapi session`, `"unreachable": true`). A run that did not reach the leg reads UNVERIFIABLE for J1, never PASS.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-tc-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/tc-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-tc-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~22/ETFS_RIVALS.TO-RIV-tc-1.a-top-up-close-is-stored-with-a-currency-and-the-owed-window-ends-on-the-page-day.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-tc-1.a-top-up-close-is-stored-with-a-currency-and-the-owed-window-ends-on-the-page-day`. Report once: each mechanical criterion's verdict line with the output above it; the judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; the lines of `_history_owed` you changed and why the OFF path is unchanged; the first and last dates `_stored_currencies` is read over; the budget count and the records one `ask` run makes on the check's fixture; the `tw-1.AC2.py` last line after your change; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.19 @2914a61989 (ADMITTED); decomposition v1.18 (round 28 appended). Source: ROUND_ANALYSIS.round22 ADDENDUM 6 @8ea0b4a05a and CTO msg 31885. Cell ids listed against all 124 existing order ids before naming (row Z-S74's remedy): aw-1 and tc-1 are unused. Chain `~22`, slot `~22`, position 1 of 1. Check drafted by a helper under the issuer's brief, merged @f3650a8bd9, re-run by the issuer at base 2dbad40215: tc-1.AC1 FAIL 5 (a to e; f, g, h PASS). The helper measured that the cell as first written breaks four arms of tw-1.AC2 (an exact line match and its budget counts); the cell's rulings (stored currencies read through the report date; the clause omitted at zero) keep it passing unchanged, measured on a simulated build. THE VEHICLE RUNS THIS FILE FROM THE WORKING TREE (rows Z-S62, Z-S72; CTO ruling 31596): the merge waits on RIV-tw-1's J1 (2026-10-09 11:00Z) and carries a pair.

**AMENDMENT 1 (issuer, 2026-10-08 ~18:2xZ, before any worker was spawned):** item 6 added -- `HISTORY_OWED_CAP` 20000, on Andrew's yes to the standing daily request ("Yes I like this strategy.", record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_171xZ_OPEN_CALLS_SIX_ANSWERED_AND_CELL_TRACKING_ASK.md` @e30fb3e610; CTO msg 31926, R24). `tw-1.AC1.py` arm (e) amended from 5000 to 20000 in the same commit, so at base it now FAILS 1 (e) and `tc-1.AC1.py` arm (g) with it: both grade the cap. The budget record stays in points requested; for a one-date request a security returns at most one record, so the recorded draw is an upper bound of the returned records, named as such in the switch-on pair. No gate limb graded this modification.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>28</round>
<slot>~22</slot>
<fabric>site-z</fabric>

<status>complete</status>
