# TO IRPT_DASHBD.TO-DB-b-19 -- PRD ruling 27: a short position's DIV debit is income, admitted by its declared share quantity (nothing served)

<to_id>IRPT_DASHBD.TO-DB-b-19</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~6</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** the CTO's L10 analysis of rounds 2-9 (@e1e0be5ba0, msg 104517), enrichment E2,
and PRD v0.7 ruling 27 (row IRPT_DASHBD-W1-S17). GATE (x) puts this in ROUND 11 (IRPT_BCKEND row S267). | **Decomp cell:**
`DB-b-19` (decomposition section 11) | **outcome_ref:** FWD-8 (the income field) | **depends_on:** DB-b-15 (merged @ce1d4a0530)

---

## WORKER FACE

**The ruling (PRD v0.7, ruling 27).** A DIV debit on a short position is a dividend the account PAID. It is the same class as the
QDV, NDV and PDV debits that DB-b-13's short-dividend fix already admits.
- The producer declares `dividend_interest_share_quantity` in `sources.json`.
- It admits a DIV debit as negative income ONLY when that quantity is negative.
- It moves the per-day INCOME field only. Return does not move on any account-day: DELTA=0 on return is the check.

**What was measured (row W1-S17).** Over the 188 `fact_trn` partitions 2026-01-02..2026-10-01, there are 39 DIV debits on FC/DV:
- 38 carry a negative `dividend_interest_share_quantity`, 822.51 absolute. These are short-account dividends, unbooked today.
- 1 carries zero shares (0.37, a long fund on an account-day with no short market value). It stays OUT.
- Adjustment keys (DIVAJ, DFRAJ, NDVAJ, NDRAJ and others) reverse an earlier credit and stay out.
- Round 6's tools are in `deliverables/0.9.0_WK_IRPT_DASHBD~1/`: `short_income_invariance_r6.py`, and the record
  `SHORT_INCOME_INVARIANCE_R6.json`.

**What you build.**
1. In `data/assets/scripts/gold/irpt_reporting/sources.json`, declare `dividend_interest_share_quantity` as a read column of
   `fact_trn`, with its basis and a comment citing ruling 27.
2. In `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`, the income term admits a DIV debit ONLY when the declared
   share quantity is negative. The QDV, NDV and PDV treatment is unchanged, and no other key moves. `METHOD_VERSION` stays 2:
   income does not enter return.
3. **Measure, reading only.** Run the producer at the base and with the change over the 188 partitions (2026-01-02..2026-10-01).
   Write `deliverables/0.9.0_WK_IRPT_DASHBD~6/SHORT_DIV_DEBIT_R11.json` with this shape:
   `{"span": ["2026-01-02","2026-10-01"], "partitions_scanned": 188, "newly_admitted_div_debit_rows": 38, "newly_admitted_amount_abs": 822.51, "admitted_with_nonnegative_share_quantity": 0, "zero_share_div_debit_rows_excluded": 1, "account_days_compared": <n>, "return_delta_nonzero_account_days": 0, "income_delta_nonzero_account_days": <n>}`.
   The numbers are what you measure. If any differs from W1-S17's, file a row with both and say why.
4. **Tests.** Create `data/assets/scripts/gold/irpt_reporting/tests/test_short_div_debit.py`, at least 3 tests, naming `DIV`,
   `share_quantity` and `short`:
   - a DIV debit with negative share quantity is negative income;
   - a DIV debit with zero share quantity is not admitted;
   - return is identical with and without the change.

<criterion id="DB11-1-AC1" cell_refs="DB-b-19"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r11/p11_1_ac1_short_div_debit_tests.py" .</invocation><expect>DB11-1-AC1 PASS</expect></criterion>
`DB11-1-AC1` -- the irpt_reporting suite passes, at least 17 tests (14 at the base), with the new file. Base: FAIL (no file).

<criterion id="DB11-1-AC2" cell_refs="DB-b-19"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r11/p11_1_ac2_short_div_debit_measured.py" .</invocation><expect>DB11-1-AC2 PASS</expect></criterion>
`DB11-1-AC2` -- exactly the 38 DIV debits are admitted (822.51), none with non-negative shares, and the zero-share row is excluded.
Return DELTA=0 on every compared account-day. Base: FAIL (no record).

<criterion id="DB11-1-AC3" cell_refs="DB-b-19"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r5/p5_ac3_suites_unchanged.py" . DB11-1-AC3</invocation><expect>DB11-1-AC3 PASS</expect></criterion>
`DB11-1-AC3` -- reporting-gold and reporting-publish suites pass with nothing removed. Base: PASS (a guard).

<expected_criteria>DB11-1-AC1,DB11-1-AC2,DB11-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. The issuer's P-2 packet is in flight on the reporting artifacts. Do not touch `infra/` or
  the source map.
- **AWS:** S3 reads only. No write, no upload, no deploy, no vendor call.
- **Refusal clause.** A change that moves return on any account-day, or admits a DIV debit with non-negative shares, is a defect:
  stop and file a row. An existing test that moves is a defect: stop and file a row. No client name in any record.

<paths>
data/assets/scripts/gold/irpt_reporting/account_return_daily.py
data/assets/scripts/gold/irpt_reporting/sources.json
data/assets/scripts/gold/irpt_reporting/tests/test_short_div_debit.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `data/assets/scripts/`, `lib/`, `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/`,
`org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 11 (round 11, workstream B), cell `DB-b-19`.
<owned_cells>DB-b-19</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB11-1-AC1, DB11-1-AC2, DB11-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6/IRPT_DASHBD.TO-DB-b-19.short-div-debit-income.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB11-1-AC1,DB11-1-AC2,DB11-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the admission rule as coded;
- the measured counts;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the reporting gold producer's income term and its source declaration; 0 served bytes move (no build, no upload, no deploy). It rides the P-2 rewrite only if merged before that packet's gold build; P-2 is never held for it (PRD ruling 27).
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the 07:41 ET reporting gold schedule is not moved.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB11-1-AC1 base FAIL (no file), DB11-1-AC2 base FAIL (no record), DB11-1-AC3 base PASS (gold 24, publish 37), dry-run at the base 2026-10-03 ~03:1xZ.
lane: the <paths> block IS the grant.
</preflight>
