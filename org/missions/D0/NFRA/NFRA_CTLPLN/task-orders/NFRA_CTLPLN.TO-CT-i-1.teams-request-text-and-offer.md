# TO NFRA_CTLPLN.TO-CT-i-1 -- workstream INBOUND round 1 CT-i-1: the Teams agent says when work is requested and what it recommends, offers the job to every box, and refuses an ungraded completion

<to_id>NFRA_CTLPLN.TO-CT-i-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~31</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>INBOUND</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-i-1` (`decompositions/NFRA_CTLPLN_DECOMP.inbound1.md`) | **outcome_ref:** FWD-20 |
**depends_on:** none. Your next order in this queue, `CT-i-3`, calls the function and the text shape you write here.

---

## WORKER FACE

### THE CELL

`CT-i-1`. The outcome (FWD-20): "a person asks for a small piece of work in Teams; Andrew gets one text saying what was asked
and what is recommended, and can answer it without opening Teams; the job goes to the box with the most room by a measurement
taken when it is offered; a seat started fresh for that job, handed a written brief, does it; a seat that did none of the work
grades it; the person who asked is told, where they asked, that it is done".

His words: "I will get the text at the Quo line from the Kimi agent with a recommendation if they identify that work is being
requested."

The Teams agent is the cloud function whose code is `data/transcripts/scripts/teams_chat/tenant.py` (the handlers) and
`assist.py` (the model call, the text to Andrew, the bus send). The protocol between it and the boxes is
`org/tier1_exec/4.0.0_SA_CRO/deliverables/REMOTE_JOBS_PROTOCOL_20261002.md`. Read all three, and
`data/transcripts/scripts/tests/test_teams_chat_jobs.py` for how a handler is driven with a fake context, before you build.

### MEASURED AT THE BASE (re-ground each)

- `tenant.py` `on_chat_messages` texts Andrew a reply draft for every unanswered message that wants a reply; `assist.py`
  `offer_text` builds that text. Nothing in either file says a message requests work, and nothing recommends.
- A job opens only when Andrew texts `#dev` on the chat's tag (`open_job`, `on_job_open`). This STAYS: a job starts on his
  reply, never by itself.
- `assist.py` holds `DEVICES = {"laptop": ..., "sitez": ...}` typed by hand; `on_job_open` offers to `a.DEVICES` and
  `on_job_bid` awards early once `set(bids) >= set(a.DEVICES)`. The device register `org/devices/DEVICES.json` holds four boxes,
  each with `name` and `inbound_queue`. The function's package carries `NAMES.json`, not the register.
- `on_job_complete` drafts the message to the requester on any `job.complete`.

### THE SEAM WITH THE BOX TOOL (fixed; the box half is another worker's)

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

