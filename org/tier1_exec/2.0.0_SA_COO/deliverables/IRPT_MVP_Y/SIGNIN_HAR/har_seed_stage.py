#!/usr/bin/env python3
"""Stage Andrew's HAR session cookies for the seed-only host leg (Andrew-direct 2026-10-03 ~16:2xZ via 0.0.0_AB_MSTR
msgs 104639/104640: "the premise is that if your long lived token has died out, here is another one").

    python har_seed_stage.py <path-to.har> [--dry-run]

Reads ONLY the two cookies a session needs -- `ycsessionid` and `csrftoken` -- from the LAST request to ycharts.com in the
HAR, and writes them as a NEW VERSION of `ycharts/session/current` carrying ONE custom stage label, `IMPORT_HAR`, and
NOT `AWSCURRENT`: the resident and the broker read AWSCURRENT only, so nothing reads the staged version except the host
leg (`har_seed_host.sh`). cf_clearance and aws-waf-token are NOT staged: they are bound to Andrew's browser, and the
host's browser mints its own WAF token. Values are held in memory and never printed; the output is the cookie NAMES,
lengths and the new version id. `--dry-run` prints what would be staged (names and lengths) and writes nothing.
After the host leg, the label is removed (`har_seed_unstage.py` step in the packet). ASCII only.
"""
import json
import sys

import boto3

SECRET_ID = "ycharts/session/current"
STAGE = "IMPORT_HAR"
NEEDED = ("ycsessionid", "csrftoken")


def main(argv):
    path, dry = argv[1], "--dry-run" in argv
    har = json.load(open(path, encoding="utf-8"))
    entries = [e for e in har["log"]["entries"] if "ycharts.com" in e["request"]["url"].split("/")[2]]
    picked, at = {}, None
    for e in sorted(entries, key=lambda x: x["startedDateTime"]):
        cookies = {c["name"]: c["value"] for c in e["request"].get("cookies", [])}
        if all(n in cookies and cookies[n] for n in NEEDED):
            picked, at = {n: cookies[n] for n in NEEDED}, e["startedDateTime"]
    if not picked:
        print("REFUSED: no request to ycharts.com carries both", NEEDED)
        return 2
    seed = [{"name": n, "value": v, "domain": ".ycharts.com", "path": "/", "secure": True, "httpOnly": n == "ycsessionid",
             "sameSite": "Lax"} for n, v in picked.items()]
    body = {"kind": "HAR_SEED", "source": "operator HAR (Andrew), last ycharts.com request %s" % at[:19], "seed_cookies": seed}
    print("seed from request at %s: %s" % (at[:19], ", ".join("%s(len %d)" % (n, len(v)) for n, v in picked.items())))
    if dry:
        print("DRY RUN: nothing written")
        return 0
    sm = boto3.client("secretsmanager", region_name="us-east-1")
    out = sm.put_secret_value(SecretId=SECRET_ID, SecretString=json.dumps(body), VersionStages=[STAGE])
    del body, seed, picked
    stages = sm.describe_secret(SecretId=SECRET_ID)["VersionIdsToStages"]
    current = [v for v, s in stages.items() if "AWSCURRENT" in s]
    print("staged version %s with %s; AWSCURRENT unchanged: %s" % (out["VersionId"], STAGE, current))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
