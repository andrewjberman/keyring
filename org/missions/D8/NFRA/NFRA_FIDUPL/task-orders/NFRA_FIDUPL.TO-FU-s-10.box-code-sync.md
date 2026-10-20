# TO NFRA_FIDUPL.TO-FU-s-10 -- keep the Fidelity box's code equal to the repo (re-deliver the shipped files)

<to_id>NFRA_FIDUPL.TO-FU-s-10</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>fidelity-box-delivery</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FU-s-10` (`decompositions/NFRA_FIDUPL_DECOMP.md` section 9) | **outcome_ref:** FWD-1 |
**depends_on:** FU-s-2 repair 2 (merged f5abe66e28)

---

## WORKER FACE

### THE CELL

**FU-s-10** -- Keep the box's code equal to the repo: re-deliver every shipped file of `infra/aws/ec2/canonical-fidelity/` (and `box/`) to `/opt/fidelity-uploader/` by SSM, md5-checked, the box left running. Contract row: C-TF. The same delivery you made in FU-s-7 leg 3 and FU-s-9 leg 5.

**Read first:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` and your own earlier ledger notes (the bridge symlinks under `/opt/fidelity-uploader`, row NFRA_FIDUPL-D1-S4).

### WHAT TO DO

1. Open a change-management entry (`.tools/deploy_ledger.py open --slug nfra-fidupl-box-code-sync-<date> ...`, one leg: code equal to the repo).
2. The FU-s-2 login-trace repair 2 is merged on box/dell1 at f5abe66e28 (signin.py gained a values-free network, form-state, console and fingerprint trace; tests 67 passing). Take the repo files at THAT head or later. Re-deliver exactly these seven to `/opt/fidelity-uploader/`, keeping the same relative layout you used before: `quo_otp.py`, `signin.py`, `signin_recon.py`, `fetch.py`, `land.py`, `box/run.py`, `box/bootstrap.sh`. Do not touch `config.json`, `profile/`, `work/`, `venv/` or the bridge symlinks. Do NOT run `bootstrap.sh`; do not run any sign-in; do not stop or start the instance (it is running; if it is stopped, tell the issuer, do not start it).
3. Run the criterion below, record the line verbatim, close the ledger leg and the entry.

### ACCEPTANCE

<criterion id="FU10-AC1" cell_refs="FU-s-10"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu10m</invocation><expect>R1-FU10M-OK all 7 shipped files match the repo on the box</expect></criterion>
`FU10-AC1` -- the seven shipped files on the box match the repo by md5.

<expected_criteria>FU10-AC1</expected_criteria>

Dry-run at the base (the box holds the pre-REPAIR-2 signin.py): `FU10-AC1` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder.
- **WORLD.** An SSM delivery to the box. Ledger first, closed last. Never read the Wealthscape secret; no sign-in; no alert.
- **Refusal clause.** A premise that fails (an md5 that will not match, the box stopped) is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP.md</decomp_doc> (round 1, section 9 addendum), cell `FU-s-10`.
<owned_cells>FU-s-10</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FU10-AC1. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_FIDUPL.TO-FU-s-10.box-code-sync.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FU10-AC1` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** the head you delivered from, the seven md5 lines, the check line verbatim, the ledger id, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- a file delivery of already-merged code; no new surface.
lane: the paths block.
</preflight>

Source: FU-x-1 attempt 2 (worker row W1-S11), FU-s-2 repair 2 merged f5abe66e28.
