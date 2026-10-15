# TO NFRA_CTLPLN.TO-CT-am-2 -- workstream BATCH round 10 (cell CT-am-2): HYGIENE batch A -- only the main tree builds the danger map and its header names its inputs (W121-S3/S4); check 8 is recorded as awaiting, not failed (W119-S1); the two real 20261008 fetch records are counted for the laptop (W111-S1)

<to_id>NFRA_CTLPLN.TO-CT-am-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~124</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in worker tree wk-NFRA_CTLPLN-124 @621ed1cfcb (merged 0efcd4e8c0): CTam2-AC1 HYGIENE-GUARD arms=6/6 ok=True; CTam2-AC2 HYGIENE-CHECK8 awaiting=True release_refused=True ok=True; CTam2-AC3 HYGIENE-LEGACY device=laptop requests=8 files=2 attributed_by=batch unattributed=0 ok=True; diff paths inside the order; proof instance VALID in the main tree. Rows W124-S1/S2/S3 OBSERVATION, INERT. The committed nerves-risk-edges.json keeps its old header until the next main-tree build. LOCAL until MSTR pushes.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>BATCH</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-am-2` (`decompositions/NFRA_CTLPLN_DECOMP.round23.md`) | **outcome_ref:** hygiene |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Three items of the CTO's round-22 hygiene batch (`ledger/ROUND_ANALYSIS.round22.md` ruling 3 and ruling 4, enrichment item 4); the batch is split in two cells for size and this is the first. Read rows `NFRA_CTLPLN-W121-S3`, `W121-S4`, `W119-S1` and `W111-S1` (Grep each id in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`) and the CVO's note on W111-S1 in `surprise-channel/adjudications/ADJUDICATION_v27.md` (its done-when: `downloads --device laptop` counts the two real 20261008 records). Facts: the map builder is `org/modules/graph/nerves_lexical.py`, the reflex is `org/modules/graph/comp_pulse.py` (both changed in round 22 by worker `~121`: the map carries `built_utc`, the reflex refreshes it, a sparse worktree never builds); the same corpus built to 2692, 2703 and 3491 edges in different trees, and the build guard has no check that `portal/` is present. `org/devices/intake/intake_check.py` records check 8 as `failed` (verdict `not_checked`) when the CTO's signature file does not exist yet. The downloads reader is `org/devices/intake/intake_request.py downloads`; the two real fetch records of batch `intake-20261008-a` carry no `device` key and read as unattributed.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. **Map build guard (ruling 3):** `nerves_lexical.py build` REFUSES (non-zero exit, a printed reason, nothing written) unless it runs in the MAIN tree (not a linked worktree: compare `git rev-parse --git-dir` with `--git-common-dir`) with a non-sparse checkout and with `portal/` initialized (a non-empty tracked `portal/` tree, not just the gitlink). The map's header gains `built_from_head` (the tree's HEAD sha), `portal_sha` (the portal submodule's checked-out sha) and `edge_count`; the reflex's refresh calls the same guard and, when the guard refuses, prints `NOT-DECIDABLE: danger map STALE and the build guard refused: <reason>` rather than building. Do NOT rebuild and recommit the map in this cell (the worker serial cannot build in the main tree); the next main-tree build writes the new header. No cross-tree comparator is kept.
2. **W119-S1:** in `org/devices/intake/intake_check.py`, when check 8's signature file does not exist, record the verdict as `awaiting` (a recorded check state, not `failed`), and make the release refuse with the reason `check 8 awaits the signature` in that state; every other state reads as it does now. Keep `test_round22_journey_record.py --check` reading `ok=True` for the pre-release and the post-release states (it maps failed-plus-absent-file to AWAITING today: make it accept the tool's new `awaiting` as well as the old form for already-written records).
3. **W111-S1 legacy records:** a batch whose fetch records predate the `device` key is declared by a file `org/devices/intake/records/<batch>/DEVICE_OF_BATCH.txt` holding one line `laptop` plus a sentence naming the route rule (C-INTAKE: the laptop alone fetches); `intake_request.py downloads` attributes a record with no `device` key to the batch's declared device when that file exists and prints `attributed_by=batch` in the line; with no declaration it stays `unattributed`. Write the declaration for `intake-20261008-a` (read its two real records; if either record names a `fetched_by` that is not a laptop seat, STOP and file a BLOCKING row). Do not edit the existing records.
4. A NEW test `.tools/tests/test_round23_hygiene_a.py` with the flags `--guard` (arms in temporary copies: refuses in a linked worktree, refuses sparse, refuses without portal content, admits in a full main tree with portal; the header fields are written; prints `HYGIENE-GUARD arms=<k>/<n> ok=<True|False>`), `--check8` (prints `HYGIENE-CHECK8 awaiting=<True|False> release_refused=<True|False> ok=<True|False>`) and `--legacy` (prints `HYGIENE-LEGACY device=laptop requests=<n> files=<k> attributed_by=batch unattributed=0 ok=<True|False>` for the real `20261008` day).

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~124/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W124-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. The reads of rows S9105 and S9101 are the issuer's and already done; do not touch the old order files.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTam2-AC1" cell_refs="CT-am-2"><invocation>python .tools/tests/test_round23_hygiene_a.py --guard</invocation><expect>ok=True</expect></criterion>
`CTam2-AC1` -- the map build refuses outside the main tree, sparse or without portal, and the header names its inputs (base: the test does not exist); report the whole line.

