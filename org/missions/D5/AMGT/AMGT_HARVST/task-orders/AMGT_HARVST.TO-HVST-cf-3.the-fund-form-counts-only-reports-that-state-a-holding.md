# AMGT_HARVST task order -- `HVST-cf-3` -- ROUND 92, workstream FUNDFORM-CODE: THE FUND FORM COUNTS ONLY THE REPORTS THAT STATE A HOLDING AND NEVER THE MISFILED MEXICO REPORTS (CTO round-91 analysis item 2; rows D1-S45, D1-S46)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cf-3.the-fund-form-counts-only-reports-that-state-a-holding</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cf-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~164</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and offline tests, plus READ-ONLY S3 reads of the bucket `opal-data-harvest` in the census step ONLY: the silver prefix `amgt/harvest/silver/research-report/` and the extraction objects each silver row names (`extract_key`), through `lib.research.harvest.store._default_client()`; never `put`, `delete`, `copy`, `sync` or a bare `aws` call. Budget: at most 800 requests and 300 MiB in all, counted in the census's last line. NO `fund_form.write`, `gold_put`, `write_one` or `silver_append` is RUN with a real client, NO deploy, NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a change that silently counts zero reports when a row lacks the key (it must raise), a change that moves a holding report out of its form, a MISFILED report that survives because the match is on the report id alone (match the security key AND the report id), a method version that is not bumped (the object name hashes it; `substrate` picks a stored form by it), an existing test fixture changed beyond the one key it needs, and a census whose baseline is read from `HEAD` after the worker's own commits (pin the baseline commit).
</preflight>

## 0. THE CELL

`lib/research/corpus/fund_form.py::gather_items` (line 241) reads every typed silver `research-report` row and returns items `(report_id, row.get("fund"), report_class, headings, extract_key)`; `build`, `distinct_funds`, `_inputs_for_fund` and `absent_fund_reports` then group by that `fund`. A report that only NAMES a fund (a candidate, an initiation, a bracketed template) is counted in that fund's form, and the two misfiled Mexico reports (`typed.MISFILED_REPORTS`) are counted in KMB's. The silver row now carries `fund_relation` (`holding`, `candidate`, `initiate`, `interest`, `template`, `unclassified`, `none`; `HVST-cg-1`, `-5`, rewritten into the bucket by `HVST-cg-2` on 2026-10-18 01:00Z). The CTO ruled (round-91 analysis item 2): **the fund form counts holding reports only, and drops the two misfiled Mexico reports.** This cell changes `fund_form.py` and its tests, and runs a read-only census. It writes no object and deploys nothing; the rebuild is a later seat order (`HVST-cf-5`).

**What the issuer measured from the stored census (`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~163/cg5_census.out`, read it) for the reports of class A, B, C and D that name a fund:** before, IDVZ 92, PFOE 43, DIVZ 2 (137 in all); after the rule (relation `holding`), IDVZ 82, PFOE 33, DIVZ 0 (115 in all); dropped 22 = `candidate` 14, `initiate` 2, `interest` 2, `template` 1, `none` 3 (three rows whose `fund` comes from a bare table token `Fund IDVZ`, the fallback window: `AZN_LN`, `NOKIA_FH`, `WALMEX*_MM`). DIVZ has no holding report at all (its only two named reports are `CLX` candidates), so `distinct_funds` returns two funds, IDVZ and PFOE. The two misfiled Mexico reports are not in that census (it excludes them); they leave on top.

## 1. THE BUILD (LOCAL, about 40 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `lib/research/corpus/fund_form.py`:
   - in `gather_items`, after the rows are read and sorted: SKIP a row whose (`security_key`, `report_id`) is listed in `typed.MISFILED_REPORTS` (match BOTH keys; read how `typed.reports_for` and `typed.MISFILED_REPORTS` name the fields); for every other row, if the key `fund_relation` is MISSING from the row, RAISE `ValueError` naming the security key and report id (a value must carry its claim: a silent zero would write empty forms); otherwise the item's fund is `row.get("fund")` when `row["fund_relation"] == "holding"` and `None` otherwise. Do not change the item tuple's shape or the extraction read;
   - `METHOD_VERSION` from `"1"` to `"2"` (the rule changed; the object name hashes it and `substrate._fund_form_member` picks a stored form by it);
   - update the module docstring (two or three ASCII sentences: `AMENDED round 92 (CTO round-91 analysis item 2, row D1-S46): a fund form counts only the reports whose silver row states fund_relation == holding; a misfiled report is never counted; a row without fund_relation raises.`) and the docstring of `absent_fund_reports` (it now also counts reports that name a fund without stating a holding);
   - change nothing else in the file.
