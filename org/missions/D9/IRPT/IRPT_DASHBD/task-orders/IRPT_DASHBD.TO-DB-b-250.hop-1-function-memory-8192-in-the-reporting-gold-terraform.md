# TO IRPT_DASHBD.TO-DB-b-250 -- the MEMORY of the hop-1 function (round 123, workstream B-49F): the reporting-gold function's `memory_size` goes from 3008 to 8192 MB in `lambda.tf` (the measured peak of one filled day is 4,025 MB, 49 percent of 8192 MB and under the 70 percent line), the timeout stays 900, nothing else changes; a one-line Terraform edit and a small facts record; nothing planned, applied or deployed

<to_id>IRPT_DASHBD.TO-DB-b-250</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~204</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>123</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 123 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-123 ANALYSIS (B-49F) section 2 ruling 1 and section 3 cell 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_123_20261015.md @1ffd4f5afb`: "B: raise the hop-1 function's memory to 8,192 MB, and keep one pass per day. The measured peak, 4,025 MB, is 49 percent of 8,192 MB: under the 70 percent line, with headroom for household growth. The hop-1 apply pair names: the three grants (round 121), `InvokeOwnFunctionOnly`, the split code hash and `memory_size = 8192`. The plan gate is 0 add / 2 change / 0 destroy") | **Rows:** IRPT_DASHBD-D2-W204-S<k> | **Decomp cell:** `DB-b-250` (decomposition section 121) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none

**Risk class WORLD** is the floor of the path below (an `infra/` path): this order edits one Terraform file and runs no Terraform command and no AWS call; the plan and the apply are another seat's act under a signed pair.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-204` (branch `wk-IRPT_DASHBD-204`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~204/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~204/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** Round 122 measured the hop-1 `filled_report_values` stage for one real day: the peak resident memory of the two reading functions is 4,024.6 MB (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~200/RD_STAGE_MEMORY_R122.json`), against the function's `memory_size = 3008`. The CTO ruled one pass per day and 8,192 MB (the Lambda ceiling is 10,240 MB). This cell makes the one edit so that the hop-1 apply pair can name it. The function's other settings, including `timeout = 900`, do not change.

**The cell (`DB-b-250`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r123/p123_mem8192.py` (your two criteria; the clauses and the facts record's exact form are in its docstring and clauses); `infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf` (the `memory_size` and `timeout` lines, and the comment at its head that says the memory is not changed: keep that comment true by editing it to say it was changed here, citing this order); round 122's record above.
2. **The edit** in `lambda.tf`: `memory_size = 8192` on the existing line; `timeout = 900` stays; update the file's header comment so that it no longer says the memory is unchanged and names this order and the measured numbers; nothing else. At most 3 existing lines may change, and at most 6 lines are added.
3. **The facts record** `RD_MEMORY_FACTS_R123.json` in your folder with EXACTLY these fields: `function` ("irpt-49f-reporting-gold-lambda"); `memory` {`from_mb` 3008, `to_mb` 8192, `lambda_limit_mb` 10240, `timeout_seconds` 900, `words`}; `headroom` {`measured_peak_mb` (read from round 122's record), `fraction_of_new_memory` (peak / 8192, four decimals), `line_fraction` (0.7), `under_line` (true), `words`}; `expected_plan` {`to_add` 0, `to_change` 2, `to_destroy` 0, `resources` (exactly `aws_iam_role_policy.irpt_reporting_gold` and `module.irpt_reporting_gold.aws_lambda_function.this`), `words` (the function changes by its code hash and its memory, the role policy by the grants of rounds 121 and 122; say who builds the bundle)}; `validated` {`ran` (boolean), `words` (the box has no terraform)}; `files_changed` (a list of exactly one: `lambda.tf`, with `file`, `sha256` of the bytes at your final commit, `kind` "terraform"); `words`; `claim` ("inferred": nothing was planned); `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage` or `resources` field.

<criterion id="DB123-1-AC1" cell_refs="DB-b-250"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r123/p123_mem8192.py" . DB123-1-AC1</invocation><expect>DB123-1-AC1 PASS</expect></criterion>
`DB123-1-AC1` -- `lambda.tf` carries exactly one `memory_size` assignment equal to 8192 and exactly one `timeout` equal to 900; in the worker's own commits it gains between 1 and 6 lines and loses at most 3, and no other infra file changes. Base: FAIL (memory_size is 3008).
<criterion id="DB123-1-AC2" cell_refs="DB-b-250"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r123/p123_mem8192.py" . DB123-1-AC2</invocation><expect>DB123-1-AC2 PASS</expect></criterion>
`DB123-1-AC2` -- `RD_MEMORY_FACTS_R123.json` has exactly the form of step 3; the measured peak equals round 122's record, the fraction equals peak / 8192 within 0.0005 and is under 0.7; the plan is 0 / 2 / 0 on the two named resources; the file hashes as recorded; flags false; no long digit run. Base: FAIL (no record).

<expected_criteria>DB123-1-AC1,DB123-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every other Terraform file, the handler, the source map, round 122's record, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files. No AWS call, no Terraform command (the box has none), no S3, no deploy, no push, no vendor call, no secret read. Writes: the repo files of the grant.
- **Client data.** None is involved.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If `lambda.tf` carries more than one `memory_size` or `timeout` assignment, or the module call does not take them from these lines, file a BLOCKING row naming the exact lines and stop on that point. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W204-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~204/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-250.hop-1-function-memory-8192-in-the-reporting-gold-terraform.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 121 (round 123, workstream B-49F), cell `DB-b-250`.
<owned_cells>DB-b-250</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB123-1-AC1, DB123-1-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~204/IRPT_DASHBD.TO-DB-b-250.hop-1-function-memory-8192-in-the-reporting-gold-terraform.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB123-1-AC1,DB123-1-AC2` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the lines you changed; the measured peak and its fraction of 8192; the expected plan; what you could not check without Terraform. Words and counts only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one Terraform file and a facts record in a branch; nothing is planned, applied, scheduled or deployed, and the apply is another seat's act under a signed never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no grant changes; the memory takes effect only at the applier's apply, under the pair.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its clauses were dry-run at the base (memory_size 3008, no record) and exercised by its self-test (a settings reader and one green and nine red facts arms).
lane: the <paths> block IS the grant.
</preflight>
