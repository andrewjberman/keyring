# TO IRPT_DASHBD.TO-DB-b-172 -- test one more reason on the 23 differing days of the 7 open windows: BD_EXCLUDES_SERVED_INCOME (the gap equals minus the served income over the prior value), its rule committed before the read, the day corrected and the window re-closed at 0.35 pp or not; the other days re-tested under the full list with Reading B; a read, S3 GET/LIST only

<to_id>IRPT_DASHBD.TO-DB-b-172</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~138</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>92</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 7063, ROUND-92 ANALYSIS @a862a037f3 section 3 item 2 | **Rows:** NONE | **Decomp cell:** `DB-b-172` (decomposition section 94) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-171 (drained @09d0ebc99a).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-138` (branch `wk-IRPT_DASHBD-138`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~138/`. Your private folder (client data lives only here, outside the repo) is
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~138/` (create it).

**Why.** Seven windows stay open. Round 91 read the ledger rows behind their 23 differing days and no reason on its list took a day. It measured a pattern: on 8 of the 12 days where Black Diamond's income is a whole multiple of the served income, the day gap (Black Diamond's daily return minus ours) equals minus the served income over the prior day's value, to within 0.01 pp. That is the signature of Black Diamond's day
return EXCLUDING an income that our return includes (it recognises the income on another day, or treats it as leaving the account). The CTO's ruling: test that as a reason, written before a fresh read; take it only if removing that income from the served day re-closes the window; re-test the other days under the full list after.

**The cell (`DB-b-172`).** A read and a private count. You change no served code and rule nothing beyond the closed list.
1. **Read the model first.** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~137/` (`RULE_LEDGER.md`, `RULE_LEDGER_ADDENDUM.md` (Reading B, adopted by the CTO as the reading of record), `ledger_rows.py`, `LEDGER_ROWS_23_DAYS.json`), `deliverables/0.9.0_WK_IRPT_DASHBD~136/` (`RULE_DAY.md`, `day_reasons.py`, `DAY_READ_7.json`: the day rule, the gap, the day-differs line 0.01 pp and the window test),
   `tieout/tieout_day_read.py`, `tieout/tieout_neither_reasons.py`; and the private files of the issuer's pull `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~134/` (`DAY_READ_PLAN.json`, `DAY_TABLE_7.json`, `pull/`) and the stored tables of `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~108/`. All READ ONLY.
