# Deploy Completion Record
**Date opened:** 2026-10-08T18:29:39.806238+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS SC-e-49 (TO-AI-e49): the AI leg of the FWD-15 missing-list act -- the kimi-k3 runner (name and key only) over the three firms' missing-list AI keys, bound by contract 0.8.0, by conditional put on absence into DynamoDB table etf-classifications (us-east-1), plus the AI listing object s3://opal-data-mdpf/mdpf/global/gold/ai_classified_securities/date=<run day>/index.json rewritten per chunk. Nothing else; bd-securities is read only. Dry run at the release head: E49-AI-DRY-RUN entries=1172 keys=1061 present_now=105 to_model=956 runner_direct=0 bound=contract 0.8.0 ok=True problems=[] -- 105 of the 1,061 keys were already landed by the e32 old-list act (the S58 overlap, written once by whichever act ran first), so 956 go to the model, under the step-1 ceiling of 1,049. SNAPSHOT org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/E49_AI_SNAPSHOT_20261007.json is written before any put and the writer refuses it if it already exists (verified absent at open). ROLLBACK: python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/e49_ai_write.py --rollback --write --snapshot <that snapshot> -- a conditional per-key DELETE of only those keys ABSENT from that snapshot carrying updated_by mdpf-secclass-model; a key that existed before the run, or one another writer put under another updated_by, is never deleted. HALVES: COO half NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD15_AI_20261007.md SIGNED WITH CONDITIONS 1-3 @a6a0410d62 (contract bound not the table's legacy vocabulary; vendor word; the S58 overlap written once), and CTO half CTO_HALF_MDPF_SECCLASS_SC_e49_FWD15_AI_RUN_20261007.md SIGNED @6eab3cda67 with four further conditions (vendor ceiling counted per chunk incl retries; the contract bound made mechanical as a per-chunk stop; the clean_name() fix at the release head; the rollback exercise reserved to the issuer).
**Authored by:** 0.7.0_AE_CloudOps~SD
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| W | verify | the AI leg runs to completion over the 956 to_model keys in chunks of 250, each chunk printing keys_sent, model_calls and landed_outside_contract=0 (COO condition 2, CTO condition 2 as a mechanical per-chunk STOP), and the final E49-AI-WRITE line | the per-chunk E49 AI chunk lines plus the E49-AI-WRITE line |  | OPEN |
| V | verify | AC1 on the landed state | python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/ai_leg_verify.py e49 org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/E49_AI_SNAPSHOT_20261007.json reads AI-LEG-VERIFY act=e49 ok=True |  | OPEN |
| G | git | the snapshot, the proof-of-spec instance, this entry and the order flip committed under this seat's author line | commit hashes with measured push state from git ls-remote |  | OPEN |

## Log

- 20261008T182939Z OPENED by 0.7.0_AE_CloudOps~SD with 3 leg(s)
