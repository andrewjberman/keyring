#!/usr/bin/env python3
"""c2_canonical_compose -- NFRA_ONTOLOGY.R1-RARITY LEG 1: the CANONICAL-FAMILY C2 instance composer
(SERVED_LINEAGE first).

Composes, from the canonical graph, instance-grain C2 rows for the three SERVED_LINEAGE-bound
canonical families -- publish-serve, scheduled-publish, generative-publish (api-serve EXCLUDED AND
STATED: its defining AUTH leg's TRIGGERS-to-the-auth-edge is unmodeled; an unmodeled edge excluded
loudly beats a fourth family matched wrong). Design RATIFIED by 4.0.0_SA_CRO 64086 against the
rider spec C2_RARITY_COORDINATE_RIDER_SPEC_20260820.md.

KEY-SPACE LAW (CRO 64057, the three-family-key-spaces measurement): instance rows carry the
canonical family key as `motif_family` UNDER ITS OWN NAME -- never overloading `family` (the A/B
motif sense) or the thread sub-family sense. No canonical family CLASS rows exist in the graph yet
(the 19 class rows are the A/B + debt planes); the binding is BY THIS PROP, and class-row minting
is NOT this leg's act.

THE COMPOSE CONTRACT mirrors c2_individuate.compose (the derive's live arm): compose() takes
(query_fn, vintage_fn), does NO file I/O, and returns the envelope doc -- so the derive can call it
beside the A/B composer when CTO/CTO~B route the hook + image rebuild. Run locally it reads the
canonical kuzu DB through kuzu_cli --json (argv list, no shell layer -- the liveness harness's own
lesson).

LOUD ZERO (CRO 64086's negative-half discipline): if the substrate this composer matches on is
ABSENT (no ServedURL nodes, no READS_URL edges), it returns a doc whose counts are zero WITH
substrate_absent naming exactly which population was empty -- never a quiet empty list. The
absent-substrate state is the world the in-container run may meet first.

INSTANCE IDENTITY is content-addressed via THE NORMATIVE HOME (precondition_token.py
_request_hash; COO 64098: the derivation home lives in the contract, not at a line number) over
{"family": motif_family_or_null, "url": served_url_node_id, "members": sorted_member_ids}.

Rule-16/lane: engine home org/modules/graph/ (AE lane); a later move to the CVO harness dir is
CVO's home call (CRO 64086) and is a file move, not a redesign.
Author: 0.8.0_AE_CloudComp (NFRA_ONTOLOGY.R1-RARITY, COO GO 64034).
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
_KUZU_CLI = os.path.join(WS, "infra", "aws", "globgrph", "kuzu_cli.py")
_PRECOND_DIR = os.path.join(WS, "org", "tier2_senior", "0.7.0_AE_CloudOps", "deliverables",
                            "NFRA_EPISTEMY.C10-PRECOND")
PRODUCER = "NFRA_ONTOLOGY.R1-RARITY LEG 1 (0.8.0_AE_CloudComp) -- canonical-family C2 instance composer, SERVED_LINEAGE first"
SL_FAMILIES = ("publish-serve", "scheduled-publish", "generative-publish")
EXCLUDED_STATED = ("api-serve: EXCLUDED -- its defining AUTH leg (TRIGGERS to the auth edge) is "
                   "unmodeled on the canonical graph (PH2-C2 sourcing table); excluded loudly, not matched wrong")
# generative markers on a producer name -- a fixed, inspectable list, not an inference
_GENERATIVE_MARKERS = ("sentiment", "ai-", "-ai", "semantic", "clustering", "generative", "llm", "gpt")


def _normative_hash():
    if _PRECOND_DIR not in sys.path:
        sys.path.insert(0, _PRECOND_DIR)
    import precondition_token  # noqa: PLC0415
    return precondition_token._request_hash  # noqa: SLF001 -- the named normative home


def _cli_query_fn(q: str) -> list:
    """Default local reader: kuzu_cli --json via an argv list (no shell layer). The derive passes
    its own in-container reader instead; retrieval failure RAISES -- it is never an empty result."""
    p = subprocess.run([sys.executable, _KUZU_CLI, "--json", q],
                       capture_output=True, text=True, timeout=600, cwd=WS)
    if p.returncode != 0:
        raise RuntimeError("kuzu query failed rc=%d: %s" % (p.returncode, p.stderr.strip()[:200]))
    out = p.stdout.strip()
    start = out.find("[")
    if start < 0:
        raise RuntimeError("kuzu query returned no JSON array (a failed retrieval is not a zero)")
    return json.loads(out[start:])


def _cli_vintage_fn() -> dict:
    """The provenance header's snapshot ids, from the same engine's stderr on a trivial query."""
    p = subprocess.run([sys.executable, _KUZU_CLI, "--json", "MATCH (n:CloudNode) RETURN count(n) AS n"],
                       capture_output=True, text=True, timeout=600, cwd=WS)
    v = {}
    for line in p.stderr.splitlines():
        t = line.strip()
        if t.startswith("nodes snapshot-id:"):
            v["nodes_snapshot_id"] = t.split(":", 1)[1].strip()
        elif t.startswith("edges snapshot-id:"):
            v["edges_snapshot_id"] = t.split(":", 1)[1].strip()
    return v


def _family_for(producers: list, triggers: list) -> tuple:
    """(motif_family | None, family_resolution). The discriminator ladder, each rung derivable:
    generative marker on a producer name -> generative-publish; a cron/rate trigger -> scheduled-publish;
    a non-cron trigger -> publish-serve; no producer/trigger plane joined -> UNRESOLVED, loudly."""
    for pr in producers:
        name = (pr.get("name") or "").lower()
        if any(m in name for m in _GENERATIVE_MARKERS):
            return ("generative-publish", "producer name carries a generative marker (%s)" % name)
    crons = [t for t in triggers if "cron(" in (t.get("props") or "") or "rate(" in (t.get("props") or "")]
    if crons:
        return ("scheduled-publish", "producer trigger carries a cron/rate schedule expression")
    if triggers:
        return ("publish-serve", "producer trigger is event-driven (non-cron)")
    if producers:
        return (None, "UNRESOLVED: producer found but NO trigger edge joined (the trigger plane does not "
                      "reach this producer in the graph) -- scheduled vs event undiscriminable, not guessed")
    return (None, "UNRESOLVED: no producer joined (SERVED_FROM edge absent for this url, or no WRITES_S3 "
                  "producer on the resolved key) -- the family needs the producer plane, not guessed")


def compose(query_fn=None, vintage_fn=None) -> dict:
    """Compose the SERVED_LINEAGE canonical-family instance layer and RETURN it. No file I/O."""
    q = query_fn or _cli_query_fn
    rh = _normative_hash()
    urls = q("MATCH (n:CloudNode) WHERE n.node_type='ServedURL' RETURN n.node_id AS id, n.name AS name")
    reads = q("MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) WHERE e.edge_type='READS_URL' "
              "RETURN a.node_id AS ep, b.node_id AS url")
    # LOUD ZERO -- the substrate check precedes everything (never a quiet empty)
    if not urls or not reads:
        return {"producer": PRODUCER, "substrate_absent":
                "SUBSTRATE ABSENT: ServedURL=%d READS_URL=%d -- the served plane this composer matches on "
                "is not present in this graph vintage; ZERO instances is an ARTIFACT OF THE SUBSTRATE, not a "
                "measurement of the estate" % (len(urls), len(reads)),
                "excluded_stated": EXCLUDED_STATED,
                "counts": {"spine_instances": 0, "by_family": {}, "family_resolved": 0, "family_unresolved": 0,
                           "contains_edges": 0},
                "nodes": [], "edges": [], "graph_vintage": (vintage_fn or _cli_vintage_fn)()}
    fetches = q("MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) WHERE e.edge_type='IS_ENDPOINT' "
                "RETURN a.node_id AS df, b.node_id AS ep")
    hooks = q("MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) WHERE e.edge_type='FETCHES' "
              "RETURN a.node_id AS hk, b.node_id AS ep")
    served_from = q("MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) WHERE e.edge_type='SERVED_FROM' "
                    "RETURN a.node_id AS url, e.props AS props")
    writers = q("MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) WHERE e.edge_type='WRITES_S3' "
                "RETURN a.node_id AS producer, a.name AS name, a.node_type AS ptype, b.node_id AS key")
    trig = q("MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) WHERE e.edge_type='TRIGGERS' "
             "RETURN a.node_id AS t, a.props AS props, b.node_id AS target, b.name AS tname")

    ep_by_url, df_by_ep, hk_by_ep, sf_by_url = {}, {}, {}, {}
    for r in reads:
        ep_by_url.setdefault(r["url"], []).append(r["ep"])
    for r in fetches:
        df_by_ep.setdefault(r["ep"], []).append(r["df"])
    for r in hooks:
        hk_by_ep.setdefault(r["ep"], []).append(r["hk"])
    for r in served_from:
        try:
            sf_by_url[r["url"]] = json.loads(r["props"] or "{}")
        except ValueError:
            sf_by_url[r["url"]] = {}
    writers_by_key = {}
    for r in writers:
        writers_by_key.setdefault(r["key"], []).append({"id": r["producer"], "name": r["name"], "type": r["ptype"]})
    trig_by_target = {}
    for r in trig:
        trig_by_target.setdefault(r["target"], []).append({"id": r["t"], "props": r.get("props") or ""})
        trig_by_target.setdefault(r.get("tname") or "", []).append({"id": r["t"], "props": r.get("props") or ""})

    nodes, edges, by_family = [], [], {}
    unresolved = 0
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    for u in sorted(urls, key=lambda x: x["id"]):
        uid = u["id"]
        eps = sorted(ep_by_url.get(uid, []))
        if not eps:
            continue    # a ServedURL nobody reads is not a served-lineage instance; counted in the denominator line
        members = [uid] + eps
        for ep in eps:
            members += sorted(df_by_ep.get(ep, [])) + sorted(hk_by_ep.get(ep, []))
        sf = sf_by_url.get(uid) or {}
        s3key_id = ("%s/%s" % (sf.get("bucket"), sf.get("s3_key"))) if sf.get("bucket") and sf.get("s3_key") else None
        producers = []
        if s3key_id:
            members.append(s3key_id)
            producers = writers_by_key.get(s3key_id, [])
            members += [p["id"] for p in producers]
        triggers = []
        for p in producers:
            triggers += trig_by_target.get(p["id"], []) + trig_by_target.get(p["name"], [])
        family, resolution = _family_for(producers, triggers)
        members = sorted(set(members))
        iid = "motifi-canon:%s:%s" % (family or "sl-spine", rh({"family": family, "url": uid, "members": members})[7:19])
        props = {"grain": "instance",
                 "motif_family": family,                       # the CANONICAL key, its own name (CRO 64057)
                 "family_resolution": resolution,
                 "canon_binding": "SERVED_LINEAGE_CANON",
                 "members": members, "members_total": len(members),
                 "member_roles": {"served_url": uid, "endpoints": eps,
                                  "s3_key": s3key_id, "producers": [p["id"] for p in producers]},
                 "composed_by": PRODUCER, "composed_at": now}
        nodes.append({"node_id": iid, "node_type": "C2Motif", "props": props})
        edges += [{"source": iid, "target": m, "edge_type": "CONTAINS", "props": {"layer": "C2instance->C1"}}
                  for m in members]
        if family:
            by_family[family] = by_family.get(family, 0) + 1
        else:
            unresolved += 1
    doc = {"producer": PRODUCER,
           "consumer": "derive_runner compose arm (hook routing = CTO/CTO~B) + the rarity rider LEG 2",
           "binding_spec": "C2_RARITY_COORDINATE_RIDER_SPEC_20260820.md + CRO 64086 ratification",
           "excluded_stated": EXCLUDED_STATED,
           "key_space_note": "motif_family = the canonical c2_motif_families key UNDER ITS OWN NAME; the A/B "
                             "`family` sense and the thread sub-family sense are DIFFERENT KEY-SPACES (CRO 64057); "
                             "no canonical class rows exist in-graph yet -- the binding is by this prop",
           "id_derivation": "normative home precondition_token.py _request_hash over "
                            "{family, url, members-sorted}; any other serialization NON-CONFORMANT",
           "counts": {"served_urls_total": len(urls),
                      "served_urls_with_readers": sum(1 for u in urls if ep_by_url.get(u["id"])),
                      "spine_instances": len(nodes),
                      "by_family": dict(sorted(by_family.items())),
                      "family_resolved": sum(by_family.values()), "family_unresolved": unresolved,
                      "contains_edges": len(edges),
                      "_denominator": "spine instances = ServedURLs with >=1 READS_URL reader (%d of %d urls); "
                                      "family resolution over those instances"
                                      % (sum(1 for u in urls if ep_by_url.get(u["id"])), len(urls))},
           "nodes": nodes, "edges": edges,
           "graph_vintage": (vintage_fn or _cli_vintage_fn)()}
    return doc


# ---------------------------------------------------------------------------------------------
def self_test() -> int:
    """Offline: a constructed POSITIVE substrate, the LOUD-ZERO negative, and 2-run determinism."""
    ok = []

    def chk(name, cond):
        ok.append(bool(cond))
        print("  [%s] %s" % ("PASS" if cond else "FAIL", name))

    FIX = {
        "urls": [{"id": "endpointurl:/api/x.json", "name": "x"}, {"id": "endpointurl:/api/y.json", "name": "y"},
                 {"id": "endpointurl:/api/z.json", "name": "z"}],
        "reads": [{"ep": "ep:x", "url": "endpointurl:/api/x.json"}, {"ep": "ep:y", "url": "endpointurl:/api/y.json"},
                  {"ep": "ep:z", "url": "endpointurl:/api/z.json"}],
        "fetch": [{"df": "df:x", "ep": "ep:x"}],
        "hooks": [],
        "sf": [{"url": "endpointurl:/api/x.json", "props": json.dumps({"bucket": "b", "s3_key": "k/x.json"})},
               {"url": "endpointurl:/api/y.json", "props": json.dumps({"bucket": "b", "s3_key": "k/y.json"})},
               {"url": "endpointurl:/api/z.json", "props": json.dumps({"bucket": "b", "s3_key": "k/z.json"})}],
        "writers": [{"producer": "lambda:cronpub", "name": "cronpub", "ptype": "LAMBDA", "key": "b/k/x.json"},
                    {"producer": "lambda:evtpub", "name": "evtpub", "ptype": "LAMBDA", "key": "b/k/y.json"},
                    {"producer": "lambda:news-ai-sentiment", "name": "news-ai-sentiment", "ptype": "LAMBDA", "key": "b/k/z.json"}],
        "trig": [{"t": "sched:daily", "props": "cron(0 2 * * ? *)", "target": "lambda:cronpub", "tname": "cronpub"},
                 {"t": "rule:onland", "props": '{"event_pattern": "s3:ObjectCreated"}', "target": "lambda:evtpub", "tname": "evtpub"}],
    }

    def qf(q):
        if "ServedURL'" in q:
            return FIX["urls"]
        if "READS_URL" in q:
            return FIX["reads"]
        if "IS_ENDPOINT" in q:
            return FIX["fetch"]
        if "FETCHES" in q:
            return FIX["hooks"]
        if "SERVED_FROM" in q:
            return FIX["sf"]
        if "WRITES_S3" in q:
            return FIX["writers"]
        if "TRIGGERS" in q:
            return FIX["trig"]
        return []

    vf = lambda: {"nodes_snapshot_id": "fx", "edges_snapshot_id": "fx"}  # noqa: E731
    d = compose(query_fn=qf, vintage_fn=vf)
    fams = {n["props"]["motif_family"] for n in d["nodes"]}
    chk("1 POSITIVE: three instances composed, one per family, discriminated by derivable planes "
        "(cron -> scheduled-publish; event -> publish-serve; generative marker -> generative-publish)",
        d["counts"]["spine_instances"] == 3 and fams == set(SL_FAMILIES)
        and d["counts"]["by_family"] == {"generative-publish": 1, "publish-serve": 1, "scheduled-publish": 1})
    chk("1b every instance: grain=instance, motif_family under its OWN name (no `family` key), CONTAINS edges to members, "
        "denominator line present",
        all(n["props"]["grain"] == "instance" and "family" not in n["props"] for n in d["nodes"])
        and d["counts"]["contains_edges"] == sum(n["props"]["members_total"] for n in d["nodes"])
        and "_denominator" in d["counts"])
    d0 = compose(query_fn=lambda q: [], vintage_fn=vf)
    chk("2 LOUD ZERO (CRO 64086): absent substrate -> zero instances WITH substrate_absent naming the empty populations "
        "('an artifact of the substrate, not a measurement of the estate') -- never a quiet empty",
        d0["counts"]["spine_instances"] == 0 and "SUBSTRATE ABSENT" in d0.get("substrate_absent", "")
        and "ServedURL=0" in d0["substrate_absent"])
    FIX2 = dict(FIX)
    FIX2["trig"] = []

    def qf2(q):
        if "TRIGGERS" in q:
            return []
        return qf(q)
    d2 = compose(query_fn=qf2, vintage_fn=vf)
    unres = [n for n in d2["nodes"] if n["props"]["motif_family"] is None]
    chk("3 UNDISCRIMINABLE stays UNRESOLVED, loudly: no trigger plane -> scheduled-vs-event NOT guessed; the generative "
        "marker still resolves its instance (2 unresolved, 1 resolved)",
        len(unres) == 2 and d2["counts"]["family_unresolved"] == 2 and d2["counts"]["by_family"] == {"generative-publish": 1}
        and all("not guessed" in n["props"]["family_resolution"] for n in unres))
    da = compose(query_fn=qf, vintage_fn=vf)
    db = compose(query_fn=qf, vintage_fn=vf)

    def strip(x):
        return json.dumps({"n": [{k: v for k, v in nn["props"].items() if k != "composed_at"} for nn in x["nodes"]],
                           "e": x["edges"], "c": x["counts"]}, sort_keys=True)
    chk("4 TWO-RUN BYTE REPRODUCIBILITY over the same inputs (ids digest-derived via the normative home)", strip(da) == strip(db))
    n = sum(1 for x in ok if x)
    print("--- c2_canonical_compose self-test: %d/%d passed ---" % (n, len(ok)))
    return 0 if n == len(ok) else 1


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or "--help" in args or "-h" in args:
        print("c2_canonical_compose -- R1 LEG 1 composer. --exercise (read canonical DB, print counts, write nothing) | "
              "--emit <path> | --self-test | --help. Unknown flags REFUSE (rc 2).")
        return 0
    if "--self-test" in args:
        return self_test()
    if args[0] not in ("--exercise", "--emit"):
        print("c2_canonical_compose: UNKNOWN argument %r -- REFUSED (rc 2)." % args[0], file=sys.stderr)
        return 2
    try:
        doc = compose()
        c = doc["counts"]
        print("c2_canonical_compose: spine_instances=%d (of %d urls, %d with readers) | by_family=%s | "
              "family_resolved=%d unresolved=%d | contains_edges=%d"
              % (c["spine_instances"], c.get("served_urls_total", 0), c.get("served_urls_with_readers", 0),
                 c["by_family"], c["family_resolved"], c["family_unresolved"], c["contains_edges"]))
        if doc.get("substrate_absent"):
            print("  %s" % doc["substrate_absent"])
        print("  %s" % c["_denominator"] if "_denominator" in c else "", end="")
        print("  excluded: %s" % doc["excluded_stated"])
        print("  vintage: %s" % doc.get("graph_vintage"))
        if args[0] == "--emit":
            out = args[1]
            json.dump(doc, open(out, "w", encoding="utf-8"), indent=1)
            print("  wrote %s" % out)
        return 0
    except Exception as e:  # noqa: BLE001
        print("c2_canonical_compose: ERROR (%s: %s) -- a failed retrieval is never a zero" % (type(e).__name__, e),
              file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
