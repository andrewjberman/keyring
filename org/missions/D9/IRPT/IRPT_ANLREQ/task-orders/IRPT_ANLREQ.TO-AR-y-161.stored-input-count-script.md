# TO IRPT_ANLREQ.TO-AR-y-161 -- a read-only script, proven offline, that counts the stored inputs the new reader would read differently and whether a report was made from each

<to_id>IRPT_ANLREQ.TO-AR-y-161</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a script in the worker's deliverables, proven on in-memory fakes; NO live call is made by this order)
**Decomp cell:** `AR-y-161` (`decompositions/IRPT_ANLREQ_DECOMP_R16_Y.md`) | **outcome_ref:** FWD-1 (hop 2, the upload door); PRD v0.4 ROUND-16 item 1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~52`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-52` (branch `wk-IRPT_ANLREQ-52`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~52 <0.9.0_WK_IRPT_ANLREQ~52@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W52-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`.

### THE CELL (`AR-y-161`, inlined) -- you BUILD A READ-ONLY SCRIPT and prove it OFFLINE. You make NO live call.

*Count the stored inputs the new reader would read differently, by cause, and whether a report was made from each.*

Why. A new upload reader was built last round and taken off the trunk: `read_input` (`infra/aws/lambda/investor-reporting/intake/uploads.py`, about lines
516-555) re-reads a stored original with the running reader and refuses unless the result equals the template stored at
acceptance, so a changed reader refuses inputs stored before it. The contract that repairs this is written
(`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`, CONTRACT C-STOREDINPUT; read it). Before the reader is re-landed the CTO needs a NUMBER: how many stored inputs the
new reader would read differently, by cause, and for each one it would turn back, whether a report was ever generated from it
and when last. A seat on another box, which holds the decrypt this box lacks, will run your script once in a read window. You
write it and prove it offline here.

**The new reader** is NOT on the trunk. Its bytes are `git show d95cf11106:infra/aws/lambda/investor-reporting/intake/template_reader.py`. The script loads the
new reader from a path given on the command line (`--new-reader <file>`), never by importing the trunk's module under another
name; the running (old) reader is the trunk's `infra/aws/lambda/investor-reporting/intake/template_reader.py` at the checkout the script runs in.

1. **Read first** (and cite file and line in your record): how an input, its template and its retained original are stored and
   keyed -- `uploads.py` (`read_input`, `_defer`, `create`, the `INPUT#`, `UPLOAD#`, `NORMALIZATION#`, `RETENTION#`, `ARTIFACT#`
   rows), `upload_resolution.py`, the storage ports the folder's tests fake; which rows carry the lane (template, csv, custody,
   mail); where the original's bytes live and under which digest; and how a generated report is tied back to the input it was
   made from (the acceptance record of an analysis request names an input: find the member, `infra/aws/lambda/investor-reporting/ycharts/generate/` and
   `infra/aws/lambda/investor-reporting/ops/owned_requests.py`). The census of last round has much of this:
   `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r14/UPLOAD_DOOR_RELEASE_CENSUS.json`.
