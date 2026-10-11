# NFRA_OPLGTW task order -- `OG-fd-1` -- each silver sweep drains only its own family's DLQ messages (round-35 E1), PHASE A: build, prove, ask

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-fd-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-fd-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~58</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- source and tests only; no Lambda is rebuilt or deployed here.
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy changes (the sweep already holds receive/delete/attrs on the DLQ).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-34 analysis @026a983b34 row Z-S91 ruling (cell E1).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-fd-1` (decomposition addendum R3-T.44, E1)

`opal-assets-silver-dlq` is ONE queue, every silver converter's on-failure destination. Each family's sweep
(`run_sweep`, `data/assets/scripts/silver/mirror_conversion.py:956`) calls `drain_dlq` (`:924-944`). That function receives
and DELETES every message up to its cap, whichever family failed, and reports them in its own run. So a family's
failures land in another family's report (row Z-S91: six Schwab failures went to a 16:00Z non-Schwab sweep).

1. Change `drain_dlq` so a sweep keeps ONLY its own family's messages:
   - read each message's family from its on-failure record (the Lambda destination record names the failing function,
     `opal-assets-silver-<family>`);
   - delete and report its own;
   - return every other message to the queue at once (`change_message_visibility`, `VisibilityTimeout=0`), not deleted
     and not in this report;
   - leave a message whose family cannot be read in the queue and count it in the report as `unattributed`. NEVER
     delete it.

   Keep the cap and its truncation report. Update every caller (`run_sweep`; `etf_conversion.py`'s call at `:620`) to
   pass its family.
2. Tests, offline with a fake SQS client, added to `data/assets/scripts/silver/tests/test_mirror_conversion.py`:
   - `test_fd1_ac01`: a planted family-A message survives family B's sweep (visibility reset, not deleted, not in B's
     report);
   - `test_fd1_ac02`: A's sweep then drains it and reports it;
   - `test_fd1_ac03`: an unattributable message is left in the queue and counted unattributed.
3. Source only. The four packaged copies under `infra/aws/lambda/opal-assets/opal-assets-silver-*/` are BUILD SNAPSHOTS.
   At the cut, 0 of 4 equal the source; the eclipse copy lacks 358 lines. Do NOT edit them.
4. The never-widen ask, `W/NEVER_WIDEN_ASK_OG-fd-1.md`, for `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~O`. It carries:
   - the behaviour change;
   - both branches;
   - the per-family PACKAGE delta the deploy would ship: for each of the six families, list what the rebuilt package
     carries beyond this change (the snapshot drift above), by file and line count;
   - the order of deploys;
   - rollback per family;
   - the live grade the applier will run: plant one synthetic family-A message, run family B's sweep, and read that the
     message survives and A's report carries it.
5. Run AC1, commit, REPORT, STOP.
6. **(A1, row Z-W58-S1)** The Schwab Lambda has its OWN `drain_dlq` (`data/assets/scripts/silver/schwab_runtime.py:247`, called at `:380`).
   It still deletes every message on the shared queue. Make it per-family by the same rule (family `schwab`), and add
   `test_fd1_ac04` to `data/assets/scripts/silver/tests/test_schwab_runtime.py`: a planted non-schwab message survives the
   schwab sweep, a schwab message is drained and reported, and an unattributable one is never deleted. Add the Schwab
   package to the ask's per-family delta and deploy order, then run AC2.

## 2. BOUNDS

- The source module, its caller, the tests and the ask. No Lambda build or deploy, no SQS call, no AWS write.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
data/assets/scripts/silver/mirror_conversion.py
data/assets/scripts/silver/etf_conversion.py
data/assets/scripts/silver/tests/test_mirror_conversion.py
data/assets/scripts/silver/schwab_runtime.py
data/assets/scripts/silver/tests/test_schwab_runtime.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~58/`. Rows: id `NFRA_OPLGTW-Z-W58-S<k>`, fabric
`site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC2" cell_refs="OG-fd-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r35/checks/fd1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)test_schwab_runtime\.py: pytest rc=0; named test passed 1 of 1; failed/error lines 0.*test_mirror_conversion\.py: pytest rc=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC1" cell_refs="OG-fd-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r35/checks/fd1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)test_mirror_conversion\.py: pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a sweep keeps only its own family's messages, and nothing is deleted unattributed.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-fd-1.per-family-dlq-drain.proof_of_spec.json`. Validate it AFTER your
LAST commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`; artifact rows pin
to the commit that carried them. Phase A leaves the order `pending`. Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- A1 (issuer, 2026-10-11 ~23:5xZ, row Z-W58-S1): Schwab's own drain_dlq joins the cell (step 6, AC2, paths), so one deploy
  closes the class for all six families. fd1.AC2 base FAIL as expected. Gate limb: GATE (viii) on the modified order.
- Round 35, E1. Pre-cut: fd1.AC1 base FAIL as expected (named tests 0 of 3; the existing suite rc=0, so the harness
  runs). A copy-equality limb was dropped at the cut: copies 0 of 4 equal; they are snapshots, not mirrors.

<status>pending</status>
<round>35</round>
<slot>~58</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
