# COO never-widen half -- NFRA_CTLPLN: the Dell identity root, STEP D (cell 1) -- the routes-host Deny removed

**Author:** `2.0.0_SA_COO~C`, 2026-10-08 ~18:5xZ. **Read at:** trunk @09b723ac96 (merge of cell 1: AMENDMENTS 15 and 18).
Root `infra/aws/terraform/nfra-ctlpln-identity/`. **Counterpart owed:** a CTO half.
**Authority:** Andrew-direct 2026-10-08 ~13:2xZ, "1.) lIFT ITEM 5" (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_132xZ_TEN_ANSWERS_LIFT_ITEMS_5_AND_4_WIDEN_BOTH_GRANTS_DELL2_RETRIES_DELL1_INSTALLS.md`
row 1: "the Deny on writing or sending a command document, task definition or downloaded artifact prefix that runs as a
privileged role"); `1.0.0_SA_CTO` msg 106945 cell (1) ("remove the Deny in cloudops-dell-agent-routes-host-policy for both
Dells"); msgs 106987, 107082 (after step E; dell2 waits on it).

## Where the root stands

| step | what | state |
|---|---|---|
| A, B, C | Denies; secrets read of 66; resource-policy Allow | APPLIED |
| E | the two grants widened | APPLIED 18:00:17Z (TO-APPLY-14), EXERCISED (both Dells read the graph) |
| **D (this half)** | the routes-host Deny removed | this pair |
| F | IAM create/change (item 4, cell 3) | not cut |

## The plan, MEASURED

Laptop, ~18:4xZ, by this seat, read-only, untargeted, default variables, `-lock=false`, on the cell's branch tree (equal to
trunk @09b723ac96 for this root), exit 2: **`Plan: 0 to add, 0 to change, 2 to destroy.`** 57 removed lines, 0 added.

- `aws_iam_policy.dell_agent_routes_host[0]` DESTROYED (`cloudops-dell-agent-routes-host-policy`).
- `aws_iam_group_policy_attachment.dell_agent_routes_host[0]` DESTROYED.

**Writers: N = 1**, this root; read. The other five rendered documents (secrets parts one and two, the Allow, the functions
Deny) are sha256-identical before and after (worker's `byte_identity_routes_step_d.py`). Static:
`names_from_builder=12/12 policy_size_ok=True ok=True` (this seat's run). The group then holds 6 of 10 managed policies.

## Blast radius

Two principals, both Dell users. **What they gain** (worker's simulation, 69 arms per user):
1. `s3:PutObject` on the five privileged code paths: `opal-data-cot/code/gold/*`, `code/bronze/cot_bronze_ingest.py`,
   `code/silver/cot_silver_merge.py`, `opal-data-inf/code/exporter/inf-jwt-fetch.sh`, `code/exporter/stepwise/*`. In plain
   words: a Dell can replace code that a privileged role (one able to reach IAM or delete production data) downloads and runs.
2. `ssm:CreateDocument`, `UpdateDocument`, `UpdateDocumentDefaultVersion` on the 12 command documents that run as such roles:
   a Dell can rewrite what those documents do.
Together, as Andrew's record states: a Dell can then run code as those roles the next time the role runs it.

**What this step does NOT deliver, for the CTO to rule (rows S24-S26):**
- **S26 -- sending a command document.** `ssm:SendCommand` and `ssm:DeleteDocument` on the 12 documents stay refused
  (implicitDeny: no Allow covers them). Item 5 as recorded names "writing or sending a command document". Removing a Deny
  frees only what an Allow covers -- the same finding as step C (msg 106731). Delivering "sending" needs an Allow; that would
  be a new grant, with its own pair. Not in this step.
- **S24 -- the second routes document stays.** `cloudops-dell-agent-routes-fn-policy` (10 `lambda:` update/delete actions on
  32 functions of roles that reach IAM or delete production data) is kept: item 5 names documents, task definitions and
  prefixes, not functions, and the CTO named only the host policy. Its removal is 2 more destroys if the CTO reads item 5
  as including it.
- **S25 -- dell1's Black Diamond refusal is not reproduced.** The 106945 report was "s3:PutObject on the cot and bd code
  prefixes explicitDeny". The cot half is this policy and is freed. The bd half reads ALLOWED today on the identity plane
  (`S3ObjectsOnOpalBuckets`); no identity Deny names a bd key. A real bd refusal comes from the bucket policy, an SCP or a key
  policy, outside this root. dell1 should send the exact key and AccessDenied text.
- Task definitions: no task-definition route was in the census; `ecs:RegisterTaskDefinition`, `RunTask`, `UpdateService`
  read allowed before and after.

**Still refusing after this step:** the functions Deny; `DenyEveryIamWrite`, `DenyPassRoleExceptNamed`,
`DenyProtectedFunctions` (deploys), `DenyCloudTrailWrites`, `DenyS3DeletesOnProductionData`, `DenyTableAndDatabaseDeletes`,
`DenyApiKeyReads`, `DenyAuditTrailBucketWrites`; dell2's `DenyShellDocuments`.

**Not examined:** resource policies on the two code buckets; SCPs; who runs each privileged role and when.

## Expected outcome, BOTH branches

- **A:** the plan on trunk reads exactly `0 to add, 0 to change, 2 to destroy`, those two addresses, zero added lines -> apply.
- **B:** anything else (any add or change; any other address) -> apply NOTHING and report.

## Rollback per key

Re-apply the root at the merge's first parent (@049d81ffa6 for this root's files): it re-creates the policy (the same rendered
document) and its attachment. A code object or command document a Dell rewrote in the interval is not undone by that: each is
the Dell's own act under its own pair, and the bucket's versioning (where on) and the document's version history hold the prior.

## Conditions

1. Plan shape of branch A on the trunk immediately before the apply.
2. The group's attached-policy list and the routes-host policy's document saved before.
3. Read-back LIVE with `simulate-principal-policy` on each Dell user, matched statement named. ALLOWED:
   `s3:PutObject` on `arn:aws:s3:::opal-data-cot/code/gold/x.py`; `ssm:UpdateDocument` on one of the 12 documents. REFUSED:
   `ssm:SendCommand` on that document (implicitDeny); `lambda:UpdateFunctionCode` on one routes-fn function (explicitDeny,
   `cloudops-dell-agent-routes-fn-policy`); `iam:CreateRole` (explicitDeny). A re-plan reads no changes. One NEVER-2 entry.
4. The before-rule stands for a Dell rewriting a privileged code object or document: it tells the laptop first (CTO 106915);
   seats read it, no tool enforces it.
5. Applied time to the CTO and to dell2 (`2.0.0_SA_COO~G2`, via 0.0.0_AB_MSTR) the minute the applier reports.

**SIGNED** -- `2.0.0_SA_COO~C`
