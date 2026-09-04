# TO ETFS_GUARDRAIL.TO-EG-s-6 -- the pre-publish gate INSIDE the renderer: the month cannot go out over real holes unless a person decides; the ladder runs first; the refusal is visible on the existing topic; the ONE renderer artifact upload to the reporter box

<to_id>ETFS_GUARDRAIL.TO-EG-s-6</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-04</issued_date>
<status>pending -- GO paired at cut (the spawn IS the GO); HANDED to the slot only after EG-s-1, EG-s-2 (your own), EG-s-4, EG-s-7, EG-sb-7 (slot 1) and EG-s-13 (slot 3) are terminal with VALID instances at HEAD -- it uploads the ONE merged renderer. Authority: PRD v0.3 @`4e30d6b635` (flat lineage @`7aa1554881`, ON ORIGIN) RATIFIED; decomposition v0.1 @`c4ab429993`, v0.1.1 in this issuance; Andrew-direct 2026-09-01 ("yes do all of the above") and 2026-09-04 ~17:0xZ (94224/94225).</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.3 (s.7.2 row S6; s.7.4 "S6 gate -> INSIDE render_month_end.py, NOT the orchestrator"; s.1 "Catch-up BEFORE the gate"; s.4 properties 3 and 5; brief s.4) | **Decomp cell:** `EG-s-6` | **outcome_ref:** FWD-2 | **verb:** wire | **depends_on:** `EG-s-1`, `EG-s-2`, `EG-s-4` (and, for the upload, every other renderer/coverage cell)

---

## THE CELL

`EG-s-6` (PRD s.7.2 S6): NEW precondition INSIDE `render_month_end.py`. Bound: *"NOT a standing service. Catch-up before gate."* RULED (s.7.4): *"inside the renderer. Putting the gate in the Lambda would require the classifier on BOTH sides of the repo/Lambda boundary -- which is exactly how S10 happened. The orchestrator gates only the SEND, on the verdict the renderer returns."* Property 3: *"Run against August 2026 as it stood before the 09-01 repair, the gate refuses and names exactly five real holes. Run against August as it stands now, it publishes."* Property 5: *"On a refusal, no report is sent, and the refusal is visible on the existing topic."* FWD-2 DONE WHEN: *"EXERCISED -- the check has actually refused a month, and the refusal reached a person."*

**The seam, so the orchestrator needs no gate of its own (read `_run` at `lambda_function.py:281-333`):** the orchestrator runs the renderer over SSM on the reporter box (`_render_command`, `:107-130`: pulls `render_month_end.py` from `ARTIFACT_PREFIX = s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/`, runs `python3 render_month_end.py --month <m> --pdf --s3-out s3://opal-data-etfs/platinum/reports/`), then checks SSM `Status == Success` and `_report_exists(month)` (`platinum/reports/<m>/etf_ownership.pdf`), and ONLY then `_email_report`. So: **a REFUSE that exits non-zero and does NOT write `etf_ownership.pdf` at the publish key already produces "no send" and an alert on the EXISTING `REPORTS_SNS_TOPIC`** (`_alert` at `:79-87`, the "render FAILED" or "SUCCESS but NO report object" branch). `EG-s-8` (slot 1) enriches that alert's text with the verdict and the egress ask; this order produces the artifacts it reads.

