"""Retry bbg's harvest WITHIN A WINDOW, which is the one thing never tried.

WHY THIS EXISTS. Andrew-direct 2026-09-27 answered YES to a paced bbg retry.
Every bbg run to date has made exactly ONE `search/query` request and then
stopped: on a 403 the producer diverts to an interactive press-and-hold it
cannot solve, job 1 comes back `request_rejected`, and that cools the PUBLISHER
so the remaining jobs of the same invocation never attempt. Two runs on 09-26
(20:32 and 22:26) were both single-shot, 114 minutes apart.

THE MEASUREMENT THAT MAKES A RETRY THE RIGHT ACT, from the producer's own
`events.jsonl` (67 bbg http events): status 200 sixty times, 403 SEVEN times --
a ~10% refusal rate on an endpoint that mostly serves. And it ALTERNATES on a
short clock: 403 03:31 -> 200 03:44 (13 min), 403 03:47 -> 200 03:55 (8 min),
403 04:40 -> 200 04:41 (SEVENTY SECONDS), all 2026-09-15, then eleven
consecutive 200s. So the bound that guarantees failure is the NO-RETRY bound,
and it is ours, not the vendor's.

WHAT IT DOES NOT DO. It makes no request of its own -- every vendor byte comes
from the existing scripted producer, unchanged, which is the MECHANISM bound on
the vendor word. It does not re-authenticate (the producer's verification limb
runs with `credentials_entered: false`; a bot check is not a sign-in). It does
not widen the job bound: `--max-jobs` stays at 8, the bound already exercised.
It does not treat the producer's rc as the answer -- the verdict is read from
`events.jsonl`, the instrument the consumer reads.

STOP CONDITIONS, all printed:
  1. a search/query 200 appears for bbg          -> CLEARED (the point of the run)
  2. --max-attempts reached with every try 403   -> NOT CLEARED in this window
  3. the producer writes no new http event       -> BLIND, stop rather than guess

Run: python drive_bbg_retry.py [--max-attempts N] [--gap S] [--max-jobs N]
"""

import argparse
import io
import json
import pathlib
import sqlite3
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]            # bbg_retry_20260927 -> AMGT_HARVST, deliverables,
                                  # 2.0.0_SA_COO, tier1_exec, org, WORKSPACE
EVENTS = ROOT / ".runtime/opal-data-harvest/events.jsonl"
RUNTIME = ROOT / ".runtime/opal-data-harvest"
PROGRESS = ROOT / ".runtime/opal-data-harvest/progress.sqlite3"
SEARCH_PATH = "/nemo-next/api/search/query"


def cooldown_remaining(publisher="bbg"):
    """Seconds until OUR OWN publisher cooldown lifts. Negative = clear.

    THIS IS THE BINDING CONSTRAINT, NOT THE VENDOR'S RECOVERY WINDOW, AND THE
    FIRST VERSION OF THIS DRIVER PACED AGAINST THE WRONG ONE. Measured
    2026-09-27: attempt 1 took a 403 and `worker.py:310` wrote a 900s cooldown
    (`request_rejected_without_verified_auth_expiry`) into progress.sqlite3;
    attempt 2 fired 300s later, and EVERY job returned `cooldown` in under one
    second with NO session load and NO http event -- it never reached the vendor
    at all. A retry inside the cooldown is not a retry, it is a no-op that looks
    like a second refusal. The cooldown OUTLIVES the process that set it, so a
    fresh invocation does not clear it.

    So the gap is read from the table rather than guessed, and 900s comfortably
    exceeds the vendor recovery range measured on 09-15 (70s to 13 min).
    """
    if not PROGRESS.exists():
        return None
    try:
        con = sqlite3.connect(str(PROGRESS))
        row = con.execute("SELECT until FROM cooldown WHERE publisher=?",
                          (publisher,)).fetchone()
        con.close()
    except sqlite3.Error:
        return None
    if not row:
        return -1.0
    return row[0] - time.time()


