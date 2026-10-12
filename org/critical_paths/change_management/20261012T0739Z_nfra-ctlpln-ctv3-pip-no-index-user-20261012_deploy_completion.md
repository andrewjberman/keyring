# Deploy Completion Record
**Date opened:** 2026-10-12T07:39:47.154378+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN TO-CT-v-3 step 4 (WORLD): persist PIP_NO_INDEX=1 as a USER-level environment variable of desktop-hk1uu7n\test on dell1 (the form kit_pip_no_egress.py measure reports ok=True), then one deliberate explicit-index download attempt that must be stopped; no file is changed, the store is HKCU\Environment
**Authored by:** 0.7.0_AE_CloudOps~CT1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | kit_pip_no_egress.py measure on dell1 reports ok=True and a form other than NONE; the BEFORE value of the user variable and the pip config file paths recorded | the PIP-NO-EGRESS last line and the BEFORE state |  | OPEN |
| L2 | activation | [Environment]::SetEnvironmentVariable('PIP_NO_INDEX','1','User'); machine-level variable, other users and every pip config file untouched | the set command and rollback (SetEnvironmentVariable PIP_NO_INDEX $null User) |  | OPEN |
| L3 | verify | the variable read back from a NEW process, and pip list / pip --version still work | new-process read of User scope and the effective process value |  | OPEN |
| L4 | verify | one deliberate python -m pip download --no-deps six==1.16.0 --index-url https://pypi.org/simple through the applied form, download only into a deleted folder | the output, rc, the folder denominator and its absence control |  | OPEN |

## Log

- 20261012T073947Z OPENED by 0.7.0_AE_CloudOps~CT1 with 4 leg(s)
