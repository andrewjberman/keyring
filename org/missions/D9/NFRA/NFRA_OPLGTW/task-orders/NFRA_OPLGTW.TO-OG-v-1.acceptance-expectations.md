# TO NFRA_OPLGTW.TO-OG-v-1 -- independent acceptance expectations and the walkthrough protocol

<to_id>NFRA_OPLGTW.TO-OG-v-1</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~6</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-v-1` | **outcome_ref:** FWD-1 .. FWD-8 | **depends_on:** `OG-c-1` | **slot:** ~6, queue position 1

---

## WORKER FACE

### THE CELL

`OG-v-1` -- **independent acceptance expectations and the walkthrough protocol**, under
`infra/aws/ec2/opal-gateway/tests/acceptance/`. Everything the round later grades is graded against what you fix here,
BEFORE the code it grades is finished and WITHOUT reading it. You are deliberately not the author of any Schwab query,
catalog or export code.

The PRD, verbatim (acceptance matrix): *"Every row starts NOT EXERCISED. Expected set is A1-A20 as data in the contract.
The test author must construct independent expected fixtures rather than calculate expectations with the query under
test. CVO's validation compares that full set before trusting any green test exit code. Record tool, UTC time, connector
URL, principal class, source/code/config version, request, expected result, actual result, and sanitized server
correlation; collect an ofid_ reference if Claude supplies one. The connector URL is the public configured MCP endpoint,
without credentials, ticket fragments or private query parameters; never tokens/customer data in repository evidence."*
The twenty rows are in the PRD's "Acceptance matrix and independent proof" table; the contract's `acceptance_ids` is the
census you match.

**What you write:**
1. `A_ROWS.json` -- one entry per A-row, A1 .. A20: the expected result, the instrument, and `operated_by` = `machine`
   (graded by `OG-v-2` or `OG-r-2` in process) or `person` (graded from a walkthrough record by `OG-v-4` or `OG-v-5`).
2. `make_fixtures.py` and the synthetic Parquet and closure fixtures it writes under `fixtures/`, following the record
   schema `OG-c-1` published (its result file under `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/`).
   Field names and types follow the contract's `fields` and the certified L4 rectangle's measured types.
3. `expect_independent.py` and the expected answers it writes under `expected/`, computed with an instrument of your own
   (for example Python `decimal` over rows read with PyArrow), never with `app/integrations/schwab/`.
4. `WALKTHROUGH_PROTOCOL.md` -- for every person-operated row, the steps, the expected observation and the sanitized
   evidence to record; the two record templates, whose landed homes are
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/CONTROLLED_WALKTHROUGH_RECORD.md` (gate G-D) and
   `.../2.0.0_SA_COO~O/PILOT_WALKTHROUGH_RECORD.md` (gate G-F); the inputs they presuppose, at
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md` and
   `.../1.0.0_SA_CTO~A/G-E_PILOT_IDENTITY_AND_GRANT.md`; and the real-data questions `OG-v-3` answers (at least one per
   master, one comparison between masters as separate snapshots, one comparison between dates). Answers to real-data
   questions are recorded by the operator OUTSIDE the repository at `C:/tmp/nfra-oplgtw-sealed/actual/`, never in a
   record; `OG-v-4` hashes them there.

**Read:** the PRD's "Acceptance matrix and independent proof", "C3", "C4" and "C5"; the contract; the certified rectangle
`workflows/atom_decomposition/runs/nfra-oplgtw/20260914T1919Z/rectangle.final.certified.json` (S3-data, the measured
types); `OG-c-1`'s result file. **Do not open `app/integrations/schwab/`.**

**The probe** for every mechanical criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v1.py`,
taking the short id, printing its measurement with its denominator, then exactly one line `VERDICT: PASS-OGV1-AC<n>` or
`VERDICT: FAIL-OGV1-AC<n> <reason>`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGV1-AC1" cell_refs="OG-v-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v1.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGV1-AC1(?![0-9])</expect></criterion>
`OGV1-AC1` -- the A-row census is exactly A1 .. A20, 20 of 20, each with its expected result, its instrument and whether a machine or a person operates it.

<criterion id="OGV1-AC2" cell_refs="OG-v-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v1.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGV1-AC2(?![0-9])</expect></criterion>
`OGV1-AC2` -- the synthetic fixtures carry two masters sharing one numeric account ID.

