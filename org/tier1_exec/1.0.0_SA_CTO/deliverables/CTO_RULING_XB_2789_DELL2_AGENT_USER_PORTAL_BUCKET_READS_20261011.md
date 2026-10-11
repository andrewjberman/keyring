# CTO ruling -- XB-20261011T093632Z-2789 (row ADVI_COTBKF-D2-S92): the dell agent users are NOT granted reads on `opalinvest-portal`

From 1.0.0_SA_CTO (laptop; owner of `infra/aws/terraform/nfra-ctlpln-identity/iam.tf`, the dell agent users' grants),
2026-10-11 ~09:4xZ. Call body: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/XB_CALL_D2_S92_DELL2_AGENT_USER_PORTAL_BUCKET_READS_20261011.md`.

## Measured (live, one principal each)

| Principal | `s3:GetBucketPublicAccessBlock` on `arn:aws:s3:::opalinvest-portal` | `s3:ListBucket` |
|---|---|---|
| `user/cloudops-dell2-agent-user` | implicitDeny (no statement matched) | implicitDeny |
| `user/cloudops-dell1-agent-user` | implicitDeny | implicitDeny |
| `user/Andrew_Berman` (the laptop's identity) | allowed | allowed |

The bucket policy carries one statement (`AllowCloudFrontOAI`, Allow `s3:GetObject`); there is no fence. The two dells are
denied because nothing grants them: the identity root gives each dell exactly its own box's acts (bus queue, resident
command documents, transcripts decrypt), by design, and `tests/simulate_dell_parity.py` holds dell1 and dell2 IDENTICAL
(Andrew-direct 2026-10-09 ~03:5xZ, AMENDMENT 26).

## Ruling: NO. Row D2-S92's rule is the permanent answer.

1. `shared-infra` is not a dell-applied root. Its appliers run as the laptop's or site Z's identity, which read every
   resource the root refreshes. A dell box that needs to plan it uses the two forms that do not refresh the portal bucket:
   a **targeted** plan (CB-bj-1's own plan read 2 to add, 0 to change, 0 to destroy, 0 errors under targeting) or
   `-refresh=false`. A refreshing, untargeted plan from a dell is never evidence of drift for a resource that identity
   cannot read, and no seat applies from such a plan. That is exactly D2-S92's rule; it stands.
2. The two reads are not granted because they would not end the chain: the untargeted refresh also failed on
   `cur:ListTagsForResource` (row 2) and would fail on every other resource of the 253 the dell users cannot describe. Granting
   read parity with the laptop identity, resource by resource, is the creep the per-box least-privilege design exists to
   refuse. A dell that must plan the whole root is the owner's case to re-open with the whole read set named, not two rows.
3. Parity holds: nothing changes for either dell user; the identity root is unchanged; no apply.
4. dell2 closes D2-S92 citing this ruling; the CB-bj-1 re-run (XB-282f) proceeds under the targeted plan it already has.
