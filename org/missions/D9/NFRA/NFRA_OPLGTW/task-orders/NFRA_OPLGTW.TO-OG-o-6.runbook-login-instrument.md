# NFRA_OPLGTW task order -- `OG-o-6` -- the runbook names the raw lake prefix as the /login instrument

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-o-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~22</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a runbook edit; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- repo only; no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ruling is the CTO's (R26, round-20 analysis s.3).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-o-6` (decomposition addendum R3-T.14, item 3; row Z-W15-S64)

R26 (b): the Glue table `mcp_audit` reads a `gw_login` record as `ts` and `outcome` only. The RAW lake prefix is
the `/login` instrument of record. In `infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md` section 5
(audit read / status summary), add ONE paragraph:
- name the prefix, bucket `opal-mcp-audit`, `audit/dt=<YYYY-MM-DD>/`;
- name the `gw_login` record and its fields `outcome`, `reason` and `email_digest`. Read the exact field set from
  `app/audit.py` `log_login`;
- state that the Glue table shows only `ts` and `outcome` for these records.
The runbook is in the gateway git tree but is not one of the host's 96 shipped files
(`deliverables/0.9.0_WK_NFRA_OPLGTW~15/r19b_release_md5.txt` lists no `runbooks/` path). A git diff of the gateway tree
from live to CLOUD will therefore show it. Add it to `deliverables/0.9.0_WK_NFRA_OPLGTW~22/LINEAGE_R18.json` `items` as
`{path, kind: CLOUD_ONLY, owner: OG-o-6, disposition: NOT_HOST_SHIPPED, note}` (R16), with the note saying the host
bytes are unchanged and the file rides the next release's tree.

## 2. BOUNDS

- Repo edits within your paths only; no deploy, no host or AWS write.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/LINEAGE_R18.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W22-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-o-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r21/checks/o6.AC1.sh; echo "exit=$?"</invocation><expect>(?s)section 5 found True; names raw prefix True; gw_login True; fields True; runbook listed CLOUD_ONLY in LINEAGE True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/NFRA_OPLGTW.TO-OG-o-6.runbook-login-instrument.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`, and on PASS edit this order's ONE `<status>` tag IN
PLACE to `complete`. Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 21 (R3-T.14, item 3). Alone. LOCAL: no release.
- Pre-cut: `o6.AC1.sh` FAIL (no prefix, no gw_login, not listed).

<status>pending</status>
<round>21</round>
<slot>~22</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
