# TO NFRA_CTLPLN.TO-CT-ai-4 -- workstream OUTCOME round 4 (cell CT-ai-4): FWD-27 -- the laptop-side logins driven once and recorded, and the arms only a person or another device can drive named with their owners

<to_id>NFRA_CTLPLN.TO-CT-ai-4</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~109</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ai-4` (`decompositions/NFRA_CTLPLN_DECOMP.round19.md`) | **outcome_ref:** FWD-27 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD outcome FWD-27 (`prd/NFRA_CTLPLN_PRD.md` line 305): every box on the tailnet answers an SSH login by key from the tailnet devices Andrew works from (rc, muse, the laptop), and from nowhere outside it. The CVO's 2026-10-13 read (`org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CTLPLN_FWD_REGRADE_20261013.md` row 27): key login works from the laptop to three of four boxes; the laptop itself refuses (its only account is an Entra account sshd cannot resolve); `PasswordAuthentication` was on at all three. The tool is `.tools/ssh-tailnet-verify.py` (read-only: `hostname` by key, and a password probe). It refuses to run without a login name (`--user`, `--user-for BOX=LOGIN` or `OPAL_SSH_USER`). The login names used on 2026-10-13 are in the CT-u-2 proof record under `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/` (read `task-orders/NFRA_CTLPLN.TO-CT-u-2.ssh-tailnet-verify-tool.md` and its proof instance) and in the CVO table above (OPAL_BLOOMBERG, DESKTOP-HK1UU7N, DESKTOP-N8RJV0A are box host names, not logins; find the login each box accepts in the u-2 record).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. A NEW test `.tools/tests/test_round19_fwd27_laptop_side.py` (standard library). It runs `.tools/ssh-tailnet-verify.py` for site Z, dell1 and dell2 from this laptop with the logins you found, as a read (`hostname` by key; no password is ever sent; no write on any box), and prints one last line: `FWD27-LAPTOP-SIDE boxes=<n> key_ok=<k> password_refused=<p> ok=<True|False>` (ok = `key_ok` equals the number of boxes). `password_refused` is reported as measured, whatever it is; it is not a pass condition (Andrew's elevated line per box turns it off).
2. Write the record `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~109/FWD27_LAPTOP_SIDE_READ.md`: the printed tool lines verbatim with their time, then one table of the FWD-27 arms this cell did NOT drive, each with the one reason and the owner: the logins from rc and from muse (Andrew's devices; owner Andrew), the laptop as a target (needs a local administrator account on the laptop, Andrew's one line), a refused login from an address outside the tailnet (needs an off-tailnet address; owner `0.0.0_AB_MSTR`), and password login off on each box (Andrew's elevated line). Do not run any elevated command and do not try a login from outside the tailnet.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~109/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W109-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. 

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTai4-AC1" cell_refs="CT-ai-4"><invocation>python .tools/tests/test_round19_fwd27_laptop_side.py</invocation><expect>key_ok=3</expect></criterion>
`CTai4-AC1` -- key login by `hostname` answers on site Z, dell1 and dell2 from the laptop (base: the file does not exist); report the whole last line, including `password_refused`.

<criterion id="CTai4-AC2" cell_refs="CT-ai-4"><invocation>python .tools/ssh-tailnet-verify.py --selftest</invocation><expect>ok=True</expect></criterion>
`CTai4-AC2` -- the verify tool's own selftest still reads ok (base: `SSH-VERIFY-SELFTEST cases=12/12 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTai4-AC1,CTai4-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~109/NFRA_CTLPLN.TO-CT-ai-4.ssh-tailnet-laptop-side-read.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTai4-AC1,CTai4-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round19.md</decomp_doc>
<owned_cells>CT-ai-4</owned_cells>
</decomp_ref>

<paths>
.tools/tests/test_round19_fwd27_laptop_side.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the logins are SSH by key to boxes on the tailnet, a read of `hostname`.
comp-adversary: RUN -- a login by password sent by mistake (the tool probes with BatchMode only; read the tool before running it); a key login reading as OK because it landed on the wrong box (the printed `hostname` must equal the box's own name); the record claiming the unreached arms as done; BLIND: rc, muse, the laptop target and the off-tailnet refusal are not driven here, and the record says so.
risk: SERVED -- three read-only SSH logins by key on boxes of the fabric; the issuer re-runs them once at close.
lane: the <paths> block IS the grant (worker RULING 1). Only a new test file and the worker's record are written.
</preflight>

Base checks, dry-run by the issuer before the cut: CTai4-AC1 FAIL as expected (the file does not exist); CTai4-AC2 base `SSH-VERIFY-SELFTEST cases=12/12 ok=True` (a control). The verify tool refuses without a login name.
Source: CTO round-18 analysis section 3 (`ledger/ROUND_ANALYSIS.round18.md` @721e05298f), msg 109398; FWD-27.
