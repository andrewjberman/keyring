# NFRA_OPLGTW task order -- `OG-ap-49` -- APPLY (repository only): land the live gateway release of `OG-ap-48` on the sitez trunk lineage, in the shape of `OG-ap-47` (round 45; round-44 analysis item 4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-49</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-49</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a repository merge; no schedule, trigger or deploy is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, no Terraform; the merge changes no gateway byte that is not already live.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-44 analysis, list item 4: "land OG-ap-48's release on box/sitez, in the shape of OG-ap-47". The released bytes are already live.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ap-49` (decomposition addendum R3-T.122, round 45, workstream ENRICH-R45-C)

**METHOD = `OG-ap-47`'s, read in `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-ap-47.round-44-land-the-eleventh-release-on-the-sitez-lineage.md` (through it `OG-ap-45`'s) and followed step by step; this order states only what differs.** Its check scripts are `ap49.AC1.sh` to `ap49.AC3.sh` in `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r45/checks/` (the `ap47` ones re-pointed at `ap49_landing.json`; they grade through `_ap43_check.py` in the same folder).

CONTEXT. `OG-ap-48` (ledger `nfra-oplgtw-gateway-release-batch13`) is STAGED behind its own gates; when its ledger is CLOSED the release is live on the host and its commit is NOT an ancestor of `box/sitez` (the release branch `rel-nfra-oplgtw-batch13` is cut from the live ref and takes its two files whole from trunk). This order lands it the way `OG-ap-47` landed the eleventh release: ONE merge of the release commit onto the `box/sitez` head. If the merge-tree at the GO shows a conflicted path, the rule of `OG-ap-45` applies (trunk's side on a gateway path; any non-gateway conflicted path is a STOP and a BLOCKING row).

START ONLY on the issuer's GO, which names `trunk_base_sha` (the `box/sitez` HEAD at the GO), `dell_sha` (here the commit to merge: the `release_sha` of `OG-ap-48`, site Z's own release; the field keeps the name `dell_sha` because the check reads it) and `manifest_sha` (your own Phase B manifest commit for `OG-ap-48`, an ancestor of trunk).

