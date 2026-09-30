# AMGT_HARVST task order -- `HVST-o-2` -- ROUND 25 chain 2 of 4: `run-local.ps1` PASSES `--harvest-grammar`, PROVED WITH A STUB (FWD-1, FWD-3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-o-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~62</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the Scheduled Task 'Opal Data Harvest - Local Publications' runs this script from the working tree; it reads Disabled with 0 triggers (2026-09-30 03:3xZ). This cell does NOT enable, register or run the task; re-arming it is a schedule reserved to Andrew.
comp-iam: RUN at L5 -- no AWS call and no vendor call; the proof replaces the Python executable with a stub that records its argv.
comp-adversary: RUN at L5 -- the adversary is a proof that reads the script's text and never runs it, so a flag added to a dead branch or after an early exit still "passes". AC1 RUNS run-local.ps1 with a stub interpreter and reads the argv it actually received.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL, NO S3 WRITE, NO COLLECTION RUN.** Do not register, enable, run or edit the Scheduled Task, and do not
   run `install-schedule.ps1`.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~62/scripts/`; outputs named `o2_*`
   -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~62/AMGT_HARVST.TO-HVST-o-2.run-local-passes-harvest-grammar.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-o-2.run-local-passes-harvest-grammar`.

<paths>
lib/opal_data_harvest/run-local.ps1
lib/opal_data_harvest/README.md
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~62/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULING (`ledger/CTO_RULING_ROUND24_N4_HOLD_GRAMMAR_FLAG_SILVER_TIE_20260930.md` ruling 2, as amended @`e49bbdb3d2`)

The collector keeps the publisher's received bytes, links the listing object, records rank and page, and writes a run
record ONLY on its `--harvest-grammar` path (`lib/opal_data_harvest/__main__.py` ~:190-194). `run-local.ps1`, the script
the Scheduled Task runs, builds
`$workerArgs = @('-m', 'lib.opal_data_harvest', 'run', '--new-only')` (~:6) without that flag.

**The change:** `run-local.ps1` passes `--harvest-grammar` on its collection run. Nothing else in the script changes:
- the `-AllSecurities` and `-MaxJobs` handling stay;
- the legacy `upload` step stays;
- the exit code stays.

Add one line to `README.md` where it describes `run-local.ps1`.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 600). TWO mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-o-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~62/scripts/o2_ac1_stub_argv.py</invocation><expect>run-local.ps1 is EXECUTED by powershell.exe with -Python pointing at a stub interpreter that records its argv and exits 0, once with no switches and once with -AllSecurities -MaxJobs 2; each recorded collection argv is printed and contains --harvest-grammar together with run and --new-only, and the -AllSecurities / --max-jobs values carry through; the same run against the base script (git show $(git merge-base HEAD CLOUD):lib/opal_data_harvest/run-local.ps1, written to a temp file beside the real one) prints an argv WITHOUT --harvest-grammar</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-o-2"><invocation>python -m pytest lib/opal_data_harvest/ -rA --tb=line</invocation><expect>all pass, with the pass count printed, including the grammar-path tests that prove received bytes are stored beside the rebuild and existing objects are unmoved</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

It does not re-arm the schedule, run the collector, or write to S3. Once this merges, any run of `run-local.ps1` (manual
or scheduled) takes the grammar path.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
- `ROUND_ANALYSIS.round24.md` s.4 item 2, as amended by `1.0.0_SA_CTO~Z` msg 26882 (@`e49bbdb3d2`), on this seat's card
  (msg 26880).
- The Scheduled Task reads Disabled with 0 triggers, so the commit moves no production fire. The cell is therefore a LOCAL
  build with NO pair.
- Re-arming the task is a schedule reserved to Andrew (`HANDOFF_L4_TO_L5_COO_Y_20260922.md:81`), on the CTO's list for
  him.
- AC1's base is `git merge-base HEAD CLOUD`, which is stable whether or not the worker has committed.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>25</round>
<slot>~62</slot>
<fabric>site-z</fabric>
