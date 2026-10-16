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
  }
]
```
