#!/usr/bin/env python3
"""seat-rules-check -- validates org/ref/SEAT_RULES.json and RUNS every probe it names.

The table lists every rule that binds a seat kind, the ONE holder of each rule (LAUNCHER = what a seat is handed
when it starts, SKILL = a skill file, GATE = a tool that refuses or flags), the place that holds it, and, for a
GATE rule, a harmless PROBE that tries the forbidden act. A rule that says "a tool refuses this" is only true if
its probe is actually refused; `exercise` is that proof.

  seat-rules-check.py validate  [--rules <file>] [--root <dir>]
  seat-rules-check.py exercise  [--rules <file>] [--root <dir>]

The last line of `exercise`:
  SEAT-RULES rules=<n> gate=<g> skill=<s> launcher=<l> pairs_covered=<c>/24 probes_pass=<p> probes_pending=<q>
             probes_fail=<f> probes_unread=<u> needs_andrew=<a> ok=<True|False>
(`probes_*` count single probe RUNS: one probe over four serials is four runs.)

Four outcomes of a probe run, none of them guessed:
  PASS     the command finished and its output showed the refusal;
  FAIL     the command FINISHED and its output did not show the refusal (or showed the forbidden text);
  UNREAD   the command did not finish within its bound, even on one retry run alone: nothing is known about whether
           the rule refused, so it is neither a pass nor a failure of the rule;
  PENDING  the tool is built by another cell and is not here yet.
`ok=True` needs no failure, no UNREAD and no PENDING.

Timing. A hook is a bash script that spawns a pipeline of processes per simple command, and each spawn costs
0.3 to 0.4 s on this class of box, so one run of .tools/hooks/never-rules-gate.sh is 5 s idle and about 16 s at 85%
processor load (measured). Probes of ONE hook script therefore run one after another (never in parallel with each
other); different mechanisms run in parallel. The bound is per mechanism: BOUND_HOOK for a .sh hook, BOUND_OTHER for
anything else, or a probe's own `bound` key. A probe that hits its bound is killed as a tree and, after every other
probe has finished (so it runs alone), is run ONCE more with the same bound before it is called UNREAD.

Probe forms (all harmless by construction; none pushes, commits, merges, applies, sends or starts a seat):
  - a hook script fed a JSON stand-in of the tool call on standard input (the form .tools/hooks/tests/ uses),
    with OPAL_AGENT_SERIAL set for that one process, run in a temporary directory that holds a scratch git repo
    on the named branch (so the hook sees a shared branch without touching the real tree);
  - owned-paths-validate.py --check-agent, which only reads;
  - a gate script's own self-test, or one pure function of it called through the `_call` helper below.
A probe whose tool does not exist yet AND whose rule says built_by another cell is PENDING, not a pass, not a failure.

Key set: THE SEAM's rule keys plus `source` (the quoted sentence of the owner's record that makes it a rule).
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import importlib.util
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import zlib

SELF = os.path.abspath(__file__).replace("\\", "/")
DEFAULT_ROOT = os.path.dirname(os.path.dirname(SELF))

KINDS = ["MSTR", "CTO", "COO", "CVO", "CRO", "CLOUDOPS", "TIER2", "WORKER"]
AREAS = ["GITOPS", "AWSDEVOPS", "WORKFLOW"]
HOLDERS = ["LAUNCHER", "SKILL", "GATE"]
TOP_KEYS = {"schema", "rules"}
RULE_KEYS = {"id", "area", "kinds", "rule", "holder", "mechanism", "probe", "built_by", "needs_andrew", "question",
             "source"}
REQUIRED_KEYS = {"id", "area", "kinds", "rule", "holder", "mechanism", "probe", "built_by", "needs_andrew"}
PROBE_KEYS = {"label", "tool", "argv", "stdin", "stdin_json", "env", "git_branch", "files", "serials", "expect",
              "expect_rc", "forbid", "stands_for_all_kinds", "bound"}
# The launcher is .tools/ajb.ps1; org/ref/SEAT_ROLES.json is the file CT-s-1 writes for it to hand a seat; a worker's
# own start text is its subagent definition (see the row filed with this table).
LAUNCHER_PATHS = {"org/ref/SEAT_ROLES.json", ".tools/ajb.ps1", ".claude/agents/worker.md"}
SKILL_RE = re.compile(r"^\.claude/skills/[A-Za-z0-9_-]+/SKILL\.md$")
ID_RE = re.compile(r"^R-(GITOPS|AWSDEVOPS|WORKFLOW)-[0-9]+$")
BUILT_BY_RE = re.compile(r"^(existing|CT-[a-z]-[0-9]+)$")
# Local classification of a serial to a kind, derived from the launcher's regular expressions (.tools/ajb.ps1
# Get-AgentLoopDirective). Used ONLY to check that a probe's serials cover the kinds its rule claims; the readers of
# the roles file resolve kinds through lib/seat_roles.py kind_of (CT-s-1).
KIND_PATTERNS = [
    ("MSTR", re.compile(r"^0\.0\.0_AB_MSTR(~[A-Za-z0-9]+)?$")),
    ("CTO", re.compile(r"^1\.0\.0_SA_CTO(~[A-Za-z0-9]+)?$")),
    ("COO", re.compile(r"^2\.0\.0_SA_COO(~[A-Za-z0-9]+)?$")),
    ("CVO", re.compile(r"^3\.0\.0_SA_CVO(~[A-Za-z0-9]+)?$")),
    ("CRO", re.compile(r"^4\.0\.0_SA_CRO(~[A-Za-z0-9]+)?$")),
    ("WORKER", re.compile(r"^0\.9\.0_WK_[A-Za-z0-9_]+~[0-9]+$")),
    ("CLOUDOPS", re.compile(r"^0\.[0-9]+\.[0-9]+_AE_Cloud(Ops|Comp)(~[A-Za-z0-9]+)?$")),
    ("TIER2", re.compile(r"^0\.[0-9]+\.[0-9]+_(DS|AE|DE|DT|RD)_[A-Za-z0-9]+(~[A-Za-z0-9]+)?$")),
]
# Per-probe bounds in seconds. A hook run was measured at about 16 s alone at 85% processor load (5 s idle):
# 90 s is a margin of about 5x on the loaded figure. Everything else is a python tool or a self-test: 60 s.
BOUND_HOOK = 90
BOUND_OTHER = 60


def probe_bound(probe):
    own = probe.get("bound")
    if isinstance(own, (int, float)) and not isinstance(own, bool) and own > 0:
        return own
    return BOUND_HOOK if str(probe.get("tool", "")).endswith(".sh") else BOUND_OTHER


def kind_of_local(serial):
    for kind, rx in KIND_PATTERNS:
        if rx.match(serial):
            return kind
    return "UNKNOWN"


# --------------------------------------------------------------------------------------------- validate
def _is_ascii(text):
    return all(ord(ch) < 128 for ch in text)


def validate(doc, root):
    """Return (problems, stats). stats: pairs (set), pending_paths (list of rule ids whose mechanism file is built by
    another cell and is not here yet)."""
    problems = []
    pairs = set()
    pending_paths = []
    if not isinstance(doc, dict):
        return ["table is not a JSON object"], {"pairs": pairs, "pending_paths": pending_paths}
    extra = sorted(set(doc) - TOP_KEYS)
    if extra:
        problems.append("unknown top-level key(s): %s" % ", ".join(extra))
    if doc.get("schema") != "seat-rules/1":
        problems.append("schema must be 'seat-rules/1'")
    rules = doc.get("rules")
    if not isinstance(rules, list) or not rules:
        problems.append("rules must be a non-empty list")
        return problems, {"pairs": pairs, "pending_paths": pending_paths}
    seen = {}
    for idx, rule in enumerate(rules):
        where = "rule[%d]" % idx
        if not isinstance(rule, dict):
            problems.append("%s is not an object" % where)
            continue
        rid = rule.get("id")
        where = str(rid) if isinstance(rid, str) else where
        unknown = sorted(set(rule) - RULE_KEYS)
        if unknown:
            problems.append("%s: unknown key(s) %s (closed key set)" % (where, ", ".join(unknown)))
        missing = sorted(REQUIRED_KEYS - set(rule))
        if missing:
            problems.append("%s: missing key(s) %s" % (where, ", ".join(missing)))
            continue
        if not isinstance(rid, str) or not ID_RE.match(rid):
            problems.append("%s: id must look like R-<GITOPS|AWSDEVOPS|WORKFLOW>-<n>" % where)
        elif rid in seen:
            problems.append("%s: id used twice (a rule with two entries has two holders; one rule, one holder)" % where)
        else:
            seen[rid] = rule
        area = rule["area"]
        if area not in AREAS:
            problems.append("%s: area %r not one of %s" % (where, area, AREAS))
        elif isinstance(rid, str) and ID_RE.match(rid) and not rid.startswith("R-%s-" % area):
            problems.append("%s: id prefix does not match area %s" % (where, area))
        kinds = rule["kinds"]
        if not isinstance(kinds, list) or not kinds or len(set(kinds)) != len(kinds) \
                or any(k not in KINDS for k in kinds):
            problems.append("%s: kinds must be a non-empty list of distinct names from %s" % (where, KINDS))
            kinds = []
        if not isinstance(rule["rule"], str) or not rule["rule"].strip():
            problems.append("%s: rule sentence is empty" % where)
        holder = rule["holder"]
        if not isinstance(holder, str):
            n = len(holder) if isinstance(holder, list) else 0
            problems.append("%s: exactly one holder required; found %s" % (where, "%d holders" % n if n else "a non-string"))
            holder = None
        elif holder not in HOLDERS:
            problems.append("%s: holder %r is not exactly one of %s" % (where, holder, HOLDERS))
            holder = None
        if not isinstance(rule["needs_andrew"], bool):
            problems.append("%s: needs_andrew must be true or false" % where)
        elif rule["needs_andrew"]:
            if not isinstance(rule.get("question"), str) or not rule["question"].strip():
                problems.append("%s: needs_andrew is true and no question is given" % where)
        elif rule.get("question") not in (None, ""):
            problems.append("%s: a question is given but needs_andrew is false" % where)
        built_by = rule["built_by"]
        if not isinstance(built_by, str) or not BUILT_BY_RE.match(built_by):
            problems.append("%s: built_by must be 'existing' or a cell id such as CT-s-3" % where)
            built_by = "existing"
        mech = rule["mechanism"]
        mpath = None
        if not isinstance(mech, dict) or set(mech) != {"path", "entry"} \
                or not isinstance(mech.get("path"), str) or not isinstance(mech.get("entry"), str) \
                or not mech["path"].strip() or not mech["entry"].strip():
            problems.append("%s: mechanism must be {path, entry}, both non-empty text" % where)
        else:
            mpath = mech["path"]
            if mpath.startswith("/") or ".." in mpath.split("/") or re.match(r"^[A-Za-z]:", mpath):
                problems.append("%s: mechanism.path %r is not repo-relative" % (where, mpath))
                mpath = None
        if mpath is not None:
            full = os.path.join(root, mpath)
            if os.path.isfile(full):
                with open(full, "rb") as fh:
                    text = fh.read().decode("utf-8", errors="replace")
                if mech["entry"] not in text:
                    problems.append("%s: entry %r does not occur in %s" % (where, mech["entry"], mpath))
            elif built_by != "existing":
                pending_paths.append(where)
            else:
                problems.append("%s: mechanism.path %s does not exist" % (where, mpath))
            if holder == "LAUNCHER" and mpath not in LAUNCHER_PATHS:
                problems.append("%s: a LAUNCHER rule names org/ref/SEAT_ROLES.json or the launcher, not %s" % (where, mpath))
            if holder == "SKILL" and not SKILL_RE.match(mpath):
                problems.append("%s: a SKILL rule names a file under .claude/skills/, not %s" % (where, mpath))
            if holder == "GATE" and (mpath in LAUNCHER_PATHS or mpath.startswith(".claude/skills/")):
                problems.append("%s: a GATE rule names a tool, not %s" % (where, mpath))
        probe = rule["probe"]
        if holder == "GATE":
            if probe is None or probe == [] or probe == {}:
                problems.append("%s: a GATE rule has no probe" % where)
            else:
                plist = probe if isinstance(probe, list) else [probe]
                for pidx, pr in enumerate(plist):
                    problems.extend(_validate_probe(where, pidx, pr, kinds))
        elif holder is not None and probe is not None:
            problems.append("%s: only a GATE rule carries a probe" % where)
        if "source" in rule and (not isinstance(rule["source"], str) or not rule["source"].strip()):
            problems.append("%s: source, when present, is a quoted sentence" % where)
        for text_value in (rule.get("rule"), rule.get("question"), rule.get("source")):
            if isinstance(text_value, str) and not _is_ascii(text_value):
                problems.append("%s: non-ASCII text" % where)
                break
        if area in AREAS:
            for kind in kinds:
                pairs.add((kind, area))
    missing_pairs = [(k, a) for a in AREAS for k in KINDS if (k, a) not in pairs]
    for kind, area in missing_pairs:
        problems.append("PAIR-MISSING %s x %s: no rule" % (kind, area))
    return problems, {"pairs": pairs, "pending_paths": pending_paths}


def _validate_probe(where, pidx, pr, kinds):
    out = []
    tag = "%s probe[%d]" % (where, pidx)
    if not isinstance(pr, dict):
        return ["%s: not an object" % tag]
    unknown = sorted(set(pr) - PROBE_KEYS)
    if unknown:
        out.append("%s: unknown key(s) %s" % (tag, ", ".join(unknown)))
    if not isinstance(pr.get("tool"), str) or not pr.get("tool"):
        out.append("%s: tool (the repo-relative file the probe exercises) is required" % tag)
    argv = pr.get("argv")
    if not isinstance(argv, list) or not argv or any(not isinstance(a, str) for a in argv):
        out.append("%s: argv must be a non-empty list of text" % tag)
    for key in ("expect", "forbid"):
        if key in pr and pr[key] is not None:
            try:
                re.compile(pr[key])
            except (re.error, TypeError):
                out.append("%s: %s is not a regular expression" % (tag, key))
    if not isinstance(pr.get("expect"), str) or not pr.get("expect"):
        out.append("%s: expect (the refusal text, as a regular expression) is required" % tag)
    rc = pr.get("expect_rc")
    if rc is not None and not isinstance(rc, int):
        out.append("%s: expect_rc must be a number or null" % tag)
    bound = pr.get("bound")
    if bound is not None and (isinstance(bound, bool) or not isinstance(bound, (int, float)) or bound <= 0):
        out.append("%s: bound must be a positive number of seconds" % tag)
    serials = pr.get("serials")
    if serials is not None:
        if not isinstance(serials, list) or not serials or any(not isinstance(s, str) for s in serials):
            out.append("%s: serials must be a non-empty list" % tag)
        else:
            covered = {kind_of_local(s) for s in serials}
            if "UNKNOWN" in covered:
                out.append("%s: a serial matches no kind" % tag)
            if not pr.get("stands_for_all_kinds"):
                lacking = [k for k in kinds if k not in covered]
                if lacking:
                    out.append("%s: no serial of kind %s (the rule binds it; add one or say stands_for_all_kinds)"
                               % (tag, ", ".join(lacking)))
    elif len(kinds) > 1 and not pr.get("stands_for_all_kinds"):
        out.append("%s: the rule binds %d kinds and the probe names no serials (add serials, or stands_for_all_kinds)"
                   % (tag, len(kinds)))
    return out


# --------------------------------------------------------------------------------------------- probe run
def _subst(obj, mapping):
    if isinstance(obj, str):
        for key, val in mapping.items():
            obj = obj.replace(key, val)
        return obj
    if isinstance(obj, list):
        return [_subst(x, mapping) for x in obj]
    if isinstance(obj, dict):
        return {k: _subst(v, mapping) for k, v in obj.items()}
    return obj


def _rmtree(path):
    def onerror(func, p, _exc):
        try:
            os.chmod(p, stat.S_IWRITE)
            func(p)
        except OSError:
            pass
    shutil.rmtree(path, onerror=onerror)


def _scratch_repo(path, branch):
    """A scratch git repo in the probe's own temp dir whose HEAD is the named branch (so a hook sees a shared branch
    without touching the real tree). Written by hand (two loose objects, HEAD, one ref) so no git process is spawned:
    on this class of box every spawn costs seconds and the probes share a 120 s bound."""
    def loose(kind, body):
        raw = ("%s %d" % (kind, len(body))).encode("ascii") + b"\x00" + body
        sha = hashlib.sha1(raw).hexdigest()
        obj_dir = os.path.join(path, ".git", "objects", sha[:2])
        os.makedirs(obj_dir, exist_ok=True)
        with open(os.path.join(obj_dir, sha[2:]), "wb") as fh:
            fh.write(zlib.compress(raw))
        return sha

    def put(rel, text):
        with open(os.path.join(path, ".git", *rel), "w", newline="\n") as fh:
            fh.write(text)

    os.makedirs(os.path.join(path, ".git", "refs", "heads"), exist_ok=True)
    tree = loose("tree", b"")
    body = "tree %s\nauthor t <t@t> 0 +0000\ncommitter t <t@t> 0 +0000\n\nscratch\n" % tree
    commit = loose("commit", body.encode("ascii"))
    put(["HEAD"], "ref: refs/heads/%s\n" % branch)
    put(["refs", "heads", branch], commit + "\n")
    put(["config"], "[core]\n\trepositoryformatversion = 0\n\tbare = false\n")


def _bash():
    sys.path.insert(0, os.path.join(DEFAULT_ROOT, ".tools"))
    try:
        from git_bash_resolver import git_bash  # type: ignore
        found = git_bash()
        if found:
            return found
    except Exception:  # noqa: BLE001
        pass
    return shutil.which("bash") or "bash"


def _kill_tree(proc):
    """Kill a timed-out probe AND its children (a hook is a bash that spawns more; killing only the parent leaves
    them holding the files open)."""
    try:
        if os.name == "nt":
            subprocess.run(["taskkill", "/T", "/F", "/PID", str(proc.pid)], capture_output=True, timeout=30)
        else:
            proc.kill()
    except Exception:  # noqa: BLE001
        pass
    try:
        proc.wait(timeout=10)
    except Exception:  # noqa: BLE001
        pass


def run_probe(rule, probe, serial, root, bash_path):
    """One probe run. Returns dict(status PASS|PENDING|FAIL|UNREAD, detail). UNREAD = the command did not finish
    within its bound; FAIL = it finished and the output did not show the refusal."""
    bound = probe_bound(probe)
    tool_path = os.path.join(root, probe["tool"])
    if not os.path.exists(tool_path):
        if rule["built_by"] != "existing":
            return {"status": "PENDING", "detail": "tool %s not built yet (built_by %s)" % (probe["tool"], rule["built_by"])}
        return {"status": "FAIL", "detail": "tool %s does not exist and the rule says it is existing" % probe["tool"]}
    tmp = tempfile.mkdtemp(prefix="seatrules_")
    try:
        cwd = tmp.replace("\\", "/")
        mapping = {"{ROOT}": root, "{CWD}": cwd, "{SERIAL}": serial or "", "{PY}": sys.executable.replace("\\", "/"),
                   "{SELF}": SELF}
        if probe.get("git_branch"):
            _scratch_repo(tmp, probe["git_branch"])
        for rel, content in (probe.get("files") or {}).items():
            dest = os.path.join(tmp, rel)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "w", encoding="utf-8", newline="") as fh:
                fh.write(_subst(content, mapping))
        argv = _subst(probe["argv"], mapping)
        if argv[0] == "bash":
            argv[0] = bash_path
        env = dict(os.environ)
        env.pop("CLAUDE_CODE_SESSION_ID", None)
        env["CLAUDE_PROJECT_DIR"] = root
        env["OPAL_AGENT_SERIAL"] = serial or ""
        env["NEVER_GATE_AUDIT"] = cwd + "/audit.log"
        env.update(_subst(probe.get("env") or {}, mapping))
        if probe.get("stdin_json") is not None:
            stdin = json.dumps(_subst(probe["stdin_json"], mapping))
        else:
            stdin = _subst(probe.get("stdin") or "", mapping)
        out_path = os.path.join(tmp, ".probe_out.txt")
        in_path = os.path.join(tmp, ".probe_in.txt")
        with open(in_path, "w", encoding="utf-8", newline="") as fh:
            fh.write(stdin)
        try:
            with open(in_path, "rb") as fin, open(out_path, "wb") as fout:
                proc = subprocess.Popen(argv, stdin=fin, stdout=fout, stderr=subprocess.STDOUT, cwd=tmp, env=env)
                try:
                    proc.wait(timeout=bound)
                except subprocess.TimeoutExpired:
                    _kill_tree(proc)
                    return {"status": "UNREAD", "detail": "did not finish: timeout after %gs" % bound}
        except OSError as exc:
            return {"status": "FAIL", "detail": "could not run: %s" % exc}
        with open(out_path, "rb") as fh:
            out = fh.read().decode("utf-8", errors="replace")
        proc_rc = proc.returncode
        want_rc = probe.get("expect_rc")
        hit = re.search(probe["expect"], out, re.S)
        if not hit:
            return {"status": "FAIL", "detail": "expected /%s/ not in output rc=%d: %s" % (
                probe["expect"], proc_rc, _squash(out))}
        if probe.get("forbid") and re.search(probe["forbid"], out, re.S):
            return {"status": "FAIL", "detail": "forbidden /%s/ present: %s" % (probe["forbid"], _squash(out))}
        if want_rc is not None and proc_rc != want_rc:
            return {"status": "FAIL", "detail": "rc=%d, expected %d: %s" % (proc_rc, want_rc, _squash(out))}
        return {"status": "PASS", "detail": "rc=%d saw: %s" % (proc_rc, _squash(out[max(0, hit.start() - 20):hit.end() + 60]))}
    except Exception as exc:  # noqa: BLE001
        return {"status": "FAIL", "detail": "probe error: %s" % exc}
    finally:
        _rmtree(tmp)


def _squash(text, limit=170):
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[:limit] + "..."


def _run_group(group, root, bash_path):
    """Run one group's jobs one after another. A group is every probe of one hook script, or one probe run."""
    out = []
    for rule, probe, serial, _label in group:
        out.append(run_probe(rule, probe, serial, root, bash_path))
    return out


