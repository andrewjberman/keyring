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
  orders are open. UPDATE 08:1xZ: the L4 bump LANDED -- PRD v0.5 @a3cad58b0d names ONE project customer-managed key
  `alias/opal-security` (new C-13, manifest S25); both owners now read the stamp the same way (`1.0.0_SA_CTO~Z` 19515,
  `2.0.0_SA_COO~Z` 19528 withdrawing its SCOPE_CHANGE wording): Z-S3 GRADUATES with the L4 bump as its remedy and
  takes no route unless Andrew reverses v0.5 before the close.

- **S4** (surfaced by `0.7.0_AE_CloudOps~S` re-grounding bound (b)'s principals before authoring the bucket policy;
  committed @cdbdcb473c with the opsec module; BLOCKING, so it also reached the issuer by message the same turn).
  Grounding RESOLVES at this seat on instruments other than the worker's IAM/STS reads: the face @5494591e91 carries
  the deliverable-2(b) and bound-(b) clauses at :23 and :47 (8 enumerate hits / 85 lines on the five quoted phrases);
  the PRD carried the same absent referent -- v0.5 @a3cad58b0d :405 (C-8) "sentinel, reconciler and CTO-admin roles"
  and :438 (C-13, minted twelve minutes before this row was read) -- so the principal Z-S4 measured absent sat in the
  ratified constraint AND in the constraint just added; the repo census (`comp-find -i 'cto-admin|terraform-apply
  role|terraform apply role'`: 35 hits / 50,969 files) finds the names ONLY in this project's texts and the day's
  broker messages -- zero in any .tf, IAM census or role declaration. That is a different mechanism from S3: the key
  was a MISLABELLED measured resource; these principals were NEVER MEASURED -- designed names that read as existing
  because they sat beside two that are explicitly new. Qualifier on the row, not a defect: "the applier is
  user/Andrew_Berman" is `sts get-caller-identity` on the worker's shell, a device-scoped fact the conclusion does not
  need (a deny-outside-a-list-of-two-absent-ARNs denies every applier there is). The worker's list-roles (216,
  client-side over 3 pages), 'lambda' control (55) and list-users stand as the worker's. DISARM recorded by the
  issuer (19519 + operating note): (a) DEFER the deny-outside-list statement to the task orders that create the
  principals (OP-s-14 / OP-s-15 / OP-s-19); SecureTransport deny only this round; the four public-access blocks are
  the control -- which is bound (b)'s own rule ("this policy names only the roles that exist today") applied to
  bound (b)'s own list, not a spec change. The issuer owned the defect ("I wrote a bound naming two principals I had
  not measured"). L4 ruled the identity half: PRD v0.6 @b482fe8a5b replaces the six "CTO-admin" referents with ONE
  Terraform-declared role `opal-security-admin` (new C-14, manifest S26); the role's TRUST (which humans may assume it)
  is Andrew's card OP-x-6 and the role is not assumable before his word. At the stamp Z-S4 reads as BOTH the face's
  (SPEC_ERROR -> L6 for the deferred statement, accepted in advance by the issuer) and the PRD's (v0.6, done). ⛔ NOT
  YET A ROW (disarm record), same note as S2/S3. Held `UNDER_INVESTIGATION`; GRADUATES on the grounding bar.

- **S5** (surfaced by `0.7.0_AE_CloudOps~S` authoring the access-logging limb, BEFORE the apply -- a deviation from
  an instruction the issuer had given minutes earlier (19517 listed access logging among what the bucket carries)
  surfaced pre-act rather than reported after; committed @cdbdcb473c; BLOCKING). Grounding RESOLVES at this seat:
  the face @5494591e91 :23 (deliverable 2(c), "CloudTrail/access-logs bucket") and :30 (S17-AC1 `get-bucket-logging`);
  the PRD v0.6 @b482fe8a5b :407-408 C-8 "access logging to the CloudTrail bucket", :482 manifest S5, :494 S17; the
  DESIRED plane: `infra/aws/terraform/shared-infra/s3.tf` @HEAD (444 lines) declares the target at :44-49 with a
  `*** LIVE -- DO NOT REMOVE ***` marker and carries ZERO tokens matching logging.s3 / LogDelivery /
  aws_s3_bucket_logging / cloudtrail.amazonaws.com (positive control: 28 `resource` lines) -- so the two CloudTrail
  policy statements the worker read live are themselves NOT Terraform-declared (a DESIRED != APPLIED on the audit-log
  bucket's policy; an OBSERVATION for that bucket's owner, shared-infra, OUT of this project and not chased here);
  the worker's module `infra/aws/terraform/opsec/s3.tf` (now @cdbdcb473c) carries the `aws_s3_bucket_logging`
  resource COMMENTED at :165 with this row's id at :142, as the row says. The worker's get-bucket-policy /
  get-bucket-acl / describe-trails reads stand as the worker's; its own "UNPROVEN, STATED AS SUCH" line on the
  31-bucket sweep (no positive control) is the honest form and is carried as written. THE L8 FINDING on top of the
  row: the acceptance read S17-AC1 names (`get-bucket-logging`) observes the CONFIGURATION and never the DELIVERY,
  so the silent failure mode (configured, nothing ever delivered) would have PASSED the criterion -- the criterion
  could not tell its two outcomes apart; the CTO's v0.7 wrote that into C-15's own violation list. DISARM recorded
  by the issuer (19534 + operating note): DEFER; the limb stays authored-and-commented; S17-AC1's logging read files
  UNCOMPUTABLE-BY-CONSTRUCTION citing this row; the audit-log bucket is not touched (never-widen); the other seven
  resources applied (plan 7/0/0, ledger entry open). L4 ruled: PRD v0.7 @237265f9f1 "OWN TARGET" -- a project-owned
  `opal-data-security-access-logs` bucket (new C-15, manifest S27), graded by a DELIVERED object under the prefix,
  never `get-bucket-logging`; the additive-grant alternative rejected on the never-widen bar. At the stamp Z-S5 reads
  as the PRD's (v0.7, done) plus the face's acceptance-read re-cut (SPEC_ERROR -> L6, named by the issuer). ⛔ NOT YET
  A ROW (disarm record). Held `UNDER_INVESTIGATION`; GRADUATES on the grounding bar.

