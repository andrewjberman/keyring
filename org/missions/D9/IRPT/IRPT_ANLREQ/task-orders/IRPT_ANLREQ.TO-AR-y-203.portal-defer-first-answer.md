# TO IRPT_ANLREQ.TO-AR-y-203.portal-defer-first-answer -- the deployed first answer of the template lane passed through the portal's readers at PROD and DEV

<to_id>IRPT_ANLREQ.TO-AR-y-203</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~58</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-203` (`decompositions/IRPT_ANLREQ_DECOMP_R19R7_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~58`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-58` (branch `wk-IRPT_ANLREQ-58`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~58 <0.9.0_WK_IRPT_ANLREQ~58@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W58-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-203`, inlined) -- THE DEPLOYED FIRST ANSWER OF THE TEMPLATE LANE THROUGH THE PORTAL'S READERS. Nothing is changed, deployed or applied.

*The cell before this one fed the portal's readers a body the deployed door never serves. This one feeds them the body it does.* The deployed door builds `UploadService` WITH `request_resolution`, so a template with an ERROR finding answers from `_defer` in `infra/aws/lambda/investor-reporting/intake/uploads.py` (read it at commit `069b8f797e`, lines 459-475): `{upload_id, input_id: None, state: "NEEDS_CORRECTION", reason: "TEMPLATE_FINDINGS", findings: _with_correction_words(findings[:MAX_STORED_FINDINGS]), findings_total: len(findings), template: <the template>}`.

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~57/r19/PORTAL_UPLOAD_ANSWER_READERS.json` (the previous cell's record: `readers` with their key policies and lines, the PROD and DEV commits `37aa1247ee4ba487e5610dc5b78d65ae28468a99` and `64980b4d3a1e11d8407b6a263ddcd5447dafaef2`, the cases, `not_read`) and the previous worker's runnable scratch at `C:/dev/wk-irpt-anlreq-57/.scratch/r19` (portal source archives at both commits, the bun scripts, and the harness `start_state_run.py` outputs; READ and COPY from it, never write into it).

1. **Build the body with the real code.** In a NEW EMPTY scratch folder under your `.scratch/r19/`, extract `intake/uploads.py`, `intake/template_reader.py`, `intake/upload_resolution.py` and the files they import from commit `069b8f797e` (git archive of the `infra/aws/lambda/investor-reporting` folders the harness's closure names), and likewise the PINNED pair from commit `f09b802cdc` (`uploads.py`) with `template_reader.py` from `3f29017cfc`. For each fixture sheet in the previous record's cases (the four NEEDS_CORRECTION sheets, plus `header_repeated_csv` if its template has an ERROR finding), run `read_template` on the sheet and build the `_defer` body by calling the REAL `_with_correction_words`, `MAX_STORED_FINDINGS` and `NEEDS_CORRECTION` from that code (import them; do not retype). Record each body's keys, `reason`, `findings_total`.
2. **Pass each body through the portal readers at BOTH commits** with bun, the same readers the previous cell ran (`parseIrEnvelope` for `analysis-input-upload`, `fileAnalysisRequest` through the same parser, `proxyableFindings`, and the findings-line functions): arms `AFTER` (moved pair) and `BEFORE` (pinned pair, for the sheets whose pinned template has an ERROR finding; say so if there are none), commits `PROD` and `DEV`. Record per case `case`, `arm`, `commit`, `reader`, `outcome` (exactly `RETURNED` or `THREW`), `codes`, `reason` (the body's reason, `TEMPLATE_FINDINGS`), `body_keys`, `body_source` (start it with the text `_defer first answer built from`), `method` (`RUN`), and what a person would see per finding code (the words as the portal produces them).
3. **If any AFTER case THREW:** name the reader, the commit and the key, and file a BLOCKING row (do NOT fix anything). If none threw, say so in the report and file one OBSERVATION row `IRPT_ANLREQ-D2-W58-S<k>` stating that the deployed first-answer shape RETURNED at both commits, with the denominator.
4. **Write `r19/PORTAL_DEFER_SHAPE_READERS.json`:** `prod_commit`, `dev_commit`, `cases` (as in step 2), `new_codes` (the words per code at PROD and DEV), `claim`, `not_read` (the HTTP route, the resident's resolution, the React render if not run, and the deployed bundles).
5. **In your report:** the cases count, whether any AFTER case threw at PROD or DEV, and the words a person sees for each code.

### ACCEPTANCE

<criterion id="AR203-y-AC1" cell_refs="AR-y-203"><invocation>python C:/dev/wk-irpt-anlreq-58/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r19/ar19_checks.py y203-defer --root C:/dev/wk-irpt-anlreq-58</invocation><expect>Y203-DEFER-OK</expect></criterion>
`AR203-y-AC1`: every case body is the `_defer` first answer (reason `TEMPLATE_FINDINGS`, with findings, findings_total, template, state, upload_id, input_id), the AFTER cases cover ACCOUNT_COLUMN_SEVERAL_VALUES, HEADER_ROW_REPEATED and TOTAL_ROW_PRESENT at both PROD and DEV, and each case has an outcome of RETURNED or THREW.

<criterion id="AR203-y-AC2J" cell_refs="AR-y-203" judgment="true"/>
`AR203-y-AC2J` (judgment, graded at L9, never by you): the bodies were built by calling the moved `uploads.py`'s own `_with_correction_words` and constants and not by hand, the readers run are the portal's own functions at the named commits, and the words a person sees are what those functions produced.

<expected_criteria>AR203-y-AC1 AR203-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~58/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R19R7_Y.md</decomp_doc>
<owned_cells>AR-y-203</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~58/IRPT_ANLREQ.TO-AR-y-203.portal-defer-first-answer.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-203`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reads of release-pin source and the portal, scratch runs outside the product tree; nothing is changed, deployed, uploaded or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading AR-y-202's rows W57-S1 to S3 against the cell; the lens: a body built by hand that differs from what the deployed door returns, or a reader run on a copy of its logic. The order requires the body built by importing the moved uploads.py's own functions and the portal's own readers at the named commits. NOT seen: the HTTP route and the deployed bundles.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on this seat's reading of rows W57-S1 to S3 as workstream `YR` round 7. Base: `AR203-y-AC1` FAIL as expected (no record).
- The PAIR and the APPLY are not this order.
