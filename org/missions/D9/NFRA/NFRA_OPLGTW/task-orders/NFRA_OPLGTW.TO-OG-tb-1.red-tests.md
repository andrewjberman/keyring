# NFRA_OPLGTW task order -- `OG-tb-1` -- the 9 OPLGTW red tests: each repaired on CLOUD or named with its reason

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-tb-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~18</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- test repairs; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS resource or permission is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the list is NFRA_MCPINDEX's round-6 L8 packet section 4, carried by the CTO (analysis round 12 s.5 item 6).
EGRESS CLASS, declared: NONE (local tests only).
</preflight>

## 1. THE CELL -- `OG-tb-1` (decomposition addendum R3-T.7, item 6)

Nine OPLGTW tests are red on the live ref and on MCPINDEX's release tree
(`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/L8_PACKET_ROUND6.md:50-59`; failure text in
`.../NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~22/probes_r8/tests_perfile_liveref_PHASEA.txt`). On CLOUD at
the cut: 3 PASS (`test_oga3_ac01`, `test_ogo1_ac07`, `test_ogq1_ac07`: their failure was a tree-relative path outside
a deploy-only tree), 6 red:

| test | failure seen (live-ref run) | likely class |
|---|---|---|
| `tests/test_browser_oidc.py::test_oga3_ac07` | KeyError 'transcript_route' | stale registry after /hx |
| `tests/test_principal_cutover.py::test_oga2_ac04` | route list mismatch (`/hx/mail/messages` present) | stale route list |
| `tests/test_data_entitlement_guard.py::test_ogz1_ac05` | KeyError 'unclassified' | stale classification table |
| `tests/test_data_entitlement_guard.py::test_ogz1_ac08` | route-set count 43 / set mismatch | stale route set |
| `tests/test_entitlement_admin.py::test_ogz2_ac06` | "expected profile + grant + operator_audit puts, got 4" | operator_audit count |
| `tests/test_schwab_export_stream.py::test_ogx4_ac03` | ServiceError: memory | environment (memory) |

1. Run each on CLOUD (`cd infra/aws/ec2/opal-gateway && python -m pytest <file>::<test>`, `AUDIT_PATH` isolated) and read
   the actual failure.
2. Where the TEST is stale against a deliberate product change (a route, tool or classification added by a named,
   released cell), update the test's expectation, citing that cell. Where the PRODUCT is wrong, do NOT fix product
   code: name it. Where the environment cannot run it (memory), name it with the measurement.
3. Write `deliverables/0.9.0_WK_NFRA_OPLGTW~18/RED_TESTS_R13.json`: one entry per test id above AND the three already
   passing, key `<file>::<test>`, value `{"status": "PASS"|"NAMED", "reason": "<the cause, the cell it traces to, or the
   product defect>"}`. A product defect also gets a surprise row.

## 2. BOUNDS

Edit ONLY the five test files named in SURFACES; no product file, no deploy. Never push, merge, rebase, stash, `checkout --`
or `clean`; never override a gate. Every `.py` edit passes `.tools/commit-gate.sh`; commit with `.tools/safe-commit.sh`.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/test_browser_oidc.py
infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py
infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
infra/aws/ec2/opal-gateway/tests/test_schwab_export_stream.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~18/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W18-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-tb-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/tb.AC1.sh; echo "exit=$?"</invocation><expect>(?s)unaccounted 0 \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: each of the 9 passes now or is named with a reason. The PASS count is reported, not required.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~18/NFRA_OPLGTW.TO-OG-tb-1.red-tests.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`; if it PASSES, append a `complete` status tag after the
order's last status line in the same commit. Report once: per test, PASS or the named reason.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 14 (addendum R3-T.7, item 6). Pre-cut on CLOUD: `tb.AC1` passing 3, unaccounted 6, FAIL. A "named" test
  that hides a product defect is the failure mode to watch at the drain.

<status>pending</status>
<status>complete</status>
<round>14</round>
<slot>~18</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
