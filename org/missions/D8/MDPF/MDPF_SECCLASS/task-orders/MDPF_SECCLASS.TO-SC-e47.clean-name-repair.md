# TO MDPF_SECCLASS.TO-SC-e47 -- round 9 SC-e-47: FWD-14 -- repair `clean_name` for acronyms, tickers used as names and joining words (row W28-S5)

<to_id>MDPF_SECCLASS.TO-SC-e47</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~56</issued_to>
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

### AMENDMENT R12c (issuer, 2.0.0_SA_COO~M1, 2026-10-07 ~18:4xZ; row MDPF_SECCLASS-S62)

`clean_name()` passes non-ASCII through. Two live rows show it:
- The e48 write landed `Vanguard US Growth Admiral` + U+2122 on VWUAX, which had no name before.
- It also landed `American Century Ultra` + U+00AE + ` Inv` on CUSIP:025083882.
The old-list set carries 40 such names (37 with U+00AE, 3 with U+2122). CLAUDE.md: no non-ASCII in production code, logs or AWS.
1. In `clean_name()`, make the output ASCII only:
   - drop the signs U+00AE, U+2122 and U+00A9;
   - fold any other character to its ASCII base with `unicodedata` NFKD (stdlib), and drop what has none;
   - collapse the doubled spaces this leaves.
   Keep the module's own source ASCII: write each sign as a backslash-u escape.
2. Pin these in `test_security_name.py`:
   - the four new issuer-table cases;
   - one accented case (`NESTL` + U+00C9 + ` SA` -> `Nestle SA`);
   - a test that `clean_name(x).isascii()` holds for every case in the module's tests.
3. The issuer table gained the four U+00AE/U+2122 cases. The criteria are as before (AC1 table, AC2 tests, AC3 census), and AC3 must
   still read ok=True at your head.
You do NOT rebuild the e48 set. The issuer rewrites the two live rows as a literal two-key act.

### AMENDMENT R12b (issuer, 2.0.0_SA_COO~M1, 2026-10-07 ~17:5xZ; the CTO's SC-e-48 re-sign condition @4f8bd85bc4)

The re-sign is SIGNED on one fix before `--write`. An X&Y token is title-cased in its second half (`S&P` -> `S&p`, `AT&T` -> `At&t`):
8 of the 1,360 writes, for example `iShares S&p 500 Growth ETF`.
1. In `clean_name()`, keep an X&Y token (letters, an ampersand, letters, no space) upper in both halves when its input is upper.
   Pin S&P, AT&T and P&G in `test_security_name.py`.
2. Rebuild the set with the same held build (`--held-root C:/Dev/wk-secclass-r9-38/.scratch`, as before).
3. **The set diff against 78715af985's TSV may touch ONLY the `clean_name` of rows whose name carries `&`.** List each changed row in
   your report. Any other diff is a STOP and a row.
4. Run the writer's dry run; it must read `refused_stale=0`.
The issuer table gained S&P, AT&T and P&G (34 cases). Criteria are as before: AC1 table, AC2 tests, AC3 census.

### AMENDMENT R12 (issuer, 2.0.0_SA_COO~M1, 2026-10-07 ~17:4xZ; release mode, SC-e-48's CTO half REFUSED @cadf21e1f1)

**Why it re-opens.** SC-e-48's clean-name write was refused on the names, not the mechanism. In its set
(`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_V2_20261007.tsv`, 1,740 rows, 1,349 WRITE), 73 writes
would land a visibly wrong name: `ABB LTD SPONSORED ADR` -> `Abb LTD Sponsored Adr`, `PGIM AAA CLO ETF` -> `Pgim Aaa Clo ETF`, and
LTD/Ltd and PLC/Plc are split across the set. The CTO's items, verbatim in substance:
1. In `clean_name()`, each depositary and fund form reads upper: ADR, ADS, ETF.
2. Each corporate form reads ONE casing, whatever the input's casing. PLC is upper (W28-S5 pin), so LTD and the foreign forms (SA, SE,
   AG, NV) are upper too. `Inc`/`Corp`/`Co` keep the title case already pinned. A pin test covers each form in both input casings,
   including a mixed-case input (`Ferguson Plc Ord` -> `Ferguson PLC Ord`).
3. Short all-caps tokens that are not dictionary words read upper (`ABB`, `AAA`, `CLO`, `PGIM`). You have no dictionary and may
   download none. Use a rule you can state: for example, a token of 2-4 letters with no vowel or an unpronounceable cluster, plus an
   explicit keep-upper list for the named ones. List every exception the rule cannot make exact in the pin test, and in your report.
4. Rebuild the set with `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/clean_name_row_set_v2.py` (read-only
   reads), then run the writer's dry run,
   `python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/clean_name_write_v2.py`, and report its line. If a firm
   read the builder needs is denied on dell1, file a row and stop; never guess a held name.

The issuer's table `R10_CHECKS/sc_e30_clean_name_table.py` gained seven cases at this amendment (31 cases; base 6 mismatches); you do
not edit it. `clean_name` must stay idempotent.

### ACCEPTANCE

<criterion id="SC9-e47-AC1" cell_refs="SC-e-47"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/sc_e30_clean_name_table.py</invocation><expect>CLEAN-NAME-TABLE ok=True</expect></criterion>
`SC9-e47-AC1` -- the issuer's grounded table (23 cases, real names, the W28-S5 cases among them) reads 0 mismatches.

<criterion id="SC9-e47-AC2" cell_refs="SC-e-47"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/v2_portal/_shared/tests/test_security_name.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC9-e47-AC2` -- the module's own tests pass, the new branch tests with them.

<criterion id="SC12-e47-AC3" cell_refs="SC-e-47,SC-e-48"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/sc_e48_name_census.py</invocation><expect>SC-E48-CENSUS ok=True</expect></criterion>
`SC12-e47-AC3` -- the rebuilt set's WRITE rows carry no title-cased depositary/foreign form, no title-case Ltd/Plc and no all-caps
Inc/Corp/Co, and no form appears in both casings across the set. The third criterion's reason: the refused act is the set, not only
the function.

<expected_criteria>SC9-e47-AC1,SC9-e47-AC2,SC12-e47-AC3</expected_criteria>

Dry-run at the base 5d70aab6c9: AC1 FAIL as expected (`ok=False cases=23 mismatches=11`); AC2 PASS as expected (control: 51 passed;
it must still pass after the edit).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
- The issuer's table `sc_e30_clean_name_table.py` is READ-ONLY to you: a case you believe it gets wrong is a surprise row, never an edit.
- **No package install and no download of any kind** (no pip, npm, curl or tool fetch, into any environment; row S49). No table
  write, no deploy, no upload, no model call.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W56-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
infra/aws/lambda/v2_portal/_shared/security_name.py
infra/aws/lambda/v2_portal/_shared/tests/test_security_name.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_V2_20261007.tsv
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-47`.
<owned_cells>SC-e-47</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e47-AC1, SC9-e47-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~56/MDPF_SECCLASS.TO-SC-e47.clean-name-repair.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e47-AC1,SC9-e47-AC2,SC12-e47-AC3` BEFORE the flip.
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
