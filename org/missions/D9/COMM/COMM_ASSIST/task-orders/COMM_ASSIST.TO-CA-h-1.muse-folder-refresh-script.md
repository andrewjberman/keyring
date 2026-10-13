# TO COMM_ASSIST.TO-CA-h-1 -- round 16 CA-h-1: the dell2 reader folder's refresh script and fixed layout (FWD-6, FWD-10, FWD-11)

<to_id>COMM_ASSIST.TO-CA-h-1</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~8</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-h-1` (`decompositions/COMM_ASSIST_DECOMP.round16.md`) | **outcome_ref:** FWD-6, FWD-10, FWD-11 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Andrew will read "what is waiting on me?" from a folder on another machine (dell2), over SSH, from a tailnet VM called muse that has
NO cloud access. A job on dell2 will refresh that folder from AWS on a schedule. You build the refresh SCRIPT and fix the folder
LAYOUT. You do not install, schedule or deploy anything: that is a later cell, run on dell2 by its own seat.

The one rule that shapes every line: **a source that could not be read must say so; absent is never shown as empty.**

### BUILD, IN THIS ORDER

1. Create the package `data/transcripts/scripts/muse_reader/` with `__init__.py` and `refresh.py` (stdlib only for the logic; AWS
   reads go through the AWS CLI by subprocess, executable name from the env var `MUSE_AWS_BIN`, default `aws`; on this laptop the
   working form is the repo shim `.tools/aws` -- read `.tools/msys_argv_guard.py` and the shim to see how to launch it from
   Python on Windows; if no form works, stop and file a BLOCKING row with what you measured).
2. `refresh.py` exposes exactly this interface (the issuer's checks import it):
   - `SOURCES = ("open_calls", "drafts", "eod_today", "sprint_today")`
   - `refresh(root, readers, now)`: `root` a folder path; `readers` a dict name -> zero-argument callable returning a list of
     dicts or raising; `now` a UTC time string like `2026-10-13T16:00:00Z`. For each source it calls the reader and writes
     `<root>/<name>.json` as one JSON object with the keys `source`, `read_at` (= `now`), `status`, `last_good_at`, `error`,
     `items`. Success: `status` `ok`, `last_good_at` = `now`, `error` null, `items` the list (an empty list is a true empty, said
     at `read_at`). A reader that raises: `status` `unreadable`, `items` null (NEVER `[]`), `error` the first 200 characters of the
     exception text, `last_good_at` carried from the previous file if one exists (else null). One source failing never stops
     the others. A reader may raise the module's `Absent` exception for "reachable, but the thing is not there yet today":
     `status` `absent`, `items` null, `last_good_at` carried.
   - It also writes `<root>/INDEX.json` (each source's `status`, `read_at`, `last_good_at`) and `<root>/README.txt` (the layout, in
     plain English: the four files, the six keys, the three statuses, and the sentence "absent and unreadable are never an empty
     list"). Write every file by temp-file-then-rename so a reader never sees half a file.
   - Run as `python data/transcripts/scripts/muse_reader/refresh.py --root <folder>` it builds the real readers, calls
     `refresh`, prints one line `MUSE-REFRESH ok=<n> absent=<n> unreadable=<n>` and exits 0 whatever the statuses are.
3. The four real readers (read-only; no write to AWS; bound every call with `--max-items` or a page cap and print the
   denominator in the stdout line):
   - `open_calls`: the cluster copies of every box's open calls. The boxes come from `org/devices/DEVICES.json`; the bucket and
     key prefix come from `.tools/open-calls.py` (read how its `--cloud` listing forms the key; import or parse its constants --
     do NOT type the bucket or prefix into your file; if they cannot be derived, stop and file a BLOCKING row). Items: the open
     calls as that tool lists them (id, box, title, age fields it carries).
   - `drafts`: DynamoDB table `teams-global-chat-assist-table` (us-east-1), the rows whose `pending` is non-null. Read how the
     table is keyed and how `pending` is shaped in `data/transcripts/scripts/teams_chat/tenant.py` and `assist.py`. Use a paged
     scan; read the whole table (print rows scanned). Items: the tag, kind, version, status, send time and the draft TEXT, and
     the chat title.
   - `eod_today`: the single row `eod:<today>` of that table, where `<today>` is formed exactly as `tenant.py` forms the End of
     Day key (read it; do not guess the timezone). No such row: raise `Absent`. Item: its pending draft text, version, status
     and send time.
   - `sprint_today`: the object listing (key, size, last-modified; no object body) of today's prefix under
     `s3://opal-data-portal-v2/daily-reports/` (read how `daily_reports` keys are formed from the repo; do not guess). Nothing
     listed: raise `Absent`.
