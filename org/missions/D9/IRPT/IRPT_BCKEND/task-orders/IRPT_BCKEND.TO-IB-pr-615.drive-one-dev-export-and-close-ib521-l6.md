# TO IRPT_BCKEND.TO-IB-pr-615 -- DRIVE ONE export through the function `irpt-export-render` by ONE direct invoke with synthetic claims (role admin, firm 49financial), read the new export's status and the pre-existing receipt, so the issuer closes L6 of ledger irpt-export-receipt-repin-20261013 (IB-pr-521); CTO ruling (B), msg 9743 (AMENDMENT 2: no user row)

<to_id>IRPT_BCKEND.TO-IB-pr-615</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~PM</workstream>

**AMENDMENT 2 (issuer, 2026-10-16 ~18:2xZ), after your two STOPs (msg 9726: the helper at HEAD moved; msg 9740: the staff-only user classifies UNKNOWN on every IR route, `_scope/resolve.py:284-296`, which I re-read) and the CTO's ruling (B), msg 9743: "ONE direct invoke of irpt-export-render with synthetic claims (role admin, firm 49financial). No user row, no email, on an account a staff export may target. Read the new export's status as readable and the pre-existing receipt as still reading, then close L6 and the ledger the same session. The receipt says the authorizer was not exercised; it was unchanged by this release. A widened test user (A) is refused."** What changed: the transient user, the helper and XA-20261016T160537Z-f98b are OUT of this order (nothing is minted, no users table is touched); the reads go through direct invokes of the function with claims. Check `r246` is amended to match; no criterion id, cell or path changes.

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `IB-pr-615` (decomposition section 241) | **outcome_ref:** FWD-21 | **Ledger:** `irpt-export-receipt-repin-20261013` (your entry, L1 to L5 closed, L6 OPEN; the issuer closes L6 and the ledger on your record)

---

## WORKER FACE

**Cell `IB-pr-615` (inlined).** IB-pr-521 moved `irpt-export-render` to the signed built digest `5/9LZBbTEWOfrnNZufc6Mqz5pbDxTxYAxpWcZVURGs4=` (ExportReceipt.schema.json v1.1 to v1.2, so the export status read stops refusing its own receipts). Its last leg, L6, is the read of a NEW export; nobody has exported since (the function has 0 invocations since the apply). This order makes that read on demand by invoking the FUNCTION directly. The release changed the function, not the authorizer, so L6 proves the function; the authorizer is not exercised and the record says so. **Paths you post are `file:///` absolute URIs or markdown links, with the repo-relative form for another box (CLAUDE.md rule 33).** No account id, name, value, token or credential goes in any record: counts and statuses only.

**Do, in this order. A STOP is reported to the issuer at once and writes nothing further.**

