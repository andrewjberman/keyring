"""Read-only step-E evidence: IAM simulation and resource metadata; no secret values."""
from __future__ import annotations

import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import shutil
import subprocess

import boto3

ROOT = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path.cwd()
ACCOUNT = "313476888478"
REGION = "us-east-1"
GROUP = "cloudops-dell-agents-group"
iam = boto3.client("iam", region_name=REGION)


def save(name, obj):
    (ROOT / name).write_text(json.dumps(obj, default=str, indent=2), encoding="utf-8")


def all_pages(client, operation, field, **kwargs):
    return [row for page in client.get_paginator(operation).paginate(**kwargs) for row in page[field]]


def principal_sim(principal, action, resource):
    # The requested CLI, one action and exactly one resource in each invocation.
    executable = shutil.which("aws.cmd") or shutil.which("aws")
    if not executable:
        raise RuntimeError("AWS CLI is not on PATH")
    command = [executable, "iam", "simulate-principal-policy", "--policy-source-arn", principal,
               "--action-names", action, "--resource-arns", resource, "--output", "json",
               "--region", REGION]
    run = subprocess.run(command, capture_output=True, text=True)
    if run.returncode:
        raise RuntimeError(f"AWS CLI rc={run.returncode}: {run.stderr}")
    return json.loads(run.stdout)["EvaluationResults"][0]


def named_matches(result, documents):
    output = []
    for match in result.get("MatchedStatements", []):
        name = match["SourcePolicyId"]
        document = documents[name]
        text = json.dumps(document, separators=(",", ":"), ensure_ascii=False)
        start, end = match["StartPosition"], match["EndPosition"]
        if start["Line"] != 1 or end["Line"] != 1:
            raise RuntimeError(f"Cannot attribute non-minified policy {name}")
        # AWS positions can include the separating comma on either side.
        low, high = start["Column"] - 1, end["Column"]
        found = []
        for statement in document["Statement"]:
            encoded = json.dumps(statement, separators=(",", ":"), ensure_ascii=False)
            at = text.find(encoded)
            if at >= low and at + len(encoded) <= high:
                found.append(statement["Sid"])
        if len(found) != 1:
            raise RuntimeError(f"Ambiguous statement attribution {name}: {found}, {start}, {end}")
        output.append({"policy": name, "sid": found[0], "aws_match": match})
    return output