2. **The rule FIRST, committed before the read.** Before you compute anything on the 23 days, write `RULE_EXCL.md` in your folder and commit it alone. It states, so that another seat would count the same way: the TEST of `BD_EXCLUDES_SERVED_INCOME` (on the day, `gap = b(d) - s(d)` in return units equals `- a(d) / m(d)` within 0.01 pp, with `a(d)` the served income received that day, `m(d)` the prior day's value,
   both as `RULE_DAY.md` defines them; and what happens when `a(d)` is zero or `m(d)` is not applicable: the test does not hold); its CORRECTION (remove that income from the served day's return, and say in a line how, so that the corrected day moves toward Black Diamond's by the income's share of the prior value); and, for the other four reasons, that they are `~137`'s tests and corrections with `BD_INCOME_PER_LOT` read as Reading B (the addendum).
   A day takes the FIRST reason on the list whose test holds and whose correction brings the day within the day-differs line (0.01 pp) of Black Diamond's; the window is then tested once, with every reasoned day corrected, at 0.35 pp. If the rule proves unworkable after the read starts, do NOT edit it: add a dated `RULE_EXCL_ADDENDUM.md` and report both readings.
3. **THE CLOSED LIST (fixed by the issuer from the CTO's ruling; the first reason that takes the day, in this order):** `BD_EXCLUDES_SERVED_INCOME` · `BD_INCOME_PER_LOT` (Reading B) · `DUPLICATE_ROW` · `BOOKING_DATE_DIFFERS` · `MISSING_IN_LEDGER` · `UNEXPLAINED`. A reason is SHOWN by a count, a multiple (an integer) or day offsets from the stored rows, never asserted. No other reason may be used; a cause you think is missing is a surprise row.
4. **The count.** Reproduce the population first: 7 accounts, 7 windows, 23 differing days, per account in plan order exactly as `~136/DAY_READ_7.json`. Record `test_held_days`: on how many of the 23 days the new reason's TEST holds (before any window test), and `round91_pattern_8_days_confirmed`: whether that equals the 8 days worker 137 measured (state the difference if not; it is a finding, not a failure).
   Then per day apply the list in order, correct, recompute, and per account decide whether the window re-closes. The other days are re-tested under the full list after the new reason's days are corrected; re-reading the rows of the two stores for that re-test is allowed (S3 GET and LIST only, as `~137` did; you may import `ledger_rows.py` by path and use its functions; do not edit it).
   NEGATIVE ARM: every uncorrected window still misses 0.35 pp. Write ONE tracked module `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~138/excl_income.py` (ASCII, passes `bash .tools/commit-gate.sh`; run under `python -I`; prints COUNTS, OFFSETS, SIZES and multiples only).
5. **If any account stays UNEXPLAINED**, file ONE surprise row (`spec_asserts` + `world_is`, counts, multiples and offsets only) and put its id in `surprise_row`; the CTO then rules on the endpoint.
6. **Record** `EXCLUDES_INCOME_23_DAYS.json` in your folder, exactly these keys: `tolerance_pp` 0.35; `rule` {`file`: "RULE_EXCL.md", `sha256` (of its committed bytes), `commit`, `written_before_read`: true}; `reasons_list` (the six names, in order); `code` {`file`, `sha256`, `tracked`: true}; `population` {`accounts`: 7, `windows`: 7, `differing_days`: 23};
   `test_held_days`; `round91_pattern_8_days_confirmed` (bool); `sources` {`bd_transactions_rows_read`, `served_rows_read`} (integers above 0: the rows you read on each side for the re-test); `per_account` (a list of 7, NO ids, plan order) each {`days_differing`, `by_reason` (the six names: int, summing to `days_differing`), `evidence` (for each reason above 0 except UNEXPLAINED: {`kind`: "count", "multiple" or "day_offsets", `values`: [ints]}),
   `unexplained_days` ([{`offset`, `size_pp`}], one per UNEXPLAINED day), `uncorrected_window_misses`, `window_closed_after_correction` (true exactly when no day is UNEXPLAINED and the window re-closes)}; `summary` {`accounts_closed_with_reasons`, `accounts_unexplained`}; `surprise_row` (only when an account is unexplained); `reads` {`vendor_calls`: 0, `secret_reads`: 0, `s3_writes`: 0}; `served_values_changed`: false; `limits`.
   NO account id, client name, security name, lot, amount, date with an account or run of eight or more digits in the record or your report.

<criterion id="DB92-1-AC1" cell_refs="DB-b-172"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r92/p92_round92.py" . DB92-1-AC1</invocation><expect>DB92-1-AC1 PASS</expect></criterion>
`DB92-1-AC1` -- the rule was committed before the read and its bytes are unchanged; the six-name list is exact; the code file is tracked; the population and per-account differing-day counts equal round 90's committed record; `test_held_days` is an integer and the days taken by the new reason do not exceed it; both sides' rows read for the re-test are counted; every account lists a six-way reason count summing to its differing days, evidence as a count, a multiple or day
offsets, the UNEXPLAINED days by offset and size, the negative arm true, and a window that is closed exactly when no day is UNEXPLAINED; the summary matches; a surprise row exactly when an account stays UNEXPLAINED; zero vendor calls, secret reads and S3 writes; no served value changed; no run of 8 or more digits. Base: FAIL.

<expected_criteria>DB92-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. Rounds 90 and 91's folders, the tie-out modules, the pulled responses and every stored table are READ ONLY.
- **No vendor call, no credential read, no session load.** You never run `tieout_day_read.py pull`, never call a Black Diamond endpoint, never read a cookie or credential file, never open a browser. Rows come from S3 reads only.
- **No served write.** S3 GET and LIST only, on the two stores `~137` named; no put, copy or delete; no Lambda, Terraform or IAM act; no deploy; no push. A denial is recorded verbatim, not retried by another route.
- **No client data in what you write.** Counts, multiples, offsets and sizes only in the repo; row detail goes only to your private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only. Commit with `.tools/safe-commit.sh` as your definition says.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W138-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES, never re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~138/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-172.bd-excludes-served-income-over-the-23-days.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 94 (round 92), cell `DB-b-172`.
<owned_cells>DB-b-172</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB92-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~138/IRPT_DASHBD.TO-DB-b-172.bd-excludes-served-income-over-the-23-days.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB92-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the rule's commit (before the read); `test_held_days` and whether it equals 8; the rows read on each side; per account (plan order, no ids): days differing, the six reason counts, closed or not, the UNEXPLAINED offsets and sizes; the evidence for each used reason; the module's commit; any row ids. Counts, multiples, offsets and sizes only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a private read of two S3 stores and a counts-only record; nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; S3 GET and LIST of the two stores round 91's worker read without a denial; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record; 25 synthetic arms dry-run) and the analysis names the negative arm.
lane: the <paths> block IS the grant.
</preflight>
