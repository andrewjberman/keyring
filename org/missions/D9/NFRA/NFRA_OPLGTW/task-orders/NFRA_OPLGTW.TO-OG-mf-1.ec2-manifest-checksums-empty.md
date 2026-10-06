# NFRA_OPLGTW task order -- `OG-mf-1` -- the opal-gateway manifest row's file_checksums emptied

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-mf-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~26</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a manifest edit; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- repo only; no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ruling is the CTO's (R26, round-20 analysis s.3).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-mf-1` (decomposition addendum R3-T.14, item 2; row Z-W15-S65)

R26: `infra/aws/ec2/EC2_MANIFEST.json` `services.opal-gateway.file_checksums` is unmaintained (8 of 10 entries
differ from the live bytes). Set it to `{}`, the estate's convention (every other service row;
`EC2_DEPLOYMENT_PROTOCOL.md:147`). Add `_checksums_note`:
"not maintained; deployed_commit plus the release's host md5 read are the record".
Change nothing else in the file: `deployed_commit` stays `2c27f3a795...`. Keep the JSON's existing indentation
and key order.

## 2. BOUNDS

- Repo edits within your paths only; no deploy, no host or AWS write.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~26/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W26-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-mf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r21/checks/mf1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)file_checksums empty map: True; note names 'not maintained' and deployed_commit: True; deployed_commit 2c27f3a795.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~26/NFRA_OPLGTW.TO-OG-mf-1.ec2-manifest-checksums-empty.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`, and on PASS edit this order's ONE `<status>` tag IN
PLACE to `complete`. Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 21 (R3-T.14, item 2). Alone. LOCAL: no release.
- Pre-cut: `mf1.AC1.sh` FAIL (the map holds 10 entries; no note).

<status>pending</status>
<round>21</round>
<slot>~26</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
