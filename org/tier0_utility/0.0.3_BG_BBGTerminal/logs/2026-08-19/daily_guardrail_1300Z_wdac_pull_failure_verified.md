# 0.0.3_BG_BBGTerminal — Daily Guardrail — 2026-08-19 (~1300Z)
**archetype:** VALIDATE

Triggered by MSTR~Z's 125642Z inbound (07:00 pull failed, WDAC block, rectified). I did NOT close on
the relay — a relay inherits its author's grounding, and the guardrail is my seat's duty. Re-derived
every limb independently. **MSTR's account reproduces in full. Two things it did not carry are below.**

## VERDICT: served data is CORRECT and HEALTHY. The 07:00 scheduled run FAILED and did not self-heal.

## Limb 1 — scheduled task (measured, not relayed)
`OPAL_BBGTML_daily_pull`: LastRunTime **2026-08-19 07:00:01 ET**, **LastResult = 1 (FAILED)**,
NextRun 2026-08-20 07:00, **NumberOfMissedRuns = 0**. `OPAL_vendor_watch` 08:09 ET rc=0.

⚠ **`NumberOfMissedRuns = 0` ON A FAILED RUN.** The counter counts runs that never STARTED; it is
blind to a run that started and returned rc=1. My 08-18 log warned a successor reading only this
field would infer clean mornings — **today it would have inferred a clean morning on a run that
failed outright.** MissedRuns is not a health instrument. LastResult is.

## Limb 2 — served artifact (independent live read, not the producer's rc)
`s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json`
LastModified **2026-08-19T12:55:37Z**, 19,201 B, ETag 8fa295250997e2ea1f16174bfb46ba8b
Body: `data_as_of` **2026-08-18**, `generated_at` **2026-08-19T12:55:36Z**.

## Limb 3 — trading calendar RESOLVED FIRST (NEVER#1)
`expected_last_trading_day(2026-08-19) = 2026-08-19` (Wednesday, no holiday).
Served 2026-08-18 -> `trading_days_behind = 1` = **the correct healthy state for a T-1 pipeline.**

## Limb 4 — `.ST` CIX content check — RUN BECAUSE TODAY MATCHED THE HAZARD SHAPE, AND IT PASSED
Yesterday's reboot #2 is a logout-class event and CIX resolution is **login-scoped** (08-03 incident),
so a pull executing after it is exactly the case that can succeed and still carry wrong custom-index
data. Measured on today's PKL through the pull's own `cma` interpreter:

| ticker | rows | inception | latest (2026-08-18) | vs 08-17 |
|---|---|---|---|---|
| `.ST Index` | 688 | 2023-12-29 @ 100.0 | 113.1072 | 113.0911 (+0.014%) |
| `.ST_BMK Index` | 688 | 2023-12-29 @ 100.0 | 118.6242 | 118.6699 (-0.039%) |
| `.ST_ETF Index` | 688 | 2023-12-29 @ 100.0 | 118.1081 | 118.1965 (-0.075%) |

**688 = 687 on 08-17 + exactly the 1 trading day since.** Not the known 1449-row/~1.9 mis-resolution.
**Denominator printed:** 112,289 `return_daily` rows (= 112,205 + 84, one day across 84 tickers),
84 distinct tickers, 2,064 matched `.ST*` (= 2,061 + 3). **Positive control** `SPX Index` = 1,413
(= 1,412 + 1); **negative control** (bogus ticker) = 0. The instrument discriminates in both
directions, so the zero would have meant something. Queried on `bbg_ticker`, not `index_name`.

## Limb 5 — the fix, exercised not assumed
`psutil` **7.2.2 pip wheel**, LOADED under the cma interpreter (`cpu_count` returned 20 — an
execution, not an import-resolution). `blpapi` 3.26.4.2, pandas 2.2.3, ipykernel 6.29.5 all load.

Timeline reconstructed from CodeIntegrity events + file mtimes (all ET):
`07:00:05` psutil blocked -> `07:00:07` **pywintypes313.dll blocked** -> `07:00:08` psutil blocked
-> `08:47:30` psutil blocked (repro) -> `08:49:27` psutil blocked (final repro), **pip wheel written
08:49:27.758** -> PKLs written **08:51/08:52** -> publish **08:55:36 ET / 12:55:36Z**.
**ZERO CodeIntegrity blocks after 08:49:27** — including none during the successful pull.

## >> FINDING 1 (new, not in the relay): THE FAILING RUN BLOCKED A SECOND BINARY, AND THE FIX COVERED ONE
`\Anaconda\envs\cma\Lib\site-packages\win32\pywintypes313.dll` (pywin32 **307, conda-owned**,
dated 2024-10-11) took the same 3077/3033 pair at **07:00:07**, same policy ID
`{0283ac0f-fff1-49ae-ada1-8a933130cad6}`. The rectification was psutil-only.

**Honest bound — I am NOT claiming this breaks tomorrow.** It fired ONCE, in the failing run, and did
**not** recur in the successful 08:51 pull; `import pywintypes` currently succeeds, resolving to a
**different copy of the same DLL** (`site-packages\pywin32_system32\pywintypes313.dll`). So it may
have been a fallback probe taken only while the kernel was already dying. **Which of those it is, is
UNDETERMINED** and I did not determine it. What IS measured: a second unsigned conda-owned binary in
this run path is known to the policy, and it is unremediated. The class has two members, not one.

## >> FINDING 2 (new): CONDA STILL BELIEVES IT OWNS psutil 7.0.0 — THIS IS THE RESURRECTION PATH
`conda-meta/psutil-7.0.0-py313ha7868ed_0.json` is still present while disk carries the pip 7.2.2
wheel. MSTR's warning ("a conda reinstall/update would resurrect the BLOCKED binary") is not a
caution about a hypothetical — **the record and the disk actively disagree right now**, so any conda
operation touching this env resolves that disagreement in conda's favour, silently, and restores the
blocked `.pyd`. Nobody has to reinstall psutil deliberately; a dependency pull is enough.

## Bearing on the decision Andrew owns (MSP exemption vs standing risk)
Both findings push the same way: per-binary remediation is whack-a-mole against a **reputation-class**
policy over an env full of unsigned conda binaries. I take NO action on it — routing only.

## Actions taken
None on the machine. Read-only throughout. No workaround, no env change, no send.
Tomorrow's 07:00 fire remains the real acceptance and I will read it.

## Compiler Tools
None fit. The surfaces were a Windows Scheduled Task record, the CodeIntegrity event log, local PKL
contents through the `cma` interpreter, conda-meta/pip metadata, and ONE served-artifact content read
by exact key. `comp-freshness` answers "is the object old", which is not "does the body carry the
right `data_as_of`"; no comp tool models Scheduled Tasks, WDAC events, PKL contents, or conda envs.
