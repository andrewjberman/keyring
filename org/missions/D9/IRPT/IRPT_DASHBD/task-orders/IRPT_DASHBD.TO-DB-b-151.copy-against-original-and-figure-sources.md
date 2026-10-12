# TO IRPT_DASHBD.TO-DB-b-151 -- the transactions copy is not the original: object metadata and row counts of both on the three sampled days, whether the original was rewritten after the copy was taken, and every figure of the tie-out records named with the store it was read from

<to_id>IRPT_DASHBD.TO-DB-b-151</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~124</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>79</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-78 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_78_20261011.md` @0ffc0f24e6, section 3 item 3, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v33.md` @7c237a67ec | **Rows:** IRPT_DASHBD-D2-W116-S2 | **Decomp cell:** `DB-b-151` (decomposition section 81) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** DB-b-143 and DB-b-145 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-124` (branch `wk-irpt-dashbd-79-124`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~124/`. Read first: section 2 of the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v33.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**Why.** The decomposition of the project that made the Black Diamond transactions copy calls it byte-identical to the original.
DB-b-143 found, on three sampled days and by metadata only, that the original object and the copy differ in size and ETag (row
W116-S2). This project's tie-out figures were read from the COPY; its shape claims about the ORIGINAL rest on one other day. The CTO:
"Every figure of this project's records taken from the transactions copy says which of the two stores it was read from. One read of the
reason on the three sampled days: object metadata and row counts of both, no amount; whether the original was rewritten after the copy
was taken."

**The cell (`DB-b-151`).** A read. You change no code and edit no other worker's record.
1. **The three days.** From `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~116/ORIGINAL_STORE_SHAPE.json` (and that worker's private
   script under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~116/`) take the two addresses and the three days. For each day and each
   store: `head-object` (size, ETag, LastModified, and the version id if any), then one narrow read for `rows` and `distinct_ids`.
   `days`: [{day, original {read, rows, distinct_ids, last_modified, size}, copy {read, rows, distinct_ids, last_modified, size,
   objects (the copy may hold a day in more than one object: say how many)}, rows_equal, ids_equal}].
2. **Was the original rewritten after the copy was taken?** `original_rewritten_after_copy` (true, false or "NOT_ESTABLISHED") with
   `rewritten_reason`: the evidence is the two LastModified stamps, the bucket's versions if it keeps them, and what the code that
   writes the original does on a re-run (read it: `merge-daily-incremental.py` and what calls it). State which of those you read. If
   the copy holds rows the original does not, or the reverse, say how many ids, as counts.
3. **Every figure names its store.** DB-b-145's list is the denominator: the 42 figures in
   `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~118/FIGURE_PRODUCERS.json`. For each, read its tracked producing script (in that
   worker's `producers/` folder) and name the store its number was READ from: `COPY` (the `silver_legacy` transactions copy),
   `ORIGINAL`, `FEED` (the custodian feed the served flow is built from), `SERVED_GOLD`, `CUSTODIAN_PULL` (the reporting-performance
   pull), `DERIVED` (computed from other figures of the same record, no store read) or `WITHDRAWN` (the three). A figure read from
   more than one store names the one its number depends on and lists the others in `also`. `figure_sources`: [{record, figure,
   store, also, script, line}], 42 entries, and `by_store` counts.
4. `s3_writes: 0`. No account id, client name or amount; write days with separators; the check refuses a record holding any run of 8
   or more digits. Private files go under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~124/`. Record `COPY_VS_ORIGINAL.json`.

<criterion id="DB79-1-AC1" cell_refs="DB-b-151"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r79/p79_round79.py" . DB79-1-AC1</invocation><expect>DB79-1-AC1 PASS</expect></criterion>
`DB79-1-AC1` -- the copy and the original are compared on the three sampled days by metadata and row count, the rewrite question is answered or stated not established, and all 42 figures name the store they were read from. Base: FAIL.

<expected_criteria>DB79-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim or boto3 as the existing readers build their client, and nothing else: for the THREE days DB-b-143 sampled (2026-08-22 to 2026-08-24), `head-object` of the original's object and of the copy's object or objects for that day, `list-object-versions` limited to those keys if the bucket is versioned, and ONE read of each object with a projection of the transaction id and the portfolio group only, to count rows and distinct ids. NO money column, NO account column. Both addresses from the code and records that name them, never typed. A denial is recorded verbatim, not retried by another route.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~124/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W124-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~124/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-151.copy-against-original-and-figure-sources.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 81 (round 79), cell `DB-b-151`.
<owned_cells>DB-b-151</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB79-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~124/IRPT_DASHBD.TO-DB-b-151.copy-against-original-and-figure-sources.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB79-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; ONE table of the three days: rows, distinct ids and last-modified of the original and of the copy, and whether they agree; whether the original was rewritten after the copy was taken and how you know; how many of the 42 figures were read from each store; what you could not establish; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; metadata and counts of six objects and a table of sources; nothing is changed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; governed reads; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
