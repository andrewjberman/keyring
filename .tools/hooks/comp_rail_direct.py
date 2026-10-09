#!/usr/bin/env python3
"""comp_rail_direct.py -- the DIRECTED denial text for the comp-rail (.tools/hooks/comp-tool-hud.sh).

Andrew-direct 2026-10-09 ~01:3xZ ("approved", REC (a)): the rail stays a mandatory gate, but every denial must hand
the agent the exact command that answers. Design:
org/tier1_exec/4.0.0_SA_CRO/deliverables/COMP_RAIL_DIRECTED_GATE_DESIGN_20261008.md. Record:
org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261009_013xZ_DIRECTED_RAIL_GATE_APPROVED_REC_A_REWRITE_RULE_21.md.

Called by the hook ONLY on a would-deny path (never on the fast path), with one JSON object on stdin:
  {"cmd": <the whole Bash command>, "kind": "search"|"census"|"aws", "piece": <index of the offending segment>,
   "ws": <workspace root>, "cwd": <the call's cwd or "">, "marker": true|false, "hint": <aws class or "">}
and prints one JSON object:
  {"verdict": "DENY"|"ALLOW", "rule": "R1".."R6"|"AWS-*", "shape": <log shape>, "message": <denial text>}

THE SEGMENT SPLIT MIRRORS THE HOOK EXACTLY: newlines and CRs become ';', quoted bodies are opaque (single quotes first,
then double quotes), and the command splits on '&&', '||' and ';'. So a piece index the hook counted names the same text
here. The failure modes (design section 1):
  F1 blind recursive search of the repo; F2 an absence concluded from a search that cannot see;
  F3 a raw AWS read the served graph or a comp-tool answers with context; F4 a census denominator cut.
"""
import json
import os
import re
import shlex
import subprocess
import sys

SEP_RX = re.compile(r"&&|\|\||;")
GREP_LEADS = {"grep", "egrep", "fgrep", "rg", "ack", "ag", "findstr"}
ARG_FLAGS = {"-e", "--regexp", "-f", "--file", "-A", "-B", "-C", "-m", "--max-count", "--include", "--exclude",
             "--exclude-dir", "-g", "--glob", "-t", "--type", "-T", "--type-not", "-d", "-D", "--context",
             "--after-context", "--before-context"}
PREFIX_RX = re.compile(r"^(([A-Za-z_][A-Za-z0-9_]*=\S*|env|sudo|time|nice)\s+)*")
WHY = {
    "F1": "F1 -- a blind recursive search of the repo (~64k tracked files plus gitignored state, unranked, no "
          "denominator, and a 0 that cannot say what it saw).",
    "F2": "F2 -- a search whose 0 would be read as 'does not exist' without saying what it looked through.",
    "F3": "F3 -- a raw AWS read the served graph or a comp-tool already answers, with context a single call lacks.",
    "F4": "F4 -- a census output piped into a receiver that can cut its denominator line.",
}


def mask_len(s):
    """Same-length mask of quoted bodies: single quotes first, then double quotes (the hook's sed order)."""
    m = re.sub(r"'[^']*'", lambda x: "'" + "x" * (len(x.group(0)) - 2) + "'", s)
    return re.sub(r'"[^"]*"', lambda x: '"' + "x" * (len(x.group(0)) - 2) + '"', m)


def split_pieces(cmd):
    """[(piece_text, sep_before)] exactly as the hook's segment loop sees them."""
    s = cmd.replace("\n", ";").replace("\r", ";")
    m = mask_len(s)
    out, start, sep = [], 0, ""
    for mt in SEP_RX.finditer(m):
        out.append((s[start:mt.start()], sep))
        sep = s[mt.start():mt.end()]
        start = mt.end()
    out.append((s[start:], sep))
    return out


def norm_piece(p):
    p = p.strip()
    p = PREFIX_RX.sub("", p)
    return p


def first_stage(p):
    m = mask_len(p)
    i = m.find("|")
    return p[:i] if i >= 0 else p


def toks(text):
    text = re.sub(r"(^|\s)#.*$", "", text)
    try:
        return shlex.split(text, posix=True)
    except ValueError:
        return text.split()


def q(s):
    return "'" + s.replace("'", "'\"'\"'") + "'"


