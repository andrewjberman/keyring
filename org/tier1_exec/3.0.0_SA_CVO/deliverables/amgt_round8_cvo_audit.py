"""Offline adapter/matcher evidence and bounded existing-remedy source checks."""

import ast
import collections
import contextlib
import datetime
import hashlib
import io
import json
import socket
import subprocess
import sys
from unittest.mock import patch
from amgt_round8_cvo_intake import ROOT, HOME, PROJECT, run, records

sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True


def main():
    intake = json.loads(
        (HOME / "AMGT_RESAPP_ROUND8_CVO_INTAKE_20260913_Z.json").read_text()
    )
    pin = intake["pin"]
    sources = [
        "lib/research/api/scoped_amgt.py",
        "lib/research/checkface/scopes.py",
        "lib/research/checkface/run_checks.py",
    ]
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in sources}
    for p in sources:
        assert (ROOT / p).read_bytes().replace(
            b"\r\n", b"\n"
        ) == subprocess.check_output(["git", "show", pin + ":" + p], cwd=ROOT).replace(
            b"\r\n", b"\n"
        )
    out = {
        "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "pin": pin,
        "source_sha256": hashes,
    }
    with (
        patch.object(socket.socket, "connect", side_effect=RuntimeError("CVO OFFLINE")),
        patch.object(
            socket.socket, "connect_ex", side_effect=RuntimeError("CVO OFFLINE")
        ),
        patch.object(
            socket, "create_connection", side_effect=RuntimeError("CVO OFFLINE")
        ),
    ):
        from lib.research.api import scoped_amgt as api

        model = api.read_model_block("BABA_US_Equity")

        def measure(fn):
            return {
                s: len(fn(model, s) or [])
                for s in ["fiscal_year_line_item", "not_a_real_scope_NOPE_xyz"]
            }

        original = api._figures
        out["matcher_before"] = measure(original)
        with patch.object(api, "_figures", lambda m, s: m.get("figures", [])):
            out["matcher_loosened"] = measure(api._figures)
            out["bound_original_during_patch"] = measure(original)
        out["matcher_restored"] = measure(api._figures)
        out["matcher_same_object_restored"] = api._figures is original
        out["matcher_denominator"] = len(model["figures"])
        import pytest

        log = io.StringIO()
        with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
            rc = pytest.main(["lib/research/api/tests", "-q", "-p", "no:cacheprovider"])
        out["tests"] = {"rc": int(rc), "stdout": log.getvalue()}

        class Resource:
            def __init__(self, mode):
                self.mode, self.calls = mode, []

            def batch_get_item(self, RequestItems):
                table, spec = next(iter(RequestItems.items()))
                keys = spec["Keys"]
                self.calls.append(keys)
                pending = keys if self.mode == "exhaust" else []
                # Keep the second requested key unresolved across every retry.
                if self.mode == "partial":
                    if not hasattr(self, "unresolved"):
                        self.unresolved = dict(keys[-1])
                    pending = [k for k in keys if k == self.unresolved]
                done = (
                    []
                    if self.mode == "absent"
                    else [k for k in keys if k not in pending]
                )
                return {
                    "Responses": {
                        table: [
                            dict(
                                k, rank=i + 1, rank_sort="%05d" % (i + 1), score=20 + i
                            )
                            for i, k in enumerate(done)
                        ]
                    },
                    "UnprocessedKeys": {table: {"Keys": pending}},
                }

        data = {
            "thesis": {
                key: api.read_thesis_bundle(key)
                for key in ["BABA_US_Equity", "BABACVOCTRL_US_Equity"]
            },
            "chart": {},
        }
        out["batch_calls"] = {}
        for mode in ["processed", "absent", "partial", "exhaust"]:
            resource = Resource(mode)
            with patch.object(api, "_dynamodb", return_value=resource):
                data["chart"][mode] = api.read_rank_series(
                    "trending",
                    "chatter",
                    ["AAA US", "BBB US"],
                    as_of_date="2026-09-12",
                    days=1,
                )
            out["batch_calls"][mode] = resource.calls
        out["input"] = data
    out["sources_unchanged"] = {
        p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h
        for p, h in hashes.items()
    }
    out["to_check"] = {
        p: run([sys.executable, ".tools/to-check.py", "--project", p, "--json"])
        for p in ["AMGT_RESAPP", "POSN_ASTTAX"]
    }
    out["directive_d5"] = run(
        [sys.executable, ".tools/directives-check.py", "--code", "D5", "--json"]
    )
    channel = [
        (p, records((ROOT / p).read_text(encoding="utf-8")))
        for p in intake["channel_sha256"]
    ]
    out["channel_census"] = {
        "files": len(channel),
        "rows": sum(len(rr) for p, rr in channel),
        "distinct_ids": len({r["id"] for p, rr in channel for r in rr}),
        "json_block_shapes": dict(
            collections.Counter(
                type(json.loads(b)).__name__
                for p, _ in channel
                for b in __import__("re").findall(
                    r"```json\s*(.*?)```",
                    (ROOT / p).read_text(encoding="utf-8"),
                    __import__("re").S,
                )
            )
        ),
        "unparseable": 0,
    }
    out["owner_disarm_s58"] = [
        r for p, rr in channel for r in rr if r["id"] == "AMGT_RESAPP-Z-S58"
    ]
    out["old_remedies"] = {
        r["id"]: dict(r, source=p)
        for p, rr in channel
        if "/remediations/" in p
        for r in rr
        if r["id"]
        in {
            "AMGT_RESAPP-Z-" + n
            for n in [
                "C-S98",
                "C-S99",
                "W11-S5",
                "W12-S1",
                "S34",
                "S36",
                "S42",
                "S22",
                "C-S33",
                "C-S49",
            ]
        }
    }
    out["map_frozen_checks"] = {}
    for seat, filename in [
        (1, "build_field_map.py"),
        (1, "check_join.py"),
        (1, "check_join_fye.py"),
        (1, "check_landing.py"),
        (2, "check_e2e.py"),
    ]:
        p = f"{PROJECT}/deliverables/0.9.0_WK_AMGT_RESAPP~{seat}/{filename}"
        text = (ROOT / p).read_text(encoding="utf-8")
        tree = ast.parse(text)
        out["map_frozen_checks"][p] = {
            "sha256": hashlib.sha256((ROOT / p).read_bytes()).hexdigest(),
            "old_bucket": "opal-data-research" in text,
            "environ_nodes": len(
                [
                    n
                    for n in ast.walk(tree)
                    if isinstance(n, ast.Attribute) and n.attr == "environ"
                ]
            ),
        }
    map_path = "org/tier1_exec/4.0.0_SA_CRO/deliverables/HARVEST_CONSUMER_CHECK_MAP_20260913_Z.md"
    out["map_sha256"] = hashlib.sha256((ROOT / map_path).read_bytes()).hexdigest()
    out["portal"] = {
        "gitlink": run(["git", "rev-parse", "HEAD:portal"]),
        "local_refs": run(
            ["git", "-C", "portal", "branch", "--contains", "a845a8be75"]
        ),
        "remote_tracking_refs": run(
            ["git", "-C", "portal", "branch", "-r", "--contains", "a845a8be75"]
        ),
        "recorded_pointer_control": run(
            ["git", "-C", "portal", "branch", "-r", "--contains", "e85f6eb84f"]
        ),
        "remote_heads": run(["git", "-C", "portal", "ls-remote", "--heads", "origin"]),
    }
    out["limits"] = (
        "No shared-source mutation, external data, deployed checks or publication. Offline real adapter with stubbed DynamoDB response boundary. In-process matcher mutant is independently rerun; worker source-mutation evidence remains attributed. Map validation is bounded to five frozen checks, not an estate-wide zero-coverage assertion. Portal remote listing is read-only; tracking-ref ancestry alone is not fresh remote reachability."
    )
    (HOME / "AMGT_RESAPP_ROUND8_CVO_EVIDENCE_20260913_Z.json").write_text(
        json.dumps(out, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "matcher": [
                    out["matcher_before"],
                    out["matcher_loosened"],
                    out["matcher_restored"],
                ],
                "tests": out["tests"],
                "channel": out["channel_census"],
                "chart": {k: v["read_completeness"] for k, v in data["chart"].items()},
            }
        )
    )
    assert (
        rc == 0
        and all(out["sources_unchanged"].values())
        and out["matcher_loosened"]["not_a_real_scope_NOPE_xyz"] == 196
    )


if __name__ == "__main__":
    main()
