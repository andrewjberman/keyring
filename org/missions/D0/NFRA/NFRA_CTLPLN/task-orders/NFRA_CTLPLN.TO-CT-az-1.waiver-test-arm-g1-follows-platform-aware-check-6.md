# TO NFRA_CTLPLN.TO-CT-az-1 -- workstream OUTCOME round 26 (cell CT-az-1): the waiver test's arm g1 follows the platform-aware check 6 (FWD-15, FWD-16)

<to_id>NFRA_CTLPLN.TO-CT-az-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~138</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the worker tree (wk-NFRA_CTLPLN-138 @ec16072890) and again in the main tree after merge 6d323036c3: CTaz1-AC1 WAIVER arms=20/20 ok=True (base 19/20); proof VALID; the diff is the one arm (verdict assertion failed -> passed plus one assertion on platform_normalised_equal), nothing else. The worker's mutant (platform rule disabled in a scratch copy) reads 19/20 with arm g1 the only FAIL. All intake suites green in the main tree: INTAKE-CHECK-TEST 60/60, INTAKE-RECEIVE-TEST 36/36, INTAKE-CLOSURE-TEST 10/10, INTAKE-FETCH-TEST 21/21, CHECK6-PLATFORM 14/14, INTAKE-PAGE 26 of 26 examples. No rows. LOCAL until MSTR pushes.</status_reason>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-az-1` (`decompositions/NFRA_CTLPLN_DECOMP.round28.md`, amendment 3) | **outcome_ref:** FWD-15, FWD-16 |
**depends_on:** CT-aw-1 (merged, 528891b0b7)

---

## WORKER FACE

### THE CELL

Cell CT-aw-1 made intake check 6 platform-aware (`org/devices/intake/intake_check.py` `check_6`, merged `528891b0b7`): across platforms a CRLF-only difference now reads `passed` and the file is listed in the evidence key `platform_normalised_equal`. The waiver test `.tools/tests/test_round27_waiver.py` (cell CT-av-1) has an arm that pinned the OLD behaviour for the same pair and now fails: `arm_g1_cross_platform_check_6_records_the_comparison_and_the_crlf_count` (about lines 279-296) asserts `c6["verdict"] == "failed"` and reads `WAIVER arms=19/20 ok=False`. The issuer ruled (as for the same stale case in `test_intake_check.py`, row `W135-S1`) that this arm follows the rule.

### BUILD

In ONLY that arm, change the verdict assertion from `"failed"` to `"passed"` (update its comment: a cross-platform CRLF-only difference is platform-normalised-equal), and add one assertion that `ev["platform_normalised_equal"]` lists the synthetic `__init__.py` (read how CT-aw-1's own test `.tools/tests/test_round28_check6_platform.py` asserts it, and copy that shape). Keep every other assertion of the arm (`py_differing_count == 1`, `differ_after_crlf_normalisation == 0`, `compared_across_platforms is True`, the two platform strings). Change NO other arm, no tool, and nothing in `org/devices/intake/`.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~138/`. NO network request, no `pip`, no install; do not touch anything under `C:/opal-intake/`. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7. CLAUDE.md and org/XXX.md are LOCKED. COMMIT as soon as the edit passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's: do not edit the order file. Pin every artifact row of your proof instance to the commit that carried it. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W138-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTaz1-AC1" cell_refs="CT-az-1"><invocation>python .tools/tests/test_round27_waiver.py</invocation><expect>WAIVER arms=20/20 ok=True</expect></criterion>
`CTaz1-AC1` -- the waiver test passes in full, its one stale arm following the platform-aware check 6 (base: `WAIVER arms=19/20 ok=False`); report the whole last line.
</proof_of_spec>

<expected_criteria>CTaz1-AC1</expected_criteria>

The invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~138/NFRA_CTLPLN.TO-CT-az-1.waiver-test-arm-g1-follows-platform-aware-check-6.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTaz1-AC1` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round28.md</decomp_doc>
<owned_cells>CT-az-1</owned_cells>
</decomp_ref>

<paths>
.tools/tests/test_round27_waiver.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request; one test-file edit.
comp-adversary: RUN -- the edit weakening the arm (the arm keeps its platform and CRLF-count assertions and gains one on `platform_normalised_equal`; a mutant that reverts the tool to `failed` must make the arm fail again); other arms changed (forbidden by the face); BLIND: none beyond the ordinary.
risk: LOCAL -- one test-file edit against synthetic wheels in temporary folders; no tool, record or released file changes.
lane: the <paths> block IS the grant (worker RULING 1). The stale arm is a consequence of CT-aw-1 (CTO ruling 3, msg 109661), recorded in the round-28 decomposition amendment 3.
</preflight>

Base check, dry-run by the issuer before the cut: CTaz1-AC1 FAIL as expected (`WAIVER arms=19/20 ok=False`).
Source: the issuer's own merge-time re-run of the neighbouring suites after CT-aw-1; FWD-15, FWD-16.
