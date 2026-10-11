# TO IRPT_ANLREQ.TO-AR-y-145 -- the release census of the upload door: which functions package the reader, every consumer of its answer, both branches of a sheet accepted yesterday

<to_id>IRPT_ANLREQ.TO-AR-y-145</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~53</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (live single-resource reads of deployed functions). NOTHING is uploaded, applied, planned or invoked.
**Decomp cell:** `AR-y-145` (`decompositions/IRPT_ANLREQ_DECOMP_R14_Y.md`) | **outcome_ref:** FWD-1 (hop 2, the upload door); TCKT_VNEXT FWD-3 by CTO msgs 5737 and 5849 | **depends_on:** `AR-y-143` merged (the built state); `AR-y-141` terminal in this slot

**NOT SPAWNED AT ISSUANCE.** The issuer spawns this order when `TO-AR-y-143` is merged, and states in a spawn amendment the merged
commits, the files changed and the finding codes as built. If there is no spawn amendment, STOP: the order was spawned too early.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~53`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-53` (branch `wk-IRPT_ANLREQ-53`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~53 <0.9.0_WK_IRPT_ANLREQ~53@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W53-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you change passes `bash .tools/commit-gate.sh <file>` before its commit.
- **The background for every cell of this round** is one record, read it first:
  `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r13/ONE_ACCOUNT_CHECK_READ.json` (what the upload door does today, run in process on four synthetic sheets), and the CTO's rulings in
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_14_20261011.md` section 2. Any sheet you build is SYNTHETIC: made-up tickers (`AAA`, `BBB`), made-up numbers, nothing that looks
  like a real account number or a person. No real uploaded file is ever read.

### THE CELL (`AR-y-145`, inlined) -- A READ of the built state, with live single-resource reads. You change no product file.

*The release census of the upload door.*

Why. Cells `AR-y-142` and `AR-y-143` (merged into your branch; read their records under
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r14/` and the spawn amendment of this order) changed
`intake/template_reader.py`, `intake/uploads.py` and perhaps `ops/status.py`. A sheet that was ACCEPTED yesterday will be TURNED
BACK after the release. The pair that authorises the release is written on this census. A release of another function this
morning was rolled back after 61 minutes because its record named no consumer of the changed answer: this census names every one.

1. **`functions_that_package_the_reader`**: from `infra/aws/lambda/ci/lambda-source-map.json`, EVERY function entry whose `files[]`
   or `staged_from` packages any changed file (print the count of entries searched). For each: ONE live read,
   `.tools/aws lambda get-function-configuration --function-name <name>` (`CodeSha256`, `LastModified`); a `BUILD_ONLY=1` build with
   `TMPDIR` outside the worktree, twice, NO `BAU_PARITY_SKIP` (if it refuses, record the refusal's lines -- do not add a skip);
   and, where the entry pins the changed files at an older commit, say so: then the build does NOT carry the change and the row
   says what re-pin the release needs. `changed_members_vs_live`: download the live package once per function
   (`get-function`, the `Code.Location` link used once in the same command, never printed, logged or written; delete the zip)
   and diff members by sha256.
2. **`consumers_of_the_answer`**: every piece of code that reads the upload door's answer -- the POST's first answer and the later
   resolved answer: in the portal BY REF (`git -C C:/dev/wk-irpt-anlreq-51/portal show origin/PROD:<path>` and `origin/DEV:<path>`;
   never a working file), in the workspace (`infra/aws/lambda/investor-reporting/` callers, the mail intake, the ticket service, any test harness that is run
   in production paths), each `{"file_function": "...", "trunk": "PROD|DEV|workspace", "one_read_through_it": "<what a seat does to
   exercise it, in words>", "admits_new_answer": true|false, "deciding_line": "<file:line and text: an exact key-set check, a
   closed list of states or codes, a switch>"}`. A new finding code, a NEEDS_CORRECTION on the FIRST answer, and the new
   first-sheet member are the three new shapes: say for each consumer which of the three it meets. A zero says what it searched.
3. **`accepted_yesterday_turned_back_today`**: `{"branch_turned_back": "<what the person sees and what is written, with lines>",
   "branch_still_accepted": "<the same sheet minus the offending row or column: what changes in the accepted answer>",
   "what_happens_to_inputs_already_accepted": "<are stored inputs re-read by the new reader anywhere -- a retry, a re-open, a
   resident re-run? with lines; if yes, an input accepted yesterday can fail today and the pair must cover it>"}`.
4. `not_read`: a list. Write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r14/UPLOAD_DOOR_RELEASE_CENSUS.json`
   and commit it.

---

**SPAWN AMENDMENT (AMENDMENT 1, issuer `2.0.0_SA_COO~Y2`, 2026-10-11 ~22:3xZ): `TO-AR-y-143` is merged. The built state, and three
things ruled or found since this face was written that bind the census.** Gate limb that graded this amendment: read from this
commit's own output.

**The built state (merged into your branch; shared head at the merge `50a044b1b1`):**
- `infra/aws/lambda/investor-reporting/intake/template_reader.py` (cell `AR-y-142`, commit `d95cf11106`): four new finding codes --
  `ACCOUNT_COLUMN_SEVERAL_VALUES`, `HEADER_ROW_REPEATED`, `TOTAL_ROW_PRESENT` (severity ERROR) and `SHEETS_NOT_READ` (NOTICE, on an
  accepted sheet) -- each with its words in a new optional `description` member on the finding.
- `infra/aws/lambda/investor-reporting/intake/uploads.py` (cell `AR-y-143`, commit `4215d98f26`): `CORRECTION_WORDS` grows from 4 codes
  to 28; and the POST (`_defer`) now ANSWERS `NEEDS_CORRECTION`, reason `TEMPLATE_FINDINGS`, with the reader's findings when any has
  severity ERROR, publishing nothing and sending nothing to the resident. A sheet with no reader ERROR answers `RESOLVING` first,
  as before.
- `infra/aws/lambda/investor-reporting/ops/status.py` (same commit; a words-only edit): the same 24 sentences, because two tests lock
  the pair. **Its served effect:** `build_envelope` adds `{"action": "CORRECT", "safe": true, "description": <words>}` to the
  envelope's `actions` when the state is NEEDS_CORRECTION and the reason is one of 24 codes that had no words before. That is a
  FOURTH new shape, beside the three the face lists: name every reader of an envelope's `actions` and say whether it admits it.
- Tests: intake folder 304 passed (292 at the round's base).

**1. The reader runs in TWO runtimes, and the source map shows only one** (record of cell `AR-y-141`,
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r14/TOTAL_LABEL_PROVIDER_ASK.json`, your own earlier order):
the `irpt-ycharts-generate` Lambda runs the POST half; the RESIDENT process on the runner host runs the reader again for a sheet
that went on to `RESOLVING`, from its own installed package. Add a member **`resident_runtime`**: how the resident's package is
built and installed (which script or document, read from the repository; no live call to the host), whether a release of the
Lambda alone leaves the resident on the OLD reader, and what a person then sees for each new finding in that half-released state
(for example: is the `SHEETS_NOT_READ` line ever shown if only the Lambda is released? does the resident's old reader still accept
a totals row that the new POST would have turned back -- can such a sheet reach it at all?). The census check does not grade this
member; the issuer reads it.

