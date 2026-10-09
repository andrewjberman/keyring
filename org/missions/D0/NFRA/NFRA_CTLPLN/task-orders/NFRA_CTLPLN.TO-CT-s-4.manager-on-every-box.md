# TO NFRA_CTLPLN.TO-CT-s-4 -- workstream SEATS round 1 CT-s-4: the fabric manager on every box: its skills read the device register, its loop finds a hung seat, and its record is read for project rulings

<to_id>NFRA_CTLPLN.TO-CT-s-4</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~14</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>SEATS</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-s-4` (`decompositions/NFRA_CTLPLN_DECOMP.seats1.md`) | **outcome_ref:** FWD-21 |
**Andrew's lines served (the delivery list):** 1, 3 | **depends_on:** none (the shared files below are the seam)

---

## WORKER FACE

### THE CELL

`CT-s-4`, FWD-21 and C-SEATS clause 3: "A fabric manager's record carries no project ruling. Its acts are merges, pulls, pushes,
integration, spawn, kill, unstick and the bid. A question of substance it receives is passed to its CTO, by a file." His
words: "MSTR whole purpose is not business logic/project reasoning, they are infrastructure managers ... They also can manage
/unstick /mstr-spawn /mstr-kill to keep their fabric running cleanly." MEASURED TODAY: the manager's loop
`.claude/skills/govern/SKILL.md` has NO step that measures a hung or dead seat (it sweeps tagged inbox subjects and a block
report), admits only the bare manager serial at Step 0, and Step 3b hardcodes a two-box world (one bus frame to the site-Z
manager; "laptop-placed" against "sitez-placed"). `.claude/skills/mstr-review/SKILL.md` checks six fixed Tier-1 serials for
liveness and warns in text that liveness is device-local. `mstr-spawn`, `mstr-kill`, `unstick` and their engines are local to
the box they run on and name no device, which is right; none reads `org/devices/DEVICES.json`. `.claude/skills/agentbus/SKILL.md`
and the bus script's usage text still describe two devices. No tool reads a manager's day for project rulings.

Andrew's words, verbatim and entire, are in `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_163xZ_FABRIC_ROLES_MSTR_CTO_COO_CVO_CRO_AND_THE_INBOUND_WORK_PIPELINE_INTO_NFRA_CTLPLN.md`. Read that record first. The line-for-line list this cell serves is
`org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_CTLPLN_SEAT_ROLES_LINE_FOR_LINE_DELIVERY_COO_C_20261007.md`.

### THE SEAM

THE SHARED FILES (fixed here so the eight cells share FILES and never wait on each other's code). All are JSON, UTF-8,
ASCII-only, and every reader REFUSES a key it does not know.
- `org/ref/SEAT_ROLES.json` (written by cell CT-s-1; read by every other cell): `schema` "seat-roles/1", `source` (the path of
  Andrew's record), `kinds`: a list of objects `kind` (one of MSTR, CTO, COO, CVO, CRO, CLOUDOPS, TIER2, WORKER),
  `serial_pattern` (a regular expression on the BASE serial, lane stripped), `is` (one sentence), `does` (list),
  `does_not` (list), `drives` (list of skill names the kind runs), `words` ("andrew" when `is`/`does` are his recorded words,
  "launcher" when carried over from the launcher's existing text). A serial that matches no kind is UNKNOWN, never guessed.
  Readers resolve a serial to a kind ONLY through `lib/seat_roles.py` `kind_of(serial)` (CT-s-1 writes it).
- `org/ref/SEAT_RULES.json` (written by cell CT-s-2): `schema` "seat-rules/1", `rules`: a list of objects `id` (R-<AREA>-<n>),
  `area` (GITOPS, AWSDEVOPS or WORKFLOW), `kinds` (list of kinds it binds), `rule` (one sentence), `holder` (exactly one of
  LAUNCHER, SKILL, GATE), `mechanism` {`path`, `entry`} (the file and the function, step or line that holds it),
  `probe` (for a GATE rule: the forbidden act as a command the checker can run in a scratch or dry mode, with the refusal text
  it expects; null otherwise), `built_by` (a cell id of this workstream when the mechanism is one this workstream builds, else
  "existing"), `needs_andrew` (true where the rule cannot be finished without a decision only he can make, with `question`).
- `org/devices/state/<device>/` (ONE WRITER: the box named, resolved from the environment variable `AGENTBUS_DEVICE` and
  `lib/devices.py`, never from a path): `seats.json` (CT-s-7), `open_calls.json` (CT-s-5). Each file carries `device`,
  `written_at` (UTC), `written_by` (serial) and its rows. A reader on another box prints each file's AGE beside what it reads.
- `org/devices/crossbox/<id>.json` (CT-s-6): one cross-box call or cross-box order as a file: `id`, `kind` ("CALL" or "ORDER"),
  `from_device`, `to_device`, `from_serial`, `to_serial`, `subject`, `body_path` (a file in the repository; the message never
  carries the substance), `state` (OPEN, ACKED, CLOSED-BOTH), `sent` {`at`, `bus_message_id`}, `ack` {`at`, `by`,
  `bus_message_id`} or null, `closed` {`from_at`, `to_at`} with either side null until that side closes.
THE DEVICE REGISTER is `org/devices/DEVICES.json`, read only through `lib/devices.py`. No cell types a device name, a serial
of a particular box, or a path under a user's home.

### BUILD

1. `.tools/seat-liveness.py` (the measurement the loop lacks), for the box it runs on (device from `AGENTBUS_DEVICE` through
   `lib/devices.py`): for each seat in this box's `org/mcp/liveness.json` and each Claude process carrying a serial (process
   truth, as `/mstr-spawn` step 1pt does: extract the serial token and compare exactly, never a substring), classify
   `MOVING` (a commit by that serial's author in the last N minutes, anchored: `git log --author "<serial> <"`; or a deliverable
   written in a live worktree of that serial), `QUIET` (alive, nothing in N minutes, no open order), `HUNG` (alive by process,
   an open task order assigned to it, nothing in N minutes: N from `--minutes`, default 45), `DEAD` (an open order or a
   registered session, no process), `UNKNOWN` (the author filter matches nothing at all in the repository's history: a serial
   that never committed reads UNKNOWN, never QUIET). It prints one line per seat and LAST
   `SEAT-LIVENESS device=<d> seats=<n> moving=<a> quiet=<b> hung=<c> dead=<e> unknown=<u> ok=<True|False>`. It READS; it does not
   unstick, spawn or kill. `--from-fixture <dir>` runs it on a recorded fixture for tests.
2. The manager's loop uses it, on every box: `.claude/skills/govern/SKILL.md` gains one step: run `seat-liveness.py`; for a HUNG
   seat run `/unstick` on it; for a DEAD seat whose order is still open, respawn it by `/mstr-spawn` (its own pre-flight
   stands); record each act in the manager's log. Step 0 admits a manager serial WITH a lane (`0.0.0_AB_MSTR~<lane>`), since
   each box's manager is a lane. Step 3b's two-box text becomes register-driven: the other boxes are read from
   `bash .tools/agentbus-sqs.sh devices`, and a frame goes to each other box's manager; no box is named in the skill.
   `.claude/skills/mstr-review/SKILL.md`: the six fixed serials become "the Tier-1 kinds in `org/ref/SEAT_ROLES.json` that this
   box's seat list holds", and a box with no reviewer seat is a finding (C-SEATS clause 7; cell CT-s-8 holds the refusal).
   `.claude/skills/agentbus/SKILL.md` and the usage strings in `.tools/agentbus-sqs.sh` (TEXT ONLY in that script: its usage
   lines; you change no logic there) describe the devices the register lists, not two by name.
   `mstr-spawn`, `mstr-kill`, `unstick`: add one sentence each that they act on THIS box only and that another box's seat is
   that box's manager's, with the register as the list of boxes; change no mechanism.
3. `.tools/mstr-record-check.py --serial <manager serial> --since <UTC> [--until <UTC>]`: reads that manager's day and lists
   anything that looks like a project ruling, for a reviewer to judge: its commits in the window touching a path whose lane is
   a project's specification, decomposition, task order, adjudication or remediation (most are already refused; a merge is
   exempt from lane checks, so a manager's MERGE commit that changes such a path with content not present on either parent is
   listed); and its sent messages in the window (`org/mcp/` holds the broker's outbox and delivery log: find where sent
   messages are kept and read them; if they cannot be read from files, say so and mark that limb UNREAD) whose subject begins
   `RULING`, `DECISION` or `ADJUDICATION`, or whose first line answers a question about a project code that is not about a
   merge, a push, a spawn, a kill, an unstick or the bid. LAST line
   `MSTR-RECORD serial=<s> window=<h>h commits=<n> ruling_paths=<a> messages=<m> ruling_shaped=<b> unread_limbs=<u> ok=<True|False>`
   (`ok=True` when every limb was read; the counts are the finding, graded by the reviewer, never by this tool).
   `--selftest`: on fixtures, a manager commit to a decomposition and a message subject `RULING ...` are both listed, and a
   merge message and a spawn notice are not.
4. `.tools/tests/test_manager_on_every_box.py`: `seat-liveness.py` on fixtures for each of the five classes, including the
   never-committed serial reading UNKNOWN and a base serial not matching its own lanes; the three skills' text contains no
   device name outside a quoted example (grep the skill files for the register's device names and the old two-box phrases);
   `mstr-record-check.py --selftest`. LAST line `MANAGER-TEST cases=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

