# TO IRPT_DASHBD.TO-DB-b-112 -- E1: apply the memory step -- gold Lambda memory_size 2048 -> 3008, the setting only, under the signed pair -- then the 10-08 dry run under 3008 as the after-proof against 85%; over either line rolls back to 2048

<to_id>IRPT_DASHBD.TO-DB-b-112</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~87</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>56</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** the memory-step pair (COO half @ca40177794, CTO half msg 3789), enrichment item E1 | **Decomp cell:** `DB-b-112` (decomposition section 58) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-109 (drained), both halves SIGNED.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-87`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~87/`.

**The cell (`DB-b-112`).** Both halves of the memory-step pair are SIGNED. Read all three files in `C:/dev/wk-irpt-dashbd-87` first:
- the packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~84/NEVER_WIDEN_PACKET_MEMSTEP.md` (sha256 `f1cc6068...`, with the census, the plan text and the dry-run event);
- the COO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_MEMSTEP_COO_HALF.md`;
- the CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_MEMSTEP_CTO_HALF.md`.

The procedure follows R44's (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~70/R44_APPLY_RECORD.json`) and DB-b-107's dry run
(`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~82/R44_HEAVY_DAY_DRYRUN.json`). It must land BEFORE the R45 release and Monday 2026-10-12 07:41 ET.

**THE CLIENT-DATA RULE (binding):** never print an account number or a client figure in a commit, record, row or report.

1. **Ledger first,** pinned to the packet sha256 `f1cc6068...` (`python .tools/deploy_ledger.py`). Legs: plan, apply, verify, dry-run proof. Commit after each
   leg, and record `ledger_entry`.
2. **Before.** Read live: CodeSha256 must be `oNgy4rnr...` and MemorySize 2048, else STOP. Record `before`.
3. **Edit `infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf` line ~59 ONLY:** `memory_size = 3008`.
   - The targeted plan (`-target=module.irpt_reporting_gold.aws_lambda_function.this`) must read `0 to add, 1 to change, 0 to destroy`, with `memory_size` the
     ONLY changed attribute. Record `plan` and `plan_changes`. Anything else is a STOP.
   - Then ONE `.tools/safe-apply.sh` from the saved plan.
   - Read back MemorySize 3008 and CodeSha256 still `oNgy4rnr...`. Record `after`.
   - A post-apply plan must read `No changes`; record `replan_no_changes`.
4. **After-proof.** ONE dry-run invoke: `{"backfill": {"start": "2026-10-08", "end": "2026-10-08"}, "accounts": "population", "dry_run": true}`.
   - Read the REPORT line.
   - Count objects written under `irpt/49financial/gold/` after the invoke start, with a positive control. Expect 0.
   - Record `dry_run` {request_id, duration_ms, max_memory_mb, written_objects} beside the before (1,685 MB, 395.1 s).
5. **Verdict.**
   - UNDER: both Duration < 765,000 ms and Max Memory < 2,556.8 MB. Close the ledger.
   - OVER: either over. Branch B: revert line 59 to 2048 through ONE targeted safe-apply. Record `rollback.memory_mb_after`, and file a row.
6. Record `MEMSTEP_APPLY_RECORD.json`. Report the deploy to `0.0.0_AB_MSTR~DELL2` through the issuer.

**No other invoke, no code change, no delete.**

<criterion id="DB56-1-AC1" cell_refs="DB-b-112"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r56/p56_round56.py" . DB56-1-AC1</invocation><expect>DB56-1-AC1 PASS</expect></criterion>
`DB56-1-AC1` -- memory 3008 is live with code unchanged, plan 0/1/0 on memory_size only, and the 10-08 dry run under 3008 is graded against 85%. Base: FAIL.

<expected_criteria>DB56-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** under the signed pair, you edit `infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf` line ~59 only, run ONE targeted safe-apply (and, on OVER only, one rollback apply), and ONE dry-run invoke. No code change, no delete.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~87/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~87/
org/critical_paths/
infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-112.memory-step-apply.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 58 (round 56), cell `DB-b-112`.
<owned_cells>DB-b-112</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB56-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~87/IRPT_DASHBD.TO-DB-b-112.memory-step-apply.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB56-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the before and after reads, the plan line, the dry-run REPORT, the verdict, the ledger, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one function's memory setting; code and artifact unchanged.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role or policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the schedule is unchanged; Monday's fire stays the acceptance.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB56-1-AC1 FAIL at base (no record). Memory-step pair: COO @ca40177794, CTO msg 3789.
lane: the <paths> block IS the grant.
</preflight>
