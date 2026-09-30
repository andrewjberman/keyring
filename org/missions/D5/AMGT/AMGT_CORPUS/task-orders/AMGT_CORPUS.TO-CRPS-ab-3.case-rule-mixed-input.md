# AMGT_CORPUS task order -- `CRPS-ab-3` -- ROUND 26: `case_rule` refuses a mixed-currency INPUT, not only the value

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ab-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface (the re-derive is a later issuer act; the scoped-API redeploy is AMGT_RESAPP's).
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 26. Serves **every served base case**.

## 1. THE CELL -- `CRPS-ab-3`

**Where this came from (round-25 analysis ruling 3).** `lib/research/api/case_rule.py` computes the Model tab's Base case. It is called
by the producer (`model_block_pull._compute_cases`) and, per request, by the scoped API (`scoped_amgt.py` about `:3195`).
- When quote and reporting currencies differ, it already refuses the VALUE: `status ABSENT`, `cause currency_mismatch`.
- It still builds and serves its constructed input `trailing_median_pe` = PX_LAST / `IS_COMP_EPS_ADJUSTED`. On `BP/ LN Equity` (quote
  GBp, reporting USD) that is 778.57, a number built from mixed currencies.
- The GBp/GBP case is NOT a mix. It is the minor-unit factor (`MINOR_UNIT_FACTOR`), and `NG/ LN Equity` serves 1,298.21 correctly.

**RULED -- what you build:**
1. When quote and reporting currencies differ beyond the minor-unit factor, `case_rule` serves every CONSTRUCTED input null with its
   reason, the trailing-median P/E included. For example `{"value": null, "reason": "..."}`, keeping the input's other descriptive
   fields.
   - The case stays `status ABSENT`, `cause currency_mismatch`.
   - No number built from mixed currencies appears anywhere in the returned case.
   - A raw input carried as landed (for example the consensus EPS figure) may stay; state your reading in the report.
2. The same-currency and GBp/GBP paths are byte-unchanged in value.
3. **Tests:** `lib/research/api/tests/test_case_rule_mixed_input_round26.py` (new):
   - the mixed case serves the input null with a reason;
   - a GBp/GBP case is unchanged;
   - a same-currency case is unchanged;
   - no network.
4. Do NOT touch any other file.

## 3. SURFACES

<paths>
lib/research/api/case_rule.py
lib/research/api/tests/test_case_rule_mixed_input_round26.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-ab-3.case-rule-mixed-input.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ab-3.case-rule-mixed-input.md
</paths>

READ-ONLY: every other file, every S3 object. Scratch `.scratch/ab3/`. Your worktree is a SPARSE checkout; never disable it.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write, NO derive, NO deploy.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W3-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ab-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round26/ab3_AC1.sh</invocation><expect>(?m)^ab3 bp_status ABSENT bp_trailing_input null bp_input_reason_set True ng_status SERVED ng_value 1298.21$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ab-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round26/ab3_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: the checker runs the producer's own `stage_derive` for BP and NG with a write-CAPTURING client (nothing is written) and reads
  each captured `cases.base`. BP's `trailing_median_pe` must be null with a reason, and NG must stay SERVED at 1,298.21.
- AC2: your tests.

## 6. WHEN YOU ARE DONE
1. Write the instance at the proof path in section 3.
2. Run `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit, and pin each
   artifact row to the commit whose BYTES you graded (verify with `git show <pin>:<path>`). It must return rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file, and commit.
4. Report ONCE: each AC line, the refusal's exact shape, and which inputs stay (with the reason).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-25 analysis ruling 3 and enrichment item 3 @`19207dfb83`. Dry-run at base CLOUD `ae1c849af1`: ab3_AC1 FAIL as
designed (`ab3 bp_status ABSENT bp_trailing_input 778.57 bp_input_reason_set False ng_status SERVED ng_value 1298.21`); ab3_AC2 FAIL.

**The served reach:** the scoped API recomputes the case per request from the DEPLOYED `case_rule`. So this fix reaches `/thesis` only
with AMGT_RESAPP's next redeploy. The producer-side block reaches it through aa-4's re-derive path (ab-4). This is named in the ab-4
pair.
<risk>LOCAL</risk>
<status>pending</status>
<round>26</round>
<slot>~3</slot>
<fabric>site-z</fabric>

<status>complete</status>
