# NFRA_OPLGTW task order -- `OG-x-4` -- the R-4 remedy: export memory FLAT at full width, the maximal query under 80% of the cap

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-x-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~11</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change and one narrow release; no cron, alarm, monitor or cadence is created or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM operation, policy, principal or role is added; the release uses safe-ec2-deploy.sh and the on-host benchmark runs in process under the existing instance role, as OG-x-3 and OG-r-3 did.
comp-adversary: DECLARED-NOT-APPLICABLE -- ruled by 1.0.0_SA_CTO~O (msg 26488, R-4 branch (a)) on a measured read (OG-r-3's CAPACITY.json, rows Z-W11-S10/S11).
EGRESS CLASS, declared: Opal's own AWS (S3 artifact upload, SSM, CloudWatch reads) plus the PyPI download for the venv -- development egress permitted to this project's COO and its workers (Andrew-direct ~21:2xZ 2026-09-28, record @7bfa5811c6).
</preflight>

## 1. THE CELL -- `OG-x-4` (decomposition addendum R2-E.4; the R-4 remedy for E5/E6)

**The ruling, verbatim** (1.0.0_SA_CTO~O, msg 26488): *"RULED (a). Memory that grows with rows (172 -> 225 -> >272 MB
at 11 columns) means the export is buffering, not streaming. That is a code gap ... The contract numbers stand. Remedy
cell, WORLD: (1) export peak memory at 11 columns is flat across 25k/125k/250k rows, within 10% of the 25k peak; (2) the
maximal query peaks under 80% of the 268,435,456-byte cap; (3) OG-x-2's 2-column proof is re-run at full width. A PRD
revision happens only if the remedied code still measures INSUFFICIENT on the same host."*

