# TO MDPF_SECCLASS.TO-SC-e47 -- round 9 SC-e-47: FWD-14 -- repair `clean_name` for acronyms, tickers used as names and joining words (row W28-S5)

<to_id>MDPF_SECCLASS.TO-SC-e47</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~35</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-47` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-14 | **depends_on:** none. Slot `~35`, first in its queue (then `TO-SC-e48`).

---

## WORKER FACE

### THE CELL

`SC-e-47`: "`clean_name` repair (W28-S5): acronyms, tickers used as names, small words; the test table grows with the measured
failures" (DECOMP_R9). Analysis ruling 2.2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md`):
FWD-14's names pass through `clean_name` "once W28-S5 is repaired"; this cell is that repair.

**The defect (row W28-S5, measured by round 8's SC-e-34):** `clean_name()` in
`infra/aws/lambda/v2_portal/_shared/security_name.py` capitalizes every all-caps word, so acronyms and tickers come out wrong:
`BP PLC` -> `Bp Plc`, `GSK PLC` -> `Gsk Plc`, `MPLX LP` -> `Mplx Lp`; a name that is only its ticker (`WMT`) -> `Wmt` (20 seed rows);
joining words read `Of`; a bank form reads `Na`.

**The rule to implement is the issuer's** (the docstring of
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/sc_e30_clean_name_table.py`, read it in full). In step 4 (an
all-capitals name), in addition to round 8's rule, keep EXACTLY as written:
- a whole name that is ONE token of 1-5 characters (a ticker used as the name);
- a token of 2-4 letters holding no vowel (A E I O U Y): an acronym or abbreviation (BP, GSK, MPLX, BK, NTS, MKTS, BLDR);
- a token in the corporate-form set {PLC, LP, LLC, NA, NV, AG, SA, SE};
and lower a joining word {OF, AND, THE, FOR, IN, ON, AT, TO, BY} that is not the first word. Everything else in round 8's rule
stands (suffix drop, keep-upper set, brand map, digit/%/ / tokens, one-letter tokens, the source's own mixed-case writing untouched).
Four round-8 expectations change with the rule: BK, NTS, MKTS and BLDR now stay upper.

**Build:**
1. Edit `security_name.py` only (keep the signature `clean_name(name: str | None) -> str | None` and the module-level constants;
   add the new sets as module-level constants).
2. Grow `infra/aws/lambda/v2_portal/_shared/tests/test_security_name.py` with one test per new rule branch (each W28-S5 input and
   one negative per branch, e.g. a 4-letter word with a vowel still capitalizes).
3. ASCII only.

### ACCEPTANCE

<criterion id="SC9-e47-AC1" cell_refs="SC-e-47"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/sc_e30_clean_name_table.py</invocation><expect>CLEAN-NAME-TABLE ok=True</expect></criterion>
`SC9-e47-AC1` -- the issuer's grounded table (23 cases, real names, the W28-S5 cases among them) reads 0 mismatches.

<criterion id="SC9-e47-AC2" cell_refs="SC-e-47"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/v2_portal/_shared/tests/test_security_name.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC9-e47-AC2` -- the module's own tests pass, the new branch tests with them.

<expected_criteria>SC9-e47-AC1,SC9-e47-AC2</expected_criteria>

Dry-run at the base 5d70aab6c9: AC1 FAIL as expected (`ok=False cases=23 mismatches=11`); AC2 PASS as expected (control: 51 passed;
it must still pass after the edit).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
- The issuer's table `sc_e30_clean_name_table.py` is READ-ONLY to you: a case you believe it gets wrong is a surprise row, never an edit.
- **No package install and no download of any kind** (no pip, npm, curl or tool fetch, into any environment; row S49). No table
  write, no deploy, no upload, no model call.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W35-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
infra/aws/lambda/v2_portal/_shared/security_name.py
infra/aws/lambda/v2_portal/_shared/tests/test_security_name.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-47`.
<owned_cells>SC-e-47</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e47-AC1, SC9-e47-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~35/MDPF_SECCLASS.TO-SC-e47.clean-name-repair.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e47-AC1,SC9-e47-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** each new rule branch and its test, the AC1 line, the AC2 summary, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a pure function and its tests; no schedule, trigger or gate names it.
comp-iam: DECLARED-NOT-APPLICABLE pure code; no role, table or bucket is read or written.
comp-adversary: RUN -- the issuer extended the grounded table with the W28-S5 inputs (real table names) and stated the rule in its docstring; base 11 mismatches; the four round-8 expectations that change are named on the face. BLIND: names outside the table and the custody feeds (SC-e-48 meets them).
lane: the <paths> block IS the grant. security_name.py is not a shipped lib/_shared member (safe_deploy_core.py:95-99).
</preflight>

Source: PRD v0.13 FWD-14 @90f99888cd; round-8 analysis ruling 2.2 @1ca9e97fc9; DECOMP_R9 @5d70aab6c9; row W28-S5.

## AMENDMENT 1 (2.0.0_SA_COO~M1, 2026-10-07 ~12:0xZ) -- ruling on row W35-S1: trailing vendor suffixes drop repeatedly

The worker applied the issuer's round-9 rule exactly and found it not idempotent: `SHS` is a no-vowel 3-letter token, so `ETF SHS COM`
cleans to `ETF SHS` and a second pass to `ETF`. RULING: step 4 drops EVERY trailing vendor-suffix token (`VENDOR_SUFFIXES`), repeatedly,
before any casing rule, so `clean_name(clean_name(x)) == clean_name(x)` for every input. The issuer's table gains `("ETF SHS COM", "ETF")`
(base at the worker's head fcadb7a348: 1 mismatch). Move `ETF SHS COM` back into the idempotence test. `<status>` re-opened to
in_progress; criteria unchanged. Gate limb: none graded this modification (no new order; no `<placeholders>`).
