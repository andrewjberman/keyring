# TO NFRA_CTLPLN.TO-CT-s-6 -- workstream SEATS round 1 CT-s-6: the cross-box route: a call or an order travels as a FILE with an acknowledgement from the other side, and closes on both boxes or neither

<to_id>NFRA_CTLPLN.TO-CT-s-6</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~16</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>SEATS</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-s-6` (`decompositions/NFRA_CTLPLN_DECOMP.seats1.md`) | **outcome_ref:** FWD-22 |
**Andrew's lines served (the delivery list):** 10 | **depends_on:** none (the shared files below are the seam)

---

## WORKER FACE

### THE CELL

`CT-s-6`, C-SEATS clauses 5 and 6: "A cross-fabric call goes CTO to its MSTR to the other fabric's MSTR to that CTO, as a file
with an acknowledgement from the other side (sent is not read). It is closed on both boxes or on neither." And: "A laptop
seat's order from another box. Its GO reaches the seat through the laptop's CTO (measured today: an order from dell2 reached
no one, because a Dell cannot message a laptop seat and the manager is barred from that tier). The cell that builds clause 5
closes this route too, so it does not depend on one seat relaying." MEASURED TODAY: `.tools/agentbus-sqs.sh` sends a free-text
envelope to a DEVICE queue with attributes `from`, `sent_at`, `from_tailnet`, `to_tailnet` and no kind; an acknowledgement is
a convention (a reply whose body says `ACK <MessageId> -- READ at ...`) with no stored record on the bus side; the local
broker (`org/mcp/server.py`) does record SENT, EMITTED and READ per message id but is local to one box; a hook
(`.tools/hooks/mstr-no-tier2-writes.sh`) bars a manager from messaging a Tier-2 seat. A typed message for a cross-box call does
not exist. YOU DO NOT CHANGE the bus's send or receive logic, the consumer, the broker or that hook: this cell adds a tool
that USES the bus's existing `send` and reads its existing output, and a file format.

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

1. `.tools/crossbox-call.py`, for the box it runs on (device from `AGENTBUS_DEVICE` through `lib/devices.py`):
   - `open --kind <CALL|ORDER> --to-device <d> --to-serial <serial> --from-serial <serial> --subject <text> --body <path in repo>`
     writes `org/devices/crossbox/<id>.json` (THE SEAM) with state OPEN and prints the ONE line the sending box's manager
     puts on the bus with the existing `bash .tools/agentbus-sqs.sh send <device> ...`: the line begins
     `CROSSBOX <id> <kind> for <to-serial>: <subject> | file org/devices/crossbox/<id>.json @<commit>` and carries no substance.
     It REFUSES when the body file is not committed (the other box reads it by pulling the commit, so an uncommitted body is
     unreadable there) and when `--to-device` is this box.
   - `sent --id <id> --bus-message-id <id>` records the bus message id returned by `send`.
   - `receive --line <the bus line as the consumer printed it>` on the RECEIVING box: parses the `CROSSBOX` line, checks the file
     exists at the named commit in this tree (if not: prints `PULL-FIRST` and the commit, and writes nothing), and DELIVERS it
     to the named seat on this box by writing ONE file into that seat's broker inbox directory in the exact form the broker
     itself writes a message file (read `org/mcp/server.py` `send_message` for the directory layout, a lane's inbox being
     `org/mcp/inbox/<base>/~<lane>/`, and for the file's header fields), with `From:` the sending serial and box, the subject,
     and a body that is only the path of the cross-box file and its body file. This is a tool writing a file for a seat on its
     own box, NOT a manager sending a message, so the Tier-2 bar is not in play: say so in the tool's header, and prove the
     watcher picks the file up by checking the file lands where `org/mcp/inbox-watch.sh` reads (read that script for the path
     and name pattern it expects; do not start it).
   - `ack --id <id> --by <serial>` on the receiving box sets state ACKED with the time and prints the ONE reply line for the bus,
     `CROSSBOX-ACK <id> READ by <serial> at <UTC>`; `acked --id <id> --line <reply line> --bus-message-id <id>` on the sending
     box records it. SENT IS NOT READ: `status --id <id>` on the sending box reads `SENT, NOT ACKED` until the reply line is
     recorded, and says how long ago it was sent.
   - `close --id <id> --side <from|to> --by <serial>` records that side's close; the state becomes CLOSED-BOTH only when both
     sides are recorded; `status` prints `HALF-CLOSED (<side> only)` otherwise. A call is settled only at CLOSED-BOTH (cell
     CT-s-5's `open-calls.py close` reads this).
   - `list [--open]` prints every cross-box file in this tree with its state and age.
   - `--selftest`: the whole exchange between two temporary "boxes" (two scratch directories standing for two checkouts, the
     bus replaced by handing the printed line across in the test): open, sent, receive (the inbox file lands), ack, acked,
     close one side (reads HALF-CLOSED, and a stand-in for the open-calls close is refused), close the other (CLOSED-BOTH);
     an uncommitted body refused; a line for a file not yet in the tree reads PULL-FIRST; a tampered line (the id altered)
     refused. LAST line `CROSSBOX-SELFTEST cases=<k>/<n> ok=<True|False>`.
2. `.claude/skills/agentbus/SKILL.md` gains a short section "A cross-box call or order": the six commands in order, who runs
   each (the CTO or the issuing seat opens; each box's manager puts the printed line on the bus and hands an arriving line to
   `receive`; the named seat acks; each side closes), and the sentence that the manager carries the line and never the
   substance. (Another cell edits the same skill file's device wording: keep your change to ONE new section at the end so the
   two merge cleanly, and say so in your report.)
3. `.tools/tests/test_crossbox_call.py`: the selftest's cases as separate assertions plus: the inbox file's name and header
   match what the broker writes for an ordinary message (compare field names with a real message file's header from
   `org/mcp/inbox/` if one is readable in your worktree, else with the writer's code); an order for a serial with no inbox
   directory on this box is refused with the reason "no such seat on this box"; an unknown key in a cross-box file is refused.
   LAST line `CROSSBOX-TEST cases=<k>/<n> ok=<True|False>`.

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
<criterion id="CTs6-AC1" cell_refs="CT-s-6"><invocation>python .tools/tests/test_crossbox_call.py</invocation><expect>CROSSBOX-TEST cases=</expect></criterion>
`CTs6-AC1` -- every case passing: the line must read `ok=True`.

<criterion id="CTs6-AC2" cell_refs="CT-s-6"><invocation>python .tools/crossbox-call.py --selftest</invocation><expect>CROSSBOX-SELFTEST cases=</expect></criterion>
`CTs6-AC2` -- the exchange between two stand-in boxes, including half-closed and sent-not-acked: the line must read `ok=True`.
</proof_of_spec>

<expected_criteria>CTs6-AC1,CTs6-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~16/NFRA_CTLPLN.TO-CT-s-6.crossbox-route.proof_of_spec.json`, validate it
with `python .tools/proof-of-spec-check.py <instance> CTs6-AC1,CTs6-AC2`, and flip `<status>` to `complete` only when every criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.seats1.md</decomp_doc>
<owned_cells>CT-s-6</owned_cells>
</decomp_ref>

