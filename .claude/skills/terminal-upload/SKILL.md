---
name: terminal-upload
description: One-command daily Bloomberg pipeline from the terminal machine: pull the data/model PKLs through Yang's notebooks (run_daily_pull.py + tripwire), push them through the portal /data-refresh channel, confirm the portal serves the new date. Use on "run the terminal upload", "pull and upload the PKLs", or "send-only" to re-send pulled PKLs. Runs only on the Bloomberg terminal machine.
---

# /terminal-upload — pull the PKLs and upload through data-refresh, no UI

One command replacing the two-step human flow (double-click `run_daily_pull.bat`, then open the
portal DataRefresh UI): **pull -> tripwire -> upload -> pipeline -> confirm served**. Yang's
notebooks are UNTOUCHED — this wraps them, exactly like the `.bat` does. The upload leg is the
gateway's server-side `opal_data_refresh_upload` (the same channel the UI uses): the big files
never pass through the chat, and it returns three confirmations (uploaded / pipeline /
displayed) so nothing half-lands silently.

> **SYNC RULE (two copies exist):** this repo file is CANONICAL. A self-contained duplicate
> lives at the DEVICE HOME level — `%USERPROFILE%\.claude\skills\terminal-upload\SKILL.md` —
> so any Claude session on the terminal machine (no repo checkout, no fabric context) can run
> the process. **Any edit here must be re-copied there** (adapting repo-relative references —
> the home copy carries its context inline). Two copies WILL drift silently otherwise; this
> line is the tripwire.

## Invocation forms

| Form | Behavior |
|---|---|
| `/terminal-upload` | Full run: pull both notebooks + tripwire + REAL upload + verify served. Date variant = `tplus1`. |
| `/terminal-upload tplus1` | Explicit prior-business-day pull. Identical to the bare form. |
| `/terminal-upload tzero` | **Same-day** pull (`date_end = today`). See DATE VARIANT below — read it before the first real send. |
| `/terminal-upload dry` | Pull + tripwire + `dry_run=True` upload (lands in pending/, NO pipeline fire). The safe exercise. |
| `/terminal-upload send-only` | Skip the pull (PKLs already produced today): tripwire only (`--skip-pull`) + upload + verify. |
| `/terminal-upload pull-only` | Pull + tripwire, stop before any upload. |
| `--allow-stale N` | Pass through to the tripwire (post-holiday mornings where as-of is legitimately older). |
| `--date YYYYMMDD` | Send a specific vintage instead of the variant's own (passed to the upload tool). |

The variant word combines with the others: `/terminal-upload tzero dry`,
`/terminal-upload tzero pull-only`, `/terminal-upload tplus1 send-only`.

**Invoking this skill IS the send authorization** — the real upload passes `confirm=True`
because the operator asked for exactly this. `dry` exists for everything short of that.

## DATE VARIANT — which day the pull targets

Both variants live in `integrations/bloomberg/pipeline/<variant>/` (repo-owned copies; Yang's live
notebooks stay untouched). They differ on exactly one line, `date_end`:

| Variant | `date_end` | Vintage on a Tue |
|---|---|---|
| `tplus1` (default) | `today + BDay(-1)` | Monday |
| `tzero` | `today` | Tuesday |

**There is no time-of-day logic in either notebook** — `tplus1` targets `today - 1
business day` whether you fire it at 08:00 or 23:00. It is not "yesterday because today
isn't in yet"; it is a fixed rule, and `tzero` is the only way to reach same-day.

**Two things to know before running `tzero` for real:**

1. **Whether Bloomberg serves a complete same-day bar is UNTESTED.** The tripwire
   verifies the as-of *is* today, but it cannot tell a complete same-day bar from a
   partial one. Until that is measured, treat tzero as an experiment: compare a tzero
   pull against the next morning's tplus1 pull of the same date before letting tzero
   feed the portal. Prefer `tzero dry` first.
2. **tzero leaves a file that tomorrow's tplus1 would reuse.** tzero writes
   `data <today> v1.pkl`; tomorrow tplus1 targets that date and the notebooks are
   idempotent by date. The runner guards this — tplus1 refuses to start on a
   tzero-produced vintage and tells you how to proceed — but do not defeat the guard
   without knowing the tzero run happened after the close.

Because both variants write into the same live `output/` under different filenames,
**always upload with the vintage named explicitly** (`date="<stamp>"`); do not let the
upload tool pick "the latest".

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

Run the **variant's** runner out of the repo — NOT `<project>\tools\run_daily_pull.py`
(that is Yang's own T-1-only copy and has no variant awareness):

```
"<cma-python>" -u "<workspace>\integrations\bloomberg\pipeline\<variant>\tools\run_daily_pull.py" \
    [--skip-pull] [--allow-stale N] [--date YYYYMMDD]
```

`<variant>` is `tplus1` (default) or `tzero`. The runner is byte-identical in both and
reads its variant from the folder it lives in; it prints the resolved variant, date rule,
and target stamp in its first four lines — **check those match what you asked for.**

- It executes the repo's notebook copies via `nbclient` with the kernel cwd set inside
  the LIVE project, so `input/`/`output/` still resolve to the real OneDrive project.
  **Do not "simplify" this back to `jupyter nbconvert`:** nbconvert takes the kernel cwd
  from the notebook file's own directory and **silently ignores**
  `--ExecutePreprocessor.cwd`, so the notebooks would build an empty `input/`+`output/`
  under `workflows/` and write the PKLs where nothing reads them — without failing.
  Measured 2026-08-04; the reasoning is in `integrations/bloomberg/pipeline/README.md`.
- The notebooks take **minutes** — run under Bash `run_in_background` and act on the
  completion notification; do not poll. The `-u` is load-bearing under redirection:
  without it the parent's buffered prints land AFTER the tripwire subprocess output and
  the log reads out of order (found in the 2026-08-03 shakedown).
- **A `BLOCKED:` exit naming a tzero vintage is the cross-variant guard, not a bug.**
  Read it and choose deliberately; do not reflexively pass `--accept-tzero-vintage`.
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
opal_data_refresh_upload(date="<the variant's target stamp>", dry_run=<dry form>, confirm=<True on real send>)
```

**Always name `date` explicitly** — pass the stamp the runner printed in Step 1, never let
the tool pick "the latest". Both variants write into the same live `output/` under
different filenames, so a tzero file sitting beside a tplus1 file makes "latest" ambiguous
in exactly the situation where getting it wrong is invisible.

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
  VARIANT:   tplus1 (today - 1 business day) | tzero (same-day) -> target <YYYYMMDD>
  PREFLIGHT: terminal OK (bbcomm :8194) | cma <path> | project OK
  PULL:      OK in <N>s | SKIPPED (send-only) | BLOCKED (tzero-vintage guard) | FAILED: <verbatim>
  TRIPWIRE:  PASS | FAIL -> STOPPED, nothing sent: <reasons>
  UPLOAD:    uploaded OK / pipeline OK / displayed OK | dry-run -> pending/ only | <failed leg>
  SERVED:    data_as_of <date> == expected <date> | MISMATCH -> <detail>
```

For `tzero`, SERVED will NOT equal the trading-day frontier that Step 4.1 describes — the
frontier is the last *completed* trading day, and tzero deliberately serves the current
one. Compare against the tzero target stamp instead, and say so explicitly in the report
so the difference is never mistaken for the staleness class.

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
