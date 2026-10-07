"""intake_closure.py -- the approved package list closed under dependencies, for Python 3.14 on 64-bit Windows, computed
from the INSTALLED copies on this machine (their METADATA). NO NETWORK: this tool makes no request to any index; it reads
files already on this machine and executes no package code.

Verbs:
  closure --target cp314-win_amd64 [--requirements <file>] [--site-packages <dir> ...] [--out <json>] [--from-file <json>]
        Start from the installable lines of requirements.txt and follow Requires-Dist through the installed copies, with
        markers evaluated for the TARGET (python_version 3.14, python_full_version 3.14.7, sys_platform win32,
        platform_system Windows, platform_machine AMD64, os_name nt, implementation_name cpython), extras followed only
        where a line or a parent asks for them, to a fixed point. Saves the JSON; the LAST line is
        INTAKE-CLOSURE target=... lines=... closure=... ok=...
        --from-file re-prints the last line of a saved JSON (the bounded form).
  explain <name> [--from-file <json>]   the chain of parents that brings a package in.
  fetchlist [--from-file <closure json>] [--assessment <md>] [--out <json>] [--md <md>]
        The closure members whose installed copy is compiled for another Python only, with the exact wheel FILE NAME each
        would need for the target, marked APPROVED / NOT-YET-APPROVED / NEW-REQUEST against the CRO's assessment of 30.
        Whether any such file exists on the index is UNREAD: nothing is asked.

Classes (exactly one per member, from org/devices/kit_python_wheels.py classify_installed, which this tool imports):
  PURE                    an installed pure-Python copy with a RECORD (can be re-packed offline)
  FITS                    an installed copy whose tags already fit the target (stable ABI, platform-only, native)
  COMPILED-OTHER-PYTHON   compiled for another Python only: a file for the target must be fetched
  NO-METADATA             no wheel metadata, an editable install, or no RECORD: no wheel can be re-packed from the copy
  UNKNOWN-NOT-INSTALLED   no installed copy on this machine: counted and named, its own dependencies are UNREAD
"""
from __future__ import annotations

import argparse
import collections
import datetime
import hashlib
import importlib.util
import json
import pathlib
import re
import site
import sys
import sysconfig

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
KW_PATH = HERE.parent / "kit_python_wheels.py"
DEFAULT_JSON = HERE / "closure_cp314_win_amd64.json"
DEFAULT_FETCH_JSON = HERE / "batch1_fetch_list.json"
DEFAULT_ASSESSMENT = (REPO / "org" / "tier1_exec" / "4.0.0_SA_CRO" / "deliverables"
                      / "PACKAGE_INTAKE_ASSESSMENT_BATCH_1_30_PACKAGES_20261007.md")
SCHEMA = "intake-closure/1"
REQUIREMENTS_NAME = "requirements.txt"
CLASSES = ("PURE", "FITS", "COMPILED-OTHER-PYTHON", "NO-METADATA", "UNKNOWN-NOT-INSTALLED")
TARGET_FULL_VERSION = "3.14.7"


def _load_kw():
    spec = importlib.util.spec_from_file_location("kit_python_wheels", KW_PATH)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["kit_python_wheels"] = mod
    spec.loader.exec_module(mod)
    return mod


kw = _load_kw()
asc = kw.asc
canon = kw.canonicalize_name


# ----------------------------------------------------------------------------------------------------------------- target

def make_target(label):
    """'cp314-win_amd64' -> the kit tool's target, with the order's python_full_version (3.14.7) for marker evaluation."""
    if "-" not in label:
        raise SystemExit("ERROR: --target must look like cp314-win_amd64")
    tag, platform = label.split("-", 1)
    target = kw.parse_target(tag, platform)
    if target["version"] == (3, 14):
        target["env"]["python_full_version"] = TARGET_FULL_VERSION
        target["env"]["implementation_version"] = TARGET_FULL_VERSION
    target["label"] = label
    return target


