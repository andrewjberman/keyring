# NFRA_OPLGTW task order -- `OG-lk-1` -- no audit-lake object gets a key with an empty time part (ruling R43, row Z-W28-S26)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-lk-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~34</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- one read-only S3 GET of an object the gateway's own audit lake holds; no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's ruling R43 (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round27.md @028a074f26).
EGRESS CLASS, declared: NONE beyond one read of Opal's own S3.
</preflight>

## 1. THE CELL -- `OG-lk-1` (decomposition addendum R3-T.25)

The gateway writes each audit record to its raw audit lake, bucket `opal-mcp-audit`, under a key of the shape
`audit/dt=<day>/<ts>-<id>.jsonl` (the writer is `_emit` in `infra/aws/ec2/opal-gateway/app/audit.py`). On 2026-10-07 one
object was written under `audit/dt=2026-10-07/-321b3117.jsonl`: its time part is EMPTY. Such a key sorts ahead of every
other key of its day, and two of them written with the same id would collide.

Do:
1. **Find which record produced it.** Read that ONE object, read-only (`.tools/aws s3 cp <s3 uri> -` or `s3api
   get-object` to a temp file outside the repo, deleted after). Record in `W/LK1_CAUSE.md` ONLY: the record's `tool`
   name, the NAMES of its fields, which time field is missing or empty, and which function in the gateway writes a
   record of that shape (read the code to find it; name file and line). Never write a field VALUE: no user, email,
   principal, id or argument value goes into any file or your report. If the object is gone or unreadable, say so and
   find the cause from the code alone.
2. **Fix the stamp at the writer.** The lake key's time part must never be empty. Fix it where the key is built, so a
   record arriving without a usable time gets the writer's own current UTC time in the same format the other keys
   carry, and the day partition is taken from that same time. Do not change any record's fields, and do not change the
   key of a record that already carries its time.
   - If the cause is a caller that builds a record without a time field, ALSO say so in `W/LK1_CAUSE.md`; fix the
     caller only if it is one line in `app/` and you name it in your report.
3. **Tests:** `infra/aws/ec2/opal-gateway/tests/test_audit_lake_key_stamp.py`, offline, the three named tests the header
   of `lk1.AC1.sh` lists, named EXACTLY `test_oglk1_ac01`, `test_oglk1_ac02`, `test_oglk1_ac03`. No test touches S3:
   fake the client. For test 03, take the earlier key-building code with
   `git show <the commit before your edit>:infra/aws/ec2/opal-gateway/app/audit.py` and name that commit as a constant.
4. Run every `tests/test_audit*.py` and `app/tests/test_rivalfunds_view.py`, each in its own process, and state each
   file's totals.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~34/`.

## 2. BOUNDS

- ONE read of ONE lake object. Write nothing to S3; delete nothing; do not list more than the one day's prefix.
- No release and no host act. This cell is BUILT and HELD on your branch; it ships in a later release.
- Fetch nothing from the internet: no `pip install`, `bun`, `npm`, `curl`, `wget`. AWS only through `.tools/aws`.
- Never print or commit an email address, tid, oid, client account id, credential, token or any audit record's value.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/audit.py
infra/aws/ec2/opal-gateway/tests/test_audit_lake_key_stamp.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~34/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W34-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-lk-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r28/checks/lk1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a record without a time gets a stamped key; a record with one keeps its key; the old builder shows the defect.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-lk-1.audit-lake-key-stamp.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If the criterion PASSES, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC output; the cause (tool name, field names, the writing function with file and line); the
   code diff; each neighbouring test file's totals; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 28, workstream LAKE-KEY-R43, cut on R43 of `ledger/ROUND_ANALYSIS.round27.md` @028a074f26 (R3-T.25). Its write
  surface (`app/audit.py`, one new test) is disjoint from workstream HOST-PIP-R40 and from OG-bi-1 (the deploy script).
- A gateway code change: it ships in a later release, after the deploy hold lifts. Held on the worker branch until
  the issuer drains it.
- If the cause sits outside `app/audit.py`, the worker reports it and the issuer amends `<paths>`.
- Pre-cut 18:3xZ: `lk1.AC1` FAIL (the test file is absent).

<status>pending</status>
<round>28</round>
<workstream>LAKE-KEY-R43</workstream>
<slot>~34</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
