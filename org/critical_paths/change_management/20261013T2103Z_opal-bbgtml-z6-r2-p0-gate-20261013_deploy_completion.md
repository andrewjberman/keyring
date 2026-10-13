# Deploy Completion Record
**Date opened:** 2026-10-13T21:03:22.582085+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261013T213057Z
**Deploy:** OPAL_BBGTML Z6 R2: bbg_fallback.ps1 P0 gate classifies listener-up-not-entitled
**Authored by:** 0.7.0_AE_CloudOps~ZS
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | bbg_fallback.ps1 edit in the shared working tree (the deploy) | commit hash | Edit committed f6cc68d6bf on box/sitez, author 0.7.0_AE_CloudOps~ZS. ONE file: integrations/bloomberg/auth/bbg_fallback.ps1, STEP 2 only, +4/-1. Bytes sha256 5aeb770858cead537dd8106754324a3428a580260cb259a2855f3c89395d9193 -> f717d111e21f30fd759c7d6cc45d9306feaf7da6b909541c42bbde18cd758bc5 (8453->8800 bytes, 111->114 lines), CRLF preserved on all 114 lines, 0 non-ASCII. Saving the file IS the deploy: it is live in the shared working tree the Scheduled Task OPAL_BBGTML_daily_pull runs. The commit-gate checked 0 of 1 files (.ps1 is outside its suffix set), so the language-appropriate instrument was run instead: [Parser]::ParseFile = 0 errors against a planted-syntax-error control that read 1. AC3 pinned to the edit commit (HEAD had moved to a peer's e488418898): git diff --stat f6cc68d6bf~1 f6cc68d6bf -- integrations/bloomberg/ = '1 file changed, 4 insertions(+), 1 deletion(-)', and name-only over the whole commit lists only bbg_fallback.ps1. | CLOSED 20261013T212946Z |
| L2 | verify | AC1 + AC2 real runs | check output | AC1 PASS exit=0, run from the shared repo root ~21:10Z against the deployed bytes: '8194 listeners before run: 1' then the fallback printed 'DAPI DOWN.' / 'P0 gate: 8194 listening (3/3) but dapi_check failed -> listener up, not entitled -> sign-in warranted.' / 'P0 gate: transport sustained-down, network OK -> sign-in warranted.' / 'fire-once ledger clear (0 in 6h).' / 'STUB: would now fill -> verify -> submit ONCE.' fallback rc=0, last line 'R2: PASS (classified listener-up-not-entitled and reached the sign-in path)'. NO 'not sustained-absent' line. AC2 PASS exit=0, un-forced: the real state took the FIRST accepted branch, 'DAPI UP -- proceed with pull, no sign-in needed.' AC3 PASS (see L1). EVIDENCE LIMIT, recorded not hidden: AC1 reaches the new branch only under -ForceDown, which short-circuits Dapi-Up before dapi_check runs, and AC2's real state was UP, so the classification is proven against a FORCED STEP-1 failure and never against a genuinely un-entitled session (surprise row OPAL_BBGTML-Z-S16). Three rows filed @ee4040615e: Z-S15 the gate's self-contradicting trailing line, Z-S16 wintrv is not a signed-out oracle (dapi_check read 'entitled session live' at 21:14:16Z with wintrv count 0), Z-S17 BLOCKING/ARMED the sign-in-script no-modify order the ruling does not cite. Rollback remains one command to sha256 5aeb7708. | CLOSED 20261013T213019Z |

## Log

- 20261013T210322Z OPENED by 0.7.0_AE_CloudOps~ZS with 2 leg(s)
- 20261013T212946Z LEG L1 closed: Edit committed f6cc68d6bf on box/sitez, author 0.7.0_AE_CloudOps~ZS. ONE file: integrations/bloomberg/auth/bbg_fallback.
- 20261013T213019Z LEG L2 closed: AC1 PASS exit=0, run from the shared repo root ~21:10Z against the deployed bytes: '8194 listeners before run: 1' then t
- 20261013T213057Z CLOSED -- all 2 legs proven
