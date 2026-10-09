# TO NFRA_CTLPLN.TO-CT-t-2 -- round 6 THREAD CT-t-2: the 4x4 directed matrix of cross-box files across every box branch

<to_id>NFRA_CTLPLN.TO-CT-t-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~52</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-t-2` (`decompositions/NFRA_CTLPLN_DECOMP.thread6.md`) | **outcome_ref:** FWD-3, FWD-22 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3: a seat on any box reaches a seat on any other box through the two boxes' managers, and the read is shown. Its bar is one
message each way between every pair in use: 12 directed pairs for four boxes. FWD-22: cross-box calls are settled on the record.
MEASURED TODAY: `org/devices/crossbox/` on box/laptop holds 10 files (schema `crossbox/1`: `from_device`, `to_device`, `state`,
`sent`, `ack`, `closed`), 1 CLOSED-BOTH with an ack and 9 OPEN with none. Each box writes its own copies on its own branch, so one
branch's folder is not the whole picture.

### BUILD

1. `.tools/crossbox-matrix.py [--fetch] [--since <UTC>]`. Union `org/devices/crossbox/*.json` over `origin/box/*`, `origin/CLOUD`
   and the working tree, read through `git show <ref>:<path>`. The same `id` on several refs is ONE file, and the most advanced
   state wins, in the order OPEN < ACKED < CLOSED-BOTH. Print each file's refs. Boxes come from `lib/devices.py`. For each directed
   pair (from, to) of distinct boxes, print the newest file with its state, whether `ack` is set, `ack.bus_message_id`, and its age.
   A pair with no file reads `NONE`.
   LAST line: `CROSSBOX-MATRIX pairs=<n> with_file=<a> acked=<b> closed_both=<c> none=<d>`.
   `n` is the number of directed pairs, 12 for four boxes, and comes from the register, never typed.
2. `--selftest` on temporary repositories:
   - the same id on two refs counts once, at its most advanced state;
   - a pair with no file reads NONE;
   - a malformed file is listed UNREADABLE and is not counted;
   - a fifth box added to a fixture register makes 20 pairs with no code edit.
   LAST line: `CROSSBOX-MATRIX-SELFTEST cases=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

**Nothing you run changes the live fabric.** You do not start, stop or message any seat. You do not push, merge or rebase. You run
no `terraform` against a backend and no `aws` call. You send nothing on the agent bus. Reads of git refs (`git log`, `git show`,
`git for-each-ref`, including `origin/box/*` and `origin/CLOUD` after one `git fetch`) are allowed. Tests run in temporary
directories or temporary git repositories. The law files `CLAUDE.md` and `org/XXX.md` are LOCKED. `.claude/settings.json` is in
no grant. No non-ASCII in any file you write. Python: standard library only; ruff clean. The device register is read only through
`lib/devices.py`; no tool types a box name, a serial of a particular box, or a path under a user's home.
FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to
`org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W<slot>-S<k>`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTt2-AC1" cell_refs="CT-t-2"><invocation>python .tools/crossbox-matrix.py --selftest</invocation><expect>CROSSBOX-MATRIX-SELFTEST cases=</expect></criterion>
`CTt2-AC1` -- every case passing; the line reads `ok=True`.

<criterion id="CTt2-AC2" cell_refs="CT-t-2"><invocation>python .tools/crossbox-matrix.py --fetch</invocation><expect>CROSSBOX-MATRIX pairs=12 with_file=</expect></criterion>
`CTt2-AC2` -- the live matrix as it stands. The issuer reads `acked` and `none` at the drain; filling the 12 pairs is the issuer's act A4.
</proof_of_spec>

<expected_criteria>CTt2-AC1,CTt2-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~52/NFRA_CTLPLN.TO-CT-t-2.crossbox-matrix.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> CTt2-AC1,CTt2-AC2`, and flip `<status>` to `complete` only when every mechanical criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.thread6.md</decomp_doc>
<owned_cells>CT-t-2</owned_cells>
</decomp_ref>

<paths>
.tools/crossbox-matrix.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- one branch's folder read as the whole picture (union over every box ref, refs printed); a duplicate id double-counted (one per id, most advanced state); the pair count typed (from the register); BLIND: a message carried on the bus with no file.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: L10 round analysis `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.20261009.md` @333d2b37b3 (1.0.0_SA_CTO msg 107787); PRD `prd/NFRA_CTLPLN_PRD.md` v0.22 @333d2b37b3, ratified-text SIGNED (current).
