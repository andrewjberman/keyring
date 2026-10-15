# TO IRPT_DASHBD.TO-DB-c-15 -- how each firm's GOLD `account_dim` is WRITTEN (49 Financial, Inflection, Cottonwood): the table's state, the code, the function, role and schedule that run it, and the Cottonwood adapter's inputs and state; a read, names, counts, dates and labels only; nothing written; the CTO's ruling (msg 8103) is that Cottonwood's `account_dim` is a SCHEDULED producer on the 49 Financial pattern, so the pattern is read first

<to_id>IRPT_DASHBD.TO-DB-c-15</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~408</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>121</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msgs 8099 and 8103 ("A one-shot gold write is not a production producer ... the build cell first reads how 49 Financial's gold account_dim is written (its function, schedule and role) and copies that pattern for Cottonwood under a *-cot-* builder-named role, scheduled after its Black Diamond silver inputs. If no 49F writer exists, add an account_dim emit to the Cottonwood holdings-performance function, with one more gold write grant, by an addendum to its pair.") | **Rows:** IRPT_DASHBD-D2-W408-S<k> | **Decomp cell:** `DB-c-15` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 8) | **outcome_ref:** FWD-2, FWD-11, FWD-15 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-408`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~408/`. Never push. No client data is read or written. A raw `aws` command in a shell call is denied by the repo's rail; do any S3 read from a short Python script (boto3, LIST and HEAD only) kept in your private folder `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~408/` and not committed. Search the repo with `comp-find '<token>' <one named folder> --files --limit 20` per named folder (the rail denies a blind recursive search).

**Why.** The Cottonwood gold `account_dim` table is unwritten, and the Cottonwood household report needs it. Round 104's packet (`deliverables/0.9.0_WK_IRPT_DASHBD~165/ACCOUNT_DIM_GOLD_PACKET.md`) proposed ONE manual partition write by an applier that does not exist, and the adapter (`data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_account_dim.py`) refuses upload by design. The CTO ruled that production must be scheduled: copy how 49 Financial's `account_dim` is written, or, if no such writer exists, add an emit to the Cottonwood holdings-performance function. Before either is cut, this cell reads what exists.

**The cell (`DB-c-15`).**
1. **The table, per firm.** For each of `49financial`, `inflection`, `cottonwood`: the builder address of its gold `account_dim` is `lib/opal_naming.py address("irpt", <firm>, "gold", "account_dim", "date=2000-01-03")` with the partition tail cut. Record `partition_count` and `newest_date` (a fresh LIST of the `date=` common prefixes; 0 and null when none). The issuer's own LIST at the cut read 0 partitions for all three at those addresses; also look for where a firm's account dimension actually lives if elsewhere (for example the Inflection `unified_account_dim` pipeline in `opal-data-inf`, or a silver/platinum table) and say so in `words`.
2. **The writers.** For each firm find the repo CODE that writes its account dimension (gold or wherever it lands) and record `writers` [{`file`, `phrase`}]: the repo path (it must name `account_dim`) and a short phrase for what it writes and where. Count them in `writer_count`. A firm with no writer has `writer_count` 0, `none_words` (which folders you searched and the denominator) and a `claim` of `absent` or `inferred`.
3. **The function, role and schedule.** For each writer that runs scheduled, record `terraform` [{`file`, `label`, `words`}]: the Terraform file under `infra/` and the exact resource or module LABEL that defines its function, its execution role and its schedule (the label must appear in the file), and in `words` the cron expression and time zone, the role's name, the inputs it reads and the prefix it writes. A writer that is not scheduled (a script run by hand) has none and `words` says how it runs.
4. **The Cottonwood adapter.** Record `cottonwood_adapter` {`file` (the adapter path above), `upload_refused` (true when the adapter source raises `NotImplementedError` for upload), `words` (what `emit_account_dim`/`gold_address` take and return, the function's tests, and what is missing for a scheduled run: an entry point, an upload path, a role, a schedule)}. Record `cottonwood_inputs` {`tables` (the Black Diamond silver tables the adapter reads, by prefix under `blackdiamond/cottonwood/silver/`), `words` (their grain, newest landed date and the time of day the newest partition of each landed, from a LIST)}.
5. **The verdict.** `verdict` is `PATTERN_EXISTS_FOR_49F` (a scheduled 49 Financial writer exists: then its `terraform` entries name the function, role and schedule to copy), `NO_49F_WRITER`, or `NOT_ESTABLISHED`. `words` states in one paragraph what the cell found and which of the CTO's two branches follows (copy the 49 Financial pattern; or add an `account_dim` emit to the Cottonwood holdings-performance function with one more write grant), with what each would need that the repo lacks. Name what you did not read.
6. **Record** `ACCOUNT_DIM_WRITER_PATTERN_R121.json` in your folder with exactly: `claim` ("measured"); `firms` {the three firm keys, each {`partition_count`, `newest_date`, `writers`, `writer_count`, `terraform`, `none_words`, `claim`, `words`}}; `cottonwood_adapter`; `cottonwood_inputs`; `verdict`; `words`; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `aws_writes` 0, `s3_reads` (integer)}; `pushed` false; `deployed` false. Names, counts, dates and words only.

<criterion id="DBC121-1-AC1" cell_refs="DB-c-15"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r121/p121_bcw.py" . DBC121-1-AC1</invocation><expect>DBC121-1-AC1 PASS</expect></criterion>
`DBC121-1-AC1` -- the record is complete; each firm's `partition_count` and `newest_date` equal a fresh LIST of its builder address; every named writer file exists and names `account_dim`; `writer_count` equals the list; every named Terraform label appears in its file; a firm with no writer carries `none_words` and a claim of absent or inferred; the adapter is the known file and `upload_refused` equals what its source says; the adapter's inputs are recorded; a `PATTERN_EXISTS_FOR_49F` verdict has a 49 Financial writer with Terraform labels; no write is recorded. Base: FAIL (no record).

<expected_criteria>DBC121-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the adapter, every Terraform file, the checkers and every contract.
- **Reads and writes.** Reads: repo files; `comp-find` per named folder; S3 LIST and HEAD under the three firms' gold `account_dim` addresses, any account-dimension location you find in the repo, and the Black Diamond Cottonwood silver prefixes the adapter reads. Writes: the record in your folder and your private folder. No write to AWS of any kind, no Terraform command, no invoke, no deploy, no push, no vendor call, no secret read, no row data read.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A search you could not run is named in `words` with the reason.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W408-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~408/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-15.account-dim-writer-pattern-read-three-firms-and-the-cottonwood-adapter.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 8, cell `DB-c-15`.
<owned_cells>DB-c-15</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC121-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~408/IRPT_DASHBD.TO-DB-c-15.account-dim-writer-pattern-read-three-firms-and-the-cottonwood-adapter.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC121-1-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; per firm the account_dim partition count, newest date and writer count; the verdict in one line and which of the CTO's two branches follows; what the adapter lacks for a scheduled run; the number of S3 reads; row ids. No client value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read record; nothing is wired, changed or deleted.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only S3 LIST and HEAD under the named prefixes; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the order READS the schedule labels and cron of existing writers and changes none.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBC121-1-AC1 FAILS at base (no record) and its fresh-LIST and file-label arms are exercised on the worker's record.
</preflight>
