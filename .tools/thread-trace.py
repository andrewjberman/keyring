#!/usr/bin/env python3
"""thread-trace.py -- read one round's five hops from git, each with its start and end time.
(NFRA_CTLPLN round 6 THREAD, cell CT-t-1; PRD FWD-1 re-based in v0.22, FWD-4.)

    python .tools/thread-trace.py --project <CODE> --round <n> [--order <id>]... [--fetch]
    python .tools/thread-trace.py --selftest

--order <id> (repeatable; NFRA_CTLPLN round 10 CT-z-1, PRD FWD-1) reads only the named orders of the round. <id> is one of:
the order's <to_id> or its file stem, each with or without the <CODE>. prefix; or the slug-less id, the first dot-separated
segment after that prefix. So TO-CT-y-2 names NFRA_CTLPLN.TO-CT-y-2.dell1-fresh-process-blocked-download, and TO-CT-y-1 does
NOT name TO-CT-y-10 (the match is exact, never a prefix). Every hop then uses only those orders: HOP 1 their issuance, HOP 2
their issued_to serial's commits on their paths, order file and proof instance, and HOP 4 and HOP 5 the rest as above. An
<id> that names no order of the round makes the read a zero-hops read (orders=NONE, 0/5, exit 1); it never falls back to the
whole round.

A round is planned on one box, worked and pushed on a box branch, merged into CLOUD by the integrator, and graded. Every hop
leaves commits, so every hop can be read from git with no live seat asked. The round's orders are the files
org/missions/D*/*/<CODE>/task-orders/*.md AND the seat orders org/tier2_senior/*/task_orders/<CODE>.*.md (NFRA_CTLPLN round 10
Amendment 1: a seat order is an order of the round too), whose <round> tag is <n> (the LAST line-anchored <status> tag is the
order's status; superseded / cancelled / withdrawn / retired orders are not part of the thread). A seat order's mission
directory is found by its <CODE> (org/missions/D*/*/<CODE>). DELIBERATE CHANGE: the unfiltered whole-round read (no --order)
now also includes the seat orders of the round; the tree orders are read exactly as before. The refs read are origin/box/*
and origin/CLOUD.

  HOP 1 PLAN       the commit that first ADDED each order (earliest = start, latest = end); its author; the box branch it is
                   first-parent history of (fewest commits behind that tip), else any ref that holds it.
  HOP 2 WORK       the first and last commit authored by an order's <issued_to> serial that touches that order's <paths>, its
                   order file or its proof instance, no earlier than that order's issuance and no later than the last such
                   commit that touches the order file or proof instance (so a later round on a reused slot is not read as this
                   one). where= the box branch each of the first and the last commit reached earliest
                   (as in HOP 3).
  HOP 3 PUBLISH    the earliest commit on a box branch's first-parent chain that contains HOP 2's last commit (a binary
                   search over that chain: containment only ever turns on going forward); start = HOP 2 end.
  HOP 4 INTEGRATE  the same search on origin/CLOUD; by= its author. pushed_by_working_box=True when that author also authored
                   a non-merge commit on the working box's side of the merge (the second parent less the first), or a HOP 2
                   commit: the working box then pushed CLOUD itself and FWD-4 does not hold.
  HOP 5 GRADE      the first commit after HOP 4, on origin/CLOUD or a box branch, by a CVO-kind or CTO-kind serial
                   (lib/seat_roles.py kind_of) that adds a line naming one of the round's criterion ids to the project's
                   surprise-channel/adjudications/, or adds a dep_stage line to project.json while naming one.

Line per hop:   HOP <n> <name> start=<UTC> end=<UTC> commit=<h> by=<serial> where=<ref>     or    HOP <n> <name> ABSENT
LAST line:      THREAD project=<CODE> round=<n> orders=<ids, comma-separated | ALL | NONE> hops=<found>/5 pushed_by_working_box=<True|False|-> elapsed=<h m s | ->
                 orders=ALL when no --order was given; orders=NONE when an --order matched no order of the round.
Exit 0 when the read found orders; 1 when the round has none (0/5) or an --order matches none (0/5); 2 on a usage, fetch or git error.
BLIND (stated): time a seat spent thinking, polling or waiting leaves no commit and is inside the hop that holds it; the
publish time is a commit time (git records no push time); a serial shared by two boxes cannot tell their seats apart, so
pushed_by_working_box compares serials, not machines. It READS git and writes nothing in the repository.
Selftest LAST line: THREAD-TRACE-SELFTEST cases=<k>/<n> ok=<True|False>.
"""
from __future__ import annotations

import argparse
import fnmatch
import glob
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
REMOTE = "origin"
BOX_PATTERN = "refs/remotes/%s/box" % REMOTE
TRUNK_REF = "refs/remotes/%s/CLOUD" % REMOTE
HOPS = ("PLAN", "WORK", "PUBLISH", "INTEGRATE", "GRADE")
DEAD = ("superseded", "cancelled", "canceled", "withdrawn", "retired")
GRADER_KINDS = ("CVO", "CTO")
SEP = "\x1e"
US = "\x1f"
CRIT_TAG = re.compile(r"<criterion\b([^>]*?)/?>")
ATTR = re.compile(r'([A-Za-z_]+)="([^"]*)"')


