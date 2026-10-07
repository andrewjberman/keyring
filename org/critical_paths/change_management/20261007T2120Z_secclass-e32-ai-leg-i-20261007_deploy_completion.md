# Deploy Completion Record
**Date opened:** 2026-10-07T21:20:00.974028+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS SC-e-32/e50 (TO-AI-e32): the AI leg of the old-list V3 act -- the kimi-k3 runner over 2,291 old-list AI keys in chunks of 250, bound by contract 0.8.0, conditional puts into DynamoDB table etf-classifications (us-east-1) plus the AI listing object s3://opal-data-mdpf/mdpf/global/gold/ai_classified_securities/date=2026-10-07/index.json rewritten per chunk; nothing else, bd-securities read only. Snapshot org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/E32_AI_SNAPSHOT_20261007.json written before any put. Rollback: python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_reclassify_write.py --rollback --set org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_RECLASSIFY_SET_V3_20261007.tsv --half org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_OLD_LIST_RECLASSIFY_20261007.md --snapshot org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/E32_AI_SNAPSHOT_20261007.json (conditional delete, per key, only keys absent from that snapshot carrying updated_by mdpf-secclass-old-list-reclassify or mdpf-secclass-model). Halves: COO SIGNED WITH CONDITIONS 1-3 (V3) and CTO SIGNED @8779dcc505 conditions 1-2.
**Authored by:** 0.7.0_AE_CloudOps~SC
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| W | verify | the AI leg runs to completion: 2,291 keys in 10 chunks of 250, each chunk printing keys_sent, model_calls and landed_outside_contract=0 (COO condition 2); the final RECLASSIFY-WRITE line | the per-chunk lines plus the RECLASSIFY-WRITE line |  | OPEN |
| V | verify | AC1 on the landed state | python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/ai_leg_verify.py e32 <snapshot> reads AI-LEG-VERIFY act=e32 ok=True |  | OPEN |
| G | git | the snapshot, the proof instance, this entry and the order flip committed on this seat's branch and merged to CLOUD | commit hashes with measured push state from git ls-remote |  | OPEN |

## Log

- 20261007T212000Z OPENED by 0.7.0_AE_CloudOps~SC with 3 leg(s)
