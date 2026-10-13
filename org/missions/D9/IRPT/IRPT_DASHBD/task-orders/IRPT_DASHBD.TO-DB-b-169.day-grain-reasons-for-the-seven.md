# TO IRPT_DASHBD.TO-DB-b-169 -- read the 7 UNEXPLAINED segments at day grain from the issuer's pull of Black Diamond's daily figures: each differing day gets a reason from round 89's closed list under a day rule committed before the read, the cause corrected and the window re-closed at 0.35 pp, else its days stay UNEXPLAINED by offset and size

<to_id>IRPT_DASHBD.TO-DB-b-169</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~136</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>90</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 6986, ROUND-90 ANALYSIS @d573cb1cb8 section 3 item 2 | **Rows:** NONE | **Decomp cell:** `DB-b-169` (decomposition section 92) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-168 (the instrument) and the issuer's pull (this order is spawned only after the issuer's pull record exists).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-136` (branch `wk-IRPT_DASHBD-136`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~136/`. Your private folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~136/` (create it). The issuer's pull is under
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~134/pull/` (private; READ ONLY: 7 raw responses and a pull record).

**Why.** PRD v0.13 decision 11b: a window outside 0.35 pp meets FWD-8 only if every day that differs inside it carries a stated reason from the closed list and correcting that cause re-closes the window. Round 89's closed list, in this order (the first reason whose single correction
re-closes the window takes the day): `MISSING_PRICE`, `FLOW_ABSENT_ONE_SIDE`, `FLOW_ON_NON_TRADING_DAY`, `INCOME_OFF_FLOW_DAY`, `BD_ACCRUED_INCOME`, `UNEXPLAINED`. You apply it at DAY grain to the 7 segments the stored tables could not explain. You make NO vendor call and read NO credential.

**The cell (`DB-b-169`).** A read and a private count. You change no served code and rule nothing beyond the closed list.
1. **Read the model first.** `org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_day_read.py` (the instrument: its `analyze` mode builds the private daily table; `DAY_DIFFERS_PP = 0.01`), `tieout_neither_reasons.py` and `deliverables/0.9.0_WK_IRPT_DASHBD~133/RULE.md` (round 89's window-level
   tests and corrections, committed and bound by hash), and the stored tables in `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~108/`. You may edit `tieout_day_read.py` only to fix a defect in its `analyze` mode (state it in a row).
