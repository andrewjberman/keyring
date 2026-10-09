# TO IRPT_DASHBD.TO-DB-b-35 -- E1: build `account_activity_daily`, `account_lot_realized` and `account_lot_unrealized_daily` for 49 Financial and their contracts, run locally (FWD-4)

<to_id>IRPT_DASHBD.TO-DB-b-35</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~20</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-22 analysis @a1873a8be7 item E1 (PRD backlog B2):
"(1) for one account and one window: beginning value + contributions - withdrawals + realized + unrealized change + income = ending
value, within one cent, printed term by term; (2) each realized lot ties to its closing transaction in the silver transactions, with a
count of lots that do not tie and the reason for each; (3) every new address and name is `lib/opal_naming.py` output, printed (rule
30)"; "Pre-2010 dates raise (calendar coverage), and a lot opened before 2010 is listed, never estimated." | **Decomp cell:** `DB-b-35`
(decomposition section 23) | **outcome_ref:** FWD-4 | **depends_on:** none.

This order BUILDS and RUNS LOCALLY. It writes nothing to S3, deploys nothing and schedules nothing. The release of these tables is a
later packet under its own halves.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-20`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~20/`.

**The outcome (FWD-4):** a person sees realized gain, unrealized change and income for a window, and an activity summary whose figures
agree with the transactions for the same window. PRD C-SHAPE names three of the eight account-grain tables this cell builds; every table
carries `firm`, `account_id`, `method_version`, `coverage`, and ONE contract file per table under `org/standards/` named
`IRPT_DASHBD_<TABLE>_CONTRACT.json`, in the shape of `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json`. A firm that lacks a
field carries null plus a `coverage` value that says why (`NO_LOTS` is the PRD's own null reason for lot columns).

**Sources (49 Financial's custodian silver, read-only, readable from this box):** `s3://opal-data-assets/schwab/08335338/silver/` --
`fact_rld` (realized lots), `fact_uln` and `fact_ult` (unrealized lots: tax-status slices, DISJOINT by account), `fact_trn` (transactions),
`dim_position`, `dim_balance`. PRIOR ART, read it and do not edit it: `data/assets/scripts/gold/runners_49f/perfrp_emit_core.py`
(lines ~1608-1640 and its readers). It chose the cost-basis column BY MEASUREMENT (`cost_basis_unamortized`, the one satisfying
`current_market_value - cost_basis == unrealized_gain_loss`) and uses the custodian's holding-term flag `h_t` (L/S). The flows
(contributions, withdrawals) and income follow the served producer's own rules: `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`
(read, never edit) and its declaration `sources.json`. Confirm the RLD vintage you read (which silver `date=` partition) and print it.

**Calendar:** `lib/trading_calendar.py` raises for a date before 2010. A lot opened before 2010 is LISTED in the record with its dates,
never estimated.

**What you build:**
1. `data/assets/scripts/gold/irpt_reporting/account_activity_lots.py`: one producer for the three tables, beside the served producer,
   importing it read-only. A `--local` mode computes a sample, writes local parquet per table and the record below; it never writes S3.
2. `data/assets/scripts/gold/irpt_reporting/tests/test_account_activity_lots.py`: offline tests on synthetic inputs: the activity
   identity holds; a realized lot with no closing transaction is untied with a reason; a pre-2010 lot is listed, not estimated; a firm
   field absent is null with its coverage reason.
3. The three contract files under `org/standards/`.
4. One local run: account `acct#24ccad9d` plus at least 9 other accounts from the served producer's population, over the window
   2026-09-01..2026-10-05. Write `ACTIVITY_LOTS_LOCAL_RUN.json` with:
   - `reconciliation`: `{account_id, window, beginning_value, contributions, withdrawals, realized, unrealized_change, income,
     ending_value}` for ONE account and the window, each term the tables' own figure;
   - `lot_tie`: `{lots_total, tied, untied, untied_lots: [{lot_id, reason}]}` over every realized lot of the sample in the window, each
     tied to its closing transaction in `fact_trn`;
   - `builder_output`: `[{call: {fn: "address"|"name", args: [...]}, output}]` for every new address and name (each table's gold
     address at least), the output exactly as `lib/opal_naming.py` returns it;
   - `rld_vintage` and `pre_2010_lots` (listed).
   Write a summary `ACTIVITY_LOTS_LOCAL_RUN.md`, COUNTS ONLY.

<criterion id="DB23-1-AC1" cell_refs="DB-b-35"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r23/p23_activity_lots.py" . DB23-1-AC1</invocation><expect>DB23-1-AC1 PASS</expect></criterion>
`DB23-1-AC1` -- one account-window ties term by term within one cent, every term printed. Base: FAIL.

<criterion id="DB23-1-AC2" cell_refs="DB-b-35"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r23/p23_activity_lots.py" . DB23-1-AC2</invocation><expect>DB23-1-AC2 PASS</expect></criterion>
`DB23-1-AC2` -- every realized lot is tied to its closing transaction or counted untied with its reason. Base: FAIL.

<criterion id="DB23-1-AC3" cell_refs="DB-b-35"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r23/p23_activity_lots.py" . DB23-1-AC3</invocation><expect>DB23-1-AC3 PASS</expect></criterion>
`DB23-1-AC3` -- every new address and name re-derives from `lib/opal_naming.py`, the three table addresses among them. Base: FAIL.

<expected_criteria>DB23-1-AC1,DB23-1-AC2,DB23-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. `account_return_daily.py`, its handler and `perfrp_emit_core.py` are read, never edited.
- **AWS:** S3 reads only. No write, no upload, no Lambda, no schedule, no vendor call. No bun (this cell runs Python only).
- **Refusal clause.** An S3 write, an edit to a served producer, an estimated pre-2010 lot, a hand-typed address, or a client figure in
  a committed `.md` is a defect: stop and file a row.

<paths>
data/assets/scripts/gold/irpt_reporting/account_activity_lots.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_activity_lots.py
org/standards/IRPT_DASHBD_ACCOUNT_ACTIVITY_DAILY_CONTRACT.json
org/standards/IRPT_DASHBD_ACCOUNT_LOT_REALIZED_CONTRACT.json
org/standards/IRPT_DASHBD_ACCOUNT_LOT_UNREALIZED_DAILY_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~20/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-35.activity-and-lot-tables.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 23 (round 23, workstream B), cell `DB-b-35`.
<owned_cells>DB-b-35</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB23-1-AC1, DB23-1-AC2, DB23-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~20/IRPT_DASHBD.TO-DB-b-35.activity-and-lot-tables.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB23-1-AC1,DB23-1-AC2,DB23-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line (AC1's seven terms), the sample, the RLD vintage, the lot-tie counts and reasons,
the pre-2010 lots listed, the builder output, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a new producer file beside the served ones and three new contracts; nothing served is read-modified or written; no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB23-1-AC1, AC2 and AC3 base FAIL (no record), dry-run at base f9386e5865 2026-10-07 ~13:4xZ; the builder control address("irpt","49financial","gold","account_activity_daily","date=2026-10-05") returns s3://opal-data-49financial/irpt/49financial/gold/account_activity_daily/date=2026-10-05.
lane: the <paths> block IS the grant.
</preflight>
