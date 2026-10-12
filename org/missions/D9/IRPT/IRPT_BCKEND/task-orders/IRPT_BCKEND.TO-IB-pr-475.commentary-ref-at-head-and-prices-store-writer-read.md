# TO IRPT_BCKEND.TO-IB-pr-475 -- READ ONLY, two reads: where `commentary_ref` is set and read at HEAD; and who writes the landed prices store and on what schedule

<to_id>IRPT_BCKEND.TO-IB-pr-475</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~330</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>165</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6476 (PRD ADDENDUM v0.49 @6bed773b76, section 2 rows D2-W309-S2 and D2-W315-S3, section 3 item 7) | **Decomp cell:** `IB-pr-475` (decomposition section 157) | **outcome_ref:** FWD-8, FWD-13

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-330/` (bash `/c/dev/wk-irpt-bckend-330`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it). **A READ, NOT A BUILD.** You edit no product file and propose no fix.

**HARD BOUNDS.** READ ONLY. No Lambda is invoked, no route is called, nobody signs in, no Secrets Manager read, nothing is written to AWS, no vendor is called. The only AWS reads allowed are the box's own
reads through `comp-find --corpus aws` (the served graph) and, if the graph does not hold the answer, ONE named `describe`/`get` of ONE named resource (state each; no enumeration). NO figure of an account,
no account id, no client or security name: names of files, functions, rules and tables, line numbers and counts only.

**Read 1 -- `commentary_ref` at HEAD** (row `IRPT_BCKEND-D2-W309-S2`; also read row `IRPT_BCKEND-D2-S99`, the vintage cut it points at; search both by id in
`org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`). The row, from code at an older base, says `commentary_ref` is set as a SIBLING attribute of the request item
(`infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py`, about lines 21-24 and 213-219), while the packager reads `record.get('commentary_ref')` from `DynamoAcceptance.get`, which returns only
the immutable record (`ycharts/generate/acceptance.py` about lines 68-71; `ycharts/research/opal_packager.py` about line 153; `reports/resident_installed.py` about line 334). Read those files AT YOUR HEAD and say whether
HEAD still has the mismatch. `commentary_ref: {verdict, cites, in_words, test_crossing}`: `verdict` is `HEAD_READS_SIBLING` (the packager reads a sibling attribute that `get` does not return), `HEAD_READS_RECORD` (the
write and the read agree at HEAD; say which commit made them agree, from `git log -S`), or `NOT_ESTABLISHED`. `test_crossing`: whether any test at HEAD crosses the draft store's write and the packager's read (cite the test, or say none does).

**Read 2 -- the landed prices store** (row `IRPT_BCKEND-D2-W315-S3`; read it whole, including the store key in its evidence). The row says the store was last written 2026-10-09 but its newest yahoo-labelled point is dated 2026-06-05, the writer
is `data/cot/scripts/gold/build_canonical_prices_v2.py` (about line 907), and no schedule for it was found (`infra/aws/terraform/cot-pipeline/ssm.tf`'s run_gold list does not name it; no cot trigger of `gold_dispatch.sh`
was found in `infra/aws`). Name the writer and its schedule: `prices_store: {writer (the script or function), writer_cite, schedule_cites (the rule, trigger or cron that runs it, if any), verdict, retired_as_source, in_words,
census: {scope, files_searched, files_with_a_hit}}`. `verdict`: `WRITER_SCHEDULED` (a schedule runs it; cite it and say its cadence), `WRITER_UNSCHEDULED` (the writer exists and nothing runs it on a schedule), or `NO_WRITER`
(no code writes this key). The census's denominator is printed beside any "not found". `retired_as_source` is `true` exactly when the verdict is `NO_WRITER` (the CTO's rule: no writer found means the store is retired AS A
SOURCE for this project; nothing is deleted). Search with the native Grep tool and `comp-find`; a zero is a result only with its denominator and a positive control (a search that finds a known writer the same way).

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~330/`: `IB165-5_two_reads.json` with `base_commit`, `commentary_ref`, `prices_store` (as above), `not_established` (a list), and
`functions_invoked`, `sign_ins_made`, `aws_writes_made`, `accounts_written`, `figures_written`, `vendor_requests_sent` each 0; and a one-page `IB165-5_TWO_READS.md` leading with the two verdicts.

<criterion id="IB165-5-AC1" cell_refs="IB-pr-475"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py" . IB165-5-AC1</invocation><expect>IB165-5-AC1 PASS</expect></criterion>
<criterion id="IB165-5-AC2" cell_refs="IB-pr-475"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py" . IB165-5-AC2</invocation><expect>IB165-5-AC2 PASS</expect></criterion>
<criterion id="IB165-5-AC3" cell_refs="IB-pr-475"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py" . IB165-5-AC3</invocation><expect>IB165-5-AC3 PASS</expect></criterion>

<expected_criteria>IB165-5-AC1, IB165-5-AC2, IB165-5-AC3</expected_criteria>

The checks grade the form, that each cite resolves to a real file and line, that `retired_as_source` agrees with the verdict, that a census denominator is present, and that nothing outside your deliverables changed. Every verdict is UNMEASURED by the issuer.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** an AWS read refused, or a criterion that cannot be met as written: file a row and report. Never weaken a check; do not edit `p165_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W330-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~330" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~330@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~330 <0.9.0_WK_IRPT_BCKEND~330@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~330/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-475.commentary-ref-at-head-and-prices-store-writer-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 157 (round 165, workstream ~P), cell `IB-pr-475`.
<owned_cells>IB-pr-475</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB165-5-AC1, IB165-5-AC2, IB165-5-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~330/IRPT_BCKEND.TO-IB-pr-475.commentary-ref-at-head-and-prices-store-writer-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; the `commentary_ref` verdict with its cites and whether a test crosses the write and the read; the prices store's writer, schedule and verdict, and the census denominator beside any not-found;
the AWS reads made (each, or none); what is not established; each criterion's last line; the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; two reads written to the worker's own deliverables folder; nothing is edited, built, invoked or served.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; at most one named describe of one resource by the box's own identity, a refusal being a stated result.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; no route is called.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; Read 2 reads which schedule runs a writer.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p165_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~18:0xZ: IB165-5 AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. Both rows are from code and a single store read by their workers; the issuer measured neither.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
