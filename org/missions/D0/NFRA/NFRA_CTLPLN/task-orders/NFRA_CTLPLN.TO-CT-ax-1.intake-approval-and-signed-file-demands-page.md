# TO NFRA_CTLPLN.TO-CT-ax-1 -- workstream OUTCOME round 25 (cell CT-ax-1): one page in the intake folder on what the tools demand of the approval file and the signed file (FWD-15, FWD-16)

<to_id>NFRA_CTLPLN.TO-CT-ax-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~136</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the worker tree (wk-NFRA_CTLPLN-136 @e23255f5c5) and again in the main tree after merge fe1ffbf219: CTax1-AC1 INTAKE-PAGE blocks=7 accepted=5 refused=21 ok=True (the planted wrong form in a copy is detected); CTax1-AC2 grep -c reads 1 (base 0); proof VALID; the page is 119 lines, ASCII; the README gained exactly one line. Two findings for the CTO, both INERT: W136-S1 the fetch approval gate (intake_fetch.py ~355-357, 630-641) and check 2 (intake_check.py ~385-402) read the approval file by different rules (a hash-suffixed line passes fetch and fails check 2; a case or space variant passes check 2 and fails fetch); W136-S2 no tool offers a read-only dry run of one approval line or one signed check-8 file, so the page says NONE where the CTO's ruling 2 expected a dry-run command (the page lists the self-tests and read-only verbs that do exist). The worker dropped the check-2 accepted block to stay under 120 lines: the laxer case and space rule of check 2 is prose, not graded. LOCAL until MSTR pushes.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ax-1` (`decompositions/NFRA_CTLPLN_DECOMP.round28.md`) | **outcome_ref:** FWD-15, FWD-16 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Round 27's yfinance batch lost four cycles to demands the intake tools make of two hand-written files and nobody had written down: the CTO's approval file (an exact `name==version` line per wheel), and the CTO's signed check-8 file (one file name per wheel, the `CHECK 8 SIGNED` marker, and the `WAIVE` line form). The CTO ruled (`org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round27.md`, ruling 2; read it) one page in the intake folder so the next batch does not rediscover them. This cell writes that page FROM THE TOOLS' OWN CODE and proves the page's example lines against the tools' own gate functions.

Read first: `org/devices/intake/README.md` (14 lines), `org/devices/intake/intake_request.py`, `intake_fetch.py`, `intake_check.py` (`check_8`, `has_sign_marker`, the waiver parsing added by cell CT-av-1, and how `approved_by` is read), `intake_closure.py`, and the two files that are the live examples: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_YFINANCE_LINUX_20261016.md` (with its addenda) and `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CHECK8_NFRA_CTLPLN_INTAKE_YFINANCE_LINUX_20261016.md`.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>` (for the two CTO files above: `org/tier1_exec/1.0.0_SA_CTO/deliverables`), retry, and name the folder, the command and the error in your final report.

### BUILD

1. **The page**, a NEW file `org/devices/intake/APPROVAL_AND_SIGNED_FILE_DEMANDS.md` (ASCII, under 120 lines), titled "What the intake tools demand of the approval file and the signed file". It carries exactly these five sections, each one short and each stating the rule the CODE enforces (cite the function and line), never what a past file happened to do:
   1. **The approval-file line:** the exact `name==version` form the tool matches, what it does with case, extras, hashes and a trailing comment, and the dry-run command the tool offers to test one line before a cut;
   2. **The signed check-8 file:** where it must live (the signer directory), that it must name the batch, the `CHECK 8 SIGNED` marker line, the exact per-wheel FILE names it must contain (one per wheel, the full wheel file name, not the project name), and the dry-run command to test them;
   3. **The `WAIVE` line:** the exact form `WAIVE <file name> check <N>: <reason>`, one file and one check per line, never checks 1 or 2, no wildcard, the reason non-empty, and that the verdict becomes `released-with-waiver`;
   4. **The order of the batch route:** request -> approval -> fetch -> checks 1-7 -> signed check 8 -> release -> pack -> verify -> send, one line each, naming the tool verb;
   5. **The dry-run commands:** every tool's own self-test or read-only verb that tests a line or a file without moving anything, as one table (tool, verb, what it reads, what it writes: nothing).
   Every example line in a fenced block marked ```` ```text accepted ```` MUST be accepted by the tool's real gate function and every example in a block marked ```` ```text refused ```` MUST be refused by it (see step 2). Use only synthetic names (`examplepkg==1.2.3`, `examplepkg-1.2.3-py3-none-any.whl`), never a real wheel.