def to_abs(path, base):
    p = os.path.expandvars(os.path.expanduser(path))
    m = re.match(r"^/(?:cygdrive/)?([A-Za-z])(/.*)?$", p)
    if m:
        p = "%s:%s" % (m.group(1).upper(), m.group(2) or "/")
    if re.match(r"^[A-Za-z]:[\\/]", p):
        return os.path.normpath(p)
    if p.startswith("/"):
        return None   # an MSYS-only path (/tmp, /usr) -- its Windows home is not knowable here
    return os.path.normpath(os.path.join(base, p))


def norm(p):
    return os.path.normcase(os.path.normpath(p)) if p else p


def worktrees(ws):
    """{normalised path: path as git prints it} for every worktree of this repo (the main one included)."""
    try:
        r = subprocess.run(["git", "-C", ws, "worktree", "list", "--porcelain"], capture_output=True, text=True,
                           timeout=10)
        out = {}
        for line in r.stdout.splitlines():
            if line.startswith("worktree "):
                path = line[9:].strip()
                out[norm(path)] = path
        return out or {norm(ws): ws}
    except Exception:
        return {norm(ws): ws}


def find_checkout(path):
    """The nearest ancestor holding .git (dir or file), or None."""
    d = path
    while d and os.path.isdir(d) is False and os.path.dirname(d) != d:
        d = os.path.dirname(d)
    while d:
        if os.path.exists(os.path.join(d, ".git")):
            return d
        nd = os.path.dirname(d)
        if nd == d:
            return None
        d = nd
    return None


def base_dir(pieces, idx, cwd, ws):
    base = cwd or ws
    for text, _ in pieces[:idx]:
        t = toks(norm_piece(text))
        if len(t) >= 2 and t[0] == "cd":
            nb = to_abs(t[1], base)
            if nb and os.path.isdir(nb):   # a cd we cannot resolve to a real folder leaves the base alone
                base = nb
    return base


def parse_grep(t):
    lead = os.path.basename(t[0])
    flags, pattern, paths, i = [], None, [], 1
    while i < len(t):
        a = t[i]
        if a in ("-e", "--regexp") and i + 1 < len(t):
            pattern = t[i + 1]
            i += 2
            continue
        if a in ARG_FLAGS and i + 1 < len(t):
            flags.append(a)
            i += 2
            continue
        if a.startswith("-") and a != "-":
            flags.append(a)
        elif pattern is None:
            pattern = a
        else:
            paths.append(a)
        i += 1
    if lead == "findstr":
        flags = [f for f in flags]
    short = "".join(f[1:] for f in flags if f.startswith("-") and not f.startswith("--"))
    opt = []
    if "i" in short or "--ignore-case" in flags:
        opt.append("-i")
    if "l" in short or "--files-with-matches" in flags:
        opt.append("--files")
    return pattern or "", paths, opt


def parse_find(t):
    dirs, glob, i = [], None, 1
    while i < len(t) and not t[i].startswith("-") and t[i] not in ("(", "!", "\\("):
        dirs.append(t[i])
        i += 1
    while i < len(t):
        if t[i] in ("-name", "-iname", "-path", "-wholename", "-ipath") and i + 1 < len(t):
            glob = t[i + 1]
            break
        i += 1
    return dirs or ["."], glob or "*"


def is_search_piece(text):
    t = toks(first_stage(norm_piece(text)))
    if not t:
        return False
    lead = os.path.basename(t[0])
    if lead == "find":
        return True
    if lead in GREP_LEADS:
        joined = " ".join(t[1:])
        return bool(re.search(r"(^|\s)-[A-Za-z]*[rR][A-Za-z]*(\s|$)|--recursive|--dereference-recursive", joined)) \
            or lead in ("rg", "ack", "ag", "findstr")
    return False


def is_aws_enum(text):
    return bool(re.search(r"aws\s+(iam\s+list-(roles|policies|users)|lambda\s+list-functions|s3api\s+list-buckets)"
                          r"(\s|$)|aws\s+s3\s+ls\s*$", norm_piece(text)))


def remainder(pieces, idx, kind):
    keep = []
    for i, (text, sep) in enumerate(pieces):
        if i == idx:
            continue
        if kind == "search" and is_search_piece(text):
            continue
        if kind == "aws" and is_aws_enum(text):
            continue
        if not text.strip():
            continue
        keep.append((text.strip(), sep.strip() if sep.strip() else ";"))
    if not keep:
        return ""
    out = keep[0][0]
    for text, sep in keep[1:]:
        out += " %s %s" % (sep, text)
    return out


def message(rule, why, run_next, rem, note=""):
    lines = ["NOTHING IN THIS CALL RAN. (comp-rail %s)" % rule, "WHY: %s" % why, "RUN NEXT: %s" % run_next]
    if rem:
        lines.append("REMAINDER (the rest of your call, which did not run): %s" % rem)
    if note:
        lines.append("NOTE: %s" % note)
    return "\n".join(lines)


