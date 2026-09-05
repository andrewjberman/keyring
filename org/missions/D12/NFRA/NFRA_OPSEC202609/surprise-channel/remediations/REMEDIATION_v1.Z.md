# NFRA_OPSEC202609 -- surprise channel, REMEDIATION v1 (round 1, site-Z fabric)

**Cut by:** `3.0.0_SA_CVO~Z` at the round-1 L10 stamp (2026-09-03T10:36:19Z), the round's ONE slug -- graduated rows only
(`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.5, s.8; spine L9/L10). Lane `TREE_CVO`.
**Filename.** This is the site-Z form the protocol names (s.9: "site Z writes `INVESTIGATION_v<N>.Z.md` ... the same
for remediation files"). The round's investigation file was opened as `INVESTIGATION_v1.md` before that clause was
applied at this seat; the project is placed on ONE fabric, so the two names are a mirror, not a collision, and the
investigation file is left as it is (append-only).
**Precondition at the stamp** (s.8): every task order under the project terminal with a VALID proof-of-spec instance
whose `surprises` entries resolve to rows -- TO-OP-S-3 @a491aaec8c (instance @3c32f20c38), TO-OP-S-17-16 @f9b2a16c2c,
TO-OP-S-8 @2da0c78f6a, TO-OP-S-5 @f49c82b891 -- and every investigation row dispositioned (rows Z-S19 and Z-S20 in the
investigation file, same commit).
**Routes.** Five rows, every one `SPEC_ERROR -> 6` (a cell the decomposition v0.1.4 already contains); the route owner
is `2.0.0_SA_COO~Z` and this document is the one artifact handed to it. No `DECOMP_INVALIDATING`; no `SCOPE_CHANGE` (the
three ratified constraints the world contradicted -- C-8's key, roles, target -- were corrected at L4 by the L4 owner
before this stamp: PRD v0.5 @a3cad58b0d, v0.6 @b482fe8a5b, v0.7 @237265f9f1).
**Why five rows and not ten.** This document carries the RE-ENTRY rows only. The other five graduated items have nothing
to re-enter and carry no row here; their facts are carried verbatim on the adjudication row Z-S19 (investigation file):
S2, S11, S13, S17 were remediated inside round 1 and are closed (disarm and remedy both landed); S1's remedy is a fabric
surface homed by the register (0.0.0_AB_MSTR~Z 19629), and its disarm is this seat's lane-addressed pointer at the
stamp, recorded as its own investigation row after the pointer. MECHANISM: the row gate (`.tools/surprise-row-gate.py`)
requires `route` + `loop_target` on every NEW remediation row, while the schema does not require them and protocol s.8
defines `route` as the re-entry decision ('what does the remedy need that does not exist yet?') -- a value that does not
exist for a remedied or out-of-project item, so writing one would put a second intent on the axis. The gate names an
audited override; on this device the tree-path files are graded by the pre-commit hook, which reads no commit message,
so the override cannot fire for a tree project (exercised on this slug at 10:36Z and 11:19Z). The divergence is filed as
a round-2 intake row for the gate's owner. S10's disarm record (1.0.0_SA_CTO~Z) is HELD off the investigation file until
this slug commits and takes the next free id; S10's row below reads ARMED until that record is on the block.
**Denominator:** 5 rows (S3, S4, S5, S10, S14). Not a zero-graduation round; round 2 opens.

```json
[
 {
  "id": "NFRA_OPSEC202609-Z-S3",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "The key the brief, PRD, decomposition and task order called 'the estate CMK' (86cc6c40) is KeyManager=AWS, alias/aws/dynamodb -- the AWS-managed DynamoDB service key; an S3 bucket cannot use it and its policy cannot be edited, so C-8 as written was unsatisfiable; 'CMK' in the estate's own records names both KeyManager=CUSTOMER and KeyManager=AWS keys, and the word travelled four limbs, each citing the one before.",
  "evidence": [
   "worker's live reads (0.7.0_AE_CloudOps~S): describe-key KeyManager=AWS; list-aliases -> alias/aws/dynamodb; positive control over all 11 keys (4 CUSTOMER, all purpose-specific); describe-table opal-users-v2 SSE KMS 86cc6c40",
   "recorded plane: infra/aws/nfra_terraform_p1/slice_storage.json:1361, :1427-1428 ('AWS-managed CMK (alias/aws/dynamodb)'); docs/briefs/security-scan-track1-findings-20260603.md:55",
   "PRD @43b75ffbd6 :401 C-8, :410-411 C-9, :454/:455 S8/S9 labels; TO face @5494591e91 :23, :48; HEAD blobs of portal-auth/dynamodb.tf and shared-infra/dynamo.tf carry zero kms declarations (controls 7 and 2 resource lines)",
   "L4 ruling: PRD v0.5 @a3cad58b0d (C-13, manifest S25: one project key alias/opal-security); disarm record Z-S7"
  ],
  "remedy": "Round 2: OP-s-25 mints the project key under Terraform; OP-s-16 (UpdateTable in place) and OP-s-17 (bucket default encryption) flip to it -- cells the decomposition v0.1.4 already contains, bound by C-13.",
  "owner": "2.0.0_SA_COO~Z (L6, the round-2 task orders on OP-s-25/16/17; worker class 0.7.0_AE_CloudOps)",
  "round": "v1",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~Z",
   "at": "2026-09-03T08:05:00Z"
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Z",
   "round": "v2"
  },
  "closed": false,
  "route": "SPEC_ERROR",
  "loop_target": 6
 },
 {
  "id": "NFRA_OPSEC202609-Z-S4",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "TO-OP-S-17-16 bound (b) named two principals for the bucket policy's deny-outside-list ('the CTO-admin role', 'the account's Terraform-apply role') that do not exist -- 0 of 216 IAM roles, the applier an IAM user; the same absent 'CTO-admin role' sat in ratified C-8 and in C-13; the names appear nowhere in the estate but this project's texts (never measured); applied as written the statement would have denied the applier and bricked the bucket at creation.",
  "evidence": [
   "worker's live reads (0.7.0_AE_CloudOps~S): list-roles 216 client-side over 3 pages; 'admin|cto|terraform' 0 hits with 'lambda' 55 as control; sts get-caller-identity user/Andrew_Berman; list-users",
   "TO face @5494591e91 :23, :47; PRD v0.5 @a3cad58b0d :405 (C-8), :438 (C-13); comp-find -i 'cto-admin|terraform-apply role|terraform apply role': 35 hits / 50,969 files, all in-project texts",
   "issuer's ruling (a) DEFER in 19519; disarm record Z-S8; L4 ruling PRD v0.6 @b482fe8a5b (C-14, manifest S26: opal-security-admin); trust = Andrew alone for round 2 (his word, 19556; PRD v0.8 @36786251af)"
  ],
  "remedy": "Round 2: OP-s-26 declares opal-security-admin with its one ruled trust principal read live; the deny-outside-list statement lands with the task orders that create the principals it names (OP-s-14 sentinel, OP-s-15 reconciler, OP-s-19 CLI, OP-s-26) -- the face's deferred statement re-cut into those faces (the issuer accepted this route in advance, 19519).",
  "owner": "2.0.0_SA_COO~Z (L6; worker class 0.7.0_AE_CloudOps)",
  "round": "v1",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~Z",
   "at": "2026-09-03T08:13:00Z"
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Z",
   "round": "v2"
  },
  "closed": false,
  "route": "SPEC_ERROR",
  "loop_target": 6
 },
 {
  "id": "NFRA_OPSEC202609-Z-S5",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "C-8's access-logging limb named the CloudTrail audit-log bucket as its target; that bucket permits only cloudtrail.amazonaws.com (no logging.s3 grant, no LogDelivery ACL) and its live policy is not even Terraform-declared, so naming the target was necessary and not sufficient; the specified acceptance read (get-bucket-logging) observes configuration and never delivery, so a configured-but-dead limb would have PASSED it.",
  "evidence": [
   "worker's live reads (0.7.0_AE_CloudOps~S): get-bucket-policy two CloudTrail statements; get-bucket-acl one CanonicalUser grant, no LogDelivery; describe-trails; the 31-bucket sweep stated UNPROVEN by the worker (no positive control)",
   "infra/aws/terraform/shared-infra/s3.tf @HEAD :44-49 declares the target with zero logging.s3 / LogDelivery / cloudtrail.amazonaws.com tokens (control 28 resource lines); infra/aws/terraform/opsec/s3.tf @cdbdcb473c :142/:165 carries the limb commented with the row id",
   "TO face @5494591e91 :23, :30; PRD v0.6 @b482fe8a5b :407-408 (C-8), :482 (S5), :494 (S17)",
   "issuer's ruling DEFER in 19534; disarm record Z-S9; L4 ruling PRD v0.7 @237265f9f1 (C-15, manifest S27: a project-owned opal-data-security-access-logs target, graded by a DELIVERED object)"
  ],
  "remedy": "Round 2: OP-s-27 declares the project-owned access-logs target in the opsec module; OP-s-17's logging limb is uncommented against it; the acceptance read is a delivered object under the prefix after one write, never the configuration -- cells the decomposition v0.1.4 already contains.",
  "owner": "2.0.0_SA_COO~Z (L6; worker class 0.7.0_AE_CloudOps)",
  "round": "v1",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~Z",
   "at": "2026-09-03T08:25:00Z"
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Z",
   "round": "v2"
  },
  "closed": false,
  "route": "SPEC_ERROR",
  "loop_target": 6
 },
 {
  "id": "NFRA_OPSEC202609-Z-S10",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "cross-firm-secret-deny.tf justifies its Deny belt on the premise that three portal/news-plane roles hold a secret:opal/* wildcard; at 2026-09-03 opal-portal-lambda-role holds no such wildcard (three explicit allowlists; simulate-principal-policy implicitDeny on the target with a role-specific positive control allowed), so the belt now sits over an allowlist and its argument describes a world that no longer exists -- in four copies of one justification.",
  "evidence": [
   "worker's live reads (0.7.0_AE_CloudOps~Z): simulate-principal-policy on opal/auth/origin-verify implicitDeny, on opal/auth/jwt-public-key allowed; the role's three inline secrets policies",
   "infra/aws/terraform/portal-auth/cross-firm-secret-deny.tf @HEAD :5, :12 (the premise); replicated in news-pipeline/ and shared-infra/ copies; extended in market-overview/ @2c63773fc9 (the 07-09 CVO sweep) -- comp-find --name: 4 files",
   "DESIRED plane page 1 of 3 (comp-find 'secret:opal/\\*|...' over infra/aws/terraform: 56 hits / 530 files): the belts' own secret:opal/bd/* deny resources and the least-privilege allowlists; no ALLOW carrying secret:opal/* for the role on that page",
   "Disarm: the disarm record by 1.0.0_SA_CTO~Z (OBSERVATION / INERT, cites Z-S10; the belt stays, the correction is the rider) is written and validated at 2026-09-03T10:38:59Z (1.0.0_SA_CTO~Z msg 19649) and HELD off the investigation file until this slug commits, because that seat's pre-write guard refuses to commit over a foreign uncommitted row; it takes the next free id at write. Until it is on the block this row reads disarm ARMED; a reader then resolves the disarm from that row (protocol s.0)"
  ],
  "remedy": "Round 2: the belt-justification correction (cross-firm-secret-deny.tf :6-10 and its copies) rides the round-2 portal-auth face TO-OP-S-1-2 (cells OP-s-1 / OP-s-2, which the decomposition v0.1.4 already contains) as a RIDER with Z-S10's scope bound written in by the disarm owner: all three named roles measured by simulate-principal-policy, one --resource-arns per call, before the sentence is rewritten, plus a measured-at vintage line. The belt itself STAYS (defence in depth over explicit allowlists; a reader must not infer any opal/* secret is already granted). The file's commit lane is CLOUD_OPS_OR_ETL, so the worker on that face carries the edit, not the CTO.",
  "owner": "2.0.0_SA_COO~Z (L6, the rider on TO-OP-S-1-2; worker class 0.7.0_AE_CloudOps; rider text from 1.0.0_SA_CTO~Z's disarm record)",
  "round": "v1",
  "disarm": {
   "state": "ARMED",
   "owner": "1.0.0_SA_CTO~Z",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Z",
   "round": "v2"
  },
  "closed": false,
  "route": "SPEC_ERROR",
  "loop_target": 6
 },
 {
  "id": "NFRA_OPSEC202609-Z-S14",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "opal-partner-demo is live but not Terraform-managed (no resource block in any .tf; absent from every readable state; the estate's own debt baseline lists it as an orphan and its 2026-06-03 provisioning task order says NOT TF-managed); the face's deliverable 3 directed a Terraform edit on it, and named partners-api/** as the module's instantiation home when the three real instantiations live in partner-firms/.",
  "evidence": [
   "git ls-files: infra/aws/terraform/partner-firms/{49financial,cottonwood,inflection,main}.tf, each 0 'demo' tokens at HEAD; partners-api/ 4 .tf that are not the module's instantiations",
   "infra/aws/globgrph/comp_debt_baseline.json:17 (DYNAMODB_TABLE/orphan); org/projects/task_orders/ADVI_DEMOAUTH.001.provision-opal-partner-demo.md:22 ('NOT TF-managed'); slice_storage.json:500, re_us-east-1.json:40134 (live)",
   "worker's reads (0.7.0_AE_CloudOps~S): terraform state list on partner-firms (three entries, no demo); describe-table opal-partner-demo (DP=true, SSE AWS-owned, PITR off, created 2026-06-03); its first broken state probe caught by its positive control",
   "issuer's ruling DEFER in 19604; disarm record Z-S15 @2d3ac2b48f; tick-2 verdict (3.0.0_SA_CVO~Z 19607; ledger row 2): adopt by import under OP-s-8's round-2 limb, plan read as the bar; decomp v0.1.4 @c8d58b1004 carries it"
  ],
  "remedy": "Round 2: OP-s-8's import limb -- terraform import of opal-partner-demo into partner-firms/, the plan captured BEFORE any settings change reading 0 to add / 0 to destroy / no 'forces replacement' with deletion_protection_enabled unchanged or true, then the five settings -- a cell the decomposition already contains. The class (live-but-unmanaged identity-plane tables) is a fabric item on the debt baseline, steward 0.7.0_AE_CloudOps, gate CTO (19629).",
  "owner": "2.0.0_SA_COO~Z (L6; worker class 0.7.0_AE_CloudOps)",
  "round": "v1",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~Z",
   "at": "2026-09-03T09:18:00Z"
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Z",
   "round": "v2"
  },
  "closed": false,
  "route": "SPEC_ERROR",
  "loop_target": 6
 }
]
```
