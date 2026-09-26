#!/usr/bin/env python3
"""UIR-07 (CTO 101506) -- the served proof of the search ranking change, before and after.

    python search_rank_arm.py <before|after> <out.json>
    python search_rank_arm.py compare <before.json> <after.json>

It invokes irpt-directory-search directly (IAM only; the same boundary the edge feeds) with the edge's trusted
headers for a synthetic internal Opal subject, as deploy_b_human_arm.py does. Search and browse are pure reads.

1. Browse 49F's first page (limit 100). Candidates are the documents whose display name has >= 2 tokens and whose
   token multiset is unique on that page; take the first 20 by id digest (deterministic across phases).
2. Query each with its name tokens REVERSED (limit 100). Record the result SET (the documents' id digests, sorted)
   and the target's 1-based rank.
Only digests and ranks are written; no display name leaves this process.

compare passes when every result set is identical before and after, every after-rank is 1, and no before-rank of
1 is lost.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import sys
import unicodedata

import boto3

SAMPLE = {"49financial": 20, "cottonwood": 5, "inflection": 5}  # deterministic entries per firm (CTO 101534)
COLLISIONS = 5  # per firm, the entries a longer name could outrank
HEADERS = {"x-origin-verify": "cloudfront", "x-user-role": "user", "x-contract-version": "v1",
           "x-user-tier": "internal", "x-firm-id": "opal-capital",
           "x-user-email": "uir07-arm@opal.test", "x-user-name": "uir07 arm"}
LAMBDA = boto3.client("lambda", region_name="us-east-1")
_WS = re.compile(r"[^a-z0-9]+")


def tokens(text):
    s = unicodedata.normalize("NFKD", str(text or ""))
    s = "".join(c for c in s if not unicodedata.combining(c))
    return [t for t in _WS.sub(" ", s.lower()).strip().split(" ") if t]


def call(route, params, firm):
    event = {"version": "2.0", "routeKey": route, "headers": dict(HEADERS),
             "queryStringParameters": dict(params, selected_tenant=firm)}
    r = LAMBDA.invoke(FunctionName="irpt-directory-search", Payload=json.dumps(event).encode())
    body = json.loads(r["Payload"].read())
    if isinstance(body.get("body"), str):
        body = json.loads(body["body"])
    data = body.get("data")
    if isinstance(data, dict) and isinstance(data.get("entries"), list):
        data = data["entries"]  # browse pages its documents under data.entries; search returns the list itself
    if r.get("FunctionError") or not isinstance(data, list):
        raise SystemExit("STOP: %s refused: %s" % (route, json.dumps(body.get("status"))[:300]))
    return data


def doc_id(doc):
    return hashlib.sha256(json.dumps(doc.get("ids") or {}, sort_keys=True).encode()).hexdigest()[:16]


def _browse_all(firm, q):
    """The page's header search: browse(q), every cursor page, in served order."""
    ids, cursor = [], None
    for _ in range(50):
        params = {"q": q, "limit": "100"}
        if cursor:
            params["cursor"] = cursor
        event = {"version": "2.0", "routeKey": "GET /api/scoped/investor-reporting/directory/browse",
                 "headers": dict(HEADERS), "queryStringParameters": dict(params, selected_tenant=firm)}
        body = json.loads(LAMBDA.invoke(FunctionName="irpt-directory-search", Payload=json.dumps(event).encode())
                          ["Payload"].read())
        data = body.get("data") or {}
        if not isinstance(data.get("entries"), list):
            raise SystemExit("STOP: browse refused: %s" % json.dumps(body.get("status"))[:300])
        ids += [(doc_id(d), sorted(tokens(d.get("display_name")))) for d in data["entries"]]
        cursor = data.get("next_cursor")
        if not cursor:
            return ids
    raise SystemExit("STOP: browse did not end within 50 pages")


def _digest(ids):
    return hashlib.sha256("|".join(sorted(ids)).encode()).hexdigest()[:16]


