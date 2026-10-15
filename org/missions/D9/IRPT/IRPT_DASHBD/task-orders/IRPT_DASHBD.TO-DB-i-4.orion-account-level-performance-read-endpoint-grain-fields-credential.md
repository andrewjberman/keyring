# TO IRPT_DASHBD.TO-DB-i-4 -- the ORION ACCOUNT-LEVEL PERFORMANCE READ: does Orion's API, as the estate's pull code reaches it, expose an account-level performance or return series; the endpoint, the grain, the fields (return, period, gross or net) and whether the pull's credential reaches it; a read of repo code, fixtures and docs, no vendor call, nothing written

<to_id>IRPT_DASHBD.TO-DB-i-4</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~304</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>116</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_116_20261015.md` section 2 ruling 1 and section 3 cell 1 (msg 7978) | **Rows:** IRPT_DASHBD-D2-W304-S<k> | **Decomp cell:** `DB-i-4` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md` section 3) | **outcome_ref:** FWD-2 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-304`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~304/`. Never push. This cell reads CODE, FIXTURES and DOCS in the repo. It makes NO vendor call, NO AWS call of any kind, and reads NO secret value: a secret is NAMED (as the code names it) and never fetched. A fixture or capture file may hold client data: read its FIELD NAMES and structure only; never copy a value, a name, an id or a figure into the repo, a row or your report.

**Why.** Opal's own reconstruction of Inflection account returns cannot be tied to Orion's client return closer than about 25 bp for most households, and two of the five likely causes cannot be tested from the transactions feed (rounds 114 and 115). The CTO ruled: stop reconstructing, and find out whether Orion itself provides an ACCOUNT-level return. If it does, the account figure a client sees will be the same system's figure as the household return. This cell answers that question from what the estate already has. It changes nothing.

**What to read (the starting points; follow what they cite).**
- `infra/aws/lambda/investor-reporting/performance/orion_adapter.py` (its header says "native household and account scopes" and names `POST /api/v1/Reporting/Scope` on `api.cloud.orionadvisor.com`, PRD row B11), `orion_live.py` (the bounded transport: how the request is sent, which credential it uses), `tenants.py`, `orion_account_mapping.py`, `orion_selected.py`, `normalize.py`, `units.py`, the directory's `fixtures/` (field names only) and `FIXTURE_MANIFEST.json`.
- The estate's Inflection pull code: every `*.py` directly inside each directory under `infra/aws/lambda/inf-pipeline/` (for example `inf-performance-daily/pull_inflection_performance_dim.py`, the `inf-api-*` directories, `inf-silver-chain/_orion_api_silver_lib.py` and `convert_orion_api_to_silver.py`, and every `jwt_freshness.py`).
- The PRD row B11 the adapter header cites and any vendor endpoint documentation in the repo: find them with `comp-find` (never a recursive grep of the repo), for example `comp-find 'B11' --files` scoped to `org/missions/D9/IRPT`, and `comp-find 'Reporting/Scope' --files`.

