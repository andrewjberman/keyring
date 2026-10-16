"""TCKT_MTADTA round 2, cell MD-x-1 checks (the door's repair). Run from the repo (worktree) root.

  python r2_check_x1.py alias -> X1-ALIAS-OK (the door decides from the invoked alias; fail closed)
  python r2_check_x1.py tf    -> X1-TF-OK    (aliases, one principal each, ListBucket out of the Deny)
  python r2_check_x1.py keys  -> X1-KEYS-OK  (the key allowlist equals builder output; no person or file name in a key)

Synthetic values only. The door API this file drives is fixed in the order's worker face.
"""
import base64
import gzip
import importlib.util
import io
import os
import re
import sys
import types

ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, "lib"))
HANDLER = os.path.join(ROOT, "infra", "aws", "lambda", "globgrph-trino-access", "handler.py")
ACCESS_TF = os.path.join(ROOT, "infra", "aws", "terraform", "trino", "access.tf")
FN = "arn:aws:lambda:us-east-1:123456789012:function:globgrph-trino-access-lambda"
PFX = "m365-metadata/trino/"
BRONZE = PFX + "bronze/audit_events/date=20261015/Audit.SharePoint_20261015T200000Z.json.gz"
BRONZE2 = PFX + "bronze/audit_events/date=20261015/Audit.SharePoint_20261015T210000Z.json.gz"
SILVER = PFX + "silver/activity_events/date=2026-10-15/data.parquet"
CURSOR = PFX + "state/subscription_cursor/current/cursor.json"
COVER = PFX + "gold/collection_coverage/date=2026-10-15/coverage_20261015T200000Z.json"


class FakeS3:
    def __init__(self):
        self.objs = {}
        self.puts = []

    def put_object(self, Bucket, Key, Body, **kw):
        self.puts.append(Key)
        self.objs[Key] = Body if isinstance(Body, bytes) else Body.encode()
        return {}

    def get_object(self, Bucket, Key, **kw):
        if Key not in self.objs:
            raise KeyError(Key)
        return {"Body": io.BytesIO(self.objs[Key])}

    def list_objects_v2(self, Bucket, Prefix="", **kw):
        return {"Contents": [{"Key": k} for k in sorted(self.objs) if k.startswith(Prefix)], "IsTruncated": False}


def load():
    if not os.path.exists(HANDLER):
        raise FileNotFoundError(HANDLER)
    spec = importlib.util.spec_from_file_location("x1_handler", HANDLER)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def ctx(alias):
    arn = FN if alias is None else FN + ":" + alias
    return types.SimpleNamespace(invoked_function_arn=arn)


def b64(b):
    return base64.b64encode(b).decode()


def ok(r):
    return isinstance(r, dict) and r.get("ok") is True


