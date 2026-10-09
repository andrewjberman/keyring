# TO IRPT_DASHBD.TO-DB-b-105 -- E1: the never-widen packet for ONE gold Lambda release carrying DB-b-97 (backfill clears the lots status record) and DB-b-104 (status key via address()) over live oNgy4rnr -- census shows only handler.py, memory headroom stated, halves UNSIGNED

<to_id>IRPT_DASHBD.TO-DB-b-105</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~80</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>52</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 16 item 1 and ADDENDUM 17 (msg 3583, @6d3d12876c), enrichment item E1 | **Decomp cell:** `DB-b-105` (decomposition section 54) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-97, DB-b-104 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-80`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~80/`.

**The cell (`DB-b-105`).** The CTO ruled (ADDENDUM 16 item 1, ADDENDUM 17 item 1) that DB-b-97 and DB-b-104 ship together as ONE gold Lambda
release over live `irpt-49f-reporting-gold-lambda` `oNgy4rnrduvN9N2axhsHBfe9izZKd8dZGeFGXAIh+cM=`, under ONE never-widen pair. The census must show only
those two orders' member, `infra/aws/lambda/investor-reporting/reporting-gold/handler.py`. This cell writes the packet only.

Read in `C:/dev/wk-irpt-dashbd-80`:
- the R44 packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~69/NEVER_WIDEN_PACKET_R44_RELEASE.md` (the template) and its census;
- the R44 apply record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~70/R44_APPLY_RECORD.json`;
- the R44 sizing record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~78/R44_SIZING_DRYRUN.json`.

1. **Census.** Compare every source-map member pinned for `oNgy4rnr` against HEAD. Exactly one may differ: `handler.py`. Any other member differing
   from the LIVE bundle means a row and a STOP. Record its pin (the box/dell2 commit carrying HEAD's bytes) and sha256, plus the live base S3 version
   (ONE get-function and ONE head-object), in `R45_RELEASE_CENSUS.json` {base_codesha256, members_changed: [{path, pin, sha256, owner_orders}],
   rollback: {base_s3_version, base_codesha256}}.
2. **Packet** `NEVER_WIDEN_PACKET_R45_RELEASE.md`:
   - **Radius:** no new key, read or grant. The status key is unchanged in bytes (DB-b-104). The backfill path now writes it: count the writers.
   - **## Branch A** and **## Branch B**, both from the handler's own rules with file and line: a backfill lands a stated day and drops it; a backfill
     refuses a day and states it.
   - **## Rollback** to `oNgy4rnr` by its S3 version.
   - **## Memory headroom:** the R44 dry run used 1,661 MB, 95.4% of the 1,740.8 MB line. State what this release adds to memory: measured on a
     local kit day, or argued from the code with file and line, and say which. The halves forbid raising a limit.
   - **## COO half** and **## CTO half**, each reading UNSIGNED.

**Read-only on AWS** (one get-function, one head-object). No build, upload or apply.

<criterion id="DB52-1-AC1" cell_refs="DB-b-105"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r52/p52_round52.py" . DB52-1-AC1</invocation><expect>DB52-1-AC1 PASS</expect></criterion>
`DB52-1-AC1` -- the census over live oNgy4rnr lists exactly handler.py, pinned to HEAD bytes, with the rollback version. Base: FAIL.

<criterion id="DB52-1-AC2" cell_refs="DB-b-105"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r52/p52_round52.py" . DB52-1-AC2</invocation><expect>DB52-1-AC2 PASS</expect></criterion>
`DB52-1-AC2` -- the packet carries both branches, the rollback, the memory headroom and two UNSIGNED halves. Base: FAIL.

<expected_criteria>DB52-1-AC1,DB52-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** two live AWS READS (get-function, head-object). No write anywhere outside your folder.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~80/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~80/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-105.r45-release-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 54 (round 52), cell `DB-b-105`.
<owned_cells>DB-b-105</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB52-1-AC1, DB52-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~80/IRPT_DASHBD.TO-DB-b-105.r45-release-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB52-1-AC1,DB52-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the census, the base S3 version, the radius line, the memory statement, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the packet scopes a later release of the gold Lambda; this cell reads only.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role or policy change; the status key is in the existing write set.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the schedule is unchanged.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB52-1-AC1 and DB52-1-AC2 FAIL at base (no census, no packet). CTO ADDENDUM 16 item 1, ADDENDUM 17 item 1.
lane: the <paths> block IS the grant.
</preflight>
