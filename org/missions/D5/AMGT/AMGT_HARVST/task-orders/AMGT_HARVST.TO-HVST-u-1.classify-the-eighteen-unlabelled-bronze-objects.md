# AMGT_HARVST task order -- `HVST-u-1` -- ROUND 4, the only cell: CLASSIFY all 18 unlabelled bronze objects across FIVE subtrees and produce the exact labelling plan. READ-ONLY. NO WRITE OF ANY KIND, NO DELETE, NO VENDOR CALL

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-u-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~18</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on lib/opal_data_harvest; this cell arms nothing, deploys nothing, and writes no object anywhere.
comp-iam: RUN at L5 on the DESIRED plane only; this cell needs S3 GET and LIST on opal-data-harvest and makes NO write, so a refusal on a read is a BLOCKING row.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~18`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/`, `integrations/` and every path in section 3 exist. If any is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~18;`.
- **NEVER RUN AN INSTALL. NEVER CALL A PUBLISHER. NEVER RUN THE HARVESTER's `run` OR `upload-*`.**

## 0. THE STANDING CLAUSE, first because it is absolute

**NO S3 DELETE OF ANY KIND -- not an object, not a noncurrent version, not a delete marker -- without Andrew's
word.** Removing a delete marker is itself a delete. **AND THIS CELL ALSO WRITES NOTHING AT ALL:** no `put_object`,
no `copy_object`, no metadata replace, no upload. **A never-overwrite refusal is a finding to file, never an
obstacle to get around.** Tonight a worker on a sibling project deleted 123 S3 objects on its own judgment to
escape exactly such a precondition; that is a hard-stop breach now carried to Andrew. **If you find yourself
reasoning toward any write, STOP and file a BLOCKING row instead.**

## 1. THE CELL, inlined in full -- `HVST-u-1` (manifest row H1, the backward half of FWD-1)

**WHERE `Z-S1` NOW STANDS, and the scope fell by more than tenfold because two seats COUNTED.** `Z-S1` claimed
bronze held `raw_bytes` that were re-serialisations rather than received bytes. The forward fix landed in round 1
and was proven in rounds 2 and 3. **The backward half is what is already in the store**, and its true size was
measured only after `3.0.0_SA_CVO~Z` counted the population instead of accepting the row's stated scope:

| received-form | count | what it is |
|---|---|---|
| `as_received` | 16 | proven, the forward fix working |
| `bbg-client-json` | 115 | the Bloomberg data subtrees, a DISCLOSED state |
| `normalised_record` | 83 | **NOT a defect -- a DISCLOSED state, which is what the metadata rule exists for** |
| **no label at all** | **18** | **THIS CELL'S POPULATION** |

**THE 18, DECOMPOSED -- and the decomposition is the whole point** (issuer's row `Z-S12`). They are ALL
seeking-alpha and they span **FIVE subtrees**:

`article` 6, `analysis` 3, `news` 3, `report` 3, `symbol` 3.

**A cell scoped to `article` alone would cover 6 of 18 and report a clean pass.** Your denominator is 18, and your
output prints the per-subtree counts so a reader can see all five were reached.

**RULED -- what you build, and it produces a PLAN rather than a change:**
1. **A classifier at `lib/opal_data_harvest/classify_unlabelled_bronze.py`**, read-only against S3, which for EACH
   of the 18 objects:
   - LISTS the unlabelled set itself rather than taking a hard-coded key list -- **the population is derived by
     reading metadata, so it stays correct if the store moves**;
   - reads the object's STORED BYTES and classifies them by what they ARE: canonically re-serialised JSON, a
     transport-shaped JSON body that is not canonical, HTML, or INDETERMINATE;
   - states the EVIDENCE for each verdict in one line (for example: equals `json.dumps(json.loads(body))`, so it is
     canonical; or differs in key order and separators, so it is transport-shaped);
   - proposes the `received-form` value that object WOULD take, and prints it as a PROPOSAL;
   - prints per object: `key <key> subtree <s> bytes <n> class <c> proposed <label> evidence <text>`.
2. **THE DENOMINATOR AND THE SUBTREE BREAKDOWN**: `objects 18 of 18`, the five per-subtree counts, and an explicit
   `undetermined <n>`. **Any object you cannot classify is UNDETERMINED with its reason. Never label by default and
   never guess.**
3. **A NEGATIVE CONTROL, the load-bearing arm:** arms proving the classifier DISCRIMINATES -- a canonically
   re-serialised body is classified canonical and a deliberately non-canonical one is NOT, and an unparseable body
   reports INDETERMINATE rather than falling into a class.
4. **PROOF THAT NOTHING WAS WRITTEN.** Poison the S3 client's `put_object`, `copy_object`, `delete_object`,
   `delete_objects` and `upload_file` so any call RAISES, print a POSITIVE CONTROL showing each raises when
   deliberately tripped, and print `write_calls 0` **from a counter, never as a literal.**

**What this cell does NOT do:**
- **it does not LABEL anything.** The metadata write is a separate question the issuer has asked of
  `1.0.0_SA_CTO~Z` and has NOT decided. Your deliverable is the plan;
- it does not re-fetch, and it makes no vendor call;
- it does not touch the 83 `normalised_record`, the 115 `bbg-client-json`, the 246 sibling research-report objects,
  or anything served;
- **it does not close `FWD-1`.** The analysis says round 4 does not, three of five publishers remain unmeasured
  live, and the listing pages round 1 discarded are gone. **Do not write a sentence that implies otherwise.**

## 2. WHERE THIS CAME FROM
Round 4, decomposition v1.3 @HEAD section 15a, the only cell, from the round-3 analysis @`4bcd9e87ca` ranked item 1.

## 3. SURFACES -- what you may read and write

<paths>
lib/opal_data_harvest/classify_unlabelled_bronze.py
lib/opal_data_harvest/test_classify_unlabelled_bronze.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~18/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-u-1.classify-the-eighteen-unlabelled-bronze-objects.md
</paths>

**READ-ONLY REFERENCES -- read these; they are deliberately NOT in the write grant:**
- `lib/opal_data_harvest/harvest_grammar.py` -- where `received_form` is set and what values exist.
- `lib/opal_data_harvest/check_as_received.py` -- round 2's shape test, the closest prior art.
- `lib/opal_data_harvest/exercise_as_received.py` -- round 3's stub-driving and poison pattern.
- `lib/research/harvest/store.py` -- the bucket constant and key grammar.

- **Only the two named files may CHANGE.** AC3 fails if anything else under `lib` changes.
- Scratch goes in `<your worktree>/.scratch/u1/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~18 <0.9.0_WK_AMGT_HARVST~18@opal.agent>" -F <msgfile> -- <paths>`.
  Write the message file with a non-shell writer.

