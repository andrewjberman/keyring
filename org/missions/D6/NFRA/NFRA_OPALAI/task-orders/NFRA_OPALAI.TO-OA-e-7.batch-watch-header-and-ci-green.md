# NFRA_OPALAI task order -- `OA-e-7` -- ROUND 2, E7: the batch cell -- the operator watch's header, and opal_ai CI that can pass

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-e-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~15</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is armed or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- the batch repair cell.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OA-e-7` (round 2, decomposition section R2.1)

Two small repairs, one cell.

**(1) The operator watch's header (parent repo, ruling I-3).** `.claude/skills/teams-assist/teams-watch.py` is an
OPERATOR-plane tool. It reads the operator's own Claude credential store, it is imported every 5 minutes by the D7
ticket-intake runner `integrations/ticketing/intake/runner.py` (the Windows Scheduled Task `OPAL_D7_ticket_intake`),
and it is the engine of the operator's `/teams-assist` catch-up. The Opal Analyst has its OWN watch, moved into
`opal_ai/opal/agent/teams_watch/teams-watch.py`. Edit the header of the parent file (its first 60 lines: the comment
banner and/or the module docstring) so that it names:
- the D7 intake runner by its path, `integrations/ticketing/intake/runner.py`;
- the operator's `/teams-assist`;
- the Analyst's own watch, `opal_ai/opal/agent/teams_watch/teams-watch.py`, stating that this file is NOT the
  Analyst's.
**Change no code.** The file is LIVE PRODUCTION: its banner says saving it is deploying it. Your edit lives only in
YOUR worktree until the issuer merges it, and the check proves the module's code (its AST, docstring aside) is
unchanged. Edit comments and the docstring only.

**(2) `opal_ai` CI that can pass (row Z-S20, FWD-13).** The only CI run on record failed: the workflow
`opal_ai/.github/workflows/ci.yml` installs ruff but never pytest, so pytest could not run; and the gate
`opal_ai/opal/checks/run_checks.sh` printed `ruff: FAIL (0 findings)` while ruff itself reported findings, because it
counts ruff's output with a line-anchored pattern (`grep -cE '^opal[/\\]'`) that ruff's default (full, and in some shells
ANSI-coloured) output format never matches. Repair:
- `ci.yml` installs BOTH pytest and ruff in a step BEFORE the step that runs `bash opal/checks/run_checks.sh`, with
  ruff PINNED `ruff==0.16.9`. That is the version the failing CI run installed unpinned (run 36203070607's log:
  `Successfully installed ruff-0.16.9`). The CI and a standalone copy must grade the same thing;
- `run_checks.sh` reports ruff's REAL finding count: ask ruff for a countable format (for example
  `--output-format concise`) with colour off, and count those lines. A planted unused import must read
  `ruff: FAIL (1 findings)`;
- every finding ruff 0.16.9 reports on `opal/` is FIXED in the code, never waived by an ignore or a rule change. Use
  the pinned binary the issuer installed: `C:/tmp/ruff-0.16.9/bin/ruff.exe` (put `C:/tmp/ruff-0.16.9/bin` FIRST on
  PATH; the box's own ruff is 0.15.11, which finds nothing, and that is why this defect was invisible here). Measured
  at the cut on `opal_ai` `fd8ab8a57f`: 13 findings, all in `opal/agent/teams_watch/teams-watch.py` (AMENDED: the cut
  said portal_lookup.py; row Z-W15-S1 measured them in the Analyst's watch, and the issuer re-read it with
  `--output-format concise`): 8 `SIM115`
  (`open()` without a context manager), 3 `BLE001` (blind `except Exception`), 1 `SIM102` (collapsible `if`) and
  1 `UP031` (`%`-formatting). Fix each one with the success path's behaviour unchanged. A narrowed `except` names the
  exceptions the guarded call can raise, and an error path keeps its message text.
The green run on a real push happens at the cutover (G-PUSH), not here.

## 2. BOUNDS

1. **`opal_ai` is a nested repository** at `<worktree>/opal_ai`, on its own branch off `opal_ai` `fd8ab8a57f`. Commit
   nested files with `git -C opal_ai commit --author "0.9.0_WK_NFRA_OPALAI~15 <0.9.0_WK_NFRA_OPALAI~15@opal.agent>" -F
   <msgfile> -- <nested paths>`, the msgfile written with the Write tool. Commit the parent file with `safe-commit.sh`.
2. No ruff ignore, `noqa`, per-file-ignore or rule-set change. No behaviour change to the success path of
   `opal/agent/teams_watch/teams-watch.py` (the Analyst's OWN watch, not the parent operator watch of item 1); its
   `test_teams_watch_lineage.py` keeps passing.
3. Standing: no push, no install (the pinned ruff is already installed), no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal
   with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
.claude/skills/teams-assist/teams-watch.py
opal_ai/.github/workflows/ci.yml
opal_ai/opal/checks/run_checks.sh
opal_ai/opal/agent/tools/portal_lookup.py
opal_ai/opal/agent/teams_watch/teams-watch.py
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~15/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `integrations/ticketing/intake/runner.py`.
Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_OPALAI-Z-W15-S<k>` (next free k for W15).

