# TO ADVI_COTBKF.TO-CB-c-3 -- round 3 CB-c-3: the crosswalk (FWD-8) -- each Commonwealth account to its current Cottonwood account by a stated rule, or unmatched with the reason

<to_id>ADVI_COTBKF.TO-CB-c-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~10</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-c-3` (`decompositions/ADVI_COTBKF_DECOMP.round3.md`) | **outcome_ref:** FWD-8 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-c-3`, FWD-8: "for each Commonwealth account, a person sees the matching current Cottonwood account, or a plain statement that it is not
yet matched, and why." C-CROSSWALK: "every Commonwealth account is either matched, with the rule that matched it, or listed as not yet
matched with the reason. No match is guessed." You build the crosswalk builder and prove it on the real data into a LOCAL directory. You
write NOTHING to S3: `--apply` is the issuer's act.

**The two sides, measured (read-only, default profile):**
- **Commonwealth** (this project's silver, `s3://opal-data-assets/commonwealth/cottonwood/silver/`): transactions (1,416,497 rows, 1,533
  accounts in `Account_Number`; columns include `Cusip`, `Symbol`, `Quantity`, `Amount`, `Trade_Date`, `Transaction_Type`,
  `Transaction_Description`, `Advisor_ID`), positions (469 rows, 83 accounts in `AccountNumber`, one day 2026-06-23, `Cusip`, `Quantity`).
  Account numbers: old 11-digit (`acct#c9405219`) and 2016+ alphanumeric (`acct#0e4ff3a3`).
- **Current Cottonwood** (Cottonwood's own firm bucket, the same firm): `s3://opal-data-cot/gold/dimensions/accounts_dimension_latest.parquet`
  (994 accounts; `account_id` like `acct#c6ac42e6`, `relationship_id`, `account_open_date` and `first_transaction_date` mostly 2026-05/06,
  `account_type`, `account_registration_type`; names mostly null) and the holdings history `s3://opal-data-cot/gold/canonical/holdings/<date>.parquet`
  (read its columns first). Read nothing from `opal-data-bd` or `opal-data-inf` (the cross-firm law).
- The current accounts open around 2026-05/06, and the delivery ends 2026-06-23: the clients appear to have moved custodian then, with
  positions transferred in kind.

**Rules, in this order, each stated in the output and applied only with its evidence:**
1. `R1-same-number`: the Commonwealth account number, normalized (case, separators, leading zeros), equals a current `account_id`.
2. `R2-in-kind-transfer`: the Commonwealth account's holdings as it left (its 2026-06-23 positions where it has them, else its holdings at
   its last activity rebuilt from its transactions) match a current account's FIRST holdings (its earliest holdings date) on the same CUSIPs
   with quantities equal within 0.001 on at least 80% of the positions by count and no conflicting candidate; print the score.
3. You may add a rule only if it is exact and its evidence is printed; a rule that could match one Commonwealth account to two current
   accounts (or two to one) is never applied -- such accounts are listed `AMBIGUOUS` with both candidates.
Every Commonwealth account gets exactly one row: `MATCHED` (rule, current account, score, evidence) or `NOT_MATCHED` (reason: for example
"closed before 2026", "no current account holds its positions", "ambiguous").

**Build `data/assets/scripts/silver/commonwealth_crosswalk.py`:** CLI `--out <local dir>`, `--apply` (writes at
`address('commonwealth', <scope>, 'silver', 'crosswalk', 'date=2026-06-23')`; unit-tested on a stub, never run by you); the scope through
`opal_naming.lookup`; device-free. Writes `crosswalk.parquet` and a `.csv`. LAST line exactly:
`CROSSWALK commonwealth_accounts=<n> every_account_listed=<True|False> matched=<m> not_matched=<u> ambiguous=<a> by_rule=<rule:count,...>`.

Tests `data/assets/scripts/silver/tests/test_commonwealth_crosswalk.py` (fixtures, no AWS): R1 normalization; R2 match at the threshold and a
miss below it; a two-candidate case listed AMBIGUOUS, never matched; every input account appears exactly once.

### ACCEPTANCE

<criterion id="CB3c3-AC1" cell_refs="CB-c-3"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_crosswalk.py</invocation><expect>passed</expect></criterion>
`CB3c3-AC1` -- the rules on fixtures, including the ambiguity control.

<criterion id="CB3c3-AC2" cell_refs="CB-c-3"><invocation>python data/assets/scripts/silver/commonwealth_crosswalk.py --out .scratch/advi_cotbkf/crosswalk</invocation><expect>CROSSWALK commonwealth_accounts=1533 every_account_listed=True</expect></criterion>
`CB3c3-AC2` -- the real data: all 1,533 Commonwealth accounts listed, each matched by a stated rule or not matched with a reason.

<criterion id="CB3c3-AC3" cell_refs="CB-c-3" judgment="true"/>
`CB3c3-AC3` -- JUDGMENT, graded by `3.0.0_SA_CVO` at L9: a sample of MATCHED rows is right on its printed evidence, and no NOT_MATCHED reason
hides a match the evidence shows.

<expected_criteria>CB3c3-AC1,CB3c3-AC2,CB3c3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Local output and caches under `.scratch/`, uncommitted.
- **No S3 write, no `--apply`;** S3 READS only of the keys named above.
- **Never guess a match.** A rule whose evidence is not printed is not a rule.
- **Within 120 seconds** for CB3c3-AC2 (cache reads under `.scratch/` and let the script read the cache when present; say so in the report).
- **Rule 13:** a DS-lane script; your commit is a candidate.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W10-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_crosswalk.py
data/assets/scripts/silver/tests/test_commonwealth_crosswalk.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round3.md</decomp_doc> (round 3), cell `CB-c-3`.
<owned_cells>CB-c-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB3c3-AC1, CB3c3-AC2, CB3c3-AC3 (judgment: UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO; never PASS or
FAIL). Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~10/ADVI_COTBKF.TO-CB-c-3.crosswalk.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB3c3-AC1,CB3c3-AC2,CB3c3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `CROSSWALK` line, the rule counts, five MATCHED rows with their evidence, the NOT_MATCHED reasons with counts, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time builder.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; reads opal-data-assets (this project) and opal-data-cot (the same firm) under the laptop profile.
comp-adversary: RUN -- cross-firm (cottonwood's own bucket only; bd and inf forbidden on the face); no guessed match (ambiguity listed, judgment criterion for the CVO); BLIND: whether the new custodian kept any old account number (R1 measures it).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.4 @51a7c07278 C-CROSSWALK, FWD-8, backlog item 5; CTO msg 105855; decomposition round 3 (measured constraint 4).
