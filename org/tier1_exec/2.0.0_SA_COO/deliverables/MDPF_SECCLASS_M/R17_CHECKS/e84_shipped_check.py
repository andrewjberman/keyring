"""SC-e-84 deploy check: the three served COT gold objects equal the repo bytes, and none is its pre-act rollback object.

Read-only. Prints one line:
  E84-SHIPPED ok=<bool> moved=<n of 3> files=[<name>:<repo md5>/<served etag>] control=<MATCH|MISMATCH>
ok is True when every served ETag equals its repo md5 AND differs from its pre-act ETag.
control is the discrimination check: every repo md5 must differ from its pre-act ETag (else the check cannot tell a ship from none).
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
BUCKET = "opal-data-cot"
# repo path under data/cot/scripts/gold/ -> pre-act ETag (head-object 2026-10-09, NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_NAME_PORT_20261009.md)
FILES = {
    "lib/etf_classifier.py": "2fef39d1373a20f40e2a0fb4c0cae0fa",
    "C_06.client_mix_timeseries.py": "ea7e6700509611a1866701f4f8e0984e",
    "D_03.composition_artifacts.py": "6f48eaf3b54c63519c379d26793cc5e0",
}


def main() -> int:
    aws = str(ROOT / ".tools" / ("aws.cmd" if sys.platform == "win32" else "aws"))
    rows, moved, control_ok, ok = [], 0, True, True
    for rel, pre in FILES.items():
        repo = hashlib.md5((ROOT / "data/cot/scripts/gold" / rel).read_bytes()).hexdigest()
        out = subprocess.run([aws, "s3api", "head-object", "--bucket", BUCKET, "--key", f"code/gold/{rel}", "--output", "json"],
                             capture_output=True, text=True)
        if out.returncode != 0:
            print(f"E84-SHIPPED ok=False error=head-object {rel} rc={out.returncode} {out.stderr.strip()[:160]}")
            return 1
        served = json.loads(out.stdout)["ETag"].strip('"')
        control_ok &= repo != pre
        hit = served == repo and served != pre
        moved += int(hit)
        ok &= hit
        rows.append(f"{rel}:{repo[:8]}/{served[:8]}")
    ok &= control_ok
    print(f"E84-SHIPPED ok={ok} moved={moved} of 3 files={rows} control={'MATCH' if control_ok else 'MISMATCH'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