def _ahead(pairs, ident, full):
    """(1-based rank of ident, how many entries ahead of it are themselves exact full-name matches)."""
    ids = [i for i, _ in pairs]
    if ident not in ids:
        return None, None
    at = ids.index(ident)
    return at + 1, sum(1 for _, t in pairs[:at] if t == full)


def _row(firm, kind, ident, q):
    full = sorted(tokens(q))
    hits = call("GET /api/scoped/investor-reporting/directory/search", {"q": q, "limit": "100"}, firm)
    pairs = [(doc_id(h), sorted(tokens(h.get("display_name")))) for h in hits]
    page = _browse_all(firm, q)
    rank, ahead = _ahead(pairs, ident, full)
    brank, bahead = _ahead(page, ident, full)
    return {"firm": firm, "kind": kind, "target": ident, "results": len(pairs),
            "result_set": _digest([i for i, _ in pairs]), "rank": rank, "full_matches_ahead": ahead,
            "browse_results": len(page), "browse_set": _digest([i for i, _ in page]), "browse_rank": brank,
            "browse_full_matches_ahead": bahead}


def _global_row(kind, ident, q):
    """The page's GLOBAL request (ClientSearch.tsx:93-106; 4.0.0_SA_CRO 101550): one browse(q) per permitted firm,
    limit 100 (PAGE_LIMIT), the answers concatenated in the contexts' order and never re-ranked (search.ts toOptions).
    The contexts' firm order is not fixed in that file, so the target's merged rank is taken over all 6 orders."""
    import itertools
    firsts = {}
    for firm in SAMPLE:
        event = {"version": "2.0", "routeKey": "GET /api/scoped/investor-reporting/directory/browse",
                 "headers": dict(HEADERS), "queryStringParameters": {"q": q, "limit": "100", "selected_tenant": firm}}
        body = json.loads(LAMBDA.invoke(FunctionName="irpt-directory-search", Payload=json.dumps(event).encode())
                          ["Payload"].read())
        firsts[firm] = [doc_id(d) for d in (body.get("data") or {}).get("entries") or []]
    ranks = []
    for order in itertools.permutations(SAMPLE):
        merged = [i for firm in order for i in firsts[firm]]
        ranks.append(merged.index(ident) + 1 if ident in merged else None)
    known = [r for r in ranks if r is not None]
    return {"firm": "GLOBAL", "kind": kind, "target": ident, "per_firm_first_page": {f: len(v) for f, v in firsts.items()},
            "global_rank_min": min(known) if known else None, "global_rank_max": max(known) if known else None,
            "merged_set": _digest([i for v in firsts.values() for i in v])}


def run():
    rows, pages = [], {}
    for firm, n in SAMPLE.items():
        page = call("GET /api/scoped/investor-reporting/directory/browse", {"limit": "100"}, firm)
        pages[firm] = len(page)
        keyed = [(doc_id(d), tuple(sorted(tokens(d.get("display_name"))))) for d in page]
        counts = {}
        for _, key in keyed:
            counts[key] = counts.get(key, 0) + 1
        unique = sorted((i, k) for i, k in keyed if len(k) >= 2 and counts[k] == 1)
        # COLLISION: another entry on the page carries every one of this name's tokens and more -- the UIR-07 shape.
        collide = [(i, k) for i, k in unique
                   if any(set(k) < set(other) for _, other in keyed)][:COLLISIONS]
        for kind, chosen in (("deterministic", unique[:n]), ("collision", collide)):
            for ident, key in chosen:
                rows.append(_row(firm, kind, ident, " ".join(reversed(key))))
    case = os.environ.get("IRPT_UIR07_CASE", "").strip()
    if case:
        # The reported case (Cottonwood, CTO 101534): the query comes from the environment and is never printed or
        # written; the target is the one document whose token multiset equals the query's.
        hits = call("GET /api/scoped/investor-reporting/directory/search", {"q": case, "limit": "100"}, "cottonwood")
        exact = [doc_id(h) for h in hits if sorted(tokens(h.get("display_name"))) == sorted(tokens(case))]
        if len(exact) != 1:
            raise SystemExit("STOP: the reported case matches %d documents, not 1" % len(exact))
        for order, q in (("case-as-reported", case), ("case-reversed", " ".join(reversed(tokens(case))))):
            rows.append(_row("cottonwood", order, exact[0], q))
            rows.append(_global_row(order, exact[0], q))
    return {"browse_pages": pages, "rows": rows}