2. **The script,** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r16/count_stored_inputs.py`:
   - Reads ONLY: a scan or query of the requests table for input rows and for accepted analysis requests (read how the product
     reads them; use the same key shapes), and `GetObject` of each template input's retained original. It contains NO write
     call of any kind (the check refuses `put_item`, `update_item`, `delete_item`, `put_object`, `delete_object`, `invoke(`,
     `send_message` anywhere in the file) and takes its table name, bucket and region from arguments, never typed in the file.
   - For each stored TEMPLATE input: read the original, run the OLD reader and compare with the stored template (a control: it
     should equal; count the ones that do not as `old_reader_differs`, they are a finding of their own); run the NEW reader and
     compare; if it differs, name the CAUSE from the new reader's finding codes (`TOTAL_ROW_PRESENT`, `HEADER_ROW_REPEATED`,
     `ACCOUNT_COLUMN_SEVERAL_VALUES`, `SHEETS_NOT_READ`, or `OTHER` with the code). An input may have several causes: count it
     once per cause and once in the total.
   - An input the script cannot read (a denied read, a missing object, a digest that does not match) is counted `unreadable` with
     the error's code. NEVER as "reads the same". A scan that is denied outright exits non-zero and prints the error's code.
   - For each input the new reader would TURN BACK (an ERROR finding): whether any accepted analysis request names it, how many,
     and the date (UTC day) of the latest; bucketed, not listed.
   - **Output: ONE JSON object on the last line of stdout, counts and dates only.** Members: `inputs_by_lane` (lane -> count),
     `template_inputs`, `old_reader_differs`, `read_differently` (total), `by_cause` (cause -> count), `turned_back` (count),
     `turned_back_with_a_report` (`{"with": n, "without": n, "latest_report_day_by_month": {"YYYY-MM": n}}`), `unreadable`
     (code -> count), `items_scanned`, `by_tenant` (tenant -> the same counts; a tenant is a firm's code, not a person),
     `read_at`. NO input id, NO upload id, NO file name, NO ticker, NO amount, NO account value, NO person. The script holds a
     file's bytes in memory only and writes nothing to disk but its one output file if `--out` is given.
   - `--self-test`: builds, IN MEMORY, a fake table and a fake object store holding SYNTHETIC stored inputs (made-up tickers and
     numbers) -- at least: one clean sheet; one with a `Total` row; one with a repeated header; one with a two-value account
     column; one two-sheet workbook; one whose object is missing; one template input with a report made from it and one
     without -- stored by the OLD reader, then runs the whole count against the fakes with the new reader loaded from
     `git show d95cf11106:...` (the self-test fetches it with `git show` into a temp file outside the worktree and deletes it)
     and prints the JSON object. The self-test asserts its own expected counts and exits non-zero on a mismatch.
3. **The record,** `.../r16/COUNT_SCRIPT_RECORD.json`: `{"reads": ["<table: which key shapes, with the product line that defines
   each>", "<bucket: which keys>"], "writes": [], "new_reader_source": "git show d95cf11106:<path>, sha256 <hex>",
   "how_a_report_is_tied_to_an_input": "<member and file:line>", "output_fields": [...], "self_test": {"inputs": <n>, "expected":
   {...}, "printed": {...}}, "invocation_for_the_reader_seat": "<the exact command, with placeholders for table, bucket, region>",
   "what_the_seat_must_hold": "<the reads it needs: decrypt on which key, GetObject on which prefix>", "not_read": [...]}`.
4. Commit the script and the record.

### ACCEPTANCE

<criterion id="AR161-y-AC1" cell_refs="AR-y-161"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r16/ar16_checks.py y161-count --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y161-COUNT-OK</expect></criterion>
`AR161-y-AC1`: the script's self-test exits 0 and prints one JSON object with the six named members; the file holds no write
call; the record names its reads, an empty write list, the new reader's source, how a report is tied to an input, and what
was not read.

<criterion id="AR161-y-AC2J" cell_refs="AR-y-161" judgment="true"/>
`AR161-y-AC2J` (judgment, graded at L9, never by you): the script's output can carry no account value, holding, id or person,
and an input it cannot read is never counted as reading the same.

<expected_criteria>AR161-y-AC1 AR161-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's
  file (status flip only).
- READ only: everything else. No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R16_Y.md</decomp_doc>
<owned_cells>AR-y-161</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR161-y-AC1 AR161-y-AC2J. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-161.stored-input-count-script.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-161`. `AR161-y-AC2J` is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR161-y-AC1,AR161-y-AC2J`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 census of last round (21 consumers; read_input at uploads.py:632-637 as then numbered; the POST writes the upload record and the retained original at :376-387) and 1 contract (C-STOREDINPUT, 5 points); NOT seen by the issuer: the key shapes of the stored rows and how a report names its input (the worker reads and cites them). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called by this cell. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers of what this cell writes. comp-iam: RUN -- by reading 2 records of this lane (TO-APPLY-Y6 step-0 stop: kms:Decrypt on the IRPT key is denied to dell2; TO-READS-Y6: the laptop identity scanned the requests table and read job rows): the script is RUN by that seat under its own read-only order; this cell changes no permission and states what the seat must hold.
comp-adversary: RUN -- by reading 1 ruling (CTO msg 6304: counts and dates, no account value, no holding) against the face; the lens: a count that prints an input id or a file name, or a denied read counted as 'reads the same'. The face forbids both, the check refuses any write call in the file, and the judgment criterion puts the output's contents before the reviewer. NOT seen: the real table.
lane: the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on PRD v0.4 @4b1447e2cc ROUND-16 item 1 and CTO msg 6304 (one more column). `AR161-y-AC1` base: FAIL as expected (no script).
- The count itself is ONE read-only Tier-2 order the issuer cuts to the seat that holds the decrypt, from this record; its result
  goes to the CTO before `TO-AR-y-162` is spawned.
- Seating: slot ~52 is reused; `TO-AR-y-162` queues behind this order in the same slot.