1. **Recognise and recommend** (`assist.py`, `tenant.py`):
   - `assist.work_request(incoming_text, chat_title, context_md, send=None)` returns a dict: `is_work` (bool), `asked` (one
     line, what was asked, at most 160 characters), `recommend` (one of "job" | "reply" | "decline"), `why` (one line, at most
     160 characters). One model call through the existing `kimi()` with a new system prompt constant `WORK_SYSTEM`; the model
     is told to answer in JSON and anything that does not parse is `is_work` False (fail closed to today's behaviour). `send`
     is the same injection point `draft_chat_reply` has.
   - `on_chat_messages` calls it for the waiting messages and stores the result on the pending item as `work`.
   - `offer_text`: when the item carries `work` with `is_work` True, the text stays ONE text and becomes: the existing head
     line; then `WORK REQUESTED by <name>: <asked>`; then `Recommend: <open a job | reply only | decline>: <why>`; then the
     incoming text and the draft as today; then the reply line `Reply #dev [notes] to open a job / 1 send the draft / 0 drop
     / notes to redraft`. When `is_work` is False the text is byte-for-byte what it is today.
2. **Offer to every box of the register** (`gen_bus_devices.py`, `NAMES.json`, `assist.py`, `tenant.py`):
   - `data/transcripts/scripts/teams_chat/gen_bus_devices.py`: `--write` reads `org/devices/DEVICES.json` and writes a
     `bus_devices` map {box name: inbound queue name} into `NAMES.json`, touching no other key; `--check` compares the two
     and prints LAST `BUS-DEVICES ok=<True|False> boxes=<n> in_register=<r> in_names=<m>`.
   - `assist.DEVICES` is read from `NAMES["bus_devices"]`; no box name or queue name is typed in either Python file.
   - `on_job_open` records `offered_to` (the list) and `offered_at` in the job's state. The early award in `on_job_bid` fires
     when every offered box has bid. A bid's `reviewer` and `unavailable_reason` are kept with it. The award text to Andrew
     names the box, its CPU and memory reading, and that reading's time.
3. **Refuse an ungraded completion** (`tenant.py` `on_job_complete`): apply the seam's fourth rule. The refusing text is
   `#<job> completion NOT accepted from <box>: <no reviewer grade | grade is not PASS | graded by the seat that did the work>.`
   A later `job.complete` for the same job that carries a good grade proceeds as today, and the job's state keeps `grade`.
4. `data/transcripts/scripts/tests/test_inbound_cloud.py`, run as a plain script (`python <file>`), every model call, text
   send, bus send and gateway call faked:
   - a message asking for a fix yields a text containing `WORK REQUESTED by`, `Recommend:` and `#dev`, and it is one text;
   - the difference control: a message that asks for nothing yields a text byte-identical to today's shape, with none of
     those three; a model answer that is not JSON does the same;
   - with a four-box `bus_devices`, `on_job_open` offers to four boxes; three bids do not award early and the fourth does;
     an unavailable bid never wins;
   - a `job.complete` with no grade, with verdict "FAIL", and with `by` equal to `coo` each leave status `working`, draft
     nothing and text the refusing line; one with a good grade reaches `verify`.
   LAST line `INBOUND-CLOUD-TEST ok=<True|False> cases=<passed>/<total>`.
5. In your deliverables folder, `INBOUND_CLOUD_DEPLOY_NOTES.md`: the two policy statements the function's role needs to send
   to the two Dell queues (write them as text; do NOT edit any Terraform file), and anything else the deploy after the drain
   must carry.

### RULES FOR THIS CELL

- **Nothing you run leaves this machine.** No call to the model, no text, no bus send, no gateway call, no AWS call: every
  test fakes them. Do not invoke or deploy the function. Edit nothing under `infra/`.
- The standing rule stays: nothing goes to Teams without Andrew's 1, and no job opens without his `#dev`.
- Build no alert, monitor or new notification: the ONLY text you change is the one he already gets.
- Keep every existing behaviour of the End of Day post untouched. Existing test files under
  `data/transcripts/scripts/tests/` are not yours to edit; if one fails because of your change, that is a surprise row.
- No non-ASCII in any file you write. Bake no absolute path. No client, firm or person name in a test beyond invented ones.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTi1-AC1" cell_refs="CT-i-1"><invocation>python data/transcripts/scripts/tests/test_inbound_cloud.py</invocation><expect>INBOUND-CLOUD-TEST ok=True</expect></criterion>
`CTi1-AC1` -- the text with its recommendation and its difference control; the four-box offer; the refused ungraded completion.

<criterion id="CTi1-AC2" cell_refs="CT-i-1"><invocation>python data/transcripts/scripts/teams_chat/gen_bus_devices.py --check</invocation><expect>BUS-DEVICES ok=True</expect></criterion>
`CTi1-AC2` -- the seam with the real neighbour: the packaged box map equals the real device register.
</proof_of_spec>

<expected_criteria>CTi1-AC1,CTi1-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~31/NFRA_CTLPLN.TO-CT-i-1.teams-request-text-and-offer.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CTi1-AC1,CTi1-AC2`, and flip `<status>` to `complete` only when
every criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.inbound1.md</decomp_doc>
<owned_cells>CT-i-1</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/tenant.py
data/transcripts/scripts/teams_chat/assist.py
data/transcripts/scripts/teams_chat/NAMES.json
data/transcripts/scripts/teams_chat/gen_bus_devices.py
data/transcripts/scripts/tests/test_inbound_cloud.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell changes no clock; the function's one-minute ingress clock is unchanged.
comp-iam: RUN by reading infra/aws/terraform/transcripts/chat_assist.tf:88-89 -- the role sends to two bus queues; the two Dell queues need two statements, which this cell writes as text only; the access change is the issuer's deploy order after the drain.
comp-adversary: RUN -- a job opened without his word (the recommendation only changes the text; #dev stays the only opener); a second text per message (asserted one); a model answer that breaks the text (non-JSON fails closed to today's text; a criterion); a box named by hand again (the map is generated from the register and checked against it); a completion nobody graded reaching the requester (refused; a criterion with its passing arm); the End of Day post disturbed (existing tests untouched and re-run at the drain). BLIND: the model's judgment on real messages; the real run is the outcome's proof.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.18 @55e2de3227 (ADMITTED), FWD-20, C-SEATS clause 8, call C of ADDENDUM v0.17; brief
I.0, O1, O3, F2; CTO ruling msg 106585.
