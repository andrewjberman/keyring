# TO NFRA_OPLGTW.TO-OG-v-4 -- grading the controlled-identity walkthrough

<to_id>NFRA_OPLGTW.TO-OG-v-4</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~6</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-v-4` | **outcome_ref:** FWD-1, FWD-3 .. FWD-8 | **depends_on:** `OG-r-2`, `OG-o-2`, `OG-i-3`, `OG-v-3`; **HELD on gates G-C and G-D** | **slot:** ~6, queue position 4

---

## WORKER FACE

### THE CELL

`OG-v-4` -- **grading the controlled-identity walkthrough.** A person at a work browser has run the walkthrough in
`OG-v-1`'s protocol against the released Gateway, with a controlled identity and its approved synthetic grant, and the
record is at HEAD. You grade that record against the protocol, the audit sink and the sealed expectations. You perform
none of the walkthrough yourself.

The two inputs, both required at HEAD before you are spawned:
- **G-C** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md` -- the
  controlled identity's verified `tid`/`oid` and its approved grant (owner `1.0.0_SA_CTO~A`).
- **G-D** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/CONTROLLED_WALKTHROUGH_RECORD.md` -- the
  walkthrough record, in `OG-v-1`'s template.

If either is absent, file a BLOCKING row and stop.

The protocol and expectations are `infra/aws/ec2/opal-gateway/tests/acceptance/WALKTHROUGH_PROTOCOL.md` and
`A_ROWS.json` (`OG-v-1`); the sealed real-data hashes are `OG-v-3`'s `SEALED_EXPECTED.json` in this slot's deliverables,
and the operator's actual answers sit outside the repository at `C:/tmp/nfra-oplgtw-sealed/actual/`. The source-bucket
baseline is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/BASELINE.json` (`OG-p-1`). Audit records
are read-only under `opal-mcp-audit` `audit/schwab/`.

The PRD's ACCEPT clauses this record is read against are FWD-3 through FWD-8 in its ENDPOINT section; quote each one you
grade in your result file.

**The probe** for every mechanical criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py`,
taking the short id, printing its measurement with its denominator, then exactly one line `VERDICT: PASS-OGV4-AC<n>` or
`VERDICT: FAIL-OGV4-AC<n> <reason>`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGV4-AC1" cell_refs="OG-v-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGV4-AC1(?![0-9])</expect></criterion>
`OGV4-AC1` -- every person-operated A-row of `OG-v-1`'s protocol has a recorded observation in the walkthrough record, denominator printed.

<criterion id="OGV4-AC2" cell_refs="OG-v-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGV4-AC2(?![0-9])</expect></criterion>
`OGV4-AC2` -- every recorded server correlation resolves to a sanitized audit record carrying the expected decision.

<criterion id="OGV4-AC3" cell_refs="OG-v-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGV4-AC3(?![0-9])</expect></criterion>
`OGV4-AC3` -- no audit record the walkthrough produced holds a disallowed field.

<criterion id="OGV4-AC4" cell_refs="OG-v-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGV4-AC4(?![0-9])</expect></criterion>
`OGV4-AC4` -- the source-bucket readbacks after grant change, revocation and rollback equal `OG-p-1`'s baseline.

<criterion id="OGV4-AC5" cell_refs="OG-v-4"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGV4-AC5(?![0-9])</expect></criterion>
`OGV4-AC5` -- the actual answers to the chosen real-data questions hash-match `OG-v-3`'s sealed expectations.

<criterion id="OGV4-J1" cell_refs="OG-v-4" judgment="true"/>
`OGV4-J1` -- graded at L9 by 3.0.0_SA_CVO: each walkthrough step's observation matches the protocol's expected observation. RECORD; NO VERDICT.

<criterion id="OGV4-J2" cell_refs="OG-v-4" judgment="true"/>
`OGV4-J2` -- graded at L9 by 3.0.0_SA_CVO: the record meets the ACCEPT clauses of FWD-3, FWD-4, FWD-5, FWD-6, FWD-7 and FWD-8. RECORD; NO VERDICT.

<expected_criteria>OGV4-AC1, OGV4-AC2, OGV4-AC3, OGV4-AC4, OGV4-AC5, OGV4-J1, OGV4-J2</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **G-C and G-D.** Both records at HEAD, or a BLOCKING row and a stop.
- **You grade; you do not operate.** No sign-in, no connector act, no grant change, no rollback, no call to the Gateway as a user. Reads only: the records, the audit sink, the bucket settings.
- **Customer data stays out of the repository.** Answers are compared by hash; no value is committed or printed.
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
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-v-4`, round 1 (section 3, S10; section 6 G-C, G-D).
<owned_cells>OG-v-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGV4-AC1` .. `OGV4-AC5`, `OGV4-J1`, `OGV4-J2` (7). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/NFRA_OPLGTW.TO-OG-v-4.controlled-walkthrough-grading.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGV4-AC1,OGV4-AC2,OGV4-AC3,OGV4-AC4,OGV4-AC5,OGV4-J1,OGV4-J2` BEFORE the
`complete` flip. Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.** Result file
`controlled-walkthrough-grading.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by
output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. This cell is HELD on project gates G-C (owner 1.0.0_SA_CTO~A) and G-D (the operator's record, landed by 2.0.0_SA_COO~O); the vendor-egress moratorium is why the walkthrough is a person's act and not a worker's.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell reads records, the audit sink and bucket settings with existing read access; it adds no AWS operation, policy, principal or role.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~6, queue position 4, handed after `OG-r-2`, `OG-o-2`, `OG-i-3` and `OG-v-3` merge AND the G-C and G-D
records are at HEAD. Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1
@8768f46770. After this cell drains, the COO removes `C:/tmp/nfra-oplgtw-sealed/` (the retention `OG-v-3` states).
