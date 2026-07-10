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

AXIS B IS A SYSTEM PROPERTY, AND THIS TOOL ONLY SEES THE GETTER
---------------------------------------------------------------
`fail_silent` here is a GETTER-LEVEL heuristic: it reads the `except` around the
`get_secret_value` call. That is NOT the system's fail-mode, in EITHER direction:

  * reader LOUD, system SILENT -- `opalinvest-auth-handler`: `jwt.ts` re-raises on a failed
    secret read, and its caller `authenticateRequest` does `catch { return null }` -> a bare 401,
    identical to a wrong password, no log. Component-loud, system-silent.
  * reader SILENT, system LOUD -- `opal-trending-image-generator`: `get_openai_key()` swallows and
    `return ''` (:144-146), but the handler two lines later does
    `if not api_key: raise ValueError("OpenAI API key not found")` (:236-237), which surfaces as a
    traceback + HTTP 500. Component-silent, system-loud. Live logs: 3 tracebacks, 9 ValueErrors.

So a row's `fail_silent=True` means "the getter swallows," never "the feature degrades quietly."
Resolve axis B at the CALLER CHAIN, per row, before calling anything a degrade.

AXIS C -- WHAT THIS TOOL CANNOT PROVE, AND THEREFORE DOES NOT CLAIM
------------------------------------------------------------------
Axis A (a dead reach) and axis B (a fail-silent reader) are both decidable from the artifact and
live IAM. They are NOT sufficient. `opal-smartx-ingestion-pipeline` passes both and is not a
degrade: the getters that would break are never invoked, and the ones that ARE invoked handle the
null config with a designed hardcoded fallback (378 log events, 0 AttributeError, real output).

  AXIS C -- the swallowing path actually EXECUTES, and something downstream DEPENDS on its output.

Only rows passing A and B and C are degrades. This tool emits CANDIDATES, never verdicts, and says
so in its own output. Ground axis C per row against the CloudWatch log and the SERVED artifact.
(`schwab-anonymizer` fails axis B -- it raises. `smartx` fails axis C -- unreachable.)

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
# fail-silent AT THE GETTER. Not the system's fail-mode -- see the axis-B note in the docstring.
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


_GETFN_CACHE: dict = {}


def _get_function(fn):
    """ONE `get-function` per Lambda, memoized. It is a documented SUPERSET of
    get-function-configuration -- it returns Code.Location AND Configuration.{Handler,
    Environment} in a single response, verified data-identical to the three separate calls
    (Handler / Env / Code.Location) on 2026-07-10. artifact() + handler_file() + env_of()
    now share this ONE aws-CLI spawn instead of making three: the per-Lambda cost is
    dominated by the Windows aws-CLI cold-start (~1.4s/spawn), and 180 Lambdas x 2 saved
    spawns is ~8 min off a ~14 min full sweep (PROFILED, not inferred -- NFRA_TOOLPASS)."""
    if fn not in _GETFN_CACHE:
        rc, out, _ = aws("lambda", "get-function", "--function-name", fn, "--output", "json")
        try:
            _GETFN_CACHE[fn] = json.loads(out) if rc == 0 and out else {}
        except ValueError:
            _GETFN_CACHE[fn] = {}
    return _GETFN_CACHE[fn]


def artifact(fn):
    out = (_get_function(fn).get("Code") or {}).get("Location")
    if not out or out == "None":
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
    """The RESOURCE side of the match. The SEARCH SPACE must itself be a proven universe.

    `list-secrets` EXCLUDES secrets pending deletion by default. A consumer that still names one
    has a DEAD reach (GetSecretValue on a scheduled-deletion secret fails), and it is exactly the
    kind of reader this tool exists to find -- so excluding those names would let the failure
    escape the search. `--include-planned-deletion` closes it: 76 live + 2 pending = 78 in this
    account on 2026-07-09. (CTO's catch: method-1 exhaustiveness holds IFF the name inventory is
    complete; the search SPACE must be a proven universe, one level down from the sweep itself.)

    Empty is not a clean sweep.
    """
    names = set()
    for r in regions:
        for extra in (["--include-planned-deletion"], []):
            rc, out, _ = aws("secretsmanager", "list-secrets", *extra, "--max-items", "500",
                             "--query", "SecretList[].Name", "--output", "text", region=r)
            if rc == 0:
                names |= {n for n in out.replace("\t", "\n").split("\n") if n.strip()}
                break          # the flag is supported; the first call is the complete listing
    if not names:
        sys.exit("comp-deadgrant: zero secrets resolved. Refusing to sweep against an empty universe.")
    return names


