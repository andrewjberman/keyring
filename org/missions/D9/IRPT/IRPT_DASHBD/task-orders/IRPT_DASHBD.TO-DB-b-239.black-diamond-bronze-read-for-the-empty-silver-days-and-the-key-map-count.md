# TO IRPT_DASHBD.TO-DB-b-239 -- the BLACK DIAMOND BRONZE READ for the 33 empty silver days and the KEY-MAP COUNT FINISHED (round 120, workstream B-49F): does the bronze layer hold 2026-04-25 to 2026-07-09 and is each bronze file itself empty, which makes the Cottonwood return gap a SOURCE_BREAK or a silver-build gap; and the exact number of the Cottonwood history's Commonwealth accounts the Black Diamond key map covers over ALL 111 non-empty allocation partitions; counts only; nothing written

<to_id>IRPT_DASHBD.TO-DB-b-239</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~193</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>120</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 120 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-120 ANALYSIS (B-49F) section 2 ruling 3 and section 3 cell 3 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_120_20261015.md @5e358b0a8f`: "Cottonwood's 06-22 to 07-10 gap: first READ whether Black Diamond's BRONZE holds those 33 days. If it does, the empty silver is a silver-build gap, and its owner re-runs that build (a separate pair). If it does not, the gap is `SOURCE_BREAK` at the seam, in words, and no figure is invented. The same read finishes the 134 unread key-map partitions, so 563 becomes an exact count") | **Rows:** IRPT_DASHBD-D2-W193-S<k> | **Decomp cell:** `DB-b-239` (decomposition section 118) | **outcome_ref:** FWD-11 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-193` (branch `wk-IRPT_DASHBD-193`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~193/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~193/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.**

**Why.** Round 119 found that Black Diamond `fact_allocations` (bucket `opal-data-assets`, prefix `blackdiamond/cottonwood/silver/fact_allocations/`) has 144 date partitions of which 33 are EMPTY (2026-04-25 to 2026-07-09), so Cottonwood has no return between the Commonwealth history's end (2026-06-22) and 2026-07-10; and that a partial key map exists (`AccountID` beside `NFS Account Number`), read over ten partitions only. The bronze layer (`blackdiamond/cottonwood/bronze/`) keeps the delivered workbooks: `bronze/allocations/ALLOCATIONS_DAILY_<date>.xlsx`. The issuer's first look: the bronze object of an empty silver day is a tiny workbook of about 4,300 bytes for 32 of the 33 days, and one day's object is about 337,000 bytes. This cell establishes it and finishes the map count. A READ: nothing is changed, deployed or written outside your folder.

**The cell (`DB-b-239`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r120/p120_bronze.py` (your criterion; its docstring defines the verdict and `gap_days`, and the checker RECOMPUTES the empty days, the bronze object sizes, the verdict, the map over every non-empty partition and the frontier coverage); round 119's key-map record and script `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~189/RD_KEY_MAP_READ_R119.json` and `key_map_read_r119.py` (the map table and columns, the normalisation, how the history ids were read: copy what you need into YOUR script, never import or edit it); round 119's Black Diamond adapter record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~188/RD_COTTONWOOD_BD_RETURN_R119.json` and its coverage output `ALLOC_PARTITION_COVERAGE_R119.txt`; `lib/opal_naming.py`.
2. **The silver partitions.** LIST the `date=` partitions of `fact_allocations` (144) and read each `data.parquet`'s row count (a footer or a one-column read; use threads, the files are small): `silver` {`partitions` (144), `empty_days` (the dates whose row count is 0, in order), `nonempty_days` (the count), `claim`}.
3. **The bronze objects.** LIST `bronze/allocations/` once. For each empty silver day record whether `ALLOCATIONS_DAILY_<date>.xlsx` exists and its size in bytes (`empty_day_objects`, one entry per empty day in order: {`date`, `present`, `bytes` (null when absent)}); `nonempty_day_bytes_min` = the smallest bronze object size among the NON-empty silver days; `gap_days` = the empty silver days whose bronze object is at least `nonempty_day_bytes_min`; `verdict` by the checker's rule (SOURCE_EMPTY: every empty day has a bronze object smaller than the minimum; SILVER_BUILD_GAP: some empty day has one at least that big; BRONZE_ABSENT: none has a bronze object; MIXED otherwise); `object_pattern` ("allocations/ALLOCATIONS_DAILY_<date>.xlsx"); `words` (what the verdict means for the gap, and for the `gap_days` if any: which dates, whether their bronze workbook holds rows is NOT read here, say so); `claim`. Do NOT open the workbooks' contents.
4. **The key map over ALL non-empty partitions.** The map of round 119 (`table` "fact_allocations", `key_column` "AccountID", `custodian_column` "NFS Account Number", `normalization` "exact" unless your read shows another is better: the checker applies the one you name): read the custodian column of EVERY non-empty partition (use threads). Write the Cottonwood history's distinct Commonwealth account ids (the `account_id` column of all 3,325 Cottonwood `account_return_daily` partitions, in the background; the address from `address("irpt", "cottonwood", "gold", "account_return_daily", ...)`, LIST for the dates) to the PRIVATE file `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~193/history_ids.txt` (one id per line; it never enters the repo). Then record `key_map` {`table`, `key_column`, `custodian_column`, `normalization`, `partitions_read` (the number of non-empty partitions you read: ALL of them), `frontier_date` ("2026-06-22"), `history_ids_file` {`path` (that private file), `sha256` (of its bytes), `ids` (the count of lines)}, `history_ids_total` (the distinct ids), `mapped_history_ids` (those found in the custodian column over all the partitions you read, under the normalisation), `frontier_ids` (distinct ids of the 2026-06-22 partition: 12), `mapped_frontier_ids`, `claim`}. The checker joins your history file to its own union of the custodian column, re-reads three history partitions to confirm their ids are in your file, and recomputes both mapped counts.
5. **Words** (the record's `words`, one paragraph): the gap's verdict in plain terms for the Cottonwood return between 2026-06-22 and 2026-07-10, and the exact map coverage (mapped of total, and how many history ids stay SOURCE_BREAK at the seam).
6. **Write your analysis as a tracked script** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~193/bd_bronze_and_map_read_r120.py` (no write call to AWS; names no other firm's place; writes ONLY a private file under your private folder).
7. **Record** `RD_BD_BRONZE_AND_MAP_R120.json` in your folder with EXACTLY these fields: `silver` (step 2), `bronze` (step 3: `object_pattern`, `empty_day_objects`, `nonempty_day_bytes_min`, `gap_days`, `verdict`, `words`, `claim`), `key_map` (step 4), `words` (step 5), `analysis` {`file` "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~193/bd_bronze_and_map_read_r120.py", `sha256`, `tracked` true}, `reads` {`s3_reads` (integer), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, `claim`, `files_in_repo` false, `served_values_changed` false, `pushed` false, `deployed` false. Every `claim` is one of `measured`, `inferred`, `held`, `absent`. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage`, `date` or `object_pattern` field; no account id.

<criterion id="DB120-3-AC1" cell_refs="DB-b-239"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r120/p120_bronze.py" . DB120-3-AC1</invocation><expect>DB120-3-AC1 PASS</expect></criterion>
`DB120-3-AC1` -- `RD_BD_BRONZE_AND_MAP_R120.json` has exactly the form of step 7; the silver partition count, the empty days, the non-empty count, every empty day's bronze object (present, bytes), the non-empty minimum, `gap_days` and the verdict EQUAL the checker's own recount (LIST and footer reads); `partitions_read` is all the non-empty partitions; the history file's sha256 is as recorded and its ids count equals `history_ids_total`; `mapped_history_ids`, `frontier_ids` and `mapped_frontier_ids` EQUAL the checker's own recount over all non-empty partitions; three history partitions' ids are in the history file; the analysis script is tracked, hashed as recorded, names no other firm's place and holds no write call; every claim is in the four-word set; zero writes, no push or deploy flags, and no run of 8 or more digits outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DB120-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every adapter, contract, module and test, round 119's scripts and records, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the Cottonwood Black Diamond silver `fact_allocations` prefix (every partition, the custodian column and row counts only), the LIST of `bronze/allocations/` (object keys and sizes ONLY: no GET of a workbook), and the Cottonwood `account_return_daily` gold prefix (the `date=` listing and the `account_id` column of every partition), the gold prefix derived by `lib/opal_naming.py address()` and nowhere else. Writes: the repo files of the grant and the private folder (the history ids file). No put, copy or delete of any kind, no deploy, no push, no vendor call, no secret read, no read of another firm's place, no Terraform.
- **Client data.** The ids file is client data: it stays in the private folder; counts, dates, hashes and words only in the repo, a row or your report; never an account number or key.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a prefix cannot be read, record the source `absent` with the refusal named, file a BLOCKING row with counts and stop on that point; an unreadable source is never a zero. If a count differs from the checker's recount, report both numbers in a BLOCKING row; do not adjust either. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W193-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~193/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-239.black-diamond-bronze-read-for-the-empty-silver-days-and-the-key-map-count.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 118 (round 120, workstream B-49F), cell `DB-b-239`.
<owned_cells>DB-b-239</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB120-3-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~193/IRPT_DASHBD.TO-DB-b-239.black-diamond-bronze-read-for-the-empty-silver-days-and-the-key-map-count.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB120-3-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the silver partitions and the empty days (count, first, last); the bronze verdict, the `gap_days` and the size classes (counts by size); the key map's exact coverage of the history and of the frontier; the words; reads and writes. Counts, dates and words only: no account number or key.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a tracked analysis script with a record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the S3 reads are GET and LIST of Cottonwood prefixes already read by the round-114, 116 and 119 reads and adapters.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms for each clause); its recounts were dry-run by the issuer against the real silver and bronze (the verdict side in 2.8 seconds).
lane: the <paths> block IS the grant.
</preflight>