**2. The after-read is bound by CTO ruling msg 5911.** "A synthetic upload there writes the same rows and the same undeletable
original, and its ticker check is a vendor call. So the pair's after-read does NOT include one unless the pair shows, from the
code, which provider the ticker check calls and that it is not the stopped YCharts path." Add a member **`ticker_check_provider`**:
`{"file_function": "...", "calls": "<host and path, with file:line>", "is_the_stopped_ycharts_path": true|false|"cannot_tell_from_code",
"evidence": "<the lines>", "after_read_without_any_provider": "<what a seat can read after the release that needs no provider and
no upload -- for example the deployed package's bytes compared member by member with the build, or the reader's refusal run in
process against the deployed zip's own template_reader.py>"}`. If the provider IS the stopped path, the census says so plainly:
the release's only live evidence is that the deployed bytes equal the build.

**3. Row `IRPT_ANLREQ-D2-W52-S14` (closed by the build):** a caller that assumed the POST's first answer is always `RESOLVING` now
sees `NEEDS_CORRECTION`. The earlier seating found three callers of the create path (the form's route; `build_upload_entry`;
`deferred_upload_service` in `upload_resolution.py`) and ran no full census. Yours is the full one.

The portal's form on DEV (`6eb13c5e875f`) already re-posts only on `RESOLVING` and shows a first-answer finding at once; PROD's form
does not. Read both refs.

### ACCEPTANCE

<criterion id="AR145-y-AC1" cell_refs="AR-y-145"><invocation>python C:/dev/wk-irpt-anlreq-53/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r14/ar14_checks.py y145-census --root C:/dev/wk-irpt-anlreq-53</invocation><expect>Y145-CENSUS-OK</expect></criterion>
`AR145-y-AC1`: the census names each packaging function with its live and built digests and the members that differ, each
consumer with one read through it and the line that decides whether it admits the new answer, both branches, and what was
not read. It grades the record's form.

<criterion id="AR145-y-AC2J" cell_refs="AR-y-145" judgment="true"/>
`AR145-y-AC2J` (judgment, graded at L9, never by you): no consumer of the door's answer is missing, and each named consumer's
deciding line is the line that actually decides.

<expected_criteria>AR145-y-AC1 AR145-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/` and this order's
  file (status flip only).
- READ only: everything else. No push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R14_Y.md</decomp_doc>
<owned_cells>AR-y-145</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR145-y-AC1 AR145-y-AC2J. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/IRPT_ANLREQ.TO-AR-y-145.upload-door-release-census.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-145`. `AR145-y-AC2J` is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with `method`, `invocation`, `denominator` and a `status_reason`
naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR145-y-AC1,AR145-y-AC2J`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 rollback record of this lane (release 5: 19 backend readers counted, 0 portal readers, 61 minutes) as the reason every consumer is a required row; NOT seen: which map entries package the reader and every consumer (this cell measures both; the count of entries searched is printed). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers of what this cell writes. comp-iam: RUN -- by reading 2 earlier orders of this lane (TO-AR-y-91, TO-AR-y-103): the dell2 identity made single-function get-function reads today; this cell makes the same kind and changes no permission.
comp-adversary: RUN -- by reading 1 ruling (item 5: both branches of a sheet accepted yesterday) against the face; the lens: an input accepted yesterday being re-read by the new reader on a retry and failing. The face makes that a required member. NOT seen: consumers outside the two repositories.
lane: the worker's deliverables; read-only on the world, the map and both repositories.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-14 analysis @1edb90ada7, item 5. `AR145-y-AC1` base: FAIL as expected (no census).
- NOT SPAWNED AT ISSUANCE: spawned when `TO-AR-y-143` is merged, with a spawn amendment naming the merged commits and the
  finding codes as built. The pair and the apply order are the issuer's, written on this census.
