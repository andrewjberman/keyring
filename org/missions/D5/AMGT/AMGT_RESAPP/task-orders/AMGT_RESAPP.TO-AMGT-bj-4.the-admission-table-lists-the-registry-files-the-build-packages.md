# AMGT_RESAPP task order -- `AMGT-bj-4` -- THE ADMISSION TABLE LISTS THE REGISTRY FILES THE BUILD PACKAGES, READ FROM THE BUILD SCRIPT (AN INSTRUMENT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bj-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~406</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bj-4.the-admission-table-lists-the-registry-files-the-build-packages</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one script, nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- git plumbing and temp directories only; no AWS call.
comp-adversary: RUN at the cut, each arm against the literal string written below: r103_admission_arms.py reads 'arms passed 4 of 5 ... R103 ADMISSION ARMS: NO' against the CURRENT tool (A2 FAILS: it lists a registry file the build does not package) and 'arms passed 5 of 5 ... YES' against the patched tool in a scratch worktree; the patched tool on the real pin 7da642c1ff and ref 6ecb5bc567 prints 12 members including `exemptions.json` and `scopes.json` and no `firm_pages.json`, which is the twelve RA1's build printed (5 packaged).
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-406` (branch `wk-AMGT_RESAPP-406`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-406`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bj-4` (round 103, decomposition s.111)

CTO~DELL1 round-102 analysis item 3 (ADDENDUM 1 of the round-102 pair, msg 4929): `r94_admission_table.py` must diff EVERY registry file the build packages, not a fixed two, and its arms are
a build that packages `exemptions.json` (must list it) and a build that packages none (must list none). The build script `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh` states
what it packages in `NAMING_REGISTRY_FILES` (seven files) and `org/standards/NAMING_SCHEMA.json`. The tool must READ that rule from the script (at the pin and at the ref), not type it.

Apply the prepared edit, then verify it. The patch is the whole of the change (ONE file, `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py`):

    cd C:/dev/wk-resapp-406 && git apply --whitespace=nowarn "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/r103_admission_table.patch"

What it does: adds `packaged_registry(ref)`, which reads `NAMING_REGISTRY_FILES` (and `NAMING_SCHEMA.json` when the script names it) from the build script AT that ref, and the registry members of the
table become the files in that list at the pin or the ref whose blob differs. If `git apply` refuses, STOP and file a BLOCKING row: do not edit by hand.

Then run AC1. The arms script builds throwaway git repositories in a temp directory (it writes nothing else): a ref that changes `exemptions.json` lists it; a ref that changes only
`firm_pages.json` (in the folder, not packaged) lists none; a ref that changes no registry file lists none; a script that adds `feeds.json` to the rule lists a changed `feeds.json`; a
`lib/` change is still listed.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W406-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. ONE file, `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py`, changed by the prepared patch and nothing else.
2. No AWS call, no network, no deploy, no store write. No `pip install`. Standing: no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~406/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bj-4"><invocation>cd C:/dev/wk-resapp-406 &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_admission_arms.py" --instrument "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py" | tail -7; echo "exit=${PIPESTATUS[0]}"</invocation><expect>five PASS rows (A1 to A5), `arms passed 5 of 5`, `R103 ADMISSION ARMS: YES`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bj-4"><invocation>cd C:/dev/wk-resapp-406 &amp;&amp; git diff --name-only "$(git merge-base HEAD box/dell1)" HEAD -- . ":(exclude)org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~406" ":(exclude)org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel" | sort</invocation><expect>exactly one line, `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py`, and no other line</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~406 <0.9.0_WK_AMGT_RESAPP~406@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~406/AMGT_RESAPP.TO-AMGT-bj-4.the-admission-table-lists-the-registry-files-the-build-packages.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- criterion AC1's and AC2's output lines;
- the tool's table for `6ecb5bc567 --pin 7da642c1ff` (first 14 lines);
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 102's pair named eleven members because this tool diffed two registry files; RA1's build printed a twelfth (`exemptions.json`) and stopped. The tool's output is an
ADMISSION aid; the build's own content diff stays the authority on what ships. The arms are the CTO's wording.

<status>complete -- 2026-10-13T18:0xZ by the issuer (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-406 @1d17d3cd4b (fix b5c16e920a) merged, proof instance VALID (rc=0). AC1 re-run by the issuer on the worker's tree: five PASS rows, arms passed 5 of 5, R103 ADMISSION ARMS: YES (the pre-patch tool reads 4 of 5 NO at A2); the tool on the real pin 7da642c1ff and ref 6ecb5bc567 prints TWELVE members including exemptions.json and scopes.json and no firm_pages.json. AMENDMENT 1 (the issuer's own order, no gate limb graded it: a modification): AC2's pathspec excluded the worker's deliverables folder but not the surprise channel, so a worker that files a row (the order's own grant) put INVESTIGATION_v1.md in the diff and AC2 read 2 lines; the pathspec now also excludes `surprise-channel`, and the issuer re-ran the AMENDED invocation on the worker's tree: exactly one line, r94_admission_table.py. Rows: W406-S1 (INERT: the worktree was cut one commit after the issuance) and S2 (INERT: the lib/ filter drops `/tests/` and `_test.py` only, so test_*.py modules are listed, which over-lists and never under-lists) are DISMISSED with no action; S3 (BLOCKING, INERT: AC2's one-line expectation could not hold beside the order's own rows) is DISMISSED, its cause the issuer's pathspec, corrected by AMENDMENT 1. The tool's output is an ADMISSION aid; the build's own content diff stays the authority.</status>
<round>103</round>
<slot>0.9.0_WK_AMGT_RESAPP~406</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
