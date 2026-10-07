# NFRA_OPLGTW task order -- `OG-hg-1` -- the halt gate reads a worker's order from the shared root, and reads the LAST status tag (CTO R35 cell 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-hg-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~30</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a shell-library change with a fixture test; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's (ledger/ROUND_ANALYSIS.round23.md @c8a3b2911e, R35 cell 1).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-hg-1` (decomposition addendum R3-T.18, item 2)

`.tools/halt-gate-check.sh` admits a spine-v3 worker serial (`0.9.0_WK_<CODE>~<n>`) through
`halt_gate_worker_issuer` (about `:184-206`). That function has two defects (rows `NFRA_OPLGTW-Z-W28-S7`, `Z-S62`):

- **It reads the orders from `HALT_GATE_REPO_ROOT`'s HEAD.** A gateway release is deployed from a release tree cut on
  the LIVE sha. That sha predates the worker's order, so the tree holds no order for a new slot and the gate refuses
  (`SERIAL RESOLVES TO NO KNOWN AGENT`, rc=3).
- **It reads the FIRST `<status>` tag** (`grep -m1`). Orders APPEND their status flips, so the first tag is the stale
  one. Slot `~15` passed earlier releases only because its completed orders' first tag reads `staged`.

Do:
1. `halt_gate_worker_issuer` looks for the worker's order in the SHARED root (`HALT_GATE_SHARED_ROOT`) FIRST: its HEAD
   through `git -C`, and its tracked order files. Only then does it look in `HALT_GATE_REPO_ROOT`.
   - A `git show` or `ls-files` that fails is still a `continue` toward refusal, never an absence verdict.
2. It reads the LAST `<status>` tag of an order file. Take the last line that matches `^<status>...</status>` at the
   start of a line, so a status word quoted in prose or in the worker face does not count.
3. Everything else in the gate is unchanged: the fail-closed refusal, the issuer inbox scan, the `[STOP]` hard block,
   `HALT_ACK`, and the audit log.
4. Add `.tools/halt-gate-worker-order-test.sh`: a self-contained fixture in a temp directory (two throwaway git repos
   wired as a shared root and a linked release worktree; no network, no real inbox). It prints exactly one line per
   case, `PASS: case <n> <what>` or `FAIL: case <n> <why>`, and exits 0 only when all four pass:
   - case 1: the release tree predates the slot's first order; the order is non-terminal in the shared root; the gate
     admits and names the issuer;
   - case 2: the order's LAST status tag is `complete` though an earlier tag in the file reads `staged`; the gate does
     NOT admit;
   - case 3: the order's FIRST tag is `complete` and its LAST tag is `pending`; the gate DOES admit;
   - case 4: with case 1's order in place, a `[STOP]` message in the issuer's inbox still halts (non-zero, no override).
   Clean the temp directory on exit.
5. Negative control: with the old function restored, case 1 and case 2 fail. Record that run in
   `W/HG1_NEGATIVE_CONTROL.md`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~30/`.

## 2. BOUNDS

- No deploy and no host act. Do not run `safe-ec2-deploy.sh`.
- Do not change `infra/aws/ec2/safe-ec2-deploy.sh` or any other caller of the gate.
- `.tools/test-haltgt-recipient-scoping.sh` read `0 passed, 9 failed` before this cell, in the issuer's worktree and in
  the shared tree. Do not edit it. Say in your report what it reads after your change, and why if it moved.
- Local bash is Git Bash with default utilities only: no `pgrep`, `flock`, `setsid` or `wget`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
.tools/halt-gate-check.sh
.tools/halt-gate-worker-order-test.sh
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~30/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W30-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-hg-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r25/checks/hg1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)rc=0; cases passed 4 of 4; FAIL lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-hg-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r25/checks/hg1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)halt-gate-ld0131-test rc=0; recipient-scoping RESULT: \d+ passed, \d+ failed.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the gate admits a new slot's worker from a release tree, reads the last status tag, and still halts on STOP.
- `AC2`: the gate's existing tests are no worse than before.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-hg-1.halt-gate-worker-order-lookup.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit this order's ONE `<status>` tag IN PLACE to `complete`.
4. Report once: literal AC output, the negative control, the diff of the function, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 24 (addendum R3-T.18, item 2). No chain: it does not ship to the gateway host.
- Pre-cut 02:5xZ: `hg1.AC1` FAIL (the fixture test is absent). `hg1.AC2`: ld0131 rc=0; recipient-scoping reads
  0 passed, 9 failed in both trees, which is the baseline the check carries.

<status>complete</status>
<round>24</round>
<slot>~30</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
