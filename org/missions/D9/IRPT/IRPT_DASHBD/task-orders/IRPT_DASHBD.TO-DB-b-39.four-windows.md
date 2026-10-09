# TO IRPT_DASHBD.TO-DB-b-39 -- E1 (after DB-b-38): the 4 non-rounding windows named against the custodian lot events and fixed through the rule, the 91 windows re-run (row W21-S4) (FWD-4)

<to_id>IRPT_DASHBD.TO-DB-b-39</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~22</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-24 analysis @99580aac8c item E1 ("each window read against the custodian's lot events, with the term or vendor behaviour named from the rows; a fix goes through the activity or lot rule with the 91-window re-run printed (ties, misses by class), never a per-account patch; anything left is carried and labelled") | **Decomp cell:** `DB-b-39`
(decomposition section 25) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-38 (same worker, same queue: run it after DB-b-38 is complete).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-22`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~22/`.

**The cell (`DB-b-39`).** Four of round 24's 36 misses are not rounding (row IRPT_DASHBD-W21-S4): three MISSING-TERM, where a lot's basis is above the cash paid, and one OTHER, where the custodian re-selected the lots relieved by an in-kind departure. The accounts are the four non-ROUNDING rows of `regrade.failures` in the round-24 record. Read `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/IDENTITY_REGRADE_E2.json` and `GAP_DIAGNOSIS_E1.json` first (round 24: the same 91 accounts over 2026-09-01..2026-10-05; 55 tie within one cent, 36 miss: ROUNDING 32 at the 0.05 tolerance, MISSING-TERM 3, OTHER 1). The producer is `data/assets/scripts/gold/irpt_reporting/account_activity_lots.py`; its sources are `s3://opal-data-assets/schwab/08335338/silver/` (`fact_trn`, `fact_rld`, `fact_uln`/`fact_ult`, `dim_position`, `dim_balance`). Round 24's re-grade helper is `deliverables/0.9.0_WK_IRPT_DASHBD~21/identity_regrade_e2.py`; copy what you need into your folder.

1. Read each of the 4 windows against the custodian's lot events (`fact_rld`, the open-lot tables, the transactions that opened and
   relieved each lot). Name what explains the gap from those rows: a term the rule misses, or a vendor behaviour (for example a basis
   that includes commission or an amount the cash leg does not carry, or a lot re-selection).
2. Fix what is a rule: change the activity or lot RULE so every account with the same pattern is handled. Never name an account id in
   the producer. A vendor behaviour you cannot reproduce from the rows stays a miss, labelled with its cause; never plug a gap.
3. Re-run the identity over the SAME 91 accounts and window, with DB-b-38's `LEG_LAG_DAYS`. Write `WINDOWS_E1.json` with `windows`
   `[{account_id, gap_before, gap_after, lot_events: [row keys], cause, kind: "RULE"|"VENDOR"}]` and `regrade` `{graded, passed, failed,
   failures: [{account_id, gap, class}]}` (class ROUNDING within 0.05, MISSING-TERM with its cause, or OTHER with its cause). Add one test
   per rule change. Write `WINDOWS_E1.md`, COUNTS ONLY.

<criterion id="DB25-2-AC1" cell_refs="DB-b-39"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r25/p25_windows.py" . DB25-2-AC1</invocation><expect>DB25-2-AC1 PASS</expect></criterion>
`DB25-2-AC1` -- the 4 windows each read against lot events with a named cause. Base: FAIL.

<criterion id="DB25-2-AC2" cell_refs="DB-b-39"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r25/p25_windows.py" . DB25-2-AC2</invocation><expect>DB25-2-AC2 PASS</expect></criterion>
`DB25-2-AC2` -- the 91 windows re-run, every miss classed; no account id in the producer. Base: FAIL.

<expected_criteria>DB25-2-AC1,DB25-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** S3 reads only. No write, no deploy, no vendor call, no bun, no download of any package, script or program.
- **Refusal clause.** A plugged gap, a per-account patch, an S3 write, a deploy, or a client figure in a committed `.md` is a defect:
  stop and file a row.

<paths>
data/assets/scripts/gold/irpt_reporting/account_activity_lots.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_activity_lots.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~22/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-39.four-windows.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 25 (round 25, workstream B), cell `DB-b-39`.
<owned_cells>DB-b-39</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB25-2-AC1, DB25-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~22/IRPT_DASHBD.TO-DB-b-39.four-windows.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB25-2-AC1,DB25-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, what you changed, the numbers each criterion prints, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a rule fix in the round-23 producer, which serves nothing yet; no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB25-2-AC1 and AC2 base FAIL (no record), dry-run at base 99580aac8c 2026-10-07 ~17:2xZ; the denominator read from round 24's record: the 4 non-ROUNDING accounts acct#470f0c95, acct#d1934437, 0018321241, acct#065caf00.
lane: the <paths> block IS the grant.
</preflight>
