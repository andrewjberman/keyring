"""SOC2_MSLOGS round 1, cell SM-a-1 checks (the door: write-once raw bronze, timeline, recollect). Run from the repo (worktree) root.

  python s1_check_a1.py ops    -> A1-OPS-OK    (alias matrix v3: timeline, recollect, get_day gone, a member never supplies bytes)
  python s1_check_a1.py bronze -> A1-BRONZE-OK (write-once, the old table frozen, the audit_records key grammar, derive over two days)
  python s1_check_a1.py detail -> A1-DETAIL-OK (timeline detail=true returns each record whole, capped by rows and by response bytes)
  python s1_check_a1.py tf     -> A1-TF-OK     (door role may invoke the collector; COLLECTOR_FUNCTION set; no TCKT; the Deny unchanged)

Synthetic values only. The door API this file drives is fixed in the order's worker face.
"""
import base64
import gzip
import importlib.util
import io
import json
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
CID = "20261015120000000001$20261015120000000001$audit_exchange$Audit_Exchange$na0001"
BRONZE = PFX + "bronze/audit_records/date=20261015/" + CID + ".json.gz"
BRONZE2 = PFX + "bronze/audit_records/date=20261016/" + CID.replace("20261015", "20261016") + ".json.gz"
OLD = PFX + "bronze/audit_events/date=20261015/Audit.SharePoint_20261015T200000Z.json.gz"
CURSOR = PFX + "state/subscription_cursor/current/cursor.json"
COVER = PFX + "gold/collection_coverage/date=2026-10-15/coverage_20261015T200000Z.json"
SILVER = PFX + "silver/activity_events/date=2026-10-15/data.parquet"
NOW = "2026-10-16T12:00:00Z"


class FakeClientError(Exception):
    """The shape botocore's ClientError carries: .response['Error']['Code']."""

    def __init__(self, code):
        super().__init__(code)
        self.response = {"Error": {"Code": code}}


class FakeS3:
    def __init__(self, head_error=None):
        self.objs = {}
        self.puts = []
        self.head_error = head_error

    def put_object(self, Bucket, Key, Body, **kw):
        self.puts.append(Key)
        self.objs[Key] = Body if isinstance(Body, bytes) else Body.encode()
        return {}

    def head_object(self, Bucket, Key, **kw):
        if self.head_error:
            raise FakeClientError(self.head_error)
        if Key not in self.objs:
            raise FakeClientError("404")
        return {"ContentLength": len(self.objs[Key])}

    def get_object(self, Bucket, Key, **kw):
        if Key not in self.objs:
            raise KeyError(Key)
        return {"Body": io.BytesIO(self.objs[Key])}

    def list_objects_v2(self, Bucket, Prefix="", **kw):
        return {"Contents": [{"Key": k} for k in sorted(self.objs) if k.startswith(Prefix)], "IsTruncated": False}


class FakeLambda:
    def __init__(self):
        self.calls = []

    def invoke(self, **kw):
        self.calls.append(kw)
        return {"StatusCode": 202}


def load():
    if not os.path.exists(HANDLER):
        raise FileNotFoundError(HANDLER)
    spec = importlib.util.spec_from_file_location("a1_handler", HANDLER)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def ctx(alias):
    return types.SimpleNamespace(invoked_function_arn=FN if alias is None else FN + ":" + alias)


def b64(b):
    return base64.b64encode(b).decode()


def ok(r):
    return isinstance(r, dict) and r.get("ok") is True


def gz(records):
    return gzip.compress(json.dumps(records).encode("utf-8"))