2. **The test**, a NEW file `.tools/tests/test_round28_intake_page.py` (standard library plus the tools; temporary folders only; no network; ASCII output): it reads the page, asserts the five section headings are present, extracts every `accepted` and `refused` block, runs each line through the REAL gate function named in the block's preceding comment line (`<!-- gate: module.function -->`), and asserts accepted blocks pass and refused blocks fail; control arm: a planted wrong form in an `accepted` block makes the test fail (prove it on a temporary copy of the page). Last line `INTAKE-PAGE blocks=<k> accepted=<a> refused=<r> ok=<True|False>`.
3. **The pointer:** one line added to `org/devices/intake/README.md` naming the page, nothing else changed in that file.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~136/`. Change NO tool: if a tool's behaviour is hard to describe or contradicts its own comment, file ONE row and describe what the code does. NO network request, no `pip`, no install; do not run `release`, `pack`, `check`, `fetch` or any verb that writes against a real batch, and write nothing under `C:/opal-intake/`. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7. CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. Pin every artifact row of your proof instance to the commit that carried it. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W136-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTax1-AC1" cell_refs="CT-ax-1"><invocation>python .tools/tests/test_round28_intake_page.py</invocation><expect>ok=True</expect></criterion>
`CTax1-AC1` -- the page carries its five sections and every accepted and refused example is graded by the tools' own gate function, with a planted wrong form failing the test (base: the test does not exist); report the whole last line with its denominator.

<criterion id="CTax1-AC2" cell_refs="CT-ax-1"><invocation>grep -c APPROVAL_AND_SIGNED_FILE_DEMANDS org/devices/intake/README.md</invocation><expect>1</expect></criterion>
`CTax1-AC2` -- the folder's README points at the page exactly once (base: 0).
</proof_of_spec>

<expected_criteria>CTax1-AC1,CTax1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~136/NFRA_CTLPLN.TO-CT-ax-1.intake-approval-and-signed-file-demands-page.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTax1-AC1,CTax1-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round28.md</decomp_doc>
<owned_cells>CT-ax-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/APPROVAL_AND_SIGNED_FILE_DEMANDS.md
org/devices/intake/README.md
.tools/tests/test_round28_intake_page.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request; a page, a test and one README line.
comp-adversary: RUN -- the page describing a past file instead of the rule (every rule cites the function and line; every example is graded by the real gate); the page and the tools drifting apart (the test is the control: a tool change that breaks an example fails it); the test grading its own opinion (it calls the tools' functions, never a copy of their regex); a planted wrong example passing (control arm); BLIND: a demand that lives in a person's habit and no code (for example which seat signs) is not on the page.
risk: LOCAL -- a documentation page, a test and one README line inside the intake folder; no tool changes, nothing released or sent.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/` is NFRA_CTLPLN's (C-INTAKE); the CTO ruled the page (round-27 analysis ruling 2, msg 109661).
</preflight>

Base checks, dry-run by the issuer before the cut: CTax1-AC1 FAIL as expected (the test file does not exist); CTax1-AC2 FAIL as expected (`grep -c` reads 0 at the base).
Source: CTO round-27 analysis ruling 2 and enrichment item 2; FWD-15, FWD-16.
