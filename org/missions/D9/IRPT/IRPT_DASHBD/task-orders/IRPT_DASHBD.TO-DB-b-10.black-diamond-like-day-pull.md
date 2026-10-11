# TO IRPT_DASHBD.TO-DB-b-10 -- ONE Black Diamond pull over Opal's gap-free segments for the five round-1 accounts, and the tie-out on like day sets

<to_id>IRPT_DASHBD.TO-DB-b-10</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** ANDREW-DIRECT ~13:2xZ "all recs approved", card 4
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261002_132xZ_ALL_RECS_APPROVED_OPEN_CALLS.md`, @0abef798f7; relayed by
1.0.0_SA_CTO msg 104263: "cut it as an IRPT_DASHBD cell under Rule 27, with no seat calling the vendor outside it") | **Decomp cell:**
`DB-b-10` (decomposition section 4) | **outcome_ref:** FWD-8 | **depends_on:** none

---

## WORKER FACE

**The word, verbatim scope and no wider.** Andrew approved ONE Black Diamond pull, scoped to the five IRPT_DASHBD round-1 accounts:
BD's return over each of Opal's gap-free segments. It is not a standing grant. That means one pull, those accounts and those
windows, and no other vendor call by anyone, before or after this cell.

**The cell.** PRD v0.6 ruling 23 (`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md`, ADDENDUM v0.6): the tie-out grades
AGREEMENT only on like day sets. A pair counts only where Opal's linked days equal BD's `daysHeld`. Round 1 had zero such pairs out
of five (`deliverables/0.4.0_DS_ClientPlatform~S/tieout/TIEOUT_49F_BLACKDIAMOND_R1.{md,json}`). This cell makes like pairs by
construction: it asks BD for its return over windows where Opal withheld no day.

**The five accounts:** acct#89d0916a, acct#f08ffd13, acct#6b914f88, acct#ffa615d2, acct#d0cf6c92.
- The BD id comes from `s3://opal-data-assets/blackdiamond/49f/_ops/taxsma_roster.json` (bd_internal_id -> schwab_account), as
  TO-DB-b-3 did.
- In round 1, acct#f08ffd13 and acct#d0cf6c92 were `pending_resolution` with no BD id. An account with no BD id is recorded as unmapped,
  with the reason, and is never guessed.

**Steps.**
1. **Segments (reads only).** From the served reporting gold `account_return_daily` (builder address `lib/opal_naming.py address("irpt",
   "49financial", "gold", "account_return_daily", "date=<d>")`), find each mapped account's GAP-FREE segments. A segment is a
   maximal run of consecutive trading days (`lib/trading_calendar.py`) whose `total_return_daily` is non-null. `opal_linked_days`
   is the segment's trading-day count, and `opal_twr` is the geometric link of its daily returns. Keep segments of at least 5
   trading days.
2. **THE ONE PULL.** One session; for each mapped account, at most ONE `performancePeriod` request carrying all of that account's
   segments as ranges.
   - Use the estate's client:
     - `infra/aws/lambda/investor-reporting/performance/bd_adapter.py` for `build_period_request` and `parse_period`; it loads the
       proven request body from `infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py`;
     - `infra/aws/lambda/investor-reporting/performance/tenants.py` for 49 Financial's route and session, the
       `blackdiamond/49f/session` secret.
   - Put the pull in one script in your deliverables folder. It reads the segments, makes the calls, and writes the records.
   - Run it ONCE. A failed call is recorded with its status and is not retried in a loop. One retry of one transport error is
     allowed and counted in `vendor_calls`.
3. **The tie-out.** For each (account, segment):
   - `bd_twr` is BD's `timeWeightedReturns.return` (a decimal fraction) for that range, and `bd_days_held` is BD's `daysHeld`;
   - `like_days` is `opal_linked_days == bd_days_held`;
   - `abs_diff` is `|opal_twr - bd_twr|`.
   - The summary gives the like-day pairs' count, median and max `abs_diff`. Unlike pairs report COVERAGE beside the difference, as
     ruling 23 says.

**Records (your deliverables folder `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/`).**
- `BD_LIKEDAY_PULL_R4.json`:
  `{"word": "@0abef798f7 card 4", "endpoint": "performancePeriod", "accounts_in_scope": [the five], "requests": [{"account",
  "bd_account", "ranges": [{"start","end"}], "http_status"}], "vendor_calls": n, "unmapped": [{"account","reason"}]}`.
  No credential, cookie or token is written anywhere.
- `TIEOUT_49F_BLACKDIAMOND_R4.json`:
  `{"pairs": [{"account","bd_account","start","end","opal_linked_days","bd_days_held","like_days","opal_twr","bd_twr",
  "abs_diff"}], "like_day_pairs": n, "summary": {...}}`.
- `TIEOUT_49F_BLACKDIAMOND_R4.md`: the table and one paragraph, with no claim beyond the numbers.
- The raw responses go in the same folder, with no account names beyond the ids above.

<criterion id="DB4-1-AC1" cell_refs="DB-b-10"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r4/p4_1_ac1_one_pull_in_scope.py" .</invocation><expect>DB4-1-AC1 PASS</expect></criterion>
`DB4-1-AC1` -- the one pull stayed in scope. The accounts are exactly the five; each requested account appears at most once;
`vendor_calls` equals the requests and is at most 5; every range is a tie-out pair; every unrequested account is unmapped with a
reason. Base: FAIL (no record).

<criterion id="DB4-1-AC2" cell_refs="DB-b-10"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r4/p4_1_ac2_like_day_pairs.py" .</invocation><expect>DB4-1-AC2 PASS</expect></criterion>
`DB4-1-AC2` -- every pair is gap-free by the trading calendar; `like_days` and `abs_diff` are what they say; the like-day count
matches. Base: FAIL (no record).

<expected_criteria>DB4-1-AC1,DB4-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** reads only (gold, roster, the session secret). Nothing is written to S3. No deploy, no Lambda invoke.
- **Vendor:** the one pull above and NO other call. The adapter's other surfaces (`performanceSeries`, any other endpoint) are not
  called.
- **Refusal clause.** If BD's `daysHeld` convention cannot match Opal's trading-day count on any window (a systematic offset), file
  a row with the measured offset. Never re-define `like_days` to make pairs match. An account with no BD id is unmapped, never
  guessed. A segment the gold cannot support is a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r4/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/performance/`, `infra/aws/lambda/opal-assets/`, `lib/`,
`data/assets/scripts/gold/irpt_reporting/`, `org/missions/D9/IRPT/IRPT_DASHBD/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 4 (round 4, workstream B), cell `DB-b-10`.
<owned_cells>DB-b-10</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB4-1-AC1, DB4-1-AC2. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/IRPT_DASHBD.TO-DB-b-10.black-diamond-like-day-pull.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB4-1-AC1,DB4-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- `vendor_calls`, the mapped and unmapped accounts;
- the like-day pairs with their `abs_diff`, and the median and max;
- any surprise row id (`IRPT_DASHBD-W1-S<k>`).

---

## RECORD FACE

<preflight>
comp-blast: RUN -- reads only on Opal; one vendor read (performancePeriod) under Andrew's per-use word; 0 served bytes move; the records feed FWD-8's grade at L9.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes; the seat's own credentials read the gold, the roster and the session secret.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: one ad hoc measurement run under a per-use vendor word; no schedule, trigger or cron is created or moved.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB4-1-AC1 base FAIL (no record), DB4-1-AC2 base FAIL (no record), dry-run at the base 2026-10-02 ~15:2xZ.
lane: the <paths> block IS the grant.
</preflight>
