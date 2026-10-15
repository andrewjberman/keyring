# AMGT_HARVST task order -- `HVST-cb-1` -- ROUND 87: THE HARVEST LIBRARY NO LONGER NAMES SITE Z AS THE BOX IT RUNS ON

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cb-1.the-library-no-longer-names-the-box-it-runs-on</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cb-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~143</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched, no installer change.
comp-iam: RUN at L5 -- LOCAL text edits and one test only. NO publisher host, NO Secrets Manager call, NO sign-in, NO browser, NO S3 call, NO collector or runner run, NO scheduled task.
comp-adversary: RUN at L5 -- the adversary is an edit that changes behaviour (a value in contracts.json that code reads), a test that cannot fail, and a sixth place that still names the box.
</preflight>

## 0. THE CELL

The harvest library was written to run on the site Z box. Andrew moved all harvest operations to dell1, and the library must say where it runs by DERIVATION, not by naming a box. Five text carriers and one test docstring in `lib/opal_data_harvest/` name "site Z" / "SiteZ" as the place it runs. This cell edits them. It is documentation and one unread contract label: no code path changes.

## 1. THE BUILD (LOCAL, about 15 product lines)

Work in your worktree. Change only the files named in `<paths>`. Make exactly these six edits and no others:
a. `lib/opal_data_harvest/README.md` line 3: the sentence `Canonical library for the `opal-data-harvest` publication collection on SiteZ.` becomes `Canonical library for the `opal-data-harvest` publication collection. It runs on the Windows box where its scheduled runner is registered (`install-cycle-schedule.ps1 -Plan` prints the task).` Nothing else in the README changes.
b. `lib/opal_data_harvest/requirements.txt` line 1: `# Versions exercised on SiteZ. Chrome itself is the installed headful channel.` becomes `# Versions exercised by the harvest runner. Chrome itself is the installed headful channel.`
c. `lib/opal_data_harvest/backfill_driver.py` line 1 (the module docstring's first line): `the site Z backfill driver` becomes `the backfill driver`. Nothing else in the file changes.
d. `lib/opal_data_harvest/tab_transport.py` line 39 (the `default_profile_root` docstring): `Site Z profile root, derived from` becomes `Profile root, derived from`. Nothing else changes.
e. `lib/opal_data_harvest/contracts.json` line 4: `"execution": "local-sitez",` becomes `"execution": "local-windows-box",`. No code reads this key (checked); the file must still parse as JSON.
f. `lib/opal_data_harvest/test_ae4_backfill_driver.py` line 1 (the module docstring): `the site Z backfill driver` becomes `the backfill driver`. Nothing else changes.
g. New test `lib/opal_data_harvest/test_cb1_no_site_name.py` (stdlib only; no network): (1) for each of the six files above, the text contains no match of the case-insensitive pattern `site ?z` (an exact `re.compile(r"site ?z", re.I)`); (2) a POSITIVE CONTROL in the same test file: that same pattern DOES match the strings `"the site Z backfill driver"` and `"SiteZ"`, so the check can fail; (3) `contracts.json` parses with `json.loads`, and its `"execution"` value is a non-empty string.
2. Do not run anything against a publisher, S3, Secrets Manager or any box; do not launch a browser; do not edit any other file. A surprise is a row; keep working.

<paths>
lib/opal_data_harvest/README.md
lib/opal_data_harvest/requirements.txt
lib/opal_data_harvest/backfill_driver.py
lib/opal_data_harvest/tab_transport.py
lib/opal_data_harvest/contracts.json
lib/opal_data_harvest/test_ae4_backfill_driver.py
lib/opal_data_harvest/test_cb1_no_site_name.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~143/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cb-1"><invocation>python -m pytest lib/opal_data_harvest/test_cb1_no_site_name.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cb-1"><invocation>python -m pytest lib/opal_data_harvest/test_ae4_backfill_driver.py lib/opal_data_harvest/test_catalog.py lib/opal_data_harvest/test_ca1_profile_renew.py lib/opal_data_harvest/test_bz9_refresh_once.py lib/opal_data_harvest/test_br2_cycle_runner.py lib/opal_data_harvest/test_ai2_ft_session.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^93 passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC2 reads exactly `93 passed`: the base's own count; the six files are all docstring, comment or label edits.
- **Dry-run at the base (issuer, dell1, 2026-10-15 ~19:1xZ):** AC1 base FAIL as expected (`no tests ran`: the file does not exist); AC2 base PASS as expected (`93 passed`).
- Before and after, run the full `lib/opal_data_harvest` suite and record both counts. One failure is known at the base on a clean main checkout (`test_bn1_names_made_whole.py::test_v_building_twice...`, CRLF against LF on disk); a sparse worktree may show more, so read the base count from your own worktree before you edit. Add none.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W143-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions.
  Its commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~143/AMGT_HARVST.TO-HVST-cb-1.the-library-no-longer-names-the-box-it-runs-on.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cb-1.the-library-no-longer-names-the-box-it-runs-on` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cb-1.the-library-no-longer-names-the-box-it-runs-on.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO `ROUND_ANALYSIS.round85.ADDENDUM_3_ALL_PUBLISHERS_TO_DELL1.md` (msg 6094) scope item "the repo carriers that name where harvest runs, which W1 finds and lists in the cut"; Andrew-direct 2026-10-15 ~16:3xZ (move all HARVEST operations to dell1; "update the repo as needed").
- **The list, with its denominator:** `comp-find -i 'site ?z|sitez|Opal Bloomberg' lib/opal_data_harvest --files` reads 7 hits across 143 files scanned; 6 of them are edited here; the 7th, `fixtures/challenges/bbg.provenance.json`, is a recorded fixture of a past capture (it names the box it was captured on) and is NOT edited. `contracts.json` `execution` is read by no code (Grep over `*.py`, `*.json`, `*.ps1`, `*.md`: one hit, the file itself).
- **Not in this cell, and whose they are:** `AMGT_HARVST_PRD.md` names site Z on 16 lines (Grep `site.?z|SiteZ|sitez`, case-insensitive, at the cut; its ENDPOINT DONE WHEN lines among them): ratified text, the CTO's edit and the CVO's re-sign, listed to the CTO in the round-87 message. Site Z's own runner, ledgers and the NFRA_OPLGTW records: site Z's. The historical `deliverables/0.7.0_AE_CloudOps~ZW/` records and the change-management entries are records of past acts and stay as written.
- Direct act: ONE cell, LOCAL, about 15 product lines; no L2, L4-R or L8-L10. Close: the merge through `safe-merge.sh` and the issuer's drain checks.
- Slot ~143, worktree `C:/dev/wk-harvst-143`, branch `wk-AMGT_HARVST-143`. Sparse set to widen at provision: `org/tier1_exec/4.0.0_SA_CRO/scripts` (AC2's tests read it).

**COMPLETE 2026-10-15 ~19:3xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** worker `0.9.0_WK_AMGT_HARVST~143` (worker-light, haiku, high), branch `wk-AMGT_HARVST-143`, head `537150ecee`, then this seat's fix `698eaad099`.
- **Defect found in review and repaired by the issuer:** the worker's `contracts.json` edit normalised the file's mixed line endings (base 120 CRLF + 16 LF) to CRLF, a 34-line diff for a one-line change. Rewritten from base bytes: 1 insertion, 1 deletion; `git diff --stat` over `lib/` now reads 6 one-line edits and the new test.
- **AC1 PASS:** `3 passed` (worker; this seat re-ran after the fix `3 passed in 0.05s`). **AC2 PASS:** `93 passed` (worker; this seat after the fix `93 passed in 2.45s`). Proof instance VALID rc 0 with `--governing-order`, re-run by this seat after the fix. Full suite per the worker: `845 passed, 1 failed (test_harvest_grammar, a sparse-worktree import), 3 skipped`, base `842 passed, 1 failed`.
- **Rows:** `D1-W143-S1` and `-S2` OBSERVATION / INERT; no action.
- **Not edited, by design:** `fixtures/challenges/bbg.provenance.json` (a recorded capture) and the PRD's 16 site Z lines (the CTO's).

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
<status>complete</status>
<round>87</round>
<workstream>CARRIERS</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
