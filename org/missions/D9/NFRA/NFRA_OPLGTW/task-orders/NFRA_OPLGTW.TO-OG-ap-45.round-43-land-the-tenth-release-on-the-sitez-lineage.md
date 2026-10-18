# NFRA_OPLGTW task order -- `OG-ap-45` -- APPLY (repository only): land the live gateway release `eff517546e` (OG-ap-44, the access-log repair) on the sitez trunk lineage, in the shape of `OG-ap-43` (the CTO's ask, msg 35792)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-45</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-45</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a repository merge; no schedule, trigger or deploy is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, no Terraform; the merge changes no gateway byte that is not already live.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ask (msg 35792): land the live release on `box/sitez` the way `OG-ap-41` and `OG-ap-43` landed the earlier ones. The released bytes are already live.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ap-45` (decomposition addendum R3-T.120 amendment A2, round 43, workstream ENRICH-R43-D)

**METHOD = `OG-ap-43`'s, read in `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-ap-43.round-43-land-the-live-releases-on-the-sitez-lineage.md` and followed step by step; this order states only what differs.** Its check scripts are `ap45.AC1.sh` to `ap45.AC3.sh` (the `ap43` ones re-pointed at `ap45_landing.json`; they grade through `r43/checks/_ap43_check.py`, the repaired script `a24674dd4d`).

CONTEXT. `eff517546eeea48811cf13f3de38926c5944c6df` (`OG-ap-44`, ledger `batch11` CLOSED 2026-10-18T20:01:40Z) is live on the host, on `a0c83303ee` (`OG-ap-42`) on dell1's `922ee425fe`. `922ee425fe` and its ancestors are already on `box/sitez` (`OG-ap-43`, merge `b1e92a9635`); `a0c83303ee` and `eff517546e` are NOT (the CTO measured it by `merge-base`, msg 35792; the manifest commit `6a813efe70` is). The issuer's `git merge-tree --write-tree HEAD eff517546e` at the cut reads CLEAN (no conflicted path): the release's four files are blob-equal to trunk's. ONE merge of `eff517546e` lands the whole chain (`a0c83303ee` and `eff517546e`, 2 commits).

