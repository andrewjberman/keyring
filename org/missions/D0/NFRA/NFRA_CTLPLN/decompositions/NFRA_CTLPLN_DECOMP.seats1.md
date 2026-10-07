# NFRA_CTLPLN decomposition -- WORKSTREAM SEATS, round 1: how each seat operates, locked into launchers, skills and gates (issuer 2.0.0_SA_COO~C; cut 2026-10-07 ~23:3xZ)

**Status: ISSUED in one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Why this seat, and why a workstream.** Andrew-direct ~21:1xZ at this seat's terminal: "Make sure all my demands about the
GitOps/AWS Ops/Agent Worfklow Ops (including the launchers/skills/etc), are met after this round."
(`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261007_211xZ_COO_C_MAKE_SURE_GITOPS_AWSOPS_AGENT_WORKFLOW_DEMANDS_ARE_MET_AND_SAY_LINE_FOR_LINE.md`).
`1.0.0_SA_CTO` ruled the split (msg 106584): this seat issues workstream SEATS (C-SEATS clauses 1 to 7, FWD-21 to FWD-25);
`2.0.0_SA_COO~R` issues workstream INBOUND (FWD-20 and clause 8, then mail under clause 9), and answered yes. The scope here
is its own, and its write surface is disjoint from round 5's (`org/devices/intake/**`, `org/devices/kit_*`) and from INBOUND's.

**PATHS THAT ARE WHOSE, said at the cut as the CTO asked.** SEATS writes: `org/ref/SEAT_ROLES.json`, `org/ref/SEAT_RULES.json`,
`lib/seat_roles.py`, `.tools/ajb.ps1`, the eight new tools named below under `.tools/`, the two apply wrappers (one block
each), `.tools/git-hooks/missions-tree-check.sh` (one call), `org/devices/state/`, `org/devices/crossbox/`,
`org/devices/deploy_notices/`, and the skills `govern`, `mstr-review`, `mstr-spawn`, `mstr-kill`, `unstick`, `agentbus`,
`open-calls`, `fabric-check`, `sequence`, `canonical-drive`, `closer-drive`. In `.claude/skills/remote-drive/SKILL.md` SEATS adds
ONE line (the reviewer at close) and INBOUND owns the rest of that file. SEATS does NOT touch: `.tools/remote-job.py`, the
Teams functions under the transcripts or chat roots, any mail reader, or the text Andrew is sent.

**Cut on:** PRD v0.19 @b44686cebc, ADMITTED (v0.19 adds FWD-26, the voice file, to workstream INBOUND only; nothing of SEATS moved) (`python .tools/prd-signoff.py status NFRA_CTLPLN` at the cut: ratified-text SIGNED,
current). Carrier: ADDENDUM v0.17 and v0.18; his records of ~16:3xZ, ~18:3xZ, ~18:5xZ and ~19:0xZ; the 24-line delivery list
(`org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_CTLPLN_SEAT_ROLES_LINE_FOR_LINE_DELIVERY_COO_C_20261007.md` @0faf18f318).

## Measured at the base (a read-only map made for this cut, ~22:2xZ, each claim with file and line in the issuer's session)

1. The launcher states each seat INLINE in `.tools/ajb.ps1` and reads no file; the text differs by seat kind and not by device;
   one script serves all four boxes; a worker serial matches no arm.
2. The manager skills and their engines are local to the box they run on and name no device; none reads the device register.
   The manager's loop has no step that measures a hung or dead seat, admits only the bare manager serial, and one step
   hardcodes two boxes.
3. By seat, tools refuse today: a shared-branch push by anyone but a manager serial; rebase, stash, clean and a bare
   Terraform apply for all; a manager on a project's specification, decomposition, adjudication and remediation files; a
   manager's message to a Tier-2 seat; a new task order committed by anyone but a COO or issued to a Tier-0 or Tier-1 seat; a
   reviewer's send to Tier-2; a worker grading its own judgment criterion; a non-reviewer signing the L8 and L9 stamps.
4. For how cloud changes are made NOTHING is seat-specific: the apply and deploy wrappers check no serial, and nothing asks
   whether a root belongs to another box's open work (a viewer computes the overlap and changes no exit code).
5. Open calls are swept from one seat's vantage and printed in chat; nothing holds one list per box.
6. The bus addresses boxes with free text and no kind; an acknowledgement is a convention with no stored record; no typed
   message carries a cross-box call.
