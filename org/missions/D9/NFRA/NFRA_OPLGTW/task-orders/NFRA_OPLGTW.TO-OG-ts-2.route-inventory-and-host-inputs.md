# NFRA_OPLGTW task order -- `OG-ts-2` -- ROUTE_CLASS for /yearinreview, host-inputs at 51 keys, per-process export dirs

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ts-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~25</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- tests only; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- local tests; no AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's (round-18 analysis s.4 item 1; rows Z-W22-S9, S10, Z-W25-S3).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ts-2` (decomposition addendum R3-T.12, item 1)

All paths are under `infra/aws/ec2/opal-gateway/`.

1. **Row Z-W22-S10.** `tests/test_principal_cutover.py`'s `ROUTE_CLASS` (about `:489-598`) lacks `/yearinreview` and
   `/yearinreview/`. Classify both with the SAME class as `/sprint`. Also align the route census in
   `tests/test_data_entitlement_guard.py` (about `:719-729`) if it lists routes.
2. **Row Z-W22-S9.** In `tests/test_schwab_host_inputs.py`:
   - `test_values_that_can_hold_whitespace_are_rendered_quoted` asserts 50 `.env` keys. Live renders 51 since r17c
     (`YEARINREVIEW_VIEW_ALLOWED_EMAILS`, CTO R15), so bump the count to 51.
   - `test_grant_writer_stages_the_contract_only_from_the_standard` calls `_derive_import_closure()` with the OLD
     signature. Align the call to CLOUD's `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/build_package.py`
     signature. Do NOT edit `build_package.py`.
   - Do NOT edit `deliverables/2.0.0_SA_COO~O/r17/Q7_SUITE_BASELINE.txt`. That file is in the issuer's lane, and the
     issuer removes the S9 pair at your drain.
3. **Row Z-W25-S3.** Two schwab runs launched concurrently share one export directory under the temp dir, and
   `test_ogx1_ac27` failed with FileNotFoundError. Give each test process its own export directory, for example under
   pytest's `tmp_path_factory` or a per-pid subdirectory, so concurrent runs cannot collide. Test fixtures only.
   - Add `tests/test_schwab_export.py::test_ogts2_export_dir_per_process`. It proves the export directory the test
     process uses is unique to that process, for example that it contains `os.getpid()` or sits under
     `tmp_path_factory`, and that two values computed for different pids differ.
   - The concurrent run alone passed before any fix (the collision is intermittent), so this named test is what
     grades the mechanism.

Each of the three files must run green in its own process. The whole schwab set must still run in one process with
0 errors (OG-ti-2's state).

## 2. BOUNDS

- No product code (`app/`), no `build_package.py` change, no deploy. Never delete, skip or xfail a test.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~25/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W25-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ts-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r19/checks/ts2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)test_principal_cutover.py rc=0 .*test_data_entitlement_guard.py rc=0 .*test_schwab_host_inputs.py rc=0 .*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ts-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r19/checks/ts2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 1 of 1; failed/error lines 0.*concurrent export runs: passed [1-9]\d*; failures beyond baseline 0 \[\]; FileNotFoundError 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~25/NFRA_OPLGTW.TO-OG-ts-2.route-inventory-and-host-inputs.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`, and on PASS edit this order's ONE `<status>` tag IN
PLACE to `complete`. Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 19 (R3-T.12, item 1). Chain: `OG-ts-2` -> `OG-rl-7`. The release carries these test fixes and runs R21's
  inventory arm green.
- Pre-cut: see the issuance commit.

- **A1 (2026-10-06 ~03:xxZ, issuer): REOPENED.** At drain c23d8914e6, AC1 and AC2 PASSed on CLOUD, but the issuer's
  re-grade of the round-18 floor `ti2.AC1` FAILed. In the one-process whole set, `test_ogts2_export_dir_per_process`
  hit `import conftest` resolving to `tests/acceptance/conftest.py`. The re-hand fix is a uniquely named
  `tests/proc_tmp_root.py`.
  - The fix was refused at commit (row Z-W25-S4) because this order read `complete`. That was the issuer's error, and
    the status returns to `pending` so the fix can land.
  - **Added criterion (no new check):** `r18/checks/ti2.AC1.sh` must PASS on the drained union.
  - Flip back to `complete` after the commit.

<status>complete</status>
<round>19</round>
<slot>~25</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
