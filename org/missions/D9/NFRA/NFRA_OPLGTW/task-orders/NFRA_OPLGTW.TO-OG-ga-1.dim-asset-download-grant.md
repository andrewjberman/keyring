# NFRA_OPLGTW task order -- `OG-ga-1` -- write `download_filtered` onto the one live dim_asset grant, then download as its holder

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ga-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~28</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one grant write and one read; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the write runs under the existing operator role opal-gateway-access-admin.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is Andrew's word (record org/tier1_exec/2.0.0_SA_COO~O/deliverables/ANDREW_DIRECT_20261006_181xZ_S41_DOWNLOAD_FILTERED_GRANT_YES.md @ca460bf9fe).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (DynamoDB, STS, SSM on the gateway host i-07dccb1615503ac99).
</preflight>

## 1. THE CELL -- `OG-ga-1` (decomposition addendum R3-T.15)

Andrew said yes to row `NFRA_OPLGTW-Z-W15-S41`. The gateway's state store `gateway-access-state-table` holds exactly ONE
principal whose grant in force names `dim_asset`. Its `scope.operations` is `describe, list, query`, so the guard refuses
that principal's `schwab_prepare_download` (`app/data_entitlement.py:69`, `:90`). Add `download_filtered` to it, change
nothing else, then prove it with one real download as that principal.

The writer is `infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py activate`. It is the ONLY writer of `POLICY#`
records. It validates the candidate, strongly reads the current grant, prints the scope diff, and writes the new revision
plus its `operator_audit` in one transaction. It runs only as the role `opal-gateway-access-admin`.

The instrument `G` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r22/checks/ga1_state.py`.
Your deliverables directory `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/`.
Off-repo directory `X` = `%LOCALAPPDATA%/opal/og-salt/ga1/`. Anything carrying a tid, oid, email or account id lives
only in `X`.

### PHASE A -- read-only

1. **Before-record.** Run `python G --before W/GA1_BEFORE.json`. It must print 1 in-force dim_asset grant and 0 carrying
   `download_filtered`. Any other count: STOP, file a BLOCKING row, and report.
2. **Operator identity.** Assume `opal-gateway-access-admin` with `aws sts assume-role`. Hold the credentials in the
   process environment only. Confirm `sts get-caller-identity` names that role. If the assume is refused, STOP, file a
   BLOCKING row naming the refusal, and report.
3. **Candidate.** Strongly read the holder's grant in force under the operator role. Write it into `X` as
   `candidate.json`, with `"download_filtered"` appended to `scope.operations` and every other field unchanged. Write the
   current scope unchanged as `X/rollback.json`, in the same candidate shape. The rollback is `activate` of that file:
   one more revision with the old operations. Use the candidate shape `activate --candidate` parses; the tests of
   `ops/schwab_entitlement_admin.py` show it.
   - **Diff without writing.** `activate` has no confirm prompt; it writes once validation passes. Import the module
     and call its `prepare(store, raw, load_contract(None), out=...)` in-process under the operator role. That prints
     the scope diff and writes nothing. The diff must change `operations` only, by `download_filtered` only. Any other
     change: STOP, file a BLOCKING row, and report. Save the diff to `X`, and put its line count and the changed-key
     list in `W/GA1_PREFLIGHT.md`.
4. **Download probe, staged.** Reuse the on-host tooling in
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/` (`rl5_ssm.py`, `rl5_host_prelude.py.txt`, the
   `RL6_DOWNLOAD` verify run). Change it so the principal is the REAL holder and the grant is read from the store
   through `app/data_entitlement`. There must be no synthetic principal and no in-memory grant.
   - Prefer the host resolving the holder itself. If the pk must be passed, pass it only in SSM parameters, never in a
     repo file or a printed line.
   - The host script prints one line `GA1_DIGEST <sha256>`. The digest is of
     `json.dumps(body, sort_keys=True).encode("utf-8")`, where `body` is the JSON object of step 8.
   - Run it once BEFORE the write. The download must be REFUSED by the entitlement guard (`ENTITLEMENT_DENIED`). Record
     the refusal line in `W/GA1_PREFLIGHT.md`.

### PHASE B -- the write (Andrew's word is the GO; there is no other gate)

5. Open the change-management ledger `nfra-oplgtw-ga1-grant-write`, with legs write, read-back and download. Commit the
   entry under `org/critical_paths/change_management/` and the sentinel
   `org/critical_paths/.open_deploys/nfra-oplgtw-ga1-grant-write.json` BEFORE the act.
