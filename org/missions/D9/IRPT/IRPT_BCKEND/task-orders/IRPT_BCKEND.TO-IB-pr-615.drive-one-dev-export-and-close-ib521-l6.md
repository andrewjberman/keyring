# TO IRPT_BCKEND.TO-IB-pr-615 -- DRIVE ONE DEV export through the real entry point under a transient staff-only user, read the new export's status and the pre-existing receipt, remove the user (read back ABSENT), so the issuer closes L6 of ledger irpt-export-receipt-repin-20261013 (IB-pr-521); CTO ruling (A), msg 9653

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

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling (A), msg 9653 (2026-10-16 16:47Z): "Drive ONE DEV export through the real entry point (the portal's export path under a staff-only transient user, the XA-f98b shape, or the route the page calls), on an account a staff login may export. Read the new export's status as readable, and the pre-existing receipt as still reading. Applier IB2 (rule 34). User minted and removed, read back ABSENT. No client is emailed. Then close L6 and the ledger the same session." | **Decomp cell:** `IB-pr-615` (decomposition section 241) | **outcome_ref:** FWD-21 | **Ledger:** `irpt-export-receipt-repin-20261013` (your entry, L1 to L5 closed, L6 OPEN; the issuer closes L6 and the ledger on your record)

---

## WORKER FACE

**Cell `IB-pr-615` (inlined).** IB-pr-521 moved `irpt-export-render` to the signed built digest `5/9LZBbTEWOfrnNZufc6Mqz5pbDxTxYAxpWcZVURGs4=` (ExportReceipt.schema.json v1.1 to v1.2, so the export status read stops refusing its own receipts). Its last leg, L6, is the read of a NEW export on DEV; nobody has exported since (the function has 0 invocations since the apply). This order makes that read on demand. **Paths you post are `file:///` absolute URIs or markdown links, with the repo-relative form for another box (CLAUDE.md rule 33).** No account id, name, value or credential goes in any record: counts and statuses only.

**Do, in this order. A STOP is reported to the issuer at once and writes nothing further beyond the removal in step 5.**

