# AMGT_HARVST task order -- `HVST-t-2` -- ROUND 3: EXERCISE the as-received capture on the three publisher paths that have NO live object, offline and stub-driven, so `Z-S1` stops resting on two paths of five; NO vendor call, NO S3 write

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-t-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~17</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on lib/opal_data_harvest; this cell arms nothing and writes nothing anywhere.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the bronze writer is driven with a STUB client.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~17`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/`, `integrations/` and every path in section 3 exist. If any is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~17;`.
- **NEVER RUN AN INSTALL. NEVER CALL A PUBLISHER OR AWS. NEVER WRITE AN S3 OBJECT. NEVER RUN THE HARVESTER's `run`
  OR `upload-*`.** Every response and every store in this cell is a stub you write.

## 1. THE CELL, inlined in full -- `HVST-t-2` (manifest row H1, outcome FWD-1)

**WHERE `Z-S1` ACTUALLY STANDS, with numbers rather than adjectives.** `C-HV-BRONZE-AS-RECEIVED` requires bronze to
hold the bytes the publisher sent. `HVST-h-1` moved capture to `PacedSession.get`. `HVST-r-2` then PROVED it, with a
printed check, on the paths that have live objects: **seeking-alpha 3 of 3 and wsj 11 of 11, `mismatch 0` on both**
-- and reported bloomberg, barrons and ft **UNPROVEN, honestly, because those paths landed no object at all.**

**THE ISSUER'S OWN CENSUS GIVES THE DENOMINATOR** (boto3 metadata read over every key under the bronze article
prefix, an instrument the cell's checker does not use): **103 objects, 14 `as_received`, 83 `normalised_record`, 6
carrying no `received-form` key at all.**

**THE DISTINCTION THIS CELL RESTS ON, and it is Rule 22's ABSENT-versus-EXERCISED-AGAINST:** those three paths are
**UNEXERCISED, not broken.** Nobody has shown the capture fails there; nobody has shown it works either. **And an
EXERCISE does not need the network.**

**RULED -- what you build:**
1. **An exercise at `lib/opal_data_harvest/exercise_as_received.py`**, offline, which for EACH of the five publisher
   paths:
   - drives that path with a STUB response whose body is fixed, known bytes -- **including a JSON body that is
     deliberately NOT canonically serialised** (odd key order, unusual separators, an escape) so a
     re-serialisation is detectable;
   - runs the REAL capture and the REAL bronze article writer against a STUB S3 client;
   - asserts the bytes handed to the stub store are **BYTE FOR BYTE** the stub response's bytes;
   - prints, PER PUBLISHER: `publisher <code> exercised <bool> byte_equal <bool> received_form <value> reason <text>`;
   - prints the DENOMINATOR: `paths_exercised <n> of 5` and `byte_equal <n> of <n>`.
2. **A NEGATIVE CONTROL, and it is the load-bearing arm:** an arm that substitutes a `json.dumps` RE-SERIALISATION
   of the same body and requires the check to REPORT FAILURE. **An instrument that cannot report the bad case
   reports nothing** -- `HVST-r-2` and `HVST-r-5` both carry this arm and it is why their results were believed.
3. **THE BOUND, printed in the output and repeated in your report:** this cell proves the CODE PATH preserves bytes
   for a stub response. **It does NOT prove anything about what those publishers' live servers send, and it does
   NOT relabel the 83 `normalised_record` objects or the 6 unlabelled ones already in bronze.** Print that
   sentence.
4. **THE POISON, NAMED**, because a no-network PASS with no poison proven is an ABSENCE: poison `PacedSession.get`'s
   real transport, `SessionManager.refresh` and `subprocess.run`, print a POSITIVE CONTROL showing each raises when
   tripped, and print `vendor_calls 0` **from a counter, never as a literal.** Read `conftest.py` first; do not
   duplicate what the package poison already covers.

**What this cell does NOT do:**
- it does not re-fetch anything, and it does not touch the 89 non-`as_received` objects;
- it does not modify `check_as_received.py` -- `HVST-r-2`'s checker is READ-ONLY here, so its graded result stays
  exactly as adjudicated;
- it does not claim a path is PROVEN against a live server. **If the exercise finds a path that does NOT preserve
  bytes, that is a FINDING, a row and a round-4 candidate, not a repair in this cell.**

## 2. WHERE THIS CAME FROM
Round 3, decomposition v1.2 @04329b6a4c section 12a, cell 2 of 2, from the round-2 analysis's ranked item `Z-S1`.
Independent of `HVST-t-1`.

## 3. SURFACES -- what you may read and write

<paths>
lib/opal_data_harvest/exercise_as_received.py
lib/opal_data_harvest/test_exercise_as_received.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~17/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-t-2.exercise-as-received-on-the-three-silent-paths.md
</paths>

**READ-ONLY REFERENCES -- read these; they are deliberately NOT in the write grant:**
- `lib/opal_data_harvest/transport.py` -- where `PacedSession.get` captures the response.
- `lib/opal_data_harvest/publishers.py` -- the five article paths.
- `lib/opal_data_harvest/harvest_grammar.py` -- `put_article_bronze` and `received_form`.
- `lib/opal_data_harvest/check_as_received.py` -- `HVST-r-2`'s checker, for its shape test; **do not edit it.**
- `lib/opal_data_harvest/census_listing_capture.py` -- `HVST-r-5`'s stub-driving and poison pattern.
- `lib/opal_data_harvest/conftest.py` -- the package poison.

- **Only the two named files may CHANGE.** AC3 fails if anything else under `lib` changes.
- Scratch goes in `<your worktree>/.scratch/t2/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~17 <0.9.0_WK_AMGT_HARVST~17@opal.agent>" -F <msgfile> -- <paths>`.
  Write the message file with a non-shell writer.

