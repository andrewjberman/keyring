# AMGT_CORPUS task order -- `CRPS-l-4` -- ROUND 10: `cases-report` REFUSES a security it cannot resolve to landed raw, instead of grading it ABSENT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-l-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only CLI stage; no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 10. Serves row **`Z-S55`**. **Read
`integrations/bloomberg/READ_HERE.md` before anything else in `integrations/bloomberg/`** -- this cell never talks to the
Bloomberg terminal or any vendor; `cases-report` reads raw that has already landed in S3.

## 1. THE CELL -- `CRPS-l-4`

**Where this came from.** `integrations/bloomberg/research/model_block_pull.py` stage `cases-report --securities <...>` takes
the Bloomberg form (`"AMD US Equity"`), maps it with `security_key(...)` and reads the newest landed raw stamp. Given the
underscore key form instead (`AMD_US_Equity`), it does not refuse: measured at the base,
`cases-report --securities AMD_US_Equity` prints `cases AMD_US_Equity base ABSENT ratio none cause none reason no consensus
EPS on the landed block` and `cases_report served 0 refused 1`, rc 0, while `"AMD US Equity"` prints `base SERVED ratio
0.659...`. The underscore form resolves to no (or the wrong) landed raw, and the instrument reports that as a real negative.
`1.0.0_SA_CTO~Z`'s first measurement of 97 keys read 0 of 97 served this way before it was caught (row `Z-S55`).

**RULED -- what you build:**
1. `cases-report` refuses, before computing anything, any requested security whose landed raw it cannot resolve: print
   `REFUSE: <input> resolves to no landed raw stamp under <prefix> (pass the Bloomberg form, e.g. "AMD US Equity")` and exit
   non-zero. Measure first how the underscore input fails today (no stamp? a different key? an empty stamp set?) and refuse on
   exactly that condition -- a resolvable Bloomberg-form security behaves byte-for-byte as today.
2. If several securities are passed and any one is unresolvable, refuse the whole invocation before computing any of them.
3. Change nothing in `derive`, `pull`, `stamp-census` or `case_rule.py`.
4. `integrations/bloomberg/research/tests/test_cases_report_refuses_unresolved.py` (new), offline: an underscore input ->
   REFUSE + non-zero; a resolvable input -> unchanged output; a mixed invocation -> refused whole.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_cases_report_refuses_unresolved.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-l-4.cases-report-refuses-unresolved-key.md
</paths>

READ-ONLY: every other file; every landed S3 object. Scratch `.scratch/l4/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NEVER run `pull` or `derive`. No Bloomberg terminal, MCP or gateway call.
- Existing tests under `integrations/bloomberg/research/tests/` keep passing unmodified.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W3-S<k>`,
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-l-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round10/l4_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-l-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round10/l4_AC2.sh</invocation><expect>(?ms)REFUSE.*^l4 planted_underscore rc [1-9]\d*$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-l-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round10/l4_AC3.sh</invocation><expect>(?m)^cases AMD_US_Equity base SERVED </expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the planted underscore key is refused with a non-zero exit (the positive control the analysis
  names); AC3 the control: the Bloomberg form still serves.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-l-4.cases-report-refuses-unresolved-key.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: how the underscore input failed before, and each AC line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-9 analysis s.2 ruling 4 + s.4 item 4 @`abfad1355c`; row `Z-S55` (the CTO's). Checks dry-run at the
base: AC1 FAIL (no tests ran); AC2 FAIL (`l4 planted_underscore rc 0`, no REFUSE); AC3 PASS (`cases AMD_US_Equity base SERVED
ratio 0.659...`).

<risk>LOCAL</risk>
<status>pending</status>
<round>10</round>
<slot>~3</slot>
<fabric>site-z</fabric>
