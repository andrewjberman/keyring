"""RCG stage-B marker: typed reference edges + mark-and-sweep reachability closure.

W1 stage B (NFRA_REPOCOHERENCEGRAPH PRD s.5). Consumes the newest scan vintage's
inventory.jsonl; emits marked.jsonl (per-file reach verdict + edge features) and, on
--cycle0, the comp-tools dependency map + the reader-anchored registry adjudication.

MARKING SEMANTICS (tracing GC): liveness flows along OUT-edges of LIVE nodes only --
a live file's dependencies and citations become live; an unmarked file's edges confer
nothing (vintage-weighted by construction: dead clusters citing each other stay dead).
RECORD-class files are excluded as EDGE SOURCES by design: a session log naming a file
must never mark it live.

BOUNDARY DECLARATION (printed every run):
  address_space      edge channels: python AST imports (incl. level-1 relative) | literal
                     repo-path tokens in EXEC/REG/DOC sources (slash paths + unique
                     basenames) | lexicon tool-token invocations in EXEC sources.
  traversal_residue  dynamic imports, getattr dispatch, f-string/constructed paths,
                     runtime S3 keys, shell variable expansion, basename references that
                     are AMBIGUOUS in the population (skipped + counted), sources >2MB
                     (skipped + counted), non-UTF8 binary content, DATA-file runtime
                     producer/consumer relations (a written-at-runtime artifact is
                     invisible here -- scan_data cycle territory, declared).
  determinism        REPRODUCIBLE on a pinned scan vintage: every set-order leak
                     into output (the dotted-module [:4] truncation, root `why`
                     labels) is sorted at its build site, so marked.jsonl and
                     edges.jsonl are byte-stable without PYTHONHASHSEED.
  presentation       the print is aggregates; per-file truth is marked.jsonl.
  failure_direction  UNDER-MARKING (false cruft) -- which is why the sweep proposes and
                     never executes, and why import resolution is deliberately generous
                     (over-marking is the safe direction). Ambiguity resolved toward LIFE.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
import warnings
from collections import defaultdict, deque
from pathlib import Path

import yaml

WS = Path(__file__).resolve().parents[2]
MAX_SOURCE_BYTES = 2_000_000
PATH_TOKEN = re.compile(r"(?:[A-Za-z0-9_.@-]+/)+[A-Za-z0-9_.@-]+")
BASENAME_TOKEN = re.compile(
    r"\b[A-Za-z0-9_-]+\.(?:py|sh|ps1|yaml|yml|json|jsonl|md|tsv|csv|tf|js|ts)\b")
REGISTRY_CANDIDATES = [
    "org/modules/graph/graph-call-manifest.yaml",
    "org/modules/graph/comp-tools.yaml",
    "org/modules/graph/TOOL_MASTER.yaml",
    "org/modules/graph/comp-coverage-map.yaml",
    "org/modules/graph/estate-coverage-manifest.yaml",
    "org/modules/graph/comp-output-contracts.yaml",
    "org/modules/graph/estate-coverage-resolver.json",
]


def newest_scan() -> Path:
    scans = sorted((WS / "rcg" / "scans").glob("*/inventory.jsonl"))
    if not scans:
        print("BLOCKED: no scan vintage found -- run rcg/bin/scan.py first")
        sys.exit(3)
    return scans[-1].parent


def load_rows(scan_dir: Path) -> list[dict]:
    with (scan_dir / "inventory.jsonl").open(encoding="utf-8", errors="replace") as h:
        return [json.loads(line) for line in h]


def read_text(path: str) -> str:
    p = WS / path
    try:
        if p.stat().st_size > MAX_SOURCE_BYTES:
            return ""
        return p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def build_root_set(population: set) -> tuple[set, dict]:
    spec = yaml.safe_load((WS / "rcg" / "charters.yaml").read_text(encoding="utf-8"))
    roots: set = set()
    why: dict = {}
    prefixes: list = []
    for entry in spec["root_set"]:
        entry = entry.strip()
        if entry.endswith("/"):
            prefixes.append(entry)
        elif entry in population:
            roots.add(entry)
            why[entry] = "root:exact"
    for p in sorted(population):
        for pref in prefixes:
            if p.startswith(pref):
                roots.add(p)
                why[p] = f"root:{pref}"
                break
    # active projects only (status filter, per charters.yaml note)
    for pj in (WS / "org" / "projects").glob("*.json"):
        rel = str(pj.relative_to(WS)).replace("\\", "/")
        try:
            status = str(json.loads(pj.read_text(encoding="utf-8")).get("status", "")).lower()
        except (OSError, json.JSONDecodeError):
            status = "unparseable"
        if rel in roots and status not in ("active", "on-hold", "on_hold"):
            roots.discard(rel)
            why.pop(rel, None)
    # lambda-source-map mapped trees
    smap = WS / "infra" / "aws" / "lambda" / "ci" / "lambda-source-map.json"
    n_lambda_roots = 0
    try:
        functions = json.loads(smap.read_text(encoding="utf-8")).get("functions", {})
    except (OSError, json.JSONDecodeError):
        functions = {}
    dirs = sorted({str(v.get("source_dir", "")).strip("/").replace("\\", "/")
                   for v in functions.values() if isinstance(v, dict)})
    for p in sorted(population):
        for d in dirs:
            if d and p.startswith(d + "/"):
                if p not in roots:
                    roots.add(p)
                    why[p] = "root:lambda-source-map"
                    n_lambda_roots += 1
                break
    # EC2_MANIFEST service trees -- EC2 code deploys via S3->EC2 pull (CLAUDE.md rules
    # 8/12), so repo-side EC2 source is live-in-production while unreferenced in-repo;
    # without this the whole infra/aws/ec2 tree reads unmarked (stage-D cycle-1 finding)
    man = WS / "infra" / "aws" / "ec2" / "EC2_MANIFEST.json"
    n_ec2 = 0
    try:
        services = json.loads(man.read_text(encoding="utf-8")).get("services", {})
    except (OSError, json.JSONDecodeError):
        services = {}
    sdirs = sorted({str(v.get("source_path", "")).strip("/").replace("\\", "/")
                    for v in services.values() if isinstance(v, dict)})
    for p in sorted(population):
        for d in sdirs:
            if d and (p == d or p.startswith(d + "/")):
                if p not in roots:
                    roots.add(p)
                    why[p] = "root:ec2-manifest"
                    n_ec2 += 1
                break
    # terraform tree
    for p in sorted(population):
        if p.startswith("infra/aws/terraform/") and p not in roots:
            roots.add(p)
            why[p] = "root:terraform"
    print(f"[roots] {len(roots)} root files ({n_lambda_roots} via lambda-source-map "
          f"{len(dirs)} dirs; {n_ec2} via EC2_MANIFEST {len(sdirs)} services)")
    return roots, why


def build_edges(rows: list[dict], no_lexicon: bool = False) -> tuple[dict, dict]:
    """Return (edges: src -> set(dst), stats). Three channels, all declared."""
    population = {r["path"] for r in rows}
    # DETERMINISM (RCG-D2): `population` is a SET, and `dotted` lists feed a [:4]
    # TRUNCATION below -- so set-iteration order selected WHICH 4 candidates became
    # edges, and PYTHONHASHSEED varied it run to run. Measured 2026-09-16 on one
    # pinned scan vintage: 3 unseeded runs -> 3 distinct marked.jsonl sha256; 2 runs
    # at PYTHONHASHSEED=0 -> byte-identical. Sorting at the BUILD sites fixes it in
    # the tool rather than in the caller's environment.
    basename_index: dict = defaultdict(list)
    for p in sorted(population):
        basename_index[p.rsplit("/", 1)[-1]].append(p)
    py_files = sorted(p for p in population if p.endswith(".py"))
    dotted: dict = defaultdict(list)
    for p in py_files:
        mod = p[:-3].replace("/", ".")
        parts = mod.split(".")
        for i in range(len(parts)):
            dotted[".".join(parts[i:])].append(p)

    # FAIL-CLOSED (RCG-D1): this used to read the lexicon behind a bare
    # `if lexicon_path.exists():`. A run before lexicon.py had ever been run
    # contributed ZERO invoke edges, printed a clean aggregate with no warning, and
    # still advertised the channel as LIVE in the boundary declaration below.
    # A missing declared input must not read as a healthy run. --no-lexicon is the
    # audited escape and DOWNGRADES the boundary declaration instead of silencing it.
    lexicon_path = newest_scan() / "lexicon.json"
    tool_tokens: dict = {}
    if not lexicon_path.exists():
        if not no_lexicon:
            print(f"BLOCKED: no lexicon.json in {lexicon_path.parent.name} -- the "
                  "tool-invocation edge channel is DECLARED LIVE in this tool's "
                  "boundary. Run rcg/bin/lexicon.py first, or pass --no-lexicon to "
                  "run with that channel explicitly DISABLED.")
            sys.exit(3)
        print("[edges] WARNING: --no-lexicon -- channel 3 (tool-token invocations) "
              "DISABLED; invoke_edges will read 0 by construction, not by absence "
              "of invocations.")
    else:
        lex = json.loads(lexicon_path.read_text(encoding="utf-8"))
        for e in lex["entries"]:
            if e["kind"] == "tool" and e["status"] == "LIVE":
                tool_tokens[e["token"]] = ".tools/" + e["token"]
    tool_rx = re.compile("|".join(re.escape(t) for t in sorted(tool_tokens, key=len,
                                                               reverse=True))
                         ) if tool_tokens else None

    edges: dict = defaultdict(set)
    stats = {"sources_scanned": 0, "import_edges": 0, "path_edges": 0,
             "invoke_edges": 0, "dangling_out": defaultdict(int),
             "ambiguous_basenames_skipped": 0, "oversize_skipped": 0}
    known_roots = {p.split("/", 1)[0] for p in population if "/" in p}

    for row in rows:
        src, fclass = row["path"], row["class"]
        if fclass not in ("EXEC", "REG", "DOC") or row["handling"] == "EXCLUDE":
            continue
        if fclass == "RECORD":
            continue
        text = read_text(src)
        if not text:
            if (WS / src).exists() and (WS / src).stat().st_size > MAX_SOURCE_BYTES:
                stats["oversize_skipped"] += 1
            continue
        stats["sources_scanned"] += 1
        # channel 1: python AST imports
        if src.endswith(".py"):
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")  # scanned files' own bad escapes
                    tree = ast.parse(text)
            except SyntaxError:
                tree = None
            if tree is not None:
                src_dir = src.rsplit("/", 1)[0] if "/" in src else ""
                for node in ast.walk(tree):
                    mods = []
                    if isinstance(node, ast.Import):
                        mods = [a.name for a in node.names]
                    elif isinstance(node, ast.ImportFrom):
                        if node.level and node.module:
                            cand = f"{src_dir}/{node.module.replace('.', '/')}.py"
                            mods = []
                            if cand in population:
                                edges[src].add(cand)
                                stats["import_edges"] += 1
                        elif node.module:
                            mods = [node.module]
                    for m in mods:
                        for dst in dotted.get(m, [])[:4]:  # generous: all candidates
                            if dst != src:
                                edges[src].add(dst)
                                stats["import_edges"] += 1
        # channel 2: literal path tokens
        for tok in set(PATH_TOKEN.findall(text.replace("\\", "/"))):
            # strip the "./" PREFIX only -- lstrip("./") strips CHARWISE and turned
            # ".tools/x" into "tools/x", losing .tools edges AND manufacturing false
            # references into the no-dot tools/ dir (measured: "60 live referrers")
            while tok.startswith("./"):
                tok = tok[2:]
            if tok in population:
                if tok != src:
                    edges[src].add(tok)
                    stats["path_edges"] += 1
            elif "/" in tok and tok.split("/", 1)[0] in known_roots and "." in \
                    tok.rsplit("/", 1)[-1]:
                stats["dangling_out"][src] += 1
        # channel 2b: unique-basename references. Inverted to token-extraction-then-
        # lookup (the per-basename substring form was O(basenames x sources) ~ 1.4e8).
        # EXEC included: python reads registries via constructed relative paths where
        # only the literal BASENAME survives in source ("comp-tools.yaml") -- without
        # this the registry adjudication under-reports readers in the LEGACY-mislabel
        # direction, the risky one for that table.
        if fclass in ("DOC", "REG", "EXEC"):
            for tok in set(BASENAME_TOKEN.findall(text)):
                if len(tok) <= 8:
                    continue
                paths = basename_index.get(tok)
                if not paths:
                    continue
                if len(paths) == 1:
                    if paths[0] != src:
                        edges[src].add(paths[0])
                        stats["path_edges"] += 1
                else:
                    stats["ambiguous_basenames_skipped"] += 1
        # channel 3: tool-token invocations
        if fclass == "EXEC" and tool_rx is not None:
            for t in set(tool_rx.findall(text)):
                dst = tool_tokens[t]
                if dst in population and dst != src:
                    edges[src].add(dst)
                    stats["invoke_edges"] += 1
    return edges, stats


def closure(roots: set, edges: dict) -> dict:
    hops: dict = {r: 0 for r in roots}
    q = deque(roots)
    while q:
        cur = q.popleft()
        for dst in edges.get(cur, ()):
            if dst not in hops:
                hops[dst] = hops[cur] + 1
                q.append(dst)
    return hops


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cycle0", action="store_true",
                        help="emit the comp-tools dependency map + registry adjudication")
    parser.add_argument("--no-lexicon", action="store_true",
                        help="run with edge channel 3 (tool-token invocations) "
                             "explicitly DISABLED instead of refusing on a missing "
                             "lexicon.json; the boundary declaration is downgraded")
    args = parser.parse_args()

    scan_dir = newest_scan()
    rows = load_rows(scan_dir)
    population = {r["path"] for r in rows}
    print(f"[mark] scan vintage {scan_dir.name} -- population {len(rows)}")

    roots, why = build_root_set(population)
    edges, stats = build_edges(rows, no_lexicon=args.no_lexicon)
    hops = closure(roots, edges)

    in_degree: dict = defaultdict(int)
    for src, dsts in edges.items():
        if src in hops:  # only live in-edges count toward liveness-strength
            for d in dsts:
                in_degree[d] += 1

    marked_rows = []
    per_root: dict = defaultdict(lambda: [0, 0])
    for r in rows:
        p = r["path"]
        live = p in hops
        per_root[r["root"]][0 if live else 1] += 1
        marked_rows.append({
            "path": p, "reach_from_root": live,
            "reach_hops": hops.get(p), "reach_root_type": why.get(p),
            "ref_mech_in_live": in_degree.get(p, 0),
            "ref_dangling_out": stats["dangling_out"].get(p, 0),
        })
    with (scan_dir / "marked.jsonl").open("w", encoding="utf-8", newline="\n") as h:
        for row in marked_rows:
            h.write(json.dumps(row) + "\n")

    with (scan_dir / "edges.jsonl").open("w", encoding="utf-8", newline="\n") as h:
        for src in sorted(edges):
            h.write(json.dumps({"src": src, "dst": sorted(edges[src])}) + "\n")
    n_live = sum(1 for r in marked_rows if r["reach_from_root"])
    handling_of = {r["path"]: r["handling"] for r in rows}
    unmarked_scoreable = [r["path"] for r in marked_rows if not r["reach_from_root"]
                          and handling_of[r["path"]] == "SCORE"]
    print(f"[edges] sources {stats['sources_scanned']} -> import {stats['import_edges']} "
          f"+ path {stats['path_edges']} + invoke {stats['invoke_edges']} edges; "
          f"oversize skipped {stats['oversize_skipped']}, ambiguous basenames skipped "
          f"{stats['ambiguous_basenames_skipped']}, files w/ dangling refs "
          f"{len(stats['dangling_out'])}")
    print(f"[mark] MARKED {n_live} / {len(rows)} ({100 * n_live / len(rows):.1f}%); "
          f"UNMARKED-SCOREABLE (the candidate mass): {len(unmarked_scoreable)}")
    print(f"{'root':<22}{'marked':>8}{'unmarked':>10}")
    for root, (m, u) in sorted(per_root.items(), key=lambda x: -(x[1][0] + x[1][1]))[:16]:
        print(f"{root:<22}{m:>8}{u:>10}")

    if args.cycle0:
        print("\n[cycle0] comp-tools dependency map (reader-anchored)")
        tools = [p for p in population if p.startswith(".tools/") and "/" not in
                 p[len(".tools/"):]]
        reads_registry: dict = defaultdict(list)
        for t in sorted(tools):
            for dst in edges.get(t, ()):
                if dst in REGISTRY_CANDIDATES:
                    reads_registry[dst].append(t)
        print(f"  registry adjudication ({len(REGISTRY_CANDIDATES)} candidates):")
        for reg in REGISTRY_CANDIDATES:
            readers = reads_registry.get(reg, [])
            verdict = f"READ by {len(readers)} live tool(s)" if readers else \
                "ZERO live .tools readers (candidate LEGACY -- verify non-tool readers)"
            print(f"    {reg:<52} {verdict}")
        into_tools_dir = sorted({src for src, dsts in edges.items() if src in hops
                                 for d in dsts if d.startswith("tools/")})
        print(f"  tools/ (no-dot) referenced by {len(into_tools_dir)} LIVE source(s)"
              + (f": {into_tools_dir[:6]}" if into_tools_dir else
                 " -- ZERO live references into tools/ (516 files)"))
        cyc = {"tools": {t: sorted(edges.get(t, ())) for t in sorted(tools)},
               "registry_readers": {k: sorted(v) for k, v in reads_registry.items()},
               "tools_nodot_live_referrers": into_tools_dir}
        (scan_dir / "cycle0_comptools.json").write_text(json.dumps(cyc, indent=1),
                                                        encoding="utf-8")
        print(f"  wrote {scan_dir.name}/cycle0_comptools.json")

    print("[boundary] " + __doc__.split("BOUNDARY DECLARATION", 1)[1].strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
