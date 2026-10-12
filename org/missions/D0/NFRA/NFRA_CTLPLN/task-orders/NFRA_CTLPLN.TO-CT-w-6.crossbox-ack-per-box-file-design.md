# TO NFRA_CTLPLN.TO-CT-w-6 -- round 8 CT-w-6: a DESIGN for the crossbox ack in a per-recipient-box file, so two boxes stop writing one JSON (E8)

<to_id>NFRA_CTLPLN.TO-CT-w-6</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~68</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-w-6` (`decompositions/NFRA_CTLPLN_DECOMP.round8.md`) | **outcome_ref:** FWD-8, FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-8: two boxes never edit one file at once. The measured exception is the crossbox call: the sender writes `org/devices/crossbox/XB-<id>.json`, and the recipient's ack, receive and close edits land in that SAME file, so the integrator resolves a merge conflict. The census `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/E8_BOX_SYNC_CONFLICTS_SINCE_20261009.txt` (read it, including its header) counts 36 conflicted merges of 1,894 and 69 conflicted paths since 2026-10-09, 61 of them `RESOLVED-OTHER`, mostly crossbox files. You write ONE design document for the CTO. You change nothing else.

### WHAT THE DESIGN MUST CONTAIN

File: `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~68/DESIGN_CROSSBOX_ACK_PER_BOX_FILE.md`. Read first: `.tools/crossbox-call.py` (every verb: open, line, status, sent, issue, send-pending, receive, ack, acked, close, withdraw, list, merge), `.tools/crossbox-matrix.py`, the integrator `.tools/box-sync.sh` (lines 48 and 265 read only `refs/remotes/origin/box/*`), `.tools/git-hooks/one-writer-check.py` and the lane `NFRA_CTLPLN_FAST_C` in `.owned-paths.yaml` (which paths a manager may commit), and five real crossbox files under `org/devices/crossbox/` (one OPEN, one ACKED, one CLOSED-BOTH, one withdrawn if any, one from the census's conflicted list). Answer each, with the file and line it rests on:
1. **Who writes which field today**, as a table over the JSON's keys: (field, written by sender or recipient, at which verb, in which commit). Print the denominator (the number of verbs and fields).
2. **The proposed split**: the sender's file keeps what only the sender writes; each recipient box writes its ack, receive and close into `org/devices/crossbox/ack/<box>/XB-<id>.json` (or a better path you justify), so each path has ONE writing box. State the file shapes (keys), and what `status`/`list`/`merge` and `crossbox-matrix.py` read to compute the same states (OPEN, SENT, DELIVERED, ACKED, CLOSED-BOTH) from the two files.
3. **The migration**: how existing single-file calls are read during the change (both shapes), and what happens to a call in flight. No existing file is rewritten.
4. **What must change**, as a list of files and functions (no patch): `crossbox-call.py` verbs, `crossbox-matrix.py`, the lane grant, `box-sync.sh`'s two known conflict classes, the one-writer check.
5. **The test plan**: cases that fail on the old shape and pass on the new, including a two-box simulation (two temporary git repositories, each writing its own side, one merge, zero conflicts) and the matrix computing the same state from both shapes.
6. **What it does NOT fix** (the surprise-channel INVESTIGATION files are append-only shared files and take a different fix, which the census shows is already handled as CHANNEL-UNION): say so with the census counts.
7. **Open questions for the CTO**, at most five, one line each.
LAST line: `DESIGN-CROSSBOX-ACK fields=<n> verbs=<n> files_to_change=<n> questions=<n>`.

### RULES FOR THIS CELL

You write the one document (and the surprise rows the rules allow). You edit no tool, no hook, no `.owned-paths.yaml`, no crossbox file. You run no `crossbox-call.py` verb that writes (`list`, `status`, `--help`, `--selftest` are allowed; `open`, `ack`, `send-pending`, `receive`, `close`, `merge`, `issue`, `withdraw` are NOT). You run no terraform and no aws and send nothing on the agent bus. No non-ASCII. The law files CLAUDE.md and org/XXX.md are LOCKED.
FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W68-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTw6-AC1" cell_refs="CT-w-6"><invocation>grep -c "DESIGN-CROSSBOX-ACK fields=" org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~68/DESIGN_CROSSBOX_ACK_PER_BOX_FILE.md</invocation><expect>1</expect></criterion>
`CTw6-AC1` -- the design exists and ends with its counts line.

<criterion id="CTw6-AC2" cell_refs="CT-w-6" judgment="true"/>
`CTw6-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO: the split leaves every path with one writing box, and the states computed from the two files equal today's.
</proof_of_spec>

<expected_criteria>CTw6-AC1,CTw6-AC2</expected_criteria>

Run CTw6-AC1 from the worktree root under `timeout 120`. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~68/NFRA_CTLPLN.TO-CT-w-6.crossbox-ack-per-box-file-design.proof_of_spec.json` (CTw6-AC2 is a judgment row, recorded as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL), validate it with `python .tools/proof-of-spec-check.py <instance> CTw6-AC1,CTw6-AC2`, and flip `<status>` to `complete` only when the mechanical criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round8.md</decomp_doc>
<owned_cells>CT-w-6</owned_cells>
</decomp_ref>

<paths>
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a design that leaves two writers on one path (the CVO's judgment); a design that cannot read the old shape (item 3); a writing verb run to "see how it works" (forbidden by the rules); BLIND: the crossbox lane's mechanical grant (the CTO rules the lane change).
lane: the <paths> block IS the grant; `deliverables/0.9.0_WK_NFRA_CTLPLN~68/` needs no entry.
</preflight>

Source: `ROUND_ANALYSIS.round7.md` (E8 carried); `deliverables/2.0.0_SA_COO~C/E8_BOX_SYNC_CONFLICTS_SINCE_20261009.txt`; PRD v0.25 FWD-8.
