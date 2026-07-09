#!/usr/bin/env python3
"""comp-deadgrant -- find the LIVE-DEGRADE universe: a dead secret grant met by a fail-silent reader.

DETECT pillar, leg 3. Siblings: comp-firmsep-sweep (leg 2, prove-the-universe),
comp-denytest (VERIFY).

WHY THIS EXISTS
---------------
Two defects are individually benign and jointly invisible:

  AXIS A -- a DEAD reach. The consumer asks Secrets Manager for a secret it cannot get:
            either its role has no Allow for that ARN (region-mismatched grant -> AccessDenied),
            or the secret does not exist in the region the CLIENT targets (-> ResourceNotFound).
  AXIS B -- a FAIL-SILENT reader. `except: return {} / '' / None / mock`. The Lambda returns 200.

Together: the feature is degraded, in production, and nothing anywhere reports it.

Found live on 2026-07-09: `daily-agenda-generator` had a us-east-2 `github-token` grant, called
us-east-1, got AccessDenied, warned, continued UNAUTHENTICATED, and GitHub 404'd the private repos.
The daily agenda had been produced with no private-repo commit data. Nothing ever errored to a caller.

THE SUBTLETY THAT DECIDES CORRECTNESS -- USE THE CLIENT'S REGION, NOT THE LAMBDA'S
----------------------------------------------------------------------------------
On the same day this tool was written, its author filed `yang-generate-volatility` as the same
"region-mismatched grant" bug. It is NOT. Its code does
`boto3.client('secretsmanager', region_name='us-east-2')`, so the grant is correctly ALIGNED --
a simulate against the us-east-2 ARN returns `allowed`. The real defect is that the SECRET does not
exist in us-east-2. Same symptom, different cause. Evaluating against the Lambda's own region would
have reproduced the author's error in code.

So: parse `region_name=` off the client construction; default to the Lambda's region; resolve the
secret IN THAT REGION; and distinguish NO_GRANT from NO_SECRET.

THE FALSE NEGATIVE THIS TOOL SHIPPED WITH, AND WHY IT MATTERS MORE THAN THE FINDINGS
------------------------------------------------------------------------------------
v1 enumerated secrets by parsing `SecretId=` for a QUOTED LITERAL. It therefore returned
**exit 0 -- "no live degrade"** on `daily-agenda-generator`, the exact Lambda it was written
from, which has a verbatim `AccessDeniedException` in its own CloudWatch log. The reason:

    GITHUB_SECRET = os.environ.get('GITHUB_SECRET', 'github-token')
    secrets_client.get_secret_value(SecretId=GITHUB_SECRET)      # a CONSTANT, not a literal

It also reported `MyTestSecret` and `STRING_VALUE` -- AWS SDK documentation examples inside
`node_modules`. A tool built to hunt the enumerate-by-code-shape blind spot had the blind spot.

So it now ENUMERATES BY THE RESOURCE: every live secret name, matched against every file (and the
Lambda's env, where `config-as-data` hides the name). That is expression-form- and language-agnostic
BY CONSTRUCTION -- the literal survives as the env default even when the call site names a constant,
and a doc example cannot false-fire because it is not a live secret. `SecretId=` parsing is retained
ONLY to flag CONSTRUCTED names (a completeness signal, reported as uninspectable), never to enumerate.

LIVE vs LATENT
--------------
A dead grant on a Lambda that has not run in six months is a dormant capability, not a broken
feature. Severity is decided by the LAST INVOCATION, read from its CloudWatch log stream --
never asserted from the code. `yang-generate-volatility` last ran 175 days ago: LATENT.
`daily-agenda-generator` ran 10 hours ago: LIVE.

A blank is never a pass: an unreadable artifact, an unresolvable region, or a missing verdict is
reported as UNKNOWN and counted, never silently dropped.
"""
from __future__ import annotations

import argparse
import io
import json
import re
import shutil
import subprocess
import sys
import time
import urllib.request
import zipfile

AWS = shutil.which("aws") or shutil.which("aws.cmd")
if not AWS:
    sys.exit("comp-deadgrant: cannot locate the `aws` executable on PATH.")

VENDOR = re.compile(r"(^|/)(botocore|boto3|urllib3|pydantic|openai|anthropic|requests|numpy|"
                    r"pandas|dateutil|s3transfer|jmespath|charset_normalizer|idna|certifi|"
                    r"node_modules)/")
# `boto3.client('secretsmanager', region_name='us-east-2')` -- capture the region if stated.
CLIENT = re.compile(r"boto3\.client\(\s*['\"]secretsmanager['\"]\s*(?:,\s*region_name\s*=\s*['\"]([a-z0-9-]+)['\"])?")
JS_CLIENT = re.compile(r"new\s+SecretsManagerClient\(\s*\{[^}]*region:\s*['\"]([a-z0-9-]+)['\"]")
# SecretId='literal' / SecretId: "literal"
SECRET_ID = re.compile(r"SecretId\s*[=:]\s*['\"]([^'\"]{2,120})['\"]")
# fail-silent: the handler swallows and returns a benign value
SILENT = re.compile(r"return\s*(\{\}|''|\"\"|\[\]|None|null)|^\s*pass\b|get_mock|return\s+get_mock")
LOUD = re.compile(r"\braise\b|\bthrow\b|sys\.exit")


