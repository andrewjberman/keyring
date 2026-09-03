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
  disarm record (Z-S6..S9); dispositions stay at L9. POSTSCRIPT: this bullet did ride another seat's commit --
  7abe7552b5 (`0.7.0_AE_CloudOps~Z`, the TO-OP-S-3 deploy commit that also carried Z-S10) -- so its first author
  line is the worker's; the text above is `3.0.0_SA_CVO~Z`'s, as the bullet says.

- **S10** (surfaced by `0.7.0_AE_CloudOps~Z` while grounding the IAM half of OP-s-3; committed @7abe7552b5;
  OBSERVATION / ARMED, disarm_owner `1.0.0_SA_CTO~Z` -- the belt file's header carries the CTO's amended ruling).
  The claim: `cross-firm-secret-deny.tf` justifies its Deny belt on the premise that three portal/news-plane roles
  hold a `secret:opal/*` WILDCARD, naming `opal-portal-lambda-role`; at 2026-09-03 that premise is false for at
  least that role (simulate-principal-policy implicitDeny on `opal/auth/origin-verify`, a ROLE-SPECIFIC positive
  control allowed on `opal/auth/jwt-public-key`, three inline secrets policies that are explicit allowlists). The
  row scopes itself to the one role it measured -- the honest form. Grounding RESOLVES at this seat on instruments
  other than the worker's simulate calls: the cited premise reads at HEAD in the portal-auth copy of the belt file
  (:5 "FINDING: `secret:opal/*` wildcard grants let three portal/news-plane roles read the BD firm's ...", :12 "WHY A
  DENY AND NOT A NARROWED ALLOW: the grant is a WILDCARD"), replicated in the news-pipeline and shared-infra copies
  and extended in market-overview's (the 2026-07-09 CVO completeness sweep, @2c63773fc9) -- FOUR copies of one
  justification, so a disarm that edits one leaves three stale; the DESIRED plane (`comp-find 'secret:opal/\*|...'`
  over infra/aws/terraform: 56 hits / 530 files, page 1 of 3 read) shows the belts' own `secret:opal/bd/*` deny
  resources and the narrowed `least-privilege-secrets.tf` allowlists, and no ALLOW carrying `secret:opal/*` for the
  role on that page -- consistent with the worker's read, not a conclusion on its own (a page is not an answer).
  The belt stays correct as defence in depth over an allowlist; what is stale is the file's argument, which is
  1.0.0_SA_CTO~Z's text to disarm across all four copies. Not blocking; the cell proceeded (the deploy commit that
  carried this row reports the origin secret DEPLOYED-VERIFIED on both gateway origins). Held `UNDER_INVESTIGATION`;
  on the grounding bar it GRADUATES; at the stamp its remedy is a comment-plane edit on a fabric gate, not a route.

- **S11** (surfaced by `0.7.0_AE_CloudOps~S` validating TO-OP-S-17-16's proof-of-spec instance before the complete
  flip -- found by running the gate, not by assuming it would pass; committed with that instance; BLOCKING). The
  claim: S1716-AC4 declared `cell_refs="OP-s-17 OP-s-16"` space-separated; `.tools/proof-of-spec-check.py:562`
  splits `cell_refs` on a comma only, so the pair read as ONE literal that matched no decomp cell, and the alignment
  limb REFUSED an instance that was otherwise clean (5 of 5 artifact rows resolved at pin, 3 of 3 surprises resolving
  to channel rows). The worker did not self-fix: `cell_refs` is the issuance half and the checker's own comment at
  :328 says so. Grounding RESOLVES at this seat: :562 and :328 read at HEAD @c765283365 by `git show`; an estate
  census on a DIFFERENT instrument (python over `git ls-files org/missions/*/*/*/task-orders/*.md`: 11 tracked faces,
  65 `cell_refs` attributes, 64 single-value, 1 multi-value -- this face) agrees with the worker's comp-find census
  on a different denominator. DISARMED ON THE FACE BEFORE THIS READ FINISHED: the issuer `2.0.0_SA_COO~Z` changed the
  one character (`cell_refs="OP-s-17,OP-s-16"`) @beacddcf26 08:56:21Z; the worker re-ran the checker, the instance
  read VALID, and TO-OP-S-17-16 flipped `complete` @f9b2a16c2c -- the round's FIRST terminal task order. The disarm
  record is `Z-S12` (`2.0.0_SA_COO~Z`, @87d1d24968). THE L8 FINDING on top of the row, a fabric item on the checker's
  surface (`1.0.0_SA_CTO~Z`, sent as 19577): the separator convention is UNDOCUMENTED -- `org/ref/TASK_ORDER_PROTOCOL.md`
  says "comma-separated" for `<expected_criteria>` (:256) and for a CLI id set (:193) and nothing for `cell_refs`;
  `org/standards/PROOF_OF_SPEC.schema.json` names `cell_refs` only in a description (:62) -- and the same face's
  `<owned_cells>` at :57 is space-separated and was read fine (2 of 2 owned cells reachable), while the checker's own
  guidance strings at :819 and :1101 write `<owned_cells>id, id</owned_cells>`. Two list attributes, two
  conventions, one file; the author copied the separator the face already used, and the refusal text sends the
  reader to the DECOMP rather than the separator. Remedy shapes as the worker offered them: split on comma or
  whitespace and say so in the protocol, or refuse whitespace with a message naming the separator. Held
  `UNDER_INVESTIGATION`; on the grounding bar it GRADUATES; its remedy on this project is done and it takes no route.

- **ROUND-1 STATE at this write (09:0xZ):** 12 rows -- S1 (this seat), S2/S3/S4/S5/S10/S11 (workers), S6/S7/S8/S9/S12
  (the issuer's disarm records for S2/S3/S4/S5/S11). Every ARMED item except S10 carries a disarm record; S10's disarm
  is the CTO's comment-plane edit on a fabric gate. Task orders: TO-OP-S-17-16 `complete` @f9b2a16c2c with a VALID
  instance; TO-OP-S-3 `pending` (deploy commit reports DEPLOYED-VERIFIED); TO-OP-S-5 and TO-OP-S-8 `staged`. The L10
  precondition (every task order terminal with a valid instance; every item dispositioned) is not met; the L9 slug and
  any route wait on it. The self-drive tick-1 verdict on OP-x-1 (the probe list) went to the driver at 09:06:12Z (delivery
  file 20260903T090612Z_3.0.0_SA_CVO_Z_VERDICT_on_SELF-DRIVE_NFRA_OPSEC202609_t.md; the receipt carried no numeric id;
  the driver's landing 19590 names it 19584, ledger row 1).

- **ROUND-1 STATE, second read (09:1xZ):** TWO of four task orders terminal -- TO-OP-S-17-16 `complete` @f9b2a16c2c and
  TO-OP-S-3 `complete` @a491aaec8c (instance @3c32f20c38); TO-OP-S-5 (`~Z`) and TO-OP-S-8 (`~S`) open on those flips
  per their GOs. Both instances checked at this seat on an instrument other than the checker: 0 schema errors each
  (Draft7 against PROOF_OF_SPEC.schema.json), and every `surprises` entry resolves to a channel row by my own reader
  (S-17-16: Z-S3/Z-S4/Z-S5/Z-S11, 4 of 4; S-3: Z-S2/Z-S10, 2 of 2); the UNCOMPUTABLE-BY-CONSTRUCTION rows are exactly
  S17-AC1 (three deferred limbs, each with its row and disarm record) and S3-AC5 (the probe, now authorized by ledger
  row 1 and computable when it runs). The issuer's own coverage runs (19595: expected ids passed, VALID rc=0 both) are
  the second instrument the L9 grades cite. Two accepted deviations on S-3 for L9: the header name is
  `X-Opal-Origin-Verify` (the PRD names none; a distinct name removes an asserted precedence dependency on the inert
  edge injection at `auth-validator-edge/index.mjs:392`), and both consumers cache the secret at 300 s against the
  runbook's 600 s wait (the worker's first build cached unbounded, which would have falsified deliverable 4's rotation
  claim -- caught before the leg closed). Z-S11 is now closed on BOTH halves: the face @beacddcf26 (issuer) and the
  checker @50ff3d674a (`1.0.0_SA_CTO~Z`: `cell_refs` split on comma and/or whitespace, documented in
  `org/standards/DECOMP_CELL_ID_CONVENTION.md`); at the stamp it takes no route. Twelve rows; nothing new since S12.
  POSTSCRIPT: this bullet rode `0.7.0_AE_CloudOps~S`'s f5859c4097 (the TO-OP-S-8 commit that carried Z-S13/Z-S14)
  after this seat's gated commit refused over those two uncommitted rows; the text is `3.0.0_SA_CVO~Z`'s.

- **S13** (surfaced by `0.7.0_AE_CloudOps~Z` at OP-s-5's mandated Phase-1 pre-write read; OBSERVATION / ARMED;
  disarm `2.0.0_SA_COO~Z`). The claim: the face says WAF logging is OFF on BOTH ACLs and creates it on both; the
  REGIONAL ACL `opal-gateway-waf` already has a live logging configuration delivering to the exact group the face
  names, retention 90 d (the face says 400 d), 84.7 MB stored, and the owning file is outside the declared lane; only
  the CLOUDFRONT ACL is unconfigured. Grounding RESOLVES at this seat on the DESIRED plane, independent of the
  worker's live wafv2/logs reads: `infra/aws/terraform/opal-gateway/waf.tf` @a7312b946b (2026-08-14, three weeks
  before this project) declares `aws_wafv2_web_acl_logging_configuration "gw"` at :194, `log_destination_configs =
  [aws_cloudwatch_log_group.waf.arn]` at :195, SIX `redacted_fields` blocks, `retention_in_days = 90` at :23; the face's
  Lane path `infra/aws/ec2/opal-gateway/**` holds 14 entries and ZERO .tf files, while `infra/aws/terraform/opal-gateway/`
  holds 16. THE MECHANISM is a new variant for the round: the brief DID measure and SAID what it measured --
  `docs/briefs/PLATFORM_ATTACK_SURFACE_ASSESSMENT_20260902.md:95` "| WAF logging (CloudFront ACL) | not configured |",
  scoped to ONE ACL; PRD FWD-5's SOURCE line (:96) carries it as "WAF logging not configured" with the qualifier gone;
  manifest S5 (:501) says "BOTH ACLs"; the face says "all OFF today". A scoped measurement lost its scope at each relay.
  90 d already meets FWD-5's ACCEPT bar and S5-AC5's ">= 7 days" (:37); 400 d is the face's own setting. The worker's
  hold on the regional half is the finding's value: deliverable 1 taken literally would have authored a SECOND logging
  configuration on an ACL that permits one, replacing a working control. Held `UNDER_INVESTIGATION`; GRADUATES on the
  grounding bar; its remedy is the issuer's two calls (retention; lane) and a face defect, not a route past L6.

- **S14** (surfaced by `0.7.0_AE_CloudOps~S` re-grounding TO-OP-S-8's five tables at their REAL carrier, BEFORE any
  write; BLOCKING / ARMED; disarm `2.0.0_SA_COO~Z`). The claim: `opal-partner-demo` is LIVE but NOT Terraform-managed;
  the module's instantiations are in `partner-firms/` (three), not the `partners-api/**` the face names (four); the
  face's deliverable 3 directs a Terraform edit on a table Terraform does not own. Grounding RESOLVES at this seat on
  the committed tree and the RECORDED plane, independent of the worker's state sweep: `git ls-files` shows
  `partner-firms/` = 49financial.tf, cottonwood.tf, inflection.tf, main.tf, each with 0 "demo" tokens at HEAD;
  `partners-api/` exists with 4 tracked .tf that are not the module's instantiations; and the estate ALREADY KNEW --
  `infra/aws/globgrph/comp_debt_baseline.json:17` records the table as `DYNAMODB_TABLE/orphan`, and the 2026-06-03
  provisioning task order `org/projects/task_orders/ADVI_DEMOAUTH.001.provision-opal-partner-demo.md:22` says "NOT
  TF-managed (CLI/script-provisioned)". The PRD's S8 row (:504) names four tables; the face's fifth came from the brief's
  F6 row (:152) -- the same brief-to-face path as S13, one column over. The worker's method note stands on its own: its
  first state probe read "no partner resources in state" for all four modules and was a BROKEN PROBE (terraform rc=1,
  a grep reading an error as an empty listing), caught by its positive control -- a clean answer and a broken one were
  byte-identical. Issuer's ruling (19604): the demo limb DEFERRED to round 2, four managed tables proceed in place, no
  import this round; the spec half (import under OP-s-8 round 2 vs a PRD edit vs a fabric cell) was tick-2's card and
  this seat's verdict went to the driver at 09:22:48Z: (a) import under the round-2 limb with no PRD change, (c) a fabric
  item, with an amendment that the import's plan read (0 add / 0 destroy / no "forces replacement"; deletion protection
  never OFF in between) is captured BEFORE the settings. Held `UNDER_INVESTIGATION`; GRADUATES; remedy in round 2.

- **ROUND-1 STATE, third read (09:2xZ):** 14 rows -- S1 (mine), S2/S3/S4/S5/S10/S11/S13/S14 (workers), S6/S7/S8/S9/S12
  (issuer disarm records); disarm records for S13 and S14 are the issuer's next appends. Task orders: TO-OP-S-17-16 and
  TO-OP-S-3 terminal with VALID instances; TO-OP-S-5 and TO-OP-S-8 open. Five worker findings share one shape -- the face
  asserted something the world did not hold -- under three mechanisms (a label taken for a fact; a name never measured;
  a scoped measurement generalised in relay), every one caught by the re-grounding before a destructive act. Nothing
  routes while two task orders are open. POSTSCRIPT (09:2xZ): the S13/S14 reads above and this bullet rode the
  issuer's 2d3ac2b48f (the commit carrying Z-S15 and Z-S16, the disarm records for S14 and S13) after this seat's
  gated commit refused over those two uncommitted rows; the text is `3.0.0_SA_CVO~Z`'s. With S15/S16 on the record,
  every ARMED worker item of the round (S2/S3/S4/S5/S11/S13/S14) carries a disarm record; S10's disarm is the CTO's
  text and S1's is this seat's act at L10. Sixteen rows. The tick-2 verdict on Z-S14's spec half (adopt by import
  under OP-s-8's round-2 limb, no PRD change, the plan read as the acceptance bar) is ledger row 2 at the driver.

- **S17** (surfaced by `0.7.0_AE_CloudOps~S` planning TO-OP-S-8's opal-users-v2 limb at its real carrier, BEFORE the
  fourth apply; BLOCKING / ARMED; disarm `2.0.0_SA_COO~Z` for the carrier half, the drift half owned elsewhere). Two
  findings. (1) CARRIER: opal-users-v2 is managed by `shared-infra/dynamo.tf`, not the `portal-auth/dynamodb.tf` the
  face (:31, :50) and the issuer's ruling 19600 both named. Grounding RESOLVES at this seat: `portal-auth/dynamodb.tf`
  @HEAD :167-175 is a COMMENT block -- "TWIN REMOVED 2026-06-29 ... canonically managed by terraform/shared-infra
  (dynamo.tf) ... a portal-auth apply would have DISABLED PITR on the auth table" -- the named file says in its own
  words where the table lives; `shared-infra/dynamo.tf` @HEAD :15-16 declares it. THE MECHANISM is a fourth variant:
  the correction was ALREADY ON THE RECORD three times before the ruling repeated the stale path -- the target file's
  own comment since June, this channel's S3 evidence (:356, 09:01Z), and the issuer's own 19504 (08:05Z) -- and the
  ruling cited the face rather than any of them. A correction is only as complete as its last surviving carrier; a
  ruling that names a path re-reads the path. The issuer's third round-2 cut rule ("a Terraform deliverable names the
  declaration carrier of every resource it edits, read live") is the remedy. (2) DRIFT: `shared-infra`'s baseline plan
  reads 1 to change on `aws_s3_bucket_lifecycle_configuration.global_graph` (rule `ms-heat-snapshots-expire-60d`), a
  foreign unapplied change; the worker's control (the sibling module planned clean in the same minute) shows the
  dirty baseline is the module's, not a stale-state artifact. Grounding RESOLVES on the tree: `shared-infra/s3.tf` @HEAD
  :339/:362 declares the rule; it was ADDED @4cd024c5c6 on 2026-07-15 by `0.8.0_AE_CloudComp~Z` and no later commit
  touched it -- DESIRED != APPLIED on that resource for up to seven weeks (never applied, or reverted out of band; the
  tree cannot say which and this seat did not query AWS). Owner class per the commit: 0.8.0_AE_CloudComp (globgrph),
  gate CTO; a fabric item for the register beside the state-bucket lifecycle finding, routed by the issuer. The
  issuer's GO (09:32Z) scoped the apply to the one table with a TWO-SIDED unscoped re-plan as the pass condition (the
  table 0-diff AND the drift still present) -- the evidence law's own remedy for a target-scoped apply ("re-read the
  population unscoped once"); a clean unscoped plan would mean the foreign change shipped. Concur. Held
  `UNDER_INVESTIGATION`; GRADUATES on the grounding bar; the carrier remedy is the corrected GO and the cut rule, the
  drift takes no route on this project.

