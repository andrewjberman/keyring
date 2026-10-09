# TO IRPT_DASHBD.TO-DB-b-101 -- E3: the 123 W73-S2 DEFECT segments of the 49F vs Black Diamond tie-out -- each fixed in our producer (with a test) or shown by a two-sided read to be Black Diamond's

<to_id>IRPT_DASHBD.TO-DB-b-101</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~76</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>49</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 15 (msg 3492, @74243ee7c8) and ADDENDUM 13.2 (msg 3501), enrichment item E3 | **Decomp cell:** `DB-b-101` (decomposition section 51) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-98 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-76`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~76/`.

**The cell (`DB-b-101`).** Row `IRPT_DASHBD-D2-W73-S2` (DB-b-98, `C:/dev/wk-irpt-dashbd-76/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~73/UNEXPLAINED_CLASSIFIED.json`, the
entries with `reason: DEFECT` and `row: IRPT_DASHBD-D2-W73-S2`) holds 123 segments where the dollars tie, the base is not near zero, and no flow-timing or window test closes the gap. The CTO ruled (ADDENDUM 15
item 4) that each gets a fix of our producer's defect or a two-sided read showing it is Black Diamond's. FWD-8 re-grades on the next tie-out after
both classes land. The tolerance stays 0.35pp.

1. **Find the cause, per segment or per shared cause.** Read our served daily series (the returns gold the tie-out read) and Black Diamond's landed
   bronze points for the window (S3 GETs only).
   - Where our producer `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` is wrong: fix it, and add a test that fails on the old
     code and passes on the fix. The disposition is `PRODUCER_FIX`, with `test`.
   - Where Black Diamond's record is the outlier on a two-sided read: the disposition is `BD_SIDE`, with `evidence` naming the file in your folder
     that shows both sides' values for the segment.
2. Record `W73_S2_RESOLUTION.json` {segments: [{account, segment, disposition, cause, test | evidence}]}: all 123, with the
   account keys exactly as the tie-out writes them.
3. A producer fix ships later under its own pair; do not deploy. If a cause needs a change outside your paths, file a row and keep the
   disposition honest.

**No vendor call, no AWS write.** Copy no client identifier beyond the account keys.

<criterion id="DB49-3-AC1" cell_refs="DB-b-101"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r49/p49_round49.py" . DB49-3-AC1</invocation><expect>DB49-3-AC1 PASS</expect></criterion>
`DB49-3-AC1` -- each of the 123 W73-S2 segments is a producer fix with a test, or a Black Diamond-side finding with evidence. Base: FAIL.

<expected_criteria>DB49-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** S3 GETs of the served returns and Black Diamond's landed bronze; you may edit the returns producer and its tests. No deploy.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~76/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~76/
data/assets/scripts/gold/irpt_reporting/account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-101.defect-w73-s2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 51 (round 49), cell `DB-b-101`.
<owned_cells>DB-b-101</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB49-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~76/IRPT_DASHBD.TO-DB-b-101.defect-w73-s2.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB49-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the causes, the counts per disposition, the producer change if any, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the returns producer; a fix reaches served output only through a later release under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 GETs only; no write, no role change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB49-3-AC1 FAIL at base (no record). Row W73-S2; CTO ADDENDUM 15 item 4.
lane: the <paths> block IS the grant.
</preflight>
