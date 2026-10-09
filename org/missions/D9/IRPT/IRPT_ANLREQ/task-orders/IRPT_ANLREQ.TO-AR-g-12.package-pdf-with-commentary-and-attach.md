# TO-AR-g-12 -- on I4: the Opal layout gains a commentary section, renders the branded package PDF, and the packager makes the I5 call (FWD-1 hops 7 and 8)

<to_id>IRPT_ANLREQ.TO-AR-g-12.package-pdf-with-commentary-and-attach</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~62</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (the Opal engine and brand) | **Decomp cell:** `AR-g-12`
(`decompositions/IRPT_ANLREQ_DECOMP_R1.md`, AMENDMENT 1 row I4s) | **outcome_ref:** FWD-1, FWD-3 | **depends_on:** none to build.
Built entirely against injected ports; the live ports name what they wait on.

---

## WORKER FACE

### Read first

`org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md`:
- the "Interfaces" table, rows I2, I4 and I5;
- AMENDMENT 1, row I4s (where the commentary lives).

Your cell is the CONSUMER of I4 and the CALLER of I5.

### THE CELL

When the commentary is drafted, a closed message arrives:

    queue_message("commentary_ready", {"tenant": t, "request_id": r})

From that message, the backend must produce the branded package PDF, with the commentary in it, and attach the package to the ticket.

There is ONE renderer: the Opal engine's own HTML layout (PRD section 4 item 1). There is no second render stack.

All code is under `infra/aws/lambda/investor-reporting/ycharts/research/`.