def marker_included(req, env, extras):
    """A Requires-Dist line is followed when its marker is true for the target with extra == '' or any requested extra."""
    if req.marker is None:
        return True
    for ex in [""] + sorted(extras):
        e = dict(env)
        e["extra"] = ex
        try:
            if req.marker.evaluate(e):
                return True
        except (kw.UndefinedComparison, kw.UndefinedEnvironmentName, TypeError, ValueError):
            continue
    return False


# ------------------------------------------------------------------------------------------------------------- installed

def default_site_dirs():
    """The running interpreter's site-packages and user site-packages, as (label, path) in sys.path order."""
    ver = "%d.%d" % sys.version_info[:2]
    out, seen = [], set()
    try:
        us = pathlib.Path(site.getusersitepackages())
        if us.is_dir():
            out.append(("<user-site-packages:%s>" % ver, us))
            seen.add(str(us.resolve()).lower())
    except (OSError, AttributeError):
        pass
    paths = sysconfig.get_paths()
    for key in ("purelib", "platlib"):
        p = pathlib.Path(paths[key])
        if p.is_dir() and str(p.resolve()).lower() not in seen:
            out.append(("<site-packages:%s>" % ver, p))
            seen.add(str(p.resolve()).lower())
    return out


def load_installed(site_dirs):
    """-> (index {norm: [ {label, info} ... ] in site_dirs order}, sources [dict])."""
    index, sources = {}, []
    for label, d in site_dirs:
        dists, unread = kw.scan_site_packages(str(d))
        sources.append({"root": label, "distributions_read": len(dists), "unreadable": unread})
        for info in dists:
            index.setdefault(canon(info["name"]), []).append({"label": label, "info": info})
    return index, sources


def classify_member(info, supported):
    """-> (class, reason, tags) for one installed copy, from the kit tool's own classifier."""
    klass, _kind, reason, tags, _fit = kw.classify_installed(info, supported)
    if klass == "PURE-INSTALLED":
        return "PURE", None, tags
    if klass == "ABI3-INSTALLED":
        return "FITS", None, tags
    if reason and reason.startswith("compiled for another Python only"):
        return "COMPILED-OTHER-PYTHON", reason, tags
    return "NO-METADATA", reason, tags


# ---------------------------------------------------------------------------------------------------------------- closure

