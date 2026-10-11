# NFRA_OPLGTW task order -- `OG-dr-1` -- the gateway deploy drains before it restarts, so a refresh in flight is not turned into a revoked session (row Z-S67)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-dr-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~35</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a change to how a one-shot deploy stops the service; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- one read-only SSM read of the service unit's stop settings; no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's ruling (1.0.0_SA_CTO~Z msg 31444) on row NFRA_OPLGTW-Z-S67.
EGRESS CLASS, declared: NONE beyond one read-only SSM command on Opal's own host. Nothing is fetched from the internet.
</preflight>

## 1. THE CELL -- `OG-dr-1` (decomposition addendum R3-T.28)

On 2026-10-07 at 21:49Z the r28 deploy restarted the gateway and one client's whole session was revoked with reason
`refresh_token_reuse` (row `NFRA_OPLGTW-Z-S67`). The rule is in
`infra/aws/ec2/opal-gateway/app/oauth_as.py` lines 903-915: a refresh token that is not the family's current generation
but equals an earlier issued one revokes the family. The reading of the event, INFERRED and not yet shown: the restart
cut a token refresh after the rotation was written and before the answer reached the client; the client retried with
the token it still held; the rule fired.

The deploy restarts the service at `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` line 416
(`sudo systemctl restart ${SYSTEMD_UNIT}.service`). The unit is `infra/aws/ec2/opal-gateway/deploy/opal-gateway.service`
(`uvicorn app.server:app --workers 1`).

**Make the deploy drain before it restarts:** the service stops taking new requests, finishes the requests in flight
and their writes, and only then stops. **Change NO security rule: `oauth_as.py` is not edited.** A grace window for the
previous token is a separate question the CTO has put to research; it is not this cell.

Do:
1. **Find what the stop does today**, and write it in `W/DR1_STOP_TODAY.md`:
   - read the unit file and the deploy's host step in the repo;
   - ONE read-only SSM command on the host: `systemctl show opal-gateway.service` for `TimeoutStopUSec`, `KillMode`,
     `KillSignal`, `SendSIGKILL`, `ExecStop`, `ExecStart`, and the journal lines of the stop at 21:49Z today
     (`journalctl -u opal-gateway.service --since "2026-10-07 21:48:30" --until "2026-10-07 21:50:30" --no-pager`).
     Record the settings and the journal's stop and start lines with their times. Print no request line that carries
     an identifier; if the journal holds any, keep counts and times only.
   - what uvicorn does on the stop signal, read from the installed uvicorn's own source in this box's Python
     environment (name the file and lines): whether it finishes in-flight requests and what bounds the wait.
   - Say plainly whether today's stop could cut a request in flight, and where.
2. **Reproduce the mechanism offline FIRST** (test 02 of `dr1.AC1.sh`): a harness around the gateway's own token
   endpoint or `oauth_as`'s refresh function with a FAKE state store, a refresh slowed after its rotation is written,
   an abrupt stop, the client's retry with the just-rotated token, and the family revoked with `refresh_token_reuse`.
   If you CANNOT reproduce it, STOP and report: the inference of row Z-S67 would then be wrong, and that is the
   finding.
3. **Make the stop a drain.** Use the smallest change that the evidence of step 1 supports: the unit's stop settings
   (a graceful signal, a stop wait long enough for an in-flight refresh and its writes, no immediate kill), uvicorn's
   own graceful-shutdown bound if it needs one, and the deploy's host step if it must stop-then-start in place of
   restart. State the drain bound in seconds in `W/DR1_DRAIN.md` and why that number.
4. **Tests:** `infra/aws/ec2/opal-gateway/tests/test_deploy_drain_before_restart.py`, the three tests the header of
   `dr1.AC1.sh` lists, named EXACTLY `test_ogdr1_ac01`, `test_ogdr1_ac02`, `test_ogdr1_ac03`. They run on this box
   (Windows): stop the server through uvicorn's own shutdown path in-process (for example `Server.should_exit`) for
   the graceful arm and by cancelling its task for the abrupt arm, in place of POSIX signals. Say in the test's
   docstring what that stands in for and what it does not show.
