# Deploy Completion Record
**Date opened:** 2026-10-06T17:28:47.879440+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261006T173423Z
**Deploy:** ETFS_RIVALS round 12: five rivalfunds Lambdas at pin CLOUD 50a2248fe9 (plan 0/5/0), one 2026-10-06 republish (au-1: audit off the page, every dialog kept)
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| N1 | activation | safe-apply C:/tmp/rv_apply12.tfplan from C:/tmp/rv-r8 @50a2248fe9 (5 code hashes) | apply output: 0 added, 5 changed, 0 destroyed | 17:29:44-17:31:31Z: HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/etfs-rivalfunds apply C:/tmp/rv_apply12.tfplan from C:/tmp/rv-r8 @50a2248fe9: Apply complete! Resources: 0 added, 5 changed, 0 destroyed (rc 0) | CLOSED 20261006T173233Z |
| N1v | verify | 5 live CodeSha256 equal the plan after-hashes (CTO condition 1) | get-function-configuration x5 | 17:3xZ: 5/5 live CodeSha256 equal the plan after-hashes (daily vOcweDKE, fetch NJEhVOcs, canonical S5Q1EsSv, silver 4cA4RBMy, publish r+H1xDcI), all LastUpdateStatus Successful | CLOSED 20261006T173233Z |
| P1 | activation | invoke etfs-rivalfunds-daily-lambda only:[publish-page] 2026-10-06 batch rv-publish-1006r12 refresh_a1 false, retries off | response status | 17:32:33-17:33:01Z: invoke etfs-rivalfunds-daily-lambda {only:[publish-page], date 2026-10-06, batch rv-publish-1006r12, refresh_a1 false}, AWS_MAX_ATTEMPTS=1: 200, no FunctionError, REPORT 458a7968 25.2 s / 413 MB; status OK; outputs index.html, audit.html, manifest.json; detail.ai SKIPPED_EXISTS | CLOSED 20261006T173330Z |
| P1v | verify | served platinum/page/date=2026-10-06 read back (CTO condition 2) | dialogs on, >=20% headroom, 0 dead, no audit link, 13/13 funds | 17:3xZ: served platinum/page/date=2026-10-06 read from S3 (index.html LastModified 17:33:01Z, 1,294,421 B): batch rv-publish-1006r12, published, 13/13 funds; holding_dialogs on; headroom 33.6% under DIALOG_SOFT_CAP (>=20%); 2,073 data-sec buttons, 424 dialogs, 0 dead; no audit block, no audit link; audit.html 1,326,857 B, 0 dead. Equals the pre-act measured render byte count | CLOSED 20261006T173359Z |

## Log

- 20261006T172847Z OPENED by 2.0.0_SA_COO~RV with 4 leg(s)
- 20261006T173233Z LEG N1 closed: 17:29:44-17:31:31Z: HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/etfs-rivalfunds apply C:/tmp/rv_appl
- 20261006T173233Z LEG N1v closed: 17:3xZ: 5/5 live CodeSha256 equal the plan after-hashes (daily vOcweDKE, fetch NJEhVOcs, canonical S5Q1EsSv, silver 4cA4
- 20261006T173330Z LEG P1 closed: 17:32:33-17:33:01Z: invoke etfs-rivalfunds-daily-lambda {only:[publish-page], date 2026-10-06, batch rv-publish-1006r12,
- 20261006T173359Z LEG P1v closed: 17:3xZ: served platinum/page/date=2026-10-06 read from S3 (index.html LastModified 17:33:01Z, 1,294,421 B): batch rv-pub
- 20261006T173423Z CLOSED -- all 4 legs proven
