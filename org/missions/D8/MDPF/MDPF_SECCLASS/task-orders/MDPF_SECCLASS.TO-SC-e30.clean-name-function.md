# TO MDPF_SECCLASS.TO-SC-e30 -- round 8 SC-e-30: FWD-14 / FWD-11 -- the one clean-name function with its test table

<to_id>MDPF_SECCLASS.TO-SC-e30</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~26</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-30` (`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) |
**outcome_ref:** FWD-14, FWD-11 | **depends_on:** none. Slot `~26` queue: this order, then `TO-SC-e31`, then `TO-SC-e32`.

---

## WORKER FACE

### THE CELL

`SC-e-30`. "The clean-name rule: one function with a test table (proper case, vendor suffixes and all-caps removed), used for
every row" (R8). It serves:
- FWD-11 ACCEPT: an AI-made entry carries "a clean, properly capitalized name" (PRD
  `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.12).
- FWD-14 ACCEPT: "the name beside each holding is the shared list's clean, properly capitalized name, not the custody feed's
  capital-letter string".
- PRD addendum v0.4 "Clean naming": "The row's `name` is written in proper case from the source name, with vendor suffixes
  and all-caps removed. The rule is one function with a test table, not a model output." Addendum v0.7 "Names": the rule
  applies to every row, not only model rows.

Its consumers (later cells, not yours): `SC-e-31` (the AI classifier writes the cleaned name on each row it lands) and
`SC-e-34` (the clean-name row set for the rows the table already holds). They import your function; keep its name and
signature exactly as below.

**Measured 2026-10-07 by the issuer (read-only scan of DynamoDB `etf-classifications`, 3,507 rows):** 883 rows carry a
`name`; 528 of them are all capitals (492 `scheduled`, 33 `seed`, 3 `legacy`); 355 already carry lowercase; 2,624 carry no
name. The all-capitals names are custody-feed strings such as `MAXIMUS INC COM`, `GOLDMAN SACHS BK USA 3.7% 2028`,
`UNITED STATES TREAS NTS 4.125% 02/28/2027`.

**Build:**
1. `infra/aws/lambda/v2_portal/_shared/security_name.py`, one public function `clean_name(name: Optional[str]) ->
   Optional[str]`. Standard library only, ASCII only, no I/O, deterministic. The rule, exactly:
   1. `None` or a blank string returns `None`.
   2. Whitespace is collapsed to single spaces and stripped.
   3. A name that already carries a lowercase letter is the source's own writing: return it after step 2 only.
   4. An all-capitals name: drop one trailing vendor suffix token (`COM` or `SHS`). Then capitalize every word (first
      letter upper, rest lower), treating each hyphen-separated part separately (`COCA-COLA` -> `Coca-Cola`), EXCEPT:
      - a token holding a digit, `%` or `/` is kept exactly (`3.7%`, `02/28/2027`, `5%27`, `10+`, `F3`);
      - a one-letter token is kept upper (share-class letters `F`, `Z`, `A`; the `N A` of a bank name);
      - a token in the keep-upper set `{ETF, ETN, USD, USA, US, U.S., REIT, II, III, IV}` is kept upper;
      - a token in the brand map `{ISHARES: iShares, JPMORGAN: JPMorgan}` takes the mapped spelling.
      No abbreviation is expanded (`BK` -> `Bk`, `TREAS` -> `Treas`): expanding is a meaning call, not casing.
   Keep the suffix list, the keep-upper set and the brand map as module-level constants, so a later cell can extend them
   with a row in a table, not a code change.
2. `infra/aws/lambda/v2_portal/_shared/tests/test_security_name.py`: your own unit tests of each limb above (each rule,
   the hyphen split, idempotence `clean_name(clean_name(x)) == clean_name(x)`, ASCII-only output).

The issuer's grounded table (17 cases, every input a real name read from the live table) is
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/sc_e30_clean_name_table.py`. Read it first; it is the
acceptance. You do not edit it.

### ACCEPTANCE

<criterion id="SC8-e30-AC1" cell_refs="SC-e-30"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/v2_portal/_shared/tests/test_security_name.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC8-e30-AC1` -- your unit tests of every limb of the rule pass.

<criterion id="SC8-e30-AC2" cell_refs="SC-e-30"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/sc_e30_clean_name_table.py</invocation><expect>CLEAN-NAME-TABLE ok=True</expect></criterion>
`SC8-e30-AC2` -- the function reproduces the issuer's 17-case table of real names, controls included.

<expected_criteria>SC8-e30-AC1,SC8-e30-AC2</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`PYTEST-BAD rc=4`, no test file); AC2 FAIL as expected
(`CLEAN-NAME-TABLE ok=False import_error=ModuleNotFoundError`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No table read is needed and no table write is allowed.** This cell is pure code.
- `_shared/` is a Lambda source directory. Do not edit any other file in it, and do not add the module to any shipped-artifacts
  list: that hookup is the issuer's at the merge (R8 "Hookups that belong to no cell").
- **Refusal clause.** If a criterion cannot be met as written (for example a table case that contradicts the rule as stated),
  stop on that criterion, write the reason in your report and a surprise row (id `MDPF_SECCLASS-W26-S<k>`), and do not
  weaken the test.

<paths>
infra/aws/lambda/v2_portal/_shared/security_name.py
infra/aws/lambda/v2_portal/_shared/tests/test_security_name.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-30`.
<owned_cells>SC-e-30</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e30-AC1, SC8-e30-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~26/MDPF_SECCLASS.TO-SC-e30.clean-name-function.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e30-AC1,SC8-e30-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the function's line count, any table case you found ambiguous against the rule, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery (comp-schedule --owner 2.0.0_SA_COO~M --budget 120, 2026-10-07 ~07:3xZ): 8 gates name the lane, all open deploy-ledger entries; none names a clean-name function. This cell declares no schedule.
comp-iam: DECLARED-NOT-APPLICABLE pure code; no role, no table, no S3. R8's comp-iam gaps read (0 gap lines on etf-classifications) stands.
comp-adversary: RUN -- R8's compose flagged _shared/security_name.py and its test GONE (expected: this cell creates them). Cell read by the issuer 2026-10-07: a read-only name census of etf-classifications (3,507 rows; 528 all-caps, 355 mixed, 2,624 unnamed) grounds the 17-case table; BLIND: names in bd-securities and the custody feeds are not sampled here (SC-e-32 and SC-e-34 meet them).
lane: the <paths> block IS the grant.
</preflight>

Risk: R8 says LOCAL; the L6 gate's inferred floor is WORLD (`<paths>` names an infra/ path, `_risk_floor`), so WORLD is
declared. The cell itself deploys nothing.

Source: PRD v0.12 FWD-11, FWD-14, addenda v0.4 and v0.7 @87ad6d2e4c; R8 @495efa3c32. Size: under 100 product lines expected
(`worker-light`, report 2 C7 trial).
