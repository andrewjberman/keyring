# TO IRPT_DASHBD.TO-DB-b-65 -- E3: NEAR_ZERO_BALANCE (153) traced -- a cause per sub-class with counts; each fixed or carried as a named class

<to_id>IRPT_DASHBD.TO-DB-b-65</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~42</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>33</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-32 ADDENDUM 1 @78928255f6 (on ADJUDICATION_v17), enrichment item E3 | **Decomp cell:** `DB-b-65` (decomposition section 35) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-58 (merged @cc72b3f60d).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-42`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~42/`.

**The cell (`DB-b-65`).** Round 31 named 153 of the 1,203 UNEXPLAINED misses NEAR_ZERO_BALANCE: the account is funded from, or emptied
to, a near-zero value inside the segment, and the two systems value those days differently. Trace them further.

**Population:** the rows of `deliverables/0.9.0_WK_IRPT_DASHBD~36/UNEXPLAINED_CLASSES_E2.json` with `cause_class == "NEAR_ZERO_BALANCE"`
(153). Take it from the record.

**Sources (read only):**
- the reader of record `org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_reader.py`;
- round 32's records `deliverables/0.9.0_WK_IRPT_DASHBD~38/REGRADE_FLOWSTART_E2.json` and `deliverables/0.9.0_WK_IRPT_DASHBD~39/LARGE_FLOW_E3.json`;
- the BD full-period pull `s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/`;
- the served gold `s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/`.

1. For each of the 153, find the sub-cause around the near-zero days. Examples: Opal's guard or carried day on a near-zero value, a return
   computed on a near-zero divisor, a funding day BD counts from its first full day, a residual balance after liquidation, a negative
   balance. Give each a `sub_class` with `evidence`. Write `counts`. Note any overlap with round 32's flow-start in-to-out list or with
   DB-b-62's LIQUIDATION_RESIDUAL_BASE / FUNDED_FROM_NEAR_ZERO.
2. For each sub_class, write `dispositions[sub_class]` {disposition: "fixed" | "named_cause", cause, note}. A fix lives in a NEW module in
   your folder and states its effect on the 153. It never edits the reader of record or the served producer.
3. Write `NEAR_ZERO_E3.json` (`rows` [{account, segment, sub_class, evidence}], `counts`, `dispositions`, `files_read`) and
   `NEAR_ZERO_E3.md` (COUNTS ONLY).

<criterion id="DB33-3-AC1" cell_refs="DB-b-65"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r33/p33_round33.py" . DB33-3-AC1</invocation><expect>DB33-3-AC1 PASS</expect></criterion>
`DB33-3-AC1` -- the 153 each carry a traced sub_class; counts equal the tally. Base: FAIL.

<criterion id="DB33-3-AC2" cell_refs="DB-b-65"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r33/p33_round33.py" . DB33-3-AC2</invocation><expect>DB33-3-AC2 PASS</expect></criterion>
`DB33-3-AC2` -- every sub_class is dispositioned fixed or named_cause, with its cause. Base: FAIL.

<expected_criteria>DB33-3-AC1,DB33-3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~42/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-65.near-zero-balance.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 35 (round 33), cell `DB-b-65`.
<owned_cells>DB-b-65</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB33-3-AC1, DB33-3-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~42/IRPT_DASHBD.TO-DB-b-65.near-zero-balance.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB33-3-AC1,DB33-3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the sub-classes with counts and dispositions, and the overlaps, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a project-owned reconciliation reader and records; nothing served, deployed or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB33-3-AC1/AC2 base FAIL at base beca8909cd (no record); positive control on a planted record PASS (153).
lane: the <paths> block IS the grant.
</preflight>
