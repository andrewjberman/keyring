#!/usr/bin/env python3
"""Fold-in Y-H (CTO batch 178): join a page walk's network hops to the backend's own lines. Reads only.

    python backend_join.py <page.har> <out.json> [--journal] [--skew-ms 4000]
    python backend_join.py --selftest

<page.har> is the walk's HAR (Playwright `recordHar`, `2.0.0_SA_COO~D`'s submit mode). Every API hop under the HTTP API
(a path in docs/contracts/investor-reporting/v1/routes.json) is matched to its route, so to its Lambda (the route's
`handler`), and then to ONE invocation of that Lambda: the earliest unclaimed START inside the hop's window. The Lambdas
log no request ids (only START/END/REPORT), and the API has no access log, so the join is by function and time.
THE LAPTOP CLOCK IS NOT AWS'S (w32time stopped; AWS Date read 2.6-3.6 s ahead on 2026-10-02): the offset is estimated
from the HAR's own response Date headers (median, 1 s resolution) and applied before matching; it is printed.

Per hop: method, route, handler, HTTP status, page ms, the REQ-/UP- ids the hop carried (URL, request body, response
body), and its invocation's RequestId, START, Duration, Init Duration, Max Memory, plus the queue ms (START - hop start).
Then, per REQ- id: the irpt-jobs row's state and time fields (consistent GetItem). With --journal: the YCharts resident's
journal lines in the window -- any line naming an id, and every IRPT_ line but an idle poll (SSM on the host;
read-only). No value of a client holding, cookie or credential
is read or written: response bodies are scanned for ids only and never stored. ASCII only.
"""
import argparse
import datetime
import email.utils
import json
import os
import re
import statistics
import subprocess
import sys
import time

ID_RE = re.compile(r"\b(?:REQ|UP)-[0-9a-f]{16,64}\b")
API_PREFIX = "/api/scoped/investor-reporting/"
LOG_LINE = re.compile(r"^(START|REPORT) RequestId: ([0-9a-f-]{36})")
FIELD = re.compile(r"(Duration|Billed Duration|Init Duration|Max Memory Used): ([0-9.]+)")
RESIDENT_INSTANCE = "i-0167fd745ad906a66"  # the YCharts resident host (resident_journal.py)
RESIDENT_UNIT = "irpt-analysis-resident.service"
TIME_FIELDS = ("requested_at", "accepted_at", "claimed_at", "submitted_at", "ready_at", "terminal_at", "updated_at")


def repo_root():
    return subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                          cwd=os.path.dirname(os.path.abspath(__file__))).stdout.strip()


def iso_ms(text):
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00")).timestamp() * 1000.0


