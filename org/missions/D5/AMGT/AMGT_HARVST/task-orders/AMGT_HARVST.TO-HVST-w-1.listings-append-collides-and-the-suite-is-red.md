# AMGT_HARVST task order -- `HVST-w-1` -- ROUND 8 cell 1 of 2 ISSUED: the LISTINGS silver append bypasses the collision retry the ARTICLES path already uses, plus the 3 red tests and one lying help string

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-w-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~23</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on lib/opal_data_harvest; this cell arms nothing and deploys nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no vendor call. The collision criterion runs against a FAKE s3 client in-process; it never touches the live bucket.
comp-adversary: DECLARED-NOT-APPLICABLE -- a source change graded by its own tests, not a produced artifact.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL. NO NETWORK. NO S3 WRITE, and no S3 READ.** This cell changes a caller and runs tests.
   If you find yourself needing the network, STOP and file a BLOCKING row.
2. **NO S3 DELETE OF ANY KIND**, here or anywhere.
3. **DO NOT TOUCH `lib/research/harvest/store.py`.** `silver_append` there is the chokepoint EVERY silver
   table in the estate writes through, including pipelines this project does not own. **It is not in your
   write grant and editing it fails the cell even if the tests pass.** The fix for criterion 1 is at the
   CALLER and nowhere else.
