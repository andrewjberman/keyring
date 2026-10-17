# AMGT_HARVST task order -- `HVST-ce-6` -- ROUND 90, workstream S43-EXCLUDE: THE CORPUS LIBRARY READS NO REPORT THAT THE MISFILED LIST EXCLUDES, SO A REBUILD OF KMB'S GOLD OBJECTS DOES NOT ADMIT THE TWO MEXICO REPORTS (worker row D1-W155-S2; CTO round-89 analysis item 3; measured by HVST-ce-1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ce-6.the-corpus-reads-no-report-on-the-misfiled-list</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ce-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~158</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and offline tests only. NO S3 call, NO AWS call, NO network, NO deploy, NO gold writer RUN (`write_one`, `--write` and `production_sequence` are NEVER run), NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is an exclusion list that exists twice and drifts (the gateway's and the library's), an exclusion keyed on report_id alone (a report id under ANOTHER security must still be read), an exclusion applied in one consumer of `reports_for` but not the others, and a test that passes whatever the code does.
</preflight>

## 0. THE CELL

The gateway excludes two misfiled Kimberly-Clark de Mexico reports from `KMB_US_Equity` through `MISFILED_REPORTS` in `infra/aws/ec2/opal-gateway/app/harvest_research.py` (read its definition and `_validate_misfiled`: entries `{security_key, report_id, reason, correct_security_key}`; today two entries, both `security_key` `KMB_US_Equity`, `report_id` `fbd50086c4065785` and `1a3b56044db679a5`). The library that BUILDS the gold dossier and continuation objects does not know this list: `lib/research/corpus/typed.py::reports_for(security_key, client=None)` (line 576) returns every silver row of the security, and its callers (`continuation.py` line 871, `report_input.py` line 57, `substrate.py` lines 185 and 228, `typed.py` line 761) feed those rows to the builders. Measured by `HVST-ce-1` (`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~155/ce1_measure.out` section (g)): a rebuild of KMB's gold objects today would read the two Mexico reports again, so a rebuilt dossier would cite them. This cell gives the library the list so that a rebuild does not.

## 1. THE BUILD (LOCAL, about 60 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `lib/research/corpus/typed.py` add a module constant `MISFILED_REPORTS`, a tuple of dicts with the keys `security_key`, `report_id` and `reason`, holding exactly the two entries of the gateway constant (same ids, same `reason` text, same `security_key`; the library does not need `correct_security_key`). Place it with the other module constants; ASCII only.
b. In `reports_for`, drop every row whose `(security_key, report_id)` equals a listed pair BEFORE ordering. A row with a listed `report_id` under a DIFFERENT `security_key` is NOT dropped; a row of the same `security_key` with an unlisted `report_id` is NOT dropped. Change nothing else in the function and nothing in `typed.py`'s other functions.
c. New test `lib/research/corpus/tests/test_typed_misfiled_reports.py`, offline, following the harness of `lib/research/corpus/tests/test_typed.py` (read it first, especially the arm around line 202 that calls `reports_for("ACME_US_Equity", client=object())`: how it fakes `store.silver_latest`; copy what you need, edit nothing in that file). Arms:
   - (1) a fake silver table with `KMB_US_Equity` rows `fbd50086c4065785`, `1a3b56044db679a5` and two others, and an `ACME_US_Equity` row: `reports_for("KMB_US_Equity")` returns only the two others, in the same order as before;
   - (2) CONTROL: a row with report id `fbd50086c4065785` under `ACME_US_Equity` is returned by `reports_for("ACME_US_Equity")`;
   - (3) every consumer sees it: `continuation._read_reports_with_bytes` (line 863), `report_input` and `substrate` (lines named above) all call `typed.reports_for`; assert by reading their source text with `inspect.getsource` that none of them reads the silver table by another route (the pattern `silver_latest(` does not appear in those three modules outside a comment), so the one filter covers them; if one of them DOES read silver by another route, say so in a surprise row and cover it with the same exclusion;
   - (4) NO DRIFT: read the text of `infra/aws/ec2/opal-gateway/app/harvest_research.py` (open the file by path from the repo root, do not import it), extract every `"report_id": "<16 hex>"` of its `MISFILED_REPORTS` block, and assert the set equals the set of `report_id`s in `typed.MISFILED_REPORTS`; skip the arm with a clear message if the gateway file is absent from a sparse checkout (`pytest.skip`), and say in your report whether it ran;
   - (5) **A MUTANT:** with `typed.MISFILED_REPORTS` monkeypatched to `()`, arm (1) FAILS (assert that it does).
d. Do not run any gold writer or S3 call; do not edit any other file. A surprise is a row; keep working.