5. Run `tests/test_deploy_base_guard.py`, `tests/test_deploy_install_no_fetch.py`,
   `tests/test_deploy_host_pip_no_upgrade.py` and every `tests/test_oauth*.py`, each in its own process, and state
   each file's totals.
6. **State the limit honestly in `W/DR1_DRAIN.md`:** what the offline tests show about the real host, and what only a
   real deploy can show. Name the one read a release should make after the next deploy (for example: families
   revoked since the deploy started, from the state table; statuses and reasons only).

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~35/`.

## 2. BOUNDS

- `app/oauth_as.py` is NOT edited. No token rule, expiry or reuse rule changes.
- ONE read-only SSM command on the host. No restart, stop, reload, deploy or write on the host. No state-store write:
  the tests use a fake store.
- Fetch nothing from the internet: no `pip install`, `bun`, `npm`, `curl`, `wget`. AWS only through `.tools/aws`.
- Never print or commit an email address, tid, oid, client account id, credential, token, token hash or family id.
- Never read the gateway's sign-in cache.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/opal-gateway/deploy/opal-gateway.service
infra/aws/ec2/opal-gateway/tests/test_deploy_drain_before_restart.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~35/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W35-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-dr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r30/checks/dr1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-dr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r29/checks/bi4.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 2 of 2; file passed (\d+); failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a refresh in flight survives a graceful stop; an abrupt stop reproduces the revocation; the deploy stops the
  service gracefully.
- `AC2`: the deploy base-guard tests still pass on the changed script.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-dr-1.deploy-drain-before-restart.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC outputs; what the stop does today (settings, journal times, uvicorn's behaviour with file
   and lines); whether the mechanism reproduced; the change (diff) and the drain bound; the limit; the neighbouring
   files' totals; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 30 (R3-T.28), cut on `1.0.0_SA_CTO~Z` msg 31444 (the round-29 analysis by message), remedy 1 of row Z-S67.
  Remedy 2, a grace for the previous token generation, is with `4.0.0_SA_CRO~Z` for research and is not cut.
- The unit file ships to the host, so this cell rides a release; that release is itself under the form's 12-hour bar
  until the drain is shown on a real deploy.
- Test 02 also converts row Z-S67's INFERRED mechanism into an exercised one, or refutes it.
- DISPOSITION (23:2xZ, issuer, on `1.0.0_SA_CTO~Z` msg 31464): BUILT and NOT DRAINED. The worker completed the cell on
  branch `wk-NFRA_OPLGTW-30-35` @47dd5053b2 (dr1.AC1 3 of 3 by its report; not re-graded by the issuer). Its own read
  and the issuer's (`deliverables/2.0.0_SA_COO~O/S67_REVOCATION_READ_20261007.md` @acf83a5716) show the 21:49Z stop was
  already graceful and the session was revoked on the new process, so the drain prevents nothing measured. The CTO
  ruled it is not shipped. The remedy of row Z-S67 is at the client: one session holds the concierge's sign-in
  (prepared by `0.0.0_AB_MSTR~Z`, applied on Andrew's word). This file's `<status>` on CLOUD stays as issued; the
  branch is kept, undrained, as the record of the build.
- Pre-cut 22:5xZ: `dr1.AC1` FAIL (the test file is absent); `bi4.AC1` PASS (file passed 8).

<status>superseded</status>
<superseded_by>1.0.0_SA_CTO~Z round-32 analysis @3566a85699 (row W35-S1): the branch was never drained, the gateway moved on to r29; the restart-free route in server.py becomes round-34 cell E3. Set by the issuer 2.0.0_SA_COO~O.</superseded_by>
<round>30</round>
<slot>~35</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
