# TO IRPT_DASHBD.TO-DB-b-154 -- how bad the moved medians are: of the 34 medians of 2026-10-09 that move when each transaction id is counted once, how many are the final served price, how many of those assets are held on a served account-day, the two over 1 percent by the same test, and whether the script path runs today

<to_id>IRPT_DASHBD.TO-DB-b-154</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~125</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>80</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 5878 (2026-10-11 ~21:37Z) | **Rows:** IRPT_DASHBD-D2-W122-S1 | **Decomp cell:** `DB-b-154` (decomposition section 82) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** DB-b-149 (drained @23a2226433).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-125` (branch `wk-irpt-dashbd-80-125`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~125/`. Read first: each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`, and the records this order names.

**Why.** DB-b-149 found that both Black Diamond price paths take a median price per asset over every row of the day object, and
the object repeats a transaction once per portfolio group: on 2026-10-09, 34 of 160 medians move when each id is counted once (row
`IRPT_DASHBD-D2-W122-S1`; record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~122/PRICE_PATHS_MEDIAN.json`). It could not say which of
the 34 reached a served price. The CTO (msg 5878): "One more read in this project, read-only, counts only, because it sets the
severity: of the 34 moved medians on 2026-10-09, how many are the FINAL served price for their asset (no Yahoo price and no override
outranking them), how many of those assets are held on a served account-day, and the two over 1 percent by that same test. And whether
the script path runs today or only the Lambda." The pipeline belongs to another fabric (dell1); this read goes to its owner. You edit
no producer and correct nothing.

**The cell (`DB-b-154`).** A read.
1. **Rebuild the 34.** Start from DB-b-149's private script and result under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~122/`
   (read them; re-run the comparison if the list of moved assets was not saved). Confirm 160 compared and 34 moved, or say what differs.
2. **Final served price.** Read the precedence in the code of both paths (`data/black_diamond/scripts/silver/bd_price_update.py` and
   `infra/aws/lambda/bd-pipeline/bd-price-update/lambda_function.py`): which tier wins for an asset (override, Yahoo close, the
   transaction median), cite file and line for each path, and say where the two paths differ. Then read the SERVED price objects for
   that day and, for each of the 34, decide from the served row itself (its source or tier column if it has one, else by comparing the
   served price with the median at the paths' own precision) whether the median IS the served price. `final_served`: {count,
   outranked_by_yahoo, outranked_by_override, not_placed, basis}; the four sum to 34. If the served object carries no way to tell, the
   count is "NOT_ESTABLISHED" and the basis says exactly what is missing.
3. **Held on a served account-day.** Of the final-served assets, how many appear in the gold holdings the price feeds (the object
   B_01 `holdings_lots` writes, or A_03's cube) for that day, by asset key only. `held_on_served_account_day`: {count, basis (which
   object, which key joined, how many of the assets joined at all)}. No account id, no value.
4. **The two over 1 percent** by the same two tests: `over_one_percent`: {moved: 2, final_served, held, basis}.
5. **Does the script path run today?** DB-b-149 found a manifest claiming a weekday run and an SSM document with no price step (row
   W122-S2). Establish it from live state: the Lambda's newest log event against the last write time of the two price objects, and any
   schedule or document that invokes the script. `script_path_runs_today`: {answer (true, false or "NOT_ESTABLISHED"), basis}.
6. `day`, `moved: 34`, `s3_writes: 0`, `limits`. NO price value, no asset name, no account id, no client name in the record or your
   report: counts and bands only. Write days with separators; the check refuses a record holding any run of 8 or more digits.
   Private files go under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~125/`. Record `MOVED_MEDIANS_SEVERITY.json`.

<criterion id="DB80-1-AC1" cell_refs="DB-b-154"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r80/p80_round80.py" . DB80-1-AC1</invocation><expect>DB80-1-AC1 PASS</expect></criterion>
`DB80-1-AC1` -- the 34 moved medians are split into final served price and outranked, the held count and the two over 1 percent are stated by the same test, and whether the script path runs today is answered, each with its basis or stated not established. Base: FAIL.

<expected_criteria>DB80-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim or boto3 as the existing readers build their client, and nothing else, all in the ONE firm's Black Diamond bucket that DB-b-149 read: the day object of 2026-10-09 (the same columns DB-b-149 read, to rebuild the list of 34), the served price objects for that day (`silver/prices/canonical_prices.parquet` and the daily price file: asset key, price and its source or tier column), the override and ticker-lookup objects the two price paths read, and the gold holdings object the price feeds for that day projected to the ASSET key only (no account, no value, no quantity). For whether the script runs: `describe-log-streams` / `get-function-configuration` on `bd-price-update`, and a read of the SSM document or schedule that would run the script. A denial is recorded verbatim, not retried by another route.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~125/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W125-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~125/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-154.moved-medians-severity-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 82 (round 80), cell `DB-b-154`.
<owned_cells>DB-b-154</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB80-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~125/IRPT_DASHBD.TO-DB-b-154.moved-medians-severity-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB80-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; of the 34, how many are the final served price, how many are outranked by Yahoo and how many by an override, and how many you could not place; how many of the final-served ones are held on a served account-day; the same two answers for the two over 1 percent; whether the script path runs today and how you know; what you could not establish; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; counts of assets; nothing is changed, no producer is edited.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; governed reads; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
