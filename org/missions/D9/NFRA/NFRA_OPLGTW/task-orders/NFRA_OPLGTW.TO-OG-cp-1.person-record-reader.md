# NFRA_OPLGTW task order -- `OG-cp-1` -- the gateway reads MC Portal's per-person `person_access` record from the grant store (PRD v2.9 C-PERSON)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-cp-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cp-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~94</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code, offline tests and the contract text only; the reader reaches the host only through a later gateway apply order, cut when this cell drains and queued after the OG-bd-3 release (CTO msg 33954 order: r30, then the tier fix, then this).
comp-iam: RUN-BY-ISSUER at the cut -- the ONE AWS call the new code makes is `dynamodb:GetItem` (ConsistentRead) on `gateway-access-state-table`, key pk `POLICY#<tid>#<oid>` / sk `person_access`, through `access_state.AccessStateStore.get`. The gateway role `opal-gateway-role` already holds `dynamodb:GetItem` on that table UNCONDITIONED (statement `AccessStateStrongRead`, `infra/aws/terraform/opal-gateway/schwab_access_state.tf:96-99`), so no grant changes. The reader writes nothing.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is `1.0.0_SA_CTO~Z`'s PRD v2.9 C-PERSON (`prd/NFRA_OPLGTW_PRD.md:1045-1066` @e5e2ce91ec), msg 33954, and correction msg 33958; NFRA_MCPORTAL C18 (`org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md:591-606`).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-cp-1` (decomposition addendum R3-T.49 A3)

PRD v2.9 C-PERSON, verbatim (`prd/NFRA_OPLGTW_PRD.md:1051-1060`):

- "`decide()` reads a person's per-person record from `gateway-access-state-table`. MC Portal C18 writes it, through
  the ONE existing grant writer."
- "The deploy-time files (`identity_tool_allowlist.txt`, the `deploy-to-ec2.sh` rosters) stay the FLOOR. A record narrows
  what the floor admits for that person. It widens only to a tool the floor already lists for some principal, and never
  to a tool the deployed gateway does not serve."
- "A record is honoured on that person's next call."
- "With no record present, behaviour is exactly as today: the floor governs."
- "The Opal-users-only gate (v2.3 item 4), the C2 owner gate and tier admission (msg 33940) are unchanged and evaluated
  first. A record can never admit a non-Opal principal."

CTO correction msg 33958: "A per-person record CAN widen a person to a tool the floor already lists for SOME principal, and
can narrow anything. It never admits a tool the deployed gateway does not serve, and never admits a non-Opal principal."

You build the READER and define the record kind. The writer is NFRA_MCPORTAL's (F2), and it is out of this cell. Every
design choice below is decided; do not re-decide any of it.

1. **The record kind (contract first).** Add `person_access` to the closed POLICY record set in three places that must
   agree:
   - `org/standards/NFRA_OPLGTW_CONTRACT.json` `state_store.record_types`;
   - its byte copy `infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json` (the two files stay byte-equal);
   - `app/access_state.py` `POLICY_RECORD_TYPES`.

   Key: `access_state.policy_key(tid, oid, "person_access")`, i.e. pk `POLICY#<tid>#<oid>` and sk `person_access`, one
   record per person and no revision part, like `principal_profile`. Add `state_store.person_access` to both contract
   copies:

   ```
   {"key": "POLICY#<tid>#<oid> / person_access",
    "writer": "the one grant writer (NFRA_MCPORTAL C18); Andrew-only writes (C2)",
    "fields": {"status": "active | revoked", "revision": "int >= 1", "stopped": "bool (default false)",
               "tools_allow": "[tool name]", "tools_deny": "[tool name]",
               "channels_allow": "[channel id]", "channels_deny": "[channel id]",
               "updated_at": "ISO-8601 UTC", "updated_by": "principal hash"},
    "channel": "the tool's integration id from app/integrations/registry (_ACTIVE_BY_TOOL); 'native' for a tool defined in app/tools.py",
    "rule": "PRD v2.9 C-PERSON"}
   ```

   No tier field. Tier records are out of this cell (open question 2 on the record face); tier keeps coming from the
   rosters. Update `tests/test_access_state.py` `test_ogd1_ac03`: the POLICY count moves 5 -> 6, and its comment names
   `person_access`.
2. **The read.** In `app/data_entitlement.py`, add `person_access(principal)`. It returns:
   - `None` when no record exists, or when the record's `status` is not `active`. Behaviour is then exactly today's.
   - Otherwise an object holding the four sets.

   The read is ONE strong `AccessStateStore.get` (already `ConsistentRead=True`), within the same request memo pattern
   `remember_allowed` uses. **Fail closed:** a get that raises, or a record whose fields do not parse (a non-list set,
   non-string names, missing `status` or `revision`), means the person's record is UNAVAILABLE. It is never read as "no
   record". This is the module's existing rule ("store unavailable / record bad -> denied", `entitlement_unavailable`),
   carried to the new kind with code `person_record_unavailable`.
