# TO NFRA_FIDUPL.TO-FU-s-5 -- the box bootstrap and the run wrapper

<to_id>NFRA_FIDUPL.TO-FU-s-5</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~3</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>fidelity-uploader</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FU-s-5` (`decompositions/NFRA_FIDUPL_DECOMP.md` v1.0) | **outcome_ref:** FWD-1 |
**depends_on:** none (interface bounds only: reference section 9)

---

## WORKER FACE

### THE CELL

**FU-s-5** -- The box runtime: `box/bootstrap.sh` (Chromium, Playwright, runtime; no secret in the environment) and `box/run.py` (calls signin, fetch, land in order, always lets the lander write the record, exits non-zero on any failure). Contract rows: C-SIGNIN, C-ISOLATION.

**Read first, in this order:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (the facts, interfaces and handoff contract every cell shares; it is part of your context) and the cell text above. The project is NFRA_FIDUPL: the Fidelity Wealthscape daily export is landed raw every morning with nobody signing in; round 1 builds one thread end to end on fixtures and a few real read-only seams, and FU-x-1 proves the live sign-in.

### WHAT TO BUILD

Build `infra/aws/ec2/canonical-fidelity/box/bootstrap.sh`, `box/run.py` and `tests/test_box_run.py` to reference sections 7 and 9.

1. `bootstrap.sh` (bash, `set -euo pipefail`, idempotent, safe to run twice) prepares a fresh Amazon Linux 2023 or Ubuntu host: installs Python 3 and pip packages `boto3` and `playwright`, runs `python3 -m playwright install --with-deps chromium`, creates `/opt/fidelity-uploader/` with `profile/` and `work/`, and writes NO secret and exports NO variable named like a password, secret, key or token. It reads nothing from the network except package indexes and the Playwright browser download.
2. `run.py`: `run_once(config, deps)` as in reference section 9. `config` is the parsed `/opt/fidelity-uploader/config.json` (POINTERS only, reference section 7). Order: create a run directory under `work_dir`; `read_secret(config["wealthscape_secret_id"])`; open the session; `fetch_day` for today's date in `America/New_York`; `land(handoff_dir, config["scope"])`. If the sign-in fails (a `SigninError`), write a handoff directory whose `listing.json` carries the `failure` (`failure_class` of the error), no files, and still call `land`, so a record is written. The process exit code is non-zero if any stage failed or the listing carries a failure, and zero otherwise.
3. `run.py` has a `main()` that loads the config path from argv or `/opt/fidelity-uploader/config.json` and wires the real `signin.open_session`, `fetch.fetch_day` and `land.land` (imported lazily so the tests need no browser). It never reads a secret from the environment and never sets one.
4. Tests with fakes: `test_calls_signin_fetch_land_in_order`, `test_stage_failure_exits_nonzero`, `test_failure_still_writes_record_via_lander`, `test_no_secret_in_environment` (assert the environment is unchanged after a run), `test_reads_config_pointers_only` (a config holding a literal password value is rejected).

### ACCEPTANCE

<criterion id="FU5-AC1" cell_refs="FU-s-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu5</invocation><expect>R1-FU5-OK passed=\d+</expect></criterion>
`FU5-AC1` -- the five named tests exist and pass.

<criterion id="FU5-AC2" cell_refs="FU-s-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu5b</invocation><expect>R1-FU5B-OK bash -n clean</expect></criterion>
`FU5-AC2` -- the bootstrap parses, installs a browser and exports no secret.

<expected_criteria>FU5-AC1,FU5-AC2</expected_criteria>

Dry-run at the base (HEAD of box/dell1 at the cut): `FU5-AC1` base: FAIL as expected.
Dry-run at the base (HEAD of box/dell1 at the cut): `FU5-AC2` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder. Everything else named here you READ.
- **Fixtures only.** Tests use SYNTHETIC data. The real Wealthscape export files hold client names and account numbers and are never read into a test, a log or a commit.
- **No secret, no alert.** No secret value anywhere (file, log, environment, command line, surprise row); no SNS, SES or notification of any kind.
- **Refusal clause.** A builder refusal (`address()` or `name()`): add nothing typed; file a surprise row (`NFRA_FIDUPL-D1-W<n>-S<k>`, next unused across every document under `surprise-channel/`) and stop that piece. A premise that fails against live state is a surprise row too, never a guess.
- **ASCII and Python 3.9 syntax** in every file (reference section 1).

Reads (outside the grant):
- `infra/aws/ec2/inf-exporter/` and `infra/aws/ec2/bd-exporter/` (how the estate's other Playwright boxes install; shape only)

<paths>
infra/aws/ec2/canonical-fidelity/box/bootstrap.sh
infra/aws/ec2/canonical-fidelity/box/run.py
infra/aws/ec2/canonical-fidelity/tests/test_box_run.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention).

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP.md</decomp_doc> (round 1), cell `FU-s-5`.
<owned_cells>FU-s-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FU5-AC1,FU5-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~3/NFRA_FIDUPL.TO-FU-s-5.box-runtime.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FU5-AC1,FU5-AC2` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, each check line verbatim, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches the schedule (FWD-2); denominator 0 schedules created by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- authoring and fakes; no grant is written.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; runs on the enrichment round that touches this surface.
lane: the paths block.
</preflight>

Source: PRD v0.4.3 (@37a9865739) and the CTO's rulings through msg 8514; decomposition round 1 cell FU-s-5; worker reference.
