# NFRA_OPLGTW task order -- `OG-db-3` -- the deploy writes the release sha to `/opt/opal-gateway/.deployed_commit` (round 41; CTO round-40 analysis item 3; row Z-S354)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-db-3</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-db-3</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~136</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a text edit of one shell script and an offline test; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM; the written file lives in the service's own folder under the deploy user.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-40 analysis item 3 (`ledger/ROUND_ANALYSIS.round40.md` @66aeb73b0c: "the deploy-written /opt/opal-gateway/.deployed_commit marker; after deploy the marker equals the release sha") from the CTO's round-21 note that the host carries no such marker (row Z-S354).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-db-3` (decomposition addendum R3-T.111, round 41, workstream ENRICH-R41)

THE GAP. Release identity on the host is read today by the md5 of the served blobs, because no file on the host names the release. `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` already holds the release sha locally (`FULL_SHA="$(git -C "$WORKSPACE_ROOT" rev-parse HEAD)"`, about line 230, with the short form `SHA`) and builds the remote install script as one unquoted heredoc (so `${...}` expands locally and `\$...` expands on the host; `REMOTE_DIR` is `/opt/opal-gateway`). Read the whole script first; `OG-db-2` has merged the `OG-db-1` preflight into it.

THE FIX (one line plus its comment; the file is `deploy-to-ec2.sh` only):
1. In the remote install section, immediately AFTER the line `sudo -u ec2-user tar -xzf /tmp/${ART} -C ${REMOTE_DIR}` (about line 362 in the unmodified file) and BEFORE the `systemctl restart`, add ONE line that writes the release sha to the marker: `printf '%s\n' "${FULL_SHA}" | sudo -u ec2-user tee ${REMOTE_DIR}/.deployed_commit >/dev/null`, preceded by a one-line comment naming `OG-db-3`, the CTO's round-40 item 3 and row Z-S354. The file holds the 40-character sha and a newline, nothing else.
2. Change nothing else in the script (no other line, no reformatting). Do not run `deploy-to-ec2.sh` (it deploys).

TESTS (new file `tests/test_og_db3.py`; no AWS, no network; read the script as text):
- `test_ogdb3_ac01`: the script text contains exactly ONE write to `.deployed_commit`; it uses `${FULL_SHA}`; it sits after the `tar -xzf` line and before the first `systemctl restart` line of the remote section; and `bash -n` reads the whole script clean.
- `test_ogdb3_ac02`: run that one marker line (extracted from the script text) in a `bash -c` with `REMOTE_DIR` set to a temp folder, `FULL_SHA` set to a 40-hex sample, and a shell function that stands in for `sudo` (`sudo() { if [ "$1" = "-u" ]; then shift 2; fi; "$@"; }`): the temp folder then holds `.deployed_commit` whose content is exactly the sample sha plus a newline.
- `test_ogdb3_ac03`: the rest of the script is unchanged: `git diff` of the file between the parent of your first commit and HEAD shows exactly one inserted code line and its comment, no deleted line (read both blobs with `git show`).

## 2. BOUNDS

- Write only the files in `<paths>`. No deploy, no AWS call, no run of `deploy-to-ec2.sh` itself, no IAM, no registry change.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/opal-gateway/tests/test_og_db3.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `deploy-to-ec2.sh` and `tests/test_og_db3.py`; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~136/`. Rows: id `NFRA_OPLGTW-Z-W136-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-db-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_db3.py test_ogdb3_ac01 test_ogdb3_ac02 test_ogdb3_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-db-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~136 '^infra/aws/ec2/opal-gateway/(deploy-to-ec2\.sh|tests/test_og_db3\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~136: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass (one marker write, in the right place, writing the sha; the rest of the script unchanged). `AC2`: the commits of this serial touch only the listed files.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-db-3.deploy-writes-the-release-sha-marker.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the AC lines).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 41, workstream ENRICH-R41 (decomposition addendum R3-T.111), cell 3 of the CTO's round-40 analysis. Risk WORLD by the L6 floor (a gateway path); no deploy in this cell. It rides the same batched release as `OG-en-21`; that release's ask names the deploy script in its diff and its Phase B reads the marker on the host (CTO criterion: after deploy, the marker equals the release sha).
- Disjoint from `OG-en-21` and `OG-en-22` (they touch `app/` only).
- The marker sits at the REMOTE_DIR root, outside `app/`, `deploy/`, `dashboard/` and `lib/`, so the release's md5 walk is not affected.
- Pre-cut: `AC1` base FAIL as expected (the test file is absent).

<status>staged</status>
<round>41</round>
<workstream>ENRICH-R41</workstream>
<slot>~136</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
