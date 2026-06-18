"""
NFRA_TSGRAPH.P2-1 -- page-rooted component-cluster extractor (PAGE -> PANEL -> DRILLDOWN lens).

Extends the P1 ts-morph extractor's output (out/portal_full.graph.json -- the HEAD-current full-portal
semantic graph, portal-node counts == live canonical Nessie graph) with an ADDITIVE cluster layer on
the SAME CloudNode/CloudEdge schema (string discriminators, NO schema break -- mirrors the P4
props/SERVED_FROM derive precedent). The P1 extractor stays untouched (cutover-signed/load-bearing);
this is an additive post-pass over its emit (Rule 20: ride the live graph, never rebuild a traversal).

Model (Andrew-steered PAGE->PANEL->DRILLDOWN, PRD section 9):
  L1 Page          = route-root component, one per portal/src/pages feature-dir (or {Feature}.tsx root).
  L2 PanelCluster  = RENDERS-descendant components grouped by SHARED DATA-SOURCE via community detection
                     WITHIN the page (the 6-source superset: endpoint | served key | RQ key | shared
                     hook | shared type | gold artifact[via served key]).
  L3 Drilldown     = nested render-children under a panel (*Modal.tsx / *Detail.tsx / _partners/{firm}
                     cohort) -- FIRST-CLASS, carrying nesting-depth + the per-firm cohort axis.

Emits (additive):
  Page / PanelCluster nodes
  CLUSTERS            : Page -> PanelCluster
  CONTAINS_DRILLDOWN  : PanelCluster -> ReactComponent (depth 1 = panel member) and ReactComponent ->
                        ReactComponent (depth 2+ = nested drilldown) -- the page-rooted render subtree,
                        depth/kind/cohort on the edge; `*0..` traversal reaches the whole subtree.
  SHARES_SOURCE       : PanelCluster <-> PanelCluster (cross-panel), carrying the shared source + type --
                        generalizes `comp-cache collisions` (RQ-key-only) to the 6-source superset.

Coverage (AC4): every one of the 119 portal/src/pages/*.tsx files is accounted for -- assigned to a
page + cluster/drilldown, OR enumerated in coverage.unresolved with a reason. 0 silent Unknown.

Run: python cluster_extract.py            (writes out/portal_clusters.graph.json + .producer.json + report)
     python cluster_extract.py --page AdvisorIntelligence   (also prints the panel->drilldown tree)
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict, deque

HERE = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
IN_GRAPH = os.path.join(HERE, "out", "portal_full.graph.json")
OUT_GRAPH = os.path.join(HERE, "out", "portal_clusters.graph.json")
OUT_PRODUCER = os.path.join(HERE, "out", "portal_clusters.producer.json")
OUT_REPORT = os.path.join(HERE, "out", "portal_clusters.report.json")

PAGES_PREFIX = "portal/src/pages/"
# noise "endpoints" the P1 queryFn resolver picks up from .then()/promise chains -- NOT data identities
ENDPOINT_NOISE = {"then", "catch", "finally", "map", "filter", "json", "all", "race"}
# L2 panel-tier directory markers (PRD section 9)
PANEL_DIR_RE = re.compile(r"/(?:_shared/(?:panels|tabs|components|charts)|components|charts|tabs|panels)/")
COHORT_RE = re.compile(r"/_partners/([^/]+)/")
DRILLDOWN_FILE_RE = re.compile(r"(Modal|Detail|Drilldown|Drawer)\.tsx$")


def page_of(path: str) -> str | None:
    """Feature-dir page key for a portal/src/pages file, else None (not page-owned)."""
    if not path.startswith(PAGES_PREFIX):
        return None
    rest = path[len(PAGES_PREFIX):]
    seg = rest.split("/", 1)[0]
    if seg.endswith(".tsx") or seg.endswith(".ts"):
        return seg[:-4] if seg.endswith(".tsx") else seg[:-3]  # {Feature}.tsx -> Feature
    return seg  # feature-dir


def is_page_tsx(path: str) -> bool:
    return path.startswith(PAGES_PREFIX) and path.endswith(".tsx")


def main() -> int:
    page_arg = None
    if "--page" in sys.argv:
        page_arg = sys.argv[sys.argv.index("--page") + 1]

    with open(IN_GRAPH, "r", encoding="utf-8") as fh:
        g = json.load(fh)
    nodes = {n["id"]: n for n in g["nodes"]}
    edges = g["edges"]

    # ---- indices ----
    rc_by_path: dict[str, list[str]] = defaultdict(list)   # file -> [rc ids declared/extracted there]
    rc_name: dict[str, str] = {}                           # rc id -> component name
    rc_path: dict[str, str] = {}                           # rc id -> file
    for nid, n in nodes.items():
        if n["label"] == "ReactComponent":
            p = n["attrs"].get("path", "")
            rc_by_path[p].append(nid)
            rc_name[nid] = n["attrs"].get("name", nid)
            rc_path[nid] = p

    hooks_by_path: dict[str, list[str]] = defaultdict(list)
    for nid, n in nodes.items():
        if n["label"] == "Hook":
            hooks_by_path[n["attrs"].get("path", "")].append(nid)

    # edge adjacency by type
    out_e: dict[str, list[tuple[str, str]]] = defaultdict(list)  # label -> [(src,dst)]
    for e in edges:
        out_e[e["label"]].append((e["src"], e["dst"]))

    fetches = defaultdict(list)   # hook -> [endpoint]
    haskey = defaultdict(list)    # hook -> [rqk]
    for s, d in out_e["FETCHES"]:
        fetches[s].append(d)
    for s, d in out_e["HAS_KEY"]:
        haskey[s].append(d)
    reads_url = defaultdict(list)  # endpoint -> [servedurl]
    for s, d in out_e["READS_URL"]:
        reads_url[s].append(d)
    refs_type = defaultdict(list)  # module -> [typedecl]
    for s, d in out_e["REFERENCES_TYPE"]:
        refs_type[s].append(d)
    # type ubiquity (a type referenced by many files is not a discriminating source)
    type_fanin: dict[str, int] = defaultdict(int)
    for s, d in out_e["REFERENCES_TYPE"]:
        type_fanin[d] += 1

    # file-grain containment: jsx in file F instantiates child rc B  =>  every rc declared in F renders B
    contains: dict[str, set[str]] = defaultdict(set)  # parent rc -> {child rc}
    for s, d in out_e["INSTANTIATES"]:
        # s = jsx:{file}:{line}:{tag}
        m = re.match(r"^jsx:(.+?):\d+:", s)
        if not m:
            continue
        parent_file = m.group(1)
        for parent_rc in rc_by_path.get(parent_file, []):
            if parent_rc != d:
                contains[parent_rc].add(d)

    # ---- data-source set per FILE (the 6-source superset) ----
    def file_primary_sources(path: str) -> set[str]:
        """endpoint | rq-key | served-url -- the data IDENTITY (drives clustering)."""
        src: set[str] = set()
        for h in hooks_by_path.get(path, []):
            for ep in fetches.get(h, []):
                fn = ep.split("endpoint:", 1)[-1]
                if fn in ENDPOINT_NOISE:
                    continue
                src.add(ep)
                for u in reads_url.get(ep, []):
                    src.add(u)
            for k in haskey.get(h, []):
                src.add(k)
        # data-fetch declared directly in an api/endpoints file (rare for page files)
        return src

    def file_struct_sources(path: str) -> set[str]:
        """shared (non-ubiquitous) types -- structural coupling (drives cross-panel SHARES_SOURCE)."""
        mod = "module:" + path
        out: set[str] = set()
        for t in refs_type.get(mod, []):
            if type_fanin[t] <= 8:  # ubiquitous types (referenced by >8 files) are not discriminating
                out.add(t)
        return out

    # ---- assemble pages + their page-owned components ----
    # the authoritative 119 set = every portal/src/pages/*.tsx Module node
    page_tsx_set = sorted({n["attrs"]["path"] for n in g["nodes"]
                           if n["label"] == "Module" and is_page_tsx(n["attrs"].get("path", ""))})
    # clustering operates only on page .tsx that declare >=1 ReactComponent. A .tsx with none (a
    # constants/types/barrel .tsx -- no JSX-returning PascalCase symbol) is NOT force-clustered into a
    # hollow singleton -- it is enumerated VISIBLE in coverage.unresolved (no-silent-Unknown invariant).
    pages: dict[str, list[str]] = defaultdict(list)  # feature -> [page-owned component file paths]
    for path in page_tsx_set:
        if rc_by_path.get(path):
            pages[page_of(path)].append(path)

    # ---- per-page community detection over panel/component files ----
    out_nodes: list[dict] = []
    out_edges: list[dict] = []
    unresolved: list[dict] = []
    report_pages: dict[str, dict] = {}

    assigned_files: set[str] = set()

    for feature, files in sorted(pages.items()):
        # community detection: DOMINANT-SOURCE assignment. Each data-bearing file joins the cluster keyed
        # by its MOST-DISTINCTIVE primary source (lowest page-local fan-in; tie -> prefer the rq-key, then
        # lexical). Files sharing that most-characteristic data identity co-cluster. This is a direct
        # bipartite community assignment -- NO transitive union -- so source-rich tab files (DistributionTab's
        # ~3900 lines of useQuery) do NOT chain every panel into one giant component (the failure mode of
        # shared-source union-find). Broadly-shared sources surface as cross-cluster SHARES_SOURCE links.
        fprim: dict[str, set[str]] = {}
        fstruct: dict[str, set[str]] = {}
        for f in files:
            fprim[f] = file_primary_sources(f)
            fstruct[f] = file_struct_sources(f)
        fanin: dict[str, int] = defaultdict(int)
        for f in files:
            for s in fprim[f]:
                fanin[s] += 1

        def _dominant(f: str) -> str | None:
            if not fprim[f]:
                return None
            return min(fprim[f], key=lambda s: (fanin[s], 0 if s.startswith("rqk:") else 1, s))

        # within-page render-parent lookup (child file -> parent files of this page)
        parents_of: dict[str, set[str]] = defaultdict(set)
        for parent_rc, kids in contains.items():
            pf = rc_path.get(parent_rc)
            if pf not in fprim:  # parent must be a page file of THIS page
                continue
            for k in kids:
                kf = rc_path.get(k)
                if kf in fprim and kf != pf:
                    parents_of[kf].add(pf)

        # cluster HOME per file. Data-bearing -> its dominant-source key. Presentational (no primary
        # source) -> the cluster of its DOMINANT data-bearing render-ancestor (BFS up parents, majority
        # vote) -- a NON-merging assignment, so a shared helper rendered across panels homes to its top
        # user WITHOUT bridging those panels. No ancestor -> VISIBLE singleton (keyed by its own path).
        cluster_root: dict[str, str] = {}
        for f in files:
            ds = _dominant(f)
            if ds is not None:
                cluster_root[f] = "src::" + ds
        for f in files:
            if f in cluster_root:
                continue
            seen = {f}
            frontier = sorted(parents_of.get(f, ()))
            votes: dict[str, int] = defaultdict(int)
            hops = 0
            while frontier and hops < 12 and not votes:
                nxt: list[str] = []
                for p in frontier:
                    if p in seen:
                        continue
                    seen.add(p)
                    pd = _dominant(p)
                    if pd is not None:
                        votes["src::" + pd] += 1
                    else:
                        nxt.extend(parents_of.get(p, ()))
                frontier = sorted(nxt)
                hops += 1
            # deterministic: highest votes, then lexical cluster key (reproducible tiebreak)
            cluster_root[f] = max(votes.items(), key=lambda kv: (kv[1], kv[0]))[0] if votes else ("file::" + f)

        clusters: dict[str, list[str]] = defaultdict(list)
        for f in files:
            clusters[cluster_root[f]].append(f)

        page_id = f"page:{feature}"

        def _root_rank(f: str) -> tuple:
            if f == f"{PAGES_PREFIX}{feature}/index.tsx":
                return (0, len(f))
            if f == f"{PAGES_PREFIX}{feature}.tsx":
                return (1, len(f))
            if f.endswith("/index.tsx"):
                return (2, f.count("/"))
            return (3, f.count("/"))
        root_file = min(files, key=_root_rank)
        out_nodes.append({"id": page_id, "label": "Page", "attrs": {
            "name": feature, "featureDir": PAGES_PREFIX + feature, "rootFile": root_file,
            "pageFileCount": len(files), "clusterCount": len(clusters),
        }})

        page_report = {"feature": feature, "files": len(files), "clusters": [], "rootFile": root_file}

        cidx = 0
        for root, cfiles in sorted(clusters.items(), key=lambda kv: -len(kv[1])):
            cluster_id = f"cluster:{feature}:{cidx}"
            # cluster's data-sources (union of member primaries), label = dominant source
            csrc: set[str] = set()
            for f in cfiles:
                csrc |= fprim[f]
            # human label: the most-shared source (deterministic: max used_by, then lexical), else basename
            label = (max(sorted(csrc), key=lambda s: (sum(1 for f in cfiles if s in fprim[f]), s))
                     if csrc else os.path.basename(cfiles[0]))
            out_nodes.append({"id": cluster_id, "label": "PanelCluster", "attrs": {
                "page": feature, "index": cidx, "label": _short(label),
                "memberFileCount": len(cfiles),
                "sources": sorted(_short(s) for s in csrc)[:25],
                "sourceCount": len(csrc),
            }})
            out_edges.append({"src": page_id, "dst": cluster_id, "label": "CLUSTERS", "attrs": {}})

            # CONTAINS_DRILLDOWN: page-rooted render subtree per cluster, depth/kind/cohort first-class
            # member rc ids in this cluster
            member_rcs = [rc for f in cfiles for rc in rc_by_path.get(f, [])]
            member_rc_set = set(member_rcs)
            # roots of the subtree = member rcs not rendered by another member rc (in-cluster)
            rendered_by_member: set[str] = set()
            for prc in member_rcs:
                for c in contains.get(prc, ()):
                    if c in member_rc_set:
                        rendered_by_member.add(c)
            roots = [rc for rc in member_rcs if rc not in rendered_by_member] or member_rcs

            # BFS the in-cluster containment subtree, emit cluster->root (depth1) + parent->child (depth+1)
            seen: dict[str, int] = {}
            dq: deque[str] = deque()
            cluster_report_members = []
            for r in roots:
                out_edges.append({"src": cluster_id, "dst": r, "label": "CONTAINS_DRILLDOWN",
                                  "attrs": _dd_attrs(rc_path[r], 1)})
                seen[r] = 1
                dq.append(r)
            while dq:
                cur = dq.popleft()
                depth = seen[cur]
                for child in sorted(contains.get(cur, ())):
                    if child not in member_rc_set:
                        continue  # stay within the page-owned cluster (boundary visible via shared layer)
                    if child in seen:
                        continue
                    seen[child] = depth + 1
                    out_edges.append({"src": cur, "dst": child, "label": "CONTAINS_DRILLDOWN",
                                      "attrs": _dd_attrs(rc_path[child], depth + 1)})
                    dq.append(child)
            for rc in member_rcs:
                d = seen.get(rc)
                a = _dd_attrs(rc_path[rc], d or 1)
                cluster_report_members.append({"component": rc_name[rc], "file": rc_path[rc],
                                               "depth": d, "kind": a["kind"], "cohort": a["cohort"]})
            for f in cfiles:
                assigned_files.add(f)
            page_report["clusters"].append({
                "id": cluster_id, "label": _short(label), "memberFiles": len(cfiles),
                "sources": sorted(_short(s) for s in csrc)[:12], "members": cluster_report_members,
            })
            cidx += 1

        # SHARES_SOURCE: link distinct PanelClusters that share a primary DATA source (the page-level
        # identity used across panels, e.g. firm-leaderboard across AdvisorsTab + ClientsTab) or a shared
        # non-ubiquitous TYPE. One edge per cluster-pair, listing all shared sources. Generalizes
        # `comp-cache collisions` (RQ-key only) to the 6-source superset.
        root_to_cidx = {root: i for i, (root, _) in enumerate(
            sorted(clusters.items(), key=lambda kv: -len(kv[1])))}
        src_clusters: dict[str, set[str]] = defaultdict(set)   # primary source -> clusters using it
        type_clusters: dict[str, set[str]] = defaultdict(set)  # structural type -> clusters using it
        for f in files:
            r = cluster_root[f]
            for s in fprim[f]:
                src_clusters[s].add(r)
            for t in fstruct[f]:
                type_clusters[t].add(r)
        pair_shared: dict[tuple, dict] = {}
        for kind, mapping in (("data", src_clusters), ("type", type_clusters)):
            for item, cs in mapping.items():
                cl = sorted(cs)
                for i in range(len(cl)):
                    for j in range(i + 1, len(cl)):
                        d = pair_shared.setdefault((cl[i], cl[j]), {"data": set(), "type": set()})
                        d[kind].add(_short(item))
        for (a, b), d in pair_shared.items():
            ca = f"cluster:{feature}:{root_to_cidx[a]}"
            cb = f"cluster:{feature}:{root_to_cidx[b]}"
            out_edges.append({"src": ca, "dst": cb, "label": "SHARES_SOURCE", "attrs": {
                "sharedSources": sorted(d["data"])[:10],
                "sharedTypes": sorted(d["type"])[:10],
                "sharedCount": len(d["data"]) + len(d["type"]),
                "sourceType": ("data+type" if d["data"] and d["type"] else ("data" if d["data"] else "type")),
            }})
        report_pages[feature] = page_report

    # ---- coverage: every 119 page .tsx accounted for ----
    for f in page_tsx_set:
        if f in assigned_files:
            continue
        # a page .tsx with no ReactComponent extracted (e.g. a barrel/re-export, a non-component .tsx)
        has_rc = bool(rc_by_path.get(f))
        unresolved.append({
            "cat": "cluster_assign", "what": f, "where": page_of(f),
            "reason": ("page .tsx declares no extracted ReactComponent (barrel/re-export/constants .tsx -- "
                       "no JSX-returning PascalCase symbol)" if not has_rc
                       else "page .tsx has components but none landed in a cluster (orphan -- investigate)"),
        })

    # ---- emit (sort nodes/edges for byte-stable, diff-friendly, reproducible output) ----
    out_nodes.sort(key=lambda n: (n["label"], n["id"]))
    out_edges.sort(key=lambda e: (e["label"], e["src"], e["dst"]))
    out = {
        "meta": {
            "project": "NFRA_TSGRAPH.P2-1 cluster layer (additive)",
            "source_graph": "out/portal_full.graph.json (P1 full-portal emit; portal counts == live Nessie)",
            "model": "PAGE(L1) -> PanelCluster(L2, community-detected by shared data-source) -> Drilldown(L3, depth+cohort)",
            "schema": "ADDITIVE -- new node_type {Page,PanelCluster} + edge_type {CLUSTERS,CONTAINS_DRILLDOWN,SHARES_SOURCE} on CloudNode/CloudEdge",
            "note": "SPIKE/P2 output -- additive layer; AE (P2-2) materializes into canonical Nessie. Verify vs the running portal, never the graph (Rule F5).",
        },
        "metrics": {
            "page_tsx_total": len(page_tsx_set),
            "page_tsx_assigned": len(assigned_files),
            "page_tsx_unresolved": len(unresolved),
            "pages": len(pages),
            "panel_clusters": sum(1 for n in out_nodes if n["label"] == "PanelCluster"),
            "nodes_by_label": _count_label(out_nodes),
            "edges_by_label": _count_label(out_edges, key="label"),
        },
        "unresolved": unresolved,
        "nodes": out_nodes,
        "edges": out_edges,
    }
    os.makedirs(os.path.dirname(OUT_GRAPH), exist_ok=True)
    with open(OUT_GRAPH, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2)

    # producer contract (AE derive ingest -- additive nodes/edges only)
    producer = {
        "producer": "ts-semantic-clusters",
        "generated_at": "STAMP_AT_STAGE",  # plain post-pass; AE re-stamps at derive (Date.now non-determinism avoided)
        "slice": "portal-clusters-p2-1",
        "nodes": [{"id": n["id"], "type": n["label"], **n["attrs"]} for n in out_nodes],
        "edges": [{"source": e["src"], "target": e["dst"], "edge_type": e["label"], **e["attrs"]} for e in out_edges],
        "coverage": {
            "node_count": len(out_nodes), "edge_count": len(out_edges),
            "page_tsx_total": len(page_tsx_set), "page_tsx_assigned": len(assigned_files),
            "unresolved": unresolved,
        },
    }
    with open(OUT_PRODUCER, "w", encoding="utf-8") as fh:
        json.dump(producer, fh, indent=2)

    with open(OUT_REPORT, "w", encoding="utf-8") as fh:
        json.dump({"metrics": out["metrics"], "pages": report_pages, "unresolved": unresolved}, fh, indent=2)

    # ---- console summary ----
    print(f"OK: {len(pages)} pages, {out['metrics']['panel_clusters']} panel clusters")
    print(f"OK: nodes {out['metrics']['nodes_by_label']}")
    print(f"OK: edges {out['metrics']['edges_by_label']}")
    print(f"OK: coverage page-tree .tsx = {len(assigned_files)}/{len(page_tsx_set)} assigned, "
          f"{len(unresolved)} VISIBLE unresolved (0 silent)")
    print("OK: wrote out/portal_clusters.graph.json + .producer.json + .report.json")

    if page_arg and page_arg in report_pages:
        _print_tree(report_pages[page_arg])
    return 0


def _short(s: str) -> str:
    for pre in ("endpoint:", "rqk:", "endpointurl:", "type:"):
        if s.startswith(pre):
            return s[len(pre):]
    return s


def _dd_attrs(path: str, depth: int) -> dict:
    cohort = None
    m = COHORT_RE.search(path)
    if m:
        cohort = m.group(1)
    if cohort:
        kind = "cohort"
    elif DRILLDOWN_FILE_RE.search(path):
        kind = "modal" if "Modal" in path else ("detail" if "Detail" in path else "drilldown")
    elif depth == 1:
        kind = "panel"
    else:
        kind = "nested"
    return {"depth": depth, "kind": kind, "cohort": cohort}


def _count_label(items: list[dict], key: str = "label") -> dict:
    out: dict[str, int] = defaultdict(int)
    for x in items:
        out[x[key]] += 1
    return dict(out)


def _print_tree(pr: dict) -> None:
    print(f"\n===== {pr['feature']} (root={pr['rootFile']}, {pr['files']} page files) =====")
    for c in pr["clusters"]:
        print(f"  [cluster {c['id']}]  label={c['label']}  members={c['memberFiles']}  sources={c['sources']}")
        for m in sorted(c["members"], key=lambda m: (m["depth"] or 99, m["file"])):
            ind = "    " + "  " * ((m["depth"] or 1))
            tag = f"<{m['kind']}" + (f" cohort={m['cohort']}" if m["cohort"] else "") + ">"
            print(f"{ind}d{m['depth']} {m['component']} {tag}  ({m['file'].split('/')[-1]})")


if __name__ == "__main__":
    sys.exit(main())
