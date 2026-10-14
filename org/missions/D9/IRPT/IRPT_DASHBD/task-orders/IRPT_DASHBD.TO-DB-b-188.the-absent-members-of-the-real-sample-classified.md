# TO IRPT_DASHBD.TO-DB-b-188 -- READ: every absent member of the real 49 Financial report sample classified as (a) mappable from an existing gold table now, (b) derivable from gold by one rule already in a ratified method, or (c) truly absent with the gold table that would hold it; read only

<to_id>IRPT_DASHBD.TO-DB-b-188</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~153</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>101</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 7451, ENRICHMENT item 2 ("The 73 ABSENT members, measured before anything is built ... Print the denominator") | **Rows:** IRPT_DASHBD-D2-W153-S<k> | **Decomp cell:** `DB-b-188` (decomposition section 103) | **outcome_ref:** FWD-21 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-153` (branch `wk-IRPT_DASHBD-153`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~153/`.

**The denominator is the sample's, and it is 62, not 73.** The CTO's message and an earlier issuer note say 73; the issuer re-counted the real sample: of the contract's 117 members, 55 hold a value and **62 hold the absent form** (`{"absent": "<reason>"}`). Of those 62, **46** are members the contract itself sources `ABSENT` (`source` equals the string "ABSENT") and **16** are members the contract sources from gold but the sample could not fill ("history not yet built": gold `account_activity_daily` holds 4 trading days; or a window that cannot open). Your record states the 62 and the checker recomputes the set from the sample.

**What the report is.** FWD-21's default performance report: the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (117 `members`, each `{id, section, baseline, label, unit, source}`; a sourced member's `source` is an object naming its gold table and fold; an absent one carries its reason). The filled real sample (client data, private, read-only, sha256 `76a48793d6979ba66358d4e1d2cdc3d59d34c9a5217df1b7b421715925ddf16d`) is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~141/HOUSEHOLD_SAMPLE.json`: top-level `household` and `values`; `values` maps each member id to a figure, a text, a `{"by_row": ...}` map, a series, or `{"absent": "<reason>"}`. The builder that made it is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~141/build_sample.py` (read its header: the folds, and why each member it left absent is absent). The gold tables' contracts are the files `org/standards/IRPT_DASHBD_*_CONTRACT.json` (one per C-SHAPE table: `account_return_daily`, `account_class_daily`, `account_activity_daily`, `account_transaction`, `account_lot_realized`, `account_lot_unrealized_daily`, `account_dim`, `market_topic_daily`; list the ones that exist). The gold tables themselves for 49 Financial sit under `s3://opal-data-49financial/irpt/49financial/gold/` (address them with `lib/opal_naming.py` `address()`, read `lib/opal_naming.py`'s own header first; S3 LIST and GET only, parquet SCHEMA and partition names only, no figure).

**The cell (`DB-b-188`): a READ. Nothing is changed, deployed or written (outside your folder).**
1. Read the contract, the sample's absent set, the builder's header and the sibling table contracts. For each of the 62 absent members decide ONE class:
   - **(a) mappable now:** an existing gold table already holds the figure under C-SHAPE (a column in a sibling contract, and the table is built for this firm) and the contract's fold for the member can be applied to it by the builder today. Evidence: `{table_contract (the org/standards/*_CONTRACT.json path), column (a column name that appears in that file), fold (one sentence: how the column maps to the member)}`. Do NOT classify as (a) a member whose source table holds too little history to fill it (for example anything that needs 12 months of activity while `account_activity_daily` holds 4 trading days): that is (c).
   - **(b) derivable by a ratified rule:** no single column holds it, but one rule already written in a ratified method derives it from gold columns (for example a fold in the contract's own text, or a method file under `org/standards/` or `docs/`). Evidence: `{method_ref (an existing file path), rule (the rule in one or two sentences)}`.
   - **(c) truly absent:** nothing in gold or a ratified rule produces it today. Evidence: `{holder (the gold table or source that WOULD hold it, in words), reason (why it is absent today, in words)}`.
2. `state_now` per member: `"contract_absent"` when the contract sources it ABSENT, `"sourced_unfilled"` otherwise (the checker verifies this).
3. **Record** `ABSENT_CLASSIFICATION.json` in your folder with exactly: `sample_sha256` (the sample's sha256 above); `denominator` (62); `members` (one entry per absent member id, once each: `{id, state_now, class, evidence}`); `counts` {`a`, `b`, `c` : integers summing to the denominator}; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, ids and words only: no figure, no account number, no run of eight or more digits.
4. Print in your report the denominator beside each count (a, b, c of 62) and, for (a), what the builder must do (one clause per member group, not per member).

<criterion id="DB101-2-AC1" cell_refs="DB-b-188"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r101/p101_round101.py" . DB101-2-AC1</invocation><expect>DB101-2-AC1 PASS</expect></criterion>
`DB101-2-AC1` -- the record is bound to the unchanged real sample; its members are exactly the sample's absent member ids, once each, with the right `state_now`; every (a) cites an existing table contract and a column that appears in it; every (b) cites an existing method file and a rule; every (c) names its holder and reason; the counts equal the tally and sum to the denominator; no write, push or deploy; no run of 8 or more digits. Base: FAIL (no record).

<expected_criteria>DB101-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the contract, the sample and the builder.
- **No write of any kind to AWS** (no S3 put/copy/delete, no DynamoDB write, no Lambda, Terraform or IAM act), **no deploy, no push, no vendor call, no secret read.** Reads only: repo files, the private sample, S3 LIST and GET of the gold tables' partition names and parquet schemas. If the comp-rail hook refuses a raw S3 call, run what it says next, or annotate `# rail-checked: <why>` (audited). A denial is recorded verbatim, not retried by another route.
- **Client data.** The sample is client data: it never goes in the repo, a row, a message or your report. Ids, counts and words only.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. When you cannot decide between classes, choose the more conservative (c over b over a) and say why in the evidence. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W153-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~153/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-188.the-absent-members-of-the-real-sample-classified.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 103 (round 101), cell `DB-b-188`.
<owned_cells>DB-b-188</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB101-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~153/IRPT_DASHBD.TO-DB-b-188.the-absent-members-of-the-real-sample-classified.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB101-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the counts a, b, c of 62 and how many of each are contract_absent and sourced_unfilled; for (a) what the builder must do, one clause per member group; for (b) the rules you cite; for (c) the gold tables that would hold them, grouped; any row ids. Counts, ids and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read; nothing is changed, deployed or written.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: repo reads and, at most, S3 LIST/GET with the box's existing identity.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and is dry-run on 8 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>