<paths>
lib/research/corpus/typed.py
lib/research/corpus/tests/test_typed_misfiled_reports.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~158/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ce-6"><invocation>python -m pytest lib/research/corpus/tests/test_typed_misfiled_reports.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ce-6"><invocation>python -m pytest lib/research/corpus/tests/test_typed.py lib/research/corpus/tests/test_library.py lib/research/corpus/tests/test_substrate.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^35 passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-17 ~16:0xZ):** AC1 FAIL as expected (the new test file does not exist); AC2 PASS as expected (`35 passed in 0.94s`). If your worktree's base count differs, say so with both counts and do not weaken the pattern.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W158-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~158/AMGT_HARVST.TO-HVST-ce-6.the-corpus-reads-no-report-on-the-misfiled-list.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ce-6.the-corpus-reads-no-report-on-the-misfiled-list` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ce-6.the-corpus-reads-no-report-on-the-misfiled-list.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO round-89 analysis (`ledger/ROUND_ANALYSIS.round89.md` @fa28a5790e, msg 7642) item 3 ("rebuild KMB's dossier from the reports that remain after the exclusions"); `HVST-ce-1` `REBUILD_NEEDS_EXCLUSION_INPUT=yes`; worker row `D1-W155-S2` (ARMED, disarm owner me: this cell disarms it when merged and the rebuild order reads it).
- **Two copies of one list, named:** the gateway's and the library's cannot share a module (the gateway tree is deployed alone), so arm (4) is a drift test that reads the gateway file as text. A later cell may make the gateway read a shipped data file; not this one.
- **The rebuild itself is `HVST-ce-4`** (a seat order: a data write on the harvest bucket, under its own never-widen pair). The continuation's input hash changes when its reports change, so KMB's rebuild writes a NEW object beside the old one (the gold writer never overwrites).
- **Class:** the gate decides; the first commit attempt declares LOCAL (`lib/` is not an infra path).
- Slot ~158, worktree `C:/dev/wk-harvst-158`, branch `wk-AMGT_HARVST-158`. Widen the sparse set at provision with `lib/research`, `infra/aws/ec2/opal-gateway/app` and `.claude/agents`.
- **SENT:** with the round-90 recut.

**COMPLETE 2026-10-17T16:3xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** worker `0.9.0_WK_AMGT_HARVST~158` (worker, haiku, high), branch `wk-AMGT_HARVST-158`, commits `c847c0c723`, `5dd4d6532f`, `9c007fb94c`, merged `87b542aed4` (safe-merge fast lane, index check 0 of 4 paths differ); worktree and branch removed. Diff read by this seat: `typed.py` (+19/-1): `MISFILED_REPORTS` (the gateway's two entries, key and id and reason) and `reports_for` drops a row only when BOTH `security_key` and `report_id` match; a new five-arm test.
- **AC1 PASS:** `5 passed` (worker; re-run here, arm (4) the no-drift arm RAN). **AC2:** the worker read FAIL (`5 failed, 30 passed`): the five failures were `FileNotFoundError` on `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922/research_docx_kpi_census.json`, which this seat's provisioning left out of the sparse checkout (row `D1-W158-S1`, INERT: an issuer defect, not a code defect). With the folder added to the sparse set this seat re-ran AC2: `35 passed` (the base count). Proof instance VALID rc 0 (re-run here).
- **Rows** `D1-W158-S1` (INERT, the sparse omission above), `-S2` (ARMED, disarm owner this seat) and `-S3` (INERT). **`-S2`:** `fund_form.py::gather_items` (line 249) and `sector_template.py::_all_rows` (line 446) read silver through `store.silver_latest`, not `reports_for`, so the exclusion does not reach them. Read by this seat: `fund_form.gather_items` builds ONE corpus-wide form from every silver row (not a per-security read); `sector_template` reads xlsx rows only for its business types, and the two Mexico reports are a docx and a pdf. So KMB's per-security reads (continuation, dossier substrate, report input) are covered; the corpus-wide `fund_form` object still counts the two reports. That is a named LIMIT, not a KMB served field, and a candidate for round 91; the issuer dispositions `-S2` with it recorded.
- **What this does NOT prove:** a rebuilt KMB object (`HVST-ce-4`).

**REOPENED 2026-10-17T19:5xZ (issuer `2.0.0_SA_COO~W1`) to `in_progress` for ONE act:** the proof instance still records the worker's AC2 FAIL, which was the issuer's own sparse-checkout omission (row `D1-W158-S1`); `round-close-check --round 90` reads REFUSED on that row. The worker `0.9.0_WK_AMGT_HARVST~158` re-runs AC2 in a complete checkout and regrades its own instance (the issuer's lane is not admitted to a worker's deliverables folder, and a terminal order grants the worker nothing). The merged code is unchanged and the issuer's re-run on the merged tree read `35 passed`.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>in_progress</status>
<round>90</round>
<workstream>S43-EXCLUDE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
