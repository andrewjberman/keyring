# NFRA_OPSEC202609 -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Assembled by:** `3.0.0_SA_CVO~Z` (L8: the CVO assembles, any seat surfaces -- `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.4).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, folder == project). Lane `ANY`.
**Project state at this write:** L3 @32daebf403, L4 @43b75ffbd6 (PRD v0.4, `dep_stage: PRD`); L5 is
`2.0.0_SA_COO~Z`'s; no task orders yet; L7 has not started. This file is opened BEFORE L7 because the first row
is about the loop's own L10 handoff mechanism on this device, found while the L8 owner read the tool it will use.
**Append-only during the round.** Denominator at this write: **1 row** (S1 appended by `3.0.0_SA_CVO~Z` 07:17Z).
**Denominator at the S3 write: 3 rows** (S3 appended by `0.7.0_AE_CloudOps~S` 2026-09-03T08:01:45Z, L7/TO-OP-S-17-16, BLOCKING/ARMED, worktree at 7c6dc7dca6). The line above is `3.0.0_SA_CVO~Z`'s and is left as written. This count is the file's state at THIS write only: the channel is lane-ANY and other seats append concurrently -- S2 was appended by `0.7.0_AE_CloudOps~Z` between this seat's read and its write.
**UPDATE 08:1xZ by `3.0.0_SA_CVO~Z` (narrative only; the json block is untouched):** L6 landed @5494591e91 (four
task orders), `dep_stage: EXECUTING` @94b6fd0d11, L7 OPEN; S2 committed @7c6dc7dca6, S3 @d59b3734c3. The S2 and S3
L8 reads below were appended at this write; no row was added or changed by it.

## L8 read -- what the CVO checked on each row

- **S1** (surfaced by `3.0.0_SA_CVO~Z` directly; the row is its first home, no message precursor). Grounding
  RESOLVES at this seat: the three cited lines of `.tools/prd-header-notify.py` read as quoted at @e906c6f156,
  and the same tool's L4 path was EXERCISED on this project minutes earlier -- its `[PRD LANDED]` row 19465 sits
  `QUEUED` at the BASE serial `2.0.0_SA_COO` (delivery state read at this seat), while every live site-Z seat is
  a `~Z` lane and the base inboxes are unwatched here. Held `UNDER_INVESTIGATION`: the DISARM is an act at L10
  (a lane-addressed pointer beside the mechanical re-offer), which has not happened yet, and DISARMED is not
  REMEDIATED -- the remedy is a lane-aware recipient in the tool, owned by the gate/notifier surface. Nothing to
  route now; a route needs every task order terminal, and none exists. UPDATE 07:4xZ: the remedy is in flight on the
  laptop @e58250f261 (LOCAL there, relayed by `0.0.0_AB_MSTR~Z` 19497); closing condition (b) is met only when a
  route notification reads READ at a `~Z` lane on this device with no hand-sent pointer, which cannot happen before
  that commit reaches SITEZ.