**Nothing you run changes the live fabric.** You do not start, stop or message any seat; you do not push, merge or rebase;
you run no `terraform` against a backend and no `aws` call that writes; you send nothing on the agent bus (bus code is tested
against a stand-in). Tests run in temporary directories or on scratch copies. No request leaves this machine.
The law files `CLAUDE.md` and `org/XXX.md` are LOCKED: you do not edit them. `org/tier0/STAKES_MATRIX.md` is Andrew's alone.
`.claude/settings.json` is not in any grant: no new hook is wired by a worker; a new check is called from an existing wrapper
or tool, or it is a tool a seat runs.
No non-ASCII in any file you write. Python: standard library only unless the order names a package; ruff clean.
Shell: Git Bash default utilities only. PowerShell: Windows PowerShell 5.1 syntax (no `&&`, no ternary).

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTs4-AC1" cell_refs="CT-s-4"><invocation>python .tools/tests/test_manager_on_every_box.py</invocation><expect>MANAGER-TEST cases=</expect></criterion>
`CTs4-AC1` -- every case passing: the line must read `ok=True`.

<criterion id="CTs4-AC2" cell_refs="CT-s-4"><invocation>python .tools/seat-liveness.py</invocation><expect>SEAT-LIVENESS device=</expect></criterion>
`CTs4-AC2` -- the measurement runs on this box against the real fabric (read only); the same line must read `ok=True`.

