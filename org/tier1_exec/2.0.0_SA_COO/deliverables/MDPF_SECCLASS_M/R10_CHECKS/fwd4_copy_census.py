#!/usr/bin/env python3
"""MDPF_SECCLASS round 8, cell SC-e-40 (FWD-4): the copy census, with a planted-copy control.

WHAT IT ANSWERS (PRD :56-62): every place in Opal's code that assigns a class to a security OUTSIDE the one shared list,
with the number of files it looked at. The one shared list (C-TABLE) is the table `etf-classifications`, the seed source
`_shared/etf_classification.py`, the seed path `yang_pipeline/seed-etf-classifications.py` and the one client
`_shared/etf_classifications_dynamodb.py`. None of those is a copy.

READS CODE ONLY (git ls-files + file reads). No AWS, no vendor, no model call. Edits nothing except its own output JSON
and, under --plant, one temporary file that it deletes before it exits.

KINDS (each hit is one `copies` entry: path, line, surface, kind, band):
  literal      a ticker->class mapping in code: a quoted ticker key whose value is a class token (dict, object, tuple
               or JSON), ticker/class on one object line, or a class-named collection (a class token key or a name such
               as FIXED_INCOME_TICKERS) holding >= MIN_LIST quoted tickers. Consecutive entries (<= GAP lines apart)
               form ONE block; a block needs >= MIN_BLOCK entries (smaller clusters are counted, not reported).
  client-copy  a file named etf_classification*.py / etf_classifications_dynamodb.py outside `_shared/` whose `_shared`
               namesake exists and is not byte-equal to it. A byte-equal shipped copy is the same list and is reported
               in `shipped_copies` with verdict BYTE-EQUAL, never as a copy.
  old-list     code (not a comment, not a docstring) that reads or writes the table named by BD_TABLE below.
  model        a model classifier that writes a class: a model-API call and a class write in the same code file.
BANDS: `test` = tests and fixtures by name; `tooling` = code under org/ and docs/ (verification and deliverable scripts,
not production). Both are listed and counted, never dropped; every other path is `prod`.

DENOMINATOR: every tracked file with extension .py .ts .tsx .js .jsx .sh .sql .json in the repo (git ls-files) and in
the portal (git -C portal ls-files src, reported as portal/<path>). Submodule gitlinks that are not checked out are
named in `scopes` and are NOT scanned. A surface whose file is missing is `scanned: false` with the reason.

PLANT (--plant): copy the bytes of one real copy to a NEW path inside a scanned scope under a name that exists nowhere
else, re-run the scan with the plant included, assert it is reported with the same kinds, delete it.

Prints:  FWD4-CENSUS denominator_files=<n> copies=<k> literal=<a> client-copy=<b> old-list=<c> model=<d> test=<t> ...
         FWD4-PLANT found=<bool> planted=<path> kind=<kind> removed=<bool>        (only with --plant)
"""
import ast
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import uuid

OUT = "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/FWD4_CENSUS_20261007.json"
SELF = "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/fwd4_copy_census.py"
EXTS = (".py", ".ts", ".tsx", ".js", ".jsx", ".sh", ".sql", ".json")
SHARED = "infra/aws/lambda/v2_portal/_shared"
V2 = "infra/aws/lambda/v2_portal"
YANG_POS = V2 + "/yang_pipeline/positioning"

# --- class vocabulary: the six classes, the legacy values and the human labels (task order, "What counts as a copy")
CLASS_TOKENS = {"cash", "fixed_income", "equity", "equities", "structured", "alternatives", "alternative", "commodities",
                "commodity", "multi_asset", "other", "unclassified"}
