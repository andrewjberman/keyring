# AMGT_RESAPP task order -- `AMGT-cc-1` -- THE SEGMENTS READER FINDS A STORED TABLE HOWEVER MANY LATER PULLS SIT ABOVE IT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-cc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~308</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a module and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only what the function or the hand-run tool already reads; no new read path is granted by this cell.
comp-adversary: RUN at the cut by the issuer's drafting read (GROUP_A_NOTES.md) -- At the base the reader looks at five objects of a folder; AMD's table sits under later pulls and its read costs 4 bodies where 2 are needed. Every build criterion FAILS at the base and every bound criterion PASSES there; the literal outputs are in that file.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call.
</preflight>

**Your worktree:** `C:/tmp/r79-308` (branch `wk-AMGT_RESAPP-308`, cut from the issuance commit with `--portal-ref d1b21c97`, the portal DEV head at the cut, and no package install). Work and commit only there. Start every shell call with `cd /c/tmp/r79-308`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-cc-1` (round 79, decomposition s.87)

A company's stored Bloomberg segment table sits in one folder, one object per pull. The reader built last round looks at the
five newest objects only. Five later pulls of other fields would hide a stored table, and the reader would then say the table
"has no revenue by business line", which is false: it stopped looking. Change the reader so that it finds the table however
many later pulls sit above it, reads no body it does not need, and says in plain words when it stopped with objects unread.

Edit `lib/research/api/segment_table.py` and its tests `lib/research/api/tests/test_segment_table.py`. Read both whole first.
The function's name, its arguments, the nine keys it returns and every sentence it serves today stay as they are.

1. `MAX_READ` becomes `20`. It is the most object BODIES one call may read. The folder is still listed once, whole, and its
   `.json` keys sorted newest first, exactly as now.
2. Walk the sorted keys newest first and read ONE body at a time. After each body, decide before reading the next:
   - if the object carries a table (the existing `_carries_table` rule: no `PG_REVENUE` field error, and it holds `PG_REVENUE`
     or `PG_OPERATING_INCOME`), it is the chosen object: STOP, read nothing more;
   - otherwise, if it is the first object seen that the existing `_usable` rule accepts, remember it as the fallback;
   - a body whose `response` is not a dictionary counts as one body read and is passed over, as now.
3. Stop reading when `MAX_READ` bodies have been read, whether or not a table was found.
4. Choose:
   - a table was found: that object, and everything after the choice (the source block, the rows, the share-capital and
     one-heading refusals, the no-revenue case) runs exactly as it does today;
   - no table was found and EVERY object of the folder was read: the fallback if there is one (today's second pass: it reads
     the no-revenue sentence with that object as its source), else `REASON_NONE_USABLE`, both exactly as today;
   - no table was found and one or more objects were left unread: return `_result(reason=REASON_NOT_ALL_READ)`: status
     `none`, no rows, no source. This holds even when a fallback was seen. The no-revenue sentence is never served by a call
     that left objects unread.
5. Add the constant, with this exact text:
   `REASON_NOT_ALL_READ = "Bloomberg's %d newest stored pulls for this name hold no business-line table; the older ones were not looked at." % MAX_READ`
6. The function still never raises: any exception is the read-failed reason, as now. Correct the module's opening text to
   describe the walk and the limit.
7. No sentence uses: identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger,
   bronze.

In `lib/research/api/tests/test_segment_table.py`:
8. Keep all seventeen existing test functions, by name. ONE existing assertion changes, and only that one: in
   `test_nothing_objects_none_usable`, `assert len(store.reads) == 5` becomes `assert len(store.reads) == 7` (the folder holds
   seven objects, fewer than the limit, so all seven are read). Add `"REASON_NOT_ALL_READ"` to the names listed in
   `test_reasons_use_plain_words`.
9. Add plant tests: a table under six newer error-free objects with no segment list is served from the table's object; eight
   objects whose newest carries the table read exactly one body; `MAX_READ + 3` objects with no segment list above a table
   read `REASON_NOT_ALL_READ`, exactly `MAX_READ` bodies and no source; a garbled object OLDER than the table is never read
   and the table is served.

You do NOT edit `lib/research/api/scoped_amgt.py`, `lib/research/api/segment_period.py`,
`lib/research/filings/table_class.py` or `lib/research/harvest/store.py`. Criterion AC2 reads the real store (read only):
it writes nothing and neither do you. Run `lib/research/api/tests/` before your commit and report its last line. In your
report, give the bodies read on `AMD_US_Equity` before and after your change.

Run the test folder your module sits in before your commit and report its last line. If a test fails only because it reads a portal file absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W308-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. `lib/research/api/scoped_amgt.py` is READ, never edited.
3. You edit `lib/research/api/segment_table.py` and its test file only.
4. Any sentence you serve to a user is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage, input ledger or bronze.
5. No `bun` command of any kind in this worktree (site Z interim rule: a worktree never installs packages).
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/segment_table.py
lib/research/api/tests/test_segment_table.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~308/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-cc-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc1.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>a table under six newer objects with no segment list is served from its own object; eight objects whose newest carries the table read one body; MAX_READ is 20; objects left unread are said to be unread and never called no revenue, with exactly MAX_READ bodies read; a folder read to its end keeps its round-78 answers; P1-P5 PASS; R79 CC1 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-cc-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc1.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>AMD US serves its rows from the newest stored object that carries the table and reads no body past it; every stored name reads as its whole folder says and reads no body it does not need (N of N); S1-S2 PASS; R79 CC1 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-cc-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_cc1.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>the seventeen round-78 plant cases are all still in test_segment_table.py and the file passes; B1 PASS; R79 CC1 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~308 <0.9.0_WK_AMGT_RESAPP~308@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~308/AMGT_RESAPP.TO-AMGT-cc-1.the-segment-reader-finds-a-stored-table.proof_of_spec.json`.
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

**ISSUER NOTES:** CTO round-78 analysis R1 and enrichment item 1 (bb-1's residual). Drafted in `deliverables/2.0.0_SA_COO~Z/round79/GROUP_A_NOTES.md` (cell A1), committed before the cut, in the issuance commit's ancestry. Checks dry-run at the base: AC1 base: run at the cut, result in the group notes; AC2 base: run at the cut, result in the group notes; AC3 base: run at the cut, result in the group notes.

<status>pending</status>
<round>79</round>
<slot>0.9.0_WK_AMGT_RESAPP~308</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>complete -- drained @0433c23f27; proof VALID rc=0 on the worker's checker; every criterion re-run by the issuer on the shared tree reads SERVED: YES; AMD read from 2 bodies; served only after the adapter cell cc-6</status>
