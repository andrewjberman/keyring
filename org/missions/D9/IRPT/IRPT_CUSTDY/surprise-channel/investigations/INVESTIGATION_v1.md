# IRPT_CUSTDY -- surprise channel, INVESTIGATION v1 (dell2 placement)

**Opened by:** `2.0.0_SA_COO~K2` at the round-1 issuance. **Home:** the project tree's channel; the gate `.tools/surprise-row-gate.py`
validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`. A seat's row is
`IRPT_CUSTDY-S<k>`; a worker's is `IRPT_CUSTDY-W<n>-S<k>`. **Append-only during the round.** Never edit an existing row.

## IRPT_CUSTDY-S1 -- the render path's input is a portal export request; whether it renders a client-report document is unmeasured

```json
{
  "id": "IRPT_CUSTDY-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T08:12:00Z",
  "one_line": "The PRD's S07 marks the render on irpt-export-render as held, but that path renders portal pages through a minted token, and whether it can render a client-report document is unmeasured.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_CUSTDY/prd/IRPT_CUSTDY_PRD.md v0.2 @c2bc15f427 section 6 row S07: claim 'held', verb 'wire'",
      "infra/aws/terraform/investor-reporting/export/b2_render.tf lines 1-17 at dell2 HEAD: submit-export mints a render token into SSM /irpt/render-token/<ATT-id> and dispatches a render host that renders the read functions' render ports",
      "aws lambda get-function irpt-export-render, 2026-10-07 ~07:5xZ: Active, LastModified 2026-10-06T01:35:28Z"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.2 S07: the render on the IRPT_BCKEND export path is held; round 1 wires the template to it.",
  "world_is": "The path exists and is live, but its input is a portal export request, not a document. Cell CU-a-4 reads the path's input contract from source and reports accepts_document; a gap is routed by the issuer to IRPT_BCKEND's COO at the drain, never written into IRPT_BCKEND's paths."
}
```

## IRPT_CUSTDY-W1-S1 -- the directory entry carries no advisor field; CU-a-1 reads the advisor from the ownership map

```json
{
  "id": "IRPT_CUSTDY-W1-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~1",
  "surfaced_at": "2026-10-07T08:25:00Z",
  "one_line": "The directory entry carries no advisor field, so the PRD's S01 claim (advisor list from the directory) fails as written; the advisor-to-accounts map is the separate ownership map, which CU-a-1 consumes instead.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/investor_reporting/directory_runner.py:450-516 @30f94c3ab1: _entry emits ids (firm/client/account/relationship), display_name, masks, permitted_scope, termination, access, revision and cohort with hierarchy_path []; no advisor or rep key; build_49f (531-641) reads dim_account and dim_relationship and joins no rep column",
      "infra/aws/lambda/investor-reporting/_scope/resolve.py:347-376 @30f94c3ab1: advisor_grant reads ownership['advisors'][advisor_id]['accounts'|'relationships'] -- the advisor lives in the ownership map, projected into the directory id space by _ids.projection_for_firm",
      "data/assets/scripts/gold/runners_49f/d08_firm_ownership_map.py:1-40 @30f94c3ab1: the producer of platinum/<firm>/ownership_map.json (schema_version 1, advisors keyed by slug); its docstring declares the SERVED map carries the Black Diamond z-id grammar, which _ids/data/custodian_key_seam.json projects (IRPT_BCKEND-W1-S22)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CU-a-1 and PRD v0.2 S01: the advisor and household live in a directory entry; the list is read from the directory (held, brief F1).",
  "world_is": "A DirectoryEntry holds households (RELATIONSHIP or ACCOUNT entries) and opaque account ids but no advisor. CU-a-1 therefore joins the firm's ownership map (--ownership, REQUIRED: the map's address is not in the naming registry so no default is typed; the edge validator reads it from the firm's platinum/ area) to the directory through _ids.projection_for_firm; nothing was invented. Unmeasured here: that the live 49 Financial map's z-id grants all resolve through the seam to directory accounts (the list prints directory_missing=<n> and the census prints it per advisor) and the live key and bucket of the map; the issuer's first real run measures both. Also an interpretation to confirm: an advisor with ANY uncovered account is excluded whole (the order's test 5), not merely that household."
}
```