BD_TABLE = "bd" + "-securities"  # built in two pieces so this file never reports itself
BD_ENV = re.compile(r"\bBD_SECURITIES_TABLE\b", re.IGNORECASE)
MIN_BLOCK = 3   # entries that make a literal block
MIN_LIST = 5    # quoted tickers that make a class-named collection a literal
GAP = 25        # lines between entries of one block
MAX_BYTES = 3_000_000
# the instrument and its own output name every pattern it looks for; reading them back would make each run report the last
# one (an unstable fixed point). They stay in the denominator and are named in the JSON as self_excluded.
SELF_EXCLUDED = {SELF, OUT}
# C-TABLE's code members: the seed source, the seed path and the one client (the table itself is not code)
ONE_LIST = {SHARED + "/etf_classification.py", V2 + "/yang_pipeline/seed-etf-classifications.py",
            SHARED + "/etf_classifications_dynamodb.py"}

TICKER = r"[A-Z][A-Z0-9]{0,5}(?:[.\-/][A-Z0-9]{1,4})?|CUSIP:[A-Z0-9]{9}"
Q = r"""['"]"""
TICK_STR = re.compile(Q + r"(" + TICKER + r")" + Q)

MODEL_PREFILTER = (b"openai", b"gpt-", b"anthropic", b"claude-", b"bedrock", b"invoke_model", b"completions", b".responses.create")
MODEL_API = re.compile(r"\bopenai\b|\bgpt-\d|\banthropic\b|\bclaude-[a-z0-9]|bedrock|invoke_model|chat\.completions|ChatCompletion|\.responses\.create", re.IGNORECASE)
CLASS_WRITE = re.compile(r"classified_by|asset_class|instrument_kind|assetClass|classif(?:y|ied|ication)", re.IGNORECASE)


def run(args, cwd, check=True):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
    if check and r.returncode != 0:
        raise RuntimeError(f"{args} rc={r.returncode}: {r.stderr.strip()[:200]}")
    return r.stdout


def repo_root():
    here = os.path.abspath(os.path.dirname(__file__))
    return run(["git", "rev-parse", "--show-toplevel"], here).strip()


def norm_class(v):
    return re.sub(r"[\s\-]+", "_", v.strip().lower())


def band_of(path):
    p = path.lower()
    name = p.rsplit("/", 1)[-1]
    if ("/tests/" in p or "/test/" in p or "/__tests__/" in p or "/fixtures/" in p or "/fixture/" in p
            or name.startswith("test_") or name.endswith(("_test.py", ".test.ts", ".test.tsx", ".test.js", ".spec.ts",
                                                          ".spec.tsx", ".spec.js")) or name == "conftest.py"):
        return "test"
    if p.startswith(("org/", "docs/")):
        return "tooling"
    return "prod"


def enumerate_files(root):
    """-> list of (rel_path, abs_path) for the repo scope and the portal scope, plus scope facts."""
    files, scopes = [], {}
    tracked = run(["git", "ls-files", "-z"], root).split("\0")
    repo = [p for p in tracked if p.endswith(EXTS)]
    for p in repo:
        files.append((p, os.path.join(root, p)))
    scopes["repo"] = {"enumerator": "git ls-files", "extensions": list(EXTS), "tracked_entries": len([p for p in tracked if p]),
                      "code_files": len(repo)}
    portal_dir = os.path.join(root, "portal")
    if os.path.isdir(portal_dir) and os.path.exists(os.path.join(portal_dir, ".git")):
        ptracked = run(["git", "-C", portal_dir, "ls-files", "-z", "src"], root).split("\0")
        pf = [p for p in ptracked if p.endswith(EXTS)]
        for p in pf:
            files.append(("portal/" + p, os.path.join(portal_dir, p)))
        scopes["portal"] = {"enumerator": "git -C portal ls-files src", "extensions": list(EXTS), "tracked_entries": len([p for p in ptracked if p]),
                            "code_files": len(pf), "head": run(["git", "-C", portal_dir, "rev-parse", "HEAD"], root).strip()}
    else:
        scopes["portal"] = {"scanned": False, "reason": "portal/ is not a provisioned checkout in this tree"}
    gl = []
    for line in run(["git", "ls-files", "-s"], root).splitlines():
        if line.startswith("160000"):
            gl.append(line.split("\t", 1)[1])
    scopes["gitlinks_not_scanned"] = {"paths": [g for g in gl if g != "portal"],
                                      "reason": "submodule pointers; their contents are not part of this repo's git ls-files"}
    return files, scopes


