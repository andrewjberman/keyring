#!/usr/bin/env python3
"""LOCAL STEP-RUNNER for the estate-report / Kimi pipeline.

Runs every DETERMINISTIC stage of estate_report_runner.py against the LOCAL repo, dumping each
stage's output to its own file so the operator can read them call by call.

WHAT IT DOES NOT DO, DELIBERATELY:
  * no S3 WRITES (write_manifest / put_object are never called -- main() and run_report() are
    not invoked; this harness calls the stage functions directly)
  * no vendor egress -- it STOPS at the built prompt. call_kimi is never reached.
  * no clone -- it points the stages at the local working repo instead of a fresh clone. The
    DIFFERENCE THIS INTRODUCES IS PRINTED, not hidden (local CLOUD may be ahead of origin/CLOUD,
    so the commit window can differ from what EC2 would see).

Usage:  python kimi_steps.py [--date YYYY-MM-DD] [--outdir DIR]
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

REPO = r"C:\Users\AndrewBerman\Desktop\ajb_workspace"
RUNNER_DIR = os.path.join(REPO, "infra", "aws", "ec2", "estate-report-runner")

# The module reads these at IMPORT time (os.environ[...] at :55-57). Stubbed so the import
# succeeds; none of them is used on any path this harness executes.
os.environ.setdefault("ESTATE_KIMI_SECRET_ID", "LOCAL-HARNESS-UNUSED")
os.environ.setdefault("ESTATE_KIMI_URL", "http://local.harness.invalid/UNUSED")
os.environ.setdefault("ESTATE_KIMI_MODEL", "LOCAL-HARNESS-UNUSED")
os.environ.setdefault("ESTATE_GITHUB_SECRET_ID", "LOCAL-HARNESS-UNUSED")
os.environ.setdefault("ESTATE_REPORT_BUCKET", "LOCAL-HARNESS-UNUSED")
os.environ.setdefault("ESTATE_REPO_URL", "https://local.harness.invalid/UNUSED.git")

sys.path.insert(0, RUNNER_DIR)


def hr(n, title):
    line = "=" * 78
    print("\n%s\nSTEP %s -- %s\n%s" % (line, n, title, line))


def dump(outdir, name, obj, as_text=False):
    p = os.path.join(outdir, name)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(obj if as_text else json.dumps(obj, indent=2, default=str))
    print("  -> wrote %s (%d bytes)" % (p, os.path.getsize(p)))
    return p


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="report date YYYY-MM-DD (default: today's scheduled window)")
    ap.add_argument("--outdir", default=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                     "kimi_steps_out"))
    args = ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)

    import estate_report_runner as R

    # ---------------------------------------------------------------- STEP 0: divergence control
    hr(0, "LOCAL vs EC2 divergence -- what this harness sees that the real run would not")
    def git(*a):
        return subprocess.run(["git", "-C", REPO] + list(a), capture_output=True,
                              text=True).stdout.strip()
    local_head = git("rev-parse", "CLOUD")
    origin_head = git("rev-parse", "origin/CLOUD")
    ahead = git("rev-list", "--count", "origin/CLOUD..CLOUD")
    print("  local  CLOUD : %s" % local_head)
    print("  origin CLOUD : %s" % origin_head)
    print("  local is %s commit(s) AHEAD of origin." % ahead)
    if ahead not in ("", "0"):
        print("  >> The EC2 runner clones origin. Those %s commit(s) are INVISIBLE to a real fire" % ahead)
        print("     and VISIBLE here. Any count below can differ from production by exactly them.")
    else:
        print("  >> No divergence. Local and origin agree; counts below are production-equivalent.")

    # ---------------------------------------------------------------- STEP 1: window
    hr(1, "resolve_window() -- the report window (scheduled marks, NOT process wall-time)")
    now_utc = datetime.now(timezone.utc)
    start_local, end_local = R.resolve_window(now_utc)
    report_date = args.date or end_local.strftime("%Y-%m-%d")
    window_desc = "%s (%s) -> %s (%s)" % (
        start_local.strftime("%Y-%m-%d %H:%M %Z"),
        start_local.astimezone(timezone.utc).strftime("%H:%MZ"),
        end_local.strftime("%Y-%m-%d %H:%M %Z"),
        end_local.astimezone(timezone.utc).strftime("%H:%MZ"))
    print("  now_utc      : %s" % now_utc.isoformat())
    print("  window       : %s" % window_desc)
    print("  report_date  : %s" % report_date)

    # ---------------------------------------------------------------- STEP 2: commits
    hr(2, "commits_in_window() -- the git half's raw input")
    commits = R.commits_in_window(REPO, start_local, end_local)
    print("  commits in window: %d" % len(commits))
    authors = {}
    for c in commits:
        authors[c.get("author", "?")] = authors.get(c.get("author", "?"), 0) + 1
    for a, n in sorted(authors.items(), key=lambda kv: -kv[1]):
        print("    %4d  %s" % (n, a))
    dump(args.outdir, "02_commits.json", commits)

    # ---------------------------------------------------------------- STEP 3: corpus
    hr(3, "capture_census() -- PART 1 of the prompt, the PRIMARY evidence (rulings/operator input)")
    nuggets, corpus_coverage = R.capture_census(REPO, start_local, end_local)
    print("  nuggets total    : %d" % len(nuggets))
    print("  by_provenance    : %s" % corpus_coverage.get("by_provenance"))
    print("  degraded_sources : %s" % corpus_coverage.get("degraded_sources"))
    print("  FRESHNESS        : %s" % corpus_coverage.get("corpus_freshness"))
    dump(args.outdir, "03_corpus_nuggets.json", nuggets)
    dump(args.outdir, "03_corpus_coverage.json", corpus_coverage)

    # ---------------------------------------------------------------- STEP 4: attribution
    hr(4, "load_attribution_maps() + compile_changed_resources() -- PART 2, the resource axis")
    maps = R.load_attribution_maps(REPO)
    resources, coverage = R.compile_changed_resources(commits, maps)
    print("  buckets          : %d" % len(resources))
    print("  changed paths    : %d" % coverage["changed_paths_total"])
    print("    chain_resolved : %d" % coverage["chain_resolved"])
    print("    area_bucketed  : %d" % coverage["area_bucketed"])
    print("    unresolved     : %d" % coverage["unresolved"])
    print("\n  RESOURCE AXIS, largest first (CTO~B's 6a20a5d42 finding: ~2/3 are NOT resources):")
    for name, body in sorted(resources.items(),
                             key=lambda kv: -len(kv[1].get("paths", [])))[:15]:
        print("    %5d  %s" % (len(body.get("paths", [])), name))
    dump(args.outdir, "04_resources.json", resources)
    dump(args.outdir, "04_attribution_coverage.json", coverage)

    # ---------------------------------------------------------------- STEP 5: budgets
    hr(5, "PROMPT BUDGETS -- how much of each half actually reaches the model")
    corpus_text, c_shown, c_total = R._render_corpus(nuggets, corpus_coverage, R.CORPUS_PROMPT_BUDGET)
    res_text, r_shown, r_total, p_total = R._summarize_resources(resources, R.RESOURCES_SUMMARY_BUDGET)
    print("  CORPUS_PROMPT_BUDGET     : %d chars" % R.CORPUS_PROMPT_BUDGET)
    print("    rendered              : %d chars" % len(corpus_text))
    print("    nuggets SHOWN         : %d of %d   <<< anything omitted here the model NEVER SEES"
          % (c_shown, c_total))
    print("  RESOURCES_SUMMARY_BUDGET : %d chars" % R.RESOURCES_SUMMARY_BUDGET)
    print("    rendered              : %d chars" % len(res_text))
    print("    resources SHOWN       : %d of %d (covering %d paths)" % (r_shown, r_total, p_total))
    dump(args.outdir, "05_corpus_rendered.txt", corpus_text, as_text=True)
    dump(args.outdir, "05_resources_rendered.txt", res_text, as_text=True)

    # ---------------------------------------------------------------- STEP 6: the prompt
    hr(6, "build_prompt() -- THE EXACT BYTES THAT WOULD GO TO THE MODEL")
    prompt = R.build_prompt(resources, window_desc, nuggets, corpus_coverage)
    est_tokens = len(prompt) // 4
    print("  prompt chars       : %d" % len(prompt))
    print("  est. prompt tokens : ~%d  (chars/4)" % est_tokens)
    print("  KIMI_MAX_TOKENS    : %d   (CEILING on output, incl. reasoning -- not a target)"
          % R.KIMI_MAX_TOKENS)
    print("  KIMI_TIMEOUT_SECONDS: %d  x %d attempt(s)" % (R.KIMI_TIMEOUT_SECONDS, R.KIMI_ATTEMPTS))
    print("  allowed PROSE_FIELDS: %s" % sorted(R.PROSE_FIELDS))
    dump(args.outdir, "06_PROMPT.txt", prompt, as_text=True)

    # ---------------------------------------------------------------- STEP 7: the boundary
    hr(7, "call_kimi() -- NOT RUN")
    print("  VENDOR EGRESS (Moonshot). Requires Andrew's explicit per-use word.")
    print("  Everything above this line is local and free. Nothing was sent anywhere.")
    print("  Nothing was written to S3: write_manifest() and put_object() were never called.")

    print("\n%s\nALL STAGE OUTPUTS: %s\n%s" % ("=" * 78, args.outdir, "=" * 78))
    return 0


if __name__ == "__main__":
    sys.exit(main())