- **THE ROUND'S PATTERN, read at L8 (S3 + S4 + S5):** three referents of ONE ratified constraint (C-8: the key,
  the roles, the target) were asserted from the brief's 09-02 reading and never read at a vintage until a worker's
  mandated re-grounding -- and each limb between them cited the one before (brief -> PRD -> decomposition, whose own
  preflight honestly declared "NOT re-measured on 2026-09-03" -> task order). Three mechanisms under one shape: a
  measured resource wearing the wrong label (S3), names never measured at all (S4), a real resource assumed to permit
  a delivery it does not (S5). Both L4 and L6 owners have banked the rule (one live read per named referent before a
  task order commits; a constraint names no resource it has not read at a vintage) and the PRD's s.6 now carries it
  in its own words. Recorded here so the L9 slug adjudicates the class once, not three times.

- **NEAR-MISS, measured, not a row:** at 08:24Z `git status` showed the worker's `infra/aws/terraform/opsec/.terraform/`
  tree STAGED, including `terraform-provider-aws_v5.100.0_x5.exe` (718,820,352 bytes on disk) and
  `opsec-round1.tfplan` -- the exact shape `.gitignore:199-205` records as having stranded every push once
  (GitHub rejects >100 MB). At 08:29Z the index and HEAD @cdbdcb473c carry only `.terraform.lock.hcl` + three `.tf`
  files; `.terraform/` and the tfplan read `!!` (ignored). The rule and the worker's discipline held; nothing was
  committed; nothing to disarm. Stated so the next reader of a raw `git status` on this device knows the shape.

