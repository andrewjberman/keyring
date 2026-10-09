# TO IRPT_ANLREQ.TO-AR-v21 -- the ticket opens the Branded PDF; the package route admits I5' and reads I7

<to_id>IRPT_ANLREQ.TO-AR-v21</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~21</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>TICKET</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the ticket service's package route ships in a later `opal-ticket-api` release; the
portal half is a product file on the CTO review route) | **Decomp cell:** `AR-v-21` (`decompositions/IRPT_ANLREQ_DECOMP_R2.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~21`.
- **Workspace worktree:** `C:/tmp/anlreq-v21` (branch `wk-irpt_anlreq-v21`, cut from the issuance commit). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~21 <0.9.0_WK_IRPT_ANLREQ~21@opal.agent>" -F <msgfile> -- <paths>`.
- **Portal worktree:** `C:/tmp/anlreq-v21-portal` (branch `wk-irpt_anlreq-v21`, from portal `origin/DEV`). Commit there with
  `git -c user.name=0.9.0_WK_IRPT_ANLREQ~21 -c user.email=0.9.0_WK_IRPT_ANLREQ~21@opal.agent commit -F <msgfile>`. If `node_modules` is
  absent, run `bun install --frozen-lockfile` there first.
- Write every message file with the Write tool. Run ticket_center tests with invalid AWS keys
  (`AWS_ACCESS_KEY_ID=x AWS_SECRET_ACCESS_KEY=y`): some older tests otherwise make live reads.

### THE CELL

The packager sends the ticket service I5: `POST /api/scoped/tickets/{ticket_id}/package` with
`{report_ref, pdf_ref, original_ref, commentary_ref, firm}`. Round 2 changes it in two ways:
- **I7.** `pdf_ref` and `commentary_ref` each travel as the canonical JSON of `{"artifact_id", "sha256", "version_id"}`: sorted keys, no
  spaces (`json.dumps(ref, sort_keys=True, separators=(",", ":"))`), at most 512 characters.
- **I5'.** For a custody-lane request `original_ref` is `null`. The other three refs stay required.

**Part A -- the ticket service** (workspace worktree). In `infra/aws/lambda/ticket_center/lambda_function.py`, `package_ticket` (:1373) and its
constants (:127-129):
1. `original_ref` may be JSON `null`. When present it is validated as today: a non-empty string of at most `PACKAGE_REF_MAX_CHARS`. A
   missing key is still refused. `report_ref`, `pdf_ref`, `commentary_ref` and `firm` stay required, exactly as today.
2. `pdf_ref` and `commentary_ref` must parse as JSON objects with EXACTLY the three keys `artifact_id`, `sha256`, `version_id`, each a
   non-empty string. The input string must EQUAL the canonical re-serialisation, so key order and spacing are part of the contract. Anything
   else is a 400 that names the field.
3. Store the package as given; the stored strings equal the strings sent. `report_ref` stays an opaque string.
4. New test file `infra/aws/lambda/ticket_center/tests/test_package_i5p_i7.py` with EXACTLY these names:
   - `test_package_admits_null_original_ref`
   - `test_package_still_requires_report_pdf_commentary` (each of the three null or missing is refused)
   - `test_package_admits_i7_canonical_refs`
   - `test_package_refuses_non_canonical_i7_ref` (a space, or unsorted keys)
   - `test_package_refuses_i7_ref_with_extra_or_missing_field`

   Use this ONE sample for both refs. It is the same sample the producer and packager cells test against:
   `{"artifact_id":"irpt-anlreq-x10-v1/49financial/req-0001/commentary","sha256":"9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08","version_id":"v1"}`
5. The existing package tests (`tests/test_package_route.py`, and `tests/test_package_principal.py` if it builds a package body) send
   plain-string refs. Update only their
   `pdf_ref` and `commentary_ref` fixtures to the sample, and say so. The whole `tests` directory stays green.

**Part B -- the portal** (portal worktree):
1. **PDF reader.** `src/pages/TicketCenter/AnalysisRequestParts.tsx` already calls `ir.getAnalysisRequestPdf(requestId, firm)`
   (`PackageReaders`, ~:217), but the real client has no such method, so the button never shows. In `src/api/endpoints/investor-reporting.ts`:
   - add `analysis-request-pdf` to the operation union (~:173) and to `IR_ROUTE_TABLE` (:209), as
     `GET ${IR_ROUTE_BASE}/analysis/requests/{requestId}/pdf`, the same shape as `analysis-request-read` (:218). The server route exists:
     `infra/aws/lambda/investor-reporting/ops/entry.py:222` (irpt-status), returning `{"download_route": {"url", "expires_at"}, "sha256", ...}`;
   - add `getAnalysisRequestPdf(requestId, selectedTenant?)` beside `getOwnedAnalysisRequest`, built the same way, returning
     `{ signedUrl: download_route.url }`. The URL is never stored or logged.
2. **I5'.** When `original_ref` is `null`, the Original file row reads exactly: `No original file: this report was built from custody data.`
3. **I7.** A `pdf_ref` or `commentary_ref` that parses as I7 is shown by its `artifact_id` with the first 12 characters of its `sha256`. A ref
   that does not parse is shown as plain text. Never build a URL or a link from any ref.
4. Commentary and Original file have NO server reader (row `IRPT_ANLREQ-D2-S6`). Keep them labelled `(no reader yet)`. Do not invent a
   route.
5. Widen the portal type `TicketPackage` (`src/api/endpoints/tickets.ts:71-74`) so `original_ref` may be `null`. Use the existing panel classes and add no colours.
6. New test file `src/pages/TicketCenter/__tests__/package-r2.test.tsx` with EXACTLY these names:
   - `the real client opens the branded PDF through analysis-request-pdf` (drive the REAL client with a stubbed transport; assert the path
     and that the signed URL reaches `openUrl`)
   - `shows the custody sentence when original_ref is null`
   - `shows an I7 ref by its artifact id`
   - `shows an unparseable ref as text and never links it`

   `package-open.test.tsx`, `commentary-package.test.tsx`, `analysis-request.test.tsx`, `analysis-form-i1.test.tsx` and
   `src/pages/InvestorReporting/__tests__/fe-s-1/adapter.test.ts` must still pass. If an assertion there encoded the old route count,
   update only that count, and say so.

### ACCEPTANCE

<criterion id="AR21-v-AC1" cell_refs="AR-v-21"><invocation>python C:/tmp/anlreq-v21/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~V2/AR_V_CHECKS/ar_v_checks.py v21-package</invocation><expect>V21-PACKAGE-OK</expect></criterion>
`AR21-v-AC1`: run from `C:/tmp/anlreq-v21`; the five named Part A tests exist and pass.

<criterion id="AR21-v-AC2" cell_refs="AR-v-21"><invocation>python C:/tmp/anlreq-v21/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~V2/AR_V_CHECKS/ar_v_checks.py v21-page --portal C:/tmp/anlreq-v21-portal</invocation><expect>V21-PAGE-OK</expect></criterion>
`AR21-v-AC2`: the four named Part B tests exist and pass.

<criterion id="AR21-v-AC3" cell_refs="AR-v-21"><invocation>python C:/tmp/anlreq-v21/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~V2/AR_V_CHECKS/ar_v_checks.py portal-tsc --portal C:/tmp/anlreq-v21-portal</invocation><expect>PORTAL-TSC-OK</expect></criterion>
`AR21-v-AC3`: the portal typechecks.

<expected_criteria>AR21-v-AC1 AR21-v-AC2 AR21-v-AC3</expected_criteria>

The issuer runs `ar_v_checks.py regress` (the whole ticket_center suite) at the drain.

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus your deliverables folder
  `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~21/` and this order's file (status flip only).
- READ only: `infra/aws/lambda/investor-reporting/**` (the server routes) and everything else in the portal.
- LOCAL: never push, never deploy, never call a live API. Dev servers run on port 5174 only. No non-ASCII.
- If the server's PDF response shape differs from the one above, keep the client to what the server returns, file a row, and keep working.

**AMENDMENT 1 (issuer, 2026-10-09 ~07:3xZ; DECOMP_R2 AMENDMENT 1 @77d85c7fd7, `~Y2` msg 2802).** The typed sample in Part A item 4 is
replaced by the ONE I7 sample for every lane: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/I7_SAMPLE.json` (@beb1d1466d,
in the issuance base). `test_package_i5p_i7.py` reads that file at test time, round-trips its `sample` against its `canonical` both ways,
and uses `canonical` for `pdf_ref` and `commentary_ref`, including in the updated package-route fixtures. The portal tests may carry the same
canonical string as a literal. Delivered to the running worker the same tick. Gate limb: none graded this modification.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_package_i5p_i7.py
infra/aws/lambda/ticket_center/tests/test_package_route.py
infra/aws/lambda/ticket_center/tests/test_package_principal.py
portal/src/api/endpoints/investor-reporting.ts
portal/src/pages/TicketCenter/AnalysisRequestParts.tsx
portal/src/api/endpoints/tickets.ts
portal/src/pages/TicketCenter/__tests__/package-r2.test.tsx
portal/src/pages/TicketCenter/__tests__/package-open.test.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-1/adapter.test.ts
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R2.md</decomp_doc> (round 2, workstream ~V2 TICKET), cell `AR-v-21`.
<owned_cells>AR-v-21</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR21-v-AC1 AR21-v-AC2 AR21-v-AC3. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~21/IRPT_ANLREQ.TO-AR-v21.package-pdf-reader-i5p-i7.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AR21-v-AC1 AR21-v-AC2 AR21-v-AC3` before the flip.
</proof_of_spec>

**REPORT (once):** each check line verbatim; the workspace and portal commits; every existing assertion you updated; any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE (no IAM; the ticket route's principals are unchanged). comp-adversary: RUN -- 4 sources read (DECOMP_R2 I5'/I7 rows; lambda_function.py :127-129 and :1373-1425; portal AnalysisRequestParts.tsx :215-300 at origin/DEV; ops/entry.py :218-233). Traps: a non-canonical ref admitted (fixed by the equality rule), null admitted on a required ref (fixed by the second test), a guessed reader for commentary/original (barred; row D2-S6).
lane: ticket_center is this seat's surface (AR-v-12); the portal half is a product file on the CTO review route.
</preflight>

Source: `~Y2` msg 2782; IRPT_ANLREQ_DECOMP_R2.md @cff0872f0f, cell AR-v-21, interfaces I5' and I7; CTO round-1 analysis (msg 2770) rulings 2-4.
The I7 sample is ~T2's rule (TO-AR-t-21, three non-empty string fields, canonical JSON at most 512) with one concrete value.

# pipeline-override: round 2's issuance is split by workstream (DECOMP_R2: "Each lane issues ONLY its cells below, into its own <workstream> scope"); this is ~V2's issuance of its one cell.

fanout: 1 of 1 chains (~V2 TICKET), cap 8.
