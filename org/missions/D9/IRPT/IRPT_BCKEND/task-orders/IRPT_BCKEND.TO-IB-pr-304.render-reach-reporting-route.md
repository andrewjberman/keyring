# TO IRPT_BCKEND.TO-IB-pr-304 -- a render token can reach the 49F reporting series route: the edge admits the path, and the reporting-read function reads the render grant (nothing served)

<to_id>IRPT_BCKEND.TO-IB-pr-304</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~107</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>39</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** the issuer, inside its decomposition, on rows IRPT_BCKEND-W105-S1 and W105-S2
(BLOCKING, INERT). IB-pr-302 (merged @7d02c6fe8b, CTO batch 205) filed them, naming this seat as owner: its Enforcer half is landed,
but nothing upstream or downstream of it reaches. GATE (x) puts this in ROUND 39 (row S267). | **Decomp cell:** `IB-pr-304`
(decomposition section 31) | **outcome_ref:** P-6 (the export survives the retirement) | **depends_on:** IB-pr-302 (merged)

---

## WORKER FACE

**Where it stands.** The PATH B export now pins and renders through the 49F reporting route under a render token (IB-pr-302), and
the Enforcer admits `reporting_read` for a render delegate. Two things still refuse, and both fail closed:
- **S1, the edge.** `infra/aws/lambda-edge/auth-validator-edge/render_auth.mjs` `RENDER_API_PATH_PATTERNS` admits a render token
  only on the performance, analysis-sections and narrative API paths. A render token on the reporting series route is refused at
  the edge, before the Enforcer.
- **S2, the function.** `irpt-49f-reporting-read-lambda` has no `IRPT_EVIDENCE_BUCKET`, no read of the render-grant objects, and no
  `_render_identity` modules. So `served.render_ports_from_env()` returns None, and every delegate read refuses.
- Three read functions already carry this wiring; copy them. `irpt-status` (ops root) and `irpt-performance-adapter` (performance
  root) take `IRPT_EVIDENCE_BUCKET` from the core remote state, stage `_render_identity/grant.py` and `report_owner.py`, and grant
  the read of the grant objects.

**What you build.**
1. **Edge (S1).** In `render_auth.mjs`, add ONE pattern named `reporting` that admits exactly the series read,
   `/^\/api\/scoped\/investor-reporting\/reporting\/[^/]+\/series$/`. It must NOT admit the manifest or the summary route.
   - Keep the three existing patterns.
   - If the edge also matches the token's route claims to the path, read how and add the matching claim for this route in the same
     shape, or file a row if the claim lives outside this file.
   - Update the comment, which says "three".
2. **Function (S2).**
   - In `infra/aws/terraform/investor-reporting/reporting-read/lambda.tf`, set `IRPT_EVIDENCE_BUCKET`. Use the same source the ops
     and performance roots use; add the core remote-state data source in this root if it is absent, in its own file within your
     paths.
   - In `.../reporting-read/iam.tf`, grant `s3:GetObject` on that bucket's `firms/*/generations/exr_*/render_grant.json` and
     nothing wider. Copy the exact key shape the other roots grant; read theirs.
   - If `report_owner.py` needs the retained report index (`IRPT_REQUESTS_TABLE`) for a prospect render, set it and the read grant
     the same way the performance root does, or file a row stating why the reporting route never serves a prospect.
3. **Package (S2).** In `infra/aws/lambda/ci/lambda-source-map.json`, the `irpt-reporting-read-lambda` entry ONLY: stage
   `_render_identity/grant.py` and `report_owner.py` at the pins and `packaged_as` the performance adapter's entry uses, and add
   them to `files`.
   - If `infra/aws/lambda/investor-reporting/PATH_MANIFEST.json` lists the read function's members, add them there too.
   - Never touch `artifact_s3_key` or `artifact_sha256`, and never run `build-and-upload.sh`.

<criterion id="IB39-1-AC1" cell_refs="IB-pr-304"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r39/p39_render_reach.py" . IB39-1-AC1</invocation><expect>IB39-1-AC1 PASS</expect></criterion>
`IB39-1-AC1` -- the edge admits the reporting series path, and only that path on the route. The three existing patterns are kept.
Base: FAIL.

<criterion id="IB39-1-AC2" cell_refs="IB-pr-304"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r39/p39_render_reach.py" . IB39-1-AC2</invocation><expect>IB39-1-AC2 PASS</expect></criterion>
`IB39-1-AC2` -- the read function is wired:
- the env is set;
- the grant read is scoped;
- the two modules are staged with sound pins;
- the materialized package installs render ports.
Base: FAIL.

<criterion id="IB39-1-AC3" cell_refs="IB-pr-304"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r39/p39_render_reach.py" . IB39-1-AC3</invocation><expect>IB39-1-AC3 PASS</expect></criterion>
`IB39-1-AC3` -- regression. Reporting passes at least 21. `_authz` passes at least 207, and its only failures are the 6 base census
tests (row S15). Base: PASS (a guard).

<expected_criteria>IB39-1-AC1,IB39-1-AC2,IB39-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. In the source map, edit ONLY the `irpt-reporting-read-lambda` entry.
- **AWS:** none. No plan, apply or invoke, and no edge publish.
- **Refusal clause.**
  - A pattern that admits more than the series read on the reporting route is a defect.
  - A grant wider than the render-grant objects is a defect.
  - Any change to a human (non-render) request's path through the edge is a defect: stop and file a row.
  - No client name in any record.

<paths>
infra/aws/lambda-edge/auth-validator-edge/render_auth.mjs
infra/aws/terraform/investor-reporting/reporting-read/lambda.tf
infra/aws/terraform/investor-reporting/reporting-read/iam.tf
infra/aws/terraform/investor-reporting/reporting-read/remote_state.tf
infra/aws/terraform/investor-reporting/reporting-read/locals.tf
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~107/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda-edge/`, `infra/aws/terraform/investor-reporting/`,
`infra/aws/lambda/investor-reporting/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 31 (round 39, workstream ~P), cell `IB-pr-304`.
<owned_cells>IB-pr-304</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB39-1-AC1, IB39-1-AC2, IB39-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~107/IRPT_BCKEND.TO-IB-pr-304.render-reach-reporting-route.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB39-1-AC1,IB39-1-AC2,IB39-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the edge pattern, and any route-claim change;
- the env source;
- the IAM statement;
- the staged pins;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the auth-validator-edge render branch (a Lambda@Edge function) and the reporting-read function's environment, role policy and package manifest; 0 served bytes move in the cell. The edge publish and the read function's apply ride P-2's window under its never-widen half.
comp-iam: RUN -- reporting-read gains s3:GetObject on the evidence bucket's render-grant objects only; text only.
comp-routes: RUN -- the edge's render-token admission gains the reporting SERIES path only (not manifest, not summary); human requests unchanged.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: the edge's render branch is not a cache behavior change; no CloudFront distribution config is edited.
comp-adversary: RUN -- IB39-1-AC1 base FAIL (no pattern admits the series path; the three existing patterns parsed), IB39-1-AC2 base FAIL (no IRPT_EVIDENCE_BUCKET), IB39-1-AC3 base PASS (reporting 21, _authz 207 with the 6 base census failures), dry-run at the base 2026-10-03 ~06:1xZ.
lane: the <paths> block IS the grant.
</preflight>
