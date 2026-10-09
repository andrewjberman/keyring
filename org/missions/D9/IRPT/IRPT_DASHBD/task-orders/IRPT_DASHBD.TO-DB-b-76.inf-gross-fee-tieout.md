# TO IRPT_DASHBD.TO-DB-b-76 -- E4: Inflection's like-for-like tie-out -- Opal's compounded GROSS return against Orion's GROSS return for the same window, with fees as their own figures sliced supervised/unsupervised/total and billed/unbilled/total (Andrew @669ab7d677)

<to_id>IRPT_DASHBD.TO-DB-b-76</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~53</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>37</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-36 ADDENDUM 5 (on ADJUDICATION_v21 @37daf4f637; PRD v0.9 @e8f96f579c), enrichment item E4 | **Decomp cell:** `DB-b-76` (decomposition section 39) | **outcome_ref:** FWD-11 | **depends_on:** none (DB-b-75 helps but is not required: the legacy alias still reads).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-53`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~53/`.

**The cell (`DB-b-76`).** Andrew-direct ~04:2xZ, record
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/ANDREW_DIRECT_20261009_042xZ_ORION_FEE_ENDPOINT_GROSS_AND_FEES_LIKE_BD.md` (read it whole): Inflection gets GROSS returns and
its fees as their own figures, sliced as 49 Financial's Black Diamond is. Round 36 (DB-b-72) compared against Orion's NET TWR:
- 24 of 562 within 0.35 pp on gross;
- 421 of 562 with the fee left in;
- row W49-S2.

1. **The adapter.** Start from round 36's adapter
   `deliverables/0.9.0_WK_IRPT_DASHBD~49/orion_account_return_daily.py` and `orion_sources.json`, copied into your folder.
   - Map flows by the RATIFIED `data/inf/scripts/silver/orion_cashflow_taxonomy.yaml` (CTO ADDENDUM 5, W49-S3).
   - Flag the two departing classes (the Internal Account Journal pair; Federal/State Tax Withheld) in the output with their counts.
   - Record `flagged_classes`.
2. **Orion's gross return.** `data/inf/manual_api/PATH_DISCOVERY.md:124`: gross vs net is a query-level `performanceOptionId` in
   `contextChange`, with `Performance.Value`; it is not a path. Read the gross figure for the sampled accounts and window, from S3 if it
   is landed. Otherwise pull it read-only from Orion's query API.
   - Tie out like for like: the same window, the same annualization, Opal's compounded gross against Orion's gross, at 0.35 pp.
   - Record `comparison_basis` "gross", `comparison_source`, `accounts`, `denominator`, `within`, `tolerance_pp`, `classes` and
     `misses`.
3. **Fees.** Name Orion's fee endpoint as `fee_source`. Candidates:
   - `Activity.Value` with `activityOptionId` 11 (Advisory Fees Paid), `PATH_DISCOVERY.md:181`;
   - the `Billing.*` paths at lines 160-175;
   - `data/inf/manual_api/orion_billing_dim.py`;
   - the one fee-classification home, `data/inf/scripts/gold/lib/fee_classification.py`.

   Report `fee_slices` for the sample's window: `supervised`, `unsupervised`, `supervision_total`, `billed`, `unbilled`,
   `billing_total`. Each is a number, or `"ABSENT: <what was searched and not found>"`. `Asset.IncludedInBilling` is flagged broken for
   some accounts (line 158): say how many.

Record `INF_GROSS_FEE_TIEOUT.json`. Keep the parquet in `.scratch/`. Hashed account keys only.

<criterion id="DB37-4-AC1" cell_refs="DB-b-76"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r37/p37_round37.py" . DB37-4-AC1</invocation><expect>DB37-4-AC1 PASS</expect></criterion>
`DB37-4-AC1` -- Opal gross vs Orion gross, within count at 0.35 pp with its denominator and account count. Base: FAIL.

<criterion id="DB37-4-AC2" cell_refs="DB-b-76"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r37/p37_round37.py" . DB37-4-AC2</invocation><expect>DB37-4-AC2 PASS</expect></criterion>
`DB37-4-AC2` -- Orion's fee source named and all six fee slices reported, each a figure or ABSENT with what was searched. Base: FAIL.

<criterion id="DB37-4-AC3" cell_refs="DB-b-76"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r37/p37_round37.py" . DB37-4-AC3</invocation><expect>DB37-4-AC3 PASS</expect></criterion>
`DB37-4-AC3` -- every miss classed, and the two departing flow classes flagged with counts. Base: FAIL.

<expected_criteria>DB37-4-AC1,DB37-4-AC2,DB37-4-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception (law 4d77a9c3ea: egress open except Bloomberg; Andrew's order @669ab7d677 names Orion's endpoint):** READ-ONLY
  calls to Orion's query API for Inflection are permitted, with the Orion credential read from its secret for the call only.
  - Never print, write or commit the credential.
  - No write call to Orion.
  - Bloomberg stays barred.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~53/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-76.inf-gross-fee-tieout.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 39 (round 37), cell `DB-b-76`.
<owned_cells>DB-b-76</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB37-4-AC1, DB37-4-AC2, DB37-4-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~53/IRPT_DASHBD.TO-DB-b-76.inf-gross-fee-tieout.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB37-4-AC1,DB37-4-AC2,DB37-4-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the gross within count and denominator, the fee source and six slices, the flagged classes, and every row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: offline records and code in the worker folder; nothing served, deployed or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB37-4-AC1/AC2/AC3 FAIL at base (no record). Rows W49-S2/S3; Andrew @669ab7d677; CTO ADDENDUM 5.
lane: the <paths> block IS the grant.
</preflight>