**The cell (`DB-i-4`).**
1. **The endpoint inventory (the denominator).** List every distinct Orion path literal `/api/vN/...` that occurs in the `*.py` files directly inside each directory under `infra/aws/lambda/inf-pipeline/` and directly inside `infra/aws/lambda/investor-reporting/performance/` (non-recursive; a trailing `/`, `.` or `,` is not part of the path). Record the sorted list as `endpoint_inventory` and the number of files you scanned as `pool_files_read`. The checker recomputes both from the repo with the same rule.
2. **The answer** `account_level_exists`: `YES` if some endpoint in the inventory returns a performance or return series for ONE ACCOUNT (not only a client or household), `NO` if the code and docs show none, `UNDETERMINED` only if the repo cannot settle it (say what would).
3. **Five sections**, each `{claim, evidence, ...}`, each `claim` one of `measured` (you saw it in a fixture or capture's structure), `inferred` (read from code or a doc), `held` (stated by a doc you could not check against the code) or `absent` (the repo says nothing), and each `evidence` a NON-EMPTY list of `{file, line, quote}` where `file` is a repo-relative path, `line` the 1-based line number, and `quote` a run of at least 6 characters copied EXACTLY from that line (the checker opens the line and requires the quote on it):
   - `endpoint`: {`method`, `path`, `host`, ...}: the endpoint that gives an account-level series (when `YES`); `path` must be in `endpoint_inventory`.
   - `grain`: {`words`}: the grain in words (an account scope or a household scope; per day, per period; what the request names to select ONE account, as the code states it).
   - `fields`: {`names`: the list of field names that carry the return, the period and any fee (as the adapter or fixture structure names them)}.
   - `gross_or_net`: {`answer`: `GROSS`, `NET`, `BOTH` or `UNDETERMINED`, `words`}: whether the series is gross or net of fees, and whether a request parameter selects it.
   - `credential`: {`answer`: `REACHES`, `DOES_NOT_REACH` or `UNDETERMINED`, `secret_named_not_read`: true, `secret_name_as_code_names_it`, `words`}: whether the credential the estate's pull uses (the refreshed Orion session token, named by the code that loads it) is the one this endpoint is called with, by the code. You cannot prove reach without a call; state what the code shows and what it does not.
4. **When the answer is not `YES`** the record carries `reason_words` (at least a sentence) instead of a filled endpoint.
5. **Who calls it today.** In `basis_words`, say whether the performance Lambda's account-level call is live in the estate (what invokes it; a schedule or a request path) or only built, and whether the `inf-pipeline` pull (which feeds the silver the tie-out used) calls it: it does NOT if its path inventory lacks the endpoint. This is the fact the CTO needs to decide where the feed is added.
6. **Record** `ORION_ACCOUNT_PERFORMANCE_READ_R116.json` in your folder with exactly: `account_level_exists`; `pool_files_read`; `endpoint_inventory`; `endpoint`; `grain`; `fields`; `gross_or_net`; `credential`; (`reason_words` when not YES); `basis_words` (words, at least 120 characters: the files read, how each section was decided, what the repo cannot show, who calls it today; no client value); `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `s3_reads` 0}; `files_in_repo_private` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, paths, line numbers, short code quotes and words only: no run of 8 or more digits except in a `file`, `path` or `sha256` field.

<criterion id="DBI116-1-AC1" cell_refs="DB-i-4"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r116/p116_orion.py" . DBI116-1-AC1</invocation><expect>DBI116-1-AC1 PASS</expect></criterion>
`DBI116-1-AC1` -- the record is complete and carries no identifier and no read or write of AWS, a secret or a vendor; `pool_files_read` and `endpoint_inventory` equal the checker's recount over the named directories; `account_level_exists` is one of the three answers; every one of the five sections carries a claim word and a non-empty evidence list whose every citation is a real file and line with the quote on that line; when the answer is `YES` the endpoint path is in the inventory, the method is GET or POST and the host, grain words and field names are present; when it is not `YES` the reason words are present; `gross_or_net.answer` and `credential.answer` are within their enums and `secret_named_not_read` is true; no push or deploy. Base: FAIL (no record).

<expected_criteria>DBI116-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every file under `infra/`, `lib/`, `data/` and every issuer check.
- **Reads and writes.** Reads: repo files and fixtures (field names only). Writes: the repo files of the grant. NO AWS call, NO vendor call, NO secret read, NO push, NO deploy.
- **Client data.** A fixture or capture may hold client data; copy no value from it. Citations are short code or doc quotes, not data.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the repo cannot settle the question, the answer is `UNDETERMINED` with what would settle it; never guess an endpoint, a grain or a field.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W304-S<k>`, with the real current UTC time (`date -u +%FT%TZ`, run at filing; never typed by hand); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~304/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-4.orion-account-level-performance-read-endpoint-grain-fields-credential.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 3, cell `DB-i-4`.
<owned_cells>DB-i-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI116-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~304/IRPT_DASHBD.TO-DB-i-4.orion-account-level-performance-read-endpoint-grain-fields-credential.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI116-1-AC1` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the answer (`account_level_exists`); the endpoint (method, host, path), the grain in one line, the field names, gross or net, the credential answer in one line; the size of the endpoint inventory (a count) and whether the `inf-pipeline` pull calls the endpoint; who calls the performance Lambda's account-level path today (one line); row ids. No client value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read of repo code and docs; one record file; nothing is read by served code, wired or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call, no secret read and no grant; the credential is named from code, never fetched.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the order READS what invokes the Lambda from code.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBI116-1-AC1 FAILS at base (no record), and the checker was fed a synthetic good record (PASS) and one with a quote not on its cited line (FAIL) before the cut.
</preflight>