2. **The day rule FIRST, committed before any read of the pulled responses.** Before you open any file under `~134/pull/`, write `RULE_DAY.md` in your folder and commit it alone. It states, so that another seat would count the same way: what a DAY DIFFERS is (the day-differs line 0.01 pp of daily return, our served daily
   return against Black Diamond's, from the ratio of consecutive cumulatives); how the window's fee add-back (`(1 + bdr) * (1 + fees / mean) - 1` of `tieout_flow_timing.py`) is carried into the daily comparison so that the daily series reproduces the stored window figure at its last date (state it, and the control it implies);
   and, for EACH of the five named reasons, its day-level TEST (what in the stored rows and the daily table makes it apply to that day, by column) and its CORRECTION (the single change to that day in the recomputation), reusing round 89's window-level wording wherever it carries over. A window is CLOSED when, after
   correcting every day a reason takes, the recomputed window return is within 0.35 pp of Black Diamond's gross window figure. If the rule proves unworkable after the read starts, do NOT edit it: add a dated `RULE_DAY_ADDENDUM.md` and report both readings.
3. **The read.** Reproduce the control first: for each of the 7, the last cumulative of Black Diamond's daily series reproduces the stored window return (`series_last_equals_stored_window`, a bool per account; a false is reported, not repaired). Then, per account: list the days that differ; give each one reason from the list or
   UNEXPLAINED; correct each reasoned cause and recompute the window; count the days per reason; `window_closed_after_correction` is true exactly when no day is UNEXPLAINED and the window re-closes. NEGATIVE ARM: `uncorrected_window_misses` is true for every account (the uncorrected window still misses 0.35 pp).
   A day left UNEXPLAINED is reported by OFFSET (calendar days from the segment start) and SIZE (pp), never by date and never with an account id.
4. **If any account has UNEXPLAINED days**, file ONE surprise row (`spec_asserts` + `world_is`, counts and offsets only) and put its id in `surprise_row`; FWD-8 is then NOT REALIZED for those accounts and the CTO rules on them.
5. **Record** `DAY_READ_7.json` in your folder, exactly these keys: `tolerance_pp` 0.35; `day_differs_pp` 0.01; `rule` {`file`: "RULE_DAY.md", `sha256` (of its committed bytes), `commit` (the hash that carried it), `written_before_read`: true}; `reasons_list` (the six names, in order); `code` {`file`, `sha256`, `tracked`: true} (the module you ran);
   `population` {`accounts`: 7, `segments`: 7}; `pull` {`requests`: 7, `http_ok`, `http_failed`} (copied from the issuer's pull record; they sum to 7); `per_account` (a list of 7, NO ids, in plan order) each {`days`, `days_differing`, `by_reason` (the six names: int, summing to `days_differing`), `unexplained_days` ([{`offset`, `size_pp`}], one per UNEXPLAINED day),
   `uncorrected_window_misses`, `series_last_equals_stored_window`, `window_closed_after_correction`}; `summary` {`accounts_closed_with_reasons`, `accounts_unexplained`}; `surprise_row` (only when an account is unexplained); `reads` {`vendor_calls_by_worker`: 0, `secret_reads`: 0, `s3_writes`: 0}; `served_values_changed`: false; `limits`. NO account id, client name, amount, date with an account or run of eight or more digits.

<criterion id="DB90-2-AC1" cell_refs="DB-b-169"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r90/p90_round90.py" . DB90-2-AC1</invocation><expect>DB90-2-AC1 PASS</expect></criterion>
`DB90-2-AC1` -- the day rule was committed before the read and its bytes are unchanged; the six-name list is exact; the code file is tracked; 7 accounts, 7 requests, ok plus failed equal 7; every account lists days, differing days, a six-way reason count summing to the differing days, the UNEXPLAINED days by offset and size, the negative arm true, the series control as a bool, and a window that is closed exactly when no day is
UNEXPLAINED; the summary matches; a surprise row exactly when an account stays UNEXPLAINED; zero worker vendor calls, secret reads and S3 writes; no served value changed; no run of 8 or more digits. Base: FAIL.

<expected_criteria>DB90-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. The pulled responses, `tieout_neither_reasons.py`, `tieout_flow_timing.py`, round 89's `RULE.md` and every stored table are READ ONLY.
- **No vendor call, no credential read, no session load.** You never run `tieout_day_read.py pull`, never call a network function, never read a cookie or credential file. If the pull is absent or incomplete, say so and stop: the issuer decides.
- **No served write.** No S3 access, no Lambda, Terraform or IAM act, no deploy, no push.
- **No client data in what you write.** Counts, offsets and sizes only in the repo; whatever you derive from the private files goes only in your private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only. Commit with `.tools/safe-commit.sh` as your definition says.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W136-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES, never re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~136/
org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_day_read.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-169.day-grain-reasons-for-the-seven.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 92 (round 90), cell `DB-b-169`.
<owned_cells>DB-b-169</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB90-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~136/IRPT_DASHBD.TO-DB-b-169.day-grain-reasons-for-the-seven.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB90-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the day rule's commit (before the read); per account (in plan order, no ids): days, days differing, the reason counts, closed or not, and the UNEXPLAINED offsets and sizes; the series control; the module's commit if you edited it; any row ids. Counts, offsets and sizes only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a private read and a counts-only record; nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS access is granted or needed; the responses are local files.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record; synthetic arms dry-run) and the analysis names the negative arm.
lane: the <paths> block IS the grant.
</preflight>