def handler_file(fn):
    """The ENTRYPOINT's file. A deployed zip may ship stale copies of itself.

    `daily-agenda-generator` contains BOTH `lambda_function.py` (region us-east-1, the live handler)
    and `package/lambda_function.py` (region us-east-2, a stale build copy). Taking whichever client
    construction the file walk saw last gave the RIGHT verdict for the WRONG mechanism -- it reported
    NO_SECRET(us-east-2) where the Lambda's own log proves AccessDenied(us-east-1). A right answer
    with an invented mechanism is exactly what Rule 22 forbids, so the region is attributed from the
    configured Handler, and a disagreement between copies is itself reported.
    """
    out = (_get_function(fn).get("Configuration") or {}).get("Handler")
    if not out or out == "None":
        return None
    mod = out.rsplit(".", 1)[0]              # `lambda_function.lambda_handler` -> `lambda_function`
    return [f"{mod.replace('.', '/')}{ext}" for ext in (".py", ".js", ".mjs", ".ts")]


def env_of(fn):
    cfg = _get_function(fn).get("Configuration") or {}
    return (cfg.get("Environment") or {}).get("Variables") or {}


def _selftest() -> int:
    """Offline regression gate (no AWS). Pins the two invariants the 2026-07-10 perf
    consolidation could break: (1) the three consumers read the RIGHT fields from ONE
    get-function response, (2) the axis-B fail-silent classifier. A mutation to either
    must make this go RED (NFRA_TOOLPASS 2a) -- the tool had NO self-test before this."""
    # 1. CONSOLIDATION -- handler_file + env_of + artifact's location all read from ONE
    #    memoized get-function response (Code.Location + Configuration.{Handler,Environment}).
    canned = {"Code": {"Location": "https://prod/pkg.zip"},
              "Configuration": {"Handler": "lambda_function.lambda_handler",
                                "Environment": {"Variables": {"GITHUB_SECRET": "github-token"}}}}
    _GETFN_CACHE["__selftest__"] = canned
    try:
        assert handler_file("__selftest__") == ["lambda_function.py", "lambda_function.js",
                                                "lambda_function.mjs", "lambda_function.ts"], \
            "handler_file must read Configuration.Handler -> entrypoint paths"
        assert env_of("__selftest__") == {"GITHUB_SECRET": "github-token"}, \
            "env_of must read Configuration.Environment.Variables"
        assert (_get_function("__selftest__").get("Code") or {}).get("Location") == "https://prod/pkg.zip", \
            "artifact's Code.Location extraction path"
        # a config with NO env must yield {} (not raise) -- the fail-safe artifact/env_of rely on
        _GETFN_CACHE["__noenv__"] = {"Configuration": {"Handler": "app.handler"}}
        assert env_of("__noenv__") == {}, "env_of must fail-safe to {} when Environment absent"
        assert handler_file("__noenv__") == ["app.py", "app.js", "app.mjs", "app.ts"], "handler_file no-env"
        # POPULATION PATH: _get_function must PARSE the aws get-function JSON (not just read a
        # pre-seeded cache). Monkeypatch aws() with a canned response so the json.loads path is
        # exercised offline -- else a mutation that breaks parsing survives (it did, until this).
        _real_aws = globals()["aws"]
        globals()["aws"] = lambda *a, **k: (0, json.dumps(canned), "")
        try:
            _GETFN_CACHE.pop("__pop__", None)
            got = _get_function("__pop__")
            assert (got.get("Configuration") or {}).get("Handler") == "lambda_function.lambda_handler", \
                "_get_function must PARSE the aws get-function JSON into the response dict"
            # a nonzero rc (call failed) must yield {} -- fail-safe, not a crash
            globals()["aws"] = lambda *a, **k: (255, "", "boom")
            _GETFN_CACHE.pop("__err__", None)
            assert _get_function("__err__") == {}, "_get_function must fail-safe to {} on a failed call"
        finally:
            globals()["aws"] = _real_aws
            _GETFN_CACHE.pop("__pop__", None)
            _GETFN_CACHE.pop("__err__", None)
    finally:
        _GETFN_CACHE.pop("__selftest__", None)
        _GETFN_CACHE.pop("__noenv__", None)
    # 2. AXIS B -- the fail-silent-reader classifier (the semantic core; unchanged by the perf fix,
    #    pinned so a future edit cannot quietly break it).
    assert SILENT.search("except Exception:\n        return {}"), "SILENT matches a swallowing getter (return {})"
    assert SILENT.search("except:\n        return None"), "SILENT matches a return-None swallow"
    assert LOUD.search("except Exception:\n        raise"), "LOUD matches a re-raise"
    assert LOUD.search("} catch (e) {\n    throw e;"), "LOUD matches a JS throw"
    assert not LOUD.search("value = get()"), "a plain read is not LOUD"
    # KNOWN GAP, pinned so it is explicit (flagged to CTO, NOT fixed -- semantic layer): SILENT's
    # `^\s*pass\b` is anchored WITHOUT re.MULTILINE, so it only catches a `pass` at the START of
    # the searched text. The tool applies SILENT to `after` (post-except text), which never starts
    # with `pass`, so a swallow-by-bare-`pass` is missed. Pin the true behavior:
    assert SILENT.search("pass  # at text start"), "SILENT: pass caught ONLY at text start"
    assert not SILENT.search("x = 1\n    pass"), "SILENT: a mid-block pass is NOT caught (no MULTILINE)"
    # the tool's own cited examples: a swallow is SILENT-not-LOUD; a re-raise is LOUD.
    swallow = "except Exception:\n    return None"
    reraise = "except Exception as e:\n    raise RuntimeError(e)"
    assert bool(SILENT.search(swallow)) and not LOUD.search(swallow[:200]), "swallow -> fail-silent"
    assert bool(LOUD.search(reraise)), "re-raise -> loud"
    print("SELF-TEST PASS: get-function consolidation field-reads (Handler/Env/Location + fail-safe) "
          "+ axis-B SILENT/LOUD classifier.")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(prog="comp-deadgrant")
    p.add_argument("--account", default="313476888478")
    p.add_argument("--live-days", type=float, default=30.0,
                   help="a consumer that ran within this window is LIVE; older is LATENT")
    p.add_argument("--json", metavar="PATH")
    p.add_argument("--limit", type=int, default=0, metavar="N",
                   help="inspect only the first N lambdas (bounded sweep; 0 = full fleet). "
                        "A full sweep is ~180 lambdas x one get-function+download each.")
    p.add_argument("--self-test", action="store_true", help="offline regression gate (no AWS)")
    a = p.parse_args()

    if a.self_test:
        return _selftest()

    fns = lambdas()
    live_names = all_live_secret_names(["us-east-1", "us-east-2"])
    now_ms = int(time.time() * 1000)
    full_n = len(fns)
    if a.limit and a.limit < full_n:
        fns = fns[:a.limit]
        print(f"NOTE: --limit {a.limit} -> inspecting {len(fns)} of {full_n} lambdas "
              f"(BOUNDED sweep, not the full fleet -- coverage is partial by request).")
    print(f"live secret names (both regions): {len(live_names)}")
    print(f"lambdas in account: {full_n}"
          f"{' (inspecting %d)' % len(fns) if len(fns) != full_n else ''}\n")
    _t_start = time.time()

    rows, uninspectable, secret_cache = [], [], {}

    def resolve(name, region):
        key = (name, region)
        if key not in secret_cache:
            rc, out, _ = aws("secretsmanager", "describe-secret", "--secret-id", name,
                             "--query", "ARN", "--output", "text", region=region)
            secret_cache[key] = out if (rc == 0 and out and out != "None") else None
        return secret_cache[key]

    for i, (fn, role_arn, pkg) in enumerate(fns, 1):
        # PROGRESS at the TOP of the loop, BEFORE any `continue`. The old every-25 print sat at
        # the loop TAIL, past four continues (Image / unreadable / no-secret-call / no-names) --
        # so it only fired for lambdas that ran the whole body, and a fleet whose first lambdas
        # mostly lack a secret call showed "no output past startup" for minutes (CTO, 13min).
        # Top-of-loop + stderr + elapsed/rate/ETA proves liveness for EVERY lambda.
        if i % 10 == 0 or i == 1 or i == len(fns):
            _el = time.time() - _t_start
            _rate = _el / (i - 1) if i > 1 else 0.0
            print(f"  ... {i}/{len(fns)} lambdas  {_el:5.0f}s elapsed  {_rate:.1f}s/lambda  "
                  f"~{_rate * (len(fns) - i) / 60:.1f}min left", file=sys.stderr, flush=True)
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
        # A NAME IS NOT A READ. Resource-matching finds a secret name wherever it appears -- including
        # inside a COMMENT. `bd-realized-trigger`'s only mention of `opal/bd/credentials` is the
        # docstring "Credentials are fetched at runtime on the EC2 from opal/bd/credentials"; it has
        # no secretsmanager client at all. v2 reported it as a dead reach. A comment must not raise a
        # security finding. So: the artifact must contain an actual CALL SITE in non-vendor code
        # before any name is attributed to it. (v1's bias was the mirror image -- it demanded a quoted
        # literal AT the call site and missed constants. Reach = call-site presence AND resource-match.)
        region, names, constructed, silent = None, set(), [], None
        name_idents, write_calls = {}, set()
        entry = handler_file(fn) or []
        regions_seen = {}                    # file -> region, to catch stale copies disagreeing
        has_call = False
        for info in z.infolist():
            if info.is_dir() or not info.filename.endswith((".py", ".js", ".mjs", ".ts")):
                continue
            if VENDOR.search(info.filename):
                continue
            try:
                probe = z.read(info).decode("utf-8", errors="replace")
            except Exception:
                continue
            if re.search(r"get_secret_value|GetSecretValueCommand|getSecretValue", probe):
                has_call = True
                break
        if not has_call:
            continue

        for info in z.infolist():
            if info.is_dir() or not info.filename.endswith((".py", ".js", ".mjs", ".ts")):
                continue
            vend = bool(VENDOR.search(info.filename))
            try:
                txt = z.read(info).decode("utf-8", errors="replace")
            except Exception:
                continue
            # A name must be BOUND, not merely MENTIONED. v3 required a call site somewhere in the
            # artifact, but then attributed every resource-matched name to it -- so a name in a
            # COMMENT still fired: `inf-otp-relay` was flagged on `twilio/credentials`, which appears
            # only in "# validation against the twilio/credentials auth token", and
            # `bd-realized-trigger` on a docstring. A binding is `X = '<name>'` or `SecretId='<name>'`.
            for nm in live_names:
                if nm not in txt:
                    continue
                for ln in txt.split("\n"):
                    if nm not in ln:
                        continue
                    st = ln.strip()
                    if st.startswith(("#", "//", "*")):
                        continue                        # a comment is not a read
                    if "SecretId" in ln or "=" in ln:   # a binding or a direct argument
                        names.add(nm)
                        for m in re.finditer(r"([A-Za-z_][A-Za-z0-9_]*)\s*=", ln):
                            name_idents.setdefault(nm, set()).add(m.group(1))
                        break
            if vend:
                continue                                # SDK chatter below this line is noise
            for m in list(CLIENT.finditer(txt)) + list(JS_CLIENT.finditer(txt)):
                if m.group(1):
                    regions_seen[info.filename] = m.group(1)
                    # the ENTRYPOINT's region wins; other copies are stale build artifacts
                    if info.filename in entry or region is None:
                        region = m.group(1) if info.filename in entry else (region or m.group(1))
            for m in re.finditer(r"SecretId\s*[=:]\s*([^,)}\n]{1,80})", txt):
                v = m.group(1).strip()
                if v.startswith(("'", '"')):
                    lit = v.strip("'\"")
                    if lit not in live_names:
                        names.add(lit)                  # a name we cannot resolve = possibly deleted
                elif "${" in v or v.startswith("`") or "+" in v or ".format" in v:
                    constructed.append(f"{info.filename}: {v[:50]}")
            for m in re.finditer(r"(?:put_secret_value|create_secret)\s*\(\s*(?:SecretId|Name)\s*=\s*([^,)\s]+)", txt):
                write_calls.add(m.group(1).strip().strip("'\""))
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
        if len(set(regions_seen.values())) > 1:
            uninspectable.append((fn, f"STALE COPY IN THE DEPLOYED ZIP -- client regions disagree "
                                      f"across files: {regions_seen}. Entrypoint {entry[0] if entry else '?'} "
                                      f"wins; the others are dead code shipped to production."))
        if not names:
            continue
        lam_region = role_arn.split(":")[3] if role_arn.count(":") > 3 else "us-east-1"
        eff = region or "us-east-1"
        read_names = set()
        for nm2, ids in name_idents.items():
            if not (ids & write_calls):
                read_names.add(nm2)
        for name in sorted(names):
            arn = resolve(name, eff)
            if arn is None:
                verdict, why = "DEAD", f"NO_SECRET in {eff}"
            else:
                # ACTION ATTRIBUTION. `inf-jwt-trigger` only ever WRITES `orion/eclipse_jwt/current`
                # (put_secret_value / create_secret); its role has PutSecretValue but no read. Testing
                # GetSecretValue there reported a dead reach on a FIRM CREDENTIAL that does not exist.
                # Test the action the code actually performs on THAT name.
                idents = name_idents.get(name, set()) | {name}
                act = ("secretsmanager:PutSecretValue" if (idents & write_calls) and name not in read_names
                       else "secretsmanager:GetSecretValue")
                rc, out, _ = aws("iam", "simulate-principal-policy",
                                 "--policy-source-arn", f"arn:aws:iam::{a.account}:role/{role}",
                                 "--action-names", act,
                                 "--resource-arns", arn, "--query",
                                 "EvaluationResults[].EvalDecision", "--output", "text")
                if rc or not out:
                    verdict, why = "UNKNOWN", "no verdict (never a pass)"
                elif out != "allowed":
                    verdict, why = "DEAD", f"NO_GRANT ({out}) on {act.split(':')[1]} in {eff}"
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

    # AXIS C. This tool proves AXIS A (a dead reach) and AXIS B (the reader swallows it). It CANNOT
    # prove AXIS C -- that the swallowing path actually EXECUTES and something downstream depends on
    # its output. `opal-smartx-ingestion-pipeline` passes A and B and is NOT a degrade: the getters
    # that would break are never invoked, and the ones that are invoked handle the null config with a
    # designed hardcoded fallback (378 log events, 0 AttributeError, real output). Its author -- me --
    # hand-verified it and still bound "is a degrade" to the proxy "reads it AND cannot" instead of to
    # the property "the degraded path runs and has a dependent consumer."
    #
    # So these are CANDIDATES, never verdicts. A tool that cannot prove the property must not name it.
    print("\n=========== CANDIDATES: axis A (dead reach) x axis B (fail-silent reader) ===========")
    print("  AXIS C IS UNVERIFIED BY THIS TOOL and is required before any row is a finding:")
    print("    does the swallowing path EXECUTE, and does anything downstream DEPEND on its output?")
    print("  Ground each row against its CloudWatch log and its SERVED artifact. Do not route raw rows.\n")
    live = [r for r in rows if r["sev"] == "LIVE" and r["fail_silent"]]
    for r in live:
        print(f"  ?? CANDIDATE {r['fn']} ({r['role']}) -> {r['secret']}: {r['why']}; "
              f"ran {r['days_since_run']}d ago; the GETTER swallows the failure")
        print("       axis B: GETTER-LEVEL ONLY -- resolve the CALLER CHAIN (a caller may re-raise,")
        print("               or may swallow a getter's raise). Component fail-mode != system fail-mode.")
        print("       axis C: UNVERIFIED -- confirm the path runs and a consumer depends on it")
    if not live:
        print("  none")
    print(f"\n  dead-reach rows: {len(rows)}   axis-A x axis-B candidates: {len(live)}   "
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
