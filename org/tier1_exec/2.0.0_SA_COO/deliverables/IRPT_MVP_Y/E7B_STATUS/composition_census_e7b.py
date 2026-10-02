"""Read-only census: every accepted analysis request's composition through the pin's own _chosen_comparisons.

Usage: python composition_census_e7b.py <owned_requests.py at the pin>

E7b copy (CTO rulings batches 142, 146): also prints the derivation for the Overview and Multi-Comp requests the
packet names, so the include=comparisons answer is read per request.
Reads irpt-requests (scan) and each composition blob by version. Writes nothing.
"""
import ast
import collections
import json
import sys

import boto3


class RequestReadRefused(ValueError):
    pass


def load_derivation(path):
    """Execute only COMPOSITION_VERSION and _chosen_comparisons from the pinned source."""
    module = ast.parse(open(path, encoding="utf-8").read())
    namespace = {"json": json, "RequestReadRefused": RequestReadRefused}
    for node in module.body:
        keep = (isinstance(node, ast.Assign)
                and any(getattr(t, "id", "") == "COMPOSITION_VERSION" for t in node.targets))
        keep = keep or (isinstance(node, ast.FunctionDef) and node.name == "_chosen_comparisons")
        if keep:
            exec(compile(ast.Module([node], []), "pin", "exec"), namespace)
    return namespace["_chosen_comparisons"]


def main(path):
    chosen = load_derivation(path)
    ddb = boto3.client("dynamodb", region_name="us-east-1")
    s3 = boto3.client("s3", region_name="us-east-1")
    items = []
    for page in ddb.get_paginator("scan").paginate(TableName="irpt-requests"):
        items.extend(page["Items"])
    kinds = collections.Counter(i["request_revision"]["S"].split("#")[0] for i in items)
    print("rows", len(items), dict(kinds))
    artifacts = {i["request_revision"]["S"].split("#", 1)[1]: i
                 for i in items if i["request_revision"]["S"].startswith("ARTIFACT#")}
    requests = [i for i in items if i["request_revision"]["S"].startswith("analysis#")]
    print("rows with composition_ref", len(requests))
    outcomes = collections.Counter()
    labels = collections.Counter()
    fails = []
    for row in requests:
        revision = row["request_revision"]["S"]
        ref = json.loads(row["record"]["S"]).get("composition_ref") or {}
        artifact = artifacts.get(ref.get("artifact_id"))
        if artifact is None:
            outcomes["NO_ARTIFACT_ROW"] += 1
            fails.append((revision, "NO_ARTIFACT_ROW"))
            continue
        blob = artifact["blob"]["M"]
        try:
            data = s3.get_object(Bucket=blob["bucket"]["S"], Key=blob["key"]["S"],
                                 VersionId=blob["version_id"]["S"])["Body"].read()
        except Exception as exc:  # a failed GET is a census row, not a crash
            outcomes["GET_FAILED"] += 1
            fails.append((revision, type(exc).__name__))
            continue
        try:
            result = chosen(data)
        except RequestReadRefused as exc:
            outcomes["REFUSED_" + str(exc)] += 1
            fails.append((revision, str(exc)))
            continue
        outcomes["OK_%d" % len(result)] += 1
        if any(name in revision for name in ("REQ-a69e5751d42c374f1d2354f9", "REQ-a1d9abc0bc037ea3d9e4a7ed")):
            print("named", revision.split("#")[1] if "#" in revision else revision, json.dumps(result))
        for entry in result:
            labels[entry["label"]] += 1
    print("outcomes", dict(outcomes))
    print("labels", dict(labels))
    print("revisions", dict(collections.Counter(r["request_revision"]["S"].rsplit("#", 1)[1] for r in requests)))
    print("tenants", dict(collections.Counter(r["tenant"]["S"] for r in requests)))
    for fail in fails[:20]:
        print("FAIL", fail)


if __name__ == "__main__":
    main(sys.argv[1])