def compare(before, after):
    key = lambda r: (r["firm"], r["kind"], r["target"])  # noqa: E731
    gb = {key(r): r for r in before["rows"] if r["firm"] == "GLOBAL"}
    ga = {key(r): r for r in after["rows"] if r["firm"] == "GLOBAL"}
    b = {key(r): r for r in before["rows"] if r["firm"] != "GLOBAL"}
    a = {key(r): r for r in after["rows"] if r["firm"] != "GLOBAL"}
    checks = [
        ("the same targets in both phases", set(a) == set(b) and len(a) > 0),
        ("every search result SET identical", all(a[t]["result_set"] == b[t]["result_set"] for t in a if t in b)),
        ("every browse(q) result SET identical (all pages)",
         all(a[t]["browse_set"] == b[t]["browse_set"] for t in a if t in b)),
        # "Rank 1" means only exact full-name matches (a same-name twin elsewhere in the firm) may precede the target.
        ("every after-rank is 1 (search)",
         all(a[t]["rank"] is not None and a[t]["rank"] - 1 == a[t]["full_matches_ahead"] for t in a)),
        ("every after-rank is 1 (browse(q), the page's header search)",
         all(a[t]["browse_rank"] is not None and a[t]["browse_rank"] - 1 == a[t]["browse_full_matches_ahead"]
             for t in a)),
        ("no before-rank of 1 lost", all(a[t]["rank"] == 1 for t in b if b[t]["rank"] == 1 and t in a)),
    ]
    for name, ok in checks:
        print("%s %s" % ("PASS" if ok else "FAIL", name))
    for t in sorted(b):
        if b[t]["rank"] != 1 or b[t]["browse_rank"] != 1:
            print("moved: %s %s search %s -> %s; browse(q) %s -> %s" % (
                t[0], t[1], b[t]["rank"], (a.get(t) or {}).get("rank"), b[t]["browse_rank"],
                (a.get(t) or {}).get("browse_rank")))
    for t in sorted(ga):
        print("GLOBAL (the page's merge, CRO 101550) %s: merged set %s; rank over the 6 firm orders %s-%s -> %s-%s%s" % (
            t[1], "identical" if ga[t]["merged_set"] == (gb.get(t) or {}).get("merged_set") else "DIFFERENT",
            (gb.get(t) or {}).get("global_rank_min"), (gb.get(t) or {}).get("global_rank_max"),
            ga[t]["global_rank_min"], ga[t]["global_rank_max"],
            "" if ga[t]["global_rank_max"] == 1 else "  -> UIR-07 OPEN at the page merge (ClientSearch.tsx:98-106)"))
    return all(ok for _, ok in checks)


def main(argv):
    if argv[1] == "compare":
        before, after = (json.load(open(p, encoding="utf-8")) for p in argv[2:4])
        raise SystemExit(0 if compare(before, after) else 3)
    out = run()
    for r in out["rows"]:
        if r["firm"] == "GLOBAL":
            print("%s GLOBAL %s: per-firm first page %s; merged rank over 6 firm orders %s-%s" % (
                argv[1], r["kind"], r["per_firm_first_page"], r["global_rank_min"], r["global_rank_max"]))
    for firm in out["browse_pages"]:
        for kind in ("deterministic", "collision", "case-as-reported", "case-reversed"):
            rows = [r for r in out["rows"] if r["firm"] == firm and r["kind"] == kind]
            if rows:
                print("%s %s %s: search ranks %s; browse(q) ranks %s" % (
                    argv[1], firm, kind, [r["rank"] for r in rows], [r["browse_rank"] for r in rows]))
    with open(argv[2], "w", encoding="utf-8", newline="\n") as f:
        json.dump({"at": dt.datetime.now(dt.timezone.utc).isoformat(), "phase": argv[1], **out}, f, indent=1)


if __name__ == "__main__":
    main(sys.argv)
