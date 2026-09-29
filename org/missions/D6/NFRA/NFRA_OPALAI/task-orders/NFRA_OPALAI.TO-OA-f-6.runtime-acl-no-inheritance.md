# NFRA_OPALAI task order -- `OA-f-6` -- DIRECT ACT, ADDENDUM R2-A4: the runtime's folders stop inheriting a Modify grant, and the boundary proves it

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-f-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~21</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a script change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS; the ACLs are an OS boundary.
comp-adversary: DECLARED-NOT-APPLICABLE -- the two new NEGATIVE arms are the adversary read.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-f-6` (decomposition ADDENDUM R2-A4; CTO ruling msg 26306)

The Windows account `Opal_Agent` runs the Opal Analyst from `C:\opal_runtime`. Its layout, from the operator's
`runtime.config.json`: `checkout_dir` `C:\opal_runtime\opal_ai` (a read-only checkout it EXECUTES), `state_dir`
`C:\opal_runtime\state` (its only writable place), and the config file itself `C:\opal_runtime\runtime.config.json`.

**The defect, measured by `0.0.0_AB_MSTR~Z` with icacls (00:23Z).** `C:\opal_runtime` grants
`NT AUTHORITY\Authenticated Users:(OI)(CI)(M)`, and every child INHERITS it. So `Opal_Agent`, an authenticated user, has
EFFECTIVE Modify on the checkout (it could rewrite the launcher and gate code it runs) and on the config. The
provisioning script adds an allow rule for `Opal_Agent` but never breaks inheritance. The boundary check did not see
it: it tests only a workspace read and a state_dir write.

Your nested base already carries every round-2 fix (branch `nfra-opalai-r2-dev`, `e63eb06`). There:
1. **`opal_ai/opal/runtime/provision/provision-account.ps1`: break inheritance and set EXPLICIT ACEs** (remove every
   inherited ACE) on FOUR targets:
   - the runtime ROOT (the parent of `checkout_dir`) and the config file (the `-Config` path): Administrators Full,
     SYSTEM Full, the operator (the account running the script) Full, `Opal_Agent` Read only;
   - `checkout_dir`: the same, with `Opal_Agent` ReadAndExecute;
   - `state_dir`: the same, with `Opal_Agent` Modify.
   No `Authenticated Users` (or `Users`, `Everyone`) ACE on any of them. Keep it idempotent, with a re-run on the
   existing user converging to the same ACLs. The declared acts CHANGE and the new plan is approved (CTO msg 26306):
   print each ACL act in `-Plan` as `PLAN: ACL <target> <principal>:<rights> INHERITANCE-OFF`, one line per target.
2. **`verify-boundary.ps1`: two NEW NEGATIVE arms**, as FILES beside the existing two (the same `-File` plumbing, each
   writing its own verdict file into `state_dir`):
   - `boundary-arm-checkout.ps1`: tries to CREATE a file in `checkout_dir`. `DENIED` or `ALLOWED` (on `ALLOWED` it
     deletes the file it made);
   - `boundary-arm-config.ps1`: opens `runtime.config.json` FOR WRITE and writes NOTHING. `DENIED` or `ALLOWED`. It must
     never change the file's bytes.
   `BOUNDARY: DENIED-OK` now requires probe DENIED, control OK, checkout DENIED and config DENIED. The one output line
   becomes `BOUNDARY: <verdict> probe=.. control=.. checkout=.. config=..`, and `ARGLEN:` names all four arms. The
   exit codes are unchanged: 0 DENIED-OK, 1 BREACH, 3 ERROR (an arm that did not run), 4 NOT-PROVISIONED.
Change no other file.

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on its own branch off `e63eb06`. Commit with
   `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~21 <0.9.0_WK_NFRA_OPALAI~21@opal.agent>" -F <msgfile> --
   <nested paths>`, the msgfile written with the Write tool. The parent `opal_ai` gitlink is NOT yours.
2. Never run provisioning without `-Plan`, never elevate, never change a real ACL, never log on as `Opal_Agent`. The
   real run is `0.0.0_AB_MSTR~Z`'s (G-ACCT steps 1-3 again, idempotent on the existing user).
3. Standing: no push, no install, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal
   with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
opal_ai/opal/runtime/provision/provision-account.ps1
opal_ai/opal/runtime/provision/verify-boundary.ps1
opal_ai/opal/runtime/provision/boundary-arm-checkout.ps1
opal_ai/opal/runtime/provision/boundary-arm-config.ps1
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~21/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W21-S<k>` (none exist at the cut; the first is S1).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the nested commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-f-6"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f6.AC1.sh; echo "exit=$?"</invocation><expect>parse errors=0; -Plan rc=0 PLAN lines>=8 INHERITANCE-OFF>=4 AuthenticatedUsers=0; other files changed vs e63eb06=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-f-6"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/f6.AC2.sh; echo "exit=$?"</invocation><expect>arm files=4; rc=1 line='BOUNDARY: BREACH probe=ALLOWED control=OK checkout=ALLOWED config=ALLOWED'; verdict files>=4; config unchanged=yes; ARGLEN 4 values, none >=1024 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~21/NFRA_OPALAI.TO-OA-f-6.runtime-acl-no-inheritance.proof_of_spec.json`.
Report once: the new -Plan output verbatim, the changed regions, the nested commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a direct act on `1.0.0_SA_CTO~O`'s ruling msg 26306, after `0.0.0_AB_MSTR~Z`'s G-ACCT step 3 PASSED
(DENIED-OK at 00:23Z) and it stopped on the inherited `Authenticated Users:Modify`. No `<round>` (the R2-A1 precedent).
Its nested base is the local round-2 DEV `nfra-opalai-r2-dev` @e63eb06 (fd8ab8a + e-2, e-4, e-7, f-3, f-4, f-5, each merged
by this seat, the cutover's step 1 done early). `0.0.0_AB_MSTR~Z` re-runs steps 1-3 from a scratch copy of the provision
folder at this cell's nested commit, then 4-6. The diff condition becomes: the scratch set equals e63eb06's
`opal/runtime` files plus this cell's change.

Two mechanical criteria: (a) the built plan, with the bound as part of it; (b) the arms run and are wired (self-test seam).
The real negative arms are MSTR~Z's run.

SPAWN ONLY WHEN: at the cut. Slot `~21`, nested worktree `--nested opal_ai=e63eb06`.

Dry-run at base (opal_ai e63eb06):
- f6.AC1 base: FAIL as expected (`PLAN lines=8 INHERITANCE-OFF=0`).
- f6.AC2 base: FAIL as expected (`arm files=2; line='BOUNDARY: BREACH probe=ALLOWED control=OK'`).

<status>pending</status>
<direct_act>true</direct_act>
<slot>~21</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