def search(req):
    cmd, ws = req["cmd"], req["ws"]
    pieces = split_pieces(cmd)
    idx = int(req["piece"])
    text = pieces[idx][0] if 0 <= idx < len(pieces) else cmd
    t = toks(first_stage(norm_piece(text)))
    if not t:
        return {"verdict": "ALLOW", "rule": "-", "shape": "unparsed", "message": ""}
    lead = os.path.basename(t[0])
    base = base_dir(pieces, idx, req.get("cwd") or "", ws)
    if lead == "find":
        targets, glob = parse_find(t)
        pattern, opt = None, []
    else:
        pattern, targets, opt = parse_grep(t)
        targets = targets or ["."]
    wts = worktrees(ws)
    nws = norm(ws)
    roots, outside, unknown = [], 0, 0
    for tg in targets:
        if any(ch in tg for ch in "*?$") and not tg.startswith(("$TEMP", "$TMP", "$HOME", "~")):
            unknown += 1
            roots.append(nws)
            continue
        a = to_abs(tg, base)
        if a is None or not (os.path.exists(a) or os.path.isdir(os.path.dirname(a))):
            unknown += 1          # not resolvable to a real place: read as this repo (deny), never as outside
            roots.append(nws)
            continue
        na = norm(a)
        hit = [w for w in wts if na == w or na.startswith(w + os.sep)]
        if hit:
            roots.append(max(hit, key=len))
            continue
        if find_checkout(a):
            roots.append("OTHER")
            continue
        outside += 1
        roots.append("OUTSIDE")
    if roots and all(r in ("OUTSIDE", "OTHER") for r in roots):
        return {"verdict": "ALLOW", "rule": "-", "message": "",
                "shape": "outside-checkout" if "OUTSIDE" in roots else "other-checkout"}
    wt = next((wts.get(r, r) for r in roots if r not in ("OUTSIDE", "OTHER") and r != nws), None)
    rel = []
    for tg in targets:
        a = to_abs(tg, base)
        r = None
        if a:
            na = norm(a)
            for w in sorted(wts, key=len, reverse=True):
                if na == w or na.startswith(w + os.sep):
                    r = os.path.relpath(a, w).replace("\\", "/")
                    break
        rel.append(r if r is not None else tg)
    infra = any(r.startswith("infra/aws/") or r.endswith(".tf") for r in rel)
    rem = remainder(pieces, idx, "search")
    dirs = " ".join(rel) if rel else "."
    if lead == "find":
        rn = "comp-find --name %s %s" % (q(glob), dirs)
        rule, why = "R2", WHY["F1"]
    else:
        rn = "comp-find %s%s %s" % (" ".join(opt) + " " if opt else "", q(pattern), dirs)
        rule, why = "R1", WHY["F1"] + " " + WHY["F2"].split(" -- ", 1)[1].capitalize()
    if wt:
        rn = "cd %s && %s" % (q(wt.replace("\\", "/")), rn)
        rule = "R3"
        why = WHY["F1"] + " (inside the linked worktree %s; run it there, as its own call)" % wt.replace("\\", "/")
    elif infra and lead != "find":
        rule = "R4"
        rn = rn + "   then, for the resource itself: comp-estate --resource %s" % q(pattern)
    if rule != "R4" and not req.get("marker", True):
        return {"verdict": "ALLOW", "rule": rule, "shape": "%s-marker-off" % rule, "message": ""}
    note = ""
    if any(f.startswith("--include") or f.startswith("--exclude") for f in t if f.startswith("-")):
        note = "--include/--exclude filters are not carried over; narrow with a pathspec instead (e.g. 'dir/*.py')."
    return {"verdict": "DENY", "rule": rule, "shape": rule, "message": message(rule, why, rn, rem, note)}


