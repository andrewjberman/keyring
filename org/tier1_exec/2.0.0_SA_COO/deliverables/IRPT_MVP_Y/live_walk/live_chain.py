"""K4 then K5 on ONE login (window 7, CRO order): log in, wait for P to delete the password, upload, wait for
NORMALIZED, submit the Overview. Exactly one POST of each; no re-POST and no retry.

Env: WALK_PW (read by name by run_upload.py, never printed), WALK_PW_NAME (polled until ParameterNotFound),
WALK_EMAIL, WALK_DEADLINE, WALK_AUTHORITY; the arms: WALK_UPLOAD_FILE, WALK_FILE_TYPE, WALK_REFERENCE_NOTIONAL (K4) and
WALK_COMPARISON_KEYS (K5).
Usage: python run_upload.py <out.json> live_chain.py      (or: python live_chain.py <out.json> --dry)

Prints LOGGED_IN once the token is held, so the operator can tell P; K4 starts only after the password parameter reads
ParameterNotFound. The outcome of each POST is read from DynamoDB, never by a second POST.
"""
import base64
import hashlib
import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import live_upload as lu  # noqa: E402  (the scrubbed call/log helpers)
import live_submit as ls  # noqa: E402  (the K5 body and its schema check)

AWS = r"C:\Users\AndrewBerman\Desktop\ajb_workspace\.tools\aws.cmd"


def say(*parts):
    print(lu.now().strftime("%H:%M:%SZ"), *parts, flush=True)


def aws_json(*args):
    out = subprocess.run([AWS, *args, "--output", "json"], capture_output=True, text=True)
    return out.returncode, (json.loads(out.stdout) if out.returncode == 0 and out.stdout.strip() else None), out.stderr


def password_gone(name):
    """True only on a successful read that lists no such parameter; a failed read is never 'gone'."""
    rc, page, _ = aws_json("ssm", "describe-parameters", "--parameter-filters",
                           json.dumps([{"Key": "Name", "Values": [name]}]))
    return rc == 0 and page is not None and not page.get("Parameters")


def normalization(upload_id):
    rc, page, err = aws_json("dynamodb", "query", "--table-name", "irpt-requests", "--consistent-read",
                             "--key-condition-expression", "tenant = :t AND begins_with(request_revision, :p)",
                             "--expression-attribute-values",
                             json.dumps({":t": {"S": lu.TENANT}, ":p": {"S": "NORMALIZATION#" + upload_id}}))
    rows = (page or {}).get("Items", [])
    if not rows:
        return None, None
    row = rows[-1]
    return row.get("state", {}).get("S"), row.get("input_id", {}).get("S")


def input_for(upload_id):
    rc, page, err = aws_json("dynamodb", "query", "--table-name", "irpt-requests", "--consistent-read",
                             "--key-condition-expression", "tenant = :t AND begins_with(request_revision, :p)",
                             "--filter-expression", "upload_id = :u",
                             "--expression-attribute-values",
                             json.dumps({":t": {"S": lu.TENANT}, ":p": {"S": "INPUT#"}, ":u": {"S": upload_id}}))
    rows = (page or {}).get("Items", [])
    return rows[0]["request_revision"]["S"].split("#", 1)[1] if rows else None


def k5_body(input_id):
    """The ONE K5 body. The first Comparison window sets WALK_COMPARISON_KEYS (comma-separated catalogue keys: one is
    Comparison, two or more Multi-Comp, as offline_submit_proof.py --comparison-keys); unset, it is window 15's
    Overview exactly."""
    import jsonschema
    keys = [k for k in os.environ.get("WALK_COMPARISON_KEYS", "").split(",") if k]
    variant = "overview" if not keys else "comparison" if len(keys) == 1 else "multicomp"
    body = dict(ls.BODY, input_id=input_id, variant=variant, comparison_keys=keys,
                request_id="y-live-1203-%s-%s" % (variant, lu.now().strftime("%Y%m%d")))
    jsonschema.Draft202012Validator(json.load(open(ls.SCHEMA, encoding="utf-8"))).validate(body)
    return body


