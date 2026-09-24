# AMGT_HARVST task order -- `HVST-r-2` -- ROUND 2: PROVE, with a PRINTED CHECK per publisher path, that bronze holds the bytes the transport received -- row `-Z-S1`'s remediation, never inferred from a passing run; CODE AND S3 READS ONLY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-r-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~12</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on any harvest surface (C1=23 C2=7 C3=12 C4=21 C5=334); this cell writes nothing to S3 and arms nothing.
comp-iam: RUN at L5 on the DESIRED plane only; this cell needs S3 READS of opal-data-harvest and makes no write, so a refusal on a read is a BLOCKING row.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~12`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/` and every path in section 3 exist. If any is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~12;`.
- **NEVER RUN AN INSTALL. NEVER CALL A PUBLISHER. NEVER WRITE TO S3. NEVER RUN THE HARVESTER's `run` OR `upload-*`.**
  S3 GET and LIST on `opal-data-harvest` are the only AWS calls this cell makes.

## 1. THE CELL, inlined in full -- `HVST-r-2` (manifest row H1, outcome FWD-1)

**WHY THIS CELL EXISTS.** Row `AMGT_HARVST-Z-S1` (the issuer's, at the cut) found that `raw_bytes` on the SA and Bloomberg
paths were `json.dumps` RE-SERIALISATIONS of already-parsed JSON, not the bytes the publisher sent -- which is
`C-HV-BRONZE-AS-RECEIVED`'s own subject. `HVST-h-1` moved capture to `PacedSession.get`, where the response object lives.

**The round-1 analysis @`f869aa705c` still lists `Z-S1` as OPEN, and the reason is the bar, not a doubt:**
**remediation is owed a PRINTED CHECK and is never inferred from a passing run** (`3.0.0_SA_CVO~Z`'s bar on `-Z-W10-S2`
and `-Z-W10-S6`: evidence *consistent with* a fix is not evidence *of* it).

**RULED -- what you build. A checker, its output, and one honest bound.**
1. **A checker at `lib/opal_data_harvest/check_as_received.py`**, read-only against S3, which for EVERY bronze article
   object the live act landed:
   - reads the object and its S3 metadata;
   - reads the local capture record for the same article from the MAIN worktree's
     `.runtime/opal-data-harvest/progress.sqlite3`, opened `mode=ro` (derive the main root with
     `git worktree list --porcelain | head -1`; never type a drive path);
   - compares the object's sha256 against the sha256 the CAPTURE recorded;
   - prints, PER PUBLISHER: `publisher <code> objects <n> hash_match <m> mismatch <k> received_form <dict>`;
   - prints the DENOMINATOR: how many objects it examined and how many it could not (with the reason).
2. **A SHAPE test, per publisher path, that a re-serialisation could not pass.** For each of the five paths, assert from
   the STORED BYTES that they are what a transport returns rather than what `json.dumps` produces:
   - for the JSON paths, the stored bytes must NOT be canonically re-serialised: compare the stored bytes against
     `json.dumps(json.loads(stored))` and require them to DIFFER (key order, separators or escaping), OR, where they
     legitimately match, say so and mark that path UNPROVEN-BY-SHAPE rather than claiming it;
   - for the HTML paths, assert the stored bytes parse as a document and carry the page's own markup.
3. **THE BOUND, stated in your own output and in your report, never omitted:** a session-layer hash proves the stored
   bytes equal **what the transport received**. It does NOT prove they equal what the SERVER SENT, because nothing
   upstream of `PacedSession` is recorded. Print that sentence beside the result.
4. **A verdict line**: `as_received_proof <PROVEN|PARTIAL|UNPROVEN> paths_proven <n> of 5`, with the per-path reason for
   anything short of proven.

**What this cell does NOT do:** it writes no S3 object, changes no production path, and re-fetches nothing. If the check
FAILS for a path, that is a finding and a row, not a fix attempt.

## 2. WHERE THIS CAME FROM
Round 2, decomposition v1.1 @04a235adb7 section 10a, cell 2 of 5. Independent of the other four.

## 3. SURFACES -- what you may read and write

<paths>
lib/opal_data_harvest/check_as_received.py
lib/opal_data_harvest/test_check_as_received.py
lib/opal_data_harvest/transport.py
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/harvest_grammar.py
lib/opal_data_harvest/silver_from_bronze.py
lib/research/harvest/store.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~12/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-r-2.as-received-proof-with-a-printed-check.md
</paths>

- **Only `check_as_received.py` and `test_check_as_received.py` may CHANGE.** Everything else listed is READ-ONLY: read
  `transport.py` and `publishers.py` to find where capture happens, and `store.py` for the key grammar. AC3 fails if any
  of them changes.
- **The main worktree's `.runtime/`** is read, SQLite opened read-only. It is not a repo path and is never committed.
- Scratch goes in `<your worktree>/.scratch/r2/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~12 <0.9.0_WK_AMGT_HARVST~12@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **NO S3 WRITE, NO VENDOR CALL, NO RE-FETCH.** Pure ASCII.
- **A path you cannot prove is UNPROVEN, not assumed.** The verdict line carries the number.
- **Surprise rows:** `AMGT_HARVST-Z-W12-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-r-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/opal_data_harvest/test_check_as_received.py -v --color=no -p no:cacheprovider 2>&1 | tail -14</invocation><expect>every arm passes and no "failed" -- including a NEGATIVE CONTROL arm proving the shape test REJECTS a deliberately re-serialised body, and an arm proving the checker reports a mismatch when the stored bytes are altered</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-r-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.opal_data_harvest.check_as_received</invocation><expect>one line per publisher carrying objects, hash_match, mismatch and received_form; a printed DENOMINATOR of objects examined and objects skipped with reasons; the verdict line "as_received_proof ... paths_proven n of 5"; "mismatch 0" for every publisher that has objects from the live act; and the BOUND sentence stating that a session-layer hash proves what the TRANSPORT received, not what the SERVER sent</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-r-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r2/ac3.py</invocation><expect>"outside_allowed []" -- only check_as_received.py and test_check_as_received.py changed, nothing else under lib; each prints "compiles True crlf 0 non_ascii 0"</expect></criterion>
</proof_of_spec>

Write `.scratch/r2/ac3.py`: diff `git merge-base HEAD SITEZ`..HEAD over `lib`, an allowed set of exactly those two files,
and a compile, CRLF and non-ASCII print per changed file.

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~12/AMGT_HARVST.TO-HVST-r-2.as-received-proof-with-a-printed-check.proof_of_spec.json`.
2. Grade with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3`, which must return rc 0.
3. Flip to `complete` only if every criterion passes. **A verdict of PARTIAL or UNPROVEN does NOT block the flip** -- the
   cell's deliverable is the printed check and its honest verdict, not a particular verdict.
4. Commit with `--only`.
5. Report once, quoting the verdict line and the bound sentence verbatim.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **The flip is deliberately NOT conditioned on PROVEN.** Conditioning it would pressure the worker to claim a proof the
   evidence does not support, which is the failure this whole row exists to prevent.
2. **The negative control in AC1 is the load-bearing arm.** A shape test that cannot reject a re-serialised body proves
   nothing, and round 1 taught this project that lesson three times.
3. **The bound is required in the OUTPUT, not just the report**, so a later reader of the artifact cannot quote the hash
   match as proof of server fidelity.

<status>complete</status>
<round>2</round>
<slot>~12</slot>
<fabric>site-z</fabric>