def census(req):
    pieces = split_pieces(req["cmd"])
    idx = int(req["piece"])
    text = norm_piece(pieces[idx][0]) if 0 <= idx < len(pieces) else req["cmd"]
    fs = first_stage(text).strip()
    m = mask_len(text)
    recv = text[m.find("|") + 1:].strip() if "|" in m else ""
    n = re.search(r"(?:head|tail)\s+(?:-n\s*)?-?(\d+)", recv)
    lead = os.path.basename(toks(fs)[0]) if toks(fs) else "the tool"
    if lead == "comp-find" and "--limit" not in fs:
        rn = "%s --limit %s" % (fs, n.group(1) if n else "20")
    elif lead == "comp-find":
        rn = fs + "   (it already pages; add --page N or --band HEAD/DEF to move through it)"
    else:
        rn = fs + "   (use its own paging flags -- see %s --help -- instead of a pipe)" % lead
    rem = remainder(pieces, idx, "census")
    msg = message("R6", WHY["F4"], rn, rem,
                  "a filter whose text contains ENUMERATE or DENOMINATOR is allowed, because it keeps the count line.")
    return {"verdict": "DENY", "rule": "R6", "shape": "R6", "message": msg}


AWS_ENUM = [
    (r"aws\s+iam\s+list-roles", "IAM_ROLE"), (r"aws\s+iam\s+list-policies", "IAM_POLICY"),
    (r"aws\s+iam\s+list-users", "IAM_USER"), (r"aws\s+lambda\s+list-functions", "LAMBDA"),
    (r"aws\s+s3api\s+list-buckets", "S3_BUCKET"), (r"aws\s+s3\s+ls\s*$", "S3_BUCKET")]


def aws(req):
    pieces = split_pieces(req["cmd"])
    idx = int(req["piece"])
    text = norm_piece(pieces[idx][0]) if 0 <= idx < len(pieces) else req["cmd"]
    fs = first_stage(text).strip()
    hint = req.get("hint") or ""
    rem = remainder(pieces, idx, "aws")
    if hint == "R5":
        ntype = next((ty for rx, ty in AWS_ENUM if re.search(rx, fs)), "IAM_ROLE")
        pm = re.search(r"contains\([^,]+,\s*[`'\"]([^`'\"]+)[`'\"]\)", text) or re.search(
            r"--(?:path-prefix|prefix)\s+(\S+)", text)
        pat = pm.group(1) if pm else "."
        rn = ("comp-find --corpus aws %s %s   (or: comp-kuzu \"MATCH (n:CloudNode) WHERE n.node_type = '%s' "
              "RETURN n.name\")" % (q(pat), ntype, ntype))
        note = "a live get-*/simulate-principal-policy/describe-* on ONE named resource is allowed: that is APPLIED evidence."
        return {"verdict": "DENY", "rule": "R5", "shape": "R5",
                "message": message("R5", WHY["F3"] + " (an enumeration the served graph holds)", rn, rem, note)}
    if hint == "aws_route":
        rn = "comp-routes behaviors | origins | rewrites | api-routes   (the CloudFront/API-GW config listing)"
        note = "a get-*/describe-* with an id (--id, --distribution-id, --rest-api-id) is allowed."
        return {"verdict": "DENY", "rule": "AWS-ROUTE", "shape": "AWS-ROUTE",
                "message": message("AWS-ROUTE", WHY["F3"], rn, rem, note)}
    if hint == "aws_deploy_verify":
        sm = re.search(r"([A-Za-z0-9_.-]+\.py)", fs)
        rn = "comp-pipescript deployed %s" % (sm.group(1) if sm else "[<script> | --firm bd|inf|cot|mdpf]")
        return {"verdict": "DENY", "rule": "AWS-DEPLOY", "shape": "AWS-DEPLOY",
                "message": message("AWS-DEPLOY", WHY["F3"] + " (a code/ listing read as deploy evidence)", rn, rem)}
    if hint == "aws_freshness":
        um = re.search(r"(s3://\S+)", fs)
        rn = "comp-freshness %s   (is it fresh)  |  comp-routes trace --json <url>   (what serves this key)" % (
            um.group(1) if um else "<artifact>")
        note = "a genuine need for the raw listing itself is a legitimate '# rail-checked: <why>'."
        return {"verdict": "DENY", "rule": "AWS-FRESH", "shape": "AWS-FRESH",
                "message": message("AWS-FRESH", WHY["F3"] + " (a served-prefix listing read as freshness)", rn, rem,
                                   note)}
    return {"verdict": "ALLOW", "rule": "-", "shape": "aws-other", "message": ""}


def main():
    try:
        req = json.loads(sys.stdin.read() or "{}")
        fn = {"search": search, "census": census, "aws": aws}[req.get("kind", "")]
        out = fn(req)
    except Exception as exc:  # noqa: BLE001 -- fail safe: the hook keeps its verdict, with a generic text
        out = {"verdict": "ERROR", "rule": "-", "shape": "helper-error", "message": "", "error": str(exc)[:200]}
    sys.stdout.write(json.dumps(out, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
