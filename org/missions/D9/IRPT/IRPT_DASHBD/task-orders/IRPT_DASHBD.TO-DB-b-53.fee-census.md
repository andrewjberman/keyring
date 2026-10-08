# TO IRPT_DASHBD.TO-DB-b-53 (RE-CUT, round 30 amendment 1) -- the fee add-back compounded in the tie-out reader, and the FULL 49F tie-out (9,078 segments) re-graded on the compounded basis: before/after counts, share within 0.35 pp, remaining misses named

<to_id>IRPT_DASHBD.TO-DB-b-53</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~34</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ruling on row IRPT_DASHBD-S35, msg 1660
(2026-10-08 21:21Z). It cancels the fee-census and fee-drag cells; this order is RE-CUT IN PLACE, because the gate admits one issuance per round. Its earlier face (Schwab fee census, worker ~32) is superseded; ~32 was stopped by the issuer and its branch is not drained. Round 30 amendment 1; decomposition section 32
addendum | **Decomp cell:** `DB-b-53` | **outcome_ref:** FWD-8 | **depends_on:** none open (round 18's record and pulls are landed).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-34`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~34/`.

**The cell (`DB-b-53`).** The 49F tie-out compares Opal's served return with Black Diamond's figure on one basis, GROSS of fees.
- Opal's served return is gross by design. BD's is net.
- Round 18 (`deliverables/0.9.0_WK_IRPT_DASHBD~13/tieout_e2_gross.py`, function `fee_addback` at lines 26-31) turned BD net into
  gross by ADDING `fees / ((bmv + emv) / 2)` to BD's net time-weighted return.
- Row IRPT_DASHBD-S35 (in `surprise-channel/investigations/INVESTIGATION_v1.md`) measured that this additive form omits the
  fee-times-return interaction over long, positive periods. Compounding it as `(1 + net) * (1 + add_back) - 1` moved the split
  tie-out's right-half median gap from +0.567 pp to +0.043 pp, and the tied count from 0 to 1,334 of 1,527.

This cell fixes the basis in the reader and re-grades the whole tie-out.

1. **The reader.** Write `tieout_compound.py` in your folder. It imports round 18's reader (`tieout_e2_gross.py`) and its own imports,
   and overrides only the gross formation, so BD gross = `(1 + bd_net_twr) * (1 + add_back) - 1`. The add-back itself is unchanged.
   Do not restate the rest of the reader.
2. **The unit test.** Write `test_tieout_compound.py` beside it. It needs a test whose name contains `chain`, showing that on the
   compounded basis two adjacent ranges chain to the whole. Use a synthetic account (no client data) whose daily net return and daily
   fee rate are constant: the two halves' compounded gross, chained as `(1+a)(1+b)-1`, equals the whole range's compounded gross within
   1e-9. Add a second test showing the additive basis does NOT chain on the same account.
3. **The full re-grade.** Re-run the round-18 tie-out on the compounded basis over its own inputs:
   - the plan;
   - BD's full-period pull `s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/`;
   - the served gold `s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/`.

   Every segment round 18 graded is in scope: 9,078 (5,416 within 0.35 pp, 3,662 outside). Per segment, write `account`, `segment`
   {start, end}, `abs_diff_pp` (compounded), `verdict`, and `reason` for an OUTSIDE row. Use round 18's reason logic and its closed set
   {FLOW_TIMING, MISSING_PRICE, INCOME_DATE, COVERAGE_DAYS, UNEXPLAINED}. Name each remaining miss; never force it into a class.
4. Write `TIEOUT_COMPOUND_E1.json`:
   - `segments`;
   - `before` {within: 5416, outside: 3662}, read from round 18's record;
   - `after` {within, outside};
   - `share_within_after`;
   - `after_outside_by_reason`;
   - `basis` and `files_read`.

   Write `TIEOUT_COMPOUND_E1.md`: COUNTS ONLY, with MATCH/DIFF before and after printed, and no account number, name or balance (the
   landed BD files carry names; never print them).

<criterion id="DB30-4-AC1" cell_refs="DB-b-53"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r30/p30_compound.py" . DB30-4-AC1</invocation><expect>DB30-4-AC1 PASS</expect></criterion>
`DB30-4-AC1` -- the tests file holds a `chain` test, and pytest on it passes. Base: FAIL.

<criterion id="DB30-4-AC2" cell_refs="DB-b-53"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r30/p30_compound.py" . DB30-4-AC2</invocation><expect>DB30-4-AC2 PASS</expect></criterion>
`DB30-4-AC2` -- exactly round 18's 9,078 graded segments; `before` equals round 18's counts; `after` and the share within 0.35 pp equal the row tally. Base: FAIL.

<criterion id="DB30-4-AC3" cell_refs="DB-b-53"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r30/p30_compound.py" . DB30-4-AC3</invocation><expect>DB30-4-AC3 PASS</expect></criterion>
`DB30-4-AC3` -- every remaining miss carries a reason from the closed set, and the by-reason counts sum to the misses. Base: FAIL.

<expected_criteria>DB30-4-AC1,DB30-4-AC2,DB30-4-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Round 18's scripts and record, the plan and the landed pulls are read, never edited.
- **AWS:** S3 reads only. NO Black Diamond or vendor call, no secret read, no S3 write, no bun, no download of any package, script or
  program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a filled figure, a reason outside the closed set, or an account number,
  name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~34/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-53.fee-census.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 32, addendum (round 30 amendment 1), cell `DB-b-53`.
<owned_cells>DB-b-53</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB30-4-AC1, DB30-4-AC2, DB30-4-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~34/IRPT_DASHBD.TO-DB-b-53.fee-census.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB30-4-AC1,DB30-4-AC2,DB30-4-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, before/after counts and the share within 0.35 pp, the misses by reason, and any
row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only re-grade over landed pulls and the served gold; no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB30-4-AC1..AC3 base FAIL (no record, no tests) at base be6b3cdbb7; positive control on a planted record built from round 18's own 9,078 graded segments PASS (before 5,416/3,662 read from the record; after tally and reasons exercised).
lane: the <paths> block IS the grant.
</preflight>