3. **Evaluation order** (C-PERSON: the existing gates first and unchanged):
   - (a) **Unchanged and first:** the Opal-users-only gate, the C2 owner gate, tier admission (OG-bd-3) and `decide()`'s
     data-grant rules. A denial from any of them is NEVER overridden by a record. The data grants are not "the floor";
     the floor is the deploy-time files.
   - (b0) **STOP (2.0.0_SA_COO~MP msg 33963; MCPORTAL FWD-21 DONE WHEN "the person stopped and restored"):** an active
     record with `stopped: true` denies EVERY tool to that principal, the master_admin included, code
     `person_record_denied`. It is checked first among the record rules, and it is a narrowing, so "can narrow anything"
     covers it. Restoring the person is `stopped: false` (or revoking the record, which returns the floor).
   - (b) **NARROW:** for ANY principal, the master_admin included ("can narrow anything"), an active record denies a
     tool in `tools_deny`, or a tool whose channel is in `channels_deny`. Code `person_record_denied`. Apply it in
     `tool_denial` (so `_run` and `call_tool` refuse) and in `visible_tools` (so the listing drops it). Deny wins over
     allow.
   - (c) **WIDEN, only at the identity-scope floor:** where `identity_scope.check(email, tool)` denies
     (`identity_scope_denied`, the call site in `app/tools.py` `_run` about line 145), an active record admits the tool
     only if ALL of these hold:
     - the tool is in `tools_allow`, or its channel is in `channels_allow`;
     - the tool is SERVED: a name registered in this process, i.e. a native tool or `registry._ACTIVE_BY_TOOL`. "The
       floor already lists for some principal": an unscoped principal's floor is every served tool;
     - the caller is an Opal principal (`tools._is_opal_user(email)`).

     Otherwise the identity-scope denial stands. An allow-name the gateway does not serve admits nothing, and
     `person_access_view(principal)` reports it under `ignored_unserved`.
   - (d) **Non-Opal principal:** widening is ignored entirely, and narrowing is still honoured.
4. **Audit.** When a record changes a decision (narrowed or widened), the call's audit `detail` carries
   `person_record_rev=<revision>`, through the existing `audit.log_call`. Write no new audit record.
5. **Tests,** in `infra/aws/ec2/opal-gateway/tests/test_og_cp1.py`, offline, with the store stubbed (record every call):
   - `test_ogcp1_ac01`: no record, and a `revoked` record, give answers identical to today for one floor-allowed tool, one
     identity-scope-denied tool and one data-grant tool.
   - `test_ogcp1_ac02`: `tools_deny` and `channels_deny` each deny a tool the floor admits, for a standard principal AND a
     master_admin; the tool is absent from `visible_tools`; code `person_record_denied`. And a `stopped: true` record
     denies every tool (a floor-allowed one, a data-grant one and a tier tool) for a master_admin; setting it back to
     false restores today's answers.
   - `test_ogcp1_ac03`: for a SCOPED Opal identity, `tools_allow` admits a served tool its allowlist lacks, and
     `channels_allow` admits a served tool of that channel. Deny beats allow when both name the tool.
   - `test_ogcp1_ac04`: `tools_allow` naming a tool the gateway does not serve admits nothing, and it appears in
     `ignored_unserved`.
   - `test_ogcp1_ac05`: a non-Opal principal with a record that allows a tool is NOT admitted, and its `tools_deny` still
     denies.
   - `test_ogcp1_ac06`: a get that raises, and a malformed record, each give `person_record_unavailable` (never today's
     answer). The data-grant and Opal-only denials still precede it.

## 2. BOUNDS

- The files in `<paths>` only. No release, deploy, grant, record or IAM write. Write no `person_access` record anywhere
  real.
- Change no rule of the existing gates (Opal-only, C2, tier, data grants), and no existing test's expectation except
  `test_ogd1_ac03`'s count.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/access_state.py
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/integrations/base.py
infra/aws/ec2/opal-gateway/tests/test_og_cp1.py
infra/aws/ec2/opal-gateway/tests/test_access_state.py
infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json
org/standards/NFRA_OPLGTW_CONTRACT.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only inputs: `app/identity_scope.py`, `app/integrations/registry.py`, `app/audit.py`, `tests/test_og_bd2.py`,
`tests/test_og_bd3.py`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~94/`. Rows: id `NFRA_OPLGTW-Z-W94-S<k>`, fabric
`site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cp-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/cp1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 7 of 7; failed/error lines 0.*contract parity test_ogd1_ac03: rc=0; 1 passed: yes.*failing ids not in the baseline: 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cp-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/cp1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)contract copies byte-equal: yes; person_access in record_types 1 time\(s\) \(want 1\).*person_access fields declared 8 of 8; missing \[\]; tier field present: no.*POLICY_RECORD_TYPES carries person_access: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the reader narrows, widens only to served tools for Opal principals, fails closed, and changes nothing when no
  record exists.
