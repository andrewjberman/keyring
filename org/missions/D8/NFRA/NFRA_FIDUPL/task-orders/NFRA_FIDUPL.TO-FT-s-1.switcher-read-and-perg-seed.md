# TO NFRA_FIDUPL.TO-FT-s-1 -- switcher-read-and-perg-seed -- the live G list, the firm table, the cross-check and the secret seed

<to_id>NFRA_FIDUPL.TO-FT-s-1</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~4</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>fidelity-r3</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-1` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 2) | **outcome_ref:** FWD-9 |
**depends_on:** none (built on fakes)

---

## WORKER FACE

### THE CELL

**FT-s-1** -- Read the G Number Switcher's list each run and turn it into the per-G list: `switcher_list.py` (the live read through the request object, the firm table of the CRO's research, the cross-check against the stored secret, the seed payload) and `perg_seed.py` (a box command that signs in, reads the live list, puts it as the value of the one secret `fidelity/alongside/perg-list` with a `measured` claim and the read time, logs out, and prints counts only). Nobody types a G number: the value is the switcher's own list.

**Read first (paths in your worktree):** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` sections 1 (rules), 7 (box layout), 9 to 12 (interfaces; section 12 is this round's); `infra/aws/ec2/canonical-fidelity/gswitch.py` (`parse_form`, `GSwitcher`), `adapters.py` (`ContextRequest`), `signin.py` (`open_session`, `Session.close`), and the CRO's research `C:/Dev/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261020_NFRA_FIDUPL_SWITCHER_LIST_READ.md` (read-only, absolute).

### WHAT TO BUILD

1. `switcher_list.py` with the functions of reference section 12 (`live_list`, `firm_for_label`, `cross_check`, `seed_payload(live, read_at)`). `firm_for_label` is a substring table, case-insensitive, first match wins in the order of the CRO's table; no match returns `("alongside", False)`. `cross_check` returns counts and ordinals only. The payload is the JSON of section 12 with `"claim": "measured"`.
2. `perg_seed.py` (python 3.9): `main(argv=None, opener=None, secrets_client=None)` loads `/opt/fidelity-uploader/config.json` (path a module constant), reads the Wealthscape credentials as `box/run.py` does, signs in through `signin.open_session` (the same persistent-profile Chrome the puller uses), builds `adapters.ContextRequest(session.context)`, calls `live_list`, writes the payload with `secretsmanager.put_secret_value(SecretId=config["perg_secret_id"], SecretString=payload)` (one call), closes the session (which logs out), and prints ONE line of counts: listed, distinct firms, unattributed. It prints no G number, label, credential or payload. Any exception prints the class name only and exits 1, still closing the session.
3. Seven tests in `tests/test_switcher_list.py` (names in the criterion): a fake request returning a synthetic form HTML with made-up G values and labels; the secret put is a fake client that records its single call.
**Fakes only.** No AWS call, no live call, no sign-in, no real secret, no real export file; every test uses synthetic data. ASCII, Python 3.9 syntax, ruff py39 clean.

### ACCEPTANCE

<criterion id="FT-s-1-AC1" cell_refs="FT-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft1</invocation><expect>R1-FT1-OK passed=\d+</expect></criterion>
`FT-s-1-AC1` -- the seven named tests exist and pass.

<expected_criteria>FT-s-1-AC1</expected_criteria>

Dry-run at the base: `FT-s-1-AC1` base: FAIL as expected

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder. Everything else named here you READ.
- **WORLD by the floor** (GATE xii floors any `infra/` path), fakes in effect. Nothing runs on the box from this order.
- **Refusal clause.** A premise that fails is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
infra/aws/ec2/canonical-fidelity/switcher_list.py
infra/aws/ec2/canonical-fidelity/perg_seed.py
infra/aws/ec2/canonical-fidelity/tests/test_switcher_list.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3), cell `FT-s-1`.
<owned_cells>FT-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-1-AC1. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~4/NFRA_FIDUPL.TO-FT-s-1.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-1-AC1` BEFORE the flip. Commit the work first, then pin.
</proof_of_spec>

**REPORT:** the criteria with output verbatim, the proof instance, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- built on fakes; runs when the live round touches the surface.
lane: the paths block.
</preflight>

Source: CTO msgs 8891 and 8909; PRD v0.5 @c4f8dc3d51; the first landed day (run record run-20261021T012004Z).
