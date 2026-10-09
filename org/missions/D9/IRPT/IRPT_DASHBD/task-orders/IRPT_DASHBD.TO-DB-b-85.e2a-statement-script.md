# TO IRPT_DASHBD.TO-DB-b-85 -- E3: build the Performance client statement runner e2a_real_statement.py (run / verify-submission / verify-persisted) and its offline test -- the persist body never asserts identity and the refs file carries no figure (CU21-AC3)

<to_id>IRPT_DASHBD.TO-DB-b-85</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~61</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>41</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 9.1 (msg 3011; the IRPT_CUSTDY handover @185805a565), enrichment item E3 | **Decomp cell:** `DB-b-85` (decomposition section 43) | **outcome_ref:** FWD-12 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-61`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~61/`.

**The cell (`DB-b-85`).** This is the build half of IRPT_CUSTDY's CU-g-2a (absorbed; handover @185805a565). Its AMENDMENT 1 moved the two real
writes to an AE seat (`DB-b-86`) and kept this offline build with a worker. Read the original cell text, which you build to:
`C:/dev/wk-irpt-dashbd-61/org/missions/D9/IRPT/IRPT_CUSTDY/task-orders/IRPT_CUSTDY.TO-CU-g-2a.real-statement-retained-and-persisted.md`, its "THE CELL"
section.

- **Product name and ids:** the product is the "Performance client statement"; in code it is `CUSTODY_REPORT`, policy `irpt-custody-x10-v1`.
- **The submission:** `infra/aws/lambda/investor-reporting/ycharts/generate/custody_submission.py`.
- **The writer:** `POST /api/scoped/investor-reporting/custody-report`, operation `custody-report-persist`. Its body is `retained_request`
  plus `document` plus an optional `provenance`, and never owner, principal, account_ids, tenant or firm_id. Code:
  `infra/aws/lambda/investor-reporting/export/custody_persist.py`, `custody_write.py`, `entry.py`.
- **The household document:** `data/assets/scripts/gold/irpt_custody/hop3_real_run.py` and `client_report_figures.py`, validated by
  `validate_document`, using this project's existing household pick (`pick_reread.py`).
- **The caller:** the writes are made by the service subject `svc-custody-statement` (its token read from
  `opal/investor-reporting/svc-custody-statement` by the AE seat). The script takes the token from an environment variable or a file
  path, never from the repo.

**Build `data/assets/scripts/gold/irpt_custody/e2a_real_statement.py`** with three subcommands:
- `run --refs <path>` retains ONE submission for ONE household and persists its document. It writes refs only: the submission ref, the
  persisted ref, revisions, the as-of date, the household's opaque id, each call's HTTP status, and an `other_firm` list.
- `verify-submission --refs <path>` re-reads LIVE and prints `SUBMISSION RETAINED policy=<revision> ref=<ref>`.
- `verify-persisted --refs <path>` re-reads LIVE and prints `PERSISTED kind=CUSTODY_REPORT revision=<n> ref=<ref>`.

**Add `data/assets/scripts/gold/irpt_custody/tests/test_e2a_real_statement.py`, offline.** It asserts that:
- the persist body never carries the five refused keys;
- the refs file holds no figure (no number but revisions and HTTP statuses).

**Do NOT run `run`.** No AWS write and no live call in this cell: the AE seat runs it in DB-b-86.

<criterion id="DB41-2-AC1" cell_refs="DB-b-85"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r41/p41_round41.py" . DB41-2-AC1</invocation><expect>DB41-2-AC1 PASS</expect></criterion>
`DB41-2-AC1` -- the offline test passes: no identity key in the persist body, no figure in the refs. Base: FAIL.

<criterion id="DB41-2-AC2" cell_refs="DB-b-85"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r41/p41_round41.py" . DB41-2-AC2</invocation><expect>DB41-2-AC2 PASS</expect></criterion>
`DB41-2-AC2` -- the runner exposes run, verify-submission and verify-persisted. Base: FAIL.

<expected_criteria>DB41-2-AC1,DB41-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you write the two files under `data/assets/scripts/gold/irpt_custody/` named in `<paths>` (a new runner and its
  test). No IRPT_BCKEND code is edited. No AWS write or live call: `run` is not executed here.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~61/
data/assets/scripts/gold/irpt_custody/e2a_real_statement.py
data/assets/scripts/gold/irpt_custody/tests/test_e2a_real_statement.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-85.e2a-statement-script.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 43 (round 41), cell `DB-b-85`.
<owned_cells>DB-b-85</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB41-2-AC1, DB41-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~61/IRPT_DASHBD.TO-DB-b-85.e2a-statement-script.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB41-2-AC1,DB41-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the script's subcommands, the test result, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a new offline runner and its test; nothing runs live in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call in this cell.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes; the route is IRPT_BCKEND's, already live.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: a one-off act; no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB41-2-AC1/AC2 FAIL at base (no script, no test). IRPT_CUSTDY TO-CU-g-2a AMENDMENT 1: the build stays a worker's.
lane: the <paths> block IS the grant.
</preflight>