- **S2** (surfaced by `0.7.0_AE_CloudOps~Z` during the GO's mandated re-grounding of OP-s-3; committed @7c6dc7dca6 with
  the task order's `staged -> pending` flip. First written 08:00Z with three off-enum fields -- `class: HAZARD`,
  `disposition: OPEN`, a non-digit timestamp -- and corrected by the worker before its commit; the mechanical
  validator reads 0 errors at HEAD). Grounding RESOLVES at this seat on a different instrument from the worker's
  tree read: `infra/aws/terraform/portal-auth/secrets.tf:5-7` and `main.tf:20-24` read exactly as quoted at
  @94b6fd0d11 via `git show` at the pin (negative control on a bogus path at the same pin fails loud); the face's
  deliverable 2 carries "never a literal" and S3-AC1 carries the "its VALUE appears in zero files of the commit"
  control at line 33. ⚠ This seat FIRST reported that phrase ABSENT (an enumerate whose three hits on line 33 were
  display-trimmed before the phrase; the issuer corrected it in 19504; re-measured here with the phrase alone: 1
  hit) -- a false zero read from a partial view, recorded so the correction is on the face. The four AWS reads
  (state bucket SSE-S3 + full public-access-block + versioning Enabled + `NoSuchLifecycleConfiguration`; CloudFront
  7 origins, 0 custom headers) are the worker's and stand as theirs. DISARM: recorded by the issuer
  `2.0.0_SA_COO~Z` as design call (a) -- state-at-rest ACCEPTED on the measured mitigations, wording clarifications
  inside deliverables the worker already owns (the secrets.tf invariant scoped to the JWT keypair; the runbook names
  the state-history residual), no criterion changed, no route -- in message 19504 and an operating note to the
  worker. ⛔ NOT YET A ROW: the file's `hazard_standing` still reads ARMED because the schema cannot express DISARMED
  (the D1_CATVIEWS-S5 gap) and the disarm record has no row of its own; the L10 precondition reads rows, so a disarm
  row citing this id (the D1_CATVIEWS-Z-S4 shape) is the carrier the round will need. Routed OUT of this project by
  the issuer: the state bucket's missing noncurrent-version expiry (owner = whoever declares the backend bucket).
  Held `UNDER_INVESTIGATION` until the round's L9 slug; on the grounding bar as it stands it GRADUATES, and with (a)
  recorded it takes no route.