def code_lines(path, text):
    """Lines of `text` as (lineno, line) with comments and docstrings blanked, for the old-list and model kinds."""
    lines = text.split("\n")
    blank = set()
    if path.endswith(".py"):
        try:
            tree = ast.parse(text)
            for node in ast.walk(tree):
                if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.body:
                    first = node.body[0]
                    if isinstance(first, ast.Expr) and isinstance(getattr(first, "value", None), ast.Constant) \
                            and isinstance(first.value.value, str):
                        blank.update(range(first.lineno, (first.end_lineno or first.lineno) + 1))
        except (SyntaxError, ValueError, RecursionError):
            pass
        marks = ("#",)
    elif path.endswith((".ts", ".tsx", ".js", ".jsx")):
        marks = ("//", "*", "/*")
    elif path.endswith(".sql"):
        marks = ("--",)
    elif path.endswith(".sh"):
        marks = ("#",)
    else:
        marks = ()
    out = []
    for i, ln in enumerate(lines, 1):
        s = ln.lstrip()
        if i in blank or (marks and s.startswith(marks)):
            continue
        out.append((i, ln))
    return out


# --- literal detection is VALUE-FIRST: one pass finds every quoted class token, then each hit looks back (or ahead) a
# few characters for the ticker it is assigned to. Far cheaper than three full-text key-first regexes over 400 MB.
VAL = re.compile(r"(['\"])(cash|fixed[ _-]?income|equit(?:y|ies)|structured|alternatives?|commodit(?:y|ies)|multi[ _-]?asset|other|unclassified)\1", re.IGNORECASE)
PAIR_TAIL = re.compile(r"(['\"])(" + TICKER + r")\1\s*(?:[:,=]|=>)\s*\(?\s*$")
BARE_TAIL = re.compile(r"(?:^|[{,\s])([A-Z][A-Z0-9]{0,5})\s*:\s*$")
OBJ_TAIL = re.compile(r"ticker\w*['\"]?\s*[:=]\s*(['\"])(" + TICKER + r")\1[^{}]{0,200}?(?:class|category|type|bucket)\w*['\"]?\s*[:=]\s*$", re.IGNORECASE)
# 'CLIP': { assetClass: 'Fixed Income', segment: '...' }  -- ticker key, object value carrying the class property
KEYOBJ_TAIL = re.compile(r"(['\"])(" + TICKER + r")\1\s*:\s*\{[^{}]{0,150}?\b(?:assetClass|asset_class|class\w*|category|type|bucket|group)['\"]?\s*:\s*$")
AHEAD_OPEN = re.compile(r"\s*:\s*(?:(?:frozenset|set|list|tuple)\()?\s*[\[\{\(]")
# a class-named constant bound to a bracket: FIXED_INCOME_TICKERS = {..}, equity_tickers: set = set([..]) (code files only)
NAMED = re.compile(r"\b\w*(?:fixed_?income|equit(?:y|ies)|cash|structured|alternatives?|commodit(?:y|ies)|multi_?asset|unclassified)\w*"
                   r"\s*(?::[^=\n]{0,60})?=\s*(?:(?:frozenset|set|list|tuple)\()?\s*[\[\{\(]", re.IGNORECASE)
# a byte-level prefilter: a file holding none of these cannot carry a class token as a value
LIT_PREFILTER = (b"equity", b"equities", b"fixed", b"structured", b"alternativ", b"commodit", b"multi", b"unclassified",
                 b'"cash"', b"'cash'", b'"other"', b"'other'")


def _coll_region(text, start, at, hits):
    opener = text[start]
    closer = {"[": "]", "{": "}", "(": ")"}[opener]
    depth, j, lim = 0, start, min(len(text), start + 8000)
    while j < lim:
        c = text[j]
        if c == opener:
            depth += 1
        elif c == closer:
            depth -= 1
            if depth == 0:
                break
        j += 1
    keys = TICK_STR.findall(text, start, j)
    if len(keys) >= MIN_LIST:
        for _ in keys:
            hits.append((at, "coll"))