def alias():
    h = load()
    os.environ["BUCKET"] = "opal-data-trino"
    s3 = FakeS3()
    s3.objs[CURSOR] = b'{"seen": {}}'
    s3.objs[COVER] = b'{"records": []}'
    s3.objs[BRONZE] = gzip.compress(b'{"event_id":"e1","creation_time":"2026-10-15T14:00:00Z","actor":"yang@opalinvest.com"}\n')
    logs = []
    stub_reader = types.SimpleNamespace(read_day_rows=lambda s3, bucket, prefix, person, date: [
        {"event_id": "b", "creation_time": "2026-10-15T14:00:00Z", "actor": "yang@opalinvest.com"},
        {"event_id": "a", "creation_time": "2026-10-15T13:00:00Z", "actor": "yang@opalinvest.com"}])
    stub_builder = types.SimpleNamespace(build=lambda events: b"PARQUET-" + str(len(events)).encode())

    def call(alias_name, ev):
        return h.handle(ev, ctx(alias_name), s3=s3, log=logs.append, silver_reader=stub_reader, silver_builder=stub_builder)

    bad = []
    # The collector alias: put, derive_silver (a count and no data), get_state on the cursor key alone.
    line = gzip.compress(b'{"event_id":"e2","creation_time":"2026-10-15T15:00:00Z","actor":"yang@opalinvest.com"}' + b"\n")
    if not ok(call("collector", {"op": "put", "dataset": "bronze", "key": BRONZE2, "body_b64": b64(line)})):
        bad.append("collector put refused")
    if not ok(call("collector", {"op": "put", "dataset": "gold", "key": COVER, "body_b64": b64(b"{}")})):
        bad.append("collector coverage put refused")
    r = call("collector", {"op": "derive_silver", "date": "2026-10-15"})
    if not ok(r) or set(r) - {"ok", "rows"}:
        bad.append("collector derive_silver must answer a count only: %r" % (r,))
    if not ok(call("collector", {"op": "get_state", "key": CURSOR})):
        bad.append("collector cursor read refused")
    for ev, why in (({"op": "get_state", "key": COVER}, "a coverage read"), ({"op": "get_day", "person": "yang@opalinvest.com", "date": "2026-10-15"}, "get_day"),
                    ({"op": "list_state", "prefix": PFX + "state/"}, "list_state"),
                    ({"op": "put", "dataset": "silver", "key": SILVER, "body_b64": b64(b"x")}, "a silver put")):
        if ok(call("collector", ev)):
            bad.append("collector alias was served %s" % why)
    # The member alias: reads and derive_silver; never a put.
    day = call("member", {"op": "get_day", "person": "yang@opalinvest.com", "date": "2026-10-15"})
    if not ok(day) or [x["event_id"] for x in day.get("rows", [])] != ["a", "b"]:
        bad.append("member get_day not the person's day in time order: %r" % (day,))
    if not ok(call("member", {"op": "get_state", "key": COVER})):
        bad.append("member coverage read refused")
    ls = call("member", {"op": "list_state", "prefix": PFX + "gold/collection_coverage/"})
    if not ok(ls) or COVER not in (ls.get("keys") or []):
        bad.append("member list_state did not list the coverage key: %r" % (ls,))
    if ok(call("member", {"op": "list_state", "prefix": PFX + "bronze/"})):
        bad.append("member list_state listed bronze")
    if not ok(call("member", {"op": "derive_silver", "date": "2026-10-15"})):
        bad.append("member derive_silver refused")
    if ok(call("member", {"op": "put", "dataset": "bronze", "key": BRONZE, "body_b64": b64(b"x")})):
        bad.append("member alias was served a put")
    # Fail closed: no alias, an unknown alias, no context.
    for name, c in (("unqualified", ctx(None)), ("unknown alias", ctx("admin")), ("no context", None)):
        for ev in ({"op": "get_day", "person": "yang@opalinvest.com", "date": "2026-10-15"}, {"op": "put", "dataset": "bronze", "key": BRONZE, "body_b64": b64(b"x")}):
            if ok(h.handle(ev, c, s3=s3, log=logs.append, silver_reader=stub_reader, silver_builder=stub_builder)):
                bad.append("%s was served %s" % (name, ev["op"]))
    r = call("collector", {"op": "put", "dataset": "bronze", "key": PFX + "bronze/audit_events/date=20261015/recon.xlsx.json.gz", "body_b64": b64(b"x")})
    if ok(r):
        bad.append("a key carrying a file name was written")
    if len(logs) < 20:
        bad.append("every call must be logged (%d lines)" % len(logs))
    if any("yang@" in x or "recon" in x for x in logs):
        bad.append("a log line carries a person or a file name")
    if bad:
        print("X1-ALIAS-REFUSED " + "; ".join(bad))
        return 1
    print("X1-ALIAS-OK calls_logged=%d" % len(logs))
    return 0


