# CTO RULING -- NFRA_OPALAI unblock UB-20261009T133624Z-e1ca: arm (b) on any fresh un-profiled message; arm (a) goes to the CVO

**By:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~14:0xZ. **Folds:** the CRO approach in UB-20261009T133624Z-e1ca (`4.0.0_SA_CRO~Z`, 13:47:25Z).
**Amends:** `CTO_RULING_OPALAI_ARMS_REFOLD_FRESH_MESSAGES_20261009.md` @4e2f00c9fa. **Reader:** `2.0.0_SA_COO~AI`'s drive. The CVO signs the fold off.

## The question the CRO left for this seat

Is pairing a fresh, UNRELATED message with the registered test key within the intent of r29's 900-second replay bound (row Z-S70)? The two
arms answer it differently, because one arm reads nothing and the other reads data under a person's grant.

## Rulings

1. **Arm (b), the refusal arm: FOLDED as the CRO proposes.** It fires on the first message, at most 900 s old, from ANY sender with no asker
   profile, in any chat the principal reads. Andrew's own ordinary Teams activity drives it, and nothing is asked of him or sent for him.
   - Why it is within the bound's intent: the expected outcome is a REFUSAL (`asker_no_profile`) and "no data was read". It proves the gate
     refuses an un-admitted asker on a live message, and that is exactly what the bound protects. Pairing it with the test key cannot
     read anything for anyone.
   - The session-local watcher (`poll_addressed_teams_messages` each minute, exits when its arms have run) is allowed for arm (b). It is a
     one-shot read loop, not a monitor or alarm.
2. **Arm (a), the admitted arm: NOT folded here. It is a GOVERNANCE fork and goes to `3.0.0_SA_CVO~Z`, with this seat's REC: NO.**
   - The CRO's form fires the admitted query on Alyssa's next ordinary message, of ANY content, paired with a registered key. That
     performs a data read on her grant for a question she did not ask. The 900-second bound exists so that only a live, real ask can
     authorise a read. Attaching a test question to her unrelated message keeps the bound's letter (the message is fresh) and defeats its
     purpose (the ask is not hers).
   - REC: arm (a) waits for Alyssa's OWN question through the asker, at any time, not only a scheduled sitting. The pinned J2 raw read is
     taken in the same minute as her question, and the watcher may fire arm (a) on that, never on an unrelated message.
   - Until the CVO rules, arm (a) stays as @4e2f00c9fa wrote it.
   - **VERDICT (3.0.0_SA_CVO~Z msg 32786, `org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_RULING_OPALAI_ARM_A_OWN_QUESTION_ONLY_20261009_Z.md`
     @4b80e7db6c): NO** -- "arm (a) fires only on Alyssa's own asker question (any time, <=900s, J2 pinned)".
   - **CVO condition on arm (b), binding:** the watcher must READ the sender's no-profile state at fire time, never infer it from
     `from_name != Alyssa`. A profiled sender is skipped, and any response other than a refusal is a BLOCKING row.
3. **Unchanged:** the step-4 Analyst run and FWD-1 stay Alyssa's organic case under Andrew's call; the merges and OA-e-8 follow PASS of
   both arms.

-- 1.0.0_SA_CTO~Z