## 4. BOUNDS
- **READ-ONLY. NO WRITE, NO DELETE, NO VENDOR CALL. Pure ASCII, LF only.**
- **BASELINES, AND THE CHECKOUT THEY WERE MEASURED IN.** Measured by the issuer in the **FULL SHARED WORKTREE**
  after the round-3 drain: `test_check_as_received` 16 passed, `test_exercise_as_received` 9,
  `test_listing_persist_durability` 4, `test_bronze_capture` 12, `test_retrieval_provenance` 18,
  `test_poison_control` 3, `test_harvest_grammar` 7. **IF A COUNT DIVERGES IN YOUR WORKTREE, FILE A ROW -- it is an
  ENVIRONMENT finding, not a repository defect and not yours to work around.**
- **THE STORE IS THE AUTHORITY ON THE POPULATION.** If your own listing finds a count other than 18, or subtree
  counts other than 6/3/3/3/3, **report YOUR measurement with its denominator and file a row.** The issuer's
  numbers are a measurement from about an hour before this cut, not a specification.
- **Surprise rows:** `AMGT_HARVST-Z-W18-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-u-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/opal_data_harvest/test_classify_unlabelled_bronze.py -v --color=no -p no:cacheprovider 2>&1 | tail -16</invocation><expect>every arm passes and no "failed" -- including the NEGATIVE CONTROL arms proving the classifier discriminates (a canonically re-serialised body classifies canonical, a deliberately non-canonical one does NOT, an unparseable body reports INDETERMINATE rather than falling into a class)</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-u-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.opal_data_harvest.classify_unlabelled_bronze</invocation><expect>one line per object carrying key, subtree, bytes, class, proposed label and evidence; "objects 18 of 18" with the five per-subtree counts printed (article, analysis, news, report, symbol); an explicit "undetermined n"; and the population DERIVED by reading metadata rather than from a hard-coded key list</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-u-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/u1/ac3.py</invocation><expect>"outside_allowed []" -- only classify_unlabelled_bronze.py and test_classify_unlabelled_bronze.py changed, nothing else under lib; each changed file prints "compiles True crlf 0 non_ascii 0"</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-u-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/u1/ac4.py</invocation><expect>"write_calls 0" read from a counter, and a POSITIVE CONTROL showing each of put_object, copy_object, delete_object, delete_objects and upload_file RAISES when deliberately tripped -- proof that the classification wrote nothing and could not have</expect></criterion>
</proof_of_spec>

Write `.scratch/u1/ac3.py` (the allowed-set diff from `git merge-base HEAD SITEZ` over `lib`, plus a compile, CRLF and
non-ASCII print per changed file) and `.scratch/u1/ac4.py` (the write-poison counter and its positive control).

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~18/AMGT_HARVST.TO-HVST-u-1.classify-the-eighteen-unlabelled-bronze-objects.proof_of_spec.json`.
2. Grade with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4`, which must return rc 0.
3. Flip to `complete` only if every criterion passes. **An UNDETERMINED count above zero does NOT block the flip** --
   an honest classification with a stated residue is the deliverable, not a full sweep.
4. Commit with `--only`.
5. Report once, with the per-subtree counts, the class distribution, the undetermined count, and `write_calls 0`.
   **Say plainly that nothing was labelled and that this does not close FWD-1.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **The write is deliberately NOT in this cell** and section 15e records why: labelling means a copy onto an
   existing key against a never-overwrite precondition, and tonight a sibling project's worker deleted 123 objects
   to escape exactly that. Handing a worker a task whose success requires getting past that guard recreates the
   breach conditions. The question is asked of the CTO in the same turn as this cut.
2. **The population is given DECOMPOSED, and the order says the store is the authority.** The analysis said 18
   without a breakdown; row `Z-S12` supplies the five subtrees. A cell told only "18" would very likely have swept
   `article` and reported 6 of 6.
3. **AC4 exists because of the breach, not because of a suspicion.** A read-only cell that proves it could not have
   written is cheap, and it is the right shape to normalise while the hard stop is live.

<status>pending</status>
<round>4</round>
<slot>~18</slot>
<fabric>site-z</fabric>