def compute(req_lines, installed, target, supported):
    """Pure core (the test drives it). req_lines [(lineno, text)]; installed = index from load_installed.
    Returns a dict: members (list), unparsed, not_applicable, fixed_point, passes, conflicts."""
    env = target["env"]
    members = {}
    unparsed, not_applicable = [], []
    work = collections.deque()

    def get(norm, display):
        m = members.get(norm)
        if m is None:
            cands = installed.get(norm, [])
            pick = cands[0] if cands else None
            m = {"norm": norm, "name": (pick["info"]["name"] if pick else display), "pick": pick,
                 "other_copies": [{"root": c["label"], "version": c["info"]["version"]} for c in cands[1:]],
                 "line": None, "line_specifier": None, "extras": set(), "edges": {}}
            members[norm] = m
            work.append(norm)
        return m

    def touch(norm, display, extras):
        created = norm not in members
        m = get(norm, display)
        grew = not set(extras) <= m["extras"]
        m["extras"] |= set(extras)
        if grew and not created:
            work.append(norm)
        return m

    def add_edge(m, parent, req_spec, marker, extras):
        key = (parent, req_spec, marker or "", tuple(sorted(extras)))
        m["edges"][key] = {"parent": parent, "specifier": req_spec, "marker": marker, "extras": sorted(extras)}

    for lineno, text in req_lines:
        p = kw.parse_requirement(text, target)
        if not p.get("ok"):
            unparsed.append({"lineno": lineno, "text": asc(text), "error": p.get("error")})
            continue
        if not p["applicable"]:
            not_applicable.append({"lineno": lineno, "text": asc(text), "marker": p["marker"]})
            continue
        m = touch(p["norm"], p["name"], p["extras"])
        m["line"] = text
        m["line_specifier"] = p["specifier"]
        add_edge(m, REQUIREMENTS_NAME, p["specifier"], p["marker"], p["extras"])

    passes = 0
    budget = 200 * (len(req_lines) + 50) + 100000
    while work and passes < budget:
        norm = work.popleft()
        passes += 1
        m = members[norm]
        if m["pick"] is None:
            continue
        for rd in m["pick"]["info"].get("requires", []):
            try:
                r = kw.Requirement(rd)
            except (kw.InvalidRequirement, ValueError):
                continue
            if not marker_included(r, env, m["extras"]):
                continue
            child = touch(canon(r.name), r.name, r.extras)
            add_edge(child, norm, str(r.specifier), str(r.marker) if r.marker is not None else None, r.extras)
    fixed_point = not work

    conflicts = []
    out = []
    for norm in sorted(members):
        m = members[norm]
        pick = m["pick"]
        entry = {"name": m["name"], "norm": norm, "kind": "line" if m["line"] is not None else "dependency",
                 "line": asc(m["line"]) if m["line"] is not None else None, "line_specifier": m["line_specifier"],
                 "requested_extras": sorted(m["extras"]), "parents": sorted({e["parent"] for e in m["edges"].values()
                                                                            if e["parent"] != REQUIREMENTS_NAME}),
                 "edges": sorted(m["edges"].values(), key=lambda e: (e["parent"], e["specifier"], e["marker"] or "")),
                 "other_copies": m["other_copies"]}
        if pick is None:
            entry.update({"version": None, "class": "UNKNOWN-NOT-INSTALLED", "reason": "no installed copy on this machine; "
                          "its own dependencies are unread", "tags": [], "evidence": None, "specifier_conflicts": []})
        else:
            info = pick["info"]
            klass, reason, tags = classify_member(info, supported)
            confl = []
            for e in entry["edges"]:
                ok = kw.satisfies(e["specifier"], info["version"])
                if ok is False:
                    confl.append({"parent": e["parent"], "specifier": e["specifier"], "installed_version": info["version"]})
            entry.update({"version": info["version"], "class": klass, "reason": reason, "tags": tags,
                          "evidence": pick["label"] + "/" + pathlib.Path(info["path"]).name, "specifier_conflicts": confl})
            for c in confl:
                conflicts.append(dict(c, child=m["name"]))
        out.append(entry)
    # depth: shortest distance from a line of the file (a line itself is depth 0)
    by = {e["norm"]: e for e in out}
    depth = {e["norm"]: 0 for e in out if e["kind"] == "line"}
    queue = collections.deque(depth)
    children = collections.defaultdict(list)
    for e in out:
        for par in e["parents"]:
            children[par].append(e["norm"])
    while queue:
        cur = queue.popleft()
        for ch in children.get(cur, []):
            if ch not in depth:
                depth[ch] = depth[cur] + 1
                queue.append(ch)
    for e in out:
        e["depth"] = depth.get(e["norm"])
    return {"members": out, "unparsed": unparsed, "not_applicable": not_applicable, "fixed_point": fixed_point,
            "passes": passes, "conflicts": conflicts, "by_norm": by}


def counts_of(members):
    c = {k: 0 for k in CLASSES}
    for m in members:
        c[m["class"]] = c.get(m["class"], 0) + 1
    return c


def last_line(data):
    members = data["members"]
    c = counts_of(members)
    lines = data["requirements_file"]["installable_lines"]
    added = sum(1 for m in members if m["kind"] != "line")
    needs = c["COMPILED-OTHER-PYTHON"] + c["NO-METADATA"]
    one_class = all(m["class"] in CLASSES for m in members)
    ok = bool(data["fixed_point"]) and one_class and not data.get("unparsed")
    line = ("INTAKE-CLOSURE target=%s lines=%d closure=%d dependencies_added=%d pure=%d fits=%d needs_fetch=%d "
            "unknown_not_installed=%d specifier_conflicts=%d fixed_point=%s ok=%s"
            % (data["target"]["label"], lines, len(members), added, c["PURE"], c["FITS"], needs,
               c["UNKNOWN-NOT-INSTALLED"], len(data["conflicts"]), bool(data["fixed_point"]), ok))
    return line, ok


