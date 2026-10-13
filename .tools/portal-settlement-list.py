#!/usr/bin/env python3
"""Write the portal settlement list Andrew rules from (NFRA_DEVPLN cell DP-s-1).

Read-only. Every git call is a read, run as ``git -C <portal> ...``: no fetch, no push, no write to the
portal repo. Standard library only. The file written, and stdout, end with the machine line:

    SETTLEMENT-LIST dev_ahead=<n> prod_ahead=<m> groups=<g> files_total=<t> files_other=<o> branches=<b>

Usage:
    python .tools/portal-settlement-list.py [--portal portal] [--out <file>]
    python .tools/portal-settlement-list.py --selftest
"""

import argparse
import collections
import datetime
import os
import shutil
import stat
import subprocess
import sys
import tempfile

DEFAULT_PORTAL = "portal"
DEFAULT_OUT = "org/missions/D0/NFRA/NFRA_DEVPLN/ledger/SETTLEMENT_LIST.md"
DEV = "origin/DEV"
PROD = "origin/PROD"
REMOTE_PREFIX = "refs/remotes/origin/"
SKIP_BRANCHES = ("DEV", "PROD", "HEAD")
CHUNK = 40  # pathspecs per git call, keeps every command line far below the Windows limit

# Group table, prefixes measured against origin/DEV at the cell run: all six exist in the repo as written,
# so no correction was needed. First match wins; a file matching none of them lands in "other".
# The class column is the unsure rule: an INPUT, not a measurement.
GROUPS = (
    ("InvestorReporting", "src/pages/InvestorReporting", "client-facing"),
    ("SecurityAnalysis", "src/pages/SecurityAnalysis", "opal-internal"),
    ("TicketCenter", "src/pages/TicketCenter", "client-facing"),
    ("AdvisorIntelligence", "src/pages/AdvisorIntelligence", "client-facing"),
    ("api", "src/api/endpoints", "client-facing"),
    ("firmAccess", "src/lib/firmAccess.ts", "client-facing"),
)
OTHER = "other"
OTHER_CLASS = "client-facing"


def ascii_text(value):
    """Force ASCII: a non-ASCII character becomes a backslash escape."""
    return value.encode("ascii", "backslashreplace").decode("ascii")


def md_cell(value):
    return ascii_text(value).replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def git(repo, *args):
    """One read-only git call; returns stdout text. Raises RuntimeError on a nonzero rc."""
    env = dict(os.environ)
    env["GIT_LITERAL_PATHSPECS"] = "1"
    env["GIT_PAGER"] = "cat"
    proc = subprocess.run(["git", "-C", repo] + list(args), capture_output=True, env=env)
    if proc.returncode != 0:
        err = proc.stderr.decode("utf-8", "replace").strip()
        raise RuntimeError("git %s rc=%d %s" % (" ".join(args), proc.returncode, err))
    return proc.stdout.decode("utf-8", "replace")


def count(repo, rng):
    return int(git(repo, "rev-list", "--count", rng).strip())


def prefix_hit(path, prefix):
    return path == prefix or path.startswith(prefix + "/")


def group_of(path):
    for name, prefix, _cls in GROUPS:
        if prefix_hit(path, prefix):
            return name
    return OTHER


def changed_files(repo):
    """Files changed on DEV since the merge base with PROD (three-dot range), NUL-separated, unquoted."""
    text = git(repo, "diff", "--name-only", "-z", PROD + "..." + DEV)
    return [name for name in text.split("\0") if name]


def commits_touching(repo, rng, paths):
    """Commits in rng touching any of paths, as {sha: author}. Chunked; empty paths gives an empty result."""
    found = {}
    for i in range(0, len(paths), CHUNK):
        args = ["log", "--format=%H%x1f%an", rng, "--"] + paths[i:i + CHUNK]
        for line in git(repo, *args).splitlines():
            if "\x1f" in line:
                sha, author = line.split("\x1f", 1)
                found[sha] = author
    return found


