# AMGT_HARVST task order -- `HVST-cd-1` -- ROUND 89, workstream S29-DOSSIER: A DOSSIER OR CONTINUATION FIELD THAT CITES A MISFILED REPORT IS NOT SERVED, AND IS NAMED (D1-S29 defect (b), rows D1-S38 and D1-S39; CTO round-88 analysis item 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cd-1.a-dossier-field-citing-a-misfiled-report-is-not-served</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cd-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~154</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and tests only. NO S3 call, NO AWS call, NO network, NO deploy, NO edit outside `<paths>`. The tests use the recording S3 fake the existing gateway tests use.
comp-adversary: RUN at L5 -- the adversary is a filter that drops a field citing a clean report (a field is excluded only when it cites a LISTED report of THIS security), a filter that reads one field shape and misses the other (the cited path can sit in `citation`, in `pack_shape` or anywhere in the entry), a control security that loses a field because a listed report id appears under a different security_key, and a test that passes whatever the code does.
</preflight>

## 0. THE CELL

The gateway tool `harvest_get_research(security_key)` (`infra/aws/ec2/opal-gateway/app/harvest_research.py`, function `_research`) already excludes two misfiled Kimberly-Clark de Mexico reports from KMB's `research_reports` list through the module constant `MISFILED_REPORTS` (a tuple of dicts with `security_key`, `report_id`, `reason`, `correct_security_key`; lines 172-211) and names them in the response key `misfiled_reports_excluded`. But the SAME response still serves two gold-dossier fields built from those reports. Measured on the live gateway 2026-10-17 (`KMB_US_Equity`): `dossier_fields` item `fund_of_record` = `"IDVZ"` and item `last_stated_position` = `{"fund":"IDVZ","size_pct":"2.25","text":"MAINTAIN 2.25% POSITION IN IDVZ"}`, each carrying a citation `report_key` of the form `.../research-report/security_key=KMB_US_Equity/fbd50086c4065785/Kimberly Clark Mexico Q2 2026 Earnings Update.docx`; another entry's `pack_shape` basis names `.../research-report/security_key=KMB_US_Equity/1a3b56044db679a5/Kimberly Clark Mexico Q2 2026 Earnings Update.pdf`; the `continuation_fields` carry the same two. So one response says the report is excluded and also serves the position it produced. The CTO ruled: **KMB's `fund_of_record` and `last_stated_position` exclude the reports on the `misfiled_reports` list, in both the dossier and the continuation; a field that cites an excluded report is not served and the exclusion is named.**

## 1. THE BUILD (LOCAL, about 60 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `infra/aws/ec2/opal-gateway/app/harvest_research.py`:
   - add a small pure helper (name it `_cited_misfiled(entry, key)`) that returns the `report_id` of the first listed report that the entry cites, else None. An entry cites the report when `json.dumps(entry, default=str)` contains the substring `security_key=<key>/<report_id>/` for a `MISFILED_REPORTS` entry whose `security_key` equals `key` (the substring is the segment the live citations carry; matching on the whole entry covers `citation`, `pack_shape` and any other place). A listed report id under a DIFFERENT security_key, or an unlisted report id, never matches;
   - in `_research`, after the dossier fields are selected (`sel = _select_fields(...)`) and before `_as_items`, drop every item of `sel` for which the helper returns a report id; do the same for the continuation fields (`cfields`). Record each dropped field in a new response key `misfiled_fields_excluded`, a list of `{"field": <name>, "part": "dossier" | "continuation", "report_id": <id>}`, present on EVERY response (`[]` when nothing is dropped; add it to the initial `body` dict next to `misfiled_reports_excluded`);
   - if the filter leaves the dossier (or continuation) with no field, record the absence through the existing `run.miss(...)` with a reason that says every field cites a misfiled report excluded from the security (see `misfiled_fields_excluded`); do not serve an empty list as if fields existed;
   - extend the existing `denominator_note` with a sentence only when something was dropped: `; %d dossier field(s) and %d continuation field(s) citing a misfiled report excluded from %s (see misfiled_fields_excluded)`. The `denominator` (the count of dossier fields read) stays what it is today;
   - change nothing else: the `MISFILED_REPORTS` constant, `_research_reports`, the budgets and every other key keep their present behaviour.
b. New test `infra/aws/ec2/opal-gateway/tests/test_cd1_dossier_misfiled.py`, offline, following the harness of `tests/test_cc2_research_misfiled.py` (read it first: its recording prefix-aware S3 fake, its principal stand-in, its audit recorder and the way it builds a dossier object; copy the helpers you need, edit nothing in that file). Use `KMB_US_Equity` with the two listed ids `fbd50086c4065785` and `1a3b56044db679a5`; every other name and value is synthetic. Arms:
   - (1) KMB: a dossier object with `fund_of_record` and `last_stated_position` whose citation `report_key` is `amgt/harvest/silver/research-report/security_key=KMB_US_Equity/fbd50086c4065785/x.docx`, one field whose `pack_shape` basis names `.../security_key=KMB_US_Equity/1a3b56044db679a5/x.pdf`, and one clean field citing `.../security_key=KMB_US_Equity/aaaa000000000001/x.docx`: the served `dossier_fields` holds only the clean field, and `misfiled_fields_excluded` names the three dropped fields with `part` `dossier` and their report ids;
   - (2) KMB continuation: the same two shapes in the continuation object are dropped and named with `part` `continuation`; a clean continuation field is kept;
   - (3) CONTROL: a synthetic security `TSTA_US_Equity` whose dossier fields cite `.../security_key=TSTA_US_Equity/fbd50086c4065785/x.docx` (a listed id under a DIFFERENT security) keeps every field and `misfiled_fields_excluded` is `[]`;
   - (4) a KMB field citing an unlisted report id is kept; `denominator` equals the number of dossier fields read (all of them, dropped or not); the `denominator_note` names the number dropped for KMB and says nothing of it for the control;
   - (5) **A MUTANT:** with `harvest_research.MISFILED_REPORTS` monkeypatched to `()`, arm (1) FAILS (assert that it does). It proves arm (1) discriminates.