- **S3** (surfaced by `0.7.0_AE_CloudOps~S` re-grounding TO-OP-S-17-16's "today" claims as its first act; committed
  @d59b3734c3 with the task order's `staged -> pending` flip; BLOCKING, so it also reached the issuer by message in
  the same turn -- the worker's act, as the GO requires). Grounding RESOLVES at this seat on four instruments that
  are not the worker's kms/dynamodb reads: the TO face @5494591e91 :48 "The estate CMK, never a new key. Read its ARN
  from Terraform (portal-auth/dynamodb.tf), never from a console" and :23 "SSE-KMS on the estate CMK with bucket-key
  enabled"; the PRD @43b75ffbd6 :401 C-8, :410-411 C-9, and the s.8 manifest labels S8 :454 / S9 :455 "(CMK, ...)";
  the HEAD blobs of `portal-auth/dynamodb.tf` (238 lines) and `shared-infra/dynamo.tf` (92 lines) carry ZERO lines
  matching kms / server_side_encryption / deletion_protection / 86cc6c40 (positive controls: 7 and 2 `resource`
  lines), so the BOUNDS' prescribed read cannot return an ARN; and the RECORDED plane corroborates the key's
  identity independently of `describe-key`: `infra/aws/nfra_terraform_p1/slice_storage.json:1361` and `:1427-1428`
  record `alias/aws/dynamodb` as "AWS-managed CMK (alias/aws/dynamodb) -- created/rotated by AWS, external-by-design",
  and `docs/briefs/security-scan-track1-findings-20260603.md:55` says most KMS-SSE in the account uses the
  aws-managed `aws/dynamodb` key. THE MECHANISM, which is the L8 finding on top of the row: "CMK" in this estate's
  own records names BOTH KeyManager=CUSTOMER and KeyManager=AWS keys. The brief's 09-02 read carried the word into
  the PRD's manifest labels and into C-8/C-9, into the decomposition (never re-measured, by its own statement) and
  into the TO's BOUNDS -- four limbs, each citing the one before; the worker's re-grounding is the first act that
  read the key's KeyManager instead of its label. Nothing here is the worker's error or the face's alone. DISARM of
  the WORK recorded by the issuer (19504 + operating note): the table proceeds to C-9 as measured
  (opal-users-v2's exact APPLIED shape, AWS-managed); the bucket proceeds with SSE-S3 as the INTERIM and every
  non-encryption property; S17-AC1's KMS limb is filed UNCOMPUTABLE-BY-CONSTRUCTION citing this row; nobody picks a
  key mid-round. The SPEC question is routed UP by the issuer to `1.0.0_SA_CTO~Z` (L4): C-8 and C-9 name a key that
  does not exist as a CMK; the issuer's rec is one customer-managed key for the project (bucket + table). ⛔ NOT YET A
  ROW, same note as S2. Held `UNDER_INVESTIGATION` until the L9 slug; on the grounding bar it GRADUATES; at the stamp
  it reads as a contradiction of a RATIFIED constraint (C-8, with the S8/S9 labels), which is the `SCOPE_CHANGE`
  shape to L2 naming C-8 -- unless the CTO's L4 version bump lands before the round closes, in which case the
  remediation is a round-2 task order and no route is needed. Stated, not stamped: no route exists while three task
  orders are open.

```json
[
 {
  "id": "NFRA_OPSEC202609-Z-S1",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z (L8 owner, reading the L10 handoff tool before the act)",
  "surfaced_at": "2026-09-03T07:17:37Z",
  "one_line": "The L10 route handoff (.tools/prd-header-notify.py kind:route) and the L4 handoff in the same tool address BASE serials (RECIPIENT default 2.0.0_SA_COO; ROUTE_OWNER {2: 1.0.0_SA_CTO, 5: 2.0.0_SA_COO, 6: 2.0.0_SA_COO}) with no lane resolution -- on site Z every live seat is a ~Z lane and the base inboxes are unwatched, so the notification re-offers until READ to an inbox nobody reads; already exercised on this project at L4 (row 19465 QUEUED at 2.0.0_SA_COO, 0 rows at 2.0.0_SA_COO~Z).",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "3.0.0_SA_CVO~Z -- DISARM at L10 (not yet due): beside the mechanical route notification, send the stamped row's pointer to the route owner's LIVE lane serial on this device (2.0.0_SA_COO~Z or 1.0.0_SA_CTO~Z), the same act 1.0.0_SA_CTO~Z performed for the L4 -> L5 handoff (msg 19471). The L4 instance is already disarmed by that pointer. DISARMED != REMEDIATED: the remedy is 1.0.0_SA_CTO's (notifier/gate surface).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    ".tools/prd-header-notify.py:49 @e906c6f156 -- RECIPIENT = os.environ.get(\"PRD_NOTIFY_TO\", \"2.0.0_SA_COO\") -- a BASE serial, env-overridable for the L4 path only",
    ".tools/prd-header-notify.py:68 @e906c6f156 -- ROUTE_OWNER = {2: \"1.0.0_SA_CTO\", 5: \"2.0.0_SA_COO\", 6: \"2.0.0_SA_COO\"} -- BASE serials, no env override, no lane lookup",
    ".tools/prd-header-notify.py:364 @e906c6f156 -- the route send passes \"to\": owner straight from ROUTE_OWNER; :101 owner = ROUTE_OWNER.get(t); nothing between them consults liveness or a lane",
    "EXERCISED on this project, L4 path: get_delivery_state(message_id=19465) read at 3.0.0_SA_CVO~Z 2026-09-03T07:1xZ -> QUEUED, 1.0.0_SA_CTO~Z -> 2.0.0_SA_COO, 'no clock stamps yet'; 1.0.0_SA_CTO~Z 19471 reports 0 rows at 2.0.0_SA_COO~Z for it",
    "get_live_agents at 3.0.0_SA_CVO~Z 2026-09-03T06:49Z: 4 live -- 0.0.0_AB_MSTR~Z, 1.0.0_SA_CTO~Z, 2.0.0_SA_COO~Z, 3.0.0_SA_CVO~Z -- no base serial registered on this device; org/XXX.md: a lane's inbox is org/mcp/inbox/{base}/~{lane}/ and the base inbox is a different directory",
    "org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md v2.3 L10 Tool: '.tools/prd-header-notify.py kind:route delivers a new route row to its owner and re-offers until READ'; Handoff: 'the stamped row to the route owner and to no one else'",
    "the L4 workaround that disarms one instance: 1.0.0_SA_CTO~Z 19471 sent the same identity to 2.0.0_SA_COO~Z by message and named the QUEUED base row -- the handoff reached its owner by a second carrier, not by the notifier"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Spine L10: 'prd-header-notify.py kind:route delivers a new route row to its owner and re-offers until READ' and 'the stamped row to the route owner and to no one else'; spine L4: 'prd-header-notify.py (post-commit) delivers a new or bumped header to 2.0.0_SA_COO and re-offers until READ. The handoff to L5 is that notification, never a dispatch.'",
  "world_is": "On site Z the owner named by the tool is a BASE serial that is not registered and whose inbox no Monitor watches; the notification is written and re-offered to a dead inbox indefinitely (READ never arrives, so the re-offer never stops), and the loop's L4 -> L5 and L10 -> owner handoffs reach their owners only by a second, hand-sent carrier. The tool's docstring names the very failure ('COO would never have been told') and the mechanism reproduces it one axis over -- right seat class, wrong instance.",
  "notes": "WHY A ROW AND NOT A MESSAGE: it is a spec-vs-world mismatch on this project's own loop, found off-task by the seat that will run L10; the row is the carrier. NOT CHASED: no edit to the tool from this seat -- a live post-commit hook edit in the shared tree is the never-rules-gate outage shape, and the surface is 1.0.0_SA_CTO's. REMEDY SHAPE, offered not prescribed: resolve the owner's live lane on the sending device (the broker's live-agents view already carries it), falling back to the base serial only when no lane of that base is live; or an env override for routes in the same shape as PRD_NOTIFY_TO. CLOSING CONDITION: (a) DISARMED when the L10 stamp on this project is followed by a lane-addressed pointer that reads READ on the delivery ledger; (b) REMEDIATED when a route notification on this device reads READ at a ~Z lane with no hand-sent pointer beside it (that is the falsifier: the mechanical carrier alone reaches the owner). The L4 instance (19465) stays QUEUED as a measured artifact of the defect; nobody should ack it from the base serial to make the number look right."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S2",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~Z (L7 worker, OP-s-3, during the mandated pre-write re-grounding)",
  "surfaced_at": "2026-09-03T08:00:11Z",
  "one_line": "TO-OP-S-3 deliverable 2 prescribes that Terraform read the origin secret via a data source and set it as a CloudFront custom_header; a custom origin header VALUE is returned in full by cloudfront:GetDistributionConfig and is therefore written into terraform state BY CONSTRUCTION -- which contradicts the portal-auth module's own stated invariant at secrets.tf:5-7 ('Manages the secret CONTAINERS only ... aws_secretsmanager_secret_version is intentionally omitted so that key material never enters Terraform state'). The state bucket has versioning ENABLED and NO lifecycle configuration, so every superseded value persists as a noncurrent object indefinitely -- a rotation (deliverable 4) retires the value from the live header but NOT from state history.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z (issuer) -- this is a DESIGN call on deliverable 2, not a defect in the worker's execution. The TO's own S3-AC1 control ('its VALUE appears in zero files of the commit') is SATISFIABLE as written and this row does not block it: state is not a file in the commit, so the criterion passes while the value still lands somewhere durable. DISARM = the issuer either (a) accepts state-at-rest as the resting place, on the measured mitigations below, or (b) names a different mechanism. NOT BLOCKING: the cell is buildable as specified and this seat is proceeding.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "infra/aws/terraform/portal-auth/secrets.tf:5-7 @94b6fd0d11 -- 'Manages the secret CONTAINERS only -- never the secret values. aws_secretsmanager_secret_version is intentionally omitted so that key material never enters Terraform state.' The module states the invariant explicitly; this cell's prescribed mechanism breaks it.",
    "infra/aws/terraform/portal-auth/main.tf:20-24 @94b6fd0d11 -- backend s3, bucket opal-313476888478-terraform-state, key portal-auth/tfstate, region us-east-1.",
    "MEASURED at this seat 2026-09-03: aws s3api get-bucket-encryption -> SSE-S3 AES256 default, SSE-C blocked; get-public-access-block -> all four true; get-bucket-versioning -> Status Enabled.",
    "MEASURED at this seat 2026-09-03: aws s3api get-bucket-lifecycle-configuration -> NoSuchLifecycleConfiguration (rc=254). Versioning Enabled + zero lifecycle = noncurrent versions are retained with no expiry.",
    "MEASURED at this seat 2026-09-03: aws cloudfront get-distribution-config --id EVTSA9VEHNZVH returns CustomHeaders per origin; origin DENOMINATOR 7, CustomHeaderCount 0 on all 7 today. The API returns header VALUES, which is why a refresh writes them to state regardless of how the header was set -- the exposure is not avoidable by choosing a different write path (console, CLI, or ignore_changes all still refresh into state).",
    "TO face NFRA_OPSEC202609.TO-OP-S-3 deliverable 2 @5494591e91 -- 'Terraform reads the value from the secret at plan time (data source), never a literal'; deliverable 1 -- 'No value in any file, log or commit message.'"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-OP-S-3 deliverable 1: 'No value in any file, log or commit message.' Deliverable 2: 'Terraform reads the value from the secret at plan time (data source), never a literal.' portal-auth/secrets.tf:5-7: 'key material never enters Terraform state.'",
  "world_is": "A CloudFront custom origin header value is a readable attribute of the distribution config, so it is persisted in terraform state by construction and no write path avoids it. The portal-auth state lives at s3://opal-313476888478-terraform-state/portal-auth/tfstate with SSE-S3 + full public-access-block (so it is encrypted at rest and not public), but versioning is Enabled with NO lifecycle configuration, so every superseded state object -- and every origin-secret value it carries -- is retained indefinitely. The literal wording of deliverable 1 is still satisfiable (state is not a file, log, or commit message), so the acceptance criteria pass while the invariant secrets.tf states for this module does not hold for the new secret.",
  "notes": "WHY A ROW AND NOT A MESSAGE: it is a spec-vs-world divergence found during the GO's mandated re-grounding, and the face names the row as the carrier. NOT BLOCKING, so it does not also reach the issuer this turn -- the cell is buildable exactly as written and this seat is continuing. SCOPE OF THE CLAIM: this is about where the value RESTS, not about whether the design works; the origin-secret mechanism itself is sound and is the right fix for the constant-header finding (brief F1). WHAT THIS ROW IS NOT: it is not an argument for a literal in the .tf (strictly worse) and not an argument against the cell. REMEDY SHAPES, offered not prescribed, for the issuer to weigh: (a) accept it -- state is encrypted, private, and already holds other sensitive material, and record that secrets.tf's invariant is now scoped to the JWT keypair rather than the module; (b) add a noncurrent-version expiry lifecycle to the state bucket so a rotation actually ages out prior values, which is the cheapest change and the one that makes deliverable 4's rotation mean what it says; (c) a different header mechanism. NOTE (b) IS A SEPARATE LANE -- the state bucket is not this cell's surface and this seat did not touch it. FALSIFIER for anyone re-checking: if a future get-bucket-lifecycle-configuration on opal-313476888478-terraform-state returns a noncurrent-expiry rule, the indefinite-retention half of this row is discharged and only the invariant half stands."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S3",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~S (L7 worker, TO-OP-S-17-16, re-grounding the face's 'today' claims before first write)",
  "surfaced_at": "2026-09-03T08:01:45Z",
  "one_line": "The key the PRD and TO call 'the estate CMK' (86cc6c40-2387-4446-b7e1-de79392e06b3) is NOT a customer-managed key: KeyManager=AWS, sole alias alias/aws/dynamodb, description 'Default key that protects my DynamoDB data when no other key is defined'. It is the AWS-managed DynamoDB service key. An S3 bucket cannot be encrypted with it and its key policy cannot be edited, so C-8's 'SSE-KMS on the estate CMK with bucket-key enabled' for opal-data-security is UNSATISFIABLE as written; the account holds no general-purpose customer-managed key. The C-9 table half is NOT blocked -- 'the one opal-users-v2 uses' reproduces exactly as server_side_encryption{enabled=true} (AWS-managed).",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z (issuer, L6) -- the encryption key for opal-data-security is a SPEC decision this seat may not make: the TO BOUNDS say 'the estate CMK, never a new key', and the only readings that satisfy C-8's security property require either a NEW customer-managed key (a bound change) or SSE-S3/AES256 (a weaker property than C-8 states). Rule 27 routes a spec error to L6; if the defect is judged to sit in PRD s.7.3/7.6 rather than the face, L6 routes it onward to L4. SURFACED, NOT ADJUDICATED. DISARM = the issuer names which key the bucket uses, in writing, on the face or by ruling.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "aws kms describe-key --key-id 86cc6c40-2387-4446-b7e1-de79392e06b3 -> KeyMetadata.KeyManager='AWS', KeyState='Enabled', Description='Default key that protects my DynamoDB data when no other key is defined'; read at this seat 2026-09-03T07:5xZ (live plane, us-east-1, account 313476888478)",
    "aws kms list-aliases --key-id 86cc6c40-2387-4446-b7e1-de79392e06b3 -> exactly one alias: alias/aws/dynamodb",
    "POSITIVE CONTROL (the probe discriminates, so 'AWS' is not an instrument artifact): the same describe-key over every key from aws kms list-keys returns KeyManager=CUSTOMER for 4ba4753c(alias/inf-ebs-key), 6090ba42(alias/agentbus-alyssa01), 72c5bf64(alias/agentbus-sim01), 8863d4ac(alias/schwab-sdd-session) and KeyManager=AWS for the aws/* service keys -- denominator 11 keys read",
    "NO GENERAL-PURPOSE ESTATE CMK EXISTS: of those 11, the only CUSTOMER-managed keys are the four purpose-specific ones above (EBS, two agentbus queues, a Schwab session key); none is an estate-wide data-at-rest CMK",
    "aws dynamodb describe-table --table-name opal-users-v2 -> SSEDescription={Status=ENABLED, SSEType=KMS, KMSMasterKeyArn=arn:aws:kms:us-east-1:313476888478:key/86cc6c40-2387-4446-b7e1-de79392e06b3}, DeletionProtectionEnabled=false, StreamSpecification=null -- the face's own referent resolves to the AWS-managed key",
    "comp-read infra/aws/terraform/portal-auth/dynamodb.tf --enumerate '(?i)kms|86cc6c40|point_in_time|deletion_protection|server_side_encryption' -> 1 hit across 238 lines, and it is a COMMENT at :170; ZERO kms / server_side_encryption / deletion_protection declarations. The TO BOUNDS name this file as the ARN's source and it does not carry it (case-insensitive; a prior case-sensitive pass returned the same shape)",
    "comp-read infra/aws/terraform/shared-infra/dynamo.tf --enumerate (same pattern) -> 4 hits: opal-users-v2 declared at :16, point_in_time_recovery at :58, and NO server_side_encryption / deletion_protection / kms -- the live table's SSE-KMS and the declaration disagree (DESIRED != APPLIED on the estate's own reference table)",
    "comp-find '86cc6c40' corpus=all -> DENOMINATOR 784 hits across 50949 files scanned; every hit is a census/report CONFIG or DOC artifact (nfra_terraform_p1 slices, AWS_ESTATE_CENSUS_20260730, worldmodel census, this seat's own tool log) -- the id appears in NO infra/aws/terraform/*.tf declaration",
    "aws s3api head-bucket --bucket opal-data-security -> 404 Not Found; aws dynamodb describe-table --table-name opal-suspicious-addresses -> ResourceNotFoundException; positive control opal-users-v2 -> ACTIVE. The face's 'absent' premise for both resources HOLDS at this vintage",
    "comp-find '(?i)opal-data-security|opal-suspicious-addresses' --files infra/aws/terraform -> 0 hits across 524 files scanned; neither resource is Terraform-declared anywhere"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-OP-S-17-16 DELIVERABLE 2 and PRD s.7.6 C-8: opal-data-security is 'SSE-KMS on the estate CMK with bucket-key enabled'. DELIVERABLE 1 and C-9: the table carries 'SSE with the estate CMK (86cc6c40..., the one opal-users-v2 uses -- read its ARN from the existing Terraform, never retype it)'. TO BOUNDS: 'The estate CMK, never a new key. Read its ARN from Terraform (portal-auth/dynamodb.tf), never from a console.' The wording treats 86cc6c40 as one customer-managed estate key usable by both S3 and DynamoDB.",
  "world_is": "86cc6c40-2387-4446-b7e1-de79392e06b3 is KeyManager=AWS -- the AWS-MANAGED DynamoDB default service key (alias/aws/dynamodb), not a CMK. Three consequences, each measured or structural: (1) an AWS-managed service key is usable only by its owning service, so an S3 bucket CANNOT specify it for SSE-KMS -- C-8 as written cannot be applied; (2) its key policy is AWS-owned and not editable and no grants can be scoped on it, which is exactly the control C-8 is buying when it says an altered case file must leave the original and principals must be scoped -- so even where it applies, the stated security property is not delivered; (3) the ARN is absent from portal-auth/dynamodb.tf, so the BOUNDS' prescribed read is impossible and the value can only come from the applied plane or a census artifact. The account holds no general-purpose customer-managed key to substitute. The C-9 half is satisfiable: reproducing opal-users-v2 exactly means server_side_encryption{enabled=true} with no kms_key_arn, which IS the AWS-managed key the face points at.",
  "notes": "WHY A ROW: a spec-vs-world divergence found while re-grounding the face's 'today' claims, which the GO named as this seat's FIRST ACT. BLOCKING, so per the GO it also reaches 2.0.0_SA_COO~Z by message in the same turn -- the row is the carrier, the message is the blocking-class notification, not a substitute for it. NOT CHASED and NOT SELF-RESOLVED: this seat did not pick a key. Choosing one would be an off-spec act mid-round (Rule 27, spec FROZEN) and would silently trade away a stated security property. WORK CONTINUES around it: the DynamoDB table (OP-s-16) is fully buildable and proceeds, as does every non-encryption property of the bucket (public-access blocks, versioning, TLS deny, principal allow-list, access logging, waf-logs/ lifecycle). REMEDY SHAPE, offered not prescribed -- (a) mint a dedicated customer-managed CMK for the evidence store, which is the only option that delivers C-8's stated property (editable key policy + scoped grants) but changes the 'never a new key' bound; (b) SSE-S3/AES256 at round 1, which needs no key and no bound change but is strictly weaker than C-8 says; (c) re-point at an existing CUSTOMER key -- rejected on inspection, all four are purpose-specific and borrowing one couples the evidence store to an unrelated blast radius. This seat recommends (a) and holds. CLOSING CONDITION: DISARMED when the issuer names the key in writing; REMEDIATED when get-bucket-encryption on the applied bucket reads the named key and the face's wording no longer calls an AWS-managed key a CMK. FALSIFIER for this row: a describe-key on 86cc6c40 returning KeyManager=CUSTOMER, or an S3 bucket in this account demonstrably encrypted with alias/aws/dynamodb."
 }
]
```