**What you build:**
1. In `render_month_end.py` `main()`, BEFORE the PDF and the upload, when `--gate` is given (the orchestrator's `_render_command` will pass it once `EG-s-8` lands; locally you pass it): `verdict = coverage_gate(month, partners, daily, universe, ladder=not args.no_ladder, probe=<the producers' probe via lambda invoke>, fixture_remove=args.fixture_remove)` -> per partner: `classify_month` (probe injected: `boto3 lambda.invoke(<producer>, {"date": d, "probe": true})` parsed into the probe's shape; where a producer answers with a written slice instead (probe mode not deployed), treat as UNKNOWN), then `remediate_month` (rungs 0-2; rung 3 writes the ask -- `EG-sb-7`), then re-classify; VERDICT `PUBLISH` iff class C == 0 for every partner (B and D are REPORTED in the verdict artifact, never swallowed); write `platinum/reports/<m>/coverage_verdict.json` ALWAYS (`{"month","verdict","per_partner":{p:{summary, coverage_line, holes:[...]}},"generated_at"}`) and `coverage_unresolved.json` only when unresolved days remain; on REFUSE: print `VERDICT: REFUSE holes=<n> ...`, upload the HTML (and the CSVs, with their coverage rows) under `platinum/reports/<m>/refused/` so a person can read what was refused, write NO `etf_ownership.pdf` at the publish key, and `sys.exit(3)`; on PUBLISH: print `VERDICT: PUBLISH holes=0 ...` and continue exactly as today. `--no-ladder` skips rungs (QA runs, so the QA never invokes a producer); `--fixture-remove <partner>:<date>,<date>...` removes those slices from the loaded series IN MEMORY (the pre-repair August fixture; nothing on S3 is touched).
2. The renderer's SELF-BOOTSTRAP for the box: at import time, if `coverage` is not importable, `aws s3 cp --recursive s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/coverage/ ./coverage/` (the box role holds `PullRendererArtifact` + `ListRendererArtifactPrefix` on that prefix, `iam.tf:53-67`), then import. The orchestrator's `_render_command` is NOT edited by this order.
3. THE ONE ARTIFACT UPLOAD (the deploy of the renderer to the box's prefix), after every renderer/coverage cell is merged at HEAD: read `docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md` first; open the ledger entry `etfs-guardrail-eg-s-6-renderer-artifact-upload` (`--leg "s3-code|activation|ec2/etfs-reports/render_month_end.py|s3api head-object ETag equals local md5 and the coverage/ prefix lists __init__.py classifier.py remediate.py trading_calendar.py _orion_vendor_asof.py"`); `.tools/aws s3 cp` `render_month_end.py`, the coverage package's committed files (`__init__.py`, `classifier.py`, `remediate.py`) AND two BUILD-TIME copies that are never committed anywhere -- `lib/trading_calendar.py` -> `.../coverage/trading_calendar.py` and `data/inf/scripts/silver/_orion_vendor_asof.py` -> `.../coverage/_orion_vendor_asof.py` (the layer pattern: copy from the canonical source at deploy time, commit nothing; CTO~Z ruling @1da1e2b73b, row ETFS_GUARDRAIL-W1-S1) -- to `s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/` and `.../coverage/`; verify by `s3api head-object` (ETag = md5 for single-part) against the local files; close the leg with that proof; close the entry; entry + sentinel COMMITTED. The scheduled 10-01 fire is then the EXERCISED read.
4. `data/etfs/scripts/presentation/tests/test_coverage_gate.py` -- ZERO AWS calls (stubs); arms: (a) five removed cottonwood days with a probe answering present+priced and `ladder=False` -> REFUSE, `holes == 5`, the five dates named; (b) all present -> PUBLISH; (c) a B day (probe priced 0) -> PUBLISH with `expected_empty == 1`, no invoke; (d) REFUSE writes the verdict artifact and NOT the publish key (assert on the stub s3's put keys); (e) the coverage line is present in the refused HTML; (f) `--no-ladder` makes zero invokes.
5. `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/the-pre-publish-gate-inside-the-renderer.result.md` -- criteria verbatim with rc and denominators; the upload's head-object proof; the ledger entry's path.

## ACCEPTANCE

<criterion id="S6-AC1" cell_refs="EG-s-6"><invocation>python -m pytest data/etfs/scripts/presentation/tests/test_coverage_gate.py -q</invocation><expect>passed</expect></criterion>
`S6-AC1` -- the six-arm battery is green (record N passed).

<criterion id="S6-AC2" cell_refs="EG-s-6"><invocation>python data/etfs/scripts/presentation/render_month_end.py --month 2026-08 --out .scratch/eg_s6_pre_repair.html --gate --no-ladder --fixture-remove cottonwood:2026-08-04,2026-08-18,2026-08-20,2026-08-21,2026-08-31; echo rc=$?</invocation><expect>VERDICT: REFUSE holes=5</expect></criterion>
`S6-AC2` -- property 3, first half: August 2026 AS IT STOOD BEFORE THE 09-01 REPAIR (the five real holes removed in memory) is REFUSED and exactly five holes are named (the probe here answers from the deployed producers' probe mode for those five dates; record `rc=3` beside the line).

<criterion id="S6-AC3" cell_refs="EG-s-6"><invocation>python data/etfs/scripts/presentation/render_month_end.py --month 2026-08 --out .scratch/eg_s6_now.html --gate --no-ladder; echo rc=$?</invocation><expect>VERDICT: PUBLISH</expect></criterion>
`S6-AC3` -- property 3, second half: August as it stands now PUBLISHES (`rc=0`; no `--s3-out`, so nothing is uploaded by this QA run).

<criterion id="S6-AC4" cell_refs="EG-s-6"><invocation>python -c "h=open('.scratch/eg_s6_pre_repair.html',encoding='utf-8').read(); print('COVERAGE_LINES_ON_REFUSE=%d' % h.count('trading days;'))"</invocation><expect>COVERAGE_LINES_ON_REFUSE=3</expect></criterion>
`S6-AC4` -- the refused deck still carries every partner's coverage line (property 6 on the REFUSE path).

<criterion id="S6-AC5" cell_refs="EG-s-6"><invocation>bash .tools/commit-gate.sh data/etfs/scripts/presentation/render_month_end.py data/etfs/scripts/presentation/tests/test_coverage_gate.py</invocation><expect>pre-commit gate clean</expect></criterion>
`S6-AC5` -- the commit gate is clean.

<criterion id="S6-AC6" cell_refs="EG-s-6"><invocation>python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/renderer_artifact_served_vs_local.py</invocation><expect>VERDICT: MATCH 6 of 6</expect></criterion>
`S6-AC6` -- the uploaded artifacts (the renderer + the three committed package files + the two build-time copies taken from `lib/` and `data/inf/scripts/silver/`) match their local sources by `head-object` ETag/md5, 6 of 6; your script prints each pair and one verdict line.

<criterion id="S6-AC7" cell_refs="EG-s-6"><invocation>.tools/aws s3api list-objects-v2 --bucket opal-313476888478-lambda-artifacts --prefix ec2/etfs-reports/coverage/ --query "Contents[].Key" --output text</invocation><expect>ec2/etfs-reports/coverage/classifier.py</expect></criterion>
`S6-AC7` -- the coverage package is at the box's pull prefix.

<criterion id="S6-AC8" cell_refs="EG-s-6" judgment="true"/>
`S6-AC8` -- graded by the CVO at L9: the gate is a render precondition and not a standing service; catch-up runs before the gate (the ports landed first; the ladder runs inside it); a REFUSE writes no report at the publish key and surfaces on the existing topic through the orchestrator's existing branches; B is never a hole; FWD-2's EXERCISED grade ("has actually refused a month, and the refusal reached a person") is a real refusal on a scheduled fire, which this order rehearses on a fixture and does not manufacture. RECORD; NO VERDICT.

<expected_criteria>S6-AC1, S6-AC2, S6-AC3, S6-AC4, S6-AC5, S6-AC6, S6-AC7, S6-AC8</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry -- your own `deliverables/<serial>/` folder, and THIS ORDER'S OWN FILE under `task-orders/` (lane ANY) for the `<status>` flip -- and nothing else.** (Restated by the issuer at the drain on row ETFS_GUARDRAIL-W1-S2: the flip was always admitted; the wording withheld it.) A path you need that it does not name is a BLOCKING row, never an override. The orchestrator (`EG-s-8`), the coverage package (`EG-s-4`/`EG-s-7`) and the producers are other cells: you IMPORT and INVOKE, you do not edit them.
- **No fabrication:** the gate writes verdict/unresolved/ask artifacts and the refused HTML; it never writes a slice or a number. `--fixture-remove` changes memory, never S3.
- **No probe in the QA runs beyond the deployed producers' probe mode** (writes nothing); `--no-ladder` on every QA run so no producer is re-run by a test. The live ladder runs on the scheduled fire.
- **NO SERVED DELETE.** Never delete anything under `platinum/reports/` or `daily/`.
- **NEVER-2 for the upload:** ledger entry before, proof after, committed; `.tools/aws` shim only; overwrite the prefix's files, delete nothing.
- **No new monitor, alarm, topic or schedule.** The refusal rides the existing topic through the existing orchestrator branches.
- **EVERY invocation is bounded.** `timeout 120`; the gated August render with five probe invokes should fit; if it does not, retry once and record.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W2-S<k>`.
- **NEVER `git push`.** Report push state as MEASURED.