c. Do not run anything against S3, AWS, a box or a browser; do not edit any other file. A surprise is a row; keep working.

<paths>
infra/aws/ec2/opal-gateway/app/harvest_research.py
infra/aws/ec2/opal-gateway/tests/test_cd1_dossier_misfiled.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~154/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cd-1"><invocation>bash infra/aws/ec2/opal-gateway/tests/run_release_suites.sh tests/test_cd1_dossier_misfiled.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cd-1"><invocation>bash infra/aws/ec2/opal-gateway/tests/run_release_suites.sh tests/test_cc1_model_basis.py tests/test_cc2_research_misfiled.py tests/test_cc3_ticker_shaped_never_exact_on_name.py tests/test_og_gt1.py tests/test_og_gt3.py tests/test_og_gt4.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^33 passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-17 ~12:0xZ):** AC1 FAIL as expected (the new test file does not exist: `ERROR: file or directory not found`, `no tests ran`); AC2 PASS as expected (`33 passed in 2.41s`). If your worktree's base count differs, say so with both counts and do not weaken the pattern.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W154-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~154/AMGT_HARVST.TO-HVST-cd-1.a-dossier-field-citing-a-misfiled-report-is-not-served.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cd-1.a-dossier-field-citing-a-misfiled-report-is-not-served` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cd-1.a-dossier-field-citing-a-misfiled-report-is-not-served.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO round-88 analysis (`ledger/ROUND_ANALYSIS.round88.md` @07264722d8, msg 7491) enrichment item 1 (S29 (b), cell 0a); rows `D1-S38` (SC1) and `D1-S39` (the CRO caller read, msg 7066); the CVO's grade on the live gateway (`ADJUDICATION_v82.md`): S29 (b) NOT fixed, S29 stays OPEN. Close condition: the live gateway read for KMB cites no `fbd50086c4065785`, with a control name unaffected; that read is `HVST-cd-2`'s, under its own never-widen pair.
- **Design choice, named:** a field is dropped whole when ANY string in its entry names a listed report of this security; a field built from one clean and one misfiled report is lost with it (the exclusion is all-or-nothing, said in the `denominator_note` sentence and in `misfiled_fields_excluded`). A silver/gold REBUILD that re-derives the dossier without the misfiled report is the true remedy and is not cut here; the CTO's item reads "exclude", and this cell does that on the served side. The substring `security_key=<key>/<report_id>/` is the segment the live citations carry (read from `cc7_served.out` line 29).
- **Class (gate, spine v3.19 L6):** `<paths>` names `infra/aws/ec2/opal-gateway/app/...`, an infrastructure path, so the floor is WORLD (as for `cc-1` to `cc-3`). The worker's acts stay LOCAL; the deploy is `HVST-cd-2`.
- Slot ~154, worktree `C:/dev/wk-harvst-154`, branch `wk-AMGT_HARVST-154`. Widen the sparse set at provision with `infra/aws/ec2/opal-gateway`, `org/tier1_exec/4.0.0_SA_CRO/scripts` and `.claude/agents` (rows `D1-W150-S1`, `D1-W152-S1`, `D1-W153-S1`: the cone left out the standing-rules file).
- **SENT:** with the round-89 issuance.

**COMPLETE 2026-10-17T12:1xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** worker `0.9.0_WK_AMGT_HARVST~154` (worker, haiku, high), branch `wk-AMGT_HARVST-154`, build `4a6a63f12c`, head `5393ddb851`, merged `9784d58e12` (safe-merge fast lane, index check 0 of 3 paths differ). Diff read by this seat: `harvest_research.py` (+45/-4): `_cited_misfiled` (the whole entry's JSON carries `security_key=<key>/<report_id>/` for a listed report of the same key) and `_drop_misfiled`; `_research` drops matching dossier and continuation fields, records them in `misfiled_fields_excluded` (present on every response, `[]` by default), says in `run.miss` when every field of a part is dropped, and adds the count sentence to `denominator_note` only when something is dropped; `denominator` unchanged.
- **AC1 PASS:** `5 passed` (worker; this seat re-ran in the worktree). **AC2 PASS:** `33 passed` (worker; re-run here, base count 33). Proof instance VALID rc 0 (re-run here). The mutant arm (`MISFILED_REPORTS = ()`) fails arm 1 as asserted. No surprise row filed.
- **What this does NOT prove:** the served tool. The code is merged, not deployed; the served KMB read with a control name is `HVST-cd-2`.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>89</round>
<workstream>S29-DOSSIER</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
