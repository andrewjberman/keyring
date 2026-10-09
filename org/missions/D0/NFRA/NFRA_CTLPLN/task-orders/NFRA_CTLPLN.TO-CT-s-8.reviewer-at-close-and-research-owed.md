# TO NFRA_CTLPLN.TO-CT-s-8 -- workstream SEATS round 1 CT-s-8: a round does not close without a reviewer on the box, and whether research is owed is read from the class

<to_id>NFRA_CTLPLN.TO-CT-s-8</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~18</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>SEATS</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-s-8` (`decompositions/NFRA_CTLPLN_DECOMP.seats1.md`) | **outcome_ref:** FWD-23, FWD-24 |
**Andrew's lines served (the delivery list):** 13, 14, 16 | **depends_on:** none (the shared files below are the seam)

---

## WORKER FACE

### THE CELL

`CT-s-8`, two small gates. (A) C-SEATS clause 7: "A reviewer per box exists before any drive on that box is counted finished";
FWD-23: "a piece of work is not counted finished until a seat that did none of it has graded it, on the box where it was done."
His words: "CVO is dedicated reviewer in those drive processes so mandatory spawn on any fabric. If there are multiple projects
attached to one macro on a fabric, it is best practice to spawn a CVO specific to that macro, e.g. CVO~NFRA." (B) The CTO's
ruling of call A from his word: "Research is owed for an operation of stakes class S3 or above (`org/tier0/STAKES_MATRIX.md`)
or a task order classed WORLD. Below that, none." MEASURED TODAY: no tool refuses a round or drive as finished for lack of a
grade; the drive skills say it in text; `.tools/proof-of-spec-check.py` stops a worker self-grading a judgment criterion;
`.tools/prd-stamp.py` refuses a non-reviewer signer of the L8 and L9 stamps but says "the stamp is a signal, not a gate";
`.tools/to-pipeline-gate.py` carries the stage enum (`ROUND_CLOSE`, `CLOSED`) and no limb at the close; nothing checks that a
reviewer is on the SAME box; no tool takes an order or an operation and says whether research is owed, and nothing maps the
stakes classes to the order classes.

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

1. `.tools/round-close-check.py --project <CODE> [--round <n>] [--device <d>]`: answers "may this round be counted finished on this
   box", printing each limb with its evidence:
   - REVIEWER-ON-BOX: a CVO-kind seat (through `lib/seat_roles.py kind_of`; minimal local fallback reading
     `org/ref/SEAT_ROLES.json` if the module is not in your worktree) is live on the box where the work was done: read this box's
     `org/mcp/liveness.json` when the box is this one, else that box's `org/devices/state/<device>/seats.json` (THE SEAM) with
     its age; an absent or stale file reads `UNREAD`, never present. A MACRO reviewer lane (a CVO serial whose lane names the
     project's four-letter macro, for example `3.0.0_SA_CVO~NFRA`) satisfies it and is printed as such.
   - GRADED: every task order of the round that is `complete` has a VALID proof instance, and every criterion flagged
     `judgment="true"` in those orders has a row in the project's adjudication file
     (`surprise-channel/adjudications/ADJUDICATION_v*.md`) or, where the project keeps the reviewer's rows in the investigation
     file, a row there authored by a CVO-kind serial that names the criterion id; list each judgment criterion with the row
     that grades it or `UNGRADED`.
   - NOT-BY-A-DOER: the grading rows' author is not the issuer or assignee of the order graded.
   LAST line `ROUND-CLOSE project=<CODE> device=<d> reviewer=<present|ABSENT|UNREAD> orders=<n> judgment=<j> graded=<g> ungraded=<u> self_graded=<s> verdict=<MAY-CLOSE|REFUSED>`.
   It READS; it flips nothing. `--selftest` on fixtures: no reviewer on the box REFUSED; an ungraded judgment criterion
   REFUSED; a grade by the order's own issuer REFUSED; a macro reviewer satisfies; all present MAY-CLOSE. LAST line
   `ROUND-CLOSE-SELFTEST cases=<k>/<n> ok=<True|False>`.
2. Make it bind where a round is closed: `.tools/git-hooks/missions-tree-check.sh` already runs, fail-closed, on any staged
   project row; when a staged `project.json` changes `dep_stage` TO `ROUND_CLOSE` or `CLOSED`, it calls
   `round-close-check.py` for that project and REFUSES the commit on `verdict=REFUSED`, printing the line. ROLLOUT as the other
   new gates of this workstream: WARN (print, do not refuse) unless the file `org/mcp/seat-gates.enforce` exists; you do NOT
   create that file. An audited override as that hook's other limbs have (read the hook for its form). Change nothing else in
   the hook, and run its own self-test (`python .tools/missions-tree-index.py --self-test` and any test the hook names)
   before and after.
3. `.claude/skills/canonical-drive/SKILL.md`, `.claude/skills/closer-drive/SKILL.md` and `.claude/skills/remote-drive/SKILL.md`: one
   added line each at the step where a round or job is counted finished: run `round-close-check.py`; REFUSED means it is not
   finished. `.claude/skills/remote-drive/SKILL.md` has NO reviewer step today: add it as that one line and nothing more (the
   inbound workstream owns the rest of that skill: keep your change to ONE line so the two merge cleanly, and say so).
   `.claude/skills/mstr-spawn/SKILL.md` already accepts any serial with a lane: add one sentence under its serial grammar that a
   reviewer lane named for a macro (`3.0.0_SA_CVO~<MACRO>`) is spawned where several projects of one macro share a box and the
   box's CTO asks for it. (Another cell adds one sentence to the same skill: keep yours to one sentence in that place.)
4. `.tools/research-owed.py --order <task order file>` or `--stakes <S0|S1|S2|S3|S4>`: prints
   `RESEARCH-OWED subject=<order id or class> risk=<LOCAL|SERVED|WORLD|-> stakes=<S0..S4|-> verdict=<OWED|NOT-OWED> rule=<...>`:
   OWED when the order's `<risk>` is WORLD or the stakes class is S3 or S4; NOT-OWED otherwise; an order with no `<risk>`
   element, or a class outside the enum, is `UNCLASSED` and exits non-zero (never guessed). The stakes class of an operation is
   GIVEN to the tool (by the flag or by a `<stakes>` element in the order if one is present); the tool does not classify an
   operation itself, because the matrix is Andrew's and its rules are judgment. It reads the class names from
   `org/tier0/STAKES_MATRIX.md`'s class table so a renamed class is caught (READ ONLY). It is deterministic: the same input gives
   the same answer on any box. `--selftest`: each of the eight inputs and the two unclassed forms. LAST line
   `RESEARCH-OWED-SELFTEST cases=<k>/<n> ok=<True|False>`.
5. `.tools/tests/test_round_close_and_research.py`: both selftests; the hook in WARN mode prints and admits a close with no
   reviewer, and with the enforce file present (in a scratch copy of the files the hook reads, never the real tree) refuses
   it; a `dep_stage` change that is not a close is untouched. LAST line `CLOSE-GATES-TEST cases=<k>/<n> ok=<True|False>`.

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
<criterion id="CTs8-AC1" cell_refs="CT-s-8"><invocation>python .tools/tests/test_round_close_and_research.py</invocation><expect>CLOSE-GATES-TEST cases=</expect></criterion>
`CTs8-AC1` -- every case passing: the line must read `ok=True`.

<criterion id="CTs8-AC2" cell_refs="CT-s-8"><invocation>python .tools/round-close-check.py --project NFRA_CTLPLN</invocation><expect>ROUND-CLOSE project=NFRA_CTLPLN</expect></criterion>
`CTs8-AC2` -- the check runs on this project on this box as it really stands (read only); the issuer reads its verdict and its list of ungraded judgment criteria at the drain.

<criterion id="CTs8-AC3" cell_refs="CT-s-8"><invocation>python .tools/research-owed.py --selftest</invocation><expect>RESEARCH-OWED-SELFTEST cases=</expect></criterion>
`CTs8-AC3` -- the line the CTO ruled, both ways and both unclassed forms: the line must read `ok=True`.
</proof_of_spec>

<expected_criteria>CTs8-AC1,CTs8-AC2,CTs8-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~18/NFRA_CTLPLN.TO-CT-s-8.reviewer-at-close-and-research-owed.proof_of_spec.json`, validate it
with `python .tools/proof-of-spec-check.py <instance> CTs8-AC1,CTs8-AC2,CTs8-AC3`, and flip `<status>` to `complete` only when every criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.seats1.md</decomp_doc>
<owned_cells>CT-s-8</owned_cells>
</decomp_ref>

