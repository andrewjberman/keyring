"""Independent offline round-7 evidence; no source mutation, deploy or vendor access."""

import collections
import contextlib
import datetime
import hashlib
import io
import json
from pathlib import Path
import socket
import subprocess
import sys
from unittest.mock import patch
from amgt_round7_cvo_intake import ROOT, HOME, run

sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True


def main():
    intake = json.loads(
        (HOME / "AMGT_RESAPP_ROUND7_CVO_INTAKE_20260912_Z.json").read_text()
    )
    pin = intake["pin"]
    sources = set()
    for p in intake["round_proofs"].values():
        sources.update(
            a["path_or_key"]
            for a in p["artifacts_produced"]
            if (ROOT / a["path_or_key"]).is_file()
        )
    sources.update(
        str(p.relative_to(ROOT)).replace("\\", "/")
        for scope in [
            "lib/research/api/tests",
            "lib/research/metrics/tests",
            "lib/research/rules/tests",
        ]
        for p in (ROOT / scope).glob("*.py")
    )
    sources.update(
        [
            "lib/research/provenance/render_print.py",
            "lib/research/checkface/run_checks.py",
            "lib/research/watchlist/store.py",
        ]
    )
    evidence = {
        "utc": datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "pin": pin,
        "source_sha256": {},
        "source_matches_pin": {},
        "limits": "No shared-source mutation; no AWS, vendor, deployment, portal checkout or publication. All tests and calls use a socket guard. Recorded worker mutants are attributed, not re-run.",
    }
    for p in sorted(sources):
        data = (ROOT / p).read_bytes()
        committed = subprocess.check_output(["git", "show", pin + ":" + p], cwd=ROOT)
        evidence["source_sha256"][p] = hashlib.sha256(data).hexdigest()
        evidence["source_matches_pin"][p] = data.replace(
            b"\r\n", b"\n"
        ) == committed.replace(b"\r\n", b"\n")
    assert all(evidence["source_matches_pin"].values()), (
        "Source drift: do not grade mismatched bytes"
    )
    with (
        patch.object(socket.socket, "connect", side_effect=RuntimeError("CVO OFFLINE")),
        patch.object(
            socket.socket, "connect_ex", side_effect=RuntimeError("CVO OFFLINE")
        ),
        patch.object(
            socket, "create_connection", side_effect=RuntimeError("CVO OFFLINE")
        ),
    ):
        import pytest

        log = io.StringIO()
        with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
            rc = pytest.main(
                [
                    "lib/research/api/tests",
                    "lib/research/rules/tests",
                    "lib/research/metrics/tests",
                    "-q",
                    "-p",
                    "no:cacheprovider",
                ]
            )
        evidence["tests"] = {"rc": int(rc), "output": log.getvalue()}
        print(json.dumps({"tests": evidence["tests"]}), flush=True)
        from lib.research.api import scoped_amgt as api

        evidence["cross"] = [
            api.resolve_axis(m, s) for m in api.MOVEMENTS for s in api.SUBJECTS
        ]
        evidence["invalid_domains"] = []
        for m, s in [("sideways", "chatter"), ("trending", "volume")]:
            try:
                value = api.resolve_axis(m, s)
                evidence["invalid_domains"].append(
                    {"pair": [m, s], "unexpected": value}
                )
            except api.AdapterError as error:
                evidence["invalid_domains"].append(
                    {"pair": [m, s], "refused": error.status, "reason": str(error)}
                )
        evidence["thesis"] = {}
        for key in ["BABA_US_Equity", "BABACVOCTRL_US_Equity", "BABA US Equity"]:
            bundle = api.read_thesis_bundle(key)
            evidence["thesis"][key] = {
                "header": len(bundle["header_figures"]),
                "fiscal": len(bundle["fiscal_year_figures"]),
                "checks": len(bundle["check_face"]),
                "prices": [
                    r
                    for r in bundle["fiscal_year_figures"]
                    if r.get("mnemonic") == "PX_LAST"
                ],
                "price_checks": [
                    r
                    for r in bundle["check_face"]
                    if str(r.get("figure_id", "")).startswith(
                        "fiscal_year_line_item:PX_LAST"
                    )
                ],
            }
        rawpath = Path(api.MODEL_BLOCK_ROOT) / "model_block_BABA_US_Equity.json"
        raw = json.loads(rawpath.read_text(encoding="utf-8"))
        model = api.read_model_block("BABA_US_Equity")
        evidence["raw_artifact"] = {
            "path": str(rawpath),
            "sha256": hashlib.sha256(rawpath.read_bytes()).hexdigest(),
            "scopes": dict(collections.Counter(r.get("scope") for r in raw["figures"])),
            "raw_prices": [
                r
                for r in raw["figures"]
                if r.get("scope") == "fiscal_year_line_item"
                and r.get("mnemonic") == "PX_LAST"
            ],
        }
        evidence["scope_control"] = {
            s: len(api._figures(model, s))
            for s in [
                "header",
                "fiscal_year_line_item",
                "fiscal_year",
                "not_a_real_scope_NOPE_xyz",
            ]
        }
        # Real request routing with supplied identity, never a JWT/origin validation claim.
        event = {
            "version": "2.0",
            "rawPath": "/api/scoped/amgt/security/BABA_US_Equity/thesis",
            "headers": {"X-Firm-Id": "CVO_OFFLINE"},
            "requestContext": {"http": {"method": "GET"}},
        }
        response = api.handler(event, None)
        body = json.loads(response["body"])
        evidence["thesis_handler"] = {
            "status": response["statusCode"],
            "keys": list(body),
            "fiscal": len(body.get("fiscal_year_figures", [])),
        }

        class MixedResource:
            def __init__(self, mode):
                self.mode, self.calls = mode, []

            def batch_get_item(self, RequestItems):
                table, spec = next(iter(RequestItems.items()))
                keys = spec["Keys"]
                self.calls.append([dict(k) for k in keys])
                pending = []
                if self.mode == "exhaust":
                    pending = keys
                elif self.mode == "mixed" and len(self.calls) == 1:
                    pending = keys[1:]
                done = (
                    []
                    if self.mode == "absent"
                    else [k for k in keys if k not in pending]
                )
                rows = [
                    dict(k, rank=i + 1, rank_sort="%05d" % (i + 1), score=20 + i)
                    for i, k in enumerate(done)
                ]
                return {
                    "Responses": {table: rows},
                    "UnprocessedKeys": {table: {"Keys": pending}},
                }

        evidence["batch_controls"] = {}
        for mode in ["processed", "absent", "mixed", "exhaust"]:
            resource = MixedResource(mode)
            with patch.object(api, "_dynamodb", return_value=resource):
                result = api.read_rank_series(
                    "trending",
                    "chatter",
                    ["AAA US", "BBB US"],
                    as_of_date="2026-09-12",
                    days=1,
                )
            evidence["batch_controls"][mode] = {
                "result": result,
                "call_count": len(resource.calls),
                "requested_per_call": resource.calls,
            }
        resource = MixedResource("mixed")
        with patch.object(api, "_dynamodb", return_value=resource):
            result = api.read_rank_series(
                "trending", "chatter", ["AAA US"], as_of_date="2026-09-12", days=105
            )
        evidence["batch_105_keys"] = {
            "completeness": result["read_completeness"],
            "point_count": result["series"][0]["point_count"],
            "batch_sizes": [len(c) for c in resource.calls],
        }
    evidence["sources_unchanged_after"] = {
        p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h
        for p, h in evidence["source_sha256"].items()
    }
    evidence["portal"] = {}
    for short in ["e85f6eb84f", "c67281460a", "83cc87f2", "e6057f26", "5b959f63ca"]:
        full = run(["git", "-C", "portal", "rev-parse", short])["stdout"].strip()
        listing = run(
            [
                "git",
                "-C",
                "portal",
                "ls-tree",
                "-r",
                "--name-only",
                full,
                "--",
                "src/pages/SecurityAnalysis",
            ]
        )
        files = listing["stdout"].splitlines()
        counts, tokens = {}, {}
        for p in files:
            text = subprocess.check_output(
                ["git", "-C", "portal", "show", full + ":" + p], cwd=ROOT
            ).decode("utf-8")
            counts[p] = sum(ord(c) > 127 for c in text)
            for token in [
                "read_completeness",
                "unresolved_point_count",
                "requested_axis",
                "served_axis",
                "corrected_overlay_status",
            ]:
                if token in text:
                    tokens.setdefault(token, []).append(p)
        evidence["portal"][short] = {
            "full": full,
            "files": len(files),
            "nonascii": sum(counts.values()),
            "affected": {p: c for p, c in counts.items() if c},
            "tokens": tokens,
            "local_refs": run(["git", "-C", "portal", "branch", "--contains", full]),
            "remote_tracking_refs": run(
                ["git", "-C", "portal", "branch", "-r", "--contains", full]
            ),
        }
    evidence["portal_hygiene_diff"] = run(
        [
            "git",
            "-C",
            "portal",
            "diff",
            "c67281460a",
            "83cc87f2",
            "--",
            "src/pages/SecurityAnalysis",
        ]
    )
    evidence["portal_negative_object"] = run(
        [
            "git",
            "-C",
            "portal",
            "cat-file",
            "-t",
            "0000000000000000000000000000000000000000",
        ]
    )
    evidence["portal_pointer"] = run(["git", "ls-tree", pin, "portal"])
    target = HOME / "AMGT_RESAPP_ROUND7_CVO_EVIDENCE_20260912_Z.json"
    target.write_text(
        json.dumps(evidence, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "path": str(target),
                "source_count": len(sources),
                "tests_rc": evidence["tests"]["rc"],
                "scope_control": evidence["scope_control"],
                "batch_105": evidence["batch_105_keys"],
                "portal": {
                    k: {f: v[f] for f in ["files", "nonascii", "tokens"]}
                    for k, v in evidence["portal"].items()
                },
            }
        )
    )
    assert rc == 0 and all(evidence["sources_unchanged_after"].values())


if __name__ == "__main__":
    main()
