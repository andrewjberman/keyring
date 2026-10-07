# TO NFRA_CTLPLN.TO-CT-d-4 -- round 4 CT-d-4: the deploy read-back -- deployed bytes compared to the commit a Dell named

<to_id>NFRA_CTLPLN.TO-CT-d-4</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~7</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-d-4` (`decompositions/NFRA_CTLPLN_DECOMP.round4.md`) | **outcome_ref:** FWD-10 |
**depends_on:** CT-d-3 (`.tools/named_commit_check.py`), merged before this order is handed

---

## WORKER FACE

### THE CELL

`CT-d-4`, PRD v0.12 ADDENDUM v0.9 (b): "one exercised deploy from a Dell of a commit no other box has merged, with the deployed bytes
read back against that commit." You BUILD the instrument that read-back runs on and prove it against stand-ins. You do NOT run the live
deploy: it needs a Dell and is run after your order by the issuer's route.

**What exists after CT-d-3:** `.tools/named_commit_check.py check --commit <full hash> [--device <name>] [--remote origin]`, printing
`NAMED-COMMIT <ADMITTED|REFUSED|UNCHANGED> commit=.. device=.. role=.. trunk=<ON-TRUNK|OFF-TRUNK> branch=.. reason=..`.

**Build:**

1. `org/devices/deploy_readback_check.py` -- arguments `--commit <full hash>`, one or more `--object <repo path>=<s3://bucket/key>`
   (a code or data file deployed by copy), zero or more `--lambda <repo zip-source dir or file>=<function name>` (optional; if you
   cannot compare a Lambda's deployed code to a repo path without a build step, support `--lambda-sha256 <function>=<expected>` instead
   and say so), `--ledger <entry path>`, `--aws <command>` (default the repo's `.tools/aws` shim), `--remote origin`. Steps, each
   printed as one line:
   (1) the named-commit check for this device and commit (call the tool; do not re-implement it); the run continues only on ADMITTED;
   (2) NOT MERGED ELSEWHERE: after a fetch, the commit is not an ancestor of `<remote>/CLOUD` (`on_trunk=False`); if it IS on the
       trunk the run still completes but reports `on_trunk=True`, which fails the exercised bar;
   (3) per `--object`: `git show <commit>:<repo path>` bytes versus the S3 object's bytes (`s3api get-object` to a temporary file),
       compared by SHA-256 and length; print both digests;
   (4) the ledger entry at `--ledger` exists, is CLOSED, and carries `named_commit=<the same hash>`;
   LAST line `DEPLOY-READBACK commit=<hash> device=<d> admitted=<True|False> on_trunk=<True|False> objects_equal=<e>/<n> ledger=<closed-named|open|missing|other-commit> ok=<True|False>`,
   `ok=True` only when admitted, `on_trunk=False`, `e == n`, `n >= 1` and the ledger is `closed-named`.
2. `org/devices/test_deploy_readback.py` -- the script run against stand-ins: a local bare repository as `origin` and a clone, a
   temporary register, a fake `--aws` command (a small Python script the test writes that serves object bytes from a table), a
   temporary ledger entry. Cases: (1) the happy path -> `ok=True`; (2) one deployed object differs by one byte -> `objects_equal=0/1`,
   `ok=False`; (3) the commit has since been merged to `origin/CLOUD` -> `on_trunk=True`, `ok=False`; (4) the ledger entry names another
   commit -> `ledger=other-commit`, `ok=False`; (5) the ledger entry is still open -> `ok=False`; (6) the commit is unpublished ->
   `admitted=False`, `ok=False`. LAST line `DEPLOY-READBACK-SELFTEST cases=<k>/6 ok=<True|False>`.

### ACCEPTANCE

<criterion id="CT4d4-AC1" cell_refs="CT-d-4"><invocation>python org/devices/test_deploy_readback.py</invocation><expect>DEPLOY-READBACK-SELFTEST cases=6/6 ok=True</expect></criterion>
`CT4d4-AC1` -- the read-back reports success only when the named commit is admitted, unmerged elsewhere, byte-equal where deployed and
recorded in a closed ledger entry; each of the five failure arms turns `ok` false.

<criterion id="CT4d4-AC2" cell_refs="CT-d-4"><invocation>python .tools/tests/test_named_commit_deploy.py</invocation><expect>NAMED-COMMIT-TEST cases=8/8 ok=True</expect></criterion>
`CT4d4-AC2` -- the control on the real neighbour: CT-d-3's eight cases still hold beside your script.

<expected_criteria>CT4d4-AC1,CT4d4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No AWS call, no deploy, no push to a real remote.** Every AWS call in your tests goes to the fake command.
- No non-ASCII in any file you write. The commit gate runs ruff: avoid ambiguous single-letter names such as `l`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W7-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
org/devices/deploy_readback_check.py
org/devices/test_deploy_readback.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `.tools/named_commit_check.py`, `.tools/tests/test_named_commit_deploy.py`,
`.tools/deploy_ledger.py`, `org/devices/DEVICES.json`, `org/devices/test_role_roundtrip.py` (the stand-in pattern: bare origin, fake AWS).

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round4.md</decomp_doc> (round 4), cell `CT-d-4`.
<owned_cells>CT-d-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT4d4-AC1, CT4d4-AC2. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~7/NFRA_CTLPLN.TO-CT-d-4.deploy-readback.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT4d4-AC1,CT4d4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines; the exact command line a Dell runs after a deploy; how a Lambda is compared (or that it is not); commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE at the worker (no AWS call); the live read-back's object reads run under the Dell's own identity at the close.
comp-adversary: RUN -- a read-back that passes on the wrong bytes (one-byte arm, case 2); a "nobody else merged it" claim that is false (case 3 turns ok false); a deploy with no closed record or a record of another commit (cases 4 and 5); running bytes older than built (the comparison is to the named commit's bytes by content, never by filename or timestamp); BLIND: a Lambda whose package is built, not copied -- stated on the face; the worker says how it compares or that it does not.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.12 @2f61412157 ADDENDUM v0.9 (b); decomposition round 4. Base dry-run at the cut: CT4d4-AC1 base FAIL as expected (no
file); CT4d4-AC2 is a control that exists only after CT-d-3 merges (FAIL at this base: the file does not exist yet -- stated).
