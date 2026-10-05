# TO IRPT_BCKEND.TO-IB-pr-321 -- two refusals stop answering UNEXPECTED: BucketUnmapped is FIRM_BINDING; MaintainedSourceRefused splits into subclasses that declare their code (S260, S175; CTO batch 253)

<to_id>IRPT_BCKEND.TO-IB-pr-321</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~124</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>52</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO RULINGS batch 253 @35e313ec06 (msg 105129), on rows S260 and S175
(and S180, which is probably S260's 500) | **Decomp cell:** `IB-pr-321` (decomposition section 46) | **outcome_ref:** FWD-8 |
**depends_on:** IB-pr-320 (merged @f9e1c4ab96; same `_authz` write surface). The risk is WORLD because the cell edits code under
infra/; it deploys nothing, and every served release is the issuer's.

---

## WORKER FACE

**What is wrong.** `reason_for` in `infra/aws/lambda/investor-reporting/_authz/errors.py` (`:116-143`) reads a declared
`public_reason_code` attribute first (`:124`), then maps by exact class name. Two refusals have neither, so they answer
`UNEXPECTED`, which the R11 status contract reserves for faults:
- `BucketUnmapped` (`IR/_authz/loaders.py:43`, a `ValueError`);
- `MaintainedSourceRefused` (`IR/_scope/maintained_sources.py:28`, a `PermissionError`). It is raised at about 50 sites.

`IR` = `infra/aws/lambda/investor-reporting`. Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-124`; run everything
from its root.

**The ruling (batch 253), which you implement and do not reinterpret:**
1. `BucketUnmapped` declares `public_reason_code = "FIRM_BINDING"` as a class attribute.
2. `MaintainedSourceRefused` stays as the base class, so every existing `except MaintainedSourceRefused` keeps working. Add three
   subclasses in `maintained_sources.py`, each declaring its code as a class attribute:
   - `MaintainedSourceUnauthorized` -> `NOT_AUTHORIZED`: an owner, identity, viewer or entitlement mismatch (for example `:62` "user
     does not match active owner", `:78` "advisor binding differs", `:671` "not permitted for this firm or principal");
   - `MaintainedSourceUnready` -> `NOT_READY`: a required SERVER source absent, malformed or changed (for example `:43`, `:55`,
     `:74`, `:87`, `:90`, `:93`, the registry/reader/descriptor/binding "unavailable" lines, and the "changed during preparation"
     lines);
   - `MaintainedSourceInvalidInput` -> `INVALID_INPUT`: a refusal of the CALLER's own input (for example "custody browser input
     required", "comparison key unknown or ambiguous"). Classify `:150` and every similar "required" site from its call site:
     INVALID_INPUT if it refuses caller input, NOT_AUTHORIZED if it is an owner check.
3. Replace EVERY `raise MaintainedSourceRefused(...)` with the right subclass. Never branch on message text. If a site fits none of
   the three classes, raise the base class there, leave it as is, and file a row naming the line. The checker then counts it as
   bare, and the issuer rules it.
4. **The census:** write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~124/S175_RAISE_SITE_CENSUS.json` with:
   - `sites`: one `{line, subclass, public_reason_code, message}` per raise of a refusal subclass in `maintained_sources.py`;
   - `unexpected_before` and `unexpected_after`: how many of the file's refusal raise sites `reason_for` answered UNEXPECTED before
     and after (expect all before, 0 after);
   - `s180_read`: whether S180's selection-create path raises `BucketUnmapped`, read from the code. Do not assume it.
5. **Tests:** `IR/_authz/tests/test_reason_codes_S260_S175.py`, at least 4 tests:
   - `reason_for(BucketUnmapped(...))` is `FIRM_BINDING` (name S260);
   - one subclass instance of each class maps to its code (NOT_AUTHORIZED, NOT_READY, INVALID_INPUT; name S175);
   - every subclass is still caught by `except MaintainedSourceRefused` and by `except PermissionError`.

<criterion id="IB52-1-AC1" cell_refs="IB-pr-321"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r52/p52_reason_codes.py" . IB52-1-AC1</invocation><expect>IB52-1-AC1 PASS</expect></criterion>
`IB52-1-AC1` -- the new tests pass (at least 4, naming S260, S175, FIRM_BINDING, NOT_READY, NOT_AUTHORIZED), and the `_authz` and
`_scope` suites pass with 0 failed. Base: FAIL.

<criterion id="IB52-1-AC2" cell_refs="IB-pr-321"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r52/p52_reason_codes.py" . IB52-1-AC2</invocation><expect>IB52-1-AC2 PASS</expect></criterion>
`IB52-1-AC2` -- no bare `raise MaintainedSourceRefused(` remains, and the census lists every refusal-subclass raise site with its
code, plus the UNEXPECTED counts before and after. Base: FAIL.

<criterion id="IB52-1-AC3" cell_refs="IB-pr-321"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r52/p52_reason_codes.py" . IB52-1-AC3</invocation><expect>IB52-1-AC3 PASS</expect></criterion>
`IB52-1-AC3` -- a GUARD: your commits touch only the grant, and nothing under infra/aws/terraform/. Base: PASS.

<expected_criteria>IB52-1-AC1,IB52-1-AC2,IB52-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none. No deploy, no `lambda-source-map.json` edit, no terraform.
- **Refusal clause.** A new reason code, a change to `PUBLIC_REASONS`, or branching on message text is out of scope: file a row.

<paths>
infra/aws/lambda/investor-reporting/_authz/
infra/aws/lambda/investor-reporting/_scope/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~124/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-321.s260-s175-reason-codes.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 46 (round 52, workstream ~P), cell `IB-pr-321`.
<owned_cells>IB-pr-321</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB52-1-AC1, IB52-1-AC2, IB52-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~124/IRPT_BCKEND.TO-IB-pr-321.s260-s175-reason-codes.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB52-1-AC1,IB52-1-AC2,IB52-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, the census counts (sites per code,
UNEXPECTED before/after), the S180 read, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the authz error mapping and the maintained-sources refusals; 0 served bytes move in the cell. The served releases (authz consumers, irpt-ycharts-generate) are the issuer's, under never-widen halves.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes; only the public_reason_code a refusal answers.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB52-1-AC1 base FAIL (no test file), IB52-1-AC2 base FAIL (bare raises at 43, 55, 62, ...), IB52-1-AC3 base PASS (guard), dry-run at base 033795b666 2026-10-05 ~05:0xZ.
lane: the <paths> block IS the grant.
</preflight>
