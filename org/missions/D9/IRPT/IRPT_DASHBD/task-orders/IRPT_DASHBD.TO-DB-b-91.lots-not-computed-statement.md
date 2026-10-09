# TO IRPT_DASHBD.TO-DB-b-91 -- E2: a skipped lots day is STATED, never an empty table -- the reporting-gold handler records each refused lots day as 'lots not computed for <date>: <reason>' in a status record the serving page reads, without the record being taken for a landed day (S40)

<to_id>IRPT_DASHBD.TO-DB-b-91</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~66</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>44</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 11 (msg 3288; CVO ADJUDICATION_v25 @5f365678bf), enrichment item E2 | **Decomp cell:** `DB-b-91` (decomposition section 46) | **outcome_ref:** FWD-4 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-66`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~66/`.

**The cell (`DB-b-91`).** The R37 fire of 11:41Z logged `LOTS_SKIPPED 2026-10-08` (row S40). The CTO ruled (ADDENDUM 11, item 1) that every day a
lots stage skips is STATED on the page that serves lots, as "lots not computed for <date>: <reason>", never as an empty table. No page serves the
lots tables yet, so the statement must live in the data that page will read.

1. In `C:/dev/wk-irpt-dashbd-66/infra/aws/lambda/investor-reporting/reporting-gold/handler.py`, on a refused lots day, write the statement
   "lots not computed for <date>: <reason>" into a status record under the lots tables' own prefixes, inside the role's existing PutObject write
   set: no new prefix, no new grant.
   - It is overwritten on a later successful day and cleared when that day lands.
   - Choose the key so the handler's newest-landed-day listing (`catch_up_lots`) never reads the status record as a landed `date=` partition.
2. Tests:
   - a refused day writes the statement with its date and reason;
   - the newest-landed listing ignores the status record;
   - a later successful day clears it.

   Record `listing_ignores_status: true` once that test passes.
3. Record `LOTS_NOT_COMPUTED.json` {tests: {passed, failed, new_test}, status_key_pattern, listing_ignores_status}.

No deploy: the change reaches the Lambda in a later release.

<criterion id="DB44-2-AC1" cell_refs="DB-b-91"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r44/p44_round44.py" . DB44-2-AC1</invocation><expect>DB44-2-AC1 PASS</expect></criterion>
`DB44-2-AC1` -- a refused lots day is stated as 'lots not computed for <date>: <reason>' in a status record the newest-landed listing ignores. Base: FAIL.

<expected_criteria>DB44-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you edit the reporting-gold handler and its tests folder. No deploy, no new prefix, no new grant.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~66/
infra/aws/lambda/investor-reporting/reporting-gold/handler.py
infra/aws/lambda/investor-reporting/reporting-gold/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-91.lots-not-computed-statement.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 46 (round 44), cell `DB-b-91`.
<owned_cells>DB-b-91</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB44-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~66/IRPT_DASHBD.TO-DB-b-91.lots-not-computed-statement.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB44-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the status key pattern, the three tests, the result, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- a producer/handler code change and tests; it reaches served output only through a later release under the R37 half; nothing deploys in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call; no role change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB44-2-AC1 FAIL at base (no record; no statement in the handler). Row S40; CTO ADDENDUM 11 item 1.
lane: the <paths> block IS the grant.
</preflight>
