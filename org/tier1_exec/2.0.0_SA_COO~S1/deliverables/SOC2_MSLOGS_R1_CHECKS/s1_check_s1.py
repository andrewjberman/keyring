"""SOC2_MSLOGS round 1, cell SM-s-1 checks (silver over audit_records, and the timeline reader). Run from the repo root.

  python s1_check_s1.py silver   -> S1-SILVER-OK   (raw records -> sorted parquet, a stable column set, raw_json losslessly)
  python s1_check_s1.py timeline -> S1-TIMELINE-OK (one account's window through an injected invoker, in order, never blank)

Synthetic values only. The API this file drives is fixed in the order's worker face.
"""
import importlib.util
import io
import json
import os
import sys

ROOT = os.getcwd()
BUILDER = os.path.join(ROOT, "infra", "aws", "lambda", "globgrph-trino-access", "silver_builder.py")
READER = os.path.join(ROOT, "data", "m365_metadata", "scripts", "silver", "read_timeline.py")
OLD_FILES = [os.path.join(ROOT, "data", "m365_metadata", "scripts", "silver", f) for f in ("read_day.py", "first_content.py")] + [
    os.path.join(ROOT, "data", "m365_metadata", "scripts", "tests", f) for f in ("test_read_day.py", "test_first_content.py")]
COLUMNS = ["record_id", "creation_time", "date", "feed", "record_type", "operation", "result_status", "user_id", "user_type",
           "client_ip", "object_id", "site_url", "item_name", "mailbox_owner", "organization_id", "raw_json"]


def load(path, name):
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.dirname(path))
    spec.loader.exec_module(m)
    return m


def records():
    return [
        {"Id": "e-2", "CreationTime": "2026-10-15T14:05:09", "Workload": "Exchange", "RecordType": 2, "Operation": "MailItemsAccessed",
         "ResultStatus": "Succeeded", "UserId": "Pat.Example@OpalInvest.com", "UserType": 0, "ClientIP": "203.0.113.9",
         "MailboxOwnerUPN": "Pat.Example@opalinvest.com", "OrganizationId": "org-1", "Item": {"Subject": "Synthetic subject"},
         "Extra": {"nested": ["café", 1, None]}},
        {"Id": "s-1", "CreationTime": "2026-10-15T13:00:00Z", "Workload": "SharePoint", "RecordType": 6, "Operation": "FileDownloaded",
         "ResultStatus": "Succeeded", "UserId": "pat.example@opalinvest.com", "UserType": 0, "ClientIP": "203.0.113.9",
         "ObjectId": "https://x.example/f.xlsx", "SiteUrl": "https://x.example/sites/a", "SourceFileName": "f.xlsx", "OrganizationId": "org-1"},
        {"Id": "a-1", "CreationTime": "2026-10-16T02:30:00", "Workload": "AzureActiveDirectory", "RecordType": 15, "Operation": "UserLoggedIn",
         "ResultStatus": "Success", "UserId": "pat.example@opalinvest.com", "UserType": 0, "ActorIpAddress": "198.51.100.4",
         "OrganizationId": "org-1", "DeviceProperties": [{"Name": "OS", "Value": "Synthetic"}]},
        {"Id": "o-1", "CreationTime": "2026-10-16T05:00:00", "Workload": "OneDrive", "RecordType": 6, "Operation": "FileAccessed",
         "UserId": "other@opalinvest.com", "ClientIP": "192.0.2.1"},
    ]