4. **PUT YOUR CHECK SCRIPTS IN**
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~23/scripts/` -- **never `.scratch/`.**
   `.scratch/` does not survive the drain and an issuer structurally cannot relocate your files afterwards.
5. **Your write surface is exactly the `<paths>` below.** Anything else is a BLOCKING row, not a workaround.

<paths>
lib/opal_data_harvest/uploads.py
lib/opal_data_harvest/__main__.py
lib/opal_data_harvest/tests/
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~23/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CELL -- `HVST-w-1`

**Three repairs that all sit UNDER the capture cell.** This lands before any capture because criterion 1 owns
the exact write path a capture writes through. You are not being asked to find any of these three; each is
isolated below with the bytes that prove it.

## 2. CRITERION 1's DEFECT, ALREADY MEASURED BY THE ISSUER -- do not re-derive it

**Row `AMGT_HARVST-Z-W9-S1`, listings half, ARMED.**

`store.silver_append` puts `part-<run_stamp>.parquet` with an unconditional `IfNoneMatch="*"`. That is a **NAME
collision, never a content check**, and `run_stamp` is **SECOND-PRECISION**
(`harvest_grammar.store.stamp(fetched_at)`). So **two appends for one source inside one second collide**, and
the second raises `PreconditionFailed`.

⭐ **THE ARTICLES PATH ALREADY SOLVED THIS. THE LISTINGS PATH BYPASSES THE SOLUTION.** Measured at the bytes:

- `uploads.py:19` defines `_silver_append_retrying_object_name`, which retries under a suffixed stamp
  (`"%s-r%d"`). Its own docstring says it is *"Shared by LegacyUploader (HVST-h-9) and HarvestUploader
  (HVST-h-3 item 8 ... disarming row AMGT_HARVST-Z-W9-S1)."*
- The ARTICLES path additionally **groups by `(source, run_stamp)` into ONE call per group**
  (`uploads.py:174-176`, `groups.setdefault(...)`).
- ⛔ **`uploads.py:277` -- the LISTINGS path -- calls `harvest_grammar.store.silver_append` DIRECTLY**, with no
  retry wrapper, **inside the per-listing loop**, so it is neither retried nor grouped.

**So the row's articles half is genuinely disarmed and its listings half is genuinely still armed.** The
docstring's claim to have disarmed `Z-W9-S1` is true of one channel only -- which is why the row stayed armed
and why this criterion exists.

**NOTE, so you do not report it as a defect:** the SECOND definition at `uploads.py:442` is a deliberate thin
same-named method wrapper whose docstring explains why it was kept. **It is not a duplicate to clean up.**

## 3. CRITERION 2's DEFECT -- the suite is RED AT HEAD, and one of the three is not a logic failure

**Row `AMGT_HARVST-Z-W21-S2`.** The suite was **already red before round 7 touched anything: 3 failed / 160
passed.** ⛔ **One of the three is `WinError 183`, a FILESYSTEM-STATE failure, not a logic failure.** Do not
force it green by changing what it asserts. If it is environmental, **say so with the error text and leave the
assertion alone** -- a test repaired by weakening it is worse than a red test, because the red one is honest.

## 4. CRITERION 3's DEFECT -- a help string that asserts the belief that broke round 6

**Row `AMGT_HARVST-Z-S27`.** `--harvest-grammar`'s help text says **"writes"** for a flag that **writes
nothing to S3**. Read alone it asserts exactly the belief that produced round 6's failure. A text fix.

## 5. BOUNDS

1. **Criterion 1 is PUBLISHER-NEUTRAL or it is not the fix.** Do not special-case `sa`. ft, barrons, bbg and
   wsj have barely written a `listing_hit` row, so the first time any of them writes two in one second it
   fails identically -- and invisibly, because the capture returns rc=0 and only the upload raises.
2. **No behaviour change to the ARTICLES path.** It already works; criterion 1 brings listings up to it.
3. **Do not widen `max_attempts`** or invent a new retry policy. Reuse the existing wrapper.
4. **Three mechanical criteria, no fourth.** If you find a fourth defect, it is a surprise ROW and you keep
   working.

## 6. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical criteria, no judgment criterion

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-w-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~23/scripts/ac1_listing_collision.py</invocation><expect>TWO LISTING APPENDS INSIDE ONE SECOND BOTH LAND, proved against a FAKE in-process s3 client that raises PreconditionFailed on a repeated key exactly as S3 does. Print, in order: (a) a NEGATIVE CONTROL at HEAD's behaviour -- the direct `store.silver_append` call site raising PreconditionFailed on the second append, with the exception text verbatim; (b) the same two appends through the repaired call site, BOTH returning a receipt, with the two distinct object names printed so the suffixed retry is visible; (c) the ROW COUNT landed across both keys, equal to the sum of the two row sets with NO row dropped. A pass requires the negative control to FAIL at HEAD -- a criterion that passes without ever reproducing the defect proves nothing</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-w-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest lib/research/harvest/tests/ lib/opal_data_harvest/tests/ -rA 2>&amp;1 | tail -60</invocation><expect>the BEFORE and AFTER counts both stated with every failing test named. `-rA` is used deliberately because `-q` NEVER PRINTS A PASSING TEST'S NODEID, which made a round-7 criterion unsatisfiable by construction (row Z-W21-S1). Expected direction: 3 failed / 160 passed at HEAD moves toward 0 failed, and any test still failing is named with its error text. ⛔ THE WinError 183 CASE IS AN ACCEPTED OUTCOME REPORTED WITH ITS CAUSE, not a failure of this cell: if it is filesystem state rather than logic, say so and LEAVE THE ASSERTION ALONE. A test made green by weakening what it asserts FAILS this criterion</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-w-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m lib.opal_data_harvest run --help 2>&amp;1 | grep -A3 "harvest-grammar"</invocation><expect>the `--harvest-grammar` help text NO LONGER SAYS "writes" for a flag that writes nothing to S3 (row Z-S27). Print the OLD string and the NEW string. The new text states what the flag actually does -- turns on the harvest-grammar bronze/silver row BUILD and passes a harvest_client to Worker -- and does not imply an S3 write</expect></criterion>
</proof_of_spec>

## 7. WHAT THIS CELL DOES NOT DO

It does not touch `lib/research/harvest/store.py`. It does not change the articles path. It makes no vendor
call, no network call and no S3 call of any kind. It does not capture anything -- the capture cell is CARDED at
Andrew pending a per-use vendor word and is not yours.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Criterion 1's scope was set by a measurement, not by the analysis's wording.** The round-7 analysis
   called this a `lib/opal_data_harvest/` repair; I confirmed that is exactly right by reading the two call
   sites. Had the fix needed `store.py`, this cell could not have been cut at LOCAL at all -- that is a
   never-widen surface with no sign-off here.
2. **AC1 demands its own negative control.** Round 7's lesson: a mechanical criterion that never reproduces
   the defect passes over an empty set. The control makes the defect appear before the fix removes it.
3. **AC2 deliberately tolerates a named failure.** The WinError 183 test is environmental; ordering a worker
   to make it green invites exactly the assertion-weakening that hides a real regression.
4. **No judgment criterion here.** Round 8's judgment criterion belongs on the CAPTURE cell (`w-2`), where a
   green mechanical column can hide a wrong result. This cell's three criteria are all mechanically decidable.

<risk>LOCAL</risk>
<status>pending</status>
<round>8</round>
<slot>~23</slot>
<fabric>site-z</fabric>
