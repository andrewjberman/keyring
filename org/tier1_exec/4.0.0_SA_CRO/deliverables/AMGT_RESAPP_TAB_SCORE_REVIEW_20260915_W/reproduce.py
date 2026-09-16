"""Offline counterexamples against the reviewed functions; no vendor requests.

Extract only named function ASTs, avoiding each instrument's top-level DAPI/S3
calls. Synthetic inputs demonstrate implementation behavior, not data coverage.
Run from the repository root. Prints JSON with source hashes for reproducibility.
"""

import ast
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
INSTRUMENTS = (
    ROOT
    / "org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_SUBSTRATE_MEASUREMENTS_20260915_W/instruments"
)
sources = {}


def functions(path, names, namespace):
    source = path.read_bytes()
    sources[str(path.relative_to(ROOT))] = hashlib.sha256(source).hexdigest()
    tree = ast.parse(source)
    selected = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name in names
    ]
    assert {node.name for node in selected} == set(names)
    future = ast.ImportFrom(
        module="__future__", names=[ast.alias(name="annotations")], level=0
    )
    module = ast.fix_missing_locations(
        ast.Module(body=[future, *selected], type_ignores=[])
    )
    exec(compile(module, str(path), "exec"), namespace)


ns = {}
functions(INSTRUMENTS / "robustness_coverage.py", ["last_n_complete"], ns)
ns["hist"] = {
    "SYNTHETIC": [
        {
            "date": f"202{i // 4 + 1}-{(i % 4 + 1) * 3:02d}-28",
            **({"X": 1} if i % 2 == 0 else {}),
        }
        for i in range(16)
    ]
}
count = ns["last_n_complete"]("SYNTHETIC", ["X"], 8)
assert count == 8 and "X" not in ns["hist"]["SYNTHETIC"][-1]


class FakeClient:
    def _execute(self, operation, route, body, scenario):
        return body


ns_lusha = {"_assert_contact_reveal_enabled": lambda: None}
functions(
    ROOT / "data/find/imo/scripts/_util/lusha_client.py", ["contacts_enrich"], ns_lusha
)
payload = ns_lusha["contacts_enrich"](FakeClient(), ["SYNTHETIC"], reveal=[])
assert payload == {"ids": ["SYNTHETIC"]}

ns_peers = {}
functions(INSTRUMENTS / "peers_v_feasibility_grain.py", ["inv", "measures"], ns_peers)
div_only = ns_peers["measures"]({"TRAIL_12M_DVD_PAID": -10, "CRNCY_ADJ_MKT_CAP": 1000})
negative_ebitda = ns_peers["measures"](
    {"TRAIL_12M_EBITDA": -5, "BEST_CUR_EV_TO_EBITDA": 10}
)
assert div_only[3] == 0.01
assert negative_ebitda[4] == 0.1

print(
    json.dumps(
        {
            "mode": "offline_synthetic_counterexamples",
            "vendor_calls": 0,
            "robustness": {
                "complete_observations_anywhere": count,
                "latest_missing": True,
                "consecutive": False,
                "passes_existing_count_gate": count >= 8,
            },
            "lusha_empty_reveal_payload": payload,
            "peers_missing_buybacks_still_yields_measure_3": div_only[3],
            "peers_negative_trailing_ebitda_positive_forward_multiple_yields_measure_4": negative_ebitda[
                4
            ],
            "source_sha256": sources,
        },
        indent=2,
    )
)