def top_committers(found, n=3):
    counts = collections.Counter(ascii_text(author) for author in found.values())
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:n]


def cherry_signs(repo, upstream, head):
    """git cherry: {sha: '+' or '-'}; '-' means the same patch already sits upstream. Merges are omitted by git."""
    signs = {}
    for line in git(repo, "cherry", upstream, head).splitlines():
        parts = line.split()
        if len(parts) == 2 and parts[0] in ("+", "-"):
            signs[parts[1]] = parts[0]
    return signs


def prod_only_rows(repo):
    signs = cherry_signs(repo, DEV, PROD)
    rows = []
    text = git(repo, "log", "--date=iso-strict", "--format=%H%x1f%an%x1f%ad%x1f%s", DEV + ".." + PROD)
    for line in text.splitlines():
        if line.count("\x1f") != 3:
            continue
        sha, author, date, subject = line.split("\x1f")
        rows.append({"sha": sha, "author": author, "date": date, "subject": subject, "sign": signs.get(sha)})
    return rows


def branch_rows(repo):
    rows = []
    for ref in git(repo, "for-each-ref", "--format=%(refname)", "refs/remotes/origin").splitlines():
        ref = ref.strip()
        if not ref.startswith(REMOTE_PREFIX):
            continue
        name = ref[len(REMOTE_PREFIX):]
        if name in SKIP_BRANCHES:
            continue
        ahead = count(repo, DEV + ".." + ref)
        if ahead <= 0:
            continue
        signs = cherry_signs(repo, DEV, ref)
        plus = sum(1 for sign in signs.values() if sign == "+")
        minus = sum(1 for sign in signs.values() if sign == "-")
        tip = git(repo, "log", "-1", "--date=iso-strict", "--format=%H%x1f%an%x1f%ad", ref).rstrip("\n")
        tip_sha, tip_author, tip_date = tip.split("\x1f")
        rows.append({
            "name": name,
            "ahead": ahead,
            "plus": plus,
            "minus": minus,
            "merges": ahead - plus - minus,
            "tip": tip_sha,
            "date": tip_date,
            "owner": tip_author,
        })
    rows.sort(key=lambda row: (-row["ahead"], row["name"]))
    return rows


def build(repo):
    """Measure everything from git. Read-only."""
    rng = PROD + ".." + DEV
    files = changed_files(repo)
    by_group = collections.OrderedDict((name, []) for name, _prefix, _cls in GROUPS)
    by_group[OTHER] = []
    for path in files:
        by_group[group_of(path)].append(path)
    groups = []
    for name, prefix, cls in GROUPS:
        found = commits_touching(repo, rng, [prefix])
        groups.append({"name": name, "class": cls, "files": len(by_group[name]),
                       "commits": len(found), "top": top_committers(found)})
    other_found = commits_touching(repo, rng, by_group[OTHER])
    groups.append({"name": OTHER, "class": OTHER_CLASS, "files": len(by_group[OTHER]),
                   "commits": len(other_found), "top": top_committers(other_found)})
    branches = branch_rows(repo)
    return {
        "now": utc_now(),
        "dev_short": git(repo, "rev-parse", "--short", DEV).strip(),
        "prod_short": git(repo, "rev-parse", "--short", PROD).strip(),
        "dev_ahead": count(repo, PROD + ".." + DEV),
        "prod_ahead": count(repo, DEV + ".." + PROD),
        "files_total": len(files),
        "files_other": len(by_group[OTHER]),
        "groups": groups,
        "groups_named": sum(1 for g in groups if g["name"] != OTHER and g["files"] > 0),
        "prod_rows": prod_only_rows(repo),
        "branches": branches,
    }


