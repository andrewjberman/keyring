# ETFS_RIVALS task order -- `RIV-ho-1` -- ROUND 27: THE HISTORY-OWED SET, FROM STORED TABLES ALONE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-ho-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~18</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (a new read-only module; it reads prefixes the daily Lambda already reads)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files, the CTO's rulings of 2026-10-07 on round 25 and the rows they cite
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. Round 15 moved every period on the page to the last 30 / 90 / 365 calendar days. The buying trend shows, beside its net figure, a month-by-month strip (bought / sold / no trade per month). Each security dialog also lists the fund's trades in the security and draws a price chart by the page's one inline script. A security named in a table or in an account's text is a button that opens that security's one dialog, which carries a section per fund. The page's price charts and rankings read closes from the gold table `security_market`, which today holds five trading days. PRD outcome FWD-24: every security a tracked fund held in the last 365 days has its year of closes, kept by the daily Bloomberg leg, which prints what is owed, asks inside the budget and carries the rest. **This order, round 27, is one of three cells of that outcome; the standing request to the vendor stays OFF in everything you build and test.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-ho-1` -- the history-owed set: every (security, trading day) of the last 365 days with no stored close, computed from stored tables alone (FWD-24, PRD v0.19 C-HISTORY-OWED)
- Measured (the CRO's analysis behind ADDENDUM G; live read by the issuer 2026-10-08): gold `security_universe` holds
  1,051 securities with `first_seen`, `last_seen` and `funds` (a comma-joined list of fund tickers); gold
  `security_market` holds closes on 5 trading days. Nothing computes what is owed.
- Interface (a NEW module `data/etfs/scripts/rivalfunds/history_owed.py`; standard library, pandas and the package's own
  readers only; NO vendor import and no network call but the sink's):
  1. `history_owed.owed(s, day, window_days=365)` -> a pandas DataFrame, one row per owed unit, columns `security_id`,
     `security_bloomberg`, `date` (ISO string), `funds`. A unit is owed when: the security is in the newest
     `security_universe` object at or before `day` with a non-blank `security_bloomberg`; `date` is a trading day
     (`lib.trading_calendar`) with `day - window_days <= date <= as_of(day)` where `as_of(day)` is the previous trading
     day of `day`; `first_seen - window_days <= date` is NOT required (a security held at any time in the window is owed
     its whole window: the PRD's "every security a tracked fund held in the last 365 days has its year of closes"), but
     the security's `last_seen` is on or after `day - window_days`; and `hc.g4_window` over the window returns no row for
     (`security_id`, `date`) whose `px_close` is not null. Rows sorted by `date` descending, then `security_id`.
  2. `history_owed.summary(df)` -> a dict `{"securities": n, "units": n, "dates": n, "newest": iso, "oldest": iso}`
     (zeros and None for an empty frame).
  3. A unit whose only stored close sits in an object the shared reader does not read (an untimed object beside timed
     ones; the mis-dated 2026-09-29 object) IS owed: the set is defined by what the readers return, not by what S3 holds.
- Rulings at the cut (issuer): the unit of the budget is this row (one security on one day). Cash lines and securities
  with no Bloomberg key are not owed (there is nothing to ask). The function writes nothing.
- Rulings on the check drafter's questions (issuer): `first_seen` is no bound at all -- a security whose `last_seen` is on
  or after `day - window_days` (inclusive) is owed every trading day of the window through `as_of(day)`, before its
  `first_seen` and after its `last_seen` included; the window's first day is inclusive; "the newest universe object at
  or before `day`" includes one dated `day`; `day` is an ISO string and `s` the sink; a blank key includes a
  whitespace-only one (`hc._blank`); an empty result still carries the four columns; `date` is an ISO string.
- **Organic trigger:** the issuer's real read prints `summary(owed(s, day))` for the live tables.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 66cab2698e or later)

- Read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/ho-1.AC1.py` before you build: its docstring is the exact interface it reads and its fixture shows the tables.
- gold `security_universe` (`gold_security_universe.py`): one object per date, `universe-<rev>.parquet` under `homes.address("rivalfunds", "etfs", "gold", "security_universe", "date=<D>")`, columns `security_id`, `security_bloomberg`, `first_seen`, `last_seen`, `funds` and others; read the newest object of a date with `gold_holding_contribution._newest_by_date`.
- gold `security_market`: read it ONLY through `gold_holding_contribution.g4_window(s, lo, hi, columns=None)` (the shared reader: it returns the rows the product's stages read, one per security and date).
- `lib.trading_calendar`: `prev_trading_day` and the calendar's trading-day test, as the other stages import it (`_tc()` in `gold_holding_contribution.py`).
- Your module must import nothing of `enrichment_bloomberg`, `collector_bloomberg`, `bbg_budget` or any vendor or network library.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~18/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r27ho1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing; read the file's existing row ids first and take an unused one), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/history_owed.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the owed set on a fixture: the trading days with no stored close, per security; the universe's bounds; closes the readers do not read leave a unit owed; shape, order, summary; nothing written, no vendor import (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/ho-1.AC1.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real read, never by you): on the live tables the printed summary is plausible against the PRD's measurement (761 securities in a fund's reports in the last year, 5 trading days of closes) and three units picked by hand are truly without a stored close.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-ho-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/ho-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-ho-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~18/ETFS_RIVALS.TO-RIV-ho-1.the-history-owed-set-from-stored-tables-alone.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-ho-1.the-history-owed-set-from-stored-tables-alone`. Report once: each mechanical criterion's verdict line with the output above it; the judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; the function's signature and each bound it applies, one line each; how many sink reads one call makes on the check's fixture; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.19 @2914a61989 (ADMITTED); decomposition v1.17 (round 27 appended). Source: PRD ADDENDUM G (FWD-24), ROUND_ANALYSIS.round22 ADDENDUM 4 and CTO ruling R13. Chain `~18`, slot `~18`, position 1 of 1. Check drafted by a helper under the issuer's brief (@80327807d9), re-run by the issuer at base 66cab2698e: ho-1.AC1 FAIL 8 (arms a to h: the module does not exist; the control i PASSES). The helper's simulated module passes; three planted defects fail the arms that grade them.

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>27</round>
<slot>~18</slot>
<fabric>site-z</fabric>