def _groups(jobs):
    """Probes of one .sh hook form one sequential group; every other job is a group of its own."""
    groups = []
    by_tool = {}
    for idx, job in enumerate(jobs):
        tool = str(job[1].get("tool", ""))
        if tool.endswith(".sh"):
            if tool not in by_tool:
                by_tool[tool] = []
                groups.append(by_tool[tool])
            by_tool[tool].append((idx,) + job)
        else:
            groups.append([(idx,) + job])
    return groups


def exercise(doc, root, workers=16, out=None):
    """Run every probe of every GATE rule. Returns (results, elapsed). Each result: dict(rule, label, serial,
    status, detail). Probes of one hook run in sequence; a probe that hit its bound is run once more alone."""
    bash_path = _bash()
    jobs = []
    for rule in doc.get("rules", []):
        if rule.get("holder") != "GATE":
            continue
        probes = rule["probe"] if isinstance(rule["probe"], list) else [rule["probe"]]
        for pidx, probe in enumerate(probes):
            label = probe.get("label") or "probe%d" % pidx
            for serial in (probe.get("serials") or [None]):
                jobs.append((rule, probe, serial, label))
    started = time.time()
    results = [None] * len(jobs)
    groups = _groups(jobs)
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futs = [pool.submit(_run_group, [g[1:] for g in group], root, bash_path) for group in groups]
        for group, fut in zip(groups, futs):
            for item, res in zip(group, fut.result()):
                results[item[0]] = res
    # The retry: every probe that hit its bound runs ONCE more, alone, now that nothing else is running.
    for idx, res in enumerate(results):
        if res["status"] != "UNREAD":
            continue
        rule, probe, serial, _label = jobs[idx]
        first = res["detail"]
        again = run_probe(rule, probe, serial, root, bash_path)
        if again["status"] == "UNREAD":
            again["detail"] = "%s; retried once alone: %s" % (first, again["detail"])
        else:
            again["detail"] = "(first run: %s; retried once alone) %s" % (first, again["detail"])
        results[idx] = again
    for res, (rule, _probe, serial, label) in zip(results, jobs):
        res.update({"rule": rule["id"], "label": label, "serial": serial or "-"})
    return results, time.time() - started


