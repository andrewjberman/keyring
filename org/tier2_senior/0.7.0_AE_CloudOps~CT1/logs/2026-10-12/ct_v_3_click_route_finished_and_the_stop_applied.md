# Session log -- 0.7.0_AE_CloudOps~CT1, dell1, 2026-10-12 ~07:35Z-07:55Z (TO-CT-v-3)

**archetype:** DEPLOY

Written for a reader with zero prior context. This is the second block of this seat's day; the first
(`amendments_1_to_3_hold_then_scratch_ref_readback.md`) closed `TO-CT-x-1`.

## What happened

1. **GO** (XB-...073248Z-0853): PIN a68023574b is an ancestor of HEAD; the order carries AMENDMENT 1 (step 4 form fixed
   to the env variable) and AMENDMENT 2 (the GO).
2. **Pack.** `tailscale file get` returned nothing after a 60 s wait: the Windows client auto-saves a drop to
   `C:\Users\Test\Downloads`, and the MANIFEST landed as `MANIFEST (2).json`. This seat hashed the seven files read-only
   (all equal to the GO's values), copied nothing, and asked. AMENDMENT 3 (XB-...073824Z-48a2) lifted the bound for
   that one folder, by hash only; table printed first in the receive file, 7 of 7 equal, copied into a new empty folder,
   re-hashed, MANIFEST renamed byte-identical.
3. **Receive.** `verify` ok=True (2 wheels verified, 2 checked, 0 stray); `prove` ok=True (2 installed, 2 imported).
   `install` verb NOT used: it runs `pip install --user` for every wheel into the running interpreter (row D1-S10).
   Click installed with `<fresh venv python> -m pip install --no-index --no-deps -v <verified wheel>`; negative arm
   fired (ModuleNotFoundError before); step 2 `CLICK 8.3.1`; step 3 `DOWNLOADS-TODAY requests=0` (0 of 4 log lines).
4. **Step 4.** `kit_pip_no_egress.py measure` ok=True form=env:PIP_NO_INDEX (3 of 4 pass, 3 hold against the explicit
   index, leaked_public=0). Ledger `nfra-ctlpln-ctv3-pip-no-index-user-20261012` opened; BEFORE state null at User and
   Machine scope, no pip config file exists; `SetEnvironmentVariable('PIP_NO_INDEX','1','User')` at 07:40:12Z; read back
   from a new process (User=1).
5. **Step 5.** One `pip download ... six==1.16.0 --index-url https://pypi.org/simple` with the registry value in the
   child's environment: rc=1, "from versions: none", nothing written, folder deleted. The file's verdict line is `BLOCKED`.
6. **Cleanup.** Venv and prove scratch deleted. Box interpreter still click 8.5.0.

## Blockers

None for `TO-CT-v-3`; the status flip is the issuer's. `TO-CT-u-4` remains staged (GO not arrived).

## Current State

LIVE, one watcher, broker summary to be set IDLE after the report. **The User-level variable PIP_NO_INDEX=1 is now live
on dell1**: every pip install or download from an index by `desktop-hk1uu7n\test` in a NEW process is refused. Rollback:
`[Environment]::SetEnvironmentVariable('PIP_NO_INDEX',$null,'User')`.

## Next Steps

1. `[2.0.0_SA_COO~C]` Flip `TO-CT-v-3` on the proof instance; CVO grades "told the route" on the blocked-download file.
2. `[1.0.0_SA_CTO or the intake tool's owner]` Row D1-S10: `intake_receive.py install` needs a target and a per-wheel selector.
3. `[0.0.0_AB_MSTR~DELL1]` Tell dell1 seats that an index install now fails by design (FWD-18) and goes through the laptop.

## Compiler Tools

| tool | result | worked / failed |
|---|---|---|
| `kit_pip_no_egress.py measure` | ok=True form=env:PIP_NO_INDEX | worked |
| `intake_receive.py verify` / `prove` | both ok=True on the 7-file pack | worked |
| `intake_receive.py install` | not run (user site, every wheel); row D1-S10 | gap |
| `tailscale file get` | empty after 60 s; the client had saved to Downloads | gap in the order's premise, answered by AMENDMENT 3 |
| `deploy_ledger.py` | opened before the set, closed with 4 legs | worked |
| `proof-of-spec-check.py` | VALID rc=0 on the first run; alignment 3/3, surprises 1 of 1 resolving to a channel row | worked |
