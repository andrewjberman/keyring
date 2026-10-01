# NFRA_MCPMSP task order -- `MS-s-1` -- ROUND 2, E6: safe-apply's naming plan stage renders the plan the apply runs

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-s-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~7</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a local gate script; tests use a fake terraform.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC1's base-bytes run is the adversary read.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-s-1` (decomposition v2 addendum R2.8; the gate owner's ruling, laptop `1.0.0_SA_CTO` msg 103400)

`.tools/safe-apply.sh` has two naming stages (read `:80-150`): a PRE-PLAN stage (`naming-apply-gate.py` on the tree's
literals) and a PLAN stage (`:116-150`) that runs `"$TERRAFORM" -chdir=<tree> plan -input=false -lock=false -out=<tmp>`
then `show -json` and grades it with `naming-apply-gate.py --plan-json`. Measured: BOTH ignore the caller's `-target`
-- the plan stage re-plans with none of the caller's args, so a targeted apply is graded on the WHOLE tree.

The ruling, in full: *"the plan stage renders the same plan the apply runs (passes -target/-replace/-var/-var-file/
-refresh/-destroy, or reads the given planfile) and is binding for targeted or planfile applies; the pre-plan stage is
WARN there; untargeted applies unchanged; a targeted plan that cannot render refuses in ENFORCE."*

Build:
1. **`.tools/safe-apply.sh`:** parse the caller's apply args once. For a TARGETED apply (any `-target`) or a PLANFILE
   apply (a positional planfile after `apply`): the plan stage passes exactly the caller's `-target`, `-replace`,
   `-var`, `-var-file`, `-refresh` and `-destroy` args to its `plan` (or, for a planfile, runs `show -json <planfile>`
   with no re-plan); its verdict binds (ENFORCE: refuse, exit 7, nothing applied); a plan that cannot render REFUSES in
   ENFORCE (exit 7) instead of today's WARN gap; the PRE-PLAN stage's verdict is WARN only (never blocks) there. An
   UNTARGETED apply without a planfile: byte-for-byte today's behaviour. Keep every other gate as it is.
2. **`.tools/tests/test_safe_apply_targeted.sh` (new):** the self-test. It runs the script named by env
   `SAFE_APPLY_UNDER_TEST` (default `.tools/safe-apply.sh`) with `SAFE_APPLY_TERRAFORM` pointed at a FAKE terraform
   (a small script in a temp dir that records its argv, writes a fixture plan JSON for `show -json`, and can be told to
   fail `plan`), `NAMING_GATE_ENFORCE=1`, and a temp tree; it isolates the halt checkpoint and the other gates by their
   own env/audited switches or fixtures (never by editing them out). It prints one line per arm -- `PASS: <arm>` or
   `FAIL: <arm>` -- then `RESULT: PASS` only when all five pass:
   - `targeted_plan_carries_caller_args` -- `apply -target=A -var x=y`: the fake's recorded `plan` argv carries
     `-target=A` and `-var x=y`; a pre-plan REFUSE does not block (WARN);
   - `targeted_out_of_pattern_refuses_enforce` -- a targeted apply whose rendered plan adds an out-of-pattern name:
     exit 7, and the fake records NO `apply`;
   - `planfile_apply_grades_given_planfile` -- `apply plan.bin`: the fake records `show -json plan.bin` and NO `plan`;
   - `untargeted_apply_unchanged` -- an untargeted apply: the fake's recorded `plan` argv is today's (no caller args),
     the pre-plan stage still binds;
   - `targeted_unrenderable_refuses_enforce` -- a targeted apply whose `plan` fails: exit 7, NO `apply` recorded.

## 2. BOUNDS

1. Write surface: exactly the `<paths>` below. `naming-apply-gate.py` and `lib/opal_naming.py` are read-only.
2. Never run safe-apply against a real tree or real terraform. No push, no vendor call. REFUSE a criterion you cannot
   meet as written.

## 3. SURFACES

<paths>
.tools/safe-apply.sh
.tools/tests/test_safe_apply_targeted.sh
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~7/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `.tools/naming-apply-gate.py`, `lib/opal_naming.py`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W7-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-s-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/s1.AC1.sh; echo "exit=$?"</invocation><expect>working safe-apply: arms PASS 5 of 5, final RESULT: PASS lines>=1; base safe-apply (0af3c52597): arms PASS fewer than 5 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~7/NFRA_MCPMSP.TO-MS-s-1.safe-apply-targeted-plan.proof_of_spec.json`.
Report once, with: which arms the base bytes fail; the check line; the commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E6 added by the CTO's analysis amendment @6924628218 (msg 27426) on the laptop gate owner's ruling
(msg 103400, relayed 27418). The ruling file @2ee337baf8 is laptop-LOCAL and its "five-arm self-test" is not on site Z:
the five arms here are the issuer's reading of the ruling's five clauses, one arm each (plan carries args / binding
refuse / planfile / untargeted unchanged / unrenderable refuses). Stated as a surprise row for the gate owner to
compare at the laptop push. No open sibling order names `.tools/safe-apply.sh` (LGIC_ENFORCE EN-t-2 and EN-t-2-r2 both
complete). Check dry-run at base: AC1 FAIL as expected (test absent).

<status>complete</status>
<round>2</round>
<slot>~7</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