# --------------------------------------------------------------------------------------------- summary
def counts(doc):
    rules = doc.get("rules", []) if isinstance(doc, dict) else []
    by_holder = {h: sum(1 for r in rules if isinstance(r, dict) and r.get("holder") == h) for h in HOLDERS}
    needs = sum(1 for r in rules if isinstance(r, dict) and r.get("needs_andrew") is True)
    return len(rules), by_holder, needs


def summary_line(doc, stats, problems, results):
    n, by_holder, needs = counts(doc)
    p_pass = sum(1 for r in results if r["status"] == "PASS")
    p_pend = sum(1 for r in results if r["status"] == "PENDING")
    p_fail = sum(1 for r in results if r["status"] == "FAIL")
    p_unread = sum(1 for r in results if r["status"] == "UNREAD")
    covered = len(stats["pairs"])
    ok = (not problems) and p_fail == 0 and p_unread == 0 and p_pend == 0 and covered == 24
    line = ("SEAT-RULES rules=%d gate=%d skill=%d launcher=%d pairs_covered=%d/24 probes_pass=%d probes_pending=%d "
            "probes_fail=%d probes_unread=%d needs_andrew=%d ok=%s" % (
                n, by_holder["GATE"], by_holder["SKILL"], by_holder["LAUNCHER"], covered, p_pass, p_pend, p_fail,
                p_unread, needs, ok))
    return line, ok


