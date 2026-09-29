# TO NFRA_OPLGTW.TO-OG-g-1 -- G-C evidence: the controlled identity's verified tid/oid and its one approved synthetic grant

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-g-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~OG</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order creates no scheduled producer, no trigger and no pipeline artifact; it writes one principal's POLICY records through a committed operator command and one evidence file.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS operation, policy, principal or role is added or changed. The order USES two existing identities: the `opal-gateway-access-admin` operator role (the only writer of POLICY records, `infra/aws/terraform/opal-gateway/schwab_access_state.tf`) and a reader identity for the strong read-back. Both exist at HEAD.
comp-adversary: DECLARED-NOT-APPLICABLE -- this order adds criteria against gate text (decomposition s.6, G-C) under the CTO's ask (msg 26435), not against ratified PRD text; it re-cuts nothing. PRD v1.1 @c80b5c85b6, both sign-off halves SIGNED and current (prd-signoff status read at the cut).
EGRESS CLASS, declared: Opal's own AWS (the POLICY write and read-back) plus ONE authoritative Entra tenant read of the controlled identity. No vendor API, no other third-party sign-in.
</preflight>

**Directive:** D9 | **Fabric:** site-z | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v1.1 @c80b5c85b6 (ADMITTED, both halves SIGNED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.3 @23b8cf4165 | **Gate:** `G-C` (decomposition s.6; ADDENDUM R2-E.3) | **outcome_ref:** FWD-1, FWD-3 .. FWD-8 (this order serves them only by unblocking `OG-v-7`, the round's E1; it grades none of them)

You are a SESSION seat, not a subagent: read this order at CLOUD HEAD, work and commit in your own worktree, and report
to `2.0.0_SA_COO~O` once, when the order is terminal.

## WHY THIS ORDER EXISTS, AND WHAT IT IS NOT

`G-C` is a project GATE, not a decomposition cell. It holds `OG-v-7` (the controlled-identity walkthrough grading, E1),
which with `OG-v-8` converts this project's build into proof. The gate requires THREE things and only the first is
recorded:

| `G-C` requires | state at this cut | owner |
|---|---|---|
| an authorized identity/data administrator | RECORDED -- Andrew-direct 2026-09-20 ~18:0xZ, *"0.7.0_AE_CloudOps is the admin. Should be the default admin for all testing tasks of cloud projects/workflows/resources."*, record @768e6df290 | `1.0.0_SA_CTO` |
| the controlled identity's **verified `tid`/`oid`** | ABSENT -- this order produces it | `0.7.0_AE_CloudOps~OG` produces; `1.0.0_SA_CTO~O` records |
| an **approved synthetic grant**, recorded | ABSENT -- this order produces it | same |

⛔ **THIS ORDER DOES NOT CLOSE `G-C`.** It produces the EVIDENCE. `1.0.0_SA_CTO~O` writes and closes the gate record at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md` from your evidence
file; those are two different acts and this order performs only the first. ⛔ **AND IT DOES NOT TOUCH THE SWITCH.**
Adding `schwab` to `ENABLED_INTEGRATIONS` is a LATER, SEPARATE act gated on its own never-widen sign-off, under
Andrew-direct ~17:1xZ 2026-09-22 (*"Yes to Schwab"*, record @465d591b25), which authorizes option (A) and nothing wider.
A grant written while the switch is OFF serves nobody, which is exactly why it is safe to write it first.

**The privilege tier today (row `NFRA_OPLGTW-S61`), stated plainly.** `OG-t-1` re-keyed the PERSON tier on `tid`/`oid`
in code (merged @3c58463f8c), but that code is NOT deployed: its release `OG-t-2` is held. The LIVE gateway still
decides MASTER_ADMIN and STANDARD_EMPLOYEE by exact email match. So a controlled identity whose email is on either live
email roster would be privileged today regardless of its grant, and AC2 below reads the DEPLOYED rosters.

## THE ACT

Produce, in one evidence file in this seat's own deliverables folder:

1. **The controlled identity**, verified: its Entra `tid` and `oid` as canonical GUIDs, read from an AUTHORITATIVE
   tenant source, with the instrument named and the read's own output quoted. The identity is a CONTROLLED, non-privileged
   test principal -- ⛔ **NEVER a master-admin address**, and never Andrew's own account: the walkthrough it enables must
   exercise refusal paths, which a master-admin identity cannot demonstrate.
2. **One synthetic grant**, prepared and activated through the committed operator command
   `infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py`, run under the `opal-gateway-access-admin` role. Its scope
   is DERIVED, not invented -- see SCOPE below -- and the derivation is written down beside it.

⛔ **IF THE TENANT ACT IS NOT YOURS TO PERFORM, THAT IS THE ANSWER AND IT IS A GOOD ONE.** If no controlled identity
exists and creating one needs a tenant administrator's interactive act, DO NOT improvise one, do not reuse a real
person's account, and do not widen an existing grant. File a BLOCKING row naming EXACTLY what a human must do, in one
paragraph a non-technical reader can act on, and stop. Andrew is at a console today; a precise ask is worth more than a
workaround.

## SCOPE OF THE GRANT -- derived from the walkthrough it must serve

The grant exists to let `OG-v-7`'s walkthrough run against `OG-v-6`'s version 2 seal. It must therefore cover, and the
evidence file must show the derivation line by line against these sources:

- `infra/aws/ec2/opal-gateway/tests/acceptance/WALKTHROUGH_PROTOCOL.md` section 4 -- the sealed questions RQ2-1 through
  RQ2-7 (7 questions) at the FIXED business dates **D_NEW = 2026-09-25** and **D_PREV = 2026-09-24** (never a fresh
  catalog read). Read at the cut from
  `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/SEALED_EXPECTED_V2.json`:
  - masters `08242234` (SmartX) and `08335338` (BlackDiamond);
  - datasets `dim_balance` (RQ2-2 .. RQ2-6) and `dim_position` (RQ2-1, RQ2-7);
  - dates: 2026-09-25 for every question; 2026-09-24 as well for RQ2-4 (SmartX) and RQ2-5 (BlackDiamond).
  Re-read the seal file at your HEAD; if it differs from this list, the seal is the authority and the difference is ONE
  surprise row.
- the same protocol's person-operated A-rows: section 3 A7 step 3 (one full authorized `download_filtered` for one
  master and date), A7 step 4 (for EACH master, one request with NO business date for its latest qualified date and its
  available dates), and `dim_asset` for the describe journey.
- `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.3 -- `fields`, `forbidden_field_classes`, `grant_date_modes`,
  `operations`, `disabled_operations`. Operations are `list`, `describe`, `query`, `download_filtered` only.
  `download_original` and any write are disabled at the model level and are never requested.

⛔ **BOUND IT SO THE DENIAL CASES STILL EXIST.** `OG-v-7` grades refusals as well as answers, so a grant wide enough to
answer everything destroys the evidence the walkthrough exists to produce. The accounts and columns stay a bounded
subset, and the evidence file NAMES at least one in-scope request that must SUCCEED and one adjacent request that must
be REFUSED, with the reason each way. A scope you cannot justify from the sources above is not in the grant.

## ACCEPTANCE

Six mechanical criteria, above the usual three, for one stated reason: a gate-evidence order with a live write has six
independent failure modes -- identity, non-privilege, validation, live read-back, walkthrough coverage, no secret -- and
none can be dropped without losing the gate's evidence.

Run every invocation from your worktree root, after your commit.

<proof_of_spec>
  <criterion id="GCG1-AC1" cell_refs="OG-g-1"><invocation>timeout 110 python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~OG/probes/og_g1.py AC1</invocation><expect>(?m)^VERDICT: PASS-GCG1-AC1(?![0-9])</expect></criterion>
  <criterion id="GCG1-AC2" cell_refs="OG-g-1"><invocation>timeout 110 python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~OG/probes/og_g1.py AC2</invocation><expect>(?m)^VERDICT: PASS-GCG1-AC2(?![0-9])</expect></criterion>
  <criterion id="GCG1-AC3" cell_refs="OG-g-1"><invocation>timeout 110 python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~OG/probes/og_g1.py AC3</invocation><expect>(?m)^VERDICT: PASS-GCG1-AC3(?![0-9])</expect></criterion>
  <criterion id="GCG1-AC4" cell_refs="OG-g-1"><invocation>timeout 110 python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~OG/probes/og_g1.py AC4</invocation><expect>(?m)^VERDICT: PASS-GCG1-AC4(?![0-9])</expect></criterion>
  <criterion id="GCG1-AC5" cell_refs="OG-g-1"><invocation>timeout 110 python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~OG/probes/og_g1.py AC5</invocation><expect>(?m)^VERDICT: PASS-GCG1-AC5(?![0-9])</expect></criterion>
  <criterion id="GCG1-AC6" cell_refs="OG-g-1"><invocation>timeout 110 python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~OG/probes/og_g1.py AC6</invocation><expect>(?m)^VERDICT: PASS-GCG1-AC6(?![0-9])</expect></criterion>
  <criterion id="GCG1-J1" cell_refs="OG-g-1" judgment="true"/>
</proof_of_spec>

- `GCG1-AC1` -- the evidence file exists at the path named in DELIVERABLE and records the controlled identity's `tid`
  and `oid` as canonical GUIDs, the AUTHORITATIVE instrument that read them, and that instrument's own quoted output. The
  probe prints each field it found against the denominator of fields required, and FAILS on a placeholder, an empty
  value or a value that is not GUID-shaped.
- `GCG1-AC2` -- the identity is NOT privileged on the LIVE gateway: the probe reads the deployed `MASTER_ADMIN_EMAILS`
  and `WRITE_CAPABLE_EMAILS` (and `MASTER_ADMIN_PRINCIPALS` / `WRITE_CAPABLE_PRINCIPALS` where the deployed config
  carries them) and prints the comparison, with the denominator of entries checked. A match either way is a FAIL, not a
  warning.
- `GCG1-AC3` -- the grant candidate PASSES the committed operator command's own validation
  (`schwab_entitlement_admin.py prepare`), and the evidence file carries that command's printed scope diff verbatim. The
  probe re-runs the validation against the recorded candidate rather than trusting the transcript.
- `GCG1-AC4` -- the grant is ACTIVE in the live table, read back with a STRONG consistent read against the principal's
  `POLICY#<tid>#<oid>` keys: profile `status` is `active`, its `grant_revision` names the grant record that exists, and
  the scope read back EQUALS the scope recorded in the evidence file, field by field, denominator printed. ⛔ The
  read-back is the evidence; the command's own success line is not.
- `GCG1-AC5` -- the scope covers what the walkthrough asks: for each of RQ2-1 .. RQ2-7 the probe checks every named
  master, dataset and business date is inside the grant (denominator 7, read from `SEALED_EXPECTED_V2.json` at HEAD, not
  from this text); A7 step 4's no-date request per master is inside it (denominator 2); and A7 step 3's
  `download_filtered` for one master and date is inside it (denominator 1). A gap is a FAIL naming the uncovered request
  -- the walkthrough would otherwise fail for a reason that has nothing to do with the system under test.
- `GCG1-AC6` -- NO SECRET AND NO CUSTOMER VALUE is in any artifact this order commits: the probe scans the evidence file,
  the probe itself and the result file for a token, cookie, client secret, complete URL with a query string, raw account
  identifier or customer amount, and prints the denominator of files scanned. The identity's `tid`/`oid` and the grant's
  scope ARE recordable; a balance, a holding, an account title or a credential is not.
- `GCG1-J1` -- graded at L9 by `3.0.0_SA_CVO~O`: the grant's scope is the NARROWEST that serves the walkthrough, and the
  evidence file's named must-succeed and must-be-refused pair is a real discriminator rather than a restatement.
  RECORD; NO VERDICT.

## DELIVERABLE

- `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~OG/G-C_CONTROLLED_IDENTITY_AND_GRANT_EVIDENCE.md` --
  the evidence, in the shape AC1..AC6 grade.
- `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~OG/probes/og_g1.py` -- the probe, taking the short id,
  printing its measurement WITH its denominator, then exactly one line `VERDICT: PASS-GCG1-AC<n>` or
  `VERDICT: FAIL-GCG1-AC<n> <reason>`. Each run finishes inside 110 s.
- `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~OG/controlled-identity-and-grant.result.md`.
- the proof-of-spec instance at
  `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~OG/NFRA_OPLGTW.TO-OG-g-1.controlled-identity-and-grant.proof_of_spec.json`,
  validated with `python .tools/proof-of-spec-check.py <instance>` BEFORE the `complete` flip. `GCG1-J1` is recorded
  `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO~O` at L9 -- a `PASS` or `FAIL` on it is
  INVALID. Flip `complete` only when every MECHANICAL criterion PASSES by output.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below and this order's own file (for the `<status>` flip).
  Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **The live write you ARE authorized to make** is exactly one principal's `POLICY#` records through
  `ops/schwab_entitlement_admin.py`, under the `opal-gateway-access-admin` role. ⛔ **NOTHING ELSE IN AWS.** No IAM change,
  no Terraform apply, no change to `ENABLED_INTEGRATIONS`, no restart, no deploy, no edit to any existing principal's
  grant. The Gateway's own runtime role is refused by that command by design; do not work around it.
- **NEVER-2 ledger.** Open `python .tools/deploy_ledger.py open --slug nfra-oplgtw-g-c-synthetic-grant ...` BEFORE the
  activation and commit the entry AND its sentinel; close it after the read-back. It names the principal by `tid`/`oid`,
  never a name or address in the ledger body, and the rollback: `revoke` at the next revision, which is a tombstone and
  never a delete.
- **Read-only everywhere else:** the records, the contract, the protocol, the table. You do not call the Gateway as a
  user, you do not sign in as the controlled identity, and you do not run the walkthrough -- that is a person's act at
  `G-D` and grading it is `OG-v-7`'s.
- **Branch.** Work in your own linked worktree cut from `CLOUD` HEAD (`git worktree add -b ae-og-g1 <path> CLOUD`). Never
  push, merge, rebase, `checkout --`, `stash` or `clean`. The issuer drains.
- **Commits.** `bash .tools/safe-commit.sh --author "0.7.0_AE_CloudOps~OG <0.7.0_AE_CloudOps~OG@opal.agent>" -F <msgfile> -- <paths>`,
  the message file written with the Write tool. Every `.py` you touch passes `.tools/commit-gate.sh`. Capture the output
  to a file; never pipe it to `tail`.
- **Interpreter.** `python` (3.11 on site Z; there is no `py -3.12` here).
- **No egress off Opal infrastructure** beyond the one tenant read this order names. No vendor API.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy is refused WITH its
  measurement -- never repaired, widened, or satisfied by a route this order does not name.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row
  each, id `NFRA_OPLGTW-Z-OG-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`. Keep working after filing.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~OG/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-g-c-synthetic-grant.json
</paths>

**REPORT:** one message to `2.0.0_SA_COO~O` when the order is terminal, naming each criterion's verdict with its
measurement, and naming separately anything a human must still do.

<!-- ===================== RECORD FACE ===================== -->

<to_id>NFRA_OPLGTW.TO-OG-g-1</to_id>
<project>NFRA_OPLGTW</project>
<issued_date>2026-09-29</issued_date>
<fabric>site-z</fabric>
<round>6</round>
<risk>WORLD</risk>
<status>pending</status>

- **Round label.** `<round>6</round>`: the pipeline gate admits one issuance per round label, and the labels already
  held are 3 (the CTO's round-2 enrichment, @e5a6dcbe2f), 4 (OG-m-2, @14d3ce32a8) and 5 (OG-m-3, @bd0e06fe4c). It drains
  with round 3.
- **Provenance.** Re-cut from the parked draft
  `deliverables/2.0.0_SA_COO~O/DRAFT_NOT_ISSUED_TO-OG-g-1_controlled_identity_and_grant.md` (parked 2026-09-22 on
  Andrew-direct ~18:2xZ, *"Finish your work and research on the OPLGTW project and do not go further with it"*; the
  project was re-seated to the ~O fabric 2026-09-27 on *"recs approved"*). Asked by `1.0.0_SA_CTO~O` msg 26435: issue it
  to `~OG`, re-read every pin at HEAD, keep the tenant-act clause verbatim. Changed from the draft: recipient `~V` ->
  `~OG`; fabric laptop -> site-z; PRD v0.9 -> v1.1 @c80b5c85b6; contract v1.0 -> v1.3; the walkthrough is OG-v-6's v2
  seal graded by OG-v-7 (not RQ1-RQ6 / OG-v-4); `py -3.12` -> `python`; the S61 paragraph states that OG-t-1 is built
  but not deployed; the NEVER-2 slug is named.
- **Seating.** `0.7.0_AE_CloudOps~OG` was spawned 2026-09-29 03:29:51Z by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO~O` msg 26198
  (seat a CloudOps lane when E1 is next). Pre-flight: process truth 0 of 16 `claude.exe`, 0 spawn markers, broker NOT
  REGISTERED, 0 tracked files naming the lane, no inbox; concurrency 13 of 20. LIVE at PID 40072.
- **Order of the remaining acts** (unchanged from the draft, and load-bearing): this order (G-C evidence) ->
  `1.0.0_SA_CTO~O` records and closes `G-C` -> the switch's never-widen sign-off, both halves, which measures fresh that a
  principal with no grant is REFUSED -> the switch ON for the walkthrough window only -> a person runs the controlled
  walkthrough (`G-D`) -> `2.0.0_SA_COO~O` hands `OG-v-7` -> the switch OFF.