def main():
    before = json.loads((ROOT / "before-iam.json").read_text(encoding="utf-8"))
    attached = all_pages(iam, "list_attached_group_policies", "AttachedPolicies", GroupName=GROUP)
    docs, policies, users = {}, {}, {}
    for n in (1, 2):
        name = f"cloudops-dell{n}-agent-user"
        user = iam.get_user(UserName=name)["User"]
        own = all_pages(iam, "list_attached_user_policies", "AttachedPolicies", UserName=name)
        inline = all_pages(iam, "list_user_policies", "PolicyNames", UserName=name)
        groups = all_pages(iam, "list_groups_for_user", "Groups", UserName=name)
        users[name] = {"arn": user["Arn"], "attached": own, "inline": inline, "groups": groups}
        if inline or [g["GroupName"] for g in groups] != [GROUP]:
            raise RuntimeError("Unexpected principal-policy surface; inspect before concluding")
        for policy in attached + own:
            arn = policy["PolicyArn"]
            if arn in policies:
                continue
            metadata = iam.get_policy(PolicyArn=arn)["Policy"]
            version = iam.get_policy_version(PolicyArn=arn, VersionId=metadata["DefaultVersionId"])["PolicyVersion"]
            policies[arn] = {"metadata": metadata, "version": version}
            docs[policy["PolicyName"]] = version["Document"]
    if all_pages(iam, "list_group_policies", "PolicyNames", GroupName=GROUP):
        raise RuntimeError("Unexpected inline group policy")

    census = json.loads((REPO / "infra/aws/terraform/nfra-ctlpln-identity/tests/vendor_secrets_census.json").read_text())
    other = next(n for n, d in census["decisions"].items() if d["decision"] == "OTHER")
    sm = boto3.client("secretsmanager", region_name=REGION)
    secrets = {n: sm.describe_secret(SecretId=n)["ARN"] for n in
               ("opal/mcp/graph-read-token", "schwab/sdd/session", other)}
    sqs = boto3.client("sqs", region_name=REGION)
    queues = {}
    for n in (1, 2):
        name = f"agentbus-global-dell{n}-queue.fifo"
        url = sqs.get_queue_url(QueueName=name)["QueueUrl"]
        queues[n] = sqs.get_queue_attributes(QueueUrl=url, AttributeNames=["QueueArn"])["Attributes"]["QueueArn"]
    bucket = "opal-cloudtrail-logs-313476888478"
    boto3.client("s3", region_name=REGION).head_bucket(Bucket=bucket)
    protected = next(s["Resource"] for s in docs["cloudops-dell-agent-deploy-policy"]["Statement"]
                     if s["Sid"] == "DenyProtectedFunctions")
    functions = all_pages(boto3.client("lambda", region_name=REGION), "list_functions", "Functions")
    function = next(f for f in functions if f["FunctionArn"] in protected)
    trails = boto3.client("cloudtrail", region_name=REGION).describe_trails(includeShadowTrails=False)["trailList"]
    trail = next(t for t in trails if t.get("S3BucketName") == bucket)
    role = iam.get_role(RoleName=function["Role"].split("/")[-1])["Role"]["Arn"]
    existence = {"secrets": secrets, "queues": queues, "audit_bucket": bucket,
                 "protected_function": function["FunctionArn"], "audit_trail": trail["TrailARN"],
                 "existing_role_for_create_action_simulation": role,
                 "cloudtrail_put_resource_policy_scope": "* (action grant only, no resource-policy call)"}
    save("resource-existence.json", existence)
    save("after-iam.json", {"captured_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                            "attached_policies": attached, "policies": policies, "users": users})

    policy_matches = []
    plan = json.loads((ROOT / "plan-before.json").read_text(encoding="utf-8"))
    for change in plan["resource_changes"]:
        if change["type"] != "aws_iam_policy":
            continue
        target = change["change"]["after"]
        if not target:
            continue
        wanted = json.loads(target["policy"])
        actual = docs[target["name"]]
        policy_matches.append({"address": change["address"], "name": target["name"], "equal": wanted == actual,
                               "document_sha256": hashlib.sha256(json.dumps(actual, sort_keys=True).encode()).hexdigest()})
    saved_versions = {}
    for name in ("cloudops-dell-agent-deploy-policy", "cloudops-dell-agent-create-policy", "cloudops-dell-agent-respol-allow-policy"):
        p = before["policies"][name]
        v = iam.get_policy_version(PolicyArn=p["metadata"]["Arn"], VersionId=p["metadata"]["DefaultVersionId"])["PolicyVersion"]
        saved_versions[name] = {"version": v["VersionId"], "retained_document_equal": v["Document"] == p["version"]["Document"]}

    fixed = [
        ("graph_read", "secretsmanager:GetSecretValue", secrets["opal/mcp/graph-read-token"], "allowed"),
        ("cloudtrail_resource_policy", "cloudtrail:PutResourcePolicy", "*", "allowed"),
        ("audit_bucket_policy", "s3:PutBucketPolicy", f"arn:aws:s3:::{bucket}", "allowed"),
        ("protected_function_permission", "lambda:AddPermission", function["FunctionArn"], "allowed"),
        ("queue_attributes", "sqs:SetQueueAttributes", queues[1], "allowed"),
        ("audit_stop", "cloudtrail:StopLogging", trail["TrailARN"], "explicitDeny"),
        ("audit_lifecycle", "s3:PutLifecycleConfiguration", f"arn:aws:s3:::{bucket}", "explicitDeny"),
        ("protected_function_code", "lambda:UpdateFunctionCode", function["FunctionArn"], "explicitDeny"),
        ("withheld_session", "secretsmanager:GetSecretValue", secrets["schwab/sdd/session"], "implicitDeny"),
        ("other_secret", "secretsmanager:GetSecretValue", secrets[other], "implicitDeny"),
        ("iam_create", "iam:CreateRole", role, "explicitDeny"),
    ]
    tasks = []
    for n in (1, 2):
        name = f"cloudops-dell{n}-agent-user"
        arms = fixed + [("bus_receive", "sqs:ReceiveMessage", queues[n], "allowed"),
                        ("bus_send", "sqs:SendMessage", queues[3 - n], "allowed")]
        tasks += [(name, label, action, resource, expected) for label, action, resource, expected in arms]

    def run_arm(task):
        user, label, action, resource, expected = task
        result = principal_sim(users[user]["arn"], action, resource)
        save(f"simulation-{user}-{label}.json", result)
        matched = named_matches(result, docs)
        return {"user": user, "arm": label, "action": action, "resource": resource,
                "expected": expected, "decision": result["EvalDecision"], "matched_statements": matched,
                "raw": result, "ok": result["EvalDecision"] == expected and not result.get("MissingContextValues")}

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        arms = list(pool.map(run_arm, tasks))
    admin = "arn:aws:iam::313476888478:user/Andrew_Berman"
    controls = []
    for label, action, resource, expected in fixed:
        if expected == "allowed":
            continue
        result = principal_sim(admin, action, resource)
        controls.append({"arm": label, "principal": admin, "raw": result,
                         "ok": result["EvalDecision"] == "allowed" and not result.get("MissingContextValues")})
    ok = (len(attached) == 7 and all(x["equal"] for x in policy_matches) and all(x["ok"] for x in arms)
          and all(x["ok"] for x in controls) and all(x["retained_document_equal"] for x in saved_versions.values()))
    output = {"taken_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "arms": arms,
              "admin_controls": controls, "attached_policies": attached, "policy_matches": policy_matches,
              "rollback_versions": saved_versions, "all_ok": ok,
              "limits": "Identity-policy simulation only; no secret values or resource policies read, no permission exercise; Dell graph queries remain pending."}
    save("readback.json", output)
    lines = [f'{x["user"]} {x["arm"]}: {x["decision"]}; matched=' +
             (", ".join(m["policy"] + "/" + m["sid"] for m in x["matched_statements"])
              or "NONE (implicitDeny: no identity Allow)") for x in arms]
    lines.append(f'READBACK arms={sum(x["ok"] for x in arms)}/{len(arms)} admin_controls={sum(x["ok"] for x in controls)}/{len(controls)} '
                 f'policy_documents={sum(x["equal"] for x in policy_matches)}/{len(policy_matches)} group_attachments={len(attached)} all_ok={ok}')
    (ROOT / "readback.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
