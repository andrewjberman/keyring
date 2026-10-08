# TO MDPF_SECCLASS.TO-SC-e70 -- AMENDMENT 1 (re-cut): round 12 SC-e-70 widened per the CTO ruling: READ-ONLY census of EVERY firm-held key absent from etf-classifications

<to_id>MDPF_SECCLASS.TO-SC-e70</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~63</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-70` (`decompositions/MDPF_SECCLASS_DECOMP_R12.md`) |
**outcome_ref:** FWD-15 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-70`, widened. The CTO ruled (1.0.0_SA_CTO~DELL1 msg 824, commit ddd3eaac69) that FWD-15's domain is what the PRD already says:
"for each firm, the held securities that have no entry ... zero for all three firms". The first census (TO-SC-e70) counted only the
99 entries the AI plan routed UNPLACED-KEY, which is a narrower and wrong domain. Row `MDPF_SECCLASS-D1-S5` in the investigation file
measured COT keys absent from the table that the 99 never saw: CSQ, FFC, ETHA, ETH, 4175_GGHC and many CXMANUAL_* keys. 33 of those
keys are not in the plan's held set either. The plan's held set is a local producer build as of 2026-10-05, marked `inferred`.

**Build:** write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/firm_held_unplaced_census.py`. Read-only.
1. **Held set, per firm, from SERVED bytes.** For each firm (cottonwood, 49financial, inflection), find the newest served holdings or
   positions artifact in that firm's own bucket (opal-data-cot, opal-data-49financial, opal-data-inflection). Start with
   `comp-which "where are <firm>'s served holdings positions"`; the BD-family gold `B_01.holdings_lots.py` writes COT's. Read it with
   boto3 (dell1 can read all three buckets since 2026-10-08T05:17:17Z). Record the bucket, key, VersionId and LastModified of each
   artifact. One firm's data is never read with another firm's artifact.
2. **Absent set.** Scan `etf-classifications` with ConsistentRead and full pagination. A held key is PRESENT if it matches a row's
   `ticker`, or `CUSIP:<cusip>`, `NAME::<name>` or `BLOOMBERG:<id>`. Otherwise it is ABSENT.
3. **Route tag** for each ABSENT key: DIRECT, AI or UNPLACED-KEY, using the same rule that produced the route field in
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/e49_replan/FWD15_AI_PLAN_<firm>_20261007.json`. Find that rule
   with comp-which and import or restate it; do not invent a new one.
4. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/FIRM_HELD_UNPLACED_CENSUS_20261008.json`. It holds, per firm: the
   artifact provenance, held count, absent count, absent USD, counts by route, and each absent key with its amount and route.
5. Print one line:
   `FIRM-HELD-CENSUS ok=<bool> firms=<n> held=<per-firm n> absent=<per-firm n> usd=<per-firm sum> e70_still_absent=<n> missing_from_widened=<n>`.
   ok means: all three firms were read from a served artifact, each with held > 0, and every absent key carries exactly one route.
   `e70_still_absent` counts the first census's 99 entries
   (`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/UNPLACED_KEY_CENSUS_20261008.json`) that are still absent from the table
   AND still held. `missing_from_widened` counts those that do NOT appear in the widened absent set; it must be 0. That is the control.

### ACCEPTANCE

<criterion id="SC12-e70b-AC1" cell_refs="SC-e-70"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/firm_held_unplaced_census.py</invocation><expect>FIRM-HELD-CENSUS ok=True firms=3</expect></criterion>
`SC12-e70b-AC1` -- all three firms come from a served artifact, each with held > 0, and every absent key has exactly one route.

<criterion id="SC12-e70b-AC2" cell_refs="SC-e-70"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/firm_held_unplaced_census.py</invocation><expect>missing_from_widened=0</expect></criterion>
`SC12-e70b-AC2` -- the control: every still-held, still-absent entry of the first census appears in the widened set.

<expected_criteria>SC12-e70b-AC1, SC12-e70b-AC2</expected_criteria>

Dry-run at the base (dell1 CLOUD, 2026-10-08 ~07:0xZ): SC12-e70b-AC1 and AC2 FAIL as expected (the script is absent).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS: reads only** (s3 get/list/head on the three firm buckets, dynamodb scan on etf-classifications). No write of any kind, no
  invoke, no vendor or model call. Never push.
- Every AWS call goes through boto3 or `.tools/aws`, bounded by `timeout 120`. A read that is denied is reported by action and
  resource in a surprise row, never worked around.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-D1-W63-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/firm_held_unplaced_census.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/FIRM_HELD_UNPLACED_CENSUS_20261008.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R12.md</decomp_doc> (round 12), cell `SC-e-70`.
<owned_cells>SC-e-70</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC12-e70b-AC1, SC12-e70b-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~63/MDPF_SECCLASS.TO-SC-e70.unplaced-key-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC12-e70b-AC1 SC12-e70b-AC2` BEFORE the flip. A judgment criterion is
recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the artifact read per firm (bucket, key, VersionId), what you changed (file:line), each criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE read-only, no schedule; the served artifact's own LastModified is recorded.
comp-iam: RUN -- dell1 firm-bucket READ applied 05:17:17Z (laptop CTO msg 106788), exercised by 2.0.0_SA_COO~M1 on opal-data-cot at 06:5xZ; etf-classifications Scan is the standing read.
comp-adversary: RUN -- a held set drawn from a build instead of served bytes (step 1 records VersionId); a narrower domain again (control AC2, missing_from_widened=0); a cross-firm read (one firm per artifact); a re-invented route rule (step 3 reuses the plan's rule).
lane: the <paths> block IS the grant.
</preflight>

AMENDMENT 1 (issuer 2.0.0_SA_COO~M1, 2026-10-08 ~07:0xZ): this order is re-cut and re-issued to slot ~63. The first census
(slot ~60, drain af53905b57, UNPLACED_KEY_CENSUS_20261008.json, criterion SC12-e70-AC1 PASS) stands as a measured input and is
the AC2 control here. Gate limb: to-pipeline-gate grades this as a modification of an existing order.

Source: CTO ruling msg 824 @ddd3eaac69 on row MDPF_SECCLASS-D1-S5 (@08297b728c); first census TO-SC-e70 (drain af53905b57).
