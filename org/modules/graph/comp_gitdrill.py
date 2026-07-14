"""
comp-gitdrill -- drill any estate node to the TIME axis of its producer (git history at vintage).

WHY (NFRA_INSTDRILL item 6, 2026-07-14, Andrew-direct). The graph tools answer "what feeds/consumes
this" (the SPACE axis). None answered "how did its PRODUCER change over time, and what did it look
like at vintage V" (the TIME axis) -- so an agent reconstructing when a served number last moved
went to raw `git log` and lost the node->file resolution the graph already holds. This closes that:
node -> producing source file(s) via the graph -> vintage-stamped commit history + `--at <ref>` to
view/diff the producer AT a vintage.

Every output line carries its commit-ish -- the "a line citation without a vintage is not a
citation" rule (CLAUDE.md 22) made mechanical. Read-only (git log / show / diff only).

Usage:
    comp-gitdrill <node|file>                  # commit history of the producing file(s)
    comp-gitdrill <node|file> --at <ref>       # show the producer AS OF a ref (blob at that vintage)
    comp-gitdrill <node|file> --at <ref> --diff # diff the producer between <ref> and HEAD
    comp-gitdrill <node|file> --limit N         # cap history (default 20)
    comp-gitdrill --json <node|file>
    comp-gitdrill --self-test                   # git log/show parity on a known-tracked file

Author: 1.0.0_SA_CTO~Z (NFRA_INSTDRILL item 6). 2026-07-14. Read-only.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.normpath(os.path.join(_HERE, "..", "..", ".."))


def _git(*args, timeout=30):
    """Run git read-only; returns (rc, stdout). Never mutates (log/show/diff/rev-parse only)."""
    try:
        p = subprocess.run(["git", "-C", _WS, *args], capture_output=True, text=True,
                           timeout=timeout, errors="replace")
        return p.returncode, (p.stdout or "")
    except Exception as e:  # noqa: BLE001
        return 1, "git error: %s" % e


def resolve_files(query: str) -> tuple[list[str], str]:
    """node-id / file-path / basename -> the producing repo file(s). Returns (files, how)."""
    q = query.strip()
    # a real path on disk?
    if os.path.exists(os.path.join(_WS, q)):
        return [q.replace("\\", "/")], "path"
    # a graph node? resolve via the trace graph's file_path.
    try:
        sys.path.insert(0, _WS)
        from org.modules.graph.trace_graph import TraceGraph  # noqa: PLC0415
        from pathlib import Path  # noqa: PLC0415
        cache = Path(_WS) / ".comp-graph" / "graph.json"
        if cache.exists():
            g = TraceGraph.load(cache)
            matches = g.find_node(q)
            files = []
            for n in matches:
                fp = getattr(n, "file_path", "")
                if fp and fp not in files:
                    files.append(fp.replace("\\", "/"))
            if files:
                return files, "graph-node(%s)" % matches[0].node_type
    except Exception:  # noqa: BLE001 -- graph optional; fall through to git pathspec
        pass
    # last resort: let git resolve a basename via --all pathspec.
    rc, out = _git("log", "--oneline", "-1", "--all", "--", "*%s*" % q, timeout=20)
    if rc == 0 and out.strip():
        rc2, files_out = _git("log", "-1", "--name-only", "--format=", "--all", "--", "*%s*" % q)
        cand = [ln.strip() for ln in files_out.splitlines() if ln.strip()]
        if cand:
            return cand[:5], "git-pathspec"
    return [], "unresolved"


def history(files: list[str], limit: int) -> list[dict]:
    out = []
    for f in files:
        rc, log = _git("log", "-n", str(limit), "--follow",
                       "--format=%h\x1f%ad\x1f%an\x1f%s", "--date=short", "--", f)
        commits = []
        for ln in log.splitlines():
            parts = ln.split("\x1f")
            if len(parts) == 4:
                commits.append({"commit": parts[0], "date": parts[1],
                                "author": parts[2], "subject": parts[3]})
        out.append({"file": f, "commits": commits})
    return out


def at_vintage(files: list[str], ref: str, do_diff: bool) -> list[dict]:
    out = []
    for f in files:
        # resolve the ref:file blob so an output line always carries WHAT vintage it is
        rc, sha = _git("rev-parse", "%s:%s" % (ref, f))
        entry = {"file": f, "ref": ref, "blob": sha.strip() if rc == 0 else None}
        if rc != 0:
            entry["error"] = "not present at %s (%s)" % (ref, sha.strip()[:80])
            out.append(entry)
            continue
        if do_diff:
            drc, diff = _git("diff", "--stat", "%s" % ref, "HEAD", "--", f)
            entry["diffstat"] = diff.strip() or "(no change between %s and HEAD)" % ref
        else:
            src_rc, content = _git("show", "%s:%s" % (ref, f))
            entry["lines"] = content.count("\n") if src_rc == 0 else None
            entry["head"] = "\n".join(content.splitlines()[:20]) if src_rc == 0 else None
        out.append(entry)
    return out


def _render(files: list[str], how: str, drill: list[dict], mode: str, ref: str = "") -> str:
    L = ["comp-gitdrill: %s  (resolved via %s -> %d file(s))" % (
        files[0] if files else "?", how, len(files))]
    if mode == "history":
        for d in drill:
            L.append("\n  %s" % d["file"])
            if not d["commits"]:
                L.append("    (no commit history -- untracked, or resolved to a non-file)")
            for c in d["commits"]:
                L.append("    %s  %s  %-22s %s" % (c["commit"], c["date"],
                                                   c["author"][:22], c["subject"][:70]))
    else:  # at vintage
        for d in drill:
            L.append("\n  %s  @ %s" % (d["file"], ref))
            if d.get("error"):
                L.append("    %s" % d["error"])
                continue
            L.append("    blob %s" % d.get("blob"))
            if "diffstat" in d:
                L.append("    diff %s..HEAD: %s" % (ref, d["diffstat"]))
            else:
                L.append("    %s lines at %s; head:" % (d.get("lines"), ref))
                for ln in (d.get("head") or "").splitlines()[:8]:
                    L.append("      | %s" % ln[:88])
    return "\n".join(L)


def _self_test() -> int:
    """git log/show parity on a KNOWN tracked file (this module itself once committed, else a
    stable repo file). Offline-ish: needs a git repo but no network."""
    results = []
    def ck(name, ok, detail=""):
        results.append(ok)
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   ({detail})" if detail else ""))

    # pick a definitely-tracked file
    probe = "CLAUDE.md"
    files, how = resolve_files(probe)
    ck("resolve.path_hit", files == ["CLAUDE.md"] and how == "path", f"{files} via {how}")

    hist = history(files, 5)
    commits = hist[0]["commits"]
    ck("history.nonempty", len(commits) >= 1, f"{len(commits)} commits")
    ck("history.every_line_has_a_vintage",
       all(c["commit"] and c["date"] for c in commits),
       "no citation without a commit-ish + date")

    # --at parity: the blob sha from rev-parse must match git's own for HEAD.
    if commits:
        av = at_vintage(files, "HEAD", do_diff=False)
        rc, direct = _git("rev-parse", "HEAD:CLAUDE.md")
        ck("at.blob_parity_with_git",
           av[0].get("blob") == direct.strip() and rc == 0,
           f"gitdrill={av[0].get('blob')} git={direct.strip()}")
        # diff HEAD..HEAD is empty (a sanity control the tool can go RED on if it ever mutated).
        avd = at_vintage(files, "HEAD", do_diff=True)
        ck("at.diff_head_head_empty", "no change" in avd[0].get("diffstat", ""),
           avd[0].get("diffstat", "")[:60])

    # a bogus node resolves to nothing, WITHOUT fabricating history.
    bf, bh = resolve_files("zzz_no_such_node_xyz")
    ck("resolve.miss_is_empty", bf == [] and bh == "unresolved", f"{bf} via {bh}")

    ok = all(results)
    print("\n" + ("OK: git log/show parity holds; every line carries a vintage" if ok
                  else "ERROR: comp-gitdrill self-test FAILED"))
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(prog="comp-gitdrill",
                                 description="drill a node to its producer's git history at vintage (read-only)")
    ap.add_argument("target", nargs="?", help="graph node id / file path / basename")
    ap.add_argument("--at", default=None, help="show the producer AS OF this git ref")
    ap.add_argument("--diff", action="store_true", help="with --at: diffstat <ref>..HEAD")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(errors="replace")
        except Exception:  # noqa: BLE001
            pass

    if args.self_test:
        return _self_test()
    if not args.target:
        ap.print_help()
        return 2

    files, how = resolve_files(args.target)
    if not files:
        print("NOT-RESOLVED: '%s' is neither a repo path, a graph node with a file_path, nor a "
              "git-tracked basename. (comp-gitdrill drills a PRODUCER file's history; a pure S3 "
              "artifact with no source file has no git axis -- try comp-icedrill for its vintages.)"
              % args.target, file=sys.stderr)
        return 3

    if args.at:
        drill = at_vintage(files, args.at, args.diff)
        if args.json:
            print(json.dumps({"target": args.target, "resolved_via": how, "ref": args.at,
                              "results": drill}, indent=1))
        else:
            print(_render(files, how, drill, "at", args.at))
        return 0

    drill = history(files, args.limit)
    if args.json:
        print(json.dumps({"target": args.target, "resolved_via": how, "history": drill}, indent=1))
    else:
        print(_render(files, how, drill, "history"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
