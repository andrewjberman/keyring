---
name: terminal-upload
description: One-command daily Bloomberg pipeline from the terminal machine - pull the data/model PKLs through Yang's notebooks (run_daily_pull.py + tripwire), then push them through the portal /data-refresh channel (opal_data_refresh_upload) and confirm the portal serves the new date - no UI. Use when asked to "run the terminal upload", "pull and upload the PKLs", "refresh the dashboard from the terminal", or to re-send already-pulled PKLs ("send-only"). Runs ONLY on the Bloomberg terminal machine. Born 2026-08-03 from the ST-mapping incident; folds its failure signatures.
---

# /terminal-upload — pull the PKLs and upload through data-refresh, no UI

One command replacing the two-step human flow (double-click `run_daily_pull.bat`, then open the
portal DataRefresh UI): **pull -> tripwire -> upload -> pipeline -> confirm served**. Yang's
notebooks are UNTOUCHED — this wraps them, exactly like the `.bat` does. The upload leg is the
gateway's server-side `opal_data_refresh_upload` (the same channel the UI uses): the big files
never pass through the chat, and it returns three confirmations (uploaded / pipeline /
displayed) so nothing half-lands silently.

## Invocation forms

| Form | Behavior |
|---|---|
| `/terminal-upload` | Full run: pull both notebooks + tripwire + REAL upload + verify served. |
| `/terminal-upload dry` | Pull + tripwire + `dry_run=True` upload (lands in pending/, NO pipeline fire). The safe exercise. |
| `/terminal-upload send-only` | Skip the pull (PKLs already produced today): tripwire only (`--skip-pull`) + upload + verify. |
| `/terminal-upload pull-only` | Pull + tripwire, stop before any upload. |
| `--allow-stale N` | Pass through to the tripwire (post-holiday mornings where as-of is legitimately older). |
| `--date YYYYMMDD` | Send a specific vintage instead of today's (passed to the upload tool). |

**Invoking this skill IS the send authorization** — the real upload passes `confirm=True`
because the operator asked for exactly this. `dry` exists for everything short of that.

## Step 0 — Preflight (all three gates, in order; any FAIL = stop with the reason)

1. **Right machine:** this skill runs ONLY where the Bloomberg Terminal lives. Gate on the
   DAPI, not on an assumption: `bloomberg_health` (bloomberg MCP) must return `ok: true`
   (`127.0.0.1:8194`). The dependency is `bbcomm`, not the Terminal GUI — the GUI may be
   closed and the pull still works (measured 2026-07-30).
