# NFRA_MCPMSP task order -- `MS-sg-1` -- ROUND 2, E2: the gateway sender gate in full (domain AND tenant, guest form, pilot scope)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-sg-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~3</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant; the gate reads Graph through the calling identity's existing token.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named refusal tests are the adversary read.
EGRESS CLASS, declared: none (tests use fakes; Graph is Opal's existing delegated path).
</preflight>

## 1. THE CELL -- `MS-sg-1` (decomposition v2, R2.2; PRD C3/C4)

Andrew's allowed sender domains, verbatim: `opalinvest.com`, `49financial.com`, `inflectionwealth.com`,
`cottonwoodmail.com`. A message is served only when its sender's address is in an allowed domain AND the sender's tenant
is registered to the firm that domain belongs to (`opalinvest.com` = Opal's own tenant). The domain comes from the
sender identity, never the message text. A guest-form address (`...#EXT#@...`) is refused. For the pilot, an
`opalinvest.com` or `49financial.com` sender is refused `asker_pilot_scope` -- but ONLY when the CALLING identity (the
gateway user making the tool call) is listed in env `MSP_CALLING_IDENTITIES` (comma-separated emails, EMPTY by default:
empty moves no Opal-staff serving; CTO ruling 27416). Every refusal leaves ONE `asker_sender_refusal` audit entry with
`sender_email` and `sender_domain` added (C4: never the message text).

Today, in `infra/aws/ec2/opal-gateway/app/asker_scope.py`: `handle_asker_query` (`:299`) resolves the sender principal
(tid/oid) and display name from the message (`_resolve_message_full` `:155`), refuses an unregistered tenant
`asker_tenant_denied` with one `SENDER_REFUSAL_TOOL` entry (`:334-338`), and reads chat members via
`read_chat_members(token, chat_id, graph_call)` (`:261`, Graph `GET /chats/{id}/members`). No domain check exists.

Build:
1. **`app/sender_gate.py` (new):** `ALLOWED_DOMAINS` (the four, mapped to firm: opalinvest.com -> Opal's own tenant,
   49financial.com -> 49financial, inflectionwealth.com -> inflection, cottonwoodmail.com -> cottonwood);
   `sender_address(members, sender_oid)` = the `email` of the member whose `userId` equals the sender oid (None when
   absent); `check(address, tenant_class, calling_email)` -> `None` (pass) or a refusal code:
   `asker_sender_domain` (no address, domain not allowed), `asker_sender_guest` (`#EXT#` in the address),
   `asker_sender_tenant_mismatch` (domain's firm != the tenant's registered firm/class), `asker_pilot_scope`
   (opalinvest.com / 49financial.com when `calling_email` is in `MSP_CALLING_IDENTITIES`, read with `os.environ` at call
   time -- do NOT edit `app/config.py`).
2. **`app/asker_scope.py`:** after the tenant is resolved, read the members (the one-on-one path too -- the sender's
   address comes from the member list), run `sender_gate.check`, and on a refusal write ONE `SENDER_REFUSAL_TOOL` entry
   with round 1's fields plus `sender_email`, `sender_domain` and the code, then return `_denial(code, reason)`. The
   existing `asker_tenant_denied` entry also gains `sender_email`/`sender_domain` where resolvable. Everything else
   unchanged.
3. **`app/audit.py`:** `_ARGS_ALLOWLIST["asker_sender_refusal"]` adds `sender_email`, `sender_domain`.
4. **`tests/test_mcpmsp_sender_gate.py` (new)** with at least: `test_allowed_domain_matching_tenant_served`,
   `test_domain_not_allowed_refused_and_logged`, `test_domain_tenant_mismatch_refused`, `test_guest_form_refused`,
   `test_opal_sender_refused_only_for_msp_calling_identity`, `test_refusal_entry_has_sender_email_domain_no_text` (fakes
   in the style of `tests/test_mcpmsp_asker_firm.py`; audit to a temp `AUDIT_PATH`).

## 2. BOUNDS

1. Write surface: exactly the `<paths>` below. `query_v0.py`, `config.py`, `internal_role.py`, `admin_*` are others'.
2. The existing asker/adapter suites must stay green (AC2). No push, no vendor call. REFUSE a criterion you cannot meet.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/sender_gate.py
infra/aws/ec2/opal-gateway/app/asker_scope.py
infra/aws/ec2/opal-gateway/app/audit.py
infra/aws/ec2/opal-gateway/tests/test_mcpmsp_sender_gate.py
infra/aws/ec2/opal-gateway/tests/test_asker_binding.py
infra/aws/ec2/opal-gateway/tests/test_asker_nochannels.py
infra/aws/ec2/opal-gateway/tests/test_asker_scope.py
infra/aws/ec2/opal-gateway/tests/test_mcpmsp_asker_firm.py
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~3/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/**` (others), `infra/aws/ec2/opal-gateway/tests/`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W3-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-sg-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e2g.AC1.sh; echo "exit=$?"</invocation><expect>pytest: N passed, 0 failed; each of the six named tests >=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-sg-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e2g.AC2.sh; echo "exit=$?"</invocation><expect>asker + adapter + round-1 suites: >=48 passed, 0 failed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MS-sg-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e2g.AC3.sh; echo "exit=$?"</invocation><expect>asker_sender_refusal allowlist includes chat_id display_name oid reason tid sender_email sender_domain; text_fields=[] verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~3/NFRA_MCPMSP.TO-MS-sg-1.gateway-sender-gate.proof_of_spec.json`.
Report once, with: the refusal codes; the three check lines; the commit hash; any row.

## AMENDMENT 1 (issuer, 2026-10-01 ~01:0xZ, on your row NFRA_MCPMSP-Z-W3-S3)

Your refusal of AC2 is upheld: an absent sender address stays REFUSED (`asker_sender_domain`) -- the gate never fails
open. The defect is the four suites' Graph fakes, which return chat members with no `email` (real Graph
`GET /chats/{id}/members` carries it). Your write surface grows by exactly those four test files (added to `<paths>`
below); in each, give every faked member an `email` in the allowed domain that matches its tenant (Opal's tenant ->
`...@opalinvest.com`; a registered partner tenant -> that firm's domain; an unregistered-tenant member -> any address),
and change NO assertion. AC2 is unchanged (>= 48 passed, 0 failed). Your row Z-W3-S4 (firm ids derived from
`catalog_gate.KNOWN_FIRMS`, pinned by `test_allowed_domain_matching_tenant_served`) is accepted as built. First
`git merge CLOUD` in your worktree to pick up this amendment; then re-run AC1-AC3, rewrite the proof instance, and append
the status flip to complete as the LAST status tag only when all three pass.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 issuance (E2; CTO ruling 27416 -- `MSP_CALLING_IDENTITIES` empty by default). Checks dry-run
at base: AC1 FAIL as expected (test absent); AC2 PASS as expected (48 passed, control); AC3 FAIL as expected (allowlist
lacks sender_email/sender_domain). AC3 is the third mechanical criterion: C4's record fields, a contract the tests
alone do not pin in the allowlist.

<status>pending</status>
<round>2</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
