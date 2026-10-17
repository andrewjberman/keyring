# NFRA_OPLGTW task order -- `OG-ap-37` -- APPLY (repository only): land dell1's gateway release `1753c741d9` (AMGT_HARVST HVST-cd-2) on the sitez trunk (CTO decision 35516)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-37</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-37</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a repository merge; no schedule, trigger or deploy is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, no Terraform; the merge changes no gateway byte.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's decision 35516: "landing dell1's release on sitez's lineage is an order you cut for ~NFRA1, as for 319c"; the released bytes are already live.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ap-37` (decomposition addendum R3-T.115, round 41, workstream ENRICH-R41-S)

CONTEXT. `0.7.0_AE_CloudOps~SC1` deployed `1753c741d988faa05fa424386bcd9aa0c5efbf71` (`AMGT_HARVST` `HVST-cd-2`, `harvest_research.py` plus `tests/test_cd1_dossier_misfiled.py`, parent `9d5b7125571520b977401634a01935924f4c9787`) to the gateway host at 2026-10-17T15:01Z from the release line `origin/rel-amgt-harvst-cd2`; its ledger closed at 15:08Z; its manifest commit `25699bc8e5` is already an ancestor of `box/sitez`. The two released files are ALREADY byte-equal on trunk (the `AMGT_HARVST` worker lineage landed them: `harvest_research.py` blob `6550449be12d`, the test blob `9a95d8232ddc`). What trunk lacks is the release commit itself as an ancestor, so this order lands that LINEAGE, changing no gateway byte.

START ONLY on the issuer's GO, which names `trunk_base_sha` (the `box/sitez` HEAD at the GO).

DO, in your own worktree (`C:/tmp/og-land-cd2`, branch `land-hvst-cd2-nfra1`, created from `trunk_base_sha`; a sparse cone holding every path in `<paths>` and the gateway folder):
1. `git merge-tree --write-tree --name-only trunk_base_sha 1753c741d988faa05fa424386bcd9aa0c5efbf71` lists the conflicted paths (ONE when this order was cut: `infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py`; print your count as the denominator). Merge `1753c741d988faa05fa424386bcd9aa0c5efbf71` into the branch with `.tools/safe-merge.sh` (its `--continue` limb keeps a conflicted merge inside the guards; never rebase, never `git stash`).
2. Resolve exactly: `client_adapter_bd49f.py` takes TRUNK's side (the blob at `trunk_base_sha`, `59bfea7afa` when this order was cut; dell1's blob equals the live ref's `48c8cc2d2f` and is the older lineage). Any other conflicted path: STOP, file a BLOCKING row naming it, create no merge commit. After the merge no gateway path differs from `trunk_base_sha`, and no Terraform, portal or `lib/` file differs from it; a path that does is a STOP.
3. Write `W/ap37_landing.json` = `{"trunk_base_sha", "dell_sha": "1753c741d988faa05fa424386bcd9aa0c5efbf71", "merge_sha", "manifest_source": "dell1_commit", "manifest_sha": "25699bc8e5ab6307b060b718d6ea1575c39f6f73"}` (40-character shas; `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`). Commit the record and run the criteria. Do NOT push: `0.0.0_AB_MSTR~Z` carries the merge to origin after the issuer's word.

## 2. BOUNDS

- Only the paths in `<paths>`. No deploy, no Terraform, no IAM, no push, no change to a gateway byte, no object or item written to any bucket or table.
- Never: `git stash`, rebase, `checkout --`, `clean`, `HALT_OVERRIDE`; print a credential or an account number.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and stop.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The tree convention grants `W`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-37"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ap37.AC1.sh; echo "exit=$?"</invocation><expect>(?s)merge parents are exactly trunk_base and the dell1 commit: yes; dell1's release is an ancestor of the merge: yes; conflicted paths \(merge-tree, the denominator\): (\d+); conflict markers in 0 of \1 paths \(want 0\).*gateway paths differing from trunk_base: 0 \(want 0, the merge changes no gateway byte\); the (\d+) conflicted gateway paths equal trunk_base's blobs: yes; terraform files differing 0 \(want 0\); paths outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-37"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ap37.AC2.sh; echo "exit=$?"</invocation><expect>(?s)manifest opal-gateway deployed_commit efcc8ae19f previous 1753c741d9 \(want efcc8ae19f and 1753c741d9\): yes.*other services and the top level unchanged from trunk_base: yes; the gateway block's other keys unchanged: yes.*manifest source: dell1's own commit 25699bc8e5 \(an ancestor of the merge\): yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a true merge of dell1's release commit on the trunk head, no conflict marker left, no gateway, Terraform or other byte changed. `AC2`: the manifest block still names the live release (`efcc8ae19f`, previous `1753c741d9`) and nothing else in it moved.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-37.land-dell1-harvest-release-on-trunk.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (the merge sha, the conflicted-path denominator, the AC lines).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 41, workstream ENRICH-R41-S (decomposition addendum R3-T.115): not on the `OG-ap-36` critical path (its re-cut reads dell1's live ref from the manifest, which the box pass already carries). Staged: the GO is the issuer's message citing this order and naming `trunk_base_sha`; sent after the `OG-ap-36` re-cut report, because the merge moves the trunk head (the release files stay byte-equal).
- Pre-cut: `ap37.AC1` and `ap37.AC2` base FAIL as expected (the record is absent); a synthetic merge commit on plumbing passes both (parents trunk and dell1, the manifest block set); controls FAIL: one parent, `harvest_research.py` differing from dell1's blob, an extra gateway file, a Terraform file, the manifest still on the old live ref, another service changed in the manifest.
- The check also supports a `landing_row` manifest source with a host md5 walk record (the CTO's fallback if dell1's manifest commit had not been pushed); it is not needed now.

- A1 (2.0.0_SA_COO~O, round 41, ~18:4xZ): `OG-ap-36` closed at 18:11:52Z, so the manifest on trunk now reads `deployed_commit` `efcc8ae19f7eebb04e2f45f45c0def28af037c24`, previous `1753c741d988faa05fa424386bcd9aa0c5efbf71`; the text above that says the manifest names `1753c741d9` is superseded by this note (the landing changes no manifest byte: it keeps trunk's block, and `ap37.AC2` now expects that pair, or the pair the record names in `expected_deployed_commit`/`expected_previous_commit`). The merge target is still dell1's release commit `1753c741d9` (AC1 unchanged). Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A2 (2.0.0_SA_COO~O, round 41, ~18:5xZ): trunk is now AHEAD of dell1's release on `harvest_research.py` (`AMGT_HARVST` `HVST-ce-3`, commit `d9d65d2184`, landed after `1753c741d9`: trunk blob `d2f07d4bf6` against dell1's `6550449be1`), so the merge of `1753c741d9` conflicts on TWO gateway paths, `client_adapter_bd49f.py` and `harvest_research.py`, not one (the earlier statement that trunk carries dell1's two files byte-equal is superseded). Resolution for BOTH: TRUNK's side (the blob at `trunk_base_sha`); after the merge NO gateway path differs from `trunk_base_sha`. `ap37.AC1` now checks that every conflicted gateway path equals `trunk_base_sha`'s blob (no longer that the two dell1 files equal dell1's blobs). Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>staged</status>
<round>41</round>
<workstream>ENRICH-R41-S</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