def literal_blocks(text, code_file=True):
    """-> (blocks, small_clusters). A block = (first_line, last_line, entries)."""
    hits = []  # (char position, key)
    for m in VAL.finditer(text):
        st = m.start()
        cls = norm_class(m.group(2))
        if cls not in CLASS_TOKENS:
            continue
        tail = text[st - 80 if st > 80 else 0:st]
        k = PAIR_TAIL.search(tail) or BARE_TAIL.search(tail)
        if k:
            key = k.group(2) if k.re is PAIR_TAIL else k.group(1)
            if norm_class(key) not in CLASS_TOKENS:
                hits.append((st, key))
                continue
        wide = text[st - 260 if st > 260 else 0:st]
        o = KEYOBJ_TAIL.search(wide[-200:]) or (OBJ_TAIL.search(wide) if "icker" in wide else None)
        if o and norm_class(o.group(2)) not in CLASS_TOKENS:
            hits.append((st, o.group(2)))
            continue
        a = AHEAD_OPEN.match(text, m.end())
        if a:
            _coll_region(text, a.end() - 1, st, hits)
    if code_file:
        for m in NAMED.finditer(text):
            _coll_region(text, m.end() - 1, m.start(), hits)
    if not hits:
        return [], 0
    hits.sort()
    # char positions -> line numbers in one pass (O(n) in total, never one count per hit)
    lined, prev, line = [], 0, 1
    for pos, k in hits:
        line += text.count("\n", prev, pos)
        prev = pos
        lined.append((line, k))
    blocks, small, cur = [], 0, []
    for h in lined + [None]:
        if h is not None and cur and h[0] - cur[-1][0] <= GAP:
            cur.append(h)
            continue
        if cur:
            if len(cur) >= MIN_BLOCK:
                blocks.append((cur[0][0], cur[-1][0], len(cur)))
            else:
                small += 1
        cur = [h] if h is not None else []
    return blocks, small


def shared_namesakes(root):
    out = {}
    d = os.path.join(root, SHARED)
    for n in sorted(os.listdir(d)):
        if n.startswith(("etf_classification",)) and n.endswith(".py"):
            with open(os.path.join(d, n), "rb") as fh:
                out[n] = (hashlib.sha1(fh.read()).hexdigest(), os.path.getsize(os.path.join(d, n)))
    return out


def surface_of(path, surf_paths):
    for sid, paths in surf_paths.items():
        if path in paths:
            return sid
    for sid, paths in surf_paths.items():
        for p in paths:
            if p.endswith("/") and path.startswith(p):
                return sid
    return "UNMAPPED"


