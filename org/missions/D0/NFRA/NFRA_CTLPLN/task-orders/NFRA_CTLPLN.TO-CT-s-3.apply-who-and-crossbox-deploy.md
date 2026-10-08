# TO NFRA_CTLPLN.TO-CT-s-3 -- workstream SEATS round 1 CT-s-3: how cloud changes are made: who may apply, and the three measurements a box runs before a deploy of its own work

<to_id>NFRA_CTLPLN.TO-CT-s-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~13</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>SEATS</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-s-3` (`decompositions/NFRA_CTLPLN_DECOMP.seats1.md`) | **outcome_ref:** FWD-25, FWD-22 |
**Andrew's lines served (the delivery list):** 19, 24 | **depends_on:** none (the shared files below are the seam)

---

## WORKER FACE

### THE CELL

`CT-s-3`, the AWS DevOps part of FWD-25 and Andrew's word of ~19:0xZ: "the laptop needs to know at all times what is going on
across the various devices, but that doesnt mean that every single commit/deploy/decision needs to come from the laptop, that
is just when there is actually an open-call / potential project overlap or a deploy that could upset another device's work."
MEASURED TODAY: `.tools/safe-apply.sh` and `.tools/safe-deploy.sh` check the halt gate, an opt-in named-commit check
(`.tools/named_commit_check.py`, the one device-aware check), naming limbs and a tag gate; NEITHER checks which seat is
applying, and nothing asks whether a root belongs to another box's open work. `.tools/placement-check.py` computes cross-box
write-set overlap as a VIEWER that never changes an exit code. Today a cross-box deploy hazard was announced as free text in
a broadcast (an untargeted apply of one root would have silently reverted a deliberately altered input another box was
testing). This cell builds two checks and calls them from the two wrappers. It builds NO alert and NO monitor: each is a read
made at the moment of an apply.

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

1. `.tools/apply-who-check.py --serial <serial> --root <terraform root dir> [--target <address> ...]`: resolves the serial's kind
   through `lib/seat_roles.py kind_of` (if that module is not in your worktree another cell is writing it: write a minimal
   local fallback that reads `org/ref/SEAT_ROLES.json` in THE SEAM's shape, and use the module when present) and prints
   `APPLY-WHO serial=<s> kind=<k> root=<name> verdict=<ADMITTED|REFUSED> reason=<...>`. The rule, as data in the script's head and
   cited from `org/ref/SEAT_RULES.json` when present: an apply is made by a CLOUDOPS seat or a TIER2 seat under a task order;
   MSTR, CTO, COO, CVO, CRO and WORKER are REFUSED (a COO spawns the worker and cuts the order, it does not apply; CLAUDE.md
   rule 13 and `/cloud-ops` are the text behind this: read both and report any conflict you find rather than resolving it).
   UNKNOWN is REFUSED. It reads; it changes nothing.
2. `.tools/crossbox-deploy-check.py --root <terraform root dir> [--target <address> ...] [--notices <dir>]`: the three measurements
   of his word, each printed with its evidence, for the box it runs on (device from `AGENTBUS_DEVICE` through `lib/devices.py`):
   - OPEN-CALL: does an OPEN cross-box call name this root or project? Reads `org/devices/crossbox/*.json` (THE SEAM) and
     `org/devices/state/*/open_calls.json` where present; absent files are "none recorded", said so.
   - OVERLAP: does another box's placed project name the same root or the same resource? Uses `.tools/placement-check.py`'s
     own functions (import it; do not copy it) for the write-set overlap, and each project row's `placement`.
   - UPSET: is there a standing deploy NOTICE that names this root (and, when the notice names resources, whether the apply is
     untargeted or one of its targets is named)? A notice is a FILE `org/devices/deploy_notices/<id>.json`: `id`, `root`,
     `resources` (list, may be empty meaning the whole root), `rule` ("targeted-only-excluding" or "no-apply"), `until` (UTC),
     `by`, `reason`, `record` (a path). An expired notice is ignored and listed as expired.
   Also reads `org/critical_paths/.open_deploys/` in EVERY live worktree (`git worktree list --porcelain`, then `ls-tree` on each
   HEAD, as CLAUDE.md's NEVER-2 clause says) for another seat's open deploy on the same root.
   LAST line `CROSSBOX-DEPLOY device=<d> root=<name> open_call=<clear|hit> overlap=<clear|hit> upset=<clear|hit> open_deploy=<clear|hit> verdict=<CLEAR|STOP>`.
   `STOP` names what it hit and says the route: a cross-box call (cell CT-s-6's tool). `CLEAR` means the box acts and tells the
   laptop.
3. Write today's real notice as the first file: `org/devices/deploy_notices/opal-assets-cot-rebalancer-until-20261008T0620Z.json`
   from `1.0.0_SA_CTO`'s broadcast (msg 106555: until 06:20Z on 2026-10-08 an apply of `infra/aws/terraform/opal-assets` is
   targeted and does not name `aws_cloudwatch_event_target.cot_rebalancer_runner_daily`; an untargeted one waits). Read the
   message file under `org/mcp/inbox/2.0.0_SA_COO/~C/read/` whose name contains `CROSS-BOX_DEPLOY_NOTICE` for the exact words,
   and cite it in `record`. If that file is not in your worktree (inboxes are not tracked), write the notice from this
   paragraph and say so.
4. Call both from the wrappers, as ONE added block each in `.tools/safe-apply.sh` and `.tools/safe-deploy.sh`, placed after the
   halt gate and before the apply: resolve the serial as the halt gate already does; run `apply-who-check.py` (REFUSED stops
   the apply with its line) and `crossbox-deploy-check.py` (STOP stops the apply with its line). ROLLOUT, so no seat is
   stranded mid-work by a new refusal: both blocks run in WARN mode (print the line, do not stop) unless the file
   `org/mcp/seat-gates.enforce` exists; you do NOT create that file. An audited override, as the other limbs have: an
   environment variable whose value is the reason, written to the wrapper's existing audit log. Change nothing else in either
   wrapper, and prove it: every existing self-test or test of the two wrappers still passes (find and run them).
5. `.tools/tests/test_apply_who_and_crossbox.py`: one serial of each of the eight kinds against the rule; a notice that names
   the root stops an untargeted apply and a targeted apply naming the resource, and clears a targeted apply that does not; an
   expired notice is ignored; an OPEN cross-box call fixture hits; another box's placed project naming the root hits; the
   wrappers in WARN mode print and proceed, and with the enforce file present (in a scratch copy of the repository files the
   wrapper reads, never the real tree) they stop: test the block's logic through a `--dry-seat-gates` path that runs the two
   checks and exits without running Terraform. LAST line `APPLY-GATES-TEST cases=<k>/<n> ok=<True|False>`.

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
<criterion id="CTs3-AC1" cell_refs="CT-s-3"><invocation>python .tools/tests/test_apply_who_and_crossbox.py</invocation><expect>APPLY-GATES-TEST cases=</expect></criterion>
`CTs3-AC1` -- every case passing: the line must read `ok=True`.

<criterion id="CTs3-AC2" cell_refs="CT-s-3"><invocation>python .tools/crossbox-deploy-check.py --root infra/aws/terraform/opal-assets</invocation><expect>upset=hit</expect></criterion>
`CTs3-AC2` -- the difference control on today's real case: an untargeted apply of that root is stopped by the notice file (until it expires; the issuer re-runs it before 06:20Z). The same line must read `verdict=STOP`.

<criterion id="CTs3-AC3" cell_refs="CT-s-3"><invocation>python .tools/apply-who-check.py --serial 2.0.0_SA_COO~C --root infra/aws/terraform/opal-assets</invocation><expect>verdict=REFUSED</expect></criterion>
`CTs3-AC3` -- a seat kind that does not apply is refused by a tool, not by another seat noticing.
</proof_of_spec>

<expected_criteria>CTs3-AC1,CTs3-AC2,CTs3-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~13/NFRA_CTLPLN.TO-CT-s-3.apply-who-and-crossbox-deploy.proof_of_spec.json`, validate it
with `python .tools/proof-of-spec-check.py <instance> CTs3-AC1,CTs3-AC2,CTs3-AC3`, and flip `<status>` to `complete` only when every criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.seats1.md</decomp_doc>
<owned_cells>CT-s-3</owned_cells>
</decomp_ref>