def silver():
    m = load(BUILDER, "s1_builder")
    import pyarrow.parquet as pq

    bad = []
    if list(m.COLUMNS) != COLUMNS:
        bad.append("COLUMNS %r" % (list(m.COLUMNS),))
    data = m.build(records())
    t = pq.read_table(io.BytesIO(data))
    if t.column_names != COLUMNS:
        bad.append("parquet columns %r" % (t.column_names,))
    ids = t.column("record_id").to_pylist()
    if ids != ["s-1", "e-2", "a-1", "o-1"]:
        bad.append("rows must be sorted by creation_time: %r" % (ids,))
    d = {i: str(x) for i, x in zip(ids, t.column("date").to_pylist())}
    if d != {"s-1": "2026-10-15", "e-2": "2026-10-15", "a-1": "2026-10-15", "o-1": "2026-10-16"}:
        bad.append("Eastern dates %r" % (d,))
    rows = {r["record_id"]: r for r in t.to_pylist()}
    for rid, orig in ((r["Id"], r) for r in records()):
        if json.loads(rows[rid]["raw_json"]) != orig:
            bad.append("raw_json is not the original record for %s" % rid)
    if rows["e-2"]["user_id"] != "pat.example@opalinvest.com" or rows["e-2"]["mailbox_owner"] != "pat.example@opalinvest.com":
        bad.append("user_id and mailbox_owner must be lower-cased: %r %r" % (rows["e-2"]["user_id"], rows["e-2"]["mailbox_owner"]))
    if rows["a-1"]["client_ip"] != "198.51.100.4" or rows["s-1"]["client_ip"] != "203.0.113.9":
        bad.append("client_ip must come from ClientIP, else ActorIpAddress")
    if rows["e-2"]["item_name"] != "Synthetic subject" or rows["s-1"]["item_name"] != "f.xlsx":
        bad.append("item_name must be SourceFileName, else the item's Subject")
    if rows["s-1"]["creation_time"] != "2026-10-15T13:00:00Z" or rows["e-2"]["creation_time"] != "2026-10-15T14:05:09Z":
        bad.append("creation_time must be ISO UTC with a trailing Z")
    if rows["e-2"]["record_type"] != "2" or rows["s-1"]["feed"] != "SharePoint":
        bad.append("record_type is a string and feed is the Workload")
    only = pq.read_table(io.BytesIO(m.build(records(), only_date="2026-10-15"))).column("record_id").to_pylist()
    if only != ["s-1", "e-2", "a-1"]:
        bad.append("only_date must keep one Eastern date: %r" % (only,))
    if m.partition_date("2026-10-16T03:59:59Z") != "2026-10-15" or m.partition_date("2026-10-16T04:00:00Z") != "2026-10-16":
        bad.append("partition_date edge")
    empty = pq.read_table(io.BytesIO(m.build([])))
    if empty.num_rows != 0 or empty.column_names != COLUMNS:
        bad.append("an empty input must give a valid empty table with the same columns")
    if "TCKT" in open(BUILDER, encoding="utf-8").read():
        bad.append("silver_builder.py still mentions TCKT")
    for f in OLD_FILES:
        if os.path.exists(f):
            bad.append("the Ticket-Center-era file still exists: %s" % os.path.relpath(f, ROOT))
    if bad:
        print("S1-SILVER-REFUSED " + "; ".join(bad))
        return 1
    print("S1-SILVER-OK rows=%d" % t.num_rows)
    return 0


def timeline():
    m = load(READER, "s1_reader")
    bad = []
    seen = []
    rows = [{"time": "2026-10-15T14:05:09Z", "feed": "Exchange", "operation": "MailItemsAccessed", "result_status": "Succeeded",
             "client_ip": "203.0.113.9", "item_name": "Synthetic subject", "user_id": "pat@opalinvest.com", "record_id": "e-2"},
            {"time": "2026-10-15T13:00:00Z", "feed": "AzureActiveDirectory", "operation": "UserLoggedIn", "result_status": "Success",
             "client_ip": "198.51.100.4", "item_name": None, "user_id": "pat@opalinvest.com", "record_id": "a-1"}]

    def invoker(p):
        seen.append(p)
        return {"ok": True, "rows": rows, "truncated": False}

    reply = m.fetch(invoker, "pat@opalinvest.com", "2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z")
    if seen != [{"op": "timeline", "account": "pat@opalinvest.com", "start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z"}]:
        bad.append("invoke payload %r" % (seen,))
    text = m.render(reply)
    i_a, i_b = text.find("UserLoggedIn"), text.find("MailItemsAccessed")
    if not (0 <= i_a < i_b):
        bad.append("not in time order")
    if "09:00:00" not in text or "10:05:09" not in text:
        bad.append("times not rendered in Eastern")
    if "198.51.100.4" not in text:
        bad.append("the client ip is not shown")
    t2 = m.render({"ok": True, "rows": rows, "truncated": True})
    if "TRUNCATED" not in t2:
        bad.append("a truncated reply must say so")
    if "no activity collected" not in m.render({"ok": True, "rows": [], "truncated": False}):
        bad.append("an empty window must read 'no activity collected', not blank")
    try:
        m.fetch(lambda p: {"ok": False, "error": "refused"}, "pat@opalinvest.com", "2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z")
        bad.append("a refused door did not raise")
    except RuntimeError:
        pass
    n = len(seen)
    for acct in ("", "not-an-address", None):
        try:
            m.fetch(invoker, acct, "2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z")
            bad.append("an invalid account %r reached the door" % (acct,))
        except ValueError:
            pass
    if len(seen) != n:
        bad.append("an invalid account made a call")
    src = open(READER, encoding="utf-8").read()
    if 'Qualifier="member"' not in src and "Qualifier='member'" not in src:
        bad.append("the real invoker must pass Qualifier='member'")
    if "TCKT" in src:
        bad.append("read_timeline.py mentions TCKT")
    if bad:
        print("S1-TIMELINE-REFUSED " + "; ".join(bad))
        return 1
    print("S1-TIMELINE-OK")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"silver": silver, "timeline": timeline}.get(mode)
    try:
        sys.exit(fn() if fn else 2)
    except FileNotFoundError as e:
        print("S1-%s-REFUSED missing %s" % (mode.upper(), e))
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        print("S1-%s-REFUSED %s: %s" % (mode.upper(), type(e).__name__, str(e)[:200]))
        sys.exit(1)
