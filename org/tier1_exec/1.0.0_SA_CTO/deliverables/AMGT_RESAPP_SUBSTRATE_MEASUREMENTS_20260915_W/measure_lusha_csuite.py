"""AMGT_RESAPP exec-management SUBSTRATE MEASUREMENT (Rule 28) -- 1.0.0_SA_CTO~W, 2026-09-15.

One company (Boeing, boeing.com), the whole C-suite via Lusha v3 contacts/prospecting (a ROSTER read:
name, title, LinkedIn URL; NO contact reveal -- the estate's interim policy keeps contacts/enrich off).
Prints: the seniority filter values Lusha exposes, the roster size, the field set each person carries,
whether any TENURE / role-start field exists, credits consumed. Key from the environment (bash side),
never printed. Egress authority: Andrew-direct ~05:2xZ (record @473526f738).
"""
import json
import os
import sys
import time

import requests

sys.path.insert(0, os.path.join(os.getcwd(), "data", "find", "imo", "scripts"))
from _util.lusha_client import LushaClient, LUSHA_API_BASE  # noqa: E402

key = os.environ.get("LUSHA_KEY_RAW", "").strip()
if not key:
    raise SystemExit("LUSHA_KEY_RAW not provided by the bash wrapper")
try:
    d = json.loads(key)
    key = next((d[k] for k in ("api_key", "LUSHA_API_KEY", "key", "value") if k in d), next(iter(d.values())))
except ValueError:
    pass
hdr = {"api_key": key, "Content-Type": "application/json"}
out_dir = os.path.join(os.environ["SCRATCH"], "lusha_measure")
os.makedirs(out_dir, exist_ok=True)
rec = {"measured_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "company_domain": "boeing.com"}

# 1. usage BEFORE (credits), rate-limited 5/min -- one read
r = requests.get(LUSHA_API_BASE + "account/usage", headers=hdr, timeout=30)
print("usage rc=%d" % r.status_code)
usage_before = r.json() if r.ok else {"error": r.text[:200]}
rec["usage_before"] = usage_before
cr = usage_before.get("credits") if isinstance(usage_before, dict) else None
print("credits before:", cr)

# 2. seniority filter values (discovery)
r = requests.get(LUSHA_API_BASE + "contacts/prospecting/filters/seniority", headers=hdr, timeout=30)
print("seniority filter rc=%d" % r.status_code)
sen = r.json() if r.ok else {"error": r.text[:300]}
rec["seniority_values"] = sen
print("seniority values:", json.dumps(sen)[:600])

# pick the C-suite-like value(s) from whatever the API calls them
vals = []
def walk(o):
    if isinstance(o, dict):
        for v in o.values():
            walk(v)
    elif isinstance(o, list):
        for v in o:
            walk(v)
    else:
        vals.append(str(o))
walk(sen)
csuite = [v for v in vals if any(t in v.lower() for t in ("c-suite", "csuite", "c_suite", "cxo", "chief", "executive"))]
print("candidate C-suite values:", csuite[:6])

# 3. the roster: contacts/prospecting on the company domain, C-suite seniority
client = LushaClient(api_key=key)
seniority_arg = csuite[:2] if csuite else None
t0 = time.time()
resp, meta = client.contacts_prospecting(company_domains=["boeing.com"], seniority=seniority_arg, page=0, page_size=50)
print("prospecting: %.1fs  meta=%s" % (time.time() - t0, getattr(meta, "to_telemetry_dict", lambda: str(meta))()))
rec["prospecting_meta"] = getattr(meta, "to_telemetry_dict", lambda: str(meta))()
rec["prospecting_response"] = resp
contacts = None
if isinstance(resp, dict):
    for k in ("contacts", "data", "results", "items"):
        if isinstance(resp.get(k), list):
            contacts = resp[k]
            break
    if contacts is None:
        for v in resp.values():
            if isinstance(v, list):
                contacts = v
                break
contacts = contacts or []
print("roster size returned:", len(contacts), "| top-level keys:", list(resp.keys())[:10] if isinstance(resp, dict) else type(resp).__name__)
fields = set()
for c in contacts:
    if isinstance(c, dict):
        fields.update(c.keys())
print("field set across the roster (%d fields):" % len(fields), sorted(fields))
tenure_like = [f for f in fields if any(t in f.lower() for t in ("tenure", "start", "since", "joined", "date"))]
print("tenure-like fields:", tenure_like)
for c in contacts[:12]:
    if isinstance(c, dict):
        print("   ", {k: str(c.get(k))[:40] for k in ("fullName", "firstName", "lastName", "jobTitle", "seniority", "department", "linkedinUrl", "companyName") if k in c})

# 4. usage AFTER
time.sleep(13)  # 5/min on the usage endpoint
r = requests.get(LUSHA_API_BASE + "account/usage", headers=hdr, timeout=30)
usage_after = r.json() if r.ok else {"error": r.text[:200]}
rec["usage_after"] = usage_after
print("credits after:", usage_after.get("credits") if isinstance(usage_after, dict) else usage_after)

p = os.path.join(out_dir, "boeing_csuite_prospecting.json")
open(p, "w", encoding="utf-8").write(json.dumps(rec, indent=2, ensure_ascii=True, default=str))
print("saved:", p)
