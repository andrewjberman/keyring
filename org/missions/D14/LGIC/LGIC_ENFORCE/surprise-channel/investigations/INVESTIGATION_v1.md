# LGIC_ENFORCE -- surprise channel, INVESTIGATION v1

**Opened by:** `2.0.0_SA_COO~G`, 2026-09-14, in LGIC_ENFORCE's L6 issuance commit, so that the round's workers have a channel to
append to. **Home:** the project tree's channel. Lane `ANY`; the gate `.tools/surprise-row-gate.py` validates every NEW row
(schema, identity, coordinate, folder == project). **Append-only.** A worker's row id is `LGIC_ENFORCE-W<n>-S<k>`, where `<n>` is
its slot; a seat's is `LGIC_ENFORCE-S<k>`.

**Denominator at this write: 1 row, LGIC_ENFORCE-S1, which mints the channel.**

```json
[
  {
    "id": "LGIC_ENFORCE-S1",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-14T19:40Z",
    "one_line": "The L6 coverage limb of the TO issuance gate reads every cell id a decomposition CITES as one of its own cells, so a decomposition that cites another project's cells cannot be covered by its own orders; and the audited override its refusal text offers is never read by that limb.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "REFUSAL, exercised: this project's first L6 attempt (no commit was made) printed 'the issuance under org/missions/D14/LGIC/LGIC_ENFORCE/project.json owns 22 of 26 cell(s) ... MISSING: LN-f-1, LN-g-1, LN-h-3, LN-l-1'. All four are LGIC_NAMING cells that decomposition v1 @8d1d4d3e2f CITES, at :76, :89, :157, :159, :209, :305, :390 and :468 (10 citations).",
        "CODE, read: .tools/to-pipeline-gate.py@a369a0f55d _coverage_gap (:414-419) takes set(CELL_ID_RE.findall(decomp_text)) over the whole document, with no project scoping; CELL_ID_RE (:262-267) accepts any [A-Z][A-Z0-9]*- prefix.",
        "CODE, read and NOT exercised: the refusal (:473-476) offers 'take the audited # pipeline-override: on one order with the reason'. OVERRIDE_RE is read only in check_file (:2365-2386), which returns early with no violations for that ONE order. The coverage limb (:422-479, called at :2728-2731) never reads it. So by source, the named route leaves the refusal standing AND exempts that order from every per-file limb.",
        "DISCRIMINATOR, exercised: decomposition v1.1 @53d221f334 changed only the ten citations, to 'LGIC_NAMING cell <x-n>'. The gate's own _coverage_gap then read 22 ids with none missing, and the next issuance attempt's gate printed 'issuance coverage 22 of 22 cell(s)'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spine v3.0 L6 carrier 1, as the gate's docstring states it (:448-452): 'the union of <owned_cells> across the staged NEW orders must equal the named decomposition's cell set'. The refusal text: 'cut the missing order(s) in this same commit, or take the audited # pipeline-override: on one order with the reason'.",
    "world_is": "The gate's 'cell set' is every cell-id token anywhere in the decomposition, including cells of other projects cited as inputs or gates. And the one alternative the refusal names is not read by the limb that refused.",
    "notes": "Worked around in this project by decomposition v1.1: the citation form only, and no cell, edge, gate or criterion moved. The remedy is the gate owner's (1.0.0_SA_CTO): scope the id set to the project's own prefix or to the decomposition's cell table, and either honour the override in the coverage limb or drop it from the refusal text. INERT: the refusal fails closed, and no order was cut on the wrong set. The cost falls on the next seat whose decomposition cites another project's cells, and the refusal's own text sends that seat to the route that does not work."
  },
  {
    "id": "LGIC_ENFORCE-W2-S1",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~2",
    "surfaced_at": "2026-09-14T20:20Z",
    "one_line": "comp-iam role <name>, the instrument TO-EN-c-2 names for the grant half, resolved 0 of the 94 roles the grants and belts name, although its own comp-iam roles listing carries 79 of them; a CamelCase control resolves.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED: 94 calls of 'timeout 120 comp-iam role <name>' in worktree wk-lgic-enforce-1-2 @fd9c9ca174, 2026-09-14 after 20:01Z: 94 of 94 printed \"No role matching '<name>'\" (for example bd-exporter-ec2-role, opal-portal-lambda-role). Output kept in the worker's .scratch/c2/compiam_role_out.txt, not committed.",
        "EXERCISED: 'comp-iam roles' at the same HEAD prints 'IAM ROLES (209 found)'; 79 of the 94 names appear in it with a source: line (bd-exporter-ec2-role: tf_resource bd_exporter).",
        "CONTROL: 'comp-iam role FredMacroIngestionLambdaRole' prints 'ROLE: FredMacroIngestionLambdaRole', source infra/aws/terraform/fred-pipeline/iam.tf, statements: 3. 'comp-iam role fred_macro_ingestion' and 'comp-iam role bd_exporter' print No role matching.",
        "SUBSTITUTE, a different plane: aws iam get-account-authorization-details (read-only): 250 roles, 7 users, 1 group, 56 managed policies; list-roles 250 and list-users 7 agree; 48 of 48 attached managed policy ARNs resolve in the dump."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-c-2 WORKER FACE, GRANTED: 'For each, give the grant line (policy name and statement, or .tf file and line). Use comp-iam role <name> per principal and the Terraform in infra/aws/terraform/.' Decomposition v1.1 s.6 (:411-412): 'EN-c-2 uses comp-iam role <name> per principal for the grant half of its census.'",
    "world_is": "comp-iam role returns No role matching for every hyphenated role name tried, 94 of 94, including 79 that comp-iam roles itself lists. So FENCE_WRITER_CENSUS.md takes each grant line from the live authorization dump (policy name, statement index and Sid), takes each role's .tf file from the comp-iam roles listing's source: line, and records the comp-iam role result per role in a comp_iam field.",
    "notes": "The census does not depend on comp-iam role: the live dump is a wider plane (250 live roles against comp-iam's 209 Terraform roles). The cause inside comp-iam was not investigated (the worker bound: nothing deeper). A seat that reads comp-iam role's No role matching as 'not declared in Terraform' is misled; recorded here, not fixed."
  },
  {
    "id": "LGIC_ENFORCE-W2-S2",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~2",
    "surfaced_at": "2026-09-14T20:20Z",
    "one_line": "bd-gold-layer-runner, which the PRD names as a known legacy principal of opal-data-49financial, is not an IAM principal: it is a stopped EC2 instance whose instance profile carries bd-exporter-ec2-role.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "LIVE READ: aws iam list-roles (250) and list-users (7), 2026-09-14 ~20:00Z: no role or user is named bd-gold-layer-runner. Roles with gold-layer in the name: bd-gold-layer-lambda-role, cot-gold-layer-ec2-role, inf-gold-layer-ec2-role, inf-gold-layer-lambda-role.",
        "LIVE READ: aws ec2 describe-instances --filters Name=tag:Name,Values=bd-gold-layer-runner -> i-01003b035d2988dfb, State stopped, IamInstanceProfile arn:aws:iam::313476888478:instance-profile/bd-exporter-profile.",
        "LIVE READ: aws iam get-instance-profile --instance-profile-name bd-exporter-profile -> Roles [bd-exporter-ec2-role].",
        "FILE: infra/aws/terraform/shared-infra/s3-49financial.tf:74-76 @fd9c9ca174: 'the ratified P2D-4 invocation contract executes the gold chain on bd-gold-layer-runner under bd-exporter-profile -- a bd-tree principal that MUST read silver inputs' outputs into gold here.'",
        "CENSUS: bd-exporter-ec2-role is granted on opal-data-49financial by a literal identity grant and is seen reading it 206 times in the window (FENCE_WRITER_CENSUS.md)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LGIC_ENFORCE_PRD.md v1.1 @78128f29ea :206-207, condition (ii): 'One is known already: the template's own comment names bd-gold-layer-runner. It is a legacy principal carrying the refused token bd, and it must read silver outputs into gold.'",
    "world_is": "bd-gold-layer-runner is the Name tag of EC2 instance i-01003b035d2988dfb (stopped). The IAM principal it runs as is bd-exporter-ec2-role, through instance profile bd-exporter-profile. The census carries bd-exporter-ec2-role, and no row carries bd-gold-layer-runner as a principal.",
    "notes": "An exemption or pattern keyed on the host name would match no principal ARN. Form only; which name the fence uses is EN-f-1's."
  },
  {
    "id": "LGIC_ENFORCE-W2-S3",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~2",
    "surfaced_at": "2026-09-14T20:20Z",
    "one_line": "The served-key write trail logs platinum/firm/ writes on opal-data-bd, -inf and -cot only, so for opal-data-49financial no write is observed at all, not only writes outside platinum/firm/.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "LIVE READ: aws cloudtrail get-event-selectors --trail-name opal-served-key-write-trail, 2026-09-14 ~19:55Z: resources.ARN StartsWith arn:aws:s3:::opal-data-inf/platinum/firm/, arn:aws:s3:::opal-data-bd/platinum/firm/, arn:aws:s3:::opal-data-cot/platinum/firm/; readOnly false. No opal-data-49financial prefix.",
        "FILE: infra/aws/terraform/globgrph/item2e_served_write_trail.tf:30 @fd9c9ca174: served_write_trail_buckets = [\"opal-data-inf\", \"opal-data-bd\", \"opal-data-cot\"].",
        "LIVE READ: aws cloudtrail get-trail-status --name opal-served-key-write-trail: IsLogging true, StartLoggingTime 1783522018 (2026-07-08T14:46:58Z). The file's header, item2e_served_write_trail.tf:4, reads '*** PROPOSED -- NOT YET APPLIED ***'.",
        "CENSUS: the trail's 2026/09/14 us-east-1 log files (112 files, 2333 records) hold 2333 WriteOnly events on platinum/firm/ in the window: bd 1 writer, inf 1, cot 1, 49financial 0."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-c-2 WORKER FACE: 'The limit you must state: the org trail logs these buckets' data events ReadOnly (cloudtrail-organization-trail.tf:73), so writes outside platinum/firm/ are NOT observed.' SEEN: 'every principal item2e_served_write_trail.tf's WriteOnly events show WRITING platinum/firm/.'",
    "world_is": "For opal-data-49financial, writes INSIDE platinum/firm/ are not observed either, because the served trail does not select that bucket. Its seen-writer count of 0 is 0 by construction, not by measurement. The census's unobserved_writes sentence states this for opal-data-49financial.",
    "notes": "The decomposition already says the served trail covers 'three served buckets' (:88-90), and Andrew's ruling 6 (decomposition :93, gate G-W) names write logging on opal-data-bd, -inf and -cot, not -49financial. The trail and its stale header are outside this order's paths; left as found."
  },
  {
    "id": "LGIC_ENFORCE-W2-S4",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~2",
    "surfaced_at": "2026-09-14T20:20Z",
    "one_line": "The order puts the role-side belts in GRANTED, but a belt is an explicit Deny; the 125 principal-bucket pairs that carry only a belt, and opal-data-49financial's bucket-policy Deny, are recorded beside granted, not in it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "FILE: infra/aws/terraform/inf-pipeline/cross-firm-deny.tf:1-28 @fd9c9ca174 ('cross-firm Deny belt', 'the belts, each a standalone aws_iam_role_policy cross-firm-bucket-deny'); bd-pipeline/bd-silver-merge.tf:13 and :75 ('EXPLICIT DENY opal-data-cot (firm-sep belt)'). comp-find -i '\\bbelts?\\b' over infra/aws/terraform: 92 hits across 578 files.",
        "LIVE READ: the authorization dump (250 roles, 7 users): principals whose policies carry a Deny naming the bucket and no Allow on it: opal-data-bd 47, opal-data-inf 18, opal-data-cot 47, opal-data-49financial 13 (125 pairs).",
        "LIVE READ: aws s3api get-bucket-policy --bucket opal-data-49financial: one statement, Sid DenyForeignFirmPrincipals, Effect Deny, Principal '*', ArnLike role/cot-*, role/inf-*, role/mdpf-*, role/opal-assets-mdpf-*.",
        "FILE: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py:535-537 @fd9c9ca174: _writers_49 reads every principal in granted and seen of opal-data-49financial as a writer that EN-f-1 must cover."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-c-2 WORKER FACE: 'GRANTED: every principal an identity policy grants any s3:* action on the bucket or its objects, plus every principal the bucket's own policy names, plus the role-side belts.'",
    "world_is": "A Deny-only row under granted would be graded as a writer by the issuer's own consumer. FENCE_WRITER_CENSUS.md records them under buckets.<bucket>.belt_only (each with its Deny statement and token) and buckets.opal-data-49financial.bucket_policy_deny. A granted principal that also carries a belt lists that belt in its own belts field.",
    "notes": "The C2 criteria read granted and seen only (check_en.py:283-309), so this placement moves no C2 verdict. Whether belts belong under granted is the issuer's call."
  }
]
```