def render(data):
    """Return (text, machine_line). The machine line is the last line of text."""
    out = []
    add = out.append
    machine = ("SETTLEMENT-LIST dev_ahead=%d prod_ahead=%d groups=%d files_total=%d files_other=%d branches=%d"
               % (data["dev_ahead"], data["prod_ahead"], data["groups_named"], data["files_total"],
                  data["files_other"], len(data["branches"])))
    add("# NFRA_DEVPLN -- portal settlement list (cell DP-s-1)")
    add("")
    add("- Measured refs (read-only, no fetch): origin/DEV `%s`, origin/PROD `%s`, written %s (UTC)."
        % (data["dev_short"], data["prod_short"], data["now"]))
    add("- Tool: `.tools/portal-settlement-list.py` on the portal repo `portal/`. Every git call is a read.")
    add("- Headline: DEV is ahead of PROD by %d commits; PROD is ahead of DEV by %d commits; %d files differ "
        "DEV-not-PROD; %d remote branches hold work not on DEV."
        % (data["dev_ahead"], data["prod_ahead"], data["files_total"], len(data["branches"])))
    add("- The class column is the unsure rule (an input). Andrew rules each group once: approve forward, "
        "hold on a branch, or drop.")
    add("")
    add("## 1. DEV-not-PROD groups (git diff --name-only origin/PROD...origin/DEV)")
    add("")
    add("| group | class | files changed | commits touching (origin/PROD..origin/DEV) | top three committers (commits) |")
    add("|---|---|---|---|---|")
    for g in data["groups"]:
        top = "; ".join("%s (%d)" % (md_cell(author), n) for author, n in g["top"]) or "none"
        add("| %s | %s | %d | %d | %s |" % (g["name"], g["class"], g["files"], g["commits"], top))
    add("")
    add("## 2. PROD-only commits (git rev-list origin/DEV..origin/PROD): %d" % len(data["prod_rows"]))
    add("")
    add("| # | sha | author | date | subject | same patch on DEV (git cherry) |")
    add("|---|---|---|---|---|---|")
    for index, row in enumerate(data["prod_rows"], 1):
        if row["sign"] == "-":
            same = "yes (DEV carries the same patch)"
        elif row["sign"] == "+":
            same = "no (patch not on DEV)"
        else:
            same = "n/a (merge commit; git cherry omits merges)"
        add("| %d | %s | %s | %s | %s | %s |" % (index, row["sha"][:8], md_cell(row["author"]),
                                                 md_cell(row["date"]), md_cell(row["subject"]), same))
    add("")
    add("## 3. Remote branches with work not on DEV (ahead of origin/DEV; excludes DEV, PROD, HEAD): %d"
        % len(data["branches"]))
    add("")
    add("| branch | ahead | cherry + (patch not on DEV) | cherry - (already on DEV) | merge commits (cherry omits) "
        "| tip sha | tip date | owner (tip author) |")
    add("|---|---|---|---|---|---|---|---|")
    for b in data["branches"]:
        add("| %s | %d | %d | %d | %d | %s | %s | %s |" % (md_cell(b["name"]), b["ahead"], b["plus"], b["minus"],
                                                         b["merges"], b["tip"][:8], md_cell(b["date"]),
                                                         md_cell(b["owner"])))
    add("")
    add("## 4. Machine lines")
    add("")
    add("```text")
    for g in data["groups"]:
        add("group %s class=%s files=%d commits=%d" % (g["name"], g["class"], g["files"], g["commits"]))
    add("```")
    add("")
    add(machine)
    return ascii_text("\n".join(out) + "\n"), machine


def write_text(path, text):
    folder = os.path.dirname(os.path.abspath(path))
    os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="ascii", newline="\n") as handle:
        handle.write(text)


# ----------------------------------------------------------------------------------------------
# Self-test: a fixture repository with known counts. Refs are created under refs/remotes/origin
# directly, so nothing is fetched and no remote exists.
# ----------------------------------------------------------------------------------------------

