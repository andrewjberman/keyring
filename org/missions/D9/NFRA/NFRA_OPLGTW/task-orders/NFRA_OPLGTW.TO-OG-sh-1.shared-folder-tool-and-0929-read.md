# NFRA_OPLGTW task order -- `OG-sh-1` -- the gateway `list_shared_folder(url)` tool, and the one 2026-09-29 request-log read for dell2 (E4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sh-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-sh-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~63</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code, tests and one read of a log already written; the tool reaches users only in a later gateway release under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change. The MASTER-tier token already carries Files.ReadWrite.All (infra/aws/ec2/opal-gateway/app/config.py:64, read by dell2 1.0.0_SA_CTO~DELL2); the tool is READ class and reaches only what is shared to the signed-in user.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-35 analysis E4 (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round35.md @682d1ced78), on Andrew's card 3 (dell2), row NFRA_TRNSPT-D2-S29, and the dell2-54ae ruling point 3.
EGRESS CLASS, declared: NONE beyond Opal's own AWS and Microsoft Graph under the user's own token.
</preflight>

## 1. THE CELL -- `OG-sh-1` (decomposition addendum R3-T.48, E4)

1. **The tool.** Add the gateway tool `list_shared_folder(url)`:
   - Encode the sharing URL as Graph's share id: `u!` + unpadded base64url of the URL.
   - Resolve `GET /shares/{share-id}/driveItem`. If it is a folder, list `.../driveItem/children` (name, id, size,
     lastModified, isFolder; follow `@odata.nextLink` with a cap). If it is a file, return its metadata.
   - Return a clear, distinguishable error for each step: resolve failed, versus children failed.
   - It is READ class. Register it the way the existing Graph tools are registered (read `app/tools.py`, near
     `read_teams_attachment`'s `/shares` resolver at about line 1206), and CLASSIFY it in `app/data_entitlement.py`. An
     unclassified tool is denied to everyone (`tool_unclassified`).
   - The existing resolver GETs `/content`, which a folder lacks, so its 404 on a folder link is ambiguous. Do not
     change that tool; the new tool is the folder path.
2. **Tests,** in `infra/aws/ec2/opal-gateway/tests/test_og_sh1.py`, with Graph stubbed:
   - `test_ogsh1_ac01`: the share id equals `u!` plus unpadded base64url for a sample URL, and a folder link lists its
     children through `/driveItem/children`.
   - `test_ogsh1_ac02`: the tool is classified READ, and a principal allowed READ tools may call it.
   - `test_ogsh1_ac03`: a 404 on resolve and a 404 on children return different, named errors.
3. **The one read (dell2-54ae ruling point 3).** One query of the gateway's request log for 2026-09-29, filtered on the
   2026-06-01 Monday meeting's id.
   - Resolve that meeting's id from NFRA_TRNSPT's own records. Start at
     `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R22_CENSUS_0929.json` and the round records beside
     it, and name the file and field you took it from.
   - Find the gateway's log group in `infra/aws/ec2/opal-gateway/`, then run ONE `filter-log-events` over that UTC day
     for the id.
   - Positive control: count any other tool call in the same group that day; it must be at least 1.
   - Verdict: `READ` (a successful fetch of that meeting), `REFUSED` (a refusal), or `NO_EVENT`.
   - Write `W/SH1_0929_READ.json` = `{"meeting_id", "meeting_id_source", "log_group", "day": "2026-09-29",
     "events_matched", "verdict", "positive_control_events", "lines": [<the matched lines' timestamps and status only>]}`.
   - If the id cannot be resolved, file a BLOCKING row and do not guess.
4. **Ask.** Write `W/NEVER_WIDEN_ASK_OG-sh-1.md` for the gateway release that ships the tool: its class, its reach (only
   what is shared to the signed-in user), the release, and the rollback (the prior release ref).

## 2. BOUNDS

- Code, tests, the one log read and the ask. No release, no deploy.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name, email, or meeting content (ids,
  timestamps and statuses only); override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/tests/test_og_sh1.py
infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py
infra/aws/ec2/opal-gateway/tests/test_data_entitlement_family.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~63/`. Rows: id `NFRA_OPLGTW-Z-W63-S<k>`, fabric
`site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sh-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r36/checks/sh1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*failing ids not in the baseline: 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-sh-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r36/checks/sh1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)meeting_id set \(source [^)]+\); log_group \S+; day 2026-09-29; events_matched \d+; verdict (READ|REFUSED|NO_EVENT); positive control [1-9]\d*.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the tool is built and classified, and nothing regresses. `AC2`: the one read is done, with a control.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-sh-1.shared-folder-tool-and-0929-read.proof_of_spec.json`. Validate it
after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip
the ONE `<status>` tag to `complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 36, E4. The read's result goes to dell2 `1.0.0_SA_CTO~DELL2` through MSTR (the issuer relays it).
- Pre-cut:
  - sh1.AC1 base FAIL as expected: the test file is absent; the baseline limb reads 0 new.
  - sh1.AC2 base FAIL as expected: the file is absent.
- bd-2 and sh-1 share `data_entitlement.py`, `server.py` and the two suites. Different hunks; the issuer merges in order
  bd-2 then sh-1.

<status>pending</status>
<round>36</round>
<slot>~63</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