b. New test `lib/research/corpus/tests/test_fund_form_holding_only.py`, offline; copy the fake client and the row fixtures from `tests/test_fund_form.py` (read it first; change it only as in c). Arms: (1) a report whose row states `fund_relation: "candidate"` is NOT in its named fund's form and is counted by `absent_fund_reports`, a `holding` one is; (2) the three reports of relation `none` with a fund (a bare-token fallback) are dropped the same way; (3) a row listed in `typed.MISFILED_REPORTS` (use the first entry's security key and report id) is not in any form, and a row with the same report id under ANOTHER security key is kept; (4) a row without the key `fund_relation` raises `ValueError` naming it; (5) a fund whose every report is a candidate is not in `distinct_funds` (no empty form); (6) `METHOD_VERSION == "2"` and the object name for one fixed input set differs from the one under `"1"`; (7) **A MUTANT:** with the holding test monkeypatched to accept every relation, arm (1) FAILS (assert that it does).
c. In `lib/research/corpus/tests/test_fund_form.py` and any other existing test of the AC2 list that fails because its silver fixture rows have no `fund_relation` or because it asserts `METHOD_VERSION == "1"`: add `"fund_relation": "holding"` to the fixture rows and change the version expectation, and NOTHING else in those files.
d. **The census (read-only).** Write `cf3_census.py` in your deliverables folder and run it once in the FOREGROUND with `python -u`, stdout to `cf3_census.out`. It reads the silver and the extractions as `gather_items` does (once), and applies TWO rules to the same fetched inputs: the BASELINE rule is `fund_form.py` as it is at commit `a9aecdd593` (`git show a9aecdd593:lib/research/corpus/fund_form.py` loaded as a second module under another name; pinned, never `HEAD`), and the NEW rule is your changed module. Output: per fund seen by either rule, `FUND <fund> reports_before=<n> reports_after=<n>` (the `build(...)` `fields.reports`); then `DROPPED <security_key> <report_id> <class> fund=<f> relation=<r>` for every A/B/C/D report counted before and not after; then exactly `CENSUS-FUND-FORM funds=<n funds with a form after> reports_before=<n> reports_after=<n> dropped_nonholding=<n> dropped_misfiled=<n> absent_before=<n> absent_after=<n> gets=<n> bytes=<n>`. **The issuer expects `funds=2 reports_after=115 dropped_nonholding=22`** (IDVZ 82, PFOE 33) and `dropped_misfiled` equal to the number of listed misfiled reports of class A to D that name a fund. **If a count differs, DO NOT edit the expectation or the code to match: print the actual lines, add a row, and report.**
e. Do not run `fund_form.write`, `_run_write`, `gold_put` or any gold or silver writer with a real client. A surprise is a row; keep working.

