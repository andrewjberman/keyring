# TO IRPT_ANLREQ.TO-AR-y-306.ordinary-viewer-authorizer -- BUILD the upload door's ordinary-viewer authorizer (a partner-firm advisor may upload for its own firm only), fail closed, tests on fakes

<to_id>IRPT_ANLREQ.TO-AR-y-306</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~121</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>36</round>
<workstream>ZA</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-306` (`decompositions/IRPT_ANLREQ_DECOMP_R36A_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~120`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-120` (branch `wk-IRPT_ANLREQ-120`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~120 <0.9.0_WK_IRPT_ANLREQ~120@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W120-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no `aws` call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-306`, inlined) -- BUILD ONLY. Nothing is released, applied, deployed or called live.

*The finding (row `IRPT_ANLREQ-D2-S93`, BLOCKING; the release-28 sitting, `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r28/SITTING_RESULT.txt`): the upload door refuses every non-Opal viewer with NOT_AUTHORIZED before it reads the file, because `infra/aws/lambda/investor-reporting/reports/generate_installed.py :336` composes `ports["ordinary_authorizer"]` as None (fail-closed by design, pinned by `reports/tests/test_generate_installed.py :201` `test_without_the_ordinary_authorizer_a_partner_upload_is_refused_and_nothing_is_written`). FWD-1 (PRD v0.5) needs a partner-firm advisor to upload its holdings file, so the producer must be built. **THE CTO'S RULING (msgs 7502 and 7505, verbatim in substance):** the producer admits a non-Opal viewer ONLY when ALL of: (1) the firm comes from the VERIFIED token context (the edge-verified headers), never from the request body; (2) that firm equals the request's firm (the selected tenant, the data firm); (3) the viewer's `allowedFirmIds` (the users PROFILE row, read as `InteractiveAccess._allowed_firm_ids` reads it, an explicit list, never `ALL`) contains that firm; (4) the viewer has an ACTIVE users row (the exact string `active`) and a PARTNER row for that firm. Everything else is refused NOT_AUTHORIZED before the file is read, as today. It is the same rule as the approved locked-firm portal route (open call 7773). Tests the CTO named: the 49F advisor admitted; another firm's advisor refused; an inactive user refused; a missing firm claim refused; an Opal viewer unchanged. It ships under a never-widen pair, so the record must state, in one paragraph, WHO GAINS UPLOAD.*

1. **Read first (all of it, with the line numbers you cite):** `infra/aws/lambda/investor-reporting/_scope/interactive_access.py` (the whole file: `InteractiveAccess.current()`, `authorize_current()`, the `ordinary_authorizer` contract `callable(principal, retained_owner) is True`, `_allowed_firm_ids`), `infra/aws/lambda/investor-reporting/reports/generate_installed.py` (:170-215 where the ports compose the access, :320-345 the `ports` dict with `ordinary_authorizer` None, :380-420 where a callable is wrapped as `ordinary(request, p, o)`), `infra/aws/lambda/investor-reporting/reports/tests/test_generate_installed.py` (:70-90, :170-215, the tests that pin the absence), `prospect.py` `resolve_prospect_owner` and `resolve.py` `trusted_only` (find them with `Grep` under `infra/aws/lambda/investor-reporting`; they build the viewer's `principal_class`, `firm_id`, `advisor_id` from the verified headers), the existing canonical profile read (`CanonicalProfileReaders.get_user`: email -> projected `opal-users-v2` PROFILE row, row `IB-pr-354`) and any existing reader of the partner rows (`opal-partner-<firm>` tables, key `email`; find who reads them and with what), and the Lambda's role: `infra/aws/terraform/investor-reporting/ycharts/iam.tf` and `generate.tf` (reading only; which DynamoDB tables and actions the `irpt-ycharts-generate` role holds today). Print what the viewer's `principal` and `owner` dicts look like for an ordinary (non-Opal) caller, with the code line that builds each member.
2. **Build the producer** in a NEW module `infra/aws/lambda/investor-reporting/_scope/ordinary_viewer.py`: a factory taking INJECTED readers (a profile reader and a partner-row reader; never a new AWS client created inside the module) and returning a callable `(request, principal, owner) -> bool` in the shape `generate_installed.py` wraps (read how, :395-415). It returns True ONLY when every one of the four conditions of the ruling holds; ANY exception, any missing field, any reader returning None, `ALL`, an empty `allowedFirmIds`, a status other than the exact string `active`, a principal class that is the Opal one (that path is already authorised elsewhere and must be UNCHANGED), or a firm mismatch between the token context, the principal, the owner and the data firm returns False. The module writes nothing and has no write method (a spy test proves it). The firm is taken from the principal/owner built from the verified headers; a firm in a request BODY or QUERY is never consulted by the module.
3. **Wire it** in `infra/aws/lambda/investor-reporting/reports/generate_installed.py` ONLY where the ports are composed from readers the Lambda already holds: replace the None at :336 with the producer built over the existing profile reader and the partner-row reader. If the Lambda's role cannot read the partner-row table today (an IAM and Terraform change would be needed), DO NOT widen anything: keep the wiring fail-closed (the partner reader returns None on a refusal, so the authorizer returns False), say so in the record's `iam_needs` with the exact policy lines, and leave the IAM change for the issuer's release pair. Keep every other line of `generate_installed.py`; `test_without_the_ordinary_authorizer_a_partner_upload_is_refused_and_nothing_is_written` must still pass UNEDITED (it tests the absent-producer path).
4. **Tests** (new file `infra/aws/lambda/investor-reporting/_scope/tests/test_ordinary_viewer.py`, at least 14, on fakes, no AWS): the 49F advisor with an active row, `allowedFirmIds` containing 49financial and a partner row is ADMITTED for 49financial; the same advisor for another firm is refused; another firm's advisor (cottonwood) for 49financial is refused; an inactive user (`status` `disabled`, `inactive`, `ACTIVE`, empty, absent) refused each; a missing firm claim refused; a firm only in the request body refused; `allowedFirmIds` absent, empty, `ALL`, a string not containing the firm: refused each; a missing partner row refused; a reader that raises refused; a profile row whose email is not the subject's refused; an Opal viewer (OPAL_GLOBAL) unchanged (the access object still authorises it; the producer is not consulted); no write method is called (spy); an end-to-end through `InteractiveAccess.authorize_current` for the admitted and a refused case. `before_arm`: run the new tests against a copy of HEAD without the module and record that they FAIL. Existing folders: `infra/aws/lambda/investor-reporting/reports/tests/test_generate_installed.py` and `infra/aws/lambda/investor-reporting/_scope/tests` pass with NO existing assertion edited (list any edit and why; the CTO expects none).
5. **Write `r36/ORDINARY_AUTHORIZER.json`:** `read` (file:line for every claim above), `rule` (the four conditions and the code line that tests each), `principal_shape` (what an ordinary caller's principal and owner carry and where), `wiring` (the lines changed in generate_installed.py), `iam_needs` (what the role holds today for the two tables, the exact policy lines; what a release needs if it lacks the partner read), `tests` (counts, the file, the folders run with their counts), `before_arm`, `authorization_change` (ONE paragraph: WHO GAINS UPLOAD, for which firm, on what conditions, and what stays refused), `release_needs` (which package carries the new module: map entry and member name; N writers), `claim`, `not_read` (the live Lambda configuration, the live users and partner rows, the edge).
6. **In your report:** the rule in four lines, the principal shape, whether the Lambda role can read the partner table today, the counts, the authorization change paragraph.

### ACCEPTANCE

<criterion id="AR306-y-AC1" cell_refs="AR-y-306"><invocation>python C:/dev/wk-irpt-anlreq-120/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y306-ordinary --root C:/dev/wk-irpt-anlreq-120</invocation><expect>Y306-ORDINARY-OK</expect></criterion>
`AR306-y-AC1`: the record states the four-condition rule with the code line that tests each, the principal shape, the wiring, what the Lambda role holds for the two tables, a new test file with at least 14 passing tests whose admitted case fails at HEAD, the existing generate_installed tests passing unedited, and the one-paragraph authorization change.

<criterion id="AR306-y-AC2J" cell_refs="AR-y-306" judgment="true"/>
`AR306-y-AC2J` (judgment, graded at L9, never by you): the producer admits only on all four conditions, takes the firm from the verified headers and never from a body or query, fails closed on every exception and every missing or malformed field, leaves the Opal path unchanged, writes nothing, is wired only over readers the Lambda already holds, and states honestly who gains upload.

<expected_criteria>AR306-y-AC1 AR306-y-AC2J</expected_criteria>

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-14 ~04:4xZ, after the first worker's BLOCKING rows `IRPT_ANLREQ-D2-W120-S1` and `-S2`; the stop was right).** (S1) The order said `test_without_the_ordinary_authorizer_a_partner_upload_is_refused_and_nothing_is_written` and its neighbours must pass UNEDITED. That was wrong: the wiring replaces the None they pin, so `reports/tests/test_generate_installed.py :83` (`absent_producers == {"ordinary_authorizer"}`) and `:212` (`factory.ordinary_authorizer is gi._ordinary_viewer_not_composed`) are red by design. The file is now in `<paths>`: edit ONLY those two pins to the new composed state (the `:83` set no longer contains `ordinary_authorizer` when the readers are composed; `:212` asserts the producer is composed and that, with a reader that returns nothing, the upload is still refused and nothing is written); keep the intent and every other assertion; list each edit with before and after text in the record (`test_edits`). The fail-closed absent-producer behaviour must stay TESTED: add a case that builds the access with `ordinary_authorizer` None and shows the refusal. (S2) The producer also serves the owned-input analysis route (`prospect_submission.py :55-56`); the CTO is asked to rule. Do not split anything until the issuer says; state the effect in `authorization_change`. (S3) The `_scope/tests` failure in `test_resolve.py` is pre-existing (your HEAD control): name it as the baseline in the record. `<issued_to>` is now `0.9.0_WK_IRPT_ANLREQ~121`: you CONTINUE in the same worktree `C:/dev/wk-irpt-anlreq-120` (branch `wk-IRPT_ANLREQ-120`), commit as `~121`, file rows `IRPT_ANLREQ-D2-W121-S<k>`, and write your record to `deliverables/0.9.0_WK_IRPT_ANLREQ~121/r36/ORDINARY_AUTHORIZER.json` (the check reads it first). Gate limb that graded this amendment: none stated (the issuer amends its own pending order's grant and assignee).

**AMENDMENT 2 (issuer `2.0.0_SA_COO~Y2`, 2026-10-14 ~04:5xZ, the CTO's ruling on row `W120-S2`, msg 7529: ACCEPTED, one authorizer serves the upload door AND the owned-input analysis route, no split, three conditions).** (1) The analysis route admits only an input the viewer OWNS: add tests through `ycharts/generate/prospect_submission.py` (or the narrowest honest seam; say which) that another advisor's input in the SAME firm is refused, and an input of ANOTHER firm is refused, and the owner's own input is admitted (read how `authorize_current` compares the retained owner's `principal_id` and `firm_id`, `_scope/interactive_access.py :101-121`, and where the analysis route calls it, `prospect_submission.py :55-56`). (3) An Opal viewer's behaviour is UNCHANGED on BOTH routes, with a test for each. (2) is the pair's: in `authorization_change` name the roles (FIRM_ADVISOR, FIRM_OPERATIONS), the firms the Lambda's role can reach, both routes, and the exact conditions, so the issuer can write "who gains upload and owned-input analysis". Gate limb that graded this amendment: none stated (the issuer amends its own pending order's tests under the CTO's ruling).

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~120/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/_scope/ordinary_viewer.py
infra/aws/lambda/investor-reporting/_scope/tests/test_ordinary_viewer.py
infra/aws/lambda/investor-reporting/reports/generate_installed.py
infra/aws/lambda/investor-reporting/reports/tests/test_generate_installed.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R36A_Y.md</decomp_doc>
<owned_cells>AR-y-306</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~120/IRPT_ANLREQ.TO-AR-y-306.ordinary-viewer-authorizer.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-306`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR306-y-AC1,AR306-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a new module and its test file and one wiring edit in generate_installed.py under the investor-reporting source tree; no live call; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the sitting result (door refusals NOT_AUTHORIZED) and the pinned fail-closed test against the cell; the lens: an authorizer that trusts a firm from the request body, one that fails open on a reader error, one that changes the Opal path. The order requires the refusal cases named, a spy that proves nothing is written, and the Opal viewer unchanged. NOT seen: the live users and partner rows (0 read), the live Lambda role beyond the Terraform source, the edge's header verification at runtime. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on row `D2-S93` (BLOCKING) and the CTO's rulings (msgs 7502, 7505) as workstream `ZA` round 36. A never-widen pair follows the cell. Base: `AR306-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
