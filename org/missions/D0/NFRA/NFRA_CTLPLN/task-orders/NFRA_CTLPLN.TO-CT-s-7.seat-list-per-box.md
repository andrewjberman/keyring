# TO NFRA_CTLPLN.TO-CT-s-7 -- workstream SEATS round 1 CT-s-7: what each seat on a box is doing, published per box, and the laptop's view of every box with each report's age

<to_id>NFRA_CTLPLN.TO-CT-s-7</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~17</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>SEATS</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-s-7` (`decompositions/NFRA_CTLPLN_DECOMP.seats1.md`) | **outcome_ref:** FWD-23 |
**Andrew's lines served (the delivery list):** 11, 23 | **depends_on:** none (the shared files below are the seam)

---

## WORKER FACE

### THE CELL

`CT-s-7`, FWD-23: "a person reading a box's list of seats can say what each operations seat is doing, and can see one that is
doing nothing"; and Andrew's word of ~19:0xZ: "the laptop needs to know at all times what is going on across the various
devices". His words on the seat: "COOs are the workers, they either run /canonical-drive /closer-drive to proceed projects,
running /remote-drive if a one-off request comes in." MEASURED TODAY: every seat list is ONE box's: the broker's
`get_live_agents` and `get_agent_status` read this box's `org/mcp/liveness.json`; `.tools/fabric-check.py` fuses this box's
telemetry and summaries; `.tools/drive-mode.py status` reads device-local markers under `org/mcp/drive_mode/`;
`org/ref/LIVE_ARMS.md` is a hand-landed register of which loop each seat is AUTHORISED to run on all four boxes (authorisation,
not activity); `.tools/sequence-check.py` reports the laptop's cap as a viewer. No tool shows what each COO on every box is
doing. This cell builds a READ made on demand. It builds no alert, no notification and no monitor.

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

1. `.tools/seat-list.py`, for the box it runs on (device from `AGENTBUS_DEVICE` through `lib/devices.py`):
   - `write` builds this box's list and writes `org/devices/state/<device>/seats.json` (THE SEAM; this box's file only). One row
     per live seat on the box (from this box's `org/mcp/liveness.json`; a seat registered but STALE is listed as STALE, not
     dropped): `serial`, `kind` (through `lib/seat_roles.py kind_of`; if that module is not in your worktree another cell is
     writing it: use a minimal local fallback reading `org/ref/SEAT_ROLES.json` and the module when present), `summary` (the
     seat's own declared line), and for a COO: `project` (from the summary's project code checked against the project rows:
     a code that is not a project row is printed as `UNRESOLVED`), `drive` (which of `canonical-drive`, `closer-drive`,
     `remote-drive` it is running: from `.tools/drive-mode.py`'s markers for its project and from the `LIVE_ARMS.md` row naming
     its serial, each cited; `NONE` when neither names one), `open_orders` (count of non-terminal task orders it ISSUED, read
     from `<issued_by>` in the order files, never from the broker's base-scoped count), `last_commit_minutes` (anchored author
     filter; `NEVER` when the serial has no commit at all), and `doing` (one of WORKING, IDLE, NOTHING: NOTHING when it has no
     drive, no open order and no commit in the window).
     LAST line `SEAT-LIST device=<d> seats=<n> coo=<c> working=<w> idle=<i> nothing=<x> reviewer=<present|ABSENT> ok=<True|False>`
     (`reviewer` is whether a CVO-kind seat is live on THIS box; `ok=True` when every seat got exactly one `doing`).
   - `show [--device <d>|--all]` prints the saved list(s) as a table a person can read without opening a log, each with the
     file's age in minutes; `--all` reads every box's file present in this tree and names each box whose file is ABSENT or
     older than `--stale-minutes` (default 90) as such. This is the laptop's view: a box's list reaches the laptop by that
     box committing its file and the manager landing it, as any file does.
   - `--from-fixture <dir>` for tests.
2. `.claude/skills/fabric-check/SKILL.md` and `.claude/skills/sequence/SKILL.md`: one added line each pointing a seat that wants
   every box's seats to `python .tools/seat-list.py show --all`, and saying their own output is one box's. `.claude/skills/sequence/SKILL.md`
   says "the laptop's 3-COO cap" in one place: reword it to read the cap from the device register's `seat_limit` for the box
   it runs on. Change no mechanism in either skill's tool.
3. `.tools/tests/test_seat_list.py`: fixtures for a box with a COO on each of the three drives, one with no drive and no order
   (NOTHING), a STALE seat, a box with no reviewer (ABSENT), a COO whose summary names a code that is no project (UNRESOLVED),
   a serial that never committed (NEVER), a base serial and its lane counted as two seats; `show --all` with one box's file
   absent and one stale; one box refusing to write another's file; an unknown key refused. LAST line
   `SEAT-LIST-TEST cases=<k>/<n> ok=<True|False>`.

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
<criterion id="CTs7-AC1" cell_refs="CT-s-7"><invocation>python .tools/tests/test_seat_list.py</invocation><expect>SEAT-LIST-TEST cases=</expect></criterion>
`CTs7-AC1` -- every case passing: the line must read `ok=True`.

<criterion id="CTs7-AC2" cell_refs="CT-s-7"><invocation>python .tools/seat-list.py write</invocation><expect>SEAT-LIST device=</expect></criterion>
`CTs7-AC2` -- the list is built for this box from the real fabric (it writes only this box's state file): the same line must read `ok=True`, and its `coo=` count is compared by the issuer with the live seats at the drain.
</proof_of_spec>

<expected_criteria>CTs7-AC1,CTs7-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~17/NFRA_CTLPLN.TO-CT-s-7.seat-list-per-box.proof_of_spec.json`, validate it
with `python .tools/proof-of-spec-check.py <instance> CTs7-AC1,CTs7-AC2`, and flip `<status>` to `complete` only when every criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.seats1.md</decomp_doc>
<owned_cells>CT-s-7</owned_cells>
</decomp_ref>

<paths>
.tools/seat-list.py
.tools/tests/test_seat_list.py
.claude/skills/fabric-check/SKILL.md
.claude/skills/sequence/SKILL.md
org/devices/state/
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a monitor or an alert built by another name (a read on demand that writes one file; nothing watches or notifies); one box's list read as the fabric's (each file carries its box and age; an absent or stale file is named so); a seat doing nothing hidden by its own summary (drive, open orders and commits are measured, not taken from the summary); the broker's base-scoped counts read as a lane's (orders are parsed from the order files); one box writing another's file (refused); BLIND: what a seat is doing between commits, and any box whose file has not been landed.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: Andrew-direct 2026-10-07 ~16:3xZ (record above), ~18:3xZ item 7, ~18:5xZ, ~19:0xZ, and ~21:1xZ at this seat's terminal
(`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261007_211xZ_COO_C_MAKE_SURE_GITOPS_AWSOPS_AGENT_WORKFLOW_DEMANDS_ARE_MET_AND_SAY_LINE_FOR_LINE.md`);
PRD `prd/NFRA_CTLPLN_PRD.md` v0.19 @b44686cebc (ADMITTED), FWD-21 to FWD-25, contract C-SEATS clauses 1 to 7; CTO msg 106584 (the split).
