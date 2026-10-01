# NFRA_OPLGTW task order -- `OG-ml-1` -- workstream TRNSPT-DEPS (O4): ADOPT the laptop mail tools (gw-mail-tools-int), BUILD only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ml-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~15</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two read tools and a $select widening; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; Mail.Read is already held (C7).
comp-adversary: DECLARED-NOT-APPLICABLE -- adoption of reviewed code per the issuer's triage @6d41bd25ec and PRD v1.2 C7.
EGRESS CLASS, declared: PyPI download of pypdf into a local venv only (development egress, Andrew-direct @7bfa5811c6 Q6). No AWS call, no deploy.
</preflight>

## 1. THE CELL -- `OG-ml-1` (decomposition addendum R3-T)

`GW` = `infra/aws/ec2/opal-gateway`. Read the triage
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/LAPTOP_MAIL_BRANCHES_TRIAGE_20260930.md` whole, and PRD
`org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v1.2 C7 "Mail tools (O4)" and "Attachments on MCP".

1. `git fetch origin gw-mail-tools-int gw-f1-read-email-fields gw-f2-email-filtered gw-f3-inspect-attachment`. Verify the
   tips by content: `6a7b9e78fa`, `5ec089b9a1`, `15ef03f0bc`, `6c61ac531b`.
2. Apply `6a7b9e78fa`'s gateway hunks with `git cherry-pick --no-commit`. DROP its `org/tier0/ledger/LD-0613.md` hunk:
   restore that file to HEAD bytes, so it is unchanged in your commit.
3. Take the three test files by content: `tests/test_read_email_fields.py` from `5ec089b9a1`,
   `tests/test_list_email_filtered.py` from `15ef03f0bc`, `tests/test_inspect_email_attachment.py` from `6c61ac531b`.
4. Re-read the hard tool count in `GW/tests/test_entitlement_admin.py::test_ogz2_ac08` at YOUR base. Set it to that
   base count + 2 (`list_email_filtered`, `inspect_email_attachment`), naming both in a comment.
5. Pin `pypdf` in `GW/requirements.txt` with one `pypdf==<version>` line. Use the version whose local install makes
   the tests pass, and record it.
6. The attachment tool stays INSPECT-only: no MCP tool returns attachment bytes (C7). If the adopted code returns
   bytes anywhere, that is a BLOCKING row.
7. The two new tools are in SAFE_TOOLS and NATIVE_TOOLS (the branch already does this; verify).

## 2. BOUNDS

1. Code and tests only. No Graph call, no AWS call, no deploy. Never edit `GRAPH_SCOPES`, the identity allowlist,
   `ms_ingest.py`, LD-0613 or the PRD.
2. Every test run sets `AUDIT_PATH` to a temp file; restore `GW/audit.jsonl` if dirtied.
3. Same worktree as `OG-tx-1` (your queue position 2): start from its committed head. Never push, merge, rebase,
   stash, `checkout --` or `clean`. REFUSE a criterion you cannot meet as written.
4. Commit with `.tools/safe-commit.sh` under your serial. Every `.py` you touch passes `.tools/commit-gate.sh`.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/destructive_ops.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/requirements.txt
infra/aws/ec2/opal-gateway/tests/test_read_email_fields.py
infra/aws/ec2/opal-gateway/tests/test_list_email_filtered.py
infra/aws/ec2/opal-gateway/tests/test_inspect_email_attachment.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W15-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ml-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/ml1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)files absent 0 of 4; pytest rc=0; passed \d+ \(expected 24 or more\); failed/error 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ml-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/ml1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)REG 2 of 2; SCOPES same.*fields present 4 of 4; pypdf pins 1; LD-0613 changed since base \w+: 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the adopted behaviour, by the 3 f-branch test files plus `test_attachment_tools.py` (24 or more passed, none
  failed).
- `AC2`: both tools are read class; the scopes are unchanged; `read_email`'s `$select` carries the 4 C7 fields;
  `pypdf` is pinned once; LD-0613 is unchanged since the cut base; `test_ogz2_ac08` passes.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-ml-1.mail-tools-adopt.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once: the tips verified, the diff stat, the
count before and after, the pypdf version, the literal AC1-AC2 output, the commits and the rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~15, queue position 2 (after `OG-tx-1`). Supersedes branches f1-f3. The four origin branches stay as the
  laptop left them; whether to delete them is MSTR's call, not this cell's.
- The byte-returning `$value` read is `OG-hr-2`'s (the headless mail route), never an MCP tool.
- `<risk>` WORLD is GATE (xii)'s floor; the cell deploys nothing.

<status>staged</status>
<round>8</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
