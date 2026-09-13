"""Feed real local adapter bundles into pinned portal consumer functions."""

import json
import socket
import subprocess
import sys
from unittest.mock import patch
from amgt_round7_cvo_intake import ROOT, HOME

sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True
with (
    patch.object(socket.socket, "connect", side_effect=RuntimeError("CVO OFFLINE")),
    patch.object(socket.socket, "connect_ex", side_effect=RuntimeError("CVO OFFLINE")),
    patch.object(socket, "create_connection", side_effect=RuntimeError("CVO OFFLINE")),
):
    from lib.research.api import scoped_amgt as api

    thesis = {
        key: api.read_thesis_bundle(key)
        for key in ["BABA_US_Equity", "BABACVOCTRL_US_Equity"]
    }
evidence = json.loads(
    (HOME / "AMGT_RESAPP_ROUND7_CVO_EVIDENCE_20260912_Z.json").read_text()
)
data = {
    "thesis": thesis,
    "chart": {k: v["result"] for k, v in evidence["batch_controls"].items()},
}
p = subprocess.run(
    ["node", str(HOME / "amgt_round7_cvo_portal.cjs")],
    cwd=ROOT,
    input=json.dumps(data),
    capture_output=True,
    text=True,
    encoding="utf-8",
    timeout=120,
)
assert p.returncode == 0, p.stderr
result = json.loads(p.stdout)
result["input"] = data
(HOME / "AMGT_RESAPP_ROUND7_CVO_PORTAL_20260912_Z.json").write_text(
    json.dumps(result, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
)
print(json.dumps({k: v for k, v in result.items() if k not in ["input", "chart"]}))