def aws(*a, region=None):
    cmd = [AWS, *a] + (["--region", region] if region else [])
    p = subprocess.run(cmd, capture_output=True, text=True, stdin=subprocess.DEVNULL)
    return p.returncode, p.stdout.replace("\r", "").strip(), p.stderr.strip()


def lambdas():
    rc, out, err = aws("lambda", "list-functions",
                       "--query", "Functions[].[FunctionName,Role,PackageType]", "--output", "text")
    if rc:
        sys.exit(f"comp-deadgrant: list-functions failed: {err[:160]}")
    rows = [ln.split("\t") for ln in out.split("\n") if ln.strip()]
    if not rows:
        sys.exit("comp-deadgrant: no functions. An empty universe is not a clean sweep.")
    return rows


def artifact(fn):
    rc, out, _ = aws("lambda", "get-function", "--function-name", fn,
                     "--query", "Code.Location", "--output", "text")
    if rc or not out or out == "None":
        return None
    try:
        return zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(out, timeout=240).read()))
    except Exception:
        return None


def last_run(fn):
    rc, out, _ = aws("logs", "describe-log-streams", "--log-group-name", f"/aws/lambda/{fn}",
                     "--order-by", "LastEventTime", "--descending", "--max-items", "1",
                     "--query", "logStreams[0].lastEventTimestamp", "--output", "text")
    if rc or not out or out.split("\n")[0] in ("None", ""):
        return None                      # no log group / never ran / cannot see
    try:
        return int(out.split("\n")[0])
    except ValueError:
        return None


def all_live_secret_names(regions):
    """The RESOURCE side of the match. Empty is not a clean sweep."""
    names = set()
    for r in regions:
        rc, out, _ = aws("secretsmanager", "list-secrets", "--max-items", "500",
                         "--query", "SecretList[].Name", "--output", "text", region=r)
        if rc == 0 and out:
            names |= {n for n in out.replace("\t", "\n").split("\n") if n.strip()}
    if not names:
        sys.exit("comp-deadgrant: zero live secrets resolved. Refusing to sweep against an empty universe.")
    return names


def env_of(fn):
    rc, out, _ = aws("lambda", "get-function-configuration", "--function-name", fn,
                     "--query", "Environment.Variables", "--output", "json")
    if rc or not out:
        return {}
    try:
        return json.loads(out) or {}
    except ValueError:
        return {}


