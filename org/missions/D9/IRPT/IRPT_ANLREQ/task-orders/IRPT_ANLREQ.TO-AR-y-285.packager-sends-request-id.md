# TO IRPT_ANLREQ.TO-AR-y-285.packager-sends-request-id -- PACKAGER: the PACKAGE body carries the request id (and revision) the packager already holds

<to_id>IRPT_ANLREQ.TO-AR-y-285</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~109</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-285` (`decompositions/IRPT_ANLREQ_DECOMP_R23D_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~109`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-109` (branch `wk-IRPT_ANLREQ-109`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~109 <0.9.0_WK_IRPT_ANLREQ~109@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W109-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-285`, inlined) -- THE PACKAGER HALF OF THE J2 CLOSE. Code and tests only; nothing is released.

***The J2 close (PRD v0.5 FWD-1, the CTO's ruling (A) msg 7204):** `svc-irpt-packager` records the REQUEST ID on the partner-firm filer's ticket once, so the ticket links to its request. What the reads found (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~92/r23/J2_REQUEST_ID.json`, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~101/r23/SUBMIT_ANALYSIS_REQUEST.json` row `IRPT_ANLREQ-D2-W101-S1`): the packager's PACKAGE body is `{report_ref, pdf_ref, original_ref, commentary_ref, firm}` where `report_ref` is the report's `report_id` (`infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py` :208-209, :168); it carries NO request id, although `handle_commentary_ready` HAS it (`request_id` from the `commentary_ready` message, :146); the ticket service's PACKAGE (`infra/aws/lambda/ticket_center/lambda_function.py` `package_ticket` ~:1468-1504) writes `package.report_ref` (an opaque string) and never the top-level `report_ref` that the drafter and the REPORT route use (`report_ref.request_id`). **THE INTERFACE (fixed here so the two cells build in parallel):** the PACKAGE body gains ONE optional member `request_id` (a string; the shape the investor-reporting request ids have: read it in `infra/aws/lambda/investor-reporting/ycharts/research/../ycharts/generate/submission.py` and `acceptance.py`, and use the SAME pattern, never a looser one); when present and valid the ticket service writes the top-level `report_ref = {request_id, revision, recorded_by, recorded_at}` ONCE (`revision` taken from the optional body member `request_revision`, an integer, default 0), conditional on `attribute_not_exists(report_ref)`; a second write with the same request id is idempotent (the PACKAGE route already answers `already_attached` for the same pointers: keep that), a DIFFERENT request id for a ticket that already holds one is refused 409 `REPORT_REF_ALREADY_RECORDED_OTHER`; absent `request_id` means today's behaviour exactly; the member is bound to the ticket's requester firm and to `PACKAGE_ALLOWED_FIRMS` exactly as PACKAGE already is; only the named package principal can send it (the route already enforces that). A change to what the packager may write is an AUTHORIZATION change: state it in one paragraph for the never-widen pair.*

1. **Read first:** `infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py` (`handle_commentary_ready` :144-197, `_attach` :200-212, the live `attach` :320-332, `IDENTITY_POINTERS`, the 409 `conflict` reading), its tests (find them: `Grep` in `infra/aws/lambda/investor-reporting/ycharts/research/tests/` and `infra/aws/lambda/investor-reporting/ycharts/generate/tests/` for `opal_packager`), and where the module is packaged (`infra/aws/lambda/ci/lambda-source-map.json` entries that list it; `resident_installed.py` :341 and :424-433 wire it in the resident). Record `read` {`payload_today` (file:line), `request_id_available_at` (file:line), `revision_available_at`, `tests_found`, `packaged_in`}.
2. **The change.** `_attach` (and the callers that build the payload) add `request_id` (the message's request id) and `request_revision` (`record['identity']['revision']`, an integer) to the PACKAGE payload, as the interface says. The idempotence stays: a 409 `PACKAGE_ALREADY_ATTACHED` is still read by the four IDENTITY pointers only (do NOT add the request id to `IDENTITY_POINTERS`: a retry after a partial first attempt must stay `already_attached`); a 409 `REPORT_REF_ALREADY_RECORDED_OTHER` is refused as `PackagerRefused("ATTACH_CONFLICT:REPORT_REF_ALREADY_RECORDED_OTHER")`. Keep every other behaviour. If the module is packaged in more than one place (the resident, a Lambda) say which and how many members change; do NOT edit the map or the recipe.
3. **Tests, before and after (new file beside the existing packager tests, at least 6 tests):** (a) the payload carries `request_id` equal to the message's and `request_revision` equal to the record's revision; (b) the payload's other five members are byte-equal to today's; (c) a 409 already-attached with the same four pointers still returns `already_attached` even when the stored package lacks a request id; (d) a 409 `REPORT_REF_ALREADY_RECORDED_OTHER` raises the named refusal; (e) a malformed request id in the message is still refused by the existing closed-message check before any call; (f) the existing packager tests pass with NO existing assertion edited unless it pinned the exact five-member payload (list each such edit: the payload is now seven members). `before_arm`: (a) FAILS at HEAD. All pass; the folders' counts; the known baseline of `ycharts/generate/tests` (4 custody failures) stated.
4. **Write `r26/PACKAGER_REQUEST_ID.json`:** `read`, `built`, `tests`, `before_arm`, `release_needs` (members changed per package, any queue or env), `claim`, `not_read`.
5. **In your report:** the payload before and after, where the module is packaged, the counts.

### ACCEPTANCE

<criterion id="AR285-y-AC1" cell_refs="AR-y-285"><invocation>python C:/dev/wk-irpt-anlreq-109/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y285-pkg-sender --root C:/dev/wk-irpt-anlreq-109</invocation><expect>Y285-PKG-SENDER-OK</expect></criterion>
`AR285-y-AC1`: the record shows the payload before and after (seven members), where the module is packaged, and a new test file with at least 6 passing tests whose case (a) fails at HEAD, with the existing packager tests edited only where they pinned the five-member payload.

<criterion id="AR285-y-AC2J" cell_refs="AR-y-285" judgment="true"/>
`AR285-y-AC2J` (judgment, graded at L9, never by you): the request id and revision are sent as the interface says, the already-attached idempotence still reads the four pointers only, a conflicting request id is a named refusal, no map or recipe was edited, and nothing was released.

<expected_criteria>AR285-y-AC1 AR285-y-AC2J</expected_criteria>

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-13 ~21:5xZ, after the first report of `AR-y-284`'s worker; two defects of the issuer's order text, the worker was right).** (1) The criterion's expected token is `Y285-PKG-SENDER-OK` (the checker prints its whole check name; the order text said `Y285-PKG-OK`). (2) The record folder is `r23/` (the checker reads `deliverables/0.9.0_WK_IRPT_ANLREQ~<n>/r23/PACKAGER_REQUEST_ID.json`), not `r26/`. A record already written to both folders is fine. Gate limb that graded this amendment: none stated (the issuer amends its own order's text).

**AMENDMENT 2 (issuer `2.0.0_SA_COO~Y2`, 2026-10-13 ~22:0xZ, after the worker's BLOCKING row `IRPT_ANLREQ-D2-W109-S1`; the stop was right).** Two existing tests outside the first grant pin the five-member PACKAGE payload: `ycharts/research/tests/test_opal_packager.py` (:155) and `ycharts/research/tests/test_packager_own_store.py` (:70). `<paths>` now names both. Edit ONLY the assertion or fixture that pins the five-member payload to the seven-member payload (the two new members are `request_id` and `request_revision`); keep every other assertion and word; list each edit in the record (`test_edits`: file, test name, before text, after text). Then commit, re-run the trunk checker (it prints `Y285-PKG-SENDER-OK`) and the proof-of-spec check, and report once. Do not flip `<status>`. Row `W109-S2` (released before `AR-y-284`, every attach gets a 400) is the issuer's: the release orders the ticket service leg first. Gate limb that graded this amendment: none stated (the issuer amends its own pending order's grant).

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~109/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_packager_request_id.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_packager.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_packager_own_store.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23D_Y.md</decomp_doc>
<owned_cells>AR-y-285</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~109/IRPT_ANLREQ.TO-AR-y-285.packager-sends-request-id.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-285`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR285-y-AC1,AR285-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test edits in a worktree; nothing is released, deployed or called; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading `AR-y-280`'s row W101-S1 and the ruling (A) against the cell; the lens: a request id written by a principal other than the packager, a second write that overwrites the first, a looser id pattern than the receiver's, an authorization change nobody stated. The order requires the new tests to FAIL at HEAD, each refusal pinned, and the change stated. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on `AR-y-280`'s BLOCKING row `W101-S1` and `AR-y-271`'s option ii (the J2 close), workstream `Y` round 26. The grant names every file the cell writes. Base: `AR285-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

<!-- ISSUER NOTE 2026-10-13 (2.0.0_SA_COO~Y2): status flipped to complete after the drain. Trunk checker y285-pkg-sender prints Y285-PKG-SENDER-OK (13 new tests, research folder 319), proof VALID. The packager must be released AFTER the ticket service leg of AR-y-284 (row W109-S2). AR285-y-AC2J is the CVO to grade. -->
