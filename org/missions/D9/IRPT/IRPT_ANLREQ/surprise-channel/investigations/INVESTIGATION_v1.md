# IRPT_ANLREQ -- surprise channel, INVESTIGATION v1 (round 1, dell2 fabric)

**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`).
Lane `ANY`. **Id grammar:** a worker's row is `IRPT_ANLREQ-D2-W<n>-S<k>`; append-only during the round.

```json
[
  {
    "id": "IRPT_ANLREQ-D2-W62-S1",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~62",
    "surfaced_at": "2026-10-09T05:40Z",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "AR-g-12: the repository registers no service subject for family ANALYSIS_COMMENTARY (SERVICE_READERS holds only svc-commentary -> REQUEST_COMPOSITION), so the live commentary reader raises COMMENTARY_READER_UNWIRED.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/reports/repository.py:28 @e7a25ac17b -- SERVICE_READERS = {\"svc-commentary\": frozenset({\"REQUEST_COMPOSITION\"})}; _service_allows admits a subject only for a family it is registered for",
        "comp-find --files 'ANALYSIS_COMMENTARY' infra/aws/lambda @e7a25ac17b -- 0 hits across 5619 files (the family is registered nowhere yet; AR-t-12's persist cell is not merged)",
        "infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_packager.py test_h_the_live_commentary_reader_is_unwired_without_a_repository_or_a_registered_subject -- asserts no subject holds the family today, and that exactly one registered subject makes the read go through ArtifactRepository.get"
      ]
    },
    "spec_asserts": "AR-g-12 / AMENDMENT 1 I4s: the packager reads the commentary bytes through the repository's service-reader family grant (repository.py:43); otherwise the live port raises COMMENTARY_READER_UNWIRED and a row is filed.",
    "world_is": "At the base the grant for ANALYSIS_COMMENTARY does not exist: no subject in SERVICE_READERS holds the family and the family is not registered. The live reader (opal_packager.live_read_artifact) reads the subject from repository.SERVICE_READERS, requires exactly one, and raises COMMENTARY_READER_UNWIRED otherwise; it names no subject itself. Some later cell must add the SERVICE_READERS entry (repository.py is outside this cell's paths)."
  },
  {
    "id": "IRPT_ANLREQ-D2-W62-S2",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~62",
    "surfaced_at": "2026-10-09T05:40Z",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "AR-g-12 idempotence: no record the cell may read holds a fact that a package was attached, so the rule reads the TICKET through an added ticket_package(ticket_id) port, whose live form raises PACKAGER_PRINCIPAL_UNSET.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py:68 @e7a25ac17b -- the acceptance record is written at accept() and carries identity, owner, browser_sha256, composition_ref, accepted_at; the READY job row (durable_job.py put_state) carries the receipt; neither has an attach field",
        "infra/aws/lambda/ticket_center/lambda_function.py:1367 package_ticket @e7a25ac17b -- the ticket stores `package` ({4 refs, attached_at, attached_by}); a second POST without prior_attached_at is refused 409 'ticket already carries a package'",
        "infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_packager.py test_g_* -- the rule in the fake: a second message makes no second render and no second attach; a failed attach leaves the pair open"
      ]
    },
    "spec_asserts": "AR-g-12 step 3: a second commentary_ready for the same pair, after a successful attach, must not render or call again; read that from the ticket or a fact the records hold; if neither can tell, file a row and keep the rule in the fake.",
    "world_is": "The records cannot tell. The ticket can (its `package` field), but the order lists no ticket-read port and whether svc-irpt-packager may GET a ticket is unread (the principal does not exist yet). So the packager takes ticket_package(ticket_id) -> package|None as an injected port (live form: PACKAGER_PRINCIPAL_UNSET) and skips render and attach when it is not None. The ticket's own 409 on a second attach without prior_attached_at is a server-side backstop against a double attach, but only after a wasted render."
  },
  {
    "id": "IRPT_ANLREQ-D2-W62-S3",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~62",
    "surfaced_at": "2026-10-09T05:40Z",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "AR-g-12 original_ref: the uploaded file a prospect request was filed on is reached at record.owner.prospect_input_id (the normalized upload's upload_id); a custody-lane request has none and is refused ORIGINAL_REF_ABSENT; whether the ticket page's reader (I6) opens an upload id is unread.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/investor-reporting/reports/request_composition.py:75-81 @e7a25ac17b -- upload_id = normalized.source.upload_id must equal owner.prospect_input_id, else PROSPECT_NORMALIZED_OWNER_BINDING",
        "infra/aws/lambda/investor-reporting/reports/request_composition.py:53-59 @e7a25ac17b -- a request without browser input_id is the custody lane and its owner carries no prospect_input_id",
        "infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_packager.py test_f_* -- an owner without prospect_input_id is refused ORIGINAL_REF_ABSENT, with no render and no attach"
      ]
    },
    "spec_asserts": "AR-g-12: original_ref = the reference of the uploaded file the request was filed on, found on the acceptance record or its composition; if not reachable, file a row and refuse ORIGINAL_REF_ABSENT; never invent one.",
    "world_is": "It is reachable for the prospect lane, as the upload id the composition is bound to (read from the record, not invented). The acceptance record has no field named original_ref. Whether an upload id (rather than a retained artifact id) is a ref the I6 signed-link reader (ops/owned_report.py:154) opens is not read here; AR-v-13 consumes it."
  },
  {
    "id": "IRPT_ANLREQ-D2-W62-S4",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "0.9.0_WK_IRPT_ANLREQ~62",
    "surfaced_at": "2026-10-09T05:40Z",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "AR-g-12 shapes the neighbouring cells have not fixed: commentary_ref is an artifact_id string in AMENDMENT 1 but a {artifact_id, sha256, version_id} dict in AR-t-12's persist_draft contract, and the draft's bytes shape is unwritten; pdf_ref is an opaque artifact id only when the injected stores carry `artifacts`.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md AMENDMENT 1 row I4s @e7a25ac17b -- 'The artifact's opaque id is commentary_ref'",
        "org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-t-12.commentary-reads-irpt-reader-persists-draft.md:49 @e7a25ac17b -- persist_draft(tenant, request_id, draft) -> {\"artifact_id\", \"sha256\", \"version_id\"}",
        "infra/aws/lambda/ticket_center/lambda_function.py:1367 package_ticket @e7a25ac17b -- every package ref must be a non-empty string; no bucket"
      ]
    },
    "spec_asserts": "AR-g-12: commentary_ref is read from the acceptance record and carried in the I5 payload as a pointer; the DRAFT's text and title reach build(commentary=...).",
    "world_is": "The packager accepts either shape on the record (a string, or a dict whose artifact_id it uses) and always sends the artifact_id string, since I5 takes strings. It reads the draft's bytes as a JSON object with a string `text` and an optional string `title`, and refuses anything else COMMENTARY_MALFORMED; AR-t-12 has not written the bytes yet, so that shape is this cell's assumption. produce_package returns pdf_ref = the retained artifact's artifact_id when stores carry `artifacts`, else the builder's key within the family (a pointer, no bucket); the live `stores` factory must supply `artifacts` for pdf_ref to be an id the ticket page can open."
  }
]
```