# ------------------------------------------------------------------------------------------------------------- the verbs

def cmd_closure(args):
    if args.from_file:
        data = json.loads(pathlib.Path(args.from_file).read_text(encoding="utf-8"))
        line, ok = last_line(data)
        print("(re-printed from %s; saved %s)" % (asc(pathlib.Path(args.from_file).name), data.get("generated_utc", "?")))
        print(line)
        return 0 if ok else 1
    target = make_target(args.target)
    supported = kw.supported_tags(target)
    req_path = pathlib.Path(args.requirements) if args.requirements else REPO / REQUIREMENTS_NAME
    req_lines, options, physical = kw.read_requirement_lines(req_path)
    site_dirs = [("<test-site:%d>" % i, pathlib.Path(d)) for i, d in enumerate(args.site_packages or [], 1)] \
        or default_site_dirs()
    installed, sources = load_installed(site_dirs)
    res = compute(req_lines, installed, target, supported)
    members = res["members"]
    data = {
        "schema": SCHEMA,
        "claim": "measured: a read of the installed copies' METADATA on this machine; no request to any index was made; "
                 "no package code was executed",
        "generated_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "target": {"label": target["label"], "python_tag": target["python_tag"], "platform": target["platform"],
                   "marker_environment": {k: v for k, v in sorted(target["env"].items()) if k != "extra" and v},
                   "tag_logic": "packaging.tags " + __import__("packaging").__version__, "supported_tag_count": len(supported)},
        "running_python": "%d.%d.%d" % sys.version_info[:3],
        "requirements_file": {"name": req_path.name, "physical_lines": physical, "installable_lines": len(req_lines),
                              "option_lines": len(options), "sha256": hashlib.sha256(req_path.read_bytes()).hexdigest()},
        "installed_sources": sources,
        "not_applicable_lines": res["not_applicable"],
        "unparsed": res["unparsed"],
        "fixed_point": res["fixed_point"],
        "passes": res["passes"],
        "counts": counts_of(members),
        "conflicts": res["conflicts"],
        "unknown_not_installed": [m["name"] for m in members if m["class"] == "UNKNOWN-NOT-INSTALLED"],
        "members": members,
    }
    data["last_line"], ok = last_line(data)
    print("Target %s: Python %s markers; %d supported tags; requirements: %d physical, %d installable, %d option lines"
          % (target["label"], TARGET_FULL_VERSION, len(supported), physical, len(req_lines), len(options)))
    print("Installed sources: " + asc(json.dumps(sources)))
    print("%-28s %-14s %-5s %-23s %-5s %s" % ("member", "installed", "kind", "class", "depth", "parents"))
    for m in members:
        print("%-28s %-14s %-5s %-23s %-5s %s" % (asc(m["name"])[:28], asc(m["version"] or "-")[:14], m["kind"][:5],
                                                  m["class"], m["depth"] if m["depth"] is not None else "-",
                                                  asc(",".join(m["parents"]))[:90]))
    for c in res["conflicts"]:
        print("SPECIFIER-CONFLICT child=%s installed=%s parent=%s specifier=%s"
              % (asc(c["child"]), c["installed_version"], asc(c["parent"]), asc(c["specifier"])))
    for n in data["unknown_not_installed"]:
        print("UNKNOWN-NOT-INSTALLED " + asc(n))
    text = json.dumps(data, indent=1, sort_keys=True, ensure_ascii=True) + "\n"
    leaks = kw.scrub_check(text)
    if leaks:
        print("ERROR: the result would bake a user path or name into the saved file (%s); not written" % leaks)
        return 2
    out = pathlib.Path(args.out) if args.out else DEFAULT_JSON
    out.write_text(text, encoding="ascii")
    print("Wrote %s (%d bytes)" % (out.name, len(text)))
    print(data["last_line"])
    return 0 if ok else 1


