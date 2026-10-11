# TO ADVI_COTBKF.TO-CB-bq-4.residual-receipt-predicate -- round 69 CB-bq-4: a receipt after an account's assets have left: the exact predicate, tested on the 179 and on every measured day

<to_id>ADVI_COTBKF.TO-CB-bq-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~109</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>69</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bq-4` (`decompositions/ADVI_COTBKF_DECOMP.round69.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT that writes a rule down exactly and tests it. You change no code.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_69_20261011.md` section 2 item 3 (the policy, word for word) and section 3 item 4; the round-68 record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~105/OUTLIERS_ON_A_REAL_BASE.json` and its `.md` (the nine causes of
the 179 days; its observation that the account's own prior-30-row outflow of 100 times the base separates the two exit classes);
`data/assets/scripts/silver/commonwealth_flows.py` (which transaction types are external flows, income, fees) and
`commonwealth_daily_returns.py` (the return formula near line 271; how a blank reason is set near line 227).

**The policy you make exact.** "A receipt that arrives after an account's assets have left (income paid late; a fee refund) is not a
return of that day and is not a contribution either. The day is blank, with that reason. ... It is defined by a recent full outflow,
never by a prior value of 100.00 or any other number."

**Your item.**

1. **Write the predicate** over one account-day, using only what the build has on that day and before it: (a) the account has had a
   FULL OUTFLOW recently (define it: over which look-back, measured in the account's own rows or in calendar days; what share of the
   pre-outflow value must have left; state each constant and where it comes from in the data, not from taste); (b) the day carries a
   RECEIPT of the kinds the policy names (list the transaction types for income and for a fee refund, from `commonwealth_flows.py`,
   with their lines) and no other activity that would make the day's return a market return; (c) what the day reads: blank, with a
   reason code you name (one code, in the style of the existing blank reasons).
2. **Test it on the 179** days of the round-68 set (rebuild the set: measured rows of
   `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/daily_returns.parquet` with a prior value of 100.00 or more and `abs(return)` above 0.10; it must read
   179). Print the confusion table against that record's nine causes: for each cause, how many days the predicate blanks and how many
   it leaves. The policy's targets are the income-after-exit days (119) and the fee-refund days (43). Say plainly what it blanks that
   it should not (a real price move, the withholding days) and what it misses.
3. **Test it on everything else:** over ALL 107,311 measured rows with a positive prior value, how many the predicate blanks, split by
   `abs(return)` at or below 0.10, 0.10 to 1.00, above 1.00, and by prior value under 1.00, 1.00 to under 100.00, 100.00 or more. A
   rule that blanks thousands of quiet days is a different rule from the one the policy states: show the number.
4. **Sensitivity:** vary each constant of (a) over a sensible range (at least three values each) and print how the two tables move.
   Recommend ONE setting and say why; mark it a recommendation.
5. **What it does to months:** how many account-months lose a measured day under the recommended setting (count only).
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~109/RESIDUAL_RECEIPT_PREDICATE.json` and a short `.md` beside it that states the predicate in plain words a person can check by hand.
   Top-level keys, exactly: `predicate` (`{"full_outflow", "receipt_types", "excludes", "reads_as"}`), `constants`, `on_the_179` (a
   list of `{"cause", "days", "blanked", "left"}`), `targets_blanked` (of 162), `non_targets_blanked`, `on_all_measured` (the split
   table), `total_blanked`, `sensitivity`, `recommended`, `account_months_touched`, `not_established`.

### ACCEPTANCE

<criterion id="CB69bq4-AC1" cell_refs="CB-bq-4"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~109/RESIDUAL_RECEIPT_PREDICATE.json',encoding='utf-8'));t=d['on_the_179'];print('RESIDUAL-RECEIPT-RECORD days=%d causes=%d targets_blanked=%d of 162 non_targets_blanked=%d total_blanked_of_all_measured=%d account_months_touched=%d reads_as=%s'%(sum(x['days'] for x in t),len(t),d['targets_blanked'],d['non_targets_blanked'],d['total_blanked'],d['account_months_touched'],d['predicate']['reads_as']))"</invocation><expect>RESIDUAL-RECEIPT-RECORD days=179 causes=9</expect></criterion>
`CB69bq4-AC1` -- the predicate is tested on all 179 days across the nine causes, and on every measured row, with its counts printed.
The CTO reads what it separates and what is left.

<criterion id="CB69bq4-AC2" cell_refs="CB-bq-4" judgment="true"/>
`CB69bq4-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the predicate is defined by a recent full outflow and
by no prior-value number; a person can apply it by hand from the `.md`; every constant has a stated source; what it blanks wrongly and
what it misses are printed, not hidden; the recommendation is marked as one.

<expected_criteria>CB69bq4-AC1,CB69bq4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local; no network call.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write.** Read-only S3 gets, heads and listings are allowed where the cell
  says so. No push. No `--refresh`. No vendor call (no Yahoo, no Bloomberg).
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, tickers, a security's price,
  ratios, version ids, ETags and reason codes only. A build log line carrying `read_account=` is never echoed: filter it out.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W109-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round69.md</decomp_doc> (round 69), cell `CB-bq-4`.
<owned_cells>CB-bq-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB69bq4-AC1, CB69bq4-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~109/ADVI_COTBKF.TO-CB-bq-4.residual-receipt-predicate.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB69bq4-AC1,CB69bq4-AC2` BEFORE the flip. Mechanical: CB69bq4-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the predicate in plain words; each constant and its source; the confusion table on the 179 by cause; what it blanks wrongly and what it misses; the split table over all measured rows and the total blanked; the sensitivity tables; the recommended setting, marked as a recommendation; account-months touched; the `RESIDUAL-RECEIPT-RECORD` line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the rule is tested on the 179 AND on every measured row, so a rule that fits the outliers by blanking quiet days shows itself; a prior-value number is barred by the policy; sensitivity is printed for every constant; BLIND: the nine causes it is scored against are one worker's classing, graded MET but placed by rule for 102 of 179 days.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-69 analysis @e0f9682779 (msg 5206), section 3 item 4, and PRD ADDENDUM v0.6 @df488019bf (msg 5217); `3.0.0_SA_CVO` REMEDIATION_v39 @22e2566c22.