- **CORRECTION OF THE RECORD by `3.0.0_SA_CVO~Z` (08:3xZ):** commit bc8d92e39e, authored by this seat, carried
  rows Z-S6, Z-S7 and Z-S8 -- `2.0.0_SA_COO~Z`'s DISARM RECORDS for Z-S2/Z-S3/Z-S4, appended 08:31Z between this seat's
  narrative edit and its commit -- under this seat's git author line, and its commit message said "no row added, no
  row changed". That sentence is FALSE: +3 rows. The rows' provenance is IN-BAND (`surfaced_by` 2.0.0_SA_COO~Z on
  each), which is what the channel and the L10 gate read, so the record's substance is right and only the commit
  metadata and that sentence are wrong; nothing is rewritten. Mechanism, stated so it is not chased: two seats, one
  shared worktree, no gate on the window between an Edit and a safe-commit -- and this seat's own pre-commit check
  PRINTED "json block differs from HEAD" without refusing. Every later commit of this file from this seat is gated:
  it does not run unless the fenced json block is byte-identical to HEAD and the diff is one narrative hunk (the
  gate refused once already, at 08:38Z, over a worker's uncommitted Z-S10 -- so this line may itself ride another
  seat's append-only commit, which the in-band attribution above makes harmless). Reported to the rows' author and the
  integrator at 19541/19542 before this line; the author's ACK 19543 confirms no harm on the record. Z-S9 (the Z-S5
  disarm record) was committed by its author @2c9fa3a440. The round's four ARMED items (Z-S2..S5) each carry a
  disarm record (Z-S6..S9); dispositions stay at L9.

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
 },
 {
  "id": "NFRA_OPSEC202609-Z-S4",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~S (L7 worker, TO-OP-S-17-16, re-grounding bound (b)'s principals before authoring the bucket policy)",
  "surfaced_at": "2026-09-03T08:11:49Z",
  "one_line": "TO bound (b) requires the opal-data-security bucket policy to deny every principal outside an explicit list that 'at this round is the CTO-admin role and the account's Terraform-apply role'. NEITHER ROLE EXISTS: 0 of 216 IAM roles match admin|cto|terraform case-insensitively (positive control: 55 match 'lambda'). The actual Terraform applier is an IAM USER, arn:aws:iam::313476888478:user/Andrew_Berman. Writing the deny-outside-list statement as specified would deny EVERY principal including the applier, bricking the bucket at the moment of its own creation -- the fixture exercise and all six S17-AC1 reads would fail, and recovery needs root.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z (issuer, L6) -- naming the principals is a SPEC act this seat may not perform. Bound (b) is self-refuting as written: it says 'a bucket policy cannot name an absent role' and then names two absent roles. SURFACED, NOT ADJUDICATED. DISARM = the issuer names the real principal(s) in writing, or rules the deny-outside-list statement DEFERRED to the round that creates the sentinel/reconciler roles (OP-s-14 / OP-s-15 / OP-s-19), which bound (b) already contemplates as the extenders of this policy.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "aws iam list-roles, ALL pages collected and counted CLIENT-SIDE -> 216 roles. (The naive 'aws iam list-roles --query length(Roles)' printed 100 / 100 / 16 -- three PAGE counts, the CLAUDE.md 22a pagination trap; 216 is the client-side count, not a page.)",
    "case-insensitive match over those 216 role names for 'admin|cto|terraform' -> 0 hits, and the names printed as '(none)'",
    "POSITIVE CONTROL on the same file and matcher: 'lambda' -> 55 hits, so the matcher and the collected file work and the zero above is a real absence, not a broken probe",
    "aws sts get-caller-identity -> arn:aws:iam::313476888478:user/Andrew_Berman -- the applying principal on this device is an IAM USER, not a role",
    "aws iam list-users -> agentbus-alyssa01-fleet-alyssa-user, Andrew_Berman, Andrew_Berman_Console, github-actions-portal, opal-portal-dashboard, Opal_Terminal, patricia@thewhitelabelcreative.com -- no user named for a CTO-admin or Terraform-apply function either",
    "TO-OP-S-17-16 DELIVERABLE 2(b) and BOUND (b), quoted: 'denies every principal outside an explicit list -- at this round the list is the CTO-admin role and the account's Terraform-apply role' / 'No principal that does not exist yet. ... this policy names only the roles that exist today and says so.'"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The face asserts that two named principals -- 'the CTO-admin role' and 'the account's Terraform-apply role' -- EXIST TODAY and are therefore safe to name in a deny-outside-list bucket policy, in explicit contrast to the sentinel/reconciler/CLI roles which do not yet exist. Bound (b) states the governing rule: 'a bucket policy cannot name an absent role.'",
  "world_is": "Both named principals are absent. 0 of 216 IAM roles match admin|cto|terraform; the Terraform applier on this device is the IAM user Andrew_Berman. The rule bound (b) states is correct and it invalidates bound (b)'s own list. Applying the statement as written is not merely unsatisfiable like Z-S3's key -- it is ACTIVELY DESTRUCTIVE: an S3 bucket policy denying all principals outside a list of two nonexistent ARNs denies the applier too, so the fixture exercise (S17-AC2) and all six applied-plane reads (S17-AC1) would fail against the bucket this TO just created, and clearing it would require the account root principal. The hazard is realised at APPLY time, not later.",
  "notes": "WHY A ROW: a spec-vs-world divergence found while re-grounding bound (b)'s principals, which is the GO's named FIRST ACT applied to the second half of the deliverable. Same failure SHAPE as Z-S3 (a face asserting a referent that does not exist) but a different and larger consequence, so it is a separate item rather than an amendment to Z-S3. BLOCKING, so it reaches 2.0.0_SA_COO~Z by message this turn per the GO. NOT CHASED and NOT SELF-RESOLVED: this seat did not substitute a principal. Naming user/Andrew_Berman in a security-evidence bucket policy is a real access-control decision with an identity-plane consequence, not a typo fix, and mid-round the spec is FROZEN (Rule 27). WORK CONTINUES: the table (OP-s-16) is entirely unaffected and is being built; so is every other bucket property -- the four public-access blocks, versioning, SSE-S3 interim per 19501, access logging to opal-cloudtrail-logs-313476888478, the waf-logs/ lifecycle, the four prefixes, no Object Lock. The bucket policy is authored with its SecureTransport deny ONLY (that statement is principal-independent and safe), with the deny-outside-list statement HELD and a Terraform comment naming this row. REMEDY SHAPES, offered not prescribed: (a) DEFER the deny-outside-list statement to OP-s-14/15/19, which bound (b) already names as this policy's extenders -- the bucket is not public in the meantime because all four public-access blocks are ON and the account is single-tenant; (b) name the real applying principal(s) explicitly; (c) create the two roles first as their own cell. This seat recommends (a) and holds: it needs no new identity decision and no new principal, and it leaves the policy exactly where bound (b) says the later cells will extend it. CLOSING CONDITION: DISARMED when the issuer rules; REMEDIATED when get-bucket-policy on the applied bucket reads a principal list whose every ARN resolves live. FALSIFIER: an aws iam get-role returning a CTO-admin or Terraform-apply role in this account."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S5",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~S (L7 worker, TO-OP-S-17-16, authoring the C-8 access-logging limb)",
  "surfaced_at": "2026-09-03T08:23:20Z",
  "one_line": "C-8's server-access-logging limb cannot be applied without modifying a bucket this task order does not own. The target opal-cloudtrail-logs-313476888478 EXISTS and IS Terraform-declared (shared-infra/s3.tf:48, so the mandate's step-2 STOP correctly did not fire), but it grants only cloudtrail.amazonaws.com (s3:GetBucketAcl + s3:PutObject) and its ACL holds exactly one CanonicalUser FULL_CONTROL grant -- there is NO grant to logging.s3.amazonaws.com and NO LogDelivery group grant. S3 server access logging requires one of those on the TARGET. The limb is authored but COMMENTED OUT in infra/aws/terraform/opsec/s3.tf; every other C-8 property applies this round.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z (issuer, L6). Granting the S3 log-delivery principal on opal-cloudtrail-logs-313476888478 is a change to a bucket owned by the shared-infra module, which the bound 'nothing else rides the apply' and the never-widen rule both refuse to this seat mid-round. Ruling 19517 listed access logging among what the bucket carries at this apply; this row is the measured reason that limb alone is held, surfaced BEFORE the apply rather than reported after. DISARM = the issuer either authorizes the target-bucket grant as its own cell/TO, re-points the target at a bucket that already permits delivery, or defers the limb to OP-s-5 (the logging cell, which delivers into waf-logs/ and must solve the same target-permission question).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "aws s3api get-bucket-policy --bucket opal-cloudtrail-logs-313476888478 -> exactly two statements: Sid=AWSCloudTrailAclCheck (Allow, Principal {\"Service\":\"cloudtrail.amazonaws.com\"}, s3:GetBucketAcl) and Sid=AWSCloudTrailWrite (Allow, same principal, s3:PutObject). No logging.s3.amazonaws.com principal in either.",
    "aws s3api get-bucket-acl --bucket opal-cloudtrail-logs-313476888478 -> grants: 1, type=CanonicalUser, Permission=FULL_CONTROL; LOG-DELIVERY grant present: False",
    "aws cloudtrail describe-trails -> opal-organization-trail (multi-region) delivers to opal-cloudtrail-logs-313476888478; opal-served-key-write-trail delivers to opal-served-key-write-trail-logs -- the target the face means is the first",
    "comp-find 'opal-cloudtrail-logs' -> infra/aws/terraform/shared-infra/s3.tf:48 `bucket = \"opal-cloudtrail-logs-313476888478\"`, tagged Name=opal-cloudtrail-logs, comment '*** LIVE -- DO NOT REMOVE ***'. The target IS Terraform-declared and it is NOT in this module -- that is precisely why this seat may not edit it.",
    "UNPROVEN, STATED AS SUCH: a sweep of get-bucket-logging over all 31 buckets in the account returned no bucket with access logging enabled. That sweep has NO positive control -- with zero configured buckets in the account, an empty render and a broken probe are indistinguishable, so this is NOT evidence that logging is unused estate-wide; it is only the absence of a counter-example."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD s.7.6 C-8 and TO-OP-S-17-16 DELIVERABLE 2(c): the bucket carries 'server access logging to the estate's CloudTrail/access-logs bucket (read its name from the existing Terraform)'. S17-AC1 lists get-bucket-logging (target = the CloudTrail/access-logs bucket) as one of the six reads. Issuer ruling 19517 lists access logging among what the bucket carries at this apply. The spec treats naming the target as sufficient to enable delivery.",
  "world_is": "Naming the target is necessary but NOT sufficient: S3 requires the TARGET bucket to permit the log-delivery principal, and this target permits only CloudTrail. Two failure modes follow and they differ in visibility. If S3 validates the target at PutBucketLogging, the apply FAILS (loud, and it fails the whole safe-apply). If S3 accepts the configuration without validating, get-bucket-logging reads CONFIGURED -- S17-AC1's logging read would PASS -- while no log object is ever delivered: a DESIRED-not-EXERCISED trap that the specified read cannot detect, because the read observes the configuration and never the delivery. The second mode is why this is a row rather than a thing to try and see: the acceptance criterion as written cannot tell the two apart.",
  "notes": "WHY A ROW AND ALSO A MESSAGE: BLOCKING for this limb, and it departs from an instruction the issuer gave minutes earlier (19517), so it is surfaced BEFORE the apply rather than reported after -- a deviation discovered pre-act must not reach the issuer as a fait accompli. NOT CHASED: this seat did not add the grant to opal-cloudtrail-logs-313476888478. That bucket belongs to shared-infra, holds the account's CloudTrail audit log, and carries a DO-NOT-REMOVE marker; widening its policy to satisfy a limb of another module is exactly the never-widen and 'nothing else rides the apply' shape. THE LIMB IS AUTHORED, NOT DELETED: the aws_s3_bucket_logging resource sits commented in infra/aws/terraform/opsec/s3.tf with the measurement and this row id beside it, so landing it later is an uncomment, not a rediscovery. S17-AC1's logging read files UNCOMPUTABLE-BY-CONSTRUCTION citing this row unless the issuer rules otherwise before the apply. NOTE FOR OP-s-5: that cell delivers WAF/ALB logs into waf-logs/ and will meet the SAME target-permission question one layer over; solving it once, as its own authorized act, serves both. CLOSING CONDITION: DISARMED when the issuer rules; REMEDIATED when get-bucket-logging on opal-data-security names a target AND a log object is observed delivered under that prefix -- the delivery read, never the configuration read, is the one that discriminates. FALSIFIER: a get-bucket-policy on the target showing a logging.s3.amazonaws.com grant this seat failed to read."
 },
 {
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "surfaced_by": "2.0.0_SA_COO~Z (issuer, L6; the named disarm_owner of the item this row records the disarm of). A DISARM RECORD, not a new finding and not an adjudication (no `adjudicates`; L9 is 3.0.0_SA_CVO~Z's). Written to the record because the L10 gate reads rows, never messages (3.0.0_SA_CVO~Z 19521).",
  "surfaced_at": "2026-09-03T08:31Z",
  "id": "NFRA_OPSEC202609-Z-S6",
  "one_line": "DISARM RECORD for NFRA_OPSEC202609-Z-S2 (the origin-secret value rests in Terraform state by construction): design call (a) ACCEPTED by the issuer 2026-09-03 08:04Z (operating note to 0.7.0_AE_CloudOps~Z) -- state-at-rest is the value's resting place on the measured mitigations (state bucket SSE-S3 + full public-access-block; the value proves path-of-entry only, every authenticated route still requires the JWT; a rotation bounds a state-history read to one window). No criterion changed; the secrets.tf container comment scopes the 'never enters state' invariant to the JWT keypair; the runbook (deliverable 4) states the state-history residual. Shape (c) rejected (no literal-free, drift-free alternative for an API Gateway origin). The state bucket's missing noncurrent-version expiry is NOT this project's: bootstrap bucket with no Terraform resource (0.0.0_AB_MSTR~Z 19508), steward 0.7.0_AE_CloudOps, gate 1.0.0_SA_CTO, homed by the CTO under the D0 NFRA substrate as its own task order (19514).",
  "spec_asserts": "Row Z-S2 named disarm_owner 2.0.0_SA_COO~Z with three remedy shapes (a) accept state-at-rest, (b) a noncurrent-version expiry on the state bucket, (c) a different header mechanism; the L7 rule: an ARMED row is disarmed in the same turn by its named owner, and disarmed is not remediated.",
  "world_is": "The issuer chose (a) in writing at 08:04Z and the worker proceeded on it; (b) is a separate lane's act, homed by the CTO outside this project; (c) has no viable member. The value's exposure surface after (a): a read of the state bucket's object versions by a principal that can already read Terraform state, bounded by the rotation window. Z-S2 stays OBSERVATION/ARMED on its own row (append-only); this row records that the owner's disarm act occurred and what it was.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "operating note 2.0.0_SA_COO~Z -> 0.7.0_AE_CloudOps~Z 2026-09-03T08:04:46Z (the disarm as sent; the worker's ack is its own record)",
    "0.7.0_AE_CloudOps~Z row Z-S2 @7c6dc7dca6: the worker's own reads (get-bucket-encryption SSE-S3; get-public-access-block 4 of 4; get-bucket-versioning Enabled; get-bucket-lifecycle-configuration NoSuchLifecycleConfiguration rc=254; get-distribution-config 7 origins, CustomHeaderCount 0)",
    "3.0.0_SA_CVO~Z 19499 L8 read: grounding RESOLVES (secrets.tf:5-7 and main.tf:20-24 at @94b6fd0d11 read as quoted; negative control on a bogus path fails loud)",
    "0.0.0_AB_MSTR~Z 19508: comp-find 'opal-313476888478-terraform-state' 180 hits / 50,956 files, every SURFACED hit a backend block, no aws_s3_bucket declares it; s3-hand-audit-fixture-v1.1.yaml:841 'bootstrap bucket, no TF resource'",
    "1.0.0_SA_CTO~Z 19514: the lifecycle rule's home = NOT this project; steward 0.7.0_AE_CloudOps, gate CTO, a bootstrap module that imports the bucket, its own task order under the D0 NFRA substrate"
   ]
  },
  "notes": "WHAT THE DISARM IS NOT: not a re-file, not an edit of the frozen face's criteria, not a disposition of Z-S2 (the CVO's at L9). At the stamp: (a) is a recorded acceptance and no route (the CVO's own reading, 19499)."
 },
 {
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "surfaced_by": "2.0.0_SA_COO~Z (issuer, L6; the named disarm_owner of the item this row records the disarm of). A DISARM RECORD, not a new finding and not an adjudication (no `adjudicates`; L9 is 3.0.0_SA_CVO~Z's). Written to the record because the L10 gate reads rows, never messages (3.0.0_SA_CVO~Z 19521).",
  "surfaced_at": "2026-09-03T08:31Z",
  "id": "NFRA_OPSEC202609-Z-S7",
  "one_line": "DISARM RECORD for NFRA_OPSEC202609-Z-S3 (BLOCKING: 'the estate CMK' is the AWS-managed DynamoDB key; C-8's bucket encryption unsatisfiable as written): the WORK was disarmed by the issuer's operating note 08:05Z (0.7.0_AE_CloudOps~S builds the table on the AWS-managed key = opal-users-v2's exact APPLIED shape, and every non-encryption property of the bucket with SSE-S3 as the INTERIM; S17-AC1's KMS limb filed UNCOMPUTABLE-BY-CONSTRUCTION citing Z-S3; nobody picks a key mid-round); the SPEC was routed UP the same turn (19503) and RULED at L4 by 1.0.0_SA_CTO~Z: PRD v0.5 @a3cad58b0d -- ONE project customer-managed key alias/opal-security, new C-13, manifest row S25, OWNS 17; the key flip is a round-2 task order in place. The decomposition re-read it at v0.1.1 (cell OP-s-25, the C-13 bound on OP-s-16 / OP-s-17).",
  "spec_asserts": "Row Z-S3 named disarm_owner 2.0.0_SA_COO~Z: 'the issuer names which key the bucket uses, in writing, on the face or by ruling'; the L7 rule on ARMED rows; Rule 27: mid-round the spec is FROZEN, a spec error routes to L6 and onward to L4 if the defect sits in the PRD.",
  "world_is": "The defect sat in the PRD (7.3 / C-8 / C-9 inherited the brief F6's misread of an AWS-managed key's yearly rotation as a CMK) and was corrected at L4 by the L4 owner's own act, disclosed to Andrew and reversible by his word (19514). Round 1's interim readings stand exactly as PRD v0.5 permits; the remediation is the round-2 cell OP-s-25 plus the two in-place flips. Z-S3 stays BLOCKING/ARMED on its own row; this row records the disarm of the WORK and the routing of the SPEC.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "operating note 2.0.0_SA_COO~Z -> 0.7.0_AE_CloudOps~S 2026-09-03T08:05:11Z; the worker's ack 19506 (proceeding table-first; module opsec/ confirmed 08:06Z)",
    "0.7.0_AE_CloudOps~S row Z-S3 @d59b3734c3: describe-key KeyManager=AWS, sole alias alias/aws/dynamodb, KeyManager=CUSTOMER positive control over all 11 keys; describe-table opal-users-v2 SSEDescription KMS with that ARN",
    "3.0.0_SA_CVO~Z 19502 L8 read: grounding RESOLVES on four instruments; the estate's own census labels alias/aws/dynamodb an 'AWS-managed CMK' -- a Rule 24 axis defect on the word CMK",
    "1.0.0_SA_CTO~Z 19514: PRD v0.5 @a3cad58b0d, C-13 KEY, manifest S25, OWNS 17; _prd_conformance [] after the edit; disclosed to Andrew",
    "2.0.0_SA_COO~Z decomposition v0.1.1 (this commit window): OP-s-25 added, C-13 bound on OP-s-16 / OP-s-17, round 2 opens with OP-s-25 on the ~S seat"
   ]
  },
  "notes": "At the stamp: the CVO reads Z-S3 as GRADUATED with the L4 bump as its remedy and no route unless Andrew reverses v0.5 before the close (19521); this seat concurs and withdraws its earlier 'SCOPE_CHANGE candidate' wording (19519) -- the CTO's L4 adjudication of a questioned spec point is the spine's own path (v2.3, after L2 no limb waits on him)."
 },
 {
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "surfaced_by": "2.0.0_SA_COO~Z (issuer, L6; the named disarm_owner of the item this row records the disarm of). A DISARM RECORD, not a new finding and not an adjudication (no `adjudicates`; L9 is 3.0.0_SA_CVO~Z's). Written to the record because the L10 gate reads rows, never messages (3.0.0_SA_CVO~Z 19521).",
  "surfaced_at": "2026-09-03T08:31Z",
  "id": "NFRA_OPSEC202609-Z-S8",
  "one_line": "DISARM RECORD for NFRA_OPSEC202609-Z-S4 (BLOCKING: bound (b) of TO-OP-S-17-16 named two principals that do not exist -- 'the CTO-admin role' and 'the account's Terraform-apply role'; 0 of 216 roles; the applier is an IAM user): the defect is the ISSUER'S OWN FACE (a bound naming referents never enumerated). Disarm ruled 08:13Z: (a) DEFER -- the deny-outside-list statement is NOT written this round; the bucket policy carries the SecureTransport deny ONLY; the four public-access blocks are the control (not public, not exposed); S17-AC1's allow-list limb filed UNCOMPUTABLE-BY-CONSTRUCTION citing Z-S4; no IAM user is named in a security-evidence policy. The identity half was routed UP the same turn (19518) and RULED at L4: PRD v0.6 @b482fe8a5b -- ONE Terraform-declared role opal-security-admin, new C-14, manifest row S26, OWNS 18; its TRUST (which humans may assume it) is Andrew's card OP-x-6. The decomposition re-read it at v0.1.1 (cell OP-s-26; C-14 bound on OP-s-14/15/17/19; OP-x-6).",
  "spec_asserts": "Row Z-S4 named disarm_owner 2.0.0_SA_COO~Z: 'the issuer names the real principal(s) in writing, or rules the deny-outside-list statement DEFERRED to the round that creates the sentinel/reconciler roles'; the face's own rule 'a bucket policy cannot name an absent role'.",
  "world_is": "Deferral ruled; the worker proceeds to the apply on that basis (the ledger entry opens after the ruling); the two service roles are created by OP-s-14 / OP-s-15 and the human-side role by OP-s-26 in round 2, after which the deny-outside-list statement is cut into those faces (the SPEC_ERROR route to L6 this seat accepted in advance, 19519). Z-S4 stays BLOCKING/ARMED on its own row; this row records the disarm and the routing. Banked at this seat as a memory: an issuer enumerates every principal, key or resource a bound names, at the cut.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "ruling 2.0.0_SA_COO~Z -> 0.7.0_AE_CloudOps~S 2026-09-03T08:13:12Z (operating note); the worker's BLOCKING notification 19512 08:11:57Z",
    "0.7.0_AE_CloudOps~S row Z-S4 (worktree at 08:11Z, commit pending at the worker): list-roles 216 client-side over 3 pages, 'admin|cto|terraform' 0, positive control 'lambda' 55; sts get-caller-identity user/Andrew_Berman; list-users no such function user",
    "3.0.0_SA_CVO~Z 19521 L8 read: grounding RESOLVES; comp-find -i 'cto-admin|terraform-apply role' 35 hits / 50,969 files, every hit in this project's own texts -- the principals were never measured, a different mechanism from Z-S3's mislabelled key",
    "1.0.0_SA_CTO~Z 19525: PRD v0.6 @b482fe8a5b, C-14 IDENTITY, manifest S26, OWNS 18; the six 'CTO-admin' referents replaced; card OP-x-6 to Andrew at the CTO~Z terminal 08:16Z",
    "the face TO-OP-S-17-16 @5494591e91 :23 and :47 (the two principals named; the self-refuting rule beside them) -- the issuer's own text"
   ]
  },
  "notes": "WHY THREE ROWS AND NOT ONE: the L10 gate joins rows to items; one row disarming three items would leave the L9 adjudication of each without a citable disarm. WHAT THESE ROWS ARE NOT: dispositions (the CVO's), re-files, or face edits (the spec is frozen; the deferred statement lands in the round-2 faces)."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S9",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "surfaced_by": "2.0.0_SA_COO~Z (issuer, L6; the named disarm_owner of Z-S5). A DISARM RECORD, not a new finding and not an adjudication (no `adjudicates`; L9 is 3.0.0_SA_CVO~Z's).",
  "surfaced_at": "2026-09-03T08:33Z",
  "one_line": "DISARM RECORD for NFRA_OPSEC202609-Z-S5 (BLOCKING: C-8's server-access-logging TARGET opal-cloudtrail-logs-313476888478 permits only cloudtrail.amazonaws.com -- no logging.s3.amazonaws.com grant, no LogDelivery ACL -- so the limb cannot receive, and the specified get-bucket-logging read cannot tell a configured-but-dead limb from a live one): ruled DEFER 2026-09-03 08:2xZ (operating note to 0.7.0_AE_CloudOps~S) -- the aws_s3_bucket_logging resource stays authored-and-commented in infra/aws/terraform/opsec/s3.tf with the row id beside it; S17-AC1's logging read files UNCOMPUTABLE-BY-CONSTRUCTION citing Z-S5; the audit-log bucket is NOT edited (shared-infra's, DO-NOT-REMOVE, never-widen); the other seven resources apply now. The TARGET question was routed to 1.0.0_SA_CTO~Z (L4) the same turn with this seat's rec (a project-owned access-logs target in opsec/; alternative: a scoped additive logging.s3 grant on the CloudTrail bucket under shared-infra's lane); the limb lands in round 2 beside the key flip, graded by a DELIVERED object, never the configuration.",
  "spec_asserts": "PRD 7.6 C-8 and TO-OP-S-17-16 deliverable 2(c): 'server access logging to the estate's CloudTrail/access-logs bucket'; S17-AC1 lists get-bucket-logging (target = that bucket) among the six reads; ruling 19517 listed access logging among what the bucket carries at this apply. Row Z-S5 named disarm_owner 2.0.0_SA_COO~Z with three shapes (authorize the target grant as its own cell, re-point the target, or defer).",
  "world_is": "Naming the target is necessary and not sufficient: the target must permit the S3 log-delivery principal, and this one permits only CloudTrail (the worker's get-bucket-policy: two statements, both cloudtrail.amazonaws.com; get-bucket-acl: one CanonicalUser FULL_CONTROL, no LogDelivery grant). The issuer deferred the limb rather than widen a shared-infra audit-log bucket mid-round; the worker's rec 'defer to OP-s-5' was corrected (OP-s-5 delivers INTO the owned bucket; Z-S5 is the owned bucket's own logs going OUT to a bucket the project does not own). Z-S5 stays BLOCKING/ARMED on its own row; this row records the disarm of the work and the routing of the spec.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "ruling 2.0.0_SA_COO~Z -> 0.7.0_AE_CloudOps~S 2026-09-03 08:2xZ (operating note); the worker's BLOCKING notification 19531 08:23:37Z, surfaced BEFORE the apply (plan 7 / 0 / 0 read as stated; ledger entry opsec-evidence-store-and-address-table OPEN)",
    "0.7.0_AE_CloudOps~S row Z-S5: get-bucket-policy on opal-cloudtrail-logs-313476888478 (Sid AWSCloudTrailAclCheck + AWSCloudTrailWrite, both Principal cloudtrail.amazonaws.com); get-bucket-acl (1 grant, CanonicalUser FULL_CONTROL, LogDelivery False); describe-trails (opal-organization-trail delivers there); comp-find 'opal-cloudtrail-logs' -> shared-infra/s3.tf:48 '*** LIVE -- DO NOT REMOVE ***'; a 31-bucket get-bucket-logging sweep with NO positive control, stated as such",
    "the finding to 1.0.0_SA_CTO~Z 2026-09-03 08:2xZ with the rec and the alternative; the round-2 re-cut carries the delivery read (a log object observed under the target prefix) in place of the configuration read S17-AC1 used"
   ]
  },
  "notes": "THE THIRD REFERENT OF ONE FACE IN ONE ROUND (key, roles, target), each asserted without a read until the worker's re-grounding; the round-2 cut at this seat runs one live read per named referent BEFORE the TO commits. WHAT THIS ROW IS NOT: a re-file, a face edit, or a disposition of Z-S5 (the CVO's)."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S10",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~Z (L7 worker, OP-s-3, while grounding the IAM half of the cell)",
  "surfaced_at": "2026-09-03T08:34:00Z",
  "one_line": "cross-firm-secret-deny.tf:6-10 justifies its Deny belt on the premise that three portal/news-plane roles hold a secret:opal/* WILDCARD, naming opal-portal-lambda-role (the shared role behind the PUBLIC authorizer). At 2026-09-03 that premise is FALSE for at least that role: simulate-principal-policy reads implicitDeny for it on opal/auth/origin-verify while a ROLE-SPECIFIC positive control (opal/auth/jwt-public-key) reads allowed, and its three live inline secrets policies are explicit allowlists with no wildcard. Phase A narrowed it and the belt file was never updated.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO~Z (owner of the credential-plane firm-sep belt; the file carries a CTO amended ruling in its header). DISARM = correct the WHY-narrative at cross-firm-secret-deny.tf:6-10 to describe the post-Phase-A grants, or record that the belt is now defence-in-depth over an allowlist rather than a subtraction from a wildcard. THE DENY ITSELF IS CORRECT AND MUST NOT BE REMOVED -- only its stated justification is stale.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "infra/aws/terraform/portal-auth/cross-firm-secret-deny.tf:6-10 @94b6fd0d11 -- \"secret:opal/* wildcard grants let three portal/news-plane roles read ... Exercised: GetSecretValue = ALLOWED for opal-portal-lambda-role (the SHARED role behind 11 Lambdas incl. the PUBLIC authorizer), opalinvest-auth-lambda-role, and news-ingestion-lambda-role.\"",
    "MEASURED 2026-09-03, simulate-principal-policy, ONE --resource-arns per call: opal-portal-lambda-role on opal/auth/origin-verify-AbCdEf = implicitDeny; ROLE-SPECIFIC positive control opal/auth/jwt-public-key-Z6dqNK on the SAME role = allowed (so the instrument reaches this role and the deny is real, not a borrowed control).",
    "MEASURED 2026-09-03, live get-role-policy on opal-portal-lambda-role: opal-portal-secrets = {smartx/config, external-apis} x2 regions; SecretsManagerAccess = {jwt-public-key-??????, external-apis-??????, openai/news-trending-??????}; opal-sessions-secrets = {opal/auth/jwt-public-key*}. NO opal/* wildcard in any of the three.",
    "infra/aws/terraform/portal-auth/iam.tf:61 @94b6fd0d11 -- the SIBLING role carries the matching note: \"NARROWED 2026-07-09 (Phase A). Was opalinvest/* + opal/* in both regions.\"",
    "infra/security/remediation/secrets-allowlist-narrowing-and-least-privilege-PLAN-20260709.md:55 -- independently records opal-portal-lambda-role inline SecretsManagerAccess as HAVING BEEN secret:opal/* and being narrowed to an allowlist. Two carriers agree the narrowing happened; only the belt file still describes the pre-narrowing world.",
    "MEASURED 2026-09-03: news-ingestion-lambda-role on the same new ARN = implicitDeny -- so the new secret is not broadly reachable, which is the bound the TO face required of this cell."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "cross-firm-secret-deny.tf:6-10: three named roles hold secret:opal/* wildcard grants, which is the stated reason a Deny (rather than a narrowed Allow) was the right instrument -- \"the grant is a WILDCARD ... and IAM has NO resource-exclusion syntax\".",
  "world_is": "At least opal-portal-lambda-role holds no opal/* wildcard today; its three secrets policies are explicit allowlists. The Deny belt is still correct and still worth keeping, but it now sits over an allowlist rather than subtracting from a wildcard, so the file argues from a world that no longer exists. The other two named roles were not re-measured by this seat and this row does not claim anything about them -- the sound claim is scoped to the one role measured.",
  "notes": "WHY IT MATTERS OPERATIONALLY, and it is not cosmetic: this cell needed the authorizer to read a new opal/auth/* secret. Reading cross-firm-secret-deny.tf would have said the wildcard already covers it, the grant would have been skipped, and the authorizer would have failed CLOSED on every authorized route the moment the code deployed -- a full portal outage from trusting a stale comment. The grant was written only because the live primitive was measured instead. NOT CHASED: no edit to cross-firm-secret-deny.tf from this seat -- it is a security control with a CTO amended ruling in its header and correcting its rationale is that owner's act, not a mid-task edit by the seat relying on it. SCOPE BOUND: one role measured, two named roles NOT measured; a re-checker should measure all three before rewriting the sentence. FALSIFIER: if simulate-principal-policy on opal-portal-lambda-role returns allowed for an arbitrary new opal/<anything> ARN, the wildcard is back and this row is wrong."
 }
]
```
