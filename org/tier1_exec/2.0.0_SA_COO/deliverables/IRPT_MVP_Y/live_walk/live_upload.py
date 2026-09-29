"""ONE live Analysis upload of the 12.03 template as the bounded Opal-class walk principal (CTO 101110, P 101113).

The password arrives in env WALK_PW (read by name from SSM by the caller, never printed). Every request and
response is logged, credential-scrubbed, as the HAR-equivalent. Polling re-POSTs the IDENTICAL body (the same
upload_token), which is the same single upload, not a second one.
"""
import base64
import datetime
import json
import os
import sys
import urllib.error
import urllib.request

API = "https://d2n2nzpeqf34ge.cloudfront.net"  # production's same-origin path: CloudFront routes /auth/* and /api/scoped/*
EMAIL = os.environ["WALK_EMAIL"]  # the new window's principal, from P's create receipt
_REGISTRY = os.path.join(os.path.dirname(os.path.abspath(__file__)), *[".."] * 6, "infra", "logic", "registry",
                         "reporting_policies.json")
_FIRMS = {f for p in json.load(open(_REGISTRY, encoding="utf-8"))["policies"] for f in p.get("firms", [])}
TENANT = os.environ["WALK_TENANT"]  # the firm this body runs as (window 21: one principal, several firms); no firm typed here
if TENANT not in _FIRMS:
    raise SystemExit("ERROR: WALK_TENANT is not a registry reporting firm (reporting_policies.json); nothing posted")
CSV = r"C:\Users\AndrewBerman\Desktop\ajb_workspace\org\tier1_exec\2.0.0_SA_COO\deliverables\IRPT_MVP_Y\aapl-vnq-12.03.csv"
OUT = sys.argv[1]
DEADLINE = datetime.datetime.fromisoformat(os.environ["WALK_DEADLINE"])  # e.g. 2026-09-26T14:40:00+00:00, before P's delete
log = []


def now():
    return datetime.datetime.now(datetime.timezone.utc)


def scrub_headers(h):
    out = {}
    for k, v in h.items():
        out[k] = "<redacted>" if k.lower() in ("authorization", "cookie", "set-cookie") else v
    return out


def call(method, path, body, headers, scrub_body=None):
    url = API + path
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    started = now()
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            status, rh, raw = r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        status, rh, raw = e.code, dict(e.headers), e.read()
    try:
        parsed = json.loads(raw.decode("utf-8"))
    except Exception:
        parsed = raw.decode("utf-8", "replace")[:2000]
    logged = parsed
    if isinstance(parsed, dict) and ("accessToken" in parsed or "refreshToken" in parsed):
        logged = {k: ("<redacted>" if "token" in k.lower() else v) for k, v in parsed.items()}
    log.append({"at": started.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), "method": method, "url": url,
                "request_headers": scrub_headers(headers),
                "request_body": scrub_body if scrub_body is not None else body,
                "status": status,
                "response_headers": scrub_headers({k: v for k, v in rh.items()
                    if k.lower() in ("content-type", "x-amzn-requestid", "apigw-requestid", "set-cookie")}),
                "response_body": logged})
    return status, parsed


def main():
    pw = os.environ.get("WALK_PW")
    if not pw:
        print("ERROR: password not supplied")
        return 2
    s, login = call("POST", "/auth/login", {"email": EMAIL, "password": pw},
                    {"Content-Type": "application/json"},
                    scrub_body={"email": EMAIL, "password": "<redacted>"})
    del pw
    token = login.get("accessToken") if isinstance(login, dict) else None
    print("login status", s, "| token present:", bool(token), "| mfaRequired:",
          isinstance(login, dict) and login.get("mfaRequired"))
    if not token:
        print("login response (scrubbed):", json.dumps(log[-1]["response_body"])[:400])
        json.dump({"principal": EMAIL, "calls": log}, open(OUT, "w", encoding="utf-8", newline="\n"), indent=1)
        return 1
    data = open(CSV, "rb").read()
    body = {"upload_token": "y-live-1203-" + now().strftime("%Y%m%dT%H%M%S"),
            "filename": "aapl-vnq-12.03.csv", "file_base64": base64.b64encode(data).decode(),
            "file_type": "csv", "declared_currency": "USD"}
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token,
               "X-Contract-Version": "v1"}
    path = "/api/scoped/investor-reporting/analysis/inputs?selected_tenant=" + TENANT
    if now() >= DEADLINE:
        print("ERROR: past the window deadline; no POST made")
        return 1
    # EXACTLY ONE POST (packet K4 audit class). The outcome is read afterwards from DynamoDB/S3, never by re-POST.
    s, resp = call("POST", path, body, headers)
    d = resp.get("data") if isinstance(resp, dict) else None
    state = d.get("state") if isinstance(d, dict) else None
    print(now().strftime("%H:%M:%SZ"), "POST", s, "state", state,
          "| ok", resp.get("ok") if isinstance(resp, dict) else None,
          "| upload_id", d.get("upload_id") if isinstance(d, dict) else None,
          "| reason", (resp.get("status") or {}).get("public_reason_code") if isinstance(resp, dict) and isinstance(resp.get("status"), dict) else None)
    json.dump({"principal": EMAIL, "tenant": TENANT, "upload_token": body["upload_token"],
               "authority": os.environ.get("WALK_AUTHORITY", "<unset>"), "calls": log},
              open(OUT, "w", encoding="utf-8", newline="\n"), indent=1)
    print("final state", state, "| calls logged", len(log))
    if isinstance(d, dict) and state == "NORMALIZED":
        print("input_id", d.get("input_id"), "| total", ((d.get("portfolio") or {}).get("holdings") or {}).get("total_dollars"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