def utc(ms):
    return datetime.datetime.fromtimestamp(ms / 1000.0, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")[:-4] + "Z"


def route_table(routes):
    """[(method, compiled path regex, route_key, handler)], most specific (fewest parameters) first."""
    table = []
    for r in routes:
        method, path = r["route_key"].split(" ", 1)
        params = path.count("{")
        rx = re.compile("^" + re.sub(r"\\\{[^}]+\\\}", "[^/]+", re.escape(path)) + "$")
        table.append((params, method, rx, r["route_key"], r.get("handler")))
    return [t[1:] for t in sorted(table, key=lambda t: t[0])]


def match_route(table, method, path):
    for m, rx, key, handler in table:
        if m == method and rx.match(path):
            return key, handler
    return None, None


def hops_from_har(har, table):
    hops, offsets = [], []
    for e in har.get("log", {}).get("entries", []):
        url = e.get("request", {}).get("url", "")
        path = url.split("://", 1)[-1].split("/", 1)[-1]
        path = "/" + path.split("?", 1)[0]
        if not path.startswith(API_PREFIX):
            continue
        method = e["request"].get("method", "")
        start = iso_ms(e["startedDateTime"])
        took = float(e.get("time") or 0.0)
        texts = [url, (e["request"].get("postData") or {}).get("text") or "",
                 (e.get("response", {}).get("content") or {}).get("text") or ""]
        ids = sorted({i for t in texts for i in ID_RE.findall(t)})
        for h in e.get("response", {}).get("headers", []):
            if h.get("name", "").lower() == "date":
                try:
                    offsets.append(email.utils.parsedate_to_datetime(h["value"]).timestamp() * 1000.0 - (start + took))
                except (TypeError, ValueError):
                    pass
        key, handler = match_route(table, method, path)
        query = url.split("?", 1)[1] if "?" in url else ""
        tenant = dict(p.split("=", 1) for p in query.split("&") if "=" in p).get("selected_tenant")
        hops.append({"method": method, "path": path, "route_key": key, "handler": handler, "tenant": tenant,
                     "status": e.get("response", {}).get("status"), "start_ms": start, "page_ms": round(took, 1),
                     "ids": ids})
    hops.sort(key=lambda h: h["start_ms"])
    # A Date header is stamped when the response leaves AWS (truncated to the second), so it sits at or before the hop's
    # end on AWS's clock; the median of (Date - end) is the offset to within a second. No header: no correction.
    offset = statistics.median(offsets) + 500.0 if offsets else 0.0
    return hops, round(offset), len(offsets)


def invocations_from_events(events):
    """{RequestId: {start_ms, duration_ms, billed_ms, init_ms, max_mem_mb, stream}} from START/REPORT events."""
    out = {}
    for ev in events:
        m = LOG_LINE.match(ev.get("message", ""))
        if not m:
            continue
        inv = out.setdefault(m.group(2), {"request_id": m.group(2), "stream": ev.get("logStreamName")})
        if m.group(1) == "START":
            inv["start_ms"] = float(ev["timestamp"])
        else:
            f = dict(FIELD.findall(ev["message"]))
            inv.update(duration_ms=float(f["Duration"]) if "Duration" in f else None,
                       billed_ms=float(f["Billed Duration"]) if "Billed Duration" in f else None,
                       init_ms=float(f["Init Duration"]) if "Init Duration" in f else None,
                       max_mem_mb=float(f["Max Memory Used"]) if "Max Memory Used" in f else None)
    return out


def join(hops, invocations_by_handler, offset_ms, skew_ms):
    """Each hop takes the earliest unclaimed invocation of its handler whose START is inside
    [hop start - skew, hop end + skew] on AWS's clock. Returns the hops (annotated) and the unclaimed invocations."""
    claimed = set()
    for hop in hops:
        lo = hop["start_ms"] + offset_ms - skew_ms
        hi = hop["start_ms"] + offset_ms + hop["page_ms"] + skew_ms
        pool = sorted((i for i in invocations_by_handler.get(hop["handler"], {}).values()
                       if i.get("start_ms") is not None and lo <= i["start_ms"] <= hi and i["request_id"] not in claimed),
                      key=lambda i: i["start_ms"])
        hop["invocation"] = None
        if pool:
            inv = pool[0]
            claimed.add(inv["request_id"])
            hop["invocation"] = dict(inv, start=utc(inv["start_ms"]),
                                     queue_ms=round(inv["start_ms"] - (hop["start_ms"] + offset_ms)))
        hop["start"] = utc(hop["start_ms"])
    spare = [dict(i, handler=h) for h, invs in invocations_by_handler.items() for i in invs.values()
             if i["request_id"] not in claimed]
    return hops, spare


def read_log_events(handler, start_ms, end_ms):
    import boto3
    logs = boto3.client("logs", region_name="us-east-1")
    events, token = [], None
    while True:
        kw = dict(logGroupName="/aws/lambda/" + handler, startTime=int(start_ms), endTime=int(end_ms),
                  filterPattern="?START ?REPORT")
        if token:
            kw["nextToken"] = token
        page = logs.filter_log_events(**kw)
        events += page.get("events", [])
        token = page.get("nextToken")
        if not token:
            return events


def job_rows(tenant_by_req):
    import boto3
    table = boto3.resource("dynamodb", region_name="us-east-1").Table("irpt-jobs")
    rows = {}
    for req, tenant in sorted(tenant_by_req.items()):
        item = table.get_item(Key={"tenant": tenant, "job": req}, ConsistentRead=True).get("Item") if tenant else None
        rows[req] = None if not item else {k: str(item[k]) for k in ("state",) + TIME_FIELDS if k in item}
    return rows


def journal_lines(ids, since_ms, until_ms):
    """The resident's journal lines in the walk's window, via SSM (read-only): every line naming an id, and every
    IRPT_ line except an idle poll (`IRPT_RESIDENT_POLL handled=0`). The resident names no REQ- id in its journal
    (measured on Y-6 runs 1-3, 2026-10-05: an id-only grep read 0 lines), so its operations are joined by window."""
    import boto3
    ssm = boto3.client("ssm", region_name="us-east-1")
    def stamp(ms):
        return datetime.datetime.fromtimestamp(ms / 1000.0, datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    pattern = "|".join(sorted(ids) + ["IRPT_"])
    script = ("journalctl -u %s --since '%s UTC' --until '%s UTC' --no-pager -o short-iso | grep -E '%s' "
              "| grep -v 'IRPT_RESIDENT_POLL handled=0' | cut -c1-400 | tail -400"
              % (RESIDENT_UNIT, stamp(since_ms), stamp(until_ms), pattern))
    cid = ssm.send_command(InstanceIds=[RESIDENT_INSTANCE], DocumentName="AWS-RunShellScript",
                           Comment="2.0.0_SA_COO~Y read-only backend join (Y-H)",
                           Parameters={"commands": [script]})["Command"]["CommandId"]
    for _ in range(60):
        time.sleep(2)
        try:
            inv = ssm.get_command_invocation(CommandId=cid, InstanceId=RESIDENT_INSTANCE)
        except ssm.exceptions.InvocationDoesNotExist:
            continue
        if inv["Status"] not in ("Pending", "InProgress", "Delayed"):
            return {"command_id": cid, "status": inv["Status"],
                    "lines": inv.get("StandardOutputContent", "").splitlines()}
    return {"command_id": cid, "status": "NO_RESULT", "lines": []}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("har", nargs="?")
    ap.add_argument("out", nargs="?")
    ap.add_argument("--journal", action="store_true")
    ap.add_argument("--skew-ms", type=float, default=4000.0)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    routes = json.load(open(os.path.join(repo_root(), "docs/contracts/investor-reporting/v1/routes.json"),
                            encoding="utf-8"))["routes"]
    hops, offset, dated = hops_from_har(json.load(open(a.har, encoding="utf-8")), route_table(routes))
    if not hops:
        print("ERROR: no API hop in", a.har)
        return 1
    lo = hops[0]["start_ms"] + offset - a.skew_ms - 1000
    hi = max(h["start_ms"] + h["page_ms"] for h in hops) + offset + a.skew_ms + 60000
    handlers = sorted({h["handler"] for h in hops if h["handler"]})
    by_handler = {h: invocations_from_events(read_log_events(h, lo, hi)) for h in handlers}
    hops, spare = join(hops, by_handler, offset, a.skew_ms)
    ids = sorted({i for h in hops for i in h["ids"]})
    tenant_by_req = {i: next((h["tenant"] for h in hops if i in h["ids"] and h["tenant"]), None)
                     for i in ids if i.startswith("REQ-")}
    result = {"har": os.path.basename(a.har), "clock_offset_ms": offset, "dated_responses": dated,
              "window": [utc(lo), utc(hi)], "handlers": handlers, "hops": hops, "unclaimed_invocations": spare,
              "ids": ids, "jobs": job_rows(tenant_by_req)}
    if a.journal and ids:
        result["journal"] = journal_lines(ids, lo, hi)
    print("clock offset (AWS - laptop) %d ms from %d dated responses; window %s .. %s" % (offset, dated, *result["window"]))
    for h in hops:
        inv = h["invocation"] or {}
        print("%s %-6s %-62s HTTP %s page %8.0f ms | %s server %s ms init %s queue %s | %s" % (
            h["start"][11:23], h["method"], (h["route_key"] or h["path"])[len("GET "):][:62], h["status"], h["page_ms"],
            h["handler"], inv.get("duration_ms"), inv.get("init_ms"), inv.get("queue_ms"), ",".join(h["ids"])))
    print("unclaimed invocations in the window: %d; jobs read: %d%s" % (
        len(spare), len(result["jobs"]), "; journal lines: %d" % len(result["journal"]["lines"]) if "journal" in result else ""))
    json.dump(result, open(a.out, "w", encoding="utf-8", newline="\n"), indent=1)
    return 0


def selftest():
    routes = [{"route_key": "GET /api/scoped/investor-reporting/analysis/requests", "handler": "irpt-status"},
              {"route_key": "GET /api/scoped/investor-reporting/analysis/requests/{requestId}", "handler": "irpt-status"},
              {"route_key": "POST /api/scoped/investor-reporting/analysis/inputs", "handler": "irpt-ycharts-generate"}]
    table = route_table(routes)
    assert match_route(table, "GET", API_PREFIX + "analysis/requests") == (routes[0]["route_key"], "irpt-status")
    assert match_route(table, "GET", API_PREFIX + "analysis/requests/REQ-" + "a" * 24)[0] == routes[1]["route_key"]
    assert match_route(table, "POST", API_PREFIX + "analysis/requests") == (None, None)
    base = iso_ms("2026-10-02T18:00:00Z")

    def entry(at, ms, method, path, body="", date_lag=0.0):
        stamp = email.utils.formatdate((base + at + ms + 3000 - date_lag) / 1000.0, usegmt=True)  # AWS is 3 s ahead
        return {"startedDateTime": utc(base + at), "time": ms,
                "request": {"method": method, "url": "https://x.example.invalid" + API_PREFIX + path +
                            "?selected_tenant=t1", "postData": {"text": body}},
                "response": {"status": 200, "headers": [{"name": "Date", "value": stamp}],
                             "content": {"text": '{"upload_id": "UP-%s"}' % ("b" * 24) if "inputs" in path else ""}}}
    har = {"log": {"entries": [entry(0, 900, "POST", "analysis/inputs", "{}"),
                               entry(2000, 3000, "GET", "analysis/requests/REQ-" + "c" * 24),
                               entry(2100, 2500, "GET", "analysis/requests"),
                               {"startedDateTime": utc(base), "time": 5, "request": {"method": "GET",
                                "url": "https://x.example.invalid/static/app.js"}, "response": {"status": 200}}]}}
    hops, offset, dated = hops_from_har(har, table)
    assert len(hops) == 3 and dated == 3 and 2500 <= offset <= 4000, (len(hops), dated, offset)
    assert hops[0]["ids"] == ["UP-" + "b" * 24] and hops[1]["ids"] == ["REQ-" + "c" * 24] and hops[0]["tenant"] == "t1"

    def ev(kind, rid, at, extra=""):
        msg = ("START RequestId: %s Version: $LATEST" % rid) if kind == "START" else (
            "REPORT RequestId: %s\tDuration: 812.5 ms\tBilled Duration: 813 ms\tMemory Size: 1024 MB\t"
            "Max Memory Used: 200 MB%s" % (rid, extra))
        return {"timestamp": base + at, "message": msg, "logStreamName": "s"}
    r1, r2, r3, r4 = ("%08d-0000-0000-0000-000000000000" % n for n in (1, 2, 3, 4))
    status = invocations_from_events([ev("START", r1, 3000 + 2150), ev("REPORT", r1, 3000 + 2900, "\tInit Duration: 160.0 ms"),
                                      ev("START", r2, 3000 + 2060), ev("REPORT", r2, 3000 + 4900),
                                      ev("START", r3, 3000 + 60000), ev("REPORT", r3, 3000 + 60500)])
    generate = invocations_from_events([ev("START", r4, 3000 + 100), ev("REPORT", r4, 3000 + 800)])
    assert status[r1]["init_ms"] == 160.0 and status[r2]["duration_ms"] == 812.5
    joined, spare = join(hops, {"irpt-status": status, "irpt-ycharts-generate": generate}, offset, 1500.0)
    got = [(h["handler"], (h["invocation"] or {}).get("request_id")) for h in joined]
    # The single read started first and takes the earlier START (r2); history takes r1; r3 is a minute later: unclaimed.
    assert got == [("irpt-ycharts-generate", r4), ("irpt-status", r2), ("irpt-status", r1)], got
    assert [s["request_id"] for s in spare] == [r3], spare
    # Negative control: with no clock correction and a tight skew, the 3 s offset loses the upload's and history's
    # invocations (only the 3 s single read's window still reaches a START).
    hops2, _, _ = hops_from_har(har, table)
    joined2, _ = join(hops2, {"irpt-status": status, "irpt-ycharts-generate": generate}, 0.0, 500.0)
    got2 = [(h["invocation"] or {}).get("request_id") for h in joined2]
    assert got2 == [None, r2, None], got2
    print("SELFTEST OK: routes, ids, clock offset %d ms, join by function and time, unclaimed, negative control" % offset)
    return 0


if __name__ == "__main__":
    sys.exit(main())