<criterion id="CTs4-AC3" cell_refs="CT-s-4"><invocation>python .tools/mstr-record-check.py --selftest</invocation><expect>MSTR-RECORD-SELFTEST</expect></criterion>
`CTs4-AC3` -- a planted project ruling in a manager's record is listed and ordinary manager acts are not; the line must read `ok=True`.
</proof_of_spec>

<expected_criteria>CTs4-AC1,CTs4-AC2,CTs4-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~14/NFRA_CTLPLN.TO-CT-s-4.manager-on-every-box.proof_of_spec.json`, validate it
with `python .tools/proof-of-spec-check.py <instance> CTs4-AC1,CTs4-AC2,CTs4-AC3`, and flip `<status>` to `complete` only when every criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.seats1.md</decomp_doc>
<owned_cells>CT-s-4</owned_cells>
</decomp_ref>

<paths>
.tools/seat-liveness.py
.tools/mstr-record-check.py
.tools/tests/test_manager_on_every_box.py
.claude/skills/govern/SKILL.md
.claude/skills/mstr-review/SKILL.md
.claude/skills/mstr-spawn/SKILL.md
.claude/skills/mstr-kill/SKILL.md
.claude/skills/unstick/SKILL.md
.claude/skills/agentbus/SKILL.md
.tools/agentbus-sqs.sh
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a manager that respawns a seat a person launched (the spawn skill's own process-truth pre-flight stands and is not weakened); a quiet seat read as hung, or a serial that never existed read as quiet (five classes, an anchored author filter, a positive control for a filter that matches nothing); a base serial matched as its own lanes (exact token comparison); a tool that grades the manager (it lists; a reviewer judges); the one cross-device channel broken by an edit to its script (usage text only, no logic); BLIND: a hang with no open order, and a manager's spoken or pasted rulings that are in no file.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: Andrew-direct 2026-10-07 ~16:3xZ (record above), ~18:3xZ item 7, ~18:5xZ, ~19:0xZ, and ~21:1xZ at this seat's terminal
(`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261007_211xZ_COO_C_MAKE_SURE_GITOPS_AWSOPS_AGENT_WORKFLOW_DEMANDS_ARE_MET_AND_SAY_LINE_FOR_LINE.md`);
PRD `prd/NFRA_CTLPLN_PRD.md` v0.19 @b44686cebc (ADMITTED), FWD-21 to FWD-25, contract C-SEATS clauses 1 to 7; CTO msg 106584 (the split).

## AMENDMENT 1 (2.0.0_SA_COO~C, 2026-10-08 ~11:2xZ) -- REOPENED, SHORT: a seat alive on ANOTHER box must never read DEAD

The cell is merged. Its first real use found a defect that nearly caused a duplicate seat. `1.0.0_SA_CTO` msg 106893:
".tools/seat-liveness.py prints DEAD for any serial with an open order and no LOCAL process. The serial string is the same on
every box, and the laptop's broker cannot see another box's sessions. The tool reads each order's project placement
(project.json placement; the device register) and prints a serial placed on another box as ELSEWHERE with the box named, never
DEAD; only a serial placed on this box with no process is DEAD. Its respawn guidance names that difference." The case that
showed it: `0.7.0_AE_CloudOps~A` read DEAD on the laptop with 38 open orders; it is alive on site Z, and a respawn would have
made a duplicate of another box's live seat. Gate limb: none graded this modification.

1. **A new class, ELSEWHERE.** For a serial with no process on this box, read WHERE its open orders' projects are placed: each
   order's project code -> that project's `project.json` `placement` field (values such as LAPTOP, SITEZ, DELL1, DELL2; read the
   register for the exact set, and `org/devices/DEVICES.json` for how a placement value names a device). Then:
   - every open order's project is placed on ANOTHER box -> `ELSEWHERE(<box>)` (name the box, or the boxes if more than one);
   - at least one open order's project is placed on THIS box -> the class is decided as today (DEAD when no process), and the
     line says how many of its orders are placed here and how many elsewhere;
   - a project with NO placement value, or an order whose project cannot be read -> the seat is `UNKNOWN` with the reason
     "placement unread for <n> order(s)", NEVER DEAD: an unread placement must not license a respawn.
   Also read the lane suffix as evidence where the register gives it meaning (a `~DELL1`, `~DELL2`, `~Z` style lane, or a lane
   the device register lists for a box): report what you found the register says about lanes and use it only if it is data
   in a file, not a naming guess.
2. The last line gains `elsewhere=<n>` between `dead=` and `unknown=`:
   `SEAT-LIVENESS device=<d> seats=<n> moving=<a> quiet=<b> hung=<c> dead=<e> elsewhere=<f> unknown=<g> ok=<...>`.
3. **Respawn guidance** in `/govern` Step 3a (the skill text you wrote): a DEAD seat is a seat placed on THIS box; ELSEWHERE is
   never respawned here and is that box's manager's to look at (name the cross-box route: the manager asks the other box's
   manager over the bus); UNKNOWN is never respawned. Keep your date guard for DEAD.
4. Tests in `.tools/tests/test_manager_on_every_box.py`: all orders placed elsewhere -> ELSEWHERE with the box named; mixed ->
   decided as today with both counts; placement missing -> UNKNOWN; a seat placed here with no process -> DEAD still.
5. Run the tool on this machine and report the line and, for each seat that read DEAD in your last pass, what it reads now.

**ACCEPTANCE.** `CTs4-AC1`, `CTs4-AC3` unchanged. `CTs4-AC2`'s expectation: if the order's `<expect>` for it names the fields
after `dead=`, the issuer changes it by this amendment to `SEAT-LIVENESS device=laptop seats=`; write the proof row's `expect`
equal to the order's text as you find it after this amendment. Rewrite the proof instance, validate, flip to `complete`.

## AMENDMENT 2 (2.0.0_SA_COO~C, 2026-10-09 ~02:2xZ) -- REOPENED, SHORT: a STAGED order is not open work, and an order's status is its LAST tag

The tool's next defect came from the field. `0.0.0_AB_MSTR` msg 107619 relayed dell1's manager (bus 4dabb0a4) verbatim:
"seat-liveness counts a STAGED task order as open work, so it reads a correctly idle seat as HUNG. Case:
0.7.0_AE_CloudOps~DELL1 flagged HUNG (99 min) on AMGT_RESAPP.TO-AMGT-dd-4, which reads [status tag: staged] at HEAD ...
Ask: exclude staged (not yet GO'd) orders from the HUNG test." The reader is `open_orders_to()` in `.tools/seat-liveness.py`
(about lines 131-155). It treats every non-terminal status as open, and it takes the FIRST status word in the file.
`1.0.0_SA_CTO` msg 107528, the gate owner's ruling, says: "an order's status is its LAST <status> tag". Gate limb: none graded
this modification.

1. **The LAST tag.** An order's status is the last `<status>` tag in the file whose word is in `SL.STATUS_WORDS`, not the first.
2. **Staged is not open work.** An order whose status (rule 1) is `staged` is waiting on its GO. It counts neither toward HUNG nor
   toward DEAD or ELSEWHERE. A seat whose only non-terminal orders are staged is classed as if it had no open order. Where the
   seat's reason line names its orders, it adds `staged=<n>` so the staged work stays visible.
3. Tests in `.tools/tests/test_manager_on_every_box.py`:
   - a live, silent seat whose only order is staged reads QUIET, never HUNG;
   - the same seat with one pending order beside the staged one reads HUNG still;
   - an order reading `pending` then `complete` (last tag complete) is not open;
   - an order reading `complete` then `pending` (last tag pending) is open.
4. Run the tool on this machine and report its last line.
5. Do NOT edit `.tools/seat-list.py`; it is outside this grant. If its own status reader shares the first-tag defect, file a row
   (`spec_asserts` + `world_is`) and keep working.

**ACCEPTANCE.** `CTs4-AC1`, `CTs4-AC2` and `CTs4-AC3` are unchanged. Rewrite the proof instance, validate it, and flip to `complete`.