7. No tool refuses a close for lack of a grade or of a reviewer on the box; no tool says whether research is owed.
8. Every seat list is one box's.
9. Project rows carry `placement` (DELL1 4, DELL2 9, LAPTOP 14, SITEZ 11, unset 6 of 44, issuer's read ~22:1xZ).

## Rule 24

Domain: the 24 lines of the delivery list. Subtraction, line by line: lines 4, 5, 6, 7 and 12 are INBOUND's (not here); line 17
is done in the specification; line 20 is done (CLAUDE.md rule 32) and held by `CT-s-2`'s table staying the only statement;
line 21 (the routing count re-taken) and line 22 (the mandate to each box's manager) are issuer acts after the drain; the
remaining 15 lines are served by the eight cells below, each line named on its order. No line is unowned. Same grain: each
cell is one holder change with its tool and test. One intent each (`CT-s-8` holds two small gates of one intent: what must be
true before work is counted finished or begun). State coherence: this round changes no live seat, pushes nothing, applies
nothing and sends nothing on the bus; every new refusal lands in WARN mode behind one enforce file a person creates.

## Cells

| cell | what | his lines | serves | risk | slot |
|---|---|---|---|---|---|
| `CT-s-1` | the ONE roles file in his terms, a resolver, and the launcher handing each seat its statement at start (a missing file never stops a launch) | 1, 11, 15, 18 | FWD-25; C-SEATS 1 | SERVED | ~6 |
| `CT-s-2` | the table of every rule with its one holder in three parts (how code moves, how cloud changes are made, how seats work), and a checker that tries one forbidden act per gate rule; three rules entered as needing his word | 18, 19, 20 | FWD-25; C-SEATS 2 | LOCAL | ~8 |
| `CT-s-3` | who may apply (a check by seat kind) and the three measurements before a box deploys its own work (open call, overlap, could upset another box), called from the two apply wrappers; deploy notices as files, today's real one first | 19, 24 | FWD-25, FWD-22 | SERVED | ~13 |
| `CT-s-4` | the manager on every box: a seat-liveness measurement, the loop step that unsticks or respawns, register-driven skills, and a read of a manager's day for project rulings | 1, 3 | FWD-21; C-SEATS 3 | LOCAL | ~14 |
| `CT-s-5` | one open-call list per box and the measurement of whether a call touches only that box (paths, placement, resources, a shared set) | 8, 9, 24 | FWD-22; C-SEATS 4 | LOCAL | ~15 |
| `CT-s-6` | the cross-box route: a call or an order as a file, an acknowledgement from the other side, closed on both boxes or neither; a Dell's order reaches a laptop seat with no person relaying | 10 | FWD-22; C-SEATS 5, 6 | SERVED | ~16 |
| `CT-s-7` | each box's seat list (every COO's project, drive, open orders; one doing nothing shown) and the laptop's view of every box with each report's age | 11, 23 | FWD-23 | LOCAL | ~17 |
| `CT-s-8` | a round is not closed without a reviewer on the box and a grade by a seat that did none of the work (called where a project row is closed); and whether research is owed, read from the class | 13, 14, 16 | FWD-23, FWD-24; C-SEATS 7 | SERVED | ~18 |

## Edges and fan-out

The cells exchange FILES whose shapes are fixed in the seam below and repeated verbatim on each order: the roles file, the
rules table, the per-box state files, the cross-box file. Where a cell reads a file another cell writes (the roles file),
it carries a minimal local fallback and uses the shared module when present, so no cell waits on another's code; where the
rules table names a gate another cell builds, its probe is counted PENDING until that gate exists and the issuer's drain run
must read zero pending. No build dependency: eight chains of one. `fanout: 8 of 8 chains, cap 8`.

Three skill files are touched by two cells each, each change confined to ONE added sentence or section in a named place so the
merges are clean: `agentbus` (`CT-s-4` device wording; `CT-s-6` one new section at the end), `mstr-spawn` (`CT-s-4` one
sentence; `CT-s-8` one sentence), and `remote-drive` (`CT-s-8` one line; the rest is INBOUND's). The issuer reads all three
after the drain.

## The seam (verbatim on every order)

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

## The issuer's acts after the drain

1. The repo-wide hygiene once; `python .tools/seat-rules-check.py exercise` on the merged trunk must read `probes_pending=0
   probes_fail=0 pairs_covered=24/24`: that run IS FWD-25's "one forbidden act per kind tried and stopped or flagged by a tool".
2. One seat of each kind started with `-PrintPrompt` and its statement read; then, on Andrew's or the CTO's next real spawn of
   each kind, the seat asked what it is and is not (FWD-25's exercise: a real start, not a print).
3. The MANDATE (line 22): one file per box's manager written from the roles file and the rules table, relayed by the cross-box
   route, acknowledged by each manager by message id.
4. The routing count re-taken (line 21) against `CONTROL_PLANE_ROUTING_COUNT_AND_WHAT_COULD_LEAVE_THE_LAPTOP_20261007.md`, kind
   by kind, with the CTO.
5. The enforce file: every new refusal of this round lands in WARN mode. Creating `org/mcp/seat-gates.enforce` turns them on
   for every seat on every box at once; that is a decision this seat puts to the CTO with the WARN lines observed, not one it
   takes. CLAUDE.md: "NEVER implement an approval gate on any work unless Andrew explicitly asks"; his word of ~16:3xZ asks
   for gates by name, and the rollout is staged so that word is honoured without stranding a seat mid-work.
6. The three lines that need his word (who pushes the shared branch from a Dell; "laptop should admin"; the routes denied the
   Dells) stay entered in the table as questions and go to him through the CTO's walk-through.
7. On a Dell: each box pulls, runs `seat-list.py write`, `seat-liveness.py`, `round-close-check.py` and the cross-box exchange
   with the laptop, and reads back. Until a box reads back, its lines are BUILT, not EXERCISED.

## Verification diet

Each order carries two or three mechanical criteria: the built behaviour, and a difference control on a REAL case where one
exists (today's deploy notice; this project's fence root reading cross-box; this box's real seat list). Judgment (whether a
seat handed its statement acts on it; whether a manager's record holds an opinion) is the reviewer's at the close.