class GitError(Exception):
    pass


# ---------------------------------------------------------------- git plumbing

def git(root: str, *args: str, ok=(0,)) -> str:
    p = subprocess.run(["git", "-c", "core.quotepath=false", *args], cwd=root, capture_output=True,
                       encoding="utf-8", errors="replace")
    if p.returncode not in ok:
        raise GitError("git %s -> rc=%d: %s" % (" ".join(args[:4]), p.returncode, p.stderr.strip()[:300]))
    return p.stdout


def utc(ct: int) -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ct))


def short(ref: str) -> str:
    return ref[len("refs/remotes/"):] if ref.startswith("refs/remotes/") else ref


class Repo:
    """One repository, with the caches a trace needs."""

    def __init__(self, root: str):
        self.root = root
        self._info: dict = {}
        self._fp: dict = {}
        self._kinds = _load_kinds()

    def refs(self) -> list:
        out = git(self.root, "for-each-ref", "--format=%(refname)", BOX_PATTERN, TRUNK_REF).split()
        return sorted(out)

    def box_refs(self) -> list:
        return [r for r in self.refs() if r != TRUNK_REF]

    def info(self, c: str) -> dict:
        if c not in self._info:
            out = git(self.root, "show", "-s", "--format=%H" + US + "%an" + US + "%ct" + US + "%P", c).strip()
            h, an, ct, parents = out.split(US)
            self._info[c] = {"hash": h, "author": an, "ct": int(ct), "parents": parents.split()}
        return self._info[c]

    def holders(self, c: str) -> list:
        out = git(self.root, "for-each-ref", "--contains", c, "--format=%(refname)", BOX_PATTERN, TRUNK_REF)
        return sorted(out.split())

    def contains(self, ref_or_commit: str, c: str) -> bool:
        p = subprocess.run(["git", "merge-base", "--is-ancestor", c, ref_or_commit], cwd=self.root,
                           capture_output=True)
        return p.returncode == 0

    def fp(self, ref: str) -> list:
        if ref not in self._fp:
            self._fp[ref] = git(self.root, "rev-list", "--first-parent", ref).split()
        return self._fp[ref]

    def first_on_chain(self, ref: str, c: str):
        """The earliest commit on ref's first-parent chain that contains c, or None. Containment is monotone along that
        chain (a commit containing c is contained by every later one), so the boundary is found by binary search."""
        chain = self.fp(ref)  # newest first
        if not chain or not self.contains(chain[0], c):
            return None
        lo, hi = 0, len(chain) - 1  # chain[lo] contains c; find the largest index that still does
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.contains(chain[mid], c):
                lo = mid
            else:
                hi = mid - 1
        return chain[lo]

    def earliest_box(self, c: str):
        """(commit, ct, ref): the box branch whose first-parent chain reached a commit containing c earliest, or None."""
        best = None
        for ref in self.box_refs():
            m = self.first_on_chain(ref, c)
            if m and (best is None or (self.info(m)["ct"], ref) < (best[1], best[2])):
                best = (m, self.info(m)["ct"], ref)
        return best

    def home(self, c: str) -> str:
        """The ref a commit first appears on: among the refs that hold it on a first-parent chain, the one with the fewest
        commits since it; else the first ref that holds it at all."""
        held = self.holders(c)
        if not held:
            return ""
        best, best_n = "", None
        for ref in held:
            if c in set(self.fp(ref)):
                n = int(git(self.root, "rev-list", "--count", "%s..%s" % (c, ref)).strip() or 0)
                if best_n is None or n < best_n:
                    best, best_n = ref, n
        return short(best or held[0])

    def kind(self, serial: str) -> str:
        return self._kinds(serial)

    def log_names(self, revs: list, pathspecs: list, *flags: str) -> list:
        """[(hash, author, ct, [files])] over revs, limited to pathspecs."""
        args = ["log", *flags, "--name-only", "--format=" + SEP + "%H" + US + "%an" + US + "%ct", *revs]
        if pathspecs:
            args += ["--", *pathspecs]
        rows = []
        for blob in git(self.root, *args).split(SEP)[1:]:
            head, _, rest = blob.partition("\n")
            h, an, ct = head.split(US)
            rows.append((h, an, int(ct), [x.strip() for x in rest.splitlines() if x.strip()]))
        return rows


