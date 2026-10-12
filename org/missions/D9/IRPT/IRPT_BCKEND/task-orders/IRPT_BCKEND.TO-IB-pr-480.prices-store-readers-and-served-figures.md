# TO IRPT_BCKEND.TO-IB-pr-480 -- READ ONLY: every reader of the landed prices store under `investor-reporting/`, and whether a served figure depends on it

<to_id>IRPT_BCKEND.TO-IB-pr-480</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~335</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>166</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6503 (CTO ROUND-166 ANALYSIS section 2 row D2-W315-S3, section 3 item 6) | **Decomp cell:** `IB-pr-480` (decomposition section 158) | **outcome_ref:** FWD-13

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-335/` (bash `/c/dev/wk-irpt-bckend-335`). Work only there; `git rev-parse HEAD` before your first commit is `base_commit` (state it). **A READ, NOT A BUILD.** You edit no product file and propose no fix.

**HARD BOUNDS.** READ ONLY. No Lambda is invoked, no route is called, nobody signs in, no Secrets Manager read, nothing is written to AWS, no vendor is called. No AWS call at all is needed: the readers are in code. NO figure of an account, no account id, no client or security name: names of files, functions and tables, line numbers and counts only.

**Why.** Worker ~330's read (`deliverables/0.9.0_WK_IRPT_BCKEND~330/IB165-5_TWO_READS.md`, section on the prices store) found that the landed prices store has a writer and nothing schedules it. The store is bucket `opal-data-cot`, key `silver/prices/canonical_prices.parquet` (registry row `legacy_addresses.json`, key `cottonwood-silver-canonical-prices`),
written by `data/cot/scripts/gold/build_canonical_prices_v2.py` (about line 907). The CTO ruled: a store with a writer that nothing runs on a schedule is not a production source; it is retired AS A SOURCE for this project, nothing is deleted. Before any code moves, ONE read: **every reader of the store under `infra/aws/lambda/investor-reporting/` and whether a served figure depends on it.**
No reader: the retirement is a line in the record. Some: those readers' answers will say `held` with the store's newest date until a scheduled source replaces it, and the replacement is cut on your read.

**Read.** Search `infra/aws/lambda/investor-reporting/` (the service, the adapters, `performance/`, `reports/`, `ycharts/`, `narrative/`, the tests and fixtures) for every way the store is NAMED or ADDRESSED: the key string `silver/prices/canonical_prices`, `canonical_prices`, the registry key `cottonwood-silver-canonical-prices`, an address built by `lib/opal_naming.py address()` for that row, a price-source argument or constant that resolves to it, and any function that reads a daily price bar for a security from "the landed store" or "the silver prices" (the second witness for bars in `performance/` is the first place to look). Use the native Grep tool and `comp-find`; read each reader whole.
For each reader record `{cite, what_it_reads, feeds_served_figure, in_words}`: `feeds_served_figure` is `true` if a figure a route returns or a page shows is computed from what it reads, `false` if it reads the store only in a test, a tool or a read-only audit, and `"NOT_ESTABLISHED"` if you cannot tell from the code (say why in `in_words`).
If a reader feeds a served figure, `dependent_figures` lists which (names of figures and routes, no values).

**The census.** `census: {pattern, files_searched, files_with_a_hit, positive_control}`: the pattern(s) you searched, the number of tracked files searched under `infra/aws/lambda/investor-reporting/`, how many had a hit, and a positive control (a search by the same method that finds a known reader or a known writer elsewhere, for example the writer's own file under `data/cot/scripts/gold/`). A zero without its denominator and its control is not a result.

**Verdict** (exactly one): `NO_READER` (the readers list is empty), `READERS_NONE_SERVED` (readers exist, none feeds a served figure), `SERVED_FIGURE_DEPENDS` (at least one reader has `feeds_served_figure: true`).

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~335/`: `IB166-5_prices_store_readers.json` with `base_commit`, `store_key`, `readers`, `census`, `verdict`, `in_words` (at least a sentence), `dependent_figures` (when the verdict says so), `not_established` (a list), and `functions_invoked`, `sign_ins_made`, `aws_writes_made`, `accounts_written`, `figures_written`, `vendor_requests_sent` each 0; and a one-page `IB166-5_PRICES_STORE_READERS.md` leading with the verdict.

<criterion id="IB166-5-AC1" cell_refs="IB-pr-480"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py" . IB166-5-AC1</invocation><expect>IB166-5-AC1 PASS</expect></criterion>
<criterion id="IB166-5-AC2" cell_refs="IB-pr-480"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py" . IB166-5-AC2</invocation><expect>IB166-5-AC2 PASS</expect></criterion>
<criterion id="IB166-5-AC3" cell_refs="IB-pr-480"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py" . IB166-5-AC3</invocation><expect>IB166-5-AC3 PASS</expect></criterion>

<expected_criteria>IB166-5-AC1, IB166-5-AC2, IB166-5-AC3</expected_criteria>

The checks grade the form, that each cite resolves to a real file and line, that the verdict agrees with the readers list and their `feeds_served_figure` values, that the census has a denominator and a positive control, and that nothing outside your deliverables changed. Every verdict is UNMEASURED by the issuer.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** a reader you cannot place, or a criterion that cannot be met as written: file a row and report. Never weaken a check; do not edit `p166_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W335-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~335" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~335@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~335 <0.9.0_WK_IRPT_BCKEND~335@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~335/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-480.prices-store-readers-and-served-figures.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 158 (round 166, workstream ~P), cell `IB-pr-480`.
<owned_cells>IB-pr-480</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB166-5-AC1, IB166-5-AC2, IB166-5-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~335/IRPT_BCKEND.TO-IB-pr-480.prices-store-readers-and-served-figures.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; every reader with `feeds_served_figure` and its cite; the verdict; the census denominator and the positive control; the figures that depend on the store, if any; what is not established; each criterion's last line; the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read written to the worker's own deliverables folder; nothing is edited, built, invoked or served.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; no AWS call is needed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; no route is called.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p166_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~19:3xZ: IB166-5 AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The store's bucket, key and registry row are worker ~330's read of the code and a ledger, not measured by the issuer.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
