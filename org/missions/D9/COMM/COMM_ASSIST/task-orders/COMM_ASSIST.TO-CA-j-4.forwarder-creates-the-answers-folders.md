# TO COMM_ASSIST.TO-CA-j-4 -- round 18 CA-j-4: the forwarder creates answers/, answers/done/ and answers/rejected/ when they are absent (seat row COMM_ASSIST-D2-S1)

<to_id>COMM_ASSIST.TO-CA-j-4</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~20</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-j-4` (`decompositions/COMM_ASSIST_DECOMP.round18.md`) | **outcome_ref:** FWD-7, FWD-8 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`data/transcripts/scripts/muse_reader/forwarder.py` carries each signed answer file from a folder on dell2 to the assistant. Today its `forward(root, send, now)` returns at once when `<root>/answers/` is absent (about line 117), so on a fresh folder it creates nothing, and the dell2 seat had to make the folders by hand.
You make it create `answers/`, `answers/done/` and `answers/rejected/` when they are missing, and nothing else.

### BUILD

1. In `forward`, replace the early return on a missing `answers/` with creating `answers/`, `answers/done/` and `answers/rejected/` (the done and rejected folders are created today only when there is something to write; create all three up front, with `parents=True, exist_ok=True`). Everything after that stays as it is: a file already present, a marker already present, the retry rule, the shapes written.
2. Edit nothing else. No non-ASCII.

### RULES

- Edit nothing but the files in `<paths>`. Code change; not deployed here (the dell2 checkout picks it up through the box pass).
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAj4-AC1" cell_refs="CA-j-4"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j4_dirs.py"</invocation><expect>J4-DIRS ok=True arms=3 of 3</expect></criterion>
`CAj4-AC1` -- the issuer's check (read it; do not edit it): on a reader folder with no `answers/`, `forward` creates all three; an answer file already there and a rejected marker are left alone; a second run is harmless. It prints ok=False at the base (1 of 3).

<criterion id="CAj4-AC2" cell_refs="CA-j-4"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i3_forward.py"</invocation><expect>I3-FORWARD ok=True arms=6 of 6</expect></criterion>
`CAj4-AC2` -- the bound, a control that PASSES at the base and must still pass: the forwarder's six arms from round 17.
</proof_of_spec>

<expected_criteria>CAj4-AC1,CAj4-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~20/COMM_ASSIST.TO-CA-j-4.forwarder-creates-the-answers-folders.proof_of_spec.json`, validate it by running the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree: `python .tools/proof-of-spec-check.py <instance> CAj4-AC1,CAj4-AC2`, and flip `<status>` to `complete` only when both pass and
the instance is VALID. Your final report names the exact lines you changed. Your surprise rows are `COMM_ASSIST-W20-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round18.md</decomp_doc>
<owned_cells>CA-j-4</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/muse_reader/forwarder.py
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-4.forwarder-creates-the-answers-folders.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~20/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; no AWS call is made.
comp-adversary: RUN -- creating the folders deletes or moves an existing answer file (refused: AC1 arm 2); a second run re-creating over markers (refused: AC1 arm 3); the once-only rule changed (refused: AC2). BLIND: the dell2 checkout picks the change up at its next box pass; the live task keeps running the old file until then.
lane: the <paths> block IS the grant (worker RULING 1). DIRECT-ACT: a few lines, LOCAL; no L8-L10; its close is the issuer's one real run.
</preflight>

Base: CAj4-AC1 base: FAIL as expected (1 of 3 arms: the control); CAj4-AC2 base: PASS as expected (control, 6 of 6). AC1 green arm not exercised before the build (the build is the early return's removal).
Source: dell2 seat report `deliverables/0.7.0_AE_CloudOps~CA2/REPORT_TO-CA-i-5.md` (row D2-S1); CTO round-17 analysis item 5.
