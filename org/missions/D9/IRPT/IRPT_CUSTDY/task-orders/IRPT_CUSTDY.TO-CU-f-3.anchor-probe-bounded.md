# TO IRPT_CUSTDY.TO-CU-f-3 -- round 6 CU-f-3 (E3): the SI anchor probe bounded -- hop 3 for the chosen advisor in at most 120 s, labels unchanged

<to_id>IRPT_CUSTDY.TO-CU-f-3</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~14</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~K2</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-f-3` (`decompositions/IRPT_CUSTDY_DECOMP.round6.md`) |
**outcome_ref:** FWD-1 | **depends_on:** `IRPT_CUSTDY.TO-CU-f-1` (same worker queue; both change `client_report_figures.py`)

---

## WORKER FACE

### THE CELL

`CU-f-3`, item E3 of the CTO's round-5 analysis (ruling W12-S1). `data/assets/scripts/gold/irpt_custody/hop3_real_run.py --advisor
matthew_gooch --as-of 2026-09-30` takes ~140-1500 s on dell2; a faulthandler dump placed the time inside the SI anchor probe's S3 listing in
`client_report_figures.py` (~line 308, called from ~710, ~754, ~861). Ruling: the probe reads a manifest (or a narrowed prefix) instead of
listing S3, so hop 3 runs inside a 120 s bound before it is ever scheduled. The SI result must not change: on real data 14 of 14 covered
accounts carry SI OK, 12 under branch (a) `since inception (first funded <date>)` and 2 under rule 2 `since <date>, the first date Opal holds`.

**Build:**
1. In `client_report_figures.py`: replace the probe's listing with a manifest read or a prefix narrowed to the accounts and dates the anchor
   rules need (read the gold's manifest / partition layout first: `account_return_daily.py` writes it). The anchor rules and labels are
   untouched.
2. A NEW script `data/assets/scripts/gold/irpt_custody/hop3_timed_check.py --advisor <slug> --as-of <d>` that runs the wrapper in-process to a
   temp file (deleted after), times it, and prints `HOP3-TIMED advisor=<slug> seconds=<n> within_120=<True|False> households=<n> accounts=<n>
   si_ok=<n> si_labels_rule1=<n> si_labels_rule2=<n>`. Nothing is committed from the run.
3. Tests in a NEW file `data/assets/scripts/gold/irpt_custody/tests/test_si_anchor_bounded.py` (fixtures, stubbed S3): the probe makes no
   unbounded listing call (assert on the stub's calls) and returns the same anchors as before on the same fixture.

### ACCEPTANCE

<criterion id="CU17-AC1" cell_refs="CU-f-3"><invocation>python data/assets/scripts/gold/irpt_custody/hop3_timed_check.py --advisor matthew_gooch --as-of 2026-09-30</invocation><expect>within_120=True</expect></criterion>
`CU17-AC1` -- the CTO's criterion (1), timed on real data on dell2. Run it under `timeout 600` so a regression reports instead of hanging.

<criterion id="CU17-AC2" cell_refs="CU-f-3"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_si_anchor_bounded.py</invocation><expect>passed</expect></criterion>
`CU17-AC2` -- the CTO's criterion (2) on fixtures: same anchors, no unbounded listing. (The real labels are in AC1's line: 14 OK, 12 + 2.)

<expected_criteria>CU17-AC1,CU17-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **AWS: read only.** Never commit a real-run output file. Never print a full account number.
- **A surprise row is committed in the same turn you write it.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a row (id `IRPT_CUSTDY-W14-S<k>`;
  `disposition` one of UNDER_INVESTIGATION | GRADUATED | DISMISSED_WITH_REASON | DECOMP_INVALIDATING), and do not weaken a test.

<paths>
data/assets/scripts/gold/irpt_custody/client_report_figures.py
data/assets/scripts/gold/irpt_custody/hop3_timed_check.py
data/assets/scripts/gold/irpt_custody/tests/test_si_anchor_bounded.py
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round6.md</decomp_doc> (round 6), cell `CU-f-3`.
<owned_cells>CU-f-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU17-AC1, CU17-AC2. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~14/IRPT_CUSTDY.TO-CU-f-3.anchor-probe-bounded.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU17-AC1,CU17-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `HOP3-TIMED` line (before and after if you can measure before), what replaced the listing, the test list, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a performance repair run by hand; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; reads opal-data-assets, opal-data-bd and opal-data-49financial with the dell2 box profile.
comp-adversary: RUN -- labels-unchanged is checked on real data in AC1's line; read-only; BLIND: whether the gold manifest carries every date the anchor rules need (the cell reads it first).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: round-5 analysis @f6160117ce section 2 (W12-S1) and section 4 E3; row W12-S1; decomposition round 6 constraint 3.
