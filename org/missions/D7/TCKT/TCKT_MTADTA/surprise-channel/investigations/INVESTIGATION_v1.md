# TCKT_MTADTA -- surprise channel, INVESTIGATION v1 (round 1, dell1 fabric)

**Opened by:** `1.0.0_SA_CTO~DELL1` at L4 (seat rows; the CVO assembles from L8, spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`). The gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`.
**Id grammar:**
- a worker's row is `TCKT_MTADTA-D1-W<n>-S<k>`;
- a seat's row is `TCKT_MTADTA-D1-S<k>` (dell1 coordinate);
- the CVO's adjudication rows live in `../adjudications/`.

**Append-only during the round.** Never edit an existing row.

```json
[
  {
    "id": "TCKT_MTADTA-D1-S1",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "1.0.0_SA_CTO~DELL1",
    "surfaced_at": "2026-10-16T06:38:00Z",
    "one_line": "The safe-commit PRD manifest gate refused PRD v0.2 with 'no top-level ENDPOINT section' when the file's only defect was CRLF line endings, while a direct run of the same gate on the working file passed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "0.0.0_AB_MSTR~DELL1 (infrastructure: .tools/safe-commit.sh and .tools/prd-manifest-gate.py); this seat only surfaces",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit of org/missions/D7/TCKT/TCKT_MTADTA/prd/TCKT_MTADTA_PRD.md (v0.2 edit) twice: 'ERROR: BLOCKED -- step-4 PRD surface-manifest gate ... no top-level ENDPOINT section the L6 matcher can resolve'",
        "python .tools/prd-manifest-gate.py <same path>, same minute: '[prd-manifest] OK: 1 step-4 PRD document(s) carry their key surfaces'",
        "byte read of the file: CR count 309 (the v0.1 blob @315f7a19af: 0); after converting to LF the commit landed @86f3caec3a"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A gate refusal names the defect it found, and the same gate gives the same verdict on the same bytes whoever runs it.",
    "world_is": "The refusal named a missing heading that was present. The real defect, CRLF line endings from a Python text-mode write on Windows, was named nowhere. The direct run and the commit-time run disagreed.",
    "notes": "The cause of the disagreement was not read: the commit-time run may see the staged blob and the direct run the working file. The fix belongs to the gate's owner: name CRLF in the refusal, or normalise before matching. Nothing was edited here."
  },
  {
    "id": "TCKT_MTADTA-D1-S2",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~S1",
    "surfaced_at": "2026-10-16T06:54:24Z",
    "one_line": "PRD C-POPULATION resolves an event's actor against the eight UPNs AND their Entra object ids read once at collection, but C-APP gives the collector app ONE permission (ActivityFeed.Read) and reading object ids needs a Graph directory permission, so the two rows cannot both hold.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~DELL1 (owns the PRD; the issuer's round-1 ruling is to resolve by the four UPN fields only and leave object_ids empty)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_MTADTA/prd/TCKT_MTADTA_PRD.md C-POPULATION (the actor is resolved across UserId, MailboxOwnerUPN, SendAsUserSmtp and SendOnBehalfOfUserSmtp, case-insensitively, against the eight UPNs and their Entra object ids read once at collection)",
        "same file, C-APP (ONE new single-purpose Entra app holds ActivityFeed.Read on the Office 365 Management APIs, app-only; the gateway apps gain no permission)",
        "org/missions/D7/TCKT/TCKT_MTADTA/decompositions/TCKT_MTADTA_DECOMP.md ruling 4 and task order TO-MD-c1 (population.json carries an empty object_ids map in round 1)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The collector reads the eight's Entra object ids once at collection and matches events by id as well as by UPN, with the app holding exactly one permission.",
    "world_is": "Reading a user's object id takes a Graph directory permission (User.Read.All or an equivalent) or the delegated token of a signed-in person; the app as specified holds neither. Audit records carry UPNs in the four named fields, so UPN matching works without it; an id-only record (a UserId that is a GUID) would be dropped as out of population.",
    "notes": "Round 1 builds UPN resolution only. Whether a GUID-only actor occurs in the feed is unread until the first real content lands (release act 4); if it does, the enrichment list takes either a one-time id lookup run by Andrew into population.json or a second permission by the CTO's ruling."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S1",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:14:07Z",
    "one_line": "TO-MD-h1 names infra/aws/terraform/transcripts/main.tf as the template to model on, but this worktree is a sparse checkout that does not materialise that directory; the template was read from HEAD with git show.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git sparse-checkout list in C:/tmp/wk-tckt-mtadta-1 (core.sparseCheckout true) names no infra/aws/terraform/transcripts and no infra/aws/terraform/trino entry; ls of infra/aws/terraform/ shows .gitignore, ROLLBACK_PROCEDURE.md, modules/ and tombstones.json only",
        "git ls-files infra/aws/terraform/transcripts lists main.tf at HEAD c9971df7ca; git show HEAD:infra/aws/terraform/transcripts/main.tf read at lines 1-135, plus its aws_kms_alias, aws_s3_bucket and public-access-block blocks",
        "git add -n infra/aws/terraform/trino/main.tf in the same worktree: rc=0, the new file is addable under the sparse set"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-h1 BUILD step 7: model infra/aws/terraform/trino/main.tf on infra/aws/terraform/transcripts/main.tf lines 1-135 (read them), in the worktree the order names.",
    "world_is": "The template path is absent from the worktree and present only at HEAD. It was read with git show, not by extracting or rebuilding the tree. The new file was written under infra/aws/terraform/trino/, which is not in the sparse list either.",
    "notes": "No tree was rebuilt. The worktree's sparse list is the cause; the template content is unchanged and was modelled from HEAD. The commit of the new file is measured at its commit and reported in the worker report."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S2",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:14:07Z",
    "one_line": "TO-MD-h1 asks for the portal targets to be committed on the portal nested branch, but the portal rule requires a cand/<box>/<slug> branch cut from the last PROD release and registered for approval; the portal commit is withheld and the regenerated files stay uncommitted in the nested checkout.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal rev-parse --abbrev-ref HEAD prints wk-TCKT_MTADTA-1-portal at 39dab87f (a DEV merge); git -C portal rev-parse origin/PROD prints ab2c4365",
        "portal/CONTRIBUTING-BOXES.md steps 1-4: build on cand/<box>/<slug> cut from the last PROD release, push under that name, register with open-calls.py add --kind approval; a box never pushes DEV",
        "python lib/opal_naming.py generate --out . rewrote three portal targets: firmDisplayNames (registry hash line only), vendorDisplayNames (hash line plus two VENDOR_DISPLAY_NAMES rows for m365-metadata), firmAccess.ts (identical to the blob bar CRLF, the working copy being CRLF under autocrlf)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-h1 WORKER FACE step 5: if portal/ files change and the worktree carries a portal checkout, commit them inside portal/ on its nested branch and name that commit.",
    "world_is": "The nested portal branch is a DEV-cut line, and the portal change rule (CONTRIBUTING-BOXES steps 1-4) routes any portal change through a cand/<box>/<slug> branch from PROD with an approval registration. The order and the rule disagree; the rule governs a portal change, so the commit was not made.",
    "notes": "Owed by the issuer 2.0.0_SA_COO~S1 and the portal owner: either a cand/dell1/<slug> branch cut from origin/PROD carrying the generated VENDOR_DISPLAY_NAMES rows, or a ruling that generator output is exempt. Criteria AC1 passes on disk; nothing was pushed."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S3",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:14:07Z",
    "one_line": "TO-MD-h1 gives the Lambda role's exception type as 'group' for globgrph-trino-access-group, but root_map.json exceptions carry node types (IAM_ROLE, LAMBDA, IAM_POLICY); the group's node type is IAM_GROUP.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/logic/registry/root_map.json exceptions: Counter over the file gives IAM_POLICY 84, IAM_ROLE 38, LAMBDA 29 and no GROUP type",
        "org/standards/NAMING_SCHEMA.json v1.13 kind.by_type maps IAM_GROUP to kind group; lib/opal_naming_rootmap.py load_map accepts any non-empty string as an exception type",
        "root_map.json roots.trino.exceptions[0] written with type IAM_GROUP; python lib/opal_naming.py validate rc=0 after the edit"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-h1 BUILD step 3: add the exception globgrph-trino-access-group with type group.",
    "world_is": "The file's exception types are node types, and the node type that carries the kind group is IAM_GROUP. The literal word group is a kind, not a type in this file.",
    "notes": "The worker wrote IAM_GROUP, the file's own vocabulary. The issuer should confirm before the MD-a-1 order reads the entry."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S4",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:14:07Z",
    "one_line": "TO-MD-h1 points to section 4 of infra/logic/06_CONFORMANCE_LEDGER.md as the R20 entry schema, but that section is the shared serving bucket; the schema is 02_DOCTRINE.md section 4 and the entries are ledger section 6.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/logic/06_CONFORMANCE_LEDGER.md line 111: '## §4. THE SHARED SERVING BUCKET -- opal-data-portal-v2'",
        "infra/logic/02_DOCTRINE.md line 599: '## §4. THE EXCEPTION REGISTER -- its schema (its ENTRIES live in 06_CONFORMANCE_LEDGER.md §6)'",
        "infra/logic/06_CONFORMANCE_LEDGER.md section 6 table: rows X1 to X17 before the edit; the new row X18 was added after X17 with the schema's columns"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-h1 BUILD step 6: read section 4 (the entry schema) and section 6 (the register) of infra/logic/06_CONFORMANCE_LEDGER.md, then add one R20 entry.",
    "world_is": "The entry schema is in infra/logic/02_DOCTRINE.md section 4; the ledger's section 4 is a different plane. The entry was written to the ledger's section 6 register table, the carrier the doctrine names.",
    "notes": "The entry follows the doctrine schema (pipeline, axis, departure, why, acknowledged, kind, state). Registered as X18."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S5",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:26:19Z",
    "one_line": "The coordinator reports TO-MD-h1 merged at issuer commit 77716ab496 on this branch, but that commit is not an ancestor of wk-TCKT_MTADTA-1 HEAD (7ffa70368d); the merge was not performed here, the order's files are read from the branch as it stands.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git cat-file -t 77716ab496 returns commit; git merge-base --is-ancestor 77716ab496 HEAD returns not-ancestor in C:/tmp/wk-tckt-mtadta-1",
        "the sparse cone of the worktree lists infra/aws/lambda/globgrph-trino-access, infra/aws/lambda/m365-metadata-collector and infra/aws/terraform/trino, but the first two directories are absent on disk at HEAD 7ffa70368d",
        "infra/aws/lambda/globgrph-trino-access/silver_builder.py is absent in the worktree; build.sh refused with rc=1 on its cp step"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-a1 BOUNDS: silver_builder.py is another cell's file, already merged in the issuer's tree; the worker creates nothing there and injects a stub in its tests. Coordinator message: the order runs in the same worktree on the same branch, after TO-MD-h1 is merged.",
    "world_is": "The issuer's merge is a commit the branch does not contain. The branch carries the h1 rows, the R20 entry and trino/main.tf (commits 21c6720238 and 7ffa70368d), and not the issuer's copy of silver_builder.py. The worker's rule forbids a merge, so the a1 files are written on the branch as it stands.",
    "notes": "The drain or the issuer must merge 77716ab496 into the branch before the a1 commit is merged to CLOUD, or the two copies of the h1 rows meet at the merge. Nothing was merged, rebased or reset."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S6",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:26:19Z",
    "one_line": "TO-MD-a1 asks for a Deny of non-TLS requests to every principal and forbids a wildcard principal, but a Deny for every principal needs Principal star, which the order's own AC2 check refuses as a wildcard; the bucket policy names the role under NotPrincipal and the role's policy denies its own non-TLS requests.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "order TCKT_MTADTA.TO-MD-a1 BUILD 4, bucket policy bullet: 'plus a Deny of any non-TLS request' and BOUNDS-level 'No wildcard principal'",
        "r1_check_a1.py tf: refuses a Principal assignment of the literal star in any form the regex reads (Principal = star-in-quotes or Principal = AWS star-in-quotes)",
        "infra/aws/terraform/trino/access.tf aws_s3_bucket_policy.trino: statement DenyNonTLSRequestsToEveryPrincipalButTheAccessRole uses NotPrincipal = the role ARN; aws_iam_role_policy.access statement DenyNonTLSRequestsByTheRole covers the role"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-a1 BUILD 4: the bucket policy carries an explicit Deny of the data actions to every principal whose aws:PrincipalArn is not the role, plus a Deny of any non-TLS request; no wildcard principal.",
    "world_is": "In AWS a Deny that reaches every principal is written with a wildcard principal, the only form of 'every principal' the policy grammar has. The order forbids that form on the same resource. The worker used NotPrincipal (every principal but the role) for both statements, and split the non-TLS deny for the role into the role's own policy.",
    "notes": "The residual is the same as C-RESIDUAL for the data actions. The issuer should confirm that NotPrincipal plus the role-side deny meet 'every principal' before the drain; the check was not weakened."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S7",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:26:19Z",
    "one_line": "TO-MD-a1 says handler.py imports stdlib plus boto3 only, but the silver reader must read parquet, which needs the AWS-managed pandas layer; the reader imports pandas lazily inside read_day_rows, not at module level.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "order TCKT_MTADTA.TO-MD-a1 BUILD 1: 'the contract above, stdlib plus boto3 imported lazily inside lambda_handler only'; the silver_reader is 'of your own in handler.py'",
        "order WORKER FACE step 2 and the silver builder: the silver builder uses the AWS-managed pandas layer, which carries pyarrow; build.sh does not package pyarrow",
        "infra/aws/lambda/globgrph-trino-access/handler.py _DaySilverReader.read_day_rows: 'import pandas' inside the function body; tests inject a stub reader and never call read_day_rows"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MD-a1 BUILD 1: handler.py is stdlib plus boto3, imported lazily inside lambda_handler only; the silver reader is the worker's own code in handler.py.",
    "world_is": "Reading the silver parquet from S3 requires a parquet decoder. The stdlib has none, and the layer that provides one is the pandas layer the order names. The reader therefore needs pandas, imported inside read_day_rows; no test exercises that path, because the tests inject the reader.",
    "notes": "The default reader is untested in this round. The issuer should either accept the lazy pandas import in the reader, or move the decode to the silver builder's cell. The stdlib-only line of BUILD 1 is not met for read_day_rows and is recorded here rather than bent."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S8",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:26:19Z",
    "one_line": "The naming gate refused three S3 key literals in handler.py (the gold coverage, silver and bronze tier prefixes), because the door carries them as typed strings; the builder's address() gives the same tails, but the Lambda package carries no lib/opal_naming.py.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commit 9d4f20bdb8 safe-commit output: '[naming-gate] NAMING REFUSE infra/aws/lambda/globgrph-trino-access/handler.py:34 gold/collection_coverage/' and lines :35 silver/activity_events/ and :36 bronze/audit_events/date=%s/; '(WARN window: 3 REFUSE verdict(s) did not block; ENFORCE is --enforce ...)'",
        "python lib/opal_naming.py address for ('m365-metadata','trino','silver','activity_events','date=2026-10-15', object='data.parquet') returns s3://opal-data-trino/m365-metadata/trino/silver/activity_events/date=2026-10-15/data.parquet; the gold and bronze forms match the handler's tails",
        "build.sh packages handler.py and silver_builder.py and nothing else, per the order's BUILD 2; lib/opal_naming.py is not in the package"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md rule 30 and the LGIC rule: every S3 address is lib/opal_naming.py address() output; a builder refusal is a missing registry row, never a hand-typed workaround.",
    "world_is": "The door builds its key prefixes from typed tier and table segments. The segments match the builder's output, and the gate grades them as REFUSE in the warn window, so the commit landed. The order's package list leaves no route for the door to call the builder at run time.",
    "notes": "The issuer decides: package the builder's key function with the door, or have Terraform pass the builder-computed prefixes as environment variables. Nothing was changed to silence the gate."
  },
  {
    "id": "TCKT_MTADTA-D1-W1-S9",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~1",
    "surfaced_at": "2026-10-16T07:26:19Z",
    "one_line": "The naming gate raised, not refused, the IAM resource pattern 'm365-metadata/trino/*' in access.tf as a secret, because its tokeniser cannot place the character star; a grader defect, not a verdict on the name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commit 9d4f20bdb8 safe-commit output: '[naming-gate] NAMING RAISE infra/aws/terraform/trino/access.tf:106 m365-metadata/trino/* -> (rule or registry defect)' with why 'RAISE as SECRET: rule or registry defect, not a refusal: G3: the tokeniser cannot place a character of a secret star'",
        "access.tf line 106 is the Resource of the ReadAndWriteTheTrinoPrefix statement of aws_iam_role_policy.access: an S3 object ARN suffix, the same shape as the transcripts pull policy"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The naming gate grades every name and address the diff writes, and a RAISE names a rule or registry defect to the owner of the gate.",
    "world_is": "The IAM policy resource pattern is an S3 object wildcard, not a name. The gate reads it as a secret and cannot place the wildcard character, so it raises instead of grading it.",
    "notes": "Owed to the naming gate's owner. The worker did not alter the resource pattern to silence it."
  }
]
```
