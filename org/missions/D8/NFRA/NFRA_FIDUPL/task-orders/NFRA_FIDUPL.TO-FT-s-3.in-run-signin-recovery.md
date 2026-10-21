# TO NFRA_FIDUPL.TO-FT-s-3 -- in-run-signin-recovery -- one full sign-in in the box's OS-launched Chrome unit over CDP

<to_id>NFRA_FIDUPL.TO-FT-s-3</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~6</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>fidelity-r3</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-3` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 2) | **outcome_ref:** FWD-1 |
**depends_on:** none (built on fakes; interface in reference section 12)

---

## WORKER FACE

### THE CELL

**FT-s-3** -- When the scripted sign-in is refused, the run may sign in once more in the box's own OS-launched Google Chrome (the `fidelity-agent-chrome.service` unit, remote debugging on `127.0.0.1:9222`, profile `/opt/fidelity-uploader/profile-agent`), the shape that the CTO proved accepted. `signin_recover.py` is that path: `recover_session(config, credentials, otp_reader)`.

**Read first (paths in your worktree):** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` sections 1 (rules), 7 (box layout), 9 to 12 (interfaces; section 12 is this round's); `signin.py` (`PlaywrightDriver`, `sign_in`, `SigninError`, `Session`), `agent_drive.py` and `box/agent_fill.py` (they already attach over CDP: copy their attach shape), and the unit's text in `C:/Dev/ajb_workspace/org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/FU-s-11_feasibility.md` heading CDP (read-only, absolute).

### WHAT TO BUILD

1. `signin_recover.py` (python 3.9): `recover_session(config, credentials, otp_reader, playwright_factory=None, runner=None, port_open=None, sleep=None)`. If the loopback port 9222 is closed, start the unit with `systemctl start fidelity-agent-chrome.service` through the injected `runner`, then wait (poll, 30 s ceiling) for the port; remember whether it started the unit. Attach with `connect_over_cdp("http://127.0.0.1:9222")` (anything other than loopback is refused before any connection), take the first context's first page, and run `signin.sign_in(signin.PlaywrightDriver(page), credentials, otp_reader)` ONCE. On success return an object with `.context`, `.page` and `.close()`; `close()` calls the driver's `logout()`, stops the playwright driver and, only if this call started the unit, stops it with `systemctl stop`. On failure raise the `SigninError` the sign-in raised (its class kept), after a best-effort logout and the same stop rule. Never loop, never retry.
2. Five tests in `tests/test_signin_recover.py` (names in the criterion): fakes for the runner, the port, the playwright factory and the driver.
**Fakes only.** No AWS call, no live call, no sign-in, no real secret, no real export file; every test uses synthetic data. ASCII, Python 3.9 syntax, ruff py39 clean.

### ACCEPTANCE

<criterion id="FT-s-3-AC1" cell_refs="FT-s-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft3</invocation><expect>R1-FT3-OK passed=\d+</expect></criterion>
`FT-s-3-AC1` -- the five named tests exist and pass.

<expected_criteria>FT-s-3-AC1</expected_criteria>

Dry-run at the base: `FT-s-3-AC1` base: FAIL as expected

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder. Everything else named here you READ.
- **WORLD by the floor**, fakes in effect. Nothing runs on the box from this order.
- **Refusal clause.** A premise that fails is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
infra/aws/ec2/canonical-fidelity/signin_recover.py
infra/aws/ec2/canonical-fidelity/tests/test_signin_recover.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3), cell `FT-s-3`.
<owned_cells>FT-s-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-3-AC1. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~6/NFRA_FIDUPL.TO-FT-s-3.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-3-AC1` BEFORE the flip. Commit the work first, then pin.
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
