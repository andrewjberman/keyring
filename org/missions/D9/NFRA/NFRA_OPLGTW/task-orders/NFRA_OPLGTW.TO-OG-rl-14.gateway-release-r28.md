# NFRA_OPLGTW task order -- `OG-rl-14` -- the r28 release on live r27 (510c8cfed2): the audit-lake key stamp (OG-lk-1), deployed by the script that cannot fetch (OG-bi-1, bi-2, bi-3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-14</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~28</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the cells are the CTO's rulings R39, R40, R43 and R46 (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round27.md @f6fd7281cf).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM) and the public gateway URL. NO package, script or program is fetched from the internet by this box; see section 1, THE INSTALL LINES.
</preflight>

## 1. THE CELL -- `OG-rl-14` (decomposition addendum R3-T.26, item 2)

Handed only after `OG-bi-3` is complete and drained. FOLLOW
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md` IN FULL: Phase A steps 1-8 (7a does
not apply: no tool and no route is added or removed), Phase B 9-12, Phase D 13. Reuse the `r27_*` tooling in
`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/`; copy to `r28_` names. First bring your
branch level with CLOUD by a plain merge of the CLOUD commit the issuer names at the hand-off (no rebase).

- **Live:** `510c8cfed2c852946e3e57fb4dd1c0467e2f3a52` (r27). Re-read it by host md5 first. If the manifest names
  another sha, STOP and report.
- **Ledger:** `nfra-oplgtw-gateway-release-r28`.
- **Release branch** `rel-nfra-oplgtw-r28`, a NEW worktree `/c/tmp/og-rel23` at the live sha. **Rollback tree:** a NEW
  `/c/tmp/og-rb22` at the live sha, proven against the live S3 artifact.
- **The release set:** every gateway difference between live and CLOUD at the hand-off, except the CLOUD-only
  `runbooks/SCHWAB_PILOT_RUNBOOK.md`. Expected:
  - `app/audit.py` (ships): the lake key builder `_lake_key` (OG-lk-1);
  - `deploy-to-ec2.sh` (the deploy tool): the pre-check before the dashboard install; the host's `--upgrade pip`
    line removed (OG-bi-1, OG-bi-2);
  - `ops/bun_cache_precheck.py` (the deploy tool's pre-check, as OG-bi-3 leaves it);
  - four source-only tests: `tests/test_audit_lake_key_stamp.py`, `tests/test_deploy_install_no_fetch.py`,
    `tests/test_deploy_install_no_fetch_complete.py`, `tests/test_deploy_host_pip_no_upgrade.py`.
  - State for each of the three non-test files whether it reaches the host, from the host md5 list, not from its path.
  - If CLOUD carries any OTHER gateway difference, STOP before the release commit and report its files and commits.
  - **If the diff touches `requirements.txt` or `bun.lock`, STOP and report:** such a release goes to the CTO first.
- **Served output moves one way.** A lake object written for a record that carries no `ts` gets a key with a time part.
  No record's fields change; a record with `ts` keeps its key. Rollback per key: redeploying live `510c8cfed2` restores
  the old builder; keys already written stay as written.

**THE INSTALL LINES (rulings R39, R40, R45; the form's "deploy script's install lines").** This is the FIRST deploy
under the pre-check, and it carries its own control.
- The deploy runs from the release tree, whose `deploy-to-ec2.sh` is the changed script. Before Phase B, run the
  pre-check by hand against the dashboard lockfile and the real cache and record `<present> of <total>`. Anything
  missing: STOP, report the list. It goes to the laptop's package intake; nothing is fetched here.
- **R45, the control.** Record the time the deploy command starts. After the deploy returns, count the entries of
  bun's install cache (top level and one level down) whose creation time OR modified time is at or after that start.
  Write `W/RL14_BUN_CACHE.json`: `deploy_started_utc`, `entries_counted`, `entries_touched_since_start`.
  **It must be 0.** Above 0 is a fetch: do NOT run the criteria, file a BLOCKING row, roll back, and report.
- The ANNOUNCE states in one line that whether a frozen install with every entry cached sends a metadata request is
  UNDETERMINED, or cites `deliverables/0.9.0_WK_NFRA_OPLGTW~33/BI3_METADATA.md` if that file decides it.
- The host step still runs `pip install -r requirements.txt`. From the deploy output, record the counts of lines
  reading `already satisfied`, `Collecting` and `Downloading`. A `Collecting` or `Downloading` line is reported to the
  issuer as a finding; it is not a rollback trigger.
- Run no other install, and no `bun` command of your own.

**BEFORE and REHEARSAL (form step 5), host runs strictly one at a time, each in its own scratch directory.** Never
write to the audit lake: call the key builder directly, or give `_emit` a fake S3 client.
- BEFORE, on the installed code: the key built for a record with no `ts` has an EMPTY time part.
- REHEARSAL, on the staged release bytes: the same record's key has a non-empty time part, and its day equals that
  time's day; a record with `ts` gets `audit/dt=<day>/<ts>-<id>.jsonl` as before; the record passed in is unchanged;
  tools 66; the scoped concierge's consent 9.
- No principal identifier is needed by this order. Do not read one. The sign-in cache is never read.

**The post-deploy read, IMMEDIATELY after the verify script, through the INSTALLED code.** Write `W/RL14_READ.json` as
`{"body": {...}, "ssm_command_id", "instance_id"}`. The host prints `RL14_DIGEST <sha256>` of
`json.dumps(body, sort_keys=True)`. Body fields, exactly: `served_release`, `installed_code: true`, `tools`,
`scoped_scope_count`, `lake_key_no_ts_time_part_empty` (false expected), `lake_key_no_ts_day_matches_time`,
`lake_key_with_ts_shape_unchanged`, `records_changed_by_key_builder` (a count), `lake_objects_written: 0`,
`grants_written: 0`.
Also re-read the standing floor into `W/RL14_FLOOR.json`: the portal login OK, the real holder on both paths, the two
refused ids making 0 requests, the status tool's `displayed_date` equal to the manifest's `generated_at`, the four
route arms, and the rivalfunds pages by the page-time read of the form (BEFORE and AFTER in the deploy window, each
with `LastModified`). Then the audit-lake read: the first `rivalfunds_view` record written after the r27 deploy
(2026-10-07T16:57:30Z), as `lake_record` (kept arg NAMES, whether `bytes` is present, write time) or `none yet`.
- **Rollback triggers:** `entries_touched_since_start` above 0; the key for a no-`ts` record still empty in its time
  part; a record changed by the builder; a rivalfunds page changing with `LastModified` unmoved; an arg other than
  `day`, `route`, `fund` kept in a rivalfunds record; the status tool failing on a well-formed id; a refused id
  making a request; tools off 66; consent off 9; a floor read off its bar.

**AMENDED A1 (after Phase A; rows Z-W28-S27 to S30).**
- **RE-CUT.** The release set gains `tests/test_deploy_base_guard.py` (cell `OG-bi-4`, source only): on the release tree
  cut in Phase A three of its tests failed, because its rig carried no lockfile. Cut a NEW branch
  `rel-nfra-oplgtw-r28b` in a NEW worktree `/c/tmp/og-rel24` at live `510c8cfed2`, ONE commit carrying the 8 files
  (as r23b was cut). Leave `rel-nfra-oplgtw-r28` and `/c/tmp/og-rel23` untouched: delete nothing, move no head. Then re-run form steps 2, 3 and 7 on the NEW sha, and
  re-read steps 1 and 4. The Phase A rehearsal (step 5) and verify-script exercise (step 6) stand: the one file that
  reaches the host, `app/audit.py`, is byte-equal in both commits, and you prove that by blob.
- **`rl14.AC1.sh` is amended by the issuer** (row S28): `deploy-to-ec2.sh` and `ops/` are no longer counted as host
  files. Its expected-PASS form now reads `1 of 1`. Run it again in step 7.
- **The floor's real-holder read stands** (row S29). It uses the issuer's off-repo file
  `%LOCALAPPDATA%/opal/og-salt/ga1/holder_pks.json`, passed inside the SSM parameters, as in every release since r23.
  "No principal identifier is needed by this order. Do not read one." means: read none from any OTHER source, and
  never the sign-in cache.
- **The audit-lake read is DROPPED from Phase B** (row S30). Phase A's read already found it: the first
  `rivalfunds_view` record after the r27 deploy was written 2026-10-07T18:55:34Z and keeps `day` and `route`, with
  `bytes` present and 0 other args (`W/r28_lake_read.stdout`). Write that into `W/RL14_FLOOR.json` as `lake_record`,
  citing that file; make no lake list or read in Phase B.

**AMENDED A2 (the CTO half on r28, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_NFRA_OPLGTW_OG-rl-14_GATEWAY_R28_20261007.md`
@8614c48050, conditions C1 and C2).**
- **The cache's size, beside the count (C1).** Immediately BEFORE the deploy command starts, and again right after it
  returns, read the total size in bytes of bun's install cache (every file, to full depth) and the number of files.
  Add to `W/RL14_BUN_CACHE.json`: `bytes_before`, `bytes_after`, `files_before`, `files_after`. Equal bytes, equal
  files and a count of 0 mean no package was written. **A difference in bytes or files is treated exactly as a count
  above 0:** do not run the criteria, file a BLOCKING row naming what differs, roll back, report.