def scan(root, files, extra, surf_paths):
    copies, shipped, small_total, read_fail, skipped_big = [], [], 0, [], []
    shared = shared_namesakes(root)
    allfiles = list(files) + list(extra)
    for rel, absp in allfiles:
        try:
            size = os.path.getsize(absp)
            if size > MAX_BYTES:
                skipped_big.append(rel)
            with open(absp, "rb") as fh:
                raw = fh.read(MAX_BYTES)
        except OSError as e:
            read_fail.append({"path": rel, "reason": str(e)})
            continue
        base = rel.rsplit("/", 1)[-1]
        band = band_of(rel)
        # --- client-copy
        if (base.startswith("etf_classification") and base.endswith(".py")) and not rel.startswith(SHARED + "/") and base in shared:
            sha = hashlib.sha1(raw).hexdigest()
            equal = sha == shared[base][0] and len(raw) == shared[base][1]
            shipped.append({"path": rel, "shared_source": SHARED + "/" + base, "byte_equal": equal,
                            "verdict": "BYTE-EQUAL" if equal else "DIFFERS", "bytes": len(raw), "shared_bytes": shared[base][1]})
            if not equal:
                copies.append({"path": rel, "line": 1, "surface": surface_of(rel, surf_paths), "kind": "client-copy", "band": band,
                               "detail": f"differs from {SHARED}/{base}"})
        if rel in ONE_LIST or rel in SELF_EXCLUDED:
            continue  # the one shared list (C-TABLE) is not a copy; it is the thing the census measures against
        low = raw.lower()
        text = None
        # --- literal
        if any(k in low for k in LIT_PREFILTER):
            text = raw.decode("utf-8", errors="replace")
            blocks, small = literal_blocks(text, code_file=not rel.endswith(".json"))
            small_total += small
            for first, last, n in blocks:
                copies.append({"path": rel, "line": first, "surface": surface_of(rel, surf_paths), "kind": "literal", "band": band,
                               "detail": f"{n} entries, lines {first}-{last}"})
        # --- old-list: code lines only (a comment or docstring that names the table is not a reader or writer)
        is_json = rel.endswith(".json")
        if BD_TABLE.encode() in low or b"bd_securities_table" in low:
            if is_json:
                n_old = low.count(BD_TABLE.encode()) + low.count(b"bd_securities_table")
                first_old = low[:min([i for i in (low.find(BD_TABLE.encode()), low.find(b"bd_securities_table")) if i >= 0])].count(b"\n") + 1
            else:
                text = text if text is not None else raw.decode("utf-8", errors="replace")
                n_old, first_old = 0, None
                for i, ln in code_lines(rel, text):
                    if BD_TABLE in ln.lower() or BD_ENV.search(ln):
                        n_old += 1
                        first_old = first_old or i
            if n_old:
                copies.append({"path": rel, "line": first_old, "surface": surface_of(rel, surf_paths), "kind": "old-list", "band": band,
                               "detail": f"{n_old} {'line(s)' if is_json else 'code line(s)'} naming the old list"})
        # --- model: a model-API call and a class write in one code file (code lines only; JSON and SQL are not callers)
        if not is_json and not rel.endswith(".sql") and any(k in low for k in MODEL_PREFILTER):
            text = text if text is not None else raw.decode("utf-8", errors="replace")
            if MODEL_API.search(text) and CLASS_WRITE.search(text):
                first_m, has_api, has_cls = None, False, False
                for i, ln in code_lines(rel, text):
                    if MODEL_API.search(ln):
                        has_api = True
                        first_m = first_m or i
                    if CLASS_WRITE.search(ln):
                        has_cls = True
                if has_api and has_cls:
                    copies.append({"path": rel, "line": first_m, "surface": surface_of(rel, surf_paths), "kind": "model", "band": band,
                                   "detail": "model-API call and a class write in one code file"})
    return copies, shipped, small_total, read_fail, skipped_big


def surface_paths(root):
    """Manifest surface -> paths. S13 and S26 are written short in the PRD; resolved against git ls-files and recorded."""
    s = {
        "S06": ["data/black_diamond/scripts/gold/B_01b.classify_new_securities.py", "data/black_diamond/scripts/gold/E_18.detect_new_securities.py"],
        "S07": ["data/cot/scripts/gold/lib/etf_classifier.py", "data/cot/scripts/gold/B_01b.classify_new_securities.py",
                "data/cot/scripts/gold/E_18.detect_new_securities.py"],
        "S10": ["data/inf/scripts/classification/classify_assets.py"],
        "S11": ["data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py"],
        "S12": [V2 + "/partners/lambdas/opal-partners-data/etf_classification.py", V2 + "/partners/lambdas/opal-partners-data/etf_classifier.py"],
        "S13": None,  # resolved below
        "S14": [SELF],
        "S15": ["lib/research/identity/positioning_chain.py"],
        "S16": ["portal/src/pages/Positioning/constants/etf-categories.ts", "portal/src/components/holdings/HoldingsBreakdownTable.tsx"],
        "S22": ["infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py"],
        "S23": ["portal/src/pages/Attribution/constants/etf-categories.ts", "portal/src/pages/Attribution/constants/holdings-shared.tsx"],
        "S24": ["portal/src/lib/tickerRegistry.ts"],
        "S25": ["data/black_diamond/scripts/classification/resolve_tickers.py"],
        "S26": [YANG_POS + "/yang-generate-positioning/lambda_function.py"],
    }
    tracked = run(["git", "ls-files", "-z"], root).split("\0")
    want = [("yang-generate-etf-returns", "etf_classification.py"), ("yang-generate-holdings-attribution", "etf_classifications_dynamodb.py"),
            ("yang-generate-positioning", "lambda_function.py"), ("market-overview-tiered-generator", "lambda_function.py")]
    s13, how = [], {}
    for d, f in want:
        hit = [p for p in tracked if p.startswith(V2 + "/") and p.endswith("/" + d + "/" + f)]
        s13.extend(hit)
        how[d + "/" + f] = hit
    s["S13"] = s13
    return s, how


