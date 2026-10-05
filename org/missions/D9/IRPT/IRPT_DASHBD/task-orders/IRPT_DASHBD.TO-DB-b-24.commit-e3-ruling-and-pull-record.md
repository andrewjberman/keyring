# TO IRPT_DASHBD.TO-DB-b-24 -- commit the DB-b-20 folder's shape ruling and first pull record, with the bearer line corrected to batches 248-249 (row W7-S1; round-15 E4)

<to_id>IRPT_DASHBD.TO-DB-b-24</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~10</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>15</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO round-15 analysis, item E4
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_DASHBD_ROUNDS_12_14_B_20261005.md` @b09cafb7a4, msg 105203) |
**Decomp cell:** `DB-b-24` (decomposition section 15) | **outcome_ref:** FWD-8 | **depends_on:** none.

---

## WORKER FACE

**Row W7-S1.** Two files exist only UNTRACKED in the shared checkout, so no worktree holds them:
- `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6/E3_SHAPE_RULING.json` (the run's shape ruling);
- `.../~6/BD_POPULATION_PULL_E3.json` (the first run's record, aborted at call 19 on HTTP 401).

The ruling's bearer line still reads "one, minted once". CTO batch 248 (re-mint before the measured expiry) and batch 249 (one
coordinator-owned shared bearer, re-minted on an interval) superseded it.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-dashbd-10`; run everything from its root.

1. Copy both files byte for byte from the shared checkout
   `C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6/` into the same
   path in your worktree. That is a read of the shared tree; write nothing there.
2. In `E3_SHAPE_RULING.json` ONLY, correct the bearer line. Name batch 248 (re-mint before the measured expiry) and batch 249 (one
   coordinator-owned shared bearer, re-minted on an interval, never one sign-in per worker). Keep every other field byte-identical.
   `BD_POPULATION_PULL_E3.json` is a historical record: commit it unchanged.
3. Neither file may hold a credential, bearer or token value. Check it before committing (search for `token`, `bearer`, `password`
   and `secret` values, not keys). If you find one, stop and file a row.

<criterion id="DB15-2-AC1" cell_refs="DB-b-24"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r15/p15_cells.py" . DB15-2-AC1</invocation><expect>DB15-2-AC1 PASS</expect></criterion>
`DB15-2-AC1` -- both files are tracked in the DB-b-20 folder and parse, and the ruling names batches 248 and 249 and no longer says
"minted once". Base: FAIL.

<criterion id="DB15-2-AC2" cell_refs="DB-b-24"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r15/p15_cells.py" . DB-GUARD</invocation><expect>DB-GUARD PASS</expect></criterion>
`DB15-2-AC2` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>DB15-2-AC1,DB15-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none. No vendor call.
- **Refusal clause.** A credential in either file, or any edit to the pull record, is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6/E3_SHAPE_RULING.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6/BD_POPULATION_PULL_E3.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~10/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-24.commit-e3-ruling-and-pull-record.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 15 (round 15, workstream B), cell `DB-b-24`.
<owned_cells>DB-b-24</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB15-2-AC1, DB15-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~10/IRPT_DASHBD.TO-DB-b-24.commit-e3-ruling-and-pull-record.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB15-2-AC1,DB15-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, the corrected bearer line, each criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- two record files committed; 0 served bytes move.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB15-2-AC1 base FAIL (both untracked), DB-GUARD base PASS, dry-run at base 53acc6abb8 2026-10-05 ~07:3xZ.
lane: the <paths> block IS the grant.
</preflight>