def _load_kinds():
    """kind_of through lib/seat_roles.py of THIS tool's own tree; a regex on the serial's role letters when it is absent."""
    path = os.path.join(ROOT, "lib", "seat_roles.py")
    try:
        spec = importlib.util.spec_from_file_location("opal_seat_roles_tt", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        data = mod.load()
        return lambda serial: mod.kind_of(serial, data)
    except Exception:  # noqa: BLE001 - lib/seat_roles.py absent or unreadable: the fallback below
        def fallback(serial: str) -> str:
            for kind, pat in (("CVO", r"_SA_CVO"), ("CTO", r"_SA_CTO"), ("COO", r"_SA_COO"), ("MSTR", r"_AB_MSTR"),
                              ("WORKER", r"_WK_")):
                if re.search(pat, serial):
                    return kind
            return "UNKNOWN"
        return fallback


# ---------------------------------------------------------------- the round's orders

def _tag(text: str, name: str):
    m = re.search(r"^<%s>(.*?)</%s>" % (name, name), text, re.M)
    return m.group(1).strip() if m else None


def _last_status(text: str) -> str:
    text = re.sub(r"<proof_of_spec>.*?</proof_of_spec>", "", text, flags=re.S)
    got = ""
    for m in re.finditer(r"^<status>(.*?)</status>", text, re.M):
        got = m.group(1).strip().lower()
    return got


def _mission_dir(root: str, code: str) -> str:
    """The project's mission directory (org/missions/D*/*/<CODE>), for an order that lives outside it (a seat order)."""
    hits = sorted(h for h in glob.glob(os.path.join(root, "org", "missions", "D*", "*", code)) if os.path.isdir(h))
    return os.path.relpath(hits[0], root).replace(os.sep, "/") if hits else "(no mission directory)"


def find_orders(root: str, code: str, rnd: str) -> list:
    out = []
    tree = os.path.join(root, "org", "missions", "D*", "*", code, "task-orders", "*.md")
    seat = os.path.join(root, "org", "tier2_senior", "*", "task_orders", code + ".*.md")
    for pattern, is_seat in ((tree, False), (seat, True)):
        for path in sorted(glob.glob(pattern)):
            text = open(path, encoding="utf-8", errors="replace").read()
            if str(_tag(text, "round")) != str(rnd):
                continue
            status = _last_status(text)
            if status.startswith(DEAD):
                continue
            block = re.search(r"^<paths>\s*\n(.*?)^</paths>", text, re.M | re.S)
            paths = [ln.split()[0] for ln in (block.group(1).splitlines() if block else []) if ln.strip()]
            crits = [dict(ATTR.findall(m.group(1))).get("id") for m in CRIT_TAG.finditer(text)]
            rel = os.path.relpath(path, root).replace(os.sep, "/")
            projdir = _mission_dir(root, code) if is_seat else rel.rsplit("/task-orders/", 1)[0]
            out.append({"rel": rel, "stem": os.path.basename(path)[:-3],
                        "id": _tag(text, "to_id") or os.path.basename(path)[:-3],
                        "issued_to": _tag(text, "issued_to") or "", "paths": paths, "status": status,
                        "criteria": [c for c in crits if c], "projdir": projdir})
    return out


def _unprefixed(name: str, code: str) -> str:
    return name[len(code) + 1:] if name.startswith(code + ".") else name


def _slugless(name: str, code: str) -> str:
    """The order id with its slug dropped: the first dot-separated segment after the CODE. prefix (TO-CT-y-2)."""
    return _unprefixed(name, code).split(".")[0]


def order_names(order: dict, code: str) -> set:
    """The spellings an --order value may take, as an EXACT set (no prefix matching): for the to_id and the file stem, the
    spelling itself, the spelling without the CODE. prefix, and the slug-less id with and without that prefix."""
    names = set()
    for raw in (order["id"], order["stem"]):
        head = _slugless(raw, code)
        names.update({raw, _unprefixed(raw, code), head, code + "." + head})
    return names


def _touches(path: str, pathspec: str) -> bool:
    return path == pathspec or fnmatch.fnmatch(path, pathspec) or path.startswith(pathspec.rstrip("/") + "/")


# ---------------------------------------------------------------- the hops

def trace(root: str, code: str, rnd: str, only=None):
    """Return (rc, lines). The last line is the THREAD summary. only: the --order values, or None for the whole round."""
    repo = Repo(root)
    every = find_orders(root, code, rnd)
    absent = ["HOP %d %s ABSENT" % (i + 1, n) for i, n in enumerate(HOPS)]
    summary = "THREAD project=%s round=%s orders=%s hops=%d/5 pushed_by_working_box=%s elapsed=%s"
    orders, shown = every, "ALL"
    if only:
        wanted = set(only)
        known = set().union(*(order_names(o, code) for o in every))
        orders = [o for o in every if order_names(o, code) & wanted]
        if not orders or wanted - known:
            return 1, absent + [summary % (code, rnd, "NONE", 0, "-", "-")]
        shown = ",".join(dict.fromkeys(_slugless(o["id"], code) for o in orders))
    if not orders:
        return 1, absent + [summary % (code, rnd, "ALL", 0, "-", "-")]
    refs = repo.refs()
    if not refs:
        raise GitError("no %s/* or %s/CLOUD refs to read" % (BOX_PATTERN, REMOTE))
    lines: list = []
    found = 0
    pushed = "-"

    # HOP 1: the commit that first added each order
    added = repo.log_names(refs, [o["rel"] for o in orders], "--diff-filter=A")
    first_add: dict = {}
    for h, an, ct, files in added:
        for f in files:
            if f not in first_add or (ct, h) < (first_add[f][2], first_add[f][0]):
                first_add[f] = (h, an, ct)
    issued = {o["rel"]: first_add[o["rel"]] for o in orders if o["rel"] in first_add}
    hop1 = None
    if issued:
        starts = sorted(issued.values(), key=lambda t: (t[2], t[0]))
        first, last = starts[0], starts[-1]
        hop1 = (first[2], last[2])
        lines.append("HOP 1 PLAN start=%s end=%s commit=%s by=%s where=%s" % (
            utc(first[2]), utc(last[2]), first[0][:10], first[1], repo.home(first[0]) or "-"))
        found += 1
    else:
        lines.append(absent[0])

    # HOP 2: the issued_to serial's commits on each order's paths, order file and proof instance
    specs = sorted({p for o in orders for p in o["paths"]} | {o["rel"] for o in orders}
                   | {o["projdir"] + "/deliverables" for o in orders})
    work = repo.log_names(refs, specs, "--no-merges")
    kept: list = []
    for o in orders:
        lo = issued[o["rel"]][2] if o["rel"] in issued else 0
        mine, closers = [], []
        for h, an, ct, files in work:
            if an != o["issued_to"] or ct < lo:
                continue
            is_close = any(f == o["rel"] or (f.startswith(o["projdir"] + "/deliverables/")
                                              and f.endswith("/" + o["stem"] + ".proof_of_spec.json")) for f in files)
            if is_close or any(_touches(f, p) for f in files for p in o["paths"]):
                mine.append((h, an, ct))
                if is_close:
                    closers.append(ct)
        cap = max(closers) if closers else None
        kept += [m for m in mine if cap is None or m[2] <= cap]
    last_work = None
    if kept:
        kept.sort(key=lambda t: (t[2], t[0]))
        w_first, w_last = kept[0], kept[-1]
        last_work = w_last
        where = sorted({short(repo.earliest_box(c)[2]) for c in (w_first[0], w_last[0]) if repo.earliest_box(c)})
        lines.append("HOP 2 WORK start=%s end=%s commit=%s by=%s where=%s" % (
            utc(w_first[2]), utc(w_last[2]), w_last[0][:10], w_last[1], ",".join(where) or "-"))
        found += 1
    else:
        lines.append(absent[1])

    # HOP 3: the first commit on a box branch that contains HOP 2's last commit
    pub = repo.earliest_box(last_work[0]) if last_work else None
    if pub:
        lines.append("HOP 3 PUBLISH start=%s end=%s commit=%s by=%s where=%s" % (
            utc(last_work[2]), utc(pub[1]), pub[0][:10], repo.info(pub[0])["author"], short(pub[2])))
        found += 1
    else:
        lines.append(absent[2])

    # HOP 4: the first commit on origin/CLOUD that contains HOP 2's last commit
    integ = None
    if last_work and TRUNK_REF in refs:
        m = repo.first_on_chain(TRUNK_REF, last_work[0])
        if m:
            integ = m
    if integ:
        mi = repo.info(integ)
        start4 = pub[1] if pub else last_work[2]
        lines.append("HOP 4 INTEGRATE start=%s end=%s commit=%s by=%s where=%s" % (
            utc(start4), utc(mi["ct"]), integ[:10], mi["author"], short(TRUNK_REF)))
        found += 1
        box_side = {a for a in kept_authors(kept)}
        if len(mi["parents"]) >= 2:
            names = git(root, "log", "--no-merges", "--format=%an", mi["parents"][1], "--not", mi["parents"][0])
            box_side |= {n for n in names.splitlines() if n}
        pushed = str(mi["author"] in box_side)
    else:
        lines.append(absent[3])

    # HOP 5: the first CVO-kind or CTO-kind commit after HOP 4 that grades a criterion of the round
    graded = None
    if integ:
        graded = find_grade(repo, orders, integ, refs)
    if graded:
        lines.append("HOP 5 GRADE start=%s end=%s commit=%s by=%s where=%s" % (
            utc(repo.info(integ)["ct"]), utc(graded[1]), graded[0][:10], graded[2], repo.home(graded[0]) or "-"))
        found += 1
    else:
        lines.append(absent[4])

    elapsed = "-"
    if hop1 and graded:
        secs = max(0, graded[1] - hop1[0])
        elapsed = "%dh%02dm%02ds" % (secs // 3600, secs % 3600 // 60, secs % 60)
    lines.append(summary % (code, rnd, shown, found, pushed, elapsed))
    return 0, lines


def kept_authors(kept: list) -> list:
    return [k[1] for k in kept]


def find_grade(repo: Repo, orders: list, after: str, refs: list):
    ids = sorted({c for o in orders for c in o["criteria"]})
    if not ids:
        return None
    projdirs = sorted({o["projdir"] for o in orders})
    specs = []
    for d in projdirs:
        specs += [d + "/surprise-channel/adjudications", d + "/project.json"]
    cands = repo.log_names(["^" + after, *refs], specs, "--no-merges", "--ancestry-path")
    cands.sort(key=lambda t: (t[2], t[0]))
    word = re.compile(r"(?<![A-Za-z0-9_-])(?:%s)(?![A-Za-z0-9_-])" % "|".join(re.escape(i) for i in ids))
    for h, an, ct, files in cands:
        if repo.kind(an) not in GRADER_KINDS:
            continue
        body = git(repo.root, "show", "--format=", "-U0", h, "--", *specs)
        added = [ln[1:] for ln in body.splitlines() if ln.startswith("+") and not ln.startswith("+++")]
        names_it = any(word.search(ln) for ln in added)
        adjud = any("/surprise-channel/adjudications/" in f for f in files)
        flips = any(f.endswith("/project.json") for f in files) and any("dep_stage" in ln for ln in added)
        if names_it and (adjud or flips):
            return (h, ct, an)
    return None


# ---------------------------------------------------------------- selftest

T0 = 1_700_000_000
MAC = "org/missions/D0/MAC/PRJ"
ORDER = MAC + "/task-orders/PRJ.TO-1.md"
PROOF = MAC + "/deliverables/0.9.0_WK_PRJ~1/PRJ.TO-1.proof_of_spec.json"
ADJ = MAC + "/surprise-channel/adjudications/ADJUDICATION_v1.md"


def _order_text(status: str, to: str = "TO-1", worker: str = "0.9.0_WK_PRJ~1", crit: str = "T1-AC1",
                path: str = "src/a.txt") -> str:
    return ("# TO PRJ.%s\n\n<to_id>PRJ.%s</to_id>\n<issued_to>%s</issued_to>\n"
            "<issued_by>2.0.0_SA_COO~A</issued_by>\n<status>%s</status>\n<round>1</round>\n\n"
            "<proof_of_spec>\n<criterion id=\"%s\" cell_refs=\"X\"><invocation>true</invocation>"
            "<expect>ok</expect></criterion>\n</proof_of_spec>\n\n<paths>\n%s\n</paths>\n"
            % (to, to, worker, status, crit, path))


class Lab:
    def __init__(self, root: str):
        self.root = root

    def run(self, author: str, ts: int, *args: str):
        env = dict(os.environ, GIT_AUTHOR_NAME=author, GIT_AUTHOR_EMAIL=author + "@opal.agent", GIT_AUTHOR_DATE="%d +0000" % ts,
                   GIT_COMMITTER_NAME=author, GIT_COMMITTER_EMAIL=author + "@opal.agent", GIT_COMMITTER_DATE="%d +0000" % ts,
                   GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_SYSTEM=os.devnull)
        p = subprocess.run(["git", "-c", "commit.gpgsign=false", *args], cwd=self.root, env=env, capture_output=True,
                           encoding="utf-8", errors="replace")
        if p.returncode != 0:
            raise GitError("lab git %s: %s" % (" ".join(args[:3]), p.stderr.strip()[:200]))
        return p.stdout

    def commit(self, author: str, ts: int, subject: str, files: dict):
        for rel, text in files.items():
            full = os.path.join(self.root, *rel.split("/"))
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
        self.run(author, ts, "add", "-A")
        self.run(author, ts, "commit", "-q", "-m", subject)

    def merge(self, author: str, ts: int, subject: str, other: str):
        self.run(author, ts, "merge", "--no-ff", "-q", "-m", subject, other)


def build_thread(root: str, grade: bool, integrator: str, box_mstr: bool):
    lab = Lab(root)
    lab.run("init", T0, "init", "-q", "-b", "CLOUD")
    lab.commit("0.0.0_AB_MSTR", T0, "base", {"README.md": "base\n"})
    lab.run("x", T0, "checkout", "-q", "-b", "box/alpha")
    lab.commit("2.0.0_SA_COO~A", T0 + 100, "issue(PRJ round 1): TO-1", {ORDER: _order_text("pending")})
    lab.run("x", T0, "checkout", "-q", "-b", "box/beta")
    if box_mstr:
        lab.commit("0.0.0_AB_MSTR~BETA", T0 + 250, "beta box work", {"beta.txt": "b\n"})
    lab.run("x", T0, "checkout", "-q", "-b", "wk-PRJ-1")
    lab.commit("0.9.0_WK_PRJ~1", T0 + 300, "work 1", {"src/a.txt": "1\n"})
    lab.commit("0.9.0_WK_PRJ~1", T0 + 500, "work 2 and close", {"src/a.txt": "2\n", ORDER: _order_text("complete"),
                                                                 PROOF: "{}\n"})
    lab.run("x", T0, "checkout", "-q", "box/beta")
    lab.merge("2.0.0_SA_COO~B", T0 + 700, "drain wk-PRJ-1", "wk-PRJ-1")
    lab.run("x", T0, "checkout", "-q", "CLOUD")
    lab.merge(integrator, T0 + 900, "integrate(%s): box/beta @x into CLOUD (box-sync)" % integrator, "box/beta")
    if grade:
        lab.commit("3.0.0_SA_CVO", T0 + 1200, "adjudicate PRJ round 1", {ADJ: "T1-AC1 MET\n"})
    for name, ref in (("CLOUD", "CLOUD"), ("box/alpha", "box/alpha"), ("box/beta", "box/beta")):
        lab.run("x", T0, "update-ref", "refs/remotes/%s/%s" % (REMOTE, name), "refs/heads/" + ref)


TO2_ORDER = MAC + "/task-orders/PRJ.TO-2.md"
TO2_PROOF = MAC + "/deliverables/0.7.0_AE_OPS~2/PRJ.TO-2.proof_of_spec.json"
TO2_SERIAL = "0.7.0_AE_OPS~2"


def build_pair(root: str):
    """Two orders in one round: TO-1 issued on box/alpha to a worker, TO-2 issued on box/gamma to a seat. Each is worked on
    its own branch, drained into its own box, and both are integrated into CLOUD and graded. Times: TO-1 issued T0+100,
    TO-2 issued T0+150, TO-1 worked T0+300..T0+500 and drained T0+600, TO-2 worked T0+200..T0+400 and drained T0+650,
    box/alpha integrated T0+700, box/gamma integrated T0+750, graded T0+1000."""
    lab = Lab(root)
    lab.run("init", T0, "init", "-q", "-b", "CLOUD")
    lab.commit("0.0.0_AB_MSTR", T0, "base", {"README.md": "base\n"})
    lab.run("x", T0, "checkout", "-q", "-b", "box/alpha")
    lab.commit("2.0.0_SA_COO~A", T0 + 100, "issue(PRJ round 1): TO-1", {ORDER: _order_text("pending")})
    lab.run("x", T0, "checkout", "-q", "-b", "wk-PRJ-1")
    lab.commit("0.9.0_WK_PRJ~1", T0 + 300, "work 1", {"src/a.txt": "1\n"})
    lab.commit("0.9.0_WK_PRJ~1", T0 + 500, "work 2 and close", {"src/a.txt": "2\n", ORDER: _order_text("complete"),
                                                                 PROOF: "{}\n"})
    lab.run("x", T0, "checkout", "-q", "box/alpha")
    lab.merge("2.0.0_SA_COO~A", T0 + 600, "drain wk-PRJ-1", "wk-PRJ-1")
    lab.run("x", T0, "checkout", "-q", "CLOUD")
    lab.run("x", T0, "checkout", "-q", "-b", "box/gamma")
    lab.commit("2.0.0_SA_COO~A", T0 + 150, "issue(PRJ round 1): TO-2", {TO2_ORDER: _order_text(
        "pending", "TO-2", TO2_SERIAL, "T2-AC1", "src/b.txt")})
    lab.run("x", T0, "checkout", "-q", "-b", "seat-PRJ-2")
    lab.commit(TO2_SERIAL, T0 + 200, "seat work 1", {"src/b.txt": "1\n"})
    lab.commit(TO2_SERIAL, T0 + 400, "seat work 2 and close", {"src/b.txt": "2\n", TO2_ORDER: _order_text(
        "complete", "TO-2", TO2_SERIAL, "T2-AC1", "src/b.txt"), TO2_PROOF: "{}\n"})
    lab.run("x", T0, "checkout", "-q", "box/gamma")
    lab.merge("2.0.0_SA_COO~C", T0 + 650, "drain seat-PRJ-2", "seat-PRJ-2")
    lab.run("x", T0, "checkout", "-q", "CLOUD")
    lab.merge("0.0.0_AB_MSTR", T0 + 700, "integrate(0.0.0_AB_MSTR): box/alpha @x into CLOUD (box-sync)", "box/alpha")
    lab.merge("0.0.0_AB_MSTR", T0 + 750, "integrate(0.0.0_AB_MSTR): box/gamma @x into CLOUD (box-sync)", "box/gamma")
    lab.commit("3.0.0_SA_CVO", T0 + 1000, "adjudicate PRJ round 1", {ADJ: "T1-AC1 MET\nT2-AC1 MET\n"})
    for name, ref in (("CLOUD", "CLOUD"), ("box/alpha", "box/alpha"), ("box/gamma", "box/gamma")):
        lab.run("x", T0, "update-ref", "refs/remotes/%s/%s" % (REMOTE, name), "refs/heads/" + ref)


SEAT_ORDER = "org/tier2_senior/0.7.0_AE_OPS~2/task_orders/PRJ.TO-3.dell1-slug.md"
SEAT_PROOF = MAC + "/deliverables/0.7.0_AE_OPS~2/PRJ.TO-3.dell1-slug.proof_of_spec.json"
SEAT_SERIAL = "0.7.0_AE_OPS~2"


def build_seat(root: str):
    """One SEAT order (under org/tier2_senior/<seat>/task_orders/, not the mission folder) in round 1, issued on box/seat, worked
    by the seat serial on its own branch at T0+200..T0+400, drained at T0+450 and integrated into CLOUD at T0+700. No grade."""
    lab = Lab(root)
    lab.run("init", T0, "init", "-q", "-b", "CLOUD")
    lab.commit("0.0.0_AB_MSTR", T0, "base", {"README.md": "base\n"})
    lab.run("x", T0, "checkout", "-q", "-b", "box/seat")
    lab.commit("2.0.0_SA_COO~A", T0 + 100, "issue(PRJ round 1): TO-3", {SEAT_ORDER: _order_text(
        "pending", "TO-3.dell1-slug", SEAT_SERIAL, "T3-AC1", "src/c.txt")})
    lab.run("x", T0, "checkout", "-q", "-b", "seat-PRJ-3")
    lab.commit(SEAT_SERIAL, T0 + 200, "seat work 1", {"src/c.txt": "1\n"})
    lab.commit(SEAT_SERIAL, T0 + 400, "seat work 2 and close", {"src/c.txt": "2\n", SEAT_ORDER: _order_text(
        "complete", "TO-3.dell1-slug", SEAT_SERIAL, "T3-AC1", "src/c.txt"), SEAT_PROOF: "{}\n"})
    lab.run("x", T0, "checkout", "-q", "box/seat")
    lab.merge("2.0.0_SA_COO~A", T0 + 450, "drain seat-PRJ-3", "seat-PRJ-3")
    lab.run("x", T0, "checkout", "-q", "CLOUD")
    lab.merge("0.0.0_AB_MSTR", T0 + 700, "integrate(0.0.0_AB_MSTR): box/seat @x into CLOUD (box-sync)", "box/seat")
    for name, ref in (("CLOUD", "CLOUD"), ("box/seat", "box/seat")):
        lab.run("x", T0, "update-ref", "refs/remotes/%s/%s" % (REMOTE, name), "refs/heads/" + ref)


def build_ten(root: str):
    """One tree order with the id PRJ.TO-10.slug, issued in round 1 and integrated into CLOUD. No work, no grade."""
    lab = Lab(root)
    lab.run("init", T0, "init", "-q", "-b", "CLOUD")
    lab.commit("0.0.0_AB_MSTR", T0, "base", {"README.md": "base\n"})
    lab.commit("2.0.0_SA_COO~A", T0 + 100, "issue(PRJ round 1): TO-10", {MAC + "/task-orders/PRJ.TO-10.slug.md": _order_text(
        "pending", "TO-10.slug", "0.9.0_WK_PRJ~1", "T10-AC1", "src/d.txt")})
    lab.run("x", T0, "update-ref", "refs/remotes/%s/CLOUD" % REMOTE, "refs/heads/CLOUD")


def selftest() -> int:
    results = []

    def case(name: str, fn):
        tmp = tempfile.mkdtemp(prefix="thread-trace-selftest-")
        try:
            ok, note = fn(tmp)
        except Exception as exc:  # noqa: BLE001 - a case that raises is a failed case
            ok, note = False, "raised %s: %s" % (type(exc).__name__, exc)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        results.append(ok)
        print("%s case %s: %s" % ("PASS" if ok else "FAIL", name, note))

    def full(tmp):
        build_thread(tmp, True, "0.0.0_AB_MSTR", False)
        rc, lines = trace(tmp, "PRJ", "1")
        want = ["HOP 1 PLAN start=%s end=%s" % (utc(T0 + 100), utc(T0 + 100)),
                "HOP 2 WORK start=%s end=%s" % (utc(T0 + 300), utc(T0 + 500)),
                "HOP 3 PUBLISH start=%s end=%s" % (utc(T0 + 500), utc(T0 + 700)),
                "HOP 4 INTEGRATE start=%s end=%s" % (utc(T0 + 700), utc(T0 + 900)),
                "HOP 5 GRADE start=%s end=%s" % (utc(T0 + 900), utc(T0 + 1200))]
        ok = rc == 0 and all(lines[i].startswith(w) for i, w in enumerate(want))
        ok = ok and "by=2.0.0_SA_COO~A where=%s/box/alpha" % REMOTE in lines[0]
        ok = ok and "where=%s/box/beta" % REMOTE in lines[1] and "by=0.0.0_AB_MSTR" in lines[3]
        tail = "hops=5/5 pushed_by_working_box=False elapsed=0h18m20s"
        return ok and lines[-1].endswith(tail), lines[-1]

    def nograde(tmp):
        build_thread(tmp, False, "0.0.0_AB_MSTR", False)
        rc, lines = trace(tmp, "PRJ", "1")
        return rc == 0 and "hops=4/5" in lines[-1] and lines[4] == "HOP 5 GRADE ABSENT" and lines[-1].endswith("elapsed=-"), lines[-1]

    def pushed(tmp):
        build_thread(tmp, True, "0.0.0_AB_MSTR~BETA", True)
        rc, lines = trace(tmp, "PRJ", "1")
        return rc == 0 and "hops=5/5 pushed_by_working_box=True" in lines[-1], lines[-1]

    def noorders(tmp):
        build_thread(tmp, True, "0.0.0_AB_MSTR", False)
        rc, lines = trace(tmp, "PRJ", "9")
        return rc != 0 and "hops=0/5" in lines[-1] and all(ln.endswith("ABSENT") for ln in lines[:5]), "rc=%d %s" % (rc, lines[-1])

    def only_first(tmp):
        build_pair(tmp)
        rc, lines = trace(tmp, "PRJ", "1", ["TO-1"])
        ok = rc == 0 and lines[0].startswith("HOP 1 PLAN start=%s end=%s" % (utc(T0 + 100), utc(T0 + 100)))
        ok = ok and "where=%s/box/alpha" % REMOTE in lines[0]
        ok = ok and lines[1].startswith("HOP 2 WORK start=%s end=%s" % (utc(T0 + 300), utc(T0 + 500)))
        ok = ok and "by=0.9.0_WK_PRJ~1 where=%s/box/alpha" % REMOTE in lines[1]
        ok = ok and not any(TO2_SERIAL in ln for ln in lines)
        return ok and lines[-1] == "THREAD project=PRJ round=1 orders=TO-1 hops=5/5 pushed_by_working_box=False elapsed=0h15m00s", lines[-1]

    def only_second(tmp):
        build_pair(tmp)
        rc, lines = trace(tmp, "PRJ", "1", ["TO-2"])
        ok = rc == 0 and lines[0].startswith("HOP 1 PLAN start=%s end=%s" % (utc(T0 + 150), utc(T0 + 150)))
        ok = ok and "where=%s/box/gamma" % REMOTE in lines[0]
        ok = ok and lines[1].startswith("HOP 2 WORK start=%s end=%s" % (utc(T0 + 200), utc(T0 + 400)))
        ok = ok and "by=%s where=%s/box/gamma" % (TO2_SERIAL, REMOTE) in lines[1]
        ok = ok and not any("0.9.0_WK_PRJ~1" in ln for ln in lines)
        return ok and lines[-1] == "THREAD project=PRJ round=1 orders=TO-2 hops=5/5 pushed_by_working_box=False elapsed=0h14m10s", lines[-1]

    def whole_round(tmp):
        build_pair(tmp)
        rc, lines = trace(tmp, "PRJ", "1")
        ok = rc == 0 and lines[0].startswith("HOP 1 PLAN start=%s end=%s" % (utc(T0 + 100), utc(T0 + 150)))
        ok = ok and "where=%s/box/alpha" % REMOTE in lines[0]
        ok = ok and lines[1].startswith("HOP 2 WORK start=%s end=%s" % (utc(T0 + 200), utc(T0 + 500)))
        ok = ok and "by=0.9.0_WK_PRJ~1 where=%s/box/alpha,%s/box/gamma" % (REMOTE, REMOTE) in lines[1]
        ok = ok and lines[2].startswith("HOP 3 PUBLISH start=%s end=%s" % (utc(T0 + 500), utc(T0 + 600)))
        ok = ok and lines[3].startswith("HOP 4 INTEGRATE start=%s end=%s" % (utc(T0 + 600), utc(T0 + 700)))
        ok = ok and lines[4].startswith("HOP 5 GRADE start=%s end=%s" % (utc(T0 + 700), utc(T0 + 1000)))
        return ok and lines[-1] == "THREAD project=PRJ round=1 orders=ALL hops=5/5 pushed_by_working_box=False elapsed=0h15m00s", lines[-1]

    def unknown_order(tmp):
        build_pair(tmp)
        rc, lines = trace(tmp, "PRJ", "1", ["TO-9"])
        ok = rc == 1 and all(ln.endswith("ABSENT") for ln in lines[:5])
        return ok and lines[-1] == "THREAD project=PRJ round=1 orders=NONE hops=0/5 pushed_by_working_box=- elapsed=-", lines[-1]

    def seat_order(tmp):
        build_seat(tmp)
        rc, lines = trace(tmp, "PRJ", "1", ["TO-3"])
        ok = rc == 0 and lines[0].startswith("HOP 1 PLAN start=%s end=%s" % (utc(T0 + 100), utc(T0 + 100)))
        ok = ok and lines[1].startswith("HOP 2 WORK start=%s end=%s" % (utc(T0 + 200), utc(T0 + 400)))
        ok = ok and "by=%s where=%s/box/seat" % (SEAT_SERIAL, REMOTE) in lines[1]
        ok = ok and lines[-1].startswith("THREAD project=PRJ round=1 orders=TO-3 hops=4/5 ")
        return ok, lines[1] + " || " + lines[-1]

    def prefix_no_collision(tmp):
        build_ten(tmp)
        rc1, lines1 = trace(tmp, "PRJ", "1", ["TO-1"])
        rc10, lines10 = trace(tmp, "PRJ", "1", ["TO-10"])
        ok = rc1 == 1 and lines1[-1] == "THREAD project=PRJ round=1 orders=NONE hops=0/5 pushed_by_working_box=- elapsed=-"
        ok = ok and rc10 == 0 and lines10[-1].startswith("THREAD project=PRJ round=1 orders=TO-10 hops=1/5 ")
        return ok, "TO-1: rc=%d %s || TO-10: rc=%d %s" % (rc1, lines1[-1], rc10, lines10[-1])

    case("full thread reads 5/5", full)
    case("no grade reads 4/5", nograde)
    case("working box pushed CLOUD itself", pushed)
    case("round with no orders reads 0/5, non-zero", noorders)
    case("--order first reads the first order's hops only", only_first)
    case("--order second reads the second order's hops only", only_second)
    case("no --order reads the whole round, orders=ALL", whole_round)
    case("--order matching no order reads 0/5, non-zero", unknown_order)
    case("seat order found; --order by its slug-less id reads its hops", seat_order)
    case("--order TO-1 does not match TO-10 (exact id, no prefix match)", prefix_no_collision)
    ok = all(results)
    print("THREAD-TRACE-SELFTEST cases=%d/%d ok=%s" % (sum(results), len(results), ok))
    return 0 if ok else 1


def main(argv: list) -> int:
    ap = argparse.ArgumentParser(description="Read one round's five hops from git.")
    ap.add_argument("--project")
    ap.add_argument("--round")
    ap.add_argument("--order", action="append", default=[], metavar="ID",
                    help="read only this order of the round (its to_id or file stem; repeatable)")
    ap.add_argument("--fetch", action="store_true", help="git fetch origin before reading")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--root", default=ROOT, help=argparse.SUPPRESS)
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.project or a.round is None:
        sys.stderr.write("usage: thread-trace.py --project <CODE> --round <n> [--order <id>]... [--fetch] | --selftest\n")
        return 2
    try:
        if a.fetch:
            git(a.root, "fetch", "-q", REMOTE)
        rc, lines = trace(a.root, a.project, a.round, a.order or None)
    except GitError as exc:
        sys.stderr.write("ERROR: %s\n" % exc)
        return 2
    print("\n".join(lines))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