def ops():
    h = load()
    os.environ["BUCKET"] = "opal-data-trino"
    os.environ["COLLECTOR_FUNCTION"] = "m365-metadata-trino-collector-lambda"
    s3 = FakeS3()
    lam = FakeLambda()
    logs = []
    rows = [{"time": "2026-10-15T14:00:00Z", "operation": "FileAccessed", "user_id": "pat@opalinvest.com"},
            {"time": "2026-10-15T13:00:00Z", "operation": "UserLoggedIn", "user_id": "pat@opalinvest.com"}]
    calls = {}

    def reader_rows(s3_, bucket, prefix, account, start, end):
        calls["args"] = (account, start, end)
        return list(calls.get("rows", rows))

    reader = types.SimpleNamespace(timeline_rows=reader_rows)
    builder = types.SimpleNamespace(build=lambda records, only_date=None: b"PARQUET-" + str(len(records)).encode())

    def call(alias, ev):
        return h.handle(ev, ctx(alias), s3=s3, log=logs.append, silver_reader=reader, silver_builder=builder, lambda_client=lam, now=NOW)

    bad = []
    # member alias: timeline over ANY account, in time order, bounded
    tl = call("member", {"op": "timeline", "account": "pat@opalinvest.com", "start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z"})
    if not ok(tl) or [r["operation"] for r in tl.get("rows", [])] != ["UserLoggedIn", "FileAccessed"] or tl.get("truncated") is not False:
        bad.append("timeline not the account's rows in time order with truncated=False: %r" % (tl,))
    if calls.get("args") != ("pat@opalinvest.com", "2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z"):
        bad.append("timeline reader args %r" % (calls.get("args"),))
    calls["rows"] = [{"time": "2026-10-15T%02d:%02d:00Z" % (i // 60, i % 60), "operation": "X"} for i in range(5001)]
    big = call("member", {"op": "timeline", "account": "pat@opalinvest.com", "start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z"})
    if not ok(big) or len(big.get("rows", [])) != 5000 or big.get("truncated") is not True:
        bad.append("timeline must cap at 5000 rows and say truncated: %r" % (len(big.get("rows", [])) if isinstance(big, dict) else big,))
    calls["rows"] = rows
    for name, ev in (("no account", {"op": "timeline", "start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z"}),
                     ("end before start", {"op": "timeline", "account": "pat@opalinvest.com", "start": "2026-10-16T00:00:00Z", "end": "2026-10-15T00:00:00Z"}),
                     ("window over 31 days", {"op": "timeline", "account": "pat@opalinvest.com", "start": "2026-08-01T00:00:00Z", "end": "2026-10-15T00:00:00Z"}),
                     ("account not a string", {"op": "timeline", "account": 7, "start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z"})):
        if ok(call("member", ev)):
            bad.append("timeline served %s" % name)
    # get_day is gone on every alias
    for alias in ("member", "collector"):
        if ok(call(alias, {"op": "get_day", "person": "yang@opalinvest.com", "date": "2026-10-15"})):
            bad.append("get_day is still served on %s" % alias)
    if ok(call("collector", {"op": "timeline", "account": "pat@opalinvest.com", "start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z"})):
        bad.append("the collector alias was served a timeline")
    # recollect: member only, the door asks the collector, no bytes from the caller
    rc = call("member", {"op": "recollect", "start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z"})
    if not ok(rc) or len(lam.calls) != 1:
        bad.append("recollect did not invoke the collector once: %r calls=%d" % (rc, len(lam.calls)))
    else:
        c0 = lam.calls[0]
        pay = json.loads(c0["Payload"].decode() if isinstance(c0["Payload"], bytes) else c0["Payload"])
        if c0.get("FunctionName") != "m365-metadata-trino-collector-lambda" or c0.get("InvocationType") != "Event":
            bad.append("recollect must invoke COLLECTOR_FUNCTION asynchronously: %r" % ({k: v for k, v in c0.items() if k != "Payload"},))
        if pay != {"recollect": {"start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z"}}:
            bad.append("recollect payload %r" % (pay,))
    n = len(lam.calls)
    for name, ev in (("older than 7 days", {"op": "recollect", "start": "2026-10-01T00:00:00Z", "end": "2026-10-02T00:00:00Z"}),
                     ("end before start", {"op": "recollect", "start": "2026-10-16T00:00:00Z", "end": "2026-10-15T00:00:00Z"}),
                     ("with record bytes", {"op": "recollect", "start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z", "body_b64": b64(b"x")}),
                     ("with records", {"op": "recollect", "start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z", "records": [{"Id": "x"}]})):
        if ok(call("member", ev)):
            bad.append("recollect served %s" % name)
    if len(lam.calls) != n:
        bad.append("a refused recollect still invoked the collector")
    if ok(call("collector", {"op": "recollect", "start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z"})):
        bad.append("the collector alias was served recollect")
    # the rest of the matrix still holds
    s3.objs[CURSOR] = b"{}"
    if not ok(call("collector", {"op": "put", "dataset": "bronze", "key": BRONZE, "body_b64": b64(gz([{"Id": "1"}]))})):
        bad.append("collector put of a raw blob refused")
    if not ok(call("collector", {"op": "get_state", "key": CURSOR})):
        bad.append("collector cursor read refused")
    if ok(call("collector", {"op": "get_state", "key": COVER})):
        bad.append("collector read a coverage key")
    if ok(call("member", {"op": "put", "dataset": "bronze", "key": BRONZE2, "body_b64": b64(gz([{"Id": "2"}]))})):
        bad.append("member alias was served a put")
    for name, c in (("unqualified", ctx(None)), ("unknown alias", ctx("admin")), ("no context", None)):
        if ok(h.handle({"op": "timeline", "account": "pat@opalinvest.com", "start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z"},
                       c, s3=s3, log=logs.append, silver_reader=reader, silver_builder=builder, lambda_client=lam, now=NOW)):
            bad.append("%s was served a timeline" % name)
    if any("pat@" in x or "recon" in x for x in logs):
        bad.append("a log line carries an account or a file name")
    if bad:
        print("A1-OPS-REFUSED " + "; ".join(bad))
        return 1
    print("A1-OPS-OK calls_logged=%d" % len(logs))
    return 0


def bronze():
    h = load()
    import opal_naming as n

    os.environ["BUCKET"] = "opal-data-trino"
    s3 = FakeS3()
    logs = []
    seen = {}
    builder = types.SimpleNamespace(build=lambda records, only_date=None: seen.update(records=list(records), only=only_date) or b"PARQUET")

    def call(alias, ev):
        return h.handle(ev, ctx(alias), s3=s3, log=logs.append, silver_builder=builder, now=NOW)

    bad = []
    body1 = gz([{"Id": "first"}])
    r1 = call("collector", {"op": "put", "dataset": "bronze", "key": BRONZE, "body_b64": b64(body1)})
    r2 = call("collector", {"op": "put", "dataset": "bronze", "key": BRONZE, "body_b64": b64(gz([{"Id": "second"}]))})
    if not ok(r1):
        bad.append("first put refused: %r" % (r1,))
    if ok(r2) or r2.get("already_stored") is not True:
        bad.append("a second write to an existing bronze key must be refused with already_stored=true: %r" % (r2,))
    if s3.objs.get(BRONZE) != body1:
        bad.append("the stored bytes changed on a second write")
    if ok(call("collector", {"op": "put", "dataset": "bronze", "key": OLD, "body_b64": b64(body1)})) or OLD in s3.objs:
        bad.append("the frozen audit_events table accepted a write")
    # fail closed: a head that fails for any reason but "not found" must not become a write (a 500, a 403, a timeout)
    for code in ("500", "403", "SlowDown"):
        broken = FakeS3(head_error=code)
        rb = h.handle({"op": "put", "dataset": "bronze", "key": BRONZE, "body_b64": b64(body1)}, ctx("collector"), s3=broken, log=logs.append,
                      silver_builder=builder, now=NOW)
        if ok(rb) or BRONZE in broken.objs or broken.puts:
            bad.append("a head_object failure %s let a bronze put through: %r" % (code, rb))
    for code in ("404", "NoSuchKey", "NotFound"):
        gone = FakeS3()
        gone.head_error = code
        rg = h.handle({"op": "put", "dataset": "bronze", "key": BRONZE, "body_b64": b64(body1)}, ctx("collector"), s3=gone, log=logs.append,
                      silver_builder=builder, now=NOW)
        if not ok(rg) or BRONZE not in gone.objs:
            bad.append("a missing key (head code %s) was not written: %r" % (code, rg))
    # derive: audit_records of D and D+1, parsed records handed to the builder
    s3.objs[BRONZE2] = gz([{"Id": "next-day", "CreationTime": "2026-10-16T03:00:00Z"}])
    s3.objs[PFX + "bronze/audit_records/date=20261017/" + CID.replace("20261015", "20261017") + ".json.gz"] = gz([{"Id": "two-days-later"}])
    s3.objs[BRONZE] = gz([{"Id": "first", "CreationTime": "2026-10-15T14:00:00Z"}])
    d = call("collector", {"op": "derive_silver", "date": "2026-10-15"})
    ids = sorted(r.get("Id") for r in seen.get("records", []))
    if not ok(d) or set(d) - {"ok", "rows"}:
        bad.append("derive_silver must answer a count only: %r" % (d,))
    if ids != ["first", "next-day"] or seen.get("only") != "2026-10-15":
        bad.append("derive must read audit_records of D and D+1 (not D+2) and pass only_date=D: ids=%r only=%r" % (ids, seen.get("only")))
    if SILVER not in s3.objs:
        bad.append("the silver partition was not written")
    # key grammar vs the builder
    def strip(a):
        return a.split("s3://opal-data-trino/", 1)[1]

    good = strip(n.address("m365-metadata", "trino", "bronze", "audit_records", "date=20261015", object=CID + ".json.gz"))
    if not h.key_ok("bronze", good):
        bad.append("the builder's audit_records key is refused: %s" % good)
    for k in (PFX + "bronze/audit_records/date=20261015/recon.xlsx.json.gz",
              PFX + "bronze/audit_records/date=20261015/pat@opalinvest.com.json.gz",
              PFX + "bronze/audit_records/person=pat/date=20261015/" + CID + ".json.gz",
              PFX + "bronze/audit_records/date=20261015/../" + CID + ".json.gz",
              PFX + "bronze/audit_records/date=2026-10-15/" + CID + ".json.gz"):
        if h.key_ok("bronze", k):
            bad.append("a key carrying a name, an address or a bad partition was admitted: %s" % k)
    if h.key_ok("bronze", OLD) is True and ok(call("collector", {"op": "put", "dataset": "bronze", "key": OLD, "body_b64": b64(body1)})):
        bad.append("audit_events writable")
    if bad:
        print("A1-BRONZE-REFUSED " + "; ".join(bad))
        return 1
    print("A1-BRONZE-OK")
    return 0


def detail():
    """timeline with detail=true: every row carries the WHOLE raw record (parsed from silver's raw_json) so an investigator can see who acted
    (AppId, ClientAppId, UserAgent, ClientIPAddress, LogonType, ...). A sync Lambda answer is limited to 6 MB, so detail answers are capped at
    1000 rows and at 5,000,000 bytes of JSON, and say truncated. Without detail the answer is exactly as before."""
    h = load()
    os.environ["BUCKET"] = "opal-data-trino"
    s3 = FakeS3()
    seen = []

    def make_rows(n, pad=0):
        out = []
        for i in range(n):
            rec = {"Id": "r%d" % i, "CreationTime": "2026-10-10T11:%02d:%02d" % (i // 60 % 60, i % 60), "Operation": "MoveToDeletedItems",
                   "UserId": "pat@opalinvest.com", "ClientIPAddress": "203.0.113.9", "AppId": "app-%d" % (i % 3),
                   "ClientInfoString": "Client=Synthetic;" + "x" * pad}
            out.append({"time": "2026-10-10T11:%02d:%02dZ" % (i // 60 % 60, i % 60), "feed": "Exchange", "operation": "MoveToDeletedItems",
                        "result_status": "Succeeded", "client_ip": None, "item_name": None, "user_id": "pat@opalinvest.com",
                        "record_id": "r%d" % i, "raw_json": json.dumps(rec)})
        return out

    state = {"rows": make_rows(3)}

    def rows_fn(s3_, bucket, prefix, account, start, end, detail=False):
        seen.append(detail)
        rs = state["rows"]
        return [dict(r) for r in rs] if detail else [{k: v for k, v in r.items() if k != "raw_json"} for r in rs]

    reader = types.SimpleNamespace(timeline_rows=rows_fn)

    def call(ev):
        return h.handle(ev, ctx("member"), s3=s3, log=lambda x: None, silver_reader=reader, lambda_client=FakeLambda(), now=NOW)

    base = {"op": "timeline", "account": "pat@opalinvest.com", "start": "2026-10-10T00:00:00Z", "end": "2026-10-11T00:00:00Z"}
    bad = []
    plain = call(dict(base))
    if not ok(plain) or any("raw" in r or "raw_json" in r for r in plain.get("rows", [])):
        bad.append("a timeline without detail must carry no raw record: %r" % (plain.get("rows", [])[:1],))
    full = call(dict(base, detail=True))
    rows = full.get("rows", []) if isinstance(full, dict) else []
    if not ok(full) or len(rows) != 3 or full.get("truncated") is not False:
        bad.append("detail timeline answer %r" % ({k: v for k, v in (full or {}).items() if k != "rows"},))
    elif any(not isinstance(r.get("raw"), dict) or "raw_json" in r for r in rows) or rows[0]["raw"].get("AppId") != "app-0":
        bad.append("each detail row must carry the parsed record under 'raw' and no 'raw_json' string: %r" % (rows[0],))
    if True not in seen:
        bad.append("the door never asked its reader for detail")
    state["rows"] = make_rows(1200)
    capped = call(dict(base, detail=True))
    if not ok(capped) or len(capped.get("rows", [])) != 1000 or capped.get("truncated") is not True:
        bad.append("a detail answer must cap at 1000 rows with truncated=true (got %d)" % len(capped.get("rows", [])))
    state["rows"] = make_rows(900, pad=9000)
    big = call(dict(base, detail=True))
    size = len(json.dumps(big))
    if not ok(big) or size > 5000000 or big.get("truncated") is not True or not big.get("rows"):
        bad.append("a detail answer must stay under 5,000,000 bytes and say truncated (bytes %d, rows %d)" % (size, len(big.get("rows", []))))
    state["rows"] = make_rows(5001)
    nodetail = call(dict(base))
    if len(nodetail.get("rows", [])) != 5000 or nodetail.get("truncated") is not True:
        bad.append("without detail the cap stays 5000")
    for val in ("yes", 1, None):
        if ok(call(dict(base, detail=val))):
            bad.append("detail=%r must be refused (a boolean only)" % (val,))
    if bad:
        print("A1-DETAIL-REFUSED " + "; ".join(bad))
        return 1
    print("A1-DETAIL-OK")
    return 0


def tf():
    if not os.path.exists(ACCESS_TF):
        print("A1-TF-REFUSED no access.tf")
        return 1
    t = open(ACCESS_TF, encoding="utf-8").read()
    bad = []
    role = re.search(r'resource\s+"aws_iam_role_policy"\s+"access".*?\n}\n', t, re.S)
    # The door must NOT reference the collector RESOURCE: collector.tf's policy references the door's alias, so a reference back is a
    # Terraform dependency cycle (the first release plan stopped on exactly that). It names the collector by local.collector_lambda_name.
    if "aws_lambda_function.collector" in t:
        bad.append("access.tf references aws_lambda_function.collector (a dependency cycle with collector.tf); use local.collector_lambda_name")
    if not role or "function:${local.collector_lambda_name}" not in role.group(0) or "lambda:InvokeFunction" not in role.group(0):
        bad.append("the door role policy must allow lambda:InvokeFunction on the arn ending function:${local.collector_lambda_name} alone")
    fn = re.search(r'resource\s+"aws_lambda_function"\s+"access".*?\n}\n', t, re.S)
    if not fn or "COLLECTOR_FUNCTION" not in fn.group(0) or "COLLECTOR_FUNCTION = local.collector_lambda_name" not in fn.group(0):
        bad.append("the door function must set COLLECTOR_FUNCTION = local.collector_lambda_name")
    # The live release measured Runtime.OutOfMemory at 1024 MB when the door derived a busy day (raw records of every account,
    # two partitions held as Python dicts): the door needs memory and time for a day of raw records.
    mem = re.search(r"memory_size\s*=\s*(\d+)", fn.group(0)) if fn else None
    tmo = re.search(r"timeout\s*=\s*(\d+)", fn.group(0)) if fn else None
    if not mem or int(mem.group(1)) < 10240:
        bad.append("the door function memory_size must be 10240 MB (the Lambda maximum; Andrew-direct 2026-10-17) (derive of a busy raw day ran out of memory at 1024)")
    if not tmo or int(tmo.group(1)) < 600:
        bad.append("the door function timeout must be at least 600 s")
    if "TCKT" in t:
        bad.append("access.tf still mentions TCKT")
    deny = re.search(r"data_actions\s*=\s*\[(.*?)\]", t, re.S)
    if not deny or "s3:ListBucket" in deny.group(1) or "s3:GetObject" not in deny.group(1):
        bad.append("the bucket Deny's data actions changed")
    grp = re.search(r'resource\s+"aws_iam_group_policy"\s+"invoke".*?\n}\n', t, re.S)
    if not grp or "aws_lambda_alias.member.arn" not in grp.group(0) or "aws_lambda_function.access.arn" in grp.group(0):
        bad.append("the group policy must still invoke the member alias alone")
    if re.search(r'resource\s+"(aws_sns_[a-z_]+|aws_cloudwatch_metric_alarm)"', t) or re.search(r'Principal\s*=\s*"\*"', t):
        bad.append("an alarm or a wildcard principal")
    if bad:
        print("A1-TF-REFUSED " + "; ".join(bad))
        return 1
    print("A1-TF-OK")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    fn_ = {"ops": ops, "bronze": bronze, "detail": detail, "tf": tf}.get(mode)
    try:
        sys.exit(fn_() if fn_ else 2)
    except FileNotFoundError as e:
        print("A1-%s-REFUSED missing %s" % (mode.upper(), e))
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        print("A1-%s-REFUSED %s: %s" % (mode.upper(), type(e).__name__, str(e)[:200]))
        sys.exit(1)
