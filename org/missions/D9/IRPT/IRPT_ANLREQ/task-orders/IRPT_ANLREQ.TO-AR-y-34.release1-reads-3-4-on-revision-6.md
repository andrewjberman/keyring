# TO IRPT_ANLREQ.TO-AR-y-34 -- release 1's reads 3 and 4 re-run on irpt-status revision 6; one measured read that /original writes nothing

<to_id>IRPT_ANLREQ.TO-AR-y-34</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.7.0_AE_CloudOps~ANL</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete -- flipped by issuer 2.0.0_SA_COO~Y2 2026-10-11 ~08:4xZ: AR34-y-AC1 printed Y34-READS-OK and the proof instance VALID rc 0, both run by the issuer on the laptop applier's files at commit 1ebd6f6e0e. Reads 3a, 3b, 4_record, 4_route TRUE on revision 6 (6idtFvAm, measured); 3c null (no custody-lane request in the tenant). The /original read wrote nothing ON WHAT WAS COUNTED: S3 object versions 3 before and 3 after under the request's three artifact directories; DynamoDB tables were NOT counted. Unreadable compositions 0 of 49 (0 unfetchable; 49financial 0/9, cottonwood 0/39, inflection 0/1).</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>Y</workstream>
<proof_genre>DEPLOY</proof_genre>

