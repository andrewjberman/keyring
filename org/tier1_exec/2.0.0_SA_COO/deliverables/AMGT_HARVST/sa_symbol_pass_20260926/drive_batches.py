"""Drive sa_symbol_resolve_pass.py in PACED batches until every name is ASKED.

WHY A DRIVER AND NOT REPEATED HAND RUNS. The endpoint's 403 is intermittent and
burst-sensitive (measured 2026-09-14, re-measured 2026-09-26): batch 1 took 54
calls clean, batch 2 hit 13 search-refusals and its stop guard fired. The scarce
resource is RATE-LIMIT HEADROOM, so the thing that makes progress is the GAP
BETWEEN batches, not more calls inside one.

WHAT IT DOES NOT DO: it does not touch the producer, does not retry a refused
name inside a batch (the producer's own stop guard owns that), and does not
widen --limit when a batch goes clean. It chains --exclude-done from each batch's
output to the next, which is the producer's own resume limb.

STOP CONDITIONS, all three printed:
  1. every name in the universe is ASKED           -> DONE
  2. two consecutive batches add ZERO newly-asked  -> STALLED, the block is not decaying
  3. the batch cap is reached                      -> CAP

Run: python drive_batches.py [--max-batches N] [--limit N] [--sleep S] [--gap G]
"""

import argparse
import pathlib
import re
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]   # .../sa_symbol_pass_20260926 -> AMGT_HARVST, deliverables,
                         # 2.0.0_SA_COO, tier1_exec, org, WORKSPACE. parents[4] is `org/`
                         # and yields org/org/... -- measured, batch 3 died on it.
PRODUCER = ROOT / "org/tier1_exec/4.0.0_SA_CRO/scripts/sa_symbol_resolve_pass.py"

SUMMARY = re.compile(
    r"POPULATION\s+(?P<pop>\d+) carried \+ (?P<batch>\d+) this batch = (?P<total>\d+) record"
)
ASKED = re.compile(r"ASKED\s+(?P<asked>\d+) of (?P<of>\d+)")
RESOLVED = re.compile(r"RESOLVED\s+(?P<n>\d+) of (?P<of>\d+)")
NOTASKED = re.compile(r"NOT ASKED\s+(?P<search>\d+) search-refused \+ (?P<news>\d+) news-refused")
NEVER = re.compile(r"NEVER REACHED\s+(?P<n>\d+)")
SERVE = re.compile(r"SERVEABLE\s+(?P<n>\d+) of (?P<of>\d+)")


def read_summary(text):
    out = {}
    for rx, keys in ((SUMMARY, ("pop", "batch", "total")), (ASKED, ("asked", "of")),
                     (RESOLVED, ("n", "of")), (NOTASKED, ("search", "news")),
                     (NEVER, ("n",)), (SERVE, ("n", "of"))):
        m = rx.search(text)
        if not m:
            continue
        for k in keys:
            out.setdefault(rx.pattern.split("\\")[0].strip() + ":" + k, m.group(k))
    a = ASKED.search(text)
    r = RESOLVED.search(text)
    na = NOTASKED.search(text)
    nv = NEVER.search(text)
    sv = SERVE.search(text)
    return {
        "asked": int(a.group("asked")) if a else None,
        "universe": int(a.group("of")) if a else None,
        "resolved": int(r.group("n")) if r else None,
        "search_refused": int(na.group("search")) if na else None,
        "never_reached": int(nv.group("n")) if nv else None,
        "serveable": int(sv.group("n")) if sv else None,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start-from", default=str(HERE / "batch2.json"))
    ap.add_argument("--first-index", type=int, default=3)
    ap.add_argument("--max-batches", type=int, default=12)
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--sleep", type=float, default=20)
    ap.add_argument("--gap", type=int, default=600,
                    help="seconds BETWEEN batches -- the decay window, the whole point")
    args = ap.parse_args()

    prev = pathlib.Path(args.start_from)
    if not prev.exists():
        print("FATAL: --start-from does not exist: %s" % prev)
        return 2

    zero_streak = 0
    last_resolved = None
    for i in range(args.first_index, args.first_index + args.max_batches):
        out = HERE / ("batch%d.json" % i)
        log = HERE / ("batch%d.log" % i)
        cmd = [sys.executable, str(PRODUCER),
               "--exclude-done", str(prev),
               "--limit", str(args.limit),
               "--sleep", str(args.sleep),
               "--out", str(out)]
        print("=== BATCH %d  exclude-done=%s ===" % (i, prev.name), flush=True)
        started = time.time()
        proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT))
        text = (proc.stdout or "") + "\n" + (proc.stderr or "")
        log.write_text(text, encoding="utf-8", newline="\n")
        s = read_summary(text)
        print("  rc=%s elapsed=%ds  asked=%s of %s  resolved=%s  search_refused=%s  never_reached=%s  serveable=%s"
              % (proc.returncode, int(time.time() - started), s["asked"], s["universe"],
                 s["resolved"], s["search_refused"], s["never_reached"], s["serveable"]), flush=True)

        if not out.exists():
            print("  STOP: batch %d wrote no output -- nothing to chain. Keeping %s as the last good population."
                  % (i, prev.name), flush=True)
            break

        if s["asked"] is not None and s["universe"] is not None and s["asked"] >= s["universe"]:
            print("  DONE: every name in the universe is ASKED (%s of %s)." % (s["asked"], s["universe"]), flush=True)
            prev = out
            break

        # GAIN IS MEASURED ON `resolved`, NOT ON `asked`. Measured 2026-09-27: after the
        # resume-predicate fix (@9fe22c1eea) deliberately shrank the CARRIED set, `asked` and the
        # population both FELL (69 -> 59 of 89 -> 83) while `resolved` held at 56. Nothing had
        # regressed -- `asked` is simply not monotonic across a predicate change, and a -10 read
        # as a non-positive "gain" would have tripped the two-strikes STALL rule and stopped the
        # run for a reason that was not a stall. `resolved` only ever rises.
        gained = None if last_resolved is None or s["resolved"] is None else s["resolved"] - last_resolved
        if gained is not None:
            print("  newly RESOLVED this batch: %d  (asked=%s of %s -- both non-monotonic by design)"
                  % (gained, s["asked"], s["universe"]), flush=True)
            if gained <= 0:
                zero_streak += 1
                if zero_streak >= 2:
                    print("  STALLED: two consecutive batches RESOLVED nothing new. "
                          "The block is not decaying on this cadence -- stopping rather than re-extending it.",
                          flush=True)
                    prev = out
                    break
            else:
                zero_streak = 0
        last_resolved = s["resolved"]
        prev = out

        print("  gap: sleeping %ds before the next batch (the decay window)" % args.gap, flush=True)
        time.sleep(args.gap)
    else:
        print("CAP: reached --max-batches without finishing.", flush=True)

    print("LAST GOOD POPULATION: %s" % prev, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
