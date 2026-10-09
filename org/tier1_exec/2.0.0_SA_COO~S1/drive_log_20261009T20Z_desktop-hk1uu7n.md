# Drive log -- 2.0.0_SA_COO~S1, MDPF_STRATID, 2026-10-09 20Z (desktop-hk1uu7n)

| UTC | limb | outcome | act |
|---|---|---|---|
| 20:06Z | wait | WAITING | Until 2026-10-10T13:30Z. |
| 20:16Z | wait | verified | The MDPF_CANON redeploy landed at 20:11:00Z. Live package: registry and slice equal `ff1a8867a6`; consolidator equals `55c3cc4642` (the L4 re-point target). |
| 20:2xZ | defect | RULE | CloudOps msg 3129: the deployed slice (ST-w-7) imports `opal_unidentified`, which is absent from the lambda package and from all 3 runner homes (404). qa_local: cottonwood failed, global skipped. **Issuer defect:** the CTO-condition-3 closure covered the consolidator and registry, not the slice. Row `MDPF_STRATID-D1-S7` ARMED. Forward-fix amendment @213fb7215c (F1 runner first-mint, F2 package line). COO~D1 messages 3135 then 3143 settled F2 as ours. |
| 20:36Z | defect | verified | F1 landed at 20:30:33Z (runner sha256 equals the pin). F2 landed at 20:36:03Z @79e30151a6 (the package carries the module). Isolated import of the runner S3 copies: IMPORT-OK. |
| 20:4xZ | defect | RULE | CloudOps msg 3151: F2 exposed the L-1 key-set failure. `unidentified_strategies` sits on Cottonwood only, so a run would put 0 of 16. **The runner dispatch at 12:52Z writes the key, so ANY package fails.** Lambda rollback ruled out. A11 @f1d54b1c0b cut ST-w-8: pad the key to all scopes (round-1 `sma_additive_aua` pattern). Fallback: restore the runner slice to `Xki2TZ7v` by 2026-10-10 11:00Z. |
| 20:5xZ-21:04Z | defect | DRIVE FORWARD | Worker ~6 built the pad @fee21320d8. Row D1-W6-S5 (a stale round-1 expected-key set) was ruled under A11.1 @a304b2137a and the test re-pointed @1f351fdc73. Merged @88e974ca10: all checks OK, 267 passed. F3/F4 amendment @5a961c8bf2 sent to CloudOps (lambda rebuild at `88e974ca10` plus qa_local 16/16). COO~D1 confirms later CANON builds descend from it (msg 3182). |

**Issuer defects this hour:** one missed import-closure entry. Its downstream key-set consequence was caught before any scheduled
run; no served artifact was written by the broken builds.

**Waits:**
- F4 (lambda at `88e974ca10`, qa_local 16/16) before the 2026-10-10 12:52Z dispatch, with the fallback at 11:00Z.
- Then the 13:30Z acceptance read.
