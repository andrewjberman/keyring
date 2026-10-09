# TO IRPT_DASHBD.TO-DB-b-109 -- E1: the never-widen packet for ONE configuration change raising the gold Lambda's memory one step above 2048 MB (the setting only, no code), with the heaviest-day dry run as before/after proof -- halves UNSIGNED, apply before Monday 2026-10-12 07:41 ET

<to_id>IRPT_DASHBD.TO-DB-b-109</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~84</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>55</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 20 and ADDENDUM 19 item 2, enrichment item E1 | **Decomp cell:** `DB-b-109` (decomposition section 57) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-107 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-84`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~84/`.

**THE CLIENT-DATA RULE (binding):** evidence carrying account numbers or client figures is written OUTSIDE the repo, under
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/<your serial>/`. The repo carries counts, sha256 and reason codes only, and account tokens in the
`acct#<sha256("49financial:<account>")[:8]>` form. Never print an account number in a commit message, a record, a row or a report.

**The cell (`DB-b-109`).** Two dry runs of 2026-10-08 on live `irpt-49f-reporting-gold-lambda` `oNgy4rnr...` read 1,661 MB and 1,685 MB, which is 96.8% of
the 1,740.8 MB line (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~82/R44_HEAVY_DAY_DRYRUN.json`). The CTO ruled (ADDENDUM 20) that ONE pair raises the configured
memory one step before Monday's 07:41 ET fire. The census is the memory setting ONLY. This cell writes the packet; the apply is a later cell, after
both halves are signed.

In `C:/dev/wk-irpt-dashbd-84`:
1. **Census.** `infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf` line ~59 reads `memory_size = 2048`. Name the step: the next size
   up, which also raises CPU. State why that size, e.g. the estate's existing gold Lambda sizes or a 1.5x step, and the new 85% line. Confirm by a
   targeted plan, reading only, that the ONLY change is `memory_size` on `module.irpt_reporting_gold.aws_lambda_function.this`, with no artifact or
   source_code_hash change.
   - Record `MEMSTEP_CENSUS.json` {base_codesha256 (live read), memory_before: 2048, memory_after, changed: ["memory_size"], plan_line}.
2. **Packet** `NEVER_WIDEN_PACKET_MEMSTEP.md`:
   - **## Census**.
   - **## Branch A:** the before/after proof. The same heaviest-day dry run, `{"backfill": {"start": "2026-10-08", "end": "2026-10-08"},
     "accounts": "population", "dry_run": true}`, re-read under the new setting. Print before and after against 85% of each setting.
   - **## Branch B:** the after read over its own 85% line means roll back to 2048.
   - **## Rollback:** the prior setting through ONE targeted safe-apply.
   - **## COO half** and **## CTO half**, each reading UNSIGNED.

Read-only on AWS (get-function-configuration). One `terraform plan`, no apply, no invoke.

<criterion id="DB55-1-AC1" cell_refs="DB-b-109"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r55/p55_round55.py" . DB55-1-AC1</invocation><expect>DB55-1-AC1 PASS</expect></criterion>
`DB55-1-AC1` -- the memory-step packet and census show the setting alone changing above 2048, with two UNSIGNED halves. Base: FAIL.

<expected_criteria>DB55-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** one get-function-configuration read and one targeted `terraform plan` (no apply). No invoke.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~84/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~84/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-109.memory-step-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 57 (round 55), cell `DB-b-109`.
<owned_cells>DB-b-109</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB55-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~84/IRPT_DASHBD.TO-DB-b-109.memory-step-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB55-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the step chosen and why, the plan line, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one function's memory setting; no code; this cell plans only.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role or policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the schedule is unchanged.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB55-1-AC1 FAIL at base (no packet). CTO ADDENDUM 20 item 1.
lane: the <paths> block IS the grant.
</preflight>