DO, in your own worktree (`C:/tmp/og-land-s49`, branch `land-sitez-rel-nfra1-49`, created from `trunk_base_sha`; a sparse cone holding every path in `<paths>` and the gateway folder):
1. `git merge-tree --write-tree --name-only trunk_base_sha dell_sha` lists the conflicted paths: print your count as the denominator. Merge `dell_sha` into the branch with `.tools/safe-merge.sh` (never rebase, never `git stash`).
2. Resolve exactly as `OG-ap-45`. The manifest block `services.opal-gateway` takes the pair `expected_deployed_commit` = the release sha of `OG-ap-48` and `expected_previous_commit` = the live ref `OG-ap-48` was cut on (`e09c30c3f0...` unless the host read another); nothing else in `EC2_MANIFEST.json` moves.
3. Write `W/ap49_landing.json` = `{"trunk_base_sha", "dell_sha", "merge_sha", "manifest_source": "dell1_commit", "manifest_sha", "expected_deployed_commit", "expected_previous_commit", "live_sha": "<the release sha of OG-ap-48>", "trunk_own_changes": [{"path": "infra/aws/ec2/opal-gateway/app/<file>.py", "why": "<the cell or commit that put this change on trunk>"}]}` (40-character shas; the field `manifest_source` keeps the value `dell1_commit` because the check reads it). `ap49.AC3` compares the gateway `app/` of the merge with `live_sha` and prints each file that is code-different or on one side only; list every one with its owner (expected after `OG-ap-48`: `admin_people_access.py` (`MP-pd-3`) while its owner has not said yes, and `destructive_ops.py`'s position-only difference (`OG-gt-11`)). Commit the record and run the criteria (AC1 to AC4). Do NOT push: I drain the branch to `box/sitez` and `0.0.0_AB_MSTR~Z` carries it to origin.

## 2. BOUNDS

- Only the paths in `<paths>`. No deploy, no Terraform, no IAM, no push, no gateway byte changed beyond what the two sides already hold, no object or item written to any bucket or table.
- Never: `git stash`, rebase, `checkout --`, `clean`, `HALT_OVERRIDE`; print a credential or an account number.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and stop.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/app/
infra/aws/ec2/opal-gateway/tests/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The tree convention grants `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-49"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r45/checks/ap49.AC1.sh; echo "exit=$?"</invocation><expect>(?s)merge parents are exactly trunk_base and the dell1 commit: yes; dell1's release is an ancestor of the merge: yes; conflicted paths \(merge-tree, the denominator\): (\d+); conflict markers in 0 of \1 paths \(want 0\).*terraform files differing 0 \(want 0\); paths outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-49"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r45/checks/ap49.AC2.sh; echo "exit=$?"</invocation><expect>(?s)manifest opal-gateway deployed_commit [0-9a-f]{10} previous [0-9a-f]{10} \(want [0-9a-f]{10} and [0-9a-f]{10}\): yes.*other services and the top level unchanged from trunk_base: yes; the gateway block's other keys unchanged: yes.*manifest source: dell1's own commit [0-9a-f]{10} \(an ancestor of the merge\): yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ap-49"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r45/checks/ap49.AC3.sh; echo "exit=$?"</invocation><expect>(?s)app/ python files compared live [0-9a-f]{10} against the merge: \d+; equal \d+; docstring-only differences \d+; code-different \d+; present on one side only \d+.*unlisted 0 \(want 0\); tools\.py code-equal to live: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="OG-ap-49"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh land49set tests/test_og_en13.py tests/test_og_en15.py tests/test_og_en17.py tests/test_og_en18.py tests/test_og_en19.py tests/test_og_en20.py tests/test_og_en21.py tests/test_og_en22.py tests/test_og_en23.py tests/test_og_en24.py tests/test_og_cl2.py tests/test_og_rv2.py tests/test_og_db3.py tests/test_og_en9.py tests/test_og_sv2.py tests/test_og_pr1.py tests/test_og_pr5.py tests/test_og_sec2.py tests/test_og_cd1.py tests/test_og_pr6.py; echo "exit=$?"</invocation><expect>(?s)land49set forward: passed (\d+); failed 0.*land49set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a true merge of the live release on the trunk head, no conflict marker, no Terraform or non-gateway byte changed. `AC2`: the manifest block names the release as live with the previous live ref as previous, from your own commit, and nothing else in it moved. `AC3`: the gateway `app/` is AST-equal to the LIVE release plus trunk's own changes, each listed with its owner. `AC4`: the window test files plus `test_og_cd1.py` and `test_og_pr6.py` pass together in both orders with the same count (the script keeps the forward text; if it prints `NO PASS LINE`, report the saved path).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-49.round-45-land-the-twelfth-release-on-the-sitez-lineage.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4 --governing-order <this order>` (the instance carries ALL FOUR criteria rows; `python3`, not `python`: ruling msg 35901), flip NOTHING (the `<status>` flip is mine), and report once (the merge sha, the conflicted-path denominator, the AC lines, the listed trunk changes with owners, the push state as a measured `ls-remote` value).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 45, workstream ENRICH-R45-C. Source: the CTO's round-44 analysis (`ledger/ROUND_ANALYSIS.round44.md` @ebefeda213, msg 35898), list item 4: "land OG-ap-48's release on box/sitez, in the shape of OG-ap-47. Then 0.0.0_AB_MSTR~Z tells dell1 the new live ref."
- Differs from `OG-ap-47`: the commit merged is `OG-ap-48`'s release; `AC4` adds `tests/test_og_pr6.py`; the record field names are kept so the same graders run.
- Pre-cut: `ap49.AC1` to `AC3` base FAIL as expected (the record is absent); `AC4` cannot be run before `OG-ap-48` exists.

<status>staged</status>
<status>complete</status>
<round>45</round>
<workstream>ENRICH-R45-C</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
