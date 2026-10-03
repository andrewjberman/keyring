# TO IRPT_BCKEND.TO-IB-pr-308 -- the export render host forwards the PATH B print query (account, version) and an Analysis print's request

<to_id>IRPT_BCKEND.TO-IB-pr-308</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~111</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 229 (msg 104735): "S308 re-pointed to 2.0.0_SA_COO~P:
add account, version and request to PRINT_QUERY_KEYS (render_export.cjs:83), with a test, under its own half." GATE (x) puts
this in ROUND 43 (row S267). | **Decomp cell:** `IB-pr-308` (decomposition section 35) | **outcome_ref:** P-6 (the export) |
**depends_on:** none. It is BUILT now, and SERVED under its own never-widen half (the CTO signs on receipt).

---

## WORKER FACE

**What is broken.** A 49 Financial PATH B export on PROD is accepted and frozen, but its render is refused (row
IRPT_BCKEND-S308).
- The render host runs `infra/aws/ec2/investor-reporting-export/render_export.cjs` (in your worktree at
  `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-111/infra/aws/ec2/investor-reporting-export/render_export.cjs`).
- Its `applyPrintQuery` (lines 116-121) copies onto the print URL only the keys in `PRINT_QUERY_KEYS` (line 83):
  `bundle, tenant, revision, kind, selection, start, end`.
- The export's PATH B print query carries `account`, `start`, `end` and `version`. `account` and `version` are dropped, so the
  served print page refuses: "This print URL names no selection".
- An Analysis print's `request` is missing from the list too.

**What you build:**
1. **The allow-list.** In `render_export.cjs`, `PRINT_QUERY_KEYS` gains `'account'`, `'version'` and `'request'`. Keep the seven
   existing keys, and keep the list on ONE line in the same `const PRINT_QUERY_KEYS = [...];` form. No other line of the
   original file changes; criterion IB43-1-AC2 checks this.
2. **Exports for the test.** Only if a test needs them: export `applyPrintQuery` and `PRINT_QUERY_KEYS` in a block APPENDED after
   the file's last line, for example `if (typeof module !== 'undefined') module.exports = { applyPrintQuery, PRINT_QUERY_KEYS };`.
   - First read how the file runs its main flow. Requiring it from a test must not start a render: guard with
     `require.main === module` if the file runs unconditionally.
   - If a guard would need to change an original line, do NOT touch the file; copy the two pure definitions into the test
     instead, and assert they equal the file's text.
3. **Tests.** Create `infra/aws/ec2/investor-reporting-export/tests/test_print_query.cjs` using `node:test`. It needs at least 4
   tests naming `account`, `version`, `selection` and `request`:
   - a PATH B query (account, start, end, version, plus bundle, tenant, revision and kind) reaches the target URL intact;
   - a PATH A query (selection, start, end) still reaches it;
   - an Analysis query's `request` reaches it;
   - an unlisted key (for example `token`, `redirect` or `next`) is DROPPED.
   No network and no browser: the tests exercise the URL-building function only.

<criterion id="IB43-1-AC1" cell_refs="IB-pr-308"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r43/p43_render_print_query_keys.py" . IB43-1-AC1</invocation><expect>IB43-1-AC1 PASS</expect></criterion>
`IB43-1-AC1` -- `PRINT_QUERY_KEYS` (read from the source) holds the seven keys plus account, version and request; the test names the
four words and passes at least 4 tests, 0 failed. Base: FAIL (seven keys, no test).

<criterion id="IB43-1-AC2" cell_refs="IB-pr-308"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r43/p43_render_print_query_keys.py" . IB43-1-AC2</invocation><expect>IB43-1-AC2 PASS</expect></criterion>
`IB43-1-AC2` -- a GUARD: only the `PRINT_QUERY_KEYS` line of the base file changes, lines may only be appended after it, and
`node --check` passes. Base: PASS.

<expected_criteria>IB43-1-AC1,IB43-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none. No upload to `s3://.../ec2/investor-reporting-export/`, no SSM, no render. The deploy is the issuer's, under its
  own never-widen half.
- **Refusal clause.** A change to the render flow, a key beyond the three named, or a vendor or network call in a test is a
  defect: stop and file a row.

<paths>
infra/aws/ec2/investor-reporting-export/render_export.cjs
infra/aws/ec2/investor-reporting-export/tests/test_print_query.cjs
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~111/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/ec2/investor-reporting-export/`, `infra/aws/lambda/investor-reporting/export/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 35 (round 43, workstream ~P), cell `IB-pr-308`.
<owned_cells>IB-pr-308</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB43-1-AC1, IB43-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~111/IRPT_BCKEND.TO-IB-pr-308.render-host-print-query-keys.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB43-1-AC1,IB43-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes, and each criterion's last line;
- the export or copy method you used;
- every test, with its expectation;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the export render host's script (s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/render_export.cjs, downloaded by every irpt-export-render-run SSM command); the change admits three print-query keys onto the print URL, nothing else; 0 served bytes move in the cell; its deploy is a separate never-widen half the CTO signs on receipt (batch 229), arms: a PROD export reaches READY with the frozen as_of, and the rendered series is the frozen VersionId.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes; the print URL gains query keys the served page already reads.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB43-1-AC1 base FAIL (seven keys, no test), IB43-1-AC2 base PASS (guard), dry-run at the base 2026-10-03 ~20:2xZ.
lane: the <paths> block IS the grant.
</preflight>
