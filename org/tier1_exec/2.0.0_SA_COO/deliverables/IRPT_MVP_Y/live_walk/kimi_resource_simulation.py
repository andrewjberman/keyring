#!/usr/bin/env python3
"""Y-4 enrichment (CTO rulings batch 199): what the runner role may read of the Kimi secrets, by IAM simulation.

    python kimi_resource_simulation.py <label>

Simulates secretsmanager:GetSecretValue for irpt-ycharts-runner-role on (a) the estate Kimi secret's real ARN, read
from describe-secret metadata (no value is read), and (b) a sibling name `astn/kimi/api-key-extra-` plus a 6-character
suffix that `astn/kimi/api-key-*` admits and `astn/kimi/api-key-??????` refuses. Prints the decision and the
MatchedStatements' policy ids (CTO batch 208). No secret value is read. ASCII only.
"""
import datetime
import sys

import boto3

label = sys.argv[1]
real = boto3.client("secretsmanager", region_name="us-east-1").describe_secret(SecretId="astn/kimi/api-key")["ARN"]
sibling = real.rsplit("astn/kimi/api-key-", 1)[0] + "astn/kimi/api-key-extra-AbCdEf"
iam = boto3.client("iam")
role = iam.get_role(RoleName="irpt-ycharts-runner-role")["Role"]["Arn"]
print("%s at %s" % (label, datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")))
for name, arn in (("the estate Kimi secret", real), ("a sibling name", sibling)):
    r = iam.simulate_principal_policy(PolicySourceArn=role, ActionNames=["secretsmanager:GetSecretValue"],
                                      ResourceArns=[arn])["EvaluationResults"][0]
    matched = sorted({m.get("SourcePolicyId") for m in r.get("MatchedStatements", [])})
    print("%-24s suffix-len %d -> %s | matched %s" % (name, len(arn.rsplit("api-key-", 1)[1]), r["EvalDecision"],
                                                       ", ".join(matched) or "none"))