6. Re-run step 1's read (`python G --before X/recheck.json`) and confirm the holder's revision is unchanged since
   Phase A. Then run `activate --candidate X/candidate.json` under the operator role:
   - `--approver "Andrew Berman"`;
   - `--source-authorization "org/tier1_exec/2.0.0_SA_COO~O/deliverables/ANDREW_DIRECT_20261006_181xZ_S41_DOWNLOAD_FILTERED_GRANT_YES.md@ca460bf9fe"`;
   - `--summary "S41: add download_filtered to the dim_asset grant"`.

   Save the full output to `X`. Record the `ACTIVATED profile_revision=... grant_revision=...` line, or the `REFUSED:`
   line, in `W/GA1_WRITE.md`. A `REFUSED: stale revision` means the record moved: re-cut Phase A once.
7. **Read-back.** Run `bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r22/checks/ga1.AC1.sh`.
   - On a FAIL, roll back immediately: `activate` `X/rollback.json` under the same role.
   - Re-run `python G --before X/after_rollback.json` and confirm the operations read as before.
   - Close the ledger ROLLED BACK and report.
8. **The real C3 download.** Run the step-4 probe AFTER the write, through SSM. Write `W/GA1_DOWNLOAD.json` as
   `{"body": {...}, "ssm_command_id": "<id>", "instance_id": "i-07dccb1615503ac99"}`. The body holds:
   - `synthetic_principal: false`, `grant_source: "store"`, `grants_written: 0` (the probe writes none);
   - `dim_asset_download`: `"OK"` or the refusal line;
   - `held_check: {returned, distinct_returned, held_cusips_in_dim_position, unheld_returned}`, as in `RL6_DOWNLOAD.r17.json`;
   - `master`, `date`, `granted_accounts` (a count only);
   - `served_release`: the host's deployed gateway commit.
9. Close every leg with proof, remove the sentinel, and commit.

## 2. BOUNDS

- **May change:** ONE new `data_entitlement` revision (plus the profile's `grant_revision` and one `operator_audit`
  record) for the one holder. If step 7 fails, also the one rollback revision.
- **Never:** any other principal's records, any other scope dimension, `download_original` or `write`, a gateway release,
  a host file, an IAM change. Never `aws dynamodb put-item`/`update-item` by hand; the admin command is the only writer.
- **Never** print or commit a tid, oid, email, account id or credential. Counts and sha256 digests only.
- **Never:** push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-ga1-grant-write.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W28-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ga-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r22/checks/ga1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)in-force active dim_asset grants 1; of them carrying download_filtered 1.*revision advanced True.*other dimensions unchanged True; other principals unchanged True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ga-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r22/checks/ga1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)held-only real-holder download: yes; ssm status Success; digest in host output: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ga-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r22/checks/ga1.AC3.sh; echo "exit=$?"</invocation><expect>(?s)entry files at HEAD=[1-9]\d*; sentinel at HEAD=no.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the store holds the one grant with `download_filtered` at a new revision, and nothing else moved.
- `AC2`: a real download as the holder returned held CUSIPs only, attested by the host's own SSM output.
- `AC3`: the ledger is closed.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ga-1.dim-asset-download-grant.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If all three criteria PASS, edit this order's ONE `<status>` tag IN PLACE to `complete`.
4. Report once: literal AC output, the pre-write refusal line, the ACTIVATED line, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 22 (addendum R3-T.15). R28 un-park event 1 (`ledger/ROUND_ANALYSIS.round21.md:32`). Andrew's word is the GO.
- Cell id: `OG-gr-*` is taken by the grain cells (OG-gr-1..3), so this cell is `OG-ga-1`.
- Never-widen (NEVER-1): NON-APPLICATION. The write set is a literal key list the actor controls (one principal's
  `POLICY#` partition: one grant revision, the profile, one audit record), and Andrew worded the exact widening. No
  halves are cut (CLAUDE.md "do not manufacture friction"). The change-management ledger is kept because the act moves
  live state.
- Pre-cut 18:4xZ: `ga1.AC1` FAIL (1 holder, 0 carrying download_filtered; no before-record). `ga1.AC2` FAIL (no
  download record). `ga1.AC3` FAIL (no ledger entry).
- Hazard carried: the post-act download is in-process on the host as the holder's principal key. It is not her own
  sign-in. That walk is OG-v-7's.

- CLOSE 19:1xZ (issuer re-grade @5d36cd195c): FAILED on AC2. AC1 PASS: grant_revision 2 -> 3, operations gain
  download_filtered only, other dimensions and principals unchanged. AC3 PASS: ledger nfra-oplgtw-ga1-grant-write
  closed. AC2 FAIL: the real-holder download is OK, 2173 rows, every held CUSIP present, 0 non-blank unheld, but 23
  blank-cusip rows pass because a blank is in the held set (integration.py:341). The query path has served the same
  rows since OG-q-7. Rows Z-W28-S1 and Z-S59 (disarmed, not resolved). The grant stays in force; reverting it removes no
  exposure. AC2 is not amended. The blank-cusip rule goes to the CTO at L10.

<status>failed</status>
<round>22</round>
<slot>~28</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
