# NFRA_MCPORTAL task order -- `MP-f-1` -- ROUND 3, E3: the gateway suite stops writing the tracked audit file (R-8)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-f-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~4</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a test fixture; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no IAM surface.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC1 carries its own positive control.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MP-f-1` (round 3, decomposition section R3.2; the round's batch cell)

In `infra/aws/ec2/opal-gateway/`, running `tests/test_owner_gate.py` appends lines to the TRACKED file `audit.jsonl`.
The audit path defaults to `./audit.jsonl` (`app/config.py:307`, `AUDIT_PATH: str = os.environ.get("AUDIT_PATH",
"./audit.jsonl")`), and the tests run with `infra/aws/ec2/opal-gateway/` as their working directory. The issuer
measured it at the cut: 14 tests passed, and the file's md5 changed.

Build: a **session-scoped fixture** in `infra/aws/ec2/opal-gateway/tests/conftest.py` that points the audit path at a
temporary file for the whole test session, before any app module reads its config. Read how `app/config.py`'s
`get_config()` caches, and how the audit writer reads the path, then pick the mechanism: the environment variable set
before import, and/or patching the cached config object. The fixture must reach every test in `tests/`. It must not
depend on test order, and must not delete or rewrite `audit.jsonl`.

**Do NOT change `app/config.py` or any `app/` file.** The running gateway's env sets `AUDIT_PATH`; the default stays.

## 2. BOUNDS

1. Your write surface is exactly `tests/conftest.py` plus your deliverables and rows.
2. Never restore `audit.jsonl` with `git restore` or `git checkout`. If a run of yours dirties it, copy it back from
   the bytes you saved before the run. AC1 does this itself.
3. The full suite does not collect on this box: 13 files fail on `No module named 'moto'`, and installing it is vendor
   egress, which is NOT granted. The full run is the issuer's drain check, not yours. Do not install anything.
4. Standing: no push. REFUSE a criterion you cannot meet as written and report the refusal with its measurement. Never
   repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/conftest.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~4/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/`, `infra/aws/ec2/opal-gateway/tests/`,
`infra/aws/ec2/opal-gateway/audit.jsonl`, `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W4-S<k>`, starting at k=1.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-f-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/f1.AC1.sh; echo "exit=$?"</invocation><expect>pytest N passed with N>=1 and 0 failed; audit.jsonl md5 before == after; porcelain before=0 after=0; control seen=yes; restored=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-f-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/f1.AC2.sh; echo "exit=$?"</invocation><expect>app/config.py at HEAD: AUDIT_PATH default line present=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~4/NFRA_MCPORTAL.TO-MP-f-1.audit-path-fixture.proof_of_spec.json`.
Report once, with:
- the mechanism you chose, and why the config's caching required it;
- the pytest line;
- the commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E3 / R-8 of ROUND_ANALYSIS.round2.md @33ca99c40e. It disarms row Z-W2-S3 (ARMED, transferred to this
seat with the project). Checks dry-run at base: AC1 FAILS as expected (md5 moved, 14 passed); AC2 PASSES as expected
(the bound). The disarm row is the issuer's act at the drain.

<status>pending</status>
<round>3</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
