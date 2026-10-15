# TO NFRA_CTLPLN.TO-CT-af-3 -- workstream BATCH round 4 (cell CT-af-3): the placement-refusal branch of the naming stage unstages every path the call staged (row W99-S1, the twin of W93-S1)

<to_id>NFRA_CTLPLN.TO-CT-af-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~102</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>BATCH</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-af-3` (`decompositions/NFRA_CTLPLN_DECOMP.round16.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Read row `NFRA_CTLPLN-W99-S1` (Grep `"id": "NFRA_CTLPLN-W99-S1"` in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`) and its twin `NFRA_CTLPLN-W93-S1`. In `.tools/safe-commit.sh` the naming stage has two refusal paths. Round 15 (`CT-ae-3`) made the ENFORCE refusal (the `elif [ "$NGATE_ENFORCE" -eq 1 ] && [ "$NGATE_RC" -ne 0 ]` branch, about :1190-1196) unstage EVERY path the call staged: it builds `_ng_all` from `IN_SCOPE` and runs `git reset -q HEAD --` over it. The PLACEMENT refusal branch just above it (`if [ "$NGATE_PLACE_HIT" -eq 1 ] && [ "$NGATE_ENFORCE" -ne 1 ]`, about :1183-1189, reached when `org/mcp/naming-place.enforce` exists and the gate prints `NAMING-PLACE: REFUSE`) still unstages only `NGATE_FILES` (the eight graded extensions), so a non-graded file staged beside them, for example the project `.md` deliverable, stays in the index after the refusal.

### BUILD

1. Make the placement refusal unstage every path in `IN_SCOPE`, the same way the ENFORCE branch does. Share the construct rather than copying it if a three-line function reads cleaner than two copies; either way the ENFORCE branch behaves exactly as it does today. The `_np_unwind` call, the error text, the printed gate output and `exit 1` are unchanged.
2. A NEW test `.tools/tests/test_placement_unstage.py` (standard library, temporary repositories only, no AWS, no network). Extract the naming stage from `safe-commit.sh` the way `.tools/tests/test_round15_batch.py` arm 2 and `.tools/tests/test_safe_commit_derivation.py` do (read both first), in a temporary repository whose tree has `org/mcp/naming-place.enforce`, with a stub `naming-gate.py` that exits non-zero and prints a line starting `NAMING-PLACE: REFUSE `. RUN THE GATE WITH ITS LIVE LIMB SWITCHED OFF (a stub only; never the real gate). Arms: (a) a `.md` and a graded `.json` both staged: after the placement refusal (exit 1) both are unstaged; (b) with `org/mcp/naming-place.enforce` absent and the stub refusing: the placement branch does not fire (the exit behaviour is whatever the base prints for the same fixture; compare against the base by running the same fixture through `git show HEAD:.tools/safe-commit.sh` extracted to a temporary file); (c) the ENFORCE branch (naming enforce present, stub refusing without a placement line) still unstages both, exit 1 (the `CT-ae-3` behaviour); (d) a clean pass (stub exits 0) leaves both staged. Final line `PLACEMENT-UNSTAGE arms=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. This edits the commit path every seat uses: run the naming gate with its LIVE LIMB SWITCHED OFF in every experiment (the way `.tools/tests/test_safe_commit_derivation.py` does), and make no AWS call. No aws, no network, no push. `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. ASCII only; Python 3.12. CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~99/NFRA_CTLPLN.TO-CT-ae-3.batch-repair-round14-rows.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W102-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTaf3-AC1" cell_refs="CT-af-3"><invocation>python .tools/tests/test_placement_unstage.py</invocation><expect>ok=True</expect></criterion>
`CTaf3-AC1` -- every arm passes, including the placement refusal that now unstages the `.md` (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTaf3-AC2" cell_refs="CT-af-3"><invocation>python .tools/tests/test_round15_batch.py</invocation><expect>ok=True</expect></criterion>
`CTaf3-AC2` -- the round-15 batch suite, whose arm 2 grades the ENFORCE refusal, still passes (base: `ROUND15-BATCH arms=9/9 ok=True`, a control); report the whole last line.

<criterion id="CTaf3-AC3" cell_refs="CT-af-3"><invocation>python .tools/tests/test_safe_commit_derivation.py</invocation><expect>ok=True</expect></criterion>
`CTaf3-AC3` -- the derivation suite still passes (base: `SAFE-COMMIT-DERIVATION cases=17/17 ok=True`, a control, about 52 seconds); report the whole last line.
</proof_of_spec>

<expected_criteria>CTaf3-AC1,CTaf3-AC2,CTaf3-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 300`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~102/NFRA_CTLPLN.TO-CT-af-3.placement-refusal-unstages-all.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTaf3-AC1,CTaf3-AC2,CTaf3-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round16.md</decomp_doc>
<owned_cells>CT-af-3</owned_cells>
</decomp_ref>

<paths>
.tools/safe-commit.sh
.tools/tests/test_placement_unstage.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the ENFORCE refusal behaviour changed by sharing the construct (arm c and CTaf3-AC2 keep it); a refusal that unstages a file it did not stage (arm a stages only the call's own paths); a clean pass that loses its staged files (arm d); the placement branch firing without `naming-place.enforce` (arm b); a live gate call in the experiment (stub only); BLIND: the placement OVERRIDE path (a `# naming-place-override:` line stages an audit row and adds it to the pathspec before the refusal), whose row `_np_unwind` removes: the worker reports whether the new unstage interacts with that row, by reading the branch, since the arms do not exercise the override.
risk: LOCAL -- a shell tool and a temporary-repository test; no infra path in `<paths>`.
lane: the <paths> block IS the grant (worker RULING 1). `.tools/safe-commit.sh` is on every seat's commit path.
</preflight>

Base checks, dry-run by the issuer before the cut: CTaf3-AC1 base: FAIL as expected (the file does not exist); CTaf3-AC2 and CTaf3-AC3 base: controls (`ROUND15-BATCH arms=9/9`, `SAFE-COMMIT-DERIVATION cases=17/17`), see the issuer's dry-run note in the issuance commit.
Source: CTO round-15 analysis section 4 item 3 (`ledger/ROUND_ANALYSIS.round15.md` @0be7eb664c); rows W99-S1, W93-S1; the `CT-ae-3` close note.