<paths>
.tools/round-close-check.py
.tools/research-owed.py
.tools/tests/test_round_close_and_research.py
.tools/git-hooks/missions-tree-check.sh
.claude/skills/canonical-drive/SKILL.md
.claude/skills/closer-drive/SKILL.md
.claude/skills/remote-drive/SKILL.md
.claude/skills/mstr-spawn/SKILL.md
org/tier0/STAKES_MATRIX.md
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a new refusal that blocks every project's close the moment it lands (WARN mode until an enforce file a person creates; an audited override); a fail-closed hook broken for every commit by the edit (one added call; its self-test before and after; a scratch copy for the enforce test); a grade by the seat that did the work counted as a grade (authors compared with issuer and assignee); another box's reviewer assumed from an absent file (unread is never present); the tool classifying an operation itself (the class is given; unclassed is an error, never a guess); BLIND: whether a grade is a good grade.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: Andrew-direct 2026-10-07 ~16:3xZ (record above), ~18:3xZ item 7, ~18:5xZ, ~19:0xZ, and ~21:1xZ at this seat's terminal
(`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261007_211xZ_COO_C_MAKE_SURE_GITOPS_AWSOPS_AGENT_WORKFLOW_DEMANDS_ARE_MET_AND_SAY_LINE_FOR_LINE.md`);
PRD `prd/NFRA_CTLPLN_PRD.md` v0.19 @b44686cebc (ADMITTED), FWD-21 to FWD-25, contract C-SEATS clauses 1 to 7; CTO msg 106584 (the split).