4. **Nothing that lets a reader act as Opal may be written.** Before any text goes into a file, replace every email address with
   `[address withheld]`. Never write a key, token, password, header or secret value, a client's address, or a raw API response.
   No message BODIES other than the draft text above.
5. No non-ASCII in the script or its output (use `OK:`/`ERROR:` style words in stdout, `ensure_ascii=True` in the JSON). Bake no
   absolute path: the folder is the `--root` argument.

### RULES FOR THIS CELL

- Edit nothing but the files in `<paths>`. AWS: read calls only (`dynamodb scan`, `s3api list-objects-v2`, `s3api get-object` of the
  open-calls copies); no put, no update, no delete, no deploy, no apply, no other call.
- Any S3 address or resource NAME you would create must be builder output (`lib/opal_naming.py`); this cell creates none. If you
  think it needs one, stop and file a BLOCKING row.
- If the laptop identity is denied a read, that source is `unreadable` (the script must still finish); report the denial and
  which call in your final report and a row. Do not change an identity or a policy.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAh1-AC1" cell_refs="CA-h-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r16/checks/check_h1_failure_shape.py"</invocation><expect>H1-FAILURE-SHAPE ok=True</expect></criterion>
`CAh1-AC1` -- the issuer's check (read it; do not edit it): a reader that raises gives `unreadable`, `items` null, the previous good time kept and the error text; the control, a reader returning `[]`, gives `ok` and `[]`; an unrelated source is unaffected. It prints ok=False at the base.

<criterion id="CAh1-AC2" cell_refs="CA-h-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r16/checks/check_h1_live.py"</invocation><expect>H1-LIVE ok=True unreadable=0 of 4</expect></criterion>
`CAh1-AC2` -- the seam against the REAL neighbours: the CLI run once under the running identity reads the four real sources; each ends `ok` or `absent`, none `unreadable`. It prints ok=False at the base.

<criterion id="CAh1-AC3" cell_refs="CA-h-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r16/checks/check_h1_census.py"</invocation><expect>hits=0 ok=True</expect></criterion>
`CAh1-AC3` -- the bound (FWD-11's census arm): the folder that run writes holds no AWS key, PEM, bearer token, JWT, secret assignment or email address; the line prints the file count (zero files is not a pass). It prints ok=False at the base.
</proof_of_spec>

<expected_criteria>CAh1-AC1,CAh1-AC2,CAh1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~8/COMM_ASSIST.TO-CA-h-1.muse-folder-refresh-script.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CAh1-AC1,CAh1-AC2,CAh1-AC3`, and flip `<status>` to `complete`
only when all three pass and the instance is VALID. Your final report names: the working AWS launch form, the denominators
(rows scanned, boxes read, objects listed), and any source that was `absent` or `unreadable` and why. Your surprise rows are
`COMM_ASSIST-W8-S<k>`; append only to the investigation file and keep its existing line endings. A second order follows for you
on this slot (CA-h-3); it reads the layout you fix here.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round16.md</decomp_doc>
<owned_cells>CA-h-1</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/muse_reader/
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-h-1.muse-folder-refresh-script.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~8/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing; the schedule is cell CA-h-2, run on dell2.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; read-only AWS calls under the running identity. dell2's read access is the admin-group apply (NFRA_CTLPLN round-12 cell 1; CTO ruling @53acd6fe5f supersedes grant (d)), not here.
comp-adversary: RUN -- an empty list on a failed read (refused: AC1's red arm, items must be null); an email address or a token in a draft (refused: BUILD 4 and AC3); a typed bucket or prefix (refused: BUILD 3 derives them); one failing source stopping the rest (AC1). BLIND: dell2's own identity and python/AWS CLI availability are not measured here; CA-h-2 reads them on the host.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAh1-AC1 base: FAIL as expected (ModuleNotFoundError muse_reader); CAh1-AC2 base: FAIL as expected (script absent); CAh1-AC3 base: FAIL as expected (files=0). AC1 green and red arms run against a stub: PASS as expected / FAIL as expected (items=[] refused).
Source: CTO round-15 analysis `ledger/ROUND_ANALYSIS.round15.md` @15fdb72f21 item 1-2; PRD v0.6 FWD-6, FWD-10, FWD-11; ruling @2f0ed70e40 sections 1-2.
