# NFRA_OPLGTW task order -- `OG-gr-3` -- adopt the measured grain (R9) in the gateway's serving metadata, on CLOUD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gr-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~22</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change on CLOUD; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM; local tests only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the grain is the CTO's ruling R9 (ledger/ROUND_ANALYSIS.round15.md section 3 @b56208fd64) on your GRAIN_R15.json.
EGRESS CLASS, declared: NONE -- local tests; one read of a measured snapshot's rows already saved by OG-gr-2, if you build the fixture from it (no new S3 read is required).
</preflight>

## 1. THE CELL -- `OG-gr-3` (decomposition addendum R3-T.9, item 1)

R9 adopts the grain you measured as a PAGING ROW-UNIQUENESS KEY, not a business identity. This changes the gateway's
serving metadata only. It never changes silver data or its producer (Andrew-direct 2026-10-03 ~17:3xZ).

1. In `infra/aws/ec2/opal-gateway/app/integrations/schwab/query.py`, change `DATASET_GRAINS`:
   - `dim_position`: `(ACCOUNT_SOURCE, "cusip", "l_s", "quantity_settled_unsettled", "quantity_cash_settled")`;
   - `dim_asset`: `("cusip", "security_description_line_1")`;
   - `dim_balance` and `dim_transaction`: unchanged.
2. In `app/integrations/schwab/datasets.json`:
   - make `grain_fields` match the new grains, in the SERVED names (`account_ref` for the account column, as today);
   - update any grain flags so `semantics.py` accepts the pair at import (it refuses a mismatch);
   - word the grain note: "a ROW-UNIQUENESS key for paging and tie-break, not a business identity; a client must not read
     the quantities as part of what a position is".
   Byte-check that this file and `query.py` are identical on CLOUD and on live `af2d762970` before you edit; they were at
   the cut.
3. New `infra/aws/ec2/opal-gateway/tests/test_schwab_grain_r9.py` with exactly:
   - `test_oggr3_ac01`: on a fixture of ONE measured qualified `dim_position` snapshot (synthetic ids, the measured
     shape, including the 2026-09-21 cash+margin pair), rows-mode paging under the new grain returns every row exactly
     once. Under the OLD grain the same fixture refuses.
   - `test_oggr3_ac02`: the same for `dim_asset`, with its blank-cusip key group.
   - `test_oggr3_ac03`: a PLANTED collision (two rows equal on all five grain columns) REFUSES paging with the module's
     own refusal. It never serves a wrong row.
   No account numbers or names in the fixture.

## AMENDMENT A2 (2026-10-04 ~00:3xZ, issuer; CTO ruling R9a @c9d5c2dd74, ROUND_ANALYSIS.round15.md section 7; row Z-W22-S4)

Your row S4 is right, and the CTO ruled on it (R9a, option (b), narrowed). Paths gain
`infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py`.

1. **The fallback.** In the single-page rows path (`integration.py` ~:687-705), take the branch ONLY when the dataset's
   grain includes a column that is NOT a served field (no request can carry it). In that branch, replace the
   per-result duplicate check with `_grain_unique` on the snapshot: the cached check paging already runs (~:536-555,
   called ~:742-752). A non-unique snapshot refuses with the SAME `duplicate_source_grain` code.
2. **Nothing else changes:**
   - a request whose narrower column set omits a SERVED grain field behaves as today;
   - aggregate mode behaves as today;
   - `dim_balance` behaves as today.
3. **Tests:**
   - restate `test_schwab_query.py::test_ogq2_ac20` to plant a FULL-grain duplicate (equal on all five R9 columns) and
     assert a single-page `dim_position` request is REFUSED `duplicate_source_grain`. List it in `GR3_TEST_EDITS.md`.
   - add to `tests/test_schwab_grain_r9.py`:
     - `test_oggr3_ac04`: a single-page `dim_position` request on a snapshot WITHOUT a full-grain duplicate is served
       (the fallback does not refuse a unique snapshot);
     - `test_oggr3_ac05`: a narrow-column `dim_balance` single-page request is unchanged (the control).
4. **AC1** now requires 5 of 5 named tests in `test_schwab_grain_r9.py` and still NO new failure beyond the baseline.
   `test_ogq2_ac20` must pass. **AC2** admits `integration.py`.
5. Build on CLOUD's `integration.py` as your branch has it. CLOUD and live differ by one line there (the live
   `aws_roles.environ_with_external_ids(...)` call). That line is not yours. `OG-rl-5` merges only your hunks onto the
   live bytes.

## AMENDMENT A1 (2026-10-03 ~23:3xZ, issuer; row Z-W22-S3)

R9's grain makes existing Schwab tests red. Their fixture writers carry no `quantity_cash_settled` (or
`security_description_line_1`). The cell's write surface did not include those files. That is the issuer's spec gap.

- **Paths widen** to every `infra/aws/ec2/opal-gateway/tests/test_schwab_*.py` file. An edit to an EXISTING test file
  may ONLY:
  - add the R9 grain columns to fixture rows or fixture schemas; or
  - restate a grain-declaration assertion to R9's grain.
  It may NEVER delete a test, skip or xfail it, or weaken an assertion.
- **`GR3_TEST_EDITS.md`** (your deliverables) lists every existing test file you edit, each with one line saying what
  changed and why.
- **AC1** now grades "no failure or error beyond the issuer's recorded baseline". The baseline is
  `deliverables/2.0.0_SA_COO~O/r16/GR3_SUITE_BASELINE.txt`: 12 ids at CLOUD 5454d04761, from
  `tests -k schwab -rfE` (3 failed, 9 errors, 115 passed). At least 130 tests must be collected. The three named tests
  must still pass.
- **AC2** admits the widened set and requires the edits file.

## 2. BOUNDS

- **Edit ONLY:** `query.py`, `datasets.json` and the new test file.
- **No:** deploy (`OG-rl-5` ships it), data change, or pipeline change.
- **Never:** push, merge, rebase, stash, `checkout --` or `clean`; override a gate.
- Every `.py` edit passes `.tools/commit-gate.sh`.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/query.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/datasets.json
infra/aws/ec2/opal-gateway/tests/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W22-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gr-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r16/checks/gr3.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 5 of 5; failed/error lines 0.*NEW beyond baseline 0 .*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gr-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r16/checks/gr3.AC2.sh; echo "exit=$?"</invocation><expect>(?s)outside the allowed set: 0; edited existing test files \d+, not listed in GR3_TEST_EDITS.md 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/NFRA_OPLGTW.TO-OG-gr-3.grain-r9-adopt.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit this order's ONE `<status>` tag IN PLACE to `complete`, in the same commit. The board and
   the gates read the first tag; never append a second one.
4. Report once: the diff summary, the literal AC output, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 16 (addendum R3-T.9, item 1); feeds `OG-rl-5`. Pre-cut 22:1xZ: `gr3.AC1` FAIL (test absent; the existing
  suites 41 passed); `gr3.AC2` FAIL (0 files).

<status>complete</status>
<round>16</round>
<slot>~22</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
