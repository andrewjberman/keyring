# TO IRPT_DASHBD.TO-DB-b-171 -- read the ledger rows behind the 23 differing days of the 7 open windows: the served side's income and flow rows against Black Diamond's landed transaction rows, under a closed list written before the read, a reason taken only if correcting that row re-closes the window within 0.35 pp; a read, S3 GET/LIST only, no vendor call

<to_id>IRPT_DASHBD.TO-DB-b-171</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~137</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>91</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 7032, ROUND-91 ANALYSIS @3a44c65c3e section 3 item 2 | **Rows:** NONE | **Decomp cell:** `DB-b-171` (decomposition section 93) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-169 (drained @4008c3c432).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-137` (branch `wk-IRPT_DASHBD-137`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~137/`. Your private folder (client data lives only here, outside the repo) is
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~137/` (create it).

**Why.** Seven windows stay open after every window-level reason of rounds 89 and 90. The day read (`DB-b-169`) found 23 days that differ between our served daily return and Black Diamond's, none of which takes a reason: only 3 are flow days; on 12 days Black Diamond's income is a whole multiple (3x to 6x) of the served income; on 2 days Black Diamond's
flow is 3x or 4x the served flow. A whole multiple of income is the signature of a BOOKING difference, not of a return method. The CTO's ruling: read the rows. For each of the 23 days, the served side's income and flow rows against Black Diamond's landed transaction rows for the same account and day (and the adjacent trading days).

**The cell (`DB-b-171`).** A read and a private count. You change no served code and rule nothing beyond the closed list.
1. **Read the model first.** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~136/` (`RULE_DAY.md`, `day_reasons.py`, `DAY_READ_7.json`: the day rule, its tests and corrections, the 23 days per account in plan order; read-only), `tieout/tieout_day_read.py`, `tieout/tieout_neither_reasons.py`, and the private files of the issuer's pull
   `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~134/` (`DAY_READ_PLAN.json`: the 7 accounts and segments; `DAY_TABLE_7.json`: the daily table with each differing day; `pull/`: Black Diamond's daily series; all READ ONLY). The stored tables are in `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~108/`.
2. **The two sides' rows.** (a) BLACK DIAMOND's side: its landed transactions, `s3://opal-data-assets/blackdiamond/49financial/silver_legacy/transactions/` (the store `~108/read90.py` read; it kept 12 columns of it; you read ALL columns for the rows of the 7 accounts on each differing day and the adjacent trading days, five calendar days either side, S3 GET and LIST only).
   (b) The SERVED side: the ledger rows the gold producer builds `external_flow` and `income_received` from. Find them in the producer of `account_return_daily` (`data/assets/scripts/gold/irpt_reporting/`; read its inputs; the estate's graph tools `comp-which` and `comp-read <path> --for "<question>"` answer where a column comes from) and read those rows for the same accounts and days, S3 GET and LIST only. If the served rows are not readable with the AWS identity
   you hold, file a surprise row quoting the denial verbatim and stop that side: no other route. Row-level detail (security, lot, quantity, amount, date) lives ONLY in your private folder.
3. **The rule FIRST, committed before any read of a ledger row of the 7.** Before you open any transaction row for these accounts, write `RULE_LEDGER.md` in your folder and commit it alone. It states, so that another seat would count the same way, for EACH reason on the closed list below: its TEST (what in the two sides' rows makes it apply to the day, by column), and its CORRECTION (the single change at row level, made on the SIDE whose
   row is at fault) and how the day's and the window's figures are then recomputed (for Black Diamond's side, its published daily return `b(d)` with the faulty row's effect removed; for the served side, `day_reasons.py`'s recomputation of `c(d)`), so that the two corrected windows are compared at 0.35 pp with the same fee add-back as round 90. A reason is TAKEN by a day only if its test holds and correcting that row brings the day within the day-differs line (0.01 pp) AND the window then re-closes within 0.35 pp
   once every reasoned day is corrected. If the rule proves unworkable after the read starts, do NOT edit it: add a dated `RULE_LEDGER_ADDENDUM.md` and report both readings.
4. **THE CLOSED LIST (the CTO's, verbatim; the first reason whose correction takes the day, in this order):**
   `BD_INCOME_PER_LOT` (Black Diamond's rows for the day are split per lot and their sum equals the multiple of the served income) · `DUPLICATE_ROW` (the same amount, date and security appears twice on one side) · `BOOKING_DATE_DIFFERS` (the amount matches on an adjacent trading day) · `MISSING_IN_LEDGER` (a row in Black Diamond with no counterpart on the served side) · `UNEXPLAINED`.
   A reason is shown by a count, a multiple (as an integer) or day offsets from the stored rows, never asserted. No other reason may be used; a cause you think is missing is a surprise row.
5. **The count.** Reproduce the population first: 7 accounts, 7 windows, 23 differing days, per account in plan order exactly as `~136/DAY_READ_7.json` (the criterion binds them). Then per day apply the tests in order, correct, recompute, and per account decide whether the window re-closes. NEGATIVE ARM: every uncorrected window still misses 0.35 pp. Write ONE tracked module
   `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~137/ledger_rows.py` (ASCII, passes `bash .tools/commit-gate.sh`; run under `python -I`; prints COUNTS, OFFSETS, SIZES and multiples only).
6. **If any account stays UNEXPLAINED**, file ONE surprise row (`spec_asserts` + `world_is`, counts, multiples and offsets only) and put its id in `surprise_row`; the CTO then rules.
7. **Record** `LEDGER_ROWS_23_DAYS.json` in your folder, exactly these keys: `tolerance_pp` 0.35; `rule` {`file`: "RULE_LEDGER.md", `sha256` (of its committed bytes), `commit`, `written_before_read`: true}; `reasons_list` (the five names, in order); `code` {`file`, `sha256`, `tracked`: true}; `population` {`accounts`: 7, `windows`: 7, `differing_days`: 23};
   `sources` {`bd_transactions_rows_read`, `served_rows_read`} (integers above 0: the rows you read on each side); `per_account` (a list of 7, NO ids, plan order) each {`days_differing`, `by_reason` (the five names: int, summing to `days_differing`), `evidence` (for each reason above 0 except UNEXPLAINED: {`kind`: "count", "multiple" or "day_offsets", `values`: [ints]}), `unexplained_days`
   ([{`offset`, `size_pp`}], one per UNEXPLAINED day), `uncorrected_window_misses`, `window_closed_after_correction` (true exactly when no day is UNEXPLAINED and the window re-closes)}; `summary` {`accounts_closed_with_reasons`, `accounts_unexplained`}; `surprise_row` (only when an account is unexplained); `reads` {`vendor_calls`: 0, `secret_reads`: 0, `s3_writes`: 0}; `served_values_changed`: false; `limits`.
   NO account id, client name, security name, lot, amount, date with an account or run of eight or more digits in the record or your report.

<criterion id="DB91-1-AC1" cell_refs="DB-b-171"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r91/p91_round91.py" . DB91-1-AC1</invocation><expect>DB91-1-AC1 PASS</expect></criterion>
`DB91-1-AC1` -- the rule was committed before the read and its bytes are unchanged; the five-name list is exact; the code file is tracked; the population and the per-account differing-day counts equal round 90's committed record; both sides' rows read are counted; every account lists a five-way reason count summing to its differing days, evidence as a count, a multiple or day offsets, the UNEXPLAINED days by
offset and size, the negative arm true, and a window that is closed exactly when no day is UNEXPLAINED; the summary matches; a surprise row exactly when an account stays UNEXPLAINED; zero vendor calls, secret reads and S3 writes; no served value changed; no run of 8 or more digits. Base: FAIL.

<expected_criteria>DB91-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. Round 90's folder, the tie-out modules, the pulled responses and every stored table are READ ONLY.
- **No vendor call, no credential read, no session load.** You never run `tieout_day_read.py pull`, never call a Black Diamond endpoint, never read a cookie or credential file, never open a browser. The rows come from S3 reads only.
- **No served write.** S3 GET and LIST only, on the two stores named above; no put, copy or delete; no Lambda, Terraform or IAM act; no deploy; no push. A denial is recorded verbatim, not retried by another route.
- **No client data in what you write.** Counts, multiples, offsets and sizes only in the repo; row detail goes only to your private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only. Commit with `.tools/safe-commit.sh` as your definition says.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W137-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES, never re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~137/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-171.ledger-rows-behind-the-23-differing-days.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 93 (round 91), cell `DB-b-171`.
<owned_cells>DB-b-171</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB91-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~137/IRPT_DASHBD.TO-DB-b-171.ledger-rows-behind-the-23-differing-days.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB91-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the rule's commit (before the read); the rows read on each side (counts); per account (plan order, no ids): days differing, the five reason counts, closed or not, the UNEXPLAINED offsets and sizes; the evidence for each used reason (counts, multiples, offsets); which store the served rows came from and how you found it; the module's commit; any row ids. Counts, multiples, offsets and sizes only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a private read of two S3 stores and a counts-only record; nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; S3 GET and LIST of two named stores with the identity the earlier tie-out cells used; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record; 23 synthetic arms dry-run) and the analysis names the negative arm.
lane: the <paths> block IS the grant.
</preflight>
