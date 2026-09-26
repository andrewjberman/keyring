"""The /analysis composition, proved WITHOUT a principal (CTO 101355): the deployed generate code, in-process.

    python offline_submit_proof.py --zip <generate.zip> [--overlay <dir>] --tenant cottonwood --input-id portfolio_...

What runs: the served zip's own modules (optionally with overlay files copied over them: the fix under test), loaded
from a fresh extract that is FIRST on sys.path. The real `generate_installed.compose_ports` and `build_boundary`, and
the real served Entry, handle one API-Gateway-shaped POST /analysis for an Opal viewer (verified-edge headers), with
report_title null, on a REAL normalized input.

Clients:
- Every READ goes to the live table or bucket (get_item, query, get_object, head_object; read-only).
- Every WRITE is captured in memory and never leaves the process (put_item, update_item, transact_write_items,
  put_object, send_message).
- Any other SDK method raises.

The one seeded fact is the viewer's canonical user profile, because a walk principal is deleted after its window.

Stages are recorded by a call tracer over functions defined in the extract. The run STOPS at the queue send. This
Lambda makes no vendor call; the first YCharts write is the resident's holdings_upload, which consumes the captured
message. The census at the end prints where every loaded first-party module came from: all must be the extract.
"""
import argparse
import copy
import json
import os
import shutil
import sys
import tempfile
import time
import zipfile

import boto3
from botocore.exceptions import ClientError

STAGES = ("submit", "validate_public_request", "current", "authorize_current", "read_input", "capture_title_source",
          "resolve_profile_fields", "resolve_comparison_fields", "capture_configuration", "admit", "validate_bindings",
          "accept", "dispatch", "put", "publish", "reserve", "send")


def cond_fail():
    return ClientError({"Error": {"Code": "ConditionalCheckFailedException", "Message": "offline"}}, "PutItem")


class CapturedWrites:
    def __init__(self):
        self.log = []

    def add(self, kind, **what):
        self.log.append(dict(kind=kind, **what))


class ReadThroughDynamo:
    """Low-level client: reads live, writes captured. Keyed by table and the item's key attributes."""
    KEYS = {"irpt-requests": ("tenant", "request_revision"), "irpt-jobs": ("tenant", "job"), "opal-users-v2": ("PK", "SK")}

    def __init__(self, real, writes, seeded_users):
        self.real, self.writes, self.mem = real, writes, {}
        self.meta = real.meta
        self.users = seeded_users  # email -> typed PROFILE item

    def _k(self, table, key):
        return (table,) + tuple(json.dumps(key[a], sort_keys=True) for a in self.KEYS[table])

    def get_item(self, TableName, Key, **kw):
        k = self._k(TableName, Key)
        if k in self.mem:
            return {"Item": copy.deepcopy(self.mem[k])}
        if TableName == "opal-users-v2":
            for item in self.users.values():
                if item["PK"] == Key["PK"] and item["SK"] == Key["SK"]:
                    return {"Item": copy.deepcopy(item)}
        return self.real.get_item(TableName=TableName, Key=Key, **kw)

    def query(self, **kw):
        if kw.get("TableName") == "opal-users-v2" and kw.get("IndexName") == "email-index":
            email = next(iter(kw["ExpressionAttributeValues"].values()))["S"]
            if email in self.users:
                item = self.users[email]
                return {"Items": [{"PK": item["PK"], "SK": item["SK"], "email": item["email"]}], "Count": 1}
        return self.real.query(**kw)

    def put_item(self, TableName, Item, **kw):
        self._put(TableName, Item, kw.get("ConditionExpression"))
        return {}

    def _put(self, table, item, condition):
        k = self._k(table, item)
        exists = k in self.mem or "Item" in self.real.get_item(TableName=table, Key={a: item[a] for a in self.KEYS[table]}, ConsistentRead=True)
        if condition and "attribute_not_exists" in condition and exists:
            raise cond_fail()
        self.mem[k] = copy.deepcopy(item)
        self.writes.add("dynamodb.put", table=table, key=[item[a].get("S") for a in self.KEYS[table]])

    def update_item(self, TableName, Key, UpdateExpression, **kw):
        k = self._k(TableName, Key)
        base = self.mem.get(k) or self.real.get_item(TableName=TableName, Key=Key, ConsistentRead=True).get("Item") or dict(Key)
        item, values = copy.deepcopy(base), kw.get("ExpressionAttributeValues", {})
        names = kw.get("ExpressionAttributeNames", {})
        for clause in UpdateExpression.replace(" REMOVE ", "\nREMOVE ").split("\n"):
            clause = clause.strip()
            if clause.startswith("SET "):
                for part in clause[4:].split(","):
                    left, right = (s.strip() for s in part.split("="))
                    item[names.get(left, left)] = values[right]
            elif clause.startswith("REMOVE "):
                for name in clause[7:].split(","):
                    item.pop(names.get(name.strip(), name.strip()), None)
        self.mem[k] = item
        self.writes.add("dynamodb.update", table=TableName, key=[Key[a].get("S") for a in self.KEYS[TableName]],
                        expression=UpdateExpression)
        return {}

    def transact_write_items(self, TransactItems, **kw):
        for op in TransactItems:
            (kind, body), = op.items()
            if kind != "Put":
                raise NotImplementedError("offline transact kind " + kind)
            self._put(body["TableName"], body["Item"], body.get("ConditionExpression"))
        self.writes.add("dynamodb.transact", count=len(TransactItems))
        return {}

    def __getattr__(self, name):
        raise AttributeError("offline dynamodb client has no " + name)