<paths>
.tools/crossbox-call.py
.tools/tests/test_crossbox_call.py
.claude/skills/agentbus/SKILL.md
org/devices/crossbox/
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- the one cross-device channel broken (no change to the bus script, the consumer, the broker or the hook: the tool prints a line and reads a line); sent read as read (a state for sent-not-acked with its age; the ack is the other side's own act); a call closed on one box and left open on the other (closed only when both sides record it; half-closed is a printed state and blocks the open-call close); an order delivered to a seat that is not on this box, or a forged line (refused; the file must exist at the named commit); a manager carrying substance (the line carries an id and a path); BLIND: a real exchange between two machines -- that is each box's to run and read back, and this seat cannot reach into a Dell.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: Andrew-direct 2026-10-07 ~16:3xZ (record above), ~18:3xZ item 7, ~18:5xZ, ~19:0xZ, and ~21:1xZ at this seat's terminal
(`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261007_211xZ_COO_C_MAKE_SURE_GITOPS_AWSOPS_AGENT_WORKFLOW_DEMANDS_ARE_MET_AND_SAY_LINE_FOR_LINE.md`);
PRD `prd/NFRA_CTLPLN_PRD.md` v0.19 @b44686cebc (ADMITTED), FWD-21 to FWD-25, contract C-SEATS clauses 1 to 7; CTO msg 106584 (the split).