1. **Gates, read only.** (a) Ledger `irpt-export-receipt-repin-20261013` reads OPEN with L1 to L5 closed and L6 OPEN; no other ledger or marker names `irpt-export-render`. (b) `irpt-export-render` CodeSha256 equals the signed built digest `5/9LZBbTEWOfrnNZufc6Mqz5pbDxTxYAxpWcZVURGs4=`. (c) **The user's authority:** `python .tools/xadj.py show --id XA-20261016T160537Z-f98b` prints `State: RULED` (the laptop CTO's YES for one synthetic staff row in `opal-users-v2`, conditions: staff role only, NO firm entitlement row, the role set printed before removal, removal read back ABSENT). The CTO's msg 9653 names this shape for THIS drive; if the helper or the table refuses, STOP and report what it printed. (d) The helper `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~149/fwd1_driver/fwd1_mint.py` has git blob `f368e9d95c62dc9fce1e6d5e04cd7fe6f79c444a`; a different value is a STOP. Read the helper and its folder `fwd1_driver/` whole before use.
2. **Mint ONE transient staff user** with the helper (it writes one PROFILE row: role user, userType test-filer, firm `opal-capital`, 3-hour TTL, conditional put; the password never leaves memory). Before any export, print and record `U1 users_row role=<role> userType=<userType> firmId=<firmId> entitlement_rows=<count of other rows under that PK, 0 expected> status=<status>`. A count other than 0, or a firmId that is not `opal-capital`, is a STOP: remove the user, report, export nothing.
3. **The pre-existing receipt, read FIRST.** Through the same read path the page uses (the export status route under the transient login, or the producer's own reader), read one receipt that existed before the apply (any stored receipt older than 2026-10-14T00:00Z; read one, not a listing of all): it must read as a status, not a refusal. Record `old_receipt_readable` and its status word.
4. **ONE new export, the real way.** Through the portal's export route as the page calls it (`POST /api/scoped/investor-reporting/export`, then `GET /api/scoped/investor-reporting/export/{exportId}` for its status), on DEV, under the transient login, on an account a staff login may export (choose by the entitlement the staff role holds; read the page's request shape first, do not invent one). **Email delivery off or not requested: no client is emailed; record `emails_sent` 0.** One POST only; if it errors, report the response class and STOP (no retry without the issuer). Poll the status route until it reads a terminal state or 10 minutes pass; record `new_export_status` (the status word) and `new_export_readable` true only if the status route returns a status and not a refusal.
5. **Remove the user and read it back ABSENT** (the helper's removal, then a get-item on the PK that reads no item). Do this even on a STOP in step 3 or 4. Record `user_removed_read_back_absent`.
6. **Do NOT close the ledger or L6** (the issuer does, on the record). **Write the record** `deliverables/0.7.0_AE_CloudOps~IB2/IB246-1_export_drive_record.json`:
`{"gates":{"ledger_open_l6_only":true,"function_code_sha256":"5/9LZBbTEWOfrnNZufc6Mqz5pbDxTxYAxpWcZVURGs4=","xa_f98b_state":"RULED","helper_blob":"f368e9d95c62dc9fce1e6d5e04cd7fe6f79c444a","cto_ruling_msg":9653},"user":{"role":"<role>","userType":"<userType>","firmId":"opal-capital","entitlement_rows":0,"removed_read_back_absent":true,"password_in_memory_only":true},"old_receipt":{"readable":true,"status":"<word>"},"new_export":{"posts":1,"http_class":"2xx","status":"<word>","readable":true,"emails_sent":0},"counters":{"exports_requested":1,"users_minted":1,"users_removed":1,"lambda_code_changes":0,"iam_changes":0,"schedule_changes":0,"files_deleted":0,"markers_closed":0}}`. No account id, name, value, token or credential in the record.
7. **Run the three criteria below from the repository root**, record each output and exit code verbatim in `IB246-1_criteria_output.txt`, write the proof instance named under proof_of_spec, validate it with `python .tools/proof-of-spec-check.py <instance>`, commit with explicit paths. Report once, under 150 words; report each STOP at once.

**Criteria (run each under `timeout 120` from the repository root):**

<criterion id="IB246-1-AC1" cell_refs="IB-pr-615"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r246/p246_cells.py" . IB246-1-AC1</invocation><expect>IB246-1-AC1 PASS</expect></criterion>
<criterion id="IB246-1-AC2" cell_refs="IB-pr-615"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r246/p246_cells.py" . IB246-1-AC2</invocation><expect>IB246-1-AC2 PASS</expect></criterion>
<criterion id="IB246-1-AC3" cell_refs="IB-pr-615"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r246/p246_cells.py" . IB246-1-AC3</invocation><expect>IB246-1-AC3 PASS</expect></criterion>

<expected_criteria>IB246-1-AC1, IB246-1-AC2, IB246-1-AC3</expected_criteria>

What the checks grade: AC1 the gates (ledger L6 only open, the function at the signed digest, XA-f98b RULED, the helper blob, the CTO ruling cited); AC2 the transient user (staff role, firm opal-capital, 0 entitlement rows, removed read back ABSENT, the password in memory only); AC3 the old receipt readable, ONE new export readable with no email, the counters. Do not edit the checks.

## BOUNDS

- **Grant:** the helper's one put and one delete on the one synthetic users row; reads of the function configuration and the ledger; ONE export request on DEV through the portal route under that login; reads of that export's status and of one pre-existing receipt; your record folder. **NO production export; NO client email or notification; NO second export; NO change to any function, role, schedule, layer or environment; NO change to any other users row; NO deletion except the one synthetic row; no ledger closed.**
- **Refusal clause:** STOP and report on any of: a helper blob that differs; XA-f98b not RULED; a role other than staff or a firm entitlement row on the user; an export that would email anyone; a refused status read of the old receipt (that is a finding about IB-pr-521, report it whole).
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
comp-blast: RUN -- one synthetic users row minted and removed in the portal's shared `opal-users-v2` (cross-box, ruled for this shape by XA-20261016T160537Z-f98b; staff role only, no firm entitlement row, 3-hour TTL as the second rollback); ONE export on DEV; nothing else is written; no function, IAM or schedule changes.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is changed.
comp-routes: RUN -- the portal's existing export route is called as the page calls it; no route is created or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p246_cells.py IB246-1 dry-run at base on dell2 2026-10-16 ~17:0xZ: AC1, AC2, AC3 FAIL (no record). Positive control (control246.py): the three positives PASS and each negative (a wrong digest, a helper blob that differs, XA not RULED, the ledger not open at L6 only, a non-staff role, a firm other than opal-capital, an entitlement row, a user not removed or not read back ABSENT, a password written out, an old receipt refused, two exports, a new export unreadable or non-2xx, an email sent, a code or IAM or schedule change, a deletion, a ledger closed by the applier) fails its own arm. NOT measured by me: the helper's current behaviour, the page's request shape and which account a staff login may export, the old receipt's status word.
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2` (dell2). Class SERVED.
</preflight>
