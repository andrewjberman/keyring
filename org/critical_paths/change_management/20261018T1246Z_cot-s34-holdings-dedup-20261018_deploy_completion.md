# Deploy Completion Record
**Date opened:** 2026-10-18T12:46:16.492963+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261018T130114Z
**Deploy:** MDPF_CANON-D1-S34: cot silver holdings dedup (account_id, asset_id) -- deploy b0a64fdc95 + 13-date silver rebuild + one B_00 --force-recent-days 20; CTO half @a31cfe4289
**Authored by:** 4.0.0_SA_CRO~DDD
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| G0 | verify | CTO guard: blank asset_id per account < 2, rows never drop; prior VersionIds | guard json | CTO guard PASS on 13 dates (09-30..10-16): blank/null AssetID rows 0 on every date (max per account 0); rows new-key >= old-key on every date (+2, 10-06 +5); prior silver/holdings VersionIds recorded in org/tier1_exec/4.0.0_SA_CRO~DDD/deliverables/S34_PREFLIGHT_GUARD_AND_PRIOR_VERSIONS_20261018.json | CLOSED 20261018T124747Z |
| R1 | s3-prefix | code/silver/cot_silver_merge.py | diff = b0a64fdc95 only; sha read-back | safe-deploy DEPLOYED [cot] + VERIFY OK; diff vs live (prior OZw3pdKN.., sha 72dcb7e5..) = b0a64fdc95 only (holdings key + fallback + _dedup_cols); s3 sha256 5a98df7a2b703f62a1c1b34c6cb9e364dd197c9301d48d4cafb272b6e1d6c741 == HEAD bytes | CLOSED 20261018T124943Z |
| S1 | activation | silver holdings --force x13 (sweep-free) | rows read back | AWS-RunShellScript 7418ec37 (no retry sweep) 12:50:46-12:52:41Z: cot_silver_merge --table holdings --date d --force for 13 dates; rows 20,844/20,892/20,921/20,946/20,981/21,026/21,284/21,301/21,303/21,310/21,380/21,512/21,520 = guard new-key counts exactly; no fallback line | CLOSED 20261018T125301Z |
| G1 | activation | gold build B_00 --force-recent-days 20 | account_performance 10-16 524,463,230.11, 10-15 530,421,988.14, 09-29 unchanged | B_00 --force-recent-days 20 by AWS-RunShellScript 12315695 (12:53:57-12:54:30Z; G4 invariants hold on every date); gold chain opal-cot-gold-run StartAt=A_05 050c9277 (12:57:52-13:00:22Z; a first StartAt=C_00 run ed83e87c skipped every step, C_00 is not in the cot chain, nothing written). account_performance before->after: 09-25 and 09-29 unchanged; 09-30 +51,152.80; 10-02 +51,264.39; 10-15 530,370,482.38 -> 530,421,988.14; 10-16 524,411,722.20 -> 524,463,230.11. SERVED platinum/firm/header_metrics.json 10-16 total.aua 524,463,230.11 = MDPF | CLOSED 20261018T130114Z |

## Log

- 20261018T124616Z OPENED by 4.0.0_SA_CRO~DDD with 4 leg(s)
- 20261018T124747Z LEG G0 closed: CTO guard PASS on 13 dates (09-30..10-16): blank/null AssetID rows 0 on every date (max per account 0); rows new-key >= 
- 20261018T124943Z LEG R1 closed: safe-deploy DEPLOYED [cot] + VERIFY OK; diff vs live (prior OZw3pdKN.., sha 72dcb7e5..) = b0a64fdc95 only (holdings key 
- 20261018T125301Z LEG S1 closed: AWS-RunShellScript 7418ec37 (no retry sweep) 12:50:46-12:52:41Z: cot_silver_merge --table holdings --date d --force for 
- 20261018T130114Z LEG G1 closed: B_00 --force-recent-days 20 by AWS-RunShellScript 12315695 (12:53:57-12:54:30Z; G4 invariants hold on every date); gold 
- 20261018T130114Z CLOSED -- all 4 legs proven
