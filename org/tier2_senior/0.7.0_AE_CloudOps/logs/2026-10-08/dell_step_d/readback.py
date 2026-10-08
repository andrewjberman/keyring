"""Step D metadata and identity simulation only; no code writes or SSM changes."""
from __future__ import annotations

import concurrent.futures
import datetime
import importlib.util
import json
from pathlib import Path

import boto3

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("step_e_readback", ROOT.parent / "dell_step_e/readback.py")
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
iam = boto3.client("iam", region_name="us-east-1")


def save(name, value):
    (ROOT / name).write_bytes((json.dumps(value, default=str, indent=2) + "\n").encode())


def main():
    before = json.loads((ROOT / "before-iam.json").read_text())
    attached = helper.all_pages(iam, "list_attached_group_policies", "AttachedPolicies", GroupName=helper.GROUP)
    policies, docs, users = {}, {}, {}
    for n in (1, 2):
        user = f"cloudops-dell{n}-agent-user"
        own = helper.all_pages(iam, "list_attached_user_policies", "AttachedPolicies", UserName=user)
        assert not helper.all_pages(iam, "list_user_policies", "PolicyNames", UserName=user)
        assert [g["GroupName"] for g in helper.all_pages(iam, "list_groups_for_user", "Groups", UserName=user)] == [helper.GROUP]
        users[user] = {"arn": iam.get_user(UserName=user)["User"]["Arn"], "attached": own}
        for p in attached + own:
            if p["PolicyName"] in policies:
                continue
            meta = iam.get_policy(PolicyArn=p["PolicyArn"])["Policy"]
            version = iam.get_policy_version(PolicyArn=p["PolicyArn"], VersionId=meta["DefaultVersionId"])["PolicyVersion"]
            policies[p["PolicyName"]] = {"metadata": meta, "version": version}
            docs[p["PolicyName"]] = version["Document"]
    assert not helper.all_pages(iam, "list_group_policies", "PolicyNames", GroupName=helper.GROUP)
    try:
        iam.get_policy(PolicyArn=before["policies"]["cloudops-dell-agent-routes-host-policy"]["metadata"]["Arn"])
        absent = False
    except iam.exceptions.NoSuchEntityException:
        absent = True
    retained = {n: p["version"]["Document"] == docs.get(n) for n, p in before["policies"].items()
                if n != "cloudops-dell-agent-routes-host-policy"}
    saved = before["policies"]["cloudops-dell-agent-routes-host-policy"]["version"]["Document"]
    document_arn = next(s["Resource"][0] for s in saved["Statement"] if s["Sid"] == "DenyRoutesToPrivilegedRolesDocuments")
    document = boto3.client("ssm", region_name="us-east-1").describe_document(Name=document_arn.split("document/", 1)[1])["Document"]
    protected = [r for s in docs["cloudops-dell-agent-routes-fn-policy"]["Statement"] for r in s["Resource"]]
    functions = helper.all_pages(boto3.client("lambda", region_name="us-east-1"), "list_functions", "Functions")
    function = next(f for f in functions if f["FunctionArn"] in protected)
    role = iam.get_role(RoleName=function["Role"].split("/")[-1])["Role"]["Arn"]
    boto3.client("s3", region_name="us-east-1").head_bucket(Bucket="opal-data-cot")
    existence = {"document_arn": document_arn, "document_name": document["Name"], "document_status": document["Status"],
                 "function_arn": function["FunctionArn"], "existing_role_arn": role, "bucket": "opal-data-cot",
                 "prospective_object": "code/gold/x.py (simulation only; no object written)"}
    save("resource-existence.json", existence)
    save("after-iam.json", {"attached_policies": attached, "policies": policies, "users": users, "routes_host_absent": absent})
    cases = [("code_write", "s3:PutObject", "arn:aws:s3:::opal-data-cot/code/gold/x.py", "allowed"),
             ("document_update", "ssm:UpdateDocument", document_arn, "allowed"),
             ("document_send", "ssm:SendCommand", document_arn, "implicitDeny"),
             ("function_code", "lambda:UpdateFunctionCode", function["FunctionArn"], "explicitDeny"),
             ("iam_create", "iam:CreateRole", role, "explicitDeny")]

    def run(case):
        user, label, action, resource, expected = case
        raw = helper.principal_sim(users[user]["arn"], action, resource)
        matches = helper.named_matches(raw, docs)
        ok = raw["EvalDecision"] == expected and not raw.get("MissingContextValues")
        if label == "function_code":
            ok = ok and any(m["policy"] == "cloudops-dell-agent-routes-fn-policy" for m in matches)
        return {"user": user, "arm": label, "action": action, "resource": resource, "expected": expected,
                "decision": raw["EvalDecision"], "matched_statements": matches, "raw": raw, "ok": bool(ok)}

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        arms = list(pool.map(run, [(u, *c) for u in users for c in cases]))
    controls = []
    for label, action, resource, expected in cases:
        if expected == "allowed":
            continue
        raw = helper.principal_sim("arn:aws:iam::313476888478:user/Andrew_Berman", action, resource)
        controls.append({"arm": label, "raw": raw, "ok": raw["EvalDecision"] == "allowed" and not raw.get("MissingContextValues")})
    ok = absent and len(attached) == 6 and all(retained.values()) and all(x["ok"] for x in arms + controls)
    result = {"captured_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "arms": arms,
              "admin_controls": controls, "attached_policies": attached, "routes_host_absent": absent,
              "retained_group_policy_documents": retained, "all_ok": bool(ok),
              "limits": "Identity simulations only; no S3 code write, no SSM document change, no SendCommand. Bucket policies/SCPs and Dell first use unexercised."}
    save("readback.json", result)
    lines = [f'{a["user"]} {a["arm"]}: {a["decision"]}; matched=' +
             (", ".join(m["policy"] + "/" + m["sid"] for m in a["matched_statements"]) or "NONE: no identity Allow") for a in arms]
    lines.append(f'READBACK arms={sum(a["ok"] for a in arms)}/10 admin_controls={sum(c["ok"] for c in controls)}/3 '
                 f'retained_policies={sum(retained.values())}/6 attachments={len(attached)} routes_host_absent={absent} all_ok={bool(ok)}')
    (ROOT / "readback.txt").write_bytes(("\n".join(lines) + "\n").encode())
    print("\n".join(lines))
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
