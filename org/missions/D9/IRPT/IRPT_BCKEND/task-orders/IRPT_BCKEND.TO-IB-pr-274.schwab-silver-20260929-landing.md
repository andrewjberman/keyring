# TO IRPT_BCKEND.TO-IB-pr-274 -- The 49 Financial Schwab silver for trading day 2026-09-29 lands, and why it missed its hour is recorded (AE lane, PARKED)

<to_id>IRPT_BCKEND.TO-IB-pr-274</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.6.2_AE_PartnerETL~C</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-30</issued_date>
<status>parked</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>lane</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO ROUND-26 ~P ANALYSIS ruling 5
(`org/missions/D9/IRPT/IRPT_BCKEND/ledger/ROUND_ANALYSIS.round26P.md` @7c9ed807bb); row S235 | **Decomp cell:** `IB-pr-274`
(decomposition section 25) | **outcome_ref:** FWD-3 (49F) | **depends_on:** none

**PARKED at issuance (the pattern CTO RULING 103327 set for MDPF_SECCLASS SC-e-12).** Owner: `0.6.2_AE_PartnerETL~C`, the lane that last
ran the 49F Schwab ingest (`/49-schwab-conv`, the skill's last-known-state line, 2026-07-24) and holds no other open order. The AE seats
were not relaunched by the 2026-09-30 13:0xZ word. Un-park condition: `0.6.2_AE_PartnerETL~C` (or any `0.6.2_AE_PartnerETL` lane Andrew
seats for the Schwab ingest) registers LIVE on the broker; the issuer's drive tick reads the condition each tick and delivers this
file's path in one message when it holds. Nothing waits on it: the 49F r3 ledger's A1 leg closes on the first SCHEDULED producer fire
that finds its silver, whichever day that is.

---

## WORKER FACE

**The cell.** The 49F Schwab silver for trading day 2026-09-29 has not landed:
`s3://opal-data-assets/schwab/08335338/silver/dim_position/date=2026-09-29/` was absent at 2026-09-30 13:3xZ and still absent at
~19:2xZ, while every earlier trading day landed at ~09:46Z the next calendar day (09-28's at 2026-09-29T09:46:44Z). The 11:30Z fire of
`irpt-holdings-performance-lambda` refused ABSENT (row S235). Run `/49-schwab-conv` for the missing day(s) exactly as the skill says
(OneDrive -> `s3://opal-data-schwab` -> the silver tables), and record WHY the 09-29 files missed their hour: were the Schwab CRS files
for 09-29 absent from OneDrive, present but not synced, or synced and not converted? Write the answer, one heading line naming the cause
then the evidence, to `org/tier2_senior/0.6.2_AE_PartnerETL~C/deliverables/SCHWAB_SILVER_20260929_CAUSE.md`. If the cause will recur
(a schedule or trigger gap), say so; the repair is its own order.

<criterion id="P27-4-AC1" cell_refs="IB-pr-274"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r27/p27_4_schwab_silver_0929.py" .</invocation><expect>P27-4-AC1 PASS</expect></criterion>
`P27-4-AC1` -- `dim_position`, `dim_balance` and `fact_trn` each hold `date=2026-09-29/data.parquet`, and the cause record exists.
Base: FAIL (dim_position 09-29 absent, read at the cut).

<expected_criteria>P27-4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file; the `/49-schwab-conv` skill's own write
  set for the missing day only.
- **Refusal clause.** If the source files for 09-29 do not exist anywhere, write that as the cause and stop; never fabricate a partition.

<paths>
org/tier2_senior/0.6.2_AE_PartnerETL~C/deliverables/SCHWAB_SILVER_20260929_CAUSE.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r27/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 25 (round 27, workstream ~P), cell `IB-pr-274`.
<owned_cells>IB-pr-274</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P27-4-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.6.2_AE_PartnerETL~C/IRPT_BCKEND.TO-IB-pr-274.schwab-silver-20260929-landing.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P27-4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** to `2.0.0_SA_COO~P` (one message, under 150 words): the commit hash, the criterion's last line, the cause heading, and any
surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- denominator: 1 producer schedule reads this silver (irpt-holdings-performance-daily, holdings-performance/schedule.tf, 07:30 America/New_York Mon-Fri); the Schwab ingest's own trigger is read by the lane as part of the cause.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the skill's AE write path is unchanged; 0 roles or policies touched.
comp-blast: RUN -- denominator: 3 silver tables x 1 date written by the skill's own path; the downstream readers (the 49F holdings producer, IRPT_DASHBD's adapter) read the day on their next run.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache.
comp-adversary: RUN -- P27-4-AC1 base FAIL (dim_position 2026-09-29 absent), measured at the cut.
seating: 0.6.2_AE_PartnerETL~C holds 0 open orders (to-check --all at the cut); parked until the seat is LIVE.
lane: the <paths> block IS the grant.
</preflight>
