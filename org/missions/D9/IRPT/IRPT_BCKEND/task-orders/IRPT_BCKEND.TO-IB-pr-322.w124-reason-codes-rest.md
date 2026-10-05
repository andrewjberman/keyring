# TO IRPT_BCKEND.TO-IB-pr-322 -- the rest of the refusal codes: 25 bare raises in two more _scope files, and a malformed firm artifact answers NOT_READY (rows W124-S1, W124-S2; CTO batch 253's class rule)

<to_id>IRPT_BCKEND.TO-IB-pr-322</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~125</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>53</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** the issuer's ruling on rows W124-S1 and W124-S2, under 1.0.0_SA_CTO RULINGS
batch 253 @35e313ec06 (refusals classed by kind: owner or identity mismatch is NOT_AUTHORIZED; a required server source absent or
malformed is NOT_READY; a refusal of caller input is INVALID_INPUT; no branching on message text) | **Decomp cell:** `IB-pr-322`
(decomposition section 47) | **outcome_ref:** FWD-8 | **depends_on:** IB-pr-321 (merged @0fff3d8363). The risk is WORLD because the
cell edits code under infra/; it deploys nothing.

---

## WORKER FACE

`IR` = `infra/aws/lambda/investor-reporting`. Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-125`; run everything
from its root. IB-pr-321 already added three subclasses of `MaintainedSourceRefused` in `IR/_scope/maintained_sources.py` (`:36-50`):
- `MaintainedSourceUnauthorized` (NOT_AUTHORIZED);
- `MaintainedSourceUnready` (NOT_READY);
- `MaintainedSourceInvalidInput` (INVALID_INPUT).

Its census `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~124/S175_RAISE_SITE_CENSUS.json` shows how 46 sites
were classed. Use the same reading.

1. **W124-S1.** `IR/_scope/canonical_profile_reads.py` (14 sites) and `IR/_scope/retained_input_authorizer.py` (11 sites) still
   `raise MaintainedSourceRefused(...)` bare, so they answer UNEXPECTED. Replace every one with the right subclass, imported from
   `maintained_sources`, by the class rule above. A site that fits none stays bare and gets a row naming the line.
2. **W124-S2.** `IR/_authz/loaders.py` `opaque_firm_for` (`:209-211`) raises `BucketUnmapped` (FIRM_BINDING) when the firm's
   directory artifact declares no `firm_id_opaque`. That is a malformed SERVER artifact, which is NOT_READY by the class rule.
   - Add a `ValueError` subclass in `loaders.py`, for example `FirmArtifactIncomplete`, declaring `public_reason_code = "NOT_READY"`.
   - Raise it there instead.
   - `BucketUnmapped` keeps FIRM_BINDING for the unmapped-firm raise (`:57`).
   - Grep for every `except BucketUnmapped` caller of `opaque_firm_for`. If any caller relies on catching that case, catch both
     there, and say so in your report.
3. **The census:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~125/W124_RAISE_SITE_CENSUS.json`, with
   `sites`, one `{file, line, subclass, public_reason_code, message}` per subclass raise in the two files. Add
   `unexpected_before` and `unexpected_after` counts.
4. **Tests:** `IR/_authz/tests/test_reason_codes_W124.py`, at least 3 tests:
   - one site from each of the two files maps to its declared code (name `W124-S1`);
   - `opaque_firm_for` on a directory with no `firm_id_opaque` raises the new exception, and `reason_for` answers `NOT_READY`
     (name `W124-S2`);
   - `BucketUnmapped` still answers `FIRM_BINDING`.

<criterion id="IB53-1-AC1" cell_refs="IB-pr-322"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r53/p53_reason_codes_rest.py" . IB53-1-AC1</invocation><expect>IB53-1-AC1 PASS</expect></criterion>
`IB53-1-AC1` -- the new tests pass (at least 3, naming W124-S1, W124-S2, NOT_READY), and the `_authz` and `_scope` suites pass with 0
failed. Base: FAIL.

<criterion id="IB53-1-AC2" cell_refs="IB-pr-322"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r53/p53_reason_codes_rest.py" . IB53-1-AC2</invocation><expect>IB53-1-AC2 PASS</expect></criterion>
`IB53-1-AC2` -- no bare raise remains in the two files, the census lists every subclass raise there, and `opaque_firm_for` no longer
raises `BucketUnmapped`. Base: FAIL.

<criterion id="IB53-1-AC3" cell_refs="IB-pr-322"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r53/p53_reason_codes_rest.py" . IB53-1-AC3</invocation><expect>IB53-1-AC3 PASS</expect></criterion>
`IB53-1-AC3` -- a GUARD: your commits touch only the grant, and nothing under infra/aws/terraform/. Base: PASS.

<expected_criteria>IB53-1-AC1,IB53-1-AC2,IB53-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none. No deploy, no `lambda-source-map.json` edit, no terraform.
- **Refusal clause.** A new reason code, a `PUBLIC_REASONS` change, or branching on message text is out of scope: file a row.

<paths>
infra/aws/lambda/investor-reporting/_authz/
infra/aws/lambda/investor-reporting/_scope/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~125/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-322.w124-reason-codes-rest.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 47 (round 53, workstream ~P), cell `IB-pr-322`.
<owned_cells>IB-pr-322</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB53-1-AC1, IB53-1-AC2, IB53-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~125/IRPT_BCKEND.TO-IB-pr-322.w124-reason-codes-rest.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB53-1-AC1,IB53-1-AC2,IB53-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, the census counts per code, the
`except BucketUnmapped` callers you found, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- refusal codes in two _scope modules and the opaque-firm read; 0 served bytes move in the cell. Released in the same issuer release round as IB-pr-320 and IB-pr-321.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes; only the public_reason_code a refusal answers.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB53-1-AC1 base FAIL (no test file), IB53-1-AC2 base FAIL (bare raises at canonical_profile_reads.py:37, ...), IB53-1-AC3 base PASS (guard), dry-run at base 80e1455217 2026-10-05 ~06:0xZ.
lane: the <paths> block IS the grant.
</preflight>