- `AC2`: the record kind is one contract everywhere it is read.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cp-1.person-record-reader.proof_of_spec.json`. Validate it after your last
commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`. Flip the ONE
`<status>` tag to `complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- PRD v2.9 C-PERSON @e5e2ce91ec; CTO msgs 33954 (cut the reader after r30 and the tier fix) and 33958 (a record can widen
  to a floor-listed served tool, never a non-Opal principal). NFRA_MCPORTAL F2 (the writer) waits on this reader.
- Release: a later gateway apply order, cut when this cell drains, queued behind the OG-bd-3 release.
- Same write surface as OG-bd-3 (`data_entitlement.py`). This cell is cut from HEAD after OG-bd-3 drained (@42f31eea0a),
  so the two never race.
- Measured at the cut: `AccessStateStore.get` is `ConsistentRead=True` and raises on an unavailable store
  (`app/access_state.py:345-356`). The gateway role's `dynamodb:GetItem` is unconditioned (`schwab_access_state.tf:96-99`).
  The contract copies are byte-equal (`cmp`). `test_ogd1_ac03` pins `{"POLICY": 5, "RUNTIME": 6}`.
- Pre-cut dry runs:
  - cp1.AC1 base: FAIL as expected (`tests/test_og_cp1.py` absent). Control limbs: test_ogd1_ac03 1 passed; bd2+bd3+family+
    guard+admin 0 new failing ids. Elapsed 22 s.
  - cp1.AC2 base: FAIL as expected (`person_access` absent from contract and code). Control limb: copies byte-equal yes.
- OPEN QUESTIONS, decided provisionally in the face; the issuer confirms or amends before the spawn:
  1. **Round placement.** PRD :1062 says the reader is cut "in the round after r30 and the tier-admission release". This
     face is cut in round 37 (workstream R37-PERSON) per the issuer's directive. If the CTO's text governs, it moves to
     round 38.
  2. **Tier records.** C-PERSON says "per-person tool, channel and tier records", but no text says how a tier record
     narrows or widens (a master_admin tier written from the panel is an admin-power widening). This face leaves tier
     OUT and keeps the rosters. A ruling is needed before any tier field.
  3. **Naming.** C18 says "any new store key or name is `lib/opal_naming.py` output", but `opal_naming.py` builds AWS
     resource names and S3 addresses only, and has no record-type builder. The literal `person_access` follows the
     existing closed tuple's hand-named types. A ruling is needed if the CTO reads rule 30 as reaching sort-key literals.
  4. **Who owns the shape.** The field names above are this cell's. NFRA_MCPORTAL F2 writes to them, so
     `2.0.0_SA_COO~MP` should see the shape before F2 is cut.


- A1 (issuer, 2026-10-15 ~03:4xZ): ISSUED. The four open questions are decided: (1) round 37, workstream R37-PERSON, in parallel with the Friday-set releases (CTO msg 34240-era sequencing: the release is a later gateway order after `OG-ap-20`); (2) tier records stay OUT, the rosters keep the tier; (3) the sort-key literal `person_access` follows the existing hand-named tuple; (4) the record shape is sent to `2.0.0_SA_COO~MP` with the issuance (their F2 writes to it). The slot is ~94. Gate limb: GATE (viii) on the issued order (placeholders NONE).

- A2 (issuer, 2026-10-15 ~04:1xZ, worker row Z-W94-S1): the worker built the reader and the native-tool widening, and found a SECOND identity-scope floor in `app/integrations/base.py` (the `_scope_check` block of the integration call path, about line 156) outside its `<paths>`: without it the widening reaches native tools only and every integration tool or channel stays `identity_scope_denied`, which defeats `channels_allow`. Ruled: `app/integrations/base.py` joins `<paths>`. At that block, where `_scope_reason` is set, call `data_entitlement.person_widens(tool, get_current_principal(), _is_opal_user(email))` exactly as `tools._run` does; a revision admits the call past THIS floor only (every later gate - min_tier, credential, egress - is unchanged), and the revision rides the call's audit detail as `person_record_rev=<n>` on the ok and error paths; None keeps today's denial. Add `test_ogcp1_ac07` (offline): an Opal principal with `channels_allow` for an integration channel is admitted past the integration floor, `tools_deny` beats it, a non-Opal principal is not admitted, a read that raises admits nothing. cp1.AC1 reads 7 of 7. The order is reopened to pending and the slot re-seated. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<workstream>R37-PERSON</workstream>
<slot>~94</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
