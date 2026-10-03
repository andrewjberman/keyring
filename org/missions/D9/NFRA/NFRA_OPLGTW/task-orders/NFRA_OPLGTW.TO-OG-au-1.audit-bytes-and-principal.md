# NFRA_OPLGTW task order -- `OG-au-1` -- the transcript read's audit record carries its returned bytes and the principal key, BUILD only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-au-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~19</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change and its tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS resource or permission is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the remedy is the CTO's (analysis round 12 s.3a, row Z-W15-S23).
EGRESS CLASS, declared: NONE (local tests only).
</preflight>

## 1. THE CELL -- `OG-au-1` (decomposition addendum R3-T.7, item 2)

Today a `read_meeting_transcript` audit record (`infra/aws/ec2/opal-gateway/app/audit.py` `log_call`, :130-139; called
from `app/tools.py` `_run`, ok path ~:174, the tool's `audit_detail` ~:615) holds `ts, user, tool, args, outcome,
detail, tier`. It names neither how many bytes the read returned nor the principal the tier decision used (the principal
cutover is live, so email no longer identifies it).

1. `log_call` gains two OPTIONAL keyword arguments, `bytes_returned: int | None = None` and `principal: str | None =
   None`. When given, the record gains top-level keys `bytes` (int) and `principal` (`"<tid>/<oid>"`). When not given,
   the record is byte-for-byte what it is today: no new keys. `user` (email) stays as the display field.
2. `read_meeting_transcript`'s ok-path audit call passes the read's `returned_bytes` and the current principal
   (`get_current_principal()`, rendered `<tid>/<oid>`). No other tool changes.
3. New file `infra/aws/ec2/opal-gateway/tests/test_audit_bytes_principal.py` with exactly these tests:
   - `test_ogau1_ac01`: a `read_meeting_transcript` ok record carries `bytes` equal to the read's `returned_bytes` and a
     `principal` matching `^[0-9a-f-]{36}/[0-9a-f-]{36}$`, and still carries `user`;
   - `test_ogau1_ac02`: a `log_call` without the new arguments writes exactly the old key set (`ts, user, tool, args,
     outcome, detail, tier`);
   - `test_ogau1_ac03`: an error-path transcript record carries no `bytes` key (nothing was returned).
   Synthetic principal and transcript only; `AUDIT_PATH` isolated; no network.

## 2. BOUNDS

Edit ONLY `app/audit.py`, `app/tools.py` and the new test file. No deploy, no release tree (`OG-rl-4` ships it). No
transcript text anywhere. Never push, merge, rebase, stash, `checkout --` or `clean`; never override a gate. Every `.py`
edit passes `.tools/commit-gate.sh`; commit with `.tools/safe-commit.sh`.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/audit.py
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/tests/test_audit_bytes_principal.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~19/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W19-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-au-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/au.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-au-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/au.AC2.sh; echo "exit=$?"</invocation><expect>(?s)outside the allowed three: 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass.
- `AC2`: the cell's commits touch only the three named gateway files.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~19/NFRA_OPLGTW.TO-OG-au-1.audit-bytes-and-principal.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`; if both PASS, append a `complete` status tag after the
order's last status line in the same commit. Report once: the diff summary, the literal AC output, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 14 (addendum R3-T.7, item 2); feeds `OG-rl-4`. Pre-cut: `au.AC2` FAIL (no commits); `rl4.AC2` on the live
  audit reads 6 post-deploy transcript reads with neither field.

<status>pending</status>
<round>14</round>
<slot>~19</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
