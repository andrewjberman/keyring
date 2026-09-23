#!/usr/bin/env python3
"""Offline-default resolver harness. Endpoint mode is explicit, never a vendor login.

Default: synthetic 50-symbol matrix, clearly labelled; not a live coverage claim.
--capture-root replays the separately authorized, pinned five-symbol CRO capture.
--endpoint uses only existing api/scoped routes with a token from --token-env.
No token, provider credential, portfolio amount or full server response is printed.
"""
import argparse
import json
import os
from pathlib import Path
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "infra/aws/lambda/investor-reporting/intake"))
from security_resolution import SecurityResolver, validate_symbols  # noqa: E402


def offline(symbols, capture_root=None):
    if capture_root:
        capture = json.loads((Path(capture_root) / "02_securities_info.json").read_text(encoding="utf-8"))
        symbols = ["AAPL", "ALPPL", "VNQ", "BREIT", "$:CASH"]
        rows = capture["json"]
        pin = "d7d044ba7a"
        status = capture["http_status"]
        scope = "CRO_PINNED_OFFLINE_CAPTURE"
    else:
        rows = [{"id": symbol, "security_id": symbol, "securitylist_security_id": f"fixture-{i}",
                 "security_name": "Synthetic fixture", "detailed_security_type": "etf",
                 "features_needed": ["fixture-gated"] if i % 5 == 0 else []}
                for i, symbol in enumerate(symbols) if i % 3 != 0]
        pin, status, scope = "SYNTHETIC_NOT_LIVE", 200, "SYNTHETIC_OFFLINE_MATRIX"
    def provider(requested):
        return {"http_status": status, "complete": True, "final_url_path": "/securities/securities_info",
                "account_id": "offline", "source_revision": pin, "requested": requested,
                "observed_at": "offline-replay", "json": rows}
    resolver = SecurityResolver(provider_check=provider, identity=lambda *args: {
        "state": "UNAVAILABLE", "reason_code": "OFFLINE_REFERENCE_NOT_INSTALLED"},
        cache=None, clock=time.time, account_id="offline", source_revision=pin)
    return resolver.check(symbols), scope, pin


def endpoint(args, symbols):
    if not args.authorized_endpoint:
        raise ValueError("endpoint mode requires --authorized-endpoint; no provider probe is implicit")
    base = args.endpoint.rstrip("/")
    url = urllib.parse.urlsplit(base)
    if (url.scheme != "https" or not url.hostname or url.username or url.password
            or url.query or url.fragment or url.path != "/api/scoped/investor-reporting"):
        raise ValueError("endpoint must be the HTTPS api/scoped/investor-reporting base")
    token = os.environ.get(args.token_env)
    if not token:
        raise ValueError("token environment variable is absent")
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *args, **kwargs):
            return None
    opener = urllib.request.build_opener(NoRedirect())
    def request(path, payload=None):
        req = urllib.request.Request(base + path, data=json.dumps(payload).encode() if payload is not None else None,
            headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"},
            method="POST" if payload is not None else "GET")
        with opener.open(req, timeout=25) as response:
            data = response.read(1024 * 1024 + 1)
            if len(data) > 1024 * 1024:
                raise ValueError("response exceeds harness bound")
            return json.loads(data)
    result = request("/securities/check", {"symbols": symbols})
    if args.advisory:
        if not args.request_token or len(symbols) != 1:
            raise ValueError("advisory requires one symbol and a stable --request-token")
        started = request("/securities/" + args.advisory,
                          {"request_token": args.request_token, "symbol": symbols[0]})
        identifier = started.get("resolution_id")
        if not isinstance(identifier, str) or not identifier or not all(c.isalnum() or c in "_-" for c in identifier):
            raise ValueError("invalid resolution identifier")
        # Bounded poll; no automatic second model request or fallback provider.
        for _ in range(12):
            poll = request("/securities/resolutions/" + identifier)
            if poll.get("state") not in ("QUEUED", "RUNNING"):
                result["advisory_state"] = poll.get("state", "UNKNOWN")
                break
            time.sleep(5)
        else:
            result["advisory_state"] = "PENDING_AFTER_POLL_BOUND"
    return result, "AUTHORIZED_SCOPED_ENDPOINT", args.source_pin


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--symbols", help="comma-separated identifiers (default: 50 synthetic identifiers)")
    parser.add_argument("--capture-root")
    parser.add_argument("--endpoint")
    parser.add_argument("--authorized-endpoint", action="store_true")
    parser.add_argument("--token-env", default="IRPT_SCOPED_BEARER")
    parser.add_argument("--source-pin", default="UNSPECIFIED")
    parser.add_argument("--advisory", choices=["suggest", "substitute"])
    parser.add_argument("--request-token")
    args = parser.parse_args()
    if args.endpoint and not args.symbols:
        parser.error("endpoint mode requires explicit --symbols; synthetic fixtures are never sent")
    if args.endpoint and args.capture_root:
        parser.error("capture replay and endpoint mode are mutually exclusive")
    started = time.monotonic()
    try:
        symbols = validate_symbols(args.symbols.split(",") if args.symbols else [f"FIXTURE{i:02}" for i in range(50)])
        result, mode, pin = endpoint(args, symbols) if args.endpoint else offline(symbols, args.capture_root)
        rows = result.get("results")
        if not isinstance(rows, list):
            raise ValueError("response does not expose results[]")
        output = {"mode": mode, "source_pin": pin, "requested_count": result.get("requested_count"),
                  "distinct_count": result.get("distinct_count"), "cache_count": result.get("cache_count"),
                  "outcomes": [{"symbol": r.get("symbol"), "state": r.get("state"),
                                "reason": r.get("reason")} for r in rows],
                  "unresolved_count": sum(r.get("state") != "FOUND" for r in rows),
                  "latency_seconds": round(time.monotonic() - started, 4)}
        if "advisory_state" in result:
            output["advisory_state"] = result["advisory_state"]
        print(json.dumps(output, indent=2))
        return 0
    except urllib.error.HTTPError as exc:
        print(json.dumps({"failure": "ENDPOINT_HTTP_ERROR", "http_status": exc.code}))
    except Exception as exc:
        # Exception text may contain URLs/tokens; disclose type only.
        print(json.dumps({"failure": "HARNESS_FAILED", "error_type": type(exc).__name__}))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