<criterion id="OGV1-AC3" cell_refs="OG-v-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v1.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGV1-AC3(?![0-9])</expect></criterion>
`OGV1-AC3` -- the synthetic fixtures carry overlapping balance fields, nulls, signs, decimal edge values and a duplicate grain.

<criterion id="OGV1-AC4" cell_refs="OG-v-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v1.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGV1-AC4(?![0-9])</expect></criterion>
`OGV1-AC4` -- the synthetic fixtures carry prompt-like text in a security description and formula-like text.

<criterion id="OGV1-AC5" cell_refs="OG-v-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v1.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGV1-AC5(?![0-9])</expect></criterion>
`OGV1-AC5` -- the synthetic closure fixtures carry missing, partial, failed and stale variants and an unversioned object.

<criterion id="OGV1-AC6" cell_refs="OG-v-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v1.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGV1-AC6(?![0-9])</expect></criterion>
`OGV1-AC6` -- expected answers are computed by an instrument independent of the query engine, named, with no import from `app/integrations/schwab/` (the probe parses every file you wrote for imports).

<criterion id="OGV1-AC7" cell_refs="OG-v-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v1.py AC7</invocation><expect>(?m)^VERDICT: PASS-OGV1-AC7(?![0-9])</expect></criterion>
`OGV1-AC7` -- for each person-operated A-row, the protocol lists the steps, the expected observation, and the sanitized evidence to record: tool, UTC time, public connector URL, server correlation, and an `ofid_` reference if Claude supplies one.

<criterion id="OGV1-AC8" cell_refs="OG-v-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v1.py AC8</invocation><expect>(?m)^VERDICT: PASS-OGV1-AC8(?![0-9])</expect></criterion>
`OGV1-AC8` -- the protocol lists the chosen real-data questions `OG-v-3` answers: at least one per master, one comparison between masters as separate snapshots, one comparison between dates.

<criterion id="OGV1-AC9" cell_refs="OG-v-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v1.py AC9</invocation><expect>(?m)^VERDICT: PASS-OGV1-AC9(?![0-9])</expect></criterion>
`OGV1-AC9` -- no fixture holds customer data (every account ID and value is synthetic, by a scan against the fixture generator's own seeds).

<expected_criteria>OGV1-AC1, OGV1-AC2, OGV1-AC3, OGV1-AC4, OGV1-AC5, OGV1-AC6, OGV1-AC7, OGV1-AC8, OGV1-AC9</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Independence.** You never read or import `app/integrations/schwab/`. Your expectations come from the PRD, the contract and your own instrument.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-c-1` merged). Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Build your own venv once: `cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`. Never commit `.venv-og/` or `.scratch/`.
- **Synthetic only.** No Schwab object is read; no real account ID, name or value appears in any file.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`. Fixture Parquet files are small (kilobytes).
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W6-S<k>`, per the worker definition. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/tests/acceptance/A_ROWS.json
infra/aws/ec2/opal-gateway/tests/acceptance/WALKTHROUGH_PROTOCOL.md
infra/aws/ec2/opal-gateway/tests/acceptance/make_fixtures.py
infra/aws/ec2/opal-gateway/tests/acceptance/expect_independent.py
infra/aws/ec2/opal-gateway/tests/acceptance/fixtures/
infra/aws/ec2/opal-gateway/tests/acceptance/expected/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-v-1`, round 1 (section 3, S10; section 5 distinct-worker constraint).
<owned_cells>OG-v-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGV1-AC1` .. `OGV1-AC9` (9). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/NFRA_OPLGTW.TO-OG-v-1.acceptance-expectations.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGV1-AC1,OGV1-AC2,OGV1-AC3,OGV1-AC4,OGV1-AC5,OGV1-AC6,OGV1-AC7,OGV1-AC8,OGV1-AC9`
BEFORE the `complete` flip. Result file `acceptance-expectations.result.md` beside it. **Flip `complete` only when every
MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. This cell fixes the record homes that gates G-C, G-D, G-E and G-F name; none holds it.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell writes synthetic fixtures and a protocol; it adds no AWS operation, policy, principal or role.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~6, queue position 1, handed after `OG-c-1` merges; a slot that authors no Schwab query, catalog or export
code (decomposition s.5, the distinct-worker constraint). Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O` (seated msg
96971, LD-0567). Decomposition v1 @8768f46770.
