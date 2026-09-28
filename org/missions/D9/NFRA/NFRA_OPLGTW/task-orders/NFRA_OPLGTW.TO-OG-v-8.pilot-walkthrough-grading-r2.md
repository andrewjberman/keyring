# NFRA_OPLGTW task order -- `OG-v-8` -- ROUND 2 (E2): grading the pilot onboarding walkthrough (re-cut of OG-v-5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-v-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~10</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>GE_RECORD</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a grading read; no cron, alarm, monitor or cadence. HELD on G-E (grant approved by Andrew 2026-09-28; activation through OG-z-2 by an authorized operator, R-7) and G-F (the pilot walkthrough itself).
comp-iam: DECLARED-NOT-APPLICABLE -- reads with existing access.
comp-adversary: DECLARED-NOT-APPLICABLE -- a re-cut of OG-v-5 whose AC1-AC4 are carried verbatim; the judgment text is the analysis's (item E2).
EGRESS CLASS, declared: NONE beyond Opal's own AWS, read-only.
</preflight>

## 1. THE CELL -- `OG-v-8` (decomposition addendum R2-E, item E2)

**Grading the pilot onboarding walkthrough.** The pilot member, the workspace owner and the operator have onboarded the
member's real, administrator-approved grant through the runbook, and the record is at HEAD. You grade it. You perform
none of it, and you activate nothing. Outcomes: FWD-1, FWD-8.

FWD-1, verbatim: *"DONE WHEN: EXERCISED -- a deliberate connection and reconnection walkthrough succeeds. ACCEPT:
Menachem signs in with his work account, asks a Schwab question in Claude, and can continue after signing out and back in
without installing developer software. PROOF: An observed owner-and-member walkthrough, including an expired sign-in and a
fresh connection."* A1: *"Real hosted Claude work-account connect, expiry, refresh, reconnect and logout without CLI."*
A20: *"Owner/member support walkthrough covers connector setting reuse, external-link confirmation, reconnect,
denial/revocation and the Claude chat/retention disclosure ... record tool, UTC timestamp, public connector URL and
sanitized server correlation, plus ofid_ if supplied."*

The two inputs, both required at HEAD before you are handed this order:
- **G-E** `<GE_RECORD>` -- the pilot member's verified `tid`/`oid`, the approved account/date/field grant from the
  identity and data administrator (`0.7.0_AE_CloudOps`, Andrew-direct 2026-09-20 ~18:0xZ, record @`768e6df290`), and the
  activation's operator audit reference. Activation runs through
  `infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py` (`OG-z-2`) by an authorized operator.
- **G-F** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/PILOT_WALKTHROUGH_RECORD.md` -- the owner-and-
  member walkthrough record, in the protocol's section 5.2 template
  (`infra/aws/ec2/opal-gateway/tests/acceptance/WALKTHROUGH_PROTOCOL.md`).

If either is absent, or `<GE_RECORD>` still reads as a token, file a BLOCKING row and stop. The active profile is read,
read-only, from the live `gateway-access-state-table` table's `POLICY#` record and its `operator_audit` records. The
table name is the CONTRACT's (`org/standards/NFRA_OPLGTW_CONTRACT.json` `state_store.table`); if the two ever disagree,
the contract wins and the disagreement is a BLOCKING row.

**The probe** for every mechanical criterion is
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v8.py`, which you write (round 1's
`og_v5.py` was never written). It takes the short id and `--ge <path>`, prints its measurement with its denominator,
then exactly one line `VERDICT: PASS-OGV8-AC<n>` or `VERDICT: FAIL-OGV8-AC<n> <reason>`. Each run finishes inside 110 s.

## 2. BOUNDS

- **Grant.** Your write surface is the `<paths>` block below. A path you need that is not named is a BLOCKING surprise
  row -- never an override.
- **G-E and G-F.** Both records at HEAD, or a BLOCKING row and a stop.
- **You grade; you do not operate.** No activation, no grant change, no sign-in, no connector act. Reads only: the
  records, the one table's `POLICY#` and `operator_audit` records, and the audit sink.
- **No customer data or personal identifier in evidence.** The `tid`/`oid` pair is cited by the G-E record's path, never
  copied into your files.
- **Worktree.** You work in the worktree named in your identity line, after `OG-v-7` merged. Never push, merge, rebase,
  `checkout --` or `clean`.