def cmd_explain(args):
    src = pathlib.Path(args.from_file) if args.from_file else DEFAULT_JSON
    data = json.loads(src.read_text(encoding="utf-8"))
    by = {m["norm"]: m for m in data["members"]}
    want = canon(args.name)
    if want not in by:
        print("NOT-IN-CLOSURE %s (%d members)" % (asc(args.name), len(by)))
        return 1
    m = by[want]
    print("%s %s: %s, class %s, depth %s" % (m["name"], m["version"] or "-", m["kind"], m["class"], m["depth"]))
    if m["kind"] == "line":
        print("  a LINE of %s: %s" % (data["requirements_file"]["name"], m["line"]))
    # shortest chain from a line to the package, by the stored parent edges
    prev = {want: None}
    queue = collections.deque([want])
    start = None
    while queue:
        cur = queue.popleft()
        if by[cur]["kind"] == "line":
            start = cur
            break
        for par in by[cur]["parents"]:
            if par in by and par not in prev:
                prev[par] = cur
                queue.append(par)
    if start is None:
        print("  no chain from a line found")
        return 1
    chain, cur = [], start
    while cur is not None:
        chain.append(cur)
        cur = prev[cur]
    hops = []
    for i, n in enumerate(chain):
        spec = ""
        if i > 0:
            edge = [e for e in by[n]["edges"] if e["parent"] == chain[i - 1]]
            spec = " (%s)" % ("; ".join(sorted({e["specifier"] or "any" for e in edge})))
        hops.append(by[n]["name"] + spec)
    print("  chain: " + " -> ".join(hops))
    print("  all parents: " + (", ".join(m["parents"]) or "none (a line only)"))
    return 0


def wheel_name(name, version):
    """The file name stem the wheel specification gives: runs of - _ . in the name become _, case lowered; '-' in the
    version becomes _; the version is the normalised form."""
    norm_name = re.sub(r"[-_.]+", "_", name).lower()
    try:
        ver = str(kw.Version(version))
    except kw.InvalidVersion:
        ver = version
    return "%s-%s" % (norm_name, ver.replace("-", "_"))


