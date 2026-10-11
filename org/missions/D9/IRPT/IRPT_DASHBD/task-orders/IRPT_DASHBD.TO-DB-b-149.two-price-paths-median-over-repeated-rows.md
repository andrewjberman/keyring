# TO IRPT_DASHBD.TO-DB-b-149 -- the two price paths that take a median over un-deduplicated Black Diamond rows and SERVE a price: what each serves and to whom, and whether the median moves on one day when each transaction id is counted once -- a read

<to_id>IRPT_DASHBD.TO-DB-b-149</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~122</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>78</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 5827 (2026-10-11 ~20:52Z), first item | **Rows:** IRPT_DASHBD-D2-W113-S2 | **Decomp cell:** `DB-b-149` (decomposition section 80) | **outcome_ref:** every consumer of those two price paths | **depends_on:** DB-b-143 (drained @cf125a14d4).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-122` (branch `wk-irpt-dashbd-78-122`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~122/`. Read first: each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`, and the records this order names.

**Why.** DB-b-143 found that the original Black Diamond transactions store repeats a transaction once per portfolio group, and that no
reader which SERVES an amount sums without the transaction id. Two readers do not sum: they take a MEDIAN over un-deduplicated rows and
serve a PRICE (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~116/ORIGINAL_STORE_SHAPE.json` names them: `bd_price_update.py` near line
265, and the Lambda `bd-price-update/lambda_function.py` near line 143). A median over rows where some transactions are repeated k
times is a weighted median: it may or may not move. The CTO: "one cell, read only, naming what each serves and to whom, and whether
the median moves when ids are counted once, on one day."

**The cell (`DB-b-149`).** A read. You change no code and write no price anywhere.
1. **Trace each path.** `paths`: [{file, line (the median), reads (store and columns), groups_by (what one median is taken over:
   per security, per date, ...), serves (the table, object or page its price lands in, followed to the first served thing), to_whom
   (which product or firm reads that), scheduled (does a schedule run it today: read the Terraform or scheduler definition, DESIRED
   versus what you can see APPLIED; say which you read), owner}]. Cite file and line.
2. **One day, both ways.** For one recent day, compute each path's medians exactly as the path does (same columns, same grouping,
   same filters: read its code), then again with each transaction id counted once. `medians` {compared, moved (the two differ beyond
   rounding to the price's own precision), unmoved}, and `bands`: counts of the moved medians by relative size of the move. If the
   two paths compute the same medians, say so and compare once. If you cannot reproduce a path's computation from its code,
   `measured: false` with the reason; do not approximate it.
3. A path whose served price moves is ONE ROW naming its owner (class OBSERVATION; it is that owner's to correct, and this cell
   corrects nothing). `s3_writes: 0`. No price, amount or account value in the repo or the report; the check refuses a record holding
   any run of 8 or more digits. Private files go under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~122/`. Record
   `PRICE_PATHS_MEDIAN.json`.

<criterion id="DB78-2-AC1" cell_refs="DB-b-149"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r78/p78_round78.py" . DB78-2-AC1</invocation><expect>DB78-2-AC1 PASS</expect></criterion>
`DB78-2-AC1` -- each of the two price paths is traced to what it serves and to whom, and on one day the medians are compared with and without counting each transaction id once, as counts. Base: FAIL.

<expected_criteria>DB78-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim or boto3 as those two paths build their client, and nothing else: ONE day of the original Black Diamond transactions store (`opal-data-bd`, the address from the paths' own code, never typed), read with exactly the columns the two paths themselves read to form a price, plus the transaction id. Prices are market data, not client data, but NO price value is written into the repo or the report: counts of medians compared and moved only. No account column is read. A denial is recorded verbatim, not retried by another route, and `medians.measured` is false with the reason.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~122/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W122-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~122/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-149.two-price-paths-median-over-repeated-rows.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 80 (round 78), cell `DB-b-149`.
<owned_cells>DB-b-149</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB78-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~122/IRPT_DASHBD.TO-DB-b-149.two-price-paths-median-over-repeated-rows.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB78-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; for each of the two paths: file and line of the median, what it serves, to whom, and whether it runs on a schedule; the day; how many medians you compared, how many moved and how many did not, and the largest relative move as a band (for example under 0.1 percent, 0.1 to 1 percent, over 1 percent) with counts per band; what you could not establish; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one read of one day and a code trace; nothing is changed, no price is written anywhere.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one governed read; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
