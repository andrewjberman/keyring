"""Typecheck a pinned disposable portal snapshot with existing locked dependencies."""

import hashlib
import io
import json
from pathlib import Path
import subprocess
import tarfile
import tempfile
from amgt_round8_cvo_intake import ROOT, HOME

pin = "a845a8be75"
snapshot = Path(tempfile.mkdtemp(prefix="cvo-r8-types-"))
deps = Path("C:/tmp/wk-amgt-7-2/portal")
paths = [
    "src",
    "tsconfig.json",
    "tsconfig.app.json",
    "tsconfig.node.json",
    "package.json",
    "bun.lock",
    "vite.config.ts",
]
archive = subprocess.check_output(
    ["git", "-C", "portal", "archive", "--format=tar", pin, *paths], cwd=ROOT
)
with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
    for member in tar.getmembers():
        resolved = (snapshot / member.name).resolve()
        assert (
            resolved.is_relative_to(snapshot.resolve())
            and not member.issym()
            and not member.islnk()
        )
    tar.extractall(snapshot, filter="data")
manifests = {}
for filename in ["package.json", "bun.lock"]:
    one = (snapshot / filename).read_bytes().replace(b"\r\n", b"\n")
    two = (deps / filename).read_bytes().replace(b"\r\n", b"\n")
    manifests[filename] = {
        "equal": one == two,
        "sha256": hashlib.sha256(one).hexdigest(),
    }
assert all(v["equal"] for v in manifests.values()), (
    "Retained dependency provenance mismatch"
)
script = snapshot / "link-dependencies.ps1"
script.write_text(
    "param([string]$LinkPath,[string]$TargetPath)\nNew-Item -ItemType Junction -Path $LinkPath -Target $TargetPath -ErrorAction Stop | Out-Null\n",
    encoding="utf-8",
)
subprocess.run(
    [
        "powershell",
        "-NoProfile",
        "-File",
        str(script),
        "-LinkPath",
        str(snapshot / "node_modules"),
        "-TargetPath",
        str(deps / "node_modules"),
    ],
    check=True,
    capture_output=True,
)
tsc = deps / "node_modules/typescript/bin/tsc"


def build():
    p = subprocess.run(
        ["node", str(tsc), "-b", "--force", "--listFiles", "--pretty", "false"],
        cwd=snapshot,
        capture_output=True,
        encoding="utf-8",
        timeout=120,
    )
    lines = p.stdout.splitlines()
    return {
        "rc": p.returncode,
        "stdout": p.stdout,
        "stderr": p.stderr,
        "files": [
            line
            for line in lines
            if len(line) > 2 and (line[1:3] == ":/" or line.startswith("/"))
        ],
        "diagnostics": [line for line in lines if "error TS" in line],
    }


baseline = build()
target = snapshot / "src/pages/SecurityAnalysis/components/RankedChart.tsx"
before = target.read_bytes()
try:
    target.write_bytes(
        before + b'\nexport const CVO_R8_TYPE_MUTANT: number = "must-fail";\n'
    )
    mutant = build()
finally:
    target.write_bytes(before)
out = {
    "pin": pin,
    "snapshot": str(snapshot),
    "dependency_root": str(deps / "node_modules"),
    "manifest_match": manifests,
    "baseline": baseline,
    "mutant": mutant,
    "restored_byte_identical": target.read_bytes() == before,
    "target_sha256": hashlib.sha256(before).hexdigest(),
    "limits": "Disposable pinned source archive, retained matching package/lock dependencies via junction. No registry egress, install, shared file mutation or promotion. Compiler build caches written only inside disposable snapshot. Does not claim worker ran a compiler or a live browser test.",
}
(HOME / "AMGT_RESAPP_ROUND8_CVO_TYPES_20260913_Z.json").write_text(
    json.dumps(out, indent=2) + "\n", encoding="utf-8"
)
print(
    json.dumps(
        {
            "baseline_rc": baseline["rc"],
            "baseline_files": len(baseline["files"]),
            "baseline_diagnostics": baseline["diagnostics"],
            "mutant_rc": mutant["rc"],
            "mutant_target_errors": [
                s for s in mutant["diagnostics"] if "RankedChart" in s
            ],
            "restored": out["restored_byte_identical"],
            "snapshot": str(snapshot),
        }
    )
)