SURFACE_NOTES = {
    "S13": "the PRD writes short paths; resolved against git ls-files under infra/aws/lambda/v2_portal (see s13_resolution). "
           "yang-generate-holdings-attribution and yang-generate-positioning carry etf_classifications_dynamodb.py (BYTE-EQUAL to _shared, see shipped_copies)",
    "S15": "positioning_chain.py:163 classify_identifier assigns an IDENTIFIER kind (cusip/figi/sedol/unclassified), not a security class: no copy",
    "S26": "the PRD writes yang-generate-positioning/lambda_function.py:95; the real path is under yang_pipeline/positioning/. ETF_GEOGRAPHY_MAPPING there "
           "maps ticker -> region (US, ...), not ticker -> class, so it is outside the four kinds; reported, not counted",
    "S14": "the instrument itself; it reads code only",
}


def surface_report(root, surf_paths, copies):
    out = {}
    for sid, paths in sorted(surf_paths.items()):
        missing = [p for p in paths if not os.path.exists(os.path.join(root, p))]
        n = sum(1 for c in copies if c["surface"] == sid)
        entry = {"paths": list(paths), "scanned": bool(paths) and not missing, "copies": n}
        if missing or not paths:
            entry["reason"] = ("missing: " + ", ".join(missing)) if missing else "no path resolved"
        if sid in SURFACE_NOTES:
            entry["note"] = SURFACE_NOTES[sid]
        out[sid] = entry
    return out


def census(root, files, scopes, surf_paths, extra=()):
    t = time.time()
    copies, shipped, small, fail, big = scan(root, files, extra, surf_paths)
    copies.sort(key=lambda c: (c["kind"], c["path"], c["line"]))
    return copies, shipped, small, fail, big, time.time() - t


def tally(copies):
    k = {x: sum(1 for c in copies if c["kind"] == x) for x in ("literal", "client-copy", "old-list", "model")}
    b = {x: sum(1 for c in copies if c["band"] == x) for x in ("prod", "test", "tooling")}
    return k, b


