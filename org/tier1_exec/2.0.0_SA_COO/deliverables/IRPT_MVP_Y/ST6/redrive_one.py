#!/usr/bin/env python3
"""Ledger irpt-resident-head-st6-20261001 leg R1: move ONE named job's message from the dead-letter queue back to
irpt-generation, then read what the resident did with it.

    python redrive_one.py <tenant> <request-id> <expected-code>

Before the move it prints the branch the job will take: the recorded actor, and whether that actor's profile row
exists (the packet's condition: a job whose actor still exists is NOT redriven, because it would resume against the
vendor). The message is re-sent with its own body and then deleted from the dead-letter queue. Afterwards it reads
the jobs row and both queue depths. No vendor call is made by this tool. ASCII only.
"""
import json
import sys
import time

import boto3
from boto3.dynamodb.types import TypeDeserializer

de = TypeDeserializer()
tenant, request_id, expected = sys.argv[1:4]
ddb = boto3.client("dynamodb", region_name="us-east-1")
sqs = boto3.client("sqs", region_name="us-east-1")
main = sqs.get_queue_url(QueueName="irpt-generation")["QueueUrl"]
dlq = sqs.get_queue_url(QueueName="irpt-generation-dlq")["QueueUrl"]


def depth(url):
    a = sqs.get_queue_attributes(QueueUrl=url, AttributeNames=["ApproximateNumberOfMessages",
                                                                "ApproximateNumberOfMessagesNotVisible"])["Attributes"]
    return "%s/%s" % (a["ApproximateNumberOfMessages"], a["ApproximateNumberOfMessagesNotVisible"])


def job():
    row = ddb.get_item(TableName="irpt-jobs", Key={"tenant": {"S": tenant}, "job": {"S": request_id}},
                       ConsistentRead=True).get("Item") or {}
    d = {k: de.deserialize(v) for k, v in row.items()}
    return {"state": d.get("state"), "detail": d.get("job_detail"), "lease": "lease_owner" in d,
            "fence": str(d.get("fence_token"))}


req = ddb.get_item(TableName="irpt-requests", Key={"tenant": {"S": tenant},
                   "request_revision": {"S": "analysis#%s#1" % request_id}}, ConsistentRead=True)["Item"]
record = json.loads(de.deserialize(req["record"]))
pid = record["owner"]["principal_id"]
profile = ddb.get_item(TableName="opal-users-v2", Key={"PK": {"S": "USER#" + pid}, "SK": {"S": "PROFILE"}},
                       ProjectionExpression="PK", ConsistentRead=True).get("Item")
index = ddb.query(TableName="opal-users-v2", IndexName="email-index", KeyConditionExpression="email = :e",
                  ExpressionAttributeValues={":e": {"S": pid}}, Select="COUNT")["Count"]
print("BRANCH for %s: actor profile row %s, email-index count %d -> expected %s"
      % (request_id, "PRESENT" if profile else "ABSENT", index, expected))
print("before: job %s | irpt-generation %s | dlq %s" % (json.dumps(job()), depth(main), depth(dlq)))
if profile or index:
    print("STOP: the actor's row exists; this job would resume against the vendor. Nothing moved.")
    sys.exit(3)
target = None
for _ in range(6):
    for m in sqs.receive_message(QueueUrl=dlq, MaxNumberOfMessages=10, VisibilityTimeout=20,
                                 WaitTimeSeconds=2).get("Messages", []):
        body = json.loads(m["Body"])
        if body.get("request_id") == request_id and body.get("tenant") == tenant and target is None:
            target = m
    if target:
        break
if target is None:
    print("STOP: the message for %s was not received from the dead-letter queue. Nothing moved." % request_id)
    sys.exit(4)
sent = sqs.send_message(QueueUrl=main, MessageBody=target["Body"])
sqs.delete_message(QueueUrl=dlq, ReceiptHandle=target["ReceiptHandle"])
print("moved at %s: sent to irpt-generation as %s; deleted from the dead-letter queue"
      % (time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), sent["MessageId"][:8]))
state = None
for _ in range(30):
    time.sleep(3)
    state = job()
    if state["state"] in ("ATTENTION", "READY"):
        break
print("after: job %s | irpt-generation %s | dlq %s (a message returning from the 20 s receive may still be in flight)"
      % (json.dumps(state), depth(main), depth(dlq)))
detail = json.loads(state["detail"]) if state.get("detail") else {}
ok = state["state"] == "ATTENTION" and detail == {"code": expected} and not state["lease"]
print("R1 %s: %s" % (request_id, "ENDED BY NAME as expected" if ok else "NOT AS EXPECTED"))
sys.exit(0 if ok else 1)
