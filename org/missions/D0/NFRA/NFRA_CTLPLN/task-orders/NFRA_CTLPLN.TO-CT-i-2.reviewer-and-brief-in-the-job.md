# TO NFRA_CTLPLN.TO-CT-i-2 -- workstream INBOUND round 1 CT-i-2: on the box, a job needs its brief file and a reviewer's passing grade before it can be reported complete

<to_id>NFRA_CTLPLN.TO-CT-i-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~32</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>INBOUND</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-i-2` (`decompositions/NFRA_CTLPLN_DECOMP.inbound1.md`) | **outcome_ref:** FWD-20 |
**depends_on:** none (the seam below is fixed text; the cloud half is another worker's)

---

## WORKER FACE

### THE CELL

`CT-i-2`, contract C-SEATS clause 8, verbatim: "**An inbound job** is done by a seat spawned fresh for it and briefed from a
file; the requester is told the outcome in the channel they asked in." And the outcome's line (FWD-20): "a seat started fresh
for that job, handed a written brief, does it; a seat that did none of the work grades it".

Andrew's words: "The agents that get those jobs should be spawned fresh, briefed, and run /remote-drive." And: "CVO is
dedicated reviewer in those drive processes".

The box side of a remote job is `.tools/remote-job.py` (run by the box's manager seat, `0.0.0_AB_MSTR`) and the skill
`.claude/skills/remote-drive/SKILL.md` (Half 1 the manager, Half 2 the operations seat `2.0.0_SA_COO~<N>` that does the job).
The protocol is `org/tier1_exec/4.0.0_SA_CRO/deliverables/REMOTE_JOBS_PROTOCOL_20261002.md`. Read all three, and
`.tools/tests/test_remote_job.py`, before you build. A reviewer seat is `3.0.0_SA_CVO`, with or without a `~lane`.

### MEASURED AT THE BASE (re-ground each)

- `cmd_accept` writes the lock with `"brief": args.brief_file` and does not check that the file exists.
- `cmd_complete` sends `job.complete` on the manager's word; nothing in the tool or the skill names a reviewer.
- `cmd_bid` says `available` false only when this box already runs a job.
- The seats live on a box are in `org/mcp/liveness.json` (gitignored, per box): serial -> an entry with a last-seen time; the
  estate reads a seat as live when it was seen within 120 seconds. Read the file's real shape before you rely on it.

### THE SEAM WITH THE CLOUD (fixed; the cloud half is another worker's)

Additions to `org/tier1_exec/4.0.0_SA_CRO/deliverables/REMOTE_JOBS_PROTOCOL_20261002.md`; nothing in it is removed.
- `job.bid` payload gains `reviewer` (the serial of a reviewer seat live on the box at the bid, or null) and, when
  `available` is false, `unavailable_reason` ("job_open" | "no_reviewer").
- `job.accepted` payload gains `brief_sha256` (the SHA-256 of the brief file the seat was handed).
- `job.complete` payload gains `coo` (the serial that did the work) and `grade`: {`by` (a reviewer serial, never equal to
  `coo`), `verdict` ("PASS"), `record` (the repo path of the reviewer's grade record), `at`}.
- The cloud treats a `job.complete` whose `grade` is absent, whose `verdict` is not "PASS", or whose `by` equals `coo` as NOT
  complete: the job stays `working`, nothing is drafted to the requester, and Andrew is texted one line under the job's tag.
- A reviewer serial is `3.0.0_SA_CVO` with or without a `~lane`.

### BUILD

1. `.tools/remote-job.py` (keep every existing verb, flag, event id and output line working; `--dry-run` still sends nothing
   and touches no lock):
   - `bid`: find a live reviewer on this box from the liveness file (path overridable by `OPAL_LIVENESS_FILE` for the test).
     None live: `available` false with `unavailable_reason` "no_reviewer" and one `WARN:` line. A job already open keeps
     "job_open". The payload carries `reviewer`.
   - `accept`: `--brief-file` is REQUIRED and must be an existing, non-empty file; `--coo` must be a `2.0.0_SA_COO~<lane>`
     serial. Otherwise one `ERROR:` line, exit 2, no lock, nothing sent. The lock and the payload carry `brief_sha256`.
   - NEW `grade <job> --as <reviewer serial> --verdict PASS|FAIL --record <repo path>`: run by the reviewer seat. Refuses
     (one `ERROR:` line, exit 2, nothing written) when `--as` is not a reviewer serial, when `--as` equals the lock's `coo`,
     when the lock does not name this job, when `--record` is not an existing file, or when `OPAL_AGENT_SERIAL` is set and
     differs from `--as`. Otherwise writes `grade` {`by`, `verdict`, `record`, `at`} into the lock and prints
     `OK: <job> graded <verdict> by <serial>`. It sends nothing.
   - `complete`: refuses (exit 2, nothing sent) unless the lock names this job and carries a grade whose verdict is PASS and
     whose `by` is not the lock's `coo`. The refusing line is exactly `ERROR: <job> has no passing reviewer grade on this
     box; nothing sent` . When it sends, the payload carries `coo` and `grade`. The old path that warned and sent anyway when
     the lock did not name the job is removed.
   - `show`: unchanged.
2. `.claude/skills/remote-drive/SKILL.md`, the smallest edit that makes the text true:
   - Half 1: the bid row says a box with no live reviewer bids unavailable. The AWARD row keeps its four steps and says the
     seat is NEW for this job (a serial not live before the award) and that `accept` refuses without the brief file. A new
     row between the completion report and `complete`: the manager hands the reviewer on its box the operations seat's
     report path and the job id by one message; the reviewer reads the real artifact, writes its grade record under its own
     deliverables folder and runs `python .tools/remote-job.py grade ...`; only then the manager runs `complete`. A FAIL
     grade goes back to the operations seat as its next item; a second FAIL is `fail` with the reason.
   - Half 2 step 8: the report goes to the manager AND names the files the reviewer should read.
   - Keep the file's length within 12 lines of what it is today. Add no date, no quotation and no incident.
3. `.tools/tests/test_remote_job_review.py`, run as a plain script, with a temporary lock path and liveness file and every
   send replaced by `--dry-run` or a fake (read how `.tools/tests/test_remote_job.py` isolates the lock and the sender):
   - `complete` with no grade refuses and sends nothing; after a PASS grade by `3.0.0_SA_CVO` the same `complete` builds an
     envelope whose payload carries `coo` and `grade` (the difference control);
   - a FAIL grade leaves `complete` refusing; `grade --as` the job's own operations seat refuses; `grade --as` a manager
     serial refuses; `grade` with a missing record file refuses;
   - `accept` without `--brief-file`, with a missing file and with an empty file refuses and writes no lock; with a real file
     the lock carries its SHA-256;
   - `bid` with no reviewer in the liveness file says `available` false, `unavailable_reason` "no_reviewer"; with a reviewer
     seen 30 seconds ago says `available` true and names it; with one seen 10 minutes ago says false.
   LAST line `REMOTE-JOB-REVIEW-TEST ok=<True|False> cases=<passed>/<total>`.

### RULES FOR THIS CELL

- **Send nothing.** No bus message, no event to the cloud, no broker message: `--dry-run` or a fake in every run. Never run
  `bid`, `accept`, `complete` or `fail` without `--dry-run` outside a test's fake. Leave the real `.tools/.remote-job.json`
  as you find it.
- **AMENDMENT 1 (issuer, REOPENED complete -> in_progress, on your rows W32-S1 to S4; it OVERRIDES the rule this line
  replaces):** `.tools/tests/test_remote_job.py` is now in your `<paths>`. Bring its four failing cases
  (`test_bid_available_with_the_contract_payload`, `test_accept_locks_then_close_unlocks`,
  `test_complete_payload_and_attempt_event_id`, `test_dry_run_sends_nothing_and_touches_no_lock`) to the contract THE SEAM
  states: each keeps what it tested and gains the new fields and preconditions (a live reviewer for an available bid, a
  brief file for accept, a PASS grade for complete). Remove no case and weaken no assertion that still holds; the six
  passing cases stay as they are. Then run criterion `CTi2-AC3`, add its row to the proof instance, re-validate against all
  three ids, and flip `<status>` to `complete`. Rows S1 to S4 are disarmed by that passing run; say so in your report.
- Spawn nothing, start no seat.
- No non-ASCII in any file you write. Bake no absolute path, no device name and no user name.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTi2-AC1" cell_refs="CT-i-2"><invocation>python .tools/tests/test_remote_job_review.py</invocation><expect>REMOTE-JOB-REVIEW-TEST ok=True</expect></criterion>
`CTi2-AC1` -- the grade, the brief file and the reviewer-aware bid, with the difference control: the same completion refused without a grade and built with one.

<criterion id="CTi2-AC2" cell_refs="CT-i-2"><invocation>python .tools/remote-job.py complete J999 --summary probe --dry-run</invocation><expect>ERROR: J999 has no passing reviewer grade on this box; nothing sent</expect></criterion>
`CTi2-AC2` -- the real tool on this box, where no job J999 was ever graded, refuses.
<criterion id="CTi2-AC3" cell_refs="CT-i-2"><invocation>python -m pytest .tools/tests/test_remote_job.py -q -p no:cacheprovider</invocation><expect>10 passed</expect></criterion>
`CTi2-AC3` -- added by AMENDMENT 1: the tool's existing ten cases pass under the new contract; the line must not read `failed`.
</proof_of_spec>

<expected_criteria>CTi2-AC1,CTi2-AC2,CTi2-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~32/NFRA_CTLPLN.TO-CT-i-2.reviewer-and-brief-in-the-job.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CTi2-AC1,CTi2-AC2`, and flip `<status>` to `complete` only when
every criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.inbound1.md</decomp_doc>
<owned_cells>CT-i-2</owned_cells>
</decomp_ref>

<paths>
.tools/remote-job.py
.tools/tests/test_remote_job_review.py
.tools/tests/test_remote_job.py
.claude/skills/remote-drive/SKILL.md
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call is added; the tool's existing send is untouched and no worker runs it.
comp-adversary: RUN -- the seat that did the work grading itself (grade refuses the lock's own operations seat; complete re-checks it); a manager grading (refused: a reviewer serial only); a completion sent on a FAIL (refused; a criterion); a box with no reviewer winning a job it cannot finish (it bids unavailable); a job accepted with no brief (refused); a stale liveness entry read as a live reviewer (the 120-second rule, tested at 30 seconds and at 10 minutes). BLIND: whether the reviewer read the real artifact is the reviewer's own act, recorded in its grade file and not checkable by this tool; a seat "spawned fresh" is told by the skill, not checked by the tool.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.18 @55e2de3227 (ADMITTED), FWD-20, C-SEATS clause 8; brief O8, F2 ("NOT found: ... a
reviewer step in /remote-drive"); CTO ruling msg 106585.