class ReadThroughTable:
    """boto3 resource Table for irpt-requests: reads live, writes captured."""

    def __init__(self, real, writes):
        self.real, self.writes, self.mem, self.name = real, writes, {}, real.name

    def get_item(self, Key, **kw):
        k = (Key["tenant"], Key["request_revision"])
        if k in self.mem:
            return {"Item": copy.deepcopy(self.mem[k])}
        return self.real.get_item(Key=Key, **kw)

    def put_item(self, Item, ConditionExpression=None, **kw):
        k = (Item["tenant"], Item["request_revision"])
        live = self.real.get_item(Key={"tenant": k[0], "request_revision": k[1]}, ConsistentRead=True).get("Item")
        current = self.mem.get(k, live)
        if ConditionExpression and "attribute_not_exists" in ConditionExpression and current is not None:
            raise cond_fail()
        if ConditionExpression and "attribute_not_exists" not in ConditionExpression:
            names, values = kw.get("ExpressionAttributeNames", {}), kw.get("ExpressionAttributeValues", {})
            if current is None or any(current.get(names[a]) != values[":" + a[1:]] for a in names):
                raise cond_fail()
        self.mem[k] = copy.deepcopy(Item)
        self.writes.add("table.put", key=list(k))
        return {}

    def query(self, **kw):
        return self.real.query(**kw)

    def __getattr__(self, name):
        raise AttributeError("offline table has no " + name)


class ReadThroughS3:
    def __init__(self, real, writes):
        self.real, self.writes, self.mem, self.n = real, writes, {}, 0

    def put_object(self, Bucket, Key, Body, **kw):
        if kw.get("IfNoneMatch") == "*" and ((Bucket, Key) in self.mem or self._live_exists(Bucket, Key)):
            raise ClientError({"Error": {"Code": "PreconditionFailed", "Message": "offline"}}, "PutObject")
        self.n += 1
        version = "offline-%d" % self.n
        self.mem[(Bucket, Key)] = (version, bytes(Body))
        self.writes.add("s3.put", bucket=Bucket, key=Key, bytes=len(Body))
        return {"VersionId": version}

    def _live_exists(self, bucket, key):
        try:
            self.real.head_object(Bucket=bucket, Key=key)
            return True
        except ClientError:
            return False

    def head_object(self, Bucket, Key, **kw):
        if (Bucket, Key) in self.mem:
            return {"VersionId": self.mem[(Bucket, Key)][0]}
        return self.real.head_object(Bucket=Bucket, Key=Key, **kw)

    def get_object(self, Bucket, Key, **kw):
        if (Bucket, Key) in self.mem:
            version, data = self.mem[(Bucket, Key)]
            import io
            return {"Body": io.BytesIO(data), "VersionId": version, "ContentLength": len(data)}
        return self.real.get_object(Bucket=Bucket, Key=Key, **kw)

    def __getattr__(self, name):
        raise AttributeError("offline s3 has no " + name)


