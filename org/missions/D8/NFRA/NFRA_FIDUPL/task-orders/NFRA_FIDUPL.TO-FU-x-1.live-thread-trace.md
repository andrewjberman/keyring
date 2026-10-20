# TO NFRA_FIDUPL.TO-FU-x-1 -- the live FWD-1 trace and the two G probes

<to_id>NFRA_FIDUPL.TO-FU-x-1</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~1</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>fidelity-uploader</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FU-x-1` (`decompositions/NFRA_FIDUPL_DECOMP.md` v1.0) | **outcome_ref:** FWD-1, FWD-9 |
**depends_on:** FU-s-7 applied and delivered; G-3 (Andrew has written the Wealthscape credential into its secret)

---

## WORKER FACE

### THE CELL

**FU-x-1** -- Closing pass for FWD-1: one on-demand run through the real chain; six files listed, downloaded, landed; the run record shows `source: automated`; then the two probes: the `account.txt` G-number read and the G-switch probe, each written as a counts-only record. Contract rows: FWD-1, C-TENANCY.

**Read first, in this order:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (the facts, interfaces and handoff contract every cell shares; it is part of your context) and the cell text above. The project is NFRA_FIDUPL: the Fidelity Wealthscape daily export is landed raw every morning with nobody signing in; round 1 builds one thread end to end on fixtures and a few real read-only seams, and FU-x-1 proves the live sign-in.

### WHAT TO BUILD

Run the thread once, for real, and read the result. FU-s-7 is closed (commit 80dd906801). Hold until the Wealthscape secret holds a value (check only that the secret has a current version: `aws secretsmanager describe-secret` shows `LastChangedDate`/a version stage; never read the value).

0. **ATTEMPT 2 (issuer, 2026-10-20 ~13:50Z): the trace first.** Attempt 1 failed twice (rows W1-S8 and W1-S9, both now repaired and verified live by the issuer: the automation role has `ec2:DescribeInstanceStatus`; the box holds the repaired `signin.py` and `signin_recon.py`; the box is RUNNING, tagged `AutoShutdown=disabled`, and the automation document no longer stops it). Before anything else run ONCE, on the box through SSM, `/opt/fidelity-uploader/venv/bin/python /opt/fidelity-uploader/signin_recon.py --trace-login`. It drives the username, the password, the factor choice and the request for the text, and stops there (it costs at most one text and reads no code). Put its printed trace in your report (it holds no value). **If it does not reach the text request, STOP: do not run steps 1 or 3, file one surprise row naming the failing step and quoting the trace line, and report.** If it does, continue with steps 1 and 3 below, each ONCE.
1. **The on-demand chain run.** Start the SAME automation the schedule uses, by hand: `aws ssm start-automation-execution --document-name <the document name from the root's outputs>` (use the `.tools/aws` shim). Wait for the execution to end; its final state is part of the record (the automation no longer stops the box). No person signs in or types a code: that is the point.
2. **Read the run record** the lander wrote (reference section 6) with `python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py x1r`. A pass means `source: automated`, no `failure_class`, six files `landed`. If the run fails, read the record's `failed_step` and `failure_class`, put them in your report, and file ONE surprise row per distinct cause (an unmeasured selector, a refused sign-in, a missing export). Do not fix other cells' code; this order's write set is deliverables only.
3. **The `account.txt` G-number read and the G-switch probe.** The box may be STOPPED when you start (the account's ec2-auto-shutdown-enforcer stopped it at 2026-10-20T00:51Z, row NFRA_FIDUPL-D1-S5; the code and venv persist on its root volume), and the automation no longer stops it. If it is stopped, first start it: `aws ec2 start-instances --instance-ids <the instance id from the root's outputs>` (a start is allowed; a STOP is not yours to do), wait until SSM reports it Online, then run, on the box through SSM, `/opt/fidelity-uploader/venv/bin/python /opt/fidelity-uploader/signin_recon.py --run-live` (the venv python: the system python3 on the box has no boto3 or playwright; it signs in a second time, so a second text message is expected). Do not stop the instance afterwards; leave it for the enforcer or the next automation run. Capture its stdout through `aws ssm get-command-invocation`. Write the two counts-only blocks verbatim to `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/<your serial>/FU-x-1_account_gnumber_read.md` (fields `columns=<n> g_number_columns=[...]`) and `.../FU-x-1_g_selector_probe.md` (fields `list_narrows=yes|no options=<n> restored_starting_g=yes|no`). **Neither file may contain an account number, a G number or any value.** The probe switches the current G number once and back and never sets a default; if its output says `restored_starting_g=no`, report that as BLOCKING.
4. Your report states, for FWD-1: the execution id, the run id, and what an analyst would open (the six destination addresses from the record).

### ACCEPTANCE

<criterion id="FX1-AC1" cell_refs="FU-x-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py x1r</invocation><expect>R1-X1R-OK source=automated landed=6</expect></criterion>
`FX1-AC1` -- the latest run record shows an automated run that landed six files.

<criterion id="FX1-AC2" cell_refs="FU-x-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py x1g</invocation><expect>R1-X1G-OK columns=\d+ g_number_columns=</expect></criterion>
`FX1-AC2` -- the account.txt G-number read is on file, counts only.

<criterion id="FX1-AC3" cell_refs="FU-x-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py x1p</invocation><expect>R1-X1P-OK list_narrows=(yes|no) options=\d+ restored_starting_g=yes</expect></criterion>
`FX1-AC3` -- the G-switch probe is on file, counts only, with the starting G restored.

<expected_criteria>FX1-AC1,FX1-AC2,FX1-AC3</expected_criteria>

Dry-run at the base (HEAD of box/dell1 at the cut): `FX1-AC1` base: FAIL as expected.
Dry-run at the base (HEAD of box/dell1 at the cut): `FX1-AC2` base: FAIL as expected.
Dry-run at the base (HEAD of box/dell1 at the cut): `FX1-AC3` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder. Everything else named here you READ.
- **Fixtures only.** Tests use SYNTHETIC data. The real Wealthscape export files hold client names and account numbers and are never read into a test, a log or a commit.
- **No secret, no alert.** No secret value anywhere (file, log, environment, command line, surprise row); no SNS, SES or notification of any kind.
- **Refusal clause.** A builder refusal (`address()` or `name()`): add nothing typed; file a surprise row (`NFRA_FIDUPL-D1-W<n>-S<k>`, next unused across every document under `surprise-channel/`) and stop that piece. A premise that fails against live state is a surprise row too, never a guess.
- **ASCII and Python 3.9 syntax** in every file (reference section 1).
- **WORLD, live.** This order signs in to Wealthscape through the box with the firm's credentials (Andrew-direct ~19:0xZ: "we are authorized users of the application"), switches the session's current G number once and back without setting a default, and reads files. It writes to `opal-data-assets` only through the lander. It stops the instance after the run.

Reads (outside the grant):
- the Terraform root outputs
- `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md`

<paths>
org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention).

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP.md</decomp_doc> (round 1), cell `FU-x-1`.
<owned_cells>FU-x-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FX1-AC1,FX1-AC2,FX1-AC3. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~1/NFRA_FIDUPL.TO-FU-x-1.live-thread-trace.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FX1-AC1,FX1-AC2,FX1-AC3` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, each check line verbatim, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches the schedule (FWD-2); denominator 0 schedules created by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- uses the grants FU-s-6 wrote and FU-s-7 applied; no new grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; runs on the enrichment round that touches this surface.
lane: the paths block.
</preflight>

Source: PRD v0.4.3 (@37a9865739) and the CTO's rulings through msg 8514; decomposition round 1 cell FU-x-1; worker reference.