<paths>
.tools/apply-who-check.py
.tools/crossbox-deploy-check.py
.tools/safe-apply.sh
.tools/safe-deploy.sh
.tools/tests/test_apply_who_and_crossbox.py
org/devices/deploy_notices/
.tools/placement-check.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a new refusal that strands a cloud-operations seat mid-apply the moment it lands (WARN mode until an enforce file a person creates; an audited override); a wrapper broken for every seat by the edit (one added block each; every existing wrapper test re-run; a dry path that never runs Terraform); the check that proves itself with its own fixture only (criterion 2 runs on today's real notice and root); a notice that never expires (an until time; expired notices listed); device named by a path (resolved from the environment and the register); BLIND: a hazard nobody wrote a notice for, and resources reached outside Terraform.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: Andrew-direct 2026-10-07 ~16:3xZ (record above), ~18:3xZ item 7, ~18:5xZ, ~19:0xZ, and ~21:1xZ at this seat's terminal
(`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261007_211xZ_COO_C_MAKE_SURE_GITOPS_AWSOPS_AGENT_WORKFLOW_DEMANDS_ARE_MET_AND_SAY_LINE_FOR_LINE.md`);
PRD `prd/NFRA_CTLPLN_PRD.md` v0.19 @b44686cebc (ADMITTED), FWD-21 to FWD-25, contract C-SEATS clauses 1 to 7; CTO msg 106584 (the split).
