# TO IRPT_DASHBD.TO-DB-b-256 -- the `dim_return_method` CLAIMS READ (round 125, workstream B-49F, row IRPT_DASHBD-D2-S78): the served 49 Financial method rows' columns against the producer's claim columns, every call site of `emit_method_row`, whether any scheduled function reaches one, which Terraform names the prefix, and which producer may write `threshold_claims_source` and where; a READ of the repo and of S3; no write, no grant

<to_id>IRPT_DASHBD.TO-DB-b-256</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~209</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>125</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 125 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-124 ANALYSIS (B-49F) section 2 ruling 4 and section 3 cell 3 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_124_20261015.md @4285776c5c`: "YES to the `dim_return_method` read for the claims columns (row D2-S78): which producer may write `threshold_claims_source`, and where. It is a read, with a grant only if a later pair needs one") | **Rows:** IRPT_DASHBD-D2-W209-S<k> | **Decomp cell:** `DB-b-256` (decomposition section 123) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-209` (branch `wk-IRPT_DASHBD-209`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~209/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~209/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The producer's method row (`emit_method_row` in `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`) carries six claim columns (`CLAIM_COLUMNS`: one claim per threshold value and `threshold_claims_source`), and the thresholds-swap ledger's leg L7 (closed, row `IRPT_DASHBD-D2-S78`) expected `threshold_claims_source` to be readable after the first scheduled fire. It was not: the scheduled function writes the daily partitions and their manifests, not the method row, and the served rows are `method_version=1` (2026-10-01) and `method_version=2` (2026-10-03). The issuer's first look: the served version-2 row has none of the six claim columns, the only call site of `emit_method_row` is the producer's own `main`, and the reporting-gold role cannot write the prefix. This cell makes that a record the checker recounts and says who may write the claims and where. A READ: nothing is written; no grant is proposed.

**The cell (`DB-b-256`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r125/p125_methodrow.py` (your criterion; every definition and every recounted list is in its docstring and `recount`); the producer's `emit_method_row`, `main` (its flags, especially the one that writes ONLY the method row), `CLAIM_COLUMNS`, `THRESHOLD_VALUES`, `threshold_claims_of` and `served_thresholds`; `infra/aws/terraform/investor-reporting/reporting-publish/` (`iam.tf`, `locals.tf`: what it does with the `dim_return_method` prefix and which principal); the reporting-gold root's `locals.tf` write list; round 120's script `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~192/balance_lag_read_r120.py` (a GET-only S3 reading pattern); `lib/opal_naming.py`.
2. **Read** (GET and LIST only): the objects under the 49 Financial `dim_return_method` prefix (from `address()`): for each `method_version=<N>/data.parquet` its parquet schema column names (the file is one small row; read the schema only, never print a value).
3. **The lists**, exactly as the checker's docstring defines them: `served_versions`, `producer_claim_columns`, `missing_in_newest`, `call_sites`, `scheduled_function_call_sites`, `terraform_files_naming_prefix`, `reporting_gold_write_list_has_prefix`.
4. **`who_may_write`** (words, in the structure the checker requires): `producer_function` (the function that builds the row), `entry_point` (the exact way it runs today: the file, the function and the flag that writes only the method row), `grant_needed` (the minimum S3 grant a principal needs to run that entry point against the 49 Financial prefix: action and resource form), `options` (at least two, each {`id`, `words`}: for example, a manual run of the producer's method-row-only entry point by a seat under a signed pair, and extending the scheduled function to emit the row with a grant; for each say what it changes, what it needs, and what it does NOT change), and `words`. Propose NO grant and make no change: a grant is a later pair's, only if the CTO takes one.
5. **Write your analysis as a tracked script** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~209/method_row_read_r125.py` (GET and LIST only; no write token even in a comment; names no other firm's place; writes ONLY a private file under your private folder).
6. **Record** `RD_METHOD_ROW_READ_R125.json` in your folder with EXACTLY these fields: `firm` ("49financial"), the seven lists of step 3 under their names, `who_may_write` (step 4), `words` (one paragraph: what is stale and why, who may write the claims and where, and what the CTO's decision is), `analysis` {`file`, `sha256`, `tracked` true}, `reads` {`s3_reads` (integer), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, `claim`, `files_in_repo` false, `served_values_changed` false, `pushed` false, `deployed` false. Every `claim` is one of `measured`, `inferred`, `held`, `absent`. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage`, `call_sites`, `scheduled_function_call_sites` or `terraform_files_naming_prefix` field.

<criterion id="DB125-3-AC1" cell_refs="DB-b-256"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r125/p125_methodrow.py" . DB125-3-AC1</invocation><expect>DB125-3-AC1 PASS</expect></criterion>
`DB125-3-AC1` -- `RD_METHOD_ROW_READ_R125.json` has exactly the form of step 6; each of the seven lists EQUALS the checker's own recount (S3 listing and parquet schemas read by the checker, GET only; the call sites and the Terraform files by a scan); `who_may_write` carries the required fields and at least two options; the script is tracked, hashed as recorded, names no other firm's place and holds no write call; zero writes, flags false, no long digit run outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DB125-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the producer, every contract, handler, test and Terraform file, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the 49 Financial gold `dim_return_method` prefix derived by `lib/opal_naming.py address()`. Writes: the repo files of the grant and the private folder. No put, copy or delete of any kind, no deploy, no Terraform, no push, no vendor call, no secret read, no read of another firm's place.
- **Client data.** None is involved: the row holds method and threshold figures, not client data; still print no value, only column names and counts.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If an object cannot be read, record the source `absent` with the refusal named, file a BLOCKING row and stop on that point. If a list differs from the checker's recount, report both in a BLOCKING row; do not adjust either. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W209-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~209/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-256.dim-return-method-claims-read-who-may-write-threshold-claims-source.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 123 (round 125, workstream B-49F), cell `DB-b-256`.
<owned_cells>DB-b-256</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB125-3-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~209/IRPT_DASHBD.TO-DB-b-256.dim-return-method-claims-read-who-may-write-threshold-claims-source.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB125-3-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the seven lists in one line each; the options and the grant they need; the words; reads and writes. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a tracked analysis script with a record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; the S3 reads are GET and LIST of one firm's gold dim_return_method prefix; the record names the grant a writer would need and proposes none.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its recounts were dry-run by the issuer against the real S3 prefix and the repo in 1.1 seconds.
lane: the <paths> block IS the grant.
</preflight>
