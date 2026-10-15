# TO NFRA_CTLPLN.TO-CT-ai-5 -- workstream BATCH round 6 (cell CT-ai-5): ONE hygiene batch -- the commit hooks say what they did not grade (109393), org/ref in the sparse base set (W105-S2), the batch test leaves no fixtures (W105-S5)

<to_id>NFRA_CTLPLN.TO-CT-ai-5</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~110</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>BATCH</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ai-5` (`decompositions/NFRA_CTLPLN_DECOMP.round19.md`) | **outcome_ref:** FWD-2 (hygiene) |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Three small items, ONE cell. Read rows `NFRA_CTLPLN-W105-S2` and `NFRA_CTLPLN-W105-S5` first (Grep each id in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`). Item 1 comes from the CTO's message 109393 (from DSGN_RBNDV2 row W8-S1): a portal `.tsx` commit passed the hooks with 0 of 3 files checked, because the risk reflex used a stale map and `.tools/commit-gate.sh` reads only `.py`, `.sh` and `.tf`.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. **The hooks say what they skipped.** Find the risk reflex's file map in `.tools/safe-commit.sh` (Grep `risk` and `map` in it) and refresh it so a `portal/**/*.tsx` path is known; and make BOTH `.tools/commit-gate.sh` and the risk reflex print one line `not graded: <N> .tsx` (N = the count of staged `.tsx` files they did not grade) instead of passing silently, when any `.tsx` file is staged. Do not add a grade for `.tsx`; DSGN_RBNDV2 covers the real grading with merge-time portal checks. Done when a commit of a portal `.tsx` file prints a non-zero checked count or that line; test it in a temporary repository with the real two scripts, with one `.tsx` file and with none (no line).
2. **`W105-S2`.** Add `org/ref/` to the base sparse set in `.tools/wk-provision.sh` (read `cmd_provision`), so the author check finds it; extend `.tools/tests/test_wk_sparse_provision.py`'s expectation of the base set if it lists it (that file is in your `<paths>`).
3. **`W105-S5`.** `.tools/tests/test_round18_batch.py` leaves its `r18_batch_*` fixture folders under the Temp folder; make it remove only the folders IT created, in a `finally`, by the path it created (never a glob over Temp). Prove it with a before and after count of `r18_batch_*` folders in Temp. The four old folders already on disk are NOT removed: recursive deletion waits on Andrew.
4. A NEW test `.tools/tests/test_round19_hygiene.py` with the flags `--tsx`, `--org-ref` and `--cleanup`, each printing `HYGIENE-<ITEM> ... ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~110/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W110-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. 

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTai5-AC1" cell_refs="CT-ai-5"><invocation>python .tools/tests/test_round19_hygiene.py --tsx</invocation><expect>ok=True</expect></criterion>
`CTai5-AC1` -- a staged portal `.tsx` file makes both hooks print `not graded: <N> .tsx`, and a commit with none prints no such line (base: the file does not exist); report the whole last line.

<criterion id="CTai5-AC2" cell_refs="CT-ai-5"><invocation>python .tools/tests/test_round19_hygiene.py --org-ref</invocation><expect>ok=True</expect></criterion>
`CTai5-AC2` -- a worktree cut by `wk-provision.sh` holds `org/ref/` (base: the file does not exist); report the whole last line.

<criterion id="CTai5-AC3" cell_refs="CT-ai-5"><invocation>python .tools/tests/test_round19_hygiene.py --cleanup</invocation><expect>ok=True</expect></criterion>
`CTai5-AC3` -- running the round-18 batch test leaves no new `r18_batch_*` folder in Temp (base: the file does not exist, and the batch test leaves them); report the whole last line.
</proof_of_spec>

<expected_criteria>CTai5-AC1,CTai5-AC2,CTai5-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~110/NFRA_CTLPLN.TO-CT-ai-5.hygiene-tsx-not-graded-org-ref-fixture-cleanup.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTai5-AC1,CTai5-AC2,CTai5-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round19.md</decomp_doc>
<owned_cells>CT-ai-5</owned_cells>
</decomp_ref>

<paths>
.tools/commit-gate.sh
.tools/safe-commit.sh
.tools/wk-provision.sh
.tools/tests/test_wk_sparse_provision.py
.tools/tests/test_round18_batch.py
.tools/tests/test_round19_hygiene.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the hook change making a commit pass or fail that did not before (the test commits a non-`.tsx` file and requires the unchanged result); the new line printed for every commit (the none-case arm); the cleanup removing a folder it did not create (it removes by the created path only); `safe-commit.sh` is on every box's commit path, so a syntax slip blocks every commit (run `bash -n` on both scripts and the existing `.tools/tests` for safe-commit before the final commit); BLIND: the `.tsx` grading itself is DSGN_RBNDV2's.
risk: LOCAL -- shell tools on the commit path, tested in temporary repositories; no infra path.
lane: the <paths> block IS the grant (worker RULING 1). `.tools/safe-commit.sh` and `.tools/commit-gate.sh` are the commit gates; the CTO ordered this change (msg 109393, round-18 analysis ruling 4). Mind the byte budget on skill files (not touched here).
</preflight>

Base checks, dry-run by the issuer before the cut: CTai5-AC1, AC2 and AC3 FAIL as expected (the test file does not exist).
Source: CTO round-18 analysis section 3 (`ledger/ROUND_ANALYSIS.round18.md` @721e05298f), msg 109398; FWD-2 (hygiene).
