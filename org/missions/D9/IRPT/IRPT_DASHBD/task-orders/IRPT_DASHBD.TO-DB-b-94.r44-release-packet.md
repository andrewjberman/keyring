# TO IRPT_DASHBD.TO-DB-b-94 -- E1: the never-widen packet for ONE gold Lambda release carrying DB-b-90 (uniqueness on final rows) and DB-b-91 (lots-not-computed statement) over live yIAQjspL -- member census showing exactly those two members, both branches, rollback, halves UNSIGNED

<to_id>IRPT_DASHBD.TO-DB-b-94</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~69</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>46</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 12 (msg 3371, @77e60c3d2b), enrichment item E1 | **Decomp cell:** `DB-b-94` (decomposition section 48) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-90, DB-b-91 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-69`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~69/`.

**The cell (`DB-b-94`).** The CTO ruled (ADDENDUM 12 item 5) that DB-b-90 and DB-b-91 are released TOGETHER as ONE gold Lambda release, after the live
`irpt-49f-reporting-gold-lambda` CodeSha256 `yIAQjspL0nPX6tJOHxD+Dv0REVoZyBNRkhmHQxUVuEE=`, under ONE never-widen pair. The member census against
live `yIAQjspL` must show exactly the members those two orders own; anything else is a STOP. This cell writes the packet only; the apply is a
later cell, after both halves are signed.

Read in `C:/dev/wk-irpt-dashbd-69`:
- the R37 delta packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~63/R37_DELTA_PACKET_1008.md` and its record
  `R37_DELTA_RECORD.json` (the source map, pins, artifact S3 version, procedure);
- `data/assets/scripts/gold/irpt_reporting/account_activity_lots.py` and `infra/aws/lambda/investor-reporting/reporting-gold/handler.py` at HEAD.

1. **The census.** Compare the source map's members as pinned for `yIAQjspL` against HEAD. Changed members must be exactly
   `account_activity_lots.py` (DB-b-90) and `reporting-gold/handler.py` (DB-b-91). If any other member differs, file a row naming it and
   STOP before the packet.
   - Record each changed member's new pin (the box/dell2 commit carrying its bytes) and sha256.
   - Record the live base S3 artifact version as `rollback.base_s3_version`. Read it live: one `get-function` plus one `head-object`.
   - Write `R44_RELEASE_CENSUS.json` {base_codesha256, members_changed: [{path, pin, sha256, owner_order}], rollback: {base_s3_version,
     base_codesha256}}.
2. **The packet** `NEVER_WIDEN_PACKET_R44_RELEASE.md` carries these sections:
   - **Radius:** no new read or grant. One new written key, `<account_activity_daily prefix>_status/lots_not_computed.json`, inside the
     existing PutObject set. Count its writers.
   - **## Branch A:** a lots day lands. The final-rows check passes, and the status record drops that day.
   - **## Branch B:** a lots day is refused by name. The statement is written, and returns and class still land. State both expected outcomes
     from the producer's own rules (cite the function and line).
   - **## Rollback:** per key, back to `yIAQjspL` by its S3 version.
   - **Sizing:** the change adds one pass over the realized rows. State it as unmeasured, or measure one local kit day, and name which.
   - **## COO half** and **## CTO half**, each reading UNSIGNED.

**Read-only on AWS** (one get-function, one head-object). No build, no upload, no apply.

<criterion id="DB46-1-AC1" cell_refs="DB-b-94"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r46/p46_round46.py" . DB46-1-AC1</invocation><expect>DB46-1-AC1 PASS</expect></criterion>
`DB46-1-AC1` -- the member census over live yIAQjspL lists exactly the DB-b-90 and DB-b-91 members, pinned to HEAD bytes, with the rollback version. Base: FAIL.

<criterion id="DB46-1-AC2" cell_refs="DB-b-94"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r46/p46_round46.py" . DB46-1-AC2</invocation><expect>DB46-1-AC2 PASS</expect></criterion>
`DB46-1-AC2` -- the packet carries both branches, the rollback and two UNSIGNED halves. Base: FAIL.

<expected_criteria>DB46-1-AC1,DB46-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** two live AWS READS (get-function, head-object). No write anywhere outside your folder.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~69/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~69/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-94.r44-release-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 48 (round 46), cell `DB-b-94`.
<owned_cells>DB-b-94</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB46-1-AC1, DB46-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~69/IRPT_DASHBD.TO-DB-b-94.r44-release-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB46-1-AC1,DB46-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the census, the base S3 version, the radius line, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the packet scopes a later release of the gold Lambda; this cell reads only.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role or policy change; the radius line states no new grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the R37 schedule is unchanged.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB46-1-AC1 and DB46-1-AC2 FAIL at base (no census, no packet). CTO ADDENDUM 12 item 5.
lane: the <paths> block IS the grant.
</preflight>
