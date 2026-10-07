# NFRA_OPLGTW task order -- `OG-bi-4` -- the deploy base-guard test rig carries a lockfile and a cache, so its tests are green under the pre-check (row Z-W28-S27)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-bi-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~33</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a test-rig change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written; the rig stubs every AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is row NFRA_OPLGTW-Z-W28-S27, found in the r28 release's Phase A.
EGRESS CLASS, declared: NONE. No network request of any kind.
</preflight>

## 1. THE CELL -- `OG-bi-4` (decomposition addendum R3-T.27)

`infra/aws/ec2/opal-gateway/tests/test_deploy_base_guard.py` runs `deploy-to-ec2.sh` inside a rig that stubs the
dashboard checkout, `bun`, `aws` and the upload. On the live tree it reads 6 passed. On a tree that carries your
pre-check (OG-bi-1, OG-bi-3) it reads 3 passed and 3 failed: the rig's dashboard stub has no `bun.lock`, so the
pre-check exits before the script reaches the step those three tests assert on. The deploy script is behaving as
built; the rig is stale against it.

Do:
1. Read the rig and say in `W/BI4_RIG.md` exactly why each of the three tests fails (name them), with the line of the
   script the run stops at.
2. Give the rig's dashboard stub a small `bun.lock` and give the run a stub cache directory (through
   `BUN_INSTALL_CACHE_DIR`, a temp directory) holding COMPLETE entries for that lockfile, so the pre-check passes for
   the right reason. Never point the rig at bun's real cache. The rig's `bun` stays a stub: no real bun runs.
3. Do NOT weaken any existing assertion of the six tests, and do not change `deploy-to-ec2.sh` or
   `ops/bun_cache_precheck.py`. If a test can only pass by changing the script, STOP and report it: that would be a
   defect in the script, not in the rig.
4. Add two tests to the same file, named EXACTLY `test_ogbi4_ac01` and `test_ogbi4_ac02`, as the header of
   `bi4.AC1.sh` describes them. The second is the negative control: one lockfile entry absent from the stub cache
   stops the script with `ERROR: bun cache miss` before the rig's upload stub is called.
5. Run `tests/test_deploy_install_no_fetch.py`, `tests/test_deploy_install_no_fetch_complete.py` and
   `tests/test_deploy_host_pip_no_upgrade.py`, each in its own process, and state each file's totals.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~33/`.

## 2. BOUNDS

- **Fetch nothing.** No real `bun` command, no `npm`, `pip install`, `curl`, `wget`. The rig's stubs stay stubs.
- No deploy, no host act, no real AWS call. The script runs only inside the rig, against stubs.
- Never touch bun's real cache.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/test_deploy_base_guard.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~33/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W33-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-bi-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r29/checks/bi4.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 2 of 2; file passed (\d+); failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the base-guard file is green (its six tests and the two new ones), and a cache miss stops the script before
  the upload.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-bi-4.deploy-base-guard-rig.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If the criterion PASSES, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC output; why each of the three tests failed; the rig's diff; that no existing assertion was
   weakened (name any assertion line you touched); the three neighbouring files' totals; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 29, workstream GUARD-RIG-S27 (R3-T.27), cut on row Z-W28-S27 from `OG-rl-14`'s Phase A: 3 tests of
  `test_deploy_base_guard.py` pass on live and fail on the release tree. A release does not ship with new red tests.
- Its file is in the gateway tree, so the r28 release set gains it and the release commit is re-cut after this drains
  (`OG-rl-14` amendment A1).
- Pre-cut 20:3xZ: see the issuance commit.

<status>pending</status>
<round>29</round>
<workstream>GUARD-RIG-S27</workstream>
<slot>~33</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