def load_table(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    try:
        raw.decode("ascii")
    except UnicodeDecodeError:
        return None, ["%s holds non-ASCII bytes" % path]
    try:
        return json.loads(raw.decode("ascii")), []
    except ValueError as exc:
        return None, ["%s is not valid JSON: %s" % (path, exc)]


def cmd_validate(rules_path, root):
    doc, errs = load_table(rules_path)
    if doc is None:
        for e in errs:
            print("PROBLEM: " + e)
        print("SEAT-RULES-VALIDATE problems=%d ok=False" % len(errs))
        return 1
    problems, stats = validate(doc, root)
    for pr in problems:
        print("PROBLEM: " + pr)
    for rid in stats["pending_paths"]:
        print("NOTE: %s mechanism file is built by another cell and is not in this tree yet" % rid)
    print("SEAT-RULES-VALIDATE rules=%d pairs_covered=%d/24 problems=%d ok=%s" % (
        counts(doc)[0], len(stats["pairs"]), len(problems), not problems))
    return 0 if not problems else 1


def cmd_exercise(rules_path, root):
    doc, errs = load_table(rules_path)
    if doc is None:
        for e in errs:
            print("PROBLEM: " + e)
        print("SEAT-RULES rules=0 gate=0 skill=0 launcher=0 pairs_covered=0/24 probes_pass=0 probes_pending=0 "
              "probes_fail=0 probes_unread=0 needs_andrew=0 ok=False")
        return 1
    problems, stats = validate(doc, root)
    for pr in problems:
        print("PROBLEM: " + pr)
    results, elapsed = exercise(doc, root)
    for r in results:
        print("PROBE %-14s %-8s %-30s %s" % (r["rule"], r["status"], r["serial"], r["detail"]))
    print("EXERCISE elapsed=%.1fs probes=%d workers=16 hook_bound=%ds other_bound=%ds" % (
        elapsed, len(results), BOUND_HOOK, BOUND_OTHER))
    line, ok = summary_line(doc, stats, problems, results)
    print(line)
    return 0 if ok else 1


# --------------------------------------------------------------------------------------------- helpers a probe calls
def cmd_call(file_path, func, jargs):
    """Import one gate script by path and print the return value of one PURE function of it."""
    file_path = os.path.abspath(file_path)
    sys.path.insert(0, os.path.dirname(file_path))
    spec = importlib.util.spec_from_file_location("seatrules_probe_target", file_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    result = getattr(mod, func)(*json.loads(jargs))
    print("RESULT: " + json.dumps(result, default=str))
    return 0


def cmd_policy_deny(file_path, sid, action):
    """Read an IAM policy file: print whether statement <sid> is an explicit Deny that names <action>."""
    with open(file_path, "rb") as fh:
        pol = json.loads(fh.read().decode("utf-8"))
    for stmt in pol.get("Statement", []):
        if stmt.get("Sid") == sid and stmt.get("Effect") == "Deny":
            acts = stmt.get("Action")
            acts = [acts] if isinstance(acts, str) else list(acts or [])
            if action in acts:
                print("POLICY-DENY sid=%s action=%s effect=Deny (declared in the file; live apply is not read)" % (sid, action))
                return 0
    print("POLICY-ABSENT sid=%s action=%s" % (sid, action))
    return 1


def main(argv):
    ap = argparse.ArgumentParser(prog="seat-rules-check.py")
    sub = ap.add_subparsers(dest="cmd")
    for name in ("validate", "exercise"):
        sp = sub.add_parser(name)
        sp.add_argument("--rules", default=None)
        sp.add_argument("--root", default=None)
    sp = sub.add_parser("_call")
    sp.add_argument("file")
    sp.add_argument("func")
    sp.add_argument("jargs")
    sp = sub.add_parser("_policy_deny")
    sp.add_argument("file")
    sp.add_argument("sid")
    sp.add_argument("action")
    args = ap.parse_args(argv[1:])
    if args.cmd in ("validate", "exercise"):
        root = (args.root or DEFAULT_ROOT).replace("\\", "/")
        rules_path = args.rules or os.path.join(root, "org", "ref", "SEAT_RULES.json")
        return (cmd_validate if args.cmd == "validate" else cmd_exercise)(rules_path, root)
    if args.cmd == "_call":
        return cmd_call(args.file, args.func, args.jargs)
    if args.cmd == "_policy_deny":
        return cmd_policy_deny(args.file, args.sid, args.action)
    ap.print_usage()
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
