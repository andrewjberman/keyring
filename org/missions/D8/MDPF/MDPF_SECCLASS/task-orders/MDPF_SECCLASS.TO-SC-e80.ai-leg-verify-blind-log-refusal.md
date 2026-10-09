# TO MDPF_SECCLASS.TO-SC-e80 -- round 16 SC-e-80: ai_leg_verify refuses when keys are absent but the given logs yield zero reason lines for them

<to_id>MDPF_SECCLASS.TO-SC-e80</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~70</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-80` (`decompositions/MDPF_SECCLASS_DECOMP_R16.md`) |
**outcome_ref:** FWD-15 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-80`, row MDPF_SECCLASS-D1-S15. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/ai_leg_verify.py` grades an
AI leg's close. Its `read_unresolved(paths)` (:71-78) keeps only lines that START with `UNRESOLVED `. On e49 the runner's stdout was
captured with a timestamp prefix (`[+   154.0s] UNRESOLVED KEY: ...`), so 387 real reason lines read as zero, and the tool reported a
confident wrong verdict with no error. Today a log that yields nothing is indistinguishable from a run that refused nothing.

**Build:**
1. Add a pure function `blind_log_refusal(absent_keys, reasons, logs)` to `ai_leg_verify.py`. It returns:
   - a problem string when `logs` is non-empty, `absent_keys` is non-empty, and NONE of `absent_keys` is a key of `reasons`;
   - `None` in every other case, including no logs given, or at least one absent key with a reason.
   The string names the counts, e.g. `blind-logs: N absent keys, 0 reason lines in M log(s) (prefixed or wrong logs?)`.
2. In `main()`, after `reasons` and `absent` are computed (:128-129), call it. If it returns a string, append it to the problems list
   that `grade()` receives, so the verdict reads `ok=False` and the problem is printed.
3. Change nothing else: `read_unresolved`'s anchored parse, `grade`, and the printed line's existing fields stay as they are. Do not
   strip prefixes; the refusal is the remedy this row asks for.

### ACCEPTANCE

<criterion id="SC16-e80-AC1" cell_refs="SC-e-80"><invocation>python -m pytest -q org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R16_CHECKS/test_r16_ai_leg_verify_blind.py</invocation><expect>3 passed</expect></criterion>
`SC16-e80-AC1` -- the three arms pass: a prefixed log with absent keys is refused; a readable log is not; no logs is not this refusal.
Do not edit this test file.

<expected_criteria>SC16-e80-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1, 2026-10-09 ~09:0xZ): SC16-e80-AC1 FAIL, as expected (3 failed: no `blind_log_refusal`).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **No AWS call at all**; the criterion is pure-function. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W70-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/ai_leg_verify.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R16.md</decomp_doc> (round 16), cell `SC-e-80`.
<owned_cells>SC-e-80</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC16-e80-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~70/MDPF_SECCLASS.TO-SC-e80.ai-leg-verify-blind-log-refusal.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC16-e80-AC1`.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), the criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE an issuer check script; nothing scheduled runs it.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call in the cell.
comp-adversary: RUN -- a readable log wrongly refused (arm 2); a no-log call wrongly refused (arm 3); the refusal silently not wired into main (step 2, read in review)
lane: the <paths> block IS the grant.
</preflight>

Source: CTO rounds 13-15 analysis section 3 item 2 (msg 2139); row D1-S15; DECOMP_R16.