<criterion id="CTam2-AC2" cell_refs="CT-am-2"><invocation>python .tools/tests/test_round23_hygiene_a.py --check8</invocation><expect>ok=True</expect></criterion>
`CTam2-AC2` -- an unsigned check 8 is recorded as awaiting and the release refuses with that reason (base: the test does not exist; the tool records `failed`); report the whole line.

<criterion id="CTam2-AC3" cell_refs="CT-am-2"><invocation>python .tools/tests/test_round23_hygiene_a.py --legacy</invocation><expect>ok=True</expect></criterion>
`CTam2-AC3` -- `downloads --device laptop` counts the two real 20261008 records, attributed by the batch declaration (base: the test does not exist; the records read unattributed); report the whole line.
</proof_of_spec>

<expected_criteria>CTam2-AC1,CTam2-AC2,CTam2-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~124/NFRA_CTLPLN.TO-CT-am-2.hygiene-danger-map-guard-check8-awaiting-legacy-device.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTam2-AC1,CTam2-AC2,CTam2-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round23.md</decomp_doc>
<owned_cells>CT-am-2</owned_cells>
</decomp_ref>

<paths>
org/modules/graph/nerves_lexical.py
org/modules/graph/comp_pulse.py
org/devices/intake/intake_check.py
org/devices/intake/intake_request.py
org/devices/intake/records/intake-20261008-a/DEVICE_OF_BATCH.txt
.tools/tests/test_round22_journey_record.py
.tools/tests/test_round23_hygiene_a.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call, no network.
comp-adversary: RUN -- the guard blocking a legitimate main-tree build (arm: full main tree with portal admits); the reflex refresh looping on a refused guard (it prints and stops); the map header fields breaking the reflex's reader (run `python .tools/tests/test_comp_pulse_battery.py`, which reads 12 of 12 at the cut, and `bash .tools/comp-pulse diff` on a real file); the `awaiting` state breaking the release or the journey records already written (the journey flags `--check` and `--release` must keep reading ok=True on the real records); a batch declaration attributing a record to the wrong device (the two records' `fetched_by` are read first); BLIND: the guard cannot prove `portal/` content is current, only present.
risk: LOCAL -- shared graph-module tools and intake tools, tested in temporary copies and on the real records read-only; no infra path.
lane: the <paths> block IS the grant (worker RULING 1). `org/modules/graph/` files and `org/devices/intake/` are admitted to a worker serial through this order's `<paths>`; the CTO ruled the batch (round-22 analysis ruling 3, 4).
</preflight>

Base checks, dry-run by the issuer before the cut: CTam2-AC1, AC2 and AC3 FAIL as expected (the test does not exist). Controls to keep: `COMP-PULSE BATTERY: 12/12 PASS`, `test_round22_journey_record.py --fetch/--check/--release/--pack/--taildrop` ok=True.
Source: CTO round-22 analysis sections 2-3 (`ledger/ROUND_ANALYSIS.round22.md` @1d8ee95b78); hygiene.
