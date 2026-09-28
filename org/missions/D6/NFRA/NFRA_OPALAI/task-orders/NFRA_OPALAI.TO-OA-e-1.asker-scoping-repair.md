# NFRA_OPALAI task order -- `OA-e-1` -- ROUND 2, E1: the asker-scoping repair (asker AND caller gate, message binding, group chats)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-e-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~10</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the chat-members read uses the concierge's EXISTING delegated Graph token; AC2 reads SSM and DynamoDB through the operator's existing access. No IAM surface is written.
comp-adversary: DECLARED-NOT-APPLICABLE -- the three negative arms (AC1) and rule J's judgment on OA-r-1 are the adversary read (decomposition R2.5).
EGRESS CLASS, declared: AWS READ on Opal's own plane (one SSM read of the host's TENANT_ID line, one DynamoDB scan, counts only). Development downloads are covered by Andrew-direct record @f8d1103a38; moto is already installed at C:/tmp/moto-target (G-MOTO GIVEN). No vendor call.
</preflight>

## 1. THE CELL -- `OA-e-1` (round 2, decomposition section R2.1)

The gateway tool `opal_asker_query` (`infra/aws/ec2/opal-gateway/app/tools.py:890`, body
`app/asker_scope.py:137 handle_asker_query`) answers a colleague's Teams question scoped to the ASKER, the sender of
the message it reads. It has three holes, and this cell closes all three in ONE change, because they all sit in that
one function and its send-side partner.

**(a) The catalog verdict is `gate(asker) AND gate(calling identity)`** (CTO ruling I-1). Today `asker_scope.py:181-182`
evaluates `catalog_gate.gate(...)` on the CALLING identity only (`query_v0._principal(calling_email)`).
- Add `resolve_asker_class(tid: str) -> Optional[tuple[str, str]]` to `asker_scope.py`. It returns
  `(catalog_gate.OPAL_INTERNAL, "")` when `tid` is Opal's own tenant, and `None` for any other tenant or an unparseable
  one. Resolve "Opal's own tenant" with the EXISTING `context.tenant_authorized(tid)` (`app/context.py:72`, which
  reads the configured `TENANT_ID`); do not add a second tenant constant. There is no tenant-to-firm registry, so no
  firm is ever returned. Never derive the class from the profile's `email` field (display only).
- In `handle_asker_query`: when `resolve_asker_class` returns `None`, refuse with code `asker_tenant_denied` BEFORE
  any catalog lookup. Otherwise evaluate `catalog_gate.gate` on the asker's class and firm AND on the caller's, and
  serve only when BOTH admit. Neither may widen the other.

**(b) The cited message is bound** (row Z-S5).
- `resolve_asker` (`asker_scope.py:100`) also selects `createdDateTime`. A message older than
  `ASKER_MESSAGE_MAX_AGE_SECONDS` is refused with code `asker_message_stale`. That constant is read in
  `asker_scope.py` as `int(os.environ.get("ASKER_MESSAGE_MAX_AGE_SECONDS", "900"))`, so config can override it with no
  `config.py` edit. A message with no parseable `createdDateTime` is refused.
- Reply binding: after `handle_asker_query` SERVES data for chat C, record `(calling email, OAuth client_id) -> (C,
  served_at)` in an in-process store in `asker_scope.py`. The host runs `GATEWAY_WORKERS=1`, so one process holds it.
  Read the client_id with the existing `context.get_current_client_id()`.
- `send_chat_message` (`tools.py:781`) and `send_channel_message` (`tools.py:827`) refuse any target that is not C
  while that binding is younger than `ASKER_MESSAGE_MAX_AGE_SECONDS`. The refusal is code `asker_reply_unbound`, is
  audited through `audit.log_call`, and makes NO Graph POST.
  - A channel target is never C. C is a chat id.
  - With no live binding, both send tools behave exactly as today.

**(c) Group chats: the scope is the intersection over every human member.**
- Read the chat's `chatType` (`GET /chats/{chat_id}`, `$select=chatType`). For `oneOnOne`, today's single-sender path
  stands.
- For any other type, read `GET /chats/{chat_id}/members` with the same delegated token. Take every member that
  carries a `userId` and a `tenantId`, EXCLUDING the calling identity itself (`context.get_current_principal().oid`).
  Each such member must:
  - resolve through (a);
  - hold an active profile and grant with the `query` operation.
- One member that fails refuses the WHOLE query, with code `asker_group_member_denied` and no data read.
- When every member passes, the effective `portal_channels` is the intersection of their grants. A grant with no
  `portal_channels` does not narrow, exactly as `asker_scope.py:190-197` treats it today.

**Tests** (fakes only: a fake `graph_call` and `acs.AccessState(client=<fake table>)`, as `tests/test_asker_scope.py`
already does; no network). Write them in the NEW file `tests/test_asker_binding.py`, with EXACTLY these four names:
- `test_old_message_from_wider_person_refused`: a profiled, wider person's message older than the window is refused
  `asker_message_stale`, and no fetch runs;
- `test_reply_to_other_chat_refused`: after a served query for chat C, `send_chat_message` to chat D is refused
  `asker_reply_unbound`, and the fake Graph sees no POST;