def read_assessment(path):
    """-> {norm: {'version': v, 'rec': 'YES'|'NO', 'row': n}} for the rows of the CRO's tables; None when absent."""
    p = pathlib.Path(path)
    if not p.is_file():
        return None
    out = {}
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|\s*`([^`=]+)==([^`]+)`", line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        last = cells[-1]
        rec = "NO" if re.search(r"\bNO\b", last) else "YES" if re.search(r"\bYES\b", last) else "UNKNOWN"
        out[canon(m.group(2))] = {"version": m.group(3).strip(), "rec": rec, "row": int(m.group(1))}
    return out


def build_fetchlist(data, assessment):
    compiled, other = [], []
    for m in data["members"]:
        if m["class"] not in ("COMPILED-OTHER-PYTHON", "NO-METADATA"):
            continue
        ass = assessment.get(m["norm"]) if assessment is not None else None
        if assessment is None:
            status = "APPROVAL-UNREAD"
        elif ass is None:
            status = "NEW-REQUEST"
        elif ass["rec"] == "YES" and ass["version"] == m["version"]:
            status = "APPROVED"
        else:
            status = "NOT-YET-APPROVED"
        item = {"name": m["name"], "norm": m["norm"], "version": m["version"], "kind": m["kind"],
                "line_specifier": m["line_specifier"], "parents": m["parents"], "class": m["class"],
                "reason": m["reason"], "status": status, "installed_tags": m["tags"],
                "assessed": ass}
        if m["class"] == "COMPILED-OTHER-PYTHON":
            item["file_name"] = wheel_name(m["name"], m["version"]) + "-cp314-cp314-win_amd64.whl"
            item["file_exists_on_index"] = "UNREAD"
            compiled.append(item)
        else:
            item["file_name"] = None
            other.append(item)
    present = set(m["norm"] for m in data["members"] if m["class"] in ("COMPILED-OTHER-PYTHON", "NO-METADATA"))
    assessed_not_needed = []
    if assessment is not None:
        for n, a in sorted(assessment.items()):
            if n not in present:
                inm = [m for m in data["members"] if m["norm"] == n]
                assessed_not_needed.append({"norm": n, "assessed_version": a["version"], "rec": a["rec"],
                                            "in_closure_as": inm[0]["class"] if inm else "ABSENT-FROM-CLOSURE"})
    summary = collections.Counter(i["status"] for i in compiled)
    return {"compiled": compiled, "other_needs_copy": other, "assessed_not_needing_fetch": assessed_not_needed,
            "summary": dict(summary)}


def fetchlist_md(data, fl, assessment_path, assessment_present):
    comp = fl["compiled"]
    out = []
    w = out.append
    w("# Intake batch 1: the fetch list derived from the dependency closure")
    w("")
    w("Derived by `org/devices/intake/intake_closure.py fetchlist` from `org/devices/intake/closure_cp314_win_amd64.json`")
    w("(saved %s), %s." % (data.get("generated_utc", "?"), data["last_line"]))
    w("")
    w("**Whether any file named below exists on the index is UNREAD: nothing was asked.** Each name follows the wheel")
    w("specification's normalisation (runs of `-`, `_`, `.` in the project name become `_`, lower case; the version is the")
    w("normalised installed version) with the tag `cp314-cp314-win_amd64`. A project may publish its Python 3.14 file under a")
    w("different tag (for example a stable-ABI `cp3NN-abi3` name), or not publish one: the fetch step's own check reads the")
    w("index by exact name and is the real control. The version is the one installed on this laptop.")
    w("")
    if not assessment_present:
        w("**The CRO's assessment file was not found in this worktree: approval is UNREAD for every row.**")
    else:
        w("Approval is read from `%s` (30 names assessed; CTO msg 106363: 26 approved, and pyarrow, pyiceberg, hdbscan and "
          "kuzu not approved at their pins). A row is APPROVED only when the assessed version equals the closure's." % assessment_path)
    w("")
    s = fl["summary"]
    w("## Counts")
    w("")
    w("- Closure members whose installed copy is compiled for another Python only: **%d**" % len(comp))
    for k in ("APPROVED", "NOT-YET-APPROVED", "NEW-REQUEST", "APPROVAL-UNREAD"):
        if s.get(k):
            w("- %s: **%d**" % (k, s[k]))
    w("- Closure members that need a copy for another reason (no wheel metadata, editable, no RECORD), listed after the "
      "table: **%d**" % len(fl["other_needs_copy"]))
    w("")
    w("## The files (compiled for another Python only)")
    w("")
    w("| # | File name that would be asked for | Status | Kind | Reached through |")
    w("|---|---|---|---|---|")
    for i, c in enumerate(comp, 1):
        via = ", ".join(c["parents"]) if c["parents"] else "(a line)"
        w("| %d | `%s` | %s | %s | %s |" % (i, c["file_name"], c["status"], c["kind"], via))
    w("")
    new = [c for c in comp if c["status"] == "NEW-REQUEST"]
    nyap = [c for c in comp if c["status"] == "NOT-YET-APPROVED"]
    w("## New requests (compiled, in the closure, not among the 30 assessed; NOT approved by this cell)")
    w("")
    if new:
        for c in new:
            w("- `%s` (%s), reached through %s" % (c["name"], c["version"], ", ".join(c["parents"]) or "a line"))
    else:
        w("- none")
    w("")
    w("## Not yet approved (assessed, not approved at this pin, or assessed at another version)")
    w("")
    if nyap:
        for c in nyap:
            a = c["assessed"]
            w("- `%s` %s: assessed %s, recommendation %s" % (c["name"], c["version"], a["version"] if a else "?",
                                                           a["rec"] if a else "?"))
    else:
        w("- none")
    w("")
    w("## Needs a copy for a reason other than compiled-for-another-Python")
    w("")
    if fl["other_needs_copy"]:
        for c in fl["other_needs_copy"]:
            w("- `%s` %s (%s): %s -- %s" % (c["name"], c["version"], c["class"], c["reason"], c["status"]))
    else:
        w("- none")
    w("")
    w("## Assessed names that this closure does not list as compiled")
    w("")
    if fl["assessed_not_needing_fetch"]:
        for a in fl["assessed_not_needing_fetch"]:
            w("- `%s` assessed %s %s; in this closure: %s" % (a["norm"], a["assessed_version"], a["rec"], a["in_closure_as"]))
    else:
        w("- none")
    w("")
    return "\n".join(out) + "\n"


def cmd_fetchlist(args):
    src = pathlib.Path(args.from_file) if args.from_file else DEFAULT_JSON
    data = json.loads(src.read_text(encoding="utf-8"))
    apath = pathlib.Path(args.assessment) if args.assessment else DEFAULT_ASSESSMENT
    assessment = read_assessment(apath)
    fl = build_fetchlist(data, assessment)
    doc = {"schema": "intake-fetch-list/1", "target": data["target"]["label"], "closure_file": src.name,
           "closure_last_line": data["last_line"],
           "claim": "derived: file names follow the wheel specification; whether any file exists on the index is UNREAD",
           "assessment_read": assessment is not None, "assessed_names": len(assessment) if assessment else 0,
           "assessment_approved": sum(1 for a in (assessment or {}).values() if a["rec"] == "YES"),
           "summary": fl["summary"], "compiled": fl["compiled"], "other_needs_copy": fl["other_needs_copy"],
           "assessed_not_needing_fetch": fl["assessed_not_needing_fetch"]}
    text = json.dumps(doc, indent=1, sort_keys=True, ensure_ascii=True) + "\n"
    out = pathlib.Path(args.out) if args.out else DEFAULT_FETCH_JSON
    out.write_text(text, encoding="ascii")
    print("Wrote %s (%d bytes)" % (out.name, len(text)))
    if args.md:
        md = fetchlist_md(data, fl, "org/tier1_exec/4.0.0_SA_CRO/deliverables/" + DEFAULT_ASSESSMENT.name, assessment is not None)
        pathlib.Path(args.md).write_text(md, encoding="ascii")
        print("Wrote %s" % pathlib.Path(args.md).name)
    s = fl["summary"]
    print("INTAKE-FETCHLIST target=%s compiled=%d approved=%d not_yet_approved=%d new_requests=%d other_needs_copy=%d "
          "assessment_read=%s" % (data["target"]["label"], len(fl["compiled"]), s.get("APPROVED", 0),
                                  s.get("NOT-YET-APPROVED", 0), s.get("NEW-REQUEST", 0), len(fl["other_needs_copy"]),
                                  assessment is not None))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="verb", required=True)
    c = sub.add_parser("closure")
    c.add_argument("--target", default="cp314-win_amd64")
    c.add_argument("--requirements")
    c.add_argument("--site-packages", action="append")
    c.add_argument("--out")
    c.add_argument("--from-file")
    e = sub.add_parser("explain")
    e.add_argument("name")
    e.add_argument("--from-file")
    f = sub.add_parser("fetchlist")
    f.add_argument("--from-file")
    f.add_argument("--assessment")
    f.add_argument("--out")
    f.add_argument("--md")
    a = ap.parse_args(argv)
    if not kw.HAVE_PACKAGING and a.verb != "explain":
        print("ERROR: the packaging library is not installed here; this tool needs it")
        return 2
    return {"closure": cmd_closure, "explain": cmd_explain, "fetchlist": cmd_fetchlist}[a.verb](a)


if __name__ == "__main__":
    sys.exit(main())