1. **The commentary section.** `layout_overview.py` `build(run_doc, kept_by_name, map_doc, brand, computed=None, ..., pricing=True)` (:1069)
   returns HTML. Pages are grouped from `map_doc["elements"]` by `el["page"]` (:1089-1100).
   - Add ONE optional keyword, `commentary=None`. When it is given (a dict carrying the DRAFT's text and title), `build` appends ONE more
     `<section class="page">` after the last page, headed "Commentary", in the same brand styling.
   - Escape every commentary string as HTML text. No markup from the commentary is ever rendered.
   - When `commentary` is None, the HTML is byte-identical to today's.
   - `render(html)` (:1127, Node playwright-core) is unchanged.
2. **The package render.** `opal_producer.py` `produce(request_ref, firm, stores)` (:205) builds and stores `overview.pdf`. Its key is
   `_address(..., object="overview.pdf")` (:252), the output of `opal_naming.address`.
   - Add the smallest path that renders the SAME report with `commentary=` set and stores it as `object="package.pdf"`, through the same
     `_address` builder (never a typed key) and the same `stores["artifacts"]` / `stores["objects"]` ports.
   - `overview.pdf` is untouched.
3. **The packager** (new `research/opal_packager.py`). `handle_commentary_ready(body, ports)`:
   - **Admit the message.** Parse `body`, REBUILD it with `queue_message("commentary_ready", {"tenant": t, "request_id": r})`
     (`infra/aws/lambda/investor-reporting/_keys/keys.py:551`; import it the way `generate/resident_worker.py` does), and require byte
     equality. Refuse any other shape or extra field by name.
   - **Read the records** through injected ports (I2):
     - the acceptance record of `(tenant, request_id)`: `generate/acceptance.py:68` `DynamoAcceptance.get`. It carries `ticket_id`
       (written by AR-y-11) and `commentary_ref` (written by AR-t-12, set once, per AMENDMENT 1 I4s);
     - the READY job row (`generate/durable_job.py`, table `irpt-jobs`). Its receipt carries `report_id`.

     If `ticket_id` or `commentary_ref` is absent, refuse by name (`TICKET_ID_ABSENT` / `COMMENTARY_REF_ABSENT`): no render and no call.
   - **Read the commentary bytes** through the repository's service-reader family grant: `reports/repository.py`
     `ArtifactRepository`, family `ANALYSIS_COMMENTARY` (AMENDMENT 1). Use an injected `read_artifact(tenant, ref) -> bytes` port. The
     live port reads through `ArtifactRepository` if it is importable from the resident package; otherwise it raises
     `COMMENTARY_READER_UNWIRED` and you file a row.
   - **Render** the package (step 2), giving `pdf_ref`.
   - **Make the I5 call** through an injected `attach(ticket_id, payload)` port, where payload is
     `{report_ref, pdf_ref, original_ref, commentary_ref, firm}`. These are pointers only (C-PACKAGE), and `firm` is the tenant.
     - `report_ref` = the receipt's `report_id`.
     - `original_ref` = the reference of the uploaded file the request was filed on. Find it on the acceptance record or its composition
       (`composition_ref`). If it is not reachable from the records, file a row and refuse `ORIGINAL_REF_ABSENT`; never invent one.
     - The live `attach` port is `POST /api/scoped/tickets/{ticket_id}/package`
       (`infra/aws/lambda/ticket_center/lambda_function.py:1367`, live), called as the ONE package principal `svc-irpt-packager`
       (2.0.0_SA_COO~V2 msg 2510; firm-bound by its PROFILE `allowedFirmIds` list). Its row and credential are a later pair, so the live
       port raises `PACKAGER_PRINCIPAL_UNSET` until they exist. Do not create, read or name any credential.
   - **Idempotence.** A second `commentary_ready` for the same pair, after a successful attach, must not render or call again. Read
     that from the ticket, or from a fact the records already hold; if neither can tell, file a row and keep the rule in the fake.
4. **Tests** (offline, fakes only; the Node render is faked by monkeypatching `layout_overview.render`):
   - `research/tests/test_layout_commentary.py`:
     - (a) `build(..., commentary=None)` equals today's `build(...)` byte for byte on the fixtures `test_layout_overview.py` uses;
     - (b) with commentary set, the HTML has exactly one more `section class="page"`, headed Commentary;
     - (c) a commentary string carrying `<script>` appears escaped.
   - `research/tests/test_opal_packager.py`:
     - (d) one admitted message: one render to `package.pdf` at the builder address, then exactly one `attach` with the five fields,
       `firm == tenant`;
     - (e) an extra field or a wrong kind is refused with no render and no attach;
     - (f) a missing `ticket_id` or `commentary_ref` is refused by name with no attach;
     - (g) a second message for the same pair makes no second render and no second attach;
     - (h) the live attach port raises `PACKAGER_PRINCIPAL_UNSET`.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR12-g-AC1" cell_refs="AR-g-12"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar1_g2_checks.py g12</invocation><expect>^AR1-G2-G12-OK</expect></criterion>

<criterion id="AR12-g-AC2" cell_refs="AR-g-12"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar1_g2_checks.py regress</invocation><expect>^AR1-G2-REGRESS-OK</expect></criterion>

<expected_criteria>AR12-g-AC1,AR12-g-AC2</expected_criteria>

- **AC1:** both new files together show at least 5 passed and 0 failed. At the base this FAILs, because the files are absent (issuer
  dry run).
- **AC2:** no test file in the generate or research suites is newly red against the base. At the base:
  - generate is red only in `test_custody_retained.py` and `test_custody_entry.py`;
  - research reads 165 passed;
  - the issuer's dry run reads `AR1-G2-REGRESS-OK`.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no upload, no AWS calls, no Node install, no HTTP call; fakes only.
- Every `.py` edit passes `.tools/commit-gate.sh`.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken a check.
- **Rows** are `IRPT_ANLREQ-D2-W62-S<k>`, in `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`.
  - Use the next unused k across the document.
  - If the file is absent, create it in the shape of `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`.
  - Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~62" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~62@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~62 <0.9.0_WK_IRPT_ANLREQ~62@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - Edit byte-preserving, ASCII only. Use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_commentary.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_packager.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~62/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-12.package-pdf-with-commentary-and-attach.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md</decomp_doc> round 1, workstream ~G, cell `AR-g-12`.
<owned_cells>AR-g-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR12-g-AC1, AR12-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~62/IRPT_ANLREQ.TO-AR-g-12.package-pdf-with-commentary-and-attach.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR12-g-AC1,AR12-g-AC2` BEFORE the flip to complete. Shape:
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~223/IRPT_BCKEND.TO-IB-yr-761.install-custody-factory.proof_of_spec.json`.
Commit the code first, then pin each artifact to a commit that contains it.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the commentary section and its escaping;
- the package key's builder call;
- where `ticket_id`, `commentary_ref`, `report_ref` and `original_ref` are read from;
- the idempotence rule;
- each live port and what it raises today;
- the commit hashes and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- the layout gains one optional page (byte-identical when absent, arm a); one new object package.pdf at the builder address beside overview.pdf; one new module. Ships in the resident package by a later release pair; nothing deploys in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is added; the svc-irpt-packager row and credential are AR-v-12's later pair (2.0.0_SA_COO~V2 msg 2510), and the repository read uses the existing service-reader family grant (AMENDMENT 1 I4s).
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; the live POST /tickets/{id}/package exists and stays refusing until package_principal is named.
comp-schedule: DECLARED-NOT-APPLICABLE -- driven by the I4 message.
comp-adversary: RUN -- read the code map (layout_overview.py :103-116, :1069-1100, :1127; opal_producer.py :91, :205-263; acceptance.py :68-112) and ~V2 msg 2510. BLIND to the I4 queue's owner and to the resident's subscription to it: no lane's write surface in the decomposition holds that infrastructure, so the issuer asked 2.0.0_SA_COO~Y2. Traps: commentary markup rendered, a second render stack, a typed key, an invented original_ref, a credential in code, a double attach. Arms (a)-(h) cover each.
lane: workstream ~G scope per the decomposition (ycharts/research/*); the <paths> block IS the grant (worker_grant).
</preflight>

Source: IRPT_ANLREQ decomposition round 1 cell AR-g-12 with AMENDMENT 1 (@8412208d47); 2.0.0_SA_COO~Y2 msgs 2487, 2506; 2.0.0_SA_COO~V2 msg 2510.
