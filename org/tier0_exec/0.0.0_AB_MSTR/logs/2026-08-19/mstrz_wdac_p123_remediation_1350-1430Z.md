# MSTR~Z — WDAC Option-C remediation P1+P2+P3 EXECUTED + re-exercised (2026-08-19)

**archetype:** DEPLOY
**Authorization:** Andrew-direct at this console, same session as the census: *"ok proceed
with P1+P2+P3 now"* — superseding the wait-for-acceptance sequencing; tomorrow's 07:00 fire
now accepts the FULL remediated state (his call, noted at execution time).
**Env:** `C:\Anaconda\envs\cma` (Bloomberg pull). Backups: 3 conda-meta records copied to
session scratchpad `p123_backup/` before any change.

## Executed

| act | before | after | exercised |
|---|---|---|---|
| P1 pywin32 | conda 307 (member #2, blocked once 07:00) | **PyPI 312** (clean uninstall→install) | pywintypes, pythoncom, win32api, win32com.client, win32con all import OK |
| P3 debugpy | conda 1.8.14 | **PyPI 1.8.21** | import OK |
| P2 conda-meta | psutil-7.0.0 / pywin32-307 / debugpy-1.8.14 records on disk, disagreeing with pip reality | records REMOVED (backed up) + `conda-meta/pinned` written: `psutil >=7.2.2`, `pywin32 >=312`, `debugpy >=1.8.21` with a comment citing the census | residual conda-meta mentions: 0. A future conda solve touching these now fails LOUD instead of silently resurrecting a blocked binary |

## Re-exercise (full ad-hoc end-to-end, 10:21 ET, rc=0)

- **Pull leg — the leg that died at 07:00 — fully exercised on the final state:** fresh
  Bloomberg pull, kernel started clean, tripwire PASS (all model checks, as-of 2026-08-18
  matches expected business day).
- **Publish leg: idempotence guard SKIP** — *"portal already serves data_as_of 2026-08-18
  ... NOT re-firing"* — correct; the publish path was exercised at 08:55 ET today and its
  components were untouched by P1/P3 (kernel-side changes only).
- **Code Integrity events since 08:49:28 (covers swaps + import tests + this run): ZERO.**
- Served object re-read: unchanged and correct (data_as_of 2026-08-18, 12:55:37Z) — the
  SKIP is why, and it is the right behavior.

## State after this act

- All three fired-or-adjacent WDAC class members in the pull chain are PyPI-wheel,
  pip-owned, pinned against conda resurrection. Census stands: no other in-chain unsigned
  member (`MSTRZ_WDAC_OPTIONC_EXPOSURE_CENSUS_20260819.md`).
- **True acceptance = 08-20 07:00 scheduled fire** (new as-of ⇒ publish leg fires for
  real). Read at the served object by this seat + BG guardrail.
- MSP path stays DEFERRED (Andrew's word); Python311 niche-wheel tail remains the
  no-local-remedy residual.

## Compiler Tools

None run — single-env remediation grounded on pip/conda state, live imports (EXERCISED),
the CodeIntegrity event oracle, and the pipeline's own end-to-end run. No coverage gap.