**What you measured in OG-r-3** (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~11/CAPACITY.json`,
host serving `4248b70b39`, cap 268,435,456 bytes): export at 11 columns (`dim_position`) peaked 171,974,656 (25k rows),
225,271,808 (125k), and 272,683,008 at 250k where it was refused `LIMIT_EXCEEDED/memory` at 1.4 s; the maximal query
peaked 286,691,328. The CSV is not the constraint (~150 bytes a row).

**Where the growth is -- HYPOTHESES from the issuer's read of the code at the issuance base, NOT findings. Confirm or
refute each by measurement before you change anything** (`GW` = `infra/aws/ec2/opal-gateway`;
`E` = `GW/app/integrations/schwab/engine.py`; print the bytes first):
- **H1 (lead).** The OUTPUT is streamed (`E:750-770` `_write_export_batches`, `fetch_record_batch` at `E:757`,
  `EXPORT_BATCH_ROWS = 8192` at `E:112`), but the INPUT is not. `_plan_job` (`E:678-701`) reads EVERY source object
  whole into Arrow through `_read_source` (`E:636-676`, which concatenates its per-batch tables at `E:676`), concatenates
  across sources (`E:693`), then registers that whole table as DuckDB's `src` (`E:713`, `con.register` at `E:617`).
  DuckDB's `memory_limit` (`E:610`; 64 MiB for exports, `E:110` and `E:1174`) bounds DuckDB's own operators, not the
  registered Arrow input, so the child's peak follows the policy-filtered input size x width.
- **H2.** `_read_source` holds the list of filtered batch tables AND their concatenation at once (`E:652-676`): a
  transient second copy per source.
- **H3 (the maximal query).** The query path holds the same whole input (H1), plus `fetch_arrow_table()` (`E:739`), plus
  per-column `to_pylist()` (`E:743`), plus the row list (`E:744`) at once, with a DuckDB `memory_limit` of
  `job_memory_bytes x 0.5` (`E:1169`, `E:995`) on top.
- The parent side (`read_export_batches`, `E:774-782`) yields one batch at a time and is not the child's peak.

**Build (the outcome is fixed; the shape is yours):**
1. **Make the export's child memory independent of the row count at full width.** The input must not be resident whole:
   for example, have DuckDB scan the Parquet sources directly (`read_parquet` over the job's source paths, with the account
   policy as a SQL predicate on the same values `_read_source` applies today, and only the referenced columns), or stream
   the policy-filtered batches into DuckDB without concatenating them. Keep every existing guarantee: the account policy is
   applied BEFORE any row reaches the result (C1/C2); the count-before-fetch cap refusal (`E:726-735`) stays; the output
   stays streamed; `DUCKDB_LOCKDOWN` and `lock_configuration` stay; no path outside the job's source list is readable.
2. **Bring the maximal query under 80% of the cap** by the same input change plus, where needed, one representation of
   the page result at a time (H3). The 500-row / 100,000-codepoint / 131,072-byte page caps (C4) do not move.
3. **Tests.** In `GW/tests/test_schwab_export_stream.py` add `test_ogx4_ac03`: OG-x-2's `test_ogx2_ac01` harness (REAL
   engine, spawned child, `export.generate_csv`) at the 11 exportable columns of `dim_position`, two sizes one order of
   magnitude apart (the 10k/100k sizes of OG-x-2 are fine), passing OG-x-2's flatness bar (peak child RSS plus parent
   tracemalloc at the larger size <= 1.2 x the smaller), printing both sizes, the column count and all four numbers.
   It must finish inside `timeout 110` on this box (OG-x-3 measured the 2-column run at 86.8 s under load; if 11 columns
   cannot fit, that is ONE BLOCKING row with the timing, never a smaller width). Every existing Schwab test stays green.
4. **`GW/tests/acceptance/onhost_bench.py`:** add the 250,000-row export and the 125,000-row probe as RECORDED cases (not
   just a largest-successful probe), all at 11 columns, and label each `export:<case> (<N> rows x 11 columns)` in the
   `ac2.jobs` list, as OG-r-3 did. Its grader test stays green.

Contract numbers never move (ruling R-4): 250,000 rows, 50 MiB, the 256 MiB job cap. A PRD revision is the input ONLY if
the remedied code still measures INSUFFICIENT on the same host: then AC1/AC2 are measured FAILs, recorded honestly.

## 2. BOUNDS

1. **Two phases.** PHASE A builds and proves locally, with no AWS write and no host contact. PHASE B runs only when the
   issuer continues you with GO.
2. **Worktree and interpreter.** You work in the worktree named in your identity line; `.venv-og` (python 3.11) serves
   every local invocation. Never push, merge, rebase, `stash`, `checkout --` or `clean`. Every pytest run sets
   `AUDIT_PATH` to a temp file; a dirtied tracked `GW/audit.jsonl` is restored to HEAD bytes, never committed.
3. **Synthetic data only.** No Schwab object is read, locally or on the host. No egress off Opal infrastructure beyond
   the preflight's EGRESS line.
4. **PHASE B release mechanics (bounds, each with its own check, printed in your report; OG-x-3's A1-A3 pattern):**
   - one-deployer census across EVERY worktree (`git worktree list --porcelain`; per tree
     `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/` AND its working dir), per-tree
     denominator printed; any OPEN sentinel naming `opal-gateway` or `gateway` that is not yours -> STOP, a BLOCKING row
     (the superseded `nfra-oplgtw-og-r-1-first-release` slug is closed on CLOUD @45d1e43657);
   - the live base resolved BY CONTENT on the host (the manifest can lag a deploy-only commit): the full gateway-tree md5
     manifest equals a named candidate commit; the release tree = that live tree + ONLY your commits' gateway files, and
     it carries the live `deploy-to-ec2.sh` UNCHANGED (its `ENABLED_INTEGRATIONS` line must equal the host `.env`);
   - a fresh NEVER-2 ledger, slug `nfra-oplgtw-export-flat-release`, entry AND sentinel committed BEFORE the upload;
   - rollback proven BEFORE the act: rebuild the live commit's artifact without uploading and compare its file set with
     the live S3 artifact, all files identical;
   - the act from the release tree with `HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~11 bash infra/aws/ec2/safe-ec2-deploy.sh
     opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`;
   - verify within 90 s of the restart: `/health` 200 on the host; the changed files equal the release bytes; the tool
     list AFTER equals BEFORE (count and sorted diff); `ENABLED_INTEGRATIONS` unchanged and without `schwab`. Any failure:
     roll back, re-verify, close the ledger ROLLED BACK. Never half-landed;
   - `EC2_MANIFEST.json` `services.opal-gateway` recorded on an LF copy (`deployed_commit` = the release,
     `previous_deployed_commit` = the committed release the live tree equals); ledger closed;
   - THEN the on-host re-measure: `onhost_bench.py` in process on `i-07dccb1615503ac99` over SSM, as OG-r-3 ran it (scratch
     directory, synthetic principals and fixtures, no restart, no config change, no state-store write beyond isolated
     `RUNTIME#bench-og-x4-*` keys), against the served code confirmed by md5; assemble the result as
     `deliverables/0.9.0_WK_NFRA_OPLGTW~11/CAPACITY_X4.json` in `CAPACITY.json`'s shape.
5. **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy is refused with its measurement,
   never repaired, widened or satisfied by a route this order does not name. Surprises: ONE row each in the investigation
   file, id `NFRA_OPLGTW-Z-W11-S<k>`, fabric `site-z`, `disarm_owner` `2.0.0_SA_COO~O`; keep working after filing.
6. **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

### PHASE A (no AWS write, no host contact)
Confirm or refute H1-H3 with a local measurement (print it), build items 1-4, run AC3 and the full Schwab suite per module,
commit through `.tools/safe-commit.sh` (every `.py` passes `.tools/commit-gate.sh`), write `ANNOUNCE_OG-x-4.md` in your
deliverables (the hypotheses' verdicts, the diff stat, AC3's output, the suite counts), report once, and STOP.

### PHASE B (GO only)
Bound 4 in order, then run AC1-AC3, write and validate the proof, flip `complete` only if all three PASS by output.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/engine.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/export.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/envelope.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/query.py
infra/aws/ec2/opal-gateway/tests/test_schwab_export_stream.py
infra/aws/ec2/opal-gateway/tests/test_schwab_export.py
infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py
infra/aws/ec2/opal-gateway/tests/test_schwab_query.py
infra/aws/ec2/opal-gateway/tests/acceptance/conftest.py
infra/aws/ec2/opal-gateway/tests/acceptance/onhost_bench.py
infra/aws/ec2/opal-gateway/tests/acceptance/test_onhost_bench_grader.py
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-export-flat-release.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~11/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="OGX4-AC1" cell_refs="OG-x-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/xf.AC1.sh; echo "exit=$?"</invocation><expect>(?s)export sizes graded 3 of 3.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="OGX4-AC2" cell_refs="OG-x-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/xf.AC2.sh; echo "exit=$?"</invocation><expect>(?s)maximal query peak=.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="OGX4-AC3" cell_refs="OG-x-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/xf.AC3.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 1 of 1.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `OGX4-AC1` (ruling (1)) -- on the host, from `CAPACITY_X4.json`: the export at 11 columns completed ok at 25,000,
  125,000 and 250,000 rows, and each peak child RSS is within 10% of the 25,000-row peak (3 of 3 graded, ratios printed).
- `OGX4-AC2` (ruling (2)) -- on the host, from `CAPACITY_X4.json`: the maximal query's peak child RSS is <= 214,748,364
  bytes (80% of 268,435,456).
- `OGX4-AC3` (ruling (3)) -- locally: `test_ogx4_ac03`, OG-x-2's flatness proof at the 11 exportable columns, passes.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~11/NFRA_OPLGTW.TO-OG-x-4.export-flat-at-width.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase. If the remedied code still
measures INSUFFICIENT, AC1/AC2 are recorded as measured FAILs with the numbers: that is the input to a PRD revision, not a
reason to change the harness or the thresholds.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~11 (the subagent that built OG-x-2, released OG-x-3 and measured OG-r-3), queue position after OG-r-3, which this
  order SUPERSEDES (OG-r-3's measurement stands as the input). Addendum R2-E.4.
- Ruling: 1.0.0_SA_CTO~O msg 26488 (R-4 branch (a)); the contract numbers stand.
- `<round>7</round>`: the pipeline gate admits one issuance per round label (3 = the round-2 enrichment, 4 = OG-m-2,
  5 = OG-m-3, 6 = OG-g-1); this cell drains with round 3.
- Check dry-runs at the issuance base: xf.AC1 FAIL (CAPACITY_X4.json absent), xf.AC2 FAIL (absent), xf.AC3 FAIL
  (test_ogx4_ac03 absent); and on OG-r-3's CAPACITY.json via the TEST-ONLY override: xf.AC1 FAIL (ratios 1.0000 /
  1.3099 / 1.5856, bound 189,172,121), xf.AC2 FAIL (286,691,328 > 214,748,364).
- The declared class is WORLD: a deploy and GATE (xii)'s floor (`infra/` path).

<status>complete</status>
<round>7</round>
<slot>~11</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