- **The build's own log (C1).** `bun run build` runs after the install. Read the deploy output between the
  `building mcportal` line and the build's end for any line that reports a download or a fetch, and record
  `build_log_download_lines` (a count, and the lines if any) in the same file. Above 0 is reported to the issuer in
  your final message as a finding.
- **The host's pip step (C2).** Record in `W/RL14_FLOOR.json` as `host_pip`: the counts of deploy-output lines reading
  `already satisfied`, `Collecting` and `Downloading`, and for any `Collecting` or `Downloading` line the PACKAGE
  NAME. That is a finding the issuer takes to the CTO the same hour. It is not a rollback trigger.

**THE MANIFEST'S `release_note`** holds this release's note only (the form's manifest-note rule).

**TIMING.** This release does not touch the send path's file (`app/integrations/opal_portal/integration.py`), so the
timing rule does not bind. State in the ANNOUNCE that you checked the release's file list for it.

**ONE STOP for the halves.** Run Phase A, write `W/ANNOUNCE_OG-rl-14.md`, commit and report. Phase B starts on the
issuer's GO, with CTO + COO + CVO halves SIGNED on the release sha. The CTO half names the script that runs and its
install lines, so the ANNOUNCE quotes the changed script's install and pre-check lines with their line numbers.

## 2. BOUNDS

- No grant or state-store write. No `.env`, secret, Terraform or IAM write. No S3 object written other than the
  release artifact the deploy wrapper uploads. No object written to the audit lake.
- Never run `opal_data_refresh_upload` with `confirm=True`, and never POST `/trigger`.
- No `/login` for the concierge. Never read the gateway's sign-in cache.
- Never print or commit a tid, oid, client account id, credential, token or execution id; never print an email address
  to a log or a record.
- Host runs one at a time: never start a second SSM run before the first returns.
- Fetch nothing from the internet. Never: push, `git stash`, rebase, `checkout --`, `clean`, `FORCE_HEADMOVE`; call a
  vendor. R13 (a) applies on the release branch only.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-r28.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/LINEAGE_R18.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`infra/aws/ec2/opal-gateway/` is written ONLY by the Phase D drain-back merge of the release branch, never edited.

Rows: id `NFRA_OPLGTW-Z-W28-S<k>` (next unused; S26 is the last used), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root, ONE AFTER THE OTHER, after the drain-back and ledger close are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-14"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r29/checks/rl14.AC1.sh; echo "exit=$?"</invocation><expect>(?s)descends from 510c8cfed2=yes; host shipped files equal the release bytes: (\d+) of \1.*sentinel at HEAD=no; gateway files differing live\.\.CLOUD after drain-back \(CLOUD-only runbook excluded\) 0.*floor: rl4.AC1 yes; ht.AC2 yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-14"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r29/checks/rl14.AC2.sh; echo "exit=$?"</invocation><expect>(?s)audit-lake key stamp on the served release: fields=yes ssm=Success digest=yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the release is live, the ledger is closed, CLOUD equals live, and the floor holds.
- `AC2`: the served gateway's key builder stamps a record that has no time, and changes nothing else.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rl-14.gateway-release-r28.proof_of_spec.json` and validate it with
`python .tools/proof-of-spec-check.py <instance>`. Flip the ONE `<status>` tag to `complete` only if both PASS. Report
once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 29 (R3-T.26, item 2). It deploys row Z-W28-S26's key fix and is the first deploy under the pre-check (R45).
- `rl14.AC1` is `rl13.AC1` with the slug and the live sha moved. It counts host files as every release file outside
  `runbooks/` and `tests/`: if `deploy-to-ec2.sh` or `ops/bun_cache_precheck.py` does not reach the host, the check's
  `eq of n` will not match and the issuer amends the script's filter BEFORE the GO (form step 7).
- `rl14.AC2` reads `RL14_READ.json` through `rl14_attest.py`, the r27 instrument with one new field rule.
- OWED BY THE ISSUER, carried: the content-hash read at the first real send (CTO half on r26, C1).
- AMENDMENT 1 (20:5xZ, issuer, after Phase A and before any GO): the release is re-cut to carry `OG-bi-4`
  (row Z-W28-S27); `rl14.AC1.sh`'s host filter drops the deploy tool's files (row S28; the criterion's `<expect>` is
  unchanged, the script's count changes from `1 of 3` to `1 of 1`); the real-holder sentence is clarified (S29); the
  lake read leaves Phase B because Phase A found the record (S30). Gate: LIMB 6 does not grade a modification; GATE
  (viii) reads placeholders NONE.
- AMENDMENT 2 (21:3xZ, issuer, before any GO): the CTO half's C1 (the cache's total bytes and file count before and
  after, a difference treated as a fetch; the build log read for a download) and C2 (the host pip step's counts and
  package names, a finding and not a trigger). No criterion changed. Gate: LIMB 6 does not grade a modification; GATE
  (viii) reads placeholders NONE.
- Pre-cut 18:5xZ: see the issuance commit.

<status>complete</status>
<round>29</round>
<slot>~28</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
