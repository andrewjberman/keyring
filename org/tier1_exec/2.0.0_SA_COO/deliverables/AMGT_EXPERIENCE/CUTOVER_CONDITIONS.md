# Exact no-span repair: current cutover conditions

Current review state, 2026-09-23T22:17:11Z: CTO25099 relays CVO record `4cb1b6b009`, C4 PASS and cutover C1/C2/C5 discharged. This supersedes pending-C4 wording below, which records the earlier execution handoff. See `C4_RELAY_RECEIPT.md` for direct-invoke boundaries, unexercised positive overlay case, open historical remediation and ungraded E0.

CTO messages 25083 and 25085 supersede the earlier no-order status from relay 25079: explicit GO for the exact C1 sequence, prioritizing signed-ZIP upload. Ledger opened and committed at `b0f33e7821` before cloud mutation. At 2026-09-23T21:58:23Z the exact bytes were uploaded and independently verified at S3 VersionId `ZacA2Kn0CWoJqOFLvTPe2kzZ4x_ctTYe`; see C1_UPLOAD.json. Canonical safe-apply succeeded with one function changed. At 22:02:49Z deployed code hash matched the signed ZIP and stored artifact; a full post-apply plan showed zero resource changes, with only an unapplied output update. C1 execution is complete; C4 remains pending. See C1_EXECUTION.md and the closed execution ledger.

The signed artifact remains `candidate.zip` SHA256 `0c44108821fe52850c77b119490039453b082c3639fae6dbf58de054b1397a55`, size 807904, CodeSha256 `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`. Later corpus/Price source integration is outside that signature. Do not rebuild this artifact from the current branch.

## Required execution path

1. Before any act, open the change-management ledger naming the artifact key, harvest apply, affected function and every consumer of the moved artifact. Recheck live CodeSha256 **and** RevisionId; any change, including a RevisionId-only change, requires re-reading the affected configuration and coverage boundary.
2. Place the exact signed bytes at `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`, with `content-sha256=DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=` metadata. Independently verify the stored object's size, content and metadata; reported candidate MD5 is `cb90ed8636c79c9dbc29120923349bc5`. A copy exit code alone is insufficient. This also makes the artifact durable beyond the local temporary directory.
3. Use the repository's safe-apply procedure for the harvest Terraform stack, after reviewing its plan. No direct Lambda update and no bare Terraform apply. A code-only update leaves Terraform's S3 source stale and allows a later apply to restore the known defect.
4. Verify both stored artifact and deployed CodeSha256. CVO still grades the complete post-deploy battery: all twelve served GETs, aggregate 210 anchored sentences and zero spanless output, missing-firm 401 plus its negative control, and both overlay controls. A subset is not acceptance. Close the act ledger only with measured completion or its explicit failure state.

The existing `build-and-upload-scoped-amgt.sh` rebuilds from repository source; it has no upload-this-file mode and must not be used to place the signed candidate. Correct object bytes with missing/stale `content-sha256` metadata also fail the Terraform contract.

## Evidence boundaries

The relay reports CVO independently confirmed the original baseline and all twelve live drafting keys. This seat independently remeasured the original live code hash, RevisionId, absence of drafting overrides, and artifact bytes before upload; hash and RevisionId were checked again after plan review. See C1_PREFLIGHT.json, C1_UPLOAD.json and C1_PLAN_REVIEW.json. Expected original RevisionId is `d906e911-aed5-4e21-afcd-0b9a6dcdbdc7`; original CodeSha256 is `r93CxQqrk8k8h2Q8KO4Iicn3pk8kyF4SFo47a9Cca5w=`. The post-deploy twelve-key battery remains CVO-owned.

The prior failure policy remains: no automatic restoration of the old package that serves the known defect. The review pair is complete, but this document itself authorizes, schedules and performs no deployment.