<paths>
data/etfs/scripts/presentation/
data/etfs/scripts/coverage/
lib/trading_calendar.py
data/inf/scripts/silver/_orion_vendor_asof.py
docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.1 @`c4ab429993` (v0.1.1 in this issuance), cell `EG-s-6`.
<owned_cells>EG-s-6</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance (2026-09-04 18:0xZ) -- WITHIN BUDGET, 5 of 5 carriers scanned, reached denominators C1=21 C2=4 C3=12 C4=20 C5=336; 0 armed gates name ETFS_GUARDRAIL, the renderer or etfs-reports.
comp-iam: RUN at L5 on etfs-reports-orchestrator (16 calls / 9 statements) and read at source for the reporter instance role (iam.tf:24-67: ReadEtfsAggregation, ListEtfsAggregation, WriteReports on platinum/reports/*, PullRendererArtifact, ListRendererArtifactPrefix) -- this order changes no policy; the box's invoke grant is EG-s-7's; the artifact upload runs under the launching seat's credentials, stated.
comp-adversary: DECLARED-NOT-APPLICABLE -- a FRESH CUT with no prior artifact to validate against; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`); `data/etfs/scripts/coverage/` is named for READING and the bootstrap copy; the ledger directory and the sentinel are named so the NEVER-2 entry can be COMMITTED.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S6-AC1` .. `S6-AC8`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-6.the-pre-publish-gate-inside-the-renderer.proof_of_spec.json`
(AMENDED BY THE ISSUER at the drain on row ETFS_GUARDRAIL-W3-S2: the instance file is named by the TASK ORDER'S OWN BASENAME stem, which is what `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`; the short `to_id` form this face carried before would have refused every flip. ONE instance file, this name, no duplicate.),
validated with `python .tools/proof-of-spec-check.py <instance> S6-AC1,S6-AC2,S6-AC3,S6-AC4,S6-AC5,S6-AC6,S6-AC7,S6-AC8` BEFORE the complete flip, which the assignee commits itself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
