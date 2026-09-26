#!/usr/bin/env python3
"""CTO 101109 (2): the backend walk acts by API on the bounded Opal-class walk principal (packet blob fe8e8d89).

    python walk_api.py <epoch> <log.jsonl> search <tenant> <query>
    python walk_api.py <epoch> <log.jsonl> perf   <tenant> <entry_kind> <entry_id> <start> <end>

Logs in through the real auth route with the password read BY NAME from the SecureString (never printed), then
sends the portal's own requests (portal/src/api/endpoints/investor-reporting.ts route table). Every request and
response is appended to <log.jsonl>, scrubbed: no password, no Authorization header, no token value.
"""
from __future__ import annotations

import datetime as dt
import json
import sys
import urllib.error
import urllib.parse
import urllib.request

import boto3

AUTH_API = "https://opalinvest.dev"  # via CloudFront: the auth handler requires the edge-injected origin header (auth-handler/src/index.ts:203-221)
ORIGIN = "https://opalinvest.dev"
BASE = ORIGIN + "/api/scoped/investor-reporting"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) opal-irpt-walk/1 (2.0.0_SA_COO~P, CTO 101109)"


def _now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


class Walk(object):
    def __init__(self, epoch, log_path):
        self.email = "irpt-walk-%s@opal.test" % epoch
        self.param = "/irpt/walk-principal/%s/password" % epoch
        self.log_path = log_path
        self.token = None
        self.secrets = []

    def log(self, row):
        text = json.dumps(row, sort_keys=True)
        for s in self.secrets:
            text = text.replace(s, "<redacted>")
        with open(self.log_path, "a", encoding="utf-8", newline="\n") as f:
            f.write(text + "\n")

    def login(self):
        pw = boto3.client("ssm").get_parameter(Name=self.param, WithDecryption=True)["Parameter"]["Value"]
        self.secrets.append(pw)
        body = json.dumps({"email": self.email, "password": pw}).encode("ascii")
        req = urllib.request.Request(AUTH_API + "/auth/login", data=body, method="POST",
                                     headers={"Content-Type": "application/json", "Origin": ORIGIN, "User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.loads(r.read())
        except urllib.error.HTTPError as e:
            self.log({"at": _now(), "request": {"method": "POST", "url": AUTH_API + "/auth/login", "body": "<redacted>"},
                      "response": {"status": e.code, "body": e.read().decode("utf-8", "replace")[:300]}})
            raise SystemExit("STOP: login HTTP %d" % e.code)
        self.token = data.get("accessToken")
        self.secrets.append(self.token)
        exp = None
        try:
            import base64
            seg = self.token.split(".")[1]
            exp = json.loads(base64.urlsafe_b64decode(seg + "=" * (-len(seg) % 4)))["exp"]
        except Exception:
            pass
        self.log({"at": _now(), "request": {"method": "POST", "url": AUTH_API + "/auth/login", "body": "<redacted>"},
                  "response": {"status": 200, "access_token_exp": exp,
                               "user": data.get("user")}})
        print("OK: login; access token exp %s (%s)" % (exp, dt.datetime.fromtimestamp(exp, dt.timezone.utc).isoformat() if exp else "?"))

    def call(self, method, path, query=None, body=None):
        url = BASE + path + ("?" + urllib.parse.urlencode(query) if query else "")
        data = json.dumps(body).encode("utf-8") if body is not None else None
        headers = {"Authorization": "Bearer " + self.token, "Accept": "application/json", "Origin": ORIGIN, "User-Agent": UA,
                   "X-Contract-Version": "v1"}
        if data is not None:
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(url, data=data, method=method, headers=headers)
        t0 = _now()
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                status, text = r.status, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            status, text = e.code, e.read().decode("utf-8", "replace")
        try:
            parsed = json.loads(text)
        except ValueError:
            parsed = text[:2000]
        self.log({"at": t0, "request": {"method": method, "url": url, "body": body, "authorization": "<redacted>"},
                  "response": {"status": status, "body": parsed}})
        return status, parsed


def main(argv):
    epoch, log_path, cmd = argv[1], argv[2], argv[3]
    w = Walk(epoch, log_path)
    w.login()
    if cmd == "search":
        tenant, query = argv[4], argv[5]
        st, out = w.call("GET", "/directory/search", {"query": query, "selected_tenant": tenant, "limit": "25"})
        print("search HTTP %s" % st)
        entries = (out.get("data") or {}).get("entries") if isinstance(out, dict) else None
        if entries is None:
            print(json.dumps(out)[:1500])
        for e in entries or []:
            print(json.dumps({k: e.get(k) for k in ("kind", "id", "entryId", "label", "displayName", "accountCount", "account_count", "status")}))
    elif cmd == "perf":
        tenant, kind, entry_id, start, end = argv[4:9]
        st, sel = w.call("POST", "/selections", {"selected_tenant": tenant}, {"scope_kind": kind, "scope_ids": [entry_id]})
        print("selection HTTP %s %s" % (st, json.dumps(sel)[:600]))
        sel_id = None
        if isinstance(sel, dict):
            d = sel.get("data") or sel
            sel_id = d.get("accountSetId") or d.get("account_set_id") or d.get("id")
        if not sel_id:
            raise SystemExit("STOP: no selection id")
        st, rep = w.call("GET", "/performance/%s" % sel_id, {"start": start, "end": end, "selected_tenant": tenant})
        print("performance HTTP %s %s" % (st, json.dumps(rep)[:1500]))
    else:
        raise SystemExit("unknown command")


if __name__ == "__main__":
    main(sys.argv)
