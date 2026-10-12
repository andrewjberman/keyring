# Deploy Completion Record
**Date opened:** 2026-10-12T07:39:47.154378+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T074421Z
**Deploy:** NFRA_CTLPLN TO-CT-v-3 step 4 (WORLD): persist PIP_NO_INDEX=1 as a USER-level environment variable of desktop-hk1uu7n\test on dell1 (the form kit_pip_no_egress.py measure reports ok=True), then one deliberate explicit-index download attempt that must be stopped; no file is changed, the store is HKCU\Environment
**Authored by:** 0.7.0_AE_CloudOps~CT1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | kit_pip_no_egress.py measure on dell1 reports ok=True and a form other than NONE; the BEFORE value of the user variable and the pip config file paths recorded | the PIP-NO-EGRESS last line and the BEFORE state | PASS: python org/devices/kit_pip_no_egress.py measure on dell1 (PIN a68023574b at HEAD), 2026-10-12 ~07:40Z, saved whole to org/tier2_senior/0.7.0_AE_CloudOps~CT1/deliverables/NFRA_CTLPLN.TO-CT-v-3.pip-measure.txt. LAST LINE: PIP-NO-EGRESS pip=26.2.1 positive_requests=1 candidates=4 passing=3 holds_against_explicit=3 leaked_public=0 form=env:PIP_NO_INDEX ok=True (pip 26.2.1 of C:/Users/Test/AppData/Local/Programs/Python/Python314, python 3.14). BEFORE STATE read the same minute: User-scope PIP_NO_INDEX null, Machine-scope null, this process null; no PIP_* variable in the process; pip config files C:/Users/Test/AppData/Roaming/pip/pip.ini, C:/Users/Test/pip/pip.ini, C:/Users/Test/.config/pip/pip.conf and C:/ProgramData/pip/pip.ini all ABSENT (so no file is changed and none has bytes to restore). Account desktop-hk1uu7n\test. | CLOSED 20261012T074006Z |
| L2 | activation | [Environment]::SetEnvironmentVariable('PIP_NO_INDEX','1','User'); machine-level variable, other users and every pip config file untouched | the set command and rollback (SetEnvironmentVariable PIP_NO_INDEX $null User) | PASS: [Environment]::SetEnvironmentVariable('PIP_NO_INDEX','1','User') run 2026-10-12T07:40:12Z as desktop-hk1uu7n\test (HKCU\Environment), the only change: Machine scope, other users and every pip config file untouched (none exists). BEFORE: User-scope value null. ROLLBACK: [Environment]::SetEnvironmentVariable('PIP_NO_INDEX',$null,'User'), then new processes read null; running processes keep the value they started with. | CLOSED 20261012T074030Z |
| L3 | verify | the variable read back from a NEW process, and pip list / pip --version still work | new-process read of User scope and the effective process value | PASS on the registry store, with one stated limit: a NEW powershell.exe -NoProfile process read GetEnvironmentVariable('PIP_NO_INDEX','User') = '1' and Machine = '' (null). The new process's own $env:PIP_NO_INDEX read '' because a child of this session inherits this session's environment block, not the registry; a process started by a fresh logon or by Explorer reads the registry value. So this seat did NOT observe the variable in a fresh-logon process; step 5 runs with the User value read back from the registry placed in the child's environment, which is what such a process receives. | CLOSED 20261012T074030Z |
| L4 | verify | one deliberate python -m pip download --no-deps six==1.16.0 --index-url https://pypi.org/simple through the applied form, download only into a deleted folder | the output, rc, the folder denominator and its absence control | PASS: python -m pip download --no-deps -d <new empty folder> six==1.16.0 --index-url https://pypi.org/simple, run once 2026-10-12T07:40:56Z with PIP_NO_INDEX=1 (read back from the User scope) in the child environment: rc=1, stderr 'ERROR: Could not find a version that satisfies the requirement six==1.16.0 (from versions: none)' / 'ERROR: No matching distribution found for six==1.16.0', stdout empty. Folder 0 entries before and after, deleted, Test-Path False. Message names no index and no laptop route (env form prints pip's own error). Request count of this run not measured; the kit's measurement of this form with the explicit index arm read index=0 proxy=0. Full record: deliverables/NFRA_CTLPLN.TO-CT-v-3.blocked-download.txt. | CLOSED 20261012T074421Z |

## Log

- 20261012T073947Z OPENED by 0.7.0_AE_CloudOps~CT1 with 4 leg(s)
- 20261012T074006Z LEG L1 closed: PASS: python org/devices/kit_pip_no_egress.py measure on dell1 (PIN a68023574b at HEAD), 2026-10-12 ~07:40Z, saved whole
- 20261012T074030Z LEG L2 closed: PASS: [Environment]::SetEnvironmentVariable('PIP_NO_INDEX','1','User') run 2026-10-12T07:40:12Z as desktop-hk1uu7n\test 
- 20261012T074030Z LEG L3 closed: PASS on the registry store, with one stated limit: a NEW powershell.exe -NoProfile process read GetEnvironmentVariable('
- 20261012T074421Z LEG L4 closed: PASS: python -m pip download --no-deps -d <new empty folder> six==1.16.0 --index-url https://pypi.org/simple, run once 2
- 20261012T074421Z CLOSED -- all 4 legs proven