def _fixture(root):
    def run(who, *args):
        cmd = ["git", "-C", root, "-c", "user.name=" + who, "-c", "user.email=%s@example.invalid" % who,
               "-c", "commit.gpgsign=false"] + list(args)
        return subprocess.run(cmd, capture_output=True, check=True).stdout.decode("utf-8", "replace").strip()

    def put(rel, body):
        path = os.path.join(root, *rel.split("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="ascii", newline="\n") as handle:
            handle.write(body)

    msg_path = os.path.join(os.path.dirname(root), "msg.txt")

    def commit(who, subject):
        with open(msg_path, "w", encoding="ascii", newline="\n") as handle:
            handle.write(subject + "\n")
        run(who, "add", "-A")
        run(who, "commit", "-q", "-F", msg_path)
        return run("fixture", "rev-parse", "HEAD")

    run("fixture", "init", "-q", "-b", "base")
    put("src/pages/InvestorReporting/a.tsx", "base a\n")
    put("src/api/endpoints/keep.ts", "base keep\n")
    put("src/pages/TicketCenter/t.tsx", "base t\n")
    base = commit("carol", "base")
    # DEV: D1 touches two investor-reporting files (1 commit, 2 files); D2 touches security + api;
    # D3 touches firmAccess and a root file that matches no prefix.
    run("fixture", "checkout", "-q", "-b", "fx-dev", base)
    put("src/pages/InvestorReporting/a.tsx", "dev a\n")
    put("src/pages/InvestorReporting/b.tsx", "dev b\n")
    commit("alice", "D1 investor reporting")
    put("src/pages/SecurityAnalysis/s.tsx", "dev s\n")
    put("src/api/endpoints/keep.ts", "dev keep\n")
    dev_d2 = commit("bob", "D2 security analysis and api")
    put("src/lib/firmAccess.ts", "dev access\n")
    put("README.md", "dev readme\n")
    dev = commit("alice", "D3 firm access and readme")
    # PROD: P1 carries the same patch as D2 (a '-' in cherry); P2 is PROD-only (a '+').
    run("fixture", "checkout", "-q", "-b", "fx-prod", base)
    run("carol", "cherry-pick", dev_d2)
    p1 = run("fixture", "rev-parse", "HEAD")
    put("src/pages/TicketCenter/t.tsx", "prod t\n")
    prod = commit("carol", "P2 ticket center")
    # Branch feat-x: F1 not on DEV ('+'), F2 is D2's patch ('-'). Branch q/x/r1: one new commit.
    run("fixture", "checkout", "-q", "-b", "fx-feat", base)
    put("src/pages/AdvisorIntelligence/ai.tsx", "feat ai\n")
    commit("carol", "F1 advisor intelligence")
    run("carol", "cherry-pick", dev_d2)
    feat = run("fixture", "rev-parse", "HEAD")
    run("fixture", "checkout", "-q", "-b", "fx-q", base)
    put("src/pages/TicketCenter/t2.tsx", "q t2\n")
    q = commit("dan", "G1 ticket center new file")
    refs = (("DEV", dev), ("PROD", prod), ("feat-x", feat), ("q/x/r1", q), ("old", base))
    for name, sha in refs:
        run("fixture", "update-ref", "refs/remotes/origin/" + name, sha)
    return p1


def selftest():
    tmp = tempfile.mkdtemp(prefix="settle-selftest-")
    cases = []
    try:
        repo = os.path.join(tmp, "repo")
        os.makedirs(repo)
        out = os.path.join(tmp, "out", "SETTLEMENT_LIST.md")
        p1 = _fixture(repo)
        data = build(repo)
        text, machine = render(data)
        write_text(out, text)
        with open(out, "r", encoding="ascii") as handle:
            written = handle.read()
        groups = {g["name"]: g for g in data["groups"]}
        branches = {b["name"]: b for b in data["branches"]}
        signs = {row["sha"]: row["sign"] for row in data["prod_rows"]}
        expect_machine = ("SETTLEMENT-LIST dev_ahead=3 prod_ahead=2 groups=4 files_total=6 files_other=1 "
                          "branches=2")
        cases = [
            ("dev_ahead", 3, data["dev_ahead"]),
            ("prod_ahead", 2, data["prod_ahead"]),
            ("files_total", 6, data["files_total"]),
            ("files_other", 1, data["files_other"]),
            ("groups (named, with files)", 4, data["groups_named"]),
            ("files InvestorReporting", 2, groups["InvestorReporting"]["files"]),
            ("files SecurityAnalysis", 1, groups["SecurityAnalysis"]["files"]),
            ("files TicketCenter", 0, groups["TicketCenter"]["files"]),
            ("files AdvisorIntelligence", 0, groups["AdvisorIntelligence"]["files"]),
            ("files api", 1, groups["api"]["files"]),
            ("files firmAccess", 1, groups["firmAccess"]["files"]),
            ("files other", 1, groups["other"]["files"]),
            ("commits InvestorReporting", 1, groups["InvestorReporting"]["commits"]),
            ("commits SecurityAnalysis", 1, groups["SecurityAnalysis"]["commits"]),
            ("commits TicketCenter", 0, groups["TicketCenter"]["commits"]),
            ("commits api", 1, groups["api"]["commits"]),
            ("commits firmAccess", 1, groups["firmAccess"]["commits"]),
            ("commits other", 1, groups["other"]["commits"]),
            ("top committers firmAccess", [("alice", 1)], groups["firmAccess"]["top"]),
            ("PROD-only commits listed", 2, len(data["prod_rows"])),
            ("PROD-only cherry '-' (same patch on DEV)", 1, sum(1 for s in signs.values() if s == "-")),
            ("PROD-only cherry '+' (not on DEV)", 1, sum(1 for s in signs.values() if s == "+")),
            ("PROD-only P1 marked '-'", "-", signs.get(p1)),
            ("branches with work not on DEV", 2, len(data["branches"])),
            ("feat-x ahead", 2, branches.get("feat-x", {}).get("ahead")),
            ("feat-x cherry +", 1, branches.get("feat-x", {}).get("plus")),
            ("feat-x cherry -", 1, branches.get("feat-x", {}).get("minus")),
            ("q/x/r1 ahead", 1, branches.get("q/x/r1", {}).get("ahead")),
            ("old branch excluded", None, branches.get("old")),
            ("root file lands in other", "other", group_of("README.md")),
            ("prefix boundary: InvestorReportingX lands in other", "other",
             group_of("src/pages/InvestorReportingX/q.ts")),
            ("output file written, machine line last", expect_machine, written.splitlines()[-1]),
            ("output file ASCII only", True, all(ord(ch) < 128 for ch in written)),
        ]
        error = None
    except Exception as exc:  # the self-test reports, it does not crash
        error = ascii_text(str(exc))
    finally:
        shutil.rmtree(tmp, onerror=_rm_readonly)
    passed = 0
    for label, want, got in cases:
        if want == got:
            passed += 1
        else:
            print("MISMATCH %s: expected=%r actual=%r" % (ascii_text(label), want, ascii_text(repr(got))))
    total = len(cases)
    if error is not None:
        print("ERROR: " + error)
        total = max(total, 1)
    ok = error is None and passed == total
    print("SETTLEMENT-LIST-SELFTEST cases=%d/%d ok=%s" % (passed, total, ok))
    return 0 if ok else 1


def _rm_readonly(func, path, _exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the portal settlement list (DEV groups, PROD-only "
                                                 "commits, branches with work not on DEV) from git.")
    parser.add_argument("--portal", default=DEFAULT_PORTAL, help="portal repo path (default: portal)")
    parser.add_argument("--out", default=DEFAULT_OUT, help="markdown file to write")
    parser.add_argument("--selftest", action="store_true", help="run the fixture self-test and exit")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    try:
        data = build(args.portal)
    except RuntimeError as exc:
        print("ERROR: " + ascii_text(str(exc)))
        return 1
    text, machine = render(data)
    write_text(args.out, text)
    print("WROTE " + ascii_text(os.path.abspath(args.out)))
    print(machine)
    return 0


if __name__ == "__main__":
    sys.exit(main())
