# Deploy Completion Record
**Date opened:** 2026-10-09T02:21:29.024483+00:00
**Status:** OPEN
**Deploy:** partner_roster T-1 into its two live readers: leg A bundles.accrual_bridge re-mint, leg B emitter vendored roster on a PINNED build (TO ADHOC.partner-roster-t1-into-live-readers, GO msg 1448, risk SERVED)
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 20.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | s3-prefix | opal-data-assets portal/gold/mdpf/_code/mdpf-accrual-bridge.tar.gz re-mint from HEAD via safe-deploy in-flow mint | new VersionId + TOOL-03/mint output line |  | OPEN |
| A2 | verify | head-object metadata roster-authority-sha256=4c104d9b.. script-sha256=648cf3f5.. unchanged | head-object Metadata read |  | OPEN |
| B0 | verify | CONTROL, NO WRITE: name the commit whose BUILD_ONLY emitter build reproduces live CodeSha256 n/Tu1ns1..; none -> STOP leg B | build sha256 base64 equality |  | OPEN |
| B1 | verify | build = B0 tree with ONLY partner_roster.json replaced by HEAD bytes (LF); roster md5 3d309b26, every other member hash = B0 | per-member hash comparison |  | OPEN |
| B2 | activation | upload artifact + targeted plan 0/1/0 + safe-apply -target on the emitter module | plan counts + apply output |  | OPEN |
| B3 | verify | get-function-configuration CodeSha256 = the B1 build | CodeSha256 read |  | OPEN |
| B4 | verify | next scheduled opal-assets-daily-emitter-daily run cron(15 17 * * ? *): Cottonwood rows read declared_cadence T-1 | emitter row read after the 17:15Z run |  | OPEN |

## Log

- 20261009T022129Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 7 leg(s)