## 4. BOUNDS
- **OFFLINE ONLY. NO S3 WRITE. NO VENDOR CALL. Pure ASCII, LF only.**
- **A path you cannot drive with a stub is reported UNEXERCISED with its reason, never assumed to preserve bytes.**
- **BASELINES, AND THE CHECKOUT THEY WERE MEASURED IN.** Measured by the issuer in the **FULL SHARED WORKTREE** at
  the round-2 drain: `test_check_as_received` 16 passed, `test_bronze_capture` 12, `test_retrieval_provenance` 18,
  `test_listing_capture_census` 18, `test_poison_control` 3, `test_harvest_grammar` 7.
  **IF A COUNT DIVERGES IN YOUR WORKTREE, FILE A ROW -- it is an ENVIRONMENT finding, not a repository defect and
  not yours to work around.** Row `Z-S4` is the issuer's own instance of exactly that from last round.
- **Surprise rows:** `AMGT_HARVST-Z-W17-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-t-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/opal_data_harvest/test_exercise_as_received.py -v --color=no -p no:cacheprovider 2>&1 | tail -16</invocation><expect>every arm passes and no "failed" -- including the NEGATIVE CONTROL arm where a json.dumps re-serialisation is substituted for the stub body and the check REPORTS FAILURE, and an arm proving a path that cannot be driven is reported UNEXERCISED rather than assumed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-t-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.opal_data_harvest.exercise_as_received</invocation><expect>five publisher lines each carrying exercised, byte_equal, received_form and reason; "paths_exercised n of 5"; "byte_equal n of n"; "vendor_calls 0" from a counter; the poison's POSITIVE CONTROL showing all three sites RAISE when tripped; and the BOUND sentence stating that this proves the CODE PATH preserves bytes for a stub response, not what a live server sends, and that it relabels no object already in bronze</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-t-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/t2/ac3.py</invocation><expect>"outside_allowed []" -- only exercise_as_received.py and test_exercise_as_received.py changed, nothing else under lib, and check_as_received.py explicitly UNCHANGED; each changed file prints "compiles True crlf 0 non_ascii 0"</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-t-2"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in test_check_as_received test_bronze_capture test_retrieval_provenance test_listing_capture_census test_poison_control test_harvest_grammar; do echo "$t :: $(python -m pytest lib/opal_data_harvest/$t.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>16 passed, 12 passed, 18 passed, 18 passed, 3 passed and 7 passed -- the suites this cell reads are untouched by it; any divergence from these full-tree counts is recorded as an environment finding with a row</expect></criterion>
</proof_of_spec>

Write `.scratch/t2/ac3.py`: the allowed-set diff from `git merge-base HEAD SITEZ` over `lib`, an explicit assertion
that `check_as_received.py` is unchanged, plus a compile, CRLF and non-ASCII print per changed file.

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~17/AMGT_HARVST.TO-HVST-t-2.exercise-as-received-on-the-three-silent-paths.proof_of_spec.json`.
2. Grade with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4`, which must return rc 0.
3. Flip to `complete` only if every criterion passes. **Any honest verdict is a pass** -- `byte_equal 5 of 5` and
   `byte_equal 3 of 5` are both valid outcomes of an exercise; what fails is an exercise that cannot tell them
   apart.
4. Commit with `--only`.
5. Report once, quoting the five publisher lines, the denominators, and the BOUND sentence verbatim.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **This cell exists because `Z-S1` was resting on two paths of five and the missing three need no egress.** The
   ABSENT-versus-EXERCISED distinction is the whole justification, and it is stated to the worker rather than
   assumed.
2. **`check_as_received.py` is read-only on purpose.** Its result was adjudicated at 21/0/1; a cell that edits the
   instrument whose output was graded invites a re-grade nobody asked for.
3. **The bound is required in the OUTPUT**, not just the report, so a later reader cannot quote `byte_equal 5 of 5`
   as proof about live servers. Same discipline as `HVST-r-2`'s bound, which the CVO cited approvingly.

<status>pending</status>
<round>3</round>
<slot>~17</slot>
<fabric>site-z</fabric>
