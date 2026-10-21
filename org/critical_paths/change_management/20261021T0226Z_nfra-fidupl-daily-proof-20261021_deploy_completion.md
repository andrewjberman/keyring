# Deploy Completion Record
**Date opened:** 2026-10-21T02:26:46.685569+00:00
**Status:** OPEN
**Deploy:** NFRA_FIDUPL FT-s-8: config.daily.json on the box (step 1, no sign-in); the daily-mode proof run held for the issuer's GO
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | ec2-baked-asset | /opt/fidelity-uploader/config.daily.json = config.json plus mode, firm_labels, account_columns only; config.json untouched | key-name list, json.tool valid, config.json md5 equal before and after; ft8c R1-FT8C-OK |  | OPEN |
| L2 | activation | ONE run of box/run.py on config.daily.json (one sign-in, 31-fold G switch) - HELD for the issuer's GO | stdout lines verbatim; ft8r R1-FT8R-OK |  | OPEN |

## Log

- 20261021T022646Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 2 leg(s)
