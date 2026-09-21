# TO NFRA_OPLGTW.TO-OG-v-5 -- grading the pilot onboarding walkthrough

<to_id>NFRA_OPLGTW.TO-OG-v-5</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~6</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-v-5` | **outcome_ref:** FWD-1, FWD-8 | **depends_on:** `OG-v-4`; **HELD on gates G-E and G-F** | **slot:** ~6, queue position 5

---

## WORKER FACE

### THE CELL

`OG-v-5` -- **grading the pilot onboarding walkthrough.** Menachem, the workspace owner and the operator have onboarded
Menachem's real, administrator-approved grant through the runbook, and the record is at HEAD. You grade it. You perform
none of it, and you activate nothing.

FWD-1, verbatim: *"DONE WHEN: EXERCISED -- a deliberate connection and reconnection walkthrough succeeds. ACCEPT:
Menachem signs in with his work account, asks a Schwab question in Claude, and can continue after signing out and back in
without installing developer software. PROOF: An observed owner-and-member walkthrough, including an expired sign-in and a
fresh connection."* A1: *"Real hosted Claude work-account connect, expiry, refresh, reconnect and logout without CLI."*
A20: *"Owner/member support walkthrough covers connector setting reuse, external-link confirmation, reconnect,
denial/revocation and the Claude chat/retention disclosure ... record tool, UTC timestamp, public connector URL and
sanitized server correlation, plus ofid_ if supplied."*

The two inputs, both required at HEAD before you are spawned:
- **G-E** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-E_PILOT_IDENTITY_AND_GRANT.md` -- Menachem's
  verified `tid`/`oid`, the identity and data administrator's approved account/date/field grant (⭐ **that administrator
  is `0.7.0_AE_CloudOps`** -- Andrew-direct 2026-09-20 ~18:0xZ, same record as G-C, @`768e6df290`), and the activation's
  operator audit reference (owner `1.0.0_SA_CTO` -- re-assigned from `1.0.0_SA_CTO~A`, which is not seated,
  by CTO ruling msg 98451 @`a0e4748ac2`, carried here by the issuer under Rule 27; ⛔ the G-E PATH above is
  UNCHANGED and still reads `1.0.0_SA_CTO~A/` deliberately, for the same seal reason as G-C -- row S54;
  activation by an authorized operator through
  `infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py`).
- **G-F** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/PILOT_WALKTHROUGH_RECORD.md` -- the pilot
  walkthrough record, in `OG-v-1`'s template.

If either is absent, file a BLOCKING row and stop. The active profile is read, read-only, from the live
`gateway-access-state-table` table's `POLICY#` record and its `operator_audit`. **THE TABLE NAME IN THIS
SENTENCE WAS `opal-gateway-access-state` UNTIL 2026-09-18 ~12:0xZ AND THAT TABLE NO LONGER EXISTS** -- `OG-i-5`
renamed it and this pending order was never carried forward. The name here is the CONTRACT's
(`org/standards/NFRA_OPLGTW_CONTRACT.json` `state_store.table`), and a `dynamodb list-tables` at amendment time
returned 44 tables of which `gateway-access-state-table` is one and `opal-gateway-access-state` is NOT.
If this name and the contract ever disagree again, the CONTRACT wins and the disagreement is a BLOCKING row.

**The probe** for every mechanical criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v5.py`,
taking the short id, printing its measurement with its denominator, then exactly one line `VERDICT: PASS-OGV5-AC<n>` or
`VERDICT: FAIL-OGV5-AC<n> <reason>`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGV5-AC1" cell_refs="OG-v-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v5.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGV5-AC1(?![0-9])</expect></criterion>
`OGV5-AC1` -- Menachem's profile is active at the revision the identity and data administrator approved, by `OG-z-2`'s audit record.

<criterion id="OGV5-AC2" cell_refs="OG-v-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v5.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGV5-AC2(?![0-9])</expect></criterion>
`OGV5-AC2` -- the active scope equals the administrator's approved account, date and field grant.

<criterion id="OGV5-AC3" cell_refs="OG-v-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v5.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGV5-AC3(?![0-9])</expect></criterion>
`OGV5-AC3` -- the pilot record covers A1 (connect, expiry, refresh, reconnect, logout) and A20 (owner and member support walkthrough).

<criterion id="OGV5-AC4" cell_refs="OG-v-5"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v5.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGV5-AC4(?![0-9])</expect></criterion>
`OGV5-AC4` -- every recorded server correlation resolves to a sanitized audit record.

<criterion id="OGV5-J1" cell_refs="OG-v-5" judgment="true"/>
`OGV5-J1` -- graded at L9 by 3.0.0_SA_CVO: the record meets FWD-1's ACCEPT clause. RECORD; NO VERDICT.

<expected_criteria>OGV5-AC1, OGV5-AC2, OGV5-AC3, OGV5-AC4, OGV5-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **G-E and G-F.** Both records at HEAD, or a BLOCKING row and a stop.
- **You grade; you do not operate.** No activation, no grant change, no sign-in, no connector act. Reads only.
- **No customer data or personal identifier in evidence.** The `tid`/`oid` pair is cited by the G-E record's path, never copied into your files; audit records are read for decisions and correlations only.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off. Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W6-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-v-5`, round 1 (section 3, S10; section 6 G-E, G-F).
<owned_cells>OG-v-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGV5-AC1` .. `OGV5-AC4`, `OGV5-J1` (5). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/NFRA_OPLGTW.TO-OG-v-5.pilot-walkthrough-grading.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGV5-AC1,OGV5-AC2,OGV5-AC3,OGV5-AC4,OGV5-J1` BEFORE the `complete`
flip. Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.** Result file
`pilot-walkthrough-grading.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. This cell is HELD on project gates G-E (owner 1.0.0_SA_CTO, re-assigned from 1.0.0_SA_CTO~A by ruling 98451 @a0e4748ac2; the PRD's runtime input) and G-F (the pilot record, landed by 2.0.0_SA_COO~O).
comp-iam: DECLARED-NOT-APPLICABLE -- this cell reads records, one table record and the audit sink with existing read access; it adds no AWS operation, policy, principal or role.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Amended 2026-09-18 ~12:0xZ by `2.0.0_SA_COO~O`, its issuer, while this order is still PENDING and BEFORE any
worker is spawned on it. ONE CHANGE, a stale live-resource name: the cell text named the access-state table
`opal-gateway-access-state`, which `OG-i-5` renamed. A worker handed this face would have read a table that does
not exist, on the one read that establishes the pilot's active profile, and the failure would have surfaced only
once a person's walkthrough was already done and waiting to be graded. **No criterion was added, removed or
re-cut; no grant changed; the open-order count is unchanged (a modification, never a new order).** Found by this
lane's own gate-precondition check while both walkthrough cells were held -- the check that asks whether a cell's
inputs still resolve, rather than whether its gate is still shut.

Seating: slot ~6, queue position 5, handed after `OG-v-4` merges AND the G-E and G-F records are at HEAD. Round 1 of
NFRA_OPLGTW, issued by `2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1 @8768f46770.
