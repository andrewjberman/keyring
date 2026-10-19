# TO NFRA_FIDUPL.TO-FU-s-7 -- apply the Fidelity root under safe-apply and deliver the code to the box

<to_id>NFRA_FIDUPL.TO-FU-s-7</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.7.0_AE_CloudOps~DELL1</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-19</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>fidelity-uploader</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FU-s-7` (`decompositions/NFRA_FIDUPL_DECOMP.md` v1.0) | **outcome_ref:** FWD-1 |
**depends_on:** FU-s-3, FU-s-4, FU-s-5, FU-s-6 terminal and merged

---

## WORKER FACE

### THE CELL

**FU-s-7** -- Apply FU-s-6 under `safe-apply` with a change-management ledger opened at start and closed at completion; deliver FU-s-1..5's files and the naming builder's minimal tree to the box by SSM. Contract row: C-TF.

**Read first, in this order:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (the facts, interfaces and handoff contract every cell shares; it is part of your context) and the cell text above. The project is NFRA_FIDUPL: the Fidelity Wealthscape daily export is landed raw every morning with nobody signing in; round 1 builds one thread end to end on fixtures and a few real read-only seams, and FU-x-1 proves the live sign-in.

### WHAT TO BUILD

This is an AWS apply, so it is addressed to the CloudOps seat on this box (CLAUDE.md rule 34; rule 20: query the dependency graph before the change; NEVER-2: open the ledger at the start and close it at completion). Hold until the issuer says the four upstream orders are merged.

1. Open a change-management entry with `.tools/deploy_ledger.py open --slug nfra-fidupl-apply-20261019 ...` (legs: the apply; the code delivery; the verify) before any AWS act. `org/critical_paths/change_management/` and `org/critical_paths/.open_deploys/` are in your `<paths>`.
2. Apply `infra/aws/terraform/canonical-fidelity-ec2/` ONLY through `.tools/safe-apply.sh`. The schedule rules are DISABLED in the root, so the apply starts no run. Apply what the FU-s-6 plan showed; if the plan differs from the merged plan in any destroy or change, STOP and file a surprise row.
3. Deliver the code to the box over SSM (the instance is stopped between runs: start it with SSM Automation or `aws ec2 start-instances`, wait until SSM reports it Online, deliver, then stop it again). The code home is a box-local directory `/opt/fidelity-uploader/` holding: the files of `infra/aws/ec2/canonical-fidelity/` (`quo_otp.py`, `signin.py`, `signin_recon.py`, `fetch.py`, `land.py`, `box/`), `config.json` (POINTERS per reference section 7, with the secret ids from the root's outputs), and the MINIMAL mirror the naming builder needs (`lib/opal_naming.py` and the registry files it loads: find them by running the builder under a temporary copy and watching what it opens), under `/opt/fidelity-uploader/repo/`. **No S3 code home exists** (the builder homes the `code` tier of scope `alongside` in the unprovisioned `opal-data-alongside`: do not use it). Deliver with `aws ssm send-command` (AWS-RunShellScript), writing files from base64 chunks; if the payload does not fit the document limits, file a surprise row naming the size and stop that leg. Then run `bootstrap.sh` on the box.
4. Close the ledger legs with proof and close the entry. The completion file name must contain `fidupl`.
Never run a Wealthscape sign-in here: that is FU-x-1.

### ACCEPTANCE

<criterion id="FU7-AC1" cell_refs="FU-s-7"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu7a</invocation><expect>R1-FU7A-OK No changes\.</expect></criterion>
`FU7-AC1` -- the applied root plans to no changes.

<criterion id="FU7-AC2" cell_refs="FU-s-7"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu7l</invocation><expect>R1-FU7L-OK completion entries=\d+, open sentinels=0</expect></criterion>
`FU7-AC2` -- the change-management entry is closed and no sentinel remains.

<expected_criteria>FU7-AC1,FU7-AC2</expected_criteria>

Dry-run at the base (HEAD of box/dell1 at the cut): `FU7-AC1` base: FAIL as expected.
Dry-run at the base (HEAD of box/dell1 at the cut): `FU7-AC2` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder. Everything else named here you READ.
- **Fixtures only.** Tests use SYNTHETIC data. The real Wealthscape export files hold client names and account numbers and are never read into a test, a log or a commit.
- **No secret, no alert.** No secret value anywhere (file, log, environment, command line, surprise row); no SNS, SES or notification of any kind.
- **Refusal clause.** A builder refusal (`address()` or `name()`): add nothing typed; file a surprise row (`NFRA_FIDUPL-D1-W<n>-S<k>`, next unused across every document under `surprise-channel/`) and stop that piece. A premise that fails against live state is a surprise row too, never a guess.
- **ASCII and Python 3.9 syntax** in every file (reference section 1).
- **WORLD.** This order changes AWS. The ledger is opened first and closed last; the apply is by `safe-apply` only; nothing is stopped, deleted or destroyed that this root did not create.

Reads (outside the grant):
- `.tools/safe-apply.sh`
- `.tools/deploy_ledger.py`
- `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md`

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention).

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP.md</decomp_doc> (round 1), cell `FU-s-7`.
<owned_cells>FU-s-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FU7-AC1,FU7-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~DELL1/NFRA_FIDUPL.TO-FU-s-7.apply-and-deploy.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FU7-AC1,FU7-AC2` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, each check line verbatim, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches the schedule (FWD-2); denominator 0 schedules created by this order.
comp-iam: RUN -- the drain prints the denominator over the applied roles; this order's own acts are the apply and an SSM delivery under the CloudOps seat's existing role.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; runs on the enrichment round that touches this surface.
lane: the paths block.
</preflight>

Source: PRD v0.4.3 (@37a9865739) and the CTO's rulings through msg 8514; decomposition round 1 cell FU-s-7; worker reference.
