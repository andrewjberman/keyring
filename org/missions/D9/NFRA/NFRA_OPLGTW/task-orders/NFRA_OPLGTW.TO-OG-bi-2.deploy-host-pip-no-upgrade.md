# NFRA_OPLGTW task order -- `OG-bi-2` -- the gateway deploy's host step no longer upgrades pip (CTO ruling msg 31243)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-bi-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~33</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-line deletion in a build script with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's ruling (1.0.0_SA_CTO~Z msg 31243).
EGRESS CLASS, declared: NONE. This cell removes an egress; it makes no network request of any kind.
</preflight>

## 1. THE CELL -- `OG-bi-2` (decomposition addendum R3-T.24)

Handed only after `OG-bi-1` is complete, in the same worktree: both cells edit
`infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.

The script's host step (the block sent to the EC2 host over SSM) runs two pip commands at every deploy:

```
sudo -u ec2-user ${REMOTE_DIR}/.venv/bin/pip install --progress-bar off --upgrade pip
sudo -u ec2-user ${REMOTE_DIR}/.venv/bin/pip install --progress-bar off -r requirements.txt
```

The first asks the package index for the newest pip at every deploy and installs it if one exists. Nothing in the
gateway needs it.

Do:
1. Delete the `--upgrade pip` line. Leave one comment line in its place saying it was removed on the CTO's ruling
   (msg 31243) because it asks the index at every deploy.
2. Do NOT change the `-r requirements.txt` line, the comment block above the two lines, or anything else in the script.
   Whether the host may install requirements at all is with Andrew and is not decided here.
3. Add `infra/aws/ec2/opal-gateway/tests/test_deploy_host_pip_no_upgrade.py` with the three named tests the header of
   `bi2.AC1.sh` lists. They read the script's text; nothing is run. For test 03, read the earlier text with
   `git show <the commit before your edit>:infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` and name that commit in the
   test as a constant.
4. `bash -n infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` must pass; state its exit code.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~33/`.

## 2. BOUNDS

- **Fetch nothing.** No `pip install`, `bun install`, `npm`, `curl`, `wget` or any command that can reach the
  internet.
- No deploy, no host act, no AWS call. The script is not run.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/opal-gateway/tests/test_deploy_host_pip_no_upgrade.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~33/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W33-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-bi-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r28/checks/bi2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the pip upgrade line is gone, the requirements line is unchanged, and the reader sees the old line in the
  earlier text.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-bi-2.deploy-host-pip-no-upgrade.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If the criterion PASSES, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC output, the diff of the script, the `bash -n` exit code, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 28, workstream HOST-PIP-R40, cut on `1.0.0_SA_CTO~Z` msg 31243 and R40 of `ledger/ROUND_ANALYSIS.round27.md`
  @028a074f26 (R3-T.24). Chain: `OG-bi-1` -> `OG-bi-2`. Its write surface overlaps OG-bi-1's one file, so the two run
  in turn in one worktree, never at once.
- The hold on gateway deploys from site Z lifts when BOTH cells are complete and drained. It does not wait on Andrew's
  answer about whether the gateway host is a "box" under his no-fetch word (asked by the CTO at ~17:4xZ).
- Standing term from the same ruling: until he answers, a gateway release whose diff touches `requirements.txt` goes
  to `1.0.0_SA_CTO~Z` before its never-widen pair.
- Pre-cut 18:0xZ: `bi2.AC1` FAIL (the test file is absent).

<status>pending</status>
<round>28</round>
<workstream>HOST-PIP-R40</workstream>
<slot>~33</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
