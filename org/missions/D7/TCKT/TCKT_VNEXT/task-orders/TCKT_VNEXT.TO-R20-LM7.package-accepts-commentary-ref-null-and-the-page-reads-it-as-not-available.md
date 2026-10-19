# TO TCKT_VNEXT.TO-R20-LM7 -- BUILD the package route's null pdf_ref and commentary_ref pair and the ticket page's "Commentary not available" (IRPT_ANLREQ v0.24 FWD-1; source and tests only)

<to_id>TCKT_VNEXT.TO-R20-LM7</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~53</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>PKGNULL</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply: a Lambda source path; the worker deploys, applies and invokes NOTHING)
**Decomp cell:** `R20-lm-7` (`decompositions/TCKT_VNEXT_DECOMP_R20.md`, AMENDMENT 4) | **outcome_ref:** the CTO's ruling msg 11065 (IRPT_ANLREQ v0.24 FWD-1 ACCEPT) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~53`.
- **Worktree:** `C:/dev/wk-tckt-vnext-53` (branch `wk-TCKT_VNEXT-53`), provisioned by the issuer, with the portal repository at `C:/dev/wk-tckt-vnext-53/portal` (its own repository, `node_modules` linked). Work and commit only there. The workspace part commits with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~53 <0.9.0_WK_TCKT_VNEXT~53@opal.agent>" -F <msgfile> -- <paths>`; the portal part commits INSIDE `C:/dev/wk-tckt-vnext-53/portal` with `git -C C:/dev/wk-tckt-vnext-53/portal commit` on its own branch (author the same serial line), never on `DEV` or `PROD`, never pushed.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `TCKT_VNEXT-D2-W53-S<k>` (take the next free `<k>`). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`. No live call of any kind: no AWS, no network, no mail, no deploy, no apply, no Terraform (`tests/conftest.py` refuses a real call). **Run no Python test file by path: pytest only, with `-p no:cacheprovider`. Run portal tests with `bun test <file>` from the portal worktree only.** Scratch outside the product tree.

### WHY