2. **Project root** — resolve under the CURRENT user profile, NEVER hardcode a username
   (this repo runs on multiple machines; the committed-path class has bitten repeatedly):
   ```
   %USERPROFILE%\OneDrive - Opal Capital\Shared - Documents\OCIO Models\Dashboard\202511 Model Portfolio Exposure
   ```
   Must contain `src\market_indices_data_pull.ipynb`, `tools\run_daily_pull.py`, `output\`.
3. **The cma python** (the env the notebooks need — tia, pandas, nbconvert):
   resolve `argv[0]` from `%APPDATA%\jupyter\kernels\cma\kernel.json`; fallback
   `C:\Anaconda\envs\cma\python.exe`; if neither exists, `BBG_CONDA_ENV` names the env.
   Invoking the env's `python.exe` directly is equivalent to the `.bat`'s `conda activate`.
   *(If the pull later dies "kernel python3 not found": `<cma-python> -m ipykernel install
   --user --name cma` — the 2026-07-31 kernel-registration fix.)*

## Step 1 — Pull + tripwire (leg 1)

```
"<cma-python>" "<project>\tools\run_daily_pull.py" [--skip-pull] [--allow-stale N]
```

- The notebooks take **minutes** — run under Bash `run_in_background` and act on the
  completion notification; do not poll.
- Both notebooks are **idempotent by date** (an existing today-PKL is reused), so re-running
  after a hiccup is always safe.
- The runner ends with the tripwire (expected keys, duplicate rows, as-of date, row-count
  bands). **Score on the OUTPUT, not just rc:** proceed ONLY on
  `RESULT: PASS -- both PKLs safe to send`. Any `FAIL:` lines -> **STOP. Never send on a
  tripwire FAIL.** Report the reasons verbatim.

**Banked failure signatures (2026-08-03 incident — recognize, stop, escalate; do not retry-hammer):**
- `responseError ... code -4003 category LIMIT ... "Access pending review [nid:...]"` —
  Bloomberg has the ACCOUNT under a data-consumption review. Terminal-side; retries make it
  worse. Escalate to Andrew/Yang with the nid.
- `ValueError: cannot reindex on an axis with duplicate labels` (or tripwire dup-rows FAIL) —
  the month-end double-append class. The notebook has carried a guard since 2026-08-03 13:08Z;
  dups appearing again mean the guard regressed. Stop; census which (index_name, date) rows
  duplicated; escalate with the census. NEVER "fix" by a naive `.last()` dedup — in
  return_monthly the daily-append row is NaN-heavy and its `return` is a 1-DAY value; a keep-
  last dedup silently destroys monthly fields (record: MDLP_MONPUB_W4 trace doc).
- A wrong-instrument series (custom `.X` ticker resolving to something else — the ST race) is
  now root-fixed (deprecated index deleted 2026-08-03), but the class exists: custom-index
  history that suddenly spans years more than its inception, at a wildly different price
  level, is a RESOLUTION fault, not market data. Stop and escalate; the remap table of
  unambiguous `PARSEKYABLE_DES` forms lives in the trace doc if pinning is ever needed.

## Step 2 — OneDrive sync gap

The upload tool reads the SharePoint copy, server-side. The local `output\` write needs ~a
minute to sync. If Step 3 reports files-not-found for today's date: wait ~60s, retry ONCE,
then stop and report (a sync stall is a finding, not a retry loop).

## Step 3 — Upload through /data-refresh (leg 2)

Gateway tool (requires the authenticated `opal` MCP; if its tools are absent, run the OAuth
flow first — the tool listing shows `opal_data_refresh_upload` when connected):

```
opal_data_refresh_upload(date="<YYYYMMDD if --date>", dry_run=<dry form>, confirm=<True on real send>)
```

Server-side it: finds the two PKLs (`data/model YYYYMMDD v1.pkl`) in the SharePoint output
folder -> uploads through the portal /data-refresh channel -> fires the Yang pipeline ->
watches to completion -> confirms against the LIVE portal manifest. **Read all three
confirmations: uploaded / pipeline / displayed.** Any missing leg = the tool says which; report
it, do not improvise a manual S3 path (the uploads/ + manifest.json trigger contract is the
pipeline owner's surface, not this skill's).

## Step 4 — Independent verify (do not end on the tool's self-report)

1. Served read: `json/benchmarks/model_portfolio_benchmarks.json` on `opal-data-portal-v2` —
   `data_as_of` must equal the **expected last trading day** (TRADING days, never wall-clock:
   Friday's date IS correct on Monday; `lib/trading_calendar.py` is the one frontier
   definition). `generated_at` fresh.
2. Sanity glance at the ST row (informational, not a gate): 1D within ~±1%, model_volatility
   ~2-4. The 2026-08-03 garbage read +2.22/vol 20.79 — that shape means STOP + escalate even
   with three green confirmations.

## Report

```
/terminal-upload <form>
  PREFLIGHT: terminal OK (bbcomm :8194) | cma <path> | project OK
  PULL:      OK in <N>s | SKIPPED (send-only) | FAILED: <verbatim reasons>
  TRIPWIRE:  PASS | FAIL -> STOPPED, nothing sent: <reasons>
  UPLOAD:    uploaded OK / pipeline OK / displayed OK | dry-run -> pending/ only | <failed leg>
  SERVED:    data_as_of <date> == expected frontier <date> | MISMATCH -> <detail>
```

## Discipline

- **Tripwire FAIL = nothing is sent.** No override in this skill; a bad file goes to a human.
- **One-shot.** No loops, no crons, no monitors/alarms built (standing moratorium) — the
  verification steps above run inside this invocation and then the skill is done.
- **Idempotent + safe to re-run** end to end: the pull reuses today's files; a re-upload of the
  same date is monotonicity-safe pipeline-side (the W2 guard rejects backward writes loudly).
- The portal keeps serving the previous day until a clean run lands — a stopped run is safe,
  a forced one is not.
- Sibling skills: `/bbg-daily` (the original two-step human flow this automates; its
  project-side doc is `tools/BBG_DAILY_SKILL.md`), `49-schwab-conv` (different pipeline).
