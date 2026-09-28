# NFRA_OPLGTW task order -- `OG-v-7` -- ROUND 2 (E1): grading the controlled-identity walkthrough (re-cut of OG-v-4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-v-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~10</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a grading read; no cron, alarm, monitor or cadence. HELD on G-C (1.0.0_SA_CTO~O writes it, R-7) and G-D (Andrew's walkthrough, R-7).
comp-iam: DECLARED-NOT-APPLICABLE -- reads with existing access, plus ssm GetParameter under /opal/nfra_oplgtw/ogv6/.
comp-adversary: DECLARED-NOT-APPLICABLE -- a re-cut of OG-v-4 whose criteria are carried; the new judgment text is the analysis's (item E1).
EGRESS CLASS, declared: NONE beyond Opal's own AWS, read-only.
</preflight>

## 1. THE CELL -- `OG-v-7` (decomposition addendum R2-E, item E1)

**Grading the controlled-identity walkthrough.** A person at a work browser has run the walkthrough in
`infra/aws/ec2/opal-gateway/tests/acceptance/WALKTHROUGH_PROTOCOL.md` against the live Gateway, using a controlled
identity and its approved synthetic grant, and the record of that walkthrough is at HEAD. You grade the record against
the protocol, the audit sink and `OG-v-6`'s seal. You perform no part of the walkthrough. Outcomes: FWD-1, FWD-2 (A7
against `OG-v-6`'s seal), FWD-3 .. FWD-8.

Both inputs must be at HEAD before you are handed this order:
- **G-C** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md`: the
  controlled identity's verified `tid`/`oid` and its approved grant. `1.0.0_SA_CTO~O` writes it with the identity
  evidence from a `0.7.0_AE_CloudOps` seat. Andrew approved G-C on 2026-09-28 (analysis R-7).
- **G-D** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/CONTROLLED_WALKTHROUGH_RECORD.md`: the
  walkthrough record, in the template of the protocol's section 5.1. This is Andrew's walkthrough (R-7).

If either is absent, file a BLOCKING row and stop.

**Your other inputs, all read-only:**
- the protocol and its expectations: `WALKTHROUGH_PROTOCOL.md` and `A_ROWS.json` in
  `infra/aws/ec2/opal-gateway/tests/acceptance/`;
- the seal: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/SEALED_EXPECTED_V2.json`,
  whose salt and answers are in SSM under `/opal/nfra_oplgtw/ogv6/`, with local copies under
  `%LOCALAPPDATA%/opal/og-salt/v2/`;
- the operator's actual answers, at `%LOCALAPPDATA%/opal/og-salt/actual_v2/`;
- the source-bucket baseline, `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/BASELINE.json`;
- the audit records, under `opal-mcp-audit` `audit/schwab/`.

The operator followed the repaired runbook `infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md` (`OG-o-3`
lands before this cell). The PRD's ACCEPT clauses are FWD-1 through FWD-8 in its ENDPOINT section
(`org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v1.1). Quote each one you grade in your result file.

