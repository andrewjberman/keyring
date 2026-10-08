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
- 20261007T230xxZ RUN 1 KILLED by the Claude Code harness for BOX memory pressure (3.93 of 31.7 GB free), not by a contract STOP: chunk 1 of 10 only, 187 of 2,291 keys landed, landed_outside_contract=0, snapshot intact, 0 snapshot keys missing, NOTHING rolled back. Record org/tier2_senior/0.7.0_AE_CloudOps~SC/deliverables/E32_AI_LEG_RUN1_KILLED_STATE_20261007.md @559feeeb5b. Step 4 NOT executed: AC1 read ok=True on the 8-percent state (row S66), so no leg was closed and the order stays pending.
- 20261008T002xxZ RESUME RULED by issuer 2.0.0_SA_COO~M1, amendment 2 @ff86568dbb: same entry, new snapshot E32_AI_SNAPSHOT_RUN2_20261007.json, run 1 snapshot stays the rollback input for the whole act, --chunk 100, completeness at close = run 1 sent + run 2 ai_to_model = 2,291. Amendment step 2 dry run DONE, read-only, rc=0: direct_keys=0 ai_keys=2104 to_model=2104 off_vocab=0, now_present=5369. WRITE ACT NOT STARTED: the harness bars restarting it unasked, and Andrew at 00:0xZ placed heavy jobs on the Dell boxes while 1.0.0_SA_CTO has asked the issuer whether to re-issue the remainder for a dell1 seat. AC1 must not run before run 2 chunk 1 rewrites the date=2026-10-08 listing (rows S64, S67: AC1 flipped ok=True to ok=False on identical state across UTC midnight).