START ONLY on the issuer's GO, which names `trunk_base_sha` (the `box/sitez` HEAD at the GO), `dell_sha` (here the commit to merge: `eff517546eeea48811cf13f3de38926c5944c6df`, site Z's own release; the field keeps the name `dell_sha` because the check reads it) and `manifest_sha` (the applier's own Phase B manifest commit `6a813efe70`, an ancestor of trunk).

DO, in your own worktree (`C:/tmp/og-land-s45`, branch `land-sitez-rel-nfra1-45`, created from `trunk_base_sha`; a sparse cone holding every path in `<paths>` and the gateway folder):
1. `git merge-tree --write-tree --name-only trunk_base_sha dell_sha` lists the conflicted paths: print your count as the denominator (the issuer read 0). Merge `dell_sha` into the branch with `.tools/safe-merge.sh` (never rebase, never `git stash`).
2. Resolve exactly: EVERY conflicted GATEWAY path takes TRUNK's side (dell1's harvest paths are already on trunk byte-equal, so none should conflict; if one does, print both blob ids and take trunk's). Any conflicted path that is not a gateway path under `infra/aws/ec2/opal-gateway/`: STOP, file a BLOCKING row naming it, create no merge commit. The manifest block `services.opal-gateway` takes the pair `expected_deployed_commit` = `eff517546eeea48811cf13f3de38926c5944c6df`, `expected_previous_commit` = `a0c83303ee48c95c16a61c0d5e8bd186b1083b66` (your own Phase B manifest commit `6a813efe70` is the source); nothing else in `EC2_MANIFEST.json` moves.
3. Write `W/ap45_landing.json` = `{"trunk_base_sha", "dell_sha", "merge_sha", "manifest_source": "dell1_commit", "manifest_sha", "expected_deployed_commit", "expected_previous_commit", "live_sha": "eff517546eeea48811cf13f3de38926c5944c6df", "trunk_own_changes": [{"path": "infra/aws/ec2/opal-gateway/app/<file>.py", "why": "<the cell or commit that put this change on trunk>"}]}` (40-character shas; `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`; the field `manifest_source` keeps the value `dell1_commit` because the check reads it, here the source is your own commit). `ap45.AC3` compares the gateway `app/` of the merge with `live_sha` and prints each file that is code-different or on one side only; list every one with its owner. Commit the record and run the criteria (AC1 to AC4). Do NOT push: I drain the branch to `box/sitez` and `0.0.0_AB_MSTR~Z` carries it to origin.

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

The tree convention grants `W`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-45"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/ap45.AC1.sh; echo "exit=$?"</invocation><expect>(?s)merge parents are exactly trunk_base and the dell1 commit: yes; dell1's release is an ancestor of the merge: yes; conflicted paths \(merge-tree, the denominator\): (\d+); conflict markers in 0 of \1 paths \(want 0\).*terraform files differing 0 \(want 0\); paths outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-45"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/ap45.AC2.sh; echo "exit=$?"</invocation><expect>(?s)manifest opal-gateway deployed_commit [0-9a-f]{10} previous [0-9a-f]{10} \(want [0-9a-f]{10} and [0-9a-f]{10}\): yes.*other services and the top level unchanged from trunk_base: yes; the gateway block's other keys unchanged: yes.*manifest source: dell1's own commit [0-9a-f]{10} \(an ancestor of the merge\): yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ap-45"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/ap45.AC3.sh; echo "exit=$?"</invocation><expect>(?s)app/ python files compared live [0-9a-f]{10} against the merge: \d+; equal \d+; docstring-only differences \d+; code-different \d+; present on one side only \d+.*unlisted 0 \(want 0\); tools\.py code-equal to live: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="OG-ap-45"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh land45set tests/test_og_en13.py tests/test_og_en15.py tests/test_og_en17.py tests/test_og_en18.py tests/test_og_en19.py tests/test_og_en20.py tests/test_og_en21.py tests/test_og_en22.py tests/test_og_en23.py tests/test_og_en24.py tests/test_og_cl2.py tests/test_og_rv2.py tests/test_og_db3.py tests/test_og_en9.py tests/test_og_sv2.py tests/test_og_pr1.py tests/test_og_pr5.py tests/test_og_sec2.py; echo "exit=$?"</invocation><expect>(?s)land45set forward: passed (\d+); failed 0.*land45set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a true merge of the live release on the trunk head, no conflict marker, no Terraform or non-gateway byte changed. `AC2`: the manifest block names `eff517546e` as live with `a0c83303ee` as previous, from your own commit, and nothing else in it moved. `AC3` (the CTO's criterion): the gateway `app/` is AST-equal to the LIVE release plus trunk's own changes, each listed with its owner. `AC4`: the window test files (the eighteen named, including `test_og_pr5.py` and `test_og_sec2.py`) pass together in both orders with the same count.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-45.round-43-land-the-tenth-release-on-the-sitez-lineage.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4 --governing-order <this order>` (the instance carries ALL FOUR criteria rows), flip NOTHING (the `<status>` flip is mine), and report once (the merge sha, the conflicted-path denominator, the AC lines, the listed trunk changes with owners, the push state as a measured `ls-remote` value).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 43, workstream ENRICH-R43-D (a fourth issuance in round 43; decomposition addendum R3-T.120 amendment A2). Source: the CTO's msg 35792 (his `OG-ap-44` half record): "`eff517546e` is not an ancestor of `box/sitez`; land it the way `OG-ap-41`/`OG-ap-43` landed the earlier releases."
- Differs from `OG-ap-43`: no dell1 side on any conflict (dell1's files are already on trunk, byte-equal), the commit merged is site Z's own release, and the manifest source is the applier's own Phase B commit; the check's `dell_sha` and `manifest_source` field names are kept so the same script grades it.
- Pre-cut: `ap45.AC1` and `AC2` base FAIL as expected (the record is absent); the synthetic dry-run on a plumbing merge (parents trunk and `eff517546e`, trunk's tree) passes `AC1` and `AC2`.

<status>staged</status>
<status>complete</status>
<round>43</round>
<workstream>ENRICH-R43-D</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