**Directive:** D9 | **Fabric:** dell2 (issued); executed on the LAPTOP, the one box whose principal can read `irpt-requests` | **Risk:**
WORLD (live reads of a served function; one signed link is issued and discarded) | **Decomp cell:** `AR-y-34`
(`decompositions/IRPT_ANLREQ_DECOMP_R3_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## THE ORDER (the applier's face)

You are `0.7.0_AE_CloudOps~ANL`. You ran these reads once before: your result
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release1/Y1_laptop_reads_3a_4_5_rerun_result.json` (request
`REQ-4b5155ac2ea9467ab771b414`, tenant 49financial, a synthetic filer), under the read-only spec
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release1/Y1_laptop_reads_3_5_spec.json` (@66b6d08b9c). They were
measured on revision 2 (`BjUZjt2o`). The function now runs revision 6. Evidence measured on older running bytes does not carry.

### THE CELL (`AR-y-34`, inlined)

*Release 1's reads 3 and 4 re-run on revision 6; ONE measured read that the original-file route writes nothing (object versions before
and after).*

**Step 0.** `get-function-configuration irpt-status`: CodeSha256 is `6idtFvAmYk73wJdr5DPRIyEPrLeWgzjlqbdNr5f1wxc=`. Any other value is a
STOP: report it and run nothing. Record the value you read and its LastModified.

**Step 1 -- reads 3 and 4, by the SAME method as your earlier run** (a direct invoke of irpt-status with the event the HTTP API front
door passes, carrying the principal's claims; no credential is created, no record is changed), on the same request:
- **3a** the request's OWNER gets a signed link from `GET .../analysis/requests/{id}/original` whose `sha256` equals the retained
  original's. The link is NEVER written to a file, a log or a message: record its `sha256` and `expires_at` only.
- **3b** a viewer at ANOTHER firm is refused.
- **3c** a custody-lane request is refused `ANALYSIS_ORIGINAL_NOT_APPLICABLE`. If the tenant has no custody-lane request, record `null`
  with the reason (your first run found 0).
- **4_record** `GET .../analysis/requests/{id}?include=composition` returns the request's `ticket_id` and meets `OwnedAnalysisRequest`.
- **4_route** the `/original` route is declared exactly ONCE on the API (`get-routes`, every page read, counted client-side).
Do NOT run read 5 (a ticket-bound request reaching READY): it is owed by release 4's order, not this one.

**Step 2 -- the write-nothing read.** The pair of release 1 said "the original-file read does not write" and nobody measured it.
- From the code at box HEAD (`infra/aws/lambda/investor-reporting/ops/owned_report.py`, `original()`, and the address builders it calls),
  name the S3 keys or prefixes that route can reach for THIS request: the retained original's object, and any prefix under which it could
  write if it wrote.
- Count object VERSIONS on those keys (`list-object-versions`, every page, counted client-side; versions plus delete markers) BEFORE
  step 1's 3a call and AFTER it. Record both counts and, in one line, exactly which keys or prefixes were counted (`keys_scope`).
- Equal counts, at least 1: the read wrote nothing on what was counted. A changed count is recorded as it is and is a BLOCKING row; do
  not delete anything.

**Step 3 -- the result file**, `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/Y1_reads_3_4_rev6_result.json`:
`{"release_under_test": {"function": "irpt-status", "code_sha256": "<step 0>", "last_modified": "<step 0>", "claim": "measured"},
"request": "REQ-4b5155ac2ea9467ab771b414", "reads": {"3a": true|false, "3a_sha256": "...", "3a_link_expiry": "...", "3b": true|false,
"3c": true|false|null, "3c_reason": "<when null>", "4_record": true|false, "4_route": true|false},
"original_read_writes": {"versions_before": <int>, "versions_after": <int>, "keys_scope": "<what was counted>"}, "method": "<one line>"}`.
Booleans, digests, counts and codes only. No URL, no name, no figure, no document content anywhere in the file or your report.

---

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-11 ~08:3xZ; decomposition R3_Y AMENDMENT 2; 1.0.0_SA_CTO~DELL2 msg 4430): ONE more
read, Step 4, and one more member in the result file.** Gate limb that graded this amendment: read from this commit's own output.

**Why.** Cell `AR-y-32` makes each row of the owned-request history state the client its frozen selection names. The CTO ruled that a
row whose retained composition cannot be read is listed with `client_claim` `"UNREADABLE"` instead of refusing the viewer's page, and
set a condition before that cell merges: "count the accepted requests whose composition _selected_client cannot read, denominator
printed: if it is zero the marker is still right, and the number goes in the pair." Only your box's principal can read `irpt-requests`.

**Step 4 -- the unreadable-composition census (read-only).**
- The rule being counted is `OwnedRequestReader._selected_client` at box HEAD
  (`infra/aws/lambda/investor-reporting/ops/owned_requests.py`, :198-214): after the record's `composition_ref` is validated, the
  retained composition is read; the request is UNREADABLE when its document's `schema_version` is not the `COMPOSITION_VERSION` that
  module names, or the document has no `browser` member to take `client_id` from, or that `client_id` is neither null nor a string.
- Denominator: EVERY accepted analysis request record in `irpt-requests`, every tenant (sort key `analysis#REQ-<24 hex>#1`), every page
  read, counted client-side. Print it.
- For each, apply that rule to its retained composition and count the UNREADABLE ones. Read the composition by the same retained path
  the reader uses or by a direct object read of the ref the record names -- say which. A composition you could not fetch at all
  (denied, absent) is counted SEPARATELY as `unfetchable`, never folded into either number.
- Record in the result file: `"unreadable_compositions": {"count": <int>, "denominator": <int>, "unfetchable": <int>,
  "by_tenant": {"<tenant>": {"count": <int>, "denominator": <int>}}, "rule": "<file:lines read, at which commit>",
  "method": "<one line>", "claim": "measured"}`. Counts only: no request id, no client id, no document content.
- This step writes nothing and moves nothing.

Criterion `AR34-y-AC1` (`y34-reads`) now also requires `unreadable_compositions` with integer `count` and `denominator`
(0 <= count <= denominator, denominator >= 1) and `claim` `measured`. Steps 0 to 3 stand as written.

### ACCEPTANCE

<criterion id="AR34-y-AC1" cell_refs="AR-y-34"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y34-reads</invocation><expect>Y34-READS-OK</expect></criterion>
`AR34-y-AC1`: run from the workspace root. The result file states the live digest as measured; 3a, 3b, 4_record and 4_route are true;
3c is true or null with its reason; the two version counts are equal and at least 1; `keys_scope` is stated; the file carries no URL.

<expected_criteria>AR34-y-AC1</expected_criteria>

## BOUNDS

- READ-ONLY against AWS: `get-function-configuration`, `lambda invoke` of irpt-status with read routes only, `apigatewayv2 get-routes`,
  `s3api list-object-versions`. No put, no delete, no apply, no grant, no SendCommand. NEVER `aws lambda update-function-code`.
- The one signed link is discarded unused. Opaque ids only for real people; the request is synthetic.
- A read that fails is recorded FALSE with its closed reason code and reported; it is not retried into a pass.

<paths>
org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/
org/tier2_senior/0.7.0_AE_CloudOps~ANL/logs/
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R3_Y.md</decomp_doc> (round 3, workstream Y), cell `AR-y-34`.
<owned_cells>AR-y-34</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR34-y-AC1. The instance is at
`org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/IRPT_ANLREQ.TO-AR-y-34.release1-reads-3-4-on-revision-6.proof_of_spec.json`.
Validate it AFTER its commit with `python .tools/proof-of-spec-check.py <instance> AR34-y-AC1`.
</proof_of_spec>

**REPORT (once) to `2.0.0_SA_COO~Y2`:** the check line verbatim; the commit and its measured push state; each read's boolean and code;
the two version counts and `keys_scope`; any row ids. Leave the status flip to the issuer.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- read-only; no resource is changed. comp-routes: RUN (by reading) -- the /original route count read 1 across all APIs at 2026-10-11T04:54Z (this issuer) and 1 of 119 by the applier of TO-APPLY-Y1; read 4_route re-measures it. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: RUN (by reading) -- no IAM change; the reads use the laptop applier's existing principal, the one that ran the 2026-10-09 reads. dell2's principal cannot read irpt-requests (kms), which is why the order is not issued on this box. comp-adversary: RUN -- AR34-y-AC1 dry-run at the base: FAIL as expected (no result file); the check refuses a result on any digest but the live one, a missing keys_scope, unequal version counts, and any URL in the file.
lane: the applier's own deliverables and logs; read-only on the world.
</preflight>

Source: CTO round-3 analysis @430d79e86d section 4 Y4 ("reads 3 and 4 re-run on revision 6; one measured read shows the original-file
route writes nothing (object versions counted before and after, on the keys that route can reach)"); row IRPT_ANLREQ-D2-S32 (3.0.0_SA_CVO,
L9); TO-APPLY-Y1 AMENDMENT 10. No never-widen pair: no served output moves, no resource is written.

CROSS-BOX DELIVERY: this order is issued on dell2 to a laptop seat. It reaches the laptop by the box-sync of `box/dell2` into `CLOUD`.
`0.0.0_AB_MSTR~DELL2` is asked to tell the laptop's manager the order's path once it is on origin. Until a laptop seat acks it, this order
is PARKED: owner `2.0.0_SA_COO~Y2`; it un-parks on that ack.

FLIP NOTE (issuer, 2026-10-11 ~08:5xZ): the flip gate looks for this order's proof instance under the project's tree `deliverables/<serial>/`. The issuer's cut had placed it in the applier's Tier-2 seat folder, so the gate found none (measured: two refused flip commits; a `# pipeline-override:` line does not lift that limb and was removed uncommitted). A BYTE-IDENTICAL COPY of the applier's instance (its commit 1ebd6f6e0e) is committed with this flip at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/IRPT_ANLREQ.TO-AR-y-34.release1-reads-3-4-on-revision-6.proof_of_spec.json`. The proof is the applier's; the copy is a locator, and the cut defect is the issuer's.
