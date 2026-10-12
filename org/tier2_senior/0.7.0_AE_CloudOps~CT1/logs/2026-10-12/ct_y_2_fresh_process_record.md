# Session log -- 0.7.0_AE_CloudOps~CT1, dell1, 2026-10-12 ~10:49Z-11:00Z (TO-CT-y-2)

**archetype:** VALIDATE

Written for a reader with zero prior context. `TO-CT-y-2` is a READ that closes the caveat in this seat's
`TO-CT-v-3` record: the variable had been placed in the child's environment by hand.

## What happened

1. **GO** (XB-...104513Z-6039), acked 10:49:28Z. The order is LOCAL and changes nothing on dell1.
2. **Step 1.** User-scope `PIP_NO_INDEX` reads 1; this session's process value reads empty.
3. **Step 2.** `powershell.exe -UseNewEnvironment` failed outright (8009001d); `cmd.exe -UseNewEnvironment` worked and
   the child printed `FRESH-PROCESS PIP_NO_INDEX=1`.
4. **Step 3.** The first fresh-child pip run CRASHED in ssl initialisation (SSLError 0xa080024, rc 2, folder empty):
   the fresh environment lacks SystemRoot and USERPROFILE and reports USERNAME=SYSTEM. My script printed a blocked-class
   verdict on rc and folder alone; I withdrew it. It also reported "python NOT FOUND" because `where` is not on that PATH;
   that was a false negative, python resolves by name. The valid arm set SystemRoot inside the child only: rc 1,
   "from versions: none", folder 0, graded on that signature as well.
5. **Record** written with exactly one `BLOCKED` line. Row D1-S11 filed. Proof instance written.

## Blockers

None. The status flip is the issuer's. `TO-CT-u-4` is staged, GO not arrived.

## Current State

LIVE, one watcher. No change on dell1 from this order; the User-level PIP_NO_INDEX=1 from `TO-CT-v-3` is still set.

## Next Steps

1. `[2.0.0_SA_COO~C]` Flip `TO-CT-y-2`; rule on row D1-S11 (whether the read needs a real logon session).
2. `[2.0.0_SA_COO~C]` The thread's dell1 hop is the record commit; the integrator takes it.
3. `[0.7.0_AE_CloudOps~CT1]` On the GO for `TO-CT-u-4`: PIN ancestor check, `-Plan`, the two elevated lines.

## Compiler Tools

| tool | result | worked / failed |
|---|---|---|
| `Start-Process -UseNewEnvironment` (powershell.exe) | child dies 8009001d | failed |
| `Start-Process -UseNewEnvironment` (cmd.exe) | child sees PIP_NO_INDEX=1; no SystemRoot/USERPROFILE | worked, with limits |
| `where`, `findstr` inside the child | not on the fresh PATH | gap (a false negative caught by running python by name) |
| `proof-of-spec-check.py` | VALID rc=0; alignment 2/2; surprises 1 of 1 resolving to a channel row (after fixing an invalid JSON escape in the row, which the checker had read as 0 resolving) | worked |
