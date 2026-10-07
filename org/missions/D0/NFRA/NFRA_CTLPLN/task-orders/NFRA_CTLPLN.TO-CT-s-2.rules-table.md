# TO NFRA_CTLPLN.TO-CT-s-2 -- workstream SEATS round 1 CT-s-2: the table of EVERY rule with its one holder, in three parts, and a checker that tries one forbidden act per seat kind

<to_id>NFRA_CTLPLN.TO-CT-s-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~8</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>SEATS</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-s-2` (`decompositions/NFRA_CTLPLN_DECOMP.seats1.md`) | **outcome_ref:** FWD-25 |
**Andrew's lines served (the delivery list):** 18, 19, 20 | **depends_on:** none (the shared files below are the seam)

---

## WORKER FACE

### THE CELL

`CT-s-2`, C-SEATS clause 2: "Where each rule is held (his three: launcher, skill, gate). A rule a tool can check is checked by a
tool; the rest is told at start. The cell ... lists every rule with its holder across the three areas: how code moves, how
cloud changes are made, how seats work." And FWD-25: "when a seat tries the thing its role forbids, a tool refuses or flags
it, and it is not left to another seat to notice; this holds for how code moves, how cloud changes are made, and how seats
work." MEASURED TODAY (a read-only map made for this cut): rules that a tool holds, by seat, are scattered: the shared-branch
push gate (`.tools/hooks/never-rules-gate.sh` GATE 5, admitting only a manager serial, with three portal carve-outs); rebase,
stash, clean and bare `terraform apply` refused for all (same file, GATES 1, 2, 4); the lane table (`.owned-paths.yaml` with
`.tools/owned-paths-validate.py --check-agent`), which refuses a manager on a project's specification, decomposition,
adjudication and remediation files; the manager-to-Tier-2 message bar (`.tools/hooks/mstr-no-tier2-writes.sh`); who may commit
a NEW task order and to whom one may be issued (`.tools/to-pipeline-gate.py` GATE (iv) and GATE (i)); the reviewer's send bar
and the act-carrying send rule (`org/mcp/server.py` `send_message`, `org/mcp/cvo_send_guard.py`); a worker self-grading a
judgment criterion (`.tools/proof-of-spec-check.py`); the stamp signer (`.tools/prd-stamp.py`). For how cloud changes are made
NOTHING is seat-specific today: the apply and deploy wrappers check no serial. Other cells of this workstream build the
missing gates; this cell writes the table and the checker that proves each row.

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

1. `org/ref/SEAT_RULES.json` in THE SEAM's shape. Build it by READING, not from the paragraph above alone: for each of the eight
   kinds in `org/ref/SEAT_ROLES.json` (if that file is not in your worktree, another cell is writing it: use the eight kind names
   in THE SEAM) and each of the three areas, list what the seat must not do and what it must do, each as one rule with its ONE
   holder. Sources to read for rules: Andrew's record (each sentence that says what a seat does or does not do is a rule);
   CLAUDE.md sections 5 and 6, "Agent Autonomy", "Git" and rule 32 (READ ONLY); `org/XXX.md` (READ ONLY); the gates named above;
   the skills `mstr-spawn`, `mstr-kill`, `unstick`, `govern`, `canonical-drive`, `closer-drive`, `remote-drive`, `open-calls`,
   `cloud-ops`. For a GATE rule, `mechanism` is the file and function or gate label, VERIFIED by you to exist at that place
   today (print file and line for each in your report), and `probe` is a command that tries the forbidden act harmlessly.
   Rules whose gate another cell of this workstream builds carry `built_by` and the probe that cell's order names:
   - `CT-s-3`: a seat kind not permitted to apply cloud changes is refused by the apply wrapper
     (probe: `python .tools/apply-who-check.py --serial <serial> --root <root>` expecting `APPLY-WHO ... verdict=REFUSED`);
     and a deploy that could upset another box is stopped (probe: `python .tools/crossbox-deploy-check.py --root <root> --notices <fixture dir>` expecting `verdict=STOP`).
   - `CT-s-4`: a manager's record carrying a project ruling is flagged (probe: `python .tools/mstr-record-check.py --selftest`).
   - `CT-s-5`: a call that touches another box cannot be settled alone (probe: `python .tools/open-calls.py scope --selftest`).
   - `CT-s-6`: a cross-box call is not closed on one side only (probe: `python .tools/crossbox-call.py --selftest`).
   - `CT-s-8`: a round is not closed with no reviewer on the box (probe: `python .tools/round-close-check.py --selftest`); and
     research owed or not is read from the class (probe: `python .tools/research-owed.py --selftest`).
   THREE rules need a decision only Andrew can make and are entered with `needs_andrew: true`, their CURRENT holder and the
   question, never decided here: who pushes the shared branch from a Dell (today only a manager serial, any lane, by GATE 5;
   his standing word is that the laptop's manager integrates and pushes; `org/devices/DEVICES.json` says site Z alone pushes
   the trunk, which is text); the laptop administering bucket, key and queue policies ("For now, laptop should admin"); and the
   routes this project denied the Dells to ten older pipeline roles.
2. `.tools/seat-rules-check.py`:
   - `validate`: closed key set; every rule has exactly one holder; every `mechanism.path` exists; every kind x area pair has
     at least one rule (a pair with none is printed and fails); every GATE rule has a probe; LAUNCHER rules name
     `org/ref/SEAT_ROLES.json` or the launcher; SKILL rules name a file under `.claude/skills/`.
   - `exercise`: for every GATE rule runs its probe in a temporary directory with a 60-second bound and compares the output
     with the expected refusal. A probe whose tool does not exist yet AND whose rule says `built_by` another cell is counted
     `PENDING` (not a pass, not a failure) and named; any other missing tool is a failure. Probes of EXISTING gates must be
     harmless by construction: `--check-agent` reads; hooks are fed a JSON stand-in of the tool call on standard input, exactly
     as the hook's own test battery does (read `.tools/hooks/tests/` for the form); nothing is pushed, committed or sent.
   - LAST line `SEAT-RULES rules=<n> gate=<g> skill=<s> launcher=<l> pairs_covered=<c>/24 probes_pass=<p> probes_pending=<q> probes_fail=<f> needs_andrew=<a> ok=<True|False>`
     (`ok=True` when `validate` passes, `probes_fail=0` and `pairs_covered=24/24`; PENDING is reported, and the issuer's drain
     run must read `probes_pending=0`).
3. `.tools/tests/test_seat_rules_check.py`: a rule with two holders is refused; a kind x area pair with no rule fails; a GATE
   rule with no probe fails; a probe that expects a refusal and gets an admit FAILS (plant one: a rule claiming a manager is
   refused on a path the lane table admits it on); a pending probe is counted pending. LAST line
   `SEAT-RULES-TEST cases=<k>/<n> ok=<True|False>`.

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
<criterion id="CTs2-AC1" cell_refs="CT-s-2"><invocation>python .tools/seat-rules-check.py exercise</invocation><expect>pairs_covered=24/24</expect></criterion>
`CTs2-AC1` -- every seat kind has a rule in each of the three areas, and every probe of an existing gate passes: the same line must read `probes_fail=0 ... ok=True`.

<criterion id="CTs2-AC2" cell_refs="CT-s-2"><invocation>python .tools/tests/test_seat_rules_check.py</invocation><expect>SEAT-RULES-TEST cases=</expect></criterion>
`CTs2-AC2` -- the checker fails on a planted false rule: the line must read `ok=True` with every case passing.
</proof_of_spec>

<expected_criteria>CTs2-AC1,CTs2-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~8/NFRA_CTLPLN.TO-CT-s-2.rules-table.proof_of_spec.json`, validate it
with `python .tools/proof-of-spec-check.py <instance> CTs2-AC1,CTs2-AC2`, and flip `<status>` to `complete` only when every criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.seats1.md</decomp_doc>
<owned_cells>CT-s-2</owned_cells>
</decomp_ref>

<paths>
org/ref/SEAT_RULES.json
.tools/seat-rules-check.py
.tools/tests/test_seat_rules_check.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a table that looks complete because an empty part was not counted (24 kind-by-area pairs, each must hold a rule); a rule claimed to be held by a gate that does not refuse (every gate rule is probed; a planted false rule must fail the checker); a probe that performs the forbidden act (hooks are fed a stand-in; nothing is pushed, committed, sent or applied); a decision of Andrew's made here by entering it as settled (three rules are entered as needing his word); BLIND: rules that exist only in a seat's habit and in no file.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: Andrew-direct 2026-10-07 ~16:3xZ (record above), ~18:3xZ item 7, ~18:5xZ, ~19:0xZ, and ~21:1xZ at this seat's terminal
(`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261007_211xZ_COO_C_MAKE_SURE_GITOPS_AWSOPS_AGENT_WORKFLOW_DEMANDS_ARE_MET_AND_SAY_LINE_FOR_LINE.md`);
PRD `prd/NFRA_CTLPLN_PRD.md` v0.19 @b44686cebc (ADMITTED), FWD-21 to FWD-25, contract C-SEATS clauses 1 to 7; CTO msg 106584 (the split).
