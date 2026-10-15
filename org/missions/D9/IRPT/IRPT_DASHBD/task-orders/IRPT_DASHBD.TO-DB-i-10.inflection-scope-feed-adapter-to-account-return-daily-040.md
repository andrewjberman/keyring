# TO IRPT_DASHBD.TO-DB-i-10 -- the SCOPE FEED ADAPTER: a pure transform from the Scope feed's silver rows (calendar days, daily factor, RETURNED / ABSENT) to rows of account_return_daily 0.4.0, on the CTO's round-118 ADDENDUM 4 rules; offline, synthetic tests, no I/O

<to_id>IRPT_DASHBD.TO-DB-i-10</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~310</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>123</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_118_20261015.md` ADDENDUM 4 (msg 8542 answered) and `2.0.0_SA_COO~D2` msg 8574 ("Contract 0.4.0 is merged ... Cut your adapter cell on it").

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-310`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~310/`. Never touch a path outside the `<paths>` block below.

**Why.** Inflection's account pages say "Account-level returns are not available for this firm yet." A feed (built by another seat) lands Orion's own account-level return as silver rows, one per account per CALENDAR day. The account pages read `account_return_daily`, whose `business_date` is the TRADING day and whose `account_id` is the dimension's form. This module is the join between the two: it is the only code that turns feed rows into contract rows. It runs offline on rows handed to it; the run against the real feed is a later cell.

**What you build (two files, no more).**
1. `data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_adapter.py` -- standard library only (no pandas, no boto3, no network, no file or AWS access, no import from `lib/`; the module does no I/O at all).
2. `data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_adapter.py` -- pytest, synthetic rows only (no real account, no client value, no real household), at least 10 tests, one of them named `test_mutant_...`.

**Read first (read only).** `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` (version 0.4.0: `columns`, `optional_columns`, `enums`, `source_rules.orion`); `data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_040.py` (the validator `row_problems(contract, row)` your rows must pass); the checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r123/p123_adapter.py` (its synthetic world, `feed()` and `expected()`, is the golden your module must reproduce exactly; read it before you write code and run it as you go).

**The cell (`DB-i-10`).** Text of the owned cell: *"The Scope feed adapter: a pure function from the feed's silver rows, an Orion-to-dimension account map and the sorted trading-day list to contract-0.4.0 rows of `account_return_daily`, with `business_date` the trading day (each non-trading calendar day's factor compounded into the next trading day), an ABSENT trading day kept ABSENT, `account_id` mapped through the dimension with Orion's id in `source_account_id`, an unmapped account written ABSENT `UNMAPPED_ACCOUNT` and counted, and a run manifest."*

### The function

`adapt(feed_rows, account_map, trading_days, firm, method_version, schema_version="1.2")` returns a dict `{"rows": [...], "absent": [...], "manifest": {...}}`.