IRPT_ANLREQ v0.24 FWD-1 ACCEPT (signed): "a commentary failure never withholds the other three". The ticket service refuses a package whose `commentary_ref` is null, so a commentary failure withholds the other three. The CTO ruled (msgs 11065 and 11078): the package route accepts `pdf_ref` and `commentary_ref` null (`pdf_ref` is the commentary PDF), both keys present, TOGETHER only, each null skipping its I7 check, as `original_ref` already skips its string test (I5'); the replace path through `prior_attached_at` is unchanged so the packager can later post all four; and the ticket page shows a null `commentary_ref` as "Commentary not available", never as an error, while the other three still open. `~Y2` cuts the packager half; both ship in one release (not your concern).

### THE CELL (`R20-lm-7`, inlined) -- BUILD ONLY. Nothing is deployed, applied or invoked.

**Part A. The Lambda** (`infra/aws/lambda/ticket_center/lambda_function.py`, function `package_ticket`, about lines 1796 to 1830; read it first; also the constants `PACKAGE_REF_FIELDS`, `PACKAGE_I7_FIELDS` at about :158-:161):
1. In the loop over `PACKAGE_REF_FIELDS + ("firm",)` that tests each value as a non-empty string of at most `PACKAGE_REF_MAX_CHARS`, `original_ref` already has `if k == "original_ref" and k in body and v is None: continue`. Give `pdf_ref` and `commentary_ref` a null rule: each may be null when its key is PRESENT in the body, and they are null TOGETHER or set together. One null beside one set is 400, and that refusal's error text names BOTH `pdf_ref` and `commentary_ref`. A MISSING key stays 400 with an error naming that key (also when its partner is null); an empty or whitespace string, a non-string non-null value and a string over the limit stay 400 naming the member. `report_ref` and `firm` stay required non-null strings.
2. In the following loop over `PACKAGE_I7_FIELDS` (`pdf_ref`, `commentary_ref`), skip the canonical-JSON test for a member that is None (only reachable when both are None); a non-null member is tested exactly as today (canonical JSON of exactly `artifact_id`, `sha256`, `version_id`).
3. The stored package keeps `pdf_ref: None` and `commentary_ref: None` as it keeps `original_ref: None`. Nothing else changes: not `_ident`, not the 409 codes, not `prior_attached_at` (the replace path), not `_package_state` (a null pair reads PARTIAL there, which is true), no other route, no `MATRIX`.
4. NO existing test arm changes. `test_package_still_requires_report_pdf_commentary` in `infra/aws/lambda/ticket_center/tests/test_package_i5p_i7.py` sends each of `report_ref`, `pdf_ref`, `commentary_ref` null ALONE and expects 400 naming that member: under the pair rule a lone null is still 400 and the error names both members, so it still passes. Change no existing assertion; if any existing test in `infra/aws/lambda/ticket_center/tests/` fails because of your change, STOP and file a BLOCKING row naming it.
5. The issuer has written the Lambda check `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_CHECKS/test_r20_package_commentary_null.py` (five tests; at the base four FAIL and one PASSES, the control). Do not edit it. You do not need to add a second Lambda test file.

**Part B. The portal** (the repository at `C:/dev/wk-tckt-vnext-53/portal`, a branch cut from `origin/DEV` @`4f9f2f633dc0`):
6. `src/api/endpoints/tickets.ts`, interface `TicketPackage` (about line 128 to 137): `pdf_ref: string | null` and `commentary_ref: string | null`, each with a one-line comment (v0.24 FWD-1: both null together when the commentary failed). Keep the existing `pdf_ref` I7 comment.
7. `src/pages/TicketCenter/AnalysisRequestParts.tsx` (also fix any type error the `pdf_ref` change raises INSIDE this file only; the reader gate `packageFileHasReader` already tests `typeof ticket.package.pdf_ref === 'string'`), the report package block (the `PACKAGE_FILES.map` near line 630; the sentence constants are near line 503): add `export const NO_COMMENTARY_SENTENCE = 'Commentary not available'`. For the row whose `f.kind === 'commentary'` when `pkg.commentary_ref === null`, render `<span data-slot="no-commentary">{NO_COMMENTARY_SENTENCE}</span>` and NOTHING else in that `<dd>`: no `Open` button (even when `pkg.pdf_ref` is a string and `packageFileHasReader('commentary', ...)` would be true), no "(no reader yet)", no `role="alert"`, no error. Every other row, and the commentary row for a string `commentary_ref`, render exactly as today. `describePackageRef` already returns `''` for null; do not rely on that for this row.
8. New test file `src/pages/TicketCenter/__tests__/package-commentary-null.test.tsx` (copy the render style of `package-r2.test.tsx` in the same folder). One named test per case: `renders Commentary not available for a null commentary_ref`; `shows no Open control and no alert for it`; `shows the sentence and no Open control when both pdf_ref and commentary_ref are null`; `still shows the sentence and no Open control when commentary_ref is null and pdf_ref is a string (defence: the server never sends it)`; `the other three rows still render their files and their Open controls`; `a string commentary_ref renders as before (control)`; `a null original_ref still reads the custody sentence (control)`.
9. Do not edit any other existing portal file or test. If an existing portal test fails because of the type change, fix nothing outside the paths: STOP and file a BLOCKING row.
10. Write a short `R20_LM7_RECORD.json` under `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~53/`: the lines you changed in each repository, the test counts (the Lambda check, the whole `infra/aws/lambda/ticket_center/tests/` folder once, the new portal file, `bun test src/pages/TicketCenter` once), the portal commit hash, `not_read`.

### ACCEPTANCE

<criterion id="R20LM7-AC1" cell_refs="R20-lm-7"><invocation>python -m pytest C:/dev/wk-tckt-vnext-53/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_CHECKS/test_r20_package_commentary_null.py -q -p no:cacheprovider --color=no</invocation><expect>^5 passed</expect></criterion>
`R20LM7-AC1`: the issuer's Lambda check passes, all five tests, run from `C:/dev/wk-tckt-vnext-53` as the working directory. Also run the whole `infra/aws/lambda/ticket_center/tests/` folder once and record the counts (a drain check; the issuer re-runs it).

<criterion id="R20LM7-AC2" cell_refs="R20-lm-7"><invocation>python C:/dev/wk-tckt-vnext-53/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_CHECKS/r20_portal_test.py --portal C:/dev/wk-tckt-vnext-53/portal --file src/pages/TicketCenter/__tests__/package-commentary-null.test.tsx --min 7</invocation><expect>^R20-PORTALTEST-OK</expect></criterion>
`R20LM7-AC2`: the new portal test file passes, its seven named tests, none failing. Also run `bun test src/pages/TicketCenter` once in the portal worktree and record the counts (a drain check).

<criterion id="R20LM7-AC3J" cell_refs="R20-lm-7" judgment="true"/>
`R20LM7-AC3J` (judgment, graded at L9, never by you): a package with a null commentary reaches the ticket and the page reads it as "Commentary not available", not as an error, while the other three still open; nothing else in `package_ticket` or the package block changed.

<expected_criteria>R20LM7-AC1 R20LM7-AC2 R20LM7-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~53/` and this order's file (status flip only). The portal paths are inside the portal repository of your worktree.
- READ only: everything else, including `infra/aws/terraform/` and the issuer's check file. Touch ONLY `package_ticket` (and the constants it reads, unchanged) in the Lambda, and only the package block in the page.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
portal/src/api/endpoints/tickets.ts
portal/src/pages/TicketCenter/AnalysisRequestParts.tsx
portal/src/pages/TicketCenter/__tests__/package-commentary-null.test.tsx
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R20.md</decomp_doc>
<owned_cells>R20-lm-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~53/TCKT_VNEXT.TO-R20-LM7.package-accepts-commentary-ref-null-and-the-page-reads-it-as-not-available.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R20-LM7`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R20LM7-AC1,R20LM7-AC2,R20LM7-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- source and tests only, nothing deployed or scheduled; the release is a later CloudOps act with `~Y2`'s packager half. comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, route or environment change; the package route's principal and firm bound are unchanged. comp-adversary: DECLARED-NOT-APPLICABLE -- a source-and-tests build with no deploy; the lens held instead by the checks: a null admitted with the key MISSING (the check holds it 400), a lone null of the pair admitted (held 400 naming both), a non-canonical string admitted (held 400), `report_ref` loosened (held 400), the replace path changed (held by the check's replace test), a null reading as an error or an Open control on the page (held by the portal tests). BLIND to: the packager's own posting, and the PROD bundle the page ships in.
</preflight>
