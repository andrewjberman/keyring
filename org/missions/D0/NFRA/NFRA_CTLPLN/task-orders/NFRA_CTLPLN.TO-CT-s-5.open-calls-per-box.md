# TO NFRA_CTLPLN.TO-CT-s-5 -- workstream SEATS round 1 CT-s-5: one list of every open call per box, and a MEASUREMENT of whether a call touches only that box

<to_id>NFRA_CTLPLN.TO-CT-s-5</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~15</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>SEATS</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-s-5` (`decompositions/NFRA_CTLPLN_DECOMP.seats1.md`) | **outcome_ref:** FWD-22 |
**Andrew's lines served (the delivery list):** 8, 9, 24 | **depends_on:** none (the shared files below are the seam)

---

## WORKER FACE

### THE CELL

`CT-s-5`, C-SEATS clause 4: "The CTO of a fabric holds one list of every open call on it. 'Touches only its fabric' is measured,
not judged: by the paths and risk class of the orders involved, the project's placement, and the cloud resources its Terraform
root names; a shared bucket or a shared trunk touches every fabric." His words: "They are responsible for accruing any and all
/open-calls on their fabric. If the open call in question only pertains to their fabric, does not interfere with any other
projects resources or materials, they can adjudicate them." MEASURED TODAY: `.claude/skills/open-calls/SKILL.md` sweeps ONE
seat's own vantage and prints cards in chat; it writes no file and runs no tool; its `--adjudicate <PROJECT>` form at the CTO
is one project. Nothing holds one list per box.

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

1. `.tools/open-calls.py`, for the box it runs on (device from `AGENTBUS_DEVICE` through `lib/devices.py`):
   - `add --project <CODE> --subject <text> --asked-by <serial> --source <path> [--orders <order file> ...] [--roots <dir> ...]`
     appends one call to `org/devices/state/<device>/open_calls.json` (THE SEAM; this box's file only: it refuses to write
     another box's) with an id `<device>-<UTC stamp>-<4 hex>`, state OPEN, and its measured scope (below).
   - `list [--device <d>|--all]` prints the list(s) with each file's age; `--all` reads every box's file that exists in this
     tree and names the boxes whose file is absent (absent is not empty).
   - `close --id <id> --by <serial> --ruling <path>` sets a call CLOSED with the ruling's path; it REFUSES when the call's scope
     reads CROSS-BOX and no cross-box file (THE SEAM, `org/devices/crossbox/`) for that call reads CLOSED-BOTH: a call that
     touches another box is not settled alone.
   - `scope --project <CODE> [--orders ...] [--roots ...]` is the MEASUREMENT, printed with its evidence and saved on the call:
     (a) PATHS: the union of `<paths>` of the orders named (or of the project's non-terminal orders when none are named); a path
     under another project's home, or in the write set of a project placed on another box (use `.tools/placement-check.py`'s
     functions: import them), is a hit;
     (b) RISK: the highest `<risk>` among those orders (WORLD is printed; it does not alone make a call cross-box);
     (c) PLACEMENT: the project row's `placement` against this box; a project placed elsewhere is a hit;
     (d) RESOURCES: for each Terraform root named (or inferred from the orders' paths under `infra/aws/terraform/`), the bucket
     names and other shared resource names it declares, compared with the same reading of every other box's placed projects'
     roots; a resource two boxes' projects both name is a hit. A SHARED set always reads as touching every box: the shared
     branch (any path in the lane table whose lane is the trunk's own registers: `org/missions/DIRECTIVES.yaml`,
     `org/missions/MACROS.yaml`, `.owned-paths.yaml`, `CLAUDE.md`, `org/XXX.md`, `.tools/**`, `lib/**`, `.claude/**`) and any
     bucket the naming registry marks shared between firms or boxes (read `infra/logic/registry/` for how a shared bucket is
     marked; if you cannot find a mark, say so and treat only an explicit list in the script's head as shared).
     LAST line `CALL-SCOPE project=<CODE> device=<d> paths=<clear|hit> placement=<clear|hit> resources=<clear|hit> shared=<clear|hit> risk=<LOCAL|SERVED|WORLD> verdict=<OWN-BOX|CROSS-BOX>`.
     `OWN-BOX` means that box's CTO may settle it; an act only Andrew can do still goes to him, named as that act (the tool
     prints that sentence; it does not decide what is such an act).
   - `scope --selftest`: fixtures for each hit kind and one clear case; LAST line `CALL-SCOPE-SELFTEST cases=<k>/<n> ok=<True|False>`.
2. `.claude/skills/open-calls/SKILL.md`: a CTO running it on its box ends by writing each card to the box's list through
   `open-calls.py add` and prints the list's path; the `--adjudicate` form runs `scope` first and proceeds only on OWN-BOX,
   routing a CROSS-BOX call to the cross-box route (`.tools/crossbox-call.py`, another cell's). The skill's existing sweep and
   card format stay.
3. `.tools/tests/test_open_calls.py`: add, list and close on a temporary state directory (the tool honours an environment
   variable `OPAL_STATE_ROOT` for tests); a call on another box's file is refused; a CROSS-BOX call cannot be closed without
   its CLOSED-BOTH file and can with it; `--all` names a box with no file as absent; an unknown key in a list file is refused.
   LAST line `OPEN-CALLS-TEST cases=<k>/<n> ok=<True|False>`.

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
<criterion id="CTs5-AC1" cell_refs="CT-s-5"><invocation>python .tools/tests/test_open_calls.py</invocation><expect>OPEN-CALLS-TEST cases=</expect></criterion>
`CTs5-AC1` -- every case passing: the line must read `ok=True`.

<criterion id="CTs5-AC2" cell_refs="CT-s-5"><invocation>python .tools/open-calls.py scope --selftest</invocation><expect>CALL-SCOPE-SELFTEST cases=</expect></criterion>
`CTs5-AC2` -- each kind of cross-box hit is measured and a clear case reads OWN-BOX: the line must read `ok=True`.

<criterion id="CTs5-AC3" cell_refs="CT-s-5"><invocation>python .tools/open-calls.py scope --project NFRA_CTLPLN --roots infra/aws/terraform/shared-infra</invocation><expect>verdict=CROSS-BOX</expect></criterion>
`CTs5-AC3` -- the difference control on a real case: this project's fence root declares the firm buckets every box's projects read, so it cannot read OWN-BOX.
</proof_of_spec>

<expected_criteria>CTs5-AC1,CTs5-AC2,CTs5-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~15/NFRA_CTLPLN.TO-CT-s-5.open-calls-per-box.proof_of_spec.json`, validate it
with `python .tools/proof-of-spec-check.py <instance> CTs5-AC1,CTs5-AC2,CTs5-AC3`, and flip `<status>` to `complete` only when every criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.seats1.md</decomp_doc>
<owned_cells>CT-s-5</owned_cells>
</decomp_ref>

<paths>
.tools/open-calls.py
.tools/tests/test_open_calls.py
.claude/skills/open-calls/SKILL.md
org/devices/state/
.tools/placement-check.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a cross-box call settled alone because the measurement read clear on a path it did not look at (four readings, a shared set that always hits, and a real root as the control); one box writing another box's list (refused: one writer per box); an absent list read as an empty one (named absent, with each file's age); the tool deciding what only Andrew can do (it prints the sentence and decides nothing); BLIND: a resource shared in practice that no Terraform declares.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: Andrew-direct 2026-10-07 ~16:3xZ (record above), ~18:3xZ item 7, ~18:5xZ, ~19:0xZ, and ~21:1xZ at this seat's terminal
(`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261007_211xZ_COO_C_MAKE_SURE_GITOPS_AWSOPS_AGENT_WORKFLOW_DEMANDS_ARE_MET_AND_SAY_LINE_FOR_LINE.md`);
PRD `prd/NFRA_CTLPLN_PRD.md` v0.19 @b44686cebc (ADMITTED), FWD-21 to FWD-25, contract C-SEATS clauses 1 to 7; CTO msg 106584 (the split).
