"""Read-through / write-capture AWS doubles for the offline hop proofs. READS go to the live service; WRITES stay in
memory and never leave the process; any other SDK method raises.

One typed DynamoDB store backs both the low-level client and the boto3 Table resource, so a row the resident writes
through the client is read back through the resource exactly as in AWS. State dumps to and loads from JSON, so the
generate phase and the resident phase (separate processes, separate code trees) share one world.

Conditions: `attribute_not_exists(...)` on a Put and the NormalizationStates `#s = :s [AND #d = :d]` conditional put
are evaluated. Every other ConditionExpression is RECORDED, not evaluated: a single-writer run is not a race test, and
the unit suites own the conditional semantics.
"""
import base64
import copy
import io
import json
import re

from boto3.dynamodb.types import TypeDeserializer, TypeSerializer
from botocore.exceptions import ClientError

KEYS = {"irpt-requests": ("tenant", "request_revision"), "irpt-jobs": ("tenant", "job"), "opal-users-v2": ("PK", "SK")}
_ser, _de = TypeSerializer(), TypeDeserializer()


def typed(item):
    return {k: _ser.serialize(v) for k, v in item.items()}


def plain(item):
    return {k: _de.deserialize(v) for k, v in item.items()}


def fail(code="ConditionalCheckFailedException", op="PutItem"):
    return ClientError({"Error": {"Code": code, "Message": "offline"}}, op)


class Writes:
    def __init__(self):
        self.log, self.reads = [], []

    def read(self, kind, **what):
        self.reads.append(dict(kind=kind, **what))

    def add(self, kind, **what):
        self.log.append(dict(kind=kind, **what))


