# Deploy Completion Record
**Date opened:** 2026-06-30T20:16:10.154123+00:00
**Status:** OPEN
**Deploy:** ADVI_BREAKS TO-3 49F served un-freeze: BD-DataMining unrealized template (431167) facts-catalog restore (facts empty -> 1 Fact/id17 MV) -- the served-AUA freeze ROOT -- plus the no-zero BRANCH-A guard. Empty facts -> 0-row unrealized -> B_01 mass-close -> D_03 empty -> D_04 publish HALT (49F served frozen 06-26). Full forensic narrative: session log 704fd7824.
**Authored by:** 0.4.0_DS_ClientPlatform~B
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit + s3 cp opal-data-bd/code/bronze/templates/unrealized.json | commit hash + live S3 facts=1/id17 MV | 82009e463 (repo-track unrealized.json under data/black_diamond/scripts/bronze/templates/) + s3 cp; live S3 facts=1/id17 Market Value verified | CLOSED 20260630T201640Z |
| L2 | activation | BD --provision -> NEW persisted templateId carrying populated facts (0.6.0_AE) | created-template facts non-empty + persisted id N, BD GET verified | 0.6.0_AE --provision -> NEW persisted templateId 486228; BD GET /template/486228 verified facts=1/id17 | CLOSED 20260630T201640Z |
| L3 | git | templateId 431167->N committed + s3 cp | commit hash + live S3 templateId=N/facts=1 | c36aa98ca (templateId 431167->486228) + s3 cp; live S3 templateId=486228/facts=1/id17 verified | CLOSED 20260630T201640Z |
| L4 | verify | persisted N test-pull non-empty (0.6.0_AE) | row-count ~471K non-empty unrealized export | 0.6.0_AE test-pull persisted 486228 NON-EMPTY: forwardfill_v2/unrealized/UNREALIZED_DAILY_2026-06-29.xlsx = 471,601 rows; silver/unrealized/2026-06-29.parquet = 102,862 holdings (independently verified NEVER#5) | CLOSED 20260630T201640Z |
| L5 | git | BRANCH-A no-zero guard: D_00._resolve_served_aua (3 served sites) + C_02 skip-degenerate-cert + DEGENERATE_CERT_MODE env (hold-or-gold) | commit hash + safe-deploy MATCH (gold code prefix) | b5a95c9f5 no-zero guard (D_00 _resolve_served_aua 3 sites + C_02 skip-degenerate + DEGENERATE_CERT_MODE default hold) + 2acfb0401 converter 0-row guard; safe-deploy PASS auto-deployed to opal-data-bd/code/gold | CLOSED 20260630T201641Z |
| L6 | verify | 23:00Z scheduled gold served un-freeze (NEVER#4, on the scheduled run) | served data_as_of 06-24->06-29 + served total.aua==certified_aua ~1.83B + certified==silver/alloc[06-29] mv-sum(excl-mask) to cent + gold_aua==holdings[06-29] mv-sum to cent + gold-freshness: canonical_holdings+client_performance LastModified > 2026-06-30T21:39:59Z (rebuilt ON the re-landed 21:39Z unrealized silver) |  | OPEN |

## Log

- 20260630T201610Z OPENED by 0.4.0_DS_ClientPlatform~B with 6 leg(s)
- 20260630T201640Z LEG L1 closed: 82009e463 (repo-track unrealized.json under data/black_diamond/scripts/bronze/templates/) + s3 cp; live S3 facts=1/id17 
- 20260630T201640Z LEG L2 closed: 0.6.0_AE --provision -> NEW persisted templateId 486228; BD GET /template/486228 verified facts=1/id17
- 20260630T201640Z LEG L3 closed: c36aa98ca (templateId 431167->486228) + s3 cp; live S3 templateId=486228/facts=1/id17 verified
- 20260630T201640Z LEG L4 closed: 0.6.0_AE test-pull persisted 486228 NON-EMPTY: forwardfill_v2/unrealized/UNREALIZED_DAILY_2026-06-29.xlsx = 471,601 rows
- 20260630T201641Z LEG L5 closed: b5a95c9f5 no-zero guard (D_00 _resolve_served_aua 3 sites + C_02 skip-degenerate + DEGENERATE_CERT_MODE default hold) + 
- 20260630T220810Z L6 CONTRACT TIGHTENED (COO 220523Z + 0.6.0 catch, ~B respawn ack 220716Z): added gold-freshness tie -- 23:00Z gold canonical_holdings+client_performance LastModified MUST be > 21:39:59Z (incorporates the re-landed unrealized silver). gold ts < 21:39Z at 23:00Z = re-run-gold-before-serve trigger, NOT a pass. 5 ties total now.
- 20260630T222313Z L6 NEVER-WIDEN GATE (COO 222020Z): the 06-26->06-29 served advance is a WIDEN -> requires explicit Andrew serve-GO before served moves. Mechanism ground-confirmed (FLIP is DEFAULT: B_00 nightly --force-recent-days 14 auto-seals 06-29 [gold_dispatch.sh:84, B_00:967/976/984/217], D_00 served as_of=perf.date.max() [D_00:615/707], live watermark max-sealed 06-26/06-29-unsealed but force-recent overrides). So L6 close now requires BOTH the 5-tie mechanical PASS AND Andrew's never-widen serve-GO. COO taking serve-vs-hold to Andrew (~38min to 23:00Z). HOLD = active EventBridge gate (AE lane), FLIP = default.