## AMENDMENT 1 (2.0.0_SA_COO~C, 2026-10-08 ~09:4xZ) -- REOPENED, SHORT: the close gate reads its own switch file, not the retired single name

The cell is merged. Since then the single switch file `org/mcp/seat-gates.enforce` was RETIRED: each check now has its own
switch (cell CT-s-3 AMENDMENT 1, merged @5302e26583; in the two wrappers the old file turns on nothing). Your hook's close gate
in `.tools/git-hooks/missions-tree-check.sh` still reads the old name (and `OPAL_SEAT_GATES_ENFORCE_FILE`), so the old file
would silently turn on the close gate alone (row NFRA_CTLPLN-W13-S28). Ruling: `1.0.0_SA_CTO` msg 106858: "1. Who apply-who grades: the seat whose session runs the tool, read from the running session's serial, never a commit's author. A drained commit is pushed by a fabric manager and applied by a deploy seat; neither is its author. 2. Where: in safe-apply only ... In safe-deploy and on a push it stays WARN until it reads the session, and it never refuses a push that deploys nothing. ... 4. Row S28, the tree hook reading the old switch name: a cell, before any switch exists. 5. No switch file today. After 1, 2 and 4, a dry pass over real pushes from all four boxes; I name the first switch from that."
Gate limb: none graded this modification. NO SWITCH FILE IS CREATED BY YOU.

1. The close gate's switch becomes `org/mcp/seat-gates.round-close.missions-tree-check.enforce` (the form
   `seat-gates.<check>.<tool>.enforce`). The old file `org/mcp/seat-gates.enforce`, if present, turns on NOTHING in the hook and
   prints one WARN line saying it is retired and naming the new file. The test-only override becomes a DIRECTORY variable,
   `OPAL_SEAT_GATES_ENFORCE_DIR` (the same variable the wrappers now read: read `.tools/safe-apply.sh`'s block for how it is
   used and match it); `OPAL_SEAT_GATES_ENFORCE_FILE` is no longer read.
2. If `.tools/round-close-check.py` or `.tools/research-owed.py` themselves name the old file anywhere, change them the same
   way; say whether they did.
3. `.tools/tests/test_round_close_and_research.py`: the cases that wrote the old file write the new one; add a case that the
   old file alone leaves the gate in WARN and prints the retired line. The generator's own self-test reads the same before
   and after.
4. Search the repository for any OTHER code reader of `seat-gates.enforce` or `OPAL_SEAT_GATES_ENFORCE_FILE` (code, not
   documents) and list each with file and line; do not edit files outside your `<paths>`.

**ACCEPTANCE.** The three ids, expectations unchanged. Rewrite the proof instance, validate, flip to `complete`.

## AMENDMENT 2 (2.0.0_SA_COO~C, 2026-10-09 ~04:4xZ) -- REOPENED, SHORT: an order without a to_id tag matches its proof by file stem; status is the LAST tag

From the field, relayed by 0.0.0_AB_MSTR msg 107718. dell2 1.0.0_SA_CTO~DELL2 (row IRPT_YCDGEN D2-S17) wrote, verbatim: "line 134 sets
id = tag(text, 'to_id') or '', so a tree order without <to_id> fails every proof match at :165 -- 19 of 19 for IRPT_YCDGEN round 6.
Fix: tag(text, 'to_id') or os.path.basename(path)[:-3], since proof instances carry the stem." The same reader also takes the FIRST
status tag. `1.0.0_SA_CTO` msg 107528, the gate owner's ruling, says: "an order's status is its LAST [status] tag". Gate limb: none
graded this modification.

1. In `.tools/round-close-check.py` `read_orders()`, an order's id is its `to_id` tag, or else its file stem. Check how the proof
   matcher (about line 165) compares ids, and make an order matched by stem pass where its proof instance names the stem.
2. An order's status is the LAST status tag whose word is a status word. Reuse `.tools/seat-list.py`'s `STATUS_WORDS` if it can be
   imported cleanly; otherwise use a local copy with a comment naming the source. `.tools/research-owed.py` gets the same rule if
   it reads status.
3. Tests in `.tools/tests/test_round_close_and_research.py`:
   - an order with no to_id whose proof instance carries the stem matches;
   - one with a to_id still matches by to_id;
   - pending then complete reads complete;
   - complete then pending reads pending.

**ACCEPTANCE.** The three ids, with expectations unchanged. Rewrite the proof instance, validate it, and flip to `complete`.
