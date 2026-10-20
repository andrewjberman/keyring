# NFRA_OPLGTW task order -- `OG-sz-2` -- one existing test pinned the old size measure: `tests/test_og_rv2.py::test_ogrv2_ac01` builds 120 wide rows that fit 50 KB COMPACT but not as served (round 47; the one regression the issuer's full-suite comparison found after `OG-sz-1`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sz-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-sz-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~173</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a test-only change; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the repair of a test premise broken by the CTO's round-46 analysis rank 2 (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round46.md` @ad17495429: "the 50 KB cap is measured on the bytes actually sent"), cell `OG-sz-1`.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-sz-2` (decomposition addendum R3-T.124, amendment A3, round 47, workstream ENRICH-R47-D)

WHY. `OG-sz-1` changed `harvest_typed._size()` to measure an answer the way the server serves it (`json.dumps(obj, indent=2, default=str)`), which is larger than the compact measure. `tests/test_og_rv2.py::test_ogrv2_ac01` ends with a block that builds 120 WIDE trade rows for one fund (`_wide_trade_part(120)`, defined at about line 289) and asserts they come back whole and narrowed "within the 50 KB answer": `not wide.get("truncated")`, `len(wide["trades"]) == 120`, `wide["denominator"]["rows_returned"] == 120`. Under the served measure 120 narrowed rows (15 columns each) are about 54 KB, so the answer is correctly truncated and the test fails (`{'absent_reason': None, 'truncated': True}`). The product behaviour is right; the test's row count is a premise of the old measure.

DO, in `infra/aws/ec2/opal-gateway/tests/test_og_rv2.py` ONLY, the smallest change that restores the premise: replace the row count 120 by **80** everywhere it names that block's count: the argument of `_wide_trade_part(...)` in the `env({...})` call, the two row-count assertions (`len(wide["trades"]) == 120` and `wide["denominator"]["rows_returned"] == 120`), and any comment or docstring of the block or of `_wide_trade_part` that says 120 rows (its docstring says "so 120 full rows would exceed the 50 KB answer"; make it say 80). Change nothing else: the assertions about `columns_dropped`, the 15-column set of each trade, "each dropped name is listed once" and `not wide.get("truncated")` stay as they are. If 80 rows still come back truncated on the merged trunk, lower the count in steps of 10 until the test passes and keep it between 60 and 79; say so in your report. Do not edit any product file, any other test or the helper `harvest_typed`.

## 2. BOUNDS

- Write only `infra/aws/ec2/opal-gateway/tests/test_og_rv2.py`, `W/` and, if a row is needed, the channel. NO product file, no other test, no release, no deploy, no AWS call.
- Never: push, `git stash`, rebase, `checkout --` or `clean`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/test_og_rv2.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~173/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W173-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sz-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sz2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)tests/test_og_rv2\.py: 4 passed, 0 failed \(want 4 passed, 0 failed\); test_ogrv2_ac01 passes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-sz-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/sz2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)lines changed [1-9]\d* \(want 1 to 12\); every removed line names the old row count or the row-count comment: ok.*narrowing assertions kept: ok; new row count N [6-9]\d \(want 60 to 119\); N appears in the part builder call and in at least two row-count assertions: ok; lines still naming 120: 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the whole file passes, `test_ogrv2_ac01` included. `AC2`: the edit is only the row count and its mentions, against the pinned blob of the file at the issuance.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-sz-2.round-47-the-wide-row-count-of-test-og-rv2-under-the-served-measure.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). Report once; the `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-D, `<risk>WORLD</risk>` is the gateway-path floor (a test under the gateway folder). Found by the issuer's per-test-id comparison of the merged trunk's full suite (1280 tests, 44 failures) against the pre-merge commit `6f2ddfd58e` (1233 tests in a sparse tree, 59 failures): the only test failing on the trunk and passing at the base is `test_ogrv2_ac01`. The 44 failures on the trunk are the live ref's own.
- READING DISCLOSED TO THE CTO: the product behaviour is the intended effect of `OG-sz-1` (P4: measure what is served); 120 narrowed wide rows no longer fit. The test is changed, not the product. The cell rides `OG-rl-17`'s take list.
- Pre-cut: `AC1` base FAIL as expected (3 passed, 1 failed); `AC2` base FAIL as expected (0 lines changed, N 120). Arm fed to the checks: a scratch copy with 120 replaced by 80 read `AC1` PASS (4 of 4) and `AC2` PASS (4 lines changed), then was restored.

<status>pending</status>
<status>complete</status>
<round>47</round>
<workstream>ENRICH-R47-D</workstream>
<slot>~173</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
