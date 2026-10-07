# TO NFRA_CTLPLN.TO-CT-d-3 -- round 4 CT-d-3: a named commit off the trunk -- a Dell deploys a commit it names and has published

<to_id>NFRA_CTLPLN.TO-CT-d-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~7</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-d-3` (`decompositions/NFRA_CTLPLN_DECOMP.round4.md`) | **outcome_ref:** FWD-10 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-d-3`, PRD v0.12 ADDENDUM v0.9 (a): "`.tools/safe-deploy.sh` and `safe-apply` accept a named commit off the trunk from a Dell, and say
so in the ledger entry; where either refuses today, the refusal's line is the cell's first read". The contract it implements (same
addendum): "the deploy names its commit by full hash in the box's own ledger entry, opened at the start and closed at completion; the
commit is on a branch the Dell has published, so any box can read the deployed bytes; the trunk merge follows and is never a
precondition. Never-widen halves still bind every served move." Andrew's word behind it: a Dell waits on no other box. You change the
two wrappers and prove the change against stand-in repositories. You DEPLOY NOTHING and APPLY NOTHING.

**What exists:** `.tools/safe-deploy.sh` (the deploy wrapper; DS code and data deploys go through it), `.tools/safe-apply.sh` (gates
`terraform apply` only; usage `.tools/safe-apply.sh [-chdir=DIR] apply [args]`), `.tools/deploy_ledger.py` (`open`, `close`; entries in
`org/critical_paths/change_management/`, sentinels in `org/critical_paths/.open_deploys/`), `.tools/git-hooks/pre-push-safe-deploy.sh`
(deploys only on a push of `refs/heads/CLOUD`; NOT yours to edit), the device register `org/devices/DEVICES.json` (a box's `role`;
`dell1` and `dell2` are `execution`), and a box's own name in the environment variable `AGENTBUS_DEVICE`. At the cut neither wrapper
contained the words `origin/CLOUD`, `is-ancestor` or `trunk`.

**FIRST READ (do this before writing anything, and put it in your report):** for each wrapper, what happens today when it is run from
a commit that is NOT an ancestor of `origin/CLOUD` -- read the script and every helper it calls, and find each place that refuses,
warns or silently proceeds on the commit's relation to the trunk. Quote the line (file:line) of every refusal you find, or state that
there is none and what the wrapper does instead.

**Build:**

