"""Cold-start smoke of a BUILT flat Lambda zip (CTO 102204 item 3): import the handler and run its cold-start build.

    python zip_cold_start_smoke.py <zip> --function <lambda name> --route "<METHOD> <path>"

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
    return 0 if not outside else 1


if __name__ == "__main__":
    sys.exit(main())