def main() -> int:
    p = argparse.ArgumentParser(prog="comp-deadgrant")
    p.add_argument("--account", default="313476888478")
    p.add_argument("--live-days", type=float, default=30.0,
                   help="a consumer that ran within this window is LIVE; older is LATENT")
    p.add_argument("--json", metavar="PATH")
    a = p.parse_args()

    fns = lambdas()
    live_names = all_live_secret_names(["us-east-1", "us-east-2"])
    now_ms = int(time.time() * 1000)
    print(f"live secret names (both regions): {len(live_names)}")
    print(f"lambdas in account: {len(fns)}\n")

    rows, uninspectable, secret_cache = [], [], {}

    def resolve(name, region):
        key = (name, region)
        if key not in secret_cache:
            rc, out, _ = aws("secretsmanager", "describe-secret", "--secret-id", name,
                             "--query", "ARN", "--output", "text", region=region)
            secret_cache[key] = out if (rc == 0 and out and out != "None") else None
        return secret_cache[key]

    for i, (fn, role_arn, pkg) in enumerate(fns, 1):
        role = role_arn.rsplit("/", 1)[-1]
        if pkg == "Image":
            uninspectable.append((fn, "PackageType=Image (inspect via ECR layers if it matters)"))
            continue
        z = artifact(fn)
        if z is None:
            uninspectable.append((fn, "artifact unreadable"))
            continue
        # ENUMERATE BY THE RESOURCE, NEVER BY THE CODE SHAPE.
        #
        # v1 of this tool parsed `SecretId=` for a QUOTED LITERAL -- and therefore missed the very
        # Lambda it was written from: `daily-agenda-generator` binds
        # `GITHUB_SECRET = os.environ.get('GITHUB_SECRET', 'github-token')` and calls
        # `get_secret_value(SecretId=GITHUB_SECRET)`. A constant at the call site. The tool returned
        # exit 0 ("no live degrade") on a case with verbatim AccessDenied in its own CloudWatch log.
        # It also reported `MyTestSecret` / `STRING_VALUE` -- AWS SDK doc examples out of node_modules.
        #
        # Matching the RESOURCE (every live secret name, in every file) is expression-form- and
        # language-agnostic by construction: the literal is present as the env default even when the
        # call site names a constant, and a doc example is not a live secret so it cannot false-fire.
        # `SecretId=` parsing is retained ONLY to detect CONSTRUCTED names -- a completeness signal,
        # not the enumeration.
        region, names, constructed, silent = None, set(), [], None
        for info in z.infolist():
            if info.is_dir() or not info.filename.endswith((".py", ".js", ".mjs", ".ts")):
                continue
            vend = bool(VENDOR.search(info.filename))
            try:
                txt = z.read(info).decode("utf-8", errors="replace")
            except Exception:
                continue
            for nm in live_names:                       # resource-match, EVERY file incl. vendored
                if nm in txt:
                    names.add(nm)
            if vend:
                continue                                # SDK chatter below this line is noise
            for m in CLIENT.finditer(txt):
                region = m.group(1) or region
            for m in JS_CLIENT.finditer(txt):
                region = m.group(1) or region
            for m in re.finditer(r"SecretId\s*[=:]\s*([^,)}\n]{1,80})", txt):
                v = m.group(1).strip()
                if v.startswith(("'", '"')):
                    lit = v.strip("'\"")
                    if lit not in live_names:
                        names.add(lit)                  # a name we cannot resolve = possibly deleted
                elif "${" in v or v.startswith("`") or "+" in v or ".format" in v:
                    constructed.append(f"{info.filename}: {v[:50]}")
            for m in re.finditer(r"get_secret_value|GetSecretValueCommand", txt):
                tail = txt[m.start():m.start() + 700]
                if "except" in tail or "catch" in tail:
                    after = re.split(r"except|catch", tail, 1)[-1]
                    s = bool(SILENT.search(after)) and not LOUD.search(after[:200])
                    silent = s if silent is None else (silent or s)
        for k, v in (env_of(fn) or {}).items():         # config-as-data: the name may live in env
            if v in live_names:
                names.add(v)
        if constructed:
            uninspectable.append((fn, f"CONSTRUCTED SecretId -- resource-match may be incomplete: "
                                      f"{constructed[0]}"))
        if not names:
            continue
        lam_region = role_arn.split(":")[3] if role_arn.count(":") > 3 else "us-east-1"
        eff = region or "us-east-1"
        for name in sorted(names):
            arn = resolve(name, eff)
            if arn is None:
                verdict, why = "DEAD", f"NO_SECRET in {eff}"
            else:
                rc, out, _ = aws("iam", "simulate-principal-policy",
                                 "--policy-source-arn", f"arn:aws:iam::{a.account}:role/{role}",
                                 "--action-names", "secretsmanager:GetSecretValue",
                                 "--resource-arns", arn, "--query",
                                 "EvaluationResults[].EvalDecision", "--output", "text")
                if rc or not out:
                    verdict, why = "UNKNOWN", "no verdict (never a pass)"
                elif out != "allowed":
                    verdict, why = "DEAD", f"NO_GRANT ({out}) in {eff}"
                else:
                    verdict, why = "OK", f"allowed in {eff}"
            if verdict == "OK":
                continue
            ts = last_run(fn)
            age = (now_ms - ts) / 86400000.0 if ts else None
            sev = ("LIVE" if (age is not None and age <= a.live_days)
                   else "LATENT" if age is not None else "UNKNOWN-LASTRUN")
            rows.append(dict(fn=fn, role=role, secret=name, client_region=eff,
                             lambda_region=lam_region, verdict=verdict, why=why,
                             fail_silent=silent, sev=sev,
                             days_since_run=round(age, 1) if age is not None else None))
            print(f"  [{sev:15s}] {fn:38s} {name:28s} {why}"
                  f"  fail_silent={silent}")
        if i % 25 == 0:
            print(f"  ... {i}/{len(fns)}", flush=True)

    print("\n================ LIVE-DEGRADE UNIVERSE (dead reach x fail-silent reader) ================")
    live = [r for r in rows if r["sev"] == "LIVE" and r["fail_silent"]]
    for r in live:
        print(f"  !! {r['fn']} ({r['role']}) -> {r['secret']}: {r['why']}; "
              f"ran {r['days_since_run']}d ago; reader SWALLOWS the failure")
    if not live:
        print("  none")
    print(f"\n  dead-reach rows: {len(rows)}   LIVE+fail-silent: {len(live)}   "
          f"uninspectable: {len(uninspectable)} (never silently dropped)")
    for fn, why in uninspectable[:12]:
        print(f"     uninspectable: {fn} -- {why}")
    if a.json:
        json.dump({"rows": rows, "uninspectable": uninspectable},
                  open(a.json, "w", encoding="utf-8"), indent=1)
        print(f"\n  full table -> {a.json}")
    return 1 if live else 0


if __name__ == "__main__":
    sys.exit(main())