<paths>
lib/research/corpus/fund_form.py
lib/research/corpus/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~164/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cf-3"><invocation>python -m pytest lib/research/corpus/tests/test_fund_form_holding_only.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cf-3"><invocation>python -m pytest lib/research/corpus/tests/test_fund_form.py lib/research/corpus/tests/test_substrate.py lib/research/corpus/tests/test_typed.py lib/research/corpus/tests/test_typed_misfiled_reports.py lib/research/corpus/tests/test_continuation_holding_stance.py lib/research/corpus/tests/test_fund_relation.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^80 passed in</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cf-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~164/cf3_census.out</invocation><expect>(?m)^CENSUS-FUND-FORM funds=2 reports_before=\d+ reports_after=115 dropped_nonholding=22 dropped_misfiled=\d+ absent_before=\d+ absent_after=\d+ gets=\d+ bytes=\d+$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-18 ~01:2xZ):** AC1 FAIL as expected (the new test file does not exist); AC2 PASS as expected (`80 passed in 1.01s` over the six files); AC3 FAIL as expected (`cat` of a file that does not exist). If your base count differs, say so with both counts and do not weaken the pattern.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W164-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~164/AMGT_HARVST.TO-HVST-cf-3.the-fund-form-counts-only-reports-that-state-a-holding.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cf-3.the-fund-form-counts-only-reports-that-state-a-holding` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cf-3.the-fund-form-counts-only-reports-that-state-a-holding.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO round-91 analysis (`ledger/ROUND_ANALYSIS.round91.md` @9bdb466396, msg 7773) item 2 ("fund_form counts holding reports only and drops the two misfiled Mexico reports; built on the new silver; rebuilt under its own pair; its dossier-build hazard holds: the code lands only together with newly written fund forms"); design note `ledger/ROUND92_PREP_FUND_FORM_CF3_DESIGN_20261018.md`. Decomposition section 122e.
- **THE SEQUENCING HAZARD, restated:** `substrate._fund_form_member` picks a stored form by `inputs` AND `METHOD_VERSION`; the moment this change is on a branch that RUNS a dossier build, every build finds no `v2` form until `HVST-cf-5` writes them. This cell MERGES the code (lib code is run from a worktree by an ordered seat; no schedule runs a dossier build, `HVST-ce-1` section (g)); no one runs a dossier build between the merge and `HVST-cf-5`. The pair of `cf-5` says so.
- **Two consequences named for the CTO:** (a) DIVZ gets NO `v2` form (no holding report names it); the `v1` DIVZ object stays stored, so `stored_funds()` still lists DIVZ and `read_latest("DIVZ")` raises `LookupError`; `_run_compare` iterates the stored funds and would fail on it (a CLI hazard, not a served one; the worker reports it, the cell does not fix it); (b) three IDVZ "reports" that came from a bare table token (`Fund IDVZ y/y`) leave the form: they were never a stated holding.
- Slot ~164, worktree `C:/dev/wk-harvst-164`, branch `wk-AMGT_HARVST-164`. Widen the sparse set at provision with `lib/research`, `.claude/agents`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922`, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~163`, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~161` and `infra/aws/ec2/opal-gateway/app` (the AC2 list reads the gateway file; its omission skipped a test in `cg-5`).
- **SENT:** with the round-92 recut.

**COMPLETE 2026-10-18T01:3xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** worker `0.9.0_WK_AMGT_HARVST~164` (worker, haiku, high), branch `wk-AMGT_HARVST-164`, feature `807907d445`, proof `c2392557c9`; merged `04be089e13` (safe-merge fast lane, index check 0 of 7). Diff read by this seat: `gather_items` skips a row listed in `typed.MISFILED_REPORTS` (both keys), raises `ValueError` for any other row without `fund_relation`, and gives an item the row's fund only when `fund_relation == "holding"` (None otherwise); `METHOD_VERSION` `"2"`; the docstrings; one fixture line in `test_fund_form.py` (`"fund_relation": "holding"`); 7 new offline arms with a mutant.
- **AC1 PASS:** `7 passed` (worker; re-run here). **AC2 PASS:** `80 passed` (re-run here). **AC3 PASS:** `CENSUS-FUND-FORM funds=2 reports_before=139 reports_after=115 dropped_nonholding=22 dropped_misfiled=2 absent_before=210 absent_after=232 gets=364 bytes=25629575` (the issuer's expectation `funds=2 reports_after=115 dropped_nonholding=22` held; **I re-ran `cf3_census.py` myself and its output is identical, line for line**): IDVZ 94 to 82 (the 94 includes the 2 misfiled), PFOE 43 to 33, DIVZ 2 to 0; the 22 non-holding drops are `candidate` 14, `initiate` 2, `interest` 2, `template` 1, `none` 3. Proof instance VALID rc 0 (re-run here).
- **Rows** `D1-W164-S1` (INERT) corrects a premise of MY order: it said the two misfiled Mexico reports are counted "in KMB's form"; a fund form is per FUND, and their silver rows carry fund `IDVZ` under security key `KMB_US_Equity`, so the baseline counts them in IDVZ (94 before, 92 without them); the cell's effect is unchanged (`dropped_misfiled=2`); `-S2` (INERT): the two misfiled silver rows carry no `fund_relation` key (the rewrite did not re-append them), so the exclusion before the key check is what stops a rebuild raising on them. Both read and accepted.
- **Named for `HVST-cf-5` and the CTO:** DIVZ gets no `v2` form (no holding report names it); the stored `v1` DIVZ object stays, so `read_latest("DIVZ")` raises `LookupError` and `_run_compare` iterates the stored funds; no dossier build may run between this merge and the `cf-5` write.
- **What this does NOT prove:** a written fund form or a dossier build that finds one (`HVST-cf-5`).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>92</round>
<workstream>FUNDFORM-CODE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
