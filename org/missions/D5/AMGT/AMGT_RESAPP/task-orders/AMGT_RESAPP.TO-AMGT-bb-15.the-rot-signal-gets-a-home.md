# AMGT_RESAPP task order -- `AMGT-bb-15` -- THE ROT SIGNAL GETS A HOME ITS OWN MODULE OWNS (ROW Z-W279-S2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-15</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~300</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_C_NOTES.md) -- The glob matches 1 file, in a worker folder, computed 2026-09-10; its only writer is rot.main(). Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r78-300` (branch `wk-AMGT_RESAPP-300`, cut from the issuance commit with `--portal-ref ba391aff`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r78-300`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-bb-15` (round 78, decomposition s.86)

Row AMGT_RESAPP-Z-W279-S2. `lib/research/freshness/build_view.py` finds the lists' rot signal with a glob over every
worker's deliverables folder (`ROT_SIGNAL_GLOB`). Production code must not read a worker's folder. Give the signal ONE
home, owned by the module that computes it, and make `build_view` read only that home.

1. **Copy, never move.** Copy
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/lists/rot_signal.json` byte for byte to
   `lib/research/lists/data/rot_signal.json`. The original stays where it is, unchanged.
2. **`lib/research/lists/rot.py`** gains `SIGNAL_HOME`: the path `data/rot_signal.json` beside the module's own file,
   worked out from `__file__` (no absolute path typed, no device path). Add one docstring line saying this is the
   signal's one home and that `python -m lib.research.lists.rot lib/research/lists/data` writes it there. Nothing else in
   `rot.py` changes: `main()` still writes beside the folder it is given, and you do not run it.
3. **`lib/research/freshness/build_view.py`:** remove `ROT_SIGNAL_GLOB`, its comment block and `import glob`.
   `find_rot_signal_path()` keeps its name and its return type and now answers `Path(rot.SIGNAL_HOME)` when that file
   exists, else `None`. It reads `rot.SIGNAL_HOME` each time it is called (through the module, not a copy taken at import).
   Import `lib.research.lists.rot` at the top of the module; it imports only the standard library. `load_rot_data`,
   `render_rot_signal`, `build` and `main` do not change. Correct the two docstring passages that describe the glob.
4. **A new test file `lib/research/freshness/tests/test_rot_home.py`** with `test_the_view_reads_the_signal_from_its_home`
   (the path found is `rot.SIGNAL_HOME`; with `rot.SIGNAL_HOME` set to a missing file, the path is `None` and the line is
   `build_view.NO_ROT_SIGNAL`) and one test that no line of `build_view.py` names a deliverables folder.

Rules:
1. You do NOT edit `lib/research/api/scoped_amgt.py`, the build script under `infra/`, or
   `lib/research/identity/tests/test_slash_safe_key_sites.py` (it must keep passing: it stubs `find_rot_signal_path` by
   that name).
2. You do not run `rot.main()` or `python -m lib.research.lists.rot`: it looks up every publisher domain, which is a
   network act nobody asked for. The copy in step 1 is the whole content change.
3. The line the view renders must not change (AC3).
4. No deploy, no store write, no vendor call. You do not delete or edit anything under a worker's deliverables folder.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W300-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited.
3. Copy, never move: the worker folder's file stays where it is.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/lists/rot.py
lib/research/lists/data/rot_signal.json
lib/research/freshness/build_view.py
lib/research/freshness/tests/test_rot_home.py
lib/research/lists/tests/test_rot.py                   (read only; it must keep passing)
lib/research/identity/tests/test_slash_safe_key_sites.py   (read only; it must keep passing)
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~300/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bb-15"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb15.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>build_view names no worker folder for the signal; rot.SIGNAL_HOME is inside lib/research/lists/, holds a byte-equal copy, and the worker folder's file is still there; the view finds the signal at its home; an absent signal reads as no signal; C1-C4 PASS; R78 BB15 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-15"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb15.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>test_rot_home.py holds test_the_view_reads_the_signal_from_its_home, and it and lib/research/lists/tests/test_rot.py pass; R78 BB15 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bb-15"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_bb15.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>the view renders the same line as at the cut; R78 BB15 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~300 <0.9.0_WK_AMGT_RESAPP~300@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~300/AMGT_RESAPP.TO-AMGT-bb-15.the-rot-signal-gets-a-home.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the test folder's last line;
- the hookup another cell must make for your work to be served, or that none is needed;
- anything your read of the code found that this order did not say;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-77 ruling 14, row Z-W279-S2. Drafted in `deliverables/2.0.0_SA_COO~Z/round78/GROUP_C_NOTES.md` (cell C6), committed @643863854d before the cut. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes; AC3 base: run at the cut, result in the group notes.

<status>pending</status>
<round>78</round>
<slot>0.9.0_WK_AMGT_RESAPP~300</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete -- drained @b68f3c888b; proof VALID rc=0 on the worker's checker; every criterion re-run by the issuer on the shared tree reads exit 0 and SERVED: YES; the data file must be in the redeploy's closure (issuer reads it at the bb-18 pair)</status>
<status>complete -- CORRECTION by the issuer (2026-10-07): the note above that the data file must be in the redeploy's closure was the issuer's assumption and is wrong; measured for the bb-18 pair, rot_signal.json is not packaged and no served route opens it (/freshness computes the register in memory); nothing else of the status changes</status>
