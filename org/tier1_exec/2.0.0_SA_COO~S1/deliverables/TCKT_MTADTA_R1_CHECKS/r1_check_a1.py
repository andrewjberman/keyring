"""TCKT_MTADTA round 1, cell MD-a-1 checks. Run from the repo (worktree) root.

  python r1_check_a1.py handler -> A1-HANDLER-OK (the one door, driven with a fake S3 client)
  python r1_check_a1.py tf      -> A1-TF-OK      (group, role, function, and the two single-principal policies)
"""
import gzip
import importlib.util
import io
import json
import os
import re
import sys

ROOT = os.getcwd()
HANDLER = os.path.join(ROOT, "infra", "aws", "lambda", "globgrph-trino-access", "handler.py")
ACCESS_TF = os.path.join(ROOT, "infra", "aws", "terraform", "trino", "access.tf")
PFX = "m365-metadata/trino/"


class FakeS3:
    def __init__(self):
        self.objs = {}
        self.puts = []

    def put_object(self, Bucket, Key, Body, **kw):
        self.puts.append((Bucket, Key, kw))
        self.objs[(Bucket, Key)] = Body if isinstance(Body, bytes) else Body.encode()
        return {}

    def get_object(self, Bucket, Key, **kw):
        if (Bucket, Key) not in self.objs:
            raise KeyError(Key)
        return {"Body": io.BytesIO(self.objs[(Bucket, Key)])}

    def list_objects_v2(self, Bucket, Prefix="", **kw):
        keys = sorted(k for (b, k) in self.objs if b == Bucket and k.startswith(Prefix))
        return {"Contents": [{"Key": k} for k in keys], "IsTruncated": False}


def load():
    spec = importlib.util.spec_from_file_location("trino_access_handler", HANDLER)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def handler():
    if not os.path.exists(HANDLER):
        print("A1-HANDLER-REFUSED no handler.py")
        return 1
    h = load()
    s3 = FakeS3()
    logs = []
    call = lambda ev: h.handle(ev, None, s3=s3, log=logs.append)  # noqa: E731
    bad = []
    body = base64_of(gzip.compress(b'{"event_id":"e1"}\n'))
    k_ok = PFX + "bronze/audit_events/date=20261016/events.json.gz"
    r = call({"op": "put", "dataset": "bronze", "key": k_ok, "body_b64": body})
    if not (isinstance(r, dict) and r.get("ok") is True and any(k == k_ok for _, k, _ in s3.puts)):
        bad.append("put under the prefix did not land: %r" % (r,))
    if s3.puts and s3.puts[0][2].get("ServerSideEncryption") != "aws:kms":
        bad.append("put did not ask for SSE-KMS")
    n_before = len(s3.puts)
    r = call({"op": "put", "dataset": "bronze", "key": "other-source/x.json", "body_b64": body})
    if not (isinstance(r, dict) and r.get("ok") is False) or len(s3.puts) != n_before:
        bad.append("a key outside the prefix was not refused")
    r = call({"op": "put", "dataset": "bronze", "key": PFX + "../escape", "body_b64": body})
    if not (isinstance(r, dict) and r.get("ok") is False):
        bad.append("a dot-dot key was not refused")
    r = call({"op": "get", "dataset": "bronze", "key": k_ok})
    if not (isinstance(r, dict) and r.get("ok") is False) or "event_id" in json.dumps(r):
        bad.append("raw bronze came back from get")
    r = call({"op": "nonsense"})
    if not (isinstance(r, dict) and r.get("ok") is False):
        bad.append("an unknown op was not refused")
    # get_day over a fake silver: the module must expose the reader as handle()'s op, with rows sorted by time.
    rows = [
        {"event_id": "b", "creation_time": "2026-10-15T14:00:00Z", "actor": "yang@opalinvest.com", "operation": "FileAccessed"},
        {"event_id": "a", "creation_time": "2026-10-15T13:00:00Z", "actor": "yang@opalinvest.com", "operation": "MailItemsAccessed"},
        {"event_id": "z", "creation_time": "2026-10-15T13:30:00Z", "actor": "bobby@opalinvest.com", "operation": "FileAccessed"},
    ]
    stub = type("Stub", (), {"read_day_rows": staticmethod(lambda s3, bucket, prefix, person, date: rows)})
    r = h.handle({"op": "get_day", "person": "yang@opalinvest.com", "date": "2026-10-15"}, None, s3=s3,
                 log=logs.append, silver_reader=stub)
    got = [x.get("event_id") for x in (r.get("rows") if isinstance(r, dict) else []) or []]
    if got != ["a", "b"]:
        bad.append("get_day not the person's rows in time order: %r" % (got,))
    r = h.handle({"op": "get_day", "person": "someone@example.com", "date": "2026-10-15"}, None, s3=s3,
                 log=logs.append, silver_reader=stub)
    if not (isinstance(r, dict) and r.get("ok") is False):
        bad.append("get_day for a non-member was not refused")
    if len(logs) < 6:
        bad.append("every call must be logged (%d log lines for 7 calls)" % len(logs))
    if bad:
        print("A1-HANDLER-REFUSED " + "; ".join(bad))
        return 1
    print("A1-HANDLER-OK calls_logged=%d" % len(logs))
    return 0


def base64_of(b):
    import base64

    return base64.b64encode(b).decode()


def tf():
    if not os.path.exists(ACCESS_TF):
        print("A1-TF-REFUSED no access.tf")
        return 1
    t = open(ACCESS_TF, encoding="utf-8").read()
    bad = []
    for res in ("aws_iam_group", "aws_iam_role", "aws_lambda_function", "aws_s3_bucket_policy", "aws_kms_key_policy",
                "aws_iam_group_policy"):
        if not re.search(r'resource\s+"%s"' % res, t):
            bad.append("missing " + res)
    for nm in ("globgrph-trino-access-group", "globgrph-trino-access-lambda", "globgrph-trino-access-role"):
        if nm not in t and not re.search(r"opal_name|name\(", t):
            bad.append("name %s not from the builder" % nm)
    # No wildcard allow principal, no wildcard Allow action on the bucket.
    if re.search(r'Principal\s*=\s*"\*"', t) or re.search(r'Principal\s*=\s*\{\s*AWS\s*=\s*"\*"', t):
        bad.append("a wildcard principal")
    if "Deny" not in t or "NotPrincipal" not in t and "StringNotEquals" not in t:
        bad.append("no explicit Deny of every principal but the role")
    if re.search(r'resource\s+"(aws_sns_[a-z_]+|aws_cloudwatch_metric_alarm|aws_ses_[a-z_]+)"', t):
        bad.append("an alarm or notification resource (C-NOALERT)")
    if bad:
        print("A1-TF-REFUSED " + "; ".join(bad))
        return 1
    print("A1-TF-OK")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"handler": handler, "tf": tf}.get(mode)
    sys.exit(fn() if fn else 2)
