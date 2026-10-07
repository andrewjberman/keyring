# Deploy Completion Record
**Date opened:** 2026-10-07T17:36:20.157837+00:00
**Status:** OPEN
**Deploy:** MDPF_HEALGAP.TO-HG-d3 (laptop box): the one real run of FWD-1 -- the 06:00Z target of rule cot-rebalancer-runner-daily carries {mode:pull,induce:auth-lapse} for exercise date D=2026-10-08 only, restored to {mode:pull} between 06:05Z and 06:20Z; the ~11:32Z cot-bronze-complete re-attempt target must heal D with nobody acting. Input-only change on one existing target, out of Terraform band for ~25 minutes; no apply, no IAM, no S3 write
**Authored by:** 0.7.0_AE_CloudOps~F
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | put-targets on cot-rebalancer-runner-daily setting Input {mode:pull,induce:auth-lapse}, same target Id and Arn | the pre-read showing exactly one target, the put time, and the read-back | PRE-READ 2026-10-07T17:38:11Z: cot-rebalancer-runner-daily had EXACTLY ONE target -- Id=cot-rebalancer-runner-daily, Arn=arn:aws:lambda:us-east-1:313476888478:function:cot-rebalancer-runner, Input={"mode":"pull"}; describe-rule State=ENABLED ScheduleExpression=cron(0 6 * * ? *). PUT 2026-10-07T17:40:36Z: aws events put-targets --rule cot-rebalancer-runner-daily with that SAME Id and SAME Arn and Input {"mode":"pull","induce":"auth-lapse"} -> FailedEntryCount 0, FailedEntries [], rc=0. READ-BACK 2026-10-07T17:41:52Z: the single target reads Id=cot-rebalancer-runner-daily, Arn unchanged, Input={"mode":"pull","induce":"auth-lapse"}; length(Targets)=1, so no target was added or removed. SEPARATION VERIFIED in the same read: cot-bronze-complete still carries its two targets with CotSilverOnBronzeComplete at {"mode":"silver-run"} and cot-rebalancer-runner-reattempt at {"mode":"pull"} -- the HG-d2 re-attempt input was NOT touched, so the ~11:32Z heal on D is a real pull and not a second induced failure. The put was made the evening before D as the order directs, so the next fire of this rule after the GO is D 2026-10-08 06:00Z and nothing else is inside the induced window. Window 24h because L4/L5 cannot be read before 13:00Z on D. | CLOSED 20261007T174308Z |
| L2 | activation | put-targets restoring Input {mode:pull} after 06:05Z and before 06:20Z on D, then HG1-d3-AC3 | the restore time, the read-back, and RESTORED-OK |  | OPEN |
| L3 | verify | targeted terraform plan on the daily rule's target in opal-assets after the restore, CHECKPOINT_DISABLE=1 (CTO half condition 3) | no change; a diff is fixed the same morning |  | OPEN |
| L4 | verify | HG1-d3-AC1 and HG1-d3-AC2 after 13:00Z on D | FAILED-OK and HEALED-OK; a BAD AC2 after 18:00Z triggers the branch (B) remedy, one invoke, recorded |  | OPEN |
| L5 | verify | CTO half condition 4: whether D's served Cottonwood figures were in place by 13:30Z | the newest silver/gold write time for D against 13:30Z, MET or MISSED |  | OPEN |

## Log

- 20261007T173620Z OPENED by 0.7.0_AE_CloudOps~F with 5 leg(s)
- 20261007T174308Z LEG L1 closed: PRE-READ 2026-10-07T17:38:11Z: cot-rebalancer-runner-daily had EXACTLY ONE target -- Id=cot-rebalancer-runner-daily, Arn