def k4_body():
    """The ONE K4 body. The Y2 arms (P_Y2_UPLOAD_ARMS_ACT_20260927.md) set WALK_UPLOAD_FILE, WALK_FILE_TYPE and
    WALK_REFERENCE_NOTIONAL; unset, it is window 15's Dollars CSV exactly."""
    upload = os.environ.get("WALK_UPLOAD_FILE", lu.CSV)
    file_type = os.environ.get("WALK_FILE_TYPE", "csv")
    if file_type not in ("csv", "xlsx") or not upload.endswith("." + file_type):
        raise ValueError("WALK_FILE_TYPE must be csv or xlsx and match the file's extension")
    data = open(upload, "rb").read()
    body = {"upload_token": "y-live-1203-" + lu.now().strftime("%Y%m%dT%H%M%S"),
            "filename": os.path.basename(upload), "file_base64": base64.b64encode(data).decode(),
            "file_type": file_type, "declared_currency": "USD"}
    if os.environ.get("WALK_REFERENCE_NOTIONAL"):
        body["reference_notional"] = os.environ["WALK_REFERENCE_NOTIONAL"]
    return body, data


def main():
    out = sys.argv[1]
    if "--dry" in sys.argv:
        body, data = k4_body()
        print("OK: K4 body", json.dumps(dict(body, file_base64="<%d bytes base64>" % len(data))),
              "sha256", hashlib.sha256(data).hexdigest()[:16])
        print("OK: K5 body validates;", json.dumps(k5_body("portfolio_" + "0" * 64)), "| no network call")
        return 0
    deadline = lu.DEADLINE
    name = "/" + os.environ["WALK_PW_NAME"].lstrip("/")
    pw = os.environ.pop("WALK_PW")
    s, login = lu.call("POST", "/auth/login", {"email": lu.EMAIL, "password": pw}, {"Content-Type": "application/json"},
                       scrub_body={"email": lu.EMAIL, "password": "<redacted>"})
    del pw
    token = login.get("accessToken") if isinstance(login, dict) else None
    result = {"principal": lu.EMAIL, "tenant": lu.TENANT, "authority": os.environ.get("WALK_AUTHORITY", "<unset>")}

    def dump():
        json.dump(dict(result, calls=lu.log), open(out, "w", encoding="utf-8", newline="\n"), indent=1)

    if not token:
        say("login status", s, "| no token; nothing posted")
        dump()
        return 1
    say("LOGGED_IN", "login status", s)
    while not password_gone(name):
        if lu.now() >= deadline:
            say("ERROR: the password parameter is still present at the deadline; no POST made")
            dump()
            return 1
        time.sleep(10)
    say("PASSWORD_DELETED", name, "reads absent")
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token, "X-Contract-Version": "v1"}
    try:
        body, data = k4_body()
    except ValueError as exc:
        say("ERROR:", exc, "; no POST made")
        return 1
    result.update(upload_file=body["filename"], upload_sha256=hashlib.sha256(data).hexdigest(),
                  reference_notional=body.get("reference_notional"))
    if lu.now() >= deadline:
        say("ERROR: past the deadline; no POST made")
        dump()
        return 1
    # K4: EXACTLY ONE POST.
    s, resp = lu.call("POST", "/api/scoped/investor-reporting/analysis/inputs?selected_tenant=" + lu.TENANT, body,
                      headers, scrub_body=dict(body, file_base64="<%d bytes base64>" % len(data)))
    d = resp.get("data") if isinstance(resp, dict) else None
    upload_id = d.get("upload_id") if isinstance(d, dict) else None
    result.update(k4_status=s, upload_id=upload_id)
    say("K4 POST", s, "state", d.get("state") if isinstance(d, dict) else None, "| upload_id", upload_id)
    dump()
    if not upload_id:
        return 1
    state = input_id = None
    while lu.now() < deadline:
        state, input_id = normalization(upload_id)
        if state in ("NORMALIZED", "NEEDS_CORRECTION", "FAILED", "REFUSED"):
            break
        time.sleep(5)
    input_id = input_id or input_for(upload_id)
    result.update(k4_state=state, input_id=input_id)
    say("K4 resolved", state, "| input_id", input_id)
    dump()
    if state != "NORMALIZED" or not input_id:
        say("K4 did not normalize; K5 not made (the packet's branch)")
        return 1
    k5 = k5_body(input_id)
    # K5: EXACTLY ONE POST.
    s, resp = lu.call("POST", "/api/scoped/investor-reporting/analysis?selected_tenant=" + lu.TENANT, k5, headers)
    d = resp.get("data") if isinstance(resp, dict) else None
    status = resp.get("status") if isinstance(resp, dict) else None
    result.update(k5_variant=k5["variant"], k5_comparison_keys=k5["comparison_keys"], k5_status=s,
                  k5_state=(status or {}).get("state"),
                  request_ref=json.dumps(d.get("identity") if isinstance(d, dict) else None)[:300])
    say("K5 POST", s, "| state", (status or {}).get("state"), "| identity", result["request_ref"])
    dump()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