## 4. PROOF OF SPEC (literal; run from your worktree root, after BOTH repos are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-e-7"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e7.AC1.sh; echo "exit=$?"</invocation><expect>header consumers named 3 of 3; code AST equal to cut=yes; compiles=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-e-7"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e7.AC2.sh; echo "exit=$?"</invocation><expect>[ruff 0.16.9] clean run last line='CHECKS: PASS'; planted run 'ruff: FAIL (N findings)'; reported=N ruff-own=N with N>=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-e-7"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e7.AC3.sh; echo "exit=$?"</invocation><expect>pytest installed before it=yes; ruff installed before it=yes; ruff pinned 0.16.9=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~15/NFRA_OPALAI.TO-OA-e-7.batch-watch-header-and-ci-green.proof_of_spec.json`.
Report once: the header lines, the ruff version pinned, the count line before and after, any finding fixed, the commit
hashes in BOTH repos, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E7 = I-3 (header) + R-4 (Z-S20 CI). Chain G, alone. The `_ARGS_ALLOWLIST` row (Z-W2-S2) is
REMEDIATED and drops out (analysis s.4 item 7).

**THE DRAIN IS A LIVE DEPLOY for (1).** `teams-watch.py` is imported by `OPAL_D7_ticket_intake` every 5 minutes FROM
THE MAIN WORKING TREE (bar A5-A7, CTO~Z ruling 3a @123071c5cd). The merge of this branch changes the live file. In the
SAME act as the merge: `python -m py_compile .claude/skills/teams-assist/teams-watch.py`, one import of the module
from the main tree, and a read of the next scheduled fire's result. Revert first if the exercise cannot finish.

**RESOLVED by the issuer before the cut (the fork flagged it as unsound):** the CI run's log shows it installed ruff 0.16.9,
unpinned. The issuer installed `ruff==0.16.9` at `C:/tmp/ruff-0.16.9` (development download, Andrew-direct @f8d1103a38)
and measured `opal/` at `fd8ab8a57f` from a clean archive: 13 findings (8 SIM115, 3 BLE001, 1 SIM102, 1 UP031). The CI
log's "15" is its own line, and the difference is not chased. The face pins 0.16.9 in ci.yml, and the checks run that
binary. `FORCE_COLOR=3` in this shell puts ANSI codes into piped ruff output (the checks unset it).

SPAWN ONLY WHEN: at the cut (no precondition). Slot `~15`, nested worktree `--nested opal_ai=fd8ab8a57f`.

Dry-run at base (main tree, CLOUD `c8df03c408`; `OA_NESTED_REF=fd8ab8a57f` = the worker's nested base):
- e7.AC1 base: FAIL as expected (`header consumers named 1 of 3; code AST equal to cut=yes; compiles=yes`).
- e7.AC2 base (re-run by the issuer with the pinned ruff): FAIL as expected (`[ruff 0.16.9] opal_ai fd8ab8a57f: clean run
  last line='CHECKS: FAIL'; planted run 'ruff: FAIL (0 findings)'; reported=0 ruff-own=14`: the 13 real findings plus
  the plant, with Z-S20's miscount reproduced). The check bounds each run at 50 s.
- e7.AC3 base (re-run): FAIL as expected (`steps=4; run_checks step=3; pytest installed before it=no; ruff installed
  before it=yes; ruff pinned 0.16.9=no`).

**AMENDMENT 1 (2.0.0_SA_COO~AI, issuer licence, 2026-09-28 ~22:0xZ), on the worker's rows Z-W15-S1/-S2:** the 13 ruff 0.16.9
findings sit in `opal_ai/opal/agent/teams_watch/teams-watch.py`, not portal_lookup.py (the cut's error: a `--statistics`
read names no file). `<paths>` gains that file, and section 1/2's text is corrected. No criterion moves. The nested-commit
refusal (Z-W15-S2) was the validator's GIT_DIR census, fixed @fd0aa6ba57 and cherry-picked onto this branch. Gate limb:
to-pipeline-gate grades a MODIFIED order only on GATE (viii) placeholders (NONE here), so no limb graded this amendment.

<status>pending</status>
<round>2</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
