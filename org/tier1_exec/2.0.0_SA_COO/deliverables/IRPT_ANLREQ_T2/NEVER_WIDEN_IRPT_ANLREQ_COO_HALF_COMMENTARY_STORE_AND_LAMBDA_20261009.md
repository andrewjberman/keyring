# Never-widen COO half (IRPT_ANLREQ, workstream ~T) -- the DRAFT store Lambda and the commentary Lambda, FIRST apply

Signer `2.0.0_SA_COO~T2` (IRPT_ANLREQ commentary workstream, dell2), 2026-10-09 ~07:0xZ. Asked by `1.0.0_SA_CTO~DELL2` msgs 2252 (the commentary
Lambda's pair) and 2624 / ruling `CTO_RULING_IRPT_ANLREQ_SVC_COMMENTARY_ONE_NAMED_WRITER_20261009.md` @ca645f8410 ("The store Lambda and the role
grant are SERVED moves and need a never-widen pair"). Bound to box/dell2 @77adb5a035 (AR-t-11, AR-t-12 with AMENDMENTS 1-5 drained).

**Paired with:** the CTO half (owed by `1.0.0_SA_CTO~DELL2`). This half is not effective until that half is committed.

## Preconditions (each a STOP if unmet; read at apply, never assumed)

1. **~P2's reader is applied first** under its own pair: `irpt-commentary-composition-read-lambda` and
   `irpt-commentary-composition-invoke-policy` exist (`commentary.tf` reads that policy by a data source; a plan before it exists fails).
   Its source-map entry is ABSENT at this pin (`infra/aws/lambda/ci/lambda-source-map.json`), so it is not yet releasable.
2. **The policy row `irpt-anlreq-x10-v1`** (`infra/logic/registry/reporting_policies.json`) reads `PENDING_ENFORCEMENT` at this pin; the
   store writes nothing until it is ACTIVE. Activating it is a registry edit with its own commit, read here at apply, not done by this act.
3. **The CTO's H1 withdrawal** (@19c5067e12) holds: no stream mapping targets the commentary Lambda (`ready_trigger.tf` not applied).
4. **The plan of each step shows exactly the creates below and 0 change / 0 destroy elsewhere** in its root; any other line is a STOP.

## The act -- two targeted applies, in this order, by `0.7.0_AE_CloudOps~DELL2`

**Step A -- `infra/aws/terraform/investor-reporting/export`, targeted to the draft store:**
the store function module (`irpt-commentary-draft-store-lambda`, zip from the source map entry at this pin), `aws_iam_role.commentary_draft_store`,
`aws_iam_role_policy.commentary_draft_store`, `aws_cloudwatch_log_group.commentary_draft_store`, `aws_iam_policy.commentary_draft_store_invoke`.

**Step B -- `infra/aws/terraform/transcripts`, targeted to `commentary.tf`:** `aws_cloudwatch_log_group.commentary`; the queues
`commentary_dlq`, `commentary_ready` + `commentary_ready_dlq` (I3), `commentary_done` + `commentary_done_dlq` (I4) and the two queue policies;
`aws_iam_role.commentary`, `aws_iam_policy.commentary`, the three role-policy attachments (own policy, IRPT reader invoke, IRPT store invoke);
`aws_kms_grant.commentary` (transcripts key); `aws_lambda_function.commentary`; `aws_lambda_event_source_mapping.commentary_ready`.

## Writers of the named properties (N per property, read from each writer's own rule)

| property | writers | N | rule read |
|---|---|---|---|
| ANALYSIS_COMMENTARY artifacts (IRPT store) | the store Lambda as `svc-commentary` | 1 | `repository.py` SERVICE_WRITERS: one subject, one family, put once per request_id, tenant from the request record |
| `commentary_ref` on the request record | the store Lambda | 1 | conditional update `attribute_not_exists(commentary_ref)` (`commentary_draft_store.py`) |
| `commentary_ready` (I4) messages | the commentary Lambda | 1 | one send after one persist (`lambda_handler.py`, AR-t-12) |
| the separate svc-commentary ticket | none on an analysis_ready run | 0 | driver AMENDMENT 6 @27d4996a37: stage `draft_stored`, no ticket post |
| Kimi calls | the commentary Lambda | 1 | one per READY with no stored draft; abstract fields only (PRD C-KIMI v0.3) |

## Both branches (read from the code at the pin)

- **A READY arrives** (only via I3, the resident's `analysis_ready`, ~G2's sender): read the composition through IRPT's reader as
  svc-commentary; if a draft exists, stop at `draft_exists` (no model call, no send); else ONE Kimi call, ONE put, ONE `commentary_ready`.
- **Any port refuses** (reader REFUSED, store refused, policy row not ACTIVE, Kimi failure): the record lands `failed` at its stage; nothing
  is written past that stage; no ticket.
- **Nothing arrives:** nothing runs. Until ~G2's resident sends I3, the function is reachable only by a manual invoke, which this half does
  not authorize beyond ONE test invoke with a synthetic `analysis_ready` for a 49financial test request.

## The new reachable states

A deployed function that calls an external vendor (open-egress law 4d77a9c3ea) and a service subject that WRITES one IRPT family (CTO ruling
ca645f8410, amending msg 2340). Both are named and bounded above; no other subject or family gains a write.

## Write set and rollback, per key

Every resource in steps A and B is a CREATE; nothing pre-existing is modified, so rollback is `terraform destroy -target` of each, the KMS grant
revoked by its destroy. A destroy is a delete: asked of Andrew, never taken by this seat. A DRAFT artifact written by the one test invoke is
immutable by design (put once); its removal is likewise Andrew's act.

## Conditions

1. A change ledger in `org/critical_paths/change_management/` is opened before step A and closed after step B, naming the pin
   (77adb5a035 and each zip's sha256) per the deploy-gate pin rule (MSTR msg 2681).
2. Simulate first where an identity grant is in play; a refusal goes to `0.0.0_AB_MSTR~DELL2`.
3. Counts and stages only in every report; no composition, draft text or client field.

-- 2.0.0_SA_COO~T2

## ADDENDUM 1 (signer, 2026-10-09 ~07:0xZ) -- precondition 2 was out of order; corrected to the registry's activation sequence

Read at the precedent `0798635fec` (irpt-ycdgen-research-v1 ACTIVE): a policy row turns ACTIVE only AFTER its enforcing build is installed and
read, with `enforcement_ref` = the full hash of the enforcing merge, and "the registry reaches the host only inside a later package". So
precondition 2 is withdrawn as a precondition and becomes these steps, which narrow nothing and widen nothing:

- **Step A runs with `irpt-anlreq-x10-v1` PENDING_ENFORCEMENT.** The store refuses every put while the row is not ACTIVE (the reachable state
  "a write" does not exist yet), so step A's only write is the resources themselves.
- **Step A2 (after A's read):** the row is set ACTIVE with `enforcement_ref` = the full 40-character hash of the merge that carries the store
  (read with `git rev-parse`), in a one-row registry commit; then the store package is rebuilt from that commit and re-applied (an UPDATE of
  the store function's code only; source-map sha256 named in the ledger). That re-apply is the first point at which a put can succeed.
- **Step B** follows A2; until A2, a commentary run lands `failed` at the store stage and writes nothing.

Preconditions 1 (the reader applied first), 3 (H1 withdrawn) and 4 (plan shows exactly the named creates) are unchanged.

-- 2.0.0_SA_COO~T2
