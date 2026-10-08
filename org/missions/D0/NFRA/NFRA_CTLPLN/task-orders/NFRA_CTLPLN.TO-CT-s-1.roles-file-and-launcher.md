# TO NFRA_CTLPLN.TO-CT-s-1 -- workstream SEATS round 1 CT-s-1: ONE file stating each seat in Andrew's terms, handed to a seat by the launcher at start on any box

<to_id>NFRA_CTLPLN.TO-CT-s-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~6</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>SEATS</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-s-1` (`decompositions/NFRA_CTLPLN_DECOMP.seats1.md`) | **outcome_ref:** FWD-25 |
**Andrew's lines served (the delivery list):** 1, 11, 15, 18 | **depends_on:** none (the shared files below are the seam)

---

## WORKER FACE

### THE CELL

`CT-s-1`, C-SEATS clause 1: "One statement of each seat. MSTR, CTO, COO, CVO, CRO: what each is and does, in Andrew's terms as
tabled in his record, lives in one file that the launcher hands a seat at start. Skills and gates cite it; none restates it."
MEASURED TODAY: the launcher `.tools/ajb.ps1` builds each seat's first message from text written INLINE in the script
(`Get-AgentLoopDirective`, a `switch -Regex` on the base serial, about lines 59 to 112; the message is assembled about lines
189 to 196). It reads no file. The text differs by seat kind and not by device. A worker serial `0.9.0_WK_*` matches no arm and
falls to the default. No file states what each seat is.

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

1. `org/ref/SEAT_ROLES.json`, in THE SEAM's shape. For MSTR, CTO, COO, CVO and CRO the `is`, `does` and `does_not` text is taken
   from Andrew's record: the table "What it states, by seat" and his verbatim paragraph above it; quote his words where the
   table quotes them and add nothing he did not say (`words`: "andrew"). For CLOUDOPS, TIER2 and WORKER carry over what the
   launcher's existing arms say (`words`: "launcher"). `drives` for COO is his three: `canonical-drive`, `closer-drive`,
   `remote-drive`. `serial_pattern` per kind is derived from the launcher's existing regular expressions (read them; say where
   two arms merge into one kind, for example the two CTO arms).
2. `lib/seat_roles.py`: `load()`, `kind_of(serial)` (lane stripped; UNKNOWN when no kind matches or two match), `statement(kind)`
   (the text a seat is handed: is, does, does not, drives), and `validate()` (closed key set; every kind has a non-empty `is`;
   every `drives` entry is a directory under `.claude/skills/`; patterns compile; the five of his kinds are present). A command
   line: `python lib/seat_roles.py kind <serial>`, `statement <serial>`, `validate`.
3. `.tools/ajb.ps1` hands the seat its statement: the first message gains, after the watcher line and BEFORE the existing role
   text, the block `statement(kind)` produced by calling `python lib/seat_roles.py statement <serial>` (resolve python the way
   the script already resolves its tools; if the call fails or the kind is UNKNOWN, the launch PROCEEDS with the existing text
   and one loud line `SEAT-ROLES: no statement for <serial> (<reason>)`: a seat must never fail to start because of this
   file). The existing arms' operational lines (which skills to run once, the loop arming) STAY in the script; the sentences in
   them that say what a seat IS are removed where the file now says it, so nothing is stated twice. Add a `-PrintPrompt`
   switch that prints the assembled first message for a serial and exits WITHOUT launching anything; the tests use only that.
   Add an arm for `0.9.0_WK_*` so a worker serial no longer falls to the default.
   You do NOT launch a seat, and you do not change how `claude` is invoked, the model lines, or the headless tool list.
4. `.tools/tests/test_seat_roles_launcher.py`: `validate` passes; `kind_of` for one serial of each kind, with and without a
   lane, including `0.0.0_AB_MSTR~DELL1` and a worker; an unknown serial is UNKNOWN; for each of the eight kinds the launcher's
   `-PrintPrompt` output contains that kind's `is` sentence from the file character for character; with the file moved aside
   (in a scratch copy of the three files, never the real ones) `-PrintPrompt` still prints a prompt and the loud line; the
   launcher text no longer contains a second statement of what MSTR is (assert the old sentence is gone). LAST line
   `SEAT-ROLES-TEST kinds=<k>/8 prompts=<p>/8 fallback_ok=<True|False> ok=<True|False>`.

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
<criterion id="CTs1-AC1" cell_refs="CT-s-1"><invocation>python lib/seat_roles.py validate</invocation><expect>SEAT-ROLES kinds=8</expect></criterion>
`CTs1-AC1` -- the file is well formed and holds his five kinds; the same line must read `ok=True`.

<criterion id="CTs1-AC2" cell_refs="CT-s-1"><invocation>python .tools/tests/test_seat_roles_launcher.py</invocation><expect>SEAT-ROLES-TEST kinds=8/8 prompts=8/8 fallback_ok=True ok=True</expect></criterion>
`CTs1-AC2` -- every kind is handed its statement by the launcher, and a missing file cannot stop a launch.
</proof_of_spec>

<expected_criteria>CTs1-AC1,CTs1-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~6/NFRA_CTLPLN.TO-CT-s-1.roles-file-and-launcher.proof_of_spec.json`, validate it
with `python .tools/proof-of-spec-check.py <instance> CTs1-AC1,CTs1-AC2`, and flip `<status>` to `complete` only when every criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.seats1.md</decomp_doc>
<owned_cells>CT-s-1</owned_cells>
</decomp_ref>

<paths>
org/ref/SEAT_ROLES.json
lib/seat_roles.py
.tools/ajb.ps1
.tools/tests/test_seat_roles_launcher.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a launcher that fails to start a seat because the new file is missing or malformed (the launch proceeds on the existing text with a loud line; tested on a scratch copy); his words paraphrased into something he did not say (quoted from the record; a kind marked by whose words it carries); a role stated twice and drifting (the script keeps only operational lines; the old sentence asserted gone); a test that launches a real seat (a print-only switch); BLIND: whether a seat that is handed the statement acts on it -- that is the exercise at the close, one seat of each kind asked what it is.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: Andrew-direct 2026-10-07 ~16:3xZ (record above), ~18:3xZ item 7, ~18:5xZ, ~19:0xZ, and ~21:1xZ at this seat's terminal
(`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261007_211xZ_COO_C_MAKE_SURE_GITOPS_AWSOPS_AGENT_WORKFLOW_DEMANDS_ARE_MET_AND_SAY_LINE_FOR_LINE.md`);
PRD `prd/NFRA_CTLPLN_PRD.md` v0.19 @b44686cebc (ADMITTED), FWD-21 to FWD-25, contract C-SEATS clauses 1 to 7; CTO msg 106584 (the split).
