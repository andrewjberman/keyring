"""ONE live read of the request-history route, as the service principal: is page 1 newest first? Read-only.

    python history_route_read.py <tenant> <out.json> [--limit N]

Row IRPT_BCKEND-S326 V1. One login as svc-irpt-analysis; GETs only; every page of the history is walked by
`next_cursor` (bounded at 20 pages). The password is read by NAME into memory and never printed. Recorded: each page's
request ids and accepted_at in order, whether page 1 is non-increasing in accepted_at, whether the walk is non-increasing
across pages, and whether any id repeats. The history is owner-bound, so it lists the service principal's own requests.
ASCII only.
"""
import json
import sys

import served_reads_before_after as reads
import svc_principal as sp


def main(argv):
    tenant, out = argv[1], argv[2]
    limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else 25
    log = []
    password = sp._sm().get_secret_value(SecretId=sp.SECRET)["SecretString"]
    code, login = sp._call("POST", "/auth/login", {"email": sp.EMAIL, "password": password},
                           {"Content-Type": "application/json"}, log)
    del password
    token = login.get("accessToken") if isinstance(login, dict) else None
    print("login HTTP %s token %s" % (code, bool(token)))
    if not token:
        return 1
    headers = {"Authorization": "Bearer " + token, "X-Contract-Version": "v1", "Content-Type": "application/json"}
    pages, cursor = [], None
    for _ in range(20):
        query = "?selected_tenant=%s&limit=%d" % (tenant, limit) + ("&cursor=" + cursor if cursor else "")
        code, resp = sp._call("GET", reads.BASE + "analysis/requests" + query, None, headers, log)
        data = resp.get("data") if isinstance(resp, dict) else None
        items = (data or {}).get("items") or []
        page = [{"request_id": (i.get("identity") or {}).get("request_id"), "accepted_at": i.get("accepted_at")}
                for i in items]
        pages.append({"http": code, "items": page, "next_cursor": bool((data or {}).get("next_cursor"))})
        print("page %d HTTP %s items %d next %s" % (len(pages), code, len(page), pages[-1]["next_cursor"]))
        cursor = (data or {}).get("next_cursor")
        if not cursor:
            break
    del token
    walk = [row for page in pages for row in page["items"]]
    times = [row["accepted_at"] for row in walk]
    first = [row["accepted_at"] for row in (pages[0]["items"] if pages else [])]
    verdict = {
        "page1_newest_first": all(a >= b for a, b in zip(first, first[1:])),
        "walk_newest_first": all(a >= b for a, b in zip(times, times[1:])),
        "ids_unique": len({row["request_id"] for row in walk}) == len(walk),
        "rows": len(walk), "pages": len(pages),
        "page1_first": pages[0]["items"][0] if pages and pages[0]["items"] else None,
    }
    print("VERDICT %s" % json.dumps(verdict, sort_keys=True))
    json.dump({"at": sp._now(), "principal": sp.EMAIL, "tenant": tenant, "limit": limit, "pages": pages,
               "verdict": verdict}, open(out, "w", encoding="utf-8", newline="\n"), indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
