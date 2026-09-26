"""K5: EXACTLY ONE POST /analysis (Overview) on the live 12.03 input, as the walk principal. No re-POST, no retry.

Env: WALK_PW (read by name by the runner, never printed), WALK_EMAIL, WALK_DEADLINE, WALK_AUTHORITY.
Usage: python live_submit.py <out.json> [--dry]   (--dry validates and prints the body; no network call)
"""
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import live_upload as lu  # noqa: E402  (reuses the scrubbed call/log helpers)

INPUT_ID = os.environ.get("WALK_INPUT_ID", "portfolio_99e76df8b63be3bccbaa0903586d46269dc13d7befd25a6b5983460d8444d68a")
SCHEMA = (r"C:\Users\AndrewBerman\Desktop\irpt-smoke-p-backend-20260923\docs\contracts\investor-reporting\v1"
          r"\AnalysisSubmissionRequest.schema.json")
BODY = {"request_id": "y-live-1203-overview-20260926", "client_id": None, "account_ids": [], "snapshot_id": None,
        "variant": "overview", "comparison_keys": [], "report_title": None,
        "prepared_for": "IRPT live walk 12.03", "input_id": INPUT_ID}


def validate():
    import jsonschema
    jsonschema.Draft202012Validator(json.load(open(SCHEMA, encoding="utf-8"))).validate(BODY)


def main():
    out = sys.argv[1]
    validate()
    if "--dry" in sys.argv:
        print("OK: body validates against AnalysisSubmissionRequest", json.dumps(BODY))
        return 0
    deadline = datetime.datetime.fromisoformat(os.environ["WALK_DEADLINE"])
    if lu.now() >= deadline:
        print("ERROR: past the deadline; no POST made")
        return 1
    email, pw = os.environ["WALK_EMAIL"], os.environ.pop("WALK_PW")
    s, login = lu.call("POST", "/auth/login", {"email": email, "password": pw}, {"Content-Type": "application/json"},
                       scrub_body={"email": email, "password": "<redacted>"})
    del pw
    token = login.get("accessToken") if isinstance(login, dict) else None
    print("login status", s, "| token present:", bool(token))
    if token:
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token, "X-Contract-Version": "v1"}
        s, resp = lu.call("POST", "/api/scoped/investor-reporting/analysis?selected_tenant=" + lu.TENANT, BODY, headers)
        d = resp.get("data") if isinstance(resp, dict) else None
        print(lu.now().strftime("%H:%M:%SZ"), "POST /analysis", s, "| data keys", sorted(d) if isinstance(d, dict) else d,
              "| status", json.dumps(resp.get("status"))[:300] if isinstance(resp, dict) else resp)
    json.dump({"principal": email, "tenant": lu.TENANT, "authority": os.environ.get("WALK_AUTHORITY", "<unset>"),
               "calls": lu.log}, open(out, "w", encoding="utf-8", newline="\n"), indent=1)
    print("calls logged", len(lu.log))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