class Dynamo:
    """Low-level client over the shared typed store."""

    def __init__(self, real, writes, seeded_users=None):
        self.real, self.writes, self.mem = real, writes, {}
        self.meta = real.meta
        self.users = seeded_users or {}

    def _k(self, table, key):
        return (table,) + tuple(json.dumps(key[a], sort_keys=True) for a in KEYS[table])

    def _live(self, table, key):
        return self.real.get_item(TableName=table, Key={a: key[a] for a in KEYS[table]}, ConsistentRead=True).get("Item")

    def current(self, table, key):
        k = self._k(table, key)
        if k in self.mem:
            return copy.deepcopy(self.mem[k])
        if table == "opal-users-v2":
            for item in self.users.values():
                if item["PK"] == key["PK"] and item["SK"] == key["SK"]:
                    return copy.deepcopy(item)
        return self._live(table, key)

    def get_item(self, TableName, Key, **kw):
        self.writes.read("dynamodb:GetItem", table=TableName, key=[next(iter(v.values())) for v in Key.values()])
        item = self.current(TableName, Key)
        return {"Item": item} if item is not None else {}

    def query(self, **kw):
        self.writes.read("dynamodb:Query", table=kw.get("TableName"), index=kw.get("IndexName"))
        if kw.get("TableName") == "opal-users-v2" and kw.get("IndexName") == "email-index":
            email = next(iter(kw["ExpressionAttributeValues"].values()))["S"]
            if email in self.users:
                item = self.users[email]
                return {"Items": [{"PK": item["PK"], "SK": item["SK"], "email": item["email"]}], "Count": 1}
        page = self.real.query(**kw)
        table = kw.get("TableName")
        if table in KEYS and "IndexName" not in kw:
            page = dict(page, Items=self._merge(table, page.get("Items", []), kw))
        return page

    def _merge(self, table, live_items, kw):
        # Captured rows under the queried partition/prefix join the live page (single-page offline use).
        values = kw.get("ExpressionAttributeValues", {})
        pk_name = KEYS[table][0]
        pk = next((v for k, v in values.items() if k in (":t", ":tenant", ":pk")), None)
        prefix = next((v.get("S") for k, v in values.items() if k in (":r", ":p", ":prefix")), None)
        by_key = {self._k(table, i): i for i in live_items}
        for k, item in self.mem.items():
            if k[0] == table and pk is not None and item.get(pk_name) == pk:
                sort = item.get(KEYS[table][1], {}).get("S", "")
                if prefix is None or sort.startswith(prefix):
                    by_key[k] = copy.deepcopy(item)
        return list(by_key.values())

    def put_item(self, TableName, Item, **kw):
        self._put(TableName, Item, kw.get("ConditionExpression"), kw)
        return {}

    def _put(self, table, item, condition, kw=None):
        current = self.current(table, item)
        if condition and "attribute_not_exists" in condition and current is not None:
            raise fail()
        if condition and re.fullmatch(r"#s = :s( AND #d = :d)?", condition.strip()):
            names, values = kw.get("ExpressionAttributeNames", {}), kw.get("ExpressionAttributeValues", {})
            if current is None or any(current.get(names[a]) != values[":" + a[1:]] for a in names):
                raise fail()
        self.mem[self._k(table, item)] = copy.deepcopy(item)
        self.writes.add("dynamodb.put", table=table, key=[item[a].get("S") for a in KEYS[table]],
                        condition=condition)

    def update_item(self, TableName, Key, UpdateExpression, **kw):
        k = self._k(TableName, Key)
        item = self.current(TableName, Key) or copy.deepcopy(Key)
        names, values = kw.get("ExpressionAttributeNames", {}), kw.get("ExpressionAttributeValues", {})

        def name(token):
            return names.get(token.strip(), token.strip())
        for verb, body in re.findall(r"(SET|REMOVE|ADD)\s+(.*?)(?=\s+(?:SET|REMOVE|ADD)\s+|$)", UpdateExpression.strip()):
            for part in [p for p in body.split(",") if p.strip()]:
                if verb == "SET":
                    left, right = (s.strip() for s in part.split("=", 1))
                    item[name(left)] = values[right]
                elif verb == "REMOVE":
                    item.pop(name(part), None)
                else:
                    field, value = part.split()
                    base = int(item.get(name(field), {"N": "0"})["N"])
                    item[name(field)] = {"N": str(base + int(values[value]["N"]))}
        self.mem[k] = item
        self.writes.add("dynamodb.update", table=TableName, key=[Key[a].get("S") for a in KEYS[TableName]],
                        expression=UpdateExpression)
        return {"Attributes": copy.deepcopy(item)}

    def transact_write_items(self, TransactItems, **kw):
        for op in TransactItems:
            (verb, body), = op.items()
            if verb == "Put":
                self._put(body["TableName"], body["Item"], body.get("ConditionExpression"), body)
            elif verb == "Update":
                self.update_item(**{k: v for k, v in body.items() if k != "ConditionExpression"})
            elif verb == "ConditionCheck":
                self.writes.add("dynamodb.condition_check", table=body["TableName"], condition=body.get("ConditionExpression"))
            else:
                raise NotImplementedError("offline transact verb " + verb)
        self.writes.add("dynamodb.transact", verbs=[next(iter(op)) for op in TransactItems])
        return {}

    def __getattr__(self, attr):
        raise AttributeError("offline dynamodb client has no " + attr)


class Table:
    """boto3 resource Table over the SAME typed store (plain in, plain out)."""

    def __init__(self, dynamo, name):
        self.dynamo, self.name = dynamo, name

    def get_item(self, Key, **kw):
        item = self.dynamo.current(self.name, typed(Key))
        return {"Item": plain(item)} if item is not None else {}

    def put_item(self, Item, ConditionExpression=None, **kw):
        extra = dict(kw)
        if "ExpressionAttributeValues" in extra:
            extra["ExpressionAttributeValues"] = typed(extra["ExpressionAttributeValues"])
        self.dynamo._put(self.name, typed(Item), ConditionExpression, extra)
        return {}

    def query(self, **kw):
        low = dict(kw, TableName=self.name)
        if "ExpressionAttributeValues" in low:
            low["ExpressionAttributeValues"] = typed(low["ExpressionAttributeValues"])
        if "ExclusiveStartKey" in low:
            low["ExclusiveStartKey"] = typed(low["ExclusiveStartKey"])
        page = self.dynamo.query(**low)
        out = {"Items": [plain(i) for i in page.get("Items", [])]}
        if page.get("LastEvaluatedKey"):
            out["LastEvaluatedKey"] = plain(page["LastEvaluatedKey"])
        return out

    def __getattr__(self, attr):
        raise AttributeError("offline table has no " + attr)


