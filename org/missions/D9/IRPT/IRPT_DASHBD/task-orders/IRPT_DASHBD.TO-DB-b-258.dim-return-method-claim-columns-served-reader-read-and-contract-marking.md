# TO IRPT_DASHBD.TO-DB-b-258 -- the SERVED-READER READ for the `dim_return_method` claim columns (round 126, workstream B-49F, row W209-S3): does any reader take a claim column from the served row; if none, the dim contract's next version marks the six claim columns `see_manifest`

<to_id>IRPT_DASHBD.TO-DB-b-258</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~211</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>126</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 126 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-126 ANALYSIS (B-49F) section 2 ruling 2 and section 3 cell 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_126_20261015.md @2cf3e13682`: "`~D2` first reads whether any SERVED reader takes a claim column from `dim_return_method`. If none does, the dim contract's next version marks the six claim columns `see_manifest` (it does not drop them silently) ... If a served reader does, the ruling flips to A").

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-211` (branch `wk-IRPT_DASHBD-211`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~211/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~211/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The served `dim_return_method` row has six claim columns in the producer (`CLAIM_COLUMNS` in `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`: `tolerance_claim`, `large_flow_share_claim`, `plausibility_band_low_claim`, `plausibility_band_high_claim`, `comparability_max_excluded_weight_claim`, `threshold_claims_source`) that the newest served version lacks, and no scheduled job writes them. The claims travel with each fire in the manifest's thresholds object. The CTO rules: if no served reader takes a claim column from the dimension, the claims ride the manifest only and the contract marks the six columns `see_manifest`; if one does, the contract stays as it is and a grant is cut instead. Your read decides which.

**The cell (`DB-b-258`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r126/p126_readers.py` (your two criteria; the candidate rule, the classes and both record forms are in it); `org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json` (version 0.6.0); the producer's `emit_method_row` and `CLAIM_COLUMNS`.
2. **The candidates.** The checker recounts them: every tracked file that names a claim column OR the token `dim_return_method`, excluding `org/`, `docs/`, `data/transcripts/`, `projects/`, `workflows/`, markdown files, tests and the producer file; plus the same search inside the portal checkout at `C:/dev/ajb_workspace/portal` (git grep there; files are listed as `portal/<path>`). Run the same search yourself and list the files.
3. **Classify every candidate file** with exactly one class: `reads_claim_column` (the code takes a claim column by name from the served row), `reads_whole_row` (the code takes every column of the served row without naming them: a whole-table read that passes the row on), `reads_other_dim_columns` (it takes other columns by name), `names_prefix_or_grant_only` (an address, a grant or a path, no column read), `writes_dim_row`, `comment_or_doc_only`. For a file that only GRANTS a read of the dimension prefix (an `iam.tf`, a `locals.tf`), follow the grant: name in your words which handler holds that grant and whether its code takes columns by name or the whole row; class that grant file by what the handler does, and cite the handler's line instead if it is a candidate. For each candidate cite ONE line: `line` (1-based) and `line_text` (that line's text, 1 to 160 characters); the checker re-reads the bytes at that line. A `reads_claim_column` line names a claim column.
4. **The decision.** `grant_A` if any candidate is classed `reads_claim_column` or `reads_whole_row`; otherwise `see_manifest`.
5. **The contract branch (the half covers BOTH).** If `see_manifest`: edit `org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json` to version `0.7.0` and ONLY: `contract_version` 0.7.0; `"carrier": "see_manifest"` added to the six claim columns' objects (and no other column); a new top-level string `carrier_note` (40 to 900 characters) saying the claims travel in the per-fire manifest's thresholds object and the columns are kept, not dropped; `supersedes` set to {contract_version "0.6.0", schema_hash the unchanged hash, `why` one sentence}. The `schema_hash` and every column's name, type, nullability, meaning and order are unchanged. If `grant_A`: do not touch the contract; file a BLOCKING row naming the reader and its line.
6. **Record** `RD_CLAIM_READERS_R126.json` in your folder with EXACTLY these fields: `claim_names` (the six names in the order above); `candidate_files` (the sorted list); `candidates` (one entry per file: `file`, `class`, `line`, `line_text`); `decision`; `words` (one paragraph, 80 to 1600 characters, no run of 8 or more digits: what you read, the readers found and what each does with the dimension, the branch taken).

<criterion id="DB126-2-AC1" cell_refs="DB-b-258"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r126/p126_readers.py" . DB126-2-AC1</invocation><expect>DB126-2-AC1 PASS</expect></criterion>
`DB126-2-AC1` -- the record has exactly the form of step 6; its `candidate_files` equal the checker's recount; each candidate has one valid class and a cited line whose bytes the checker re-reads and finds equal; a `reads_claim_column` line names a claim column; the `decision` follows the classes.
<criterion id="DB126-2-AC2" cell_refs="DB-b-258"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r126/p126_readers.py" . DB126-2-AC2</invocation><expect>DB126-2-AC2 PASS</expect></criterion>
`DB126-2-AC2` -- the contract matches the decision: under `grant_A` it is byte-equal to the base; under `see_manifest` it is version 0.7.0 with exactly the six claim columns carrying `carrier` `see_manifest`, the schema hash and every column unchanged, a `carrier_note` naming the manifest and `supersedes` naming 0.6.0, and no other key changed.

<expected_criteria>DB126-2-AC1,DB126-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the producer, every handler, adapter, test and Terraform file, the other contracts, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files and git history, and the portal checkout read-only. Writes: the repo files of the grant and your private folder. No AWS call, no Terraform command, no push.
- **Client data.** None is involved.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a candidate cannot be classed from its code, class it by the nearest honest class, say so in the words and file a row; never class a reader as absent to reach `see_manifest`.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W211-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/standards/IRPT_DASHBD_DIM_RETURN_METHOD_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~211/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-258.dim-return-method-claim-columns-served-reader-read-and-contract-marking.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 124 (round 126, workstream B-49F), cell `DB-b-258`.
<owned_cells>DB-b-258</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB126-2-AC1, DB126-2-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~211/IRPT_DASHBD.TO-DB-b-258.dim-return-method-claim-columns-served-reader-read-and-contract-marking.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB126-2-AC1,DB126-2-AC2` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the candidate files with their classes (one line each); the decision; whether the contract changed; reads and writes. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read, a record and (on one branch) a contract version in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no grant is changed; under grant_A the order cuts none, it reports the reader for a later pair.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its recount and arms were exercised by its self-test (record and both contract branches) and by a scratch reference record on each branch.
lane: the <paths> block IS the grant.
</preflight>