- **ROUND-1 STATE, fourth read (09:3xZ):** 17 rows. Seven referents on round-1 faces were written from a reading
  (S3 key, S4 roles, S5 target, S11 separator, S13 regional control + file, S14 demo table's management, S17
  opal-users-v2's carrier), under four mechanisms (label-for-fact; never-measured; scope-lost-in-relay;
  correction-not-reaching-the-ruling); every one caught by the mandated pre-write re-grounding; zero destructive acts.
  Two task orders terminal with VALID instances; TO-OP-S-5 and TO-OP-S-8 open. Nothing routes. POSTSCRIPT (09:3xZ):
  the S17 read and this bullet rode the issuer's 9656280efe (Z-S18, the disarm record for S17) after this seat's gated
  commit refused over that uncommitted row; the text is `3.0.0_SA_CVO~Z`'s. Eighteen rows: with S18 on the record,
  every ARMED worker item of the round (S2/S3/S4/S5/S11/S13/S14/S17) carries the issuer's disarm record; S10's disarm
  is the CTO's text and S1's is this seat's act at L10.

## L9 adjudication + L10 stamp -- round 1, the one slug (2026-09-03T10:36:19Z, `3.0.0_SA_CVO~Z`)

**Precondition applied at this seat (spine L10; protocol s.8):** task orders terminal 4 of 4 (TO-OP-S-3 @a491aaec8c,
TO-OP-S-17-16 @f9b2a16c2c, TO-OP-S-8 @2da0c78f6a, TO-OP-S-5 @f49c82b891); proof-of-spec instances valid with every
`surprises` entry resolving to a row 4 of 4 (schema Draft7, 0 errors each; 4/4, 2/2, 2/2, 1/1 by my own reader; the
issuer's coverage-checked runs 19595 / 19634 / 19646 as the second instrument); rows at HEAD 18, all
`UNDER_INVESTIGATION` until this slug. HEAD f49c82b891 = origin/SITEZ at the read.
**Dispositions (rows Z-S19, Z-S20 below):** GRADUATED -- S1, S2, S3, S4, S5, S10, S11, S13, S14, S17 (10 findings, every
mechanism re-derived at this seat on a second instrument); DISMISSED_WITH_REASON -- S6, S7, S8, S9, S12, S15, S16, S18
(the issuer's disarm records: records of acts, carried on the items they disarm). 18 of 18 dispositioned.
**Remediation document:** `../remediations/REMEDIATION_v1.Z.md`, 5 rows, every one `SPEC_ERROR -> 6`: S3 (the key
flip: OP-s-25/16/17), S4 (the deny statement with the C-14 role: OP-s-14/15/19/26), S5 (the logging target: OP-s-27 +
OP-s-17's limb), S10 (the belt-justification correction as a RIDER on the round-2 portal-auth face TO-OP-S-1-2, cells
OP-s-1/OP-s-2, with the disarm owner's scope bound: all three roles measured before the sentence is rewritten; the belt
stays), S14 (the demo table's import under OP-s-8's round-2 limb, the plan read as the bar) -- each a cell decomposition
v0.1.4 already contains. 0 `DECOMP_INVALIDATING`; 0 `SCOPE_CHANGE` (C-8's key, roles and target were corrected at L4 by
the L4 owner before this stamp: v0.5 @a3cad58b0d, v0.6 @b482fe8a5b, v0.7 @237265f9f1). The other five graduated items
carry NO remediation row; their facts are carried verbatim on Z-S19's evidence: S2, S11, S13, S17 were remediated inside
round 1 and are closed (disarm and remedy both landed); S1's remedy is a fabric surface homed by the register
(0.0.0_AB_MSTR~Z 19629), its disarm is this seat's lane-addressed pointer at the stamp, recorded as its own row after
the pointer. WHY: the row gate (`.tools/surprise-row-gate.py`, the mechanism at commit) requires `route` +
`loop_target` on every NEW remediation row, while the schema does not require them and protocol s.8 defines `route` as
the re-entry decision ('what does the remedy need that does not exist yet?') -- a value that does not exist for a
remedied or out-of-project item; writing one would put a second intent on the axis. The gate names an audited override;
on this device the tree-path files are graded by the pre-commit hook (`.git/hooks/pre-commit:137-138`), which reads no
commit message, and safe-commit's override reader keys on the legacy `org/surprise_channel` spelling only, so the
escape cannot fire for a tree project (exercised on this slug at 10:36Z and 11:19Z). The divergence is filed as a
round-2 intake row for the gate's owner. S10's disarm record (1.0.0_SA_CTO~Z, written and validated 10:38:59Z) is HELD
off this file until this slug commits and takes the next free id; S10's remediation row reads ARMED until then. Not a
zero-graduation round: the project does not close; round 2 opens on the routed rows at L6, owner `2.0.0_SA_COO~Z`.
**Handoff:** the remediation document is the one artifact, to the route owner and no one else. The mechanical
`prd-header-notify.py kind:route` addresses the BASE serial (row S1); this seat's lane-addressed pointer to
`2.0.0_SA_COO~Z` in the same turn is S1's own disarm act, recorded as its own row (next free id at write) after the
pointer. `dep_stage: ROUND_CLOSE` is the row owner's flip on this stamp (`1.0.0_SA_CTO~Z`).
**What the round said about the loop, once:** seven referents on four faces were written from a reading and none
survived the workers' mandated pre-write re-grounding; zero destructive acts. The three cut rules banked by the issuer
and the CTO are the remedy for the class; this slug routes only what the cells need.

## L8 reads -- round 2 (opened on the stamp @fdbe7360b9; L6 cut 19679: TO-OP-S-25-26-27 @435dcf9d85, TO-OP-S-2 @339213aa54)

**Z-S24 (0.7.0_AE_CloudOps~Z, TO-OP-S-2 Phase-1 pre-write read; BLOCKING / ARMED, disarm owner the issuer) -- read 2026-09-03T12:12:54Z at this
seat on two instruments, row S25 below.** FALSE half: the nine data routes ARE declared (shared-infra/apigateway-portal/routes.tf,
one block each, authorization NONE; 41 blocks in the file, 29 already CUSTOM; the graph DB reads 71 of 72 route nodes DECLARED),
so deliverable 1 is nine in-place attribute edits on existing blocks and the 'dangerous naive repair' never arises. TRUE half: the
face names portal-auth/, which declares no apigatewayv2 resource. Mechanism: main.tf read in full, routes.tf beside it unopened;
estate probes keyed on the literal API id, which a route declaration does not carry (it carries the handle). Disarm = the issuer's
one-line path amendment; sent UP to 2.0.0_SA_COO~Z at the read. The worker is stopped on the false half; the row is the carrier.

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
 },
 {
  "id": "NFRA_OPSEC202609-Z-S11",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~S (L7 worker, TO-OP-S-17-16, validating the proof-of-spec instance before the complete flip)",
  "surfaced_at": "2026-09-03T08:54:43Z",
  "one_line": "TO-OP-S-17-16's S1716-AC4 declares cell_refs=\"OP-s-17 OP-s-16\" SPACE-separated, but .tools/proof-of-spec-check.py:562 splits that attribute on COMMA only -- `[c.strip() for c in attrs.get(\"cell_refs\", \"\").split(\",\") if c.strip()]` -- so the pair is read as ONE literal cell id 'OP-s-17 OP-s-16', which resolves against no cell in the decomp and REFUSES the instance. The instance is otherwise VALID: all other violations are cleared. This face is the estate's ONLY multi-value cell_refs (1 hit across 79 mission files), which is why the separator convention was never exercised before.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z (issuer, L6) -- cell_refs is the TO's ISSUANCE half. The checker's own comment at :328 says 'NOTHING HERE IS DERIVED. cell_refs are read as DECLARED in the TO's issuance half', so the assignee rewriting its own acceptance-to-cell mapping would defeat the control the checker exists to hold. SURFACED, NOT SELF-FIXED. DISARM = the issuer changes the one character in the face (space -> comma), or authorizes this seat to, or rules the criterion should cite a single cell. The complete flip waits on it and on nothing else.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    ".tools/proof-of-spec-check.py:562 -- `refs = [c.strip() for c in attrs.get(\"cell_refs\", \"\").split(\",\") if c.strip()]`; the separator is a comma and there is no whitespace split anywhere in the file (comp-read --enumerate 'cell_refs' -> 7 hits across 1127 lines, all inspected: :328 and :391 comments, :562 the parse, :590/:771 the no-refs bookkeeping, :762/:775 the violation emitters)",
    "proof-of-spec-check.py on the instance -> \"VIOLATION: alignment: cell_ref 'OP-s-17 OP-s-16' (cited by ['S1716-AC4']) does NOT exist in .../NFRA_OPSEC202609_DECOMP.md\"; alignment-forward-2 reads '2/3 distinct cell_ref(s) resolve' -- the 2 that resolve are the single-valued OP-s-17 and OP-s-16",
    "estate census: comp-find 'cell_refs=\"[^\"]*[ ,][^\"]*\"' --files org/missions -> DENOMINATOR 1 hit across 79 file(s) scanned, and the single hit IS this task order. No other TO in the estate declares a multi-value cell_refs, so the comma convention at :562 has never been exercised by a face until now.",
    "the instance's other violations are CLEARED: artifact-resolution now reads '5 resolved at pin / 0 pending-on-worktree / 0 UNRESOLVED-HERE' over a denominator of 5 rows, and surprises-frame reads '3 entries; 3 open with a row id; 3 resolve to a channel row' in ENFORCE mode. cell_refs is the only remaining refusal."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-OP-S-17-16 declares `<criterion id=\"S1716-AC4\" cell_refs=\"OP-s-17 OP-s-16\"/>`, i.e. that this criterion discharges BOTH owned cells, and the face's <owned_cells> names both. The face assumes a space-separated pair is a readable two-value citation.",
  "world_is": "The checker splits cell_refs on a comma and nothing else, so the space-separated pair is one unsplittable literal that matches no declared cell. The alignment check then reports the strongest possible form of failure -- 'a citation to a cell that is not there is worse than no citation' -- for a criterion whose citation is in fact CORRECT in substance and wrong only in punctuation. Note the failure is not symmetric: alignment-backward still reads 2/2 owned cells reachable, because S17-AC* and S16-AC* cite the two cells singly elsewhere. So the mapping the estate cares about is intact; only this one row's rendering refuses.",
  "notes": "WHY A ROW: the last thing between a fully-evidenced deliverable and its complete flip, found by running the gate rather than by assuming it would pass. NOT SELF-FIXED: cell_refs is the issuance half and the assignee does not get to rewrite the mapping its own work is graded against -- that is the whole point of the alignment check. The fix is ONE CHARACTER in the face: cell_refs=\"OP-s-17,OP-s-16\". WIDER THAN THIS PROJECT, offered not prescribed: because no other face in the estate has ever used a multi-value cell_refs, the next author to write one will hit this identically, and the failure text points at the DECOMP ('the cell is not there') rather than at the separator, which sends the reader to the wrong file. Two candidate remedies for whoever owns the checker: split on comma AND whitespace, or refuse a cell_refs value containing whitespace with a message naming the separator. Neither is this seat's to make. CLOSING CONDITION: DISARMED when the face is corrected and proof-of-spec-check returns VALID rc=0; REMEDIATED when a multi-value cell_refs either parses or is refused with a message that names the separator. FALSIFIER: a proof-of-spec-check run that accepts a space-separated cell_refs pair."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S12",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "surfaced_by": "2.0.0_SA_COO~Z (issuer, L6; the named disarm_owner of Z-S11). A DISARM RECORD, not a new finding and not an adjudication (no `adjudicates`; L9 is 3.0.0_SA_CVO~Z's).",
  "surfaced_at": "2026-09-03T09:01Z",
  "one_line": "DISARM RECORD for NFRA_OPSEC202609-Z-S11 (BLOCKING: TO-OP-S-17-16's S1716-AC4 declared cell_refs=\"OP-s-17 OP-s-16\" space-separated; .tools/proof-of-spec-check.py:562 splits cell_refs on a comma only, so the pair read as one literal id, matched no decomp cell, and the alignment limb refused an instance that was otherwise clean): DISARMED 2026-09-03 08:56Z by the issuer's one-character edit on the face -- cell_refs=\"OP-s-17,OP-s-16\" @beacddcf26 (1 file, 1 insertion / 1 deletion, byte count unchanged at 14025). Not a spec change: both cells were declared at L6 and the face's <owned_cells> named both; only the separator the checker reads moved. The assignee's refusal to self-edit the issuance half was correct (the checker's own :328 comment; the GO's task-orders/** scope = the status flip only). The checker re-run at THIS seat on the worker's instance after the fix reads VALID rc=0 (alignment forward 7/7 criteria, 2/2 cell_refs resolve, backward 2/2 owned cells reachable; artifacts 5 of 5 resolved at pin; surprises 3 of 3 resolve to channel rows); the worker's own re-run + the complete flip are the exercise. The wider half (an undocumented separator; <owned_cells> and cell_refs read by two conventions on one face; a refusal text that names the decomp instead of the separator) is a FABRIC item on 1.0.0_SA_CTO~Z's checker surface, no OWNS item, no project route -- named on Z-S11 and in 3.0.0_SA_CVO~Z's L8 read (19576).",
  "spec_asserts": "Z-S11's disarm condition, verbatim in shape: 'the issuer changes the one character in the face (space -> comma), or authorizes this seat to, or rules the criterion should cite a single cell. The complete flip waits on it and on nothing else.' The face's S1716-AC4 discharges BOTH owned cells (the 0-diff re-plan and the push-state read grade the whole TO, not one cell).",
  "world_is": "The first shape was taken: the issuer typed the character. The criterion keeps both cells (a single-cell citation would have under-declared what the 0-diff re-plan grades). No file under .tools was edited by this seat; the checker's comma-only split stands at @c765283365 :562 until its owner moves it. Z-S11 stays on its own row for 3.0.0_SA_CVO~Z's disposition (its L8 read: GRADUATES on the grounding bar, remedy on this project done, no route); this row records the disarm of the work only.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "commit beacddcf26 (2.0.0_SA_COO~Z, 2026-09-03 08:56:21Z): task-orders/NFRA_OPSEC202609.TO-OP-S-17-16.evidence-store-and-address-table.md :36 cell_refs=\"OP-s-17,OP-s-16\"; safe-commit gates OK (to-pipeline-gate, missions-tree-check 0 violations, surprise-row-gate)",
    ".tools/proof-of-spec-check.py run at this seat 08:57Z on deliverables/0.7.0_AE_CloudOps~S/NFRA_OPSEC202609.TO-OP-S-17-16.evidence-store-and-address-table.proof_of_spec.json: VALID rc=0, checker-vintage c765283365, 7 acceptance rows, 0 violations (COVERAGE UNCHECKED -- no expected_criterion_ids passed; the cert consumer runs step-zero)",
    "0.7.0_AE_CloudOps~S 19571 (08:53Z) + 19572 (08:55Z, id correction Z-S6 -> Z-S11): the refusal text, :562 read at source, the estate census (1 multi-value cell_refs across 79 mission files; 3.0.0_SA_CVO~Z's second instrument: 65 attributes across 11 tracked faces, 1 multi-value), the reason not to self-fix",
    "3.0.0_SA_CVO~Z 19576 (08:59Z): L8 grounding RESOLVES; the disarm read on the face at HEAD forty seconds after the commit; the wider half routed to 1.0.0_SA_CTO~Z's surface, offered not prescribed"
   ]
  },
  "notes": "THE FOURTH ROW OF ROUND 1 WHOSE CAUSE SITS IN THE ISSUANCE HALF (key, roles, target, and now a separator) -- three referents asserted without a read, and one convention copied from the face's own <owned_cells> line that the checker accepts there and refuses one line down. The round-2 cut rule extends by one clause: every multi-value attribute on a face is written in the separator the reading tool declares, and where the tool declares none, single values only. WHAT THIS ROW IS NOT: a re-file, an edit to Z-S11, or a disposition of it (the CVO's)."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S13",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~Z (L7 worker, OP-s-5, at the face's mandated Phase-1 pre-write read)",
  "surfaced_at": "2026-09-03T09:14:00Z",
  "one_line": "TO-OP-S-5 asserts WAF logging is OFF on BOTH ACLs and instructs this cell to create it on both. At my vintage the REGIONAL ACL opal-gateway-waf ALREADY HAS a logging configuration -- live, delivering to log group aws-waf-logs-opal-gateway (the exact group name the TO specifies) with 84,723,696 bytes stored, declared in Terraform at infra/aws/terraform/opal-gateway/waf.tf:194 with the authorization and cookie redactions already present. Only the CLOUDFRONT ACL is genuinely unconfigured (WAFNonexistentItemException). Two consequences: the group's retention is 90 d, not the 400 d the TO specifies; and the file that owns it is infra/aws/terraform/opal-gateway/waf.tf, which is NOT inside the lane the TO declares for the gateway WAF (infra/aws/ec2/opal-gateway/**).",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z (issuer) -- two calls, neither the worker's to make alone: (a) whether the existing 90 d retention on aws-waf-logs-opal-gateway is RAISED to the TO's 400 d, and (b) if so, whether this seat may edit infra/aws/terraform/opal-gateway/waf.tf, which the TO's own Lane clause does not name. NOT BLOCKING: the CloudFront half of leg 1 is genuinely absent, squarely in lane, and is being built now.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "LIVE 2026-09-03: aws wafv2 get-logging-configuration on the CLOUDFRONT ACL (arn ...global/webacl/opal-cloudfront-protection/a09833c0-4043-49fc-a92c-0dcdeaff9abd) -> WAFNonexistentItemException, i.e. NO logging configuration. The brief's F3 claim holds for THIS ACL.",
    "LIVE 2026-09-03: the same call on the REGIONAL ACL (arn ...regional/webacl/opal-gateway-waf/181df35e-e886-40c6-a8dc-9d0b60346a44) RETURNS a LoggingConfiguration: LogDestinationConfigs = [arn:aws:logs:us-east-1:313476888478:log-group:aws-waf-logs-opal-gateway], LogType WAF_LOGS, LogScope CUSTOMER, ManagedByFirewallManager false, and SIX RedactedFields -- authorization, cookie, x-amzn-ava-user-context, x-amzn-oidc-accesstoken, x-amzn-oidc-data, x-amzn-oidc-identity.",
    "LIVE 2026-09-03: aws logs describe-log-groups --log-group-name-prefix aws-waf-logs- -> exactly ONE group, aws-waf-logs-opal-gateway, retentionInDays 90, storedBytes 84723696. The stored bytes are the discriminator: this is not a declared-but-idle configuration, it has been receiving records.",
    "DESIRED plane: infra/aws/terraform/opal-gateway/waf.tf:194 resource aws_wafv2_web_acl_logging_configuration \"gw\"; :195 log_destination_configs = [aws_cloudwatch_log_group.waf.arn]; :200-226 six redacted_fields blocks; :20 resource aws_cloudwatch_log_group \"waf\" with :23 retention_in_days = 90. So the live state is IaC-declared and not console drift.",
    "TO-OP-S-5 face @5494591e91 title: 'WAF logging on both ACLs, CloudFront access logs, ALB access logs -- all OFF today'; deliverable 1: 'WAF logging on BOTH ACLs to CloudWatch Logs ... opal-gateway-waf (REGIONAL) -> aws-waf-logs-opal-gateway ... Retention 400 days on both groups'; compiler_tools_mandate phase 1 step 1 expect: '0 logging configurations today (the brief's zero re-measured)', if_mismatch 'STOP; a logging configuration already present is a row before any edit'.",
    "TO-OP-S-5 face Lane clause names 'the gateway ALB / regional WAF Terraform under infra/aws/ec2/opal-gateway/**'; the resource actually lives at infra/aws/terraform/opal-gateway/waf.tf. Measured: the path the TO names is not the path that holds the resource."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-OP-S-5: WAF logging is OFF on both ACLs today and this cell creates it on both, with retention 400 d on both groups; the gateway/regional WAF Terraform lives under infra/aws/ec2/opal-gateway/**; Phase-1 expects 0 logging configurations.",
  "world_is": "One of the two ACLs (REGIONAL opal-gateway-waf) already has a live, IaC-declared logging configuration delivering to the exact log group the TO names, with the two required redactions already in place plus four more, and 84.7 MB already stored. Its retention is 90 d rather than 400 d -- which SATISFIES FWD-5's stated ACCEPT bar (>= 7 d, S5-AC5) but not the TO's specified setting. The owning file is infra/aws/terraform/opal-gateway/waf.tf, outside the lane the TO declares. The CLOUDFRONT ACL is genuinely unconfigured, so half of deliverable 1 is real work and half is already done.",
  "notes": "WHY A ROW AND NOT A HALT: the face's Phase-1 step says STOP on this mismatch, and the row is that stop discharged -- the estate's standing rule is to append a row and keep working, and the work that remains (the CloudFront ACL half) is untouched by this finding, in lane, and proceeding. NOTHING WAS EDITED on the regional side. WHY IT MATTERS: had this seat followed deliverable 1 literally it would have authored a SECOND aws_wafv2_web_acl_logging_configuration for an ACL that already has one -- wafv2 permits one logging configuration per ACL, so the apply would either have failed or silently replaced a working control that is currently capturing gateway traffic, and replacing it at 400 d would also have been an unrequested change to a module this TO does not name. THE RETENTION QUESTION IS GENUINELY OPEN, not a defect: 90 d clears the criterion's own bar (S5-AC5 is '>= 7 d on every destination', with 400 d described as 'the settings'), so the two halves of the TO disagree about what is being asserted, and only the issuer can say whether mirroring C-8 at 400 d is worth an out-of-lane edit to a live control. SCOPE BOUND: this row is about the REGIONAL ACL only; the CloudFront ACL's absence is re-measured and confirmed. FALSIFIER: if get-logging-configuration on the regional ACL later returns WAFNonexistentItemException, this row is wrong and the TO's premise was right."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S14",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~S (L7 worker, TO-OP-S-8, re-grounding the five tables at their REAL declaration carrier before any write)",
  "surfaced_at": "2026-09-03T09:16:35Z",
  "one_line": "opal-partner-demo is LIVE but NOT TERRAFORM-MANAGED, so TO-OP-S-8 DELIVERABLE 3 directs a Terraform SSE/PITR change on a table Terraform does not own. Three carrier claims on the face are wrong and they share one root: (a) the module's instantiations are in infra/aws/terraform/partner-firms/, NOT under partners-api/** as the Lane says; (b) there are THREE instantiations (49financial, cottonwood, inflection), not the four the mandate's step-2 expects; (c) the fourth, opal-partner-demo, is absent from source (0 literal hits over 530 files; no firm_id=\"demo\" anywhere) AND from every initialized module's terraform state. The other four tables are managed and their work proceeds.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z (issuer, L6). Bringing an unmanaged live table under Terraform is a `terraform import`, which is materially more than the face's 'five settings on five tables' and carries the estate's own recorded resurrection/drift hazard (shared-infra/s3.tf documents a declaration that outlived its deleted bucket and would have recreated it). The alternative -- an out-of-band `aws dynamodb update-table` -- is a console-equivalent act against the face's Terraform bound. Either is a scope decision, not a worker's. SURFACED, NOT ADJUDICATED. DISARM = the issuer rules which: import the table as part of this cell, split it into its own cell, or defer the demo limb and cut S8-AC1/AC2/AC3's denominators from five to four.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "comp-find 'opal-partner-demo|partner_demo' --files infra/aws/terraform -> 0 hit(s) across 530 file(s) scanned. NOTE this arm alone is NOT sufficient: the module CONSTRUCTS the name as \"opal-partner-${var.firm_id}\", so a literal probe structurally cannot find an instantiation -- which is exactly why the constructor's input was searched too.",
    "comp-find 'firm_id *= *\"demo\"|firm_demo|\"demo\"' --files infra/aws/terraform -> 1 hit, and it is infra/aws/terraform/ticket-center/main.tf, unrelated to partner tables. No demo instantiation exists in source.",
    "comp-find 'partner-firm-table' --files infra/aws/terraform -> 4 hits: partner-firms/49financial.tf, partner-firms/cottonwood.tf, partner-firms/inflection.tf, and shared-infra/main.tf. The shared-infra hits are COMMENTS at :238 and :243 describing the pattern, not an instantiation (read at source). So THREE instantiations.",
    "terraform -chdir=infra/aws/terraform/partner-firms state list -> exactly three entries: module.firm_49financial|firm_cottonwood|firm_inflection .aws_dynamodb_table.partner_table. No demo.",
    "A sweep of every module carrying an initialized .terraform dir, resolving each aws_dynamodb_table in state to its `name` attribute, found NO resource named opal-partner-demo. POSITIVE CONTROL on that same loop: it resolves module.firm_49financial.aws_dynamodb_table.partner_table -> name=opal-partner-49financial, so the name-extraction works and the NOT-FOUND is a real absence.",
    "SCOPE LIMIT, stated: that state sweep covers only modules with an initialized .terraform dir on this device, not every module in the estate. The SOURCE arm is the complete one (530 files, 0 declarations); the state arm corroborates it. An earlier state probe returned '(no partner resources in state)' for all four modules and was a BROKEN PROBE -- terraform exited rc=1 'Backend initialization required' and the grep read an error, not a listing; caught by a positive control on partner-firms, which demonstrably has three.",
    "The table is nonetheless LIVE: aws dynamodb describe-table opal-partner-demo (BEFORE snapshot 2026-09-03T09:04:21Z) -> DeletionProtectionEnabled=true, SSE AWS-OWNED (no SSEDescription KMS), TableId 99ddc090..., CreationDateTime 2026-06-03T15:26:08, PITR DISABLED -- matching brief F6's row for it exactly.",
    "The other four tables ARE managed and their settings re-ground to brief F6 at this seat's vintage: opal-users-v2 (portal-auth/dynamodb.tf) DP=false PITR=ENABLED SSE=KMS 86cc6c40; opal-partner-49financial / -cottonwood / -inflection (modules/partner-firm-table/main.tf) DP=false PITR=DISABLED SSE=KMS 86cc6c40."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-OP-S-8's Lane names 'infra/aws/terraform/modules/partner-firm-table/main.tf and the module's instantiations under infra/aws/terraform/partners-api/**'. DELIVERABLE 3 directs opal-partner-demo's server_side_encryption to be switched to the estate CMK with PITR ON via Terraform, and S8-AC1/AC2 both carry a denominator of FIVE tables. The compiler mandate's phase-1 step 2 expects an instantiation count agreeing with 'the brief names 4 partner tables incl. demo'.",
  "world_is": "The instantiations live in partner-firms/, not partners-api/**; there are three of them, not four; and opal-partner-demo is not declared in any .tf nor present in any readable terraform state, while being live in the account. Consequences: DELIVERABLE 3 cannot be performed as written -- there is no resource block to edit -- and S8-AC1/AC2's five-of-five denominators are only reachable for the demo table by an act (import, or an out-of-band update-table) the face does not authorise. S8-AC3 additionally asserts the demo table 'was UPDATED not replaced (TableId / CreationDateTime identical before and after)', a control that presupposes Terraform is doing the updating. The face's own bound -- a plan that would REPLACE any table is a STOP -- is the reason this matters: an unmanaged table brought under management carelessly is precisely how a replace gets planned.",
  "notes": "WHY A ROW: found by the re-grounding this round taught and the issuer explicitly asked for (19501 item 3, 19587: 'the five tables at their REAL declaration carrier, never the face's named one'). It is the same failure SHAPE as Z-S3 -- a face naming a carrier that does not hold the thing -- which is now the fourth instance on this project, so the pattern is worth the issuer's attention beyond this cell. NOT CHASED: no import run, no update-table, no console act. WORK CONTINUES on the four MANAGED tables, which is the majority of the cell and is unaffected: deletion_protection_enabled on opal-users-v2 (portal-auth/dynamodb.tf), and point_in_time_recovery + deletion_protection_enabled added to modules/partner-firm-table/main.tf so all three real partner tables inherit them. Phase-1 step 4 is DISCHARGED and clears the way for whichever ruling lands: the AWS-managed key's policy (Id auto-dynamodb-3) carries the via-service grant -- Principal AWS:* conditioned on kms:CallerAccount=313476888478 and kms:ViaService=dynamodb.*.amazonaws.com -- so a demo-table SSE switch cannot fail on key policy whenever it is authorised. REMEDY SHAPES, offered not prescribed: (a) rule the demo limb OUT of this cell and cut S8-AC1/AC2 to four of four, S8-AC3 to N/A -- smallest act, and the demo table holds 1 item and no real client identity; (b) authorise a `terraform import` of the table into partner-firms as an explicit sub-act, with the plan required to show 0 to add / 0 to replace before any apply; (c) a separate cell for adopting unmanaged identity-plane tables, since the same question will recur. This seat recommends (a) for this round and (c) as the durable answer, and holds. CLOSING CONDITION: DISARMED when the issuer rules; REMEDIATED when either the demo table reads PITR ENABLED + SSE KMS under Terraform management, or the face's denominators and Lane match the world. FALSIFIER: a terraform state entry anywhere resolving to name opal-partner-demo."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S15",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "surfaced_by": "2.0.0_SA_COO~Z (issuer, L6; the named disarm_owner of Z-S14). A DISARM RECORD, not a new finding and not an adjudication (no `adjudicates`; L9 is 3.0.0_SA_CVO~Z's).",
  "surfaced_at": "2026-09-03T09:26Z",
  "one_line": "DISARM RECORD for NFRA_OPSEC202609-Z-S14 (BLOCKING, before any write: TO-OP-S-8's fifth table opal-partner-demo is LIVE -- DP=true, SSE AWS-owned, PITR DISABLED, TableId 99ddc090, created 2026-06-03 -- but has NO Terraform resource block anywhere, so DELIVERABLE 3's Terraform SSE/PITR change has nothing to edit; the three real partner instantiations are in infra/aws/terraform/partner-firms/, not the partners-api/** the face named): ruled DEFER 2026-09-03 09:18Z (operating note to 0.7.0_AE_CloudOps~S) -- REC (a) taken: the demo limb DEFERRED to round 2 (no `terraform import`, no `aws dynamodb update-table`, no console act this round); the FOUR managed tables proceed now in place (deletion_protection on opal-users-v2 in portal-auth/dynamodb.tf, PITR already ENABLED live; point_in_time_recovery + deletion_protection_enabled on modules/partner-firm-table/main.tf so 49financial / cottonwood / inflection inherit) under the standing bound that a plan which would REPLACE any table is a STOP and a row; S8-AC1 / S8-AC2 / S8-AC3 keep their five-of-five denominators on the frozen face and file the demo limb UNCOMPUTABLE-BY-CONSTRUCTION citing Z-S14 (the S17-AC1 shape). The spec half -- adopt the demo table by IMPORT under OP-s-8's round-2 limb (this seat's rec: plan 0 add / 0 replace before any apply, then the five settings; no PRD change) or a separate cell for adopting live-but-unmanaged identity-plane tables (the worker's (c), the durable answer, a fabric item) -- was routed to 1.0.0_SA_CTO~Z (L4) the same turn under Andrew's ~08:5xZ delegation.",
  "spec_asserts": "TO-OP-S-8 DELIVERABLE 3 and S8-AC1 / S8-AC2 / S8-AC3: five identity/RBAC tables, five settings, all by Terraform, denominators five of five, the TableId control presupposing Terraform does the updating; the face's SURFACES named partners-api/** as the partner tables' carrier. Row Z-S14 named disarm_owner 2.0.0_SA_COO~Z with three shapes (rule the demo limb out of this round; authorize an explicit import sub-act; a separate adoption cell).",
  "world_is": "The demo table exists on the applied plane and nowhere on the desired plane: no module constructs it (the constructor's input firm_id \"demo\" appears nowhere; every initialized module's state resolves to names that exclude it, with firm_49financial -> opal-partner-49financial as the positive control), and the carrier of the three real instantiations is partner-firms/. The issuer deferred the limb rather than authorize an import mid-round (an import is materially more than five settings, and the estate's own shared-infra/s3.tf records what a careless declaration-vs-live mismatch does) or an out-of-band update-table (a console-equivalent act against the face's Terraform bound). Z-S14 stays BLOCKING/ARMED on its own row for 3.0.0_SA_CVO~Z's disposition; this row records the disarm of the work and the routing of the spec. METHOD NOTE carried from the row: the worker's first state probe returned 'no partner resources in state' for all four modules and was a BROKEN PROBE (terraform rc=1 'Backend initialization required' read as an empty listing); a positive control on partner-firms caught it -- the clean answer and the broken one were byte-identical.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "ruling 2.0.0_SA_COO~Z -> 0.7.0_AE_CloudOps~S 2026-09-03 09:18Z (operating note); the worker's BLOCKING notification 19599 09:16Z, surfaced BEFORE any write",
    "0.7.0_AE_CloudOps~S row Z-S14: comp-find 'opal-partner-demo|partner_demo' 0 / 530 files (the name is constructed, so this arm alone proves nothing); comp-find 'firm_id *= *\"demo\"|firm_demo' 0; 'partner-firm-table' 4 hits of which shared-infra/main.tf:238,:243 are comments; terraform -chdir=partner-firms state list = 49financial, cottonwood, inflection; every aws_dynamodb_table in every initialized module's state resolved to name, no opal-partner-demo, positive control firm_49financial -> opal-partner-49financial; BEFORE snapshot 09:04:21Z DP=true, SSE AWS-OWNED, PITR DISABLED, TableId 99ddc090",
    "the question to 1.0.0_SA_CTO~Z 2026-09-03 09:18Z with the rec (import under OP-s-8's round-2 limb, plan 0 add / 0 replace) and the alternative (an adoption cell for unmanaged identity-plane tables, a fabric item)"
   ]
  },
  "notes": "THE FIFTH REFERENT OF ROUND 1 ASSERTED WITHOUT A READ (key, roles, target, separator, carrier); every one inherited from the brief's or the face's reading and never read until L7. The round-2 cut rule at this seat now reads: one live read per named referent BEFORE a task order commits -- principal, key, bucket, table, ARN, AND the declaration carrier of every resource a Terraform deliverable edits (a resource that is live but unmanaged cannot be edited by Terraform without an import, and an import is its own act). WHAT THIS ROW IS NOT: a re-file, a face edit, or a disposition of Z-S14 (the CVO's)."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S16",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "surfaced_by": "2.0.0_SA_COO~Z (issuer, L6; the named disarm_owner of Z-S13). A DISARM RECORD, not a new finding and not an adjudication (no `adjudicates`; L9 is 3.0.0_SA_CVO~Z's).",
  "surfaced_at": "2026-09-03T09:26Z",
  "one_line": "DISARM RECORD for NFRA_OPSEC202609-Z-S13 (OBSERVATION/ARMED, surfaced at TO-OP-S-5's own Phase-1 pre-write read: the REGIONAL ACL opal-gateway-waf ALREADY HAS a live, Terraform-declared logging configuration delivering to aws-waf-logs-opal-gateway -- the exact group the face names -- with six redacted fields and 84,723,696 bytes stored, declared at infra/aws/terraform/opal-gateway/waf.tf:194 @a7312b946b with retention 90 d at :23; only the CLOUDFRONT ACL is unconfigured; the face said 'all OFF today', specified 400 d on both groups, and named a Lane, infra/aws/ec2/opal-gateway/**, that holds 0 .tf files): RULED 2026-09-03 09:2xZ (operating note to 0.7.0_AE_CloudOps~Z) -- (a) the regional group's retention STAYS 90 d this round, NOT raised: 90 d clears FWD-5's ACCEPT bar and S5-AC5's own '>= 7 days on every destination', the face's bound reads 'retention values are settings; >= 7 d is the bar', and raising a live control's retention in a module the task order does not name is an unrequested mid-round change (a round-2 cell naming the correct carrier if the estate wants 400 there); (b) NO edit to infra/aws/terraform/opal-gateway/waf.tf -- the regional ACL's configuration STANDS (wafv2 permits ONE logging configuration per ACL; a second would have failed or replaced a working control), deliverable 1's regional half is DISCHARGED BY PRIOR STATE and files on the read with the citation; the CloudFront half proceeds as written at 400 d, in lane. No criterion changed: S5-AC1's regional half PASSES on the read of the existing configuration citing waf.tf:194 @a7312b946b + this row; S5-AC5 files the regional value 90 d as read, PASS on the bar with the qualifier that the face's setting was 400 and the issuer ruled 90 stands.",
  "spec_asserts": "TO-OP-S-5 @5494591e91: title 'WAF logging on both ACLs, CloudFront access logs, ALB access logs -- all OFF today'; deliverable 1 'WAF logging on BOTH ACLs ... Retention 400 days on both groups'; Lane clause 'the gateway ALB / regional WAF Terraform under infra/aws/ec2/opal-gateway/**'; compiler_tools_mandate phase-1 expect '0 logging configurations today', if_mismatch 'STOP; a logging configuration already present is a row before any edit'. Row Z-S13 named disarm_owner 2.0.0_SA_COO~Z with two calls: whether 90 d is raised to 400, and if so whether the worker may edit the out-of-lane file.",
  "world_is": "One of the two ACLs already carries the control the face said to create, IaC-declared and receiving records; its retention is 90 d, which satisfies the PRD's bar and not the face's setting; the file that owns it is outside the lane the face declared. THE MECHANISM (the CVO's L8 read, 19606): the brief DID measure and SAID what it measured -- PLATFORM_ATTACK_SURFACE_ASSESSMENT_20260902.md:95 'WAF logging (CloudFront ACL) | not configured', a row scoped to ONE ACL; PRD FWD-5's SOURCE line carries it without the qualifier; manifest S5 says 'BOTH ACLs'; the face says 'all OFF today'. A scoped measurement lost its scope at each relay and reached L6 as a universal -- not a referent never read, a referent read once and generalised. The issuer took the face's two settings (400 d, the Lane path) from the reading, not from a read of the module. Z-S13 stays ARMED on its own row for 3.0.0_SA_CVO~Z's disposition; this row records the disarm of the work.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "ruling 2.0.0_SA_COO~Z -> 0.7.0_AE_CloudOps~Z 2026-09-03 09:2xZ (operating note); the worker's row Z-S13 surfaced 09:14Z at the pre-write read, NOTHING EDITED on the regional side",
    "0.7.0_AE_CloudOps~Z row Z-S13, LIVE: get-logging-configuration on the CLOUDFRONT ACL -> WAFNonexistentItemException; on the REGIONAL ACL -> LoggingConfiguration with LogDestinationConfigs = aws-waf-logs-opal-gateway and six RedactedFields; describe-log-groups --log-group-name-prefix aws-waf-logs- -> exactly one group, retentionInDays 90, storedBytes 84723696 (the discriminator against a declared-but-idle configuration)",
    "3.0.0_SA_CVO~Z 19606 (L8, DESIRED plane at HEAD 783cd86750, independent of the worker's reads): infra/aws/terraform/opal-gateway/waf.tf @a7312b946b :194 aws_wafv2_web_acl_logging_configuration 'gw', :195 log_destination_configs, six redacted_fields blocks, :23 retention_in_days = 90; the face's Lane path holds 14 entries and 0 .tf; the brief's :95 row scoped to the CloudFront ACL, the PRD's :96 SOURCE line without the qualifier",
    "TO-OP-S-5 face: S5-AC5 '>= 7 days on every destination'; bound 'Retention values are settings; >= 7 d is the bar. No shorter retention anywhere.'"
   ]
  },
  "notes": "THE SIXTH REFERENT OF ROUND 1 WRITTEN FROM A READING (key, roles, target, separator, carrier, and now a control's existence + its file); this one is the relay class: the brief measured one ACL and said so, and every relay after it dropped the scope. THE THIRD ROUND-2 CUT RULE, banked with the two before it: a relayed measurement carries its scope or it is not relayed -- and a face that says 'create X' names the read that shows X absent, per instance, before it is cut. WHAT THIS ROW IS NOT: a re-file, a face edit, or a disposition of Z-S13 (the CVO's)."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S17",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~S (L7 worker, TO-OP-S-8, planning the opal-users-v2 limb at its real carrier)",
  "surfaced_at": "2026-09-03T09:30:56Z",
  "one_line": "TWO findings on the opal-users-v2 limb, one corrective and one hazardous. (1) CARRIER: the table is managed by infra/aws/terraform/shared-infra/dynamo.tf, NOT portal-auth/dynamodb.tf as the face and ruling 19600 both say -- terraform state proves it (shared-infra holds aws_dynamodb_table.opal_users_v2; portal-auth holds the LEGACY opal_users), and portal-auth's two opal-users-v2 mentions are COMMENTS at :167/:173 recording that the TWIN was removed 2026-06-29. (2) HAZARD: shared-infra's BASELINE plan is NOT clean -- 0 add / 1 change / 0 destroy on aws_s3_bucket_lifecycle_configuration.global_graph, an unrelated globgrph rule (ms-heat-snapshots-expire-60d) belonging to another seat. An unscoped apply for this cell would have carried a foreign change, against the bound 'nothing else rides the apply'.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z (issuer, L6) for the CARRIER half -- a correction to the face's and the ruling's named path, which this seat records rather than adjudicates. The DRIFT half is owned by whoever holds globgrph / shared-infra: the unapplied global_graph lifecycle change is NOT this seat's to apply, revert or investigate. This seat DISARMS the hazard for its own act by scoping the apply (-target=aws_dynamodb_table.opal_users_v2), which is the mechanism the bound calls for; the drift itself remains ARMED for its owner and is left exactly as found.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "terraform -chdir=infra/aws/terraform/shared-infra state list -> includes aws_dynamodb_table.opal_users_v2; terraform -chdir=infra/aws/terraform/portal-auth state list -> aws_dynamodb_table.opal_users (LEGACY), opal_firms, opal_offices, opal_sessions, portal_auth_mfa, portal_auth_throttle, user_permissions -- NO opal_users_v2. The two modules do not both manage it.",
    "comp-read infra/aws/terraform/portal-auth/dynamodb.tf --enumerate 'opal-users-v2|opal_users_v2' -> 2 hits, BOTH comments: ':167 # --- opal-users-v2 --- TWIN REMOVED 2026-06-29 (CVO dispatch a47d169ef) ---' and ':173 # De-duped: `terraform state rm aws_dynamodb_table.opal_users_v2` (live table ...)'. So the face's TO-OP-S-8 check 'confirm none of the five tables is ALSO declared there -- a table declared twice is a row' PASSES: it is declared once, and a prior twin was already removed by the estate in June.",
    "shared-infra BASELINE plan, run BEFORE any edit by this seat: 'Plan: 0 to add, 1 to change, 0 to destroy' with '# aws_s3_bucket_lifecycle_configuration.global_graph will be updated in-place' -- adding a rule id ms-heat-snapshots-expire-60d, filter prefix warehouse/ms_heat/snapshots/, expiration 60 days. Nothing in this cell touches globgrph or that bucket.",
    "CONTROL that the baseline read is real and not a stale-state artifact: the sibling module partner-firms was planned the same way in the same minute and read '0-diff / No changes', so a dirty baseline is a property of shared-infra, not of this seat's tooling or credentials.",
    "SCOPED plan after this seat's edit: 'aws_dynamodb_table.opal_users_v2 will be updated in-place / Plan: 0 to add, 1 to change, 0 to destroy', with Terraform's own 'Warning: Resource targeting is in effect' printed and recorded rather than suppressed.",
    "The scoped plan changes EXACTLY ONE attribute, read from terraform show -json: deletion_protection_enabled False -> True. server_side_encryption reads [{'enabled': True, 'kms_key_arn': ''}] BEFORE and AFTER -- identical -- so the apply does NOT drop the live table's SSE despite the resource block declaring no server_side_encryption. That was the specific hazard checked, not assumed."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-OP-S-8 DELIVERABLE 1 and its Lane place opal-users-v2 in `infra/aws/terraform/portal-auth/dynamodb.tf`, and issuer ruling 19600 item 2 repeats that path. The face's bound requires that 'nothing else rides the apply' and that the plan read 0 to add / 0 to destroy on every table, which presupposes the module being applied is otherwise clean.",
  "world_is": "opal-users-v2 is declared and state-managed in shared-infra/dynamo.tf; portal-auth only carries the historical comments of a twin removed in June. And shared-infra is NOT otherwise clean: it carries an unapplied, unrelated globgrph lifecycle change from another seat. The two findings compound -- following the face's named path would have found no resource to edit, and editing the real one and applying the module unscoped would have shipped a foreign change under this cell's ledger entry and this seat's author line. Neither failure announces itself: the first looks like a missing declaration, the second looks like a successful apply.",
  "notes": "WHY A ROW: a spec-vs-world divergence (the carrier) plus an estate condition found off-task (the drift), both surfaced BEFORE the apply. The carrier half is the FIFTH instance this project of a face naming a referent that was never read -- after the key (Z-S3), the roles (Z-S4), the log target (Z-S5) and the demo table's management (Z-S14) -- and it is worth the issuer's attention as a pattern rather than as five separate corrections. NOT CHASED: the global_graph drift is left EXACTLY as found. This seat did not apply it, did not revert it, and did not investigate whose it is beyond naming the resource; a foreign unapplied change is its owner's, and touching it would be the never-widen violation this row exists to avoid. HOW THE ACT PROCEEDS ANYWAY: the apply is SCOPED with -target=aws_dynamodb_table.opal_users_v2, which is the sanctioned mechanism for 'nothing else rides the apply' (cloud-ops pre-flight step 2 permits targeting and requires it be declared). ITS OWN TRAP, NAMED AND AVOIDED: a -target apply verified by a -target re-plan proves nothing, because the scoped check cannot see what the scope excluded. Verification is therefore an UNSCOPED re-plan whose PASS condition is two-sided -- opal_users_v2 shows 0-diff AND the global_graph drift is still present and untouched. A clean unscoped plan would mean this seat had silently applied someone else's change. CLOSING CONDITION: the carrier half is DISARMED when the issuer records the correct path; the drift half is REMEDIATED only by its owner applying or withdrawing it. FALSIFIER for the carrier half: a terraform state entry for opal_users_v2 under portal-auth."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S18",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "surfaced_by": "2.0.0_SA_COO~Z (issuer, L6; the named disarm_owner of Z-S17). A DISARM RECORD, not a new finding and not an adjudication (no `adjudicates`; L9 is 3.0.0_SA_CVO~Z's).",
  "surfaced_at": "2026-09-03T09:35Z",
  "one_line": "DISARM RECORD for NFRA_OPSEC202609-Z-S17 (BLOCKING, surfaced BEFORE the fourth apply of TO-OP-S-8: (1) opal-users-v2 is managed by infra/aws/terraform/shared-infra/dynamo.tf -- state list aws_dynamodb_table.opal_users_v2 -- NOT portal-auth/dynamodb.tf as the face and the issuer's 19600 item 2 both said (portal-auth's state holds the LEGACY opal_users; its two v2 mentions are comments recording the 2026-06-29 de-dup via state rm); (2) shared-infra's BASELINE plan is not clean: aws_s3_bucket_lifecycle_configuration.global_graph 1 to change, adding rule ms-heat-snapshots-expire-60d -- a committed, UNAPPLIED, FOREIGN change an unscoped apply would ship under this cell's ledger and author line; partner-firms planned clean in the same minute as the control): RULED 2026-09-03 09:32Z (operating note to 0.7.0_AE_CloudOps~S) -- GO on the SCOPED apply as the worker designed it: -target=aws_dynamodb_table.opal_users_v2 DECLARED in ledger entry opsec-s8-users-v2-deletion-protection, the scoped plan reading exactly ONE attribute (deletion_protection_enabled False -> True; server_side_encryption identical before and after in terraform show -json, the check that the apply would not drop SSE-KMS on the identity table); the PASS condition TWO-SIDED on an UNSCOPED re-plan -- opal_users_v2 0-diff AND the global_graph drift STILL PRESENT untouched (a clean unscoped plan would mean the cell silently shipped another module's change: a failure, not a success); S8-AC3's TableId + CreationDateTime control on this table as on the three; the carrier correction ACCEPTED for the face and the ruling; the foreign drift left exactly as found and routed as a FABRIC item to 0.0.0_AB_MSTR~Z and 1.0.0_SA_CTO~Z the same turn.",
  "spec_asserts": "TO-OP-S-8 face and the issuer's ruling 19600 item 2: opal-users-v2's carrier is portal-auth/dynamodb.tf; the face's bound: a plan that would REPLACE any table is a STOP and a row; the cloud-ops pre-flight permits a -target apply only with targeting declared. Row Z-S17 named disarm_owner 2.0.0_SA_COO~Z; the worker stated it would proceed to commit and apply unless the issuer said otherwise.",
  "world_is": "The identity table is declared once, in shared-infra, and the estate de-duplicated it in June; the face named the module that USED to hold a twin. The shared module's committed state is ahead of its applied state by one foreign lifecycle rule, so any unscoped apply there is a carrier for someone else's change -- the scoped apply with a two-sided unscoped verification is the only shape that changes one attribute and proves it changed nothing else. The issuer did not chase, apply, or revert the foreign drift; it is its module owner's (the global-graph resource), with the fabric's operator holding the /govern read. Z-S17 stays on its own row for 3.0.0_SA_CVO~Z's disposition; this row records the disarm of the work.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "ruling 2.0.0_SA_COO~Z -> 0.7.0_AE_CloudOps~S 2026-09-03 09:32Z (operating note; GO on the scoped apply as designed); the worker's BLOCKING notification 19619 09:31Z, surfaced BEFORE the apply, three partner tables already DONE (0 add / 3 change / 0 destroy; TableId + CreationDateTime identical; PITR EarliestRestorableDateTime 2026-09-03T05:24:22-04:00; MFA/throttle byte-identical; re-plan 0-diff; baseline read clean BEFORE the edit)",
    "0.7.0_AE_CloudOps~S row Z-S17: shared-infra `terraform state list` -> aws_dynamodb_table.opal_users_v2; portal-auth state list -> aws_dynamodb_table.opal_users (legacy), no v2; portal-auth/dynamodb.tf :167/:173 comments 'TWIN REMOVED 2026-06-29 (CVO dispatch a47d169ef)'; shared-infra baseline plan 0 / 1 / 0 naming aws_s3_bucket_lifecycle_configuration.global_graph (rule ms-heat-snapshots-expire-60d, prefix warehouse/ms_heat/snapshots/, 60 d); scoped plan -target=aws_dynamodb_table.opal_users_v2 -> 0 / 1 / 0, `terraform show -json`: deletion_protection_enabled False -> True, server_side_encryption [{enabled: True, kms_key_arn: ''}] before AND after",
    "the fabric items to 0.0.0_AB_MSTR~Z (09:33Z) and 1.0.0_SA_CTO~Z (09:33Z, item 4 of the v0.1.4 delivery): the foreign unapplied change in shared-infra, left as found"
   ]
  },
  "notes": "THE SEVENTH REFERENT OF ROUND 1 WRITTEN FROM A READING (key, roles, target, separator, the regional control + its file, the demo table's management, this carrier) -- and the second time the issuer REPEATED the face's wrong carrier in a ruling (19600 item 2) rather than reading it: the ruling is a face too. The banked round-2 cut rule applies to operating notes as well: name a carrier only after a state list or a `git show` has returned it this round. WHAT THIS ROW IS NOT: a re-file, a face edit, or a disposition of Z-S17 (the CVO's); nor an act on the foreign drift."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S19",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z (L9 adjudication row; the round's one slug at L10)",
  "surfaced_at": "2026-09-03T10:36:19Z",
  "one_line": "L9 ADJUDICATION, round 1: the ten grounded items GRADUATE -- S1, S2, S3, S4, S5, S10, S11, S13, S14, S17 -- each with its mechanism attributed at source or on a live primitive with a control, its denominators carried, and its remedy holder named. The remediation document REMEDIATION_v1.Z.md carries the five whose remedy needs a cell the decomposition already contains (S3, S4, S5, S10, S14 -> SPEC_ERROR -> 6). The other five carry no remediation row and their facts are carried on this row's evidence: S2, S11, S13, S17 remediated inside round 1 and closed; S1 a fabric surface homed by the register, disarmed by this seat's lane-addressed pointer at the stamp.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_OPSEC202609-Z-S1",
   "NFRA_OPSEC202609-Z-S2",
   "NFRA_OPSEC202609-Z-S3",
   "NFRA_OPSEC202609-Z-S4",
   "NFRA_OPSEC202609-Z-S5",
   "NFRA_OPSEC202609-Z-S10",
   "NFRA_OPSEC202609-Z-S11",
   "NFRA_OPSEC202609-Z-S13",
   "NFRA_OPSEC202609-Z-S14",
   "NFRA_OPSEC202609-Z-S17"
  ],
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "Each adjudicated item's grounding was re-derived at this seat on an instrument other than its surfacing seat's, recorded in this file's L8 narrative under the item's heading (S1 07:17Z; S2/S3 08:1xZ; S4/S5 08:3xZ; S10 08:5xZ; S11 09:0xZ; S13/S14 09:2xZ; S17 09:3xZ), with the instrument and its denominator named each time",
    "The L10 precondition read at the stamp: every task order under the project terminal with a VALID proof-of-spec instance whose surprises entries resolve to rows (TO-OP-S-3 @a491aaec8c / instance @3c32f20c38; TO-OP-S-17-16 @f9b2a16c2c; TO-OP-S-8 @2da0c78f6a; TO-OP-S-5 @f49c82b891) -- checked at this seat by schema (Draft7, 0 errors each) and by resolving every surprises id against this file's block, and by the issuer's coverage-checked runs (19595, 19634, 19646)",
    "The dispositions are grouped by value, one adjudication row per value, because a row's disposition applies to every id it adjudicates (org/ref/SURPRISE_CHANNEL_PROTOCOL.md section 4, 'Setting a disposition'); the disarm records S6-S9, S12, S15, S16, S18 are adjudicated by the sibling row Z-S20",
    "FABRIC ITEM (no remediation row; homed by the register, 0.0.0_AB_MSTR~Z 19629): NFRA_OPSEC202609-Z-S1 -- class OBSERVATION / ARMED; disarm DISARMED by 3.0.0_SA_CVO~Z at 2026-09-03T10:36:19Z; remediation OPEN, owner 1.0.0_SA_CTO, round v2; closed False; remedy: A lane-aware recipient in the notifier (the laptop's e58250f261 when it reaches SITEZ); until then every L4 and L10 handoff on this device is accompanied by a hand-sent lane-addressed pointer.; builder: 1.0.0_SA_CTO (notifier/gate surface; the laptop's commit is the carrier); mechanism: .tools/prd-header-notify.py @e906c6f156 addresses BASE serials only (:49 RECIPIENT default 2.0.0_SA_COO; :68 ROUTE_OWNER {2: 1.0.0_SA_CTO, 5/6: 2.0.0_SA_COO}; :364 sends to that owner with no lane lookup); on site Z every live seat is a ~Z lane and the base inboxes are unwatched, so the L4 and L10 handoffs re-offer to a dead inbox until a READ that cannot come.",
    "CLOSED IN ROUND 1 (no remediation row; carried here verbatim): NFRA_OPSEC202609-Z-S2 -- class OBSERVATION / ARMED; disarm DISARMED by 2.0.0_SA_COO~Z at 2026-09-03T08:04:00Z; remediation REMEDIATED, owner 2.0.0_SA_COO~Z, round v1; closed True; remedy: Design call (a) ACCEPTED: state-at-rest is the value's resting place on the measured mitigations (SSE-S3 + full public-access-block; the value proves path-of-entry only; a rotation bounds a state-history read to one window); wording clarifications inside the worker's deliverables (secrets.tf's invariant scoped to the JWT keypair; the runbook names the state-history residual). The state bucket's missing noncurrent-version expiry is homed OUT of this project (0.0.0_AB_MSTR~Z 19629: a steward item on the debt baseline, or a D0 brief at 4.0.0_SA_CRO).; builder: 2.0.0_SA_COO~Z (the design call, recorded); the lifecycle item's steward is 0.7.0_AE_CloudOps, gate 1.0.0_SA_CTO, outside this project; mechanism: A CloudFront custom origin header value is returned in full by cloudfront:GetDistributionConfig, so the origin secret is written into Terraform state by construction on every write path; the portal-auth state bucket is versioning-Enabled with NO lifecycle, so superseded values persist indefinitely; portal-auth/secrets.tf:5-7's invariant ('key material never enters Terraform state') does not hold for the new secret.",
    "CLOSED IN ROUND 1 (no remediation row; carried here verbatim): NFRA_OPSEC202609-Z-S11 -- class BLOCKING / ARMED; disarm DISARMED by 2.0.0_SA_COO~Z at 2026-09-03T08:56:21Z; remediation REMEDIATED, owner 1.0.0_SA_CTO~Z, round v1; closed True; remedy: Done on both halves: the face @beacddcf26 (issuer) and the checker @50ff3d674a (CTO), documented in DECOMP_CELL_ID_CONVENTION.md; exercised by the issuer's coverage run on the fixed checker (19634).; builder: 2.0.0_SA_COO~Z (face) and 1.0.0_SA_CTO~Z (checker) -- both landed; mechanism: TO-OP-S-17-16's S1716-AC4 declared cell_refs='OP-s-17 OP-s-16' space-separated; .tools/proof-of-spec-check.py:562 split cell_refs on a comma only, read the pair as one literal matching no cell, and refused an otherwise-valid instance; the separator convention was undocumented and the same file read <owned_cells> tolerantly.",
    "CLOSED IN ROUND 1 (no remediation row; carried here verbatim): NFRA_OPSEC202609-Z-S13 -- class OBSERVATION / ARMED; disarm DISARMED by 2.0.0_SA_COO~Z at 2026-09-03T09:26:00Z; remediation REMEDIATED, owner 2.0.0_SA_COO~Z, round v1; closed True; remedy: Done for this project: the regional half is discharged by prior state at its real carrier; the CloudFront half proceeds under TO-OP-S-5. The face's lane defect and the relay's scope loss are covered by the issuer's third round-2 cut rule (a relayed measurement carries its scope; a Terraform deliverable names the declaration carrier of every resource it edits, read live).; builder: 2.0.0_SA_COO~Z (the ruling and the cut rule); mechanism: The face said WAF logging was OFF on both ACLs; the regional ACL has had a live, Terraform-declared logging configuration since 2026-08-14 (opal-gateway/waf.tf:194 @a7312b946b, retention 90 d), delivering to the exact group the face named; the brief measured only the CloudFront ACL and said so (:95), and the qualifier was dropped at the PRD's SOURCE line, the manifest and the face -- a scoped measurement generalised in relay; the face's Lane path holds no Terraform.",
    "CLOSED IN ROUND 1 (no remediation row; carried here verbatim): NFRA_OPSEC202609-Z-S17 -- class BLOCKING / ARMED; disarm DISARMED by 2.0.0_SA_COO~Z at 2026-09-03T09:32:00Z; remediation REMEDIATED, owner 2.0.0_SA_COO~Z, round v1; closed True; remedy: Done for this project: the carrier corrected in the GO and the table protected in place (TO-OP-S-8 complete @2da0c78f6a; TableId and CreationDateTime identical); the issuer's cut rule covers the carrier class. The drift (apply-or-retire the global_graph rule) is a fabric item routed to the laptop with 0.8.0_AE_CloudComp / NFRA_GLOBGRPH as the owner class (19629).; builder: 2.0.0_SA_COO~Z (the GO and the cut rule); the drift's owner class is 0.8.0_AE_CloudComp, placement the laptop's; mechanism: opal-users-v2 is managed by shared-infra/dynamo.tf, not the portal-auth/dynamodb.tf the face and the issuer's ruling both named -- a correction that already existed in three places (the target file's own comment block since 2026-06-29; this channel's S3 evidence; the issuer's own 19504) and did not reach the ruling; and shared-infra's baseline plan carried a foreign unapplied change (a global_graph lifecycle rule committed 2026-07-15 @4cd024c5c6 by 0.8.0_AE_CloudComp~Z) that an unscoped apply would have shipped."
   ]
  },
  "disposition": "GRADUATED",
  "spec_asserts": "Spine L9 (org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md v2.3): 'a disposition on every row ... and, for graduated rows, remediation rows ... issued as ONE slug for the round at L10 (one artifact, one moment)'; the graduation bar is a grounding bar.",
  "world_is": "Ten of the round's eighteen rows are findings and every one is grounded on its own evidence and re-derived here; eight are the issuer's disarm records for the ARMED findings and are not findings themselves. Seven of the ten findings say the same thing about the loop's inputs: a face asserted something about the world that the world did not hold (a label taken for a fact; a name never measured; a scoped measurement generalised in relay; a correction that never reached the ruling that needed it), and every one was caught by the workers' mandated pre-write re-grounding before a destructive act -- zero destructive acts this round. The other three are the loop's own instruments: the notifier's base-serial addressing (S1), the checker's undocumented separator (S11), and a deny belt whose justification outlived its premise (S10).",
  "notes": "WHAT THE SLUG DOES AND DOES NOT DO. It dispositions; it does not re-cut a face, re-decompose, or write to a worker. Five routes go to 2.0.0_SA_COO~Z at L6 as one artifact (the remediation document) and to no one else; the mechanical notifier's delivery to the BASE serial is disarmed by this seat's lane-addressed pointer to 2.0.0_SA_COO~Z in the same turn (S1's own disarm act). NO row is DECOMP_INVALIDATING: every remedy that needs building sits on a cell the decomposition already contains at v0.1.4 (OP-s-25, OP-s-26, OP-s-27, OP-s-8's import limb, OP-s-14/15/19's deny statement, OP-s-1/OP-s-2's portal-auth face carrying S10's rider). NO row is SCOPE_CHANGE: the three ratified-constraint contradictions (C-8's key, roles and target) were corrected at L4 by the L4 owner's own act (v0.5, v0.6, v0.7), disclosed to Andrew and reversible by his word, before this stamp -- the remedy for each is a round-2 task order on an existing cell, which is SPEC_ERROR, not a re-entry at L2. The round is not a zero-graduation round, so the project does not close; round 2 opens on the routed rows. WHY FIVE REMEDIATION ROWS AND NOT TEN: the row gate requires route + loop_target on every NEW remediation row; the schema does not require them and protocol s.8 defines route as the re-entry decision, which has no value for a remedied or out-of-project item -- writing one would put a second intent on the axis (rule 24 iii). The gate's named override is read by safe-commit only for the legacy org/surprise_channel spelling; tree-path files are graded by the pre-commit hook, which reads no message, so the escape cannot fire for a tree project (exercised twice on this slug). The five items without a row are carried on this row's evidence, verbatim; the divergence is a round-2 intake row."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S20",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z (L9 adjudication row; the round's one slug at L10)",
  "surfaced_at": "2026-09-03T10:36:19Z",
  "one_line": "L9 ADJUDICATION, round 1: the eight DISARM RECORDS -- S6, S7, S8, S9, S12, S15, S16, S18 -- are DISMISSED WITH REASON: each is the record of a disarm act by its named owner, not a finding; its content is carried on the item it disarms and in that item's remediation row (disarm.state DISARMED, owner, at), so it seeds no remediation row of its own.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "NFRA_OPSEC202609-Z-S6",
   "NFRA_OPSEC202609-Z-S7",
   "NFRA_OPSEC202609-Z-S8",
   "NFRA_OPSEC202609-Z-S9",
   "NFRA_OPSEC202609-Z-S12",
   "NFRA_OPSEC202609-Z-S15",
   "NFRA_OPSEC202609-Z-S16",
   "NFRA_OPSEC202609-Z-S18"
  ],
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "Each of the eight rows names itself a DISARM RECORD in its surfaced_by and one_line, carries no adjudicates field, and cites the item it disarms by id; each is OBSERVATION / INERT by its own terms",
    "Each disarm act is carried onto the disarmed item's remediation row in REMEDIATION_v1.Z.md as disarm {state: DISARMED, owner: 2.0.0_SA_COO~Z, at: <the record's own timestamp>}, so dismissing the record loses nothing the L10 gate reads",
    "The D1_CATVIEWS-Z-S4 precedent (2.0.0_SA_COO~Z, 2026-09-03 07:03Z): a disarm record is 'not a new finding and not an adjudication'"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A disarm record is the record of an act, not a finding: it has no mechanism of its own to graduate and no remedy of its own to route. Its substance -- who disarmed what, when, on what grounding -- is carried verbatim on the disarmed item's remediation row, which is the carrier the L10 gate and the next round read. Dismissing the record keeps the channel's item count honest (ten findings, not eighteen) without losing a byte of what the record said.",
  "spec_asserts": "Protocol section 4: 'not valid or not worth carrying is dismissed with its reason'; section 5: the remediation row carries the two-state disarm block; section 0: a reader resolves a row's state from the newest row that cites it.",
  "world_is": "Eight of the round's eighteen rows are disarm records, each valid, each already reflected in the remediation row of the item it cites; carrying them forward as items would count eight acts as eight findings.",
  "notes": "Nothing is lost: the records stay on this file's block byte-identical (append-only), and each remediation row's disarm block names the record's owner and timestamp. If a later reader wants the disarm's grounding, the record row is the citation."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S21",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "surfaced_by": "1.0.0_SA_CTO~Z (the named disarm_owner of Z-S10; L4 owner; the /self-drive driver). A DISARM RECORD, not a new finding and not an adjudication (no `adjudicates`; L9 is 3.0.0_SA_CVO~Z's).",
  "surfaced_at": "2026-09-03T11:42Z",
  "one_line": "DISARM RECORD for NFRA_OPSEC202609-Z-S10 (OBSERVATION/ARMED: infra/aws/terraform/portal-auth/cross-firm-secret-deny.tf:6-10 justifies its Deny belt on the premise that three roles hold a secret:opal/* WILDCARD, a premise Phase A of 2026-07-09 retired for at least opal-portal-lambda-role): DISARMED 2026-09-03T11:42Z by the row's SECOND shape, the record -- THE DENY BELT IS CORRECT AND STAYS; it is now defence-in-depth over explicit allowlists rather than a subtraction from a wildcard, and a reader of that file must NOT infer that any opal/* secret is already granted to those roles: every new secret needs its own explicit Allow, which is exactly why OP-s-3's authorizer grant was written from the live primitive and not from the comment. The narrative correction at :6-10 is the file's own lane's act (CLOUD_OPS_OR_ETL per .owned-paths.yaml; not this seat's), routed as a RIDER on the round-2 portal-auth face (TO-OP-S-1-2 at 0.7.0_AE_CloudOps~Z; S10's remediation row @fdbe7360b9 carries it as SPEC_ERROR -> 6) with the row's own scope bound written in: measure all three named roles by simulate-principal-policy (one --resource-arns per call, a positive control as a separate invocation) BEFORE rewriting the sentence. No security control changed; no .tf edited by this seat.",
  "spec_asserts": "Z-S10's disarm condition, verbatim in shape: 'DISARM = correct the WHY-narrative at cross-firm-secret-deny.tf:6-10 to describe the post-Phase-A grants, or record that the belt is now defence-in-depth over an allowlist rather than a subtraction from a wildcard. THE DENY ITSELF IS CORRECT AND MUST NOT BE REMOVED -- only its stated justification is stale.' Its scope bound: 'one role measured, two named roles NOT measured; a re-checker should measure all three before rewriting the sentence.' Its falsifier: 'if simulate-principal-policy on opal-portal-lambda-role returns allowed for an arbitrary new opal/<anything> ARN, the wildcard is back and this row is wrong.'",
  "world_is": "The second shape is taken here, on the record, by the named disarm owner: the belt stands as defence-in-depth over allowlists; the stale rationale is named as stale in the project's own channel; the file's text is unchanged at :6-10 pending its lane's rider. WHY THE RECORD AND NOT THE EDIT: the file's commit lane is CLOUD_OPS_OR_ETL (0.5.0/0.6.x/0.7.0/0.8.0 AE classes), not the CTO's, although the CTO authored the amended ruling in its header; an audited author override for a comment edit mid-round would spend a singular escape on a narrative, and the round-2 face already touches portal-auth in that lane. The sound claim stays scoped exactly as Z-S10 scoped it: opal-portal-lambda-role measured (its three secrets policies are explicit allowlists; a new opal/auth/* ARN reads implicitDeny; the role-specific positive control reads allowed); opalinvest-auth-lambda-role and news-ingestion-lambda-role NOT re-measured by this seat, the rider measures them. The 2026-07-09 narrowing is recorded on two other carriers (iam.tf:61 'NARROWED 2026-07-09 (Phase A). Was opalinvest/* + opal/* in both regions'; infra/security/remediation/secrets-allowlist-narrowing-and-least-privilege-PLAN-20260709.md:55), so the premise at :6-10 has been stale for 56 days on a file whose own header says it grounded before authoring -- a grounded-then-frozen rationale, the same class as the three referents of C-8.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "infra/aws/terraform/portal-auth/cross-firm-secret-deny.tf:5-18 @435dcf9d85 -- the FINDING paragraph ('secret:opal/* wildcard grants let three portal/news-plane roles read ...') and the WHY-A-DENY paragraph ('the grant is a WILDCARD ... IAM has NO resource-exclusion syntax'); read at HEAD by this seat before this row",
    "NFRA_OPSEC202609-Z-S10 grounding (0.7.0_AE_CloudOps~Z, 2026-09-03): simulate-principal-policy, ONE --resource-arns per call: opal-portal-lambda-role on opal/auth/origin-verify-* = implicitDeny; role-specific positive control opal/auth/jwt-public-key-* on the SAME role = allowed; live get-role-policy: three explicit allowlist policies, no opal/* wildcard -- carried as the worker's measurement, not re-run here",
    "infra/aws/terraform/portal-auth/iam.tf:61 @435dcf9d85 -- the sibling role's note 'NARROWED 2026-07-09 (Phase A). Was opalinvest/* + opal/* in both regions.'",
    "infra/security/remediation/secrets-allowlist-narrowing-and-least-privilege-PLAN-20260709.md:55 -- independently records opal-portal-lambda-role's inline SecretsManagerAccess as having been secret:opal/* and narrowed to an allowlist",
    ".owned-paths.yaml -- infra/aws/** resolves to lane CLOUD_OPS_OR_ETL (permitted: the AE classes; 1.0.0_SA_CTO not among them), measured by this seat's lane resolver before choosing the record shape",
    "surprise-channel/remediations/REMEDIATION_v1.Z.md @fdbe7360b9 (3.0.0_SA_CVO~Z) -- S10's remediation row routes the rider SPEC_ERROR -> 6 onto TO-OP-S-1-2 with this scope bound; 2.0.0_SA_COO~Z 19648/19667 -- the round-2 portal-auth faces at 0.7.0_AE_CloudOps~Z: the rider's carrier"
   ]
  },
  "notes": "WHAT THIS ROW DOES NOT CLAIM: anything about opalinvest-auth-lambda-role or news-ingestion-lambda-role (unmeasured by both seats); that the Deny belt should move (it must not); that the file's text is corrected (it is not, until the rider lands). WHAT IT ASKS OF NOBODY NOW: round 1 is stamped and this row is INERT; the rider is the COO's on the round-2 face and the ~Z worker's to execute in its own lane, measuring all three roles first. THE CLASS, stated once for the L8 narrative: a rationale grounded at authoring and then frozen while the world it described was narrowed 56 days later by a sibling program -- the fourth 'referent asserted from a reading' of this round after the key, the roles and the target, except that this one was TRUE when written; the fix for that class is a rationale that names its vintage, which the rider should add (a 'measured at <date>' line on :6-10)."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S22",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z (DISARM RECORD for NFRA_OPSEC202609-Z-S1; disarm_owner named on Z-S1 itself)",
  "surfaced_at": "2026-09-03T11:46:13Z",
  "one_line": "DISARM RECORD for NFRA_OPSEC202609-Z-S1 (the notifier's base-serial addressing): DISARMED at the round-1 L10 stamp @fdbe7360b9 by 3.0.0_SA_CVO~Z's lane-addressed pointer to 2.0.0_SA_COO~Z carrying the route document, delivered 2026-09-03T11:28:06Z (inbox 2.0.0_SA_COO/~Z, file 20260903T112806Z_3.0.0_SA_CVO_Z_L10_STAMP_NFRA_OPSEC202609_round_1__fdbe.md, filesystem + broker + channel push) beside whatever the mechanical kind:route delivery addressed to the BASE serial. DISARMED is not REMEDIATED: the remedy (a lane-aware notifier; the laptop's e58250f261 reaching SITEZ) stays OPEN on the fabric register (0.0.0_AB_MSTR~Z 19629), owner 1.0.0_SA_CTO; every L4 and L10 handoff on this device keeps its hand-sent lane pointer until then.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "Z-S1 at HEAD names disarm_owner 3.0.0_SA_CVO~Z at L10 by lane pointer; protocol s.6: a disarm is reported as a new row citing the armed row; s.5: DISARMED is not REMEDIATED (two states, two owners, two clocks)",
    "The act: send_message 3.0.0_SA_CVO~Z -> 2.0.0_SA_COO~Z at 11:28:06Z, subject 'L10 STAMP NFRA_OPSEC202609 round 1 @fdbe7360b9 ...', receipt 'delivered ... (filesystem + broker + channel push)'; the same turn's pointers to 1.0.0_SA_CTO~Z (11:28:29Z) and 0.0.0_AB_MSTR~Z (11:28:41Z) name the disarm",
    "Why a row and not the remediation document: the round's remediation document carries the five re-entry rows only (see Z-S19's notes and the document header); S1's remedy is outside the project's cells, so its disarm is recorded here, item-side, exactly as the issuer's disarm records S6-S18 were"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Z-S1 (HEAD): disarm_owner 3.0.0_SA_CVO~Z, disarms at L10 by a lane-addressed pointer beside the mechanical base-serial delivery; protocol s.6 and s.5 as cited.",
  "world_is": "The lane-addressed pointer carrying the L10 route document was delivered to 2.0.0_SA_COO~Z at 11:28:06Z; Z-S1's hazard (an L10 handoff reaching only the base serial) did not occur for this stamp. The notifier's addressing is unchanged on SITEZ until e58250f261 lands here, so the hazard re-arms at every future L4/L10 handoff unless the hand-sent pointer accompanies it.",
  "notes": "Record of an act, not a finding; it adjudicates nothing and seeds no remediation row. Reader rule (protocol s.0): the newest row citing Z-S1 carries its disarm state -- this one."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S23",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z (surfaced at the round-1 L10 stamp; fabric gate scope, owner 1.0.0_SA_CTO)",
  "surfaced_at": "2026-09-03T11:46:13Z",
  "one_line": "FABRIC GATE: .tools/surprise-row-gate.py refuses any NEW remediation row without route + loop_target (docstring :12; _check_row :439-444), with no exemption for remediation.state REMEDIATED or an out-of-project remedy, while remediation_row.schema.json leaves route/loop_target optional and enumerates REMEDIATED, and protocol s.8 :177 defines route as the re-entry decision ('what does the remedy need that does not exist yet?') with no value for 'nothing'; AND the escape the gate prints ('# surprise-row-override: <reason>' in the commit body) is unreachable for a tree project on this device: the reader is .tools/safe-commit.sh :641-690, keyed on the legacy *org/surprise_channel/* spelling (:645), while tree paths are refused by .git/hooks/pre-commit :137-138 (python surprise-row-gate.py $STAGED || exit 1), which reads no message; the gate's own OVERRIDE_RE (:81) is defined and never applied. Exercised on the round-1 slug: 10:36:19Z refused with 12 violations (six rows without route); 11:19:30Z refused with 10 violations with the marker line in the -F file, no 'WARN: surprise-row-gate OVERRIDDEN' line and no audit entry. Consequence: four items remediated inside round 1 (S2, S11, S13, S17) and one fabric item (S1) carry no remediation row, so the machine-readable closed flag of s.5 exists for none of them; their facts ride Z-S19's evidence verbatim.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    ".tools/surprise-row-gate.py @HEAD: docstring :12 'NEW remediation row -> must carry route AND loop_target'; _check_row :439-444 appends the two violations whenever route or loop_target is None; OVERRIDE_RE :81 compiled, 0 uses (comp-read --enumerate 'OVERRIDE_RE\\.|_message|msg_path|COMMIT_EDITMSG|environ': 0 hits across 743 lines)",
    "org/surprise_channel/schemas/remediation_row.schema.json @HEAD: required = [id, class, hazard_standing, mechanism, evidence, remedy, owner, round, remediation]; route enum of three re-entry values, loop_target enum [2, 5, 6], both optional; remediation.state enum [OPEN, REMEDIATED]; closed described as 'DISARMED IS NOT REMEDIATED ... for other classes, remediation.state=REMEDIATED'",
    "org/ref/SURPRISE_CHANNEL_PROTOCOL.md @HEAD s.8 :163 'Graduated rows receive a remediation row per section 5'; :177-180 route = the re-entry decision, three values, the gate refuses any pair off the map; s.5 :136-141 an INERT row is closed when REMEDIATED, an ARMED row when both states have landed -- on the remediation row",
    ".tools/safe-commit.sh @HEAD :641-690: the override extractor runs only when a dispatched path matches *org/surprise_channel/*INVESTIGATION_v* or *org/surprise_channel/*REMEDIATION_v* (:645); a tree path org/missions/.../surprise-channel/... never enters the block (silent no-op for the path class the tree spec created)",
    ".git/hooks/pre-commit :137-138 on this device (installed by .tools/git-hooks/install-surprise-row-gate.sh): runs the gate on every staged channel file and exits 1 on refusal; a pre-commit hook has no commit message to read",
    "STATE, exercised on the round-1 slug (this seat, safe-commit -F): 10:36:19Z refused (12 violations, six no-route rows); 11:19:30Z refused (10 violations, five no-route rows) with 'surprise-row-override: ...' as a body line of the -F file; neither run printed the WARN OVERRIDDEN line; the slug landed at 11:26:31Z @fdbe7360b9 carrying only the five re-entry rows"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The gate's printed refusal names an audited override as the escape; protocol s.8 and the schema describe remediation rows that carry REMEDIATED and closed with route optional; s.8 says every graduated row receives a remediation row.",
  "world_is": "For a tree project on this device no remediation row can commit without a route, the printed escape cannot fire, and the only truthful way to stamp was to carry the five non-re-entry items on the adjudication row instead of the remediation document -- so three carriers (gate, schema, s.8) disagree and the mechanism wins by construction. A seat under time pressure has the false-route option open (a manufactured L6 re-entry), which nothing refuses.",
  "notes": "Remedy holders as measured, all 1.0.0_SA_CTO's surfaces (this seat proposes, does not edit): (a) the safe-commit case pattern at :645 -- add the tree spelling so the audited override reaches tree paths, or move the override read into the gate itself (it already compiles OVERRIDE_RE) fed by the hook's own message-less context via an env or the -F file; (b) the gate's rule at :439-444 -- an exemption for remediation.state REMEDIATED / closed true and for a remedy homed outside the project, or the protocol's s.8 amended to say the remediation document carries re-entry rows only and closure rides the adjudication row; (c) whichever of (b) is chosen, s.8 :163 and s.5 :136-141 rewritten to match, so the three carriers agree. Sent to 1.0.0_SA_CTO~Z 11:28:29Z with the same text."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S24",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~Z (L7 worker, OP-s-2, at the face's mandated Phase-1 pre-write read)",
  "surfaced_at": "2026-09-03T11:58:00Z",
  "one_line": "TO-OP-S-2 deliverable 1 instructs an aws_apigatewayv2_route resource per route 'in Terraform in portal-auth/', and its Lane clause describes portal-auth/ as holding 'the HTTP API opal-portal-data-proxy-api, its routes and portal-jwt-authorizer'. NONE of those three is in portal-auth: the module declares ZERO aws_apigatewayv2 resources across all 16 of its .tf files. The real carrier is infra/aws/terraform/shared-infra/apigateway-portal/main.tf, which declares the API (aws_apigatewayv2_api.portal) and the authorizer (aws_apigatewayv2_authorizer.portal_jwt) and NO ROUTE AT ALL -- zero aws_apigatewayv2_route resources anywhere for this API. So the nine data routes have NO TERRAFORM CARRIER, which is the same condition that caused the issuer to exclude OP-s-1 (the REST API) from this very GO.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z (issuer) -- this is a buildability question on deliverable 1, not a defect in execution, and it has a real remedy the face does not authorize: terraform import each of the 9 live routes into shared-infra/apigateway-portal/ and THEN set authorization_type/authorizer_id. That is a materially different act in a module the face does not name, so it is the issuer's call and not the worker's. BLOCKING because deliverable 1 CANNOT be performed as written and the alternative reading is actively dangerous (see notes).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "MEASURED 2026-09-03 at this seat: for each of the 16 .tf files in infra/aws/terraform/portal-auth/, a grep -c for 'aws_apigatewayv2' returns 0. POSITIVE CONTROL on the same probe: infra/aws/terraform/partners-api/api-gateway.tf = 13, infra/aws/terraform/bd-pipeline/api-gateway.tf = 7 -- so the probe finds these resources where they exist and the zero is an absence, not a broken matcher.",
    "infra/aws/terraform/shared-infra/apigateway-portal/main.tf @e0df0ac956, read in full (58 lines): it declares aws_apigatewayv2_api.portal (:19) and aws_apigatewayv2_authorizer.portal_jwt (:43, REQUEST, opal-portal-authorizer) and NOTHING ELSE. There is no aws_apigatewayv2_route resource in the file. Its own header at :6-7 says the API 'Serves: ... portal-data-proxy (sentiment/keyword) routes' -- a description of what the API serves, NOT a declaration of the routes.",
    "MEASURED: grep -rl '7k3ed8px20' --include='*.tf' infra/ returns 9 files; none of them declares a route for this API. comp-find 'aws_apigatewayv2_route' -> 260 hits across 51,157 files, all in bd-pipeline, inf-pipeline, partners-api and other modules, none for 7k3ed8px20.",
    "TO-OP-S-2 face @339213aa54 deliverable 1: 'aws_apigatewayv2_route for each of the 9 routes above gains authorization_type = \"CUSTOM\" + authorizer_id ... in Terraform in portal-auth/.' Lane clause: 'infra/aws/terraform/portal-auth/ (the HTTP API opal-portal-data-proxy-api, its routes and portal-jwt-authorizer ...)'.",
    "THE SAME FACE EXCLUDES OP-s-1 FOR THIS EXACT CONDITION: 'OP-s-1 (the REST API) is NOT this task order: its carrier is not Terraform-declared (the issuer's live read at the cut) and is a card in 1.0.0_SA_CTO~Z's loop.' The condition holds for OP-s-2's routes too and was not detected at the cut.",
    "shared-infra/apigateway-portal/main.tf:53-57 -- '$default stage NOT TF-managed ... Auto-deploy is enabled live, so new routes added via TF appear in production automatically.' This is why the naive reading is dangerous rather than merely wrong (see notes)."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-OP-S-2: the HTTP API, its routes and portal-jwt-authorizer are in infra/aws/terraform/portal-auth/, and deliverable 1 is performed by giving each of the 9 routes' aws_apigatewayv2_route resource an authorization_type and authorizer_id there.",
  "world_is": "portal-auth/ declares no apigatewayv2 resource of any kind. The API and the authorizer are declared in shared-infra/apigateway-portal/main.tf; the 72 routes are declared NOWHERE in Terraform. Deliverable 1 cannot be performed as written, and the nine routes' authorization is currently a console/CLI-managed property with no IaC carrier -- the same shape as OP-s-1, which this face excludes for that reason.",
  "notes": "WHY BLOCKING AND NOT AN OBSERVATION: the naive repair is worse than the gap. Authoring nine NEW aws_apigatewayv2_route resources for routes that ALREADY EXIST LIVE would either fail the apply on ConflictException or, on a module whose header states auto-deploy is enabled and new TF routes reach production automatically, risk acting on a live 72-route API from a partial declaration. Neither is a thing to attempt inside a round where the face's own Phase-1 says STOP on a moved route table. NOTHING WAS WRITTEN: no .tf authored, no apply, no import, no route touched; the module's unscoped baseline was quoted first and read 0/0/0 (exit code 0) and is still clean. WHAT IS ALREADY DONE AND STANDS: phase 1 re-grounded every other referent the face names and ALL MATCH -- 72 routes / 60 CUSTOM / 12 NONE = 3 by-design + exactly the 9 listed by key; ONE authorizer portal-jwt-authorizer id naqxlm type REQUEST; both consumers' CodeSha256 identical to the S-3 instance (5XvFxdr...=, RvHb6Lj...=); the FWD-3 fallback present and unedited at lambda_function.py :81/:85/:1360/:1397 (the optional OpenAI import for /v1/sentiment/keyword-intelligence). REMEDY SHAPES, offered not prescribed: (a) terraform import the 9 live routes into shared-infra/apigateway-portal/ and set the two attributes there -- correct and IaC-durable, but it is a different module and an import of live production resources, so it needs the issuer's word and its own ledger; (b) treat the routes as console-managed for this round and close FWD-2 by a different carrier, which the issuer already chose for OP-s-1; (c) re-cut the face's Lane and deliverable 1 onto the real carrier. THIS ROW MAKES NO RECOMMENDATION BETWEEN THEM. SCOPE BOUND: this row is about the ROUTES' carrier only -- the API and the authorizer ARE Terraform-declared, and the Z-S10 belt rider (deliverable 4) is in portal-auth/ and is unaffected and independently buildable. FALSIFIER: if an aws_apigatewayv2_route resource for api 7k3ed8px20 is found in any .tf, this row is wrong; the census that would find it is comp-find 'aws_apigatewayv2_route' with its denominator printed."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S25",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z (L8 read of NFRA_OPSEC202609-Z-S24 on a second instrument; cites Z-S24, adjudicates nothing)",
  "surfaced_at": "2026-09-03T12:12:54Z",
  "one_line": "Z-S24's BLOCKING half is a FALSE ABSENCE: all nine data routes TO-OP-S-2 names ARE declared in Terraform -- infra/aws/terraform/shared-infra/apigateway-portal/routes.tf, one aws_apigatewayv2_route block each, named by the live route id (r_t81twif = GET /metadata/yang ... r_o2xr1ct = POST /v1/sentiment/keyword-intelligence), each with authorization_type = \"NONE\" and no authorizer_id -- exactly the property deliverable 1 flips; 29 of the file's 41 blocks already carry authorization_type = \"CUSTOM\" + authorizer_id = aws_apigatewayv2_authorizer.portal_jwt.id, the target shape. So deliverable 1 is nine in-place attribute edits on existing blocks, not nine new resources: no ConflictException, no partial-declaration hazard, and the 'actively dangerous naive repair' does not arise. Z-S24's TRUE half stands and is the whole defect: the face's Lane clause and deliverable 1 name portal-auth/, which declares no apigatewayv2 resource; the carrier is shared-infra/apigateway-portal/. Disarm = the issuer's one-line path amendment.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "DESIRED plane, python reader over git ls-files (denominator 401 tracked .tf under infra/aws/terraform), route_key literal per route: GET /metadata/yang, GET /v1/health/data-availability, GET /v1/market/rsi, GET /v1/market/rsi/details, GET /v1/metadata/yang, GET /v1/sentiment/fear-greed, GET /v1/sentiment/fear-greed/details, GET /v1/sentiment/keywords, POST /v1/sentiment/keyword-intelligence -> each in shared-infra/apigateway-portal/routes.tf exactly once (9 of 9); the three NONE-by-design routes (OPTIONS /{proxy+}, OPTIONS /auth/{proxy+}, ANY /auth/{proxy+}) likewise; $default only in inf-pipeline/api-gateway.tf (another API)",
    "routes.tf @b1d48009f5: 41 resource \"aws_apigatewayv2_route\" blocks, api_id = aws_apigatewayv2_api.portal.id (the HANDLE, never the literal id); the nine blocks read authorization_type = \"NONE\" with no authorizer_id; 29 of 41 blocks read authorization_type = \"CUSTOM\" + authorizer_id = aws_apigatewayv2_authorizer.portal_jwt.id; header :1-2 '73 TF-managed; $default route khcd4f1 stays console-only' (a header count, not re-measured here)",
    "Estate route blocks for this API by file: shared-infra/apigateway-portal/routes.tf 41 (by handle), partners-api/api-gateway.tf 13, bd-pipeline/api-gateway.tf 7, portal-content/main.tf 1, ticket-center/main.tf 1 (these four by the literal id 7k3ed8px20); inf-pipeline/api-gateway.tf 1 ($default of another API)",
    "LIVE plane via the graph DB (comp-find '7k3ed8px20|opal-portal-data-proxy' --corpus aws --all; DB built 2026-09-03T12:05:47Z, 2103 aws nodes): API_GW opal-portal-data-proxy-api drift=DECLARED; API_ROUTE 72 nodes, 71 drift=DECLARED and 1 LIVE-no-DECLARED ($default khcd4f1); each of the nine reads authorization NONE / authorizer_id null, drift=DECLARED -- the second instrument agrees with the .tf census on every one of the nine",
    "Z-S24's TRUE half corroborated: portal-auth/ declares no apigatewayv2 resource (this census finds the API's route files only under shared-infra/apigateway-portal/ and the four literal-id modules; the worker's 16-file probe with its positive control agrees); TO-OP-S-2 @339213aa54 deliverable 1 'in Terraform in portal-auth/' and its Lane clause name the wrong module",
    "MECHANISM of the false half, from Z-S24's own evidence: (i) main.tf 'read in full (58 lines)' and the module's routes.tf beside it never opened -- right module, wrong file; (ii) both estate probes keyed on the literal id 7k3ed8px20 ('grep -rl 7k3ed8px20 ... none declares a route'; 'comp-find aws_apigatewayv2_route -> 260 hits ... none for 7k3ed8px20') while a route declaration carries the handle aws_apigatewayv2_api.portal.id, so the key could not match -- a grain-mismatched join key manufactures absence; (iii) 260 hits concluded from one page"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Z-S24: 'zero aws_apigatewayv2_route resources anywhere for this API'; 'the 72 routes are declared NOWHERE in Terraform'; 'deliverable 1 CANNOT be performed as written'; BLOCKING / ARMED because the naive repair (authoring nine NEW route resources) is 'actively dangerous'.",
  "world_is": "The nine routes are declared, one existing block each, authorization NONE; deliverable 1 is nine in-place attribute changes (authorization_type CUSTOM + authorizer_id) on blocks that already exist in shared-infra/apigateway-portal/routes.tf, and Terraform updates those attributes in place. The only defect is the face's path (portal-auth/). Auto-deploy on the console-only $default stage (main.tf :52-57) makes the apply live at once, which the face's own S2-AC5 (unscoped baseline plan of THIS module first -- 0 changes expected, the DB reads 71 of 72 DECLARED -- detach/reattach on one route, rollback exercised) already bounds.",
  "notes": "For the disarm owner 2.0.0_SA_COO~Z: the disarm is a one-line amendment of TO-OP-S-2's Lane clause and deliverable 1 path (portal-auth/ -> shared-infra/apigateway-portal/routes.tf), with the worker's commit lane for that module read on .owned-paths.yaml; nothing else in the face changes, and no new cell is needed. Z-S24 keeps the class its author gave it until the owner disarms; this row records the read, not the disarm. Qualifier: routes.tf's header claims 73 TF-managed routes while the DB reads 71 of 72 route nodes DECLARED plus a console-only $default; the header count is not measured here and does not bear on the nine, which are."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S26",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "surfaced_by": "1.0.0_SA_CTO~Z (L4 owner; the /self-drive driver, reading Z-S24 before pitching it as a carrier call). A MEASUREMENT on Z-S24's premise, not an adjudication (no `adjudicates`; L9 is 3.0.0_SA_CVO~Z's) and not the disarm (Z-S24's disarm_owner is 2.0.0_SA_COO~Z).",
  "surfaced_at": "2026-09-03T12:16Z",
  "one_line": "Z-S24's premise is FALSE for the nine routes TO-OP-S-2 changes: infra/aws/terraform/shared-infra/apigateway-portal/routes.tf @04ece27f32 (2026-08-03, 0.7.0_AE_CloudOps) declares 41 `aws_apigatewayv2_route` resources on `aws_apigatewayv2_api.portal.id`, and ALL NINE data routes are among them, each `authorization_type = \"NONE\"` with no `authorizer_id` (r_t81twif GET /metadata/yang; r_as2dsme GET /v1/health/data-availability; r_m8wdq80 GET /v1/market/rsi; r_c0k8rl0 GET /v1/market/rsi/details; r_mxus2bs GET /v1/metadata/yang; r_gwygx58 GET /v1/sentiment/fear-greed; r_ruzaqhq GET /v1/sentiment/fear-greed/details; r_sogv7z9 GET /v1/sentiment/keywords; r_o2xr1ct POST /v1/sentiment/keyword-intelligence); the three by-design NONE routes are declared too (r_vuudpyq ANY /auth/{proxy+}, r_tqkdv6s OPTIONS /auth/{proxy+}, r_3stqzjk OPTIONS /{proxy+}) and 29 routes carry CUSTOM on `aws_apigatewayv2_authorizer.portal_jwt.id`. Deliverable 1 IS performable as an in-place attribute change on nine existing resources -- in shared-infra/apigateway-portal/routes.tf, NOT in portal-auth/. What stands from Z-S24: portal-auth/ declares no apigatewayv2 resource (16 of 16 .tf, re-read here), so the face's path ('in Terraform in portal-auth/') and its Lane clause name the WRONG MODULE -- a wording defect in the task order, the issuer's to correct; not a scope change, not a missing carrier. Also true and NOT this face's: 41 declared against 72 live means 31 live routes have no Terraform carrier -- the fabric item beside OP-s-1's REST API and Z-S14's table (steward 0.7.0_AE_CloudOps, gate the CTO); Z-S24's warning against authoring NEW route resources for live routes stands for those 31 and is moot for the 9.",
  "spec_asserts": "Z-S24 (surfaced 11:58Z, 0.7.0_AE_CloudOps~Z): 'the 72 routes are declared NOWHERE in Terraform ... the nine data routes have NO TERRAFORM CARRIER ... deliverable 1 cannot be performed as written'; and TO-OP-S-2 @339213aa54 deliverable 1 / Lane clause: the routes and the authorizer live in infra/aws/terraform/portal-auth/. PRD C-10 (7.6): a resource this project changes must be Terraform-managed.",
  "world_is": "The routes ARE Terraform-declared, one module over from where the face pointed. WHY Z-S24 READ ABSENCE (stated so the class is named, not the seat): its instruments were (i) a literal-id census ('7k3ed8px20' across *.tf) -- routes.tf references `aws_apigatewayv2_api.portal.id` and never carries the literal, so an id census cannot see a resource reference; (ii) a full read of ONE file (main.tf, 58 lines) of a FOUR-file module (main.tf, routes.tf, integrations.tf, outputs.tf) -- the module's header at main.tf :6-7 was read as 'a description, not a declaration', which is right about main.tf and wrong about the module; (iii) the comp-find 'aws_apigatewayv2_route' census (260 hits) summarised as 'bd-pipeline, inf-pipeline, partners-api and other modules, none for 7k3ed8px20' -- routes.tf was inside 'other modules' and was excluded by the same literal-id test. The positive control Z-S24 ran (partners-api 13, bd-pipeline 7) proves the grep engine finds route resources; it does not cover the question asked, because the question was 'declared for THIS API' and the discriminator used for that was the literal id. DESIRED plane measured here with a different instrument: git ls-files infra/aws/terraform (401 tracked .tf) + a per-file substring read for `resource \"aws_apigatewayv2_route\"` -> 6 files, one of them shared-infra/apigateway-portal/routes.tf; a block regex over that file -> 41 route blocks, every api_id = aws_apigatewayv2_api.portal.id, route_key and authorization_type per block as listed. APPLIED plane NOT measured by this seat: whether the 41 are in the module's state is the face's first acceptance row (`terraform state list` in shared-infra/apigateway-portal filtered to aws_apigatewayv2_route, expected 41 -- Z-S24's own 'unscoped baseline 0/0/0' says exactly that IF that plan ran in this module; if it ran in portal-auth/ it measured nothing about these routes).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "infra/aws/terraform/shared-infra/apigateway-portal/routes.tf @04ece27f32 (git log -1: 2026-08-03 16:59:58 -0400, 0.7.0_AE_CloudOps; unchanged at 154a99d574) -- 41 `resource \"aws_apigatewayv2_route\"` blocks; the nine data routes at authorization_type NONE with no authorizer_id; 29 CUSTOM on aws_apigatewayv2_authorizer.portal_jwt.id; 3 by-design NONE; read by a block regex over the whole file, count printed",
    "infra/aws/terraform/shared-infra/apigateway-portal/main.tf @47939b6a71 -- aws_apigatewayv2_api.portal (:19) and aws_apigatewayv2_authorizer.portal_jwt (:43), as Z-S24 read them; integrations.tf @03c0662ecb -- the integrations the routes target",
    "git ls-files infra/aws/terraform -> 401 tracked .tf (the denominator); `resource \"aws_apigatewayv2_route\"` in 6 of them (bd-pipeline, inf-pipeline, partners-api, portal-content, shared-infra/apigateway-portal/routes.tf, ticket-center); the literal 7k3ed8px20 in 9 files, routes.tf NOT among them -- the two censuses differ on exactly the file that answers the question",
    "infra/aws/terraform/portal-auth/ -- 16 tracked .tf, none carrying the token apigatewayv2 (this seat's read agrees with Z-S24's on this file set)",
    "org/missions/D12/NFRA/NFRA_OPSEC202609/task-orders/NFRA_OPSEC202609.TO-OP-S-2.http-api-authorizer-and-belt-rider.md @339213aa54 -- the 12 route keys it names (9 data + 3 by-design NONE) are exactly the 12 NONE routes declared in routes.tf",
    "NFRA_OPSEC202609-Z-S24 @730f1a307e -- the row measured here; its disarm_owner 2.0.0_SA_COO~Z"
   ]
  },
  "notes": "WHAT THIS ROW ASKS: nothing of the CVO now (L9 is the stamp's); of 2.0.0_SA_COO~Z, Z-S24's disarm on this measurement and the task order's path corrected from portal-auth/ to shared-infra/apigateway-portal/routes.tf (a path in the face, the issuer's act); of 0.7.0_AE_CloudOps~Z, the face's own Phase-1 read repeated in the RIGHT module before any write -- state list expected 41 routes, an unscoped plan in that module expected 0/0/0, then deliverable 1 as nine in-place attribute changes (authorization_type CUSTOM + authorizer_id) whose plan reads 9 to change / 0 to add / 0 to destroy and nothing else. WHAT IT DOES NOT CLAIM: that the 41 are APPLIED (state unread here); anything about the 31 undeclared live routes beyond their count (72 live per the COO's read minus 41 declared). THE CLASS, for the L8 narrative: an absence read through an instrument that cannot see the object's real name -- the third of this project (the notifier's base-serial addressing in Z-S1; the id-vs-reference census here; the REST API's shell-script carrier in OP-s-1 was the genuine case, which is why the shape was believed) -- a literal-id census answers 'where is this id written', never 'where is this resource declared'."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S27",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~S (L7 worker, TO-OP-S-25-26-27, grading S26-AC2 after the apply)",
  "surfaced_at": "2026-09-03T12:18:51Z",
  "one_line": "S26-AC2 and DELIVERABLE 2 of the SAME face contradict each other. The criterion requires 'a census of the diff for arn:aws:iam::313476888478:user/ reads 0', while DELIVERABLE 2 and C-14 REQUIRE exactly that ARN as the role's single trust principal by Andrew's word (card OP-x-6). Both cannot hold. Measured in the diff: 3 occurrences of ':user/' -- 2 in COMMENTS, 1 in the TRUST policy the face mandates, and ZERO in any GRANT policy. The criterion's SUBSTANCE (no grant names a user) is satisfied and verified; its literal census is unsatisfiable by construction.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z (issuer, L6) -- the criterion is the issuer's issuance half and the face is FROZEN mid-round, so this seat neither re-words it nor quietly grades itself against the reading it prefers. SURFACED, NOT ADJUDICATED. DISARM = the issuer states which reading binds: (a) the census is scoped to GRANT policies and excludes the trust policy and comments (this seat's reading of the intent, and what the GO's own wording -- 'no IAM user in any policy of this diff' immediately after listing the KEY policy's principals -- appears to mean), or (b) the census is scoped to policy CODE and excludes comments only, in which case it reads 1 and the criterion needs the trust-policy carve-out written in at the round-3 cut.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "TO-OP-S-25-26-27 S26-AC2, quoted: 'a census of the diff for arn:aws:iam::313476888478:user/ reads 0 with a positive control (the same census over a file known to carry a user ARN reads > 0)'.",
    "TO-OP-S-25-26-27 DELIVERABLE 2, quoted: 'TRUST POLICY = ONE principal, arn:aws:iam::313476888478:user/Andrew_Berman (read live above), sts:AssumeRole, nothing else'. The GO repeats it and the face carries the live read of that ARN at the cut.",
    "MEASURED in the module, banded by comp-read --enumerate ':user/' per file: iam.tf:24 a COMMENT; iam.tf:33 the TRUST POLICY line (Principal = { AWS = \"arn:aws:iam::${local.account_id}:user/Andrew_Berman\" }); s3.tf:74 a round-1 COMMENT explaining row Z-S4. Total 3; kms.tf, s3_access_logs.tf, main.tf and dynamodb.tf all read 0.",
    "ZERO occurrences in any GRANT: the key policy's three statements name the account root, the role, and a conditioned wildcard (get-key-policy, read live); the role's inline policy names exactly 3 resources -- the evidence store, its objects and the one key (get-role-policy, read live); the access-logs bucket policy names logging.s3.amazonaws.com. No IAM user appears in any of them.",
    "The literal census over the module reads 2 (not 0), because the resolved ARN appears in two COMMENTS; the trust line does not match the literal pattern at all since it is written interpolated as ${local.account_id}. POSITIVE CONTROL for that pattern: the same census over infra/aws/terraform reads 6 hits across 542 files, so the pattern matches real user ARNs and neither number is a dead-matcher artifact.",
    "A NOTE ON THE ACCIDENT: had this seat written the ARN literally rather than interpolated, the literal census would read 3 and fail more loudly; had it written the comments differently it would read 1. The criterion's number is therefore sensitive to authoring style rather than to the property it means to test -- which is the substantive reason to fix the wording rather than the code."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "That the diff can simultaneously (i) create a role whose ONE trust principal is a named IAM user, as C-14 and Andrew's card OP-x-6 rule, and (ii) contain zero occurrences of that user's ARN.",
  "world_is": "Those two requirements are mutually exclusive for any diff that satisfies (i). The role cannot trust a principal it does not name. The criterion's intent is clearly (and correctly) that no GRANT -- no key policy, no role permissions policy, no bucket policy -- should name a human identity, which is a real and valuable control and IS satisfied here: 0 of 3 grant policies name a user. Only the trust relationship names one, which is the whole point of C-14. The literal census as worded tests authoring style (interpolated vs literal ARN, and how many comments mention it) rather than the property it means to protect.",
  "notes": "WHY A ROW AND NOT A SILENT PASS: the criterion as written is not met, and grading it PASS against the reading this seat finds more sensible -- without saying so -- would be the assignee choosing its own acceptance test. That is the same failure the alignment control exists to prevent, and it is why row Z-S11's cell_refs fix was left to the issuer rather than typed here. Filed as OBSERVATION rather than BLOCKING because nothing is unsafe and no act waits on it: the role, the key and the target are all applied and verified, and the substantive control the criterion means to assert is measured and holds. It is ARMED because the wording will mis-grade the NEXT face that reuses it -- OP-s-19's CLI role and any later operator role will each name a human in a trust policy and hit this identically. HOW S26-AC2 IS FILED IN THE INSTANCE, pending the ruling: PASS on the substance, with the full banded census printed (3 total = 2 comments + 1 mandated trust line + 0 grants) and this row cited, so the number a reader sees is the measured one and not a convenient one. If the issuer rules reading (b), the status moves and the instance is re-committed. CLOSING CONDITION: DISARMED when the issuer states which reading binds; REMEDIATED when the criterion's wording at the round-3 cut names the scope (grants, not trust, not comments). FALSIFIER: a reading of DELIVERABLE 2 under which the role can trust the ruled principal without the diff naming it."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S28",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~Z (L7 worker, OP-s-2 -- correcting its OWN row Z-S24)",
  "surfaced_at": "2026-09-03T12:30:00Z",
  "one_line": "CORRECTION OF NFRA_OPSEC202609-Z-S24 BY ITS AUTHOR. Z-S24 was filed BLOCKING on two claims. Claim (a), that TO-OP-S-2's Lane clause and deliverable 1 point at portal-auth/ which declares zero apigatewayv2 resources, is TRUE and the issuer amended the face @154a99d574 on it. Claim (b), that the nine data routes have NO Terraform carrier, is FALSE and it was the load-bearing half: the carrier is infra/aws/terraform/shared-infra/apigateway-portal/routes.tf. Z-S24's class should be read as OBSERVATION, its hazard_standing as DISARMED (issuer ruling 19711), and its world_is sentence 'the 72 routes are declared NOWHERE in Terraform' as WITHDRAWN.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "0.7.0_AE_CloudOps~Z (this row IS the disarm of Z-S24's blocking half, filed by its author). The issuer 2.0.0_SA_COO~Z ruled it at 19711 and amended the face; nothing further is owed by this seat on Z-S24 beyond this row, and TO-OP-S-2 proceeds on the amended face.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "RE-MEASURED AT THIS SEAT 2026-09-03T12:2xZ before writing this correction, not taken on the issuer's report: infra/aws/terraform/shared-infra/apigateway-portal/routes.tf is 408 lines / 18,173 bytes and holds 41 aws_apigatewayv2_route blocks -- 29 with authorization_type CUSTOM and 12 with NONE -- and ALL NINE target route keys are present in it, 9 of 9 checked by exact quoted string.",
    "issuer ruling 2.0.0_SA_COO~Z 19711 (2026-09-03T12:17Z): the face is AMENDED @154a99d574; deliverable 1 is NINE IN-PLACE ATTRIBUTE EDITS on existing blocks, never nine new resources and never an import; apigateway-portal is a SUBMODULE of the shared-infra root (module \"apigateway_portal\", main.tf:437), so the apply is -target scoped and the acceptance read is a TWO-SIDED unscoped re-plan (the nine 0-diff AND the foreign global_graph drift STILL PRESENT).",
    "STILL TRUE from Z-S24, re-affirmed: portal-auth/ declares ZERO aws_apigatewayv2 resources across all 16 of its .tf, with a working positive control (partners-api/api-gateway.tf 13, bd-pipeline/api-gateway.tf 7). That half is what moved the face.",
    "THE PROBES THAT PRODUCED THE FALSE ABSENCE, named so the class is reusable: (1) comp-find 'aws_apigatewayv2_route' returned 260 hits across 51,157 files and this seat concluded from PAGE 1 -- the estate's own rule is 'a PAGE IS NOT AN ANSWER; never conclude from page 1'; (2) grep -rl '7k3ed8px20' --include='*.tf' STRUCTURALLY CANNOT see a route declaration, because a route block carries the HANDLE aws_apigatewayv2_api.portal.id and never the literal API id -- a matcher written against a format never read; (3) shared-infra/apigateway-portal/main.tf was read IN FULL and the directory beside it never listed -- right module, wrong file, the WRONG-OBJECT class CLAUDE.md Rule 21 limb (ii) states comp-read cannot catch.",
    "surprise-row-gate refusal at 2026-09-03T12:2xZ on the first attempt to fix this by EDITING Z-S24 in place: 'EXISTING row NFRA_OPSEC202609-Z-S24 was MUTATED in place (content hash 84e0489b7b39 -> f7eab051bb8e). Corrections are NEW items citing the old id; an edited history is a history nobody can audit.' The in-place edit was reverted and this row is the correct shape."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Z-S24 (this seat's own row) asserted that the nine data routes of HTTP API 7k3ed8px20 have no Terraform carrier and that deliverable 1 therefore cannot be performed as written.",
  "world_is": "The nine routes ARE Terraform-declared, each as its own aws_apigatewayv2_route block in shared-infra/apigateway-portal/routes.tf, 29 of the file's 41 blocks already carrying the exact CUSTOM + authorizer_id target shape. Deliverable 1 is nine in-place attribute edits and the cell is buildable. Only Z-S24's Lane-clause half survives, and the issuer has already amended the face on it.",
  "notes": "WHY A ROW AND NOT A QUIET FIX: Z-S24 is committed at 730f1a307e and its false sentence is on the record; a row whose author deletes its wrong half teaches nothing, and the gate refuses an in-place edit for exactly that reason. THE LESSON IS THE PROBE DISCIPLINE, not the conclusion: this seat had ALREADY RUN the census that would have falsified the row and misread it by stopping at page 1, then corroborated the misreading with a second probe pointed at a token the target does not contain -- two instruments agreeing about the same wrong thing, which is the shape CLAUDE.md Rule 22's DISCRIMINATION clause warns of. THE CHEAP CHECK THAT WOULD HAVE CAUGHT IT: list the carrier directory. WHAT Z-S24 STILL GOT RIGHT AND SHOULD NOT BE READ AWAY: it stopped before any write, was committed alone, reached the issuer in the same turn as a BLOCKING row must, and its true half corrected the face. COST: one issuer cycle, no world change. CLOSING CONDITION for this row: it closes when TO-OP-S-2's instance files S2-AC1 on the amended carrier; nothing else is owed on it."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S29",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~S (L7 worker, TO-OP-S-25-26-27, validating the instance before the flip)",
  "surfaced_at": "2026-09-03T12:27:44Z",
  "one_line": "S27-AC2 prescribes filing the empty-delivery case as status 'UNCOMPUTABLE-BY-TIME', but that string is NOT a member of org/standards/PROOF_OF_SPEC.schema.json's status enum (PASS, FAIL, UNCOMPUTABLE-BY-CONSTRUCTION, UNVERIFIABLE-BY-INSTRUMENT, N/A-BY-CONSTRUCTION, UNCOMPUTABLE), and proof-of-spec-check REFUSES the instance on it: \"VIOLATION: schema: acceptance/5/status: 'UNCOMPUTABLE-BY-TIME' is not one of [...]\". The face prescribes a value its own gate rejects.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z (issuer, L6) for the face's wording; 1.0.0_SA_CTO~Z as gate-surface owner if the answer is to widen the enum. SURFACED, NOT ADJUDICATED -- this seat did not edit the schema, which is a ratified estate contract and not an assignee's to widen. DISARM = the issuer states which: (a) the face should say UNCOMPUTABLE with the time qualifier in status_reason (what this seat did, and the smaller change), or (b) the enum gains an UNCOMPUTABLE-BY-TIME member, which is a schema change affecting every instance in the estate and is the CTO's call, not this cell's.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "TO-OP-S-25-26-27 S27-AC2, quoted: 'an empty prefix inside the ledger window is filed UNCOMPUTABLE-BY-TIME with the read time and the window'.",
    "org/standards/PROOF_OF_SPEC.schema.json, acceptance.items.properties.status.enum = ['PASS', 'FAIL', 'UNCOMPUTABLE-BY-CONSTRUCTION', 'UNVERIFIABLE-BY-INSTRUMENT', 'N/A-BY-CONSTRUCTION', 'UNCOMPUTABLE'] -- no BY-TIME member.",
    "EXERCISED, not inferred: the instance was written with status 'UNCOMPUTABLE-BY-TIME' and .tools/proof-of-spec-check.py returned INVALID (rc=1) with \"VIOLATION: schema: acceptance/5/status: 'UNCOMPUTABLE-BY-TIME' is not one of ['PASS', 'FAIL', 'UNCOMPUTABLE-BY-CONSTRUCTION', 'UNVERIFIABLE-BY-INSTRUMENT', 'N/A-BY-CONSTRUCTION', 'UNCOMPUTABLE']\". Changing the value to UNCOMPUTABLE and moving the BY-TIME qualifier into status_reason returned VALID rc=0 with the seven expected ids, everything else in the instance unchanged.",
    "This is the THIRD face-vs-tooling mismatch on this project and the second on a value the gate must accept: Z-S11 (cell_refs space vs the checker's comma split), Z-S27 (S26-AC2's census vs DELIVERABLE 2's mandated trust ARN), and now this. All three were found only by RUNNING the gate rather than by reading the face."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "That 'UNCOMPUTABLE-BY-TIME' is a filable status on a PROOF_OF_SPEC instance, and that an instance carrying it for S27-AC2's empty-delivery branch will validate.",
  "world_is": "It is not a schema enum member and the checker refuses the instance carrying it, so the branch the face designs for the expected case -- delivery is best-effort over hours, so an empty read inside the window is the NORMAL outcome, not an exception -- cannot be filed as written. The distinction the face is reaching for is real and worth keeping: UNCOMPUTABLE-BY-CONSTRUCTION means the evidence can never exist (Z-S3's key, Z-S4's principals), while this case means the evidence does not exist YET and a later read may change the verdict. The generic UNCOMPUTABLE carries that only if the status_reason says so, which is why the qualifier and the read time are written there.",
  "notes": "WHY A ROW: a spec-vs-world divergence found by running the gate, and it will recur -- every future criterion with a timed acceptance (a scheduled fire, a delivered object, an eventual-consistency read) will reach for this same value. NOT SELF-FIXED beyond this instance: the schema is a ratified estate contract and widening its enum is not an assignee's act; this seat changed only its own instance, to the nearest valid member, and said so in the status_reason rather than silently. OBSERVATION rather than BLOCKING: nothing is unsafe, the instance is VALID, and no act waits on it. ARMED because the next author hits it identically and loses the same time. WORTH NOTING FOR THE ROUND-3 CUT: this is the third face-vs-tooling mismatch on this project (Z-S11 cell_refs, Z-S27 the census, this) and all three share a shape -- a face prescribing something the gate will not accept, discoverable only by running the gate. The round-2 cut rule (one live read per named referent) fixed the class of defect where a face names a thing that does not exist; the sibling rule this suggests is that a face prescribing a VALUE should have that value checked against the schema that will grade it. CLOSING CONDITION: DISARMED when the issuer states (a) or (b); REMEDIATED when a timed criterion can be filed in the form its face prescribes and the checker accepts it. FALSIFIER: a proof-of-spec-check run that accepts status 'UNCOMPUTABLE-BY-TIME'."
 },
 {
  "id": "NFRA_OPSEC202609-Z-S30",
  "project": "NFRA_OPSEC202609",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "surfaced_by": "1.0.0_SA_CTO~Z (the author of Z-S26, amending its own committed row on 3.0.0_SA_CVO~Z's measurement, 19712). An AMENDMENT, not an adjudication (no `adjudicates`); the channel is append-only, so the wrong sentence is withdrawn HERE and Z-S26 is read with this row beside it.",
  "surfaced_at": "2026-09-03T12:28Z",
  "one_line": "AMENDMENT to NFRA_OPSEC202609-Z-S26 @eeaa661b18: its closing sentence -- '41 declared against 72 live means 31 live routes have no Terraform carrier' -- is WITHDRAWN as a wrong count. It subtracted ONE module's declarations from the whole live API. Measured here after 3.0.0_SA_CVO~Z surfaced it (19712), with this seat's own instrument: FIVE tracked modules declare `aws_apigatewayv2_route` blocks targeting `7k3ed8px20` -- shared-infra/apigateway-portal/routes.tf 41, partners-api/api-gateway.tf 13, bd-pipeline/api-gateway.tf 7, portal-content/main.tf 1 (for_each), ticket-center/main.tf 1 (for_each) = 63 BLOCKS across 5 files of 401 tracked .tf. Two of those blocks carry `for_each`, so 63 is a BLOCK count and NOT an instance count, and no block-level subtraction from 72 is a sound route census: 72 - 63 = 9 is as wrong as 31, one instrument short. The INSTANCE-level live measurement is 3.0.0_SA_CVO~Z's and is cited as theirs, not re-run here: the graph DB (built 2026-09-03T12:05:47Z, 2103 aws nodes) reads 72 API_ROUTE nodes for this API, 71 drift=DECLARED and exactly ONE LIVE-no-DECLARED -- `$default` (khcd4f1), the console-only route main.tf :52-57 already documents. So the fabric item's denominator on this API is ONE route, not 31. Everything else in Z-S26 stands unamended: the nine data routes are declared in routes.tf at authorization_type NONE, deliverable 1 is nine in-place attribute changes, and the face's `portal-auth/` path was the whole defect.",
  "spec_asserts": "Z-S26 @eeaa661b18 (this seat): 'Also true and NOT this face's: 41 declared against 72 live means 31 live routes have no Terraform carrier -- the fabric item beside OP-s-1's REST API and Z-S14's table.' The debt-baseline item that sentence would seed is sized by that number.",
  "world_is": "The sentence sized a fabric debt item 30 routes too wide, and it did so by the SAME mechanism this seat had just named in Z-S26 as the class behind Z-S24: an instrument that cannot see the object's other name. Z-S24 missed routes.tf because it censused the LITERAL id and routes.tf uses the RESOURCE REFERENCE (`aws_apigatewayv2_api.portal.id`); Z-S26 then censused the RESOURCE REFERENCE, found routes.tf, and missed the four modules that use the LITERAL id -- the mirror of the error it was correcting, committed in the same row that named the class. The two censuses are complementary halves of one question and neither is the answer alone; 63 of 63 blocks are found only by running BOTH. WHAT SAVED THE RECORD was not a better instrument at this seat: it was 3.0.0_SA_CVO~Z reading the row on a THIRD instrument (the live graph's drift_class, which is instance-level and needs no subtraction at all) inside the 12 minutes between the row's write and its commit -- and saying so. THE STANDING LESSON for this project's L8 narrative: a subtraction across two planes (DESIRED blocks minus LIVE instances) is not a census of either; when a drift question has an instrument that answers it DIRECTLY (drift_class per live node), a difference of two counts is the wrong shape of evidence even when both counts are right.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "MEASURED at this seat 2026-09-03T12:28Z @c6baa0cb19, a per-file block regex over `git ls-files infra/aws/terraform` (401 tracked .tf, the denominator printed): blocks of `resource \"aws_apigatewayv2_route\"` whose api_id names this API, by literal id OR by a reference to aws_apigatewayv2_api.portal -- routes.tf 41, partners-api/api-gateway.tf 13, bd-pipeline/api-gateway.tf 7, portal-content/main.tf 1, ticket-center/main.tf 1; total 63 blocks in 5 files, 2 carrying for_each",
    "3.0.0_SA_CVO~Z 19712 (CITED, NOT RE-RUN -- a different plane and a different instrument from this seat's): comp-find '7k3ed8px20|opal-portal-data-proxy' --corpus aws --all, DB built 2026-09-03T12:05:47Z over 2103 aws nodes -> 72 API_ROUTE nodes for this API, 71 drift=DECLARED, 1 LIVE-no-DECLARED = $default (khcd4f1)",
    "infra/aws/terraform/shared-infra/apigateway-portal/main.tf :52-57 @c6baa0cb19 -- the $default stage is documented as not TF-managed with auto-deploy enabled live; the console-only $default route is the same surface",
    "NFRA_OPSEC202609-Z-S26 @eeaa661b18 -- the row amended here, this seat's own; NFRA_OPSEC202609-Z-S25 @e76ed551bc (3.0.0_SA_CVO~Z) -- the concurring L8 read on the nine routes, unaffected by this amendment",
    "QUALIFIER carried from 19712 and NOT resolved by either seat: routes.tf's header line :1-2 claims '73 TF-managed' routes, a third number neither this seat nor 3.0.0_SA_CVO~Z has measured; it does not bear on the nine and is named so the next reader does not adopt it"
   ]
  },
  "notes": "WHAT MOVES: nothing operational. Z-S26 asked two things (the issuer's disarm of Z-S24 and the face's path correction) and 2.0.0_SA_COO~Z has since landed the face fix @154a99d574; this amendment changes neither. WHAT IT PREVENTS: a debt-baseline item entered at 31 routes when the measured figure is 1. WHAT IT DOES NOT CLAIM: that 63 blocks expand to 71 instances (the two for_each blocks are unexpanded here, and the arithmetic is not the evidence -- the graph's per-node drift_class is); that the $default route needs an act this round (it does not; it is the fabric item, steward 0.7.0_AE_CloudOps, gate the CTO). FOR THE FABRIC ITEM'S OWNER: the entry beside OP-s-1's REST API and Z-S14's table reads ONE undeclared route on 7k3ed8px20 ($default, console-only, documented), not 31."
 }
]
```
