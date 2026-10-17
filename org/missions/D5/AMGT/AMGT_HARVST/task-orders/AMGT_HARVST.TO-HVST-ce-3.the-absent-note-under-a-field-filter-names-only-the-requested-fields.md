# AMGT_HARVST task order -- `HVST-ce-3` -- ROUND 90, workstream S29-WORDING: UNDER A FIELD FILTER, `parts_absent.dossier` NAMES ONLY THE REQUESTED FIELDS IT EXCLUDED (CTO round-89 analysis item 2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ce-3.the-absent-note-under-a-field-filter-names-only-the-requested-fields</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ce-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~157</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and offline tests only. NO S3 call, NO AWS call, NO network, NO deploy, NO edit outside `<paths>`. The tests use the recording S3 fake the existing gateway tests use.
comp-adversary: RUN at L5 -- the adversary is a wording that still says "every dossier field" when only requested fields were considered, a change that alters the no-filter wording the earlier test already pins, a change that touches the fields served, and a test that passes whatever the code does.
</preflight>

## 0. THE CELL

In `infra/aws/ec2/opal-gateway/app/harvest_research.py`, function `_research`, after `HVST-cd-1` the dossier branch reads: `sel = _select_fields(allf, fields, stamp)`, then `sel, dropped = _drop_misfiled(sel, key, "dossier")`, and when `sel` is left empty and `dropped` is not, it calls `run.miss("dossier", "every dossier field cites a misfiled report excluded from the security (see misfiled_fields_excluded)")`. With a `fields` argument, `sel` holds only the REQUESTED fields, so the sentence is wrong: only the requested fields were excluded, not every dossier field. The CTO's wording nit: **with a field filter, `parts_absent.dossier` names only the requested fields it excluded.**

## 1. THE BUILD (LOCAL, about 40 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `harvest_research.py`, in that one `run.miss("dossier", ...)` call: when the caller passed a non-empty `fields` argument, the reason reads `the requested dossier field(s) <comma-separated names, in the order requested> cite a misfiled report excluded from the security (see misfiled_fields_excluded)`, naming ONLY the requested fields that were dropped (the `dropped` entries of part `dossier`); when no `fields` argument is passed, the sentence stays EXACTLY as it is today. Change nothing else.
b. New test `infra/aws/ec2/opal-gateway/tests/test_ce3_parts_absent_wording.py`, offline, following the harness of `tests/test_cd1_dossier_misfiled.py` (read it first: its recording S3 fake, principal stand-in and audit recorder; copy the helpers you need, edit nothing in that file). Use `KMB_US_Equity` and the listed ids `fbd50086c4065785` and `1a3b56044db679a5`; every other name and value is synthetic. Arms:
   - (1) `fields=["fund_of_record"]` on a KMB dossier where `fund_of_record` cites `.../security_key=KMB_US_Equity/fbd50086c4065785/x.docx` and a clean field `company_name` exists: `dossier_fields` is absent and `parts_absent["dossier"]` names `fund_of_record`, says `requested`, and does NOT say `every dossier field`;
   - (2) `fields=["fund_of_record", "last_stated_position"]` both citing a listed report: the reason names both, in that order;
   - (3) NO FILTER, every dossier field cites a listed report: the reason is exactly the sentence of today (`every dossier field cites a misfiled report excluded from the security (see misfiled_fields_excluded)`);
   - (4) `fields=["company_name"]` (clean) on the same dossier: `dossier_fields` holds it and `parts_absent` has no `dossier` key; `misfiled_fields_excluded` is `[]`;
   - (5) **A MUTANT:** with the new wording replaced by the old sentence (monkeypatch is not possible on a literal: instead assert in a second test function that the string `every dossier field` does NOT appear in the reason of arm (1), and show it fails when run against the pre-change module loaded from `git show HEAD:infra/aws/ec2/opal-gateway/app/harvest_research.py` into a temporary module).
c. Do not run anything against S3, AWS, a box or a browser; do not edit any other file. A surprise is a row; keep working.

<paths>
infra/aws/ec2/opal-gateway/app/harvest_research.py
infra/aws/ec2/opal-gateway/tests/test_ce3_parts_absent_wording.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~157/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ce-3"><invocation>bash infra/aws/ec2/opal-gateway/tests/run_release_suites.sh tests/test_ce3_parts_absent_wording.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ce-3"><invocation>bash infra/aws/ec2/opal-gateway/tests/run_release_suites.sh tests/test_cd1_dossier_misfiled.py tests/test_cc1_model_basis.py tests/test_cc2_research_misfiled.py tests/test_cc3_ticker_shaped_never_exact_on_name.py tests/test_og_gt1.py tests/test_og_gt3.py tests/test_og_gt4.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^38 passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-17 ~16:0xZ):** AC1 FAIL as expected (the new test file does not exist: `no tests ran`); AC2 PASS as expected (`38 passed in 2.27s`). If your worktree's base count differs, say so with both counts and do not weaken the pattern.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W157-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~157/AMGT_HARVST.TO-HVST-ce-3.the-absent-note-under-a-field-filter-names-only-the-requested-fields.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ce-3.the-absent-note-under-a-field-filter-names-only-the-requested-fields` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ce-3.the-absent-note-under-a-field-filter-names-only-the-requested-fields.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO round-89 analysis (`ledger/ROUND_ANALYSIS.round89.md` @fa28a5790e, msg 7642) item 2 ("same cell as item 1 if it ships in the same release"). It is a CODE cell only: the lib fix (`HVST-ce-2`) takes effect through a gold rebuild and needs no gateway release, so this wording change would ride a gateway release of its own (`HVST-ce-5`, under its own never-widen pair, defined in decomposition section 120a); the issuer will batch it with any other gateway change that is due rather than restart the host for a wording alone.
- **Class (gate, spine v3.19 L6):** `<paths>` names `infra/aws/ec2/opal-gateway/app/...`, an infrastructure path, so the floor is WORLD (as for `cd-1`). The worker's acts stay LOCAL.
- Slot ~157, worktree `C:/dev/wk-harvst-157`, branch `wk-AMGT_HARVST-157`. Widen the sparse set at provision with `infra/aws/ec2/opal-gateway`, `org/tier1_exec/4.0.0_SA_CRO/scripts` and `.claude/agents`.
- **SENT:** with the round-90 recut.

<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>90</round>
<workstream>S29-WORDING</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