def tf():
    if not os.path.exists(ACCESS_TF):
        print("X1-TF-REFUSED no access.tf")
        return 1
    t = open(ACCESS_TF, encoding="utf-8").read()
    bad = []
    deny = re.search(r"data_actions\s*=\s*\[(.*?)\]", t, re.S)
    if not deny:
        bad.append("no data_actions list")
    elif re.search(r"s3:ListBucket", deny.group(1)):
        bad.append("s3:ListBucket or s3:ListBucketVersions is still in the Deny")
    for a in ("collector", "member"):
        if not re.search(r'resource\s+"aws_lambda_alias"\s+"%s"' % a, t):
            bad.append("no aws_lambda_alias %s" % a)
    if not re.search(r"publish\s*=\s*true", t):
        bad.append("function must publish a version for the aliases")
    grp = re.search(r'resource\s+"aws_iam_group_policy"\s+"invoke".*?\n}\n', t, re.S)
    if not grp or "aws_lambda_alias.member.arn" not in grp.group(0) or "aws_lambda_function.access.arn" in grp.group(0):
        bad.append("the group policy must invoke the member alias ARN alone")
    perm = re.search(r'resource\s+"aws_lambda_permission".*?\n}\n', t, re.S)
    if not perm or "collector" not in perm.group(0) or "aws_iam_role.collector.arn" not in perm.group(0):
        bad.append("no resource permission admitting the collector role on the collector alias")
    if re.search(r'Principal\s*=\s*"\*"', t):
        bad.append("a wildcard principal")
    if re.search(r'resource\s+"(aws_sns_[a-z_]+|aws_cloudwatch_metric_alarm)"', t):
        bad.append("an alarm or notification resource")
    if bad:
        print("X1-TF-REFUSED " + "; ".join(bad))
        return 1
    print("X1-TF-OK")
    return 0


def keys():
    h = load()
    import opal_naming as n

    bad = []

    def strip(a):
        return a.split("s3://opal-data-trino/", 1)[1]

    good = {
        "bronze": strip(n.address("m365-metadata", "trino", "bronze", "audit_events", "date=20261015", object="Audit.SharePoint_20261015T200000Z.json.gz")),
        "silver": strip(n.address("m365-metadata", "trino", "silver", "activity_events", "date=2026-10-15", object="data.parquet")),
        "state": strip(n.address("m365-metadata", "trino", "state", "subscription_cursor", "current", object="cursor.json")),
        "gold": strip(n.address("m365-metadata", "trino", "gold", "collection_coverage", "date=2026-10-15", object="coverage_20261015T200000Z.json")),
    }
    for ds, key in good.items():
        if not h.key_ok(ds, key):
            bad.append("builder key refused for %s: %s" % (ds, key))
    if not good["bronze"].startswith(h.PREFIX):
        bad.append("PREFIX %r is not the builder's prefix" % h.PREFIX)
    refused = [
        ("bronze", PFX + "bronze/audit_events/date=20261015/recon.xlsx.json.gz"),
        ("bronze", PFX + "bronze/audit_events/date=20261015/yang@opalinvest.com/x.json.gz"),
        ("bronze", PFX + "bronze/audit_events/person=yang/date=20261015/Audit.SharePoint_20261015T200000Z.json.gz"),
        ("gold", PFX + "gold/collection_coverage/date=2026-10-15/Q3 wire for ACME.json"),
        ("state", PFX + "state/subscription_cursor/current/cursor.json/../x"),
        ("silver", PFX + "silver/activity_events/date=2026-10-15/yang.parquet"),
        ("bronze", "other-source/bronze/x.json"),
    ]
    for ds, key in refused:
        if h.key_ok(ds, key):
            bad.append("a key carrying a person, file name or foreign prefix was admitted: %s" % key)
    if bad:
        print("X1-KEYS-REFUSED " + "; ".join(bad))
        return 1
    print("X1-KEYS-OK")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"alias": alias, "tf": tf, "keys": keys}.get(mode)
    try:
        sys.exit(fn() if fn else 2)
    except FileNotFoundError as e:
        print("%s-REFUSED missing %s" % (mode.upper(), e))
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        print("X1-%s-REFUSED %s: %s" % (mode.upper(), type(e).__name__, e))
        sys.exit(1)