**The probe** for every mechanical criterion is
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v7.py`, which you write. You may start
from round 1's `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py`, which implements
only its AC8 (its docstring says AC1-AC7 and AC9 were never implemented). Your probe takes the short id and
`--gc <path>`, prints its measurement with its denominator, then prints exactly one line:
`VERDICT: PASS-OGV7-AC<n>` or `VERDICT: FAIL-OGV7-AC<n> <reason>`. Each run finishes inside 110 s.

## 2. BOUNDS

- **Grant.** You may write the `<paths>` block below. If you need a path that is not named here, that is a BLOCKING
  surprise row, never an override.
- **G-C and G-D** are both at HEAD, or you file a BLOCKING row and stop.
- **You grade; you do not operate.** No sign-in, no connector act, no grant change, no rollback, no call to the
  Gateway as a user. You may only read: the records, the audit sink, the bucket settings, the closure markers (AC6)
  and SSM under `/opal/nfra_oplgtw/ogv6/` (GetParameter with decryption, compared in memory).
- **Customer data stays out of the repository and off stdout.** Answers are compared by hash. The ONE exception is
  AC8's commit, and it happens only after AC5 is graded.
- **Worktree.** You work in the worktree named in your identity line, cut after `OG-v-6` and `OG-o-3` have merged.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** `.venv-og`, exactly as `OG-v-6` built it. Never commit `.venv-og/` or `.scratch/`.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any
  vendor API.
- **Commits.** Commit with `.tools/safe-commit.sh` under your serial. Every `.py` you touch passes `.tools/commit-gate.sh`.
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

Eight mechanical criteria: this is a grading cell carrying round 1's OG-v-4 criteria forward, not a build order.

<proof_of_spec>
  <criterion id="OGV7-AC1" cell_refs="OG-v-7"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v7.py AC1 --gc org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md</invocation><expect>(?m)^VERDICT: PASS-OGV7-AC1(?![0-9])</expect></criterion>
  <criterion id="OGV7-AC2" cell_refs="OG-v-7"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v7.py AC2 --gc org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md</invocation><expect>(?m)^VERDICT: PASS-OGV7-AC2(?![0-9])</expect></criterion>
  <criterion id="OGV7-AC3" cell_refs="OG-v-7"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v7.py AC3 --gc org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md</invocation><expect>(?m)^VERDICT: PASS-OGV7-AC3(?![0-9])</expect></criterion>
  <criterion id="OGV7-AC4" cell_refs="OG-v-7"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v7.py AC4 --gc org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md</invocation><expect>(?m)^VERDICT: PASS-OGV7-AC4(?![0-9])</expect></criterion>
  <criterion id="OGV7-AC5" cell_refs="OG-v-7"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v7.py AC5 --gc org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md</invocation><expect>(?m)^VERDICT: PASS-OGV7-AC5(?![0-9])</expect></criterion>
  <criterion id="OGV7-AC6" cell_refs="OG-v-7"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v7.py AC6 --gc org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md</invocation><expect>(?m)^VERDICT: PASS-OGV7-AC6(?![0-9])</expect></criterion>
  <criterion id="OGV7-AC7" cell_refs="OG-v-7"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v7.py AC7 --gc org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md</invocation><expect>(?m)^VERDICT: PASS-OGV7-AC7(?![0-9])</expect></criterion>
  <criterion id="OGV7-AC8" cell_refs="OG-v-7"><invocation>timeout 110 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/probes/og_v7.py AC8 --gc org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md</invocation><expect>(?m)^VERDICT: PASS-OGV7-AC8(?![0-9])</expect></criterion>
  <criterion id="OGV7-J1" cell_refs="OG-v-7" judgment="true"/>
  <criterion id="OGV7-J2" cell_refs="OG-v-7" judgment="true"/>
</proof_of_spec>

- `OGV7-AC1`: every person-operated A-row of the protocol has a recorded observation in the walkthrough record. The
  denominator is printed.
- `OGV7-AC2`: every server correlation in the record resolves to a sanitized audit record that carries the expected
  decision.
- `OGV7-AC3`: no audit record produced by the walkthrough holds a disallowed field.
- `OGV7-AC4`: the source-bucket readbacks after the grant change, the revocation and the rollback equal `OG-p-1`'s
  baseline.
- `OGV7-AC5`: each actual answer to the section 4 questions was asked at the question's fixed date, and it hash-matches
  `SEALED_EXPECTED_V2.json` under the SSM-held salt. N of N is printed, where N is the number of questions in the seal.
  No value is printed.
- `OGV7-AC6`: for each master (`08242234`, `08335338`), the latest qualified date that the record shows A7's no-date
  request returned equals the newest `schwab/<master>/meta/complete/date=*.json` marker in `opal-data-assets` that has
  `closure.status` `qualified` and a LastModified earlier than the recorded ask time. Read-only; denominator 2 printed.
- `OGV7-AC7`: for each master, the available-dates list that the record shows A7's no-date request returned contains
  both of `OG-v-6`'s fixed dates (`D_PREV`, `D_NEW`, read from `SEALED_EXPECTED_V2.json`). Denominator 2 printed.
- `OGV7-AC8` applies AFTER AC5 has been graded. It is round 1's `OGV4-AC9`, carried. The salt and the expected-answer
  files are committed into your deliverables as drain evidence, and the probe re-derives every digest in
  `SEALED_EXPECTED_V2.json` from the committed files. It prints the number that match against the denominator. The
  probe first checks that AC5's recorded verdict exists. ORDERING IS THE CRITERION: committing the salt before AC5 is
  graded FAILS.
- `OGV7-J1`: graded at L9 by `3.0.0_SA_CVO~O`. Each walkthrough step's observation matches the protocol's expected
  observation. RECORD; NO VERDICT.
- `OGV7-J2`: graded at L9 by `3.0.0_SA_CVO~O`. This is the round's judgment criterion on a WORLD cell. For each of
  FWD-1 and FWD-3 through FWD-8, every clause of its ACCEPT sentence has at least one line in the record stating what
  the PERSON OBSERVED: the screen, the downloaded file, or the refusal text. Server logs and audit records never stand
  in for an observation. PASS only when every ACCEPT clause has an observed line. RECORD; NO VERDICT.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~10/NFRA_OPLGTW.TO-OG-v-7.controlled-walkthrough-grading-r2.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>` BEFORE the `complete` flip. Record each judgment row as
`UNVERIFIABLE-BY-INSTRUMENT`, naming `3.0.0_SA_CVO~O` at L9. The result file is
`controlled-walkthrough-grading-r2.result.md`. Flip to `complete` only when every MECHANICAL criterion PASSES by output.
Report once, in your final message. You cannot send or receive messages.

<!-- ===================== RECORD FACE ===================== -->

**What changed from `OG-v-4`, exactly.** The re-cut is "unchanged" in substance; these are the only differences:
1. **Gates.** G-C and G-E were approved by Andrew on 2026-09-28. G-D is his walkthrough (R-7). The G-C path is the
   CTO's pin (msg 26198): `deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md`, the evidence from a
   `0.7.0_AE_CloudOps` seat the COO seats when E1 is next.
2. **The seal.** AC5 and AC7 read `OG-v-6`'s `SEALED_EXPECTED_V2.json` and its fixed dates, not OG-v-3's set, its re-seal
   `d5af54a90a`, or `2026-09-15`. FWD-2 joins outcome_ref through A7; its live exercise is the COO's close run (Q4).
3. **Criteria.** `OGV4-AC8` (phase-1 re-seal) is RETIRED here, because `OG-v-6` is the seal. `OGV4-AC9` is carried as
   `OGV7-AC8`. AC1-AC7 and J1 are carried with their text unchanged apart from the seal and date references. J2 is the
   round's judgment criterion text (analysis section 4 item 1), widened to FWD-1 and FWD-3..8.
4. **Single hand-off.** Slot ~10, queue position 2: handed once, after `OG-v-6` and `OG-o-3` merge AND G-C and G-D are
   at HEAD.
5. **Runbook dependency.** `OG-o-3` repairs `SCHWAB_PILOT_RUNBOOK.md` before the walkthrough (OGO2-J1).

After this cell drains, the COO removes `%LOCALAPPDATA%/opal/og-salt/v2/` and `actual_v2/`. The SSM parameters under
`/opal/nfra_oplgtw/ogv6/` stay as the copy of record until the round closes.

<status>staged</status>
<round>3</round>
<slot>~10</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