def main(argv):
    root = repo_root()
    do_plant = "--plant" in argv
    t0 = time.time()
    files, scopes = enumerate_files(root)
    surf_paths, s13_how = surface_paths(root)
    copies, shipped, small, fail, big, secs = census(root, files, scopes, surf_paths)
    kinds, bands = tally(copies)
    n = len(files)
    data = {
        "denominator_files": n,
        "self_excluded": {"paths": sorted(SELF_EXCLUDED), "reason": "they name every pattern the census looks for; they stay in the denominator"},
        "scopes": scopes,
        "surfaces": surface_report(root, surf_paths, copies),
        "copies": copies,
        "plant": {"ran": False},
        "copies_by_kind": kinds,
        "copies_by_band": bands,
        "copies_by_surface": {sid: sum(1 for c in copies if c["surface"] == sid) for sid in sorted({c["surface"] for c in copies})},
        "shipped_copies": shipped,
        "s13_resolution": s13_how,
        "unreadable": fail,
        "read_truncated_over_bytes": {"limit": MAX_BYTES, "files": big},
        "literal_clusters_below_threshold": small,
        "thresholds": {"MIN_BLOCK": MIN_BLOCK, "MIN_LIST": MIN_LIST, "GAP": GAP},
        "census_seconds": round(secs, 1),
    }
    line = (f"FWD4-CENSUS denominator_files={n} copies={len(copies)} literal={kinds['literal']} client-copy={kinds['client-copy']} "
            f"old-list={kinds['old-list']} model={kinds['model']} test={bands['test']} tooling={bands['tooling']} prod={bands['prod']} "
            f"seconds={secs:.1f}")
    rc = 0
    if do_plant:
        rc = plant(root, files, surf_paths, copies, data)
    else:
        # a plain re-run must not erase the control's record: carry the prior plant result forward, marked as carried
        try:
            with open(os.path.join(root, OUT), encoding="utf-8") as fh:
                prior = json.load(fh).get("plant") or {}
            if prior.get("ran"):
                data["plant"] = dict(prior, carried_from_prior_run=True)
        except (OSError, ValueError):
            pass
    with open(os.path.join(root, OUT), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(data, fh, indent=1, sort_keys=False)
        fh.write("\n")
    print(line)
    if do_plant:
        p = data["plant"]
        print(f"FWD4-PLANT found={p['found']} planted={p['planted']} kind={p['kind']} removed={p['removed']}")
    print(f"total_seconds={time.time() - t0:.1f} out={OUT}")
    return rc


def plant(root, files, surf_paths, copies, data):
    """Negative control: put one real copy back under a new name in a scanned scope; the census must find it."""
    # source = the largest prod client-copy that is also a literal, else any prod literal
    by_path = {}
    for c in copies:
        if c["band"] == "prod":
            by_path.setdefault(c["path"], set()).add(c["kind"])
    cands = [p for p, ks in by_path.items() if "literal" in ks and not p.startswith("portal/")]
    cands.sort(key=lambda p: (("client-copy" not in by_path[p]), p))
    if not cands:
        data["plant"] = {"ran": True, "found": False, "planted": "-", "kind": "-", "removed": True, "reason": "no real literal copy to copy"}
        return 1
    src = cands[0]
    kinds = sorted(by_path[src])
    tag = uuid.uuid4().hex[:12]
    base = src.rsplit("/", 1)[-1]
    # a unique directory inside the source's own scope; the basename is kept so the client-copy rule is exercised too
    pdir = src.rsplit("/", 1)[0] + "/zz_fwd4_plant_" + tag
    rel = pdir + "/" + base
    absd, absf = os.path.join(root, pdir), os.path.join(root, rel)
    assert not os.path.exists(absd), "plant path collides"
    found, removed, got, rescan = False, False, [], {}
    try:
        os.makedirs(absd)
        with open(os.path.join(root, src), "rb") as fh:
            raw = fh.read()
        with open(absf, "wb") as fh:
            fh.write(raw)
        # the re-scan covers the scope the plant sits in (the lambda tree of the source) plus the plant; a second pass over all
        # 21k files would not fit the 120 s bound beside the first
        prefix = "/".join(src.split("/")[:4]) + "/"
        scope_files = [f for f in files if f[0].startswith(prefix)]
        c2, _, _, _, _, _ = census(root, scope_files, {}, surf_paths, extra=[(rel, absf)])
        got = sorted({c["kind"] for c in c2 if c["path"] == rel})
        found = got == kinds
        rescan = {"scope_prefix": prefix, "files": len(scope_files) + 1}
    finally:
        try:
            if os.path.exists(absf):
                os.remove(absf)
            if os.path.isdir(absd):
                os.rmdir(absd)
        except OSError:
            pass
        removed = not os.path.exists(absd)
    data["plant"] = {"ran": True, "found": found, "planted": rel, "source": src, "kind": ",".join(kinds), "kinds_reported": got, "rescan": rescan,
                     "removed": removed, "untracked_check": "git status --short on the plant path must be empty"}
    return 0 if (found and removed) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
