# TO IRPT_BCKEND.TO-IB-pr-318 -- one read-only readers census of the 49F perfrp leaf (W100-S2, CTO batch 247 item 1)

<to_id>IRPT_BCKEND.TO-IB-pr-318</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~121</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>49</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO RULINGS batch 247 item 1 (msg 105044): "`~P` runs one read-only readers
census: router and CloudFront paths, plus portal code referencing the key. The census goes on the row." | **Decomp cell:**
`IB-pr-318` (decomposition section 43) | **outcome_ref:** FWD-8 | **depends_on:** none.

---

## WORKER FACE

**The leaf.** `s3://opal-data-portal-v2/platinum/advi/49financial/perfrp_performance_account.json`: LastModified
2026-09-01T03:16:07Z, 1,923,593 bytes. It still carries the inflated 2025-01-10 day. It belongs to ADVI_PERFRP (that project's D2
hold), and PATH B, not the leaf, serves 49F on the investor-reporting pages. The question: does anything still READ this leaf?

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-121`. Run everything from its root. All reads, no writes anywhere but
your deliverables folder and one channel row.

**What you read, recording each surface with what you searched and its denominator (how many items were examined):**
1. **CloudFront:** the distributions serving `opalinvest.dev` and the portal origin. List every cache behavior's path pattern and
   origin (boto3 `cloudfront.get_distribution_config`), and record whether any behavior can serve `platinum/advi/49financial/`
   from `opal-data-portal-v2`.
2. **API routes / router:** any route or Lambda that reads `perfrp_performance_account` or `platinum/advi/` (search
   `infra/aws/lambda/`, `infra/aws/terraform/` and `org/modules/graph/` with the native Grep tool; record the file count searched).
3. **Portal code at PROD:** the portal at `c69b4747` (`git -C portal show c69b4747:<path>`, or `git -C portal grep -n
   'perfrp_performance_account\|platinum/advi' c69b4747 -- src`). Record which files reference the key and which page or route
   loads them.
4. **Recent reads, if cheap:** whether S3 server access logs or CloudTrail data events exist for that bucket (just whether they
   exist; do not enable anything).

**What you produce:**
- `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~121/W100S2_READERS_CENSUS.json` holds:
  - `leaf`;
  - `surfaces`: a list of `{name, searched, denominator, readers: [...]}`;
  - `verdict`: `NO_READER` or `LIVE_READER`;
  - `evidence`: the reads that decide the verdict.

  **LIVE_READER** means a served page or route can still load the leaf.
- **One row** appended to `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id
  `IRPT_BCKEND-W121-S1`. It names `IRPT_BCKEND-W100-S2`, with the verdict and the census path:
  - **NO_READER:** OBSERVATION / INERT, `disarm_owner` the ADVI_PERFRP owner (`2.0.0_SA_COO`), the re-point per batch 247.
  - **LIVE_READER:** BLOCKING / ARMED, `disarm_owner` `2.0.0_SA_COO~P`; the issuer brings the withdrawal packet to the CTO.

<criterion id="IB49-2-AC1" cell_refs="IB-pr-318"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r49/p49_cells.py" . IB49-2-AC1</invocation><expect>IB49-2-AC1 PASS</expect></criterion>
`IB49-2-AC1` -- the census holds the leaf, its surfaces each with what was searched and a denominator, the verdict and the
evidence; and a channel row added since base names W100-S2. Base: FAIL.

<expected_criteria>IB49-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** reads only. No S3 write or delete, and no logging or CloudTrail change.
- **Refusal clause.** Any write to AWS, or any change to the leaf, is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~121/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-318.w100-s2-perfrp-readers-census.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 43 (round 49, workstream ~P), cell `IB-pr-318`.
<owned_cells>IB-pr-318</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB49-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~121/IRPT_BCKEND.TO-IB-pr-318.w100-s2-perfrp-readers-census.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB49-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, the verdict with its deciding evidence, each surface's denominator, the
criterion's last line, and the row id.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read-only census; 0 served bytes move.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only.
comp-routes: RUN -- CloudFront behaviors and API routes are READ to find readers; none is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: CloudFront config is read, never changed.
comp-adversary: RUN -- IB49-2-AC1 base FAIL (no census), dry-run at base b77b84cbb4 2026-10-05 ~00:5xZ.
lane: the <paths> block IS the grant.
</preflight>
