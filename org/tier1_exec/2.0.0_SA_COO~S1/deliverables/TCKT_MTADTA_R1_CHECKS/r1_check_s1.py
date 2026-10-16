"""TCKT_MTADTA round 1, cell MD-s-1 checks. Run from the repo (worktree) root.

  python r1_check_s1.py silver  -> S1-SILVER-OK  (bronze events -> sorted parquet, fixed columns)
  python r1_check_s1.py readday -> S1-READDAY-OK (one person's day, in order, through an injected invoker)
"""
import importlib.util
import io
import os
import sys

ROOT = os.getcwd()
BUILDER = os.path.join(ROOT, "infra", "aws", "lambda", "globgrph-trino-access", "silver_builder.py")
READDAY = os.path.join(ROOT, "data", "m365_metadata", "scripts", "silver", "read_day.py")
COLS = ["event_id", "creation_time", "date", "actor", "workload", "operation", "record_type", "result_status",
        "subject_hash", "participants", "site", "file_id", "file_name", "extension", "folder", "client_ip_class"]


def load(path, name):
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.dirname(path))
    spec.loader.exec_module(m)
    return m


def b(event_id, t, actor="yang@opalinvest.com", op="FileAccessed"):
    return {"event_id": event_id, "creation_time": t, "actor": actor, "workload": "SharePoint", "operation": op,
            "record_type": 6, "result_status": "Succeeded", "subject_hash": None, "participants": [],
            "site": "ops", "file_id": "f1", "file_name": "recon.xlsx", "extension": "xlsx", "folder": "Shared Documents/Ops",
            "client_ip_class": "remote"}


def silver():
    m = load(BUILDER, "s1_builder")
    import pyarrow.parquet as pq

    rows = [b("c", "2026-10-15T20:30:00Z"), b("a", "2026-10-15T13:00:00Z"), b("b", "2026-10-15T13:00:01Z"),
            b("late", "2026-10-16T02:30:00Z")]
    data = m.build(rows)
    t = pq.read_table(io.BytesIO(data))
    bad = []
    if t.column_names != COLS:
        bad.append("columns %r" % (t.column_names,))
    ids = t.column("event_id").to_pylist()
    if ids != ["a", "b", "c", "late"]:
        bad.append("order %r" % (ids,))
    dates = t.column("date").to_pylist()
    # 02:30Z on the 16th is 22:30 ET on the 15th: the partition date is the Eastern date.
    if [str(d) for d in dates] != ["2026-10-15"] * 4:
        bad.append("partition dates %r" % (dates,))
    if m.partition_date("2026-10-16T05:00:00Z") != "2026-10-16" or m.partition_date("2026-10-16T03:59:59Z") != "2026-10-15":
        bad.append("partition_date edge")
    if bad:
        print("S1-SILVER-REFUSED " + "; ".join(bad))
        return 1
    print("S1-SILVER-OK rows=%d" % t.num_rows)
    return 0


def readday():
    m = load(READDAY, "s1_readday")
    bad = []
    rows = [
        {"event_id": "b", "creation_time": "2026-10-15T14:05:09Z", "operation": "FileAccessed", "workload": "SharePoint",
         "file_name": "recon.xlsx", "folder": "Shared Documents/Ops", "participants": []},
        {"event_id": "a", "creation_time": "2026-10-15T13:00:00Z", "operation": "Send", "workload": "Exchange",
         "file_name": None, "folder": None, "participants": ["alyssa@opalinvest.com", "external"]},
    ]
    seen = []

    def invoker(payload):
        seen.append(payload)
        return {"ok": True, "rows": rows}

    text = m.render(m.fetch(invoker, "yang@opalinvest.com", "2026-10-15"))
    if seen != [{"op": "get_day", "person": "yang@opalinvest.com", "date": "2026-10-15"}]:
        bad.append("invoke payload %r" % (seen,))
    i_a, i_b = text.find("Send"), text.find("FileAccessed")
    if not (0 <= i_a < i_b):
        bad.append("not in time order")
    if "09:00:00" not in text or "10:05:09" not in text:
        bad.append("times not rendered in Eastern")
    try:
        m.fetch(invoker, "someone@example.com", "2026-10-15")
        bad.append("a non-member was not refused before any invoke")
    except ValueError:
        pass
    if len(seen) != 1:
        bad.append("the non-member reached the door")
    if bad:
        print("S1-READDAY-REFUSED " + "; ".join(bad))
        return 1
    print("S1-READDAY-OK")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"silver": silver, "readday": readday}.get(mode)
    try:
        sys.exit(fn() if fn else 2)
    except FileNotFoundError as e:
        print("%s-REFUSED missing %s" % (mode.upper(), e))
        sys.exit(1)
