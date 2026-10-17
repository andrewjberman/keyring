# AMGT_HARVST task order -- `HVST-cg-4` -- ROUND 92, workstream GATEWAY-FUNDREL: THE GATEWAY'S `research_reports[]` ENTRY GAINS THE FIELD `fund_relation` (code and offline tests only; the release is a later seat order) (row D1-S46; CTO round-91 analysis item 1 and msg 7775)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cg-4.the-gateway-research-report-entry-has-a-fund-relation-field</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cg-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~162</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and offline tests ONLY. No S3 call of any kind, no gateway call, no deploy, NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a change that serves the new field but drops or reorders an old one (the pinned-tuple arm), a test that passes with the field absent (the mutant arm), an old silver row without the key that raises instead of serving `None`, and a change that reaches a second place in the file.
</preflight>

## 0. THE CELL

The gateway tool `harvest_get_research` serves each silver `research-report` row as an entry made from a FIXED tuple of keys: `infra/aws/ec2/opal-gateway/app/harvest_research.py` line 60, `REPORT_FIELDS`, used at lines 288 and 292 as `rec = {f: row.get(f) for f in REPORT_FIELDS}` (then `rec["part"] = part`). The silver row is about to gain a key `fund_relation` (another cell), one of `holding`, `candidate`, `initiate`, `interest`, `template`, `unclassified`, `none`. Until the tuple names it, no gateway consumer sees it. **Add `"fund_relation"` to `REPORT_FIELDS`, immediately after `"fund_absent_reason"`, and change nothing else in the file.** A row written before the key exists has no `fund_relation`; `row.get` already serves it as `None`, which is correct and must stay (it is not a relation). This cell changes code and tests only; it deploys nothing.

## 1. THE BUILD (code and offline tests only; about 40 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `infra/aws/ec2/opal-gateway/app/harvest_research.py`: the tuple `REPORT_FIELDS` gains `"fund_relation"` right after `"fund_absent_reason"`. Nothing else in the file.
b. New test `infra/aws/ec2/opal-gateway/tests/test_cg4_report_fund_relation.py`, offline. Read `infra/aws/ec2/opal-gateway/tests/test_cc2_research_misfiled.py` first and copy its way of driving `_research_reports` (its fake run and its parquet-row fixtures); change nothing in it. Arms:
   - (1) a silver row carrying `fund_relation: "candidate"` is served with `fund_relation == "candidate"` in its `research_reports` entry, beside `fund`, `fund_evidence` and `fund_absent_reason` unchanged;
   - (2) a row WITHOUT the key (written before the field) is served with `fund_relation is None` and every other field exactly as before; the entry's key set is `set(REPORT_FIELDS) | {"part"}`;
   - (3) `REPORT_FIELDS` equals exactly `("report_id", "report_class", "class_evidence", "fund", "fund_evidence", "fund_absent_reason", "fund_relation", "period", "period_source", "period_evidence", "period_absent_reason", "author", "author_absent_reason")` (a pinned tuple: any other change fails);
   - (4) all seven values (`holding`, `candidate`, `initiate`, `interest`, `template`, `unclassified`, `none`) pass through unchanged, none renamed or dropped;
   - (5) **A MUTANT:** with `harvest_research.REPORT_FIELDS` monkeypatched to the tuple WITHOUT `"fund_relation"`, arm (1) FAILS (assert that it does).
c. Do not touch any other file; do not call the gateway or S3; do not deploy. A surprise is a row; keep working.

