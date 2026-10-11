# TO ADVI_COTBKF.TO-CB-bl-4.stamp-switch -- round 64 CB-bl-4: the older mint tests supply a stamped manifest and the test-only switch leaves the product file

<to_id>ADVI_COTBKF.TO-CB-bl-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~93</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>64</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bl-4` (`decompositions/ADVI_COTBKF_DECOMP.round64.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Read first:** rows ADVI_COTBKF-D2-W86-S2 and D2-W87-S1 in the channel, and `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_64_20261011.md` section 3 (the test-hygiene row).

**The problem.** The mint adapter refuses an unstamped manifest, but it carries a module flag `REQUIRE_STAMPED` (line 142, read at
line 759) that exists only so an OLDER test module can pass bare manifests: `data/assets/scripts/silver/tests/conftest.py` line 52
sets it False for `test_commonwealth_ard_apply`. A product-code switch whose only user is a test is an escape hatch.

**Your item. No AWS call; tests fake S3.**

1. In `data/assets/scripts/silver/tests/test_commonwealth_ard_apply.py`: every manifest a test hands to `apply_days` or
   `verify_served` is a STAMPED manifest (the three fields the stamp writes: `vocabulary_notes`, `reasons_sidecar` with its address,
   sha256 and rows, `method_row`), built the way `test_commonwealth_ard_mint_claims.py` builds one. Where a test's faked bucket then
   needs the sidecar and the method row, give it them. Keep every assertion's `==`; update an expected line only to the line the
   stamped path really prints.
2. Remove the switch: delete the `REQUIRE_STAMPED` monkeypatch (and its fixture if nothing else uses it) from `tests/conftest.py`, and
   delete the `REQUIRE_STAMPED` flag and the branch that reads it from
   `data/assets/scripts/silver/commonwealth_account_return_daily.py`, so an unstamped manifest is refused unconditionally. Change
   nothing else in the adapter.
3. Commit the test changes FIRST with the switch still in place (they must pass); then the removal. Report both pytest lines.

**If a test cannot pass on a stamped manifest without weakening an assertion or changing other product code, stop: that is the
refusal clause, and say which test.**

### ACCEPTANCE

<criterion id="CB64bl4-AC1" cell_refs="CB-bl-4"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB64bl4-AC1` -- the silver suite passes with the variable unset: 0 failed, 0 errors, 12 skipped as before this order.

<criterion id="CB64bl4-AC2" cell_refs="CB-bl-4"><invocation>python -c "a=open('data/assets/scripts/silver/commonwealth_account_return_daily.py',encoding='utf-8').read();c=open('data/assets/scripts/silver/tests/conftest.py',encoding='utf-8').read();print('STAMP-SWITCH adapter_hits=%d conftest_hits=%d'%(a.count('REQUIRE_STAMPED'),c.count('REQUIRE_STAMPED')))"</invocation><expect>STAMP-SWITCH adapter_hits=0 conftest_hits=0</expect></criterion>
`CB64bl4-AC2` -- the switch is gone from the product file and from the conftest.

<expected_criteria>CB64bl4-AC1,CB64bl4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch:** `apply_days`, `build`, `verify_served` or any mode of the adapter beyond the flag and its one branch; any other
  test; anything under `data/assets/scripts/gold/`.
- **Do NOT run `--apply` or `--verify-served`.** No AWS or S3 call. No push.
- **No gate override** of any kind and no `--force`. If a gate refuses and the fix is not an ordinary correction inside your grant,
  stop and report its exact refusal line.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row: the next
  free `ADVI_COTBKF-D2-S<k>` id read from the channel at write time, `"fabric": "dell2"`, `surfaced_at` read from the clock. Do not
  weaken or skip a test.

<paths>
data/assets/scripts/silver/commonwealth_account_return_daily.py
data/assets/scripts/silver/tests/conftest.py
data/assets/scripts/silver/tests/test_commonwealth_ard_apply.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round64.md</decomp_doc> (round 64), cell `CB-bl-4`.
<owned_cells>CB-bl-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB64bl4-AC1, CB64bl4-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~93/ADVI_COTBKF.TO-CB-bl-4.stamp-switch.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB64bl4-AC1,CB64bl4-AC2` BEFORE the flip. Both are mechanical.
</proof_of_spec>

**REPORT:** the pytest line after the test changes with the switch still in place, and after its removal; the `STAMP-SWITCH` line; what each test now supplies, by count; the diff of the adapter (it should be the flag and one branch); commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one hand-run adapter and its tests.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; tests fake S3.
comp-adversary: RUN -- the tests change first with the switch in place, so a test that only passed through the switch shows itself before the switch goes; == is kept; BLIND: a caller outside the tests that set the flag (the issuer found none by reading the two files that name it).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-64 analysis @5cc2574c67 (msg 4579), section 4 item 4; `3.0.0_SA_CVO` REMEDIATION_v36 @877c95fb20.
