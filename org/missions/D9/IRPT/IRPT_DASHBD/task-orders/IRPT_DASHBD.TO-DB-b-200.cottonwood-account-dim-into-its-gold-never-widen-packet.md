# TO IRPT_DASHBD.TO-DB-b-200 -- COTTONWOOD account_dim INTO ITS address() GOLD: the NEVER-WIDEN PACKET for the one write (the exact keys, the rollback, that no other key moves); a read and a packet, nothing is written to AWS

<to_id>IRPT_DASHBD.TO-DB-b-200</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~165</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>104</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-104 ANALYSIS item 3 ("Cottonwood `account_dim` and the household key into its `address()` gold. Each packet names the exact keys written, the rollback, and that no other key moves.") | **Rows:** IRPT_DASHBD-D2-W165-S<k> | **Decomp cell:** `DB-b-200` (decomposition section 106) | **outcome_ref:** FWD-21, FWD-2 | **depends_on:** none (round 103's `DB-b-196` built the contract, the adapter and a read-only dry run).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-165` (branch `wk-IRPT_DASHBD-165`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~165/`.

**Why.** Cottonwood's gold has one of the eight C-SHAPE tables (`account_return_daily`); `account_dim` and the household key (the Black Diamond relationship id) are the adapter's first table. Round 103 built the contract `org/standards/IRPT_DASHBD_ACCOUNT_DIM_CONTRACT.json`, the adapter `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_account_dim.py` (its tests pass, an `upload=False` default) and a read-only dry run on Cottonwood's own silver (999 accounts, 223 household keys; record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~161/COTTONWOOD_ACCOUNT_DIM.json`). Landing the table in Cottonwood's gold is a gold WRITE under a never-widen pair. This cell writes the packet that pair rests on (the COO half is the issuer's, the CTO half is the CTO's) and writes nothing to AWS.

**The cell (`DB-b-200`): a READ and a PACKET.**
1. **Read.** The contract, the adapter and its tests, the dry-run record, the model packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PACKET_FDRXX_CASH_CLASSIFIER.md` (its numbered sections are the packet's required headings), the 49 Financial gold producer `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (`emit_day`: what a partition's write is: `data.parquet` and `manifest.json`, how the 49F production Lambda is deployed and scheduled), and Cottonwood's gold today (named-prefix LIST of `s3://opal-data-cottonwood/irpt/cottonwood/gold/` top level and of `.../gold/account_dim/` to prove it is empty; the bucket from `lib/opal_naming.py address()` only, never the registry's bucket field; a live `get-bucket-versioning` of that bucket). Find who writes under that gold home today (the `account_return_daily` producer, the holdings builders): your list of WRITERS of the `account_dim` prefix is the count the pair needs (expected none: verify, do not assume).
2. **The packet.** `ACCOUNT_DIM_GOLD_PACKET.md` in your folder with the numbered sections the checker looks for: `## 1. The act` (ONE apply: one `date=` partition of `account_dim` (the newest silver date the dry run used, as the adapter computes it) written to `s3://opal-data-cottonwood/irpt/cottonwood/gold/account_dim/date=<D>/` as `data.parquet` and `manifest.json`, by an AE applier with the exact invocation shape of the adapter's upload path, no live run; if the adapter has no upload path yet, say what the applier's order must add and why it is not a rider on this packet), `## 2. What moves` (the counts: accounts, household keys, nulls per column; nothing served changes: no page reads `account_dim` yet), `## 3. When and where` (no schedule is touched by this apply; the table's own schedule is a later packet), `## 4b. Writers` (every writer of the target prefix, counted: N is printed), `## 5. Both branches` (the write lands; the write fails after `data.parquet` and before `manifest.json`: what a partial partition looks like and how it is detected), `## 6. Rollback` (per key: delete the two new keys; the bucket's versioning state as read; confirm NO other key moves: the prefix is empty today and nothing else is written), `## 7. Conditions` (ledger first; live bytes re-read: the prefix still empty at the moment of the apply, else STOP; the adapter's tests and an import smoke at the pinned commit first; no other table written; the questions for the CTO's half, including whether the four dimension fields the silver does not carry (client id, tax status, opened date, first data date) ship as nulls with a coverage value), `## 8. Not established`. The packet says "never-widen".
3. **Record** `ACCOUNT_DIM_GOLD_PACKET.json` in your folder with exactly: `address_args` (`["irpt", "cottonwood", "gold", "account_dim", "date=2026-10-12"]`, the five `address()` arguments of the partition the dry run named: use the partition date the adapter computes); `keys_written` (`[{bucket: "opal-data-cottonwood", prefix: "irpt/cottonwood/gold/account_dim/", objects_per_partition: 2}]`); `rollback` (words); `no_other_key_moves` true; `writes_in_this_cell` false; `counts` {`accounts`, `relationship_ids`, `partitions_written_by_the_apply` (1)}; `adapter_file` and `adapter_sha256` (of the adapter at HEAD); `applier` (the AE seat class, in words); `run_command_shape` (the exact invocation shape, no live run); `writers_of_the_property` (a list: the counted writers); `both_branches` (words); `packet_file` and `packet_sha256`; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, names and words only; a sha256 value is exempt from the digit rule.

<criterion id="DB104-4-AC1" cell_refs="DB-b-200"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r104/p104_round104.py" . DB104-4-AC1</invocation><expect>DB104-4-AC1 PASS</expect></criterion>
`DB104-4-AC1` -- the address arguments are the five address() arguments of the Cottonwood account_dim partition and every key written is in opal-data-cottonwood under irpt/cottonwood/gold/account_dim/; the rollback is stated, no other key moves, nothing is written in this cell; accounts, relationship ids and the partitions the apply writes are counted above 0; the adapter at HEAD hashes as recorded and the applier, the exact run-command shape, the counted writers and both branches are stated; the packet file exists, is hashed, says never-widen and carries the eight numbered sections; no write, push or deploy. Base: FAIL (no record).

<expected_criteria>DB104-4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the adapter, the contract and the dry-run record.
- **No write of any kind to AWS** (no S3 put/copy/delete, no DynamoDB write, no Lambda, EventBridge, Terraform or IAM act, no run of the adapter's upload path), **no deploy, no push, no vendor call, no secret read.** Reads only: repo files; S3 named-prefix LIST of Cottonwood's own gold prefix and `get-bucket-versioning` with the box's existing identity. Never another firm's data. A denial is recorded verbatim, not retried by another route. If the comp-rail hook refuses a raw S3 call, run what it says next or annotate `# rail-checked: <why>`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Where you cannot establish something say NOT_ESTABLISHED with the reason; never guess. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W165-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~165/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-200.cottonwood-account-dim-into-its-gold-never-widen-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 106 (round 104), cell `DB-b-200`.
<owned_cells>DB-b-200</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB104-4-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~165/IRPT_DASHBD.TO-DB-b-200.cottonwood-account-dim-into-its-gold-never-widen-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB104-4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the keys and the partition; the counted writers of the prefix; the bucket's versioning state; the rollback; whether the adapter has an upload path and what the applier needs; what is not established; row ids. Counts, names and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a packet document; nothing is written, served or deployed; the apply is a later WORLD order under a pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: named-prefix LIST of one firm's own gold and a versioning read with the box's existing identity; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and is dry-run on 3 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>