def bbg_http_events():
    """Every bbg http event the producer has logged. The CONSUMER's instrument."""
    if not EVENTS.exists():
        return []
    out = []
    for line in io.open(EVENTS, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        try:
            d = json.loads(line)
        except ValueError:
            continue
        if d.get("publisher") == "bbg" and d.get("event") == "http":
            out.append(d)
    return out


def search_events(rows):
    return [d for d in rows if d.get("path") == SEARCH_PATH]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-attempts", type=int, default=8)
    ap.add_argument("--gap", type=int, default=0,
                    help="EXTRA seconds between attempts ON TOP of waiting out our own "
                         "cooldown; 0 is right, because the 900s cooldown already exceeds "
                         "the measured vendor recovery range (70s-13min)")
    ap.add_argument("--cooldown-margin", type=int, default=20,
                    help="seconds added after the cooldown's `until` before firing")
    ap.add_argument("--max-jobs", type=int, default=8,
                    help="unchanged from the bound already exercised; this driver does not widen it")
    args = ap.parse_args()

    baseline = len(search_events(bbg_http_events()))
    print("BASELINE: %d bbg search/query event(s) already logged" % baseline, flush=True)

    cleared = False
    log = []
    for i in range(1, args.max_attempts + 1):
        # WAIT OUT OUR OWN COOLDOWN FIRST. Firing inside it reaches no vendor and
        # produces a false second refusal -- measured, see cooldown_remaining().
        rem = cooldown_remaining("bbg")
        if rem is None:
            print("  WARN: cannot read the cooldown table at %s -- proceeding, but a "
                  "`cooldown` result this attempt means the wait was not observed." % PROGRESS,
                  flush=True)
        elif rem > 0:
            wait = int(rem) + args.cooldown_margin
            print("  our own bbg cooldown has %ds left; sleeping %ds (+%ds margin) so this "
                  "attempt can actually reach the vendor" % (int(rem), wait, args.cooldown_margin),
                  flush=True)
            time.sleep(wait)
        else:
            print("  our own bbg cooldown is CLEAR (%ds past)" % int(-rem), flush=True)

        cmd = [sys.executable, "-m", "lib.opal_data_harvest", "run",
               "--publishers", "bbg",
               "--harvest-grammar",
               "--runtime-root", str(RUNTIME),
               "--all-securities",
               "--max-jobs", str(args.max_jobs)]
        print("=== ATTEMPT %d of %d ===" % (i, args.max_attempts), flush=True)
        started = time.time()
        proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT))
        text = (proc.stdout or "") + "\n" + (proc.stderr or "")
        (HERE / ("attempt%d.log" % i)).write_text(text, encoding="utf-8", newline="\n")

        # THE VERDICT COMES FROM THE PRODUCER'S EVENT LOG, NOT FROM rc AND NOT FROM
        # run.log -- run.log carries job-level events ONLY and cannot show an http
        # status, so a 403 read there is INVISIBLE. Measured 2026-09-27: run.log and
        # run2.log contain the string "403" ZERO times for runs that both got one.
        new = search_events(bbg_http_events())[baseline:]
        statuses = [d.get("status") for d in new]
        print("  rc=%s elapsed=%ds  NEW search/query event(s): %d  statuses=%s"
              % (proc.returncode, int(time.time() - started), len(new), statuses), flush=True)
        log.append({"attempt": i, "rc": proc.returncode,
                    "elapsed_s": int(time.time() - started),
                    "new_search_events": len(new), "statuses": statuses,
                    "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})

        if not new:
            print("  BLIND: the producer logged no new search/query event this attempt. "
                  "Stopping rather than retrying against an instrument that cannot see.", flush=True)
            break

        if 200 in statuses:
            print("  CLEARED: search/query returned 200 on attempt %d. The no-retry bound WAS the blocker."
                  % i, flush=True)
            cleared = True
            baseline = len(search_events(bbg_http_events()))
            break

        baseline = len(search_events(bbg_http_events()))
        if i < args.max_attempts:
            print("  gap: sleeping %ds before the next attempt (the recovery window)" % args.gap, flush=True)
            time.sleep(args.gap)
    else:
        print("NOT CLEARED: %d attempt(s), every one refused. The window read here does NOT decay."
              % args.max_attempts, flush=True)

    (HERE / "attempts.json").write_text(
        json.dumps({"cleared": cleared, "attempts": log,
                    "gap_s": args.gap, "max_jobs": args.max_jobs}, indent=1),
        encoding="utf-8", newline="\n")
    print("CLEARED=%s  attempts=%d" % (cleared, len(log)), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
