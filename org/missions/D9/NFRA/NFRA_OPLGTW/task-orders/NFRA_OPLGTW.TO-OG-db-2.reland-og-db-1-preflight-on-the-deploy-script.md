# NFRA_OPLGTW task order -- `OG-db-2` -- re-land `OG-db-1`'s PREFLIGHT block on the deploy script that `OG-ap-33` landed from the live blob (round 40; CTO decision 35438, row Z-S356)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-db-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-db-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~133</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a text edit of one shell script in the repository; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM; the block runs no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's decision 35438 on row Z-S356: `OG-ap-33` landed the live `deploy-to-ec2.sh` WHOLE (it lacks trunk's `OG-db-1` preflight, which the live release never carried), and this cell re-lands that block so the trunk work is tracked and not dropped.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-db-2` (decomposition addendum R3-T.110, round 40, workstream ENRICH-R40-Q)

STARTS only from a worktree cut AFTER `OG-ap-33` is merged: the file `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` in your worktree is then the live blob (no `OG-db-1` preflight block). Read it whole first.

DO: insert into `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` the PREFLIGHT block exactly as trunk carries it at commit `33fb4d9708`: print it with `git show 33fb4d9708:infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` and take the lines from the line starting `# --- NFRA_OPLGTW OG-db-1` through the line `if [ "${1:-}" = "--preflight-only" ]; then echo "PREFLIGHT OK"; exit 0; fi` (17 lines when this order was cut), BYTE FOR BYTE, plus one blank line after it, immediately BEFORE the line starting `# --- NFRA_OPLGTW OG-tl-1` (the transcript-allowlist block). Change nothing else in the file: no deletion, no other insertion, no reformatting. Do not run the deploy script (it deploys); the criteria run only the extracted block.

## 2. BOUNDS

- Write only the files in `<paths>`. No deploy, no AWS call, no run of `deploy-to-ec2.sh` itself, no IAM, no registry change.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `deploy-to-ec2.sh` only; the rest you read. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~133/`. Rows: id `NFRA_OPLGTW-Z-W133-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-db-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/db2.AC1.sh 0.9.0_WK_NFRA_OPLGTW~133; echo "exit=$?"</invocation><expect>(?s)diff of the deploy script across the cell: 1 insertion\(s\), 0 other change\(s\) \(want 1 and 0\).*equal in order: yes; inserted before the OG-tl-1 block: yes.*bash -n on the post-cell file: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-db-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/db2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)preflight block extracted: yes \(\d+ lines\); runs alone on this repo: PREFLIGHT OK rc=0: yes; control \(empty root\) refuses: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-db-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~133 '^infra/aws/ec2/opal-gateway/deploy-to-ec2\.sh$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~133: files touched [1-9]\d*; product files 1; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the file differs from its pre-cell blob by ONE insertion (the trunk block, in order, before the allowlist block) and nothing else, and reads clean under `bash -n`. `AC2`: the extracted block runs alone, prints `PREFLIGHT OK` on this repo and refuses on an empty root. `AC3`: your commits touch only the deploy script (plus the standing record paths).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-db-2.reland-og-db-1-preflight-on-the-deploy-script.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hash, the AC lines).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 40, workstream ENRICH-R40-Q (decomposition addendum R3-T.110). Cut in the same issuance as `OG-ap-33` Amendment A2, per the CTO's decision 35438. Row `Z-S356` stays open until this cell lands. The block reaches the host only through the next release's never-widen (the deploy script is a gateway-tree file; a release that takes it names it in its ask).
- Spawn only after `OG-ap-33` merges: the pre-cell blob must be the live script. `risk` WORLD by the L6 floor (a gateway path); no deploy.
- Pre-cut: `db2.AC1` base FAIL as expected (no commit by the serial); dry-run on a temp repo with synthetic history: PASS arm; controls FAIL (the block twice; a live line deleted too; the block in the wrong place; the block altered). `db2.AC2` PASS on the post-cell script, FAIL on the live script (block absent), and its control (empty root) refuses. The AC2 check never runs the deploy script: it extracts the block into a temp file.

<status>complete</status>
<round>40</round>
<workstream>ENRICH-R40-Q</workstream>
<slot>~133</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