- `test_group_chat_unprofiled_member_refused`: a group chat with one member who has no profile is refused
  `asker_group_member_denied`, and no fetch runs;
- `test_same_chat_recent_message_served`: the POSITIVE arm. A recent message from a profiled Opal-tenant asker in a
  one-on-one chat is served, and a reply to that same chat is not refused by the binding.

Add more tests beside them as you need. `tests/test_asker_scope.py` must keep passing, and you may extend it.
AMENDED (row Z-W10-S2): `tests/test_portal_grant.py`'s two asker tests
(`test_asker_portal_scope_admits_granted_channel`, `test_asker_portal_scope_refuses_other_channel`) build a fake
message with a foreign tenant and no `createdDateTime`, so your (a) and (b) now refuse them before the channel check
they exist to test. Update ONLY their fixtures (the configured tenant, a recent `createdDateTime`, a `oneOnOne`
chat) so each again reaches and asserts the portal-channel verdict it was written for. Never change an assertion.

**R-5 (row Z-W8-S1).** Run `tests/test_data_entitlement_guard.py` with moto from `C:/tmp/moto-target`, from
`infra/aws/ec2/opal-gateway`:
```
PYTHONPATH="C:/tmp/moto-target;." python -m pytest tests/test_data_entitlement_guard.py -q
```
At the round-2 cut this read exactly 10 passed and 2 failed: `test_ogz1_ac05` (KeyError `'unclassified'`) and
`test_ogz1_ac08` (the route-class set). Both are recorded in row NFRA_OPALAI-Z-S36 and neither is yours. Do NOT fix
them. Your change must add no new failure and must not change that failed set.

## 2. BOUNDS

1. No other tool's gate, policy record, grant, or the legacy path of existing tools changes. No `app/audit.py`,
   `app/identity_scope.py` or `app/config.py` edit. The concierge seed is NOT widened here; that is OA-e-3's.
2. Nothing is deployed. The release is OA-r-1, a separate order.
3. The Graph members read may be refused by the token's scopes. If so, STOP on (c), file a BLOCKING row with the Graph
   error, and never widen a permission.
4. Standing: no push, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal with its
   measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/asker_scope.py
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/tests/test_asker_scope.py
infra/aws/ec2/opal-gateway/tests/test_asker_binding.py
infra/aws/ec2/opal-gateway/tests/test_portal_grant.py
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~10/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `app/context.py`, `app/query_v0.py`, `app/graphql_plumbing/catalog_gate.py`,
`app/data_entitlement.py`, `app/access_state.py`, `app/graph.py`, `tests/test_data_entitlement_guard.py`.

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W10-S<k>` (next free k for W10; none exist at the cut, so the first is S1).

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-e-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e1.AC1.sh; echo "exit=$?"</invocation><expect>named arms passed 4 of 4; failed/errored tests 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-e-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e1.AC2.sh; echo "exit=$?"</invocation><expect>host TENANT_ID read=yes (ssm status Success); active profiles=N>0 resolved opal-internal=N; foreign tenant -> None -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-e-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e1.AC3.sh; echo "exit=$?"</invocation><expect>moto from C:/tmp/moto-target: 5.2.3; passed>=10; failed=[test_ogz1_ac05 test_ogz1_ac08]; new failures=[] -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~10/NFRA_OPALAI.TO-OA-e-1.asker-scoping-repair.proof_of_spec.json`.
Report once:
- what you changed, with file:line;
- the value of the window;
- the commit hashes (OA-r-1 cherry-picks exactly these);
- the three negative arms' and the positive arm's pytest lines;
- the R-5 counts;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E1 (I-1 + Z-S5) + R-5 (Z-W8-S1). WORLD by the infra floor; the build itself deploys nothing.
AC1 is the built behaviour, AC2 the seam against the live host's tenant and the live policy store, and AC3 the R-5
no-regression bound.

SPAWN ONLY WHEN: at the cut. G-MOTO is GIVEN (Andrew-direct record @f8d1103a38; moto 5.2.3 at `C:/tmp/moto-target`).
The slot continues with OA-r-1, then OA-e-3, then OA-e-9.

Dry-run at base (CLOUD `c8df03c408`, ~20:5xZ):
- e1.AC1 base: FAIL as expected (`tests/test_asker_binding.py` absent).
- e1.AC2 base: FAIL as expected (host TENANT_ID read=yes, ssm Success; `asker_scope.resolve_asker_class` absent).
- e1.AC3 base: PASS as expected. It is a no-regression bound: moto 5.2.3, 10 passed, failed=[test_ogz1_ac05
  test_ogz1_ac08], row Z-S36 @3c61dbe4d3.

**AMENDMENT (2.0.0_SA_COO~AI, issuer licence, ~22:1xZ):** `<paths>` gains tests/test_portal_grant.py (row Z-W10-S2); e1.AC1's matcher accepts `tests\` or `tests/` (row Z-W10-S1). The served base at the cut is `6a98a0553a`, not `fe94911257`, and the base resolution gains the .env key-set tie-break
(row Z-S38). No criterion's expectation moves. Gate limb: to-pipeline-gate grades a MODIFIED order only on GATE (viii)
placeholders (NONE), so no limb graded this amendment.

<status>pending</status>
<round>2</round>
<slot>~10</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
