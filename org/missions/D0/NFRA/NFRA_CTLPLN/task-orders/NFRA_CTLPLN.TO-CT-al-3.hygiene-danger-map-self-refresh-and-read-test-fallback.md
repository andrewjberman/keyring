# TO NFRA_CTLPLN.TO-CT-al-3 -- workstream BATCH round 9 (cell CT-al-3): ONE hygiene batch -- the danger map carries its build time and the risk reflex refreshes it itself (S9127, W117-S1/S2/S3), and the FWD-5 read test works after the ledger entry is closed

<to_id>NFRA_CTLPLN.TO-CT-al-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~121</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the worker tree (wk-NFRA_CTLPLN-121 @82cf40bd09) and again in the main tree after the merge 0b35c0c854: HYGIENE-MAPAGE inside_time=True mtime_ignored=True rebuild_once=True ok=True; HYGIENE-SPARSE builds=0 reads_main_or_blind=True ok=True; FWD5-POSITIVE versions=2 etag_equals_repo_md5=True other_changed=0 audit_actor=0.0.0_AB_MSTR ok=True (the read test now works after the ledger entry closed; 0 of 190 keys); HYGIENE-MAP tsx_classed=1 py_classed=1 ok=True (round-20 --map) and its --stale SKIP; COMP-PULSE BATTERY 12/12 PASS (denominator 12) in the main tree; comp-pulse diff on a real file reads REFLEX CLEAN against 2703 danger nodes in 0.9 s; proof VALID. Rulings on the worker's rows: S1 (a sparse worktree reads its own checked-out map, which is the main tree's committed map at that commit, before the main tree's file) is accepted: the committed map is the one artifact both read. S2 is closed by this merge (the committed map now carries built_utc). S3/S4 (the same corpus builds to 2692, 2703, 3491 edges by tree; the build guard has no portal check) are carried to the CTO as the map's owner. The map was built in a scratch full-index clone because the main tree is outside a worker's grant; the output was copied byte for byte.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>BATCH</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-al-3` (`decompositions/NFRA_CTLPLN_DECOMP.round22.md`) | **outcome_ref:** hygiene |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Read rows `NFRA_CTLPLN-S9127` and `W117-S1`, `W117-S2`, `W117-S3` (Grep each id in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`), and the CTO's round-21 analysis ruling 7 (`ledger/ROUND_ANALYSIS.round21.md`): the danger map `org/modules/graph/nerves-risk-edges.json` is this change's own, a tool artifact with no served consumer, so a self-refreshing read is enough and NO new scheduled task is installed (standing moratorium on monitors). Facts at the cut: the reflex is `comp-pulse diff` (`.tools/comp-pulse` calls `org/modules/graph/comp_pulse.py`); the map is built by `python org/modules/graph/nerves_lexical.py build`; the reflex decides STALE from the file's mtime, so the map reads fresh after any checkout and stale after a week untouched (W117-S1); nothing in the diff path rebuilds it (W117-S3); a build in a sparse worktree emits a 51-node map silently (W117-S2). Item 3 is from the CTO's round-21 inputs: `.tools/tests/test_round21_fwd5_positive_read.py` reads the ledger entry's open time from the open sentinel, which `deploy_ledger.py close` removes, so after close it prints `other_changed=-1 ok=False`.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. **S1:** make the map carry its build time INSIDE the file (a field the build writes, for example `built_utc`), and make the reflex read that field for the age; the file's mtime is never used. A map without the field reads as unknown age and is treated as stale.
2. **S3:** when the reflex finds the map older than its threshold, it rebuilds the map itself once (the same build command, in-process or a child, with a timeout of 120 s and a lock so two reflexes do not both build), then reads it; if the rebuild fails or times out it prints the existing `NOT-DECIDABLE: danger map STALE` and the reason. No scheduled task, no loop, no new service.
3. **S2:** a build or rebuild in a SPARSE worktree never runs (detect `core.sparseCheckout` true, or a node count far below the main tree's); the reflex there reads the main tree's map (`git rev-parse --git-common-dir` gives the main tree) or prints `BLIND: sparse worktree, no map` and exits as NOT-DECIDABLE. The 51-node silent build must not be possible.
4. **Read test fallback:** in `.tools/tests/test_round21_fwd5_positive_read.py`, when the open sentinel `org/critical_paths/.open_deploys/ctlpln-r21-fwd5-one-script-20261015.json` is absent, read the entry's open time from its closed completion record under `org/critical_paths/change_management/` (`*ctlpln-r21-fwd5-one-script-20261015_deploy_completion.md`); the default run then prints `other_changed=0` (as the CloudOps seat recorded 0 of 190). Add the flag `--since <UTC>` for an explicit open time.
5. A NEW test `.tools/tests/test_round22_hygiene.py`: flag `--map-age` (temporary copies of the map: an aged embedded time -> stale and the rebuild stub is called once; a fresh embedded time with an OLD mtime -> fresh and no rebuild; a map with no embedded time -> stale) prints `HYGIENE-MAPAGE inside_time=<True|False> mtime_ignored=<True|False> rebuild_once=<True|False> ok=<True|False>`; flag `--sparse` (a real sparse worktree cut by `.tools/wk-provision.sh`, or a mock of the sparse test) prints `HYGIENE-SPARSE builds=<n> reads_main_or_blind=<True|False> ok=<True|False>`. Rebuild the map ONCE at the end with the new build (it now carries its time), from a FULL tree (the main tree or a worktree with the corpus folders), and commit that output as it came; run `bash .tools/comp-pulse diff` on one staged `.py` and one staged `.tsx` afterwards and report both outputs.
Keep `python .tools/tests/test_comp_pulse_battery.py` at no fewer than 10 passing arms of 12 and `python .tools/tests/test_round20_hygiene.py --map` and `--stale` passing.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~121/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W121-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. The 33-row listing of ruling 9 is the issuer's, not yours.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTal3-AC1" cell_refs="CT-al-3"><invocation>python .tools/tests/test_round22_hygiene.py --map-age</invocation><expect>ok=True</expect></criterion>
`CTal3-AC1` -- the age comes from inside the map, the mtime is ignored, and an old map is rebuilt once by the reflex (base: the test does not exist); report the whole line.

<criterion id="CTal3-AC2" cell_refs="CT-al-3"><invocation>python .tools/tests/test_round22_hygiene.py --sparse</invocation><expect>ok=True</expect></criterion>
`CTal3-AC2` -- a sparse worktree never builds a map and reads the main tree's or reports BLIND (base: the test does not exist); report the whole line.

<criterion id="CTal3-AC3" cell_refs="CT-al-3"><invocation>python .tools/tests/test_round21_fwd5_positive_read.py</invocation><expect>other_changed=0</expect></criterion>
`CTal3-AC3` -- after the ledger entry is closed the FWD-5 read test still counts the other keys changed since the open time (base: `other_changed=-1 ok=False`); report the whole `FWD5-POSITIVE` line (it reads S3 and takes about a minute).
</proof_of_spec>

<expected_criteria>CTal3-AC1,CTal3-AC2,CTal3-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~121/NFRA_CTLPLN.TO-CT-al-3.hygiene-danger-map-self-refresh-and-read-test-fallback.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTal3-AC1,CTal3-AC2,CTal3-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round22.md</decomp_doc>
<owned_cells>CT-al-3</owned_cells>
</decomp_ref>

<paths>
org/modules/graph/comp_pulse.py
org/modules/graph/nerves_lexical.py
org/modules/graph/nerves-risk-edges.json
.tools/tests/test_round22_hygiene.py
.tools/tests/test_round20_hygiene.py
.tools/tests/test_round21_fwd5_positive_read.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write; AC3 makes read-only S3 `head`/`list` calls.
comp-adversary: RUN -- the reflex rebuilding on every commit (the threshold test and the lock; the rebuild runs once per stale period); a rebuild that hangs a commit (timeout 120 s, then NOT-DECIDABLE); a rebuilt map in a partial tree classing less than the real one (rebuild only from a full tree, node count printed); a map without the embedded time read as fresh (it reads stale); the risk reflex is on every commit path on this box, so a regression blocks or blinds every commit: run the comp-pulse battery and the real `comp-pulse diff` before the final commit; the committed map is generated data, shared, large (about 96k lines changed last time); BLIND: other boxes carry their own copy of the map file via git and read the embedded time too.
risk: LOCAL -- shared graph-module tools and one generated data file, tested in temporary copies; no infra path.
lane: the <paths> block IS the grant (worker RULING 1). `org/modules/graph/` files are admitted to a worker serial through this order's `<paths>` (ADHC_OWNPTH.005); the CTO ruled the change and owns the map (round-21 analysis ruling 7).
</preflight>

Base checks, dry-run by the issuer before the cut: CTal3-AC1 and AC2 FAIL as expected (the test file does not exist); CTal3-AC3 FAIL as expected (`other_changed=-1 ok=False` after the entry closed).
Source: CTO round-21 analysis sections 2-3 (`ledger/ROUND_ANALYSIS.round21.md` @a558191b7c), msg 109483; hygiene.
