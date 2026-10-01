#!/usr/bin/env python3
"""One empty-headers invoke of a function, printing its identity and the answer's shape (a served-move condition).

    python lambda_empty_invoke.py <function> <label>

The event carries no headers, so the boundary refuses CONTRACT_VERSION before anything is resolved: a cold import of
the bundle through the real entry point, with no firm, no client and no write. Prints CodeSha256, LastModified,
LastUpdateStatus, the status code, whether the answer carries `errorMessage`, and the refusal's code. ASCII only.
"""
import json
import sys

import boto3

fn, label = sys.argv[1], sys.argv[2]
lam = boto3.client("lambda", region_name="us-east-1")
cfg = lam.get_function_configuration(FunctionName=fn)
out = lam.invoke(FunctionName=fn, Payload=json.dumps({"headers": {}}).encode())
body = json.loads(out["Payload"].read() or b"null")
status = (body.get("status") or {}) if isinstance(body, dict) else {}
print("%s %s | CodeSha256 %s | LastModified %s | LastUpdateStatus %s | invoke StatusCode %s FunctionError %s | "
      "errorMessage %s | reason %s | keys %s"
      % (label, fn, cfg["CodeSha256"], cfg["LastModified"][:19], cfg.get("LastUpdateStatus"), out.get("StatusCode"),
         out.get("FunctionError"), "errorMessage" in body if isinstance(body, dict) else None,
         status.get("public_reason_code"), sorted(body) if isinstance(body, dict) else type(body).__name__))
ok = out.get("FunctionError") is None and isinstance(body, dict) and "errorMessage" not in body \
    and status.get("public_reason_code") == "CONTRACT_VERSION"
sys.exit(0 if ok else 1)
