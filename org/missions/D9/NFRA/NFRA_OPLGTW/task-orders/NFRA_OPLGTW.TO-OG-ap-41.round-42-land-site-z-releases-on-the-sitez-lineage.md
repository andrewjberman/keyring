# NFRA_OPLGTW task order -- `OG-ap-41` -- APPLY (repository only): land site Z's two live gateway release commits `efcc8ae19f` (OG-ap-36 A4) and `d077cef043` (OG-ap-38 A1) on the sitez trunk lineage, resolving to trunk's side (dell1 CTO ruling via `0.0.0_AB_MSTR~Z` msg 35630)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-41</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-41</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a repository merge; no schedule, trigger or deploy is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, no Terraform; the merge changes no gateway byte.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is dell1 CTO's ruling (its msg 7926, relayed by MSTR msg 35630): site Z lands its two gateway release commits on its own lineage first and resolves its own conflicts; dell1's `cg-3` merges on top afterwards. The released bytes are already live.
EGRESS CLASS, declared: NONE.
</preflight>

## 0. AMENDMENT A1 (2.0.0_SA_COO~O, round 42, ~07:1xZ; the CTO's msg 35639) -- READ THIS FIRST; it overrides sections 1 to 4 where they differ

`OG-ap-39` is LIVE: ledger `nfra-oplgtw-gateway-release-batch8` CLOSED 2026-10-18T07:01:17Z, live `aa2efa2cf3dee82030c00f85425f686132adcf4a` (parent `4257a2aa42`, dell1's `cg-3` release, whose parent is `d077cef043`). The landing therefore takes the NEW live release in ONE merge: the commit to merge is `aa2efa2cf3dee82030c00f85425f686132adcf4a`, which carries `4257a2aa42`, `d077cef043` and `efcc8ae19f` (4 commits not on `box/sitez`), so that trunk's lineage equals the live line. Measured by the issuer at the amendment (trunk head `86d72b7931`): the merge-tree is CLEAN (NO conflicted path: trunk now carries the release's `tools.py` and `test_og_db3.py` bytes, so both sides are equal) and the merged tree equals trunk's tree, i.e. no byte changes. Where sections 1 to 4 say `d077cef043` read `aa2efa2cf3dee82030c00f85425f686132adcf4a`, and where they say two conflicted paths read: print YOUR denominator (0 when this order was amended; any conflicted path is still resolved to TRUNK's side and any non-gateway conflicted path is a STOP). The record `W/ap41_landing.json` is now `{"trunk_base_sha", "dell_sha": "aa2efa2cf3dee82030c00f85425f686132adcf4a", "merge_sha", "manifest_source": "dell1_commit", "manifest_sha": "6d98c6a32665cb08fd710862e8272dcae8364906", "expected_deployed_commit": "aa2efa2cf3dee82030c00f85425f686132adcf4a", "expected_previous_commit": "4257a2aa42e5366270b3652f21dba90872dbb1e0", "live_sha": "aa2efa2cf3dee82030c00f85425f686132adcf4a", "trunk_own_changes": [...]}` (`manifest_sha` is the applier's own Phase B manifest commit, an ancestor of the merge). `ap41.AC3` compares the gateway `app/` of the merge with the LIVE release `aa2efa2cf3` (the record's `live_sha`): `tools.py` is code-equal and docstring-equal now, and the files that remain code-different are trunk's own changes to list. There is no Part 2: this merge already takes `OG-ap-39`'s release commit. Gate limb: GATE (viii) on the modified order (placeholders NONE).

## 1. THE CELL -- `OG-ap-41` (decomposition addendum R3-T.119 amendment A7, round 42, workstream ENRICH-R42-E)

CONTEXT. Site Z deployed `efcc8ae19f` (`OG-ap-36` A4, 2026-10-17) and `d077cef043` (`OG-ap-38` A1, 2026-10-18 00:02Z) to the gateway host from release lines cut on the live ref of the day. `efcc8ae19f` is an ANCESTOR of `d077cef043`, so ONE merge of `d077cef043` lands both (2 commits). Neither commit is an ancestor of `box/sitez` or of origin `CLOUD` today (they sit on origin only as `0.0.0_AB_MSTR~Z`'s scratch refs). Every gateway byte they carry is ALREADY on trunk (the release files were taken whole from trunk at their cut and trunk has only moved forward), so this order lands the LINEAGE and changes no gateway byte. Dell1's `HVST-cg-3` release `4257a2aa42` (parent `d077cef043`) merges on top of this landing; until then dell1 cuts from its own release line.

START ONLY on the issuer's GO, which names `trunk_base_sha` (the `box/sitez` HEAD at the GO).

DO, in your own worktree (`C:/tmp/og-land-s42`, branch `land-sitez-rel-nfra1`, created from `trunk_base_sha`; a sparse cone holding every path in `<paths>` and the gateway folder):
1. `git merge-tree --write-tree --name-only trunk_base_sha d077cef04333500595a7a531ebddc2f43e5f8789` lists the conflicted paths. TWO when this order was cut: `infra/aws/ec2/opal-gateway/app/tools.py` (content) and `infra/aws/ec2/opal-gateway/tests/test_og_db3.py` (add/add). Print your count as the denominator. Merge `d077cef04333500595a7a531ebddc2f43e5f8789` into the branch with `.tools/safe-merge.sh` (its `--continue` limb keeps a conflicted merge inside the guards; never rebase, never `git stash`).
2. Resolve exactly: EVERY conflicted gateway path takes TRUNK's side (the blob at `trunk_base_sha`). Any conflicted path that is not a gateway path under `infra/aws/ec2/opal-gateway/`: STOP, file a BLOCKING row naming it, create no merge commit. After the merge NO gateway path differs from `trunk_base_sha`, no Terraform file differs from it, and no path outside `<paths>` plus the project tree differs; a path that does is a STOP. The `EC2_MANIFEST.json` stays exactly as trunk has it (`opal-gateway` `deployed_commit` `4257a2aa42e5366270b3652f21dba90872dbb1e0`, `previous_deployed_commit` `d077cef04333500595a7a531ebddc2f43e5f8789`).
3. Write `W/ap41_landing.json` = `{"trunk_base_sha", "dell_sha": "d077cef04333500595a7a531ebddc2f43e5f8789", "merge_sha", "manifest_source": "dell1_commit", "manifest_sha": "22214e3c4ac0153f61e0e36d7e015b89b036aae5", "expected_deployed_commit": "4257a2aa42e5366270b3652f21dba90872dbb1e0", "expected_previous_commit": "d077cef04333500595a7a531ebddc2f43e5f8789"}` (40-character shas; `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`; the field `dell_sha` names the commit that is merged, here site Z's own `d077cef043`, because the check is the one `OG-ap-37` used). The record ALSO carries `"trunk_own_changes": [{"path": "infra/aws/ec2/opal-gateway/app/<file>.py", "why": "<the cell or commit that put this change on trunk>"}]` for every file `ap41.AC3` prints as code-different or one-sided. Commit the record and run the criteria (AC1 to AC4). Do NOT push: I drain the branch to `box/sitez` and `0.0.0_AB_MSTR~Z` carries it to origin, then I tell dell1.

## 2. BOUNDS

- Only the paths in `<paths>`. No deploy, no Terraform, no IAM, no push, no change to a gateway byte, no object or item written to any bucket or table.
- Never: `git stash`, rebase, `checkout --`, `clean`, `HALT_OVERRIDE`; print a credential or an account number.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and stop.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/tests/test_og_db3.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The tree convention grants `W`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-41"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r42/checks/ap41.AC1.sh; echo "exit=$?"</invocation><expect>(?s)merge parents are exactly trunk_base and the dell1 commit: yes; dell1's release is an ancestor of the merge: yes; conflicted paths \(merge-tree, the denominator\): (\d+); conflict markers in 0 of \1 paths \(want 0\).*gateway paths differing from trunk_base: 0 \(want 0, the merge changes no gateway byte\); the (\d+) conflicted gateway paths equal trunk_base's blobs: yes; terraform files differing 0 \(want 0\); paths outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-41"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r42/checks/ap41.AC2.sh; echo "exit=$?"</invocation><expect>(?s)manifest opal-gateway deployed_commit aa2efa2cf3 previous 4257a2aa42 \(want aa2efa2cf3 and 4257a2aa42\): yes.*other services and the top level unchanged from trunk_base: yes; the gateway block's other keys unchanged: yes.*manifest source: dell1's own commit 6d98c6a326 \(an ancestor of the merge\): yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ap-41"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r42/checks/ap41.AC3.sh; echo "exit=$?"</invocation><expect>(?s)app/ python files compared live aa2efa2cf3 against the merge: \d+; equal \d+; docstring-only differences \d+; code-different \d+; present on one side only \d+.*unlisted 0 \(want 0\); tools\.py code-equal to live: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="OG-ap-41"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh land41set tests/test_og_en13.py tests/test_og_en15.py tests/test_og_en17.py tests/test_og_en18.py tests/test_og_en19.py tests/test_og_en20.py tests/test_og_en21.py tests/test_og_en22.py tests/test_og_en23.py tests/test_og_en24.py tests/test_og_cl2.py tests/test_og_rv2.py tests/test_og_db3.py tests/test_og_en9.py tests/test_og_sv2.py tests/test_og_pr1.py; echo "exit=$?"</invocation><expect>(?s)land41set forward: passed (\d+); failed 0.*land41set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC3` (the CTO's criterion, msg 35632): the gateway `app/` is AST-equal to the LIVE release `4257a2aa42` plus trunk's own changes; the record's `trunk_own_changes` lists every code-different or one-sided file as `{"path", "why"}` (the check prints the names; at the cut they were `admin_people_access.py`, `destructive_ops.py`, `family_depth.py`, `probe_listener.py`, `server.py`: name for each the cell or commit that put it on trunk). `AC4`: the window test files (the sixteen named) pass together in both orders with the same count.
- `AC1`: a true merge of site Z's release commit on the trunk head, no conflict marker left, no gateway, Terraform or other byte changed (this resolves the CTO's "keeps both live's lines and trunk's": the release's lines are trunk's lines, because the release files were taken whole from trunk; `AC3` proves it on the code). `AC2`: the manifest block still names dell1's `cg-3` release as live (`4257a2aa42`, previous `d077cef043`) and nothing else in it moved.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-41.round-42-land-site-z-releases-on-the-sitez-lineage.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (the merge sha, the conflicted-path denominator, the AC lines, the listed trunk changes, the push state as a measured `ls-remote` value). PART 2 (a later GO, after `OG-ap-39`'s Phase B has closed its ledger): the same merge for `OG-ap-39`'s release commit `aa2efa2cf3dee82030c00f85425f686132adcf4a`, issued as an amendment of this order; do not start it on this GO.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 42, workstream ENRICH-R42-E (decomposition addendum R3-T.119 amendment A7; one issuance per workstream). The ask comes from dell1's CTO through `0.0.0_AB_MSTR~Z` (msg 35630): site Z lands `d077cef043` and `efcc8ae19f` on its own lineage first and resolves its own conflicts; MSTR measured the same two conflicts (`app/tools.py`, `tests/test_og_db3.py`) and the same two commits. Precedent and grading: `OG-ap-37` (the same check, `_ap37_check.py` modes 1 and 2).
- Independent of `OG-ap-39`: that release is cut on `4257a2aa42` from its own branch and compares blobs with trunk at its `trunk_sha` (an immutable commit), so the landing moves the trunk head and no blob. The later landing of `OG-ap-39`'s and `OG-ap-40`'s release commits is a follow-up order of the same shape.
- Pre-cut: `ap41.AC1` and `ap41.AC2` base FAIL as expected (the record is absent); the synthetic dry-run on a plumbing merge commit (parents trunk and `d077cef043`, trunk's tree) passes both; controls FAIL: one parent (no merge), the manifest pair not what the record expects.

<status>staged</status>
<round>42</round>
<workstream>ENRICH-R42-E</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
