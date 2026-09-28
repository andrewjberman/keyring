"""Cold-start smoke of a BUILT flat Lambda zip (CTO 102204 item 3): import the handler and run its cold-start build.

    python zip_cold_start_smoke.py <zip> --function <lambda name> --route "<METHOD> <path>" [--owner-refusal "<METHOD> <path>"]

The failure it catches (irpt-status HyEyoJ67, 2026-09-27): a zip whose files came from different source vintages. For
example, HEAD entry.py calling served.render_ports_from_env() beside an older served.py, which fails only when the
handler first builds. Every unit suite passes on the source tree; only the BUILT zip shows it.

What runs:
- the zip is extracted fresh and made the ONLY first-party path, as Lambda's /var/task is;
- the function's Handler and Environment NAMES/VALUES are read from its live configuration (read-only; no secret value
  is read: a secret-id variable is a name);
- the handler is called ONCE with an unauthenticated API-Gateway event on --route, a route THIS function serves (the
  gateway never sends it another), so it builds its boundary and answers a refusal.

No AWS call can leave the process: AWS_ENDPOINT_URL points at a closed local port. Any call the cold start attempts
fails fast and is REPORTED, never made. PASS = the handler returned a response; FAIL = the import or the cold-start
build raised, with the exception class and its first line.

--owner-refusal adds the second arm (CTO 102269): an Opal viewer's verified-edge owner read with NO selected_tenant, so
the firm refused is the viewer's own and the refusal is raised INSIDE the owner read, where it is recorded (window 20's
exact shape). It must answer a NAMED refusal. irpt-status 5fSyChId passed the cold start and failed exactly here: its
refusal record raised TypeError (public_line(admitted=)) and every such refusal became a 500.
"""
import argparse
import importlib
import json
import os
import subprocess
import sys
import tempfile
import zipfile

AWS = r"C:\Users\AndrewBerman\Desktop\ajb_workspace\.tools\aws.cmd"


def live_configuration(function):
    out = subprocess.run([AWS, "lambda", "get-function-configuration", "--function-name", function,
                          "--query", "{h:Handler,env:Environment.Variables}", "--output", "json"],
                         capture_output=True, text=True)
    if out.returncode:
        raise SystemExit("ERROR: get-function-configuration %s rc=%d" % (function, out.returncode))
    cfg = json.loads(out.stdout)
    return cfg["h"], cfg.get("env") or {}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("zip")
    ap.add_argument("--function", required=True)
    ap.add_argument("--route", required=True, help='e.g. "GET /api/scoped/investor-reporting/status"')
    ap.add_argument("--owner-refusal", help='e.g. "GET /api/scoped/investor-reporting/status/{jobId}"')
    a = ap.parse_args(argv)
    handler_ref, env = live_configuration(a.function)
    module_name, function_name = handler_ref.rsplit(".", 1)
    root = tempfile.mkdtemp(prefix="cold-start-")
    zipfile.ZipFile(a.zip).extractall(root)
    os.environ.update(env)
    os.environ.update(AWS_ENDPOINT_URL="http://127.0.0.1:9", AWS_DEFAULT_REGION="us-east-1",
                      AWS_ACCESS_KEY_ID="smoke", AWS_SECRET_ACCESS_KEY="smoke", AWS_SESSION_TOKEN="smoke")
    for var in ("AWS_PROFILE",):
        os.environ.pop(var, None)
    sys.path[:] = [root] + [p for p in sys.path if "site-packages" in p or p.endswith(("DLLs", "lib", "Lib"))]
    print("zip %s | function %s | handler %s | env names %s" % (os.path.basename(a.zip), a.function, handler_ref,
                                                                sorted(env)))
    try:
        module = importlib.import_module(module_name)
        method, path = a.route.split(" ", 1)
        event = {"version": "2.0", "routeKey": a.route, "rawPath": path, "headers": {}, "queryStringParameters": {},
                 "requestContext": {"http": {"method": method}}, "body": "{}" if method == "POST" else None,
                 "isBase64Encoded": False}
        answer = getattr(module, function_name)(event, None)
    except Exception as exc:  # noqa: BLE001 -- the verdict IS the exception class
        import traceback
        first = str(exc).splitlines()[0][:200] if str(exc) else ""
        print("FAIL: %s: %s" % (type(exc).__name__, first))
        for frame in traceback.extract_tb(exc.__traceback__)[-4:]:
            print("   at %s:%d %s" % (os.path.relpath(frame.filename, root) if frame.filename.startswith(root)
                                     else frame.filename, frame.lineno, frame.name))
        return 1
    envelope = answer.get("status") if isinstance(answer, dict) else None
    status = answer.get("statusCode") or (envelope.get("state") if isinstance(envelope, dict) else None)
    print("   response keys:", sorted(answer)[:8] if isinstance(answer, dict) else type(answer).__name__)
    outside = sorted(n for n, m in list(sys.modules.items()) if getattr(m, "__file__", None)
                     and os.path.exists(os.path.join(root, n + ".py")) and not m.__file__.startswith(root))
    print("PASS: the cold-start build answered an unauthenticated request with state/statusCode %s | first-party modules "
          "from outside the zip: %s" % (status, outside or "none"))

    if a.owner_refusal and not outside:
        method, path = a.owner_refusal.split(" ", 1)
        viewer = {"x-contract-version": "v1", "x-origin-verify": "cloudfront", "x-user-email": "smoke-viewer@opal.test",
                  "x-user-role": "admin", "x-user-type": "Dev", "x-firm-id": "opal-capital", "x-user-name": "Smoke Viewer"}
        event = {"version": "2.0", "routeKey": a.owner_refusal, "rawPath": path, "headers": viewer,
                 "queryStringParameters": {},  # no selected_tenant: the viewer's own firm is refused INSIDE the owner read
                 "pathParameters": {"jobId": "REQ-" + "0" * 24, "requestId": "REQ-" + "0" * 24},
                 "requestContext": {"http": {"method": method}}, "isBase64Encoded": False}
        try:
            refused = getattr(module, function_name)(event, None)
        except Exception as exc:  # noqa: BLE001
            print("FAIL: owner-read refusal raised %s: %s" % (type(exc).__name__, (str(exc).splitlines() or [""])[0][:200]))
            return 1
        body = refused
        if isinstance(refused, dict) and isinstance(refused.get("body"), str):
            try:
                body = json.loads(refused["body"])
            except ValueError:
                body = {}
        status = (body.get("status") or {}) if isinstance(body, dict) else {}
        code = refused.get("statusCode") if isinstance(refused, dict) else None
        if code == 500 or not status.get("public_reason_code"):
            print("FAIL: owner-read refusal answered statusCode %s, reason %s" % (code, status.get("public_reason_code")))
            return 1
        print("PASS: owner-read refusal answered a named refusal: %s %s" % (status.get("state"), status.get("public_reason_code")))
    return 0 if not outside else 1


if __name__ == "__main__":
    sys.exit(main())
