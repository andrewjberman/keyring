"""
nerves_lexical -- NFRA_NERVES L3b: THE LEXICAL UNLOCK. Danger zones become graph-native.

THE GAP THIS CLOSES, stated plainly:

    The danger zones are ALREADY WRITTEN DOWN. Holds, frozen files, incident costs, stamp-order
    traps -- in memory/, the ledgers, CLAUDE.md, the critical-path docs, WITH file:line citations.
    And an agent running `comp-blast` on a frozen file gets NO WARNING unless it happened to read
    the prose. Fully lexical. Zero graph presence.

    That is the gap that nearly cost us the estate three times.

This entity-links the corpus onto the nodes it protects or indicts, so the danger map becomes an
ACTIVE IMMUNE RESPONSE instead of a wiki. `comp-blast build_assets_dim.py` RETURNS THE HOLD.

EDGE CLASSES (doc -> node), each carrying its CITATION (a claim without a citation is not a claim,
CLAUDE.md 22 -- so every edge here names its doc + line, and a reader can go check it):

  HOLD      a standing prohibition / freeze on the node. THE LOUDEST. ("NEVER", "FROZEN", "DO NOT",
            "HELD", "prohibition", "hard stop", a critical_paths/HOLD_* doc.)
  RISK      an incident/defect/cost the node was implicated in. ("incident", "broke", "corrupted",
            "$", "P0", "catastrophic", "postmortem".)
  DOCTRINE  a rule that binds behaviour around the node (CLAUDE.md law, doctrine docs, memory
            feedback). Not a prohibition on the node itself -- a way you must treat it.

ADDRESSING IS L2's KEYSTONE (nerves_resolve) -- this module does NOT invent a second resolver.

HONESTY: a mention is EVIDENCE, not proof. Every edge carries `confidence` (EXACT node-id/path
match vs a basename that could be several things) and its quote. UNKNOWN is a band: a doc that
names nothing addressable is reported, never silently dropped.

Read-only. Emits org/modules/graph/nerves-risk-edges.json (tracked -- the danger map is reviewable
by construction).

Usage:
    nerves_lexical scan [--json]        # the edges + their citations
    nerves_lexical build                # emit the edge file
    nerves_lexical check <node>         # what does the corpus SAY about this node?
    nerves_lexical --self-test
Author: 1.0.0_SA_CTO~Z (NFRA_NERVES L3b). 2026-07-14.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.normpath(os.path.join(_HERE, "..", "..", ".."))
sys.path.insert(0, _HERE)

from nerves_resolve import resolve  # noqa: E402

OUT = os.path.join(_HERE, "nerves-risk-edges.json")

# The corpus: where the estate writes down what it knows about danger.
_CORPUS = [
    ("CLAUDE.md", "DOCTRINE"),                       # the law
    ("org/critical_paths", "HOLD"),                  # holds / freezes / runbooks
    ("org/tier0/ledger", "DOCTRINE"),                # decision records
    ("docs/doctrine", "DOCTRINE"),
    ("docs/references", "RISK"),                     # incident records
]
# memory/ lives outside the repo (the agent memory dir) -- included when present.
_MEMORY_DIR = os.path.expanduser(
    "~/.claude/projects/C--Users-AndrewBerman-Desktop-ajb-workspace/memory")

# Language that ESCALATES a mention. Order matters: HOLD dominates RISK dominates DOCTRINE.
_HOLD_RX = re.compile(
    r"\b(NEVER|FROZEN|FREEZE|DO NOT|DON'T TOUCH|HELD|HOLD|PROHIBIT|PROHIBITION|FORBIDDEN|"
    r"HARD STOP|STOP|SEALED|must not|never rewrite|no verb touches)\b", re.I)
_RISK_RX = re.compile(
    r"\b(incident|postmortem|post-mortem|P0|SEV1|broke|broken|corrupt|catastroph|outage|"
    r"regression|defect|silently|lost|deleted|mis-?attribut|false|wrong)\b", re.I)

# Node-shaped references worth resolving out of prose.
_REF_RX = re.compile(
    r"`([^`\n]{3,80})`"                                   # inline-code (the usual citation form)
    r"|\b([\w./-]+\.(?:py|tsx?|jsx?|json|ya?ml|sh|tf|parquet))\b"   # a file
    r"|\b(s3://[\w./-]+)"                                  # an s3 uri
    r"|\b((?:opal|bd|inf|cot|mdpf)-[\w-]{3,})\b")          # a bucket/lambda-ish estate name


def _iter_docs():
    for rel, default_kind in _CORPUS:
        p = os.path.join(_WS, rel)
        if os.path.isfile(p):
            yield p, rel, default_kind
        elif os.path.isdir(p):
            for root, _d, files in os.walk(p):
                for fn in sorted(files):
                    if fn.endswith(".md"):
                        fp = os.path.join(root, fn)
                        yield fp, os.path.relpath(fp, _WS).replace("\\", "/"), default_kind
    if os.path.isdir(_MEMORY_DIR):
        for fn in sorted(os.listdir(_MEMORY_DIR)):
            if fn.endswith(".md"):
                yield os.path.join(_MEMORY_DIR, fn), "memory/" + fn, "DOCTRINE"


def _classify(line: str, doc_rel: str, default_kind: str) -> str:
    """HOLD > RISK > DOCTRINE. A hold DOC makes every mention in it at least suspect; the LINE's own
    language can escalate. We never DE-escalate a hold doc."""
    is_hold_doc = "critical_paths" in doc_rel and ("HOLD" in doc_rel.upper()
                                                   or "DOOR" in doc_rel.upper())
    if is_hold_doc or _HOLD_RX.search(line):
        return "HOLD"
    if _RISK_RX.search(line):
        return "RISK"
    return default_kind


def scan(max_edges_per_node: int = 6):
    """-> (edges, stats). Every edge carries doc + LINE NUMBER + the quote: a claim without a
    citation is not a claim."""
    by_node = defaultdict(list)
    ambiguous_refs = []
    docs_scanned = docs_with_no_addressable_ref = 0
    for path, rel, default_kind in _iter_docs():
        docs_scanned += 1
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                lines = fh.readlines()
        except OSError:
            continue
        found_any = False
        for i, line in enumerate(lines, 1):
            if len(line) > 2000:
                line = line[:2000]
            for m in _REF_RX.finditer(line):
                ref = next((g for g in m.groups() if g), "")
                ref = ref.strip().strip("`,.:;()[]")
                if not ref or len(ref) < 4:
                    continue
                r = resolve(ref)
                if not r.addressed:
                    continue
                kind = _classify(line, rel, default_kind)
                # > 1, not > 2: several candidates IS ambiguous (nerves_resolve.py AMBIGUOUS state, WP-4 ruling);
                # at > 2 a two-way ambiguous DOCTRINE/RISK ref was KEPT as a claim, against the split below.
                # (1.0.0_SA_CTO~X 2026-08-28 on 0.4.0_DT_ClientPlatform~X 78718.)
                ambiguous = len(r.node_ids) > 1
                # THE PRECISION/SAFETY SPLIT -- the two errors are NOT symmetric:
                #   DOCTRINE/RISK on an ambiguous ref -> DROP. A false claim here is pure noise, and
                #     a danger map with false claims trains agents to IGNORE the warning.
                #   HOLD on an ambiguous ref -> KEEP, on every candidate, MARKED ambiguous. A missed
                #     HOLD can cost the estate; a noisy one costs an agent ten seconds of reading the
                #     citation. `_orion_api_silver_lib.py` -- ONE OF THE THREE FROZEN FILES -- has SIX
                #     copies (the vendored-fork problem the frozen-three hold is partly ABOUT), so a
                #     pure precision gate silently dropped the hold on the most dangerous class of
                #     file in the estate. OVER-WARN ON A HOLD. NEVER UNDER-WARN.
                if ambiguous and kind != "HOLD":
                    ambiguous_refs.append(ref)
                    continue
                found_any = True
                for nid in r.node_ids[:6]:
                    by_node[nid].append({
                        "kind": kind,
                        "doc": rel,
                        "line": i,                      # THE CITATION
                        "ref": ref,
                        "confidence": r.confidence,
                        "ambiguous": ambiguous,         # stated, never hidden
                        "quote": line.strip()[:180],
                    })
        if not found_any:
            docs_with_no_addressable_ref += 1

    edges = []
    for nid, claims in by_node.items():
        # HOLD first, then RISK, then DOCTRINE; strongest citations first.
        order = {"HOLD": 0, "RISK": 1, "DOCTRINE": 2}
        claims.sort(key=lambda c: (order.get(c["kind"], 9), c["doc"]))
        kinds = sorted({c["kind"] for c in claims}, key=lambda k: order.get(k, 9))
        edges.append({
            "node": nid,
            "severity": kinds[0],                     # the strongest claim binds
            "kinds": kinds,
            "n_claims": len(claims),
            "claims": claims[:max_edges_per_node],
        })
    edges.sort(key=lambda e: ({"HOLD": 0, "RISK": 1, "DOCTRINE": 2}.get(e["severity"], 9),
                              -e["n_claims"]))
    from collections import Counter as _C
    stats = {
        "docs_scanned": docs_scanned,                        # THE DENOMINATOR
        "docs_with_no_addressable_ref": docs_with_no_addressable_ref,
        "refs_dropped_as_too_ambiguous": len(ambiguous_refs),
        "top_ambiguous_refs": [r for r, _n in _C(ambiguous_refs).most_common(8)],
        "nodes_with_claims": len(edges),
        "by_severity": {k: sum(1 for e in edges if e["severity"] == k)
                        for k in ("HOLD", "RISK", "DOCTRINE")},
        "total_claims": sum(e["n_claims"] for e in edges),
    }
    return edges, stats


def _render(edges, stats, top=18):
    L = ["nerves-lexical -- the LEXICAL UNLOCK (NFRA_NERVES L3b): the danger map becomes graph-native",
         "  DENOMINATOR: %d corpus docs scanned | %d named nothing addressable (reported, not dropped)"
         % (stats["docs_scanned"], stats["docs_with_no_addressable_ref"]),
         "  NODES WITH CLAIMS: %d   (HOLD %d | RISK %d | DOCTRINE %d)  from %d citations"
         % (stats["nodes_with_claims"], stats["by_severity"]["HOLD"], stats["by_severity"]["RISK"],
            stats["by_severity"]["DOCTRINE"], stats["total_claims"]),
         "  DROPPED as TOO AMBIGUOUS: %d refs (a ref matching >2 nodes cannot pin a claim to any one"
         % stats["refs_dropped_as_too_ambiguous"],
         "     of them -- a false HOLD trains agents to ignore the map). e.g. %s"
         % ", ".join(stats["top_ambiguous_refs"][:5]),
         "",
         "  THE HOLDS (the loudest -- an agent touching these must SEE this):"]
    holds = [e for e in edges if e["severity"] == "HOLD"][:top]
    for e in holds:
        L.append("    %s   (%d claims)" % (e["node"], e["n_claims"]))
        c = e["claims"][0]
        L.append("       %s:%d  \"%s\"" % (c["doc"], c["line"], c["quote"][:100]))
    if not holds:
        L.append("    (none)")
    return "\n".join(L)


def claims_for(node_id: str, edges=None):
    """The consumer API: what does the corpus SAY about this node?"""
    if edges is None:
        if not os.path.exists(OUT):
            return None
        try:
            edges = json.load(open(OUT, encoding="utf-8")).get("edges", [])
        except Exception:  # noqa: BLE001
            return None
    for e in edges:
        if e["node"] == node_id:
            return e
    return None


def _self_test() -> int:
    results = []
    def ck(name, ok, detail=""):
        results.append(ok)
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   ({detail})" if detail else ""))

    # classification: a hold doc + NEVER language escalate; plain prose does not.
    ck("classify.never_is_a_hold",
       _classify("NEVER rewrite historical bronze keys", "org/tier0/ledger/LD-1.md", "DOCTRINE") == "HOLD")
    ck("classify.hold_doc_dominates",
       _classify("just a mention", "org/critical_paths/HOLD_INF_X.md", "HOLD") == "HOLD")
    ck("classify.incident_is_risk",
       _classify("this caused a P0 outage and corrupted the served spine",
                 "docs/references/INCIDENTS.md", "RISK") == "RISK")
    ck("classify.plain_is_doctrine",
       _classify("the script reads a parquet", "org/tier0/ledger/LD-1.md", "DOCTRINE") == "DOCTRINE")

    edges, stats = scan()
    ck("live.corpus_scanned", stats["docs_scanned"] > 50, f"{stats['docs_scanned']} docs")
    ck("live.holds_found", stats["by_severity"]["HOLD"] > 0,
       f"{stats['by_severity']['HOLD']} nodes carry a HOLD")

    # THE ACCEPTANCE (the brief's, verbatim): a HOLD edge on a FROZEN-THREE file must exist and be
    # returnable. This is the sentence the whole layer exists for.
    frozen = ["build_assets_dim", "_orion_api_silver_lib", "convert_transactions_to_silver"]
    covered = {f: False for f in frozen}
    for e in edges:
        for f in frozen:
            if f in e["node"] and e["severity"] == "HOLD":
                covered[f] = True
    # ALL THREE. Not "at least one" -- the frozen three are a SET, and a hold on two of three is a
    # hold on none (the runner FATALs on whichever one you did not fix; that is the Door-5 lesson).
    ck("ACCEPTANCE.ALL_THREE_frozen_files_carry_a_HOLD", all(covered.values()),
       f"{ {k: v for k, v in covered.items()} }")
    # every claim carries its CITATION (doc + line) -- a claim without one is not a claim.
    ck("citation.every_claim_cites_doc_and_line",
       all(c.get("doc") and c.get("line") for e in edges for c in e["claims"]))

    ok = all(results)
    print("\n" + ("OK: THE LEXICAL UNLOCK -- the danger map is graph-native and every claim cites its line"
                  if ok else "ERROR: nerves_lexical self-test FAILED"))
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(prog="nerves-lexical")
    ap.add_argument("cmd", nargs="?", default="scan", choices=["scan", "build", "check"])
    ap.add_argument("node", nargs="?", default="")
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

    if args.cmd == "check":
        r = resolve(args.node)
        nid = r.node_ids[0] if r.addressed else args.node
        e = claims_for(nid)
        if not e:
            print("nerves-lexical: the corpus says NOTHING addressable about %s." % nid)
            print("  (That is an ABSENCE OF EVIDENCE, not evidence of safety -- the corpus may")
            print("   describe it in prose this linker could not address. UNKNOWN is a band.)")
            return 3
        print("nerves-lexical: %s -- %s (%d claims)" % (e["node"], e["severity"], e["n_claims"]))
        for c in e["claims"]:
            print("  [%s] %s:%d  \"%s\"" % (c["kind"], c["doc"], c["line"], c["quote"][:120]))
        return 0

    edges, stats = scan()
    if args.cmd == "build":
        doc = {"_README": "NFRA_NERVES L3b -- the LEXICAL UNLOCK. Danger zones (holds/risks/doctrine) "
                          "entity-linked from the corpus onto the nodes they protect or indict. Every "
                          "claim carries its doc + LINE (a claim without a citation is not a claim). "
                          "A mention is EVIDENCE, not proof -- confidence is stated. Regenerate: "
                          "nerves_lexical build.",
               "stats": stats, "edges": edges}
        # Atomic publish: a bare dump onto OUT lets a reader (or the comp-pulse auto-refresh,
        # which serializes only COMMIT-PATH rebuilds) see torn JSON mid-write. tmp + os.replace
        # makes the swap atomic on the same filesystem.
        tmp = OUT + ".tmp"
        with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(doc, fh, indent=1)
        os.replace(tmp, OUT)
        print("nerves-lexical: %d nodes carry claims -> %s"
              % (len(edges), os.path.relpath(OUT, _WS)))
    if args.json:
        print(json.dumps({"stats": stats, "edges": edges[:40]}, indent=1))
    else:
        print(_render(edges, stats))
    return 0


if __name__ == "__main__":
    sys.exit(main())