class S3:
    def __init__(self, real, writes):
        self.real, self.writes, self.mem, self.n = real, writes, {}, 0

    def _live_exists(self, bucket, key):
        try:
            self.real.head_object(Bucket=bucket, Key=key)
            return True
        except ClientError:
            return False

    def put_object(self, Bucket, Key, Body, **kw):
        if kw.get("IfNoneMatch") == "*" and ((Bucket, Key) in self.mem or self._live_exists(Bucket, Key)):
            raise fail("PreconditionFailed", "PutObject")
        self.n += 1
        version = "offline-%d" % self.n
        self.mem[(Bucket, Key)] = (version, bytes(Body))
        self.writes.add("s3.put", bucket=Bucket, key=Key, bytes=len(Body))
        return {"VersionId": version}

    def head_object(self, Bucket, Key, **kw):
        self.writes.read("s3:HeadObject", bucket=Bucket, key=Key, version=bool(kw.get("VersionId")))
        if (Bucket, Key) in self.mem:
            return {"VersionId": self.mem[(Bucket, Key)][0], "ContentLength": len(self.mem[(Bucket, Key)][1])}
        return self.real.head_object(Bucket=Bucket, Key=Key, **kw)

    def get_object(self, Bucket, Key, **kw):
        self.writes.read("s3:GetObject", bucket=Bucket, key=Key, version=bool(kw.get("VersionId")))
        if (Bucket, Key) in self.mem:
            version, data = self.mem[(Bucket, Key)]
            return {"Body": io.BytesIO(data), "VersionId": version, "ContentLength": len(data)}
        return self.real.get_object(Bucket=Bucket, Key=Key, **kw)

    def __getattr__(self, attr):
        raise AttributeError("offline s3 has no " + attr)


class Sqs:
    """Captures sends; delivers a scripted inbox to receive_message; records deletes and visibility changes."""

    def __init__(self, writes, inbox=None):
        self.writes, self.sent, self.inbox = writes, [], list(inbox or [])

    def send_message(self, QueueUrl, MessageBody, **kw):
        self.sent.append(MessageBody)
        self.writes.add("sqs.send", queue=QueueUrl, bytes=len(MessageBody))
        return {"MessageId": "offline-%d" % len(self.sent)}

    def receive_message(self, **kw):
        if not self.inbox:
            return {}
        body = self.inbox.pop(0)
        return {"Messages": [{"Body": body, "ReceiptHandle": "offline-receipt", "MessageId": "offline-in"}]}

    def delete_message(self, **kw):
        self.writes.add("sqs.delete", receipt=kw.get("ReceiptHandle"))
        return {}

    def change_message_visibility(self, **kw):
        self.writes.add("sqs.visibility", timeout=kw.get("VisibilityTimeout"))
        return {}

    def __getattr__(self, attr):
        raise AttributeError("offline sqs has no " + attr)


def dump(path, dynamo, s3, sqs):
    state = {"dynamo": [[list(k), v] for k, v in dynamo.mem.items()],
             "s3": [[b, k, v, base64.b64encode(d).decode()] for (b, k), (v, d) in s3.mem.items()],
             "sent": sqs.sent}
    json.dump(state, open(path, "w", encoding="utf-8"))


def load(path, dynamo, s3):
    state = json.load(open(path, encoding="utf-8"))
    for k, v in state["dynamo"]:
        dynamo.mem[tuple(k)] = v
    for b, k, v, d in state["s3"]:
        s3.mem[(b, k)] = (v, base64.b64decode(d))
    s3.n = len(state["s3"])
    return state["sent"]