- `feed_rows`: a list of dicts with the feed silver keys `day` (ISO `YYYY-MM-DD`), `account_id` (Orion's id; `str(int(x))` of it is the key form), `status` (`RETURNED` or `ABSENT`), `reason_class`, `daily_factor`, `start_market_value`, `end_market_value`, `fee_basis`, `calc_gross_of_fees`. A value may be `None` or NaN: both mean absent, never zero.
- `account_map`: dict `{orion id (str): dimension account_id (str)}`. An account is MAPPED when its key is present.
- `trading_days`: ascending, unique ISO strings (the performance axis; the caller supplies them, you never read a calendar).
- Raise `ValueError` if `trading_days` is not strictly ascending, or if ANY feed row has `calc_gross_of_fees` true (the feed is NET; a gross row is refused, not converted).

### The rules (the checker's golden is these rules run on a synthetic world)

Let `min_day` and `max_day` be the smallest and largest `day` in `feed_rows`. The output domain is the trading days `t` with `min_day <= t <= max_day`. For each account in the feed (key `str(int(account_id))`) and each such `t`, in this order:

1. **Unmapped account** -> NO row; one `absent` record with `reason_class` `UNMAPPED_ACCOUNT` for that `t`, `source_account_id` None (Orion's id is not written for an unmapped account).
2. **Own row not usable.** The account's feed row on `t` is missing, or its status is not `RETURNED`, or its factor is null -> `absent` record, `reason_class` = that row's own `reason_class` when it has one, else `NO_FEED_ROW`. Weekend or holiday factors are NEVER moved onto an ABSENT trading day.
3. **The window.** `prev` = the previous trading day in `trading_days` (None for the first). The window is every calendar day `d` with `prev < d <= t` and `d >= min_day`. The account's first RETURNED day is `first`; a window day before `first` is skipped (the series had not begun). Any other window day whose row is missing, not RETURNED or without a factor -> `absent` record `INCOMPLETE_WINDOW` (no fill, no assumption of 1).
4. **The factor.** The product of the window's usable factors; `total_return_daily` = product - 1.0 (a float). `carried_days` = the number of window days used.
5. **`market_value_eod`.** The `start_market_value` of the account's row on the calendar day AFTER `t`, if that row is RETURNED and the value is not null; else `t`'s own `end_market_value` if not null; else `absent` record `NO_EOD_VALUE`. (Basis: a day's end value is the next day's start value; the feed carries `end_market_value` only on its last day. The manifest says this is inferred.)
6. **A row** carries exactly the contract's 19 columns plus the optional `source`, `flow_claim`, `source_account_id`: `firm` (the argument), `account_id` (the mapped dimension id), `business_date` `t`, `market_value_eod`, `external_flow` None, `income_received` None, `income_return` None, `total_return_daily`, `return_basis` `TWR`, `holdings_price_return` None, `holdings_price_return_reason` None, `fee_amount` None, `fee_amount_reason` `FEE_RAIL_UNUSED`, `day_quality` `MEASURED`, `guard_state` `GUARD_NOT_REACHED`, `history_scope` `PARTIAL_HISTORY`, `carried_days`, `method_version` (the argument), `schema_version` (the argument), `source` `orion`, `flow_claim` `absent`, `source_account_id` `int(orion id)`. Rows sort by `(account_id, business_date)`.
7. **An `absent` record** is `{"account_id": <orion id string>, "source_account_id": <int or None>, "business_date": t, "reason_class": <class>}` (an int for a mapped account, None for an unmapped one). Reason classes used: the feed's own (`NO_GROUP`, `GROUP_NO_SERIES`, `NO_START_DATE_AT_SOURCE`, `SERIES_ENDED_AT_SOURCE`, passed through), `UNMAPPED_ACCOUNT`, and three this module adds: `NO_FEED_ROW`, `INCOMPLETE_WINDOW`, `NO_EOD_VALUE`. A trading day is in `rows` or in `absent`, never both, never neither.
8. **The manifest** (dict): `accounts_in_feed`, `accounts_mapped`, `accounts_unmapped`, `rows` (the row count), `absent_by_reason` (a dict of counts over the absent records), `calendar_days_compounded` (the sum over rows of `carried_days - 1`), and three strings of words (20 characters or more each): `compounding` (states that each non-trading calendar day's factor is multiplied into the next trading day's factor and that an ABSENT trading day stays ABSENT), `market_value_basis` (rule 5, marked inferred), `fee_basis` (names `NET`).

### The tests

Your own synthetic world (do not copy the checker's data; different accounts and days). Cover: a weekend compounded into Monday; a holiday; an ABSENT trading day beside returned weekend days; a series that starts mid-window; an interior gap; an unmapped account; `SERIES_ENDED_AT_SOURCE` pass-through; both EOD-value branches and `NO_EOD_VALUE`; a None and a NaN factor; the two `ValueError` refusals; every output row validated by `row_problems` imported from the contract test module; and `test_mutant_...`: take the module's source text, change ONE rule (for example replace the multiplication `factor *= ...` of the compounding loop with an assignment), execute the mutated source, and assert its output differs from the real module's on your weekend case. ASCII only. Run `python -I -m pytest -q <your test file>` until green.

<criterion id="DBI123-1-AC1" cell_refs="DB-i-10"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r123/p123_adapter.py" . DBI123-1-AC1</invocation><expect>DBI123-1-AC1 PASS</expect></criterion>
`DBI123-1-AC1` -- the module reproduces the checker's golden: the trading-day compounding with its `carried_days`, an ABSENT trading day kept ABSENT, leading days skipped, the interior gap, `UNMAPPED_ACCOUNT` (no row, no source id), `SERIES_ENDED_AT_SOURCE` pass-through, the EOD value rule and `NO_EOD_VALUE`, and the manifest counts. Base: FAIL (no module).

<criterion id="DBI123-1-AC2" cell_refs="DB-i-10"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r123/p123_adapter.py" . DBI123-1-AC2</invocation><expect>DBI123-1-AC2 PASS</expect></criterion>
`DBI123-1-AC2` -- every output row has exactly the contract's columns and optional columns, passes `~D2`'s declarations-driven validator for contract 0.4.0, carries `source` `orion`, `flow_claim` `absent`, null flows and an int `source_account_id`; the validator is live (an Orion row with a null flow and no claim, and a claim beside both flows, are refused); the module refuses a gross-of-fees row and an unsorted calendar with `ValueError`. Base: FAIL (no module).

<criterion id="DBI123-1-AC3" cell_refs="DB-i-10"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r123/p123_adapter.py" . DBI123-1-AC3</invocation><expect>DBI123-1-AC3 PASS</expect></criterion>
`DBI123-1-AC3` -- your test file exists, names a `test_mutant_` test, and passes under `python -I -m pytest -q` with at least 10 tests passed. Base: FAIL (no test file).

<expected_criteria>DBI123-1-AC1,DBI123-1-AC2,DBI123-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the contract, `~D2`'s test module, `lib/`, `infra/`, the feed script, the other adapters and every issuer check.
- **No I/O.** The module opens no file, makes no network or AWS call, reads no calendar, no clock and no environment variable; its only imports are the standard library. The tests write nothing outside pytest's temp area.
- **Client data.** None. Every row in your tests and record is synthetic; no run of 8 or more digits in anything you write except a `sha256` value or a path.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A rule that seems wrong, or a case the rules do not cover, is a surprise ROW and you keep the rule as written; never invent a reason class or a fill.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W310-S<k>`, with the real current UTC time (`date -u +%FT%TZ`, run at filing; never typed by hand); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_adapter.py
data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_adapter.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~310/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-10.inflection-scope-feed-adapter-to-account-return-daily-040.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 9, cell `DB-i-10`.
<owned_cells>DB-i-10</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI123-1-AC1, DBI123-1-AC2, DBI123-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~310/IRPT_DASHBD.TO-DB-i-10.inflection-scope-feed-adapter-to-account-return-daily-040.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI123-1-AC1 DBI123-1-AC2 DBI123-1-AC3` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the three criteria's last lines; the number of tests passed; any case the rules did not cover (as row ids); the line count of the module. No client value, no account or household id, no date.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one new pure module and its test file; nothing is wired, scheduled, served or deployed, and no existing file is edited.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call, no secret, no grant; the module does no I/O.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; all three criteria FAIL at base (no module), the checker passed a reference implementation of the rules on AC1 and AC2, and six single-rule mutants of that reference (no compounding, leading days not skipped, unmapped dropped, claim removed, gap filled, a guessed source id) each failed the checker before the cut.
</preflight>
