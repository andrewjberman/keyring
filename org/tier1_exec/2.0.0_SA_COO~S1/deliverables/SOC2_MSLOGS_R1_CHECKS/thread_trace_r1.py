"""SOC2_MSLOGS round 1 thread trace at the drain: the REAL collector, door, silver builder and timeline reader wired together over an
in-memory S3, with a fake Management API. Synthetic records only. Run from the repo root.   python thread_trace_r1.py -> THREAD-R1-OK
"""
import base64
import importlib.util
import json
import os
import sys
import types

ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, "lib"))
CK = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.join(ROOT, "data", "m365_metadata", "scripts", "collector")
DOOR = os.path.join(ROOT, "infra", "aws", "lambda", "globgrph-trino-access")
sys.path[:0] = [PKG, DOOR]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


a1 = load(os.path.join(CK, "s1_check_a1.py"), "tt_a1")
collect = load(os.path.join(PKG, "collect.py"), "tt_collect")
door = load(os.path.join(DOOR, "handler.py"), "tt_door")
builder = load(os.path.join(DOOR, "silver_builder.py"), "tt_builder")
reader = load(os.path.join(ROOT, "data", "m365_metadata", "scripts", "silver", "read_timeline.py"), "tt_reader")
FN = a1.FN
os.environ["BUCKET"] = "opal-data-trino"
os.environ["COLLECTOR_FUNCTION"] = "m365-metadata-trino-collector-lambda"
NOW = "2026-10-16T12:00:00Z"


def recs(who, other):
    return [{"Id": "r-%s-1" % who, "CreationTime": "2026-10-15T14:00:00", "Workload": "Exchange", "RecordType": 2, "Operation": "MailItemsAccessed",
             "UserId": who, "ClientIP": "203.0.113.9", "ResultStatus": "Succeeded"},
            {"Id": "r-%s-2" % other, "CreationTime": "2026-10-15T15:00:00", "Workload": "SharePoint", "RecordType": 6, "Operation": "FileDownloaded",
             "UserId": other, "ClientIP": "198.51.100.4", "SourceFileName": "q3.xlsx"}]


class Source:
    def __init__(self):
        cid = "20261015140000000001$20261015140000000001$audit_exchange$Audit_Exchange$na0001"
        self.raw = (json.dumps(recs("pat@opalinvest.com", "sam@opalinvest.com"), indent=1) + "\n").encode()
        self.cid = cid

    def list_content(self, ct, start, end):
        return [{"id": self.cid, "created": "2026-10-15T14:00:00.000Z"}] if ct == "Audit.Exchange" else []

    def fetch_raw(self, ct, blob_id):
        return self.raw


class Access:
    """The collector's client of the door: the real door handler, collector alias, in-memory S3."""

    def __init__(self, s3, lam):
        self.s3, self.lam = s3, lam

    def _call(self, ev, alias="collector"):
        ctx = types.SimpleNamespace(invoked_function_arn=FN + ":" + alias)
        return door.handle(ev, ctx, s3=self.s3, log=lambda x: None, silver_builder=builder, lambda_client=self.lam, now=NOW)

    def put(self, dataset, key, body):
        r = self._call({"op": "put", "dataset": dataset, "key": key, "body_b64": base64.b64encode(body).decode()})
        if r.get("ok") or r.get("already_stored"):
            return r
        raise RuntimeError("door refused put: %s" % r.get("error"))

    def get_state(self, key):
        r = self._call({"op": "get_state", "key": key})
        return base64.b64decode(r["body_b64"]) if r.get("ok") else None

    def derive_silver(self, date):
        return self._call({"op": "derive_silver", "date": date})


def main():
    bad = []
    s3, lam = a1.FakeS3(), a1.FakeLambda()
    acc = Access(s3, lam)
    out = collect.run_once(Source(), acc, {}, NOW)
    if out.get("failed") != 0 or out.get("fetched") != 1 or not out.get("complete"):
        bad.append("collector fire %r" % ({k: v for k, v in out.items() if k != "cursor"},))
    bronze = [k for k in s3.objs if "/bronze/audit_records/" in k]
    silver = [k for k in s3.objs if "/silver/activity_events/" in k]
    if len(bronze) != 1 or not silver:
        bad.append("bronze=%d silver=%d" % (len(bronze), len(silver)))
    again = collect.run_once(Source(), acc, {}, NOW, cursor=out["cursor"])
    if again.get("fetched") != 0:
        bad.append("second fire re-fetched")
    cold = collect.run_once(Source(), acc, {}, NOW, cursor=None)
    if cold.get("already_stored") != 1 or cold.get("failed") != 0:
        bad.append("cold start over a stored blob: %r" % ({k: v for k, v in cold.items() if k != "cursor"},))
    ctx = types.SimpleNamespace(invoked_function_arn=FN + ":member")

    def invoker(p):
        return door.handle(p, ctx, s3=s3, log=lambda x: None, silver_builder=builder, lambda_client=lam, now=NOW)

    reply = reader.fetch(invoker, "Pat@OpalInvest.com", "2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z")
    text = reader.render(reply)
    if "MailItemsAccessed" not in text or "FileDownloaded" in text or "203.0.113.9" not in text:
        bad.append("timeline for pat: %r" % text[:200])
    other = reader.render(reader.fetch(invoker, "sam@opalinvest.com", "2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z"))
    if "FileDownloaded" not in other or "q3.xlsx" not in other:
        bad.append("timeline for sam: %r" % other[:200])
    if "no activity collected" not in reader.render(reader.fetch(invoker, "nobody@opalinvest.com", "2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z")):
        bad.append("unknown account not reported empty")
    rc = door.handle({"op": "recollect", "start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z"}, ctx, s3=s3, log=lambda x: None, lambda_client=lam, now=NOW)
    if not rc.get("ok") or len(lam.calls) != 1:
        bad.append("recollect %r" % (rc,))
    if bad:
        print("THREAD-R1-REFUSED " + "; ".join(bad))
        return 1
    print("THREAD-R1-OK bronze=%d silver=%d" % (len(bronze), len(silver)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