- **Interpreter.** `.venv-og` as `OG-v-6` built it. Never commit `.venv-og/` or `.scratch/`.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any
  vendor API.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** Anything off-spec is one surprise row, and you keep working.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_OPLGTW-Z-W10-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

Four mechanical criteria: a grading cell carrying OG-v-5's AC1-AC4 verbatim, not a build order.

<proof_of_spec>
  <criterion id="OGV8-AC1" cell_refs="OG-v-8"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v8.py AC1 --ge <GE_RECORD></invocation><expect>(?m)^VERDICT: PASS-OGV8-AC1(?![0-9])</expect></criterion>
  <criterion id="OGV8-AC2" cell_refs="OG-v-8"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v8.py AC2 --ge <GE_RECORD></invocation><expect>(?m)^VERDICT: PASS-OGV8-AC2(?![0-9])</expect></criterion>
  <criterion id="OGV8-AC3" cell_refs="OG-v-8"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v8.py AC3 --ge <GE_RECORD></invocation><expect>(?m)^VERDICT: PASS-OGV8-AC3(?![0-9])</expect></criterion>
  <criterion id="OGV8-AC4" cell_refs="OG-v-8"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v8.py AC4 --ge <GE_RECORD></invocation><expect>(?m)^VERDICT: PASS-OGV8-AC4(?![0-9])</expect></criterion>
  <criterion id="OGV8-J1" cell_refs="OG-v-8" judgment="true"/>
</proof_of_spec>

- `OGV8-AC1` -- the pilot member's profile is active at the revision the identity and data administrator approved, by
  `OG-z-2`'s audit record.
- `OGV8-AC2` -- the active scope equals the administrator's approved account, date and field grant.
- `OGV8-AC3` -- the pilot record covers A1 (connect, expiry, refresh, reconnect, logout) and A20 (owner and member
  support walkthrough), denominator printed.
- `OGV8-AC4` -- every recorded server correlation resolves to a sanitized audit record.
- `OGV8-J1` -- graded at L9 by `3.0.0_SA_CVO~O`: every clause of FWD-1's and FWD-8's ACCEPT sentences has at least one
  line in the record stating what the PERSON OBSERVED (screen, downloaded file, refusal text); server logs and audit
  records never stand in for an observation; PASS only when every ACCEPT clause has an observed line. RECORD; NO VERDICT.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/NFRA_OPLGTW.TO-OG-v-8.pilot-walkthrough-grading-r2.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>` BEFORE the `complete` flip. The judgment row is
`UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO~O` at L9. Result file `pilot-walkthrough-grading-r2.result.md`. Flip
`complete` only when every MECHANICAL criterion PASSES by output. Report once, in your final message.

<!-- ===================== RECORD FACE ===================== -->

**What changed from `OG-v-5`, exactly:** (1) G-E's grant is approved (R-7); the G-E path is no longer pinned to
`1.0.0_SA_CTO~A/` (the pin was round 1's seal reason, row S54, and E2 has no seal) -- it becomes `<GE_RECORD>`, filled at
hand-off from the G-E record's committed path. (2) `OGV5-J1` is REPLACED by the round's observed-line judgment text and
widened to FWD-8, matching the outcomes. (3) AC1-AC4 carried; ids renumbered to `OGV8-*`. (4) The probe is written by
this cell: round 1 never wrote `og_v5.py`.

**OPEN AT HAND-OFF -- the pilot member's identity (Andrew-direct G-ASKER, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_212xZ_O_FABRIC_OPEN_CALLS_ANSWERED.md` @7bfa5811c6, call
1):** Menachem is DEFERRED (his Claude desktop app would need its own MCP hookup); Alyssa runs the close-run tests with
the SAME entitlements as Menachem's approved G-E grant, AFTER Andrew's own speed and efficacy test, and her grant does not
widen before that. The FWD-1 text quoted above names Menachem; at hand-off the issuer re-reads the G-E record and states
in the hand-off whose walkthrough G-F records. A change of subject that moves an ACCEPT clause is a question for
`1.0.0_SA_CTO~O`, never the worker's.

Seating: slot ~10, queue position 3, handed after `OG-v-7` merges AND G-E and G-F are at HEAD.

<status>staged</status>
<round>3</round>
<slot>~10</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
