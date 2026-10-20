# TO IRPT_ANLREQ.TO-AR-y-470.commentary-pdf-route-binds-by-logical-id-and-signs-the-pdfs-own-sha -- FIX AND PROVE OFFLINE: the status route that opens a request's commentary PDF compares the PDF's own sha256 with the commentary DRAFT's sha256 and so can never match; bind by the logical id and sign the PDF's own sha; no release, no deploy

<to_id>IRPT_ANLREQ.TO-AR-y-470.commentary-pdf-route-binds-by-logical-id-and-signs-the-pdfs-own-sha</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~344</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ129</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-470` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 and FWD-9 (the reports open from the ticket) | **depends_on:** run 7c receipt (`org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e7c/A_E2E7C.txt`, stop at R, row IRPT_ANLREQ-D2-S233), CTO msg 11508

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~344`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-344` (branch `wk-IRPT_ANLREQ-344`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~344 <0.9.0_WK_IRPT_ANLREQ~344@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W344-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first), with `to_id` exactly the order's id, a `controls.mutant` that FIRES and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "AR470-y-AC1,AR470-y-AC2,AR470-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID.

### THE CELL (`AR-y-470`, inlined)

*The measured defect (run 7c, CTO msg 11508).* `GET analysis/requests/{REQ}/commentary-pdf` (route `analysis-request-commentary-pdf`, `infra/aws/lambda/investor-reporting/ops/entry.py:246`) answered the closed code `INVALID_INPUT` after the IAM grant cleared; the `irpt-status` log reads `RequestReadRefused` `COMMENTARY_PDF_BINDING`. The packager retains the commentary PDF under the logical id `<request_id>-commentary-<DRAFT sha256>` in the Opal report family (`infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py`, `live_retained_package` near lines 285-286); the retained artifact's own `sha256` is the PDF bytes'. `ops/owned_report.py` method `commentary_pdf` (near lines 335-379) takes `sha` from the acceptance record's `commentary_ref` (the DRAFT's sha256), derives the logical id from it, reads the retained artifact through `self.requests.artifacts.head(...)` and refuses `COMMENTARY_PDF_BINDING` when `retained.get("sha256") != sha` (near line 369-371). The two shas are different by construction, so the route can never answer a link.

*The change (CTO ruling: fix the route, not the packager).* In `ops/owned_report.py` `commentary_pdf` only: keep the binding by LOGICAL ID (it already ties the PDF to that draft sha: the id is derived from the draft sha and the owner, and the repository's own owner, tenant and retention checks apply), and replace the comparison `retained.get("sha256") != sha` by: `retained["family"]` equals `COMMENTARY_FAMILY`, `retained["byte_length"]` is an int greater than 0, and `retained["sha256"]` is a 64-hex string; then sign with `retained["sha256"]` (not the draft's) and return that sha in the answer's `sha256` member. Keep the first check on `commentary_ref["sha256"]` being 64-hex (it derives the logical id). No other method, route, error text or file changes; `pdf` (the Overview report's route, `analysis-request-pdf`) is NOT changed by this cell.

*Read, then prove.* (1) Read `owned_report.py` `commentary_pdf` and `pdf`, `opal_packager.py` `live_retained_package`, and the existing tests of these routes (find them under `infra/aws/lambda/investor-reporting/ops/tests/` and `reports/tests/`; say which exercise `commentary_pdf` and with what shas). (2) Make the change. (3) New test file `infra/aws/lambda/investor-reporting/ops/tests/test_commentary_pdf_binding.py` (offline, no network, built on the fixtures the existing tests use): (a) a request whose `commentary_ref.sha256` is a real draft sha D and whose retained artifact has a DIFFERENT sha P (the production shape) answers a signed link whose signer was called with sha P; (b) the same test MUST FAIL on the code as it stands at the cut commit (prove it: run it against `git show <cut>:infra/aws/lambda/investor-reporting/ops/owned_report.py` in a scratch copy and record the failure line in your deliverable `MUTANT_REPORT.txt`); (c) a retained artifact of the wrong family, a zero length, a non-64-hex sha, and a missing storage key each still refuse (four cases, each by its own existing error name); (d) a request with no `commentary_ref` still answers `COMMENTARY_PDF_NOT_RETAINED`. Commit the route edit and the test as ONE commit (message citing AR-y-470), then your deliverables and instance.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~344/`: `check_commentary_binding.py` (stdlib only, ruff clean, offline) reads `owned_report.py` by AST and prints `COMMENTARY-BINDING-OK family=yes length=yes sha_hex=yes signs_own_sha=yes draft_sha_compare_gone=yes` when `commentary_pdf` has the new checks, signs `retained["sha256"]` and no longer compares it with the draft sha, else `COMMENTARY-BINDING-BAD <why>` (rc 1); `--selftest` mutates the source text in memory (the old comparison put back; the sign call given the draft sha) and prints `CONTROL-FIRES` only when BOTH read BAD. Criterion AC1 is the new test file run with pytest.

---

## ACCEPTANCE

<criterion id="AR470-y-AC1" cell_refs="AR-y-470"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ops/tests/test_commentary_pdf_binding.py -q --color=no -p no:cacheprovider 2>&1 | tail -1</invocation><expect>^[0-9]+ passed</expect></criterion>
<criterion id="AR470-y-AC2" cell_refs="AR-y-470"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~344/check_commentary_binding.py</invocation><expect>^COMMENTARY-BINDING-OK family=yes length=yes sha_hex=yes signs_own_sha=yes draft_sha_compare_gone=yes$</expect></criterion>
<criterion id="AR470-y-AC3" cell_refs="AR-y-470"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~344/check_commentary_binding.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~344/IRPT_ANLREQ.TO-AR-y-470.commentary-pdf-route-binds-by-logical-id-and-signs-the-pdfs-own-sha.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-470.commentary-pdf-route-binds-by-logical-id-and-signs-the-pdfs-own-sha`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR470-y-AC1,AR470-y-AC2,AR470-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-470</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/ops/owned_report.py
infra/aws/lambda/investor-reporting/ops/tests/test_commentary_pdf_binding.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~344/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-470.commentary-pdf-route-binds-by-logical-id-and-signs-the-pdfs-own-sha.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one route method edited, one new test file, and checks in the worker deliverables; nothing is released, deployed or run against AWS; the irpt-status release that ships it is a later order under a signed pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the CTO ruling (msg 11508), run 7c's receipt and the route source against this cell; the lens: a binding check removed that was the only tie of the PDF to the request (the logical-id derivation and the repository's owner and tenant checks must remain), a signer called with the draft sha, a test that passes on today's code (the mutant report must show it fails), the Overview report's own route changed, a PDF of another request or family accepted, an error text changed. NOT seen (blind): the live artifact index item for run 7c's request (its rows were deleted); denominator: three criteria.
</preflight>
