# TO ADVI_COTBKF.TO-CB-ad-1.scale-factor-trace -- round 30 CB-ad-1: read-only trace of the ~2.45x r28/r26 day-value factor on two accounts

<to_id>ADVI_COTBKF.TO-CB-ad-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~57</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ad-1` (`decompositions/ADVI_COTBKF_DECOMP.round30.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3's daily chain (`data/assets/scripts/silver/`) values each account-day from holdings x close. It is run by
`commonwealth_sweep_regrade.py` with `--before-cash-leg` / `--after-cash-leg` (`method_r26`, `method_r28`) and `--data-dir`.

Rule `method_r28` added split repairs in `commonwealth_daily_valuation.py`:
- `split_plan` at line 318;
- `apply_splits` at line 380;
- `LAST_PLAN` at line 296 holds the last run's plan.

On accounts **B3S728504 and B3S728506**, `method_r28`'s day values are 2.43-2.47x `method_r26`'s on EVERY valued day (row
ADVI_COTBKF-D2-S45). Monthly returns still mostly match, because a constant factor cancels in a return. The served levels in
`account_day_value` differ from r26 by that factor, and which level is right is unmeasured.

The leading candidate (CTO ADDENDUM 5) is a split adjustment applied to quantity and not price, or the reverse. Candidate CUSIPs from
the round-29 dividend trace (`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~55/div_dating_trace.md`):
- 808524102, applied split x3 and an earlier x2;
- 808524839, applied split x2.

**Your item.** READ-ONLY: no rule change, no S3 write. Write a script
`data/assets/scripts/silver/commonwealth_scale_trace.py --data-dir <dir> --out <dir>`. For each of the two accounts, on a sample of
valued days (at least the first and last valued day of each calendar year, plus every day where the r28/r26 ratio changes by more
than 1%), it prints per CUSIP held:
- quantity, close and value under `method_r26` and under `method_r28`;
- the split factor r28 applied to that CUSIP (from `split_plan`, with its source: rows or store).

It then names the CUSIP(s) whose value difference carries the account's factor. Where the delivery holds an outside level (a
reported market value or position value for the account or CUSIP on that day), print it beside both.

Classify each account by a rule written in the script BEFORE its run, to one of:
- `split_double_applied` (r28 scales a close that was already as traded);
- `split_missing_r26` (r26 lacked a needed scale, so r28 is right);
- `cash_leg`;
- `other:<what>`;
- `untraced:<what was checked>`.

Also say which level the outside value supports, where one exists. Write `scale_trace.md`. LAST line exactly:
`SCALE-TRACE accounts=2 split_double_applied=<a> split_missing_r26=<b> cash_leg=<c> other=<d> untraced=<e>`.

### ACCEPTANCE

<criterion id="CB30ad1-AC1" cell_refs="CB-ad-1"><invocation>python data/assets/scripts/silver/commonwealth_scale_trace.py --data-dir .scratch/advi_cotbkf/r28 --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~57</invocation><expect>SCALE-TRACE accounts=2</expect></criterion>
`CB30ad1-AC1` -- both accounts traced to a class. Data-dir `.scratch/advi_cotbkf/r28` is the built input; if it is absent, rebuild it
with the default re-grade.

<criterion id="CB30ad1-AC2" cell_refs="CB-ad-1" judgment="true"/>
`CB30ad1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: each account's class follows from the printed per-CUSIP
rows by the script's pre-written rule, and the "which level is right" statement rests on an outside value where one exists.

<expected_criteria>CB30ad1-AC1,CB30ad1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Large output goes under `.scratch/`,
  uncommitted.
- **Read-only.** No rule change, no S3 write. Read only the buckets the chain reads plus dell1's store. Never read `opal-data-bd`,
  `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W57-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_scale_trace.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round30.md</decomp_doc> (round 30), cell `CB-ad-1`.
<owned_cells>CB-ad-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB30ad1-AC1, CB30ad1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~57/ADVI_COTBKF.TO-CB-ad-1.scale-factor-trace.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB30ad1-AC1,CB30ad1-AC2` BEFORE the flip. Mechanical: CB30ad1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the SCALE-TRACE line, each account's class with its carrying CUSIP rows, and the outside value if any; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only trace.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- read-only; class by a rule written before the run; BLIND: an account with no outside level (named, level left unjudged).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 5 @abbf204c7e (msg 2921); row D2-S45.
