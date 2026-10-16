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
    "id": "TCKT_MTADTA-D1-W2-S1",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~2",
    "surfaced_at": "2026-10-16T07:06:00Z",
    "one_line": "TO-MD-i1 says identity.tf is one of four files in the root infra/aws/terraform/trino/, but that directory is absent at HEAD of the worker branch and no sibling file of it is tracked; the three siblings belong to cells MD-h-1, MD-a-1 and MD-c-1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git ls-files infra/aws/terraform/trino returns no path at worktree HEAD c9971df7ca; the same query on the main checkout lists none either",
        "org/missions/D7/TCKT/TCKT_MTADTA/decompositions/TCKT_MTADTA_DECOMP.md lines 41-49: trino/main.tf (MD-h-1), trino/access.tf (MD-a-1), trino/collector.tf (MD-c-1) and trino/identity.tf (MD-i-1) are the four files of the root, none yet merged",
        "task order TCKT_MTADTA.TO-MD-i1 lines 61 and 89: 'one of four in the root infra/aws/terraform/trino/'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The Terraform root infra/aws/terraform/trino/ already carries its four files when the identity file is written, so the identity file joins an existing root.",
    "world_is": "The root does not exist at HEAD; identity.tf is written as the first file of the directory in this worktree. Its check (r1_check_i1.py tf) passes on that file alone. Nothing was weakened; the three sibling files are not created here.",
    "notes": "The sibling cells land their files at the round-1 drain. Whether the trino root is complete at merge time is for the drain's refuser and the L8 read, not for this cell."
  },
  {
    "id": "TCKT_MTADTA-D1-W2-S2",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_TCKT_MTADTA~2",
    "surfaced_at": "2026-10-16T07:06:30Z",
    "one_line": "The worker worktree is a sparse checkout that does not materialise org/surprise_channel/, so the row schema org/surprise_channel/schemas/investigation_item.schema.json that the surprise-row gate validates against is absent from the worker's tree although it is tracked at HEAD.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C /c/tmp/wk-tckt-mtadta-2 config core.sparseCheckout = true; git sparse-checkout list does not include org/surprise_channel",
        "git ls-files org/surprise_channel/schemas lists investigation_item.schema.json and remediation_row.schema.json; ls org/surprise_channel/ in the worktree reports no such directory",
        "the main checkout C:/Dev/ajb_workspace holds the schema on disk"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Every worker tree carries the surprise channel schema on disk, so a worker can validate its own row against it at commit.",
    "world_is": "The schema is not on disk in this worker's worktree. The row written here was not validated against the schema by this worker; the gate is run at commit and its output is recorded in the report.",
    "notes": "Nothing was changed in the sparse-checkout configuration. The fix belongs to the worktree provisioning owner (the sparse cone for worker worktrees)."
  }
]
```
