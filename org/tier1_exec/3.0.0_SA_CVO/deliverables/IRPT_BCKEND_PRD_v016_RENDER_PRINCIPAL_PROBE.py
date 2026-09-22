"""Offline reproduction of the v0.16 renderer-principal contract gap."""
import importlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PIN = "54a2c0564cef8c2a155aa297518391113383b519"
PATHS = [
    "infra/aws/lambda/investor-reporting/_scope/resolve.py",
    "infra/aws/lambda/investor-reporting/_authz/enforce.py",
]
for rel in PATHS:
    assert subprocess.run(
        ["git", "diff", "--exit-code", PIN, "--", rel], cwd=ROOT,
        capture_output=True, check=False,
    ).returncode == 0, "historical probe: reviewed code has moved: " + rel

sys.path.insert(0, str(ROOT / "infra/aws/lambda/investor-reporting/_authz"))
enforce = importlib.import_module("enforce")

headers = {"x-origin-verify": "cloudfront", "x-firm-id": "49financial",
           "x-user-role": "renderer", "x-user-tier": "render"}
classifier = enforce._scope.classify_principal
exact = classifier(headers)
with_subject = classifier(dict(headers, **{"x-user-email": "render-fixture"}))
control = classifier(dict(headers, **{"x-user-email": "render-fixture",
                                      "x-advisor-id": "fixture-advisor"}))
assert exact[0] == with_subject[0] == "UNKNOWN"
assert control[0] == "FIRM_ADVISOR"
binding = enforce.FirmBinding("49financial", "fir_fixture")
guard = enforce.Enforcer(
    binding,
    lambda _: {"firm_id_opaque": "fir_fixture", "entries": []},
    lambda _: {}, lambda _: ({}, "fixture-1"),
)
scope, refusal = guard.resolve_now(enforce.Request(headers, "performance"))
assert scope is None and refusal.code == "NO_PRINCIPAL"
print(json.dumps({"pin": PIN, "exact": exact, "with_subject": with_subject,
                  "advisor_control": control, "enforcer": refusal.as_envelope(),
                  "result": "4 assertions passed; v0.16 contract gap reproduced"}, indent=2))