<paths>
infra/aws/ec2/opal-gateway/app/harvest_research.py
infra/aws/ec2/opal-gateway/tests/test_cg4_report_fund_relation.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~162/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cg-4"><invocation>python -m pytest infra/aws/ec2/opal-gateway/tests/test_cg4_report_fund_relation.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cg-4"><invocation>python -m pytest infra/aws/ec2/opal-gateway/tests/test_ce3_parts_absent_wording.py infra/aws/ec2/opal-gateway/tests/test_cd1_dossier_misfiled.py infra/aws/ec2/opal-gateway/tests/test_cc1_model_basis.py infra/aws/ec2/opal-gateway/tests/test_cc2_research_misfiled.py infra/aws/ec2/opal-gateway/tests/test_cc3_ticker_shaped_never_exact_on_name.py infra/aws/ec2/opal-gateway/tests/test_og_gt1.py infra/aws/ec2/opal-gateway/tests/test_og_gt3.py infra/aws/ec2/opal-gateway/tests/test_og_gt4.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^43 passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-17 ~23:2xZ):** AC1 FAIL as expected (the test file does not exist); AC2 PASS as expected (`43 passed in 2.82s` over the eight files). If your base count differs, say so with both counts and do not weaken the pattern.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W162-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~162/AMGT_HARVST.TO-HVST-cg-4.the-gateway-research-report-entry-has-a-fund-relation-field.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cg-4.the-gateway-research-report-entry-has-a-fund-relation-field` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cg-4.the-gateway-research-report-entry-has-a-fund-relation-field.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO msg 7775 (cut `cg-3`, the gateway release: `REPORT_FIELDS` gains `fund_relation`, the two `ce-3` files ride it, one release under its own pair, site Z told first, the stale-base guard on the live commit). This cell is the CODE half; the RELEASE (`HVST-cg-3`, a seat order for `0.7.0_AE_CloudOps~SC1`) is cut after the silver rewrite (`HVST-cg-2`) lands, so the field is never served empty (CTO order). Decomposition section 122a.
- **The release carries three commits' files** (the stale-base guard of `ledger/ROUND91_CARRIED_FOR_NEXT_GATEWAY_RELEASE.md` applies): this cell's two paths plus the two `ce-3` paths; `git diff --name-status <live> <release>` must list exactly those four.
- **Class WORLD by the path floor, not by the work:** the gate refuses `LOCAL` because `<paths>` names `infra/aws/ec2/opal-gateway/app/harvest_research.py` (spine v3.19 L6: an infrastructure path floors the class at WORLD). The cell deploys nothing; the deploy is `HVST-cg-3` under its own pair. **Its own workstream:** `GATEWAY-FUNDREL`, because `cg-1` already holds the issuance of workstream `SILVER-FUNDREL` for this round (one issuance per workstream and round, row `AMGT_RESAPP-Z-S154`).
- Parallel with `cg-1`: the write sets are disjoint (`lib/research/corpus` against `infra/aws/ec2/opal-gateway`).
- Slot ~162, worktree `C:/dev/wk-harvst-162`, branch `wk-AMGT_HARVST-162`. Widen the sparse set at provision with `infra/aws/ec2/opal-gateway`, `.claude/agents`.
- **SENT:** with the round-92 recut.

**COMPLETE 2026-10-17T23:5xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** worker `0.9.0_WK_AMGT_HARVST~162` (worker-light, haiku, high), branch `wk-AMGT_HARVST-162`, feature commit `4536e9ecb9`, proof `1653b599ea`; merged `290f2e9e6d` (safe-merge fast lane, index check 0 of 5). Diff read by this seat: `REPORT_FIELDS` gains `"fund_relation"` after `"fund_absent_reason"` (the tuple is rewrapped onto three lines, 2 insertions 1 deletion, nothing else in the file); the new test has five arms (served beside unchanged fund fields, a row without the key served `None`, the pinned tuple, all seven values, a mutant).
- **AC1 PASS:** `5 passed` (worker twice; re-run here on the merged tree). **AC2 PASS:** `43 passed` (re-run here). Proof instance VALID rc 0 (re-run here).
- **Declared exclusion, accepted:** the attached-entry path (line 292, `attached_from`) is not asserted for `fund_relation`; it uses the same `REPORT_FIELDS` tuple, so it carries the key by construction. A later test may cover it.
- **Row `D1-W162-S1` (ARMED, disarm owner this seat):** its claim (a CLOSED batch-4 ledger says a release was rolled back to `d3ae88be46`) is true of that ledger and is superseded: that rollback closed 2026-10-17 02:13Z, and `EC2_MANIFEST.json` since moved `d3ae88be46` to `9d5b71255` (01:53Z commit), `1753c741d9` (cd-2, 11:07Z) and `efcc8ae19f` (OG-ap-36, 13:43Z). The release `HVST-cg-3` is cut on the live commit read from the manifest, the instance and `/opt/opal-gateway/.deployed_commit`; the reflex hold on a commit of this cell was advisory. Dismissed by row `D1-S48`.
- **What this does NOT prove:** a served `fund_relation` (that is `HVST-cg-3`, after the silver rewrite).

<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<status>complete</status>
<round>92</round>
<workstream>GATEWAY-FUNDREL</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
