# NFRA_OPLGTW task order -- `OG-ap-43` -- APPLY (repository only): land the live gateway releases `3b94a83e05` (OG-ap-40) and dell1's `6575999df5` on the sitez trunk lineage, in the shape of `OG-ap-41`

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-43</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-43</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a repository merge; no schedule, trigger or deploy is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, no Terraform; the merge changes no gateway byte that is not already live.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-42 analysis item 8, in the shape of `OG-ap-41` (dell1 CTO ruling via `0.0.0_AB_MSTR~Z`: site Z lands its releases on its own lineage first and resolves its own conflicts; `0.0.0_AB_MSTR~Z` then tells dell1, which may cut from trunk again).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ap-43` (decomposition addendum R3-T.120, round 43, workstream ENRICH-R43-A)

**METHOD = `OG-ap-41`'s, AS AMENDED (A1), read in `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-ap-41.round-42-land-site-z-releases-on-the-sitez-lineage.md` and followed step by step; this order states only what differs.**

CONTEXT. `3b94a83e05` (OG-ap-40, ledger `batch9` CLOSED 2026-10-18T10:31:55Z) and `6575999df5d22c0123abfc0c88cd1c6f1efe8c96` (dell1's harvest release, deployed 10:52:49Z; parent `3b94a83e05`, seven harvest paths) are live, and neither is an ancestor of `box/sitez` (the CTO measured it by `merge-base`). ONE merge of the NEWEST live release lands both: the commit to merge is named in the GO as `dell_sha` (it is `6575999df5d22c0123abfc0c88cd1c6f1efe8c96` today; if `OG-ap-42` has closed first it is that release's commit, which carries `6575999df5`; verify by `git merge-base --is-ancestor`). dell1's four harvest files are on trunk only through this landing.

START ONLY on the issuer's GO, which names `trunk_base_sha` (the `box/sitez` HEAD at the GO), `dell_sha`, and the commit that carries dell1's own manifest block naming `dell_sha` (`manifest_sha`; dell1's W1 commits it after its deploy: if the GO names none yet, STOP and say so).

DO, in your own worktree (`C:/tmp/og-land-s43`, branch `land-sitez-rel-nfra1-43`, created from `trunk_base_sha`; a sparse cone holding every path in `<paths>` and the gateway folder):
1. `git merge-tree --write-tree --name-only trunk_base_sha dell_sha` lists the conflicted paths: print your count as the denominator. Merge `dell_sha` into the branch with `.tools/safe-merge.sh` (its `--continue` limb keeps a conflicted merge inside the guards; never rebase, never `git stash`).
2. Resolve exactly: EVERY conflicted GATEWAY path takes TRUNK's side, EXCEPT dell1's own harvest paths (`app/harvest_research.py`, `app/harvest_figures.py`, `app/harvest_identity.py`, `app/harvest_keys.py`, their two tests and the fixture): for those, the merge takes DELL1's side, because those files are live from dell1 and trunk holds the older blobs; for each such path print both blob ids and which you took. Any conflicted path that is not a gateway path under `infra/aws/ec2/opal-gateway/`: STOP, file a BLOCKING row naming it, create no merge commit. The manifest block `services.opal-gateway` takes the pair `expected_deployed_commit` = `dell_sha`, `expected_previous_commit` = its parent as the manifest source (`manifest_sha`) records it; nothing else in `EC2_MANIFEST.json` moves.
3. Write `W/ap43_landing.json` = `{"trunk_base_sha", "dell_sha", "merge_sha", "manifest_source": "dell1_commit", "manifest_sha", "expected_deployed_commit", "expected_previous_commit", "live_sha": "<the live release the check compares with>", "trunk_own_changes": [{"path": "infra/aws/ec2/opal-gateway/app/<file>.py", "why": "<the cell or commit that put this change on trunk>"}]}` (40-character shas; `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`). `ap43.AC3` compares the gateway `app/` of the merge with `live_sha` and prints each file that is code-different or on one side only, marking in `why` whether it is SITE-Z-OWN or DELL1-OWN; list every such file. Commit the record and run the criteria (AC1 to AC4). Do NOT push: I drain the branch to `box/sitez` and `0.0.0_AB_MSTR~Z` carries it to origin, then tells dell1.

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
  <criterion id="AC1" cell_refs="OG-ap-43"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/ap43.AC1.sh; echo "exit=$?"</invocation><expect>(?s)merge parents are exactly trunk_base and the dell1 commit: yes; dell1's release is an ancestor of the merge: yes; conflicted paths \(merge-tree, the denominator\): (\d+); conflict markers in 0 of \1 paths \(want 0\).*each dell1-own and holding dell1's blob: yes\); the \d+ conflicted gateway paths resolved \(dell1-own to dell1's blob, any other to trunk's\): yes; terraform files differing 0 \(want 0\); paths outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-43"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/ap43.AC2.sh; echo "exit=$?"</invocation><expect>(?s)manifest opal-gateway deployed_commit [0-9a-f]{10} previous [0-9a-f]{10} \(want [0-9a-f]{10} and [0-9a-f]{10}\): yes.*other services and the top level unchanged from trunk_base: yes; the gateway block's other keys unchanged: yes.*manifest source: dell1's own commit [0-9a-f]{10} \(an ancestor of the merge\): yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ap-43"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/ap43.AC3.sh; echo "exit=$?"</invocation><expect>(?s)app/ python files compared live [0-9a-f]{10} against the merge: \d+; equal \d+; docstring-only differences \d+; code-different \d+; present on one side only \d+.*unlisted 0 \(want 0\); tools\.py code-equal to live: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="OG-ap-43"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh land43set tests/test_og_en13.py tests/test_og_en15.py tests/test_og_en17.py tests/test_og_en18.py tests/test_og_en19.py tests/test_og_en20.py tests/test_og_en21.py tests/test_og_en22.py tests/test_og_en23.py tests/test_og_en24.py tests/test_og_cl2.py tests/test_og_rv2.py tests/test_og_db3.py tests/test_og_en9.py tests/test_og_sv2.py tests/test_og_pr1.py; echo "exit=$?"</invocation><expect>(?s)land43set forward: passed (\d+); failed 0.*land43set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a true merge of the live release on the trunk head, no conflict marker left, no Terraform or non-gateway byte changed. `AC2`: the manifest block names the release as live with its parent as previous, the pair taken from dell1's own commit, and nothing else in it moved. `AC3` (the CTO's criterion): the gateway `app/` is AST-equal to the LIVE release plus trunk's own changes, each listed with its owner. `AC4`: the window test files (the sixteen named) pass together in both orders with the same count.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-43.round-43-land-the-live-releases-on-the-sitez-lineage.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4 --governing-order <this order>` (the instance carries ALL FOUR criteria rows), flip NOTHING (the `<status>` flip is mine), and report once (the merge sha, the conflicted-path denominator, the AC lines, the listed trunk changes with their owners, the push state as a measured `ls-remote` value).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 43, workstream ENRICH-R43-A. Source: round-42 analysis item 8 ("land 3b94a83e05 and 6575999df5 on box/sitez, in the shape of OG-ap-41; trunk's side on conflicts; AC3 lists every path that differs from live, each marked site-Z-own or dell1-own; then MSTR~Z tells dell1, which may cut from trunk again").
- The cell departs from OG-ap-41 in ONE stated way: on dell1's own harvest paths a conflict takes DELL1's side, not trunk's, because the CTO's standing condition makes those four files dell1's (they are live from dell1 and trunk holds older blobs). If the issuer's `merge-tree` at the GO shows no conflict on them (the usual case), the clause is idle. Disclosed so the CTO can correct it.
- `ap43.AC1` to `AC3` are `ap41`'s scripts re-pointed at `ap43_landing.json`; they grade through `r38/checks/_ap37_check.py` modes 1 and 2.
- Chain: independent of the builds; its `dell_sha` may be `OG-ap-42`'s release if that closes first.
- Pre-cut: `AC1` and `AC2` base FAIL as expected (the record is absent).

<status>staged</status>
<round>43</round>
<workstream>ENRICH-R43-A</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