class CapturedSqs:
    def __init__(self, writes):
        self.writes, self.sent = writes, []

    def send_message(self, QueueUrl, MessageBody, **kw):
        self.sent.append(MessageBody)
        self.writes.add("sqs.send", queue=QueueUrl, bytes=len(MessageBody))
        return {"MessageId": "offline-%d" % len(self.sent)}

    def __getattr__(self, name):
        raise AttributeError("offline sqs has no " + name)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", required=True)
    ap.add_argument("--overlay", help="a directory whose files replace the zip's same-named files")
    ap.add_argument("--tenant", default="cottonwood")
    ap.add_argument("--input-id", required=True)
    ap.add_argument("--viewer", default="irpt-offline-proof@opal.test")
    ap.add_argument("--out", help="directory to write the captured composition and queue message (for a resident replay)")
    a = ap.parse_args(argv)

    extract = tempfile.mkdtemp(prefix="irpt-proof-")
    zipfile.ZipFile(a.zip).extractall(extract)
    overlaid = []
    if a.overlay:
        for name in sorted(os.listdir(a.overlay)):
            if os.path.isfile(os.path.join(a.overlay, name)):  # files only; a __pycache__ dir is not an overlay
                shutil.copyfile(os.path.join(a.overlay, name), os.path.join(extract, name))
                overlaid.append(name)
    sys.path.insert(0, extract)
    os.environ.setdefault("IRPT_DIRECTORY_BUCKET_MAP", json.dumps({"49financial": "opal-data-bd", "cottonwood": "opal-data-cot", "inflection": "opal-data-inf"}))
    print("extract", extract, "| overlay", overlaid or "none")

    writes = CapturedWrites()
    region = "us-east-1"
    seeded = {a.viewer: {"PK": {"S": "USER#" + a.viewer}, "SK": {"S": "PROFILE"}, "email": {"S": a.viewer},
                         "firmId": {"S": "opal-capital"}, "status": {"S": "active"}, "name": {"S": "Offline Proof Viewer"}}}
    ddb = ReadThroughDynamo(boto3.client("dynamodb", region_name=region), writes, seeded)
    table = ReadThroughTable(boto3.resource("dynamodb", region_name=region).Table("irpt-requests"), writes)
    s3 = ReadThroughS3(boto3.client("s3", region_name=region), writes)
    sqs = CapturedSqs(writes)

    reached = []

    def tracer(frame, event, arg):
        if event == "call":
            code = frame.f_code
            if code.co_filename.startswith(extract) and code.co_name in STAGES:
                label = "%s.%s" % (os.path.basename(code.co_filename)[:-3], code.co_name)
                if not reached or reached[-1] != label:
                    reached.append(label)
        return None

    import generate_installed as gi
    import composition_admission as _ca
    _validate = _ca.CompositionAdmission.validate

    def validate_reporting_cause(self, document):
        # Diagnostic only: print the chained cause of a CLOSED_COMPOSITION_REQUIRED, then re-raise it unchanged.
        try:
            return _validate(self, document)
        except Exception as exc:
            cause = exc.__cause__
            print("ADMISSION REFUSED:", type(exc).__name__, exc, "| cause:", type(cause).__name__ if cause else None,
                  str(cause)[:700] if cause else "",
                  "| at", list(getattr(cause, "absolute_path", []))[:12], "| schema", list(getattr(cause, "absolute_schema_path", []))[:14])
            raise
    _ca.CompositionAdmission.validate = validate_reporting_cause
    env = {gi.QUEUE_URL_ENV: "https://sqs.us-east-1.amazonaws.com/313476888478/irpt-generation",
           gi.REQUESTS_TABLE_ENV: "irpt-requests", gi.JOBS_TABLE_ENV: "irpt-jobs"}
    ports = gi.compose_ports(clients={"dynamodb": ddb, "table": table, "s3": s3, "sqs": sqs}, environ=env,
                             clock=time.time)
    boundary = gi.build_boundary(ports)
    body = {"request_id": "y-offline-proof-%d" % int(time.time()), "client_id": None, "account_ids": [],
            "snapshot_id": None, "variant": "overview", "comparison_keys": [], "report_title": None,
            "prepared_for": "IRPT offline proof", "input_id": a.input_id}
    headers = {"x-contract-version": "v1", "x-origin-verify": "cloudfront", "x-user-email": a.viewer,
               "x-user-role": "admin", "x-user-type": "Dev", "x-firm-id": "opal-capital", "x-user-name": "Offline Proof Viewer"}
    event = {"routeKey": "POST /api/scoped/investor-reporting/analysis", "headers": headers,
             "queryStringParameters": {"selected_tenant": a.tenant}, "body": json.dumps(body)}

    sys.settrace(tracer)
    try:
        answer = boundary.handle(event)
    finally:
        sys.settrace(None)

    print("\nANSWER:", json.dumps({k: answer.get(k) for k in ("ok", "status", "operation")}, default=str)[:600])
    data = answer.get("data")
    print("DATA keys:", sorted(data) if isinstance(data, dict) else data)
    print("\nSTAGES REACHED (%d):" % len(reached))
    for i, s in enumerate(reached, 1):
        print("  %2d %s" % (i, s))
    print("\nCAPTURED WRITES (%d; none left this process):" % len(writes.log))
    for w in writes.log:
        print("  ", json.dumps(w)[:230])
    composition = None
    for (bucket, key), (_, blob) in s3.mem.items():
        if "/request_compositions/" in key:
            composition = json.loads(blob)
    if composition:
        resolved = composition.get("resolved", {})
        prof, prov = resolved.get("profile", {}), resolved.get("profile_provenance", {})
        title_src = prov.get("report_title", {}).get("source_id")
        print("\nCOMPOSITION: report_title=%r from source %r (kind %s); prepared_by=%r; organization=%r"
              % (prof.get("report_title"), title_src, resolved.get("source_descriptors", {}).get(title_src, {}).get("source_kind"),
                 prof.get("prepared_by"), prof.get("organization")))
    print("QUEUE MESSAGES:", [json.loads(m).get("kind") for m in sqs.sent])
    if a.out and composition:
        os.makedirs(a.out, exist_ok=True)
        json.dump(composition, open(os.path.join(a.out, "composition.json"), "w", encoding="utf-8"), sort_keys=True)
        json.dump([json.loads(m) for m in sqs.sent], open(os.path.join(a.out, "messages.json"), "w", encoding="utf-8"))
        print("WROTE", os.path.join(a.out, "composition.json"), "and messages.json")
    loaded = {m.__name__: getattr(m, "__file__", None) for m in list(sys.modules.values()) if getattr(m, "__file__", None)}
    first_party = {n: f for n, f in loaded.items() if os.path.exists(os.path.join(extract, n + ".py"))}
    # Compare by file identity: Windows reports the same directory as a short (ANDREW~1) or long path.
    outside = {n: f for n, f in first_party.items() if not os.path.samefile(os.path.dirname(f), extract)}
    print("\nMODULE CENSUS: %d first-party modules loaded, %d from the extract, %d from elsewhere %s"
          % (len(first_party), len(first_party) - len(outside), len(outside), sorted(outside) or ""))
    for n, f in sorted(outside.items()):
        print("   OUTSIDE %s <- %s" % (n, f))
    print("   sys.path head:", [p for p in sys.path[:8]])
    refused = not isinstance(data, dict) or answer.get("ok") is False
    print("\nRESULT:", "REFUSED" if refused else "ACCEPTED", "| stopped at the queue send; no vendor call is made by this Lambda")
    return 1 if refused or outside else 0


if __name__ == "__main__":
    sys.exit(main())