1. `.tools/named_commit_check.py` -- ONE reading both wrappers call. `check --commit <hash> [--device <name>] [--remote origin]`:
   - `--commit` must be a FULL 40-character hash that resolves in this repository; a short or symbolic name is REFUSED.
   - The device is `--device` or `AGENTBUS_DEVICE`; unset is REFUSED. Its `role` is read from the register.
   - The commit is `ON-TRUNK` when it is an ancestor of `<remote>/CLOUD` (after `git fetch <remote>`; a fetch that fails is REFUSED,
     never treated as off-trunk), otherwise `OFF-TRUNK`.
   - `ON-TRUNK`: ADMITTED for any device (today's behaviour).
   - `OFF-TRUNK` from a device whose role is `execution`: ADMITTED only if the commit is reachable from at least one remote branch of
     `<remote>` that this device has published (`git branch -r --contains <hash>` after the fetch); print the branch. Not reachable from
     any remote branch -> REFUSED (`not published: no other box can read the deployed bytes`).
   - `OFF-TRUNK` from any other role: the behaviour you found in the FIRST READ is kept unchanged (if the wrappers do not refuse
     today, the check prints `UNCHANGED` and admits; if they refuse, it refuses with the same words).
   - It prints ONE result line, `NAMED-COMMIT <ADMITTED|REFUSED|UNCHANGED> commit=<hash> device=<d> role=<r> trunk=<ON-TRUNK|OFF-TRUNK> branch=<b|-> reason=<text>`,
     and exits 0 for ADMITTED and UNCHANGED, non-zero for REFUSED.
2. `.tools/safe-deploy.sh` and `.tools/safe-apply.sh`: each accepts the commit it is deploying (an environment variable
   `DEPLOY_COMMIT=<full hash>`; when unset the wrapper uses `git rev-parse HEAD` and behaves as today), calls the check, refuses on a
   REFUSED result, and on an `OFF-TRUNK` admission prints the result line and makes the open ledger entry carry it: the wrappers must
   pass or append `named_commit=<hash> trunk=OFF-TRUNK branch=<b> device=<d>` to the entry the actor opened (read `deploy_ledger.py`
   for how an entry is written and how a field or note is added; if the wrapper has no handle on the actor's entry, it REFUSES an
   off-trunk deploy that has no open sentinel for this device and says so -- the actor opens the entry first, which NEVER-2 already
   requires). The smallest edit that does this; no other behaviour of either wrapper changes. Both stay Git Bash 3.6.7 safe, ASCII only.
3. `.tools/tests/test_named_commit_deploy.py` -- the cases, each in a temporary directory with a local bare repository as `origin`, a
   clone, and a temporary copy of the register; no real remote, no AWS, no deploy (the wrappers are run only as far as the check: give
   them a `--check-only` path or call the check exactly as they call it, and say which):
   (1) dell1, a commit on `origin/CLOUD` -> ADMITTED, ON-TRUNK;
   (2) dell1, a commit off the trunk and pushed to `origin/q/dell1/X/round1` -> ADMITTED, OFF-TRUNK, branch printed;
   (3) dell1, a commit off the trunk and NOT pushed -> REFUSED, not published;
   (4) dell1, the case-2 commit named by its 7-character short hash -> REFUSED;
   (5) laptop (role `control-plane`), the case-2 commit -> the FIRST READ's behaviour, unchanged;
   (6) device unset -> REFUSED;
   (7) `origin` unreachable (the remote URL points nowhere) -> REFUSED, never OFF-TRUNK;
   (8) the wrapper, on case 2 with an open sentinel, leaves `named_commit=<hash>` in the ledger entry (a temporary ledger directory).
   LAST line `NAMED-COMMIT-TEST cases=<k>/8 ok=<True|False>`.

### ACCEPTANCE

<criterion id="CT4d3-AC1" cell_refs="CT-d-3"><invocation>python .tools/tests/test_named_commit_deploy.py</invocation><expect>NAMED-COMMIT-TEST cases=8/8 ok=True</expect></criterion>
`CT4d3-AC1` -- a Dell's published off-trunk commit is admitted and recorded; an unpublished, short-named or unverifiable one is refused;
another box's behaviour is as it was. Cases 3, 4, 6 and 7 are the control arms of case 2.

<criterion id="CT4d3-AC2" cell_refs="CT-d-3"><invocation>bash -n .tools/safe-deploy.sh && bash -n .tools/safe-apply.sh && bash .tools/safe-apply.sh -chdir=infra/aws/terraform/nfra-ctlpln-identity version 2>&1 | grep -c "gates 'terraform apply' only"</invocation><expect>1</expect></criterion>
`CT4d3-AC2` -- the seam probe against the REAL wrapper, a control: both parse, and `safe-apply.sh` still answers a non-apply
subcommand with its own one-line refusal ("this wrapper gates 'terraform apply' only"), exactly as at the base, so the edit put the
named-commit check on the `apply` path only and never runs terraform or the check for `plan` or `version`.

<expected_criteria>CT4d3-AC1,CT4d3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No deploy, no `terraform apply`, no push, no AWS call.** Both wrappers are used by every seat on four boxes: make the smallest edit,
  keep every existing path working when `DEPLOY_COMMIT` is unset, and run the wrappers' own existing tests if any exist under
  `.tools/tests/` (name them and their results in your report).
- You do NOT edit `.tools/git-hooks/pre-push-safe-deploy.sh` (C-TRUNK-DEPLOY is unchanged: it governs a publish, not a deploy), nor
  `.tools/deploy_ledger.py`. If the ledger tool cannot carry the field without an edit, that is a surprise row and your report, and the
  wrapper prints the line instead.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W7-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
.tools/safe-deploy.sh
.tools/safe-apply.sh
.tools/named_commit_check.py
.tools/tests/test_named_commit_deploy.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `.tools/deploy_ledger.py`, `.tools/git-hooks/pre-push-safe-deploy.sh`,
`.tools/halt-gate-check.sh`, `org/devices/DEVICES.json`, `lib/devices.py`, `org/devices/test_readers.py` (the fixture pattern).

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round4.md</decomp_doc> (round 4), cell `CT-d-3`.
<owned_cells>CT-d-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT4d3-AC1, CT4d3-AC2. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~7/NFRA_CTLPLN.TO-CT-d-3.named-commit-deploy.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT4d3-AC1,CT4d3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the FIRST READ (every refusal line found, or none); both last lines; the diff size of each wrapper; how the ledger entry
carries the field; existing wrapper tests run and their results; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy in this cell.
comp-adversary: RUN -- a Dell deploying bytes no other box can read (unpublished commit refused, case 3); a moving name (short or symbolic names refused, case 4); a failed fetch read as off-trunk and admitted (case 7: refused); the change widening another box's deploy (case 5: unchanged, read first); a deploy with no record (off-trunk admission requires the actor's open entry and writes the commit into it, case 8); BLIND: the real wrappers end to end on a Dell -- the round's one real run (CT-d-4's read-back) is the test.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.12 @2f61412157 ADDENDUM v0.9 (a), FWD-10 as amended; Andrew-direct record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_070xZ_DELLS_ARE_WORKHORSES_IRPT_PAIR_DELL2_NO_LANE_CAP_NO_TRUNK_WAIT_SEAT_ON_DELLS.md`;
decomposition round 4. Base dry-run at the cut: CT4d3-AC1 base FAIL as expected (no test file); CT4d3-AC2 is a control and reads `1` at the base (ran at the cut: `bash -n` on both wrappers rc 0; `safe-apply.sh ... version`
printed the wrapper's "gates 'terraform apply' only" line).