1. **Gates, read only.** (a) Ledger `irpt-export-receipt-repin-20261013` reads OPEN with L1 to L5 closed and L6 OPEN; no other ledger or marker names `irpt-export-render`. (b) `irpt-export-render` CodeSha256 equals `5/9LZBbTEWOfrnNZufc6Mqz5pbDxTxYAxpWcZVURGs4=`. (c) Read the function's handler and `infra/aws/lambda/investor-reporting/_scope/resolve.py` whole before building any event: the event the function reads is the one the API authorizer produces (the injected headers/claims `X-User-Role`, `X-User-Type`, the verified firm, and so on); build yours from the SOURCE, not from memory.
2. **Build the synthetic event.** Claims: role `admin`, firm `49financial` (this resolves FIRM_OPERATIONS, resolve.py:286). No advisor id, no Opal principal, no email address, no client user type. **No email or notification is requested** (record `emails_sent` 0). The account the export targets is one a staff export may target under that scope (choose through the function's own contract; counts only in the record, never an id). Nothing is written to the users table, Cognito or any IAM object.
3. **The pre-existing receipt, read FIRST.** Invoke the function's export-status read (the `GET /api/scoped/investor-reporting/export/{exportId}` shape) for ONE receipt that existed before the apply (stored before 2026-10-14T00:00Z; take one, not a listing): it must return a status, not a refusal. Record `old_receipt_readable` and its status word. (Read invokes are counted as `status_reads`; they write nothing.)
4. **ONE new export.** Invoke the function ONCE with the export-creation shape (`POST /api/scoped/investor-reporting/export`) and the claims above. If it errors, report the response class and STOP (no retry without the issuer). Then read its status with the status-read invoke until it reads a terminal state or 10 minutes pass. Record `new_export_status` and `new_export_readable` true only if the status read returns a status and not a refusal.
5. **Do NOT close the ledger or L6** (the issuer does, on the record). **Write the record** `deliverables/0.7.0_AE_CloudOps~IB2/IB246-1_export_drive_record.json`:
`{"gates":{"ledger_open_l6_only":true,"function_code_sha256":"5/9LZBbTEWOfrnNZufc6Mqz5pbDxTxYAxpWcZVURGs4=","cto_ruling_msg":9743},"claims":{"role":"admin","firm":"49financial","user_row_minted":false,"authorizer_exercised":false},"old_receipt":{"readable":true,"status":"<word>"},"new_export":{"creating_invokes":1,"http_class":"2xx","status":"<word>","readable":true,"emails_sent":0},"counters":{"creating_invokes":1,"status_reads":<n>,"users_minted":0,"users_removed":0,"lambda_code_changes":0,"iam_changes":0,"schedule_changes":0,"files_deleted":0,"markers_closed":0}}`. No account id, name, value, token or credential in the record.
6. **Run the three criteria below from the repository root**, record each output and exit code verbatim in `IB246-1_criteria_output.txt`, write the proof instance named under proof_of_spec, validate it with `python .tools/proof-of-spec-check.py <instance>`, commit with explicit paths. Report once, under 150 words; report each STOP at once.

**Criteria (run each under `timeout 120` from the repository root):**

<criterion id="IB246-1-AC1" cell_refs="IB-pr-615"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r246/p246_cells.py" . IB246-1-AC1</invocation><expect>IB246-1-AC1 PASS</expect></criterion>
<criterion id="IB246-1-AC2" cell_refs="IB-pr-615"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r246/p246_cells.py" . IB246-1-AC2</invocation><expect>IB246-1-AC2 PASS</expect></criterion>
<criterion id="IB246-1-AC3" cell_refs="IB-pr-615"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r246/p246_cells.py" . IB246-1-AC3</invocation><expect>IB246-1-AC3 PASS</expect></criterion>

<expected_criteria>IB246-1-AC1, IB246-1-AC2, IB246-1-AC3</expected_criteria>

What the checks grade: AC1 the gates (ledger L6 only open, the function at the signed digest, the CTO ruling cited); AC2 the claims (role admin, firm 49financial, no user row minted, the authorizer stated NOT exercised); AC3 the old receipt readable, ONE creating invoke with a readable status and no email, the counters. Do not edit the checks.

## BOUNDS

- **Grant:** `lambda:InvokeFunction` on `irpt-export-render` ONLY: exactly ONE creating invoke and read-only status invokes; reads of the function configuration, its source and the ledger; your record folder. **NO user row, Cognito or IAM write; NO production client export; NO email or notification; NO second creating invoke; NO change to any function, role, schedule, layer or environment; NO deletion; no ledger closed; no widened test user (the CTO refused (A)).**
- **Refusal clause:** STOP and report on any of: a function digest that differs; an export that would email anyone; a refused status read of the old receipt (that is a finding about IB-pr-521, report it whole); an event the function rejects for a missing claim you cannot read from its source.
- **Row ids** `IRPT_BCKEND-D2-IB2-S<k>` or the next free `D2-S<k>`. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-615.drive-one-dev-export-and-close-ib521-l6.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 241 (round 5, workstream ~PM), cell `IB-pr-615`.
<owned_cells>IB-pr-615</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB246-1-AC1, IB246-1-AC2, IB246-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-615.drive-one-dev-export-and-close-ib521-l6.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- ONE export-creating direct invoke of `irpt-export-render` with synthetic claims (admin, firm 49financial) plus read-only status invokes; the function writes its own export artifact under its own path; no user row, no IAM, no email; the authorizer is not exercised (unchanged by IB-pr-521).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is changed; the invoke runs on the operator's existing lambda:InvokeFunction.
comp-routes: DECLARED-NOT-APPLICABLE -- the portal route is not called; the function is invoked directly.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p246_cells.py IB246-1 amended to the claims shape: dry-run at base on dell2 2026-10-16 ~18:3xZ AC1 to AC3 FAIL (no record); positive control (control246.py): three positives PASS and each negative (a wrong digest, the ledger not at L6 only, a ruling not cited, a non-admin role, a firm other than 49financial, a user row minted, the authorizer claimed exercised, an old receipt refused, two creating invokes, a non-2xx, an unreadable export, an email, no status read, a code or IAM or schedule change, a deletion, a user minted or removed, a ledger closed) fails its own arm. NOT measured by me: the function's event contract beyond resolve.py lines 284-296, the old receipt's status word, whether a creating invoke needs a field I did not read.
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2` (dell2). Class SERVED.
</preflight>
